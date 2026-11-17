#!/usr/bin/env python3
import collections,json,statistics
from pathlib import Path
root=Path(__file__).resolve().parents[1]/'results/full_watermark_study'
rows=json.loads((root/'results.json').read_text())
out=['# Pełny eksperyment: SEW i ACW','','Porównanie diagnostyk Ruffa dla oryginałów i plików po znakowaniu: [Ruff przed znakowaniem i po nim](ruff_przed_znakowaniem.md).','','Szczegółowy opis procedury, plików i ograniczeń znajduje się w [metodologii](README.md). Tabela liczy diagnostyki zgłoszone przed poprawkami; W oznacza jedynie prefiks kodu Ruffa, a nie ogólną klasyfikację ważności.','','| Zbiór | Metoda | Wszystkie | Wykonano | Błąd składni po znakowaniu | Ruff domyślny: razem / W | Ruff rozszerzony: razem / W |','|---|---|---:|---:|---:|---:|---:|']
for ds in ('bigcodebench','codecontests'):
 for method in ('sew','acw'):
  g=[x for x in rows if x['dataset']==ds and x['method']==method]; ok=[x for x in g if x['status']=='ok']
  def issues(p):
   c=collections.Counter()
   for x in ok:c.update(x['ruff'][p]['codes'])
   return f"{sum(c.values())} / {sum(v for k,v in c.items() if k.startswith('W'))}"
  out.append(f"| {ds} | {method.upper()} | {len(g)} | {len(ok)} | {sum(bool(x['syntax_error']) for x in ok)} | {issues('default')} | {issues('strict')} |")
out+=['','## Detekcja przed i po Ruffie','','W kolumnie „zanik” licznik obejmuje wyłącznie próbki wykryte przed poprawkami, a mianownik wszystkie takie próbki, dla których wynik po Ruffie jest dostępny. W obu wariantach Ruff wykonuje poprawki oraz formatowanie. Dla ACW detekcja oznacza brak zmian po ponownym zastosowaniu całego przyjętego łańcucha transformacji, a nie potwierdzenie autorstwa.','','| Zbiór | Metoda | Wykryto przed / poprawnie przeanalizowane | Zanik: domyślny | Zanik: rozszerzony |','|---|---|---:|---:|---:|']
for ds in ('bigcodebench','codecontests'):
 for method in ('sew','acw'):
  g=[x for x in rows if x['dataset']==ds and x['method']==method and x['status']=='ok']
  def d(v):
   if method=='sew':return v.get('verdict')=='Watermark detected'
   return v.get('fixed_point')
  before=[x for x in g if d(x.get('detection_before',{})) is not None]
  positives=[x for x in before if d(x.get('detection_before',{}))]
  def loss(p):
   eligible=[x for x in positives if d(x['ruff'][p].get('detection_after',{})) is not None]
   return f"{sum(not d(x['ruff'][p]['detection_after']) for x in eligible)} / {len(eligible)}"
  out.append(f'| {ds} | {method.upper()} | {len(positives)} / {len(before)} | {loss("default")} | {loss("strict")} |')
out+=['','## Błędy składni po ACW','']
errors=[x for x in rows if x['method']=='acw' and x.get('status')=='ok' and x.get('syntax_error')]
if errors:
 out.append(f'Po znakowaniu ACW błąd składni wystąpił w **{len(errors)}** plikach. Są zachowane w oryginalnej postaci; nie były uznawane za wiarygodne wyniki detekcji ACW.');out.append('')
 out.append('Reguła 45 usuwa pozostałe spacje, gdy liczba spacji we wcięciu nie jest wielokrotnością czterech, co może zniszczyć strukturę bloków.');out.append('')
 for x in errors:out.append(f"- [{x['id']}]({x['dataset']}/{x['index']:04d}/acw/watermarked.py): {x['syntax_error']}")
else: out.append('Nie wykryto błędów składni w plikach poprawnie przetworzonych przez ACW.')
out+=['','## Złożoność przed Ruffem','','Porównanie metryk dla oryginałów i tych samych plików po znakowaniu: [złożoność przed i po](zlozonosc_przed_i_po.md).','','Średnie obliczono ze skutecznie odczytanych wyników: złożoność cyklomatyczna Radona dla bloków, indeks utrzymywalności Radona dla plików oraz złożoność poznawcza Complexipy dla funkcji. W nawiasach podano liczby elementów, na których obliczono średnie.','','| Zbiór | Metoda | Radon CC: średnia (liczba bloków) | Radon MI: średnia (liczba plików) | Complexipy: średnia (liczba funkcji) |','|---|---|---:|---:|---:|']
for ds in ('bigcodebench','codecontests'):
 for method in ('sew','acw'):
  g=[x for x in rows if x['dataset']==ds and x['method']==method and x['status']=='ok' and not x.get('syntax_error')]
  cc=[]; mi=[]; cog=[]
  for x in g:
   folder=root/ds/f"{x['index']:04d}"/method
   try:
    a=json.loads((folder/'radon_cc.out').read_text()); cc += [z['complexity'] for v in a.values() if isinstance(v,list) for z in v if isinstance(z,dict) and isinstance(z.get('complexity'),(int,float))]
   except (ValueError,OSError,AttributeError):pass
   try:
    a=json.loads((folder/'radon_mi.out').read_text()); mi += [z['mi'] for z in a.values() if isinstance(z,dict) and isinstance(z.get('mi'),(int,float))]
   except (ValueError,OSError,AttributeError):pass
   try:
    a=json.loads((folder/'complexipy.json').read_text()); cog += [z['complexity'] for z in a if isinstance(z,dict) and isinstance(z.get('complexity'),(int,float))]
   except (ValueError,OSError,TypeError):pass
  def avg(v):return f'{statistics.mean(v):.2f} ({len(v)})' if v else 'brak danych (0)'
  out.append(f'| {ds} | {method.upper()} | {avg(cc)} | {avg(mi)} | {avg(cog)} |')
out+=['','## Status analiz','']
statuses=collections.Counter((x['method'],x['status']) for x in rows)
for (method,status),n in sorted(statuses.items()):out.append(f'- {method.upper()}, {status}: {n}.')
out+=['','Complexipy zwraca kod 1 również po przekroczeniu progu złożoności; pełne wyjścia narzędzi, kody wyjścia oraz szczegóły poszczególnych funkcji znajdują się w katalogach próbek. Radon może wypisać błąd parsowania w JSON mimo kodu wyjścia 0.','', '[Wyniki maszynowe](results.json).']
(root/'podsumowanie.md').write_text('\n'.join(out)+'\n',encoding='utf8')
