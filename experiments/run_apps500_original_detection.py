#!/usr/bin/env python3
"""Recreate detector controls for the unmarked APPS Qwen/Llama originals.

This script reads the saved original.py artifacts, never edits them, runs the
local SEW detector, and reapplies ACW through the configured Sourcery pipeline.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "SEW"))

from sew import EXPERIMENT_KEY, detect  # noqa: E402
from run_apps500_acw import OUT, execute_batches  # noqa: E402


FIELDS = (
    "dataset", "problem_id", "sample_index", "variant", "detector", "status",
    "verdict", "positive", "reason", "p", "n_sites", "n_grades", "code_sha256",
    "error_type", "error",
)


def read_marking_keys() -> list[tuple[str, str, str]]:
    with (OUT / "01_marking.csv").open(newline="", encoding="utf-8") as stream:
        return sorted({
            (row["dataset"], row["problem_id"], row["sample_index"])
            for row in csv.DictReader(stream)
        })


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path,
                        default=ROOT / "results/apps500_quality/source_data/original_code",
                        help="folder containing <dataset>/<problem_id>/<sample_index>/original.py")
    parser.add_argument("--output", type=Path,
                        default=ROOT / "results/apps500_quality/source_data/original_detection.csv")
    args = parser.parse_args()

    sew_rows: list[dict[str, Any]] = []
    acw_entries: list[dict[str, Any]] = []
    for dataset, problem_id, sample_index in read_marking_keys():
        path = args.source_dir / dataset / problem_id / sample_index / "original.py"
        try:
            code = path.read_text(encoding="utf-8")
            digest = hashlib.sha256(code.encode("utf-8")).hexdigest()
        except Exception as error:
            for variant, detector_name in (("sew", "SEW"), ("acw_notab", "ACW_fixed_point"),
                                           ("acw_full", "ACW_fixed_point")):
                sew_rows.append({
                    "dataset": dataset, "problem_id": problem_id, "sample_index": sample_index,
                    "variant": variant, "detector": detector_name, "status": "error",
                    "verdict": "", "positive": "", "reason": "original_unavailable",
                    "code_sha256": "", "error_type": type(error).__name__, "error": str(error),
                })
            continue

        try:
            result = detect(code, "python", EXPERIMENT_KEY)
            positive = result.get("verdict") == "Watermark detected"
            sew_rows.append({
                "dataset": dataset, "problem_id": problem_id, "sample_index": sample_index,
                "variant": "sew", "detector": "SEW", "status": "ok",
                "verdict": result.get("verdict", ""),
                "positive": int(positive), "reason": result.get("reason", ""),
                "p": result.get("p", ""), "n_sites": result.get("n_sites", ""),
                "n_grades": result.get("n_grades", ""), "code_sha256": digest,
                "error_type": "", "error": "",
            })
        except Exception as error:
            sew_rows.append({
                "dataset": dataset, "problem_id": problem_id, "sample_index": sample_index,
                "variant": "sew", "detector": "SEW", "status": "error",
                "verdict": "", "positive": "", "reason": "", "code_sha256": digest,
                "error_type": type(error).__name__, "error": str(error),
            })

        for variant in ("acw_notab", "acw_full"):
            acw_entries.append({
                "sample_id": f"original:{dataset}:{problem_id}:{sample_index}:{variant}",
                "dataset": dataset, "problem_id": problem_id, "sample_index": sample_index,
                "variant": variant, "arm": "original_control", "source_code": code,
                "source_path": str(path), "code_sha256": digest,
            })

    # ACW's detector is the fixed-point check: reapplying that ACW variant must
    # leave the original code unchanged. Failed applications remain explicit.
    acw_results, _operations = execute_batches(acw_entries, "original_control")
    for item in acw_results:
        positive = item["source_code"] == item["output_code"]
        applied = bool(item.get("applied"))
        sew_rows.append({
            "dataset": item["dataset"], "problem_id": item["problem_id"],
            "sample_index": item["sample_index"], "variant": item["variant"],
            "detector": "ACW_fixed_point", "status": "ok" if applied else "error",
            "verdict": ("Watermark detected" if positive else "No watermark evidence") if applied else "",
            "positive": int(positive) if applied else "", "reason": "fixed_point_check",
            "code_sha256": item.get("code_sha256", ""), "error_type": item.get("error_type", ""),
            "error": item.get("error", ""),
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sew_rows.sort(key=lambda row: (row["dataset"], int(row["problem_id"]),
                                  int(row["sample_index"]), row["variant"]))
    with args.output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(sew_rows)
    print(f"Saved {len(sew_rows)} original-code detector rows to {args.output}")
    print("Regenerate the workbook with: python3 experiments/export_apps500_detection_excel.py")


if __name__ == "__main__":
    main()
