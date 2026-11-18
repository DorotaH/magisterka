# Badanie główne ACW i SEW

## Stan i decyzje przed uruchomieniem

- [Kryteria](spis_zbiorow/kryteria.md) zapisano przed profilowaniem. Ich SHA-256 znajduje się obok.
- [Projekt hipotez](hipotezy.md) czeka na akceptację i zamrożenie.
- [Spis zbiorów](spis_zbiorow/spis_zbiorow.md) i [figura F1](spis_zbiorow/fig_F1.pdf) obejmują sześć zbiorów. Odczyty APPS dla pierwszych rozwiązań opisują etap przed filtrowaniem testami.
- APPS zawiera 38 problemów call-based z dostępnym rozwiązaniem, przy 5000 problemów w splicie. Docelowe około 40% przy 600–1000 problemów wymagałoby 240–400 problemów call-based. Ten parametr protokołu wymaga decyzji autorki.
- Próba ClassEval zawiera jedną porażkę oryginału w teście kalendarza, który oczekuje wydarzenia z 2 stycznia 2024 r. Kryterium co najmniej 100 próbek po filtrach wymaga ustalenia zasad dla testów zależnych od czasu.

## Odtworzenie pilotażu i próba ClassEval

W [porównaniu CodeContests](compatibility/comparison.json) użyto pierwszych 20 wpisów z `SEW/scripts/codecontests_selection.json`. Identyfikatory sprawdzono względem metadanych, a kod wejściowy pochodził z zachowanych oryginałów w pilotażu. Na potrzeby porównania użyto historycznego skryptu `experiments/full_study.py` z rewizji `3821f810d` ze wskazanym osobnym katalogiem wyjściowym i źródłem próbek. Dla obu metod wynik znakowania był identyczny bajtowo w 20/20 próbkach. Zgodne były także komunikaty składni i rozkłady kodów Ruffa dla obu profili. Źródła ACW i SEW odpowiadały rewizjom odpowiednio `2236dc304478a31fe7cc7cc393527375024428db` i `3c873186a56033e73347391b7aedebce1f7f71d0`.

[Próba ClassEval](pilot_classeval/test_results.json) objęła pierwsze 20 klas. Dziewiętnaście oryginałów przeszło testy. Wśród nich nie zaobserwowano regresji po SEW, pełnym ACW, ACW bez reguły 45 ani po łączonym trybie Ruffa dla SEW i pełnego ACW (oba profile). Testy uruchomiono z limitem 10 s i izolacją sieci przez Bubblewrap. Test ClassEval_17 zależny od daty zawiódł także dla oryginału. Pilotaż sprawdzał podzbiór macierzy docelowej, pomijał osobne tryby Ruffa oraz wariant ACW bez reguły 45 po Ruffie.

Weryfikacja środowiska i odtworzenie użyły Python 3.14.4, Sourcery 1.46.0, Ruff 0.17.5, Radon 6.0.1, Complexipy 9.0.0 i autopep8 2.3.2. SHA-256 danych pobranych do profilowania zapisano w profilach. Figurę można odtworzyć z zapisanych profili poleceniem:

```sh
python3.14 experiments/make_figures.py results/main_study/spis_zbiorow
```

## Protokół v2 (obowiązujący)

Sekcje powyżej dokumentują stan odziedziczony. W badaniu v2 stosujemy [poprawki protokołu](poprawki_protokolu.md), [zamrożone hipotezy](hipotezy.md) i plan wymieniony w [liście zadań](tasks_v2.md). [Profile trzech poziomów](spis_zbiorow/reprezentatywnosc.md) rozróżniają cały zbiór, pulę po filtrach oraz próbę. Losowanie ma seed `20261118`. Hash każdego pliku wejściowego i hash źródła jednostki zapisano w `selection.json` odpowiedniego zbioru. Dobór APPS wykorzystuje liczności komórek trudność × SLOC i przydziela pozostałe miejsca metodą największych reszt.

Pilotaż v2 zawiera 20 jednostek na zbiór. [Podsumowanie pilotażu](pilot_v2/podsumowanie.md) i [przegląd reguł](przeglad_regul_semantyka.md) dokumentują różnice z tego etapu. Pilotowe pomiary statyczne włączono do pełnych wyników z odnośnikami do ich trwałych plików. Rozwiązania i pliki wyjściowe pozostają lokalnymi artefaktami. Ocen LLM i ludzi jeszcze nie zbierano.

### Powtórzenie

Użyj Python 3.14 oraz wersji narzędzi z `environment.json`. Sourcery musi działać w zalogowanej sesji CLI. Dodatkowe zależności obejmują libcst, chardet i gramatykę Python Tree-sitter, PyArrow do danych Parquet, NumPy, SciPy i Matplotlib do analiz oraz lctk, sortedcontainers i freezegun w środowisku testowym. Dla części ClassEval potrzebny jest pandas. Bubblewrap izoluje wykonanie od sieci i plików domowych. Przypięte źródła trzech zbiorów opisują pliki selekcji. Poniższe ścieżki danych są przykładami nazw lokalnych plików.

```sh
study=results/main_study
python3.14 experiments/select_samples.py --mercury /dane/mercury-eval.parquet \
    --classeval /dane/ClassEval_data.json --apps /dane/apps/0000.parquet /dane/apps/0001.parquet --out "$study"
python3.14 experiments/run_main_study.py --study "$study" --output "$study/pilot_v2" --pilot
python3.14 experiments/run_main_study.py --study "$study" --output "$study"
python3.14 experiments/run_correctness.py --study "$study" --measurements "$study" \
    --mercury /dane/mercury-eval.parquet --classeval /dane/ClassEval_data.json \
    --apps /dane/apps/0000.parquet /dane/apps/0001.parquet --freezegun /dane/bench-deps
python3.14 experiments/export_measurements.py "$study"
python3.14 experiments/analyze_measurements.py "$study"
python3.14 experiments/make_figures.py "$study/spis_zbiorow" --measurements "$study"
python3.14 experiments/build_review_packet.py "$study" --participants 60
python3.14 experiments/report_study.py "$study" --root "$study"
```

Gdy manifesty i oryginały są już zapisane, do wznowienia wystarczy etap odpowiadający brakującym wynikom. Skrypt sprawdza SHA-256 hipotez i plików wejściowych. Wynik jednostki zapisuje atomowo po zakończeniu porównania. Logi wszystkich poleceń Sourcery zawiera katalog `batches/`, a dla poszczególnych narzędzi plik `result.json` jednostki. Ścieżka w logu może prowadzić do równoważnego pliku użytego w deduplikacji detekcji po SHA-256. Wznowienie po przerwaniu może odtworzyć ostatnią niezamkniętą partię.

## Odtworzenie dużych plików po sklonowaniu

Duże pliki zapisano jako strumienie gzip w częściach do 24 MiB. Aby odtworzyć oryginalne ścieżki JSON i CSV, uruchom z katalogu repozytorium:

```sh
python3 experiments/restore_study_files.py
```

Skrypt sprawdza SHA-256 z manifestu i zachowuje istniejące pliki zgodne ze skrótem.
