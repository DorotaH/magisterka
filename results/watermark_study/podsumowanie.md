# Wyniki eksperymentu

Wyniki dotyczą pilotażu: pierwszych 20 zadań BigCodeBench v0.1.4 i pierwszych 20 wybranych w repozytorium rozwiązań CodeContests. Szczegóły metody i ograniczenia są w [README](README.md).

## bigcodebench

| Metoda | Próbek | Zmieniony kod | Poprawna składnia | Wykryto przed | Ruff domyślny: diagnostyki (W / pozostałe) | Wykryto po domyślnym | Ruff rozszerzony: diagnostyki (W / pozostałe) | Wykryto po rozszerzonym |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sew | 20 | 20 | 20 | 20 | 44 (0 / 44) | 2 | 215 (85 / 130) | 3 |
| acw_partial | 20 | 20 | 20 | 20 | 32 (0 / 32) | 0 | 425 (301 / 124) | 0 |

## codecontests

| Metoda | Próbek | Zmieniony kod | Poprawna składnia | Wykryto przed | Ruff domyślny: diagnostyki (W / pozostałe) | Wykryto po domyślnym | Ruff rozszerzony: diagnostyki (W / pozostałe) | Wykryto po rozszerzonym |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sew | 20 | 20 | 20 | 18 | 73 (0 / 73) | 9 | 215 (82 / 133) | 12 |
| acw_partial | 20 | 20 | 18 | 20 | 30 (0 / 30) | 2 | 764 (674 / 90) | 2 |

W tabeli „wykryto” dla ACW oznacza jedynie brak zmian po ponownym zastosowaniu lokalnych reguł; to nie jest wynik pełnego detektora ACW. Liczby po Ruffie obejmują również próbki niewykryte przed Ruffem i nie stanowią same w sobie miary utraty znaku. W oznacza kody reguł z prefiksem W; Ruff nie przypisuje wszystkim pozostałym diagnostykom jednolitej kategorii „error”.

Dokładne dane, statusy błędów, liczby dla poszczególnych reguł oraz wyniki detekcji i metryk znajdują się w [results.json](results.json) i katalogach próbek.

Dwie próbki częściowego ACW w CodeContests (`CodeContests/valid/12` i `CodeContests/valid/24`) po transformacji mają niepoprawną składnię. Ich wynik `fixed_point` nie jest wiarygodnym wykryciem: reguły przestawiania nie mogą poprawnie przeanalizować takiego kodu. Ruff nie mógł ich sformatować; zachowano jego diagnostykę i status błędu. Wyniki metryk dla tych plików należy traktować jako nieudane analizy.

Wśród próbek SEW wykrytych przed Ruffem detekcja zanikła po wariancie domyślnym w 18/20 plikach BigCodeBench i 9/18 CodeContests; po wariancie rozszerzonym odpowiednio w 17/20 i 6/18. Oba warianty obejmują formatowanie, więc wynik nie izoluje wpływu samego lintowania.
