#!/usr/bin/env python3
"""Watermark reference MBPP solutions; never execute dataset code."""
import argparse
import ast
from concurrent.futures import ProcessPoolExecutor
import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'ACW/source'))
sys.path.insert(0, str(ROOT / 'SEW'))


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def prepare_acw(config, write_config=True, run_sourcery=True):
    for command in ('sourcery', 'autopep8'):
        if not shutil.which(command):
            raise RuntimeError(f'Missing {command}; install requirements-mbpp.txt first.')
    from one_rule_format import tab_convert_process
    from base_ast import (transform_operations_add, transform_operations_mult,
                          transform_comparison_LG, transform_comparison_LGE)
    from refact_list import refactoring_list
    if write_config:
        config.write_text("version: '1'\nrule_settings:\n  enable:\n" +
                          ''.join(f'    - {r}\n' for r in refactoring_list), encoding='utf-8')

    def transform(code):
        with tempfile.TemporaryDirectory(prefix='acw-mbpp-') as tmp:
            path = Path(tmp) / 'solution.py'
            path.write_text(code, encoding='utf-8')
            if run_sourcery:
                result = subprocess.run(
                    ['sourcery', 'review', '--config', str(config), '--fix', str(path)],
                    capture_output=True, text=True, timeout=180)
                if result.returncode != 0:
                    raise RuntimeError(f'Sourcery failed ({result.returncode}):\n{result.stdout}\n{result.stderr}')
            with contextlib.redirect_stdout(io.StringIO()) as captured:
                # Upstream reorder_process still calls the old four-argument API.
                # Current base_ast functions transform an entire file via LibCST.
                for transform_file in (transform_operations_add, transform_operations_mult,
                                       transform_comparison_LG, transform_comparison_LGE):
                    transform_file(str(path))
                for selection in ('E225,E226,E227,E228,E241,E242,E251,E252,E231',
                                  'E27', 'E123', 'W292', 'E301,E302,E305,E306'):
                    subprocess.run(['autopep8', '--in-place', f'--select={selection}', str(path)],
                                   check=True, capture_output=True, text=True, timeout=60)
                tab_convert_process(45, str(path))
            if any(line.startswith('Error processing file ')
                   for line in captured.getvalue().splitlines()):
                raise RuntimeError(captured.getvalue())
            return path.read_text(encoding='utf-8')
    return transform


def syntax_status(code):
    try:
        ast.parse(code)
        return {'valid': True}
    except SyntaxError as error:
        return {'valid': False, 'error': str(error)}


def normalize_sew_verdicts(row):
    """Use the detector's verdict, which also enforces minimum evidence."""
    if row.get('method') == 'sew' and row.get('status') != 'error':
        for field, details in (('original_detected', 'original_detection'),
                               ('watermarked_detected', 'watermarked_detection')):
            detected = row[details]['verdict'] == 'Watermark detected'
            if row.get(field) != detected:
                row.setdefault('legacy_p_only', {})[field] = row.get(field)
            row[field] = detected
    return row


def evaluate_task(job):
    task, method, config, key, alpha = job
    code, task_id = task['code'], task['task_id']
    start = time.perf_counter()
    row = dict(task_id=task_id, method=method)
    marked = None
    try:
        if method == 'acw':
            transform = prepare_acw(Path(config), write_config=False)
            marked = transform(code)
            # Preserve the first output even if reapplication/detection fails.
            try:
                reapplied = transform(marked)
                row.update(status='ok', original_detected=(marked == code),
                           watermarked_detected=(reapplied == marked))
            except Exception as error:
                row.update(status='error', error=f'Detection failed: {error}')
        else:
            from sew import embed, detect
            result = embed(code, 'python', key)
            marked = result['code']
            original = detect(code, 'python', key, alpha=alpha)
            detection = detect(marked, 'python', key, alpha=alpha)
            row.update(status=result['status'], original_detection=original,
                       watermarked_detection=detection,
                       original_detected=original['verdict'] == 'Watermark detected',
                       watermarked_detected=detection['verdict'] == 'Watermark detected')
        if marked is not None:
            row.update(changed=marked != code, syntax=syntax_status(marked))
    except Exception as error:
        row.update(status='error', error=str(error))
    row['seconds'] = time.perf_counter() - start
    return row, marked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--method', choices=['both', 'acw', 'sew'], default='both')
    parser.add_argument('--limit', type=int, default=20, help='Number of tasks; 0 means all')
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--out', type=Path, default=ROOT / 'results/mbpp')
    parser.add_argument('--revision', default='refs/convert/parquet',
                        help='HF Parquet revision; use a commit for reproducibility')
    parser.add_argument('--key', default='76' * 16, help='SEW key in hex; default is public experiment key')
    parser.add_argument('--alpha', type=float, default=0.01)
    parser.add_argument('--workers', type=int, default=1, help='Independent worker processes')
    parser.add_argument('--resume', action='store_true', help='Continue matching existing output')
    parser.add_argument('--prepare-only', action='store_true',
                        help='Save the selected dataset and originals for the batch runner')
    args = parser.parse_args()
    if args.limit < 0 or args.offset < 0 or args.workers < 1 or not 0 < args.alpha < 1:
        parser.error('limit/offset must be nonnegative and 0 < alpha < 1')
    key = bytes.fromhex(args.key)
    if not key:
        parser.error('key must not be empty')
    out = args.out.resolve()
    methods = ['acw', 'sew'] if args.method == 'both' else [args.method]
    if 'acw' in methods:
        for command in ('sourcery', 'autopep8'):
            if not shutil.which(command):
                parser.error(f'Missing {command}. Activate your venv and run: '
                             'python3 -m pip install -r requirements-mbpp.txt')
        __import__('one_rule_format')  # Check imports before reserving output.
    if 'sew' in methods:
        __import__('sew')
    from datasets import load_dataset
    from huggingface_hub import hf_hub_download
    # Read only the full/test table; modern datasets cannot execute mbpp.py.
    parquet = hf_hub_download('Muennighoff/mbpp', 'full/test/0000.parquet',
                              repo_type='dataset', revision=args.revision)
    dataset = load_dataset('parquet', data_files={'test': parquet}, split='test')
    stop = min(len(dataset), args.offset + args.limit) if args.limit else len(dataset)
    tasks = list(dataset.select(range(args.offset, stop)))
    if not tasks:
        raise RuntimeError('No tasks selected')
    # Reserve output only after dependencies and dataset have been checked.
    metadata = dict(dataset='Muennighoff/mbpp', subset='full', split='test',
        revision=args.revision, resolved_revision=Path(parquet).parents[2].name,
        fingerprint=dataset._fingerprint, task_ids=[t['task_id'] for t in tasks],
        methods=methods, alpha=args.alpha, sew_key=args.key if 'sew' in methods else None,
        input='reference code', correctness_tests_run=False,
        acw_configuration='RQ1 pipeline; missing upstream config reconstructed from refact_list',
        acw_reorder_adapter='base_ast file-level LibCST API')
    if args.resume:
        previous = json.loads((out / 'metadata.json').read_text(encoding='utf-8'))
        if previous != metadata:
            parser.error('Cannot resume: experiment metadata differs')
    else:
        out.mkdir(parents=True, exist_ok=False)
        write_json(out / 'metadata.json', metadata)
    if 'acw' in methods:
        prepare_acw(out / 'acw.sourcery.yaml')
    for name in ['original', *methods]:
        (out / name).mkdir(exist_ok=args.resume)
    rows = []
    if args.resume:
        rows = [normalize_sew_verdicts(json.loads(line))
                for line in (out / 'results.jsonl').read_text().splitlines()]
        for row in rows:
            if row['status'] != 'error' and not (out / row['method'] / f"{row['task_id']}.py").exists():
                parser.error('Cannot resume: a completed output file is missing')
    completed = {(r['task_id'], r['method']) for r in rows}
    with (out / 'dataset.jsonl').open('w', encoding='utf-8') as snapshot:
        for task in tasks:
            snapshot.write(json.dumps(task, ensure_ascii=False) + '\n')
            code, task_id = task['code'], task['task_id']
            (out / 'original' / f'{task_id}.py').write_text(code, encoding='utf-8')
    if args.prepare_only:
        print(f'Prepared {len(tasks)} tasks in {out}', flush=True)
        return
    jobs = [(task, method, str(out / 'acw.sourcery.yaml'), key, args.alpha)
            for task in tasks for method in methods if (task['task_id'], method) not in completed]
    with ProcessPoolExecutor(max_workers=args.workers) as executor, \
         (out / 'results.jsonl').open('a' if args.resume else 'w', encoding='utf-8') as results:
        for index, (row, marked) in enumerate(executor.map(evaluate_task, jobs), len(rows) + 1):
            if marked is not None:
                (out / row['method'] / f"{row['task_id']}.py").write_text(marked, encoding='utf-8')
            rows.append(row)
            results.write(json.dumps(row, ensure_ascii=False) + '\n')
            results.flush()
            print(f"[{index}/{len(tasks) * len(methods)}] {row['method']} "
                  f"task={row['task_id']}: {row['status']}", flush=True)
    summary = {}
    for method in methods:
        selected = [r for r in rows if r['method'] == method]
        valid = [r for r in selected if r['status'] != 'error']
        summary[method] = dict(total=len(selected), errors=len(selected)-len(valid),
            evaluated=len(valid), changed=sum(r['changed'] for r in valid),
            abstained=sum(r['status'].startswith('abstain') for r in valid),
            detected_original=sum(r['original_detected'] for r in valid),
            detected_watermarked=sum(r['watermarked_detected'] for r in valid),
            seconds=sum(r['seconds'] for r in selected))
    with (out / 'code_pairs.jsonl').open('w', encoding='utf-8') as pairs:
        by_id = {t['task_id']: t for t in tasks}
        for row in rows:
            task = by_id[row['task_id']]
            marked_file = out / row['method'] / f"{row['task_id']}.py"
            if not marked_file.exists():
                continue
            pairs.write(json.dumps(dict(task_id=row['task_id'], method=row['method'],
                prompt=task.get('text'), code_before=task['code'],
                code_after=marked_file.read_text(encoding='utf-8'), tests=task.get('test_list', []),
                code_before_syntax=syntax_status(task['code']),
                code_after_syntax=syntax_status(marked_file.read_text(encoding='utf-8')),
                watermark_result=row), ensure_ascii=False) + '\n')
    write_json(out / 'summary.json', summary)
    print(json.dumps(summary, indent=2))
    if any(r['status'] == 'error' for r in rows):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
