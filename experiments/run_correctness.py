"""Run benchmark probes in independent network-isolated processes."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import random
import subprocess
import time

from select_samples import rows, write_json

WORKER = Path(__file__).with_name("benchmark_worker.py").resolve()
DATASETS = ("mercury_eval", "classeval", "apps")
VARIANTS = ("original", "sew", "acw_notab", "acw_full")
ADAPTER_VERSION = 4


def read(path):
    return json.loads(path.read_text())


def run(argv, stdin=None):
    start = time.monotonic()
    try:
        proc = subprocess.run(argv, input=stdin, text=True, errors="replace", capture_output=True, timeout=6)
        return {"argv": argv, "exit": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
                "seconds": time.monotonic() - start}
    except subprocess.TimeoutExpired as error:
        return {"argv": argv, "exit": None, "status": "timeout",
                "stdout": (error.stdout or b"").decode(errors="replace"),
                "stderr": (error.stderr or b"").decode(errors="replace"), "seconds": time.monotonic()-start}


def sandbox(source, payload, mode, deps, stdin=None):
    argv = ["prlimit", "--as=1073741824", "--cpu=5", "--fsize=4194304", "--nofile=64", "--",
            "bwrap", "--unshare-all", "--die-with-parent", "--clearenv", "--setenv", "PATH", "/usr/bin",
            "--setenv", "HOME", "/tmp", "--setenv", "PYTHONDONTWRITEBYTECODE", "1",
            "--setenv", "PYTHONHASHSEED", "0", "--setenv", "TZ", "UTC",
            "--setenv", "OPENBLAS_NUM_THREADS", "1",
            "--ro-bind", "/usr", "/usr", "--symlink", "usr/lib", "/lib",
            "--symlink", "usr/lib64", "/lib64", "--proc", "/proc", "--dev", "/dev",
            "--tmpfs", "/tmp", "--chdir", "/tmp"]
    if deps:
        argv += ["--ro-bind", str(deps), "/tmp/deps", "--setenv", "PYTHONPATH", "/tmp/deps"]
    if source:
        argv += ["--ro-bind", str(source), "/tmp/solution.py"]
    if mode == "apps_stdin":
        return run([*argv, "--", "/usr/bin/python3.14", "/tmp/solution.py"], stdin)
    argv += ["--ro-bind", str(payload), "/tmp/payload.json", "--ro-bind", str(WORKER), "/tmp/worker.py",
             "--", "/usr/bin/python3.14", "/tmp/worker.py", mode, "/tmp/payload.json"]
    if source:
        argv.append("/tmp/solution.py")
    result = run(argv)
    if result["exit"] == 0:
        try:
            result["result"] = json.loads(result["stdout"])["answer"]
        except (ValueError, KeyError, TypeError):
            pass
    return result


def subset(records, cap, rng):
    return sorted(rng.sample(range(len(records)), min(cap, len(records))))


def outputs(run):
    if run["exit"] != 0:
        return None
    return run.get("result", run["stdout"])


def equivalent_stdout(left, right):
    return left.split() == right.split()


def test_apps(code, payload, folder, deps):
    result = []
    for index in payload["selected"]:
        passed = None
        call = bool(payload.get("fn_name"))
        value = payload["inputs"][index]
        expected = payload["outputs"][index]
        if call:
            path = folder / f"input_{index}.json"
            write_json(path, {"fn_name": payload["fn_name"], "input": value})
            process = sandbox(code, path, "apps_call", deps)
            if process.get("result") is not None:
                got = json.loads(process["result"]["result"])
                passed = got == expected or (isinstance(expected, list) and expected == [got])
        else:
            value = "\n".join(map(str, value)) if isinstance(value, list) else str(value)
            if not value.endswith("\n"):
                value += "\n"
            process = sandbox(code, None, "apps_stdin", deps, value)
            if process["exit"] == 0:
                expected = "\n".join(map(str, expected)) if isinstance(expected, list) else str(expected)
                passed = equivalent_stdout(process["stdout"], expected)
        result.append({"case": index, "official_pass": passed, "process": process})
    return result


def benchmark(job):
    dataset, folder, sample, row, deps = job
    out = folder / "correctness_v2"
    path = out / "result.json"
    if path.exists():
        previous = read(path)
        if previous.get("adapter_version") == ADAPTER_VERSION:
            return previous
        previous_run = out / f'adapter_{previous.get("adapter_version", 2)}'
        previous_run.mkdir(exist_ok=True)
        for logged in out.glob("*.json"):
            logged.replace(previous_run / logged.name)
    out.mkdir(parents=True, exist_ok=True)
    seed = int.from_bytes(hashlib.sha256(sample["sample_id"].encode()).digest()[:8], "big")
    rng = random.Random(seed)
    tests = None
    if dataset == "mercury_eval":
        official = json.loads(row["test_cases"])
        indices = subset(official, 10, rng)
        write_json(out / "generator_input.json", {"generator_code": row["generator_code"], "seed": seed,
                   "limit": 10, "official": official[:1]})
        generator = sandbox(None, out / "generator_input.json", "mercury_generate", deps)
        write_json(out / "generator_run.json", generator)
        generated = generator.get("result", [])
        cases = [official[i] for i in indices] + [{"input": value} for value in generated]
        tests = {"cases": cases, "published_indices": indices, "seed": seed,
                 "convert_offline": row["convert_offline"], "evaluate_offline": row["evaluate_offline"],
                 "entry_point": row["entry_point"]}
    elif dataset == "classeval":
        tests = {"test": row["test"], "test_classes": row["test_classes"], "seed": seed,
                 "freeze": "2024-01-01 12:00:00" if sample["sample_id"] == "ClassEval_17" else None}
    else:
        data = json.loads(row["input_output"] or "{}")
        if data.get("inputs") and data.get("outputs"):
            tests = {**data, "selected": subset(data["inputs"], 20, rng), "seed": seed}
    if tests is None:
        output = {"dataset": dataset, "sample_id": sample["sample_id"], "status": "not_run",
                  "reason": "missing_tests", "adapter_version": ADAPTER_VERSION}
        write_json(path, output)
        return output
    payload = out / "cases.json"
    write_json(payload, tests)
    if dataset == "mercury_eval":
        official_payload = out / "official_cases.json"
        generated_payload = out / "generated_cases.json"
        write_json(official_payload, {**tests, "cases": [case for case in tests["cases"] if "expected" in case]})
        write_json(generated_payload, {**tests, "cases": [case for case in tests["cases"] if "expected" not in case]})
    outcome = {}
    embedded = read(folder / "result.json")["variants"]
    for variant in VARIANTS:
        source = Path(embedded[variant]["embedded"]["path"])
        if dataset == "apps":
            log = test_apps(source, tests, out, deps)
            observed = [outputs(x["process"]) for x in log]
            pass_flags = [x["official_pass"] for x in log]
        elif dataset == "mercury_eval":
            official = sandbox(source, official_payload, "mercury", deps)
            generated = sandbox(source, generated_payload, "mercury", deps)
            official_count = len(tests["published_indices"])
            generated_count = len(tests["cases"]) - official_count
            official_answer = official.get("result", {})
            generated_answer = generated.get("result", {})
            observed = official_answer.get("outputs", [None]*official_count) + generated_answer.get("outputs", [None]*generated_count)
            pass_flags = official_answer.get("verdicts", [None]*official_count)
            log = {"official": official, "generated": generated,
                   "status": "timeout" if any(x.get("status") == "timeout" for x in (official, generated)) else None}
        else:
            log = sandbox(source, payload, "classeval", deps)
            answer = log.get("result")
            if answer:
                observed = [answer["observed"]]
                pass_flags = [answer["pass"]]
            else:
                observed = [None]
                pass_flags = [None]
        write_json(out / f"{variant}.json", log)
        base = outcome.get("original", {}).get("observed")
        original_available = base is not None and any(x is not None for x in base)
        match = None
        if variant == "original" and any(x is not None for x in observed):
            match = True
        if original_available:
            pairs = [(x, y) for x, y in zip(base, observed) if x is not None]
            if pairs:
                if dataset == "apps" and not tests.get("fn_name"):
                    match = all(isinstance(y, str) and equivalent_stdout(x, y) for x, y in pairs)
                else:
                    match = all(x == y for x, y in pairs)
        outcome[variant] = {"observed": observed,
                            "official": "pass" if pass_flags and all(x is True for x in pass_flags)
                            else "fail" if any(x is False for x in pass_flags) else "error",
                            "differential": "identical" if match else "different" if match is False else "error",
                            "timeouts": sum(x["process"].get("status") == "timeout" for x in log)
                            if isinstance(log, list) else int(log.get("status") == "timeout")}
    result = {"dataset": dataset, "sample_id": sample["sample_id"], "status": "run",
              "adapter_version": ADAPTER_VERSION, "variants": outcome, "comparison": "public_call_return_trace" if dataset == "classeval" else "outputs"}
    write_json(path, result)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--study", type=Path, required=True)
    p.add_argument("--measurements", type=Path, required=True)
    p.add_argument("--mercury", type=Path, required=True)
    p.add_argument("--classeval", type=Path, required=True)
    p.add_argument("--apps", type=Path, nargs="+", required=True)
    p.add_argument("--freezegun", type=Path)
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--pilot", action="store_true")
    args = p.parse_args()
    study, measurement = args.study.resolve(), args.measurements.resolve()
    mercury = {r["slug_name"]: r for r in rows(args.mercury, ["slug_name", "test_cases", "generator_code",
               "convert_offline", "evaluate_offline", "entry_point"])}
    classeval = {r["task_id"]: r for r in read(args.classeval)}
    apps = {str(r["problem_id"]): r for path in args.apps
            for r in rows(path, ["problem_id", "input_output"])}
    jobs = []
    for name, dataset in zip(DATASETS, (mercury, classeval, apps), strict=True):
        selection = read(study / name / "selection.json")
        ids = set(selection["pilot"]) if args.pilot else None
        for sample in selection["samples"]:
            identity = sample["sample_id"]
            if ids is None or identity in ids:
                folder = measurement / name / identity
                if (folder / "result.json").exists():
                    jobs.append((name, folder, sample, dataset[identity],
                                 args.freezegun.resolve() if args.freezegun else None))
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for index, _ in enumerate(pool.map(benchmark, jobs), 1):
            if index % 20 == 0:
                print(f"{index}/{len(jobs)}", flush=True)


if __name__ == "__main__":
    main()
