"""Render the dataset profiling figure and export its underlying values."""

import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profiles", type=Path)
    parser.add_argument("--measurements", type=Path)
    args = parser.parse_args()

    if args.measurements:
        names = {"mercury_eval": "Mercury-eval", "classeval": "ClassEval", "apps": "APPS"}
        profiles = []
        for dataset, label in names.items():
            levels = json.loads((args.profiles / f"levels_{dataset}.json").read_text(encoding="utf-8"))
            profiles.append({"dataset": label, **levels["selected"]})
        profiles.extend(json.loads((args.profiles / f"profil_{name}.json").read_text(encoding="utf-8"))
                        for name in ("bigcodebench", "codecontests"))
        figure_folder = args.measurements / "figures"
        figure_folder.mkdir(parents=True, exist_ok=True)
        basename = "F1"
    else:
        profiles = [json.loads(path.read_text(encoding="utf-8"))
                    for path in sorted(args.profiles.glob("profil_*.json"))]
        figure_folder = args.profiles
        basename = "fig_F1"
    colors = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#56B4E9"]
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), layout="constrained")
    fig.supxlabel("Pionowe znaczniki pokazują medianę. W legendach podano liczebność.")
    axes[0].set(xlabel="SLOC na plik (skala logarytmiczna)", xscale="log")
    axes[1].set(xlabel="Complexipy na funkcję")
    with (figure_folder / f"{basename}.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["dataset", "sample_id", "unit", "metric", "value", "included"])
        for index, profile in enumerate(profiles):
            measures = {"sloc": [], "complexipy": []}
            name = profile["dataset"]
            for sample in profile["samples"]:
                sample_id = sample["sample_id"]
                if "raw" in sample:
                    sloc = sample["raw"]["sloc"]
                    writer.writerow([name, sample_id, "file", "sloc", sloc, sloc > 0])
                    if sloc > 0:
                        measures["sloc"].append(sloc)
                for function in sample.get("complexipy", []):
                    score = function["complexity"]
                    unit = f'{function["name"]}:{function["line"]}'
                    writer.writerow([name, sample_id, unit, "complexipy", score, True])
                    measures["complexipy"].append(score)
            for axis, (metric, values) in zip(axes, measures.items()):
                if values:
                    color = colors[index % len(colors)]
                    axis.ecdf(values, label=f"{name} (n={len(values)})", color=color)
                    median = profile["summary"][metric]["median"]
                    if metric != "sloc" or median > 0:
                        axis.vlines(median, 0, 0.5, colors=color, linestyles="dotted")
    for axis in axes:
        axis.set(ylabel="Dystrybuanta empiryczna", ylim=(0, 1.03))
        axis.grid(alpha=0.2)
        axis.legend(fontsize=8, loc="lower right")
    fig.savefig(figure_folder / f"{basename}.pdf")
    fig.savefig(figure_folder / f"{basename}.png", dpi=300)
    plt.close(fig)
    if args.measurements:
        from study_figures import render_study
        render_study(args.measurements)



if __name__ == "__main__":
    main()
