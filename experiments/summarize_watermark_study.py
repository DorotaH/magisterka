import json
from collections import Counter
from pathlib import Path
root=Path(__file__).resolve().parents[1]/'results/watermark_study'
rows=json.loads((root/'results.json').read_text())
lines=['# Wyniki eksperymentu', '', 'Wyniki dotyczą pilotażu: pierwszych 20 zadań BigCodeBench v0.1.4 i pierwszych 20 wybranych w repozytorium rozwiązań CodeContests. Szczegóły metody i ograniczenia są w [README](README.md).', '']
for ds in ['bigcodebench','codecontests']:
 lines += [f'## {ds}', '', '| Metoda | Próbek | Zmieniony kod | Poprawna składnia | Wykryto przed | Ruff domyślny: diagnostyki (W / pozostałe) | Wykryto po domyślnym | Ruff rozszerzony: diagnostyki (W / pozostałe) | Wykryto po rozszerzonym |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
 for method in ['sew','acw_partial']:
  group=[r for r in rows if r['dataset']==ds and r['method']==method]
  def detected(x): return x.get('verdict')=='Watermark detected' if method=='sew' else x.get('fixed_point') is True
  def stats(profile):
   rr=[r['ruff'][profile] for r in group if profile in r.get('ruff',{})]; c=Counter()
   for x in rr:c.update(x['codes'])
   w=sum(v for k,v in c.items() if k.startswith('W'))
   return f'{sum(c.values())} ({w} / {sum(c.values())-w})',sum(detected(x['detection_after']) for x in rr)
  d,dd=stats('default'); s,sd=stats('strict')
  lines.append(f"| {method} | {len(group)} | {sum(r.get('changed',False) for r in group)} | {sum(r.get('watermarked_valid_python',False) for r in group)} | {sum(detected(r.get('detection_before',{})) for r in group)} | {d} | {dd} | {s} | {sd} |")
 lines.append('')
lines += ['W tabeli „wykryto” dla ACW oznacza jedynie brak zmian po ponownym zastosowaniu lokalnych reguł; to nie jest wynik pełnego detektora ACW. Liczby po Ruffie obejmują również próbki niewykryte przed Ruffem i nie stanowią same w sobie miary utraty znaku. W oznacza kody reguł z prefiksem W; Ruff nie przypisuje wszystkim pozostałym diagnostykom jednolitej kategorii „error”.', '', 'Dwie próbki częściowego ACW w CodeContests (valid/12 i valid/24) mają niepoprawną składnię; ich wynik fixed_point nie jest wiarygodnym wykryciem. Szczegóły w results.json.', '', 'Dokładne dane, statusy błędów, liczby dla poszczególnych reguł oraz wyniki detekcji i metryk znajdują się w [results.json](results.json) i katalogach próbek.']
(root/'podsumowanie.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
