"""Run the paired watermark and Ruff measurements in resumable batches."""

import argparse
import ast
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stderr, redirect_stdout
import difflib
from hashlib import sha256
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
import tokenize

import autopep8

from select_samples import write_json

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "SEW"), str(ROOT / "ACW/source")]
from sew import detect, embed
from base_ast import (transform_operations_add, transform_operations_mult,
                      transform_comparison_LG, transform_comparison_LGE)
from one_rule_format import tab_convert_process

KEYS = [bytes.fromhex(byte * 16) for byte in ("76", "31", "92")]
PROFILES = {"default": [], "strict": ["--select", "E,F,W,I,B,UP,SIM"]}
MODES = ("check", "fix", "format", "fix_format")
VARIANTS = ("original", "sew", "acw_notab", "acw_full")
GROUPS = ("E225,E226,E227,E228,E241,E242,E251,E252,E231", "E27", "E123", "W292",
          "E301,E302,E305,E306")
TRANSFORMS = (transform_operations_add, transform_operations_mult,
              transform_comparison_LG, transform_comparison_LGE)
DATASETS = ("mercury_eval", "classeval", "apps")


def command(argv, timeout=120):
    started = time.monotonic()
    try:
        result = subprocess.run(argv, capture_output=True, timeout=timeout)
        return dict(argv=argv, exit=result.returncode, stdout=result.stdout.decode(errors="replace"),
                    stderr=result.stderr.decode(errors="replace"), seconds=time.monotonic() - started)
    except subprocess.TimeoutExpired as error:
        return dict(argv=argv, exit=None, stdout=(error.stdout or b"").decode(errors="replace"),
                    stderr=(error.stderr or b"").decode(errors="replace"), seconds=time.monotonic() - started,
                    error="timeout")


def read(path):
    return path.read_bytes().decode("utf-8")


def tree(code):
    try:
        result = ast.parse(code)
        compile(result, "<sample>", "exec")
        return result, None
    except (SyntaxError, ValueError) as error:
        return None, str(error)


def tokens(code):
    try:
        return [(token.type, token.string) for token in tokenize.generate_tokens(io.StringIO(code).readline)
                if token.type not in {tokenize.COMMENT, tokenize.NL, tokenize.NEWLINE,
                                      tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER}]
    except (SyntaxError, tokenize.TokenError):
        return None


def invasion(original, candidate):
    a, b = original.splitlines(), candidate.splitlines()
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    ta, tb = tokens(original), tokens(candidate)
    t1, t2 = tree(original)[0], tree(candidate)[0]
    return {
        "line_similarity": matcher.ratio(),
        "changed_lines": sum(max(j-i, l-k) for op, i, j, k, l in matcher.get_opcodes() if op != "equal"),
        "token_similarity": difflib.SequenceMatcher(None, ta, tb, autojunk=False).ratio()
        if ta is not None and tb is not None else None,
        "delta_tokens": len(tb) - len(ta) if ta is not None and tb is not None else None,
        "delta_ast_nodes": sum(1 for _ in ast.walk(t2)) - sum(1 for _ in ast.walk(t1))
        if t1 is not None and t2 is not None else None,
        "ast_equal": ast.dump(t1) == ast.dump(t2) if t1 is not None and t2 is not None else None,
    }


def local_acw(input_path, out, audit=False, tabs=True):
    out.mkdir(parents=True, exist_ok=True)
    path = out / "without_tabs.py"
    shutil.copyfile(input_path, path)
    log = io.StringIO()
    steps = []
    with redirect_stdout(log), redirect_stderr(log):
        for rule, transform in enumerate(TRANSFORMS, 36):
            before = path.read_bytes()
            transform(str(path))
            after = path.read_bytes()
            steps.append({"rule": rule, "changed": before != after})
            if audit and before != after:
                (out / f"rule_{rule}.py").write_bytes(after)
        for rule, group in enumerate(GROUPS, 40):
            before = read(path)
            after = autopep8.fix_code(before, options={"select": group.split(",")})
            path.write_bytes(after.encode())
            steps.append({"rule": rule, "changed": before != after})
            if audit and before != after:
                (out / f"rule_{rule}.py").write_bytes(after.encode())
        full = out / "with_tabs.py"
        if tabs:
            shutil.copyfile(path, full)
            tab_convert_process(45, str(full))
            steps.append({"rule": 45, "changed": path.read_bytes() != full.read_bytes()})
    (out / "local.log").write_text(log.getvalue(), encoding="utf-8")
    write_json(out / "steps.json", steps)
    return path, full


def static_metrics(path, script):
    result = {}
    radon = ("raw",) if script else ("raw", "cc", "mi", "hal")
    for name in radon:
        result[name] = command(["radon", name, "-j", str(path)])
    target = path.with_name("complexipy.json")
    target.unlink(missing_ok=True)
    script_flag = ["--check-script"] if script else []
    result["complexipy"] = command(["complexipy", "--isolated", "--no-ignore", *script_flag,
                                    "--output-format", "json", "--output", str(target), str(path)])
    if target.exists():
        result["complexipy"]["data"] = json.loads(read(target))
    return result


def measure_state(path, original, variant, script, static):
    code = read(path)
    state = {"path": str(path), "sha256": sha256(path.read_bytes()).hexdigest(),
             "changed": code != original, "syntax_error": tree(code)[1],
             "invasion": invasion(original, code),
             "tab_lines": sum(line.startswith("\t") for line in code.splitlines())}
    if variant in ("original", "sew"):
        keys = KEYS if variant == "original" else KEYS[:1]
        state["sew"] = [detect(code, "python", key, alpha=.01) for key in keys]
    if static:
        state["metrics"] = static_metrics(path, script)
    return state


def diagnostics(path, profile):
    run = command(["ruff", "check", "--isolated", "--no-cache", *PROFILES[profile],
                   "--output-format", "json", str(path)])
    try:
        codes = Counter(item["code"] or "invalid-syntax" for item in json.loads(run["stdout"]))
        return run, dict(codes)
    except (ValueError, TypeError, KeyError):
        return run, None


def measure_variant(job):
    folder, original_path, source, variant, script = job
    original = read(original_path)
    base = folder / variant / "embedded" / "code.py"
    base.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, base)
    states = {"embedded": measure_state(base, original, variant, script, True)}
    baseline = {profile: diagnostics(base, profile) for profile in PROFILES}
    states["embedded"]["ruff_baseline"] = {
        profile: {"diagnostic_command": run, "diagnostics": codes}
        for profile, (run, codes) in baseline.items()
    }
    for profile, options in PROFILES.items():
        for mode in MODES:
            dest = folder / variant / profile / mode / "code.py"
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(base, dest)
            operations = []
            if mode in ("fix", "fix_format"):
                operations.append(command(["ruff", "check", "--isolated", "--no-cache",
                                           *options, "--fix", str(dest)]))
                if mode == "fix_format":
                    shutil.copyfile(dest, dest.with_name("after_fix.py"))
            if mode in ("format", "fix_format"):
                operations.append(command(["ruff", "format", "--isolated", "--no-cache", str(dest)]))
            run, codes = baseline[profile] if mode == "check" else diagnostics(dest, profile)
            state = measure_state(dest, original, variant, script, mode == "fix_format")
            state.update(operations=operations, diagnostic_command=run, diagnostics=codes)
            states[f"{profile}/{mode}"] = state
    return states


def sourcery(directory, config, log):
    result = command(["sourcery", "review", "--config", str(config), "--fix", str(directory)], timeout=3600)
    write_json(log, result)
    if result["exit"] != 0:
        raise RuntimeError(f"Sourcery zakończył się kodem {result['exit']}. Zobacz {log}")


def fresh(path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def analyze_batch(output, batch_dir, batch, config, workers):
    embedding = batch_dir / "sourcery_embedding"
    fresh(embedding)
    records = []
    for index, (dataset, meta, original) in enumerate(batch):
        folder = output / dataset / meta["sample_id"]
        acw_path = embedding / f"{index:04d}.py"
        shutil.copyfile(original, acw_path)
        emb = embed(read(original), "python", KEYS[0])
        sew = folder / "sew_source.py"
        sew.parent.mkdir(parents=True, exist_ok=True)
        sew.write_bytes(emb.pop("code").encode())
        records.append((dataset, meta, original, folder, acw_path, sew, emb))
    sourcery(embedding, config, batch_dir / "embedding.json")
    jobs = []
    for _, meta, original, folder, acw_path, sew, _ in records:
        shutil.copyfile(acw_path, folder / "after_sourcery.py")
        notab, full = local_acw(acw_path, folder / "acw_steps", audit=True)
        for variant, path in zip(VARIANTS, (original, sew, notab, full), strict=True):
            jobs.append((folder, original, path, variant, meta["structure"] == "script"))
    with ThreadPoolExecutor(max_workers=workers) as executor:
        measured = list(executor.map(measure_variant, jobs))
    detection = batch_dir / "sourcery_detection"
    fresh(detection)
    replays = {}
    for job, states in zip(jobs, measured, strict=True):
        _, _, _, variant, _ = job
        if variant == "sew":
            continue
        for state in states.values():
            if state["syntax_error"]:
                state["acw"] = {"reason": "invalid_syntax"}
                continue
            src = Path(state["path"])
            digest = state["sha256"]
            if digest not in replays:
                changed = detection / f"{len(replays):05d}.py"
                shutil.copyfile(src, changed)
                replays[digest] = (src, changed, [])
            replays[digest][2].append((state, variant))
    if replays:
        sourcery(detection, config, batch_dir / "detection.json")
        for digest, (original, after_sourcery, states) in replays.items():
            path = batch_dir / "acw_replay" / digest
            tabs = any(variant != "acw_notab" for _, variant in states)
            notab, full = local_acw(after_sourcery, path, tabs=tabs)
            versions = {"acw_notab": notab, "acw_full": full}
            fixed = {name: target.read_bytes() == original.read_bytes()
                     for name, target in versions.items() if target.exists()}
            for state, variant in states:
                state["acw"] = {name: fixed[name] for name in (fixed if variant == "original" else (variant,))}
                state["acw_replay"] = str(path)
    for index, (dataset, meta, _, folder, _, _, emb) in enumerate(records):
        states = dict(zip(VARIANTS, measured[index * 4:(index + 1) * 4], strict=True))
        write_json(folder / "result.json", {"dataset": dataset, "sample": meta,
                                            "sew_embedding": emb, "variants": states})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--batch-size", type=int, default=20)
    args = parser.parse_args()
    study = args.study.resolve()
    output = args.output.resolve()
    configuration = ROOT / "results/full_watermark_study/acw_sourcery.yaml"
    tools = ("radon", "complexipy", "ruff", "autopep8", "sourcery")
    versions = {name: command([name, "--version"]) for name in tools}
    if any(result["exit"] != 0 for result in versions.values()):
        raise RuntimeError("Brak narzędzia pomiarowego: " + str(versions))
    hypothesis = study / "hipotezy.md"
    frozen = (study / "hipotezy.sha256").read_text().split()[0]
    if sha256(hypothesis.read_bytes()).hexdigest() != frozen:
        raise ValueError("Frozen hypotheses checksum does not match")
    write_json(output / "environment.json", {"python": sys.version, "commands": versions,
               "hypotheses_sha256": frozen,
               "config_sha256": sha256(configuration.read_bytes()).hexdigest(), "argv": sys.argv})
    pending = []
    for dataset in DATASETS:
        selection = json.loads(read(study / dataset / "selection.json"))
        samples = selection["samples"]
        if args.pilot:
            ids = set(selection["pilot"])
            samples = [sample for sample in samples if sample["sample_id"] in ids]
        for sample in samples:
            identity = sample["sample_id"]
            target = output / dataset / identity / "result.json"
            if target.exists() and json.loads(read(target))["sample"] == sample:
                continue
            original = study / dataset / identity / "original.py"
            if sha256(original.read_bytes()).hexdigest() != sample["sha256"]:
                raise ValueError(f"SHA-256 mismatch: {original}")
            pending.append((dataset, sample, original))
    for offset in range(0, len(pending), args.batch_size):
        batch = pending[offset:offset + args.batch_size]
        digest = sha256(repr([(name, row["sample_id"]) for name, row, _ in batch]).encode()).hexdigest()[:16]
        analyze_batch(output, output / "batches" / digest, batch, configuration, args.workers)
        print(f"{min(offset + len(batch), len(pending))}/{len(pending)}", flush=True)
    for dataset in DATASETS:
        results = [json.loads(read(path)) for path in sorted((output / dataset).glob("*/result.json"))]
        write_json(output / dataset / "results.json", results)


if __name__ == "__main__":
    main()
