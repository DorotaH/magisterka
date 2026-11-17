#!/usr/bin/env python3
"""Run isolated Ruff diagnostics on original inputs and compare matched samples."""
import collections, concurrent.futures, json, os, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'results/full_watermark_study'
RUFF = os.environ.get('RUFF_BINARY', 'ruff')
PROFILES = {'default': [], 'strict': ['--select', 'E,F,W,I,B,UP,SIM']}

def main():
    version = subprocess.run([RUFF, '--version'], text=True, capture_output=True, check=True).stdout.strip()
    if version != 'ruff 0.17.5':
        raise RuntimeError(f'Expected ruff 0.17.5 for comparison; found {version}')
    rows = json.loads((ROOT / 'results.json').read_text(encoding='utf8'))
    originals = {(x['dataset'], x['index']): x['id'] for x in rows}
    def run(entry):
        (dataset, index), identifier = entry
        folder = ROOT / dataset / f'{index:04d}'
        result = {'dataset': dataset, 'index': index, 'id': identifier, 'ruff': {}}
        for profile, opts in PROFILES.items():
            cmd = [RUFF, 'check', '--isolated', *opts, '--output-format', 'json', str(folder / 'original.py')]
            r = subprocess.run(cmd, text=True, capture_output=True, timeout=120)
            if r.returncode not in (0, 1):
                raise RuntimeError(f'{identifier} {profile}: Ruff returned {r.returncode}: {r.stderr}')
            findings = json.loads(r.stdout)
            (folder / f'ruff_before_{profile}_diagnostics.json').write_text(json.dumps(findings, ensure_ascii=False, indent=2), encoding='utf8')
            result['ruff'][profile] = {'diagnostics': len(findings), 'codes': dict(collections.Counter(f['code'] for f in findings)), 'exit': r.returncode}
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        baseline = list(executor.map(run, sorted(originals.items())))
    (ROOT / 'ruff_before_results.json').write_text(json.dumps({'ruff_version': version, 'samples': baseline}, ensure_ascii=False, indent=2), encoding='utf8')
    by_key = {(r['dataset'], r['index']): r for r in baseline}
    out = ['# Ruff przed znakowaniem i po nim', '', f'Przeanalizowano {len(baseline)} oryginalnych plików: 1140 BigCodeBench oraz 203 CodeContests. Użyto {version}, tych samych profili i tych samych plików wejściowych co w głównym eksperymencie. Diagnostykę zebrano bez zmian plików: `ruff check --isolated --output-format json`; wariant rozszerzony dodaje `--select E,F,W,I,B,UP,SIM`.', '', 'Wartości po znakowaniu pochodzą z diagnostyki **przed** poprawkami i formatowaniem Ruffa. Różnica to zmiana sumy diagnostyk na tych samych próbkach; nie określa, które poszczególne problemy powstały ani zniknęły, ponieważ znakowanie mogło także przesunąć lub zmienić istniejące diagnostyki.', '', '| Zbiór | Profil | Przed znakowaniem | Po SEW | Różnica SEW | Po ACW | Różnica ACW |', '|---|---|---:|---:|---:|---:|---:|']
    for dataset in ('bigcodebench', 'codecontests'):
        for profile in PROFILES:
            orig = [x for x in baseline if x['dataset'] == dataset]
            before = sum(x['ruff'][profile]['diagnostics'] for x in orig)
            after = {m: sum(x['ruff'][profile]['diagnostics'] for x in rows if x['dataset']==dataset and x['method']==m and x['status']=='ok') for m in ('sew','acw')}
            out.append(f"| {dataset} | {profile} | {before} | {after['sew']} | {after['sew']-before:+} | {after['acw']} | {after['acw']-before:+} |")
    out += ['', '## Liczba próbek z co najmniej jedną diagnostyką', '', '| Zbiór | Profil | Przed | Po SEW | Po ACW |', '|---|---|---:|---:|---:|']
    for dataset in ('bigcodebench', 'codecontests'):
        for profile in PROFILES:
            before = sum(x['ruff'][profile]['diagnostics'] > 0 for x in baseline if x['dataset'] == dataset)
            after = {m: sum(x['ruff'][profile]['diagnostics'] > 0 for x in rows if x['dataset']==dataset and x['method']==m and x['status']=='ok') for m in ('sew','acw')}
            out.append(f"| {dataset} | {profile} | {before} | {after['sew']} | {after['acw']} |")
    out += ['', '## Najczęstsze kody przed znakowaniem', '']
    for dataset in ('bigcodebench', 'codecontests'):
        for profile in PROFILES:
            counts = collections.Counter()
            for x in baseline:
                if x['dataset']==dataset: counts.update(x['ruff'][profile]['codes'])
            out.append(f"- {dataset}, {profile}: " + ', '.join(f'{k}: {v}' for k,v in counts.most_common(10)))
    out += ['', 'Wyniki porównania obejmują wszystkie próbki, także 11 plików ACW z błędami składni; takie diagnostyki są uwzględnione w liczbach po ACW. Ruff nie klasyfikuje wszystkich diagnostyk jednoznacznie jako błędów lub ostrzeżeń; pełne kody i komunikaty znajdują się w JSON.', '', 'Pliki `ruff_before_default_diagnostics.json` i `ruff_before_strict_diagnostics.json` znajdują się obok `original.py` każdej próbki. Zestawienie maszynowe: [ruff_before_results.json](ruff_before_results.json). Wyniki po znakowaniu i informacje o ograniczeniach: [główne podsumowanie](podsumowanie.md) i [metodologia](README.md).']
    (ROOT/'ruff_przed_znakowaniem.md').write_text('\n'.join(out)+'\n', encoding='utf8')
    print('Processed', len(baseline), 'originals with', version)

if __name__ == '__main__':
    main()
