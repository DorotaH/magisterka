#!/usr/bin/env python3
"""Reproduce post-Sourcery ACW stages on copies; compile without executing code."""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import contextlib
import csv
import io
import json
from pathlib import Path
import subprocess
import tempfile

import run_mbpp


def check(code):
    try:
        compile(code, '<audit>', 'exec')
        return {'valid': True}
    except (SyntaxError, ValueError) as error:
        return {'valid': False, 'error': str(error)}


def audit(job):
    task_id, root, out = job
    from base_ast import (transform_operations_add, transform_operations_mult,
                          transform_comparison_LG, transform_comparison_LGE)
    from one_rule_format import tab_convert_process
    phases = {}
    phases['original'] = check((root / 'original' / f'{task_id}.py').read_text())
    with tempfile.TemporaryDirectory(prefix='acw-stage-audit-') as tmp:
        path = Path(tmp) / 'solution.py'
        path.write_bytes((root / 'stages/embed/input' / f'{task_id}.py').read_bytes())
        phases['sourcery'] = check(path.read_text())
        for index, transform in enumerate((transform_operations_add, transform_operations_mult,
                                           transform_comparison_LG, transform_comparison_LGE), 36):
            transform(str(path))
            phases[f'reorder_{index}'] = check(path.read_text())
        for index, selection in enumerate((
                'E225,E226,E227,E228,E241,E242,E251,E252,E231',
                'E27', 'E123', 'W292', 'E301,E302,E305,E306'), 40):
            subprocess.run(['autopep8', '--in-place', f'--select={selection}', str(path)],
                           capture_output=True, check=True, timeout=60)
            phases[f'autopep8_{index}'] = check(path.read_text())
        before = path.read_text()
        (out / 'before_tabs' / f'{task_id}.py').write_text(before, encoding='utf-8')
        tab_convert_process(45, str(path))
        after = path.read_text()
        phases['tabs_45'] = check(after)
    first_failure = next((name for name, status in phases.items() if not status['valid']), None)
    return dict(task_id=task_id, phases=phases, first_failure=first_failure,
                matches_saved_acw=after == (root / 'acw' / f'{task_id}.py').read_text(),
                newly_broken_by_tabs=phases['autopep8_44']['valid'] and not phases['tabs_45']['valid'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--workers', type=int, default=8)
    args = parser.parse_args()
    root, out = args.input.resolve(), args.out.resolve()
    ids = json.loads((root / 'metadata.json').read_text())['task_ids']
    out.mkdir(parents=True, exist_ok=False)
    (out / 'before_tabs').mkdir()
    # Upstream prints source diffs. Suppress those once for the entire thread pool.
    with contextlib.redirect_stdout(io.StringIO()), ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(audit, [(task_id, root, out) for task_id in ids]))
    (out / 'results.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows))
    summary = dict(total=len(rows), matches_saved_acw=sum(r['matches_saved_acw'] for r in rows),
        first_failure=dict(Counter(r['first_failure'] or 'none' for r in rows)),
        invalid_by_stage={stage: sum(not r['phases'][stage]['valid'] for r in rows)
                          for stage in rows[0]['phases']},
        newly_broken_by_tabs=sum(r['newly_broken_by_tabs'] for r in rows))
    run_mbpp.write_json(out / 'summary.json', summary)
    with (out / 'stages.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=['task_id', 'stage', 'valid', 'error'])
        writer.writeheader()
        for row in rows:
            for stage, status in row['phases'].items():
                writer.writerow(dict(task_id=row['task_id'], stage=stage, **status))
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
