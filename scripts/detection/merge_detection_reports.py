#!/usr/bin/env python3
"""Merge detector JSONL files, adding a filename stem to every result."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import TextIO


def append_report(
    stream: TextIO,
    report_path: Path,
    model: str,
    detector: str,
) -> int:
    pattern = re.compile(rf"^{model}_\d+\.py$")
    count = 0
    with report_path.open(encoding="utf-8") as report:
        for line_number, line in enumerate(report, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"{report_path}:{line_number}: invalid JSON: {error}") from error

            filename = Path(str(row.get("input", ""))).name
            if not pattern.fullmatch(filename):
                raise ValueError(
                    f"{report_path}:{line_number}: expected a {model}_N.py input, got {filename!r}"
                )
            output = {
                "problem": Path(filename).stem,
                "model": model,
                "detector": detector,
                "jsonl": row,
            }
            stream.write(json.dumps(output, ensure_ascii=False) + "\n")
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for model in ("llama", "qwen"):
        for detector in ("acw", "sew"):
            parser.add_argument(f"--{model}-{detector}", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    with args.output.open("w", encoding="utf-8", newline="\n") as stream:
        for model in ("llama", "qwen"):
            for detector in ("acw", "sew"):
                report = getattr(args, f"{model}_{detector}")
                total += append_report(stream, report, model, detector)

    print(f"Wrote {total} detection records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
