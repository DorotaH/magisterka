# Wpływ watermarkowania na statyczne metryki jakości

Zbiór: 974 zadań referencyjnych MBPP. Delta = oznakowany kod minus oryginał.

Wyniki dotyczą zapisanej implementacji i konfiguracji. Nie są pełną replikacją publikacji. Nie uruchamiano testów funkcjonalnych.

## Kompletność pomiarów

| Kod | Etap | Narzędzie | Status | Liczba |
|---|---|---|---|---|
| acw | Przed Ruffem | complexipy | ok | 577 |
| acw | Przed Ruffem | complexipy | syntax_error | 397 |
| acw | Przed Ruffem | radon | ok | 577 |
| acw | Przed Ruffem | radon | syntax_error | 397 |
| acw | Przed Ruffem | ruff | ok | 577 |
| acw | Przed Ruffem | ruff | syntax_error | 397 |
| acw | Tylko formatter | complexipy | ok | 577 |
| acw | Tylko formatter | complexipy | preprocessing_error | 397 |
| acw | Tylko formatter | radon | ok | 577 |
| acw | Tylko formatter | radon | preprocessing_error | 397 |
| acw | Tylko formatter | ruff | ok | 577 |
| acw | Tylko formatter | ruff | preprocessing_error | 397 |
| acw | Domyślny linter, bez formattera | complexipy | ok | 577 |
| acw | Domyślny linter, bez formattera | complexipy | syntax_error | 397 |
| acw | Domyślny linter, bez formattera | radon | ok | 577 |
| acw | Domyślny linter, bez formattera | radon | syntax_error | 397 |
| acw | Domyślny linter, bez formattera | ruff | ok | 577 |
| acw | Domyślny linter, bez formattera | ruff | syntax_error | 397 |
| acw | Prefiksy repo-max, bez formattera | complexipy | ok | 577 |
| acw | Prefiksy repo-max, bez formattera | complexipy | syntax_error | 397 |
| acw | Prefiksy repo-max, bez formattera | radon | ok | 577 |
| acw | Prefiksy repo-max, bez formattera | radon | syntax_error | 397 |
| acw | Prefiksy repo-max, bez formattera | ruff | ok | 577 |
| acw | Prefiksy repo-max, bez formattera | ruff | syntax_error | 397 |
| acw | ALL + formatter | complexipy | ok | 577 |
| acw | ALL + formatter | complexipy | preprocessing_error | 397 |
| acw | ALL + formatter | radon | ok | 577 |
| acw | ALL + formatter | radon | preprocessing_error | 397 |
| acw | ALL + formatter | ruff | ok | 577 |
| acw | ALL + formatter | ruff | preprocessing_error | 397 |
| original | Przed Ruffem | complexipy | ok | 974 |
| original | Przed Ruffem | radon | ok | 974 |
| original | Przed Ruffem | ruff | ok | 974 |
| original | Tylko formatter | complexipy | ok | 974 |
| original | Tylko formatter | radon | ok | 974 |
| original | Tylko formatter | ruff | ok | 974 |
| original | Domyślny linter, bez formattera | complexipy | ok | 974 |
| original | Domyślny linter, bez formattera | radon | ok | 974 |
| original | Domyślny linter, bez formattera | ruff | ok | 974 |
| original | Prefiksy repo-max, bez formattera | complexipy | ok | 974 |
| original | Prefiksy repo-max, bez formattera | radon | ok | 974 |
| original | Prefiksy repo-max, bez formattera | ruff | ok | 974 |
| original | ALL + formatter | complexipy | ok | 974 |
| original | ALL + formatter | radon | ok | 974 |
| original | ALL + formatter | ruff | ok | 974 |
| sew | Przed Ruffem | complexipy | ok | 974 |
| sew | Przed Ruffem | radon | ok | 974 |
| sew | Przed Ruffem | ruff | ok | 974 |
| sew | Tylko formatter | complexipy | ok | 974 |
| sew | Tylko formatter | radon | ok | 974 |
| sew | Tylko formatter | ruff | ok | 974 |
| sew | Domyślny linter, bez formattera | complexipy | ok | 974 |
| sew | Domyślny linter, bez formattera | radon | ok | 974 |
| sew | Domyślny linter, bez formattera | ruff | ok | 974 |
| sew | Prefiksy repo-max, bez formattera | complexipy | ok | 974 |
| sew | Prefiksy repo-max, bez formattera | radon | ok | 974 |
| sew | Prefiksy repo-max, bez formattera | ruff | ok | 974 |
| sew | ALL + formatter | complexipy | ok | 974 |
| sew | ALL + formatter | radon | ok | 974 |
| sew | ALL + formatter | ruff | ok | 974 |

## Wszystkie dostępne poprawne pary: przed Ruffem

Każda średnia „przed” i „po” dotyczy tych samych zadań. Kohorta wspólna wymaga dostępnego pomiaru danej metryki dla obu metod.

| Metoda | Metryka | n | Średnia przed | Średnia po | Średnia delta | 95% CI średniej delty | Spadek / bez zmian / wzrost |
|---|---|---|---|---|---|---|---|
| acw | ruff/default.violations | 577 | 0.4107 | 0.2461 | -0.1646 | [-0.1993, -0.1317] | 93/481/3 |
| sew | ruff/default.violations | 974 | 0.4456 | 0.5688 | 0.1232 | [0.0903, 0.1571] | 23/847/104 |
| acw | ruff/all.violations | 577 | 14.8354 | 16.0659 | 1.2305 | [0.7730, 1.7054] | 268/49/260 |
| sew | ruff/all.violations | 974 | 12.6776 | 12.3881 | -0.2895 | [-0.3460, -0.2310] | 412/458/104 |
| acw | complexipy/functions_total | 577 | 3.1092 | 2.6135 | -0.4957 | [-0.5823, -0.4125] | 145/432/0 |
| sew | complexipy/functions_total | 974 | 2.4097 | 2.4343 | 0.0246 | [0.0062, 0.0431] | 9/941/24 |
| acw | complexipy/total | 577 | 3.1092 | 2.6135 | -0.4957 | [-0.5789, -0.4159] | 145/432/0 |
| sew | complexipy/total | 974 | 2.4097 | 2.4343 | 0.0246 | [0.0072, 0.0441] | 9/941/24 |
| acw | radon/cc.function_total | 577 | 3.4055 | 3.2530 | -0.1525 | [-0.1958, -0.1161] | 76/501/0 |
| sew | radon/cc.function_total | 974 | 2.9384 | 2.9415 | 0.0031 | [-0.0031, 0.0123] | 1/972/1 |
| acw | radon/mi | 577 | 74.7788 | 76.3738 | 1.5949 | [1.3408, 1.8674] | 12/383/182 |
| sew | radon/mi | 974 | 78.7803 | 78.1674 | -0.6129 | [-0.8340, -0.4119] | 133/782/59 |
| acw | radon/raw.sloc | 577 | 7.7470 | 6.8475 | -0.8995 | [-1.0191, -0.7833] | 223/352/2 |
| sew | radon/raw.sloc | 974 | 6.6756 | 6.6499 | -0.0257 | [-0.0575, 0.0072] | 52/896/26 |
| acw | radon/halstead.volume | 577 | 57.3905 | 55.1651 | -2.2254 | [-3.4988, -1.2754] | 63/495/19 |
| sew | radon/halstead.volume | 974 | 42.5037 | 43.5496 | 1.0460 | [0.7139, 1.4304] | 13/842/119 |

## Wspólne zadania ACW i SEW: przed Ruffem

Każda średnia „przed” i „po” dotyczy tych samych zadań. Kohorta wspólna wymaga dostępnego pomiaru danej metryki dla obu metod.

| Metoda | Metryka | n | Średnia przed | Średnia po | Średnia delta | 95% CI średniej delty | Spadek / bez zmian / wzrost |
|---|---|---|---|---|---|---|---|
| acw | ruff/default.violations | 577 | 0.4107 | 0.2461 | -0.1646 | [-0.1993, -0.1317] | 93/481/3 |
| sew | ruff/default.violations | 577 | 0.4107 | 0.5806 | 0.1698 | [0.1196, 0.2218] | 19/474/84 |
| acw | ruff/all.violations | 577 | 14.8354 | 16.0659 | 1.2305 | [0.7730, 1.7054] | 268/49/260 |
| sew | ruff/all.violations | 577 | 14.8354 | 14.5598 | -0.2756 | [-0.3536, -0.1976] | 255/237/85 |
| acw | complexipy/functions_total | 577 | 3.1092 | 2.6135 | -0.4957 | [-0.5823, -0.4125] | 145/432/0 |
| sew | complexipy/functions_total | 577 | 3.1092 | 3.1282 | 0.0191 | [0.0000, 0.0399] | 6/558/13 |
| acw | complexipy/total | 577 | 3.1092 | 2.6135 | -0.4957 | [-0.5789, -0.4159] | 145/432/0 |
| sew | complexipy/total | 577 | 3.1092 | 3.1282 | 0.0191 | [0.0000, 0.0399] | 6/558/13 |
| acw | radon/cc.function_total | 577 | 3.4055 | 3.2530 | -0.1525 | [-0.1958, -0.1161] | 76/501/0 |
| sew | radon/cc.function_total | 577 | 3.4055 | 3.4038 | -0.0017 | [-0.0052, 0.0000] | 1/576/0 |
| acw | radon/mi | 577 | 74.7788 | 76.3738 | 1.5949 | [1.3408, 1.8674] | 12/383/182 |
| sew | radon/mi | 577 | 74.7788 | 73.9223 | -0.8566 | [-1.2105, -0.5533] | 90/440/47 |
| acw | radon/raw.sloc | 577 | 7.7470 | 6.8475 | -0.8995 | [-1.0191, -0.7833] | 223/352/2 |
| sew | radon/raw.sloc | 577 | 7.7470 | 7.6984 | -0.0485 | [-0.0936, -0.0017] | 39/523/15 |
| acw | radon/halstead.volume | 577 | 57.3905 | 55.1651 | -2.2254 | [-3.4988, -1.2754] | 63/495/19 |
| sew | radon/halstead.volume | 577 | 57.3905 | 58.3734 | 0.9829 | [0.6198, 1.3936] | 12/483/82 |

## Interpretacja i zakres

- Mniej naruszeń i niższa złożoność zwykle oznaczają poprawę tej konkretnej miary. Dla Maintainability Index kierunek jest odwrotny. Liczby linii i metryki Halsteada nie są samodzielnym werdyktem jakości.
- Błędów składni i błędów narzędzi nie zastępujemy zerami. Brak poprawnego pomiaru wyklucza parę z danej metryki.
- ACW ma 397 błędnych składniowo wyników: 395 powstaje w regule tabulatorów, 2 już w Sourcery. Średnie ACW opisują zatem podzbiór, który przetrwał tę implementację. Kohorta wspólna ogranicza różnicę składu grup, ale nie usuwa tego ograniczenia.
- Complexipy liczy także kod modułu. Metryki functions_total i module rozdzielają te składniki. Wyniki funkcji są dokładnie tym, co udostępnia API narzędzia, także przy funkcjach zagnieżdżonych.
- Radon uwzględnia funkcje zagnieżdżone i metody; agregat klasy nie jest ponownie dodawany do sumy funkcji.
- Przedziały: 2000 powtórzeń bootstrapu sparowanych zadań, deterministyczny seed bazowy 20261116. To opis zmienności w tym benchmarku, nie dowód uogólnienia na inne modele, języki lub klucze. Nie wybierano klucza ani progu na podstawie uzyskanych wyników.
- Wszystkie metryki, w tym po każdym wariancie Ruffa, są w exports/quality_summary.csv. Surowe pary: exports/watermark_quality_pairs.csv; wpływ Ruffa na tę samą wersję: exports/ruff_quality_pairs.csv.

Pełna definicja przebiegu: [METHODS.md](METHODS.md). Detekcja: [DETECTION.md](DETECTION.md).
