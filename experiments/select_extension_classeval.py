"""Validate and select the existing ClassEval generations for extension v3."""

import argparse
import csv
import json
import re
from collections import Counter
from hashlib import sha256
from pathlib import Path

from restore_study_files import restore
from select_samples import inspect, write_json

ROOT = Path(__file__).resolve().parents[1]
EXTENSION = ROOT / "results/extension_v3"
MODELS = ("classeval_qwen25c7b", "classeval_llama31_8b")
PARAMETERS = ("system_prompt", "user_template", "temperature", "top_p", "max_tokens", "base_seed")
EXTRACTION_FAILURES = {"no_class", "no_code_block", "truncated"}
SEED = 20261118


def load_model(directory, expected_pairs, dataset_hash):
    manifest = json.loads((directory / "manifest.json").read_bytes())
    if manifest["dataset_sha256"] != dataset_hash or not manifest.get("model_revision"):
        raise ValueError(f"Niezgodny zbiór lub brak rewizji modelu w {directory}")
    source = directory / "generations.jsonl"
    payload = source.read_bytes()
    records = {}
    for line in payload.splitlines():
        row = json.loads(line)
        identity = (row["task_id"], row["sample_index"])
        if identity in records and records[identity] != row:
            raise ValueError(f"Sprzeczny duplikat w {source}: {identity}")
        records[identity] = row
        for field in ("prompt_sha256", "raw_sha256", "code_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", row[field]):
                raise ValueError(f"Niepoprawny {field} w {source}: {identity}")
        for field, text in (("raw_sha256", "raw_response"), ("code_sha256", "code")):
            if sha256(row[text].encode()).hexdigest() != row[field]:
                raise ValueError(f"Niezgodny {field} w {source}: {identity}")
    if records.keys() != expected_pairs:
        raise ValueError(f"Niezgodna lista zadań i indeksów w {source}")
    return manifest, records, sha256(payload).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--classeval", type=Path, required=True)
    args = parser.parse_args()

    reference = json.loads((ROOT / "results/main_study/classeval/selection.json").read_bytes())
    dataset_hash = reference["source_sha256"]["classeval.json"]
    dataset = args.classeval.read_bytes()
    if sha256(dataset).hexdigest() != dataset_hash:
        raise ValueError("Niezgodny SHA-256 źródłowego ClassEval")
    tasks = {row["task_id"]: bool(row["test"] and row["test_classes"]) for row in json.loads(dataset)}
    if len(tasks) != 100 or any(not re.fullmatch(r"ClassEval_\d+", task) for task in tasks):
        raise ValueError("Niepoprawna lista zadań ClassEval")
    pairs = {(task, index) for task in tasks for index in range(5)}

    entries = json.loads((EXTENSION / "split_files/manifest.json").read_bytes())
    for entry in entries:
        restore(ROOT, entry)
    layer = EXTENSION / "warstwa_C"
    models = {name: load_model(layer / name, pairs, dataset_hash) for name in MODELS}
    first, second = (models[name][0] for name in MODELS)
    if any(first[key] != second[key] for key in PARAMETERS):
        raise ValueError("Manifesty zawierają różne parametry generowania")

    exclusions = []
    selection = {"seed": SEED, "source_sha256": {"classeval.json": dataset_hash}, "samples": []}
    for name, (manifest, records, generation_hash) in models.items():
        directory = layer / name
        selection["source_sha256"][f"{name}/generations.jsonl"] = generation_hash
        selection["source_sha256"][f"{name}/manifest.json"] = sha256((directory / "manifest.json").read_bytes()).hexdigest()
        for (task, index), row in sorted(records.items()):
            sample_id = f"{task}_{index}"
            status = row["extraction_status"]
            if status in EXTRACTION_FAILURES:
                exclusions.append((name, task, index, status))
                continue
            if status != "ok":
                raise ValueError(f"Nieznany status ekstrakcji: {status}")
            reason, sloc, structure = inspect(row["code"])
            if reason:
                exclusions.append((name, task, index, reason))
                continue
            selection["samples"].append({
                "dataset": name, "sample_id": sample_id, "task_id": task,
                "sample_index": index, "model": manifest["model"],
                "model_revision": manifest["model_revision"], "sloc": sloc,
                "structure": structure, "sha256": row["code_sha256"],
                "tests_available": tasks[task], "source": f"{name}/generations.jsonl",
            })
    write_json(layer / "selection.json", selection)
    with (layer / "wykluczenia.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(("dataset", "task_id", "sample_index", "reason"))
        writer.writerows(exclusions)
    for name in MODELS:
        accepted = sum(row["dataset"] == name for row in selection["samples"])
        reasons = Counter(reason for dataset, _, _, reason in exclusions if dataset == name)
        print(name, accepted, dict(reasons))


if __name__ == "__main__":
    main()
