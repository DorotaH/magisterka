"""Summarize extension v3 measurements and bootstrap ClassEval by task."""

import argparse
import ast
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from analyze_measurements import (
    MARGINS,
    METRICS,
    SEED,
    VARIANTS,
    holm,
    statistics,
    wilson,
)
from export_measurements import diagnostic_metrics, numerical_metrics
from select_extension_classeval import EXTENSION, ROOT

MAIN = ROOT / "results/main_study"
STAGES = [("", ""), *((p, m) for p in ("default", "strict")
                      for m in ("check", "fix", "format", "fix_format"))]


def read(path):
    return json.loads(path.read_bytes())


def write(path, fields, items):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(items)


def schema(name):
    with (MAIN / "summary" / name).open(newline="", encoding="utf-8") as stream:
        return next(csv.reader(stream))


def state_metrics(state):
    result = {name: value for level, name, value, _ in numerical_metrics(state)
              if level == "file" and value is not None}
    result.update(diagnostic_metrics(state, None))
    return result


def groups(root, layer, partial):
    selection = read(EXTENSION / layer / "selection.json")
    result = defaultdict(list)
    for sample in selection["samples"]:
        name = sample["dataset"]
        folder = root / layer / name / sample["sample_id"]
        path = folder / "result.json"
        tests = folder / "correctness_v2" / "result.json"
        if not path.exists() or (layer == "warstwa_C" and sample["tests_available"] and not tests.exists()):
            if partial:
                continue
            raise FileNotFoundError(f"Brak pełnego pomiaru {folder}")
        record = read(path)
        if record["sample"] != sample:
            raise ValueError(f"Niezgodna próbka {path}")
        metrics = {variant: {stage: state_metrics(state) for stage, state in states.items()}
                   for variant, states in record["variants"].items()}
        outcomes = read(tests)["variants"] if tests.exists() else {}
        unit = (sample.get("task_id", sample["sample_id"]), metrics, outcomes, folder)
        scope = "script" if sample["structure"] == "script" else "main"
        result[name, scope].append(unit)
        result["all", scope].append(unit)
    return result


class TaskBootstrap:
    def __init__(self, tasks):
        self.index = {key: i for i, key in enumerate(sorted(set(tasks)))}
        if not self.index:
            self.weights = np.empty((0, 0))
            return
        n = len(self.index)
        self.weights = np.random.default_rng(SEED).multinomial(n, np.full(n, 1/n), size=10000).astype(float)

    def draws(self, observations):
        counts = np.zeros(len(self.index))
        sums = np.zeros(len(self.index))
        for task, value in observations:
            index = self.index[task]
            counts[index] += 1
            sums[index] += value
        sizes = self.weights @ counts
        observed = sizes > 0
        return (self.weights @ sums)[observed] / sizes[observed]

    def interval(self, observations):
        values = self.draws(observations)
        return np.quantile(values, [.025, .975]) if len(values) else (None, None)


def pair_row(group, metric, profile, mode, units, variant, bootstrap, rng):
    stage = f"{profile}/{mode}" if profile else "embedded"
    pairs = [(task, data["original"][stage].get(metric), data[variant][stage].get(metric))
             for task, data, _, _ in units]
    valid = [(task, a, b) for task, a, b in pairs if a is not None and b is not None]
    delta = [(task, float(b) - float(a)) for task, a, b in valid]
    margin = MARGINS.get(metric, .1 if metric == "ruff_group_other" else None)
    row = {**group, "variant": variant, "metric": metric, "profile": profile, "mode": mode,
           "excluded": len(units)-len(valid), "n": len(valid)}
    if not valid:
        return row
    original = [float(a) for _, a, _ in valid]
    marked = [float(b) for _, _, b in valid]
    row.update(mean_original=np.mean(original), mean_variant=np.mean(marked),
               median_original=np.median(original), median_variant=np.median(marked))
    if bootstrap is None:
        row.update(statistics([value for _, value in delta], margin, rng))
    else:
        values = [value for _, value in delta]
        draws = bootstrap.draws(delta)
        low, high = np.quantile(draws, [.025, .975])
        row.update(mean_delta=np.mean(values), median_delta=np.median(values),
                   mean_ci_low=low, mean_ci_high=high, upper_mean_95=np.quantile(draws, .95))
    return row


def rate(group, variant, measure, values, bootstrap, profile="", mode="", key=""):
    n = len(values)
    events = sum(value for _, value in values)
    low, high = wilson(events, n) if bootstrap is None else bootstrap.interval(values)
    return {**group, "variant": variant, "measure": measure, "n": n, "events": events,
            "fraction": events/n if n else None, "ci_low": low, "ci_high": high,
            "profile": profile, "mode": mode, "key": key}


def rates(group, units, bootstrap):
    originals = [(task, tests["original"]["official"] == "pass")
                 for task, _, tests, _ in units if "original" in tests]
    if originals:
        yield rate(group, "original", "original_pass", originals, bootstrap)
    for variant in VARIANTS:
        detector = "sew_detected_0" if variant == "sew" else f"fixed_{variant}"
        changes = [(task, data[variant]["embedded"]["changed"]) for task, data, _, _ in units]
        syntax = [(task, not data[variant]["embedded"]["syntax_valid"]) for task, data, _, _ in units]
        yield rate(group, variant, "changed", changes, bootstrap)
        yield rate(group, variant, "syntax_error", syntax, bootstrap)
        equal = [(task, data[variant]["embedded"]["ast_equal"]) for task, data, _, _ in units
                 if "ast_equal" in data[variant]["embedded"]]
        yield rate(group, variant, "ast_equal", equal, bootstrap)
        compared = [(task, tests[variant]["differential"] == "different")
                    for task, _, tests, _ in units if variant in tests
                    and tests["original"]["official"] == "pass"
                    and tests[variant]["official"] in {"pass", "fail"}
                    and any(value is not None for value in tests[variant]["observed"])]
        yield rate(group, variant, "different", compared, bootstrap)
        if originals:
            regression = [(task, tests[variant]["official"] == "fail")
                          for task, _, tests, _ in units if variant in tests
                          and tests["original"]["official"] == "pass"
                          and tests[variant]["official"] in {"pass", "fail"}]
            yield rate(group, variant, "official_regression", regression, bootstrap)
            for status in ("pass", "fail", "error"):
                values = [(task, tests[variant]["official"] == status)
                          for task, _, tests, _ in units if variant in tests]
                yield rate(group, variant, f"test_{status}", values, bootstrap)
            values = [(task, bool(tests[variant]["timeouts"]))
                      for task, _, tests, _ in units if variant in tests]
            yield rate(group, variant, "test_timeout", values, bootstrap)
        for profile, mode in STAGES:
            stage = f"{profile}/{mode}" if profile else "embedded"
            detection = [(task, data[variant][stage][detector]) for task, data, _, _ in units
                         if detector in data[variant][stage]]
            yield rate(group, variant, "detected", detection, bootstrap, profile, mode or "embedded")
            if profile:
                kept = [(task, data[variant][stage][detector]) for task, data, _, _ in units
                        if data[variant]["embedded"].get(detector) and detector in data[variant][stage]]
                yield rate(group, variant, "survival", kept, bootstrap, profile, mode)
            for key in range(3 if variant == "sew" else 1):
                control = f"sew_detected_{key}" if variant == "sew" else detector
                alarms = [(task, data["original"][stage][control]) for task, data, _, _ in units
                          if control in data["original"][stage]
                          and data["original"][stage].get(f"sew_evaluable_{key}", True)]
                yield rate(group, variant, "false_alarm", alarms, bootstrap, profile, mode or "embedded", key)


def normalized(path):
    try:
        tree = ast.parse(path.read_bytes())
        compile(tree, str(path), "exec")
        return ast.dump(tree, include_attributes=False)
    except (SyntaxError, ValueError):
        return None


def structural_changes(units):
    totals = defaultdict(lambda: [0, 0, 0])
    for _, _, _, folder in units:
        step_dir = folder / "acw_steps"
        before = normalized(folder / "original.py")
        stages = [("sourcery", folder / "after_sourcery.py")]
        for step in read(step_dir / "steps.json"):
            number = step["rule"]
            path = step_dir / ("with_tabs.py" if number == 45 else f"rule_{number}.py")
            stages.append((str(number), path if step["changed"] else None))
        for name, path in stages:
            after = normalized(path) if path else before
            total = totals[name]
            total[0] += 1
            total[1] += before is not None and after is not None and before != after
            total[2] += before is None or after is None
            before = after
    for rule, (n, changed, invalid) in totals.items():
        yield {"rule": rule, "n": n, "ast_changed": changed, "uncomparable": invalid}


def sourcery_rules(root, layer, partial):
    selection = read(EXTENSION / layer / "selection.json")["samples"]
    if layer == "warstwa_C":
        selection.sort(key=lambda row: row["dataset"])
    batches = defaultdict(list)
    for sample in selection:
        folder = root / layer / sample["dataset"] / sample["sample_id"]
        result = folder / "result.json"
        if partial and not result.exists():
            continue
        original = read(result)["variants"]["original"]["embedded"]
        batch = Path(original["acw_replay"]).parents[1]
        batches[batch].append((sample["dataset"], folder))
    totals = defaultdict(lambda: [0, 0, 0])
    for batch, samples in batches.items():
        stdout = read(batch / "embedding.json")["stdout"]
        by_file = defaultdict(Counter)
        for index, rule in re.findall(r"/sourcery_embedding/(\d+)\.py:\d+(?:-\d+)? ([a-z0-9-]+)$",
                                      stdout, re.MULTILINE):
            by_file[int(index)][rule] += 1
        for index, (name, folder) in enumerate(samples):
            after = folder / "after_sourcery.py"
            embedded = batch / "sourcery_embedding" / f"{index:04d}.py"
            if embedded.read_bytes() != after.read_bytes():
                raise ValueError(f"Niezgodne przypisanie logu Sourcery dla {folder}")
            first, last = normalized(folder / "original.py"), normalized(after)
            changed = first is not None and last is not None and first != last
            for rule, suggestions in by_file[index].items():
                for dataset in (name, "all"):
                    total = totals[dataset, rule]
                    total[0] += 1
                    total[1] += suggestions
                    total[2] += changed
    for (dataset, rule), (files, suggestions, ast_changed) in sorted(totals.items()):
        yield {"dataset": dataset, "rule": rule, "files": files, "reported": suggestions,
               "files_with_ast_change": ast_changed}


def test_errors(grouped):
    for (model, _), units in grouped.items():
        if model == "all":
            continue
        for task, _, outcomes, folder in units:
            for variant, result in outcomes.items():
                if result["official"] != "error":
                    continue
                log = read(folder / "correctness_v2" / f"{variant}.json")
                lines = log["stderr"].splitlines()
                yield {"dataset": model, "task_id": task, "sample_id": folder.name,
                       "variant": variant, "process_exit": log["exit"],
                       "status": log.get("status", "error"),
                       "last_stderr_line": lines[-1] if lines else ""}


def summarize(root, output, layer, partial):
    rng = np.random.default_rng(SEED)
    paired, proportions, structural = [], [], []
    grouped = groups(root, layer, partial)
    for (name, scope), units in grouped.items():
        group = {"dataset": name, "stratum": "population", "label": scope}
        bootstrap = TaskBootstrap(task for task, *_ in units) if layer == "warstwa_C" else None
        for variant in VARIANTS:
            for profile, mode in STAGES:
                for metric in METRICS:
                    if (metric.startswith("ruff") and not profile
                            or metric.startswith(("cc_", "complexipy_", "mi_", "raw_"))
                            and mode not in ("", "fix_format")):
                        continue
                    paired.append(pair_row(group, metric, profile, mode, units, variant, bootstrap, rng))
        proportions.extend(rates(group, units, bootstrap))
        structural.extend({**group, **row} for row in structural_changes(units))
    if layer == "warstwa_A":
        holm(paired, "wilcoxon_p", "wilcoxon_p_holm")
        holm(paired, "tost_p", "tost_p_holm")
    directory = output / layer / "summary"
    write(directory / "paired.csv", schema("paired.csv"), paired)
    write(directory / "proportions.csv", schema("proportions.csv"), proportions)
    write(directory / "reguly_ast.csv", ("dataset", "stratum", "label", "rule", "n",
                                        "ast_changed", "uncomparable"), structural)
    if not partial:
        write(directory / "reguly_sourcery.csv",
              ("dataset", "rule", "files", "reported", "files_with_ast_change"),
              sourcery_rules(root, layer, partial))
    if layer == "warstwa_C":
        write(directory / "bledy_testow.csv", ("dataset", "task_id", "sample_id", "variant",
                                              "process_exit", "status", "last_stderr_line"),
              test_errors(grouped))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    parser.add_argument("--output", type=Path, default=EXTENSION)
    parser.add_argument("--layer", choices=("warstwa_A", "warstwa_C"))
    parser.add_argument("--partial", action="store_true")
    args = parser.parse_args()
    for layer in (args.layer,) if args.layer else ("warstwa_A", "warstwa_C"):
        summarize(args.measurements, args.output, layer, args.partial)


if __name__ == "__main__":
    main()
