#!/usr/bin/env python3
"""Run Ruff with the strict project configuration."""

from ruff_cli import run

if __name__ == "__main__":
    raise SystemExit(run("strict"))
