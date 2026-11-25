# Wyniki detekcji watermarków APPS

Skoroszyt `APPS_watermark_detection.xlsx` zawiera dwa arkusze macierzowe:
`Macierz bazowa` i `Macierz rygor`. Każdy wiersz identyfikuje zbiór, zadanie i
indeks próbki. Kolumny pokazują detekcję na kodzie oryginalnym, na kodzie po
znakowaniu oraz na kodzie po `ruff fix`, `ruff format` i `ruff fix_format`.

Pozostałe arkusze przechowują pełne rekordy detekcji, statusy znakowania oraz
szczegóły detekcji SEW. `check` jest zapisany w arkuszu `Detekcja`, ale nie ma
osobnej kolumny w macierzy, bo nie zmienia kodu. W macierzy `1` oznacza
pozytywną detekcję, `0` negatywną. Pusta komórka oznacza brak wykonanego wyniku
albo status błędu; szczegółowy status jest w arkuszu `Detekcja`.

CSV w `source_data/` są wejściami generatora i zostały skopiowane z zapisanych
wyników eksperymentu. Oryginalne pliki Python użyte do odtworzenia kontroli są
w `source_data/original_code/`. Skrypty nie nadpisują tych kodów.

## Uzupełnienie detekcji na kodach oryginalnych

Wcześniej usunięte kontrole detekcji na oryginałach trzeba odtworzyć, aby
wypełnić trzy kolumny `oryginał` w macierzach. Wymaga to zalogowanego Sourcery
dla detektora ACW. W katalogu głównym repozytorium uruchom:

```bash
PYTHONPATH="$PWD/SEW:$PWD/ACW/source:$PWD/ACW/.tools/local/lib/python3.14/dist-packages${PYTHONPATH:+:$PYTHONPATH}" \
PATH="$PWD/ACW/.tools/local/bin:$PATH" \
python3 experiments/run_apps500_original_detection.py
```

Po zakończeniu powstanie `source_data/original_detection.csv`. Następnie
odśwież skoroszyt:

```bash
python3 experiments/export_apps500_detection_excel.py
```

Generator korzysta wyłącznie z plików w repozytorium i zapisuje jeden wynik:
`results/apps500_quality/APPS_watermark_detection.xlsx`.
