# Wykrywalność przed i po Ruffie

Wykrycie SEW oznacza oficjalny werdykt, przy alpha=0,01 i minimum 5 niezależnych obserwacji. ACW oznacza dokładną identyczność bajtów po ponownym zastosowaniu zapisanej konfiguracji.

Każdy profil Ruffa zaczyna od tej samej wersji wejściowej. Profile nie są nakładane kolejno.

| Kod / detektor | Etap | Wykryte / ocenione | Brak wyniku | W poprawnym kodzie | Za mało danych SEW | 95% Wilson |
|---|---|---|---|---|---|---|
| acw/acw | Przed Ruffem | 552/974 | 0 | 542/577 | 0 | [53.54%, 59.75%] |
| acw/acw | Tylko formatter | 0/577 | 397 | 0/577 | 0 | [0.00%, 0.66%] |
| acw/acw | Domyślny linter, bez formattera | 556/974 | 0 | 546/577 | 0 | [53.95%, 60.16%] |
| acw/acw | Prefiksy repo-max, bez formattera | 506/974 | 0 | 496/577 | 0 | [48.81%, 55.07%] |
| acw/acw | ALL + formatter | 0/577 | 397 | 0/577 | 0 | [0.00%, 0.66%] |
| original/acw | Przed Ruffem | 0/974 | 0 | 0/974 | 0 | [0.00%, 0.39%] |
| original/acw | Tylko formatter | 0/974 | 0 | 0/974 | 0 | [0.00%, 0.39%] |
| original/acw | Domyślny linter, bez formattera | 0/974 | 0 | 0/974 | 0 | [0.00%, 0.39%] |
| original/acw | Prefiksy repo-max, bez formattera | 0/974 | 0 | 0/974 | 0 | [0.00%, 0.39%] |
| original/acw | ALL + formatter | 0/974 | 0 | 0/974 | 0 | [0.00%, 0.39%] |
| original/sew | Przed Ruffem | 3/974 | 0 | 3/974 | 212 | [0.10%, 0.90%] |
| original/sew | Tylko formatter | 3/974 | 0 | 3/974 | 219 | [0.10%, 0.90%] |
| original/sew | Domyślny linter, bez formattera | 2/974 | 0 | 2/974 | 215 | [0.06%, 0.75%] |
| original/sew | Prefiksy repo-max, bez formattera | 3/974 | 0 | 3/974 | 214 | [0.10%, 0.90%] |
| original/sew | ALL + formatter | 3/974 | 0 | 3/974 | 170 | [0.10%, 0.90%] |
| sew/sew | Przed Ruffem | 708/974 | 0 | 708/974 | 214 | [69.81%, 75.39%] |
| sew/sew | Tylko formatter | 136/974 | 0 | 136/974 | 221 | [11.93%, 16.28%] |
| sew/sew | Domyślny linter, bez formattera | 652/974 | 0 | 652/974 | 217 | [63.92%, 69.82%] |
| sew/sew | Prefiksy repo-max, bez formattera | 648/974 | 0 | 648/974 | 215 | [63.51%, 69.42%] |
| sew/sew | ALL + formatter | 65/974 | 0 | 65/974 | 172 | [5.27%, 8.42%] |

## Zmiany dla tych samych zadań

| Kod / detektor | Etap | Utrzymane | Utracone | Nowe | Brak w obu | Brak porównania |
|---|---|---|---|---|---|---|
| acw/acw | Tylko formatter | 0 | 542 | 0 | 35 | 397 |
| acw/acw | Domyślny linter, bez formattera | 552 | 0 | 4 | 418 | 0 |
| acw/acw | Prefiksy repo-max, bez formattera | 502 | 50 | 4 | 418 | 0 |
| acw/acw | ALL + formatter | 0 | 542 | 0 | 35 | 397 |
| original/acw | Tylko formatter | 0 | 0 | 0 | 974 | 0 |
| original/acw | Domyślny linter, bez formattera | 0 | 0 | 0 | 974 | 0 |
| original/acw | Prefiksy repo-max, bez formattera | 0 | 0 | 0 | 974 | 0 |
| original/acw | ALL + formatter | 0 | 0 | 0 | 974 | 0 |
| original/sew | Tylko formatter | 1 | 2 | 2 | 969 | 0 |
| original/sew | Domyślny linter, bez formattera | 2 | 1 | 0 | 971 | 0 |
| original/sew | Prefiksy repo-max, bez formattera | 3 | 0 | 0 | 971 | 0 |
| original/sew | ALL + formatter | 0 | 3 | 3 | 968 | 0 |
| sew/sew | Tylko formatter | 136 | 572 | 0 | 266 | 0 |
| sew/sew | Domyślny linter, bez formattera | 652 | 56 | 0 | 266 | 0 |
| sew/sew | Prefiksy repo-max, bez formattera | 648 | 60 | 0 | 266 | 0 |
| sew/sew | ALL + formatter | 65 | 643 | 0 | 266 | 0 |

## Ograniczenia i ważne rozróżnienia

- Brak wyniku po odmowie Ruffa nie oznacza negatywnej detekcji. Takie rekordy mają detected=NULL.
- Surowe liczby ACW przed Ruffem i po samym linterze obejmują także błędny składniowo kod. Osobne kolumny pokazują wynik w poprawnym podzbiorze. Samo wykrycie nie potwierdza użyteczności programu.
- Liczba wykryć w kontrolach może być taka sama przed i po, mimo że dotyczą innych zadań. Dlatego zapisano pełne przejścia, nie tylko sumy.
- Minimum dowodu w SEW jest częścią oficjalnej decyzji. Poprzednie 908 wynikające z samego p<0,01 nie jest liczbą poprawnych wykryć; prawidłowy licznik bazowy to 708.
- Przedziały Wilsona mają modelowe założenie obserwacji Bernoulliego. To jeden benchmark i jeden klucz; wyniki nie są oceną uniwersalnej skuteczności.
- Repo-max stosuje prefiksy aktualnego repozytorium na przypiętej wersji Ruffa. Nie udajemy identycznego historycznego zestawu 369 reguł z publikacji.

Wszystkie rekordy i p-value: [exports/detections.csv](exports/detections.csv). Przejścia: [exports/detection_transitions.csv](exports/detection_transitions.csv).
