"""Profile licensed reference-code datasets before extension v3 watermarking."""

import argparse
import ast
import csv
import json
import tarfile
from hashlib import file_digest
from pathlib import Path
from statistics import median
from textwrap import dedent
from tokenize import TokenError, detect_encoding

from radon.raw import analyze
from select_samples import inspect, rows


def json_lines(path):
    with path.open(encoding="utf-8") as source:
        yield from map(json.loads, source)


def deveval(metadata, archive):
    with tarfile.open(metadata) as source:
        records = [json.loads(line) for line in source.extractfile("data.jsonl")]
    wanted = {f'Source_Code/{record["completion_path"]}' for record in records}
    files = {}
    with tarfile.open(archive, "r|gz") as source:
        for member in source:
            if member.name in wanted and member.isfile():
                stream = source.extractfile(member)
                encoding, prefix = detect_encoding(stream.readline)
                files[member.name] = (b"".join(prefix) + stream.read()).decode(encoding).splitlines(keepends=True)
    for record in records:
        name = f'Source_Code/{record["completion_path"]}'
        if name not in files:
            yield [None]
            continue
        start = record["signature_position"][0] - 1
        end = record["body_position"][1]
        yield [dedent("".join(files[name][start:end]))]


def sources(base):
    mercury = base / "mercury-train.parquet"
    yield "mercury_train", mercury, (
        [entry["solution"] for entry in row["solutions"]]
        for row in rows(mercury, ["solutions"])
    )
    for split in ("train", "test"):
        leetcode = base / f"leetcode-{split}.jsonl"
        yield f"leetcode_{split}", leetcode, ([row["completion"]] for row in json_lines(leetcode))
    taco = base / "taco-test.parquet"
    yield "taco_test", taco, (json.loads(row["solutions"] or "[]") for row in rows(taco, ["solutions"]))
    effibench = base / "effibench-data.jsonl"
    yield "effibench", effibench, ([row["canonical_solution"]] for row in json_lines(effibench))
    repoexec = base / "repoexec.parquet"
    yield "repoexec", repoexec, ([row["raw_solution"]] for row in rows(repoexec, ["raw_solution"]))
    archive = base / "deveval-source.tar.gz"
    yield "deveval", archive, deveval(base / "deveval-metadata.tar.gz", archive)
    apps = base / "apps-test.jsonl"
    yield "apps", apps, (json.loads(row["solutions"] or "[]")[:1] for row in json_lines(apps))


def profile(codes):
    samples = parsable = functions = candidates = scripts = 0
    lengths = []
    for solutions in codes:
        if not solutions:
            continue
        samples += 1
        first = solutions[0]
        if first is None:
            continue
        reason, _, structure = inspect(first)
        parsable += reason != "invalid_python"
        if reason != "invalid_python":
            functions += any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                             for node in ast.walk(ast.parse(first)))
        try:
            lengths.append(analyze(first).sloc)
        except (SyntaxError, TokenError, ValueError):
            pass
        script_candidate = False
        for code in solutions:
            reason, _, structure = inspect(code)
            if reason:
                continue
            if structure != "script":
                candidates += 1
                break
            script_candidate = True
        else:
            scripts += script_candidate
    return samples, parsable, functions, median(lengths), candidates, scripts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    profiles = []
    for name, path, codes in sources(args.inputs):
        with path.open("rb") as source:
            digest = file_digest(source, "sha256").hexdigest()
        if name == "effibench" and digest != "65be3e180133c906329a58324d4384cae4e6d8a9ee3e4f1978cae96632b6f11b":
            raise ValueError("Niezgodna suma SHA-256 pliku EffiBench względem wskaźnika Git LFS")
        samples, parsable, functions, sloc, candidates, scripts = profile(codes)
        eligible = (sloc >= 15 and functions / samples >= 0.8
                    and parsable / samples >= 0.9 and candidates >= 100)
        profiles.append((name, path.name, digest, samples, parsable, functions, sloc,
                         candidates, scripts, eligible))
        print(name, profiles[-1][3:], flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pending = args.output.with_suffix(".tmp")
    with pending.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(("dataset", "source_file", "source_sha256", "samples_with_code", "parsable",
                         "with_functions", "median_sloc", "candidates", "script_candidates", "eligible"))
        writer.writerows(profiles)
    pending.replace(args.output)


if __name__ == "__main__":
    main()
