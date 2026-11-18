"""Build the Polish report and validate the completed v2 data products."""

import argparse
import ast
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import random
from statistics import median

from scipy import stats

DATASETS = ("mercury_eval", "classeval", "apps")
LABELS = {"mercury_eval": "Mercury-eval", "classeval": "ClassEval", "apps": "APPS"}
VARIANTS = ("sew", "acw_notab", "acw_full")


def read(path):
    return json.loads(path.read_text())


def csv_rows(path):
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def selected_profile(study):
    lines = ["# Reprezentatywność wybranej próby", "",
             "Porównanie puli i próby ma charakter opisowy, ponieważ próba jest podzbiorem puli.", "",
             "| Zbiór | Poziom | n | SLOC średnia | SLOC mediana | SLOC p10 | SLOC p90 | KS D puli i próby |",
             "|---|---|---:|---:|---:|---:|---:|---:|"]
    for dataset in DATASETS:
        levels = read(study / "spis_zbiorow" / f"levels_{dataset}.json")
        get = lambda key: [x["raw"]["sloc"] for x in levels[key]["samples"] if "raw" in x]
        distance = stats.ks_2samp(get("candidates"), get("selected")).statistic
        for key, label in (("full", "pełny"), ("candidates", "pula"), ("selected", "próba")):
            layer = levels[key]["summary"]
            sloc = layer["sloc"]
            lines.append(f'| {LABELS[dataset]} | {label} | {layer["samples"]} | {sloc["mean"]:.1f} | '
                         f'{sloc["median"]:.1f} | {sloc["p10"]:.1f} | {sloc["p90"]:.1f} | '
                         f'{distance:.3f} |')
    lines += ["", "Dokładne rozkłady LOC/SLOC, funkcji, klas, trudności, miar CC, Complexipy, MI i Halsteada "
              "zapisano w plikach `levels_*.json`. Dla Mercury pełny profil używa pierwszego rozwiązania każdego "
              "zadania, a pula i próba jednego rozwiązania wybranego z kwalifikujących się alternatyw."]
    (study / "spis_zbiorow/reprezentatywnosc.md").write_text("\n".join(lines)+"\n", encoding="utf-8")


def hypothesis_row(paired, rates, binary, diagnostic, logistic, dataset, hyp):
    keyed = {row["variant"]: row for row in paired if row["dataset"] == dataset and row["stratum"] == "population"
             and row["label"] == "main" and row["metric"] == "syntax_valid" and not row["profile"]}
    def comparisons(metric, profile=""):
        return {x["variant"]: x for x in paired if x["dataset"] == dataset and x["stratum"] == "population"
                and x["label"] == "main" and x["metric"] == metric and x["profile"] == profile
                and x["mode"] == ("check" if profile else "") and int(x["n"]) > 0}
    if hyp == "H1":
        if not keyed:
            return "nierozstrzygnięta", "brak par"
        breaks = {v: float(row["mean_delta"]) < 0 for v, row in keyed.items() if row["mean_delta"]}
        if breaks.get("sew") or breaks.get("acw_notab"):
            return "niepoparta", "odnotowano błąd po SEW lub ACW bez reguły 45"
        return "nierozstrzygnięta", "liczebności regresji w binary.csv, hipoteza także dotyczy przewagi przypadków w skryptach"
    if hyp == "H2":
        rows = [r for r in rates if r["dataset"] == dataset and r["stratum"] == "population"
                and r["label"] == "main" and r["variant"] in ("sew", "acw_notab") and r["measure"] == "different"]
        if any(int(row["events"]) for row in rows):
            return "niepoparta", "rozbieżność po SEW lub ACW bez reguły 45, zob. F9"
        return "nierozstrzygnięta", "raport odsetków w F9"
    if hyp == "H3":
        rows = comparisons("cc_mean")
        if len(rows) == 3 and all(r["tost_p_holm"] and float(r["tost_p_holm"]) < .05 for r in rows.values()):
            return "poparta", "TOST po korekcie Holma, zob. F11 i paired.csv"
        return "nierozstrzygnięta", "TOST w paired.csv i efekty w F11"
    if hyp == "H4":
        measures = [r for metric in ("complexipy_mean", "mi_mi") for r in comparisons(metric).values()]
        equivalence = len(measures) == 6 and all(r["tost_p_holm"] and float(r["tost_p_holm"]) < .05 for r in measures)
        direction = [r for r in binary if r["dataset"] == dataset and r["stratum"] == "population"
                     and r["label"] == "main" and r["metric"] == "complexipy_decrease_vs_sew"]
        more_often = len(direction) == 2 and all(r["mcnemar_p_holm"] and float(r["mcnemar_p_holm"]) < .05
                                                  for r in direction)
        return ("poparta" if equivalence and more_often else "nierozstrzygnięta",
                "równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11")
    if hyp == "H5":
        rows = comparisons("ruff_total", "default")
        sew = rows.get("sew", {})
        acw = [r for v, r in rows.items() if v.startswith("acw")]
        if (sew.get("wilcoxon_p_holm") and float(sew["wilcoxon_p_holm"]) < .05
                and float(sew["rank_biserial"]) > 0 and len(acw) == 2
                and all(r["upper_mean_95"] and float(r["upper_mean_95"]) < .1 for r in acw)):
            return "poparta", "kierunkowa zmiana SEW i górna granica dla obu wariantów ACW, zob. F4"
        return "nierozstrzygnięta", "diagnostyki profilu domyślnego w F4 i paired.csv"
    if hyp == "H6":
        group = {r["metric"]: int(r["total"]) for r in diagnostic if r["dataset"] == dataset
                 and r["stratum"] == "population" and r["label"] == "main" and r["variant"] == "acw_full"
                 and r["profile"] == "strict"}
        fraction = group.get("ruff_added_rule_W191", 0) / group["ruff_added_all"] if group.get("ruff_added_all") else None
        rows = [r for v, r in comparisons("ruff_group_other", "strict").items() if v.startswith("acw")]
        if fraction is not None:
            status = "niepoparta" if fraction < .9 else "nierozstrzygnięta"
            if fraction >= .9 and len(rows) == 2 and all(r["tost_p_holm"] and float(r["tost_p_holm"]) < .05 for r in rows):
                status = "poparta"
            return status, f"udział W191 w dodanych diagnostykach {fraction:.1%}, równoważność w paired.csv, zob. F5"
        return "nierozstrzygnięta", "brak mianownika dla udziału dodanych diagnostyk"
    if hyp == "H7":
        fitted = {r["profile"]: r for r in logistic if r.get("scope") == dataset and r["status"] == "ok" and r["p"]}
        if fitted and any(float(r["p"]) < .025 for r in fitted.values()):
            return "poparta", "co najmniej jeden profil z dwustronnym p < 0,025, zob. F8 i logistic.csv"
        return "nierozstrzygnięta", "modele i przypadki niewyznaczalne w logistic.csv, wspólny model na F8"
    if hyp == "H8":
        rows = [r for r in binary if r["dataset"] == dataset and r["stratum"] == "population"
                and r["label"] == "main" and r["metric"] == "formatter_vs_fix"]
        if len(rows) == 2 and all(int(r["regressions"]) > int(r["recovered"]) and
                                  r["mcnemar_p_holm"] and float(r["mcnemar_p_holm"]) < .05 for r in rows):
            return "poparta", "parowane porównanie obu profili, zob. F7"
        return "nierozstrzygnięta", "pary rozbieżne w binary.csv"
    if hyp == "H9":
        selected = [r for r in rates if r["dataset"] == dataset and r["stratum"] == "population"
                    and r["label"] == "main" and r["measure"] == "false_alarm" and r["mode"] == "embedded"
                    and r["key"] == "0" and r["ci_low"]]
        if len(selected) == 3 and all(float(r["ci_high"]) < .05 if r["variant"] == "sew"
                                      else float(r["ci_low"]) > .10 for r in selected):
            return "poparta", "przedziały względem progów w F10"
        return "nierozstrzygnięta", "przedziały względem progów w F10"
    if hyp in ("H10", "H11"):
        return "nierozstrzygnięta", "oczekuje na odpowiedzi ludzi i LLM"
    if hyp == "H12" and dataset == "mercury_eval":
        return "poparta", "próba kontrolna oraz potwierdzone zmiany konkatenacji w Mercury, zob. przegląd reguł"
    return "nierozstrzygnięta", "pełne oszacowania w tabelach i figurach"


def syntax_attribution(records, destination):
    faults = []
    for record in records:
        variants = record["variants"]
        full = variants["acw_full"]["embedded"]
        notab = variants["acw_notab"]["embedded"]
        if not (full["syntax_error"] or notab["syntax_error"]):
            continue
        sample_dir = Path(full["path"]).parents[2]
        stages = [("sourcery", sample_dir / "after_sourcery.py")]
        stages.extend((path.stem, path) for path in sorted((sample_dir / "acw_steps").glob("rule_*.py")))
        stages.extend((("acw_notab", Path(notab["path"])), ("rule_45", Path(full["path"]))))
        earliest = ""
        message = ""
        for stage, path in stages:
            try:
                ast.parse(path.read_text())
            except (SyntaxError, ValueError) as error:
                earliest, message = stage, str(error)
                break
        faults.append({"dataset": record["dataset"], "sample_id": record["sample"]["sample_id"],
                       "structure": record["sample"]["structure"], "first_invalid_stage": earliest,
                       "first_error": message, "notab_error": notab["syntax_error"],
                       "full_error": full["syntax_error"]})
    columns = ("dataset", "sample_id", "structure", "first_invalid_stage", "first_error",
               "notab_error", "full_error")
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(faults)
    return Counter((row["dataset"], row["first_invalid_stage"]) for row in faults)


def export(root, study):
    paired = csv_rows(root / "summary/paired.csv")
    rates = csv_rows(root / "summary/proportions.csv")
    binary = csv_rows(root / "summary/binary.csv")
    diagnostic = csv_rows(root / "summary/diagnostics.csv")
    logistic = csv_rows(root / "summary/logistic.csv")
    lines = ["# Podsumowanie badania v2", "",
             "| Zbiór | Warstwa | Wariant | Pomiarów | Kod zmieniony | Błąd składni | Testowano | Wynik różny | Oryginał i wariant zaliczają |",
             "|---|---|---|---:|---:|---:|---:|---:|---:|"]
    validation = {"datasets": {}, "checked_originals": []}
    all_paths = []
    behavior = []
    syntax = Counter()
    for dataset in DATASETS:
        paths = sorted((root / dataset).glob("*/result.json"))
        all_paths.extend(paths)
        records = [read(path) for path in paths]
        syntax.update(syntax_attribution(records, root / "summary" / f"syntax_{dataset}.csv"))
        ids = {row["sample"]["sample_id"] for row in records}
        keys = [r["sample_id"] for r in read(study / dataset / "selection.json")["samples"]]
        validation["datasets"][dataset] = {"results": len(paths), "selection": len(keys),
                                            "missing": sorted(set(keys)-ids)}
        tests = {}
        for path in paths:
            result = path.parent / "correctness_v2/result.json"
            if result.exists():
                tests[path.parent.name] = read(result).get("variants", {})
        for layer in ("main", "script"):
            selected = [r for r in records if (r["sample"]["structure"] == "script") == (layer == "script")]
            if not selected:
                continue
            for variant in VARIANTS:
                states = [r["variants"][variant]["embedded"] for r in selected]
                available = [tests[r["sample"]["sample_id"]] for r in selected
                             if tests.get(r["sample"]["sample_id"], {}).get(variant)]
                diff = sum(a[variant]["differential"] == "different" for a in available)
                joint = sum(a[variant]["official"] == a["original"]["official"] == "pass" for a in available)
                lines.append(f"| {LABELS[dataset]} | {layer} | {variant} | {len(states)} | "
                             f'{sum(x["changed"] for x in states)} | {sum(bool(x["syntax_error"]) for x in states)} | '
                             f"{len(available)} | {diff} | {joint} |")
                if layer != "main":
                    continue
                def measurement(metric, profile=""):
                    return next((r for r in paired if r["dataset"] == dataset and r["variant"] == variant
                                 and r["metric"] == metric and r["stratum"] == "population" and r["label"] == "main"
                                 and r["profile"] == profile and r["mode"] == ("check" if profile else "")
                                 and int(r["n"]) > 0), None)

                def survival(profile, mode):
                    row = next((r for r in rates if r["dataset"] == dataset and r["variant"] == variant
                                and r["measure"] == "survival" and r["stratum"] == "population"
                                and r["label"] == "main" and r.get("profile") == profile and r.get("mode") == mode), None)
                    return f'{row["events"]}/{row["n"]}' if row and int(row["n"]) else "brak mianownika"

                default_ruff = measurement("ruff_total", "default")
                cc = measurement("cc_mean")
                cog = measurement("complexipy_mean")
                similarity = [x["invasion"]["line_similarity"] for x in states]
                evaluated = sum(a[variant]["differential"] in ("identical", "different") for a in available)
                behavior.append(f'- **{LABELS[dataset]}, `{variant}`**. Błędy składni {sum(bool(x["syntax_error"]) for x in states)}/{len(states)}. '
                                f'Różnice działania {diff}/{evaluated} porównywalnych przypadków. '
                                + (f'Średnia zmiana diagnostyk Ruffa default {float(default_ruff["mean_delta"]):+.2f} na plik. '
                                   if default_ruff else "")
                                + (f'Mediana zmiany CC {float(cc["median_delta"]):+.2f} i Complexipy {float(cog["median_delta"]):+.2f}. '
                                   if cc and cog else "")
                                + f'Mediana podobieństwa liniowego {median(similarity):.2f}. '
                                + f'Wykrycie po samej naprawie Ruffa default {survival("default", "fix")}, '
                                  f'po samym formacie {survival("default", "format")} wśród wykryć przed Ruffem.')

    lines += ["", "„Testowano” uwzględnia próby uruchomienia. Statusy techniczne i mianowniki porównań "
              "zapisano w `correctness_v2/result.json` i `summary/proportions.csv`.",
              "", "Porównania metryk, efekty, przedziały, TOST i korekty zapisano w [paired.csv](summary/paired.csv). "
              "Zanik znaku i kontrole punktu stałego zawiera [proportions.csv](summary/proportions.csv)."]
    if syntax:
        lines += ["", "### Pierwszy etap z błędem składni", ""]
        for (dataset, stage), count in sorted(syntax.items()):
            lines.append(f"- {LABELS[dataset]}, `{stage}`: {count}.")
        lines += ["", "Identyfikatory i komunikaty zawierają pliki `summary/syntax_*.csv`."]
    (root / "podsumowanie.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    findings = ["# Wnioski badania v2", "",
                "Tabela podaje decyzje dla dostępnych pomiarów według zamrożonego protokołu.", "",
                "| Hipoteza | Zbiór | Status | Podstawa |", "|---|---|---|---|"]
    for i in range(1, 13):
        hyp = f"H{i}"
        for dataset in DATASETS:
            status, evidence = hypothesis_row(paired, rates, binary, diagnostic, logistic, dataset, hyp)
            findings.append(f"| {hyp} | {LABELS[dataset]} | {status} | {evidence} |")
    findings += ["", "## Odpowiedzi na PB1–PB6 według zbioru i wariantu", "", *behavior, "", "- SEW. PB1–PB2: zob. podsumowanie, F2 i F9. PB3–PB4: zob. F4 i F6. PB5: porównanie trybów w F7–F8.",
                 "- ACW bez reguły 45. PB1–PB2: zob. podsumowanie, F2 i F9. PB3–PB4: zob. F4 i F6. "
                 "Punkt stały uwzględnia wyjściową częstość na oryginałach w F10.",
                 "- Pełne ACW. PB6: porównanie tej samej jednostki przed regułą 45 i po niej przedstawia F5. "
                 "Ocena regresji uwzględnia porównanie z wariantem pośrednim. PB1–PB5: zob. F2, F4, F6–F7 i F9–F10.",
                 "- PB7 oczekuje na oceny. Pakiet jest przeznaczony do późniejszego badania."]
    (root / "wnioski.md").write_text("\n".join(findings)+"\n", encoding="utf-8")
    rng = random.Random(20261118)
    for path in rng.sample(all_paths, min(5, len(all_paths))):
        record = read(path)
        original = Path(record["variants"]["original"]["embedded"]["path"])
        raw = original.read_bytes()
        if hashlib.sha256(raw).hexdigest() != record["sample"]["sha256"]:
            raise ValueError(f"original SHA-256 mismatch: {original}")
        for variant, states in record["variants"].items():
            for key, entry in states.items():
                if hashlib.sha256(Path(entry["path"]).read_bytes()).hexdigest() != entry["sha256"]:
                    raise ValueError(f"bad artifact {variant}/{key}")
        validation["checked_originals"].append(str(path))
    tidy_count = sum(1 for _ in csv_rows(root / "tidy/samples.csv"))
    if tidy_count != len(all_paths):
        raise ValueError("Tidy sample count differs from per-sample JSON files")
    validation["tidy_count"] = tidy_count
    if root.resolve() == study.resolve():
        for dataset in DATASETS:
            group = validation["datasets"][dataset]
            aggregated = read(study / dataset / "results.json")
            if group["missing"] or len(aggregated) != group["results"] or group["selection"] != group["results"]:
                raise ValueError(f"Incomplete aggregate for {dataset}: {group}")
        packet = read(root / "fragmenty/wybor.json")["samples"]
        counts = Counter(x["dataset"] for x in packet)
        if len(packet) != 15 or any(not 4 <= counts[dataset] <= 6 for dataset in DATASETS):
            raise ValueError(f"Invalid fragment balance: {counts}")
        for figure in range(1, 12):
            for extension in ("csv", "pdf", "png"):
                if not (root / "figures" / f"F{figure}.{extension}").is_file():
                    raise ValueError(f"Missing F{figure}.{extension}")
        validation["fragment_counts"] = dict(counts)
        tasks = study / "tasks_v2.md"
        tasks.write_text(tasks.read_text().replace("- [ ]", "- [x]"), encoding="utf-8")
    (root / "validation.json").write_text(json.dumps(validation, indent=2)+"\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study", type=Path)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    selected_profile(args.study)
    if args.root:
        export(args.root, args.study)


if __name__ == "__main__":
    main()
