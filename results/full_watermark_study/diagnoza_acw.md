# Diagnoza błędów składni ACW

W pliku `ACW/source/one_rule_format.py` funkcja `tab_convert_process` oblicza `leading_spaces // 4` tabulatorów i dokleja `line.lstrip(' ')`. W ten sposób usuwa także resztę 1–3 spacji, co zmniejsza wcięcie, jeśli nie jest ono wielokrotnością czterech.

Sprawdzono 11 plików z błędami składni: ponownie zastosowano cztery funkcje CST z `base_ast.py` oraz pięć grup autopep8 do plików po etapie Sourcery, bez uruchamiania reguły tabulatorów. Wszystkie 11 plików przechodziły `ast.parse` przed regułą 45. Po wykonaniu pełnego łańcucha występował błąd składni. Poszczególne identyfikatory i komunikaty są w [podsumowaniu](podsumowanie.md), a kod oryginalny i oznakowany w katalogach próbek.

Drugą usterką repozytorium jest to, że `reorder_process` wywołuje funkcje z `base_ast.py` z czterema argumentami, chociaż przyjmują jedną ścieżkę. W eksperymencie użyto bezpośrednich wywołań tych funkcji. Żadnej z powyższych usterek nie poprawiano w źródłach ACW; pierwszą zachowano w przebiegu i zmierzono jej skutki.
