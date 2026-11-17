#!/usr/bin/env python3
"""Analyze the original corpus and compare matched per-file complexity metrics."""
import concurrent.futures, json, os, statistics, subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'results/full_watermark_study'
WORKERS = int(os.environ.get('WATERMARK_WORKERS', '8'))
COMMANDS = {
    'radon_cc': lambda p, d: ['radon', 'cc', '-j', str(p)],
    'radon_mi': lambda p, d: ['radon', 'mi', '-j', str(p)],
    'radon_raw': lambda p, d: ['radon', 'raw', '-j', str(p)],
    'complexipy': lambda p, d: ['complexipy', '--isolated', '--no-ignore', '--output-format', 'json', '--output', str(d / 'complexipy.json'), str(p)],
}

def run(item):
    dataset, index, ident = item
    folder = ROOT / dataset / f'{index:04d}'
    out = folder / 'original_metrics'
    out.mkdir(exist_ok=True)
    status = {'dataset': dataset, 'index': index, 'id': ident, 'tools': {}}
    for name, build in COMMANDS.items():
        try:
            p = subprocess.run(build(folder / 'original.py', out), capture_output=True, text=True, timeout=120)
            (out / f'{name}.out').write_text(p.stdout, encoding='utf8')
            (out / f'{name}.err').write_text(p.stderr, encoding='utf8')
            status['tools'][name] = {'exit': p.returncode}
        except (OSError, subprocess.TimeoutExpired) as e:
            status['tools'][name] = {'error': str(e)}
    (out / 'status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding='utf8')
    return status

def read_metrics(folder):
    result = {}
    errors = {}
    for name in ('radon_cc', 'radon_mi', 'radon_raw'):
        try:
            raw = json.loads((folder / f'{name}.out').read_text(encoding='utf8'))
            if name == 'radon_cc' and raw == {}:
                result['cc_blocks'] = 0
                result['cc_mean'] = None
                continue
            if len(raw) != 1: raise ValueError('expected exactly one file')
            v = next(iter(raw.values()))
            if isinstance(v, dict) and 'error' in v: raise ValueError(v['error'])
            if name == 'radon_cc':
                if not isinstance(v, list): raise ValueError('expected blocks')
                vals = [b['complexity'] for b in v]
                result['cc_blocks'] = len(vals)
                result['cc_mean'] = statistics.mean(vals) if vals else None
            elif name == 'radon_mi': result['mi'] = v['mi']
            else: result['sloc'] = v['sloc']
        except (ValueError, OSError, KeyError, TypeError) as e: errors[name] = str(e)
    try:
        data = json.loads((folder / 'complexipy.json').read_text(encoding='utf8'))
        if not isinstance(data, list): raise ValueError('expected list of functions')
        values = [x['complexity'] for x in data]
        result['cognitive_functions'] = len(values)
        result['cognitive_mean'] = statistics.mean(values) if values else None
    except (ValueError, OSError, KeyError, TypeError) as e: errors['complexipy'] = str(e)
    return result, errors

def main():
    version_checks = [('radon', '6.0.1'), ('complexipy', 'complexipy 9.0.0')]
    versions = {}
    for name, expected in version_checks:
        version = subprocess.run([name, '--version'], text=True, capture_output=True, check=True).stdout.strip()
        if version != expected: raise RuntimeError(f'{name}: expected {expected}, got {version}')
        versions[name] = version
    rows = json.loads((ROOT / 'results.json').read_text(encoding='utf8'))
    samples = sorted({(x['dataset'], x['index'], x['id']) for x in rows})
    print('Analyzing', len(samples), 'original files', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        statuses = []
        for n, status in enumerate(pool.map(run, samples), 1):
            statuses.append(status)
            if n % 200 == 0 or n == len(samples): print(n, '/', len(samples), flush=True)
    comparisons = []
    for x in rows:
        folder = ROOT / x['dataset'] / f"{x['index']:04d}"
        before, before_errors = read_metrics(folder / 'original_metrics')
        after, after_errors = read_metrics(folder / x['method'])
        if x.get('syntax_error') or x.get('status') != 'ok':
            after = {}
            after_errors['watermarked'] = x.get('syntax_error') or x.get('status')
        comparisons.append({'dataset': x['dataset'], 'id': x['id'], 'index': x['index'], 'method': x['method'], 'original': before, 'watermarked': after, 'original_errors': before_errors, 'watermarked_errors': after_errors})
    (ROOT / 'complexity_original_results.json').write_text(json.dumps({'versions': versions, 'statuses': statuses, 'comparisons': comparisons}, ensure_ascii=False, indent=2), encoding='utf8')
    report(comparisons)

def report(rows):
    metrics = [('cc_mean', 'Radon CC — średnia z bloków w pliku'), ('mi', 'Radon MI — indeks utrzymywalności pliku'), ('cognitive_mean', 'Complexipy — średnia z funkcji w pliku'), ('sloc', 'Radon — liczba linii kodu SLOC')]
    out = ['# Złożoność oryginałów a kodu oznakowanego', '', 'Przeanalizowano oryginały 1140 próbek BigCodeBench i 203 wybranych rozwiązań CodeContests tymi samymi wersjami i poleceniami Radona oraz Complexipy co kod oznakowany. Metryki kodu oznakowanego pochodzą z etapu przed uruchomieniem Ruffa.', '', 'Każda para średnich poniżej obejmuje **te same pliki**: wyłącznie próbki z dostępnym wynikiem danej metryki po obu stronach. W CC i Complexipy najpierw liczona jest średnia z bloków lub funkcji w pliku, a następnie średnia po plikach; pliki bez takich elementów nie wchodzą do tych dwóch porównań. Oryginały analizowano jeden raz dla obu metod.', '']
    for dataset in ('bigcodebench', 'codecontests'):
        out += [f'## {dataset}', '', '| Metoda | Metryka | Par plików | Oryginał: średnia | Po znakowaniu: średnia | Średnia różnica | Wzrost / bez zmian / spadek |', '|---|---|---:|---:|---:|---:|---:|']
        for method in ('sew', 'acw'):
            group = [x for x in rows if x['dataset'] == dataset and x['method'] == method]
            for key, label in metrics:
                pairs = [(x['original'].get(key), x['watermarked'].get(key)) for x in group]
                pairs = [(a, b) for a, b in pairs if isinstance(a, (int, float)) and isinstance(b, (int, float))]
                if not pairs:
                    out.append(f'| {method.upper()} | {label} | 0 | — | — | — | — |'); continue
                old = statistics.mean(a for a, b in pairs); new = statistics.mean(b for a, b in pairs)
                changes = Counter('up' if b-a > 1e-9 else 'down' if b-a < -1e-9 else 'same' for a, b in pairs)
                delta = new-old
                if abs(delta) < 0.005: delta = 0.0
                out.append(f"| {method.upper()} | {label} | {len(pairs)} | {old:.2f} | {new:.2f} | {delta:+.2f} | {changes['up']} / {changes['same']} / {changes['down']} |")
        out.append('')
    out += ['MI ma inną skalę niż złożoność: większa wartość jest zazwyczaj interpretowana jako większa łatwość utrzymania według modelu Radona. SLOC to liczba linii kodu według Radona. Wyniki to miary statyczne; nie potwierdzają poprawności działania ani nie wyjaśniają same z siebie przyczyn zmian.', '', 'Jedenaście niepoprawnych składniowo wyników ACW CodeContests wyłączono z porównań. Niektóre pliki nie zawierają funkcji lub bloków analizowanych przez narzędzia; brak wartości oraz szczegóły błędów zapisano osobno. Complexipy może zakończyć się kodem 1 po przekroczeniu progu; sam kod wyjścia nie oznacza niepowodzenia parsowania.', '', 'Surowe wyniki oryginału i statusy narzędzi znajdują się przy każdej próbce w katalogu `original_metrics/`; wyniki oznakowanych próbek pozostają w katalogach `sew/` i `acw/`. Zestawienie wszystkich par: [complexity_original_results.json](complexity_original_results.json).']
    (ROOT / 'zlozonosc_przed_i_po.md').write_text('\n'.join(out)+'\n', encoding='utf8')

if __name__ == '__main__': main()
