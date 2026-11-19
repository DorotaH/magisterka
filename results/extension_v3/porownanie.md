# Porównanie badania głównego i rozszerzenia

Δ oznacza średnią różnicę wariant minus oryginał w parach z pomiarem po obu stronach. Ruff check podano dla obu profili, a przeżywalność dla trybu `fix_format` wśród jednostek z wykrywalnym znakiem przed przetworzeniem. Różnice w obserwacji badania głównego pochodzą z dostępnych porównań różnicowych. Dla warstwy C mianownik ograniczono do oryginałów zaliczających test i wariantów z porównywalną obserwacją. Kreska oznacza brak oszacowania. Różnice śladów wynikające z odczytów zegara i potwierdzoną regresję ACW opisano w [kontrolach uzupełniających](warstwa_C/kontrola_zachowania.md).

| Próba | Wariant | Zmienione | Δ Ruff default | Δ Ruff strict | Δ CC | Δ Complexipy | Δ MI | Błędy składni | Różnice w obserwacji | Przeżywalność default | Przeżywalność strict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Badanie główne (n=1041) | SEW | 1038/1041 (99,7%) | 1,028 | 0,415 | -0,003 | 0,007 | 0,121 | 0/1041 (0,0%) | 1/1015 (0,1%) | 523/1019 (51,3%) | 598/1019 (58,7%) |
| Badanie główne (n=1041) | ACW bez reguły 45 | 1034/1041 (99,3%) | -0,169 | -1,199 | -0,058 | -0,482 | 0,415 | 3/1041 (0,3%) | 58/1015 (5,7%) | 864/905 (95,5%) | 690/905 (76,2%) |
| Badanie główne (n=1041) | Pełne ACW | 1040/1041 (99,9%) | -0,003 | 23,811 | -0,060 | -0,488 | 0,417 | 44/1041 (4,2%) | 99/1015 (9,8%) | 0/868 (0,0%) | 0/868 (0,0%) |
| ClassEval ludzki (n=99) | SEW | 98/99 (99,0%) | 0,970 | 0,242 | -0,006 | -0,020 | -0,353 | 0/99 (0,0%) | 0/93 (0,0%) | 34/95 (35,8%) | 34/95 (35,8%) |
| ClassEval ludzki (n=99) | ACW bez reguły 45 | 99/99 (100,0%) | -0,283 | -1,212 | -0,037 | -0,470 | 0,832 | 0/99 (0,0%) | 4/93 (4,3%) | 87/94 (92,6%) | 77/94 (81,9%) |
| ClassEval ludzki (n=99) | Pełne ACW | 99/99 (100,0%) | -0,283 | 30,172 | -0,037 | -0,470 | 0,832 | 0/99 (0,0%) | 5/93 (5,4%) | 0/94 (0,0%) | 0/94 (0,0%) |
| warstwa A · Łącznie (n=1615) | SEW | 1614/1615 (99,9%) | 0,505 | -0,012 | -0,003 | 0,002 | 0,189 | 0/1615 (0,0%) | — | 703/1604 (43,8%) | 748/1604 (46,6%) |
| warstwa A · Łącznie (n=1615) | ACW bez reguły 45 | 1587/1615 (98,3%) | -0,149 | -1,654 | -0,107 | -0,667 | 0,588 | 0/1615 (0,0%) | — | 1420/1446 (98,2%) | 1205/1446 (83,3%) |
| warstwa A · Łącznie (n=1615) | Pełne ACW | 1615/1615 (100,0%) | -0,063 | 22,320 | -0,110 | -0,679 | 0,602 | 60/1615 (3,7%) | — | 0/1389 (0,0%) | 0/1389 (0,0%) |
| warstwa C · Qwen (n=469) | SEW | 469/469 (100,0%) | 0,580 | -0,388 | 0,002 | 0,007 | -0,094 | 0/469 (0,0%) | 0/123 (0,0%) | 110/454 (24,2%) | 109/454 (24,0%) |
| warstwa C · Qwen (n=469) | ACW bez reguły 45 | 469/469 (100,0%) | -0,426 | -1,337 | -0,017 | -0,112 | -0,230 | 0/469 (0,0%) | 4/123 (3,3%) | 436/464 (94,0%) | 381/464 (82,1%) |
| warstwa C · Qwen (n=469) | Pełne ACW | 469/469 (100,0%) | -0,426 | 30,051 | -0,017 | -0,112 | -0,230 | 0/469 (0,0%) | 4/123 (3,3%) | 0/464 (0,0%) | 0/464 (0,0%) |
| warstwa C · Łącznie (n=924) | SEW | 920/924 (99,6%) | 0,544 | -0,337 | 0,000 | 0,004 | -0,100 | 0/924 (0,0%) | 1/206 (0,5%) | 218/887 (24,6%) | 230/887 (25,9%) |
| warstwa C · Łącznie (n=924) | ACW bez reguły 45 | 924/924 (100,0%) | -0,430 | -1,291 | -0,018 | -0,139 | -0,111 | 0/924 (0,0%) | 6/206 (2,9%) | 843/908 (92,8%) | 722/908 (79,5%) |
| warstwa C · Łącznie (n=924) | Pełne ACW | 924/924 (100,0%) | -0,430 | 32,129 | -0,018 | -0,139 | -0,111 | 0/924 (0,0%) | 6/206 (2,9%) | 0/908 (0,0%) | 0/908 (0,0%) |
| warstwa C · Llama (n=455) | SEW | 451/455 (99,1%) | 0,508 | -0,284 | -0,001 | 0,001 | -0,107 | 0/455 (0,0%) | 1/83 (1,2%) | 108/433 (24,9%) | 121/433 (27,9%) |
| warstwa C · Llama (n=455) | ACW bez reguły 45 | 455/455 (100,0%) | -0,433 | -1,244 | -0,020 | -0,167 | 0,012 | 0/455 (0,0%) | 2/83 (2,4%) | 407/444 (91,7%) | 341/444 (76,8%) |
| warstwa C · Llama (n=455) | Pełne ACW | 455/455 (100,0%) | -0,433 | 34,270 | -0,020 | -0,167 | 0,012 | 0/455 (0,0%) | 2/83 (2,4%) | 0/444 (0,0%) | 0/444 (0,0%) |
