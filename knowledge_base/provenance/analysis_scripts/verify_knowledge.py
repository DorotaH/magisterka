#!/usr/bin/env python3
"""Verify the complete database, exact bytes, aggregates and optional tool outputs."""

import argparse
import ast
from collections import defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import sqlite3
import sys

from research_metrics import syntax
from run_mbpp import write_json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def same_number(left, right):
    return math.isclose(left, right, rel_tol=1e-12, abs_tol=1e-12)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument(
        "--external",
        action="store_true",
        help="Compare every record with original experiment logs",
    )
    parser.add_argument(
        "--recompute-sew",
        action="store_true",
        help="Recompute every SEW verdict using archived detector sources",
    )
    args = parser.parse_args()
    root = args.base.resolve()
    db_path = root / "knowledge.sqlite"
    db = sqlite3.connect(db_path.as_uri() + "?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    require(
        db.execute("PRAGMA integrity_check").fetchone()[0] == "ok",
        "SQLite integrity failure",
    )
    require(
        not db.execute("PRAGMA foreign_key_check").fetchall(), "Broken foreign keys"
    )
    metadata = {
        r["key"]: json.loads(r["value_json"])
        for r in db.execute("SELECT * FROM metadata")
    }
    dmeta = metadata["detections"]
    ids = set(dmeta["task_ids"])
    task_ids = {r[0] for r in db.execute("SELECT task_id FROM tasks")}
    require(task_ids == ids, "Task selection differs")
    n = len(ids)
    expected_artifacts = n * len(dmeta["sources"]) * len(dmeta["stages"])
    artifacts = {r["artifact_id"]: r for r in db.execute("SELECT * FROM artifacts")}
    require(len(artifacts) == expected_artifacts, "Artifact count differs")
    blobs = {
        r["sha256"]: bytes(r["content"]) for r in db.execute("SELECT * FROM code_blobs")
    }
    for sha, data in blobs.items():
        require(hashlib.sha256(data).hexdigest() == sha, f"Corrupted blob: {sha}")
    syntax_cache = {}
    function_count_cache = {}
    for key, artifact in artifacts.items():
        require(
            artifact["task_id"] in ids
            and artifact["variant"] in dmeta["sources"]
            and artifact["stage"] in dmeta["stages"],
            f"Invalid artifact key: {key}",
        )
        if artifact["status"] == "available":
            data = blobs[artifact["sha256"]]
            if artifact["sha256"] not in syntax_cache:
                syntax_cache[artifact["sha256"]] = syntax(data)["valid"]
            require(
                bool(artifact["syntax_valid"]) == syntax_cache[artifact["sha256"]],
                f"Syntax flag differs: {key}",
            )
            if args.external:
                require(
                    Path(artifact["origin"]).read_bytes() == data,
                    f"External artifact differs: {key}",
                )
        else:
            require(
                artifact["sha256"] is None and artifact["syntax_valid"] is None,
                f"Missing artifact has data: {key}",
            )
    for task in db.execute("SELECT task_id,raw_json FROM tasks"):
        original = json.loads(task["raw_json"])["code"].encode("utf-8")
        sha = artifacts[f"original:before:{task['task_id']}"]["sha256"]
        require(
            blobs[sha] == original, f"Original dataset bytes differ: {task['task_id']}"
        )
    measurements = {
        (r["artifact_id"], r["tool"]): r
        for r in db.execute("SELECT * FROM measurements")
    }
    require(len(measurements) == expected_artifacts * 3, "Measurement count differs")
    values = defaultdict(dict)
    for row in db.execute("SELECT * FROM metric_values"):
        require(math.isfinite(row["value"]), "Non-finite metric")
        values[(row["artifact_id"], row["tool"])][row["metric"]] = row["value"]
    functions = defaultdict(list)
    for row in db.execute("SELECT * FROM function_results ORDER BY ordinal"):
        functions[(row["artifact_id"], row["tool"], row["kind"])].append(row)
    expected_metrics = {"ruff": 4, "complexipy": 6, "radon": 26}
    for key, row in measurements.items():
        artifact_id, tool = key
        require(tool in expected_metrics, f"Unexpected tool: {tool}")
        artifact = artifacts[artifact_id]
        require(
            row["status"] != "tool_error",
            f"Unresolved tool error: {key}: {row['error']}",
        )
        details = json.loads(row["details_json"])
        if artifact["status"] != "available":
            require(
                row["status"] == "preprocessing_error" and not values[key],
                f"Invalid unavailable measurement: {key}",
            )
            continue
        if row["status"] == "ok":
            require(artifact["syntax_valid"] == 1, f"Success on invalid syntax: {key}")
            require(
                len(values[key]) == expected_metrics[tool],
                f"Metric schema mismatch: {key}",
            )
        if tool == "ruff":
            for profile in ("default", "all"):
                diagnostics = details[profile]["diagnostics"]
                require(
                    values[key][f"{profile}.violations"] == len(diagnostics),
                    f"Ruff count differs: {key}",
                )
                safe = sum(
                    d.get("fix") is not None and d["fix"].get("applicability") == "safe"
                    for d in diagnostics
                )
                require(
                    values[key][f"{profile}.safe_fixable"] == safe,
                    f"Ruff fix count differs: {key}",
                )
        elif row["status"] == "ok":
            records = functions[(artifact_id, tool, "functions")]
            if tool == "complexipy":
                nonmodule = [r for r in records if r["name"] != "<module>"]
                scores = [r["complexity"] for r in nonmodule]
                module = sum(
                    r["complexity"] for r in records if r["name"] == "<module>"
                )
                require(
                    same_number(values[key]["functions_total"], sum(scores)),
                    f"Cognitive sum differs: {key}",
                )
                require(
                    same_number(values[key]["module"], module),
                    f"Cognitive module differs: {key}",
                )
                require(
                    same_number(values[key]["total"], module + sum(scores)),
                    f"Cognitive total differs: {key}",
                )
                require(
                    values[key]["function_count"] == len(scores),
                    f"Cognitive count differs: {key}",
                )
            else:
                scores = [r["complexity"] for r in records]
                require(
                    same_number(values[key]["cc.function_total"], sum(scores)),
                    f"Radon sum differs: {key}",
                )
                require(
                    values[key]["cc.function_count"] == len(scores),
                    f"Radon count differs: {key}",
                )
                sha = artifact["sha256"]
                if sha not in function_count_cache:
                    function_count_cache[sha] = sum(
                        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                        for node in ast.walk(ast.parse(blobs[sha]))
                    )
                require(
                    len(records) == function_count_cache[sha],
                    f"Radon missed a declared function: {key}",
                )
                unique = {
                    (
                        r["line_start"],
                        json.loads(r["details_json"])["column"],
                        r["line_end"],
                    )
                    for r in records
                }
                require(
                    len(unique) == len(records), f"Double-counted Radon function: {key}"
                )
                for name, value in details["raw"].items():
                    require(
                        values[key][f"raw.{name}"] == value,
                        f"Raw metric differs: {key}",
                    )
                for name, value in details["halstead_total"].items():
                    require(
                        values[key][f"halstead.{name}"] == value,
                        f"Halstead metric differs: {key}",
                    )
    detector_groups = len(dmeta["sources"]) + (
        1 if "original" in dmeta["sources"] else 0
    )
    detections = list(db.execute("SELECT * FROM detections"))
    require(
        len(detections) == n * len(dmeta["stages"]) * detector_groups,
        "Detection count differs",
    )
    recomputed = 0
    if args.recompute_sew:
        sys.path.insert(0, str(root / "provenance/source_snapshot/SEW"))
        from sew import detect

        key = bytes.fromhex(dmeta["sew_key"])
    for row in detections:
        artifact = artifacts[row["artifact_id"]]
        raw = json.loads(row["raw_json"])
        require(
            raw["input_sha256"] == artifact["sha256"],
            f"Detection input hash differs: {row['artifact_id']}",
        )
        require(
            raw["syntax_valid"] == artifact["syntax_valid"],
            f"Detection syntax flag differs: {row['artifact_id']}",
        )
        if row["status"] != "ok":
            require(
                row["detected"] is None and artifact["sha256"] is None,
                "Unavailable detection is a negative result",
            )
            continue
        require(row["detected"] in (0, 1), "Missing detection decision")
        if row["detector"] == "acw":
            sha = row["reapplied_sha256"]
            require(sha in blobs, "Missing ACW reapplication bytes")
            require(
                bool(row["detected"]) == (sha == artifact["sha256"]),
                f"ACW equality differs: {row['artifact_id']}",
            )
        else:
            result = raw["detection"]
            require(
                bool(row["detected"]) == (result["verdict"] == "Watermark detected"),
                "SEW verdict ignored",
            )
            require(
                row["p"] == result["p"] and row["n_grades"] == result["n_grades"],
                "SEW details differ",
            )
            if row["detected"]:
                require(
                    row["n_grades"] >= 5 and row["p"] < dmeta["alpha"],
                    "SEW minimum evidence/alpha violated",
                )
            if args.recompute_sew:
                actual = detect(
                    blobs[artifact["sha256"]],
                    "python",
                    key,
                    alpha=dmeta["alpha"],
                    q_path=root / "provenance/sew_q_table.json",
                )
                require(
                    actual == result, f"Recomputed SEW differs: {row['artifact_id']}"
                )
                recomputed += 1
                if recomputed % 1000 == 0:
                    print(f"Recomputed {recomputed} SEW detections", flush=True)
    expected_transitions = n * (len(dmeta["stages"]) - 1) * detector_groups
    require(
        db.execute("SELECT COUNT(*) FROM v_detection_transitions").fetchone()[0]
        == expected_transitions,
        "Transition count differs",
    )
    require(
        db.execute("""SELECT COUNT(*) FROM v_detection_transitions
            WHERE transition='unavailable' AND after_detected IS NOT NULL AND before_status='ok' """).fetchone()[
            0
        ]
        == 0,
        "Unavailable transition has an after decision",
    )
    external_records = 0
    if args.external:
        hashes = json.loads((root / "provenance/input_hashes.json").read_text())
        for path, sha in hashes.items():
            require(
                hashlib.sha256(Path(path).read_bytes()).hexdigest() == sha,
                f"Changed experiment log: {path}",
            )
        quality_path = next(
            Path(p) for p in hashes if p.endswith("/measurements.jsonl")
        )
        for line in quality_path.read_text().splitlines():
            row = json.loads(line)
            for result in row["measurements"]:
                k = (row["artifact_id"], result["tool"])
                saved = measurements[k]
                require(
                    saved["status"] == result["status"]
                    and saved["error"] == result.get("error"),
                    f"External status differs: {k}",
                )
                require(
                    values[k] == result["metrics"],
                    f"External metric values differ: {k}",
                )
                require(
                    json.loads(saved["details_json"]) == result.get("details", {}),
                    f"External raw details differ: {k}",
                )
                external_records += 1
    exports = {
        "quality_values.csv": "v_quality",
        "watermark_quality_pairs.csv": "v_watermark_pairs",
        "ruff_quality_pairs.csv": "v_ruff_quality_pairs",
        "tool_statuses.csv": "measurements",
        "detections.csv": "detections",
        "detection_transitions.csv": "v_detection_transitions",
        "functions.csv": "function_results",
        "syntax_failures.csv": None,
        "transformations.csv": "transformations",
    }
    export_counts = {}
    for filename, table in exports.items():
        with (root / "exports" / filename).open(newline="", encoding="utf-8") as handle:
            count = sum(1 for _ in csv.DictReader(handle))
        expected = db.execute(
            f"SELECT COUNT(*) FROM {table}"
            if table
            else "SELECT COUNT(*) FROM artifacts WHERE syntax_valid=0"
        ).fetchone()[0]
        require(count == expected, f"CSV row count differs: {filename}")
        export_counts[filename] = count
    summary = json.loads((root / "quality_summary.json").read_text())
    for result in summary:
        view = (
            "v_common_watermark_pairs"
            if result["cohort"] == "common"
            else "v_watermark_pairs"
        )
        actual = db.execute(
            f"""SELECT COUNT(*),AVG(before),AVG(after),AVG(delta),SUM(delta>0),SUM(delta<0),SUM(delta=0)
            FROM {view} WHERE method=? AND stage=? AND tool=? AND metric=?""",
            (result["method"], result["stage"], result["tool"], result["metric"]),
        ).fetchone()
        require(actual[0] == result["n"], "Summary denominator differs")
        for index, name in [(1, "mean_before"), (2, "mean_after"), (3, "mean_delta")]:
            require(
                same_number(actual[index], result[name]),
                f"Summary mean differs: {name}",
            )
        require(
            tuple(actual[4:])
            == (result["increased"], result["decreased"], result["unchanged"]),
            "Summary change counts differ",
        )
    evidence = dict(
        status="passed",
        tasks=n,
        artifacts=len(artifacts),
        code_blobs=len(blobs),
        measurements=len(measurements),
        metric_values=sum(map(len, values.values())),
        detections=len(detections),
        independent_sew_recomputations=recomputed,
        external_measurements_compared=external_records,
        csv_rows=export_counts,
        quality_summaries_verified=len(summary),
        checks=[
            "SQLite integrity and foreign keys",
            "all artifact and blob hashes",
            "exact original dataset bytes",
            "syntax flags by fresh compile",
            "all measurement statuses and aggregate sums",
            "ACW equality for every stored reapplication",
            "SEW official verdict, alpha and minimum evidence",
            "paired denominators and means",
            "CSV completeness",
        ],
    )
    write_json(root / "validation.json", evidence)
    build = json.loads((root / "build.json").read_text())
    require(build["reports_complete"], "Reports are incomplete")
    require(
        build["database_sha256"] == hashlib.sha256(db_path.read_bytes()).hexdigest(),
        "Database changed after build",
    )
    build["validation_complete"] = True
    write_json(root / "build.json", build)
    print(json.dumps(evidence, indent=2), flush=True)


if __name__ == "__main__":
    main()
