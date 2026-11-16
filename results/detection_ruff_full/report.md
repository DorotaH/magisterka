> Przebieg kontrolny z normalizacją CRLF/LF. Końcowy raport: [detection_ruff_exact](../detection_ruff_exact/report.md).

# Detekcja watermarków przed i po Ruffie

Zadania MBPP: 974. SEW: alpha=0.01.

Próba podstawowa: formatowanie Ruff. Rygorystyczna: wszystkie reguły, bezpieczne poprawki i formatowanie. Użyto dokładnych kopii z analizy jakości.

| Kod / detektor | Etap | Wykryte | Ocenione | Brak wyniku | Wykryte w poprawnym kodzie | Poprawne składniowo ocenione |
|---|---|---:|---:|---:|---:|---:|
| acw/acw | before | 552 | 974 | 0 | 542 | 577 |
| acw/acw | ruff_default | 0 | 577 | 397 | 0 | 577 |
| acw/acw | ruff_strict | 0 | 577 | 397 | 0 | 577 |
| original/acw | before | 0 | 974 | 0 | 0 | 974 |
| original/acw | ruff_default | 0 | 974 | 0 | 0 | 974 |
| original/acw | ruff_strict | 0 | 974 | 0 | 0 | 974 |
| original/sew | before | 3 | 974 | 0 | 3 | 974 |
| original/sew | ruff_default | 3 | 974 | 0 | 3 | 974 |
| original/sew | ruff_strict | 3 | 974 | 0 | 3 | 974 |
| sew/sew | before | 705 | 974 | 0 | 705 | 974 |
| sew/sew | ruff_default | 154 | 974 | 0 | 154 | 974 |
| sew/sew | ruff_strict | 65 | 974 | 0 | 65 | 974 |

## Zmiany na tych samych zadaniach

| Kod / detektor / Ruff | Utrzymane wykrycie | Utracone | Nowe | Brak wykrycia w obu | Brak porównania |
|---|---:|---:|---:|---:|---:|
| original/acw/ruff_default | 0 | 0 | 0 | 974 | 0 |
| original/acw/ruff_strict | 0 | 0 | 0 | 974 | 0 |
| original/sew/ruff_default | 1 | 2 | 2 | 969 | 0 |
| original/sew/ruff_strict | 0 | 3 | 3 | 968 | 0 |
| acw/acw/ruff_default | 0 | 542 | 0 | 35 | 397 |
| acw/acw/ruff_strict | 0 | 542 | 0 | 35 | 397 |
| sew/sew/ruff_default | 154 | 551 | 0 | 269 | 0 |
| sew/sew/ruff_strict | 65 | 640 | 0 | 269 | 0 |

Brak wyniku po błędzie Ruffa nie oznacza niewykrytego watermarku. Surowa detekcja ACW obejmuje także błędny składniowo kod; podano osobne liczniki dla poprawnych plików. Dla SEW zachowano rozróżnienie braku dowodów i zbyt małej liczby obserwacji w results.jsonl oraz summary.json.

Kod po Ruffie: inputs/. Ponowne transformacje ACW: acw_reapplied/. Każdy rekord zawiera ścieżkę pliku i SHA-256. Nie wykonywano testów funkcjonalnych.
