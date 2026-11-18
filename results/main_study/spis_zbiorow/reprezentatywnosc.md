# Reprezentatywność wybranej próby

Porównanie puli i próby ma charakter opisowy, ponieważ próba jest podzbiorem puli.

| Zbiór | Poziom | n | SLOC średnia | SLOC mediana | SLOC p10 | SLOC p90 | KS D puli i próby |
|---|---|---:|---:|---:|---:|---:|---:|
| Mercury-eval | pełny | 256 | 18.3 | 15.0 | 8.0 | 33.0 | 0.000 |
| Mercury-eval | pula | 242 | 24.0 | 20.0 | 15.0 | 38.0 | 0.000 |
| Mercury-eval | próba | 242 | 24.0 | 20.0 | 15.0 | 38.0 | 0.000 |
| ClassEval | pełny | 100 | 34.9 | 33.0 | 19.9 | 53.1 | 0.000 |
| ClassEval | pula | 99 | 35.1 | 33.0 | 20.0 | 53.2 | 0.000 |
| ClassEval | próba | 99 | 35.1 | 33.0 | 20.0 | 53.2 | 0.000 |
| APPS | pełny | 3765 | 22.6 | 17.0 | 6.0 | 45.0 | 0.011 |
| APPS | pula | 1002 | 37.4 | 31.5 | 18.0 | 61.0 | 0.011 |
| APPS | próba | 600 | 37.0 | 31.0 | 18.0 | 61.0 | 0.011 |

Dokładne rozkłady LOC/SLOC, funkcji, klas, trudności, miar CC, Complexipy, MI i Halsteada zapisano w plikach `levels_*.json`. Dla Mercury pełny profil używa pierwszego rozwiązania każdego zadania, a pula i próba jednego rozwiązania wybranego z kwalifikujących się alternatyw.
