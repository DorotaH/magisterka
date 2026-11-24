#!/usr/bin/env python3
"""Run the main Ruff actions on original and SEW-marked APPS artifacts."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import shutil
import subprocess
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from sew import EXPERIMENT_KEY, detect
from run_apps500_acw import execute_batches


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "watermark-results" / "apps500_quality"
RUFF = ROOT / "ACW" / ".tools" / "local" / "bin" / "ruff"
PROFILES = {
    "default": [],
    "strict": ["--select", "E,F,W,I,B,UP,SIM"],
}
MODES = ("check", "fix", "format", "fix_format")
VARIANTS = ("original", "sew", "acw_notab", "acw_full")
TIME_LIMIT_SECONDS = 120


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_code(code: str) -> tuple[bool, str]:
    try:
        tree = ast.parse(code)
        compile(tree, "<sample>", "exec")
        return True, ""
    except (SyntaxError, ValueError, TypeError) as error:
        return False, str(error)


def run_command(argv: list[str], timeout: int = TIME_LIMIT_SECONDS) -> dict[str, Any]:
    started = time.monotonic()
    try:
        result = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
        return {
            "argv": argv, "exit": result.returncode, "stdout": result.stdout,
            "stderr": result.stderr, "seconds": time.monotonic() - started,
            "error": "" if result.returncode < 2 else "tool_exit_error",
        }
    except subprocess.TimeoutExpired as error:
        return {
            "argv": argv, "exit": None,
            "stdout": (error.stdout or b"").decode("utf-8", "replace") if isinstance(error.stdout, bytes) else (error.stdout or ""),
            "stderr": (error.stderr or b"").decode("utf-8", "replace") if isinstance(error.stderr, bytes) else (error.stderr or ""),
            "seconds": time.monotonic() - started, "error": "timeout",
        }
    except Exception as error:
        return {
            "argv": argv, "exit": None, "stdout": "", "stderr": "",
            "seconds": time.monotonic() - started,
            "error": f"{type(error).__name__}: {error}",
        }


def parse_diagnostics(run: dict[str, Any]) -> tuple[list[dict[str, Any]], str]:
    try:
        parsed = json.loads(run["stdout"] or "[]")
        if not isinstance(parsed, list):
            raise TypeError("Ruff JSON output is not a list")
        diagnostics = []
        for item in parsed:
            location = item.get("location") or {}
            end = item.get("end_location") or {}
            diagnostics.append({
                "code": item.get("code") or "invalid-syntax",
                "message": item.get("message", ""),
                "row": location.get("row"), "column": location.get("column"),
                "end_row": end.get("row"), "end_column": end.get("column"),
                "fixable": bool(item.get("fix")),
            })
        return diagnostics, "ok"
    except (ValueError, TypeError, AttributeError) as error:
        return [], f"diagnostics_parse_error: {error}"


def diagnostics_command(path: Path, profile: str) -> list[str]:
    return [str(RUFF), "check", "--isolated", "--no-cache", *PROFILES[profile],
            "--output-format", "json", str(path)]


def run_job(job: dict[str, Any]) -> dict[str, Any]:
    source = Path(job["source_abs"])
    profile = job["ruff_profile"]
    mode = job["ruff_mode"]
    dest = Path(job["output_abs"])
    dest.parent.mkdir(parents=True, exist_ok=True)
    operations = []
    try:
        if mode == "check":
            dest = source
        else:
            shutil.copyfile(source, dest)
            if mode in ("fix", "fix_format"):
                fix_cmd = [str(RUFF), "check", "--isolated", "--no-cache", *PROFILES[profile], "--fix", str(dest)]
                operations.append({"stage": "fix", **run_command(fix_cmd)})
            if mode in ("format", "fix_format"):
                fmt_cmd = [str(RUFF), "format", "--isolated", "--no-cache", str(dest)]
                operations.append({"stage": "format", **run_command(fmt_cmd)})
        check_run = run_command(diagnostics_command(dest, profile))
        diagnostics, diagnostic_status = parse_diagnostics(check_run)
        code = dest.read_text(encoding="utf-8")
        parses, parse_error = parse_code(code)
        result = {
            **job, "path": str(dest.relative_to(OUT)), "code_sha256": sha(dest),
            "changed": dest.read_bytes() != source.read_bytes(), "parses": parses,
            "parse_error": parse_error, "operations": operations,
            "diagnostic_command": check_run, "diagnostics": diagnostics,
            "diagnostic_status": diagnostic_status,
            "status": "ok" if diagnostic_status == "ok" and check_run["error"] != "timeout" else "error",
        }
        return result
    except Exception as error:
        return {
            **job, "path": str(dest.relative_to(OUT)) if dest.is_absolute() and dest.exists() else "",
            "code_sha256": sha(dest) if dest.exists() else "", "changed": "", "parses": "",
            "parse_error": "", "operations": operations, "diagnostic_command": {},
            "diagnostics": [], "diagnostic_status": "error", "status": "error",
            "error_type": type(error).__name__, "error": str(error),
        }


def detect_result(path: Path) -> dict[str, Any]:
    try:
        result = detect(path.read_text(encoding="utf-8"), "python", EXPERIMENT_KEY)
        return {"status": "ok", **result}
    except Exception as error:
        return {"status": "error", "error_type": type(error).__name__, "error": str(error)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, help="optional pilot limit; production run omits this")
    args = parser.parse_args()

    stage1 = read_jsonl(OUT / "artifacts_stage1.jsonl")
    if args.limit is not None:
        selected_ids = {row["sample_id"] for row in stage1[: args.limit]}
        stage1 = [row for row in stage1 if row["sample_id"] in selected_ids]
    sources = [row for row in stage1 if row["stage"] in ("base", "marked")]
    jobs: list[dict[str, Any]] = []
    artifact_errors: list[dict[str, Any]] = []
    for source in sources:
        sample_id = source["sample_id"]
        variant = source["variant"]
        for profile in PROFILES:
            for mode in MODES:
                artifact_id = f"{sample_id}|ruff|{variant}|{profile}|{mode}"
                source_path = OUT / source["path"]
                output_path = source_path.parent / "ruff" / variant / profile / f"{mode}.py"
                jobs.append({
                    "artifact_id": artifact_id, "dataset": source["dataset"],
                    "sample_id": sample_id, "problem_id": source["problem_id"],
                    "sample_index": source["sample_index"], "stage": "ruff",
                    "variant": variant, "ruff_profile": profile, "ruff_mode": mode,
                    "source_path": source["path"], "source_abs": str(source_path),
                    "output_abs": str(output_path), "source_code_sha256": source["code_sha256"],
                    "sloc": source.get("sloc"),
                })

    # Preserve an explicit status for samples without an eligible SEW artifact.
    marking = []
    with (OUT / "01_marking.csv").open(encoding="utf-8") as stream:
        marking = list(csv.DictReader(stream))
    have_sew = {row["sample_id"] for row in sources if row["variant"] == "sew"}
    have_variant = {(row["sample_id"], row["variant"]) for row in sources}
    for row in marking:
        sample_id = f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}"
        if row["variant"] in ("acw_notab", "acw_full") and (sample_id, row["variant"]) not in have_variant:
            for profile in PROFILES:
                for mode in MODES:
                    artifact_errors.append({
                        "artifact_id": f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}|ruff|{row['variant']}|{profile}|{mode}",
                        "dataset": row["dataset"], "sample_id": sample_id,
                        "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                        "stage": "ruff", "variant": row["variant"], "ruff_profile": profile,
                        "ruff_mode": mode, "status": "not_run",
                        "error_type": row["error_type"] or "blocked_external_api",
                        "error": row["error"] or "ACW artifact unavailable because Sourcery API access was rejected",
                    })
        if row["variant"] == "sew" and sample_id not in have_sew:
            for profile in PROFILES:
                for mode in MODES:
                    artifact_errors.append({
                        "artifact_id": f"{sample_id}|ruff|sew|{profile}|{mode}",
                        "dataset": row["dataset"], "sample_id": sample_id,
                        "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                        "stage": "ruff", "variant": "sew", "ruff_profile": profile,
                        "ruff_mode": mode, "status": "not_run",
                        "error_type": row["error_type"], "error": row["error"],
                    })
    base_samples = {row["sample_id"] for row in sources if row["variant"] == "original"}
    if len(base_samples) != len({row["sample_id"] for row in stage1 if row["stage"] == "base"}):
        raise ValueError("A base input artifact is missing from the stage-one ledger")

    results = []
    operations = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(run_job, job) for job in jobs]
        for index, future in enumerate(as_completed(futures), start=1):
            row = future.result()
            results.append(row)
            for operation in row.get("operations", []):
                operations.append({"artifact_id": row["artifact_id"], **operation})
            if index % 1000 == 0:
                print(f"ruff artifacts {index}/{len(jobs)}", flush=True)
    results.sort(key=lambda row: row["artifact_id"])

    # ACW detection is a fixed-point check: reapply ACW to each distinct Ruff output.
    acw_inputs: dict[tuple[str, str], dict[str, Any]] = {}
    for row in results:
        if not row["variant"].startswith("acw"):
            continue
        path = OUT / row["path"] if row.get("path") else None
        if path is None or not path.is_file():
            continue
        digest = sha(path)
        key = row["variant"], digest
        if key not in acw_inputs:
            acw_inputs[key] = {
                "sample_id": f"{row['variant']}:{digest}", "dataset": row["dataset"],
                "problem_id": row["problem_id"], "sample_index": row["sample_index"],
                "variant": row["variant"], "arm": "ruff", "source_code": path.read_text(encoding="utf-8"),
                "source_path": row["path"], "code_sha256": digest,
            }
    acw_detected, acw_operations = execute_batches(list(acw_inputs.values()), "detect_after_ruff")
    acw_detection: dict[tuple[str, str], dict[str, Any]] = {}
    for item in acw_detected:
        key = item["variant"], item["code_sha256"]
        positive = item["source_code"] == item["output_code"]
        acw_detection[key] = {
            "status": "ok" if item["applied"] else "error",
            "verdict": "Watermark detected" if positive else "No watermark evidence",
            "positive": positive if item["applied"] else "",
            "reason": "fixed_point_check", "error_type": item["error_type"], "error": item["error"],
        }
    write_jsonl(OUT / "acw_post_ruff_detection.jsonl", [
        {"variant": variant, "code_sha256": digest, **acw_detection.get((variant, digest), {})}
        for variant, digest in sorted(acw_inputs)
    ])
    write_jsonl(OUT / "acw_post_ruff_operations.jsonl", acw_operations)

    ruff_summary = []
    ruff_details = []
    detection_rows = []
    stage2_artifacts = []
    for row in results:
        counts = Counter(item["code"] for item in row["diagnostics"])
        ruff_summary.append({
            "artifact_id": row["artifact_id"], "dataset": row["dataset"],
            "sample_id": row["sample_id"], "problem_id": row["problem_id"],
            "sample_index": row["sample_index"], "stage": "ruff", "variant": row["variant"],
            "ruff_profile": row["ruff_profile"], "ruff_mode": row["ruff_mode"],
            "status": row["status"], "exit": row.get("diagnostic_command", {}).get("exit"),
            "diagnostic_count": len(row["diagnostics"]),
            "diagnostic_codes": json.dumps(dict(sorted(counts.items())), sort_keys=True),
            "path": row.get("path", ""), "code_sha256": row.get("code_sha256", ""),
            "changed": row.get("changed", ""), "parses": row.get("parses", ""),
            "diagnostic_status": row.get("diagnostic_status", ""),
        })
        for diagnostic in row["diagnostics"]:
            ruff_details.append({"artifact_id": row["artifact_id"], **diagnostic})
        output_path = OUT / row["path"] if row.get("path") else None
        if row["variant"] == "sew" and output_path and output_path.is_file():
            detector = detect_result(output_path)
            detector_name = "SEW"
        elif row["variant"].startswith("acw") and output_path and output_path.is_file():
            detector = acw_detection.get((row["variant"], row["code_sha256"]), {
                "status": "error", "error_type": "acw_detection_missing", "error": "ACW fixed-point result missing"
            })
            detector_name = "ACW_fixed_point"
        elif row["variant"] == "original":
            detector = {"status": "not_applicable", "verdict": "", "positive": "", "reason": "original artifact"}
            detector_name = ""
        else:
            detector = {"status": "error", "error_type": "artifact_missing", "error": "Ruff output artifact missing"}
            detector_name = ""
        detection_rows.append({
            "artifact_id": row["artifact_id"], "dataset": row["dataset"],
            "problem_id": row["problem_id"], "sample_index": row["sample_index"],
            "variant": row["variant"], "detector": detector_name, "ruff_profile": row["ruff_profile"],
            "ruff_mode": row["ruff_mode"], "status": detector.get("status"),
            "verdict": detector.get("verdict", ""),
            "positive": detector.get("positive", detector.get("verdict") == "Watermark detected"),
            "reason": detector.get("reason", ""), "p": detector.get("p", ""),
            "n_sites": detector.get("n_sites", ""), "n_grades": detector.get("n_grades", ""),
            "error_type": detector.get("error_type", ""), "error": detector.get("error", ""),
        })
        stage2_artifacts.append({
            "artifact_id": row["artifact_id"], "dataset": row["dataset"],
            "sample_id": row["sample_id"], "problem_id": row["problem_id"],
            "sample_index": row["sample_index"], "stage": "ruff", "variant": row["variant"],
            "ruff_profile": row["ruff_profile"], "ruff_mode": row["ruff_mode"],
            "path": row.get("path", ""), "source_code_sha256": row["source_code_sha256"],
            "code_sha256": row.get("code_sha256", ""), "changed": row.get("changed", ""),
            "parses": row.get("parses", ""), "parse_error": row.get("parse_error", ""),
            "sloc": row.get("sloc"), "status": row["status"],
        })

    OUT.mkdir(parents=True, exist_ok=True)
    write_jsonl(OUT / "ruff_artifacts.jsonl", stage2_artifacts)
    write_jsonl(OUT / "ruff_runs.jsonl", results)
    write_jsonl(OUT / "ruff_operations.jsonl", operations)
    write_csv(OUT / "ruff_check_summary.csv", ruff_summary, (
        "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "stage", "variant",
        "ruff_profile", "ruff_mode", "status", "exit", "diagnostic_count", "diagnostic_codes",
        "path", "code_sha256", "changed", "parses", "diagnostic_status",
    ))
    write_csv(OUT / "ruff_diagnostics.csv", ruff_details, (
        "artifact_id", "code", "message", "row", "column", "end_row", "end_column", "fixable",
    ))
    write_csv(OUT / "02_detection_after_ruff.csv", detection_rows, (
        "artifact_id", "dataset", "problem_id", "sample_index", "variant", "detector", "ruff_profile",
        "ruff_mode", "status", "verdict", "positive", "reason", "p", "n_sites", "n_grades",
        "error_type", "error",
    ))
    write_csv(OUT / "ruff_stage_status.csv", artifact_errors, (
        "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "stage", "variant",
        "ruff_profile", "ruff_mode", "status", "error_type", "error",
    ))

    all_artifacts = stage1 + stage2_artifacts
    write_jsonl(OUT / "artifacts_all.jsonl", all_artifacts)
    (OUT / "stage2_environment.json").write_text(json.dumps({
        "ruff_version": "0.17.5",
        "profiles": {
            "default": {"isolated": True, "select": ["E4", "E7", "E9", "F"], "ignore": []},
            "strict": {"isolated": True, "select": ["E", "F", "W", "I", "B", "UP", "SIM"], "ignore": []},
        },
        "modes": {"check": "diagnostics only", "fix": "ruff check --fix", "format": "ruff format", "fix_format": "ruff check --fix then ruff format"},
        "workers": args.workers,
        "per_command_timeout_seconds": TIME_LIMIT_SECONDS,
        "acw_status": "ACW fixed-point detection runs on distinct Ruff output hashes",
        "acw_post_ruff_distinct_inputs": len(acw_inputs),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
