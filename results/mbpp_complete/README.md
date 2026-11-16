# Wyniki MBPP — ACW i SEW

20 zadań referencyjnych MBPP (ID 1–20), każde w trzech wersjach:
`original/`, `acw/`, `sew/`. `code_pairs.jsonl` zawiera 40 rekordów:
opis zadania, kod przed i po, testy (nieuruchomione), detekcję i walidację składni.

Sourcery 1.33.0; konfiguracja reguł ACW zrekonstruowana z refact_list.
W adapterze naprawiono niezgodne wywołanie reguł 36–39; transformacje upstream
pozostawiono bez zmian. W SEW użyto publicznego klucza eksperymentalnego.

Wszystkie 40 transformacji zmieniło kod. Detekcja: ACW 11/20, SEW 19/20;
są to surowe wyniki detektorów, również dla kodu z błędną składnią.
ACW wygenerowało 8 plików z niepoprawną składnią. Nie poprawiano wyników
ręcznie. ID: 2, 4, 7, 8, 10, 13, 15, 17.
Reguła 45 upstream zamienia wcięcia na tabulatory, usuwając resztę z dzielenia
liczby spacji przez 4; w kodzie z wcięciem dwuspacjowym usuwa to wcięcie.

Raport jakości: `../quality_complete/report.md`.
Metryki obliczono dla 12 poprawnych składniowo par ACW i 20 par SEW.
Błędy są jawnie zapisane w `../quality_complete/pairs.jsonl`.
Nie uruchamiano testów poprawności funkcjonalnej.
