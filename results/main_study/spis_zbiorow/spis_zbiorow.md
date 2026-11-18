# Spis zbiorów

| Zbiór | Próbki | Parsowalne | Z funkcją | Mediana SLOC | Status i uzasadnienie |
|---|---:|---:|---:|---:|---|
| ClassEval | 100 | 100 | 100 | 33 | **główny v2**. 99 kandydatów po filtrach. |
| APPS | 3765 | 3457 | 1162 | 17 | **główny v2**. 1 002 kandydatów w profilu pierwszego rozwiązania. |
| BigCodeBench | 1140 | 1140 | 1140 | 13.0 | **pomocniczy**. Mediana 13 SLOC przy progu 15. |
| CodeContests | 203 | 203 | 101 | 27 | **pomocniczy**. 101/203 plików zawiera funkcję przy progu 80%. |
| MBPP | 974 | 974 | 974 | 5 | **odrzucony**. Mediana 5 SLOC przy progu 15. |
| HumanEval | 164 | 164 | 164 | 7 | **odrzucony**. Mediana 7 SLOC przy progu 15. |
| DevEval | 1825 | 1817 | 1817 | 8 | **rezerwa**. 394 kandydatów. Parsowalność oznacza wyodrębnienie funkcji lub metody według metadanych. |
| LiveCodeBench | — | — | — | — | **nie zmierzono**. Brak udostępnionych rozwiązań referencyjnych w standardowym wydaniu. |
| DS-1000 | 1000 | 928 | 324 | 3 | **odrzucony**. 12 kandydatów, mediana 3 SLOC. |
| CRUXEval | 800 | 800 | 800 | 5 | **odrzucony**. 0 kandydatów. |
| Mercury-eval | 256 | 256 | 256 | 15 | **główny v2**. 242 zadania mają co najmniej jedno kwalifikujące się rozwiązanie. |
| Mercury-train | 1633 | 1628 | 1626 | 15 | **pomocniczy**. W badanym wydaniu split nie dostarcza generatorów ani przypadków testowych. |
| LeetCodeDataset test | 228 | 228 | 228 | 16 | **opcjonalny**. 128 kandydatów. Długość pola completion bez wspólnego kodu testowego. |
| LeetCodeDataset train | 2641 | 2641 | 2641 | 13 | **pomocniczy**. 1 016 kandydatów. Długość pola completion. |
| EffiBench | 1000 | 1000 | 1000 | 13 | **rezerwa**. 385 kandydatów, pokrycie 917 tytułów z LeetCodeDataset. |
| TACO test | 1000 | 988 | 548 | 25 | **rezerwa**. 894 zadania z co najmniej jednym kwalifikującym się rozwiązaniem, w tym 28 call-based. |
| RepoExec | 355 | 355 | 355 | 7 | **pomocniczy**. 71 kandydatów, zmierzono funkcję docelową. |

## Zakres pomiaru

W APPS profil dotyczy pierwszego rozwiązania każdego zadania z opublikowanymi rozwiązaniami. W całym splicie było 5000 zadań, w tym 1235 bez rozwiązań. Spośród pozostałych 38 ma pole `fn_name`. W profilu pierwszego rozwiązania 20 z tych 38 próbek jest parsowalnych i ma co najmniej 15 SLOC. Uruchomienie testów i wybór spośród pozostałych rozwiązań mogą zmienić wyniki filtrowania, ale 38 pozostaje górną granicą liczby zadań call-based.

Sprawdzono identyczne ciągi źródłowe na podstawie SHA-256. To porównanie dotyczy rozwiązań, a wspólne zadania mogą mieć różne rozwiązania.

- Brak identycznych źródeł między profilowanymi zbiorami.

Rozkłady, odczyty Radona i Complexipy dla każdej próbki oraz wersje narzędzi zawierają pliki `profil_*.json`. Koszt testów oraz licencje zbiorów innych niż ClassEval pozostają do weryfikacji.

[Eksport APPS](https://huggingface.co/datasets/codeparrot/apps) · [ClassEval](https://github.com/FudanSELab/ClassEval) · [Wyniki pilotażu](../../full_watermark_study/README.md)

Wpisy Mercury, LeetCodeDataset, EffiBench, TACO, RepoExec, DevEval, DS-1000 i CRUXEval uzupełniono z wcześniejszego pomiaru porównawczego. Rozkłady Mercury i TACO opisują pierwsze zapisane rozwiązanie na zadanie. Liczba kandydatów dla tych dwóch zbiorów uwzględnia dowolne dostępne rozwiązanie.
