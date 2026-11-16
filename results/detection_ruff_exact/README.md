# Detekcja watermarków — pełny MBPP, przed i po Ruffie

To końcowy przebieg na dokładnych bajtach plików, z zachowaniem CRLF/LF.
974 zadania; 11688 rekordów detekcji. `results.csv` i `results.jsonl` wskazują
zadanie, źródło, detektor, etap, status, werdykt, pliki i SHA-256.
`transitions.csv` zapisuje zmiany wykrycia dla tych samych zadań.

| Kod | Przed Ruffem | Formatowanie | Wszystkie bezpieczne poprawki + formatowanie |
|---|---:|---:|---:|
| ACW | 552 / 974 | 0 / 577 | 0 / 577 |
| SEW | 708 / 974 | 136 / 974 | 65 / 974 |

Dla 397 błędnych składniowo wyników ACW Ruff nie zwrócił przetworzonego kodu.
Po Ruffie mają `detected: null`, nie `false`. Przed Ruffem w poprawnym
składniowo podzbiorze ACW wykryto 542 / 577 znaków; wszystkie te wykrycia
zostały utracone po obu próbach Ruffa. Surowy licznik 552 zawiera też
10 wykryć w kodzie niepoprawnym składniowo.

W oryginałach MBPP detektor ACW wskazał 0 / 974, a SEW 3 / 974 na każdym
etapie. To te same liczebności, ale nie zawsze te same zadania — szczegóły
są w `transitions.csv`.

SEW: alpha=0,01, minimum 5 niezależnych obserwacji, oficjalny werdykt
`Watermark detected`. `Insufficient evidence` pozostaje oddzielnym werdyktem.
W poprzednim liczniku używano samego p<0,01, co dawało 908 zamiast 708 wykryć
przed Ruffem. Poprawiono licznik, zachowując stare dane w
`../mbpp_full_complete/*.legacy-p-only`. Szczegółowe wyniki detektora się nie zmieniły.

Ruff 0.17.5, tryb isolated, target Python 3.10, 88 znaków, line-ending=auto.
Podstawowa próba to samo formatowanie. Rygorystyczna: check --select ALL
--fix --no-unsafe-fixes, potem formatowanie. Poprawki działają na kopiach.
Nie wykonywano testów funkcjonalnych; samo wykrycie nie potwierdza poprawności kodu.

`inputs/` przechowuje dokładne kopie przed i po Ruffie;
`acw_reapplied/` przechowuje kod po ponownym ACW. Przy zgodności wszystkich
hashy wykorzystano zapisane detekcje kodu ACW, który miał już LF. Wskazuje je
pole `reused_from` oraz `metadata.json`. Oryginały CRLF i wyniki Ruffa oceniono ponownie.

`summary.json`, `transitions_summary.json` i [report.md](report.md) podają
wszystkie liczniki. `validation.json` opisuje sprawdzenia kompletności i hashy.
`sew_q_table.json` to kopia tabeli kalibracyjnej; `detector_sources.json`
zawiera hashe użytych źródeł. Wcześniejszy przebieg `../detection_ruff_full`
normalizował końce linii i pozostaje wyłącznie do audytu.

Odtworzenie od początku (nowy folder):

```bash
python detect_ruff.py --input results/mbpp_full_complete --quality results/quality_full --out results/detection_repeat --workers 8
```
