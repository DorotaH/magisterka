# Podsumowanie badania v2

| Zbiór | Warstwa | Wariant | Pomiarów | Kod zmieniony | Błąd składni | Testowano | Wynik różny | Oryginał i wariant zaliczają |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Mercury-eval | main | sew | 242 | 240 | 0 | 242 | 0 | 238 |
| Mercury-eval | main | acw_notab | 242 | 239 | 0 | 242 | 17 | 223 |
| Mercury-eval | main | acw_full | 242 | 242 | 6 | 242 | 23 | 217 |
| ClassEval | main | sew | 99 | 98 | 0 | 99 | 0 | 89 |
| ClassEval | main | acw_notab | 99 | 99 | 0 | 99 | 4 | 85 |
| ClassEval | main | acw_full | 99 | 99 | 0 | 99 | 5 | 85 |
| APPS | main | sew | 600 | 600 | 0 | 600 | 1 | 518 |
| APPS | main | acw_notab | 600 | 598 | 3 | 600 | 28 | 499 |
| APPS | main | acw_full | 600 | 600 | 33 | 600 | 57 | 472 |
| APPS | script | sew | 100 | 100 | 0 | 100 | 0 | 89 |
| APPS | script | acw_notab | 100 | 98 | 0 | 100 | 9 | 80 |
| APPS | script | acw_full | 100 | 99 | 5 | 100 | 14 | 75 |

„Testowano” uwzględnia próby uruchomienia. Statusy techniczne i mianowniki porównań zapisano w `correctness_v2/result.json` i `summary/proportions.csv`.

Porównania metryk, efekty, przedziały, TOST i korekty zapisano w [paired.csv](summary/paired.csv). Zanik znaku i kontrole punktu stałego zawiera [proportions.csv](summary/proportions.csv).

### Pierwszy etap z błędem składni

- APPS, `rule_45`: 35.
- APPS, `sourcery`: 3.
- Mercury-eval, `rule_45`: 6.

Identyfikatory i komunikaty zawierają pliki `summary/syntax_*.csv`.
