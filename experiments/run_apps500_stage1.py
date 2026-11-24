#!/usr/bin/env python3
"""Compute APPS SLOC groups, SEW marking, and the format-first arm."""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import signal
import time
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from radon.raw import analyze
from sew import EXPERIMENT_KEY, detect, embed


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "watermark-results" / "apps500_quality"
INPUT = OUT / "input"
TIME_LIMIT_SECONDS = 120
DATASETS = ("qwen", "llama")
VARIANTS = ("acw_notab", "acw_full", "sew")


@contextmanager
def time_limit(seconds: int):
    if not hasattr(signal, "SIGALRM"):
        yield
        return
    previous = signal.getsignal(signal.SIGALRM)

    def expired(_signum, _frame):
        raise TimeoutError(f"sample time limit exceeded ({seconds}s)")

    signal.signal(signal.SIGALRM, expired)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def digest(text: str | None) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest() if text is not None else ""


def write_csv(path: Path, rows: list[dict[str, Any]], fields: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def sample_id(row: dict[str, Any]) -> str:
    return f"{row['dataset']}:{row['problem_id']}:{row['sample_index']}"


def sample_path(row: dict[str, Any]) -> Path:
    return OUT / "code" / str(row["dataset"]) / str(row["problem_id"]) / str(row["sample_index"])


def parse_status(code: str | None) -> tuple[bool | None, str]:
    if code is None:
        return None, "input_code_missing"
    try:
        ast.parse(code)
        compile(code, "<sample>", "exec")
        return True, ""
    except (SyntaxError, ValueError, TypeError) as error:
        return False, str(error)


def simple_sloc(code: str) -> int:
    return sum(bool(line.strip()) and not line.lstrip().startswith("#") for line in code.splitlines())


def get_sloc(code: str | None) -> tuple[int | None, str, str]:
    if code is None:
        return None, "unavailable_missing_code", "code is null in source row"
    try:
        return int(analyze(code).sloc), "radon.raw.analyze", ""
    except Exception as error:
        try:
            return simple_sloc(code), "simple_nonblank_noncomment_fallback", f"Radon error: {type(error).__name__}: {error}"
        except Exception as fallback_error:
            return None, "unavailable", f"Radon: {error}; fallback: {fallback_error}"


def fixed_group(sloc: int | None) -> str:
    if sloc is None:
        return "sloc_unavailable"
    if sloc < 5:
        return "<5"
    if sloc < 10:
        return "5–10"
    if sloc < 20:
        return "10–20"
    if sloc < 50:
        return "20–50"
    return "50+"


def quantile_partition(values: list[int], requested_groups: int = 5) -> dict[str, Any]:
    counts = Counter(values)
    unique = sorted(counts)
    actual = min(requested_groups, len(unique))
    if not unique:
        return {"requested_groups": requested_groups, "actual_groups": 0, "boundaries": [],
                "intervals": [], "reason": "no SLOC values"}
    if actual < requested_groups:
        reason = f"only {len(unique)} distinct SLOC values; tied values are not split"
    else:
        reason = ""

    # Dynamic programming chooses integer cut points between distinct values,
    # minimizing total absolute deviation from the requested equal-count targets.
    prefix = []
    running = 0
    for value in unique:
        running += counts[value]
        prefix.append(running)
    n = len(values)
    k = actual
    dp: dict[tuple[int, int], tuple[float, tuple[int, ...]]] = {}
    for end in range(1, len(unique) + 1):
        dp[(1, end)] = (abs(prefix[end - 1] - n / k), ())
    for groups in range(2, k + 1):
        for end in range(groups, len(unique) + 1):
            best = None
            for cut in range(groups - 1, end):
                prior = dp.get((groups - 1, cut))
                if prior is None:
                    continue
                target = groups * n / k
                cost = prior[0] + abs(prefix[end - 1] - target)
                cuts = prior[1] + (cut,)
                candidate = (cost, cuts)
                if best is None or candidate < best:
                    best = candidate
            if best is not None:
                dp[(groups, end)] = best
    cuts = dp[(k, len(unique))][1]
    lower_bounds = [unique[0]] + [unique[cut] for cut in cuts]
    upper_bounds = [*lower_bounds[1:], None]
    intervals = [
        {"group": f"Q{i + 1}", "lower_inclusive": low, "upper_exclusive": high,
         "count": sum(counts[v] for v in unique if v >= low and (high is None or v < high))}
        for i, (low, high) in enumerate(zip(lower_bounds, upper_bounds, strict=True))
    ]
    return {
        "requested_groups": requested_groups,
        "actual_groups": actual,
        "boundaries": lower_bounds[1:],
        "intervals": intervals,
        "reason": reason,
    }


def assign_quantile(sloc: int | None, partition: dict[str, Any]) -> str:
    if sloc is None:
        return "sloc_unavailable"
    for interval in partition["intervals"]:
        if sloc >= interval["lower_inclusive"] and (
            interval["upper_exclusive"] is None or sloc < interval["upper_exclusive"]
        ):
            return interval["group"]
    return "sloc_unassigned"


def run_detector(code: str, key: bytes = EXPERIMENT_KEY) -> dict[str, Any]:
    try:
        result = detect(code, "python", key)
        return {"status": "ok", **result}
    except Exception as error:
        return {"status": "error", "error_type": type(error).__name__, "error": str(error)}


def load_samples() -> list[dict[str, Any]]:
    samples = []
    for dataset in DATASETS:
        path = INPUT / f"{dataset}_generations.jsonl"
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                row = json.loads(line)
                row["dataset"] = dataset
                samples.append(row)
    samples.sort(key=lambda row: (row["dataset"], int(row["problem_id"]), int(row["sample_index"])))
    return samples


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, help="optional pilot limit; production run omits this")
    args = parser.parse_args()
    samples = load_samples()
    if args.limit is not None:
        samples = samples[:args.limit]

    sloc_rows = []
    partitions: dict[str, Any] = {}
    fixed_counts: dict[str, Counter[str]] = {name: Counter() for name in DATASETS}
    for row in samples:
        code = row.get("code") if isinstance(row.get("code"), str) else None
        sloc, method, error = get_sloc(code)
        row["_code"] = code
        row["_sloc"] = sloc
        row["_sloc_method"] = method
        row["_sloc_error"] = error
        row["_sample_id"] = sample_id(row)
        fixed = fixed_group(sloc)
        fixed_counts[row["dataset"]][fixed] += 1
        sloc_rows.append({
            "dataset": row["dataset"], "problem_id": row["problem_id"],
            "sample_index": row["sample_index"], "sloc": sloc,
            "count_method": method, "count_error": error,
            "input_code_sha256": digest(code), "source_reported_sloc": row.get("sloc"),
            "input_status": row.get("extraction_status", "ok" if code is not None else "code_missing"),
        })

    pooled = [row["_sloc"] for row in samples if row["_sloc"] is not None]
    partitions["common_qwen_llama"] = quantile_partition(pooled)
    for dataset in DATASETS:
        partitions[dataset] = quantile_partition([
            row["_sloc"] for row in samples if row["dataset"] == dataset and row["_sloc"] is not None
        ])
    OUT.mkdir(parents=True, exist_ok=True)
    write_csv(OUT / "00_sloc.csv", sloc_rows, (
        "dataset", "problem_id", "sample_index", "sloc", "count_method", "count_error",
        "input_code_sha256", "source_reported_sloc", "input_status",
    ))
    group_rows = []
    for row in samples:
        sloc = row["_sloc"]
        group_rows.append({
            "dataset": row["dataset"], "problem_id": row["problem_id"],
            "sample_index": row["sample_index"], "sloc": sloc,
            "group_type": "fixed", "group": fixed_group(sloc),
        })
        group_rows.append({
            "dataset": row["dataset"], "problem_id": row["problem_id"],
            "sample_index": row["sample_index"], "sloc": sloc,
            "group_type": "common_quantile", "group": assign_quantile(sloc, partitions["common_qwen_llama"]),
        })
        group_rows.append({
            "dataset": row["dataset"], "problem_id": row["problem_id"],
            "sample_index": row["sample_index"], "sloc": sloc,
            "group_type": "dataset_quantile", "group": assign_quantile(sloc, partitions[row["dataset"]]),
        })
    write_csv(OUT / "00_groups.csv", group_rows,
              ("dataset", "problem_id", "sample_index", "sloc", "group_type", "group"))
    (OUT / "grupy_rowne.json").write_text(
        json.dumps({
            "method": "SLOC integer cut points selected from distinct values; minimize total absolute deviation from equal-count targets; tied SLOC values are not split",
            "common_boundaries_source": "pooled qwen and llama samples; no between-dataset metrics are calculated",
            "partitions": partitions,
        }, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    detection_rows = []
    marking_rows = []
    fmt_rows = []
    artifacts = []
    for row in samples:
        code = row["_code"]
        sloc = row["_sloc"]
        sid = row["_sample_id"]
        folder = sample_path(row)
        folder.mkdir(parents=True, exist_ok=True)
        original_path = folder / "original.py"
        if code is not None:
            original_path.write_text(code, encoding="utf-8", newline="")
            parses, parse_error = parse_status(code)
            artifacts.append({
                "dataset": row["dataset"], "sample_id": sid, "problem_id": row["problem_id"],
                "sample_index": row["sample_index"], "stage": "base", "variant": "original",
                "ruff_profile": "", "ruff_mode": "", "path": str(original_path.relative_to(OUT)),
                "source_code_sha256": digest(code), "code_sha256": digest(code), "changed": False,
                "parses": parses, "parse_error": parse_error, "sloc": sloc,
            })
        else:
            parses, parse_error = None, "code missing"
        for variant in ("acw_notab", "acw_full"):
            eligible = sloc is not None and sloc >= 5 and code is not None
            marking_rows.append({
                "dataset": row["dataset"], "problem_id": row["problem_id"],
                "sample_index": row["sample_index"], "arm": "main", "variant": variant,
                "sloc": sloc, "applied": False if eligible else "",
                "parses": "", "changed": "", "detection_status": "blocked" if eligible else "",
                "detection_verdict": "", "detection_positive": "", "marking_passed": "",
                "error_type": "blocked_external_api" if eligible else (
                    "input_code_missing" if code is None else "sloc_below_5"
                ),
                "error": "Sourcery API access rejected by automatic review; no code was sent" if eligible else "",
                "output_path": "", "tool_seconds": "",
            })

        # User steered this run to attempt marking at every SLOC size.
        eligible = sloc is not None and code is not None
        if not eligible:
            marking_rows.append({
                "dataset": row["dataset"], "problem_id": row["problem_id"],
                "sample_index": row["sample_index"], "arm": "main", "variant": "sew",
                "sloc": sloc, "applied": False if code is not None else "",
                "parses": parses, "changed": False if code is not None else "",
                "detection_status": "not_run" if code is not None else "error",
                "detection_verdict": "", "detection_positive": "", "marking_passed": "",
                "error_type": "sloc_below_5" if code is not None else "input_code_missing",
                "error": "" if code is not None else "code is null in source row",
                "output_path": "", "tool_seconds": "",
            })
        else:
            start = time.monotonic()
            embedded = None
            try:
                with time_limit(TIME_LIMIT_SECONDS):
                    embedded = embed(code, "python", EXPERIMENT_KEY)
                tool_seconds = time.monotonic() - start
                marked_code = embedded.pop("code")
                if isinstance(marked_code, bytes):
                    marked_code = marked_code.decode("utf-8", "replace")
                marked_path = folder / "sew.py"
                marked_path.write_text(marked_code, encoding="utf-8", newline="")
                parses_marked, parse_error_marked = parse_status(marked_code)
                changed = marked_code != code
                detector = run_detector(marked_code)
                applied = embedded.get("status") == "ok"
                positive = detector.get("verdict") == "Watermark detected"
                error_type = ""
                if embedded.get("status") == "abstain:not_converged":
                    error_type = "not_converged"
                elif embedded.get("status") == "abstain:parse":
                    error_type = "input_unparsable"
                elif embedded.get("status") not in ("ok", "abstain:no_sites"):
                    error_type = embedded.get("status", "embedding_error")
                marking_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "arm": "main", "variant": "sew",
                    "sloc": sloc, "applied": applied, "parses": parses_marked,
                    "changed": changed, "detection_status": detector.get("status"),
                    "detection_verdict": detector.get("verdict"), "detection_positive": positive,
                    "marking_passed": bool(applied and parses_marked and positive),
                    "error_type": error_type or ("post_embedding_syntax_error" if parses_marked is False else ""),
                    "error": parse_error_marked or detector.get("error", ""),
                    "output_path": str(marked_path.relative_to(OUT)), "tool_seconds": tool_seconds,
                    "embed_status": embedded.get("status"), "n_sites": embedded.get("n_sites"),
                    "n_grades": embedded.get("n_grades"), "n_edits": embedded.get("n_edits"),
                    "iterations": embedded.get("iterations"),
                })
                detection_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "method": "sew", "arm": "main_marked",
                    "status": detector.get("status"), "verdict": detector.get("verdict"),
                    "positive": positive, "reason": detector.get("reason", ""),
                    "p": detector.get("p"), "n_sites": detector.get("n_sites"),
                    "n_grades": detector.get("n_grades"), "error": detector.get("error", ""),
                })
                artifacts.append({
                    "dataset": row["dataset"], "sample_id": sid, "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "stage": "marked", "variant": "sew",
                    "ruff_profile": "", "ruff_mode": "", "path": str(marked_path.relative_to(OUT)),
                    "source_code_sha256": digest(code), "code_sha256": digest(marked_code),
                    "changed": changed, "parses": parses_marked, "parse_error": parse_error_marked,
                    "sloc": sloc,
                })
            except TimeoutError as error:
                tool_seconds = time.monotonic() - start
                marking_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "arm": "main", "variant": "sew",
                    "sloc": sloc, "applied": False, "parses": "", "changed": "",
                    "detection_status": "not_run", "detection_verdict": "",
                    "detection_positive": "", "marking_passed": False,
                    "error_type": "timeout", "error": str(error), "output_path": "",
                    "tool_seconds": tool_seconds,
                })
            except Exception as error:
                tool_seconds = time.monotonic() - start
                marking_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "arm": "main", "variant": "sew",
                    "sloc": sloc, "applied": False, "parses": "", "changed": "",
                    "detection_status": "not_run", "detection_verdict": "",
                    "detection_positive": "", "marking_passed": False,
                    "error_type": type(error).__name__, "error": str(error), "output_path": "",
                    "tool_seconds": tool_seconds,
                })

        if eligible:
            fmt_dir = folder / "fmt_first"
            fmt_dir.mkdir(parents=True, exist_ok=True)
            formatted_path = fmt_dir / "original_formatted.py"
            formatted_path.write_text(code, encoding="utf-8", newline="")
            command = [str(ROOT / "ACW/.tools/local/bin/ruff"), "format", "--isolated", "--no-cache", str(formatted_path)]
            start = time.monotonic()
            try:
                import subprocess

                result = subprocess.run(command, capture_output=True, text=True, timeout=TIME_LIMIT_SECONDS)
                formatted_code = formatted_path.read_text(encoding="utf-8")
                formatted_parses, formatted_parse_error = parse_status(formatted_code)
                format_status = "ok" if result.returncode == 0 else "error"
                format_error = result.stderr.strip()
                format_seconds = time.monotonic() - start
                fmt_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "arm": "fmt_first",
                    "variant": "original_formatted", "applied": result.returncode == 0,
                    "parses": formatted_parses, "changed": formatted_code != code,
                    "detection_status": "not_applicable", "detection_verdict": "",
                    "detection_positive": "", "marking_passed": "",
                    "error_type": "" if result.returncode == 0 else "ruff_format_error",
                    "error": format_error or formatted_parse_error,
                    "input_path": str(original_path.relative_to(OUT)),
                    "output_path": str(formatted_path.relative_to(OUT)),
                    "command": json.dumps(command), "tool_seconds": format_seconds,
                })
                artifacts.append({
                    "dataset": row["dataset"], "sample_id": sid, "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "stage": "fmt_first", "variant": "original_formatted",
                    "ruff_profile": "", "ruff_mode": "", "path": str(formatted_path.relative_to(OUT)),
                    "source_code_sha256": digest(code), "code_sha256": digest(formatted_code),
                    "changed": formatted_code != code, "parses": formatted_parses,
                    "parse_error": formatted_parse_error, "sloc": sloc,
                })
                if format_status == "ok":
                    for blocked_variant in ("acw_notab", "acw_full"):
                        fmt_rows.append({
                            "dataset": row["dataset"], "problem_id": row["problem_id"],
                            "sample_index": row["sample_index"], "arm": "fmt_first",
                            "variant": blocked_variant, "applied": False, "parses": "",
                            "changed": "", "detection_status": "blocked",
                            "detection_verdict": "", "detection_positive": "",
                            "marking_passed": "", "error_type": "blocked_external_api",
                            "error": "Sourcery API access rejected by automatic review; no code was sent",
                            "input_path": str(formatted_path.relative_to(OUT)), "output_path": "",
                            "command": "", "tool_seconds": "",
                        })
                    start = time.monotonic()
                    with time_limit(TIME_LIMIT_SECONDS):
                        fmt_embedded = embed(formatted_code, "python", EXPERIMENT_KEY)
                    fmt_marked = fmt_embedded.pop("code")
                    if isinstance(fmt_marked, bytes):
                        fmt_marked = fmt_marked.decode("utf-8", "replace")
                    sew_path = fmt_dir / "sew.py"
                    sew_path.write_text(fmt_marked, encoding="utf-8", newline="")
                    fmt_parses, fmt_parse_error = parse_status(fmt_marked)
                    fmt_detect = run_detector(fmt_marked)
                    fmt_applied = fmt_embedded.get("status") == "ok"
                    fmt_positive = fmt_detect.get("verdict") == "Watermark detected"
                    fmt_error_type = ""
                    if fmt_embedded.get("status") == "abstain:not_converged":
                        fmt_error_type = "not_converged"
                    elif fmt_embedded.get("status") == "abstain:parse":
                        fmt_error_type = "input_unparsable"
                    fmt_rows.append({
                        "dataset": row["dataset"], "problem_id": row["problem_id"],
                        "sample_index": row["sample_index"], "arm": "fmt_first",
                        "variant": "sew", "applied": fmt_applied, "parses": fmt_parses,
                        "changed": fmt_marked != formatted_code,
                        "detection_status": fmt_detect.get("status"),
                        "detection_verdict": fmt_detect.get("verdict"),
                        "detection_positive": fmt_positive,
                        "marking_passed": bool(fmt_applied and fmt_parses and fmt_positive),
                        "error_type": fmt_error_type or ("post_embedding_syntax_error" if fmt_parses is False else ""),
                        "error": fmt_parse_error or fmt_detect.get("error", ""),
                        "input_path": str(formatted_path.relative_to(OUT)),
                        "output_path": str(sew_path.relative_to(OUT)),
                        "command": json.dumps(command), "tool_seconds": time.monotonic() - start,
                        "embed_status": fmt_embedded.get("status"),
                    })
                    artifacts.append({
                        "dataset": row["dataset"], "sample_id": sid, "problem_id": row["problem_id"],
                        "sample_index": row["sample_index"], "stage": "fmt_first", "variant": "sew",
                        "ruff_profile": "", "ruff_mode": "", "path": str(sew_path.relative_to(OUT)),
                        "source_code_sha256": digest(formatted_code), "code_sha256": digest(fmt_marked),
                        "changed": fmt_marked != formatted_code, "parses": fmt_parses,
                        "parse_error": fmt_parse_error, "sloc": sloc,
                    })
            except Exception as error:
                fmt_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "arm": "fmt_first",
                    "variant": "original_formatted", "applied": False, "parses": "",
                    "changed": "", "detection_status": "not_run", "detection_verdict": "",
                    "detection_positive": "", "marking_passed": False,
                    "error_type": "timeout" if isinstance(error, TimeoutError) else type(error).__name__,
                    "error": str(error), "input_path": str(original_path.relative_to(OUT)),
                    "output_path": str(formatted_path.relative_to(OUT)),
                    "command": json.dumps(command), "tool_seconds": time.monotonic() - start,
                })
        else:
            for skipped_variant in VARIANTS:
                fmt_rows.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "arm": "fmt_first",
                    "variant": skipped_variant, "applied": False if code is not None else "",
                    "parses": parses, "changed": False if code is not None else "",
                    "detection_status": "not_run", "detection_verdict": "",
                    "detection_positive": "", "marking_passed": "",
                    "error_type": "sloc_below_5" if code is not None else "input_code_missing",
                    "error": "", "input_path": "", "output_path": "", "command": "", "tool_seconds": "",
                })

    write_csv(OUT / "01_sew_detection.csv", detection_rows, (
        "dataset", "problem_id", "sample_index", "method", "arm", "status", "verdict",
        "positive", "reason", "p", "n_sites", "n_grades", "error",
    ))
    write_csv(OUT / "01_marking.csv", marking_rows, (
        "dataset", "problem_id", "sample_index", "arm", "variant", "sloc", "applied",
        "parses", "changed", "detection_status", "detection_verdict", "detection_positive",
        "marking_passed", "error_type", "error", "output_path", "tool_seconds", "embed_status",
        "n_sites", "n_grades", "n_edits", "iterations",
    ))
    write_csv(OUT / "01_fmt_first.csv", fmt_rows, (
        "dataset", "problem_id", "sample_index", "arm", "variant", "applied", "parses",
        "changed", "detection_status", "detection_verdict", "detection_positive", "marking_passed",
        "error_type", "error", "input_path", "output_path", "command", "tool_seconds", "embed_status",
    ))
    write_jsonl(OUT / "artifacts_stage1.jsonl", artifacts)

    filter_rows = []
    for dataset in DATASETS:
        rows = [row for row in samples if row["dataset"] == dataset]
        filter_rows.extend([
            {"dataset": dataset, "stage": "input", "filter": "all_input_rows", "n_rows": len(rows)},
            {"dataset": dataset, "stage": "marking", "filter": "sloc_below_5", "n_rows": sum(row["_sloc"] is not None and row["_sloc"] < 5 for row in rows)},
            {"dataset": dataset, "stage": "input", "filter": "code_missing", "n_rows": sum(row["_code"] is None for row in rows)},
        ])
        for label in ("<5", "5–10", "10–20", "20–50", "50+", "sloc_unavailable"):
            filter_rows.append({
                "dataset": dataset, "stage": "SLOC", "filter": label,
                "n_rows": fixed_counts[dataset][label],
            })
    write_csv(OUT / "00_filter_counts.csv", filter_rows, ("dataset", "stage", "filter", "n_rows"))
    (OUT / "stage1_environment.json").write_text(json.dumps({
        "python": __import__("sys").version,
        "radon_version": __import__("radon").__version__,
        "sew_key_hex": EXPERIMENT_KEY.hex(),
        "sew_alpha": __import__("sew.config", fromlist=["ALPHA"]).ALPHA,
        "sew_min_evidence": __import__("sew.config", fromlist=["MIN_EVIDENCE"]).MIN_EVIDENCE,
        "sample_timeout_seconds": TIME_LIMIT_SECONDS,
        "timeout_basis": "120-second per-command timeout used by main study; SEW pilot completed below one second",
        "sample_rows_processed": len(samples),
        "acw_status": "blocked_external_api; Sourcery code transmission was rejected by automatic review",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
