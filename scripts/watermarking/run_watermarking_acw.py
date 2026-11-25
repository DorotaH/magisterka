#!/usr/bin/env python3
"""Apply the ACW repository's rules to Python files."""

import argparse
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from operation_utils import (add_io_arguments, apply_acw_files, copy_file, output_path,
                             python_files, relative_path, write_report)  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    add_io_arguments(parser)
    parser.add_argument("--variant", choices=("acw_notab", "acw_full"), default="acw_notab")
    parser.add_argument("--report", type=Path, help="Optional JSONL status report")
    parser.add_argument("--batch-size", type=int, default=50,
                        help="Files passed together to each Sourcery rule (default: 50).")
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")

    files = python_files(args.input)
    report = args.report or (args.output / "watermark_report.jsonl")
    rows = []
    with tempfile.TemporaryDirectory(prefix="acw-watermark-") as directory:
        for start in range(0, len(files), args.batch_size):
            sources = files[start:start + args.batch_size]
            staged_files = []
            targets = []
            for source in sources:
                target = output_path(source, args.input, args.output)
                staged = Path(directory) / relative_path(source, args.input)
                copy_file(source, staged)
                staged_files.append(staged)
                targets.append(target)

            batch_rows = apply_acw_files(staged_files, args.variant, args.batch_size)
            for row, source, staged, target in zip(
                batch_rows, sources, staged_files, targets, strict=True
            ):
                copy_file(staged, target)
                row["input"] = str(source)
                row["output"] = str(target)
                row["variant"] = args.variant
                row["changed"] = source.read_bytes() != target.read_bytes()
                rows.append(row)
            write_report(report, rows)
            completed = len(rows)
            print(f"{completed}/{len(files)} próbek przetworzono")

    if any(row["status"] != "ok" for row in rows):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
