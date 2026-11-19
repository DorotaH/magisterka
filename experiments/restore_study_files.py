"""Restore the split study files from the published archive parts."""

import argparse
import gzip
from hashlib import file_digest
import json
from pathlib import Path
import shutil
import tempfile


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def restore(root, entry):
    target = root / entry["path"]
    if target.exists():
        if digest(target) != entry["sha256"]:
            raise ValueError(f"Existing file differs from the archive: {target}")
        return

    with tempfile.TemporaryDirectory(dir=target.parent) as directory:
        temporary = Path(directory)
        archive = temporary / "data.gz"
        with archive.open("wb") as stream:
            for part in entry["parts"]:
                with (root / part).open("rb") as source:
                    shutil.copyfileobj(source, stream)
        restored = temporary / "restored"
        with gzip.open(archive, "rb") as source, restored.open("wb") as stream:
            shutil.copyfileobj(source, stream)
        if digest(restored) != entry["sha256"]:
            raise ValueError(f"Checksum mismatch: {target}")
        restored.replace(target)


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path,
                        default=root / "results/main_study/split_files/manifest.json")
    args = parser.parse_args()
    for entry in json.loads(args.manifest.read_text(encoding="utf-8")):
        restore(root, entry)
        print(entry["path"])


if __name__ == "__main__":
    main()
