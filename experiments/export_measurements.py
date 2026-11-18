"""Export paired measurements from the resumable study JSON files."""

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
from statistics import mean, median

DATASETS = ("mercury_eval", "classeval", "apps")
FIELDS = ("sample_id", "dataset", "variant", "stage", "ruff_profile", "ruff_mode",
          "level", "metric", "value", "unit_id")


def unpack(run):
    try:
        return next(iter(json.loads(run["stdout"]).values()))
    except (ValueError, AttributeError, StopIteration):
        return None


def numerical_metrics(state):
    yield "file", "syntax_valid", state["syntax_error"] is None, ""
    yield "file", "changed", state["changed"], ""
    yield "file", "tab_lines", state["tab_lines"], ""
    for name, value in state["invasion"].items():
        yield "file", name, value, ""
    for index, key in enumerate(state.get("sew", [])):
        yield "file", f"sew_detected_{index}", key["verdict"] == "Watermark detected", ""
        yield "file", f"sew_evaluable_{index}", key["verdict"] != "Insufficient evidence", ""
        yield "file", f"sew_p_{index}", key["p"], ""
        yield "file", f"sew_sites_{index}", key.get("n_sites"), ""
    for name, value in state.get("acw", {}).items():
        if isinstance(value, bool):
            yield "file", f"fixed_{name}", value, ""
    for name, result in state.get("metrics", {}).items():
        parsed = unpack(result) if name != "complexipy" else result.get("data")
        if name in ("cc", "complexipy") and isinstance(parsed, list):
            values = []
            for index, block in enumerate(parsed):
                value = block["complexity"]
                unit = str(index) + ":" + block.get("function_name", block.get("name", ""))
                if name == "complexipy" and block.get("function_name") == "<module>":
                    yield "file", "complexipy_module", value, ""
                else:
                    yield "function", name, value, unit
                if name == "cc":
                    yield "function", "cc_rank", block["rank"], unit
                values.append(value)
            if values:
                for label, fun in (("mean", mean), ("median", median), ("max", max)):
                    yield "file", f"{name}_{label}", fun(values), ""
        elif isinstance(parsed, dict) and "error" not in parsed:
            if name == "hal":
                parsed = parsed["total"]
            for key, value in parsed.items():
                yield "file", f"{name}_{key}", value, ""


def family(code):
    return next((prefix for prefix in ("F", "E9", "B", "UP", "SIM", "I", "E", "W")
                 if code.startswith(prefix)), "inne")


def diagnostic_group(code):
    return "formatting" if code in {"W191", "W291", "W293", "E501"} or code.startswith("E70") else "other"


def diagnostic_metrics(state, baseline):
    codes = state.get("diagnostics")
    if codes is None:
        return
    yield "ruff_total", sum(codes.values())
    for code, count in codes.items():
        yield f"ruff_{code}", count
    by_group = Counter()
    for code, count in codes.items():
        by_group[family(code)] += count
        by_group[diagnostic_group(code)] += count
    for group in ("F", "E9", "B", "UP", "SIM", "I", "E", "W", "inne", "formatting", "other"):
        yield f"ruff_group_{group}", by_group[group]
    if baseline is None:
        return
    impacts = {"added": Counter(), "removed": Counter()}
    for code in set(codes) | set(baseline):
        delta = codes.get(code, 0) - baseline.get(code, 0)
        direction = "added" if delta > 0 else "removed"
        for group in ("all", family(code), diagnostic_group(code), f"rule_{code}"):
            impacts[direction][group] += abs(delta)
    for direction, impact in impacts.items():
        for group, count in impact.items():
            yield f"ruff_{direction}_{group}", count
    for group in impacts["added"].keys() | impacts["removed"].keys():
        yield f"ruff_net_{group}", impacts["added"][group] - impacts["removed"][group]


def rows(path):
    record = json.loads(path.read_text())
    sample_id = record["sample"]["sample_id"]
    dataset = record["dataset"]
    variants = record["variants"]
    for variant, states in variants.items():
        for stage, state in states.items():
            profile, mode = stage.split("/") if "/" in stage else ("", "")
            prefix = (sample_id, dataset, variant, "ruff" if profile else stage, profile, mode)
            for level, metric, value, unit in numerical_metrics(state):
                if value is not None:
                    yield (*prefix, level, metric, int(value) if isinstance(value, bool) else value, unit)
            if profile:
                base = variants["original"][stage]["diagnostics"]
                for metric, value in diagnostic_metrics(state, base):
                    yield (*prefix, "file", metric, value, "")
            else:
                for p, ruff in state["ruff_baseline"].items():
                    base = variants["original"][stage]["ruff_baseline"][p]["diagnostics"]
                    for metric, value in diagnostic_metrics(ruff, base):
                        yield (sample_id, dataset, variant, stage, p, "check", "file", metric, value, "")
    correctness = path.parent / "correctness_v2" / "result.json"
    if correctness.exists():
        for variant, test in json.loads(correctness.read_text()).get("variants", {}).items():
            for field in ("differential", "official", "timeouts"):
                yield (sample_id, dataset, variant, "correctness", "", "", "file", field, test[field], "")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    args = parser.parse_args()
    out = args.measurements / "tidy"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "measurements_long.csv").open("w", encoding="utf-8", newline="") as m, \
         (out / "samples.csv").open("w", encoding="utf-8", newline="") as s:
        measurements = csv.writer(m)
        measurements.writerow(FIELDS)
        samples = csv.writer(s)
        samples.writerow(("sample_id", "dataset", "structure", "difficulty", "format", "sloc", "sloc_band",
                          "cognitive_band", "source_sha256"))
        for dataset in DATASETS:
            for path in sorted((args.measurements / dataset).glob("*/result.json")):
                record = json.loads(path.read_text())
                sample = record["sample"]
                sloc = sample["sloc"]
                metrics = dict((name, value) for level, name, value, _
                               in numerical_metrics(record["variants"]["original"]["embedded"]) if level == "file")
                max_complexipy = metrics.get("complexipy_max")
                cognitive = ("0–4" if max_complexipy < 5 else "5–14" if max_complexipy < 15 else "≥15") if max_complexipy is not None else ""
                band = "<20" if sloc < 20 else "20–39" if sloc < 40 else "40–99" if sloc < 100 else "≥100"
                samples.writerow((sample["sample_id"], dataset, sample["structure"], sample.get("difficulty"),
                                  sample.get("format"), sloc, band, cognitive, sample["sha256"]))
                measurements.writerows(rows(path))
    (out / "slownik_kolumn.md").write_text(
        "# Słownik kolumn\n\n"
        "- `sample_id` i `dataset` identyfikują jednostkę.\n"
        "- `variant`, `stage`, `ruff_profile` i `ruff_mode` identyfikują stan.\n"
        "- `level`, `unit_id` identyfikują plik albo blok/funkcję.\n"
        "- `metric` i `value` przechowują wynik. Brak wiersza oznacza niedostępny pomiar.\n"
        "- `ruff_added_*`, `ruff_removed_*` i `ruff_net_*` opisują zmiany wobec oryginału w tym samym trybie.\n"
        "- `sew_detected_*` używa indeksu klucza. Zero oznacza klucz eksperymentalny. Wynik interpretujemy z `sew_evaluable_*`.\n"
        "- `complexipy_module` to pomiar modułu w warstwie skryptów APPS.\n"
        "- `samples.csv` dodaje cechy oryginału, warstwy i SHA-256.\n", encoding="utf-8")


if __name__ == "__main__":
    main()
