"""Profile Python reference solutions without executing their code."""

import argparse
import ast
from collections import Counter
from gzip import open as gzip_open
from hashlib import file_digest, sha256
from importlib.metadata import version
import json
from pathlib import Path
import statistics
import sys
from tokenize import TokenError

from complexipy import code_complexity
from radon.complexity import cc_rank, cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze


def read_samples(path, layout):
    if layout == "directory":
        for source in sorted(path.rglob("original.py")):
            yield str(source.parent.relative_to(path)), source.read_text(encoding="utf-8"), None
        return

    if layout == "apps":
        from pyarrow.parquet import ParquetFile

        files = sorted(path.glob("*.parquet")) if path.is_dir() else [path]
        if not files:
            raise ValueError(f"No Parquet shards in {path}")
        columns = ["problem_id", "solutions", "input_output", "difficulty"]
        for shard in files:
            for batch in ParquetFile(shard).iter_batches(batch_size=64, columns=columns):
                for row in batch.to_pylist():
                    candidates = json.loads(row["solutions"] or "[]")
                    if candidates:
                        tests = json.loads(row["input_output"] or "{}")
                        metadata = {
                            "tests_available": bool(tests.get("inputs")),
                            "difficulty": row["difficulty"],
                            "format": "call-based" if tests.get("fn_name") else "stdin",
                        }
                        yield str(row["problem_id"]), candidates[0], metadata
        return

    if layout in {"mbpp", "humaneval"}:
        opener = gzip_open if path.suffix == ".gz" else open
        with opener(path, "rt", encoding="utf-8") as stream:
            for line in stream:
                row = json.loads(line)
                if layout == "humaneval":
                    code = row["prompt"] + row["canonical_solution"]
                    tests = row["test"]
                else:
                    code = row["code"]
                    tests = row["test_list"]
                yield str(row["task_id"]), code, {"tests_available": bool(tests)}
        return

    for row in json.loads(path.read_text(encoding="utf-8")):
        if layout == "classeval":
            source = row["solution_code"]
            imports = [line for line in row["import_statement"] if line not in source.splitlines()]
            if imports:
                source = "\n".join([*imports, "", source])
            yield row["task_id"], source, {"tests_available": bool(row["test"] and row["test_classes"])}
        else:
            yield str(row["sample_id"]), row["source"], row.get("metadata")


def profile_sample(sample_id, source, metadata):
    record = {"sample_id": sample_id, "sha256": sha256(source.encode()).hexdigest(),
              "loc": len(source.splitlines()), "metadata": metadata, "errors": {}}
    try:
        record["raw"] = analyze(source)._asdict()
    except (SyntaxError, TokenError, ValueError) as error:
        record["errors"]["radon_raw"] = str(error)
    try:
        compile(source, sample_id, "exec")
        tree = ast.parse(source, filename=sample_id)
    except (SyntaxError, ValueError) as error:
        record["errors"]["syntax"] = str(error)
        return record

    nodes = list(ast.walk(tree))
    record["functions"] = sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) for node in nodes)
    record["classes"] = sum(isinstance(node, ast.ClassDef) for node in nodes)
    record["cc"] = [{"name": block.name, "line": block.lineno,
                     "complexity": block.complexity, "rank": cc_rank(block.complexity)}
                    for block in cc_visit(source)]
    record["mi"] = mi_visit(source, multi=True)
    record["halstead"] = h_visit(source).total._asdict()
    try:
        cognitive = code_complexity(source, no_ignore=True, with_plans=False)
        record["complexipy"] = [
            {"name": function.name, "line": function.line_start, "complexity": function.complexity}
            for function in cognitive.functions
        ]
    except (RuntimeError, ValueError) as error:
        record["errors"]["complexipy"] = str(error)
    return record


def distribution(values):
    ordered = sorted(values)
    if not ordered:
        return {"n": 0}
    if len(ordered) == 1:
        p10 = p90 = ordered[0]
    else:
        quantiles = statistics.quantiles(ordered, n=10, method="inclusive")
        p10, p90 = quantiles[0], quantiles[-1]
    return {"n": len(ordered), "mean": statistics.mean(ordered), "median": statistics.median(ordered),
            "p10": p10, "p90": p90, "max": ordered[-1]}


def summarize(rows):
    parsed = [row for row in rows if "syntax" not in row["errors"]]
    cc = [block for row in parsed for block in row["cc"]]
    cognitive = [function["complexity"] for row in parsed for function in row.get("complexipy", [])]
    return {
        "samples": len(rows),
        "parsable": len(parsed),
        "loc": distribution(row["loc"] for row in rows),
        "sloc": distribution(row["raw"]["sloc"] for row in rows if "raw" in row),
        "without_functions": sum(row["functions"] == 0 for row in parsed),
        "without_classes": sum(row["classes"] == 0 for row in parsed),
        "without_functions_or_classes": sum(row["functions"] == row["classes"] == 0 for row in parsed),
        "functions_per_file": distribution(row["functions"] for row in parsed),
        "cc": distribution(block["complexity"] for block in cc),
        "cc_ranks": dict(Counter(block["rank"] for block in cc)),
        "complexipy": distribution(cognitive),
        "complexipy_zeros": cognitive.count(0),
        "mi": distribution(row["mi"] for row in parsed),
        "halstead": {key: distribution(row["halstead"][key] for row in parsed)
                     for key in (parsed[0]["halstead"] if parsed else {})},
        "tests_available": dict(Counter(
            str((row["metadata"] or {}).get("tests_available")) for row in rows
        )),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--layout", choices=["directory", "classeval", "apps", "mbpp", "humaneval", "json"], required=True)
    parser.add_argument("--source")
    parser.add_argument("--license")
    args = parser.parse_args()
    rows = [profile_sample(*sample) for sample in read_samples(args.input, args.layout)]
    sources = [args.input] if args.input.is_file() else []
    if args.layout == "apps" and args.input.is_dir():
        sources = sorted(args.input.glob("*.parquet"))
    hashes = {}
    for source in sources:
        with source.open("rb") as stream:
            hashes[source.name] = file_digest(stream, "sha256").hexdigest()
    manifest = {
        "dataset": args.dataset, "source": args.source, "license": args.license,
        "input_sha256": hashes,
        "command": sys.argv, "python": sys.version,
        "versions": {package: version(package) for package in ("radon", "complexipy")},
        "summary": summarize(rows), "samples": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pending = args.output.with_suffix(".tmp")
    pending.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pending.replace(args.output)


if __name__ == "__main__":
    main()
