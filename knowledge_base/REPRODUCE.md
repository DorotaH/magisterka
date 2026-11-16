# Odtworzenie i weryfikacja

## Odczyt istniejącej bazy

Wystarczy standardowy Python z SQLite. Po pobraniu skompresowanej bazy:

```bash
python knowledge_base/unpack.py
python query_research.py overview
python query_research.py task 104 --stage ruff_lint_default
python query_research.py sql "SELECT variant,stage,detector,transition,COUNT(*) FROM v_detection_transitions GROUP BY variant,stage,detector,transition"
```

Bazę można otworzyć także w przeglądarce SQLite. Dokładne źródło eksportuje się
poleceniem `code ... --save NOWY_PLIK`; istniejący plik nie jest nadpisywany.

## Środowisko pomiarowe

Użyto Pythona 3.14.4 i wersji pakietów zapisanych w
`provenance/quality_metadata.json` oraz `provenance/requirements-lock.txt`.
Do odczytu bazy i CSV nie trzeba instalować tych bibliotek. Do ponownego
znakowania ACW potrzebne jest działające logowanie Sourcery z dostępem do CLI.

W osobnym środowisku z głównego katalogu projektu:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r knowledge_base/provenance/requirements-lock.txt
sourcery login
```

Repozytoria ACW i SEW muszą znajdować się w katalogach `ACW/` i `SEW/`.
Wersje użytych źródeł i ich hashe zachowano w `provenance/source_snapshot/`
i `provenance/source_hashes.json`. Konfiguracja Sourcery i tabela SEW są
osobnymi plikami proweniencji. Nie zapisano tokenów logowania.

## Pełny nowy przebieg

Wszystkie katalogi wyjściowe poniżej mają być nowe. Polecenia uruchamia się
z głównego katalogu projektu. Pobranie MBPP wymaga Internetu albo cache HF.

```bash
python run_mbpp.py --limit 0 --revision 39ad389e423dd348012ea1b1bcbf224aad8f34a4 --prepare-only --out results/repeat_input
python run_mbpp_batch.py --input results/repeat_input --out results/repeat_marked --workers 8
python audit_acw_stages.py --input results/repeat_marked --out results/repeat_audit --workers 8
python detect_ruff.py --input results/repeat_marked --out results/repeat_detection --stages before ruff_default ruff_strict ruff_lint_default ruff_lint_repo_max --workers 8
python measure_research.py --input results/repeat_detection --out results/repeat_quality --workers 8
python build_knowledge.py --input results/repeat_marked --detections results/repeat_detection --quality results/repeat_quality --audit results/repeat_audit --out knowledge_repeat
python report_knowledge.py --base knowledge_repeat --bootstrap 2000
python verify_knowledge.py --base knowledge_repeat --external --recompute-sew
```

Jest to przebieg zapisanej implementacji z odtworzoną konfiguracją ACW,
nie gwarantowana replikacja artykułu. Znakowanie i narzędzia nie uruchamiają
testów datasetu ani jego funkcji. Nie dodaje się formattera przed znakowaniem,
ponieważ zmieniłby badany punkt odniesienia. Nie naprawia się kodu ACW ręcznie.

Detekcję i pomiary można wznowić tym samym poleceniem z `--resume`.
Zmiana wejść, wersji lub definicji pomiaru jest odrzucana. Pomiary naprawiają
wyłącznie urwany ostatni rekord własnego checkpointu, zachowując jego kopię.
Błąd w środku pliku przerywa wznowienie. Budowę SQLite można powtórzyć
do nowego katalogu bez ponownego liczenia narzędzi.

## Co zostało zweryfikowane

- Wszystkie 974 oryginały w bazie mają identyczne bajty jak rekordy datasetu.
- Wszystkie zapisane fragmenty kodu i ponowne wyjścia ACW mają poprawne SHA-256.
- Każdy stan ma wynik/status każdego z trzech narzędzi.
- Wszystkie wartości, szczegóły i statusy porównano z 43 830 rekordami pomiarowymi.
- Kontrolę składni powtórzono; sumy funkcji i modułów sprawdzono z surowymi wynikami.
- Liczby funkcji Radona porównano ze wszystkimi deklaracjami w AST tego zbioru.
- Każda decyzja ACW zgadza się z identycznością zapisanego wejścia i ponownego wyjścia.
- Wszystkie 9740 szczegółowych wyników SEW przeliczono z archiwalnego detektora i tabeli.
- Sprawdzono klucze obce, integralność SQLite, kompletność CSV i mianowniki podsumowań.
- Testy regresji obejmują CRLF, minimum dowodu SEW, braki wyników, niezależność
  narzędzi, zagnieżdżone funkcje Radona i wznawianie checkpointów.

```bash
python -m unittest discover -s tests
python verify_knowledge.py --base knowledge_base --external --recompute-sew
```

Opcja `--external` wymaga zachowanych pierwotnych katalogów `results/`,
ponieważ sprawdza pełne logi i pliki wejściowe. Bez niej weryfikacja działa
na samowystarczalnej bazie i jej proweniencji. `--recompute-sew` wymaga
zależności parsera SEW. Szczegóły aktualnego sprawdzenia są w `validation.json`.

Czasów pomiarów pod obciążeniem nie należy traktować jako kontrolowanego
benchmarku wydajności. Ponowny przebieg może mieć inne czasy i hash całego
SQLite, mimo identycznych wyników merytorycznych. Celem odtworzenia są
zapisane wejścia, definicje, metryki i werdykty, a nie identyczny czas działania.
