#!/usr/bin/env python3
"""Run APPS official input/output cases on saved Qwen/Llama code artifacts.

The APPS ZIPs used to prepare this experiment contain generated code and task
IDs, not APPS test cases. This runner fetches the public APPS test split via
Hugging Face ``datasets``, joins by APPS ``problem_id``, and executes the saved
original, marked, fmt_first, and Ruff-transformed artifacts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/apps500_quality/source_data"
CODE_ROOT = DATA / "artifacts_code"
SUMMARY_OUT = DATA / "apps_test_summary.csv"
CASES_OUT = DATA / "apps_test_cases.csv"

SUMMARY_FIELDS = (
    "artifact_id", "dataset", "problem_id", "sample_index", "arm", "variant",
    "ruff_profile", "ruff_mode", "artifact_path", "code_sha256", "status",
    "test_cases", "passed", "failed", "compile_errors", "runtime_errors", "timeouts",
    "strict_pass", "failed_case_indices", "case_results", "error",
)
CASE_FIELDS = (
    "artifact_id", "dataset", "problem_id", "sample_index", "arm", "variant",
    "ruff_profile", "ruff_mode", "case_index", "status", "passed", "actual", "error",
)

# Each code artifact gets its own interpreter process. That gives a wall-clock
# timeout and per-process resource limits; it is still not a complete security
# sandbox for arbitrary programs.
CHILD_RUNNER = r'''import builtins, contextlib, io, json, signal, sys, traceback

class CaseTimeout(Exception): pass
def timed_out(_signum, _frame): raise CaseTimeout("case time limit exceeded")

def plain(value):
    if isinstance(value, tuple): return [plain(x) for x in value]
    if isinstance(value, list): return [plain(x) for x in value]
    if isinstance(value, dict): return {str(k): plain(v) for k, v in value.items()}
    return value

def same_output(actual, expected):
    if plain(actual) == plain(expected): return True
    candidates = expected if isinstance(expected, list) else [expected]
    for candidate in candidates:
        if plain(actual) == plain(candidate): return True
        if isinstance(actual, str) and isinstance(candidate, str):
            a, e = actual.strip(), candidate.strip()
            if a == e or [x.strip() for x in a.splitlines()] == [x.strip() for x in e.splitlines()]: return True
            if sorted(a.split()) == sorted(e.split()): return True
            try:
                af, ef = [float(x) for x in a.split()], [float(x) for x in e.split()]
                if len(af) == len(ef) and all(abs(x-y) <= 1e-3 for x,y in zip(af,ef)): return True
            except Exception: pass
    return False

code_path = sys.argv[1]
timeout_seconds = float(sys.argv[2])
memory_mb = int(sys.argv[3])
spec = json.load(sys.stdin)
with open(code_path, encoding="utf-8") as f: source = f.read()
try:
    import resource
    memory = memory_mb * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
    resource.setrlimit(resource.RLIMIT_FSIZE, (32 * 1024 * 1024, 32 * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    cpu = max(2, int(timeout_seconds * max(1, len(spec.get("cases", []))) + 2))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu + 1))
except (ImportError, AttributeError, OSError, ValueError):
    pass
try:
    compiled = compile(source, code_path, "exec")
except Exception as exc:
    print(json.dumps({"compile_error": type(exc).__name__ + ": " + str(exc)}))
    raise SystemExit(0)

fn_name = spec.get("fn_name")
namespace = {"__name__": "__main__"}
if fn_name:
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            exec(compiled, namespace, namespace)
        target = namespace.get(fn_name)
        if target is None and "Solution" in namespace:
            target = getattr(namespace["Solution"](), fn_name)
        if target is None: raise AttributeError("function not found: " + str(fn_name))
    except Exception as exc:
        print(json.dumps({"compile_error": type(exc).__name__ + ": " + str(exc)}))
        raise SystemExit(0)

outcomes = []
signal.signal(signal.SIGALRM, timed_out)
for case in spec["cases"]:
    signal.alarm(max(1, int(timeout_seconds)))
    stdout = io.StringIO()
    try:
        if fn_name:
            args = case.get("input")
            if not isinstance(args, list): args = [args]
            value = target(*args)
            passed = same_output(value, case.get("expected"))
            actual = repr(plain(value))
        else:
            stdin = case.get("input", "")
            if isinstance(stdin, list): stdin = "\n".join(str(x) for x in stdin)
            old_stdin, old_stdout = sys.stdin, sys.stdout
            sys.stdin, sys.stdout = io.StringIO(str(stdin)), stdout
            try:
                exec(compiled, namespace, namespace)
            except SystemExit:
                pass
            finally:
                sys.stdin, sys.stdout = old_stdin, old_stdout
            actual = stdout.getvalue()
            passed = same_output(actual, case.get("expected"))
        outcomes.append({"status": "passed" if passed else "failed", "passed": bool(passed), "actual": str(actual)[:12000], "error": ""})
    except CaseTimeout as exc:
        outcomes.append({"status": "timeout", "passed": False, "actual": stdout.getvalue()[:12000], "error": str(exc)})
    except Exception as exc:
        outcomes.append({"status": "runtime_error", "passed": False, "actual": stdout.getvalue()[:12000], "error": type(exc).__name__ + ": " + str(exc)})
    finally:
        signal.alarm(0)
print(json.dumps({"outcomes": outcomes}, ensure_ascii=False))
'''


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def artifact_info(path: Path) -> dict[str, str]:
    parts = path.relative_to(CODE_ROOT).parts
    dataset, problem_id, sample_index = parts[:3]
    arm, variant, profile, mode = "main", "", "", ""
    tail = parts[3:]
    if tail[0] == "ruff":
        arm, variant, profile, mode = "ruff", tail[1], tail[2], Path(tail[3]).stem
    elif tail[0] == "fmt_first":
        arm, variant = "fmt_first", Path(tail[1]).stem
    else:
        variant = Path(tail[0]).stem
    rel = path.relative_to(ROOT).as_posix()
    return {
        "artifact_id": rel, "dataset": dataset, "problem_id": problem_id,
        "sample_index": sample_index, "arm": arm, "variant": variant,
        "ruff_profile": profile, "ruff_mode": mode, "artifact_path": rel,
        "code_sha256": sha256(path),
    }


def load_tests(wanted_ids: set[str], split: str) -> dict[str, dict[str, Any]]:
    try:
        from datasets import load_dataset
    except ImportError as exc:
        raise SystemExit("Missing dependency. Install it with: python3 -m pip install datasets") from exc
    print(f"Loading APPS {split!r} split from Hugging Face; this may download the dataset.", flush=True)
    records: dict[str, dict[str, Any]] = {}
    dataset = load_dataset("codeparrot/apps", split=split, streaming=True)
    for row in dataset:
        problem_id = str(row.get("problem_id", ""))
        if problem_id not in wanted_ids:
            continue
        raw = row.get("input_output")
        try:
            input_output = json.loads(raw) if isinstance(raw, str) else raw
            inputs = input_output["inputs"]
            outputs = input_output["outputs"]
            if len(inputs) != len(outputs):
                raise ValueError("input/output case counts differ")
            records[problem_id] = {
                "fn_name": input_output.get("fn_name"),
                "cases": [{"input": i, "expected": o} for i, o in zip(inputs, outputs, strict=True)],
            }
        except Exception as exc:
            records[problem_id] = {"fn_name": None, "cases": [], "data_error": f"{type(exc).__name__}: {exc}"}
        if len(records) == len(wanted_ids):
            break
    missing = wanted_ids - records.keys()
    if missing:
        print(f"APPS split did not return {len(missing)} selected problem IDs.", flush=True)
    return records


def evaluate_one(job: tuple[Path, dict[str, str], dict[str, Any], float, int]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    path, info, tests, timeout, memory_mb = job
    base = dict(info)
    base["error"] = ""
    cases = tests.get("cases", [])
    if tests.get("data_error"):
        base.update(status="test_data_error", test_cases=0, passed=0, failed=0,
                    compile_errors=0, runtime_errors=0, timeouts=0, strict_pass="",
                    failed_case_indices="", case_results="", error=tests["data_error"])
        return base, []
    if not cases:
        base.update(status="no_testcases", test_cases=0, passed=0, failed=0,
                    compile_errors=0, runtime_errors=0, timeouts=0, strict_pass="",
                    failed_case_indices="", case_results="", error="APPS input_output is empty or unavailable")
        return base, []

    wall_timeout = max(timeout * len(cases) + 8, 15)
    try:
        with tempfile.TemporaryDirectory(prefix="apps-artifact-") as workdir:
            run = subprocess.run(
                [sys.executable, "-I", "-c", CHILD_RUNNER, str(path), str(timeout), str(memory_mb)],
                input=json.dumps(tests, ensure_ascii=False), cwd=workdir,
                capture_output=True, text=True, timeout=wall_timeout,
                env={"PATH": os.environ.get("PATH", ""), "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8"},
            )
        payload = json.loads(run.stdout) if run.stdout.strip() else {}
        if payload.get("compile_error"):
            rows = [{"status": "compile_error", "passed": False, "actual": "", "error": payload["compile_error"]}
                    for _ in cases]
        else:
            rows = payload.get("outcomes", [])
            if len(rows) != len(cases):
                raise ValueError(f"runner returned {len(rows)} outcomes for {len(cases)} cases; exit={run.returncode}; {run.stderr[-1000:]}")
        if run.returncode and not rows:
            raise RuntimeError(f"runner exit {run.returncode}: {run.stderr[-2000:]}")
    except subprocess.TimeoutExpired:
        rows = [{"status": "timeout", "passed": False, "actual": "", "error": f"artifact exceeded {wall_timeout}s wall time"}
                for _ in cases]
    except Exception as exc:
        rows = [{"status": "runner_error", "passed": False, "actual": "",
                 "error": f"{type(exc).__name__}: {exc}"} for _ in cases]

    counts = {status: sum(row.get("status") == status for row in rows)
              for status in ("passed", "failed", "compile_error", "runtime_error", "timeout", "runner_error")}
    passed = counts["passed"]
    base.update(
        status="ok" if not any(counts[x] for x in ("compile_error", "runtime_error", "timeout", "runner_error")) else "error",
        test_cases=len(cases), passed=passed,
        failed=counts["failed"], compile_errors=counts["compile_error"],
        runtime_errors=counts["runtime_error"] + counts["runner_error"], timeouts=counts["timeout"],
        strict_pass=int(passed == len(cases)),
        failed_case_indices=";".join(str(index) for index, row in enumerate(rows, 1)
                                     if not row.get("passed")),
        case_results=json.dumps([row.get("status", "runner_error") for row in rows], separators=(",", ":")),
        error="" if not counts["runner_error"] else rows[0].get("error", ""),
    )
    case_rows = []
    for index, (test_case, outcome) in enumerate(zip(cases, rows, strict=True), 1):
        case_rows.append({
            **{key: info[key] for key in ("artifact_id", "dataset", "problem_id", "sample_index", "arm", "variant", "ruff_profile", "ruff_mode")},
            "case_index": index, "status": outcome.get("status", "runner_error"),
            "passed": int(bool(outcome.get("passed"))),
            "actual": "" if outcome.get("passed") else str(outcome.get("actual", ""))[:2000],
            "error": str(outcome.get("error", ""))[:2000],
        })
    return base, case_rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--code-root", type=Path, default=CODE_ROOT)
    parser.add_argument("--split", default="test", choices=("train", "test"))
    parser.add_argument("--workers", type=int, default=min(8, os.cpu_count() or 1))
    parser.add_argument("--timeout", type=float, default=3.0, help="CPU/wall limit in seconds per test case")
    parser.add_argument("--memory-mb", type=int, default=1024)
    parser.add_argument("--limit-artifacts", type=int, help="pilot only; omit to process every saved Python artifact")
    parser.add_argument("--summary-out", type=Path, default=SUMMARY_OUT)
    parser.add_argument("--cases-out", type=Path, default=CASES_OUT)
    args = parser.parse_args()

    code_root = args.code_root.resolve()
    artifacts = sorted(path for path in code_root.rglob("*.py") if path.is_file())
    if args.limit_artifacts:
        artifacts = artifacts[:args.limit_artifacts]
    if not artifacts:
        raise SystemExit(f"No Python artifacts found under {code_root}")
    infos = [(path, artifact_info(path)) for path in artifacts]
    tests = load_tests({info["problem_id"] for _, info in infos}, args.split)
    print(f"Testing {len(artifacts)} saved code artifacts across {len(tests)} APPS problems.", flush=True)

    args.summary_out.parent.mkdir(parents=True, exist_ok=True)
    args.cases_out.parent.mkdir(parents=True, exist_ok=True)
    summary_tmp = args.summary_out.with_suffix(args.summary_out.suffix + ".tmp")
    cases_tmp = args.cases_out.with_suffix(args.cases_out.suffix + ".tmp")
    completed = 0
    started = time.monotonic()
    with summary_tmp.open("w", newline="", encoding="utf-8") as summary_stream, \
         cases_tmp.open("w", newline="", encoding="utf-8") as cases_stream:
        summary_writer = csv.DictWriter(summary_stream, fieldnames=SUMMARY_FIELDS, lineterminator="\n")
        case_writer = csv.DictWriter(cases_stream, fieldnames=CASE_FIELDS, lineterminator="\n")
        summary_writer.writeheader()
        case_writer.writeheader()
        jobs = []
        for path, info in infos:
            problem_tests = tests.get(info["problem_id"])
            if problem_tests is None:
                problem_tests = {"fn_name": None, "cases": [], "data_error": "problem_id missing from APPS split"}
            jobs.append((path, info, problem_tests, args.timeout, args.memory_mb))
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
            job_iter = iter(jobs)
            pending = set()
            for _ in range(min(len(jobs), max(1, args.workers) * 4)):
                pending.add(pool.submit(evaluate_one, next(job_iter)))
            while pending:
                finished, pending = wait(pending, return_when=FIRST_COMPLETED)
                for future in finished:
                    summary, case_rows = future.result()
                    summary_writer.writerow(summary)
                    case_writer.writerows(case_rows)
                    completed += 1
                    try:
                        pending.add(pool.submit(evaluate_one, next(job_iter)))
                    except StopIteration:
                        pass
                if completed % 250 == 0 or completed == len(jobs):
                    elapsed = time.monotonic() - started
                    print(f"completed {completed}/{len(jobs)} artifacts in {elapsed:.0f}s", flush=True)
    summary_tmp.replace(args.summary_out)
    cases_tmp.replace(args.cases_out)
    print(f"Summary: {args.summary_out}")
    print(f"Case details: {args.cases_out}")
    print("Update the one-workbook output with: python3 experiments/export_apps500_detection_excel.py")


if __name__ == "__main__":
    main()
