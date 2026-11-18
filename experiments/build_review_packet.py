"""Create a blinded review packet from completed paired measurements."""

import argparse
import ast
from collections import Counter
import csv
from difflib import SequenceMatcher
import hashlib
from html import escape
from itertools import combinations
import json
from pathlib import Path
import random
from statistics import mean, median
from textwrap import dedent

import numpy as np
from scipy import optimize, sparse, stats

from profile_dataset import profile_sample
from select_samples import write_json

DATASETS = ("mercury_eval", "classeval", "apps")
VARIANTS = ("original", "sew", "acw_notab", "acw_full")
SLOTS = ("A", "A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F", "G", "H")
RATIONALE = {"A": "blisko środka rozkładu SLOC i Complexipy",
             "B": "SLOC między p10 a p25", "C": "Complexipy między p75 a p90",
             "D": "małe podobieństwo liniowe SEW", "E": "małe podobieństwo liniowe ACW bez reguły 45",
             "F": "duży udział tabulatorów i różnica między wariantami ACW",
             "G": "błąd składni pełnego ACW", "H": "mała ingerencja obu metod"}


def read(path):
    return json.loads(path.read_text())


def functions(source):
    found = {}
    def walk(node, prefix):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                name = (*prefix, child.name)
                if not isinstance(child, ast.ClassDef):
                    start = min([child.lineno, *(x.lineno for x in child.decorator_list)])
                    found[name] = (start, child.end_lineno)
                walk(child, name)
            else:
                walk(child, prefix)
    walk(ast.parse(source), ())
    return found


def state_code(states, key):
    return Path(states[key]["path"]).read_text()


def fragments(variants):
    stages = {"raw": "embedded", "formatted": "default/format"}
    sources = {(condition, variant): state_code(states, key)
               for condition, key in stages.items() for variant, states in variants.items()}
    lines = {key: source.splitlines() for key, source in sources.items()}
    if max(map(len, lines.values())) <= 50:
        return {condition: ({v: sources[condition, v] for v in VARIANTS},
                            {v: [1, len(lines[condition, v])] for v in VARIANTS}, None)
                for condition in stages}
    try:
        ranges = {key: functions(source) for key, source in sources.items()}
        choices = set.intersection(*(set(x) for x in ranges.values()))
    except SyntaxError:
        return None
    candidates = []
    for name in choices:
        selected = {key: value[name] for key, value in ranges.items()}
        length = max(end-start+1 for start, end in selected.values())
        if length <= 50:
            candidates.append((length, name, selected))
    if not candidates:
        return None
    _, name, selection = max(candidates, key=lambda x: (x[0], x[1]))
    matched = {}
    for condition in stages:
        bodies, locations = {}, {}
        for variant in VARIANTS:
            a, b = selection[condition, variant]
            bodies[variant] = "\n".join(lines[condition, variant][a-1:b])+"\n"
            locations[variant] = [a, b]
        matched[condition] = (bodies, locations, ".".join(name))
    return matched


def observations(root):
    candidates = []
    excluded = Counter()
    for dataset in DATASETS:
        for path in sorted((root / dataset).glob("*/result.json")):
            item = read(path)
            variants = item["variants"]
            if item["sample"]["structure"] == "script":
                continue
            invalid = {v for v, states in variants.items() if states["embedded"]["syntax_error"]}
            if invalid - {"acw_full"}:
                excluded["other_invalid"] += 1
                continue
            stimuli = fragments(variants)
            if stimuli is None:
                excluded["length_or_missing_match"] += 1
                continue
            raw_code = stimuli["raw"][0]
            anchor = raw_code["original"].splitlines()
            lexical = {}
            for variant in ("sew", "acw_notab", "acw_full"):
                code = raw_code[variant].splitlines()
                matcher = SequenceMatcher(None, anchor, code, autojunk=False)
                lexical[variant] = (matcher.ratio(), sum(max(j-i, l-k) for op, i, j, k, l in matcher.get_opcodes() if op != "equal"))
            excerpt = profile_sample(item["sample"]["sample_id"], dedent(raw_code["original"]), {})
            tabs = sum(line.startswith("\t") for line in raw_code["acw_full"].splitlines())
            correctness = path.parent / "correctness_v2/result.json"
            candidate = dict(dataset=dataset, sample_id=item["sample"]["sample_id"],
                             sloc=excerpt.get("raw",{}).get("sloc", len(anchor)),
                             file_sloc=item["sample"]["sloc"], structure=item["sample"]["structure"],
                             cc_max=max((x["complexity"] for x in excerpt.get("cc", [])), default=0),
                             invalid=bool(invalid),
                             complexipy=max((x["complexity"] for x in excerpt.get("complexipy", [])), default=0),
                             sew_similarity=lexical["sew"][0], sew_changed=lexical["sew"][1],
                             acw_similarity=lexical["acw_notab"][0], acw_changed=lexical["acw_notab"][1],
                             full_similarity=lexical["acw_full"][0],
                             tabs=tabs, tab_fraction=tabs/max(1, len(anchor)),
                             sites=item["sew_embedding"].get("n_sites"),
                             survived=variants["sew"]["default/fix_format"]["sew"][0]["verdict"] == "Watermark detected",
                             correctness={k:v["differential"] for k,v in read(correctness).get("variants",{}).items()}
                             if correctness.exists() else None, **stimuli)
            candidates.append(candidate)
    return candidates, excluded


def rank(candidates, seed):
    normal = [x for x in candidates if not x["invalid"]]
    columns = {k: np.asarray([x[k] for x in normal]) for k in ("sloc", "complexipy")}
    limits = {"B": np.quantile(columns["sloc"], [.1, .25]), "C": np.quantile(columns["complexipy"], [.75, .9])}
    identities = [x["sample_id"] for x in candidates]
    scores = []
    for slot_index, slot in enumerate(SLOTS):
        ranked = []
        for i, x in enumerate(candidates):
            if slot == "G" and not x["invalid"]:
                continue
            if slot != "G" and x["invalid"]:
                continue
            if slot == "A" and x["dataset"] != DATASETS[slot_index]:
                continue
            if slot == "A":
                same = [a for a in normal if a["dataset"] == x["dataset"]]
                score = sum(abs(x[k]-median(a[k] for a in same))/max(1., np.std([a[k] for a in same]))
                            for k in columns)
            elif slot in limits:
                lo, hi = limits[slot]
                val = x["sloc" if slot == "B" else "complexipy"]
                if not lo <= val <= hi:
                    continue
                score = abs(val - (lo+hi)/2)
            elif slot == "D":
                score = x["sew_similarity"]
            elif slot == "E":
                score = x["acw_similarity"]
            elif slot == "F":
                score = -x["tab_fraction"]-abs(x["full_similarity"]-x["acw_similarity"])
            elif slot == "G":
                score = -x["tabs"]
            else:
                score = 2-x["sew_similarity"]-x["acw_similarity"]
            tie = hashlib.sha256(f"{seed}:{slot}:{x['dataset']}:{identities[i]}".encode()).hexdigest()
            ranked.append((score, tie, i))
        scores.append(sorted(ranked))
    return scores


def assign(candidates, rankings):
    choices = [(slot, order, item) for slot, ranks in enumerate(rankings)
               for order, (_, _, item) in enumerate(ranks)]
    size = len(SLOTS) + len(candidates) + len(DATASETS)
    indices, variables = [], []
    for var, (slot, _, item) in enumerate(choices):
        dataset = DATASETS.index(candidates[item]["dataset"])
        indices.extend((slot, len(SLOTS)+item, len(SLOTS)+len(candidates)+dataset))
        variables.extend((var, var, var))
    matrix = sparse.coo_matrix((np.ones(len(indices)), (indices, variables)), shape=(size, len(choices))).tocsr()
    lower = [1]*len(SLOTS)+[0]*len(candidates)+[4]*len(DATASETS)
    upper = [1]*len(SLOTS)+[1]*len(candidates)+[6]*len(DATASETS)
    objective = [order/max(1,len(rankings[slot])) for slot, order, _ in choices]
    solved = optimize.milp(objective, integrality=np.ones(len(choices)), bounds=optimize.Bounds(0, 1),
                          constraints=optimize.LinearConstraint(matrix, lower, upper))
    if not solved.success:
        raise SystemExit(f"Nie można obsadzić wszystkich slotów z ograniczeniami v2: {solved.message}")
    return sorted((slot, item, order) for (slot, order, item), value in zip(choices, solved.x) if value > .5)


def csv_file(path, headers, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def build(root, people, seed):
    candidates, excluded = observations(root)
    ranked = rank(candidates, seed)
    selected = assign(candidates, ranked)
    packet = root / "pakiet_oceny"
    fragments_out = root / "fragmenty"
    for path in (packet, fragments_out):
        path.mkdir(exist_ok=True)
    rng = random.Random(seed)
    headers = ["fragment", "dataset", "sample_id", "slot", "rank", "sloc", "complexipy", "sew_similarity",
               "acw_similarity", "sew_changed", "acw_changed", "tab_fraction", "survived", "sites", "structure"]
    fields = ("sloc", "complexipy", "cc_max", "sew_similarity", "acw_similarity", "tab_fraction")
    selections = []
    key = {}
    log = ["# Uzasadnienie doboru fragmentów", "",
           f"Pula liczy {len(candidates)} jednostek. Wykluczenia: {dict(excluded)}.",
           "Dobór celowy według slotów z ograniczeniem 4–6 fragmentów na zbiór. Rangi minimalizowano łącznie.",
           "SLOC, CC, Complexipy i podobieństwo odnoszą się do prezentowanego fragmentu. Liczba miejsc SEW, detekcja i wyniki testów dotyczą całej jednostki.", ""]
    used = {item for _, item, _ in selected}
    for slot_id, item, order in selected:
        source = candidates[item]
        slot = SLOTS[slot_id]
        frag_id = f"F{slot_id+1:02}"
        aliases = list("ABCD")
        rng.shuffle(aliases)
        key[frag_id] = dict(zip(aliases, VARIANTS))
        sub = packet / frag_id
        sub.mkdir(exist_ok=True)
        info = {k:v for k,v in source.items() if k not in ("raw", "formatted")}
        info.update(fragment=frag_id, slot=slot, rank=order+1,
                    reserve=[{"dataset": candidates[i]["dataset"], "sample_id": candidates[i]["sample_id"]}
                             for _, _, i in ranked[slot_id] if i not in used][:2])
        info["percentiles"] = {field: float(stats.percentileofscore([x[field] for x in candidates], source[field]))
                               for field in fields}
        for condition in ("raw", "formatted"):
            stimulus = source[condition]
            if stimulus is None:
                continue
            code, ranges, name = stimulus
            info[condition] = {"name": name, "line_ranges": ranges}
            folder = sub / condition
            folder.mkdir(exist_ok=True)
            for alias, variant in key[frag_id].items():
                text = code[variant]
                (folder / f"{alias}.txt").write_text(text, encoding="utf-8")
                (folder / f"{alias}.html").write_text(
                    '<!doctype html><html lang="pl"><meta charset="utf-8"><title>Fragment</title>'
                    '<style>pre{font:14px monospace;tab-size:4;line-height:1.5;padding:16px}</style>'
                    f'<pre>{escape(text)}</pre></html>', encoding="utf-8")
        selections.append(info)
        log += [f"## {frag_id}, slot {slot}", "",
                f"Źródło {source['dataset']} / `{source['sample_id']}`. Kryterium {RATIONALE[slot]}. Ranga {order+1}.",
                f"Percentyle: {info['percentiles']}.",
                f"Rezerwa: {info['reserve']}. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.", ""]
    write_json(fragments_out / "wybor.json", {"seed": seed, "pool": len(candidates), "excluded": dict(excluded),
                                            "samples": selections})
    csv_file(fragments_out / "features.csv", headers, ([x.get(k) for k in headers] for x in selections))
    write_json(root / "klucz.json", key)
    (fragments_out / "uzasadnienie.md").write_text("\n".join(log), encoding="utf-8")
    rep = ["# Porównanie celowej próby z pulą", "",
           "Wartości KS opisują rozbieżność rozkładów. Dobór celowy ogranicza interpretację wartości p.", "",
           "| Metryka | Próba: średnia, mediana, zakres | Pula: średnia, mediana, zakres | KS D |",
           "|---|---|---|---:|"]
    for field in fields:
        a, b = ([x[field] for x in rows] for rows in (selections, candidates))
        def fmt(v):
            return f"{mean(v):.2f}, {median(v):.2f}, {min(v):.2f}–{max(v):.2f}"
        rep.append(f"| {field} | {fmt(a)} | {fmt(b)} | {stats.ks_2samp(a,b).statistic:.3f} |")
    (fragments_out / "reprezentatywnosc.md").write_text("\n".join(rep)+"\n", encoding="utf-8")
    pairings = list(combinations(VARIANTS, 2))
    trials = []
    judges = []
    for i in range(people):
        for j, x in enumerate(selections):
            fragment = x["fragment"]
            pair = pairings[(i+j) % 6]
            aliases = {variant: k for k, variant in key[fragment].items()}
            order = [aliases[v] for v in pair[::-1 if (i//6+j) % 2 else 1]]
            for condition in ("raw", "formatted"):
                if condition not in x:
                    continue
                trials.append([i+1, fragment, condition, *order, int(x["slot"] != "G")])
    for x in selections:
        fragment = x["fragment"]
        for a, b in combinations(sorted(key[fragment]), 2):
            for condition in ("raw", "formatted"):
                if condition in x:
                    for repeat in range(1, 4):
                        judges.extend([[fragment, condition, a, b, repeat], [fragment, condition, b, a, repeat]])
    csv_file(root / "trials.csv", ("participant", "fragment", "condition", "left", "right", "human_eligible"), trials)
    csv_file(packet / "llm_trials.csv", ("fragment", "condition", "left", "right", "repeat"), judges)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("measurements", type=Path)
    p.add_argument("--participants", type=int, default=60)
    p.add_argument("--seed", type=int, default=20261118)
    args = p.parse_args()
    build(args.measurements, args.participants, args.seed)


if __name__ == "__main__":
    main()
