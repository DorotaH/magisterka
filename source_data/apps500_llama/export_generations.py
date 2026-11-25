#!/usr/bin/env python3
"""Export generated code from generations.jsonl into numbered Python files."""

import argparse
import json
from pathlib import Path


def export_generations(
    input_path: Path, output_dir: Path, mapping_path: Path, prefix: str
) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    mapping = []

    with input_path.open(encoding="utf-8") as source:
        for number, line in enumerate(source, start=1):
            if not line.strip():
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid JSON on line {number}: {error}") from error

            if "code" not in record or "problem_id" not in record:
                raise ValueError(
                    f"Line {number} must contain 'code' and 'problem_id' fields"
                )

            filename = f"{prefix}_{len(mapping) + 1}.py"
            code = record["code"]
            if not isinstance(code, str):
                raise ValueError(f"'code' on line {number} must be a string")

            (output_dir / filename).write_text(code, encoding="utf-8")
            mapping.append(
                {"filename": filename, "problem_id": record["problem_id"]}
            )

    mapping_path.parent.mkdir(parents=True, exist_ok=True)
    mapping_path.write_text(
        json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return len(mapping)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export code records from JSONL to numbered .py files."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).with_name("generations.jsonl"),
        help="Input JSONL file (default: generations.jsonl beside this script).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).with_name("generated"),
        help="Directory for exported .py files (default: generated/).",
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path(__file__).with_name("generated_mapping.json"),
        help="Output mapping JSON (default: generated_mapping.json).",
    )
    parser.add_argument(
        "--prefix", default="llama",
        help="Filename prefix, for example llama or qwen (default: llama).",
    )
    args = parser.parse_args()

    count = export_generations(args.input, args.output_dir, args.mapping, args.prefix)
    print(f"Wrote {count} Python files to {args.output_dir}")
    print(f"Wrote mapping to {args.mapping}")


if __name__ == "__main__":
    main()
