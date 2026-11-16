#!/usr/bin/env python3
"""Read-only access to tasks, exact code and research results."""

import argparse
import csv
import json
from pathlib import Path
import sqlite3
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db",
        type=Path,
        default=Path(__file__).with_name("knowledge.sqlite"),
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("overview")
    task = commands.add_parser("task")
    task.add_argument("task_id", type=int)
    task.add_argument("--stage", default="before")
    code = commands.add_parser("code")
    code.add_argument("task_id", type=int)
    code.add_argument(
        "--variant", choices=["original", "acw", "sew"], default="original"
    )
    code.add_argument("--stage", default="before")
    code.add_argument("--save", type=Path, help="Write exact bytes to a new file")
    audit = commands.add_parser("audit-code")
    audit.add_argument("task_id", type=int)
    audit.add_argument(
        "--stage", choices=["sourcery", "before_tabs"], default="before_tabs"
    )
    audit.add_argument("--save", type=Path)
    sql = commands.add_parser("sql")
    sql.add_argument("query", help="Read-only SQL query; output is CSV")
    args = parser.parse_args()
    path = args.db.resolve()
    db = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA query_only=ON")
    allowed = {
        sqlite3.SQLITE_SELECT,
        sqlite3.SQLITE_READ,
        sqlite3.SQLITE_FUNCTION,
        sqlite3.SQLITE_RECURSIVE,
    }
    db.set_authorizer(
        lambda action, *unused: (
            sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY
        )
    )
    if args.command == "overview":
        for table in (
            "tasks",
            "artifacts",
            "measurements",
            "metric_values",
            "function_results",
            "detections",
        ):
            print(
                f"{table}: {db.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]}"
            )
        print("\nPomiar / status / liczba:")
        for row in db.execute(
            "SELECT tool,status,COUNT(*) n FROM measurements GROUP BY tool,status"
        ):
            print(dict(row))
    elif args.command == "task":
        item = db.execute(
            "SELECT * FROM tasks WHERE task_id=?", (args.task_id,)
        ).fetchone()
        if item is None:
            parser.error("No such task")
        print(f"MBPP {args.task_id}: {item['prompt']}")
        print(
            f"Testy: {len(json.loads(item['tests_json']))}; nie uruchamiano ich w tym badaniu."
        )
        print("\nWersje kodu i status narzędzi:")
        for row in db.execute(
            """SELECT a.variant,a.stage,a.syntax_valid,m.tool,m.status,m.error
            FROM artifacts a JOIN measurements m USING(artifact_id) WHERE task_id=? AND stage=?
            ORDER BY variant,tool""",
            (args.task_id, args.stage),
        ):
            print(json.dumps(dict(row), ensure_ascii=False))
        print("\nDetekcja we wszystkich etapach:")
        for row in db.execute(
            """SELECT a.variant,a.stage,d.detector,d.status,d.detected,d.verdict,d.p,d.n_grades
            FROM artifacts a JOIN detections d USING(artifact_id) WHERE task_id=? ORDER BY variant,detector,stage""",
            (args.task_id,),
        ):
            print(json.dumps(dict(row), ensure_ascii=False))
        print("\nMetryki dla wybranego etapu:")
        for row in db.execute(
            "SELECT * FROM v_quality WHERE task_id=? AND stage=? AND status='ok' ORDER BY variant,tool,metric",
            (args.task_id, args.stage),
        ):
            print(json.dumps(dict(row), ensure_ascii=False))
    elif args.command in ("code", "audit-code"):
        if args.command == "code":
            row = db.execute(
                "SELECT code,syntax_error FROM v_artifact_code WHERE task_id=? AND variant=? AND stage=?",
                (args.task_id, args.variant, args.stage),
            ).fetchone()
        else:
            row = db.execute(
                "SELECT content,NULL FROM audit_artifacts JOIN code_blobs USING(sha256) WHERE task_id=? AND stage=?",
                (args.task_id, args.stage),
            ).fetchone()
        if row is None or row[0] is None:
            parser.error(
                f"No code available: {row[1] if row else 'unknown task/stage'}"
            )
        data = bytes(row[0])
        if args.save:
            with args.save.open("xb") as handle:
                handle.write(data)
            print(f"Saved exact bytes: {args.save}")
        else:
            sys.stdout.buffer.write(data)
    else:
        result = db.execute(args.query)
        writer = csv.writer(sys.stdout)
        writer.writerow([c[0] for c in result.description])
        writer.writerows(result)


if __name__ == "__main__":
    main()
