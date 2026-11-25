#!/usr/bin/env python3
"""Embed SEW watermarks into a Python file or directory of files."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from operation_utils import (add_io_arguments, copy_file, output_path, progress,
                             python_files, relative_path, setup_sew, write_report)  # noqa: E402

sew = setup_sew()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_io_arguments(parser)
    parser.add_argument("--language", default="python")
    parser.add_argument("--key", default=sew.EXPERIMENT_KEY.hex(), help="Watermark key in hex")
    parser.add_argument("--report", type=Path, help="Optional JSONL status report")
    args = parser.parse_args()
    key = bytes.fromhex(args.key)
    files = python_files(args.input)
    rows = []
    report = args.report or (args.output / "watermark_report.jsonl")
    with tempfile.TemporaryDirectory(prefix="sew-watermark-") as directory:
        for index, source in enumerate(files, 1):
            target = output_path(source, args.input, args.output)
            staged = Path(directory) / relative_path(source, args.input)
            staged.parent.mkdir(parents=True, exist_ok=True)
            original = source.read_text(encoding="utf-8")
            try:
                result = sew.embed(original, args.language, key)
                code = result["code"]
                if result["status"] != "ok":
                    print(f"ERROR {source}: {result['status']}", file=sys.stderr)
                rows.append({"input": str(source), "output": str(target), "status": result["status"],
                             "changed": code != original, "n_sites": result.get("n_sites"),
                             "n_edits": result.get("n_edits")})
            except Exception as error:
                code = original
                rows.append({"input": str(source), "output": str(target), "status": "error",
                             "error": f"{type(error).__name__}: {error}"})
                print(f"ERROR {source}: {type(error).__name__}: {error}", file=sys.stderr)
            staged.write_text(code, encoding="utf-8", newline="")
            copy_file(staged, target)
            write_report(report, rows)
            progress(index, len(files))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
