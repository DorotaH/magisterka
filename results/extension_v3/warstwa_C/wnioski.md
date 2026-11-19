# Wnioski eksploracyjne

Porównania dotyczą wyłącznie opisanych zbiorów i zastosowanego potoku. Brak odnotowanej różnicy oznacza brak zdarzeń w danym mianowniku.

- SEW zmienił 920/924 (99,6%) próbek. Błędy składni wystąpiły w 0/924 (0,0%), a przeżywalność po Ruff strict w trybie `fix_format` wyniosła 230/887 (25,9%). Różny ślad testowy odnotowano w 1/206 (0,5%).

- ACW bez reguły 45 zmienił 924/924 (100,0%) próbek. Błędy składni wystąpiły w 0/924 (0,0%), a przeżywalność po Ruff strict w trybie `fix_format` wyniosła 722/908 (79,5%). Różny ślad testowy odnotowano w 6/206 (2,9%).

- Pełne ACW zmienił 924/924 (100,0%) próbek. Błędy składni wystąpiły w 0/924 (0,0%), a przeżywalność po Ruff strict w trybie `fix_format` wyniosła 0/908 (0,0%). Różny ślad testowy odnotowano w 6/206 (2,9%).

Kontrola przy wspólnym czasie wyjaśniła różnice widoczne dla TimeUtils. Dla SQLQueryBuilder odtworzono regresję ACW po regule 36. [Wyniki kontroli](kontrola_zachowania.md)
