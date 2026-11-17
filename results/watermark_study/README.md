# Eksperyment znakowania kodu

Pilotaż, bez losowania: pierwsze 20 pozycji BigCodeBench v0.1.4 (kod `complete_prompt` + `canonical_solution`) oraz pierwsze 20 rozwiązań Python z listy `SEW/scripts/codecontests_selection.json` (CodeContests, valid/test). Są to rozwiązania referencyjne lub ludzkie, a nie generacje wybranego modelu. Nie mierzymy poprawności funkcjonalnej. Wybór nie jest reprezentatywny dla całych zbiorów. ID i wszystkie wyniki są w `results.json`.

`original.py` zawiera kod wejściowy; `sew/watermarked.py` i `acw_partial/watermarked.py` kod po znakowaniu; `ruff_default.py` i `ruff_strict.py` są niezależnymi kopiami po zmianach Ruffa. SEW korzysta z oryginalnych `embed`/`detect`, klucz eksperymentalny to `76` powtórzone 16 razy; werdykt jest obliczony z domyślnym progiem implementacji (0,01). Status abstencji i liczba miejsc są zapisane w JSON.

ACW jest **częściowe**: wykorzystano lokalne kroki z `RQ1-get-results.py` (reguły 36–45: przestawianie, autopep8 i tabulatory). Brakuje pierwszego kroku Sourcery i właściwej konfiguracji `.sourcery.yaml`, której repozytorium nie zawiera. Próba użycia Sourcery zakończyła się żądaniem uwierzytelnienia. Dlatego nie jest to pełne ACW. `fixed_point` oznacza tylko, że ponowne zastosowanie tych lokalnych kroków nie zmieniło pliku; nie potwierdza obecności znaku i może zachodzić również w kodzie oryginalnym. Błędy składni i awarie narzędzi są zapisywane; nie przeprowadzano testów semantyki.

Każdy profil Ruffa zaczyna od tej samej oznakowanej wersji. Diagnostyki są zapisywane przed poprawkami w osobnym pliku JSON. Polecenia: `ruff check --isolated --output-format json`, następnie `ruff check --isolated --fix` i `ruff format --isolated`; rozszerzony profil dodaje do `check` `--select E,F,W,I,B,UP,SIM`. Są to bezpieczne poprawki Ruffa bez `--unsafe-fixes`, po których uruchomiono formatter. Ruff nie ma ogólnego podziału wszystkich wyników na błędy i ostrzeżenia: podajemy sumę i kody; prefiks W jest kategorią reguł, nie uniwersalną klasyfikacją ważności. Sama analiza `ruff check` bez `--fix` nie zmienia pliku.

Przed Ruffem uruchomiono `radon cc -j`, `radon mi -j`, `radon raw -j` oraz `complexipy --isolated --no-ignore --output-format json`; dla każdego pliku są surowe wyjścia stdout/stderr, JSON Complexipy (jeśli powstał) oraz kody wyjścia. Ruff 0.17.5, Radon 6.0.1, Complexipy 9.0.0, Python 3.14. Skrypt nie uruchamia kodu z benchmarków.

Powtórzenie: zainstaluj `ruff radon complexipy tree-sitter tree-sitter-python tree-sitter-java tree-sitter-cpp pyarrow autopep8 astor libcst chardet`, pobierz poniższe pliki do katalogu `WATERMARK_DATA`, a następnie uruchom `python3 experiments/run_watermark_study.py` i `python3 experiments/summarize_watermark_study.py`. `WATERMARK_LIMIT` zmienia liczbę próbek (domyślnie 20). Potrzebne programy muszą być dostępne w PATH. Skrypt nadpisuje wyniki istniejących próbek.

Źródła plików Parquet i SHA-256:

- [BigCodeBench v0.1.4](https://huggingface.co/datasets/bigcode/bigcodebench/blob/main/data/v0.1.4-00000-of-00001.parquet), lokalna nazwa `bigcode.parquet`: `d9a4965821c9507ebdfb551c288656b2d5fe553234f5183044333ca8a4018267`.
- [CodeContests valid](https://huggingface.co/datasets/deepmind/code_contests/blob/main/data/valid-00000-of-00001-5e672c5751f060d3.parquet), `valid.parquet`: `02e8c1ccedae716f1e43cc813fcb7823c3db666ea92638820aba80e8cef451ab`.
- [CodeContests test](https://huggingface.co/datasets/deepmind/code_contests/blob/main/data/test-00000-of-00001-9c49eeff30aacaa8.parquet), `test.parquet`: `aa426cbdb202bf8703b658bcb31fd1878ca7cfd33ca07d3b703dc94ca6a2b651`.
