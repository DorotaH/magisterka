#!/usr/bin/env python3
"""Build one Excel workbook from the saved APPS watermark detector results.

The workbook contains two binary matrices (default/strict Ruff profiles), the
full long-form detector records, and the watermark marking status records.
Unrun or failed detections are blank in binary cells and explicitly labelled
by status in the detailed sheets; they are never converted to zero.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/apps500_quality/source_data"
OUTPUT = ROOT / "results/apps500_quality/APPS_watermark_detection.xlsx"
KEY = ("dataset", "problem_id", "sample_index")
METHODS = ("acw_notab", "acw_full", "sew")
RUFF_ACTIONS = ("fix", "format", "fix_format")

MATRIX_FIELDS = [
    "dataset", "problem_id", "sample_index",
    "oryginał · ACW bez reguły 45", "oryginał · ACW z regułą 45", "oryginał · SEW",
    "kod oznakowany · ACW bez reguły 45", "kod oznakowany · ACW z regułą 45",
    "kod oznakowany · SEW",
    *[f"{method_label} · Ruff {action}" for method_label in
      ("ACW bez reguły 45", "ACW z regułą 45", "SEW") for action in RUFF_ACTIONS],
]

LONG_FIELDS = [
    "record_source", "dataset", "problem_id", "sample_index", "variant", "detector",
    "ruff_profile", "ruff_mode", "status", "verdict", "detection_0_1", "reason",
    "p", "n_sites", "n_grades", "error_type", "error", "applied", "parses",
    "changed", "marking_passed", "code_sha256",
]

MARK_FIELDS = [
    "dataset", "problem_id", "sample_index", "arm", "variant", "sloc", "applied",
    "parses", "changed", "detection_status", "detection_verdict", "detection_0_1",
    "marking_passed", "error_type", "error", "output_path", "tool_seconds",
    "sourcery_batch_id",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def cell_value(row: dict[str, str] | None) -> str:
    if not row or row.get("status", "ok") not in ("ok", "success"):
        return ""
    value = row.get("positive", row.get("detection_positive", ""))
    if value in ("True", "true", "1", 1, True):
        return "1"
    if value in ("False", "false", "0", 0, False):
        return "0"
    return ""


def key_of(row: dict[str, str]) -> tuple[str, str, str]:
    return tuple(row.get(field, "") for field in KEY)  # type: ignore[return-value]


def xml_text(value: object) -> str:
    text = str(value) if value is not None else ""
    # Excel cells cannot contain XML control characters; retain printable text.
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    # Excel's maximum cell text length is 32,767 characters.
    if len(text) > 32767:
        text = text[:32720] + " … [cell text truncated]"
    return escape(text)


def col_name(number: int) -> str:
    result = ""
    while number:
        number, rem = divmod(number - 1, 26)
        result = chr(65 + rem) + result
    return result


def worksheet_xml(rows: list[list[object]], widths: list[int] | None = None) -> str:
    max_cols = max((len(row) for row in rows), default=1)
    max_rows = max(len(rows), 1)
    dimension = f"A1:{col_name(max_cols)}{max_rows}"
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">',
        f'<dimension ref="{dimension}"/>',
        '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" '
        'activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>',
    ]
    if widths:
        parts.append('<cols>')
        for index, width in enumerate(widths, 1):
            parts.append(f'<col min="{index}" max="{index}" width="{width}" customWidth="1"/>')
        parts.append('</cols>')
    parts.append('<sheetData>')
    for row_index, row in enumerate(rows, 1):
        parts.append(f'<row r="{row_index}">')
        for col_index, value in enumerate(row, 1):
            ref = f"{col_name(col_index)}{row_index}"
            style = ' s="1"' if row_index == 1 else ""
            if value is None or value == "":
                parts.append(f'<c r="{ref}"{style}/>')
            elif isinstance(value, int) or (isinstance(value, str) and value in ("0", "1")):
                parts.append(f'<c r="{ref}"{style}><v>{value}</v></c>')
            else:
                parts.append(f'<c r="{ref}" t="inlineStr"{style}><is><t xml:space="preserve">'
                             f'{xml_text(value)}</t></is></c>')
        parts.append('</row>')
    parts.append('</sheetData>')
    parts.append(f'<autoFilter ref="A1:{col_name(max_cols)}{max_rows}"/>')
    parts.append('</worksheet>')
    return "".join(parts)


def as_long_record(source: str, row: dict[str, str], **overrides: str) -> dict[str, str]:
    result = {field: "" for field in LONG_FIELDS}
    result.update(row)
    result["record_source"] = source
    if not result.get("status"):
        result["status"] = row.get("detection_status", "")
    if not result.get("verdict"):
        result["verdict"] = row.get("detection_verdict", "")
    if "detection_0_1" not in result or not result["detection_0_1"]:
        result["detection_0_1"] = row.get("positive", row.get("detection_positive", ""))
    result.update(overrides)
    return {field: str(result.get(field, "")) for field in LONG_FIELDS}


def make_workbook(data: Path, output: Path) -> None:
    marking = read_csv(data / "01_marking.csv")
    sew_detail = read_csv(data / "01_sew_detection.csv")
    after_ruff = read_csv(data / "02_detection_after_ruff.csv")
    original = read_csv(data / "original_detection.csv")
    if not marking or not after_ruff:
        raise SystemExit(f"Missing required saved result CSVs in {data}")

    keys = sorted({key_of(row) for row in marking},
                  key=lambda item: (item[0], int(item[1]), int(item[2])))
    marking_map = {(key_of(row), row["variant"]): row for row in marking}
    sew_map = {key_of(row): row for row in sew_detail}
    original_map = {(key_of(row), row["variant"]): row for row in original}
    ruff_map = {
        (key_of(row), row["variant"], row["ruff_profile"], row["ruff_mode"]): row
        for row in after_ruff
    }

    profile_sheets: dict[str, list[list[object]]] = {}
    for profile, sheet_title in (("default", "Macierz bazowa"), ("strict", "Macierz rygor")):
        matrix: list[list[object]] = [MATRIX_FIELDS]
        for key in keys:
            record: dict[str, object] = dict(zip(KEY, key, strict=True))
            for variant, title in zip(METHODS, MATRIX_FIELDS[3:6], strict=True):
                record[title] = cell_value(original_map.get((key, variant)))
            for variant, title in zip(METHODS, MATRIX_FIELDS[6:9], strict=True):
                if variant == "sew":
                    record[title] = cell_value(sew_map.get(key))
                else:
                    record[title] = cell_value(marking_map.get((key, variant)))
            col = 9
            for variant in METHODS:
                for action in RUFF_ACTIONS:
                    row = ruff_map.get((key, variant, profile, action))
                    record[MATRIX_FIELDS[col]] = cell_value(row)
                    col += 1
            matrix.append([record.get(field, "") for field in MATRIX_FIELDS])
        profile_sheets[sheet_title] = matrix

    long_rows: list[list[object]] = [LONG_FIELDS]
    for row in marking:
        item = as_long_record("marked", row,
                              detector="SEW" if row["variant"] == "sew" else "ACW_fixed_point")
        if row["variant"] == "sew" and key_of(row) in sew_map:
            details = sew_map[key_of(row)]
            for field in ("verdict", "positive", "reason", "p", "n_sites", "n_grades", "error"):
                if details.get(field, "") != "":
                    item[field] = details[field]
            item["detection_0_1"] = details.get("positive", "")
            item["status"] = details.get("status", item["status"])
        long_rows.append([item[field] for field in LONG_FIELDS])

    for row in original:
        item = as_long_record("original_control", row,
                              detection_0_1=row.get("positive", ""))
        long_rows.append([item[field] for field in LONG_FIELDS])
    if not original:
        for key in keys:
            for variant, detector in (("acw_notab", "ACW_fixed_point"),
                                      ("acw_full", "ACW_fixed_point"), ("sew", "SEW")):
                item = as_long_record("original_control", {
                    "dataset": key[0], "problem_id": key[1], "sample_index": key[2],
                    "variant": variant, "detector": detector, "status": "not_run",
                    "verdict": "", "positive": "", "reason": "",
                }, detection_0_1="")
                long_rows.append([item[field] for field in LONG_FIELDS])

    for row in after_ruff:
        item = as_long_record("after_ruff", row,
                              detection_0_1=row.get("positive", ""))
        long_rows.append([item[field] for field in LONG_FIELDS])

    marking_rows: list[list[object]] = [MARK_FIELDS]
    for row in marking:
        mark_record = dict(row)
        mark_record["detection_0_1"] = row.get("detection_positive", "")
        marking_rows.append([mark_record.get(field, "") for field in MARK_FIELDS])

    sew_rows: list[list[object]] = [[
        "dataset", "problem_id", "sample_index", "method", "arm", "status", "verdict",
        "detection_0_1", "reason", "p", "n_sites", "n_grades", "error",
    ]]
    for row in sew_detail:
        sew_rows.append([row.get(field, "") for field in (
            "dataset", "problem_id", "sample_index", "method", "arm", "status", "verdict",
            "positive", "reason", "p", "n_sites", "n_grades", "error",
        )])

    sheets = [
        ("Macierz bazowa", profile_sheets["Macierz bazowa"]),
        ("Macierz rygor", profile_sheets["Macierz rygor"]),
        ("Detekcja", long_rows),
        ("Znakowanie", marking_rows),
        ("SEW szczegóły", sew_rows),
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    content_types = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                     '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
                     '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
                     '<Default Extension="xml" ContentType="application/xml"/>',
                     '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>',
                     '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    for i in range(1, len(sheets) + 1):
        content_types.append(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    content_types.append('</Types>')
    workbook = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>']
    rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    root_rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
                 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
                 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>',
                 '</Relationships>']
    for index, (name, _rows) in enumerate(sheets, 1):
        workbook.append(f'<sheet name="{escape(name)}" sheetId="{index}" r:id="rId{index}"/>')
        rels.append(f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{index}.xml"/>')
    workbook.extend(['</sheets><calcPr calcId="191029"/></workbook>'])
    rels.append(f'<Relationship Id="rId{len(sheets)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>')
    rels.append('</Relationships>')
    styles = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
              '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
              '<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font>'
              '<font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font></fonts>'
              '<fills count="3"><fill><patternFill patternType="none"/></fill>'
              '<fill><patternFill patternType="gray125"/></fill>'
              '<fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill></fills>'
              '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
              '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
              '<cellXfs count="2"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
              '<xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/></cellXfs>'
              '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>')
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as book:
        book.writestr("[Content_Types].xml", "".join(content_types))
        book.writestr("_rels/.rels", "".join(root_rels))
        book.writestr("xl/workbook.xml", "".join(workbook))
        book.writestr("xl/_rels/workbook.xml.rels", "".join(rels))
        book.writestr("xl/styles.xml", styles)
        for index, (_name, rows) in enumerate(sheets, 1):
            width = [20] * max((len(row) for row in rows), default=1)
            for c in range(min(3, len(width))):
                width[c] = 18 if c == 0 else 16
            if index in (1, 2):
                width = [18, 14, 12] + [21] * (len(width) - 3)
            if index == 3:
                width = [20, 16, 14, 14, 18, 22, 15, 15, 15, 24, 12, 24, 14, 12, 12, 20, 48, 12, 12, 12, 15, 66]
            book.writestr(f"xl/worksheets/sheet{index}.xml", worksheet_xml(rows, width))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DATA)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    make_workbook(args.data_dir, args.output)
    print(f"Saved workbook: {args.output}")
    if not (args.data_dir / "original_detection.csv").is_file():
        print("Original-code control detections are not run yet; those matrix cells are blank.")
        print("Run experiments/run_apps500_original_detection.py, then regenerate this workbook.")


if __name__ == "__main__":
    main()
