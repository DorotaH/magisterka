# Metody i zakres badania

## Dane i znakowanie

Wejście: `Muennighoff/mbpp`, konfiguracja `full`, tabela
`full/test/0000.parquet`, rewizja
`39ad389e423dd348012ea1b1bcbf224aad8f34a4`, 974 zadania.
Użyto pola `code`: to rozwiązania referencyjne. Nie generowano rozwiązań LLM.
Opisy, testy zwykłe i dodatkowe oraz kod konfiguracji testów zachowano w bazie.
Testów nie uruchamiano.

Oryginał ma wersję `original`; wyniki znakowania — `acw` i `sew`.
Ich dokładne bajty pochodzą z zapisanego pełnego przebiegu. Nowsze analizy
nie nadpisują tych plików. SHA-256 wskazuje konkretną zawartość, a nie tylko nazwę.

ACW: Sourcery 1.33.0, konfiguracja z `refact_list.py`, reguły przestawiania
36–39 wywołane przez aktualny interfejs plikowy LibCST, pięć przebiegów
autopep8 2.3.2 i reguła 45 konwersji wcięć. Oryginalnej `.sourcery.yaml`
brakowało; zapisana konfiguracja jest rekonstrukcją. Zbiorcze uruchamianie
Sourcery porównano z osobnymi uruchomieniami: zgodny kod na 86 zadaniach
i zgodna detekcja na 20 zadaniach kontrolnych. Nie jest to dowód pełnej
równoważności z implementacją z publikacji.

SEW: kod biblioteki i tabela kalibracyjna w `provenance/source_snapshot/SEW/`
oraz `provenance/sew_q_table.json`. Klucz publicznego eksperymentu:
`76767676767676767676767676767676`. Nie zmieniano bibliotek ACW/SEW.

## Pięć niezależnych stanów kodu

Wszystkie próby Ruffa zaczynają od tej samej wersji wejściowej. To rozgałęzienia,
nie kolejne etapy nakładane jeden po drugim.

| Identyfikator | Operacja |
|---|---|
| `before` | Dokładne wejście, przed Ruffem |
| `ruff_default` | Sam `ruff format` |
| `ruff_strict` | `ruff check --select ALL --fix --no-unsafe-fixes`, następnie `ruff format` |
| `ruff_lint_default` | Domyślne `ruff check --fix --no-unsafe-fixes`, bez formattera |
| `ruff_lint_repo_max` | `ruff check --select PL,UP,B,SIM,I,F,FURB --fix --no-unsafe-fixes`, bez formattera |

Ruff 0.17.5; wszędzie `--isolated --no-cache --target-version py310
--line-length 88 --stdin-filename solution.py`. Dla formattera obowiązuje
domyślne `line-ending=auto`. Wejście i wyjście przechodzą jako bajty,
bez translacji CRLF/LF. Nazwa `solution.py` jest stała, aby numeryczne ID
nie tworzyły sztucznych naruszeń zasad nazw modułów.

Repo-max odpowiada prefiksom lokalnego `ACW/source/ruff.toml` na obecnej,
przypiętej wersji Ruffa. Nie jest deklarowaną replikacją historycznych
103/369 transformacji z artykułu. W artykule są próby lintera; formatter
to osobna interwencja. Sprzeczne lub wyłączane reguły `ALL` rozstrzyga Ruff;
komunikaty i pełne diagnostyki zapisano.

## Pomiary trzech narzędzi

Każdy dostępny stan kodu jest mierzony niezależnie. Błąd jednego narzędzia
nie usuwa wyników pozostałych.

- **Ruff:** diagnostyka `check` osobno dla reguł domyślnych i `ALL`.
  Liczba naruszeń i diagnostyk z bezpieczną poprawką; pełne komunikaty,
  lokalizacje i poprawki dostępne przez `v_ruff_diagnostics`.
  Krótkie rozwiązania MBPP nie są pełnymi modułami produkcyjnymi: część
  reguł dotyczy dokumentacji i konwencji projektu, a nie samego algorytmu.
- **Complexipy 9.0.0:** `code_complexity(check_script=True, no_ignore=True,
  with_plans=False)`. Zapisano wyniki zwracanych funkcji i pseudofunkcji
  `<module>`, w tym złożoność per linia. `functions_total` wyklucza moduł,
  `module` pokazuje go osobno, a `total` obejmuje oba składniki.
  Granularność funkcji zagnieżdżonych odpowiada API Complexipy.
- **Radon 6.0.1:** CC przez `cc_visit` i `add_inner_blocks`; funkcje i metody
  deduplikowane według położenia, klasy trzymane osobno. Liczba funkcji
  została sprawdzona względem wszystkich deklaracji funkcji w AST tego
  zbioru. MI przez `mi_visit(multi=True)`, statystyki `raw.analyze`, Halstead
  przez `h_visit`. Szczegóły API zapisano bez wymyślania dodatkowych ocen jakości.

Sprawdzenie `compile(..., 'exec')` tworzy obiekt kodu, ale go nie wykonuje.
To kontrola poprawności składni i statycznych ograniczeń Pythona 3.14,
nie test funkcjonalności. Wersja języka docelowego Ruffa to Python 3.10.

## Wykrywanie znaku

Oryginały bada się oboma detektorami. ACW bada się detektorem ACW,
a SEW detektorem SEW. Nie wykonano eksperymentu krzyżowego ACW→SEW.

ACW: ponowne zastosowanie tej samej zapisanej konfiguracji; wykrycie wymaga
identyczności całego kodu, łącznie z białymi znakami i końcami linii.
Zapisano również dokładny wynik ponownego ACW i jego SHA-256 w bazie.
Wykrycie w niepoprawnym kodzie jest zachowane i jawnie oznaczone składnią.

SEW: oficjalne `detect(..., calibrate=True, alpha=0.01)`, zapisany klucz
i tabela kalibracyjna. Pozytywna decyzja to wyłącznie `Watermark detected`.
Wymagane jest minimum 5 niezależnych obserwacji. `Insufficient evidence`
pozostaje odrębnym wynikiem także przy niskim p-value. Zapisano cały zwrot
detektora, m.in. `p`, `p_all`, `p_syntax`, liczbę obserwacji i trafień.

Weryfikacja przeliczyła niezależnie wszystkie 9740 decyzji SEW przy użyciu
archiwalnego źródła i zamrożonej tabeli, porównując pełne wyniki.

## Braki, błędy i kohorty

397 plików ACW ma błędną składnię. Audyt identycznie odtworzył wszystkie
974 końcowe pliki: 395 błędów powstaje w regule 45, 2 już w Sourcery.
Podane przyczyny odnoszą się do uruchomionej implementacji i konfiguracji.
Nie ustalono jeszcze szczegółowej reguły Sourcery odpowiedzialnej za te dwa pliki.

Formatter odmawia pracy na tych plikach: wynik ma status `preprocessing_error`
i brak kodu po próbie. Sam linter może zwrócić niepoprawny kod; zachowano
go wraz z błędem składni. Taki przypadek nie jest brakiem pliku i nadal
można zapisać surowy wynik detekcji.

Statusy pomiarów: `ok`, `syntax_error`, `tool_error`, `preprocessing_error`.
Diagnostyki Ruffa przy błędnej składni są niepełne; zachowano je do audytu,
ale nie włączono ich do porównań jakości. Braków nie zastępuje się zerami.
Detekcja po nieudanym przetwarzaniu ma `detected=NULL`, nie `false`.

`available` to wszystkie poprawne pary dla danej metryki; `common` wymaga
tej samej metryki dla oryginału i obu metod na tym samym zadaniu. W pełnym
zbiorze przed Ruffem jest 577 poprawnych par ACW i 974 SEW; wspólna kohorta
ma 577 zadań. Każdy mianownik jest zapisany per metryka i etap.

## Statystyka i granice wniosków

Delta jakości = po znakowaniu minus oryginał. Dla skutku Ruffa porównuje się
kod po Ruffie z tą samą wersją przed Ruffem. Zapisano średnie, mediany,
minima, maksima i liczby wzrostów/spadków/braku zmiany.

Dla ośmiu wybranych metryk bazowych podano 95% percentylowe przedziały
bootstrapu: 2000 losowań sparowanych zadań, seed bazowy 20261116. Resampling
dotyczy zadań, nie pojedynczych funkcji. Te same dane mają te same przedziały,
niezależnie od nazwy kohorty. Dla proporcji detekcji pokazano przedziały Wilsona.
Przedziały są opisem zależnym od założeń o próbie i nie dowodzą uogólnienia.
Nie przeprowadzano serii testów istotności ani doboru korzystnego progu.

Jeden benchmark, rozwiązania referencyjne, jeden publiczny klucz i jedna
rekonstrukcja konfiguracji nie wystarczają do oceny wszystkich LLM i metod.
Narzędzia statyczne są wskaźnikami jakości; nie zastępują oceny ludzi ani
testów funkcjonalnych. `ast_equal` w tabeli transformacji jest porównaniem
AST bez położeń, nie dowodem równoważności semantycznej.

Dotychczasowe problemy z p-value i translacją końców linii zostały jawnie
skorygowane. Starsze dane pozostają w `results/` do audytu; ta baza korzysta
z przebiegu dokładnych bajtów i oficjalnych werdyktów.
