# Złożoność oryginałów a kodu oznakowanego

Przeanalizowano oryginały 1140 próbek BigCodeBench i 203 wybranych rozwiązań CodeContests tymi samymi wersjami i poleceniami Radona oraz Complexipy co kod oznakowany. Metryki kodu oznakowanego pochodzą z etapu przed uruchomieniem Ruffa.

Każda para średnich poniżej obejmuje **te same pliki**: wyłącznie próbki z dostępnym wynikiem danej metryki po obu stronach. W CC i Complexipy najpierw liczona jest średnia z bloków lub funkcji w pliku, a następnie średnia po plikach; pliki bez takich elementów nie wchodzą do tych dwóch porównań. Oryginały analizowano jeden raz dla obu metod.

## bigcodebench

| Metoda | Metryka | Par plików | Oryginał: średnia | Po znakowaniu: średnia | Średnia różnica | Wzrost / bez zmian / spadek |
|---|---|---:|---:|---:|---:|---:|
| SEW | Radon CC — średnia z bloków w pliku | 1140 | 3.08 | 3.08 | +0.00 | 0 / 1140 / 0 |
| SEW | Radon MI — indeks utrzymywalności pliku | 1140 | 85.41 | 85.20 | -0.21 | 54 / 921 / 165 |
| SEW | Complexipy — średnia z funkcji w pliku | 1140 | 2.08 | 2.16 | +0.08 | 66 / 1069 / 5 |
| SEW | Radon — liczba linii kodu SLOC | 1140 | 14.36 | 14.29 | -0.07 | 63 / 909 / 168 |
| ACW | Radon CC — średnia z bloków w pliku | 1140 | 3.08 | 3.08 | +0.00 | 1 / 1137 / 2 |
| ACW | Radon MI — indeks utrzymywalności pliku | 1140 | 85.41 | 85.40 | -0.01 | 60 / 967 / 113 |
| ACW | Complexipy — średnia z funkcji w pliku | 1140 | 2.08 | 2.02 | -0.05 | 0 / 1105 / 35 |
| ACW | Radon — liczba linii kodu SLOC | 1140 | 14.36 | 14.25 | -0.10 | 47 / 906 / 187 |

## codecontests

| Metoda | Metryka | Par plików | Oryginał: średnia | Po znakowaniu: średnia | Średnia różnica | Wzrost / bez zmian / spadek |
|---|---|---:|---:|---:|---:|---:|
| SEW | Radon CC — średnia z bloków w pliku | 101 | 4.28 | 4.28 | +0.00 | 0 / 100 / 1 |
| SEW | Radon MI — indeks utrzymywalności pliku | 203 | 57.74 | 58.05 | +0.31 | 104 / 59 / 40 |
| SEW | Complexipy — średnia z funkcji w pliku | 101 | 5.63 | 5.64 | +0.01 | 6 / 92 / 3 |
| SEW | Radon — liczba linii kodu SLOC | 203 | 47.39 | 46.40 | -1.00 | 17 / 84 / 102 |
| ACW | Radon CC — średnia z bloków w pliku | 98 | 4.30 | 4.30 | -0.01 | 2 / 87 / 9 |
| ACW | Radon MI — indeks utrzymywalności pliku | 192 | 57.49 | 57.73 | +0.24 | 76 / 96 / 20 |
| ACW | Complexipy — średnia z funkcji w pliku | 98 | 5.65 | 5.18 | -0.47 | 0 / 63 / 35 |
| ACW | Radon — liczba linii kodu SLOC | 192 | 48.61 | 47.28 | -1.33 | 9 / 116 / 67 |

MI ma inną skalę niż złożoność: większa wartość jest zazwyczaj interpretowana jako większa łatwość utrzymania według modelu Radona. SLOC to liczba linii kodu według Radona. Wyniki to miary statyczne; nie potwierdzają poprawności działania ani nie wyjaśniają same z siebie przyczyn zmian.

Jedenaście niepoprawnych składniowo wyników ACW CodeContests wyłączono z porównań. Niektóre pliki nie zawierają funkcji lub bloków analizowanych przez narzędzia; brak wartości oraz szczegóły błędów zapisano osobno. Complexipy może zakończyć się kodem 1 po przekroczeniu progu; sam kod wyjścia nie oznacza niepowodzenia parsowania.

Surowe wyniki oryginału i statusy narzędzi znajdują się przy każdej próbce w katalogu `original_metrics/`; wyniki oznakowanych próbek pozostają w katalogach `sew/` i `acw/`. Zestawienie wszystkich par: [complexity_original_results.json](complexity_original_results.json).
