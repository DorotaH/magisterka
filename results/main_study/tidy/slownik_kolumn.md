# Słownik kolumn

- `sample_id` i `dataset` identyfikują jednostkę.
- `variant`, `stage`, `ruff_profile` i `ruff_mode` identyfikują stan.
- `level`, `unit_id` identyfikują plik albo blok/funkcję.
- `metric` i `value` przechowują wynik. Brak wiersza oznacza niedostępny pomiar.
- `ruff_added_*`, `ruff_removed_*` i `ruff_net_*` opisują zmiany wobec oryginału w tym samym trybie.
- `sew_detected_*` używa indeksu klucza. Zero oznacza klucz eksperymentalny. Wynik interpretujemy z `sew_evaluable_*`.
- `complexipy_module` to pomiar modułu w warstwie skryptów APPS.
- `samples.csv` dodaje cechy oryginału, warstwy i SHA-256.
