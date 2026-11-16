#!/usr/bin/env python3
"""Run full MBPP using directory-level Sourcery passes and unchanged ACW rules."""
import argparse
from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

from run_mbpp import evaluate_task, normalize_sew_verdicts, prepare_acw, syntax_status, write_json


def finish_file(job):
    path, config = job
    try:
        transform = prepare_acw(Path(config), write_config=False, run_sourcery=False)
        return Path(path).stem, transform(Path(path).read_text(encoding='utf-8')), None
    except Exception as error:
        return Path(path).stem, None, str(error)


def batch_pass(label, codes, out, config, workers):
    stage = out / 'stages' / label
    stage.mkdir(parents=True, exist_ok=True)
    checkpoint = stage / 'completed.json'
    if checkpoint.exists():
        print(f'{label}: loading completed checkpoint', flush=True)
        return json.loads(checkpoint.read_text(encoding='utf-8'))
    inputs = stage / 'input'
    inputs.mkdir(exist_ok=True)
    for task_id, code in codes.items():
        (inputs / f'{task_id}.py').write_text(code, encoding='utf-8')
    print(f'{label}: Sourcery review of {len(codes)} files', flush=True)
    with (stage / 'sourcery.stdout').open('w') as stdout, \
         (stage / 'sourcery.stderr').open('w') as stderr:
        result = subprocess.run(['sourcery', 'review', '--config', str(config),
                                 '--fix', str(inputs)], stdout=stdout, stderr=stderr,
                                timeout=3600, check=False)
    if result.returncode:
        raise RuntimeError(f'{label}: Sourcery exited {result.returncode}; see {stage}')
    outputs = {}
    jobs = [(str(inputs / f'{task_id}.py'), str(config)) for task_id in codes]
    print(f'{label}: applying reordering and formatting rules', flush=True)
    with ProcessPoolExecutor(max_workers=workers) as pool:
        for index, (task_id, code, error) in enumerate(pool.map(finish_file, jobs), 1):
            outputs[task_id] = {'code': code, 'error': error}
            if index % 50 == 0 or index == len(codes):
                print(f'{label}: {index}/{len(codes)}', flush=True)
    write_json(checkpoint, outputs)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True,
                        help='Existing run containing dataset.jsonl and metadata.json')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--quality-out', type=Path)
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    if args.workers < 1:
        parser.error('--workers must be positive')
    source, out = args.input.resolve(), args.out.resolve()
    metadata = json.loads((source / 'metadata.json').read_text())
    tasks = list(map(json.loads, (source / 'dataset.jsonl').read_text().splitlines()))
    assert [t['task_id'] for t in tasks] == metadata['task_ids']
    metadata.update(methods=['acw', 'sew'], execution='two directory-level Sourcery passes',
                    batch_equivalence_check='20 tasks: identical code and detection to individual passes')
    if args.resume:
        if json.loads((out / 'metadata.json').read_text()) != metadata:
            parser.error('Cannot resume a different experiment')
    else:
        out.mkdir(parents=True, exist_ok=False)
        write_json(out / 'metadata.json', metadata)
        shutil.copy2(source / 'dataset.jsonl', out / 'dataset.jsonl')
    for name in ('original', 'acw', 'sew'):
        (out / name).mkdir(exist_ok=True)
    originals = {str(t['task_id']): t['code'] for t in tasks}
    for task_id, code in originals.items():
        (out / 'original' / f'{task_id}.py').write_text(code, encoding='utf-8')
    config = out / 'acw.sourcery.yaml'
    prepare_acw(config)
    key = bytes.fromhex(metadata['sew_key'])
    alpha = metadata['alpha']
    rows = []
    sew_checkpoint = out / 'sew-results.json'
    if sew_checkpoint.exists():
        rows.extend(normalize_sew_verdicts(row) for row in json.loads(sew_checkpoint.read_text()))
    else:
        for index, task in enumerate(tasks, 1):
            row, marked = evaluate_task((task, 'sew', str(config), key, alpha))
            if marked is not None:
                (out / 'sew' / f"{task['task_id']}.py").write_text(marked, encoding='utf-8')
            rows.append(row)
            if index % 100 == 0 or index == len(tasks):
                print(f'SEW: {index}/{len(tasks)}', flush=True)
        write_json(sew_checkpoint, rows)
    start = time.perf_counter()
    marked_results = batch_pass('embed', originals, out, config, args.workers)
    marked_codes = {task_id: r['code'] for task_id, r in marked_results.items()
                    if r['code'] is not None}
    for task_id, code in marked_codes.items():
        (out / 'acw' / f'{task_id}.py').write_text(code, encoding='utf-8')
    reapplied = batch_pass('detect', marked_codes, out, config, args.workers)
    elapsed = time.perf_counter() - start
    for task in tasks:
        task_id = str(task['task_id'])
        marked = marked_results[task_id]
        detected = reapplied.get(task_id, {})
        error = marked['error'] or detected.get('error')
        row = dict(task_id=task['task_id'], method='acw', seconds=None)
        if error:
            row.update(status='error', error=error)
        else:
            row.update(status='ok', changed=marked['code'] != task['code'],
                       syntax=syntax_status(marked['code']),
                       original_detected=marked['code'] == task['code'],
                       watermarked_detected=detected['code'] == marked['code'])
        rows.append(row)
    rows.sort(key=lambda r: (r['task_id'], r['method']))
    (out / 'results.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n'
                                            for r in rows), encoding='utf-8')
    by_id = {t['task_id']: t for t in tasks}
    with (out / 'code_pairs.jsonl').open('w', encoding='utf-8') as pairs:
        for row in rows:
            task = by_id[row['task_id']]
            path = out / row['method'] / f"{row['task_id']}.py"
            if path.exists():
                code = path.read_text(encoding='utf-8')
                pairs.write(json.dumps(dict(task_id=row['task_id'], method=row['method'],
                    prompt=task.get('text'), code_before=task['code'], code_after=code,
                    tests=task.get('test_list', []), code_before_syntax=syntax_status(task['code']),
                    code_after_syntax=syntax_status(code), watermark_result=row),
                    ensure_ascii=False) + '\n')
    summary = {}
    for method in ('acw', 'sew'):
        selected = [r for r in rows if r['method'] == method]
        valid = [r for r in selected if r['status'] != 'error']
        summary[method] = dict(total=len(selected), errors=len(selected)-len(valid),
            evaluated=len(valid), changed=sum(r['changed'] for r in valid),
            abstained=sum(r['status'].startswith('abstain') for r in valid),
            syntax_invalid=sum(not r['syntax']['valid'] for r in valid),
            detected_original=sum(r['original_detected'] for r in valid),
            detected_watermarked=sum(r['watermarked_detected'] for r in valid))
    write_json(out / 'summary.json', summary)
    write_json(out / 'timing.json', {'acw_batch_wall_seconds': elapsed,
                                   'per_sample_acw_seconds': None,
                                   'note': 'Batch timing includes both passes; resume timing covers current invocation.'})
    print(json.dumps(summary, indent=2), flush=True)
    if args.quality_out:
        result = subprocess.run([sys.executable, str(Path(__file__).with_name('analyze_quality.py')),
            '--input', str(out), '--out', str(args.quality_out.resolve())], check=False)
        write_json(out / 'quality-status.json', {'exit_code': result.returncode,
                   'note': '1 means some samples could not be analyzed; see quality pairs.jsonl.'})
    return int(any(r['status'] == 'error' for r in rows))


if __name__ == '__main__':
    raise SystemExit(main())
