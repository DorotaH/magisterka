#!/usr/bin/env python3
"""Measure paired original/ACW/SEW files without executing their code."""
import argparse
import ast
from collections import Counter
import csv
import difflib
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import statistics
import subprocess
import sys


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def ruff(command, code, *options):
    result = subprocess.run(
        [sys.executable, '-m', 'ruff', command, '--isolated', '--no-cache',
         '--target-version', 'py310', '--line-length', '88', *options,
         '--stdin-filename', 'solution.py', '-'],
        input=code, text=True, capture_output=True, timeout=60)
    allowed = (0, 1) if command == 'check' else (0,)
    if result.returncode not in allowed:
        raise RuntimeError(result.stderr or result.stdout)
    return result


def edit_counts(before, after):
    removed = added = 0
    matcher = difflib.SequenceMatcher(None, before.splitlines(), after.splitlines(), autojunk=False)
    for tag, i, j, k, end in matcher.get_opcodes():
        if tag != 'equal':
            removed += j - i
            added += end - k
    return {'changed': int(before != after), 'lines_removed': removed, 'lines_added': added}


def analyze(code, artifact):
    from complexipy import code_complexity
    from radon.complexity import cc_visit
    from radon.metrics import h_visit, mi_visit
    from radon.raw import analyze as raw_analyze

    artifact.mkdir(parents=True, exist_ok=True)
    (artifact / 'source.py').write_text(code, encoding='utf-8')
    # Parsing is a syntax check, not a functional correctness test.
    ast.parse(code)
    metrics = {}
    details = {}
    for profile in ('default', 'strict'):
        selection = ['--select', 'ALL'] if profile == 'strict' else []
        lint = ruff('check', code, *selection, '--output-format', 'json')
        diagnostics = json.loads(lint.stdout)
        formatted_input = code
        if profile == 'strict':
            fixed = ruff('check', code, *selection, '--fix', '--no-unsafe-fixes')
            formatted_input = fixed.stdout
            details['strict_fix_stderr'] = fixed.stderr
        formatted = ruff('format', formatted_input).stdout
        (artifact / f'ruff_{profile}.py').write_text(formatted, encoding='utf-8')
        (artifact / f'ruff_{profile}.diff').write_text(''.join(difflib.unified_diff(
            code.splitlines(keepends=True), formatted.splitlines(keepends=True),
            fromfile='source.py', tofile=f'ruff_{profile}.py')), encoding='utf-8')
        details[f'ruff_{profile}'] = {'diagnostics': diagnostics, 'stderr': lint.stderr,
            'counts_by_rule': dict(Counter(d['code'] for d in diagnostics)),
            'remaining': json.loads(ruff('check', formatted, *selection,
                                        '--output-format', 'json').stdout)}
        prefix = f'ruff.{profile}'
        metrics[f'{prefix}.violations'] = len(diagnostics)
        metrics[f'{prefix}.remaining'] = len(details[f'ruff_{profile}']['remaining'])
        metrics.update({f'{prefix}.{k}': v for k, v in edit_counts(code, formatted).items()})

    cognitive = code_complexity(code, no_ignore=True, with_plans=False)
    functions = [dict(name=f.name, complexity=f.complexity,
                      line_start=f.line_start, line_end=f.line_end) for f in cognitive.functions]
    details['complexipy'] = {'complexity': cognitive.complexity, 'functions': functions}
    scores = [f['complexity'] for f in functions]
    metrics.update({'cognitive.total': cognitive.complexity, 'cognitive.functions': len(scores),
                    'cognitive.max': max(scores, default=0),
                    'cognitive.mean': statistics.mean(scores) if scores else 0})
    blocks = cc_visit(code)

    def block_dict(block):
        item = dict(name=block.name, lineno=block.lineno, complexity=block.complexity)
        item['children'] = [block_dict(b) for b in
                            [*getattr(block, 'methods', []), *getattr(block, 'closures', [])]]
        return item

    details['radon_cc'] = [block_dict(b) for b in blocks]
    # Class scores aggregate methods: do not double-count classes in function summaries.
    seen = set()

    def function_scores(block):
        if hasattr(block, 'methods'):
            return [s for b in block.methods for s in function_scores(b)]
        identity = (block.lineno, block.col_offset, block.name)
        if identity in seen:
            return []
        seen.add(identity)
        return [block.complexity, *[s for b in getattr(block, 'closures', [])
                                   for s in function_scores(b)]]

    cc = [score for block in blocks for score in function_scores(block)]
    metrics.update({'cc.total': sum(cc), 'cc.max': max(cc, default=0),
                    'cc.mean': statistics.mean(cc) if cc else 0, 'cc.functions': len(cc),
                    'maintainability_index': mi_visit(code, multi=True)})
    raw = raw_analyze(code)._asdict()
    details['radon_raw'] = raw
    metrics.update({f'raw.{k}': v for k, v in raw.items()})
    halstead = h_visit(code)
    details['halstead'] = {'total': halstead.total._asdict(),
                          'functions': [{'name': n, **v._asdict()} for n, v in halstead.functions]}
    metrics.update({f'halstead.{k}': v for k, v in halstead.total._asdict().items()})
    save(artifact / 'details.json', details)
    return metrics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=Path('results/mbpp'))
    parser.add_argument('--out', type=Path, default=Path('results/quality'))
    parser.add_argument('--methods', nargs='+', choices=['acw', 'sew'], default=['acw', 'sew'])
    args = parser.parse_args()
    root, out = args.input.resolve(), args.out.resolve()
    originals = sorted((root / 'original').glob('*.py'))
    if not originals:
        parser.error(f'No original/*.py files in {root}; run run_mbpp.py first.')
    versions = {name: version(name) for name in ('ruff', 'complexipy', 'radon')}
    if out == root or root in out.parents:
        parser.error('--out must be outside the input directory')
    out.mkdir(parents=True, exist_ok=False)
    save(out / 'metadata.json', {'input': str(root), 'versions': versions,
        'python': sys.version, 'methods': args.methods, 'target_version': 'py310',
        'line_length': 88, 'strict_fixes': 'safe only', 'delta': 'after - before',
        'correctness_tests_run': False,
        'input_metadata': json.loads((root / 'metadata.json').read_text())
        if (root / 'metadata.json').exists() else None})
    statuses = {}
    if (root / 'results.jsonl').exists():
        for line in (root / 'results.jsonl').read_text().splitlines():
            row = json.loads(line)
            statuses[(str(row['task_id']), row['method'])] = row
    pairs, flat = [], []
    with (out / 'pairs.jsonl').open('w', encoding='utf-8') as stream:
        for index, path in enumerate(originals, 1):
            task = path.stem
            before_code = path.read_text(encoding='utf-8')
            try:
                before = analyze(before_code, out / 'artifacts' / task / 'original')
                before_error = None
            except Exception as exc:
                before, before_error = None, str(exc)
            for method in dict.fromkeys(args.methods):
                source_status = statuses.get((task, method), {})
                pair = {'task_id': task, 'method': method,
                        'watermark_status': source_status.get('status', 'unknown')}
                try:
                    if before_error is not None:
                        raise RuntimeError(f'Original analysis failed: {before_error}')
                    if source_status.get('status') == 'error':
                        raise RuntimeError(f"Watermark failed: {source_status.get('error')}")
                    after_code = (root / method / path.name).read_text(encoding='utf-8')
                    after = analyze(after_code, out / 'artifacts' / task / method)
                    pair.update(status='ok', changed=before_code != after_code,
                        before_sha256=hashlib.sha256(before_code.encode()).hexdigest(),
                        after_sha256=hashlib.sha256(after_code.encode()).hexdigest(),
                        before=before, after=after,
                        delta={k: after[k] - v for k, v in before.items()})
                    for metric in before:
                        flat.append(dict(task_id=task, method=method,
                            watermark_status=pair['watermark_status'], metric=metric,
                            before=before[metric], after=after[metric], delta=pair['delta'][metric]))
                    (out / 'artifacts' / task / method / 'watermark.diff').write_text(
                        ''.join(difflib.unified_diff(before_code.splitlines(keepends=True),
                            after_code.splitlines(keepends=True), fromfile='original', tofile=method)),
                        encoding='utf-8')
                except Exception as exc:
                    pair.update(status='error', error=str(exc))
                pairs.append(pair)
                stream.write(json.dumps(pair, ensure_ascii=False) + '\n')
                stream.flush()
                print(f'[{index}/{len(originals)}] {task} {method}: {pair["status"]}', flush=True)
    with (out / 'metrics.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            'task_id', 'method', 'watermark_status', 'metric', 'before', 'after', 'delta'])
        writer.writeheader()
        writer.writerows(flat)
    summary = {}
    for method in dict.fromkeys(args.methods):
        selected = [p for p in pairs if p['method'] == method]
        valid = [p for p in selected if p['status'] == 'ok']
        summary[method] = {'total': len(selected), 'paired': len(valid),
            'errors': len(selected) - len(valid),
            'abstained': sum(p['watermark_status'].startswith('abstain') for p in valid),
            'changed': sum(p['changed'] for p in valid), 'metrics': {}}
        for key in valid[0]['before'] if valid else []:
            deltas = [p['delta'][key] for p in valid]
            summary[method]['metrics'][key] = {
                'mean_before': statistics.mean(p['before'][key] for p in valid),
                'mean_after': statistics.mean(p['after'][key] for p in valid),
                'mean_delta': statistics.mean(deltas), 'median_delta': statistics.median(deltas),
                'increased': sum(d > 0 for d in deltas), 'decreased': sum(d < 0 for d in deltas),
                'unchanged': sum(d == 0 for d in deltas)}
    save(out / 'summary.json', summary)
    lines = ['# Porównanie jakości kodu', '', 'Delta = po − przed. Tylko kompletne pary.',
             'Wyniki nie potwierdzają poprawności funkcjonalnej.', '']
    for method, result in summary.items():
        lines += [f'## {method.upper()}', '',
                  f'Pary: {result["paired"]}; błędy: {result["errors"]}; '
                  f'odmowy osadzenia: {result["abstained"]}; zmienione: {result["changed"]}.', '',
                  '| Metryka | Średnia przed | Średnia po | Średnia delta |',
                  '|---|---:|---:|---:|']
        for key, values in result['metrics'].items():
            lines.append(f'| {key} | {values["mean_before"]:.4f} | '
                         f'{values["mean_after"]:.4f} | {values["mean_delta"]:+.4f} |')
        lines.append('')
    (out / 'report.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Report: {out / "report.md"}')
    return int(any(p['status'] == 'error' for p in pairs))


if __name__ == '__main__':
    raise SystemExit(main())
