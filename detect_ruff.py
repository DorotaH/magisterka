#!/usr/bin/env python3
"""Detect ACW/SEW marks before and after the two recorded Ruff profiles."""
import argparse
from collections import Counter
import csv
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import shutil
import subprocess
import sys

from run_mbpp import syntax_status, write_json
from run_mbpp_batch import batch_pass


STAGES = ('before', 'ruff_default', 'ruff_strict')
ALL_STAGES = STAGES + ('ruff_lint_default', 'ruff_lint_repo_max')
PROFILE_DESCRIPTIONS = {
    'before': 'untouched input',
    'ruff_default': 'format only; isolated, py310, 88',
    'ruff_strict': 'check --select ALL --fix --no-unsafe-fixes, then format; isolated, py310, 88',
    'ruff_lint_default': 'check --fix --no-unsafe-fixes; no formatter; default lint rules',
    'ruff_lint_repo_max': 'check --select PL,UP,B,SIM,I,F,FURB --fix --no-unsafe-fixes; no formatter; current Ruff, repository prefixes',
}


def digest(code):
    return hashlib.sha256(code.encode('utf-8')).hexdigest()


def ruff_exact(command, code, *options):
    # text=True would silently normalize CRLF in the formatter's output.
    result = subprocess.run([sys.executable, '-m', 'ruff', command, '--isolated',
        '--no-cache', '--target-version', 'py310', '--line-length', '88', *options,
        '--stdin-filename', 'solution.py', '-'], input=code.encode('utf-8'),
        capture_output=True, timeout=60, check=False)
    if result.returncode not in ((0, 1) if command == 'check' else (0,)):
        raise RuntimeError(result.stderr.decode('utf-8', 'replace'))
    return result.stdout.decode('utf-8')


def write_csv(path, rows, fields):
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)


def prepare_inputs(root, quality, out, task_ids, sources, stages=STAGES, reuse=None):
    """Run Ruff on exact source bytes; preserve the tool's line endings."""
    prepared = {}
    for source in sources:
        for stage in stages:
            (out / 'inputs' / source / stage).mkdir(parents=True, exist_ok=True)
        for task_id in task_ids:
            task_id = str(task_id)
            original = (root / source / f'{task_id}.py').read_bytes().decode('utf-8')
            cached_source = quality / 'artifacts' / task_id / source / 'source.py' if quality else None
            normalized = original.replace('\r\n', '\n').replace('\r', '\n')
            if cached_source and cached_source.exists() and cached_source.read_text(encoding='utf-8') != normalized:
                raise RuntimeError(f'Quality artifact does not match {source}/{task_id}')
            reusable_source = (reuse is not None
                and (reuse / 'inputs' / source / 'before' / f'{task_id}.py').exists()
                and (reuse / 'inputs' / source / 'before' / f'{task_id}.py').read_bytes() == original.encode())
            for stage in stages:
                entry = {}
                try:
                    if stage == 'before':
                        code = original
                        entry['preprocessing'] = 'none'
                    elif reusable_source and (reuse / 'inputs' / source / stage / f'{task_id}.py').exists():
                        code = (reuse / 'inputs' / source / stage / f'{task_id}.py').read_bytes().decode('utf-8')
                        entry['preprocessing'] = 'hash-verified prior exact run'
                    elif reusable_source and (reuse / 'inputs' / source / stage / f'{task_id}.error.json').exists():
                        raise RuntimeError(json.loads((reuse / 'inputs' / source / stage / f'{task_id}.error.json').read_text())['error'])
                    elif stage.startswith('ruff_lint_'):
                        selection = ('--select', 'PL,UP,B,SIM,I,F,FURB') if stage == 'ruff_lint_repo_max' else ()
                        code = ruff_exact('check', original, *selection, '--fix', '--no-unsafe-fixes')
                        entry['preprocessing'] = 'fresh lint fixes, without formatter'
                    else:
                        # Invalid inputs must have an explicit Ruff failure, not a negative detection.
                        code = original
                        if stage == 'ruff_strict':
                            code = ruff_exact('check', code, '--select', 'ALL', '--fix', '--no-unsafe-fixes')
                        code = ruff_exact('format', code)
                        entry['preprocessing'] = 'fresh Ruff execution on exact bytes'
                    path = out / 'inputs' / source / stage / f'{task_id}.py'
                    path.write_bytes(code.encode('utf-8'))
                    entry.update(status='ready', code=code, input_file=str(path.relative_to(out)),
                                 input_sha256=digest(code), syntax_valid=syntax_status(code)['valid'])
                except Exception as error:
                    entry.update(status='preprocessing_error', error=str(error),
                                 input_sha256=None, input_file=None, syntax_valid=None)
                    write_json(out / 'inputs' / source / stage / f'{task_id}.error.json', entry)
                prepared[(source, stage, task_id)] = entry
        print(f'Prepared {source}: {len(task_ids)} tasks, {len(stages)} stages', flush=True)
    return prepared


def summarize(rows, stages=STAGES):
    summary = {}
    for source, detector in sorted({(r['source'], r['detector']) for r in rows}):
        stage_results = {}
        for stage in stages:
            selected = [r for r in rows if (r['source'], r['detector'], r['stage']) ==
                        (source, detector, stage)]
            available = [r for r in selected if r['status'] == 'ok']
            valid = [r for r in available if r['syntax_valid']]
            stage_results[stage] = dict(total=len(selected), evaluated=len(available),
                unavailable=len(selected)-len(available), detected=sum(r['detected'] for r in available),
                rate=sum(r['detected'] for r in available)/len(available) if available else None,
                syntax_valid_evaluated=len(valid),
                syntax_valid_detected=sum(r['detected'] for r in valid),
                verdicts=dict(Counter(r.get('verdict', r['status']) for r in selected)))
        summary[f'{source}/{detector}'] = stage_results
    return summary


def transitions(rows, stages=STAGES):
    by_key = {(r['source'], r['detector'], r['stage'], r['task_id']): r for r in rows}
    result = []
    for before in rows:
        if before['stage'] != 'before':
            continue
        for stage in stages:
            if stage == 'before':
                continue
            after = by_key[(before['source'], before['detector'], stage, before['task_id'])]
            row = {k: before[k] for k in ('task_id', 'source', 'detector')}
            row.update(stage=stage, before_detected=before.get('detected'),
                       after_detected=after.get('detected'))
            if before['status'] != 'ok' or after['status'] != 'ok':
                row['transition'] = 'unavailable'
            elif before['detected'] and not after['detected']:
                row['transition'] = 'lost'
            elif not before['detected'] and after['detected']:
                row['transition'] = 'gained'
            elif before['detected']:
                row['transition'] = 'retained'
            else:
                row['transition'] = 'not_detected_both'
            result.append(row)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--quality', type=Path, help='Optional legacy quality-artifact cross-check')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--sources', nargs='+', choices=['original', 'acw', 'sew'],
                        default=['original', 'acw', 'sew'])
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--limit', type=int, default=0)
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--reuse-acw', type=Path,
                        help='Reuse ACW detections only when all exact input hashes match')
    parser.add_argument('--reuse-detections', type=Path,
                        help='Reuse an exact-byte run when versions, configuration and hashes match')
    parser.add_argument('--stages', nargs='+', choices=ALL_STAGES, default=list(STAGES))
    args = parser.parse_args()
    if args.workers < 1 or args.limit < 0:
        parser.error('workers must be positive and limit nonnegative')
    root, quality, out = args.input.resolve(), args.quality.resolve() if args.quality else None, args.out.resolve()
    dataset_meta = json.loads((root / 'metadata.json').read_text())
    quality_meta = json.loads((quality / 'metadata.json').read_text()) if quality else None
    if quality_meta and (quality_meta['input'] != str(root)
            or quality_meta['versions']['ruff'] != version('ruff')
            or quality_meta['target_version'] != 'py310' or quality_meta['line_length'] != 88
            or quality_meta['strict_fixes'] != 'safe only'):
        parser.error('Quality artifacts must match input directory and installed Ruff version')
    ids = dataset_meta['task_ids'][:args.limit or None]
    sources = list(dict.fromkeys(args.sources))
    stages = list(dict.fromkeys(args.stages))
    if 'before' not in stages:
        parser.error('--stages must include before for paired comparisons')
    config_text = (root / 'acw.sourcery.yaml').read_text()
    metadata = dict(input=str(root), quality=str(quality) if quality else None, task_ids=ids, sources=sources,
        stages=stages, alpha=dataset_meta['alpha'], sew_key=dataset_meta['sew_key'],
        ruff_version=version('ruff'), sourcery_version=version('sourcery'),
        line_endings='exact input/output bytes; Ruff line-ending=auto',
        reuse_acw_from=str(args.reuse_acw.resolve()) if args.reuse_acw else None,
        reuse_detections_from=str(args.reuse_detections.resolve()) if args.reuse_detections else None,
        acw_config_sha256=digest(config_text),
        profiles={stage: PROFILE_DESCRIPTIONS[stage] for stage in stages},
        detectors={'acw': 'exact equality after reapplication of recorded ACW pipeline',
                   'sew': 'official calibrated detect verdict, including minimum-evidence requirement'},
        unavailable_policy='Ruff failures are unavailable, never negative detections',
        correctness_tests_run=False)
    if args.resume:
        previous_meta = json.loads((out / 'metadata.json').read_text())
        previous_meta.setdefault('reuse_detections_from', None)
        if previous_meta != metadata:
            parser.error('Resume metadata differs')
    else:
        out.mkdir(parents=True, exist_ok=False)
        write_json(out / 'metadata.json', metadata)
    (out / 'groups').mkdir(exist_ok=True)
    config = out / 'acw.sourcery.yaml'
    config.write_text(config_text, encoding='utf-8')
    reuse = args.reuse_detections.resolve() if args.reuse_detections else None
    if reuse:
        previous_meta = json.loads((reuse / 'metadata.json').read_text())
        for name in ('input', 'acw_config_sha256', 'sourcery_version', 'ruff_version',
                     'line_endings', 'sew_key', 'alpha'):
            if previous_meta[name] != metadata[name]:
                parser.error(f'Cannot reuse detections: {name} differs')
        for stage in set(stages) & set(previous_meta['stages']):
            if previous_meta['profiles'][stage] != metadata['profiles'][stage]:
                parser.error(f'Cannot reuse different profile: {stage}')
    prepared = prepare_inputs(root, quality, out, ids, sources, stages, reuse)
    if reuse:
        for source in sources:
            for detector in (('acw', 'sew') if source == 'original' else (source,)):
                for stage in stages:
                    label = f'{source}__{detector}__{stage}'
                    cached_path = reuse / 'groups' / f'{label}.json'
                    if not cached_path.exists():
                        continue
                    cached = {r['task_id']: r for r in json.loads(cached_path.read_text())}
                    selected = [cached[i] for i in ids]
                    if any(r['input_sha256'] != prepared[(source, stage, str(r['task_id']))]['input_sha256']
                           for r in selected):
                        raise RuntimeError(f'Changed reuse inputs: {label}')
                    for row in selected:
                        if row.get('reapplied_file'):
                            src = reuse / row['reapplied_file']
                            if digest(src.read_bytes().decode('utf-8')) != row['reapplied_sha256']:
                                raise RuntimeError(f'Invalid reused output: {src}')
                            dst = out / row['reapplied_file']
                            dst.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(src, dst)
                        row['reused_from'] = str(reuse)
                    write_json(out / 'groups' / f'{label}.json', selected)
    if args.reuse_acw:
        previous = args.reuse_acw.resolve()
        previous_meta = json.loads((previous / 'metadata.json').read_text())
        for name in ('input', 'acw_config_sha256', 'sourcery_version', 'ruff_version'):
            if previous_meta[name] != metadata[name]:
                parser.error(f'Cannot reuse ACW: {name} differs')
        if 'acw' in sources:
            for stage in stages:
                label = f'acw__acw__{stage}'
                cached = json.loads((previous / 'groups' / f'{label}.json').read_text())
                by_id = {r['task_id']: r for r in cached}
                selected = [by_id[i] for i in ids]
                if any(r['input_sha256'] != prepared[('acw', stage, str(r['task_id']))]['input_sha256']
                       for r in selected):
                    print(f'{label}: input hashes differ; recomputing', flush=True)
                    continue
                for row in selected:
                    if row.get('reapplied_file'):
                        src = previous / row['reapplied_file']
                        if digest(src.read_bytes().decode('utf-8')) != row['reapplied_sha256']:
                            raise RuntimeError(f'Invalid reused output hash: {src}')
                        dst = out / row['reapplied_file']
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(src, dst)
                    row['reused_from'] = str(previous)
                write_json(out / 'groups' / f'{label}.json', selected)
                print(f'{label}: reused {len(selected)} hash-verified detections', flush=True)
    from sew import detect
    key = bytes.fromhex(dataset_meta['sew_key'])
    rows = []
    for source in sources:
        detectors = ('acw', 'sew') if source == 'original' else (source,)
        for detector in detectors:
            for stage in stages:
                label = f'{source}__{detector}__{stage}'
                checkpoint = out / 'groups' / f'{label}.json'
                if checkpoint.exists():
                    saved = json.loads(checkpoint.read_text())
                    if any(r['input_sha256'] != prepared[(source, stage, str(r['task_id']))]['input_sha256']
                           for r in saved):
                        raise RuntimeError(f'Changed inputs for checkpoint {label}')
                    rows.extend(saved)
                    print(f'{label}: loaded checkpoint', flush=True)
                    continue
                codes = {str(i): prepared[(source, stage, str(i))]['code'] for i in ids
                         if prepared[(source, stage, str(i))]['status'] == 'ready'}
                reapplied = (batch_pass(label, codes, out, config, args.workers)
                             if detector == 'acw' and codes else {})
                group = []
                for task_id in ids:
                    entry = prepared[(source, stage, str(task_id))]
                    row = dict(task_id=task_id, source=source, detector=detector, stage=stage,
                        status=entry['status'], input_file=entry['input_file'],
                        input_sha256=entry['input_sha256'], syntax_valid=entry['syntax_valid'])
                    try:
                        if entry['status'] != 'ready':
                            row.update(error=entry['error'], detected=None)
                        elif detector == 'acw':
                            result = reapplied[str(task_id)]
                            if result['error']:
                                raise RuntimeError(result['error'])
                            detected = result['code'] == entry['code']
                            path = out / 'acw_reapplied' / source / stage / f'{task_id}.py'
                            path.parent.mkdir(parents=True, exist_ok=True)
                            path.write_text(result['code'], encoding='utf-8')
                            row.update(status='ok', detected=detected,
                                verdict='Watermark detected' if detected else 'No watermark evidence',
                                reapplied_sha256=digest(result['code']),
                                reapplied_file=str(path.relative_to(out)))
                        else:
                            result = detect(entry['code'], 'python', key, alpha=dataset_meta['alpha'])
                            row.update(status='ok', detected=result['verdict'] == 'Watermark detected',
                                       verdict=result['verdict'], p=result['p'],
                                       n_grades=result['n_grades'], detection=result)
                    except Exception as error:
                        row.update(status='detection_error', detected=None, error=str(error))
                    group.append(row)
                write_json(checkpoint, group)
                rows.extend(group)
                print(f'{label}: {sum(r.get("detected") is True for r in group)} detected; '
                      f'{sum(r["status"] != "ok" for r in group)} unavailable', flush=True)
    (out / 'results.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows),
                                      encoding='utf-8')
    write_csv(out / 'results.csv', rows, ['task_id', 'source', 'detector', 'stage', 'status',
        'syntax_valid', 'detected', 'verdict', 'p', 'n_grades', 'input_sha256',
        'input_file', 'reapplied_sha256', 'reapplied_file', 'error'])
    changes = transitions(rows, stages)
    write_csv(out / 'transitions.csv', changes, ['task_id', 'source', 'detector', 'stage',
        'before_detected', 'after_detected', 'transition'])
    summary = summarize(rows, stages)
    write_json(out / 'summary.json', summary)
    transition_summary = {}
    for row in changes:
        label = f'{row["source"]}/{row["detector"]}/{row["stage"]}'
        transition_summary.setdefault(label, Counter())[row['transition']] += 1
    write_json(out / 'transitions_summary.json', transition_summary)
    lines = ['# Detekcja watermarków przed i po Ruffie', '',
        f'Zadania MBPP: {len(ids)}. SEW: alpha={dataset_meta["alpha"]}.', '',
        'Próba podstawowa: formatowanie Ruff. Rygorystyczna: wszystkie reguły, '
        'bezpieczne poprawki i formatowanie. Zachowano dokładne bajty wejścia i wyjścia '
        '(w tym CRLF/LF); Ruff używa line-ending=auto.', '',
        '| Kod / detektor | Etap | Wykryte | Ocenione | Brak wyniku | '
        'Wykryte w poprawnym kodzie | Poprawne składniowo ocenione |',
        '|---|---|---:|---:|---:|---:|---:|']
    for label, stages in summary.items():
        for stage, value in stages.items():
            lines.append(f'| {label} | {stage} | {value["detected"]} | {value["evaluated"]} | '
                         f'{value["unavailable"]} | {value["syntax_valid_detected"]} | '
                         f'{value["syntax_valid_evaluated"]} |')
    lines += ['', '## Zmiany na tych samych zadaniach', '',
        '| Kod / detektor / Ruff | Utrzymane wykrycie | Utracone | Nowe | '
        'Brak wykrycia w obu | Brak porównania |', '|---|---:|---:|---:|---:|---:|']
    for label, counts in transition_summary.items():
        lines.append(f'| {label} | {counts["retained"]} | {counts["lost"]} | '
                     f'{counts["gained"]} | {counts["not_detected_both"]} | {counts["unavailable"]} |')
    lines += ['', 'Brak wyniku po błędzie Ruffa nie oznacza niewykrytego watermarku. '
        'Surowa detekcja ACW obejmuje także błędny składniowo kod; podano osobne liczniki '
        'dla poprawnych plików. Dla SEW zachowano rozróżnienie braku dowodów '
        'i zbyt małej liczby obserwacji w results.jsonl oraz summary.json.', '',
        'Kod po Ruffie: inputs/. Ponowne transformacje ACW: acw_reapplied/. '
        'Każdy rekord zawiera ścieżkę pliku i SHA-256. '
        'Nie wykonywano testów funkcjonalnych.']
    (out / 'report.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'Finished: {len(rows)} detection records; report: {out / "report.md"}', flush=True)
    return int(any(r['status'] == 'detection_error' for r in rows))


if __name__ == '__main__':
    raise SystemExit(main())
