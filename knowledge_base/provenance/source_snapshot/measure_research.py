#!/usr/bin/env python3
"""Measure every exact artifact with independent tools and resumable checkpoints."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import sys

from research_metrics import measure_artifact
from run_mbpp import write_json


def inventory(root):
    meta = json.loads((root / 'metadata.json').read_text())
    artifacts = []
    for source in meta['sources']:
        for stage in meta['stages']:
            for task_id in meta['task_ids']:
                relative = Path('inputs') / source / stage / f'{task_id}.py'
                path = root / relative
                item = dict(artifact_id=f'{source}:{stage}:{task_id}', task_id=task_id,
                            source=source, stage=stage)
                if path.exists():
                    data = path.read_bytes()
                    item.update(status='available', path=str(path),
                                relative_path=str(relative), sha256=hashlib.sha256(data).hexdigest())
                else:
                    error = path.with_suffix('.error.json')
                    if not error.exists():
                        raise RuntimeError(f'Artifact is not yet prepared: {path}')
                    details = json.loads(error.read_text())
                    item.update(status='preprocessing_error', path=None, relative_path=None,
                                sha256=None, error=details['error'])
                artifacts.append(item)
    return meta, artifacts


def load_checkpoint(path):
    if not path.exists():
        return {}
    raw = path.read_bytes()
    lines = raw.splitlines(keepends=True)
    completed, offset = {}, 0
    for index, line in enumerate(lines):
        try:
            row = json.loads(line)
        except (json.JSONDecodeError, UnicodeDecodeError):
            if index != len(lines)-1:
                raise RuntimeError('Corrupted checkpoint before its final record') from None
            backup = path.with_name(path.name+'.incomplete-tail')
            if backup.exists():
                raise RuntimeError('An incomplete-tail backup already exists') from None
            backup.write_bytes(line)
            path.write_bytes(raw[:offset])
            break
        if row['artifact_id'] in completed:
            raise RuntimeError(f'Duplicate checkpoint key: {row["artifact_id"]}')
        completed[row['artifact_id']] = row
        offset += len(line)
    return completed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if args.workers < 1:
        parser.error('workers must be positive')
    root, out = args.input.resolve(), args.out.resolve()
    detection_meta, artifacts = inventory(root)
    fingerprint = hashlib.sha256(json.dumps(artifacts, sort_keys=True).encode()).hexdigest()
    metadata = dict(input=str(root), input_fingerprint=fingerprint,
        versions={n: version(n) for n in ('ruff', 'complexipy', 'radon')}, python=sys.version,
        implementation_sha256=hashlib.sha256(Path(__file__).with_name('research_metrics.py').read_bytes()).hexdigest(),
        task_ids=detection_meta['task_ids'], sources=detection_meta['sources'], stages=detection_meta['stages'],
        target_version='py310', line_length=88, exact_bytes=True, independent_tools=True,
        compile_check_only=True, correctness_tests_run=False,
        complexipy=dict(check_script=True, no_ignore=True, with_plans=False),
        radon=dict(mi_multi=True, cc_inner_blocks=True, cc_class_aggregates_not_added_to_functions=True),
        ruff=dict(lint_profiles=['default', 'ALL'], stdin_filename='solution.py', isolated=True),
        timing_note='Per-artifact wall time under concurrent load; not a controlled benchmark.')
    if args.resume:
        if json.loads((out / 'metadata.json').read_text()) != metadata:
            parser.error('Cannot resume: inputs, versions or measurement definitions differ')
    else:
        out.mkdir(parents=True, exist_ok=False)
        write_json(out / 'metadata.json', metadata)
        write_json(out / 'artifacts.json', artifacts)
    checkpoint = out / 'measurements.jsonl'
    completed = load_checkpoint(checkpoint)
    expected = {a['artifact_id']: a for a in artifacts}
    for artifact_id, row in completed.items():
        if artifact_id not in expected or row['sha256'] != expected[artifact_id]['sha256']:
            raise RuntimeError(f'Checkpoint input mismatch: {artifact_id}')
    pending = [a for a in artifacts if a['artifact_id'] not in completed]
    with checkpoint.open('a', encoding='utf-8') as stream:
        for artifact in [a for a in pending if a['status'] != 'available']:
            row = dict(artifact_id=artifact['artifact_id'], sha256=None,
                       syntax={'valid': None}, source_metrics={},
                       measurements=[dict(tool=tool, status='preprocessing_error', metrics={},
                            error=artifact['error'], seconds=None) for tool in ('ruff', 'complexipy', 'radon')])
            stream.write(json.dumps(row, ensure_ascii=False)+'\n')
            completed[row['artifact_id']] = row
        stream.flush()
        available = [a for a in pending if a['status'] == 'available']
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = [pool.submit(measure_artifact, (a['artifact_id'], a['path'], a['sha256']))
                       for a in available]
            for future in as_completed(futures):
                row = future.result()
                stream.write(json.dumps(row, ensure_ascii=False)+'\n')
                stream.flush()
                completed[row['artifact_id']] = row
                if len(completed) % 250 == 0 or len(completed) == len(artifacts):
                    print(f'Measured {len(completed)}/{len(artifacts)} artifacts', flush=True)
    assert len(completed) == len(artifacts)
    statuses = Counter((m['tool'], m['status']) for row in completed.values() for m in row['measurements'])
    summary = dict(artifacts=len(artifacts), files=sum(a['status']=='available' for a in artifacts),
        tool_measurements=len(artifacts)*3,
        statuses={f'{tool}/{status}': count for (tool, status), count in sorted(statuses.items())},
        syntax_invalid=sum(row['syntax']['valid'] is False for row in completed.values()))
    write_json(out / 'summary.json', summary)
    print(json.dumps(summary, indent=2), flush=True)
    return int(any(status=='tool_error' for tool, status in statuses))


if __name__ == '__main__':
    raise SystemExit(main())
