# Podsumowanie badania v2

| Zbiór | Warstwa | Wariant | Pomiarów | Kod zmieniony | Błąd składni | Testowano | Wynik różny | Oryginał i wariant zaliczają |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Mercury-eval | main | sew | 20 | 20 | 0 | 20 | 0 | 18 |
| Mercury-eval | main | acw_notab | 20 | 20 | 0 | 20 | 3 | 16 |
| Mercury-eval | main | acw_full | 20 | 20 | 0 | 20 | 3 | 16 |
| ClassEval | main | sew | 20 | 20 | 0 | 20 | 0 | 19 |
| ClassEval | main | acw_notab | 20 | 20 | 0 | 20 | 0 | 19 |
| ClassEval | main | acw_full | 20 | 20 | 0 | 20 | 0 | 19 |
| APPS | main | sew | 20 | 20 | 0 | 20 | 0 | 17 |
| APPS | main | acw_notab | 20 | 20 | 0 | 20 | 0 | 17 |
| APPS | main | acw_full | 20 | 20 | 1 | 20 | 1 | 17 |

„Testowano” uwzględnia próby uruchomienia. Statusy techniczne i mianowniki porównań zapisano w `correctness_v2/result.json` i `summary/proportions.csv`.

Porównania metryk, efekty, przedziały, TOST i korekty zapisano w [paired.csv](summary/paired.csv). Zanik znaku i kontrole punktu stałego zawiera [proportions.csv](summary/proportions.csv).

### Pierwszy etap z błędem składni

- APPS, `rule_45`: 1.

Identyfikatory i komunikaty zawierają pliki `summary/syntax_*.csv`.
