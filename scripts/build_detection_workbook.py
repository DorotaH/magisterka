#!/usr/bin/env python3
"""Build an Excel workbook from per-sample SEW/ACW detection reports.

Expected input layout under --results-dir:
  llama/<column>.jsonl
  qwen/<column>.jsonl

Each report is the JSONL output of a detection script and must contain input
(ending in llama_N.py or qwen_N.py) and positive (0 or 1) for every sample.
When a problem has multiple generations, its cell is 1 if a majority were
detected, otherwise 0.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


ROOT = Path(__file__).resolve().parents[1]
MODELS = ("llama", "qwen")
COLUMNS = (
    ("kod", "kod"),
    ("kod_po_acw", "kod po ACW"),
    ("kod_po_sew", "kod po SEW"),
    ("ruff_bazowy", "Ruff format bazowy"),
    ("ruff_rygorystyczny", "Ruff format rygorystyczny"),
    ("acw_bez_tab", "ACW bez reguły z tab"),
)


def read_problem_ids(path: Path) -> list[object]:
    ids: list[object] = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {error}") from error
            if row.get("status", "ok") != "ok":
                raise ValueError(f"{path}:{line_number}: detection failed for {row.get('input')}")
            if "problem_id" not in record:
                raise ValueError(f"{path}:{line_number}: missing problem_id")
            ids.append(record["problem_id"])
    return ids


def read_report(path: Path, model: str, sample_count: int) -> list[int]:
    values: list[int | None] = [None] * sample_count
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{path}:{line_number}: invalid JSON: {error}") from error
            match = re.search(rf"(?:^|/){model}_(\d+)\.py$", str(row.get("input", "")))
            if not match:
                raise ValueError(f"{path}:{line_number}: input must end in {model}_N.py")
            index = int(match.group(1)) - 1
            if index < 0 or index >= sample_count:
                raise ValueError(f"{path}:{line_number}: sample index is out of range")
            if values[index] is not None:
                raise ValueError(f"{path}:{line_number}: duplicate sample {model}_{index + 1}.py")
            positive = row.get("positive")
            if positive not in (0, 1, False, True):
                raise ValueError(f"{path}:{line_number}: missing binary positive value")
            values[index] = int(positive)

    missing = [i + 1 for i, value in enumerate(values) if value is None]
    if missing:
        preview = ", ".join(map(str, missing[:8]))
        suffix = "…" if len(missing) > 8 else ""
        raise ValueError(f"{path}: missing {len(missing)} samples: {preview}{suffix}")
    return [int(value) for value in values]


def majority_by_problem(problem_ids: list[object], values: list[int]) -> dict[object, int]:
    votes: dict[object, list[int]] = defaultdict(list)
    for problem_id, value in zip(problem_ids, values, strict=True):
        votes[problem_id].append(value)
    return {
        problem_id: int(sum(problem_votes) * 2 >= len(problem_votes) + 1)
        for problem_id, problem_votes in votes.items()
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-root", type=Path, default=ROOT / "source_data",
        help="Directory containing apps500_llama/ and apps500_qwen/.",
    )
    parser.add_argument(
        "--results-dir", type=Path, default=ROOT / "results/detections",
        help="Directory containing <model>/<column>.jsonl detection reports.",
    )
    parser.add_argument(
        "--output", type=Path, default=ROOT / "results/watermark_detection.xlsx",
        help="Path of the Excel workbook to create.",
    )
    args = parser.parse_args()

    workbook = Workbook()
    workbook.remove(workbook.active)
    id_sheet = workbook.create_sheet("problem_id_map")
    id_sheet.append(("model", "row", "problem_id"))
    id_sheet.freeze_panes = "A2"

    header_fill = PatternFill("solid", fgColor="1F4E78")
    for model in MODELS:
        generation_path = args.data_root / f"apps500_{model}" / "generations.jsonl"
        problem_ids = read_problem_ids(generation_path)
        unique_ids = list(dict.fromkeys(problem_ids))
        column_results: dict[str, dict[object, int]] = {}

        for slug, _ in COLUMNS:
            report_path = args.results_dir / model / f"{slug}.jsonl"
            sample_values = read_report(report_path, model, len(problem_ids))
            column_results[slug] = majority_by_problem(problem_ids, sample_values)

        sheet = workbook.create_sheet(model)
        sheet.append(("problem", *(label for _, label in COLUMNS)))
        for cell in sheet[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

        for row_index, problem_id in enumerate(unique_ids, start=1):
            row_label = f"p{row_index}"
            sheet.append((row_label, *(column_results[slug][problem_id] for slug, _ in COLUMNS)))
            id_sheet.append((model, row_label, problem_id))

        sheet.freeze_panes = "B2"
        sheet.auto_filter.ref = sheet.dimensions
        sheet.column_dimensions["A"].width = 14
        for column_index in range(2, len(COLUMNS) + 2):
            sheet.column_dimensions[get_column_letter(column_index)].width = 24
        sheet.row_dimensions[1].height = 34

    id_sheet.column_dimensions["A"].width = 14
    id_sheet.column_dimensions["B"].width = 14
    id_sheet.column_dimensions["C"].width = 18
    args.output.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(args.output)
    print(f"Created {args.output}")


if __name__ == "__main__":
    main()
