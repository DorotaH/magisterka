#!/usr/bin/env python3
"""Generate descriptive, paired research reports directly from the database."""

import argparse
from collections import defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import random
import sqlite3
import statistics

from run_mbpp import write_json


LABELS = {
    "before": "Przed Ruffem",
    "ruff_default": "Tylko formatter",
    "ruff_strict": "ALL + formatter",
    "ruff_lint_default": "Domyślny linter, bez formattera",
    "ruff_lint_repo_max": "Prefiksy repo-max, bez formattera",
}
SELECTED = [
    ("ruff", "default.violations"),
    ("ruff", "all.violations"),
    ("complexipy", "functions_total"),
    ("complexipy", "total"),
    ("radon", "cc.function_total"),
    ("radon", "mi"),
    ("radon", "raw.sloc"),
    ("radon", "halstead.volume"),
]


def number(value):
    return "—" if value is None else f"{value:.4f}"


def percentile(ordered, p):
    index = (len(ordered) - 1) * p
    low = math.floor(index)
    high = math.ceil(index)
    return ordered[low] + (ordered[high] - ordered[low]) * (index - low)


def bootstrap_mean(values, key, iterations):
    if len(set(values)) == 1:
        return values[0], values[0]
    seed = int(hashlib.sha256(key.encode()).hexdigest()[:16], 16) ^ 20261116
    rng = random.Random(seed)
    means = sorted(
        sum(rng.choices(values, k=len(values))) / len(values) for _ in range(iterations)
    )
    return percentile(means, 0.025), percentile(means, 0.975)


def wilson(hits, total):
    if not total:
        return None, None
    z = 1.959963984540054
    p = hits / total
    center = (p + z * z / (2 * total)) / (1 + z * z / total)
    half = (
        z
        * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total))
        / (1 + z * z / total)
    )
    return max(0, center - half), min(1, center + half)


def markdown_table(headers, rows):
    return [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
        *["| " + " | ".join(str(v) for v in row) + " |" for row in rows],
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--bootstrap", type=int, default=2000)
    args = parser.parse_args()
    if args.bootstrap < 100:
        parser.error("Use at least 100 bootstrap resamples")
    root = args.base.resolve()
    db = sqlite3.connect(f"file:{root / 'knowledge.sqlite'}?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    n = db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    groups = defaultdict(list)
    pairs = list(
        db.execute(
            "SELECT * FROM v_watermark_pairs ORDER BY stage,tool,metric,method,task_id"
        )
    )
    available = {
        (r["task_id"], r["stage"], r["tool"], r["metric"], r["method"]) for r in pairs
    }
    for row in pairs:
        key = (row["method"], row["stage"], row["tool"], row["metric"])
        groups[("available", *key)].append(row)
        other = "sew" if row["method"] == "acw" else "acw"
        if (
            row["task_id"],
            row["stage"],
            row["tool"],
            row["metric"],
            other,
        ) in available:
            groups[("common", *key)].append(row)
    summaries = []
    ci_cache = {}
    for key, rows in sorted(groups.items()):
        cohort, method, stage, tool, metric = key
        values = [r["delta"] for r in rows]
        result = dict(
            cohort=cohort,
            method=method,
            stage=stage,
            tool=tool,
            metric=metric,
            n=len(rows),
            mean_before=statistics.mean(r["before"] for r in rows),
            mean_after=statistics.mean(r["after"] for r in rows),
            mean_delta=statistics.mean(values),
            median_delta=statistics.median(values),
            min_delta=min(values),
            max_delta=max(values),
            increased=sum(v > 0 for v in values),
            decreased=sum(v < 0 for v in values),
            unchanged=sum(v == 0 for v in values),
            ci95_low=None,
            ci95_high=None,
            ci_method=None,
        )
        if stage == "before" and (tool, metric) in SELECTED:
            ci_key = json.dumps(
                [tool, metric, [(r["task_id"], r["delta"]) for r in rows]]
            )
            if ci_key not in ci_cache:
                ci_cache[ci_key] = bootstrap_mean(values, ci_key, args.bootstrap)
            result["ci95_low"], result["ci95_high"] = ci_cache[ci_key]
            result["ci_method"] = f"paired task bootstrap; {args.bootstrap} resamples"
        summaries.append(result)
    with (root / "exports/quality_summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)
    write_json(root / "quality_summary.json", summaries)
    lookup = {
        (r["cohort"], r["method"], r["stage"], r["tool"], r["metric"]): r
        for r in summaries
    }
    report = [
        "# Wpływ watermarkowania na statyczne metryki jakości",
        "",
        f"Zbiór: {n} zadań referencyjnych MBPP. Delta = oznakowany kod minus oryginał.",
        "",
        "Wyniki dotyczą zapisanej implementacji i konfiguracji. Nie są pełną replikacją publikacji. "
        "Nie uruchamiano testów funkcjonalnych.",
        "",
        "## Kompletność pomiarów",
        "",
    ]
    counts = db.execute("""SELECT a.variant,a.stage,m.tool,m.status,COUNT(*) n FROM artifacts a
        JOIN measurements m USING(artifact_id) GROUP BY a.variant,a.stage,m.tool,m.status
        ORDER BY a.variant,a.stage,m.tool,m.status""").fetchall()
    report += markdown_table(
        ["Kod", "Etap", "Narzędzie", "Status", "Liczba"],
        [
            (
                r["variant"],
                LABELS.get(r["stage"], r["stage"]),
                r["tool"],
                r["status"],
                r["n"],
            )
            for r in counts
        ],
    )
    for cohort, title in [
        ("available", "Wszystkie dostępne poprawne pary"),
        ("common", "Wspólne zadania ACW i SEW"),
    ]:
        report += [
            "",
            f"## {title}: przed Ruffem",
            "",
            "Każda średnia „przed” i „po” dotyczy tych samych zadań. "
            "Kohorta wspólna wymaga dostępnego pomiaru danej metryki dla obu metod.",
            "",
        ]
        rows = []
        for tool, metric in SELECTED:
            for method in ("acw", "sew"):
                r = lookup.get((cohort, method, "before", tool, metric))
                if r:
                    rows.append(
                        (
                            method,
                            f"{tool}/{metric}",
                            r["n"],
                            number(r["mean_before"]),
                            number(r["mean_after"]),
                            number(r["mean_delta"]),
                            f"[{number(r['ci95_low'])}, {number(r['ci95_high'])}]",
                            f"{r['decreased']}/{r['unchanged']}/{r['increased']}",
                        )
                    )
        report += markdown_table(
            [
                "Metoda",
                "Metryka",
                "n",
                "Średnia przed",
                "Średnia po",
                "Średnia delta",
                "95% CI średniej delty",
                "Spadek / bez zmian / wzrost",
            ],
            rows,
        )
    report += [
        "",
        "## Interpretacja i zakres",
        "",
        "- Mniej naruszeń i niższa złożoność zwykle oznaczają poprawę tej konkretnej miary. "
        "Dla Maintainability Index kierunek jest odwrotny. Liczby linii i metryki Halsteada nie są samodzielnym werdyktem jakości.",
        "- Błędów składni i błędów narzędzi nie zastępujemy zerami. Brak poprawnego pomiaru wyklucza parę z danej metryki.",
        "- ACW ma 397 błędnych składniowo wyników: 395 powstaje w regule tabulatorów, 2 już w Sourcery. "
        "Średnie ACW opisują zatem podzbiór, który przetrwał tę implementację. Kohorta wspólna ogranicza różnicę składu grup, "
        "ale nie usuwa tego ograniczenia.",
        "- Complexipy liczy także kod modułu. Metryki functions_total i module rozdzielają te składniki. "
        "Wyniki funkcji są dokładnie tym, co udostępnia API narzędzia, także przy funkcjach zagnieżdżonych.",
        "- Radon uwzględnia funkcje zagnieżdżone i metody; agregat klasy nie jest ponownie dodawany do sumy funkcji.",
        f"- Przedziały: {args.bootstrap} powtórzeń bootstrapu sparowanych zadań, deterministyczny seed bazowy 20261116. "
        "To opis zmienności w tym benchmarku, nie dowód uogólnienia na inne modele, języki lub klucze. "
        "Nie wybierano klucza ani progu na podstawie uzyskanych wyników.",
        "- Wszystkie metryki, w tym po każdym wariancie Ruffa, są w exports/quality_summary.csv. "
        "Surowe pary: exports/watermark_quality_pairs.csv; wpływ Ruffa na tę samą wersję: exports/ruff_quality_pairs.csv.",
        "",
        "Pełna definicja przebiegu: [METHODS.md](METHODS.md). Detekcja: [DETECTION.md](DETECTION.md).",
    ]
    (root / "RESULTS.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    detection_rows = db.execute("""SELECT a.variant,a.stage,d.detector,COUNT(*) total,
      SUM(d.status='ok') evaluated,SUM(COALESCE(d.detected,0)) detected,
      SUM(d.status='ok' AND a.syntax_valid=1) valid_evaluated,
      SUM(d.status='ok' AND a.syntax_valid=1 AND d.detected=1) valid_detected,
      SUM(d.verdict='Insufficient evidence') insufficient
      FROM detections d JOIN artifacts a USING(artifact_id)
      GROUP BY a.variant,a.stage,d.detector ORDER BY a.variant,d.detector,a.stage""").fetchall()
    detection = []
    for row in detection_rows:
        r = dict(row)
        r["unavailable"] = r["total"] - r["evaluated"]
        r["rate"] = r["detected"] / r["evaluated"] if r["evaluated"] else None
        r["ci95_low"], r["ci95_high"] = wilson(r["detected"], r["evaluated"])
        detection.append(r)
    with (root / "exports/detection_summary.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(detection[0]))
        writer.writeheader()
        writer.writerows(detection)
    detection_report = [
        "# Wykrywalność przed i po Ruffie",
        "",
        "Wykrycie SEW oznacza oficjalny werdykt, przy alpha=0,01 i minimum 5 niezależnych obserwacji. "
        "ACW oznacza dokładną identyczność bajtów po ponownym zastosowaniu zapisanej konfiguracji.",
        "",
        "Każdy profil Ruffa zaczyna od tej samej wersji wejściowej. Profile nie są nakładane kolejno.",
        "",
    ]
    detection_report += markdown_table(
        [
            "Kod / detektor",
            "Etap",
            "Wykryte / ocenione",
            "Brak wyniku",
            "W poprawnym kodzie",
            "Za mało danych SEW",
            "95% Wilson",
        ],
        [
            (
                f"{r['variant']}/{r['detector']}",
                LABELS.get(r["stage"], r["stage"]),
                f"{r['detected']}/{r['evaluated']}",
                r["unavailable"],
                f"{r['valid_detected']}/{r['valid_evaluated']}",
                r["insufficient"] or 0,
                f"[{100 * r['ci95_low']:.2f}%, {100 * r['ci95_high']:.2f}%]"
                if r["rate"] is not None
                else "—",
            )
            for r in detection
        ],
    )
    changes = db.execute("""SELECT variant,stage,detector,transition,COUNT(*) n
        FROM v_detection_transitions GROUP BY variant,stage,detector,transition
        ORDER BY variant,detector,stage,transition""").fetchall()
    change_groups = defaultdict(dict)
    for r in changes:
        change_groups[(r["variant"], r["detector"], r["stage"])][r["transition"]] = r[
            "n"
        ]
    detection_report += ["", "## Zmiany dla tych samych zadań", ""]
    detection_report += markdown_table(
        [
            "Kod / detektor",
            "Etap",
            "Utrzymane",
            "Utracone",
            "Nowe",
            "Brak w obu",
            "Brak porównania",
        ],
        [
            (
                f"{v}/{d}",
                LABELS.get(s, s),
                c.get("retained", 0),
                c.get("lost", 0),
                c.get("gained", 0),
                c.get("not_detected_both", 0),
                c.get("unavailable", 0),
            )
            for (v, d, s), c in sorted(change_groups.items())
        ],
    )
    detection_report += [
        "",
        "## Ograniczenia i ważne rozróżnienia",
        "",
        "- Brak wyniku po odmowie Ruffa nie oznacza negatywnej detekcji. Takie rekordy mają detected=NULL.",
        "- Surowe liczby ACW przed Ruffem i po samym linterze obejmują także błędny składniowo kod. "
        "Osobne kolumny pokazują wynik w poprawnym podzbiorze. Samo wykrycie nie potwierdza użyteczności programu.",
        "- Liczba wykryć w kontrolach może być taka sama przed i po, mimo że dotyczą innych zadań. "
        "Dlatego zapisano pełne przejścia, nie tylko sumy.",
        "- Minimum dowodu w SEW jest częścią oficjalnej decyzji. Poprzednie 908 wynikające z samego p<0,01 "
        "nie jest liczbą poprawnych wykryć; prawidłowy licznik bazowy to 708.",
        "- Przedziały Wilsona mają modelowe założenie obserwacji Bernoulliego. "
        "To jeden benchmark i jeden klucz; wyniki nie są oceną uniwersalnej skuteczności.",
        "- Repo-max stosuje prefiksy aktualnego repozytorium na przypiętej wersji Ruffa. "
        "Nie udajemy identycznego historycznego zestawu 369 reguł z publikacji.",
        "",
        "Wszystkie rekordy i p-value: [exports/detections.csv](exports/detections.csv). "
        "Przejścia: [exports/detection_transitions.csv](exports/detection_transitions.csv).",
    ]
    (root / "DETECTION.md").write_text(
        "\n".join(detection_report) + "\n", encoding="utf-8"
    )
    examples = [
        "# Przykłady i ścieżka dowodowa",
        "",
        "Wybór przykładów jest deterministyczny. Pełne bajty kodu są w SQLite; "
        "poniższy tekst służy tylko do czytania.",
        "",
        "## Uszkodzenie wcięcia: zadanie 2",
        "",
    ]
    if db.execute("SELECT 1 FROM tasks WHERE task_id=2").fetchone():
        for label, query in [
            (
                "Przed regułą 45",
                "SELECT b.content FROM audit_artifacts a JOIN code_blobs b USING(sha256) WHERE task_id=2 AND stage='before_tabs'",
            ),
            (
                "Po regule 45",
                "SELECT code FROM v_artifact_code WHERE task_id=2 AND variant='acw' AND stage='before'",
            ),
        ]:
            item = db.execute(query).fetchone()
            if item:
                examples += [
                    f"### {label}",
                    "",
                    "````python",
                    bytes(item[0]).decode("utf-8"),
                    "````",
                    "",
                ]
    for method in ("acw", "sew"):
        row = db.execute(
            """SELECT * FROM v_watermark_pairs WHERE stage='before' AND method=?
            AND tool='complexipy' AND metric='functions_total' ORDER BY ABS(delta) DESC,task_id LIMIT 1""",
            (method,),
        ).fetchone()
        if not row:
            continue
        examples += [
            f"## Największa bezwzględna zmiana złożoności funkcji: {method}, ID {row['task_id']}",
            "",
            f"Przed: {row['before']}; po: {row['after']}; delta: {row['delta']}. "
            "To wybrany skrajny przykład, nie reprezentatywna średnia.",
            "",
        ]
        for variant in ("original", method):
            code = db.execute(
                "SELECT code FROM v_artifact_code WHERE task_id=? AND variant=? AND stage='before'",
                (row["task_id"], variant),
            ).fetchone()[0]
            examples += [
                f"### {variant}",
                "",
                "````python",
                bytes(code).decode("utf-8"),
                "````",
                "",
            ]
    (root / "EXAMPLES.md").write_text("\n".join(examples) + "\n", encoding="utf-8")
    build = json.loads((root / "build.json").read_text())
    build.update(
        reports_complete=True,
        bootstrap_resamples=args.bootstrap,
        bootstrap_seed=20261116,
    )
    write_json(root / "build.json", build)
    print(
        f"Generated reports and {len(summaries)} paired quality summaries", flush=True
    )


if __name__ == "__main__":
    main()
