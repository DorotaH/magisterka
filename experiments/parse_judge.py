"""Validate and extract blinded LLM judgments from a JSONL response log."""

import argparse
import csv
import json
from pathlib import Path

CRITERIA = ("readability", "naming", "idiomaticity", "maintainability", "error_risk", "automation_traces")
METADATA = ("fragment", "condition", "left", "right", "repeat", "model", "parameters")


def parse(record):
    raw = record["response"]
    if isinstance(raw, str):
        raw = raw.strip()
        if raw.startswith("```") and raw.endswith("```"):
            raw = raw.split("\n", 1)[1][:-3]
        raw = json.loads(raw)
    preference = raw["preference"]
    if preference not in ("left", "right") or not str(raw["reason"]).strip():
        raise ValueError("Invalid preference")
    flat = {name: record[name] for name in METADATA}
    flat["parameters"] = json.dumps(flat["parameters"], sort_keys=True)
    flat.update(preference=preference, preferred_alias=record[preference], reason=raw["reason"])
    for side in ("left", "right"):
        for criterion in CRITERIA:
            item = raw[side][criterion]
            score = item["score"]
            if type(score) is not int or not 1 <= score <= 5 or not str(item["reason"]).strip():
                raise ValueError(f"Invalid rubric entry: {side}.{criterion}")
            flat[f"{side}_{criterion}"] = score
            flat[f"{side}_{criterion}_reason"] = item["reason"]
    return flat


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows, errors = [], []
    with args.input.open(encoding="utf-8") as stream:
        for line, text in enumerate(stream, 1):
            try:
                rows.append(parse(json.loads(text)))
            except (KeyError, ValueError, TypeError, IndexError) as error:
                errors.append({"line": line, "error": str(error)})
    if rows:
        with args.output.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    args.output.with_suffix(".errors.json").write_text(json.dumps(errors, indent=2)+"\n")
    if errors:
        raise SystemExit(f"{len(errors)} records failed validation")


if __name__ == "__main__":
    main()
