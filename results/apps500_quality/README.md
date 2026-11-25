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
wyników eksperymentu. `source_data/original_code/` zawiera poprawione kody
oryginalne Qwena i Llamy. Ich skróty zgadzają się z 44 wpisami w
`source_data/original_code_repairs.jsonl`. `source_data/artifacts_code/`
zawiera oryginały, warianty oznakowane i wszystkie zapisane warianty Ruffa.
Skrypty nie nadpisują tych kodów.

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

## Testy poprawności APPS

APPS udostępnia wejścia i oczekiwane wyjścia w polu `input_output`. Dwa ZIP-y
z generacjami użyte w tym badaniu zawierają listę identyfikatorów zadań i kody,
ale nie zawierają przypadków testowych. Skrypt pobiera testowy podział APPS z
Hugging Face, dopasowuje go po `problem_id` i testuje wszystkie zapisane pliki
Python w `source_data/artifacts_code/`.

Przygotuj osobne środowisko Pythona, pobierz zależności i uruchom komplet:

```bash
python3 -m venv /tmp/apps-test-env
/tmp/apps-test-env/bin/pip install datasets
/tmp/apps-test-env/bin/python experiments/run_apps500_correctness.py --workers 8 --timeout 3
python3 experiments/export_apps500_detection_excel.py
```

Test runner zapisuje podsumowanie każdego artefaktu i wynik każdego przypadku
do `source_data/apps_test_summary.csv` oraz `source_data/apps_test_cases.csv`.
Generator dołącza je do tego samego skoroszytu; arkusze przypadków są dzielone,
jeśli przekroczą limit wierszy Excela. `--limit-artifacts 20` uruchamia mały
pilot przed pełnym przebiegiem.

Runner wykonuje wygenerowany Python w osobnym procesie dla każdego artefaktu,
z limitami czasu i pamięci. Nie jest to pełna izolacja bezpieczeństwa.
