#!/usr/bin/env python3
"""Detect ACW by checking whether its repository rules leave a fixed point."""

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from operation_utils import add_io_arguments, apply_acw_files, python_files, write_report  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_io_arguments(parser, "JSONL report path")
    parser.add_argument("--variant", choices=("acw_notab", "acw_full"), default="acw_notab")
    parser.add_argument("--batch-size", type=int, default=1500,
                        help="Files passed together to each Sourcery rule (default: 1500).")
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error("--batch-size must be at least 1")

    sources = python_files(args.input)
    rows = []
    with tempfile.TemporaryDirectory(prefix="acw-detect-") as directory:
        candidates = []
        originals = []
        for source in sources:
            relative = source.name if args.input.is_file() else source.relative_to(args.input.resolve())
            candidate = Path(directory) / relative
            candidate.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, candidate)
            candidates.append(candidate)
            originals.append(source.read_bytes())
        statuses = apply_acw_files(candidates, args.variant, args.batch_size)
        for source, candidate, original, result in zip(
            sources, candidates, originals, statuses, strict=True
        ):
            if result["status"] != "ok":
                rows.append({"input": str(source), "variant": args.variant,
                             "status": "error", "errors": result["errors"]})
                continue
            positive = candidate.read_bytes() == original
            rows.append({"input": str(source), "variant": args.variant,
                         "status": "ok", "positive": int(positive)})
    write_report(args.output, rows)
    if any(row["status"] != "ok" for row in rows):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
