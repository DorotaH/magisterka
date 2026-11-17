# Ruff przed znakowaniem i po nim

Przeanalizowano 1343 oryginalnych plików: 1140 BigCodeBench oraz 203 CodeContests. Użyto ruff 0.17.5, tych samych profili i tych samych plików wejściowych co w głównym eksperymencie. Diagnostykę zebrano bez zmian plików: `ruff check --isolated --output-format json`; wariant rozszerzony dodaje `--select E,F,W,I,B,UP,SIM`.

Wartości po znakowaniu pochodzą z diagnostyki **przed** poprawkami i formatowaniem Ruffa. Różnica to zmiana sumy diagnostyk na tych samych próbkach; nie określa, które poszczególne problemy powstały ani zniknęły, ponieważ znakowanie mogło także przesunąć lub zmienić istniejące diagnostyki.

| Zbiór | Profil | Przed znakowaniem | Po SEW | Różnica SEW | Po ACW | Różnica ACW |
|---|---|---:|---:|---:|---:|---:|
| bigcodebench | default | 1593 | 1916 | +323 | 1487 | -106 |
| bigcodebench | strict | 7908 | 8704 | +796 | 21653 | +13745 |
| codecontests | default | 745 | 1085 | +340 | 735 | -10 |
| codecontests | strict | 2849 | 3041 | +192 | 9776 | +6927 |

## Liczba próbek z co najmniej jedną diagnostyką

| Zbiór | Profil | Przed | Po SEW | Po ACW |
|---|---|---:|---:|---:|
| bigcodebench | default | 1033 | 1127 | 956 |
| bigcodebench | strict | 1135 | 1139 | 1140 |
| codecontests | default | 133 | 175 | 137 |
| codecontests | strict | 192 | 202 | 203 |

## Najczęstsze kody przed znakowaniem

- bigcodebench, default: I001: 989, RUF059: 141, B006: 66, W605: 57, BLE001: 45, TRY004: 35, F841: 33, F821: 30, UP024: 15, F401: 14
- bigcodebench, strict: E501: 4141, W293: 1528, I001: 989, W291: 769, B006: 66, UP015: 61, W605: 57, B904: 50, B905: 37, F841: 33
- codecontests, default: F401: 352, I001: 134, B023: 41, PIE808: 25, UP032: 23, PLR1711: 14, SIM114: 11, SIM115: 11, F841: 10, F821: 8
- codecontests, strict: W191: 630, W293: 543, F401: 352, E701: 177, I001: 134, W292: 108, W291: 108, E402: 107, E702: 104, E741: 92

Wyniki porównania obejmują wszystkie próbki, także 11 plików ACW z błędami składni; takie diagnostyki są uwzględnione w liczbach po ACW. Ruff nie klasyfikuje wszystkich diagnostyk jednoznacznie jako błędów lub ostrzeżeń; pełne kody i komunikaty znajdują się w JSON.

Pliki `ruff_before_default_diagnostics.json` i `ruff_before_strict_diagnostics.json` znajdują się obok `original.py` każdej próbki. Zestawienie maszynowe: [ruff_before_results.json](ruff_before_results.json). Wyniki po znakowaniu i informacje o ograniczeniach: [główne podsumowanie](podsumowanie.md) i [metodologia](README.md).
