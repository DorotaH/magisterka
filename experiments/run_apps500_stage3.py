#!/usr/bin/env python3
"""Calculate static metrics for every available APPS artifact."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "watermark-results" / "apps500_quality"
TOOLS = ROOT / "ACW" / ".tools" / "local" / "bin"
RUFF = TOOLS / "ruff"
RADON = TOOLS / "radon"
COMPLEXIPY = TOOLS / "complexipy"
TIMEOUT = 120
PROFILES = {
    "default": [],
    "strict": ["--select", "E,F,W,I,B,UP,SIM"],
}


def lines(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def command(argv: list[str]) -> dict[str, Any]:
    started = time.monotonic()
    try:
        proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=TIMEOUT)
        return {"argv": argv, "exit": proc.returncode, "stdout": proc.stdout,
                "stderr": proc.stderr, "seconds": time.monotonic() - started,
                "status": "ok" if proc.returncode == 0 else "error"}
    except subprocess.TimeoutExpired as error:
        return {"argv": argv, "exit": None, "stdout": str(error.stdout or ""),
                "stderr": str(error.stderr or ""), "seconds": time.monotonic() - started,
                "status": "timeout"}
    except Exception as error:
        return {"argv": argv, "exit": None, "stdout": "", "stderr": str(error),
                "seconds": time.monotonic() - started, "status": "error"}


def json_for_path(run: dict[str, Any], path: Path) -> Any:
    if run["status"] != "ok":
        raise RuntimeError(run["stderr"] or f"exit={run['exit']}")
    value = json.loads(run["stdout"] or "{}")
    # Radon uses the exact path in JSON; Complexipy writes to its requested file.
    wanted = str(path)
    if isinstance(value, dict):
        if wanted in value:
            return value[wanted]
        for key, result in value.items():
            if Path(key).name == path.name:
                return result
    return value


def static_metrics(item: dict[str, Any]) -> dict[str, Any]:
    path = OUT / item["path"]
    result: dict[str, Any] = {
        "artifact_id": item["artifact_id"], "dataset": item["dataset"],
        "sample_id": item["sample_id"], "problem_id": item["problem_id"],
        "sample_index": item["sample_index"], "stage": item["stage"],
        "variant": item["variant"], "ruff_profile": item.get("ruff_profile", ""),
        "ruff_mode": item.get("ruff_mode", ""), "path": item["path"],
        "code_sha256": item.get("code_sha256") or sha(path),
    }
    for metric, argv in (
        ("radon_raw", [str(RADON), "raw", "-j", str(path)]),
        ("radon_mi", [str(RADON), "mi", "-j", str(path)]),
        ("radon_cc", [str(RADON), "cc", "-j", str(path)]),
    ):
        run = command(argv)
        result[f"{metric}_status"] = run["status"]
        result[f"{metric}_error"] = run["stderr"] if run["status"] != "ok" else ""
        try:
            result[metric] = json_for_path(run, path) if run["status"] == "ok" else None
        except Exception as error:
            result[metric] = None
            result[f"{metric}_status"] = "error"
            result[f"{metric}_error"] = str(error)
    complex_path = OUT / "metrics" / "complexipy" / f"{result['code_sha256']}.json"
    complex_path.parent.mkdir(parents=True, exist_ok=True)
    run = command([str(COMPLEXIPY), "--isolated", "--no-ignore", "--check-script",
                   "--output-format", "json", "--output", str(complex_path), str(path)])
    result["complexipy_status"] = run["status"]
    result["complexipy_error"] = run["stderr"] if run["status"] != "ok" else ""
    try:
        if run["status"] != "ok":
            raise RuntimeError(run["stderr"] or f"exit={run['exit']}")
        result["complexipy"] = json.loads(complex_path.read_text(encoding="utf-8"))
    except Exception as error:
        result["complexipy"] = None
        result["complexipy_status"] = "error"
        result["complexipy_error"] = str(error)
    return result


def static_metrics_batch(batch: list[tuple[str, dict[str, Any]]], batch_number: int) -> dict[str, dict[str, Any]]:
    """Invoke Radon and Complexipy once per batch while keeping file-level status."""
    paths = [str(OUT / item["path"]) for _, item in batch]
    result = {digest: {"code_sha256": digest} for digest, _ in batch}
    tool_specs = (
        ("radon_raw", [str(RADON), "raw", "-j", *paths]),
        ("radon_mi", [str(RADON), "mi", "-j", *paths]),
        ("radon_cc", [str(RADON), "cc", "-j", *paths]),
    )
    for metric, argv in tool_specs:
        run = command(argv)
        try:
            parsed = json.loads(run["stdout"] or "{}") if run["status"] == "ok" else {}
            if not isinstance(parsed, dict):
                raise TypeError("Radon JSON output is not a mapping")
        except Exception as error:
            parsed = {}
            message = run["stderr"] or str(error)
        else:
            message = run["stderr"] if run["status"] != "ok" else ""
        for digest, item in batch:
            path = str(OUT / item["path"])
            value = parsed.get(path)
            if metric == "radon_cc" and value is None and run["status"] == "ok" and item.get("parses") is True:
                # Radon omits a file from CC JSON when it contains no eligible blocks.
                value = []
            if value is None:
                result[digest][metric] = None
                result[digest][f"{metric}_status"] = "error"
                result[digest][f"{metric}_error"] = message or "Radon returned no record for file"
            else:
                result[digest][metric] = value
                result[digest][f"{metric}_status"] = "ok"
                result[digest][f"{metric}_error"] = ""

    complex_path = OUT / "metrics" / "complexipy" / f"batch-{batch_number:05d}.json"
    complex_path.parent.mkdir(parents=True, exist_ok=True)
    run = command([str(COMPLEXIPY), "--isolated", "--no-ignore", "--check-script",
                   "--output-format", "json", "--output", str(complex_path), *paths])
    by_path: dict[str, list[dict[str, Any]]] = {}
    error_message = run["stderr"] or run["stdout"] or f"Complexipy exit={run['exit']}"
    try:
        if not complex_path.is_file():
            raise RuntimeError(error_message or "Complexipy output file is missing")
        parsed = json.loads(complex_path.read_text(encoding="utf-8"))
        for entry in parsed:
            key = str(Path(entry.get("path", "")).resolve()) if entry.get("path") else ""
            by_path[key] = by_path.get(key, []) + [entry]
    except Exception as error:
        error_message = str(error)
    for digest, item in batch:
        path = str((OUT / item["path"]).resolve())
        functions = by_path.get(path)
        result[digest]["complexipy"] = functions
        result[digest]["complexipy_status"] = "ok" if functions is not None else "error"
        if functions is not None:
            result[digest]["complexipy_error"] = ""
        else:
            candidates = [line.strip() for line in (run["stderr"] + "\n" + run["stdout"]).splitlines()
                          if str((OUT / item["path"]).resolve()) in line or "No files were found" in line]
            result[digest]["complexipy_error"] = "\n".join(candidates) or error_message
    return result


def ruff_check(path: Path, artifact_id: str, dataset: str, sample_id: str,
               problem_id: Any, sample_index: Any, stage: str, variant: str,
               profile: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    argv = [str(RUFF), "check", "--isolated", "--no-cache", *PROFILES[profile],
            "--output-format", "json", str(path)]
    run = command(argv)
    try:
        diagnostics = json.loads(run["stdout"] or "[]")
        if not isinstance(diagnostics, list):
            raise TypeError("Ruff output must be a JSON list")
        status = "ok" if run["exit"] in (0, 1) else run["status"]
    except Exception as error:
        diagnostics = []
        status = "error"
        run["stderr"] = f"{run['stderr']} {error}".strip()
    codes: dict[str, int] = {}
    for diag in diagnostics:
        code = diag.get("code", "invalid-syntax")
        codes[code] = codes.get(code, 0) + 1
    summary = {
        "artifact_id": artifact_id, "dataset": dataset, "sample_id": sample_id,
        "problem_id": problem_id, "sample_index": sample_index, "stage": stage,
        "variant": variant, "ruff_profile": profile, "status": status,
        "exit": run["exit"], "diagnostic_count": len(diagnostics),
        "diagnostic_codes": json.dumps(dict(sorted(codes.items())), sort_keys=True),
        "command": json.dumps(argv), "error": run["stderr"] if status != "ok" else "",
    }
    details = [{
        "artifact_id": artifact_id, "ruff_profile": profile,
        "code": diag.get("code", "invalid-syntax"), "message": diag.get("message", ""),
        "row": (diag.get("location") or {}).get("row"),
        "column": (diag.get("location") or {}).get("column"),
    } for diag in diagnostics]
    return summary, details


def main() -> None:
    artifacts = lines(OUT / "artifacts_all.jsonl")
    for item in artifacts:
        item.setdefault("artifact_id", f"{item.get('sample_id', '')}|{item.get('stage', '')}|{item.get('variant', '')}")
    available = [item for item in artifacts if item.get("path") and (OUT / item["path"]).is_file()]
    missing = [item for item in artifacts if not item.get("path") or not (OUT / item["path"]).is_file()]
    hashes: dict[str, dict[str, Any]] = {}
    for item in available:
        path = OUT / item["path"]
        digest = sha(path)
        representative = dict(item)
        representative["code_sha256"] = digest
        hashes.setdefault(digest, representative)

    # Compute static metrics once per unique source, then retain a row for every artifact.
    cache: dict[str, dict[str, Any]] = {}
    batches = [list(hashes.items())[start:start + 100] for start in range(0, len(hashes), 100)]
    with ThreadPoolExecutor(max_workers=8) as pool:
        future_map = {pool.submit(static_metrics_batch, batch, number): batch
                      for number, batch in enumerate(batches)}
        for index, future in enumerate(as_completed(future_map), 1):
            batch = future_map[future]
            try:
                cache.update(future.result())
            except Exception as error:
                for digest, _ in batch:
                    cache[digest] = {"code_sha256": digest, "radon_raw_status": "error",
                                     "radon_raw_error": str(error), "radon_mi_status": "error",
                                     "radon_mi_error": str(error), "radon_cc_status": "error",
                                     "radon_cc_error": str(error), "complexipy_status": "error",
                                     "complexipy_error": str(error)}
            if index % 10 == 0 or index == len(batches):
                print(f"metric batches {index}/{len(batches)}; unique code {min(index * 100, len(hashes))}/{len(hashes)}", flush=True)

    metric_rows: list[dict[str, Any]] = []
    block_rows: list[dict[str, Any]] = []
    complex_rows: list[dict[str, Any]] = []
    for item in available:
        digest = sha(OUT / item["path"])
        cached = cache[digest]
        row = {key: value for key, value in cached.items() if key not in ("artifact_id",)}
        row.update({key: item.get(key, "") for key in (
            "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "stage",
            "variant", "ruff_profile", "ruff_mode", "path", "sloc", "status")})
        if not row.get("status"):
            row["status"] = "ok"
        metric_rows.append(row)
        cc = row.get("radon_cc")
        if row.get("radon_cc_status") == "ok" and isinstance(cc, list):
            for block in cc:
                block_rows.append({"artifact_id": item["artifact_id"], **block})
        elif row.get("radon_cc_status") == "ok":
            # Empty block list remains explicitly distinct from numeric complexity zero.
            block_rows.append({"artifact_id": item["artifact_id"], "status": "undefined", "reason": "no function, method, or class blocks"})
        cp = row.get("complexipy")
        if row.get("complexipy_status") == "ok" and isinstance(cp, list):
            for function in cp:
                complex_rows.append({"artifact_id": item["artifact_id"], **function})

    for item in missing:
        metric_rows.append({"artifact_id": item.get("artifact_id", ""), "dataset": item.get("dataset", ""),
                            "sample_id": item.get("sample_id", ""), "problem_id": item.get("problem_id", ""),
                            "sample_index": item.get("sample_index", ""), "stage": item.get("stage", ""),
                            "variant": item.get("variant", ""), "status": "error",
                            "radon_raw_status": "not_run", "radon_mi_status": "not_run",
                            "radon_cc_status": "not_run", "complexipy_status": "not_run",
                            "radon_raw_error": "artifact unavailable", "radon_mi_error": "artifact unavailable",
                            "radon_cc_error": "artifact unavailable", "complexipy_error": "artifact unavailable"})

    # Ruff check metrics for artifacts created by fmt_first, for both rule profiles.
    fmt_artifacts = [item for item in available if item["stage"] == "fmt_first"]
    ruff_summaries: list[dict[str, Any]] = []
    ruff_details: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = []
        for item in fmt_artifacts:
            path = OUT / item["path"]
            for profile in PROFILES:
                futures.append(pool.submit(ruff_check, path, item["artifact_id"], item["dataset"],
                                           item["sample_id"], item["problem_id"], item["sample_index"],
                                           item["stage"], item["variant"], profile))
        for future in as_completed(futures):
            summary, details = future.result()
            ruff_summaries.append(summary)
            ruff_details.extend(details)

    # Keep Ruff rows for fmt_first attempts that had no code artifact.
    for row in read_csv(OUT / "01_fmt_first.csv"):
        path = row.get("output_path", "")
        if path and (OUT / path).is_file():
            continue
        if row["variant"] not in ("original_formatted", "acw_notab", "acw_full", "sew"):
            continue
        artifact_id = f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}|fmt_first|{row['variant']}"
        for profile in PROFILES:
            ruff_summaries.append({
                "artifact_id": artifact_id, "dataset": row["dataset"],
                "sample_id": f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}",
                "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                "stage": "fmt_first", "variant": row["variant"], "ruff_profile": profile,
                "status": "not_run", "exit": "", "diagnostic_count": "", "diagnostic_codes": "",
                "command": "", "error": row["error"] or row["error_type"] or "input artifact unavailable",
            })

    # A failed marking attempt is still measured when its output file exists.
    for table_name in ("01_marking.csv", "01_fmt_first.csv"):
        with (OUT / table_name).open(encoding="utf-8") as stream:
            for row in csv.DictReader(stream):
                if row["variant"] not in ("acw_notab", "acw_full", "sew", "original_formatted"):
                    continue
                path = row.get("output_path", "")
                if path and (OUT / path).is_file():
                    continue
                error = row["error"] or row["error_type"] or "marking did not produce an artifact"
                metric_rows.append({
                    "artifact_id": f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}|{row.get('arm', '')}|{row['variant']}",
                    "dataset": row["dataset"], "sample_id": f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}",
                    "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                    "stage": row.get("arm", ""), "variant": row["variant"], "status": "not_run",
                    **{f"{tool}_status": "not_run" for tool in ("radon_raw", "radon_mi", "radon_cc", "complexipy")},
                    **{f"{tool}_error": error for tool in ("radon_raw", "radon_mi", "radon_cc", "complexipy")},
                })

    write_csv(OUT / "metrics_artifacts.csv", metric_rows, [
        "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "stage", "variant",
        "ruff_profile", "ruff_mode", "path", "sloc", "status", "radon_raw_status", "radon_raw_error",
        "radon_raw", "radon_mi_status", "radon_mi_error", "radon_mi", "radon_cc_status",
        "radon_cc_error", "radon_cc", "complexipy_status", "complexipy_error", "complexipy",
    ])
    write_jsonl(OUT / "metrics_radon_cc_blocks.jsonl", block_rows)
    write_jsonl(OUT / "metrics_complexipy_functions.jsonl", complex_rows)
    write_csv(OUT / "ruff_fmt_first_summary.csv", ruff_summaries, [
        "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "stage", "variant",
        "ruff_profile", "status", "exit", "diagnostic_count", "diagnostic_codes", "command", "error",
    ])
    write_csv(OUT / "ruff_fmt_first_diagnostics.csv", ruff_details,
              ["artifact_id", "ruff_profile", "code", "message", "row", "column"])

    # Attach the three requested SLOC partitions without aggregating or comparing datasets.
    groups: dict[tuple[str, str, str], dict[str, str]] = {}
    with (OUT / "00_groups.csv").open(encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            key = (row["dataset"], row["problem_id"], row["sample_index"])
            groups.setdefault(key, {})[row["group_type"]] = row["group"]
    by_group: list[dict[str, Any]] = []
    for item in metric_rows:
        key = (str(item.get("dataset", "")), str(item.get("problem_id", "")), str(item.get("sample_index", "")))
        group_map = groups.get(key, {})
        for group_type in ("fixed", "common_quantile", "dataset_quantile"):
            if group_type in group_map:
                by_group.append({**item, "group_type": group_type, "group": group_map[group_type]})
    write_csv(OUT / "metrics_by_sloc_group.csv", by_group, [
        "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "stage", "variant",
        "ruff_profile", "ruff_mode", "group_type", "group", "sloc", "status", "radon_raw_status",
        "radon_raw_error", "radon_raw", "radon_mi_status", "radon_mi_error", "radon_mi",
        "radon_cc_status", "radon_cc_error", "radon_cc", "complexipy_status", "complexipy_error", "complexipy",
    ])

    (OUT / "stage3_environment.json").write_text(json.dumps({
        "radon": "6.0.1", "complexipy": "9.0.0", "ruff": "0.17.5",
        "commands": {"radon_raw": "radon raw -j", "radon_mi": "radon mi -j", "radon_cc": "radon cc -j",
                     "complexipy": "complexipy --isolated --no-ignore --check-script --output-format json --output <json> <file>",
                     "ruff_check": "ruff check --isolated --no-cache [strict options] --output-format json <file>"},
        "timeout_seconds": TIMEOUT, "static_metrics_deduplication": "by SHA-256; one row retained per artifact",
        "aggregation": "none; metrics_by_sloc_group is artifact-level data with SLOC group labels",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"metric rows {len(metric_rows)}; unique code hashes {len(hashes)}; fmt_first Ruff rows {len(ruff_summaries)}", flush=True)


if __name__ == "__main__":
    main()
