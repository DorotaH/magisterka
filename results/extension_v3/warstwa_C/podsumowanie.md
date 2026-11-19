# Podsumowanie

| Próba | Wariant | Zmienione | Δ Ruff default | Δ Ruff strict | Δ CC | Δ Complexipy | Δ MI | Błędy składni | Różnice w obserwacji | Przeżywalność default | Przeżywalność strict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Qwen | SEW | 469/469 (100,0%) | 0,580 | -0,388 | 0,002 | 0,007 | -0,094 | 0/469 (0,0%) | 0/123 (0,0%) | 110/454 (24,2%) | 109/454 (24,0%) |
| Qwen | ACW bez reguły 45 | 469/469 (100,0%) | -0,426 | -1,337 | -0,017 | -0,112 | -0,230 | 0/469 (0,0%) | 4/123 (3,3%) | 436/464 (94,0%) | 381/464 (82,1%) |
| Qwen | Pełne ACW | 469/469 (100,0%) | -0,426 | 30,051 | -0,017 | -0,112 | -0,230 | 0/469 (0,0%) | 4/123 (3,3%) | 0/464 (0,0%) | 0/464 (0,0%) |
| Łącznie | SEW | 920/924 (99,6%) | 0,544 | -0,337 | 0,000 | 0,004 | -0,100 | 0/924 (0,0%) | 1/206 (0,5%) | 218/887 (24,6%) | 230/887 (25,9%) |
| Łącznie | ACW bez reguły 45 | 924/924 (100,0%) | -0,430 | -1,291 | -0,018 | -0,139 | -0,111 | 0/924 (0,0%) | 6/206 (2,9%) | 843/908 (92,8%) | 722/908 (79,5%) |
| Łącznie | Pełne ACW | 924/924 (100,0%) | -0,430 | 32,129 | -0,018 | -0,139 | -0,111 | 0/924 (0,0%) | 6/206 (2,9%) | 0/908 (0,0%) | 0/908 (0,0%) |
| Llama | SEW | 451/455 (99,1%) | 0,508 | -0,284 | -0,001 | 0,001 | -0,107 | 0/455 (0,0%) | 1/83 (1,2%) | 108/433 (24,9%) | 121/433 (27,9%) |
| Llama | ACW bez reguły 45 | 455/455 (100,0%) | -0,433 | -1,244 | -0,020 | -0,167 | 0,012 | 0/455 (0,0%) | 2/83 (2,4%) | 407/444 (91,7%) | 341/444 (76,8%) |
| Llama | Pełne ACW | 455/455 (100,0%) | -0,433 | 34,270 | -0,020 | -0,167 | 0,012 | 0/455 (0,0%) | 2/83 (2,4%) | 0/444 (0,0%) | 0/444 (0,0%) |

## Poprawność oryginałów

- Qwen, zaliczenie testów przez oryginał 123/469 (26,2%).
- Łącznie, zaliczenie testów przez oryginał 206/924 (22,3%).
- Llama, zaliczenie testów przez oryginał 83/455 (18,2%).

Przeżywalność dotyczy trybu `fix_format` i próbek wykrywalnych po znakowaniu. Δ oznacza średnią zmianę w parze. Pełne mianowniki, przedziały i wyniki wszystkich trybów są w [tabelach CSV](summary/).

Porównania zachowania obejmują ślady zależne od zegara. [Kontrole uzupełniające](kontrola_zachowania.md) wyjaśniają różnice czasowe i potwierdzają regresję ACW.
