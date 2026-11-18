# Przegląd semantyki reguł ACW

| Reguła | Operacja | Przypadki wymagające kontroli |
|---|---|---|
| 36 | Zamienia miejscami operandy `+` na podstawie skrótu ich zapisu. | Konkatenuje napisy i listy w odwrotnej kolejności, może zmienić wywołania operatorów przeciążonych i kolejność efektów ubocznych. |
| 37 | Zamienia miejscami operandy `*` według analogicznego porządku. | Operatory przeciążone oraz efekty uboczne przy obliczaniu operandów. |
| 38 | Zamienia operandy pojedynczego porównania `<` / `>` i odwraca operator. | Kolejność obliczania operandów i niestandardowe metody porównań. |
| 39 | Analogiczna zamiana dla `<=` / `>=`. | Kolejność obliczania operandów i niestandardowe metody porównań. |
| 45 | Zastępuje wiodące spacje przez tabulatory, dzieląc liczbę spacji całkowicie przez 4. | Reszta 1–3 spacji jest gubiona. Może to zmienić granice bloków oraz treść wielowierszowych napisów. |

Reguły 36–39 analizują składnię CST, bez sprawdzania typów w czasie wykonania. Reguły porównań pomijają porównania łańcuchowe. Wśród reguł Sourcery sprawdzimy w szczególności przekształcenia warunków i wyrażeń boolowskich pod kątem kolejności oraz krótkiego spięcia. Sama nazwa reguły nie wystarcza do stwierdzenia zmiany zachowania.

## Odtworzony przypadek kontrolny

W kopii lokalnej oryginalna funkcja `transform_operations_add` zmieniła ciało `return b + a` na `return a + b`. Dla argumentów `("A", "B")` wynik zmienił się z `"BA"` na `"AB"`, a dla `([1], [2])` z `[2, 1]` na `[1, 2]`. Oba pliki były poprawne składniowo. To potwierdza możliwość zmiany działania w samej regule 36, wspólnej dla `acw_full` i `acw_notab`.

W starszym pilotażu ClassEval_15 reguła 36 zamieniła `currentPos + i` na `i + currentPos` podczas obliczania indeksu. Testy tej klasy przeszły w obu wersjach. Przykład pokazuje wystąpienie transformacji w danych pilotażowych. [Log próbki](pilot_classeval/classeval/0015/acw/acw_local.log)

Źródła [reguł 36–39](../../ACW/source/base_ast.py) i [reguły 45](../../ACW/source/one_rule_format.py).

## Przypadki w pilotażu v2

- Mercury `reverse-words-in-a-string`. Reguła 36 zamieniła `p+k[i]` na `k[i]+p` oraz przestawiła składniki konkatenacji ze spacją w drugiej gałęzi. Wersja oryginalna i SEW przeszły oceniane testy oficjalne. Obie wersje ACW zwróciły inne wyniki. [Log transformacji](pilot_v2/mercury_eval/reverse-words-in-a-string/acw_steps/local.log)
- Mercury `integer-to-english-words`. Zmiany kolejności składników napisów wystąpiły w przekształceniach ACW, a obie wersje ACW nie przeszły ocenianych testów oryginału. [Log transformacji](pilot_v2/mercury_eval/integer-to-english-words/acw_steps/local.log)
- APPS `1062`. Reguła 36 zamieniła `cans + sc` na `sc + cans` w instrukcji `print`. Wybrane wejścia nie ujawniły różnicy w wyjściu. Przypadek ilustruje granice obserwacji w podzbiorze testów. [Log transformacji](pilot_v2/apps/1062/acw_steps/local.log)

Kontrolne odtworzenie na zapisanych testach oficjalnych izoluje wkład reguły 36. Wejścia były identyczne przed i po zastosowaniu reguły. Wynik różnił się w 8/8 uruchomień `reverse-words-in-a-string` i 7/8 uruchomień `integer-to-english-words`. [Odtworzenie, odwracanie słów](pilot_v2/mercury_eval/reverse-words-in-a-string/rule36_audit/result.json) · [Odtworzenie, zapis liczby](pilot_v2/mercury_eval/integer-to-english-words/rule36_audit/result.json)

## Błędy składni powstałe przed regułą 45

W APPS `3833` i `3903` pierwszym niepoprawnym składniowo stanem jest zapis po Sourcery. W pierwszym pliku poziom dedentu nie odpowiada żadnemu zewnętrznemu blokowi. W drugim parser zgłasza mieszanie spacji z tabulatorami w bloku. Błędy są obecne również w `acw_notab`. Późniejszy krok reguły 45 zmienia osobny wariant. [Stan APPS 3833 po Sourcery](apps/3833/after_sourcery.py) · [Stan APPS 3903 po Sourcery](apps/3903/after_sourcery.py)
