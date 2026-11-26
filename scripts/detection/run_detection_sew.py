#!/usr/bin/env python3
"""Detect SEW watermarks in a Python file or directory of files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "SEW"))
sys.path.insert(0, str(ROOT / "scripts"))

from operation_utils import add_io_arguments, progress, python_files, setup_sew, write_report  # noqa: E402

sew = setup_sew()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    add_io_arguments(parser, "JSONL report path")
    parser.add_argument("--language", default="python")
    parser.add_argument("--key", default=sew.EXPERIMENT_KEY.hex(), help="Watermark key in hex")
    args = parser.parse_args()
    key = bytes.fromhex(args.key)
    files = python_files(args.input)
    rows = []
    for index, source in enumerate(files, 1):
        try:
            result = sew.detect(source.read_text(encoding="utf-8"), args.language, key)
            rows.append({"input": str(source), "status": "ok", "positive": int(
                result.get("verdict") == "Watermark detected"), **result})
        except Exception as error:
            rows.append({"input": str(source), "status": "error",
                         "error": f"{type(error).__name__}: {error}"})
            print(f"ERROR {source}: {type(error).__name__}: {error}", file=sys.stderr)
        progress(index, len(files))
    write_report(args.output, rows)
    return 1 if any(row["status"] != "ok" for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
