# Pełny eksperyment: SEW i ACW

Porównanie diagnostyk Ruffa dla oryginałów i plików po znakowaniu: [Ruff przed znakowaniem i po nim](ruff_przed_znakowaniem.md).

Szczegółowy opis procedury, plików i ograniczeń znajduje się w [metodologii](README.md). Tabela liczy diagnostyki zgłoszone przed poprawkami; W oznacza jedynie prefiks kodu Ruffa, a nie ogólną klasyfikację ważności.

| Zbiór | Metoda | Wszystkie | Wykonano | Błąd składni po znakowaniu | Ruff domyślny: razem / W | Ruff rozszerzony: razem / W |
|---|---|---:|---:|---:|---:|---:|
| bigcodebench | SEW | 1140 | 1140 | 0 | 1916 / 57 | 8704 / 2896 |
| bigcodebench | ACW | 1140 | 1140 | 0 | 1487 / 57 | 21653 / 16178 |
| codecontests | SEW | 203 | 203 | 0 | 1085 / 0 | 3041 / 1390 |
| codecontests | ACW | 203 | 203 | 11 | 735 / 0 | 9776 / 8364 |

## Detekcja przed i po Ruffie

W kolumnie „zanik” licznik obejmuje wyłącznie próbki wykryte przed poprawkami, a mianownik wszystkie takie próbki, dla których wynik po Ruffie jest dostępny. W obu wariantach Ruff wykonuje poprawki oraz formatowanie. Dla ACW detekcja oznacza brak zmian po ponownym zastosowaniu całego przyjętego łańcucha transformacji, a nie potwierdzenie autorstwa.

| Zbiór | Metoda | Wykryto przed / poprawnie przeanalizowane | Zanik: domyślny | Zanik: rozszerzony |
|---|---|---:|---:|---:|
| bigcodebench | SEW | 1136 / 1140 | 1100 / 1136 | 1083 / 1136 |
| bigcodebench | ACW | 1137 / 1140 | 1137 / 1137 | 1137 / 1137 |
| codecontests | SEW | 189 / 203 | 101 / 189 | 51 / 189 |
| codecontests | ACW | 154 / 192 | 154 / 154 | 154 / 154 |

## Błędy składni po ACW

Po znakowaniu ACW błąd składni wystąpił w **11** plikach. Są zachowane w oryginalnej postaci; nie były uznawane za wiarygodne wyniki detekcji ACW.

Reguła 45 usuwa pozostałe spacje, gdy liczba spacji we wcięciu nie jest wielokrotnością czterech, co może zniszczyć strukturę bloków.

- [CodeContests/valid/12](codecontests/0009/acw/watermarked.py): expected an indented block after 'if' statement on line 144 (<unknown>, line 145)
- [CodeContests/valid/24](codecontests/0018/acw/watermarked.py): expected an indented block after 'for' statement on line 2 (<unknown>, line 3)
- [CodeContests/valid/72](codecontests/0055/acw/watermarked.py): expected an indented block after 'for' statement on line 3 (<unknown>, line 4)
- [CodeContests/valid/80](codecontests/0062/acw/watermarked.py): expected an indented block after 'for' statement on line 1 (<unknown>, line 2)
- [CodeContests/test/14](codecontests/0095/acw/watermarked.py): expected an indented block after 'for' statement on line 1 (<unknown>, line 2)
- [CodeContests/test/40](codecontests/0112/acw/watermarked.py): expected an indented block after class definition on line 6 (<unknown>, line 7)
- [CodeContests/test/46](codecontests/0116/acw/watermarked.py): expected an indented block after 'for' statement on line 1 (<unknown>, line 2)
- [CodeContests/test/100](codecontests/0151/acw/watermarked.py): expected an indented block after 'for' statement on line 1 (<unknown>, line 2)
- [CodeContests/test/134](codecontests/0173/acw/watermarked.py): expected an indented block after function definition on line 10 (<unknown>, line 11)
- [CodeContests/test/139](codecontests/0178/acw/watermarked.py): expected an indented block after 'for' statement on line 2 (<unknown>, line 3)
- [CodeContests/test/148](codecontests/0187/acw/watermarked.py): expected an indented block after 'for' statement on line 1 (<unknown>, line 2)

## Złożoność przed Ruffem

Porównanie metryk dla oryginałów i tych samych plików po znakowaniu: [złożoność przed i po](zlozonosc_przed_i_po.md).

Średnie obliczono ze skutecznie odczytanych wyników: złożoność cyklomatyczna Radona dla bloków, indeks utrzymywalności Radona dla plików oraz złożoność poznawcza Complexipy dla funkcji. W nawiasach podano liczby elementów, na których obliczono średnie.

| Zbiór | Metoda | Radon CC: średnia (liczba bloków) | Radon MI: średnia (liczba plików) | Complexipy: średnia (liczba funkcji) |
|---|---|---:|---:|---:|
| bigcodebench | SEW | 3.07 (1151) | 85.20 (1140) | 2.15 (1147) |
| bigcodebench | ACW | 3.07 (1151) | 85.40 (1140) | 2.02 (1147) |
| codecontests | SEW | 3.02 (810) | 58.05 (203) | 3.29 (745) |
| codecontests | ACW | 2.98 (789) | 57.73 (192) | 3.00 (727) |

## Status analiz

- ACW, ok: 1343.
- SEW, ok: 1343.

Complexipy zwraca kod 1 również po przekroczeniu progu złożoności; pełne wyjścia narzędzi, kody wyjścia oraz szczegóły poszczególnych funkcji znajdują się w katalogach próbek. Radon może wypisać błąd parsowania w JSON mimo kodu wyjścia 0.

[Wyniki maszynowe](results.json).
