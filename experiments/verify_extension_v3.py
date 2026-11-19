"""Independently check selected summary rows against the raw measurements."""

import argparse
import csv
import json
import math
from pathlib import Path
from random import Random

from select_extension_classeval import EXTENSION, SEED

VARIANTS = ("sew", "acw_notab", "acw_full")


def load(path):
    return json.loads(path.read_bytes())


def table(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def compare(run, layer):
    directory = EXTENSION / layer
    selection = load(directory / "selection.json")["samples"]
    data = {}
    for sample in selection:
        path = run / layer / sample["dataset"] / sample["sample_id"] / "result.json"
        record = load(path)
        assert record["sample"] == sample
        data[sample["dataset"], sample["sample_id"]] = record["variants"]
    rates = table(directory / "summary/proportions.csv")
    pairs = table(directory / "summary/paired.csv")
    available = sorted({dataset for dataset, _ in data})
    rng = Random(SEED)
    for dataset in available:
        originals = [states for (name, _), states in data.items() if name == dataset]
        variant = rng.choice(VARIANTS)
        measure = rng.choice(("changed", "syntax_error"))
        matching = [row for row in rates if row["dataset"] == dataset and row["label"] == "main"
                    and row["variant"] == variant and row["measure"] == measure]
        expected = sum(bool(variants[variant]["embedded"][measure]) for variants in originals)
        n, events = (int(matching[0][field]) for field in ("n", "events"))
        assert (n, events) == (len(originals), expected), (layer, dataset, variant, measure)

        profile = rng.choice(("default", "strict"))
        differences = []
        for states in originals:
            before = states["original"][f"{profile}/check"]["diagnostics"]
            after = states[variant][f"{profile}/check"]["diagnostics"]
            if before is not None and after is not None:
                differences.append(sum(after.values()) - sum(before.values()))
        matched = next(row for row in pairs if row["dataset"] == dataset and row["label"] == "main"
                   and row["variant"] == variant and row["metric"] == "ruff_total"
                   and row["profile"] == profile and row["mode"] == "check")
        assert int(matched["n"]) == len(differences)
        if differences:
            assert math.isclose(float(matched["mean_delta"]), sum(differences)/len(differences), abs_tol=1e-12)
        print(layer, dataset, variant, measure, n, events, profile, len(differences))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    args = parser.parse_args()
    for layer in ("warstwa_A", "warstwa_C"):
        compare(args.measurements, layer)


if __name__ == "__main__":
    main()
