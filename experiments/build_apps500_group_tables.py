#!/usr/bin/env python3
"""Join APPS 500 Ruff and detection records to the prepared SLOC groups."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "watermark-results" / "apps500_quality"
GROUP_TYPES = ("fixed", "common_quantile", "dataset_quantile")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    groups: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in read_csv(OUT / "00_groups.csv"):
        key = row["dataset"], row["problem_id"], row["sample_index"]
        groups.setdefault(key, {})[row["group_type"]] = row["group"]

    # Detection records by artifact and all three requested group schemes.
    detection_records: list[dict[str, Any]] = []
    sources = [
        ("sew_marked", OUT / "01_sew_detection.csv", "method"),
        ("main_marking", OUT / "01_marking.csv", "variant"),
        ("fmt_first", OUT / "01_fmt_first.csv", "variant"),
    ]
    for arm_label, path, method_key in sources:
        for row in read_csv(path):
            key = row["dataset"], row["problem_id"], row["sample_index"]
            for group_type in GROUP_TYPES:
                if group_type not in groups.get(key, {}):
                    continue
                detection_records.append({
                    "dataset": row["dataset"], "problem_id": row["problem_id"],
                    "sample_index": row["sample_index"], "record_source": arm_label,
                    "arm": row.get("arm", ""),
                    "method": row.get(method_key, ""), "group_type": group_type,
                    "group": groups[key][group_type], "sloc": row.get("sloc", ""),
                    "applied": row.get("applied", ""), "parses": row.get("parses", ""),
                    "changed": row.get("changed", ""),
                    "detection_status": row.get("status", row.get("detection_status", "")),
                    "verdict": row.get("verdict", row.get("detection_verdict", "")),
                    "positive": row.get("positive", row.get("detection_positive", "")),
                    "reason": row.get("reason", ""), "p": row.get("p", ""),
                    "error_type": row.get("error_type", ""), "error": row.get("error", ""),
                })
    write_csv(OUT / "detection_by_sloc_group.csv", detection_records, [
        "dataset", "problem_id", "sample_index", "record_source", "arm", "method",
        "group_type", "group", "sloc", "applied", "parses", "changed", "detection_status",
        "verdict", "positive", "reason", "p", "error_type", "error",
    ])

    # Ruff summaries (including fmt_first) plus explicit statuses where no code was available.
    ruff_records: list[dict[str, Any]] = []
    ruff_sources = [
        ("main", read_csv(OUT / "ruff_check_summary.csv")),
        ("fmt_first", read_csv(OUT / "ruff_fmt_first_summary.csv")),
    ]
    for source_name, rows in ruff_sources:
        for row in rows:
            key = row["dataset"], row["problem_id"], row["sample_index"]
            for group_type in GROUP_TYPES:
                if group_type not in groups.get(key, {}):
                    continue
                ruff_records.append({**row, "record_source": source_name, "group_type": group_type,
                                     "group": groups[key][group_type]})
    for row in read_csv(OUT / "ruff_stage_status.csv"):
        key = row["dataset"], row["problem_id"], row["sample_index"]
        for group_type in GROUP_TYPES:
            if group_type not in groups.get(key, {}):
                continue
            ruff_records.append({
                **row, "record_source": row["stage"], "group_type": group_type,
                "group": groups[key][group_type], "diagnostic_count": "",
                "diagnostic_codes": "", "exit": "", "path": "", "code_sha256": "",
            })
    write_csv(OUT / "ruff_by_sloc_group.csv", ruff_records, [
        "artifact_id", "dataset", "sample_id", "problem_id", "sample_index", "record_source",
        "stage", "variant", "ruff_profile", "ruff_mode", "group_type", "group", "status",
        "exit", "diagnostic_count", "diagnostic_codes", "path", "code_sha256", "error_type", "error",
    ])


if __name__ == "__main__":
    main()
