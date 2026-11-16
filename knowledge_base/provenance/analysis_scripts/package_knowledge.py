#!/usr/bin/env python3
"""Freeze framework scripts and create a verified, portable database archive."""

import argparse
import gzip
import hashlib
from importlib.metadata import distributions
import json
from pathlib import Path
import shutil

from run_mbpp import write_json


UNPACK = '''#!/usr/bin/env python3
"""Restore the exact verified SQLite database from its portable archive."""
import gzip
import hashlib
import json
from pathlib import Path
import tempfile

base=Path(__file__).resolve().parent
expected=json.loads((base/'build.json').read_text())['database_sha256']
target=base/'knowledge.sqlite'
if target.exists():
    if hashlib.sha256(target.read_bytes()).hexdigest()!=expected:
        raise SystemExit('Existing knowledge.sqlite has a different hash; it was not overwritten.')
    print('Verified database already exists.')
else:
    with tempfile.NamedTemporaryFile(dir=base,prefix='unpack-',suffix='.sqlite',delete=False) as output:
        temporary=Path(output.name)
        sha=hashlib.sha256()
        with gzip.open(base/'knowledge.sqlite.gz','rb') as source:
            for block in iter(lambda:source.read(1024*1024),b''):
                output.write(block)
                sha.update(block)
    if sha.hexdigest()!=expected:
        temporary.unlink()
        raise SystemExit('Archive checksum mismatch; database was not installed.')
    temporary.rename(target)
    print('Restored and verified knowledge.sqlite.')
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True)
    parser.add_argument("--dependency-path", type=Path, required=True)
    args = parser.parse_args()
    root = args.base.resolve()
    build = json.loads((root / "build.json").read_text())
    if not build["validation_complete"] or not build["reports_complete"]:
        parser.error("Validation and reports must be complete")
    source_hashes = json.loads((root / "provenance/source_hashes.json").read_text())
    framework_hashes = {}
    paths = sorted(Path(".").glob("*.py")) + sorted(Path("tests").glob("*.py"))
    paths += sorted(Path(".").glob("requirements*.txt"))
    for path in paths:
        target = root / "provenance/analysis_scripts" / path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        framework_hashes[str(path)] = sha
        if str(path) not in source_hashes:
            archived = root / "provenance/source_snapshot" / path
            archived.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, archived)
            source_hashes[str(path)] = sha
    write_json(root / "provenance/source_hashes.json", source_hashes)
    write_json(root / "provenance/framework_hashes.json", framework_hashes)
    lock = sorted(
        {
            f"{d.metadata['Name']}=={d.version}"
            for d in distributions(path=[str(args.dependency_path)])
        }
    )
    (root / "provenance/requirements-lock.txt").write_text("\n".join(lock) + "\n")
    (root / "unpack.py").write_text(UNPACK, encoding="utf-8")
    query = Path("query_research.py").read_text()
    # The distributed helper lives beside the database instead of in the project root.
    old = 'Path(__file__).with_name("knowledge_base") / "knowledge.sqlite"'
    if old not in query:
        raise RuntimeError("Query helper default-path expression changed")
    query = query.replace(old, 'Path(__file__).with_name("knowledge.sqlite")')
    (root / "query.py").write_text(query, encoding="utf-8")
    (root / ".gitignore").write_text(
        "knowledge.sqlite\n*.sqlite-journal\n__pycache__/\n"
    )
    database = root / "knowledge.sqlite"
    if hashlib.sha256(database.read_bytes()).hexdigest() != build["database_sha256"]:
        raise RuntimeError("Database checksum changed")
    with (
        database.open("rb") as source,
        (root / "knowledge.sqlite.gz").open("wb") as target,
    ):
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=target, compresslevel=6, mtime=0
        ) as compressed:
            shutil.copyfileobj(source, compressed)
    sha = hashlib.sha256()
    with gzip.open(root / "knowledge.sqlite.gz", "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            sha.update(block)
    if sha.hexdigest() != build["database_sha256"]:
        raise RuntimeError("Compressed database verification failed")
    required = [
        "README.md",
        "METHODS.md",
        "SCHEMA.md",
        "RESULTS.md",
        "DETECTION.md",
        "EXAMPLES.md",
        "REPRODUCE.md",
        "validation.json",
        "query.py",
        "unpack.py",
        "knowledge.sqlite.gz",
    ]
    if not all((root / name).exists() for name in required):
        raise RuntimeError("Required knowledge-base artifact is missing")
    manifest = {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file()
        and p.name not in ("manifest.json", "knowledge.sqlite")
        and "__pycache__" not in p.parts
    }
    write_json(
        root / "manifest.json",
        dict(
            files=manifest,
            database_sha256=build["database_sha256"],
            compressed_database_verified=True,
            expected_tasks=build["counts"]["tasks"],
        ),
    )
    print(
        f"Packaged {len(manifest)} files; compressed database: "
        f"{(root / 'knowledge.sqlite.gz').stat().st_size / 1024 / 1024:.2f} MiB",
        flush=True,
    )


if __name__ == "__main__":
    main()
