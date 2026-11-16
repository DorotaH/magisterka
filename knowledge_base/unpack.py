#!/usr/bin/env python3
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
