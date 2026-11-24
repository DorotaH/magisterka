#!/usr/bin/env python3
"""Include APPS solutions below five SLOC in the ACW and SEW arms."""

from __future__ import annotations

import ast
import csv
import json
import subprocess
import time
from pathlib import Path
from typing import Any

from run_apps500_acw import OUT, RUFF, execute_batches, parse_status, read_csv, read_jsonl, sha, write_csv, write_jsonl
from sew import EXPERIMENT_KEY, detect, embed

TIMEOUT = 120


def sew_attempt(entry: dict[str, Any], source_code: str, output_path: Path) -> dict[str, Any]:
    started = time.monotonic()
    try:
        embedded = embed(source_code, "python", EXPERIMENT_KEY)
        code = embedded.get("code")
        if isinstance(code, bytes):
            code = code.decode("utf-8", "replace")
        if not isinstance(code, str):
            raise RuntimeError(f"SEW returned no code (status={embedded.get('status')})")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(code, encoding="utf-8", newline="")
        try:
            parsed = ast.parse(code)
            compile(parsed, "<sample>", "exec")
            parses, parse_error = True, ""
        except (SyntaxError, ValueError, TypeError) as error:
            parses, parse_error = False, str(error)
        try:
            detection = detect(code, "python", EXPERIMENT_KEY)
            detection_status = "ok"
        except Exception as error:
            detection = {}
            detection_status = "error"
            detection_error = f"{type(error).__name__}: {error}"
        else:
            detection_error = ""
        applied = embedded.get("status") == "ok"
        positive = detection.get("verdict") == "Watermark detected"
        embed_status = embedded.get("status", "")
        if embed_status == "abstain:not_converged":
            error_type = "not_converged"
        elif embed_status == "abstain:parse":
            error_type = "input_unparsable"
        elif embed_status != "ok":
            error_type = str(embed_status or "embedding_error")
        elif not parses:
            error_type = "post_embedding_syntax_error"
        else:
            error_type = ""
        return {
            "code": code, "applied": applied, "parses": parses, "parse_error": parse_error,
            "changed": code != source_code, "detection_status": detection_status,
            "detection_verdict": detection.get("verdict", ""), "detection_positive": positive,
            "marking_passed": bool(applied and parses and positive), "embed_status": embed_status,
            "error_type": error_type, "error": parse_error or detection_error,
            "tool_seconds": time.monotonic() - started, "n_sites": embedded.get("n_sites", ""),
            "n_grades": embedded.get("n_grades", ""), "n_edits": embedded.get("n_edits", ""),
            "iterations": embedded.get("iterations", ""),
        }
    except Exception as error:
        return {"code": source_code, "applied": False, "parses": "", "parse_error": "",
                "changed": False, "detection_status": "error", "detection_verdict": "",
                "detection_positive": "", "marking_passed": False, "embed_status": "error",
                "error_type": "timeout" if isinstance(error, TimeoutError) else type(error).__name__,
                "error": str(error), "tool_seconds": time.monotonic() - started}


def main() -> None:
    sloc_rows = read_csv(OUT / "00_sloc.csv")
    low_rows = [row for row in sloc_rows if int(row["sloc"] or 0) < 5]
    main_entries: list[dict[str, Any]] = []
    fmt_entries: list[dict[str, Any]] = []
    fmt_results: dict[str, dict[str, Any]] = {}

    for row in low_rows:
        sid = f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}"
        original = OUT / "code" / row["dataset"] / row["problem_id"] / row["sample_index"] / "original.py"
        if not original.is_file():
            continue
        code = original.read_text(encoding="utf-8")
        common = {"sample_id": sid, "dataset": row["dataset"], "problem_id": row["problem_id"],
                  "sample_index": row["sample_index"], "sloc": int(row["sloc"]),
                  "source_code": code, "source_path": str(original.relative_to(OUT))}
        main_entries.append({**common, "arm": "main"})

        fmt_dir = original.parent / "fmt_first"
        fmt_dir.mkdir(parents=True, exist_ok=True)
        formatted_path = fmt_dir / "original_formatted.py"
        argv = [str(RUFF), "format", "--isolated", "--no-cache", str(formatted_path)]
        started = time.monotonic()
        formatted_path.write_text(code, encoding="utf-8", newline="")
        try:
            result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=TIMEOUT)
            formatted_code = formatted_path.read_text(encoding="utf-8")
            fmt_ok = result.returncode == 0
            error = result.stderr.strip()
            parses, parse_error = parse_status(formatted_code)
            fmt_results[sid] = {"ok": fmt_ok, "code": formatted_code, "path": formatted_path,
                                "error": error or parse_error,
                                "tool_seconds": time.monotonic() - started,
                                "command": json.dumps(argv), "parses": parses}
            if fmt_ok:
                fmt_entries.append({**common, "arm": "fmt_first", "source_code": formatted_code,
                                    "source_path": str(formatted_path.relative_to(OUT))})
        except Exception as error:
            fmt_results[sid] = {"ok": False, "code": code, "path": formatted_path,
                                "error": str(error), "tool_seconds": time.monotonic() - started,
                                "command": json.dumps(argv), "parses": False}

    initial: dict[tuple[str, str], dict[str, Any]] = {}
    operations: list[dict[str, Any]] = []
    for arm, entries in (("main", main_entries), ("fmt_first", fmt_entries)):
        transformed, ops = execute_batches(entries, f"small_mark_{arm}")
        operations.extend(ops)
        for item in transformed:
            code_notab = item["output_code"]
            code_full = "".join("\t" * ((len(line) - len(line.lstrip(" "))) // 4) + line.lstrip(" ")
                                for line in code_notab.splitlines(keepends=True))
            initial[(item["sample_id"], arm)] = {**item, "code_notab": code_notab, "code_full": code_full}

    detector_inputs: list[dict[str, Any]] = []
    for arm, entries in (("main", main_entries), ("fmt_first", fmt_entries)):
        for item in entries:
            result = initial[(item["sample_id"], arm)]
            for variant, code in (("acw_notab", result["code_notab"]), ("acw_full", result["code_full"])):
                detector_inputs.append({**item, "variant": variant, "source_code": code})
    detected, ops = execute_batches(detector_inputs, "small_detect")
    operations.extend(ops)
    acw_detect: dict[tuple[str, str, str], dict[str, Any]] = {}
    for item in detected:
        positive = item["source_code"] == item["output_code"]
        parses, parse_error = parse_status(item["output_code"])
        acw_detect[(item["sample_id"], item["arm"], item["variant"])] = {
            "applied": item["applied"], "status": "ok" if item["applied"] else "error",
            "positive": positive if item["applied"] else "", "verdict": "Watermark detected" if positive else "No watermark evidence",
            "error_type": item["error_type"], "error": item["error"],
            "parses": parses, "parse_error": parse_error,
        }

    marking_rows = read_csv(OUT / "01_marking.csv")
    fmt_rows = read_csv(OUT / "01_fmt_first.csv")
    artifacts = read_jsonl(OUT / "artifacts_stage1.jsonl")
    artifact_keys = {(r["sample_id"], r["stage"], r["variant"]) for r in artifacts}
    fmt_fields = list(fmt_rows[0].keys())

    for item in main_entries:
        sid = item["sample_id"]
        result = initial[(sid, "main")]
        for variant, code in (("acw_notab", result["code_notab"]), ("acw_full", result["code_full"])):
            target = OUT / "code" / item["dataset"] / str(item["problem_id"]) / str(item["sample_index"]) / f"{variant}.py"
            target.write_text(code, encoding="utf-8", newline="")
            parses, parse_error = parse_status(code)
            det = acw_detect[(sid, "main", variant)]
            marking_rows = [r for r in marking_rows if not (
                r["dataset"] == item["dataset"] and r["problem_id"] == str(item["problem_id"])
                and r["sample_index"] == str(item["sample_index"]) and r["variant"] == variant and r["arm"] == "main")]
            marking_rows.append({
                "dataset": item["dataset"], "problem_id": item["problem_id"], "sample_index": item["sample_index"],
                "arm": "main", "variant": variant, "sloc": item["sloc"], "applied": result["applied"],
                "parses": parses, "changed": code != item["source_code"], "detection_status": det["status"],
                "detection_verdict": det["verdict"], "detection_positive": det["positive"],
                "marking_passed": bool(result["applied"] and parses and det["positive"] is True),
                "error_type": result["error_type"] or ("post_marking_syntax_error" if not parses else ""),
                "error": result["error"] or parse_error or det["error"], "output_path": str(target.relative_to(OUT)),
                "tool_seconds": result.get("batch_seconds", ""), "sourcery_batch_id": result.get("batch_number", ""),
            })
            artifact = {"dataset": item["dataset"], "sample_id": sid, "problem_id": item["problem_id"],
                        "sample_index": item["sample_index"], "stage": "marked", "variant": variant,
                        "ruff_profile": "", "ruff_mode": "", "path": str(target.relative_to(OUT)),
                        "source_code_sha256": sha(item["source_code"]), "code_sha256": sha(code),
                        "changed": code != item["source_code"], "parses": parses, "parse_error": parse_error,
                        "sloc": item["sloc"], "status": "ok" if result["applied"] else "error"}
            if (sid, "marked", variant) not in artifact_keys:
                artifacts.append(artifact); artifact_keys.add((sid, "marked", variant))

        # Attempt SEW below five SLOC too; retain abstention as an explicit row.
        sew_path = OUT / "code" / item["dataset"] / str(item["problem_id"]) / str(item["sample_index"]) / "sew.py"
        sew_result = sew_attempt(item, item["source_code"], sew_path)
        marking_rows = [r for r in marking_rows if not (
            r["dataset"] == item["dataset"] and r["problem_id"] == str(item["problem_id"])
            and r["sample_index"] == str(item["sample_index"]) and r["variant"] == "sew" and r["arm"] == "main")]
        marking_rows.append({
            "dataset": item["dataset"], "problem_id": item["problem_id"], "sample_index": item["sample_index"],
            "arm": "main", "variant": "sew", "sloc": item["sloc"], "applied": sew_result["applied"],
            "parses": sew_result["parses"], "changed": sew_result["changed"],
            "detection_status": sew_result["detection_status"], "detection_verdict": sew_result["detection_verdict"],
            "detection_positive": sew_result["detection_positive"], "marking_passed": sew_result["marking_passed"],
            "error_type": sew_result["error_type"], "error": sew_result["error"],
            "output_path": str(sew_path.relative_to(OUT)), "tool_seconds": sew_result["tool_seconds"],
            "embed_status": sew_result["embed_status"], "n_sites": sew_result.get("n_sites", ""),
            "n_grades": sew_result.get("n_grades", ""), "n_edits": sew_result.get("n_edits", ""),
            "iterations": sew_result.get("iterations", ""),
        })
        if (sid, "marked", "sew") not in artifact_keys:
            artifacts.append({"dataset": item["dataset"], "sample_id": sid, "problem_id": item["problem_id"],
                              "sample_index": item["sample_index"], "stage": "marked", "variant": "sew",
                              "ruff_profile": "", "ruff_mode": "", "path": str(sew_path.relative_to(OUT)),
                              "source_code_sha256": sha(item["source_code"]), "code_sha256": sha(sew_result["code"]),
                              "changed": sew_result["changed"], "parses": sew_result["parses"],
                              "parse_error": sew_result["parse_error"], "sloc": item["sloc"],
                              "status": "ok" if sew_result["applied"] else "error"})
            artifact_keys.add((sid, "marked", "sew"))

    for item in main_entries:
        sid = item["sample_id"]
        result = initial[(sid, "main")]
        fmt = fmt_results[sid]
        original_formatted = {"dataset": item["dataset"], "problem_id": item["problem_id"],
                              "sample_index": item["sample_index"], "arm": "fmt_first",
                              "variant": "original_formatted", "applied": fmt["ok"],
                              "parses": fmt["parses"], "changed": fmt["code"] != item["source_code"],
                              "detection_status": "not_applicable", "detection_verdict": "",
                              "detection_positive": "", "marking_passed": "",
                              "error_type": "" if fmt["ok"] else "ruff_format_error", "error": fmt["error"],
                              "input_path": item["source_path"],
                              "output_path": str(fmt["path"].relative_to(OUT)),
                              "command": fmt["command"], "tool_seconds": fmt["tool_seconds"]}
        fmt_rows = [r for r in fmt_rows if not (
            r["dataset"] == item["dataset"] and r["problem_id"] == str(item["problem_id"])
            and r["sample_index"] == str(item["sample_index"]) and r["variant"] in
            ("original_formatted", "acw_notab", "acw_full", "sew"))]
        fmt_rows.append(original_formatted)
        if fmt["ok"]:
            formatted_path = fmt["path"]
            if (sid, "fmt_first", "original_formatted") not in artifact_keys:
                artifacts.append({"dataset": item["dataset"], "sample_id": sid, "problem_id": item["problem_id"],
                                  "sample_index": item["sample_index"], "stage": "fmt_first",
                                  "variant": "original_formatted", "ruff_profile": "", "ruff_mode": "",
                                  "path": str(formatted_path.relative_to(OUT)),
                                  "source_code_sha256": sha(item["source_code"]), "code_sha256": sha(fmt["code"]),
                                  "changed": fmt["code"] != item["source_code"], "parses": fmt["parses"],
                                  "parse_error": "", "sloc": item["sloc"], "status": "ok"})
                artifact_keys.add((sid, "fmt_first", "original_formatted"))
            fmt_result = initial.get((sid, "fmt_first"))
            if fmt_result:
                for variant, code in (("acw_notab", fmt_result["code_notab"]), ("acw_full", fmt_result["code_full"])):
                    target = OUT / "code" / item["dataset"] / str(item["problem_id"]) / str(item["sample_index"]) / "fmt_first" / f"{variant}.py"
                    target.write_text(code, encoding="utf-8", newline="")
                    det = acw_detect[(sid, "fmt_first", variant)]
                    parses, parse_error = parse_status(code)
                    fmt_rows.append({"dataset": item["dataset"], "problem_id": item["problem_id"],
                                     "sample_index": item["sample_index"], "arm": "fmt_first", "variant": variant,
                                     "applied": fmt_result["applied"], "parses": parses,
                                     "changed": code != fmt["code"], "detection_status": det["status"],
                                     "detection_verdict": det["verdict"], "detection_positive": det["positive"],
                                     "marking_passed": bool(fmt_result["applied"] and parses and det["positive"] is True),
                                     "error_type": fmt_result["error_type"] or ("post_marking_syntax_error" if not parses else ""),
                                     "error": fmt_result["error"] or parse_error or det["error"],
                                     "input_path": str(formatted_path.relative_to(OUT)),
                                     "output_path": str(target.relative_to(OUT)), "command": "Sourcery + ACW rules 36–44" + (" + 45" if variant == "acw_full" else ""),
                                     "tool_seconds": fmt_result.get("batch_seconds", ""),
                                     "sourcery_batch_id": fmt_result.get("batch_number", "")})
                    if (sid, "fmt_first", variant) not in artifact_keys:
                        artifacts.append({"dataset": item["dataset"], "sample_id": sid, "problem_id": item["problem_id"],
                                          "sample_index": item["sample_index"], "stage": "fmt_first", "variant": variant,
                                          "ruff_profile": "", "ruff_mode": "", "path": str(target.relative_to(OUT)),
                                          "source_code_sha256": sha(fmt["code"]), "code_sha256": sha(code),
                                          "changed": code != fmt["code"], "parses": parses, "parse_error": parse_error,
                                          "sloc": item["sloc"], "status": "ok" if fmt_result["applied"] else "error"})
                        artifact_keys.add((sid, "fmt_first", variant))
                sew_path = formatted_path.parent / "sew.py"
                sew_result = sew_attempt(item, fmt["code"], sew_path)
                fmt_rows.append({"dataset": item["dataset"], "problem_id": item["problem_id"],
                                 "sample_index": item["sample_index"], "arm": "fmt_first", "variant": "sew",
                                 "applied": sew_result["applied"], "parses": sew_result["parses"],
                                 "changed": sew_result["changed"], "detection_status": sew_result["detection_status"],
                                 "detection_verdict": sew_result["detection_verdict"], "detection_positive": sew_result["detection_positive"],
                                 "marking_passed": sew_result["marking_passed"], "error_type": sew_result["error_type"],
                                 "error": sew_result["error"], "input_path": str(formatted_path.relative_to(OUT)),
                                 "output_path": str(sew_path.relative_to(OUT)), "command": "SEW embed after Ruff format",
                                 "tool_seconds": sew_result["tool_seconds"], "embed_status": sew_result["embed_status"]})
                if (sid, "fmt_first", "sew") not in artifact_keys:
                    artifacts.append({"dataset": item["dataset"], "sample_id": sid, "problem_id": item["problem_id"],
                                      "sample_index": item["sample_index"], "stage": "fmt_first", "variant": "sew",
                                      "ruff_profile": "", "ruff_mode": "", "path": str(sew_path.relative_to(OUT)),
                                      "source_code_sha256": sha(fmt["code"]), "code_sha256": sha(sew_result["code"]),
                                      "changed": sew_result["changed"], "parses": sew_result["parses"],
                                      "parse_error": sew_result["parse_error"], "sloc": item["sloc"],
                                      "status": "ok" if sew_result["applied"] else "error"})
                    artifact_keys.add((sid, "fmt_first", "sew"))
        else:
            for variant in ("acw_notab", "acw_full", "sew"):
                fmt_rows.append({"dataset": item["dataset"], "problem_id": item["problem_id"],
                                 "sample_index": item["sample_index"], "arm": "fmt_first", "variant": variant,
                                 "applied": False, "parses": "", "changed": "", "detection_status": "not_run",
                                 "detection_verdict": "", "detection_positive": "", "marking_passed": False,
                                 "error_type": "fmt_first_input_error", "error": fmt["error"],
                                 "input_path": item["source_path"], "output_path": "", "command": fmt["command"],
                                 "tool_seconds": fmt["tool_seconds"]})

    sort_key = lambda row: (row.get("dataset", ""), int(row.get("problem_id", 0) or 0),
                            int(row.get("sample_index", 0) or 0), row.get("arm", ""), row.get("variant", ""))
    marking_rows.sort(key=sort_key); fmt_rows.sort(key=sort_key); artifacts.sort(key=lambda row:(row["dataset"],int(row["problem_id"]),int(row["sample_index"]),row["stage"],row["variant"]))
    write_csv(OUT / "01_marking.csv", marking_rows, list(marking_rows[0].keys()))
    write_csv(OUT / "01_fmt_first.csv", fmt_rows, fmt_fields)
    write_jsonl(OUT / "artifacts_stage1.jsonl", artifacts)
    previous = read_jsonl(OUT / "acw_sourcery_runs.jsonl")
    write_jsonl(OUT / "acw_sourcery_runs.jsonl", previous + operations)
    print(f"small SLOC samples attempted: {len(main_entries)} main, {len(fmt_entries)} fmt_first", flush=True)


if __name__ == "__main__":
    main()
