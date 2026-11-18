# Ręczna kontrola pięciu próbek

Z zakończonego pilotażu wylosowano bez zwracania 2 jednostki Mercury, 1 ClassEval i 2 APPS, seed 20261118. Dla każdej porównano kod oryginalny z wariantami i zestawiono wynik z oceną składni. Niezależna kontrola integralności losuje próbki z pełnego przebiegu i zapisuje SHA-256 w `validation.json`.

| Zbiór i próbka | Obserwacja w różnicy |
|---|---|
| Mercury `evaluate-reverse-polish-notation` | SEW zmienił formatowanie i przestawił argumenty mnożenia wewnątrz lambdy używanej dla liczb. W ACW bez tabulatorów odwrócono porównanie pętli. Pełne ACW zmieniło także wcięcia. |
| Mercury `interleaving-string` | SEW zmienił m.in. pusty literał słownika na `dict()`. ACW bez tabulatorów zmienił odstępy indeksów i porównania, a reguła 45 zmieniła wcięcia metod i funkcji zagnieżdżonej. |
| ClassEval `ClassEval_22` | Widać wpływ Sourcery na usunięcie `else` po wcześniejszym `return`. SEW zmienił odstępy i zapis inicjalizacji listy. |
| APPS `1062` | SEW połączył dwa odczyty wejścia w jedno przypisanie. ACW zamienił operandy konkatenacji w funkcji pomocniczej. |
| APPS `1025` | Oryginał importuje `gcd` z `fractions`. Składnia jest poprawna. W Pythonie 3.14 błąd importu może uniemożliwić ocenę działania, mimo że plik nadal podlega analizie statycznej. |

## Pełny przebieg

Pięć plików wylosowano z manifestów pełnego badania tym samym ziarnem, przy porządku zbiorów Mercury, ClassEval, APPS i leksykograficznym porządku identyfikatorów w każdym zbiorze. Obejrzano różnice kodu, statusy składni i wskazane wyniki detekcji.

| Zbiór i próbka | Obserwacja w różnicy |
|---|---|
| APPS `1358` | SEW zmienił odstępy. Reguła 36 przestawiła wyrażenie `res + center` w ACW. Sam format Ruffa zmienił werdykt SEW, podczas gdy sama naprawa zachowała wykrycie. |
| APPS `2572` | Skrypt bez funkcji. SEW połączył przypisania `arr` i `res`. Pełne ACW wprowadziło tabulatory w zagnieżdżonych blokach. Trzy warianty zachowały składnię. |
| Mercury `reaching-points` | SEW połączył przypisania dwóch krotek i odwrócił porównanie. W ACW bez tabulatorów widać znormalizowane odstępy i porównania. Wykrycie SEW przetrwało osobne tryby naprawy i formatu. |
| Mercury `isomorphic-strings` | SEW i ACW bez tabulatorów nie zmieniły kodu. Pełne ACW zmieniło wcięcia. SEW po próbie osadzenia zwrócił brak dowodu znaku. |
| Mercury `contains-duplicate` | SEW zmienił odstępy w czterech liniach, a ACW bez tabulatorów dodało puste linie. Wykrycie SEW zanikło po samym formacie. |
