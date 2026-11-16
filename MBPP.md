# MBPP: ACW i SEW

Skrypt używa gotowego `code` z `Muennighoff/mbpp`, konfiguracja `full`, split `test`.
Nie generuje kodu modelem i nie uruchamia testów poprawności z datasetu.
Zalecane środowisko: Python 3.10 (jak w SEW), osobny venv.

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements-mbpp.txt
sourcery login --token "$SOURCERY_TOKEN"
python run_mbpp.py --limit 20
```

Wszystkie zadania:

```bash
python run_mbpp.py --limit 0 --workers 12 --out results/mbpp_full
```

Jedna metoda:

```bash
python run_mbpp.py --method sew --limit 20 --out results/mbpp_sew
python run_mbpp.py --method acw --limit 20 --out results/mbpp_acw
```

Folder wynikowy musi być nowy. `--workers N` uruchamia niezależne procesy robocze
(domyślnie jeden). Każda próbka nadal przechodzi tę samą sekwencję transformacji.
`--resume` kontynuuje zapisany przebieg po sprawdzeniu zgodności danych, klucza
i parametrów. Ukończone rekordy, także błędy, nie są ponawiane. Aby wznowić pełny przebieg:

```bash
python run_mbpp.py --limit 0 --workers 12 --out results/mbpp_full --resume
```

Przy przypiętej rewizji podaj również tę samą wartość `--revision`.
Pobranie danych wymaga Internetu lub lokalnego cache HF.
`--revision COMMIT` pozwala przypiąć wersję datasetu. Domyślnie odczytywana jest
tabela `full/test/0000.parquet` z rewizji `refs/convert/parquet`, zgodna z nowymi
wersjami `datasets`, które nie obsługują skryptów datasetów. Commit musi zawierać
tę tabelę; rozwiązany identyfikator rewizji trafia do `metadata.json`.

Wyniki: `dataset.jsonl` (wejście i testy), `original/`, `acw/`, `sew/`
(pliki Python), `results.jsonl` (detekcja i błędy dla każdego zadania),
`summary.json` (liczniki), `metadata.json` (parametry).
`code_pairs.jsonl` zawiera po zakończeniu pary kodu wraz z treścią zadania,
testami (nieuruchomionymi), walidacją składni i wynikami detekcji.
Błędy pojedynczych próbek są zapisywane; po zakończeniu skrypt zwraca kod 1,
jeśli wystąpił błąd. `seconds` obejmuje transformacje i detekcję, a nie samo osadzanie.

ACW stosuje kolejność z `ACW/source/RQ1-get-results.py`: Sourcery,
reguły 36–39, pięć przebiegów autopep8, reguła 45.
Reguły 36–39 są wywoływane bezpośrednio z `base_ast.py`, ponieważ upstreamowy
`reorder_process` nadal przekazuje cztery argumenty do funkcji, które przyjmują
już tylko ścieżkę pliku. Samych transformacji nie zmieniono.
Ponieważ repozytorium nie zawiera wymaganej `.sourcery.yaml`, skrypt tworzy
konfigurację włączającą reguły z `refact_list.py`. Jest to rekonstrukcja,
a nie gwarancja dokładnego odtworzenia eksperymentu autorów.
Detekcja ACW oznacza identyczność kodu po ponownym zastosowaniu transformacji.
SEW używa własnego embed/detect, tabeli kalibracyjnej repozytorium i publicznego
klucza eksperymentalnego (można zmienić przez `--key HEX`).

`detected_original` liczy fałszywe alarmy na rozwiązaniach referencyjnych;
`detected_watermarked` wykrycia na wynikach transformacji. `abstained` oznacza
odmowy osadzenia SEW i jest uwzględniane w liczbie ocenionych próbek.
To porównanie na kodzie referencyjnym, a nie ocena generacji LLM.
Nie sprawdza zachowania funkcjonalności — do tego potrzebny jest osobny runner testów.

## Badanie jakości: Ruff, Complexipy, Radon

Po wygenerowaniu par uruchom analizator w tym samym środowisku:

```bash
python -m pip install -r requirements-quality.txt
python analyze_quality.py --input results/mbpp --out results/quality
```

Pełny przebieg od danych do raportu:

```bash
python run_mbpp.py --limit 0 --workers 12 --out results/mbpp_full
python analyze_quality.py --input results/mbpp_full --out results/quality_full
```

Jeżeli przygotowano tylko SEW, dodaj `--methods sew` (analogicznie `acw`).
Analizator wymaga `original/ID.py` i `sew/ID.py` lub `acw/ID.py`.
Zapisuje też kopie obu wersji kodu, więc raport zawiera materiał przed i po.
Folder wyjściowy musi być nowy i znajdować się poza folderem wejściowym.
Nie uruchamia rozwiązań ani testów z datasetu.

Zgodnie z planem badania:

- **Ruff, próba podstawowa:** domyślny zestaw reguł lintera oraz formatowanie
  przy długości linii 88. Liczymy naruszenia i linie zmienione przez formatter.
- **Ruff, próba rygorystyczna:** `--select ALL`, automatyczne bezpieczne poprawki,
  następnie formatowanie. Liczymy naruszenia przed, pozostałe po oraz zakres zmian.
  Reguły wzajemnie sprzeczne Ruff rozstrzyga sam; komunikaty są zachowane.
  Poprawki wymagające `--unsafe-fixes` nie są włączone.
- **Complexipy:** złożoność poznawcza każdej funkcji, wynik całego fragmentu,
  liczba funkcji, maksimum i średnia. Komentarze wyłączające analizę są ignorowane.
- **Radon:** złożoność cyklomatyczna funkcji i metod (także funkcji zagnieżdżonych),
  indeks utrzymywalności, metryki Halsteada i liczby linii.
  Wyniki klas nie są ponownie dodawane do sumy złożoności ich metod.

Complexipy i Radon zawsze mierzą zapisany kod oryginalny i oznakowany,
przed poprawkami Ruffa. Ruff pracuje przez stdin, w izolacji od konfiguracji
projektu, ze stałym targetem Python 3.10. Formatowanie i poprawki trafiają
do osobnych plików. Narzędzia i ich wersje są zapisane w `metadata.json`.

Wyniki analizatora:

- `report.md`: czytelne porównanie średnich przed/po i różnic dla każdej metody;
- `metrics.csv`: jeden wiersz na zadanie, metodę i metrykę, do dalszej analizy;
- `pairs.jsonl`: metryki przed/po, różnice, status osadzenia, hashe kodu i błędy;
- `summary.json`: średnie, mediany różnic i liczby wzrostów/spadków/braku zmian;
- `artifacts/ID/{original,acw,sew}/`: kod źródłowy, szczegóły per funkcja,
  diagnostyka Ruffa, poprawione kopie i diffy.

Delta zawsze oznacza **po minus przed**. Dla naruszeń i złożoności wzrost
zwykle oznacza pogorszenie, dla indeksu utrzymywalności kierunek jest odwrotny.
Zmiany liczby linii i metryk Halsteada same w sobie nie przesądzają o jakości.
Średnie obejmują wyłącznie kompletne, poprawnie przeanalizowane pary dla danej
metody; liczebności ACW i SEW mogą się różnić. Odmowy osadzenia SEW pozostają
w porównaniu i mają osobny licznik oraz status w CSV/JSONL. Błędy nie są zerami;
skrypt kontynuuje analizę i kończy z kodem 1, jeżeli wystąpił choć jeden błąd.
Nie należy utożsamiać poprawnej składni z zachowaniem semantyki programu.

## Pełny zbiór: szybsze przetwarzanie zbiorcze

Przy 974 zadaniach można uruchomić Sourcery na całym katalogu zamiast osobno
dla każdej próbki. Kolejność reguł ACW jest taka sama. Na 20 zadaniach kontrolnych
potwierdzono identyczność kodu wynikowego i detekcji z trybem pojedynczych plików.
To kontrola na próbce, nie dowód równoważności dla każdego możliwego programu.

```bash
python run_mbpp.py --limit 0 --prepare-only --out results/mbpp_input
python run_mbpp_batch.py --input results/mbpp_input --out results/mbpp_full_complete --quality-out results/quality_full --workers 8
```

`run_mbpp_batch.py` zapisuje punkty wznowienia dla SEW i obu przebiegów ACW.
Przy przerwaniu znakowania ponów tę samą komendę z `--resume`. Jeżeli raport
jakości już powstał, do ponownej analizy użyj osobnego `analyze_quality.py`
z nowym folderem wyjściowym.

W `stages/` pozostają kopie wejść obu przebiegów Sourcery oraz logi.
`timing.json` podaje łączny czas faz ACW; czasów poszczególnych próbek
ACW nie da się wyodrębnić z trybu zbiorczego (`seconds: null`).
Nie należy porównywać tych czasów z czasem pojedynczej próbki z wcześniejszego przebiegu.

## Detekcja przed i po Ruffie

```bash
python detect_ruff.py --input results/mbpp_full_complete --quality results/quality_full --out results/detection_ruff_exact --workers 8
```

Skrypt bada oryginały MBPP oboma detektorami, wyniki ACW detektorem ACW,
a wyniki SEW detektorem SEW. Dla każdej grupy zapisuje trzy etapy:
kod wejściowy, wynik podstawowego formatowania Ruff i wynik rygorystycznych
bezpiecznych poprawek wszystkich reguł plus formatowanie. Sprawdza zgodność
źródeł i konfiguracji z analizą jakości, ale uruchamia Ruffa ponownie na
dokładnych bajtach kodu. Odczyt i zapis nie normalizują CRLF/LF;
Ruff zachowuje swoje domyślne `line-ending=auto`.
Nie dopisuje domyślnych poprawek lintera do próby podstawowej.

Detekcja ACW to dokładna identyczność kodu po ponownym zastosowaniu zapisanej
konfiguracji ACW, bez ignorowania białych znaków. Detekcja SEW to oficjalny
werdykt `Watermark detected`: samo `p < alpha` nie wystarcza, jeśli liczba
niezależnych obserwacji jest mniejsza od minimum detektora. Taki przypadek
pozostaje `Insufficient evidence`, a nie pozytywnym wykryciem.

`report.md` i `summary.json` podają liczniki i mianowniki dla każdego etapu.
`results.jsonl` zawiera pełne wyniki, `results.csv` ich tabelaryczną wersję,
a `transitions.csv` pokazuje, dla których zadań Ruff utrzymał, usunął lub
wprowadził wykrycie. `transitions_summary.json` podsumowuje te przejścia.
`inputs/` zawiera kopie ocenianego kodu, `acw_reapplied/` wyniki ponownego ACW.
Rekordy wskazują pliki i hashe SHA-256, a `stages/` zachowuje logi Sourcery.

Niepoprawny składniowo kod jest badany przed Ruffem, z jawnym znacznikiem
składni. Jeśli Ruff nie może go przetworzyć, wynik po Ruffie ma status
`preprocessing_error` i `detected: null`. Nie wliczamy go jako negatywnej
detekcji. Raport podaje także wykrycia w podzbiorze poprawnym składniowo.
Nie wykonywano testów poprawności funkcjonalnej.

Przerwaną detekcję można wznowić tą samą komendą z `--resume`.
`--limit 2` służy do krótkiego sprawdzenia całego przebiegu.
Opcja `--reuse-acw FOLDER` pozwala wykorzystać zapisane detekcje ACW dla
oznaczonego kodu wyłącznie przy zgodności konfiguracji, wersji i wszystkich
hashy wejść. Każdy wykorzystany wynik ponownego ACW ma sprawdzany SHA-256.
