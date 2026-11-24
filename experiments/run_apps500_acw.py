#!/usr/bin/env python3
"""Apply and detect ACW on APPS Qwen/Llama artifacts through Sourcery."""

from __future__ import annotations

import argparse
import ast
import contextlib
import csv
import hashlib
import io
import json
import os
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import autopep8
import base_ast
from sew import EXPERIMENT_KEY, detect

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "watermark-results" / "apps500_quality"
RUFF = ROOT / "ACW" / ".tools" / "local" / "bin" / "ruff"
SOURCERY = ROOT / "ACW" / ".tools" / "local" / "bin" / "sourcery"
SOURCERY_CONFIG = OUT / "config" / "acw_sourcery.yaml"
TIMEOUT = 120
BATCH_SIZE = 100
WORKERS = 4
AUTOPEP8_RULES = (
    ("E225", "E226", "E227", "E228", "E241", "E242", "E251", "E252", "E231"),
    ("E27",), ("E123",), ("W292",), ("E301", "E302", "E305", "E306"),
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def sha(code: str) -> str:
    return hashlib.sha256(code.encode("utf-8")).hexdigest()


def parse_status(code: str) -> tuple[bool, str]:
    try:
        ast.parse(code)
        compile(code, "<acw-sample>", "exec")
        return True, ""
    except (SyntaxError, ValueError, TypeError) as error:
        return False, str(error)


def apply_local_rules(path: Path, include_tabs: bool) -> tuple[bool, str]:
    errors: list[str] = []
    for rule, transform in (
        (36, base_ast.transform_operations_add),
        (37, base_ast.transform_operations_mult),
        (38, base_ast.transform_comparison_LG),
        (39, base_ast.transform_comparison_LGE),
    ):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                transform(str(path))
        except Exception as error:
            errors.append(f"rule_{rule}: {type(error).__name__}: {error}")
    for offset, selection in enumerate(AUTOPEP8_RULES, start=40):
        try:
            source = path.read_text(encoding="utf-8")
            formatted = autopep8.fix_code(source, options={"select": list(selection)})
            path.write_text(formatted, encoding="utf-8", newline="")
        except Exception as error:
            errors.append(f"rule_{offset}: {type(error).__name__}: {error}")
    if include_tabs:
        try:
            lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
            output = []
            for line in lines:
                leading_spaces = len(line) - len(line.lstrip(" "))
                output.append("\t" * (leading_spaces // 4) + line.lstrip(" "))
            path.write_text("".join(output), encoding="utf-8", newline="")
        except Exception as error:
            errors.append(f"rule_45: {type(error).__name__}: {error}")
    return not errors, "; ".join(errors)


def run_sourcery_batch(batch: list[dict[str, Any]], phase: str, batch_number: int,
                       include_tabs: bool = False) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    started = time.monotonic()
    operation: dict[str, Any] = {
        "phase": phase, "batch_number": batch_number,
        "sample_ids": [item["sample_id"] for item in batch],
        "variants": sorted({item.get("variant", "") for item in batch}),
        "file_count": len(batch), "timeout_seconds": TIMEOUT,
    }
    outputs: list[dict[str, Any]] = []
    try:
        with tempfile.TemporaryDirectory(prefix=f"acw_{phase}_{batch_number:04d}_", dir=OUT) as work:
            workdir = Path(work)
            files: dict[str, Path] = {}
            for index, item in enumerate(batch):
                name = f"sample_{index:04d}.py"
                path = workdir / name
                path.write_text(item["source_code"], encoding="utf-8", newline="")
                files[name] = path
            env = os.environ.copy()
            dist = ROOT / "ACW" / ".tools" / "local" / "lib" / "python3.14" / "dist-packages"
            env["PYTHONPATH"] = str(dist) + (":" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
            local_bin = str(ROOT / "ACW" / ".tools" / "local" / "bin")
            env["PATH"] = local_bin + os.pathsep + env.get("PATH", "")
            argv = [str(SOURCERY), "review", "--config", str(SOURCERY_CONFIG),
                    "--fix", "--no-summary", str(workdir)]
            try:
                run = subprocess.run(argv, cwd=ROOT, env=env, capture_output=True, text=True,
                                     timeout=TIMEOUT)
                operation.update({"argv": argv, "exit": run.returncode, "stdout": run.stdout,
                                  "stderr": run.stderr, "status": "ok" if run.returncode == 0 else "error"})
            except subprocess.TimeoutExpired as error:
                operation.update({"argv": argv, "exit": None, "stdout": str(error.stdout or ""),
                                  "stderr": str(error.stderr or ""), "status": "timeout"})
            for index, item in enumerate(batch):
                path = files[f"sample_{index:04d}.py"]
                local_ok, local_error = apply_local_rules(path, include_tabs or item.get("variant") == "acw_full")
                try:
                    output_code = path.read_text(encoding="utf-8")
                    read_error = ""
                except Exception as error:
                    output_code = item["source_code"]
                    read_error = f"read_output: {type(error).__name__}: {error}"
                sourcery_ok = operation["status"] == "ok"
                outputs.append({
                    **item, "output_code": output_code,
                    "sourcery_ok": sourcery_ok, "local_ok": local_ok,
                    "applied": bool(sourcery_ok and local_ok and not read_error),
                    "error_type": ("timeout" if operation["status"] == "timeout" else
                                   "sourcery_error" if not sourcery_ok else
                                   "local_rule_error" if not local_ok else
                                   "artifact_read_error" if read_error else ""),
                    "error": "\n".join(part for part in (
                        (operation.get("stderr", "") + "\n" + operation.get("stdout", "")).strip()
                        if not sourcery_ok else "", local_error, read_error) if part),
                })
    except Exception as error:
        operation.update({"status": "batch_error", "exit": None,
                          "stderr": f"{type(error).__name__}: {error}"})
        outputs = [{**item, "output_code": item["source_code"], "sourcery_ok": False,
                    "local_ok": False, "applied": False, "error_type": "batch_error",
                    "error": operation["stderr"]} for item in batch]
    operation["seconds"] = time.monotonic() - started
    return outputs, operation


def execute_batches(entries: list[dict[str, Any]], phase: str,
                    include_tabs: bool = False) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    batches = [entries[start:start + BATCH_SIZE] for start in range(0, len(entries), BATCH_SIZE)]
    results: list[dict[str, Any]] = []
    operations: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(run_sourcery_batch, batch, phase, number, include_tabs): (number, batch)
                   for number, batch in enumerate(batches)}
        for completed, future in enumerate(as_completed(futures), 1):
            batch_results, operation = future.result()
            for row in batch_results:
                row["batch_number"] = operation["batch_number"]
                row["batch_seconds"] = operation["seconds"]
            results.extend(batch_results)
            operations.append(operation)
            if completed % 10 == 0 or completed == len(batches):
                print(f"{phase} Sourcery batches {completed}/{len(batches)}", flush=True)
    results.sort(key=lambda row: (row["sample_id"], row.get("variant", "")))
    operations.sort(key=lambda row: row["batch_number"])
    return results, operations


def tabbed_copy(code: str) -> str:
    lines = code.splitlines(keepends=True)
    output = []
    for line in lines:
        leading_spaces = len(line) - len(line.lstrip(" "))
        output.append("\t" * (leading_spaces // 4) + line.lstrip(" "))
    return "".join(output)


def load_initial_entries() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sloc_rows = read_csv(OUT / "00_sloc.csv")
    fmt_rows = read_csv(OUT / "01_fmt_first.csv")
    fmt_ok = {(r["dataset"], r["problem_id"], r["sample_index"])
              for r in fmt_rows if r["variant"] == "original_formatted" and r["applied"] == "True"}
    entries_main: list[dict[str, Any]] = []
    entries_fmt: list[dict[str, Any]] = []
    for row in sloc_rows:
        sample_id = f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}"
        source = OUT / "code" / row["dataset"] / row["problem_id"] / row["sample_index"] / "original.py"
        if not source.is_file():
            continue
        code = source.read_text(encoding="utf-8")
        entry = {"sample_id": sample_id, "dataset": row["dataset"],
                 "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                 "sloc": int(row["sloc"]) if row["sloc"] else None,
                 "source_code": code, "source_path": str(source.relative_to(OUT))}
        entries_main.append({**entry, "arm": "main"})
        if (row["dataset"], row["problem_id"], row["sample_index"]) in fmt_ok:
            fmt_path = source.parent / "fmt_first" / "original_formatted.py"
            if fmt_path.is_file():
                entries_fmt.append({**entry, "arm": "fmt_first",
                                    "source_code": fmt_path.read_text(encoding="utf-8"),
                                    "source_path": str(fmt_path.relative_to(OUT))})
    return entries_main, entries_fmt


def main() -> None:
    global WORKERS, BATCH_SIZE
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=WORKERS)
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    args = parser.parse_args()
    WORKERS, BATCH_SIZE = args.workers, args.batch_size

    entries_main, entries_fmt = load_initial_entries()
    initial: dict[tuple[str, str], dict[str, Any]] = {}
    operations: list[dict[str, Any]] = []

    for arm, entries in (("main", entries_main), ("fmt_first", entries_fmt)):
        transformed, op_rows = execute_batches(entries, f"mark_{arm}")
        operations.extend(op_rows)
        for row in transformed:
            key = row["sample_id"], arm
            code_notab = row["output_code"]
            code_full = tabbed_copy(code_notab)
            initial[key] = {**row, "code_notab": code_notab, "code_full": code_full}

    marking_rows = read_csv(OUT / "01_marking.csv")
    fmt_marking_rows = read_csv(OUT / "01_fmt_first.csv")
    detection_rows = read_csv(OUT / "01_sew_detection.csv")
    artifacts = read_jsonl(OUT / "artifacts_stage1.jsonl")
    eligible = {r["sample_id"] for r in entries_main}
    detection_entries: list[dict[str, Any]] = []
    for row in entries_main:
        result = initial[(row["sample_id"], "main")]
        for variant, code in (("acw_notab", result["code_notab"]), ("acw_full", result["code_full"])):
            detection_entries.append({**row, "arm": "main", "variant": variant,
                                      "source_code": code, "source_path": row["source_path"]})
    for row in entries_fmt:
        result = initial[(row["sample_id"], "fmt_first")]
        for variant, code in (("acw_notab", result["code_notab"]), ("acw_full", result["code_full"])):
            detection_entries.append({**row, "arm": "fmt_first", "variant": variant,
                                      "source_code": code, "source_path": row["source_path"]})

    detected, op_rows = execute_batches(detection_entries, "detect")
    operations.extend(op_rows)
    detect_map: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in detected:
        parses, parse_error = parse_status(row["output_code"])
        positive = row["output_code"] == row["source_code"]
        detect_map[(row["sample_id"], row["arm"], row["variant"])] = {
            **row, "parses": parses, "parse_error": parse_error,
            "detection_status": "ok" if row["applied"] else "error",
            "verdict": "Watermark detected" if positive else "No watermark evidence",
            "positive": positive if row["applied"] else "",
        }

    artifact_keys = {(row["sample_id"], row["stage"], row["variant"]) for row in artifacts}
    for row in entries_main:
        sid = row["sample_id"]
        result = initial[(sid, "main")]
        for variant, code in (("acw_notab", result["code_notab"]), ("acw_full", result["code_full"])):
            out = OUT / row["source_path"]
            del out
            target = OUT / "code" / row["dataset"] / str(row["problem_id"]) / str(row["sample_index"]) / f"{variant}.py"
            target.write_text(code, encoding="utf-8", newline="")
            parses, parse_error = parse_status(code)
            marked = variant in ("acw_notab", "acw_full") and sid in eligible
            if marked:
                detected_row = detect_map[(sid, "main", variant)]
                base = {"dataset": row["dataset"], "problem_id": row["problem_id"],
                        "sample_index": row["sample_index"], "arm": "main", "variant": variant,
                        "sloc": row["sloc"], "applied": result["applied"], "parses": parses,
                        "changed": code != row["source_code"],
                        "detection_status": detected_row["detection_status"],
                        "detection_verdict": detected_row["verdict"],
                        "detection_positive": detected_row["positive"],
                        "marking_passed": bool(result["applied"] and parses and detected_row["positive"] is True),
                        "error_type": result["error_type"] or ("post_marking_syntax_error" if not parses else ""),
                        "error": result["error"] or parse_error or detected_row["error"],
                        "output_path": str(target.relative_to(OUT)),
                        "tool_seconds": result.get("batch_seconds", ""),
                        "sourcery_batch_id": result.get("batch_number", ""),
                    }
                marking_rows = [r for r in marking_rows if not (
                    r["dataset"] == row["dataset"] and r["problem_id"] == str(row["problem_id"])
                    and r["sample_index"] == str(row["sample_index"]) and r["variant"] == variant and r["arm"] == "main")]
                marking_rows.append(base)
                artifact = {
                    "dataset": row["dataset"], "sample_id": sid, "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "stage": "marked", "variant": variant,
                    "ruff_profile": "", "ruff_mode": "", "path": str(target.relative_to(OUT)),
                    "source_code_sha256": sha(row["source_code"]), "code_sha256": sha(code),
                    "changed": code != row["source_code"], "parses": parses,
                    "parse_error": parse_error, "sloc": row["sloc"], "status": "ok" if result["applied"] else "error",
                }
                identity = (sid, "marked", variant)
                if identity not in artifact_keys:
                    artifacts.append(artifact)
                    artifact_keys.add(identity)

    for row in entries_fmt:
        sid = row["sample_id"]
        result = initial[(sid, "fmt_first")]
        for variant, code in (("acw_notab", result["code_notab"]), ("acw_full", result["code_full"])):
            target = OUT / "code" / row["dataset"] / str(row["problem_id"]) / str(row["sample_index"]) / "fmt_first" / f"{variant}.py"
            target.write_text(code, encoding="utf-8", newline="")
            parses, parse_error = parse_status(code)
            detected_row = detect_map[(sid, "fmt_first", variant)]
            fmt_marking_rows = [r for r in fmt_marking_rows if not (
                r["dataset"] == row["dataset"] and r["problem_id"] == str(row["problem_id"])
                and r["sample_index"] == str(row["sample_index"]) and r["variant"] == variant)]
            fmt_marking_rows.append({
                "dataset": row["dataset"], "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                "arm": "fmt_first", "variant": variant, "applied": result["applied"], "parses": parses,
                "changed": code != row["source_code"], "detection_status": detected_row["detection_status"],
                "detection_verdict": detected_row["verdict"], "detection_positive": detected_row["positive"],
                "marking_passed": bool(result["applied"] and parses and detected_row["positive"] is True),
                "error_type": result["error_type"] or ("post_marking_syntax_error" if not parses else ""),
                "error": result["error"] or parse_error or detected_row["error"],
                "input_path": row["source_path"], "output_path": str(target.relative_to(OUT)),
                "command": "Sourcery configured rules + ACW rules 36–44" + (" + 45" if variant == "acw_full" else ""),
                "tool_seconds": result.get("batch_seconds", ""), "sourcery_batch_id": result.get("batch_number", ""),
            })
            artifact = {
                "dataset": row["dataset"], "sample_id": sid, "problem_id": row["problem_id"],
                "sample_index": row["sample_index"], "stage": "fmt_first", "variant": variant,
                "ruff_profile": "", "ruff_mode": "", "path": str(target.relative_to(OUT)),
                "source_code_sha256": sha(row["source_code"]), "code_sha256": sha(code),
                "changed": code != row["source_code"], "parses": parses,
                "parse_error": parse_error, "sloc": row["sloc"], "status": "ok" if result["applied"] else "error",
            }
            identity = (sid, "fmt_first", variant)
            if identity not in artifact_keys:
                artifacts.append(artifact)
                artifact_keys.add(identity)

    sort_key = lambda row: (row.get("dataset", ""), int(row.get("problem_id", 0) or 0), int(row.get("sample_index", 0) or 0), row.get("arm", ""), row.get("variant", ""))
    marking_rows.sort(key=sort_key)
    fmt_marking_rows.sort(key=sort_key)
    detection_rows.sort(key=sort_key)
    artifacts.sort(key=lambda row: (row["dataset"], int(row["problem_id"]), int(row["sample_index"]), row["stage"], row["variant"]))
    write_csv(OUT / "01_marking.csv", marking_rows, list(marking_rows[0].keys()))
    write_csv(OUT / "01_fmt_first.csv", fmt_marking_rows, list(fmt_marking_rows[0].keys()))
    write_csv(OUT / "01_sew_detection.csv", detection_rows, list(detection_rows[0].keys()))
    write_jsonl(OUT / "artifacts_stage1.jsonl", artifacts)
    write_jsonl(OUT / "acw_sourcery_runs.jsonl", operations)
    env_path = OUT / "acw_environment.json"
    env_path.write_text(json.dumps({
        "sourcery_version": "1.46.0", "libcst_version": "1.9.0", "autopep8_version": autopep8.__version__,
        "sourcery_config": str(SOURCERY_CONFIG),
        "rule_mapping": {"acw_notab": "Sourcery configured rules 1–35, ACW LibCST rules 36–39, autopep8 rules 40–44",
                         "acw_full": "acw_notab plus ACW indentation-to-tab rule 45"},
        "workers": WORKERS, "batch_size": BATCH_SIZE, "batch_timeout_seconds": TIMEOUT,
        "source_rows": len(entries_main), "fmt_first_rows": len(entries_fmt),
        "mark_batches": sum(r["phase"].startswith("mark_") for r in operations),
        "detection_batches": sum(r["phase"] == "detect" for r in operations),
        "status": "completed_with_per_batch_statuses",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ACW outputs: main inputs={len(entries_main)}, fmt_first inputs={len(entries_fmt)}, detections={len(detected)}", flush=True)


if __name__ == "__main__":
    main()
