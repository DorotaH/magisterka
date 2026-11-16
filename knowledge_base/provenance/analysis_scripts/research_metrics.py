"""Independent, exact-input quality measurements for the research database."""
from collections import Counter
import hashlib
import json
import math
import statistics
import subprocess
import sys
import time
import warnings

warnings.filterwarnings('ignore', category=SyntaxWarning)


def syntax(data):
    try:
        compile(data, '<research-input>', 'exec')
        return {'valid': True}
    except (SyntaxError, ValueError) as error:
        return {'valid': False, 'error': str(error), 'line': getattr(error, 'lineno', None)}


def source_metrics(data):
    text = data.decode('utf-8')
    lines = text.splitlines()
    return {'bytes': len(data), 'lines': len(lines), 'crlf': data.count(b'\r\n'),
            'lf_without_cr': data.count(b'\n') - data.count(b'\r\n'),
            'tab_characters': text.count('\t'),
            'leading_tab_lines': sum(line.startswith('\t') for line in lines),
            'trailing_whitespace_lines': sum(line != line.rstrip(' \t') for line in lines),
            'max_line_length': max(map(len, lines), default=0)}


def lint(data, select=None):
    args = [sys.executable, '-m', 'ruff', 'check', '--isolated', '--no-cache',
            '--target-version', 'py310', '--line-length', '88', '--output-format', 'json']
    if select:
        args += ['--select', select]
    result = subprocess.run([*args, '--stdin-filename', 'solution.py', '-'],
                            input=data, capture_output=True, timeout=60, check=False)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.decode('utf-8', 'replace'))
    return json.loads(result.stdout), result.stderr.decode('utf-8', 'replace')


def measure_ruff(data, valid):
    metrics, details = {}, {}
    parse_error = not valid
    for profile, selection in [('default', None), ('all', 'ALL')]:
        diagnostics, stderr = lint(data, selection)
        parse_error |= any(d['code'] in (None, 'invalid-syntax') for d in diagnostics)
        metrics[f'{profile}.violations'] = len(diagnostics)
        metrics[f'{profile}.safe_fixable'] = sum(
            d.get('fix') is not None and d['fix'].get('applicability') == 'safe'
            for d in diagnostics)
        details[profile] = {'diagnostics': diagnostics, 'stderr': stderr,
                            'counts_by_rule': dict(Counter(d['code'] for d in diagnostics))}
    return {'status': 'syntax_error' if parse_error else 'ok', 'metrics': metrics, 'details': details,
            'error': 'Diagnostics for invalid syntax are incomplete and excluded from paired quality summaries.'
            if parse_error else None}


def measure_complexipy(code):
    from complexipy import code_complexity
    result = code_complexity(code, check_script=True, no_ignore=True, with_plans=False)
    functions = [dict(name=f.name, complexity=f.complexity, line_start=f.line_start,
                      line_end=f.line_end,
                      line_complexities=[{'line': line.line, 'complexity': line.complexity}
                                         for line in f.line_complexities])
                 for f in result.functions]
    scores = [f['complexity'] for f in functions if f['name'] != '<module>']
    metrics = {'total': result.complexity, 'functions_total': sum(scores),
               'module': sum(f['complexity'] for f in functions if f['name'] == '<module>'),
               'function_count': len(scores), 'function_max': max(scores, default=0),
               'function_mean': statistics.mean(scores) if scores else 0}
    return {'status': 'ok', 'metrics': metrics, 'details': {'functions': functions}}


def measure_radon(code):
    from radon.complexity import add_inner_blocks, cc_visit, cc_rank
    from radon.metrics import h_visit, mi_visit
    from radon.raw import analyze
    from radon.visitors import ComplexityVisitor, Function
    functions, classes, seen = [], [], set()
    for block in add_inner_blocks(cc_visit(code)):
        key = (type(block).__name__, block.lineno, block.col_offset, block.endline)
        if key in seen:
            continue
        seen.add(key)
        entry = dict(name=block.fullname, line_start=block.lineno, line_end=block.endline,
                     column=block.col_offset, complexity=block.complexity,
                     rank=cc_rank(block.complexity))
        (functions if isinstance(block, Function) else classes).append(entry)
    scores = [f['complexity'] for f in functions]
    raw = analyze(code)._asdict()
    halstead = h_visit(code)
    metrics = {'cc.function_total': sum(scores), 'cc.function_count': len(scores),
               'cc.function_max': max(scores, default=0),
               'cc.function_mean': statistics.mean(scores) if scores else 0,
               'cc.module': ComplexityVisitor.from_code(code).complexity,
               'cc.class_count': len(classes), 'mi': mi_visit(code, multi=True),
               **{f'raw.{key}': value for key, value in raw.items()},
               **{f'halstead.{key}': value for key, value in halstead.total._asdict().items()}}
    return {'status': 'ok', 'metrics': metrics, 'details': {'functions': functions,
        'classes': classes, 'raw': raw, 'halstead_total': halstead.total._asdict(),
        'halstead_functions': [{'name': name, **value._asdict()}
                              for name, value in halstead.functions]}}


def measure_artifact(job):
    """A failing tool cannot suppress the other tools' results."""
    from pathlib import Path
    artifact_id, path, expected_sha = job
    data = Path(path).read_bytes()
    actual_sha = hashlib.sha256(data).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(f'Input hash mismatch: {path}')
    code = data.decode('utf-8')
    syntax_result = syntax(data)
    results = []
    for tool in ('ruff', 'complexipy', 'radon'):
        start = time.perf_counter()
        try:
            if tool == 'ruff':
                result = measure_ruff(data, syntax_result['valid'])
            elif not syntax_result['valid']:
                result = {'status': 'syntax_error', 'error': syntax_result['error'], 'metrics': {}}
            else:
                result = (measure_complexipy if tool == 'complexipy' else measure_radon)(code)
            for key, value in result['metrics'].items():
                if not math.isfinite(value):
                    raise ValueError(f'Non-finite metric {key}: {value}')
        except Exception as error:
            result = {'status': 'tool_error', 'error': str(error), 'metrics': {}}
        results.append(dict(tool=tool, seconds=time.perf_counter()-start, **result))
    return {'artifact_id': artifact_id, 'sha256': actual_sha, 'syntax': syntax_result,
            'source_metrics': source_metrics(data), 'measurements': results}
