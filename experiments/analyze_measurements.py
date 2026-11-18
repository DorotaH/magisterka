"""Analyze paired sample-level measurements and save reproducible summary tables."""

import argparse
from collections import defaultdict
import csv
from pathlib import Path
import warnings

import numpy as np
from scipy import optimize, special, stats


VARIANTS = ("sew", "acw_notab", "acw_full")
MARGINS = {"cc_mean": .5, "complexipy_mean": 1., "mi_mi": 2.}
METRICS = (*MARGINS, "raw_sloc", "ruff_total", "ruff_group_other", "syntax_valid",
           "line_similarity", "token_similarity", "changed_lines", "tab_lines")
SEED = 20261118


def wilson(k, n):
    if not n:
        return None, None
    z = stats.norm.ppf(.975)
    fraction = k / n
    denom = 1 + z*z/n
    center = (fraction + z*z/(2*n))/denom
    spread = z * np.sqrt(fraction*(1-fraction)/n + z*z/(4*n*n))/denom
    return max(0, center-spread), min(1, center+spread)


def holm(rows, key, output):
    ranked = sorted((row for row in rows if row.get(key) is not None), key=lambda row: row[key])
    previous = 0
    for i, row in enumerate(ranked):
        previous = min(1., max(previous, (len(ranked)-i)*row[key]))
        row[output] = previous


def statistics(differences, margin, rng):
    n = len(differences)
    delta = np.asarray(differences, dtype=float)
    if not n:
        return {"n": 0}
    if np.all(delta == delta[0]):
        low = high = mean_low = mean_high = delta[0]
    else:
        boot_median, boot_mean = [], []
        for _ in range(10):
            draw = rng.choice(delta, size=(1000, n))
            boot_median.extend(np.median(draw, axis=1))
            boot_mean.extend(draw.mean(axis=1))
        low, high = np.quantile(boot_median, [.025, .975])
        mean_low, mean_high = np.quantile(boot_mean, [.025, .975])
    nonzero = delta[delta != 0]
    if len(nonzero):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            p = float(stats.wilcoxon(delta).pvalue)
        ranks = stats.rankdata(abs(nonzero))
        effect = float(np.sum(np.sign(nonzero)*ranks)/np.sum(ranks))
    else:
        p, effect = 1., 0.
    tost = None
    if margin and n > 1:
        se = np.std(delta, ddof=1)/np.sqrt(n)
        location = np.mean(delta)
        if se:
            tost = float(max(stats.t.sf((location+margin)/se, n-1), stats.t.cdf((location-margin)/se, n-1)))
        else:
            tost = float(abs(location) >= margin)
    standard_error = np.std(delta, ddof=1)/np.sqrt(n) if n > 1 else None
    upper_mean = np.mean(delta) + stats.t.ppf(.95, n-1)*standard_error if standard_error is not None else None
    return {"n": n, "mean_delta": float(np.mean(delta)), "median_delta": float(np.median(delta)),
            "upper_mean_95": upper_mean,
            "ci_low": float(low), "ci_high": float(high),
            "mean_ci_low": float(mean_low), "mean_ci_high": float(mean_high),
            "wilcoxon_p": p, "rank_biserial": effect,
            "tost_p": tost, "equivalence_margin": margin}


def proportion(group, measure, values):
    n, k = len(values), sum(values)
    low, high = wilson(k, n)
    return {**group, "measure": measure, "n": n, "events": k,
            "fraction": k/n if n else None, "ci_low": low, "ci_high": high}


def write(path, data):
    fields = list(dict.fromkeys(key for row in data for key in row))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def load(path):
    with path.open(newline="", encoding="utf-8") as stream:
        yield from csv.DictReader(stream)


def group_samples(samples):
    groups = defaultdict(list)
    for sample in samples:
        dataset = sample["dataset"]
        identity = sample["sample_id"]
        scope = "script" if sample["structure"] == "script" else "main"
        groups[(dataset, "population", scope)].append(identity)
        for field in ("structure", "sloc_band", "cognitive_band", "difficulty", "format"):
            label = sample[field]
            if label:
                groups[(dataset, f"{scope}/{field}", label)].append(identity)
    return groups


def regression(data, sizes):
    datasets = sorted({key[0] for key in sizes})
    results = []
    for profile in ("default", "strict"):
        pairs = []
        for (dataset, identity), sloc in sizes.items():
            original = data.get((dataset, identity, "sew", "embedded", "", ""), {})
            after = data.get((dataset, identity, "sew", "ruff", profile, "fix_format"), {})
            if original.get("sew_detected_0") == "1" and "sew_detected_0" in after:
                pairs.append((dataset, sloc, int(after["sew_detected_0"] == "0")))
        if not pairs:
            continue
        design = np.array([[1, np.log(sloc), *[int(dataset == d) for d in datasets[1:]]]
                           for dataset, sloc, _ in pairs])
        y = np.asarray([outcome for _, _, outcome in pairs])
        if len(set(y)) < 2 or np.linalg.matrix_rank(design) < design.shape[1]:
            results.append({"profile": profile, "n": len(pairs), "status": "unidentifiable"})
            continue
        def objective(beta):
            eta = design @ beta
            return float(np.sum(np.logaddexp(0, eta)-y*eta)), design.T @ (special.expit(eta)-y)
        fit = optimize.minimize(objective, np.zeros(design.shape[1]), jac=True, method="BFGS")
        if not fit.success or np.max(np.abs(fit.x)) > 25:
            results.append({"profile": profile, "n": len(pairs), "status": "nonconvergence_or_separation"})
            continue
        predicted = special.expit(design @ fit.x)
        variance = np.linalg.pinv(design.T @ (predicted[:, None]*(1-predicted[:, None])*design))
        std = np.sqrt(variance[1, 1])
        for dataset in datasets:
            observed_sl = [sloc for d, sloc, _ in pairs if d == dataset]
            if not observed_sl:
                continue
            for sloc in np.geomspace(min(observed_sl), max(observed_sl), 50):
                x = np.array([1, np.log(sloc), *[int(dataset == d) for d in datasets[1:]]])
                eta, error = x @ fit.x, np.sqrt(x @ variance @ x)
                results.append({"profile": profile, "n": len(pairs), "dataset": dataset, "status": "ok",
                                "coefficient": fit.x[1], "coefficient_se": std,
                                "p": 2*stats.norm.sf(abs(fit.x[1]/std)) if std else None,
                                "sloc": sloc, "prediction": special.expit(eta),
                                "ci_low": special.expit(eta-1.96*error), "ci_high": special.expit(eta+1.96*error)})
    return results


def analyze(root):
    rng = np.random.default_rng(SEED)
    tidy = root / "tidy"
    out = root / "summary"
    out.mkdir(parents=True, exist_ok=True)
    samples = list(load(tidy / "samples.csv"))
    groups = group_samples(samples)
    values = defaultdict(dict)
    for row in load(tidy / "measurements_long.csv"):
        if row["level"] == "file":
            key = tuple(row[name] for name in ("dataset", "sample_id", "variant", "stage", "ruff_profile", "ruff_mode"))
            values[key][row["metric"]] = row["value"]

    comparisons, rates, binary, diagnostic = [], [], [], []
    for (dataset, axis, label), identities in groups.items():
        group = {"dataset": dataset, "stratum": axis, "label": label}
        def get(i, variant, stage="embedded", profile="", mode=""):
            return values.get((dataset, i, variant, stage, profile, mode), {})
        for variant in VARIANTS:
            if variant.startswith("acw"):
                cognitive = [(get(i, name).get("complexipy_mean") for name in ("original", "sew", variant))
                             for i in identities]
                pairs = [(float(sew) < float(base), float(acw) < float(base))
                         for base, sew, acw in cognitive if None not in (base, sew, acw)]
                acid = pairs.count((False, True))
                reverse = pairs.count((True, False))
                binary.append({**group, "variant": variant, "metric": "complexipy_decrease_vs_sew",
                               "n": len(pairs), "regressions": acid, "recovered": reverse,
                               "mcnemar_p": stats.binomtest(acid, acid+reverse, .5, alternative="greater").pvalue
                               if acid+reverse else 1.})
            for metric in METRICS:
                for profile, mode in (("", ""), ("default", "check"), ("strict", "check"),
                                      ("default", "fix_format"), ("strict", "fix_format")):
                    if metric.startswith("ruff") and not profile:
                        continue
                    if metric.startswith(("cc_", "complexipy_", "mi_", "raw_")) and mode == "check":
                        continue
                    stage = "ruff" if mode == "fix_format" else "embedded"
                    pairs = [(get(i, "original", stage, profile, mode).get(metric),
                              get(i, variant, stage, profile, mode).get(metric)) for i in identities]
                    delta = [float(b)-float(a) for a, b in pairs if a is not None and b is not None]
                    row = {**group, "variant": variant, "metric": metric, "profile": profile, "mode": mode,
                           "excluded": len(identities)-len(delta)}
                    described = statistics(delta, MARGINS.get(metric, .1 if metric == "ruff_group_other" else None), rng)
                    if delta:
                        valid = [(float(a), float(b)) for a, b in pairs if a is not None and b is not None]
                        described.update(mean_original=float(np.mean([a for a, _ in valid])),
                                         mean_variant=float(np.mean([b for _, b in valid])),
                                         median_original=float(np.median([a for a, _ in valid])),
                                         median_variant=float(np.median([b for _, b in valid])))
                    comparisons.append({**row, **described})
                    if metric == "syntax_valid" and not profile:
                        a = delta.count(-1)
                        b = delta.count(1)
                        binary.append({**row, "regressions": a, "recovered": b, "n": len(delta),
                                       "mcnemar_p": stats.binomtest(a, a+b, .5).pvalue if a+b else 1.})
            tests = [get(i, variant, "correctness").get("differential") for i in identities]
            rates.append(proportion({**group, "variant": variant}, "different",
                                    [x == "different" for x in tests if x in ("identical", "different")]))
            for profile in ("default", "strict"):
                if axis == "population":
                    operations = [get(i, variant, "embedded", profile, "check") for i in identities]
                    names = {m for item in operations for m in item if m.startswith(("ruff_added_", "ruff_removed_"))}
                    for name in sorted(names):
                        nonmissing = [item for item in operations if "ruff_total" in item]
                        diagnostic.append({**group, "variant": variant, "profile": profile, "metric": name,
                                           "n": len(nonmissing), "total": sum(int(item.get(name, 0)) for item in nonmissing)})
                detector = "sew_detected_0" if variant == "sew" else f"fixed_{variant}"
                positive = [i for i in identities if get(i, variant).get(detector) == "1"]
                for mode in ("check", "fix", "format", "fix_format"):
                    observed = [get(i, variant, "ruff", profile, mode).get(detector) for i in positive]
                    rates.append(proportion({**group, "variant": variant, "profile": profile, "mode": mode},
                                            "survival", [x == "1" for x in observed if x is not None]))
                    if variant == "sew" and mode == "format":
                        paired = [(get(i, variant, "ruff", profile, "fix").get(detector),
                                   get(i, variant, "ruff", profile, "format").get(detector)) for i in positive]
                        paired = [(a, b) for a, b in paired if a is not None and b is not None]
                        d = paired.count(("1", "0"))
                        e = paired.count(("0", "1"))
                        binary.append({**group, "variant": variant, "profile": profile, "metric": "formatter_vs_fix",
                                       "n": len(paired), "regressions": d, "recovered": e,
                                       "mcnemar_p": stats.binomtest(d, d+e, .5, alternative="greater").pvalue if d+e else 1.})
                for mode in ("check", "fix", "format", "fix_format"):
                    for key in range(3 if variant == "sew" else 1):
                        detector = f"sew_detected_{key}" if variant == "sew" else f"fixed_{variant}"
                        controls = [get(i, "original", "ruff", profile, mode) for i in identities]
                        rates.append(proportion({**group, "variant": variant, "profile": profile, "mode": mode, "key": key},
                                                "false_alarm", [x.get(detector) == "1" for x in controls
                                                if detector in x and x.get(f"sew_evaluable_{key}", "1") == "1"]))
            controls = [get(i, "original") for i in identities]
            for key in range(3 if variant == "sew" else 1):
                detector = f"sew_detected_{key}" if variant == "sew" else f"fixed_{variant}"
                rates.append(proportion({**group, "variant": variant, "mode": "embedded", "key": key},
                                        "false_alarm", [x.get(detector) == "1" for x in controls
                                        if detector in x and x.get(f"sew_evaluable_{key}", "1") == "1"]))
    for sample_set, keys in ((comparisons, ("wilcoxon_p", "tost_p")), (binary, ("mcnemar_p",))):
        families = defaultdict(list)
        for row in sample_set:
            families[(row["dataset"], row["stratum"], row["label"], row.get("profile"), row.get("mode"))].append(row)
        for family in families.values():
            for key in keys:
                holm(family, key, key + "_holm")
    write(out / "paired.csv", comparisons)
    write(out / "proportions.csv", rates)
    write(out / "binary.csv", binary)
    write(out / "diagnostics.csv", diagnostic)
    sizes = {(s["dataset"], s["sample_id"]): float(s["sloc"]) for s in samples if s["structure"] != "script"}
    logistic = [row | {"scope": "pooled"} for row in regression(values, sizes)]
    for dataset in sorted({d for d, _ in sizes}):
        logistic.extend(row | {"scope": dataset} for row in
                        regression(values, {key: value for key, value in sizes.items() if key[0] == dataset}))
    write(out / "logistic.csv", logistic)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    analyze(parser.parse_args().measurements)


if __name__ == "__main__":
    main()
