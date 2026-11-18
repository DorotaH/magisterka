"""Select and profile study samples from the recorded benchmark inputs."""

import argparse
import ast
from collections import Counter, defaultdict
import csv
from fractions import Fraction
from hashlib import file_digest, sha256
import json
from pathlib import Path
import random
from tokenize import TokenError

from pyarrow.parquet import ParquetFile
from radon.raw import analyze

from profile_dataset import profile_sample, read_samples, summarize


def rows(path, columns):
    for batch in ParquetFile(path).iter_batches(batch_size=32, columns=columns):
        yield from batch.to_pylist()


def inspect(code):
    try:
        tree = ast.parse(code)
        compile(tree, "<sample>", "exec")
        sloc = analyze(code).sloc
    except (SyntaxError, TokenError, ValueError):
        return "invalid_python", None, None
    nodes = list(ast.walk(tree))
    structure = "script"
    if any(isinstance(node, ast.ClassDef) for node in nodes):
        structure = "class"
    elif any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in nodes):
        structure = "function"
    return ("short" if sloc < 15 else None), sloc, structure


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(".tmp")
    pending.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pending.replace(path)


def candidate(sample_id, code, metadata, exclusions, dataset):
    reason, sloc, structure = inspect(code)
    if reason:
        exclusions.append((dataset, sample_id, reason))
        return None
    return {"sample_id": sample_id, "code": code, "sloc": sloc, "structure": structure, **metadata}


def sloc_band(sloc):
    return next((b for b in (20, 40, 100) if sloc < b), 1000)


def stratified(pool, cap, rng):
    if len(pool) <= cap:
        return sorted(pool, key=lambda x: x["sample_id"])
    strata = defaultdict(list)
    for item in pool:
        strata[(item["difficulty"], sloc_band(item["sloc"]))].append(item)
    shares = {key: Fraction(cap * len(values), len(pool)) for key, values in strata.items()}
    quotas = {key: int(value) for key, value in shares.items()}
    ranked = sorted(shares, key=lambda key: (-(shares[key] - quotas[key]), key))
    for key in ranked[:cap - sum(quotas.values())]:
        quotas[key] += 1
    return [item for key in sorted(strata) for item in rng.sample(strata[key], quotas[key])]


def select_mercury(path, rng, exclusions):
    full, pool = [], []
    for row in rows(path, ["slug_name", "difficulty", "solutions"]):
        sample_id = row["slug_name"]
        solutions = row["solutions"]
        if not solutions:
            exclusions.append(("mercury_eval", sample_id, "no_solution"))
            continue
        full.append((sample_id, solutions[0]["solution"], {"difficulty": row["difficulty"]}))
        choices = []
        for index, solution in enumerate(solutions):
            code = solution["solution"]
            reason, sloc, structure = inspect(code)
            if reason is None and structure != "script":
                choices.append((index, code, sloc, structure))
        if not choices:
            exclusions.append(("mercury_eval", sample_id, "no_eligible_solution"))
            continue
        index, code, sloc, structure = rng.choice(choices)
        pool.append(dict(sample_id=sample_id, code=code, sloc=sloc, structure=structure,
                         difficulty=row["difficulty"], solution_index=index, eligible_solutions=len(choices)))
    return full, pool, pool


def select_classeval(path, exclusions):
    full = list(read_samples(path, "classeval"))
    pool = [item for sample_id, code, meta in full
            if (item := candidate(sample_id, code, meta, exclusions, "classeval"))]
    return full, pool, pool


def select_apps(paths, rng, exclusions, archived):
    main, scripts = [], []
    for path in paths:
        for row in rows(path, ["problem_id", "solutions", "input_output", "difficulty"]):
            sample_id = str(row["problem_id"])
            solutions = json.loads(row["solutions"] or "[]")
            if not solutions:
                exclusions.append(("apps", sample_id, "no_solution"))
                continue
            tests = json.loads(row["input_output"] or "{}")
            metadata = {"difficulty": row["difficulty"],
                        "format": "call-based" if tests.get("fn_name") else "stdin"}
            item = candidate(sample_id, solutions[0], metadata, exclusions, "apps")
            if item is None:
                continue
            if sha256(item["code"].encode()).hexdigest() in archived:
                exclusions.append(("apps", sample_id, "identical_codecontests_source"))
            elif item["structure"] == "script":
                scripts.append(item)
                exclusions.append(("apps", sample_id, "script_layer"))
            else:
                main.append(item)
    call = [x for x in main if x["format"] == "call-based"]
    stdin = [x for x in main if x["format"] == "stdin"]
    selected = call + stratified(stdin, 600 - len(call), rng)
    selected += rng.sample(scripts, min(100, len(scripts)))
    return main, selected


def profile_selection(items):
    return [profile_sample(item["sample_id"], item["code"],
                           {key: value for key, value in item.items() if key != "code"})
            for item in items]


def persist(output, dataset, seed, sources, full, pool, selected):
    directory = output / dataset
    samples = []
    for item in selected:
        row = {key: value for key, value in item.items() if key != "code"}
        code = item["code"].encode()
        row["sha256"] = sha256(code).hexdigest()
        sample = directory / item["sample_id"]
        sample.mkdir(parents=True, exist_ok=True)
        original = sample / "original.py"
        if original.exists() and original.read_bytes() != code:
            raise ValueError(f"Existing original differs: {original}")
        original.write_bytes(code)
        write_json(sample / "meta.json", row)
        samples.append(row)
    source_hashes = {}
    for path in sources:
        with path.open("rb") as stream:
            source_hashes[path.name] = file_digest(stream, "sha256").hexdigest()
    pilot_rng = random.Random(seed)
    pilot = pilot_rng.sample([x["sample_id"] for x in samples if x["structure"] != "script"], 20)
    write_json(directory / "selection.json", {"seed": seed, "source_sha256": source_hashes,
               "samples": samples, "pilot": pilot})
    candidates = profile_selection(pool)
    wanted = {x["sample_id"] for x in selected if x["structure"] != "script"}
    chosen = [x for x in candidates if x["sample_id"] in wanted]
    layers = {"full": full, "candidates": candidates, "selected": chosen}
    write_json(output / "spis_zbiorow" / f"levels_{dataset}.json", {
        level: {"summary": summarize(data), "difficulty": Counter(
            (x.get("metadata") or {}).get("difficulty", "unknown") for x in data),
            "samples": data}
        for level, data in layers.items()
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mercury", type=Path, required=True)
    parser.add_argument("--classeval", type=Path, required=True)
    parser.add_argument("--apps", type=Path, nargs="+", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20261118)
    args = parser.parse_args()
    exclusions = []
    rng = random.Random(args.seed)
    mercury = select_mercury(args.mercury, rng, exclusions)
    classeval = select_classeval(args.classeval, exclusions)
    profiles = args.out / "spis_zbiorow"
    archived = {x["sha256"] for x in json.loads((profiles / "profil_codecontests.json").read_text())["samples"]}
    apps_pool, apps_selected = select_apps(args.apps, rng, exclusions, archived)
    apps_full = json.loads((profiles / "profil_apps.json").read_text())["samples"]
    for dataset, sources, full, candidates, selected in (
        ("mercury_eval", [args.mercury], [profile_sample(*x) for x in mercury[0]], *mercury[1:]),
        ("classeval", [args.classeval], [profile_sample(*x) for x in classeval[0]], *classeval[1:]),
        ("apps", args.apps, apps_full, apps_pool, apps_selected),
    ):
        persist(args.out, dataset, args.seed, sources, full, candidates, selected)
        print(dataset, len(full), len(candidates), len(selected), flush=True)
    with (profiles / "wykluczenia.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["dataset", "sample_id", "reason"])
        writer.writerows(exclusions)


if __name__ == "__main__":
    main()
