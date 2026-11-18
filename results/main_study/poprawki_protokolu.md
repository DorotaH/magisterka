# Poprawki protokołu v2

Wszystkie poniższe decyzje pochodzą z protokołu v2 zatwierdzonego do wykonania 18 listopada 2026 r. Zostały podjęte przed znakowaniem nowej próby v2 i bez wglądu w jej wyniki znakowania. Stan zastany obejmuje wcześniejszy pilotaż CodeContests i ClassEval oraz profilowanie kandydatów.

| Nr | Data | Decyzja | Powód |
|---|---|---|---|
| 1 | 2026-11-18 | Główne zbiory to Mercury-eval, ClassEval i APPS test. BigCodeBench ≥ 15 SLOC i LeetCodeDataset test pozostają rozszerzeniami wymagającymi zgody. | Metody, klasy i dłuższe programy reprezentują trzy jednostki naturalnie występujące w danych. |
| 2 | 2026-11-18 | Kwalifikacja zależy od obecności funkcji lub metody. Raportujemy format wywołania jako cechę APPS. | W APPS jest 38 problemów call-based z rozwiązaniami, a wiele programów stdin zawiera funkcje. |
| 3 | 2026-11-18 | Liczność określamy po filtrach struktury, składni i SLOC. Minimalny SLOC wynosi 15 na jednostkę, a mediana pełnego zbioru ma charakter opisowy. Próg 100 traktujemy jako heurystykę i uwzględniamy 99 klas ClassEval. | Filtr stosujemy do faktycznego kodu poddanego znakowaniu. |
| 4 | 2026-11-18 | Wyniki testów stanowią osobną warstwę poprawności. Dobór do analizy statycznej odbywa się niezależnie od testów. | Zachowujemy kandydatów z błędami środowiska testowego lub testami zależnymi od daty. |
| 5 | 2026-11-18 | Skrypty APPS bez funkcji tworzą osobną warstwę. Raportujemy metryki raw i Complexipy na poziomie modułu, zachowując źródłowy układ kodu. | Opakowanie w funkcję zmienia wcięcie i zakres nazw, co ma znaczenie dla obu metod. |

Autorka zaakceptowała H1–H12 i marginesy równoważności przed pilotażem v2. Po przeglądzie reguły 36 potwierdziła użycie obu oryginalnych wariantów ACW oraz pomiar regresji.
