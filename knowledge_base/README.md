# Baza badania: watermarkowanie, jakość kodu i wykrywalność

Ten katalog jest głównym punktem wejścia do wyników. Jednostką badania jest
zadanie MBPP; wersje kodu i wyniki narzędzi łączą ten sam `task_id`.

| Zawartość | Liczba |
|---|---:|
| Zadania referencyjne MBPP | 974 |
| Stany kodu, wraz z jawnymi brakami wyniku | 14 610 |
| Wyniki trzech narzędzi, wraz ze statusami błędów | 43 830 |
| Wartości metryk | 459 264 |
| Rekordy wyników funkcji i klas | 39 420 |
| Rekordy detekcji, wraz z brakami wyniku | 19 480 |

## Co otworzyć

1. **[RESULTS.md](RESULTS.md)** — porównanie jakości przed i po znakowaniu,
   dostępne i wspólne kohorty ACW/SEW, przedziały bootstrapu oraz liczebności.
2. **[DETECTION.md](DETECTION.md)** — wykrycia przed i po każdej próbie Ruffa,
   przypadki zbyt małej liczby obserwacji, utracone i nowe wykrycia.
3. **[METHODS.md](METHODS.md)** — dokładne definicje etapów, narzędzi i ograniczeń.
4. **[EXAMPLES.md](EXAMPLES.md)** — kod i konkretne przykłady zmian.
5. **[SCHEMA.md](SCHEMA.md)** — struktura SQLite, CSV i definicje metryk.
6. **[REPRODUCE.md](REPRODUCE.md)** — polecenia odtworzenia i weryfikacji.

## Najważniejsze wyniki detekcji

Licznik to wykryte / ocenione. Wykrycie nie potwierdza poprawności programu.

| Kod | Przed Ruffem | Tylko formatter | ALL + formatter | Domyślny linter | Linter repo-max |
|---|---:|---:|---:|---:|---:|
| ACW | 552/974 | 0/577 | 0/577 | 556/974 | 506/974 |
| SEW | 708/974 | 136/974 | 65/974 | 652/974 | 648/974 |

397 wyników ACW ma błędną składnię. Formatter ich nie przetworzył, więc te
braki **nie są negatywnymi detekcjami**. Przed Ruffem w poprawnym podzbiorze
ACW wykryto 542/577 znaków. Szczegółowe tabele rozdzielają kod poprawny i błędny.

## Jak oglądać pojedyncze zadanie

Z głównego katalogu projektu:

```bash
python query_research.py overview
python query_research.py task 2
python query_research.py code 104 --variant sew --save /tmp/mbpp_104_sew.py
python query_research.py audit-code 2 --stage before_tabs
```

Program do odczytu działa na standardowej bibliotece Pythona. Nie wymaga
Sourcery ani uruchamiania kodu z datasetu. Eksport kodu zachowuje dokładne bajty.

## Dane do dalszej analizy

- [knowledge.sqlite](knowledge.sqlite) — samowystarczalna baza: kod jako BLOB,
  zadania i testy, metryki, diagnostyka, detekcja i audyt.
- [exports/quality_summary.csv](exports/quality_summary.csv) — podsumowania
  każdej metryki, metody, etapu i kohorty.
- [exports/watermark_quality_pairs.csv](exports/watermark_quality_pairs.csv)
  — każda para oryginał/oznaczony, przed Ruffem i po każdej próbie.
- [exports/ruff_quality_pairs.csv](exports/ruff_quality_pairs.csv) — wpływ
  Ruffa na tę samą wersję kodu.
- [exports/quality_values.csv](exports/quality_values.csv) — wartości per kod,
  narzędzie i metryka; zachowano także puste wartości ze statusem błędu.
- [exports/functions.csv](exports/functions.csv) — wyniki funkcji i klas.
- [exports/detections.csv](exports/detections.csv) — detekcje i p-value.
- [exports/detection_transitions.csv](exports/detection_transitions.csv)
  — zmiany wykryć dla tych samych zadań.
- [exports/tool_statuses.csv](exports/tool_statuses.csv) i
  [exports/syntax_failures.csv](exports/syntax_failures.csv) — kompletne błędy.
- [validation.json](validation.json) — wykonane sprawdzenia, w tym ponowna
  detekcja wszystkich 9740 przypadków SEW z archiwalnego kodu detektora.

Wersja skompresowana `knowledge.sqlite.gz` służy do przenoszenia i GitHuba;
surowy plik SQLite można odtworzyć poleceniem `python knowledge_base/unpack.py`.

## Granice wniosków

To pomiary statyczne referencyjnego MBPP, z jedną konfiguracją ACW i jednym
publicznym kluczem SEW. Nie oceniano generacji LLM ani nie wykonywano testów
funkcjonalnych. Brak oryginalnej konfiguracji Sourcery ogranicza replikowalność
ACW względem publikacji. Średnie jakości ACW dotyczą poprawnego podzbioru;
dlatego raportuje się także wyniki na wspólnych zadaniach obu metod.

Surowe wyniki i rozpoznane problemy zachowano, bez ręcznego poprawiania
oznakowanego kodu ani wybierania korzystniejszego klucza.
