#!/usr/bin/env python3
"""Prepare the two APPS 500-task generated-code datasets without filtering."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def member(archive: zipfile.ZipFile, suffix: str) -> str:
    matches = [name for name in archive.namelist() if name.endswith(suffix)]
    if len(matches) != 1:
        raise ValueError(f"Expected one {suffix} in {archive.filename}, got {len(matches)}")
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--downloads", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    archives: dict[str, dict[str, Any]] = {}
    for label, filename in (("qwen", "apps500_qwen.zip"), ("llama", "apps500_llama.zip")):
        path = args.downloads / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        shutil.copy2(path, args.output / filename)
        with zipfile.ZipFile(path) as archive:
            task_meta = json.loads(archive.read(member(archive, "tasks.json")))
            generation_name = member(archive, "generations.jsonl")
            raw_generation = archive.read(generation_name)
            generations = [json.loads(line) for line in raw_generation.splitlines() if line.strip()]
        ids = task_meta["problem_ids"]
        if task_meta.get("split") != "test":
            raise ValueError(f"{filename} split is not test")
        if len(ids) != task_meta.get("n_tasks") or len(set(ids)) != len(ids):
            raise ValueError(f"Invalid task list in {filename}")
        if {int(row["problem_id"]) for row in generations} != set(ids):
            raise ValueError(f"Generation task IDs differ from tasks.json in {filename}")
        if any(row.get("split") != "test" or row.get("dataset") != "apps" for row in generations):
            raise ValueError(f"Unexpected dataset or split value in {filename}")
        (args.output / f"{label}_generations.jsonl").write_bytes(raw_generation)
        (args.output / f"{label}_tasks.json").write_text(
            json.dumps(task_meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        archives[label] = {
            "archive": filename,
            "archive_sha256": sha256(path),
            "task_meta": task_meta,
            "generation_file": f"{label}_generations.jsonl",
            "generation_sha256": hashlib.sha256(raw_generation).hexdigest(),
            "generations": generations,
        }

    qwen_ids = archives["qwen"]["task_meta"]["problem_ids"]
    llama_ids = archives["llama"]["task_meta"]["problem_ids"]
    if qwen_ids != llama_ids:
        raise ValueError("Qwen and Llama task ID lists are not identical")

    counts_path = args.output / "input_counts.csv"
    with counts_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=("dataset", "problem_id", "sample_index", "model", "code_present", "extraction_status"),
        )
        writer.writeheader()
        for dataset, info in archives.items():
            for row in info["generations"]:
                writer.writerow({
                    "dataset": dataset,
                    "problem_id": row.get("problem_id"),
                    "sample_index": row.get("sample_index"),
                    "model": row.get("model"),
                    "code_present": isinstance(row.get("code"), str) and bool(row["code"]),
                    "extraction_status": row.get("extraction_status", ""),
                })

    manifest = {
        "scope": ["qwen", "llama"],
        "selection": "problem_ids and generations from the supplied apps500_* ZIP files; no post-generation filtering",
        "shared_problem_ids": qwen_ids,
        "inputs": {
            label: {
                key: value
                for key, value in info.items()
                if key != "generations"
            }
            | {
                "generation_rows": len(info["generations"]),
                "model_row_counts": dict(Counter(str(row.get("model", "")) for row in info["generations"])),
            }
            for label, info in archives.items()
        },
    }
    (args.output / "input_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
