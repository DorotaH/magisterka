"""Plots based solely on exported study tables."""

import csv
from pathlib import Path
from statistics import median

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np


COLORS = {"original": "#666666", "sew": "#0072B2", "acw_notab": "#E69F00", "acw_full": "#009E73"}
LABELS = {"mercury_eval": "Mercury-eval", "classeval": "ClassEval", "apps": "APPS"}
VARIANTS = ("sew", "acw_notab", "acw_full")
METRICS = {"cc_mean": "Radon CC", "complexipy_mean": "Complexipy", "mi_mi": "MI", "raw_sloc": "SLOC"}


def read(path):
    with path.open(encoding="utf-8", newline="") as stream:
        yield from csv.DictReader(stream)


def save(fig, folder, name, data):
    fig.savefig(folder / f"{name}.pdf")
    fig.savefig(folder / f"{name}.png", dpi=300)
    if data:
        with (folder / f"{name}.csv").open("w", encoding="utf-8", newline="") as stream:
            fields = list(dict.fromkeys(key for row in data for key in row))
            writer = csv.DictWriter(stream, fields)
            writer.writeheader()
            writer.writerows(data)
    plt.close(fig)


def setup(h, w, width=10, height=6):
    fig, axes = plt.subplots(h, w, figsize=(width, height), layout="constrained", squeeze=False)
    for axis in axes.flat:
        axis.grid(alpha=.18)
        axis.set_axisbelow(True)
    return fig, axes


def number(row, key):
    return float(row[key])


def point_interval(axis, row, x, color, y="fraction", horizontal=False):
    value = number(row, y)
    low, high = number(row, "ci_low"), number(row, "ci_high")
    err = [[max(value-low, 0)], [max(high-value, 0)]]
    if horizontal:
        axis.errorbar(value, x, xerr=err, fmt="o", color=color, capsize=3)
    else:
        axis.errorbar(x, value, yerr=err, fmt="o", color=color, capsize=3)


def render_study(root):
    summary = root / "summary"
    out = root / "figures"
    out.mkdir(parents=True, exist_ok=True)
    samples = {(x["dataset"], x["sample_id"]): x for x in read(root / "tidy/samples.csv")}
    def main(row):
        return row.get("stratum") == "population" and row.get("label") == "main"
    paired = [row for row in read(summary / "paired.csv") if main(row) and int(row["n"]) > 0]
    rates = [row for row in read(summary / "proportions.csv") if row.get("n") not in ("", "0")]
    diagnostics = [row for row in read(summary / "diagnostics.csv") if main(row)]
    raw = {}
    after_ruff = {}
    for row in read(root / "tidy/measurements_long.csv"):
        if row["level"] == "file":
            if (row["stage"], row["variant"], row["ruff_mode"], row["metric"]) == ("ruff", "sew", "fix_format", "sew_detected_0"):
                after_ruff[(row["dataset"], row["sample_id"], row["ruff_profile"])] = row["value"]
            if row["stage"] in ("embedded", "correctness"):
                raw[(row["dataset"], row["sample_id"], row["variant"], row["metric"], row["ruff_profile"])] = row["value"]

    def values(dataset, variant, metric, profile=""):
        return [(sample, float(raw[(dataset, sample, variant, metric, profile)]))
                for d, sample in samples if d == dataset and samples[d, sample]["structure"] != "script"
                and (d, sample, variant, metric, profile) in raw]

    fig2, a2 = setup(4, 3, 12, 10)
    fig3, a3 = setup(4, 3, 12, 10)
    scatter = []
    rng = np.random.default_rng(20261118)
    for i, (metric, label) in enumerate(METRICS.items()):
        for j, (dataset, dataset_name) in enumerate(LABELS.items()):
            one, two = a2[i, j], a3[i, j]
            base = dict(values(dataset, "original", metric))
            n_labels = []
            for k, variant in enumerate(VARIANTS):
                current = dict(values(dataset, variant, metric))
                ids = sorted(base.keys() & current.keys())
                b = [base[x] for x in ids]
                c = [current[x] for x in ids]
                n_labels.append(f"{variant}\n(n={len(b)})")
                if not b:
                    continue
                delta = np.array(c)-b
                if len(set(delta)) > 1:
                    artists = one.violinplot(delta, positions=[k], widths=.75, showextrema=False)
                    for body in artists["bodies"]:
                        body.set_facecolor(COLORS[variant])
                one.scatter(k+rng.uniform(-.12, .12, len(delta)), delta, s=7, alpha=.25, color=COLORS[variant])
                match = next((row for row in paired if row["metric"] == metric and row["variant"] == variant
                              and row["dataset"] == dataset and not row["profile"]), None)
                if match:
                    point_interval(one, match, k, COLORS[variant], y="median_delta")
                two.scatter(b, c, color=COLORS[variant], s=9, alpha=.3, label=f"{variant} (n={len(b)})")
                scatter.extend(dict(dataset=dataset, variant=variant, sample_id=x, metric=metric,
                                    before=y, after=z, delta=z-y) for x, y, z in zip(ids, b, c))
            one.set(xticks=range(3), xticklabels=n_labels, ylabel=f"Δ {label}", title=dataset_name)
            one.axhline(0, color="gray", linewidth=.8)
            lo, hi = two.get_xlim()
            deux = two.get_ylim()
            ll, hh = min(lo, deux[0]), max(hi, deux[1])
            two.plot([ll, hh], [ll, hh], color="gray", linewidth=.8)
            two.set(xlabel=f"{label}, oryginał", ylabel="Po znakowaniu", title=dataset_name)
            if two.collections:
                two.legend(fontsize=6)
    fig2.suptitle("Zmiany parowane po znakowaniu. Mediana i bootstrapowy 95% PU")
    fig3.suptitle("Wyniki poszczególnych próbek przed znakowaniem i po nim")
    save(fig2, out, "F2", scatter)
    save(fig3, out, "F3", scatter)

    families = ("F", "E9", "B", "UP", "SIM", "I", "E", "W")
    fig, axes = setup(2, 3, 12, 6)
    matrix_rows = []
    for i, profile in enumerate(("default", "strict")):
        for j, (dataset, label) in enumerate(LABELS.items()):
            axis = axes[i, j]
            matrix = []
            plotted_n = set()
            for variant in VARIANTS:
                result = {row["metric"]: int(row["total"]) for row in diagnostics if row["dataset"] == dataset
                          and row["variant"] == variant and row["profile"] == profile}
                plotted_n.update(int(row["n"]) for row in diagnostics if row["dataset"] == dataset
                                 and row["variant"] == variant and row["profile"] == profile)
                for direction in ("added", "removed"):
                    row = [result.get(f"ruff_{direction}_{family}", 0) for family in families]
                    matrix.append(row if direction == "added" else [-x for x in row])
                    matrix_rows.extend(dict(dataset=dataset, profile=profile, variant=variant, family=f,
                                            direction=direction, count=count) for f, count in zip(families, row))
            lim = max(np.abs(matrix).max(), 1)
            axis.imshow(matrix, cmap="RdBu", vmin=-lim, vmax=lim, aspect="auto")
            for y, line in enumerate(matrix):
                for x, val in enumerate(line):
                    axis.text(x, y, str(val), ha="center", va="center", fontsize=6,
                              color="white" if abs(val) > lim*.64 else "black")
            axis.set(xticks=range(len(families)), xticklabels=families, yticks=range(6),
                     yticklabels=[f"{v} {d}" for v in VARIANTS for d in ("+", "−")],
                     title=f"{label}, {profile}, n={max(plotted_n, default=0)}")
            axis.tick_params(axis="y", labelsize=7)
    fig.suptitle("Diagnostyki Ruffa dodane (+) i usunięte (−) względem oryginału")
    save(fig, out, "F4", matrix_rows)

    fig, axes = setup(1, 3, 12, 4)
    tab_rows = []
    for axis, (dataset, label) in zip(axes.flat, LABELS.items()):
        for i, variant in enumerate(("original", "acw_notab", "acw_full")):
            for k, metric in enumerate(("ruff_total", "ruff_W191")):
                x = [v for _, v in values(dataset, variant, metric, "strict")]
                total = values(dataset, variant, "ruff_total", "strict")
                if not total:
                    continue
                if k:
                    by_id = dict(values(dataset, variant, metric, "strict"))
                    x = [y-by_id.get(s, 0) for s, y in total]
                means = np.concatenate([rng.choice(x, size=(1000, len(x))).mean(axis=1) for _ in range(10)])
                estimate = dict(dataset=dataset, variant=variant, exclude_w191=bool(k), n=len(x),
                                fraction=np.mean(x), ci_low=np.quantile(means, .025), ci_high=np.quantile(means, .975))
                tab_rows.append(estimate)
                pos = i+(.16 if k else -.16)
                axis.bar(pos, estimate["fraction"], width=.28, alpha=.5 if k else .9, color=COLORS[variant])
                point_interval(axis, estimate, pos, COLORS[variant])
        counts = [row["n"] for row in tab_rows if row["dataset"] == dataset]
        axis.set(xticks=range(3), xticklabels=["oryginał", "bez 45", "pełne"], ylim=(0, None),
                 title=f"{label}, n={max(counts, default=0)}", ylabel="Średnia liczba diagnostyk")
    common_top = max(axis.get_ylim()[1] for axis in axes.flat)
    for axis in axes.flat:
        axis.set_ylim(0, common_top)
    fig.suptitle("Ruff strict, reguła 45. Jaśniejsze słupki pomijają W191. 95% PU bootstrap")
    save(fig, out, "F5", tab_rows)

    fig, axes = setup(2, 3, 12, 6)
    invasion = []
    for i, metric in enumerate(("line_similarity", "changed_lines")):
        for j, (dataset, label) in enumerate(LABELS.items()):
            axis = axes[i, j]
            for variant in VARIANTS:
                measured = values(dataset, variant, metric)
                if measured:
                    axis.ecdf([x for _, x in measured], color=COLORS[variant],
                              label=f"{variant} (n={len(measured)})")
                invasion.extend(dict(dataset=dataset, variant=variant, sample_id=s, metric=metric, value=x)
                                for s, x in measured)
            axis.set(title=label, xlabel="Podobieństwo liniowe" if not i else "Zmienione linie",
                     ylabel="Dystrybuanta empiryczna")
            axis.legend(fontsize=6)
    save(fig, out, "F6", invasion)

    for figure, measure in (("F7", "survival"), ("F10", "false_alarm")):
        source = [x for x in rates if main(x) and x["measure"] == measure and
                  (x.get("mode") == "embedded" if figure == "F10" else True)]
        fig, axes = setup(1 if figure == "F10" else 2, 3, 12, 3 if figure == "F10" else 6)
        for i, profile in enumerate(("",) if figure == "F10" else ("default", "strict")):
            for j, (dataset, label) in enumerate(LABELS.items()):
                axis = axes[i, j]
                modes = ("embedded",) if figure == "F10" else ("check", "fix", "format", "fix_format")
                for x, mode in enumerate(modes):
                    selected = [row for row in source if row["dataset"] == dataset and row.get("profile", "") == profile
                                and row.get("mode") == mode]
                    for k, row in enumerate(selected):
                        pos = x+(k-(len(selected)-1)/2)*.15
                        axis.bar(pos, float(row["fraction"]), width=.13, color=COLORS[row["variant"]], alpha=.65)
                        point_interval(axis, row, pos, COLORS[row["variant"]])
                        axis.annotate(row["n"], (pos, float(row["fraction"])), fontsize=6, xytext=(0, 5),
                                      textcoords="offset points", ha="center")
                axis.set(ylim=(0, 1.08), xticks=range(len(modes)), xticklabels=modes,
                         title=f"{label} {profile}", ylabel="Odsetek")
        fig.legend(handles=[Patch(color=COLORS[v], label=v) for v in VARIANTS], loc="outside lower center", ncol=3)
        fig.suptitle(("Przeżywalność znaku" if figure == "F7" else "Fałszywe alarmy SEW i punkty stałe ACW")
                     + ", 95% PU Wilsona, liczebności przy punktach")
        save(fig, out, figure, source)

    logistic = list(read(summary / "logistic.csv"))
    fig, axes = setup(1, 2, 10, 4)
    bins = []
    for axis, profile in zip(axes.flat, ("default", "strict")):
        fitted = [r for r in logistic if r.get("status") == "ok" and r["profile"] == profile and r.get("scope", "pooled") == "pooled"]
        for j, (dataset, label) in enumerate(LABELS.items()):
            color = ("#0072B2", "#D55E00", "#009E73")[j]
            seq = [r for r in fitted if r["dataset"] == dataset]
            if seq:
                x, y, lo, hi = ([float(r[k]) for r in seq] for k in ("sloc", "prediction", "ci_low", "ci_high"))
                axis.plot(x, y, label=label, color=color)
                axis.fill_between(x, lo, hi, alpha=.18, color=color)
            for band in ("<20", "20–39", "40–99", "≥100"):
                group = [(float(sample["sloc"]), after_ruff[d, sid, profile] == "0")
                         for (d, sid), sample in samples.items() if d == dataset and sample["structure"] != "script"
                         and sample["sloc_band"] == band and raw.get((d, sid, "sew", "sew_detected_0", "")) == "1"
                         and (d, sid, profile) in after_ruff]
                if not group:
                    continue
                n = len(group)
                x = median(sloc for sloc, _ in group)
                fraction = sum(lost for _, lost in group)/n
                z = 1.959964
                d = 1+z*z/n
                c = (fraction+z*z/(2*n))/d
                w = z*np.sqrt(fraction*(1-fraction)/n+z*z/(4*n*n))/d
                point = dict(profile=profile, dataset=dataset, sloc=x, n=n, fraction=fraction,
                             ci_low=max(0,c-w), ci_high=min(1,c+w), row_type="sloc_band", band=band)
                bins.append(point)
                point_interval(axis, point, x, color)
                axis.annotate(str(n), (x, fraction), xytext=(4, 4), textcoords="offset points", fontsize=6)
        if fitted:
            axis.legend()
        axis.set(xscale="log", ylim=(0, 1.05), xlabel="SLOC (skala log)", ylabel="Prawdopodobieństwo zaniku", title=profile)
    fig.suptitle("Zanik SEW po Ruffie. Punkty i 95% PU Wilsona, model z pasmem 95% PU")
    save(fig, out, "F8", [r | {"row_type": "logistic"} for r in logistic] + bins)

    fig, axes = setup(1, 3, 12, 4)
    correct = []
    for axis, (dataset, label) in zip(axes.flat, LABELS.items()):
        for i, variant in enumerate(VARIANTS):
            bottom = 0
            counts = {k: 0 for k in ("identical", "different", "error")}
            for d, s in samples:
                status = raw.get((d, s, variant, "differential", ""))
                if d == dataset and status in counts:
                    counts[status] += 1
            for status, color in zip(counts, ("#009E73", "#D55E00", "#777777")):
                count = counts[status]
                axis.bar(i, count, bottom=bottom, color=color, label=status if i == 0 else None)
                correct.append(dict(dataset=dataset, variant=variant, status=status, n=count))
                bottom += count
            axis.text(i, bottom, str(bottom), ha="center", va="bottom")
        axis.set(xticks=range(3), xticklabels=VARIANTS, title=label, ylabel="Liczba próbek")
        axis.legend(fontsize=7)
    save(fig, out, "F9", correct)

    fig, axes = setup(1, len(METRICS), 13, 5)
    forest = [r for r in paired if r["metric"] in METRICS and not r["profile"]]
    for axis, metric in zip(axes.flat, METRICS):
        chosen = [r for r in forest if r["metric"] == metric]
        axis.axvline(0, color="gray", linewidth=.8)
        ticklabels = []
        for i, r in enumerate(chosen):
            cols = {**r, "ci_low": r["mean_ci_low"], "ci_high": r["mean_ci_high"]}
            point_interval(axis, cols, i, COLORS[r["variant"]], y="mean_delta", horizontal=True)
            ticklabels.append(f'{LABELS[r["dataset"]]} {r["variant"]} ({r["n"]})')
        if chosen and chosen[0]["equivalence_margin"]:
            margin = float(chosen[0]["equivalence_margin"])
            axis.axvline(margin, color="gray", linestyle="dotted")
            axis.axvline(-margin, color="gray", linestyle="dotted")
        axis.set(yticks=range(len(chosen)), yticklabels=ticklabels, title=METRICS[metric], xlabel="Średnia zmiana")
        axis.tick_params(axis="y", labelsize=6)
    fig.suptitle("Efekty parowane. Średnia i 95% PU bootstrap")
    save(fig, out, "F11", forest)
