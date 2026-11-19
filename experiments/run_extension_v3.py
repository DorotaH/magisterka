"""Run the frozen extension v3 using the main study measurement pipeline."""

import argparse
import fcntl
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from hashlib import sha256
from pathlib import Path

from run_correctness import benchmark
from run_main_study import analyze_batch, command
from select_extension_classeval import EXTENSION, ROOT
from select_samples import write_json

MAIN = ROOT / "results/main_study"
CONFIG = ROOT / "results/full_watermark_study/acw_sourcery.yaml"


def read_json(path):
    return json.loads(path.read_bytes())


def verify_frozen(path, checksum):
    expected = checksum.read_text().split()[0]
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"Niezgodna suma kontrolna {path}")
    return expected


def selected_sources(layer, inputs):
    if layer == "warstwa_C":
        selection = read_json(EXTENSION / layer / "selection.json")
        for source, expected in selection["source_sha256"].items():
            path = (inputs if source == "classeval.json" else EXTENSION / layer) / source
            if sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError(f"Niezgodny SHA-256 {path}")
        for name in sorted({row["dataset"] for row in selection["samples"]}):
            source = EXTENSION / layer / name / "generations.jsonl"
            records = {(row["task_id"], row["sample_index"]): row["code"]
                       for row in map(json.loads, source.read_bytes().splitlines())}
            for row in selection["samples"]:
                if row["dataset"] == name:
                    yield name, row, records[row["task_id"], row["sample_index"]]
        return
    selection = read_json(EXTENSION / layer / "selection.json")
    for row in selection["samples"]:
        path = EXTENSION / layer / row["dataset"] / row["sample_id"] / "original.py"
        yield row["dataset"], row, path.read_bytes().decode()


def measure(args, layer):
    output = args.output / layer
    selected = list(selected_sources(layer, args.inputs))
    pending = []
    for dataset, sample, code in selected:
        content = code.encode()
        if sha256(content).hexdigest() != sample["sha256"]:
            raise ValueError(f"Niezgodny SHA-256 próbki {sample['sample_id']}")
        folder = output / dataset / sample["sample_id"]
        target = folder / "result.json"
        if target.exists():
            if read_json(target)["sample"] != sample:
                raise ValueError(f"Poprzedni wynik różni się od bieżącej selekcji: {target}")
            continue
        folder.mkdir(parents=True, exist_ok=True)
        original = folder / "original.py"
        original.write_bytes(content)
        pending.append((dataset, sample, original))
        if args.limit is not None and len(pending) >= args.limit:
            break

    batches = []
    for offset in range(0, len(pending), args.batch_size):
        batch = pending[offset:offset + args.batch_size]
        batch_hash = sha256(repr([(name, row["sample_id"], row["sha256"])
                                  for name, row, _ in batch]).encode()).hexdigest()[:16]
        batches.append((output, output / "batches" / batch_hash, batch, CONFIG, args.workers))
    if batches:
        execute_batches(batches, layer, args.parallel_batches, len(pending))
    return [(dataset, sample) for dataset, sample, _ in selected
            if (output / dataset / sample["sample_id"] / "result.json").is_file()]


def worker_state(directory):
    state = directory / str(os.getpid())
    state.mkdir(parents=True, exist_ok=True)
    os.environ["XDG_DATA_HOME"] = str(state)


def execute_batches(batches, layer, parallelism, total):
    completed = 0
    if parallelism == 1:
        for job in batches:
            analyze_batch(*job)
            completed += len(job[2])
            print(layer, completed, total, flush=True)
        return
    state_dir = batches[0][0] / "sourcery_worker_state"
    with ProcessPoolExecutor(max_workers=parallelism, initializer=worker_state,
                             initargs=(state_dir,)) as pool:
        futures = {pool.submit(analyze_batch, *job): len(job[2]) for job in batches}
        try:
            for future in as_completed(futures):
                future.result()
                completed += futures[future]
                print(layer, completed, total, flush=True)
        finally:
            for future in futures:
                future.cancel()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--layer", choices=("warstwa_A", "warstwa_C"), required=True)
    parser.add_argument("--deps", type=Path)
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=40)
    parser.add_argument("--parallel-batches", type=int, default=1)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--correctness", action="store_true")
    args = parser.parse_args()
    args.output = args.output.resolve()
    if min(args.workers, args.batch_size, args.parallel_batches) < 1:
        parser.error("Liczba procesów, wątków i rozmiar partii muszą być dodatnie")
    if args.output == MAIN or MAIN in args.output.parents:
        raise ValueError("Wyniki rozszerzenia wymagają osobnego katalogu")
    if args.correctness and (args.layer != "warstwa_C" or args.deps is None):
        parser.error("--correctness wymaga warstwy C i --deps")

    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / f"{args.layer}.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        run_layer(args)


def run_layer(args):
    protocol_hash = verify_frozen(EXTENSION / "protokol.md", EXTENSION / "protokol.sha256")
    hypothesis_hash = verify_frozen(MAIN / "hipotezy.md", MAIN / "hipotezy.sha256")
    expected_env = read_json(MAIN / "environment.json")
    versions = {name: command([name, "--version"]) for name in expected_env["commands"]}
    if any(result["exit"] != 0 or result["stdout"] != expected_env["commands"][name]["stdout"]
           for name, result in versions.items()):
        raise RuntimeError("Niezgodne wersje narzędzi pomiarowych")
    if sys.version.split()[0] != expected_env["python"].split()[0]:
        raise RuntimeError("Niezgodna wersja Pythona")
    config_hash = sha256(CONFIG.read_bytes()).hexdigest()
    if config_hash != expected_env["config_sha256"]:
        raise RuntimeError("Niezgodna konfiguracja Sourcery")
    write_json(args.output / args.layer / "environment.json", {
        "python": sys.version, "commands": versions, "protocol_sha256": protocol_hash,
        "hypotheses_sha256": hypothesis_hash, "config_sha256": config_hash,
    })
    selected = measure(args, args.layer)
    if args.correctness:
        output = args.output / args.layer
        dataset = {row["task_id"]: row for row in read_json(args.inputs / "classeval.json")}
        jobs = [("classeval", output / name / sample["sample_id"], sample,
                 dataset[sample["task_id"]], args.deps.resolve())
                for name, sample in selected if sample["tests_available"]]
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for _ in pool.map(benchmark, jobs):
                pass


if __name__ == "__main__":
    main()
