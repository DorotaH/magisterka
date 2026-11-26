#!/usr/bin/env python3
"""Build per-sample ACW and SEW detection tables in a two-sheet workbook."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring

ROOT = Path(__file__).resolve().parents[1]
MODELS = ("llama", "qwen")
VARIANTS = ("original", "watermarked", "ruff_default", "ruff_strict")
HEADERS = (
    "plik", "problem_id", "kod oryginalny", "zwatermarkowany",
    "Ruff normalny", "Ruff strict",
)


def report_rows(path: Path, model: str) -> dict[int, dict]:
    if not path.is_file():
        return {}
    rows = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        match = re.search(rf"(?:^|/){model}_(\d+)\.py$", str(row.get("input", "")))
        if not match:
            raise ValueError(f"{path}:{line_number}: input must end in {model}_N.py")
        sample = int(match.group(1))
        if sample in rows:
            raise ValueError(f"{path}:{line_number}: duplicate sample {model}_{sample}.py")
        rows[sample] = row
    return rows


def result_cell(rows: dict[int, dict], sample: int):
    row = rows.get(sample)
    if row is None:
        return "error: brak raportu"
    if row.get("status", "ok") != "ok":
        return "error"
    verdict = row.get("verdict")
    if verdict == "Watermark detected":
        return "wykryto"
    if verdict == "No watermark evidence":
        return "nie wykryto"
    if verdict == "Insufficient evidence":
        return "za mało danych"
    positive = row.get("positive")
    if positive not in (0, 1, False, True):
        return "error: brak wyniku 0/1"
    return "wykryto" if int(positive) else "nie wykryto"


def col_name(number: int) -> str:
    name = ""
    while number:
        number, rem = divmod(number - 1, 26)
        name = chr(65 + rem) + name
    return name


def add_cell(row: Element, ref: str, value, style: int = 0) -> None:
    attrs = {"r": ref}
    if style:
        attrs["s"] = str(style)
    if isinstance(value, int):
        cell = SubElement(row, "c", attrs)
        SubElement(cell, "v").text = str(value)
    else:
        attrs["t"] = "inlineStr"
        cell = SubElement(row, "c", attrs)
        inline = SubElement(cell, "is")
        SubElement(inline, "t", {"{http://www.w3.org/XML/1998/namespace}space": "preserve"}).text = str(value)


def sheet_xml(sections: list[tuple[str, list[tuple]]]) -> bytes:
    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
    root = Element("worksheet", {"xmlns": ns})
    SubElement(root, "dimension", {"ref": "A1:F3005"})
    views = SubElement(root, "sheetViews")
    view = SubElement(views, "sheetView", {"workbookViewId": "0"})
    SubElement(view, "pane", {"ySplit": "2", "topLeftCell": "A3", "activePane": "bottomLeft", "state": "frozen"})
    cols = SubElement(root, "cols")
    for index, width in enumerate((18, 14, 23, 23, 20, 20), 1):
        SubElement(cols, "col", {"min": str(index), "max": str(index), "width": str(width), "customWidth": "1"})
    data = SubElement(root, "sheetData")
    row_num = 1
    for title, records in sections:
        row = SubElement(data, "row", {"r": str(row_num), "ht": "24", "customHeight": "1"})
        add_cell(row, f"A{row_num}", title, 1)
        row_num += 1
        row = SubElement(data, "row", {"r": str(row_num), "ht": "36", "customHeight": "1"})
        for col, header in enumerate(HEADERS, 1):
            add_cell(row, f"{col_name(col)}{row_num}", header, 2)
        row_num += 1
        for record in records:
            row = SubElement(data, "row", {"r": str(row_num)})
            for col, value in enumerate(record, 1):
                add_cell(row, f"{col_name(col)}{row_num}", value)
            row_num += 1
        if title == "SEW":
            row_num += 1
    merges = SubElement(root, "mergeCells", {"count": "2"})
    SubElement(merges, "mergeCell", {"ref": "A1:F1"})
    SubElement(merges, "mergeCell", {"ref": "A1504:F1504"})
    return tostring(root, encoding="utf-8", xml_declaration=True)


def write_xlsx(path: Path, worksheets: dict[str, list[tuple[str, list[tuple]]]]) -> None:
    types = Element("Types", {"xmlns": "http://schemas.openxmlformats.org/package/2006/content-types"})
    SubElement(types, "Default", {"Extension": "rels", "ContentType": "application/vnd.openxmlformats-package.relationships+xml"})
    SubElement(types, "Default", {"Extension": "xml", "ContentType": "application/xml"})
    SubElement(types, "Override", {"PartName": "/xl/workbook.xml", "ContentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"})
    SubElement(types, "Override", {"PartName": "/xl/styles.xml", "ContentType": "application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"})
    package_rels = Element("Relationships", {"xmlns": "http://schemas.openxmlformats.org/package/2006/relationships"})
    SubElement(package_rels, "Relationship", {"Id": "rId1", "Type": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument", "Target": "xl/workbook.xml"})
    workbook = Element("workbook", {"xmlns": "http://schemas.openxmlformats.org/spreadsheetml/2006/main", "xmlns:r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"})
    book_sheets = SubElement(workbook, "sheets")
    rels = Element("Relationships", {"xmlns": "http://schemas.openxmlformats.org/package/2006/relationships"})
    for index, name in enumerate(worksheets, 1):
        SubElement(book_sheets, "sheet", {"name": name, "sheetId": str(index), "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id": f"rId{index}"})
        SubElement(rels, "Relationship", {"Id": f"rId{index}", "Type": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet", "Target": f"worksheets/sheet{index}.xml"})
    SubElement(rels, "Relationship", {"Id": f"rId{len(worksheets)+1}", "Type": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles", "Target": "styles.xml"})
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="3"><font><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="13"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Calibri"/></font></fonts>
<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill></fills>
<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="3"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0"/><xf numFmtId="0" fontId="2" fillId="2" borderId="0" xfId="0"/></cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>'''
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", tostring(types, encoding="utf-8", xml_declaration=True))
        archive.writestr("_rels/.rels", tostring(package_rels, encoding="utf-8", xml_declaration=True))
        archive.writestr("xl/workbook.xml", tostring(workbook, encoding="utf-8", xml_declaration=True))
        archive.writestr("xl/_rels/workbook.xml.rels", tostring(rels, encoding="utf-8", xml_declaration=True))
        archive.writestr("xl/styles.xml", styles)
        for index, sections in enumerate(worksheets.values(), 1):
            archive.writestr(f"xl/worksheets/sheet{index}.xml", sheet_xml(sections))


def main() -> None:
    worksheets = {}
    for model in MODELS:
        generation_path = ROOT / "source_data" / f"apps500_{model}" / "generations.jsonl"
        generations = [json.loads(line) for line in generation_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        problem_ids = [row.get("problem_id") for row in generations]
        if any(problem_id is None for problem_id in problem_ids):
            raise ValueError(f"{generation_path}: missing problem_id")
        source_paths = {
            "sew": {
                "original": ROOT / "results/detections/raw" / f"{model}_generated_sew.jsonl",
                "watermarked": ROOT / "results/detections/raw" / f"{model}_sew.jsonl",
                "ruff_default": ROOT / "results/detections/after_ruff" / f"{model}_sew_default.jsonl",
                "ruff_strict": ROOT / "results/detections/after_ruff" / f"{model}_sew_strict.jsonl",
            },
            "acw": {
                "original": ROOT / "results/detections/raw" / f"{model}_generated_acw.jsonl",
                "watermarked": ROOT / "results/detections/raw" / f"{model}_acw.jsonl",
                "ruff_default": ROOT / "results/detections/after_ruff" / f"{model}_acw_default.jsonl",
                "ruff_strict": ROOT / "results/detections/after_ruff" / f"{model}_acw_strict.jsonl",
            },
        }
        sections = []
        for method in ("sew", "acw"):
            reports = {variant: report_rows(path, model) for variant, path in source_paths[method].items()}
            records = []
            for sample, problem_id in enumerate(problem_ids, 1):
                records.append((
                    f"{model}_{sample}", problem_id,
                    *(result_cell(reports[variant], sample) for variant in VARIANTS),
                ))
            sections.append((method.upper(), records))
        worksheets[model] = sections
    output = ROOT / "results/watermark_detection.xlsx"
    write_xlsx(output, worksheets)
    print(f"Created {output}")


if __name__ == "__main__":
    main()
