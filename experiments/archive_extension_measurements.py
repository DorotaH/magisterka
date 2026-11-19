"""Archive tidy measurements from each complete extension v3 layer."""

import argparse
import csv
import gzip
import json
from hashlib import sha256
from io import TextIOWrapper
from pathlib import Path

from export_measurements import FIELDS, rows
from select_extension_classeval import EXTENSION, ROOT
from select_samples import write_json

PART_SIZE = 16 * 1024 * 1024


def archive(layer, run):
    directory = EXTENSION / layer
    destination = directory / "measurements_long.csv.gz"
    selection = json.loads((directory / "selection.json").read_bytes())
    digest = sha256()
    with (
        destination.open("wb") as compressed,
        gzip.GzipFile(filename="", mode="wb", fileobj=compressed, mtime=0) as archive_file,
        TextIOWrapper(archive_file, encoding="utf-8", newline="") as stream,
    ):
        writer = csv.writer(stream)
        writer.writerow(FIELDS)
        for sample in selection["samples"]:
            result = run / layer / sample["dataset"] / sample["sample_id"] / "result.json"
            if layer == "warstwa_C" and sample["tests_available"]:
                correctness = result.parent / "correctness_v2" / "result.json"
                if not correctness.is_file():
                    raise FileNotFoundError(correctness)
            writer.writerows(rows(result))
    chunks = []
    with destination.open("rb") as source:
        for index, content in enumerate(iter(lambda: source.read(PART_SIZE), b"")):
            part = directory / f"measurements_long.csv.gz.part{index:03}"
            part.write_bytes(content)
            chunks.append(str(part.relative_to(ROOT)))
    with gzip.open(destination, "rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    destination.unlink()
    return {"path": str((directory / "measurements_long.csv").relative_to(ROOT)),
            "sha256": digest.hexdigest(), "parts": chunks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("measurements", type=Path)
    args = parser.parse_args()
    entries = [archive(layer, args.measurements) for layer in ("warstwa_A", "warstwa_C")]
    write_json(EXTENSION / "split_files/measurements.json", entries)


if __name__ == "__main__":
    main()
