"""Shared Ruff formatter CLI implementation."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from operation_utils import add_io_arguments, copy_file, output_path, python_files, write_report  # noqa: E402


def run(profile: str) -> int:
    parser = argparse.ArgumentParser(description=f"Run Ruff using the {profile} configuration.")
    add_io_arguments(parser)
    parser.add_argument("--action", choices=("check", "fix", "format", "fix-format"), default="format")
    parser.add_argument("--ruff", type=Path, default=ROOT / "ACW/.tools/local/bin/ruff")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--report", type=Path, help="Optional JSONL status/diagnostics report")
    args = parser.parse_args()
    executable = str(args.ruff) if args.ruff.is_file() else shutil.which("ruff")
    if not executable:
        parser.error("Ruff was not found; install it or pass --ruff /path/to/ruff")
    config = Path(__file__).resolve().parent / "config" / f"ruff.{profile}.toml"
    rows: list[dict[str, Any]] = []
    files = python_files(args.input)
    for index, source in enumerate(files):
        target = output_path(source, args.input, args.output)
        copy_file(source, target)
        commands = []
        command_results = []
        lint_json: list[dict[str, Any]] = []
        operation_errors = []
        try:
            if args.action in ("fix", "fix-format"):
                command = [executable, "check", "--config", str(config), "--fix", str(target)]
                commands.append(command)
                fixed = subprocess.run(command, capture_output=True, text=True,
                                       timeout=args.timeout, check=False)
                command_results.append({"command": command, "returncode": fixed.returncode,
                                        "stdout": fixed.stdout, "stderr": fixed.stderr})
            if args.action in ("format", "fix-format"):
                command = [executable, "format", "--config", str(config), str(target)]
                commands.append(command)
                formatted = subprocess.run(command, capture_output=True, text=True,
                                           timeout=args.timeout, check=False)
                command_results.append({"command": command, "returncode": formatted.returncode,
                                        "stdout": formatted.stdout, "stderr": formatted.stderr})
                if formatted.returncode != 0:
                    operation_errors.append({"command": "format", "returncode": formatted.returncode,
                                             "stderr": formatted.stderr, "stdout": formatted.stdout})
            command = [executable, "check", "--config", str(config), "--output-format", "json", str(target)]
            commands.append(command)
            checked = subprocess.run(command, capture_output=True, text=True,
                                     timeout=args.timeout, check=False)
            command_results.append({"command": command, "returncode": checked.returncode,
                                    "stdout": checked.stdout, "stderr": checked.stderr})
            try:
                lint_json = json.loads(checked.stdout or "[]")
            except json.JSONDecodeError:
                lint_json = []
            row = {"input": str(source), "output": str(target), "profile": profile,
                   "action": args.action,
                   "status": "ok" if checked.returncode in (0, 1) and not operation_errors else "error",
                   "diagnostic_count": len(lint_json),
                   "diagnostic_codes": [entry.get("code") for entry in lint_json],
                   "diagnostics": lint_json, "commands": commands,
                   "command_results": command_results, "operation_errors": operation_errors,
                   "stderr": checked.stderr, "changed": source.read_bytes() != target.read_bytes()}
        except (OSError, subprocess.TimeoutExpired) as error:
            row = {"input": str(source), "output": str(target), "profile": profile,
                   "action": args.action, "status": "error",
                   "error": f"{type(error).__name__}: {error}", "commands": commands}
        rows.append(row)
        print(f"[{index + 1}/{len(files)}] {source} -> {target}: {row['status']}")
    write_report(args.report, rows)
    return 1 if any(row["status"] != "ok" for row in rows) else 0
