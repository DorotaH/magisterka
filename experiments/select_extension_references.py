"""Select the eligible reference solutions and audit duplicate exclusions."""

import argparse
import csv
import json
import re
from hashlib import sha256
from pathlib import Path

from profile_extension_candidates import json_lines
from select_extension_classeval import EXTENSION, ROOT, SEED
from select_samples import inspect, rows, write_json


def candidates(inputs):
    for row in rows(inputs / "mercury-train.parquet", ["slug_name", "solutions"]):
        yield "mercury_train", row["slug_name"], (entry["solution"] for entry in row["solutions"])
    for row in json_lines(inputs / "leetcode-test.jsonl"):
        yield "leetcode_test", row["task_id"], (row["completion"],)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    args = parser.parse_args()
    profiles = EXTENSION / "spis_zbiorow/kandydaci.csv"
    with profiles.open(newline="", encoding="utf-8") as stream:
        eligible = {row["dataset"]: row for row in csv.DictReader(stream) if row["eligible"] == "True"}
    if eligible.keys() != {"mercury_train", "leetcode_test"}:
        raise ValueError("Zestaw kwalifikujących się zbiorów różni się od protokołu")

    layer = EXTENSION / "warstwa_A"
    source_hashes = {}
    for row in eligible.values():
        path = args.inputs / row["source_file"]
        digest = sha256(path.read_bytes()).hexdigest()
        if digest != row["source_sha256"]:
            raise ValueError(f"Niezgodny SHA-256 {path}")
        source_hashes[path.name] = digest

    reference = ROOT / "results/main_study"
    prior = {}
    for dataset in ("apps", "mercury_eval", "classeval"):
        prior[dataset] = json.loads((reference / dataset / "selection.json").read_bytes())["samples"]
    seen = {row["sha256"]: f'{dataset}/{row["sample_id"]}'
            for dataset, samples in prior.items() for row in samples}
    excluded = [("apps", row["sample_id"], "previously_selected_task", "main_study/apps")
                for row in prior["apps"]]
    selected = []
    identities = set()
    for dataset, sample_id, solutions in candidates(args.inputs):
        if not re.fullmatch(r"[A-Za-z0-9_-]+", sample_id) or (dataset, sample_id) in identities:
            raise ValueError(f"Niepoprawny lub powtórzony identyfikator {dataset}/{sample_id}")
        identities.add((dataset, sample_id))
        for index, code in enumerate(solutions):
            reason, sloc, structure = inspect(code)
            if reason or structure == "script":
                continue
            digest = sha256(code.encode()).hexdigest()
            if digest in seen:
                excluded.append((dataset, sample_id, "identical_code", seen[digest]))
                break
            folder = layer / dataset / sample_id
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "original.py").write_bytes(code.encode())
            seen[digest] = f"{dataset}/{sample_id}"
            selected.append({
                "dataset": dataset, "sample_id": sample_id, "solution_index": index,
                "sloc": sloc, "structure": structure, "sha256": digest,
                "source": eligible[dataset]["source_file"],
            })
            break
        else:
            excluded.append((dataset, sample_id, "no_eligible_solution", ""))
    for name in eligible:
        if sum(row["dataset"] == name for row in selected) < 100:
            raise ValueError(f"Za mało próbek po deduplikacji: {name}")
    write_json(layer / "selection.json", {"seed": SEED, "source_sha256": source_hashes, "samples": selected})
    with (layer / "wykluczenia.csv").open("w", encoding="utf-8", newline="") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(("dataset", "sample_id", "reason", "matched_source"))
        writer.writerows(excluded)


if __name__ == "__main__":
    main()
