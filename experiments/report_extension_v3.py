"""Produce extension v3 summaries, thesis comparison, and figures from CSV."""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from analyze_extension_v3 import MAIN, write
from select_extension_classeval import EXTENSION

VARIANTS = {"sew": "SEW", "acw_notab": "ACW bez reguły 45", "acw_full": "Pełne ACW"}
LABELS = {"mercury_train": "Mercury-train", "leetcode_test": "LeetCodeDataset test",
          "mercury_eval": "Mercury-eval", "classeval": "ClassEval ludzki",
          "apps": "APPS", "classeval_llama31_8b": "Llama", "classeval_qwen25c7b": "Qwen",
          "all": "Łącznie"}
COLORS = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00"]


def read(path):
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def select(rows, **keys):
    return [row for row in rows if all(row[key] == value for key, value in keys.items())]


def number(value):
    return f"{value:.3f}".replace(".", ",")


def event(row):
    if row is None or not int(row["n"]):
        return "—"
    percent = f'{100 * float(row["fraction"]):.1f}'.replace(".", ",")
    return f'{row["events"]}/{row["n"]} ({percent}%)'


def count_rows(items):
    if not items:
        return None
    n = sum(int(row["n"]) for row in items)
    events = sum(int(row["events"]) for row in items)
    return {"n": n, "events": events, "fraction": events/n if n else None}


def weighted(rows):
    numerator = sum(float(row["mean_delta"]) * int(row["n"])
                    for row in rows if row["mean_delta"])
    denominator = sum(int(row["n"]) for row in rows if row["mean_delta"])
    return number(numerator/denominator) if denominator else "—"


def panel(rates, pairs, variant, legacy=False):
    relevant = select(rates, variant=variant)
    def proportion(measure, profile="", mode=""):
        return event(count_rows(select(relevant, measure=measure, profile=profile, mode=mode)))

    def delta(metric, profile="", mode=""):
        return weighted(select(pairs, variant=variant, metric=metric, profile=profile, mode=mode))

    syntax = proportion("syntax_error")
    changed = proportion("changed")
    if legacy:
        syntax_rows = select(pairs, variant=variant, metric="syntax_valid", profile="", mode="")
        n = sum(int(row["n"]) for row in syntax_rows)
        errors = sum(round((1-float(row["mean_variant"])) * int(row["n"]))
                     for row in syntax_rows if row["mean_variant"])
        syntax = event({"n": n, "events": errors, "fraction": errors/n if n else None})
    return (changed, delta("ruff_total", "default", "check"), delta("ruff_total", "strict", "check"),
            delta("cc_mean"), delta("complexipy_mean"), delta("mi_mi"), syntax,
            proportion("different"), proportion("survival", "default", "fix_format"),
            proportion("survival", "strict", "fix_format"))


TABLE_HEADER = ("Próba", "Wariant", "Zmienione", "Δ Ruff default", "Δ Ruff strict", "Δ CC",
              "Δ Complexipy", "Δ MI", "Błędy składni", "Różnice w obserwacji",
              "Przeżywalność default", "Przeżywalność strict")


def table(rows):
    lines = ["| " + " | ".join(TABLE_HEADER) + " |",
             "|" + "|".join(["---"] * len(TABLE_HEADER)) + "|"]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(lines)


def summarize_layer(root, layer):
    directory = root / layer
    rates = read(directory / "summary/proportions.csv")
    pairs = read(directory / "summary/paired.csv")
    scopes = dict.fromkeys((row["dataset"], row["label"]) for row in rates)
    lines = []
    for dataset, label in scopes:
        name = LABELS[dataset] if label == "main" else f"{LABELS[dataset]} (skrypty)"
        ratio = select(rates, dataset=dataset, label=label)
        baseline = select(ratio, variant="original", measure="original_pass")
        if baseline:
            lines.append(f"- {name}, zaliczenie testów przez oryginał {event(baseline[0])}.")
    report_rows = list(build_layer_rows(rates, pairs))
    body = "# Podsumowanie\n\n" + table(report_rows) + "\n"
    if lines:
        body += "\n## Poprawność oryginałów\n\n" + "\n".join(lines) + "\n"
    body += "\nPrzeżywalność dotyczy trybu `fix_format` i próbek wykrywalnych po znakowaniu. Δ oznacza średnią zmianę w parze. Pełne mianowniki, przedziały i wyniki wszystkich trybów są w [tabelach CSV](summary/).\n"
    if (directory / "kontrola_zachowania.md").exists():
        body += "\nPorównania zachowania obejmują ślady zależne od zegara. [Kontrole uzupełniające](kontrola_zachowania.md) wyjaśniają różnice czasowe i potwierdzają regresję ACW.\n"
    (directory / "podsumowanie.md").write_text(body, encoding="utf-8")
    notes = [
        "# Wnioski eksploracyjne",
        "",
        ("Porównania dotyczą wyłącznie opisanych zbiorów i zastosowanego potoku. "
         "Brak odnotowanej różnicy oznacza brak zdarzeń w danym mianowniku."),
    ]
    for variant, label in VARIANTS.items():
        both = select(rates, dataset="all", label="main", variant=variant)
        change = count_rows(select(both, measure="changed"))
        syntax = count_rows(select(both, measure="syntax_error"))
        survival = count_rows(select(both, measure="survival", profile="strict", mode="fix_format"))
        conclusion = (f"- {label} zmienił {event(change)} próbek. Błędy składni wystąpiły w "
                      f"{event(syntax)}, a przeżywalność po Ruff strict w trybie `fix_format` "
                      f"wyniosła {event(survival)}.")
        if layer == "warstwa_C":
            conclusion += f' Różny ślad testowy odnotowano w {event(count_rows(select(both, measure="different")))}.'
        notes.extend(("", conclusion))
    if (directory / "kontrola_zachowania.md").exists():
        notes.extend(("", ("Kontrola przy wspólnym czasie wyjaśniła różnice widoczne dla TimeUtils. "
                      "Dla SQLQueryBuilder odtworzono regresję ACW po regule 36. "
                      "[Wyniki kontroli](kontrola_zachowania.md)")))
    (directory / "wnioski.md").write_text("\n".join(notes) + "\n", encoding="utf-8")
    return report_rows


def build_layer_rows(rates, pairs):
    for dataset, label in dict.fromkeys((row["dataset"], row["label"]) for row in rates):
        name = LABELS[dataset] if label == "main" else f"{LABELS[dataset]} (skrypty)"
        for variant, variant_label in VARIANTS.items():
            yield (name, variant_label, *panel(select(rates, dataset=dataset, label=label),
                                                  select(pairs, dataset=dataset, label=label), variant))


def figure(root):
    measures = []
    for layer in ("warstwa_A", "warstwa_C"):
        for row in read(root / layer / "summary/proportions.csv"):
            if (row["dataset"] != "all" and row["label"] == "main" and row["measure"] == "survival"
                    and row["mode"] == "fix_format" and row["fraction"]):
                measures.append(row)
    if not measures:
        return
    path = root / "figures"
    write(path / "F1.csv", measures[0].keys(), measures)
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), layout="constrained", sharey=True)
    datasets = list(dict.fromkeys(row["dataset"] for row in measures))
    width = 0.8 / len(datasets)
    for ax, profile in zip(axes, ("default", "strict")):
        for i, dataset in enumerate(datasets):
            first = True
            for j, variant in enumerate(VARIANTS):
                values = select(measures, dataset=dataset, variant=variant, profile=profile)
                if values:
                    value = values[0]
                    fraction, lo, hi = (float(value[key]) for key in ("fraction", "ci_low", "ci_high"))
                    ax.bar(j - .4 + width*(i+.5), fraction, width, color=COLORS[i],
                           label=LABELS[dataset] if first else None,
                           yerr=[[max(0, fraction-lo)], [max(0, hi-fraction)]], capsize=2)
                    first = False
        ax.set(title=f"Ruff {profile}", xticks=range(len(VARIANTS)),
               xticklabels=("SEW", "ACW bez 45", "ACW"), ylim=(0, 1.06))
        ax.grid(axis="y", alpha=.2)
    axes[0].set_ylabel("Przeżywalność po fix_format")
    handles, labels = axes[0].get_legend_handles_labels()
    if handles:
        fig.legend(handles, labels, loc="outside lower center", ncols=2, frameon=False, fontsize=8)
    fig.savefig(path / "F1.pdf")
    fig.savefig(path / "F1.png", dpi=300)
    plt.close(fig)


def quality_figure(root):
    data = []
    for layer in ("warstwa_A", "warstwa_C"):
        for row in read(root / layer / "summary/paired.csv"):
            if (row["dataset"] != "all" and row["label"] == "main" and row["mean_delta"]
                    and ((row["metric"] == "complexipy_mean" and not row["profile"])
                         or (row["metric"] == "ruff_total" and row["profile"] == "strict"
                             and row["mode"] == "check"))):
                data.append(row)
    if not data:
        return
    folder = root / "figures"
    write(folder / "F2.csv", data[0].keys(), data)
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), layout="constrained")
    datasets = list(dict.fromkeys(row["dataset"] for row in data))
    for ax, (metric, title) in zip(axes, (("complexipy_mean", "Complexipy"),
                                        ("ruff_total", "Diagnostyki Ruff strict"))):
        ax.axvline(0, color="0.6", lw=1)
        for index, dataset in enumerate(datasets):
            points = select(data, dataset=dataset, metric=metric)
            for row in points:
                variant = list(VARIANTS).index(row["variant"])
                location = variant + (index-(len(datasets)-1)/2) * .16
                x, low, high = (float(row[key]) for key in ("mean_delta", "mean_ci_low", "mean_ci_high"))
                ax.hlines(location, low, high, color=COLORS[index])
                ax.plot(x, location, "o", color=COLORS[index],
                        label=LABELS[dataset] if not variant else None)
        ax.set(yticks=range(len(VARIANTS)), yticklabels=VARIANTS.values(),
               xlabel="Średnia zmiana na plik", title=title)
        ax.grid(axis="x", alpha=.2)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncols=2, frameon=False, fontsize=8)
    fig.savefig(folder / "F2.pdf")
    fig.savefig(folder / "F2.png", dpi=300)
    plt.close(fig)


def baseline_changes():
    counts = defaultdict(list)
    with (MAIN / "tidy/measurements_long.csv").open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            if (row["metric"] == "changed" and row["stage"] == "embedded"
                    and row["variant"] in VARIANTS and not row["ruff_profile"]):
                counts[row["dataset"], row["variant"]].append(int(row["value"]))
    return [
        {"dataset": dataset, "variant": variant, "measure": "changed", "profile": "", "mode": "",
         "n": len(values), "events": sum(values), "fraction": sum(values)/len(values)}
        for (dataset, variant), values in counts.items()
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=EXTENSION)
    args = parser.parse_args()
    root = args.output
    result = []
    main_rates = select(read(MAIN / "summary/proportions.csv"), stratum="population")
    main_rates.extend(baseline_changes())
    main_pairs = select(read(MAIN / "summary/paired.csv"), stratum="population")
    detailed = read(MAIN / "tidy/samples.csv")
    for name, baseline in (("Badanie główne", None), ("ClassEval ludzki", "classeval")):
        rates = select(main_rates, dataset=baseline) if baseline else main_rates
        pairs = select(main_pairs, dataset=baseline) if baseline else main_pairs
        n = sum(baseline is None or row["dataset"] == baseline for row in detailed)
        for variant, variant_label in VARIANTS.items():
            result.append((f"{name} (n={n})", variant_label, *panel(rates, pairs, variant, legacy=True)))
    for layer in ("warstwa_A", "warstwa_C"):
        rows = list(summarize_layer(root, layer))
        current = read(root / layer / "summary/proportions.csv")
        for row in rows:
            chosen = next((dataset for dataset, name in LABELS.items() if name == row[0]), None)
            if chosen is None:
                continue
            counts = select(current, dataset=chosen, label="main", measure="changed", variant="sew")
            if chosen == "all" or layer == "warstwa_C":
                result.append((f'{layer.replace("_", " ")} · {row[0]} (n={counts[0]["n"]})', *row[1:]))
    body = """# Porównanie badania głównego i rozszerzenia

Δ oznacza średnią różnicę wariant minus oryginał w parach z pomiarem po obu stronach. Ruff check podano dla obu profili, a przeżywalność dla trybu `fix_format` wśród jednostek z wykrywalnym znakiem przed przetworzeniem. Różnice w obserwacji badania głównego pochodzą z dostępnych porównań różnicowych. Dla warstwy C mianownik ograniczono do oryginałów zaliczających test i wariantów z porównywalną obserwacją. Kreska oznacza brak oszacowania. Różnice śladów wynikające z odczytów zegara i potwierdzoną regresję ACW opisano w [kontrolach uzupełniających](warstwa_C/kontrola_zachowania.md).

"""
    (root / "porownanie.md").write_text(body + table(result) + "\n", encoding="utf-8")
    write(root / "porownanie.csv", TABLE_HEADER, (dict(zip(TABLE_HEADER, row, strict=True)) for row in result))
    figure(root)
    quality_figure(root)


if __name__ == "__main__":
    main()
