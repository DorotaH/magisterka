"""Shared command-line helpers for processing Python files in batches."""

from __future__ import annotations

import argparse
import contextlib
import importlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


@contextlib.contextmanager
def suppress_child_output():
    sys.stdout.flush()
    sys.stderr.flush()
    saved_stdout, saved_stderr = os.dup(1), os.dup(2)
    with open(os.devnull, "w") as sink:
        try:
            os.dup2(sink.fileno(), 1)
            os.dup2(sink.fileno(), 2)
            yield
        finally:
            os.dup2(saved_stdout, 1)
            os.dup2(saved_stderr, 2)
            os.close(saved_stdout)
            os.close(saved_stderr)


def add_io_arguments(parser: argparse.ArgumentParser, output_help: str = "Output directory") -> None:
    parser.add_argument("--input", required=True, type=Path, help="Python file or directory")
    parser.add_argument("--output", required=True, type=Path, help=output_help)


def setup_sew():
    sew_path = str(ROOT / "SEW")
    if sew_path not in sys.path:
        sys.path.insert(0, sew_path)
    local = ROOT / "ACW/.tools/local/lib"
    for package_path in local.glob("python*/*-packages"):
        package = str(package_path)
        if package not in sys.path:
            sys.path.insert(0, package)
        os.environ["PYTHONPATH"] = package + os.pathsep + os.environ.get("PYTHONPATH", "")
    return importlib.import_module("sew")


def acw_single_process_file():
    acw = ROOT / "ACW"
    source = str(acw / "source")
    if source not in sys.path:
        sys.path.insert(0, source)
    local = acw / ".tools/local"
    os.environ["PATH"] = str(local / "bin") + os.pathsep + os.environ.get("PATH", "")
    for package_path in (local / "lib").glob("python*/*-packages"):
        if str(package_path) not in sys.path:
            sys.path.insert(0, str(package_path))
        os.environ["PYTHONPATH"] = str(package_path) + os.pathsep + os.environ.get("PYTHONPATH", "")
    from one_rule_format import single_process_file

    return single_process_file


def apply_acw_files(
    paths: list[Path], variant: str, batch_size: int = 50
) -> list[dict[str, Any]]:
    if batch_size < 1:
        raise ValueError("batch_size must be at least 1")

    method = acw_single_process_file()
    from refact_list import refactoring_list

    errors_by_path: dict[Path, list[dict[str, Any]]] = {path: [] for path in paths}
    chunks = [paths[i:i + batch_size] for i in range(0, len(paths), batch_size)]
    sourcery = shutil.which("sourcery")
    if not sourcery:
        raise FileNotFoundError("Sourcery CLI was not found")

    # ACW applies these rules sequentially. Applying one rule to a batch keeps
    # the same per-file order while avoiding one CLI startup per file and rule.
    authentication_failed = False
    for rule_number, rule_name in enumerate(refactoring_list, start=1):
        for chunk in chunks:
            if authentication_failed:
                for path in chunk:
                    errors_by_path[path].append({
                        "rule": rule_number,
                        "message": "skipped after Sourcery authentication failure",
                    })
                continue

            with tempfile.TemporaryDirectory(prefix=f"acw-sourcery-{rule_number}-") as directory:
                batch_dir = Path(directory)
                staged_paths = []
                for index, path in enumerate(chunk):
                    staged = batch_dir / f"{index:05d}_{path.name}"
                    shutil.copyfile(path, staged)
                    staged_paths.append(staged)

                command = [sourcery, "review", "--fix", "--enable", rule_name,
                           "--verbose", str(batch_dir)]
                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=False)
                    messages = (result.stdout or "") + (result.stderr or "")
                    failed = result.returncode != 0 or re.search(
                        r"failed to authenticate|command failed|traceback", messages,
                        re.IGNORECASE,
                    )
                    if failed:
                        detail = messages.strip()[-2000:] or f"exit status {result.returncode}"
                        for path in chunk:
                            errors_by_path[path].append({"rule": rule_number, "message": detail})
                        if re.search(r"failed to authenticate|api\.sourcery\.ai", messages,
                                      re.IGNORECASE):
                            authentication_failed = True
                    for path, staged in zip(chunk, staged_paths, strict=True):
                        shutil.copyfile(staged, path)
                except (OSError, subprocess.SubprocessError) as error:
                    detail = f"{type(error).__name__}: {error}"
                    for path in chunk:
                        errors_by_path[path].append({"rule": rule_number, "message": detail})

    # The remaining transformations are local and retain ACW's original order.
    local_rules = range(36, 46 if variant == "acw_full" else 45)
    for path in paths:
        for rule in local_rules:
            stdout, stderr = io.StringIO(), io.StringIO()
            try:
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    method(rule, str(path))
                messages = stdout.getvalue() + stderr.getvalue()
                if re.search(r"error processing|traceback|rule \d+ exec failed",
                             messages, re.IGNORECASE):
                    errors_by_path[path].append({"rule": rule, "message": messages.strip()[-2000:]})
            except Exception as error:
                errors_by_path[path].append({
                    "rule": rule,
                    "message": f"{type(error).__name__}: {error}",
                })

    results = []
    for number, path in enumerate(paths, 1):
        errors = errors_by_path[path]
        result = {"input": str(path), "status": "error" if errors else "ok", "errors": errors}
        results.append(result)
        if errors:
            print(f"ERROR {path}: {len(errors)} ACW rule failure(s)", file=sys.stderr)
        progress(number, len(paths))
    return results


def progress(completed: int, total: int, interval: int = 250) -> None:
    if completed % interval == 0 or completed == total:
        print(f"{completed}/{total} próbek przebadanych")


def python_files(input_path: Path) -> list[Path]:
    if input_path.is_file():
        if input_path.suffix != ".py":
            raise ValueError(f"Input file must end in .py: {input_path}")
        return [input_path.resolve()]
    if not input_path.is_dir():
        raise FileNotFoundError(input_path)
    return sorted(path.resolve() for path in input_path.rglob("*.py") if path.is_file())


def output_path(source: Path, input_path: Path, output: Path) -> Path:
    input_path = input_path.resolve()
    output = output.resolve()
    target = output / relative_path(source, input_path)
    if target == source:
        raise ValueError("Output must not overwrite the input file")
    return target


def relative_path(source: Path, input_path: Path) -> Path:
    return Path(source.name) if input_path.is_file() else source.relative_to(input_path.resolve())


def write_report(path: Path | None, rows: list[dict[str, Any]]) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


