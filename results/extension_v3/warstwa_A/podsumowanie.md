# Podsumowanie

| Próba | Wariant | Zmienione | Δ Ruff default | Δ Ruff strict | Δ CC | Δ Complexipy | Δ MI | Błędy składni | Różnice w obserwacji | Przeżywalność default | Przeżywalność strict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mercury-train | SEW | 1491/1492 (99,9%) | 0,492 | -0,083 | -0,003 | -0,003 | 0,184 | 0/1492 (0,0%) | — | 642/1481 (43,3%) | 680/1481 (45,9%) |
| Mercury-train | ACW bez reguły 45 | 1489/1492 (99,8%) | -0,158 | -1,798 | -0,114 | -0,713 | 0,639 | 0/1492 (0,0%) | — | 1304/1324 (98,5%) | 1105/1324 (83,5%) |
| Mercury-train | Pełne ACW | 1492/1492 (100,0%) | -0,145 | 21,914 | -0,115 | -0,708 | 0,637 | 14/1492 (0,9%) | — | 0/1313 (0,0%) | 0/1313 (0,0%) |
| Łącznie | SEW | 1614/1615 (99,9%) | 0,505 | -0,012 | -0,003 | 0,002 | 0,189 | 0/1615 (0,0%) | — | 703/1604 (43,8%) | 748/1604 (46,6%) |
| Łącznie | ACW bez reguły 45 | 1587/1615 (98,3%) | -0,149 | -1,654 | -0,107 | -0,667 | 0,588 | 0/1615 (0,0%) | — | 1420/1446 (98,2%) | 1205/1446 (83,3%) |
| Łącznie | Pełne ACW | 1615/1615 (100,0%) | -0,063 | 22,320 | -0,110 | -0,679 | 0,602 | 60/1615 (3,7%) | — | 0/1389 (0,0%) | 0/1389 (0,0%) |
| LeetCodeDataset test | SEW | 123/123 (100,0%) | 0,659 | 0,854 | -0,008 | 0,064 | 0,241 | 0/123 (0,0%) | — | 61/123 (49,6%) | 68/123 (55,3%) |
| LeetCodeDataset test | ACW bez reguły 45 | 98/123 (79,7%) | -0,041 | 0,089 | -0,017 | -0,115 | -0,038 | 0/123 (0,0%) | — | 116/122 (95,1%) | 100/122 (82,0%) |
| LeetCodeDataset test | Pełne ACW | 123/123 (100,0%) | 0,935 | 27,236 | -0,019 | -0,117 | -0,069 | 46/123 (37,4%) | — | 0/76 (0,0%) | 0/76 (0,0%) |

Przeżywalność dotyczy trybu `fix_format` i próbek wykrywalnych po znakowaniu. Δ oznacza średnią zmianę w parze. Pełne mianowniki, przedziały i wyniki wszystkich trybów są w [tabelach CSV](summary/).
