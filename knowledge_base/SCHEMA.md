# Schemat danych i słownik metryk

Klucz wersji kodu: `artifact_id = variant:stage:task_id`, np.
`sew:ruff_lint_default:104`. SHA-256 wskazuje dokładne bajty UTF-8.

## Tabele SQLite

| Tabela | Zawartość |
|---|---|
| `tasks` | Opis, testy, kod konfiguracji testów i pełny rekord MBPP |
| `code_blobs` | Deduplicowane dokładne bajty kodu, SHA-256 i rozmiar |
| `artifacts` | Zadanie, wersja, etap, status, hash, kontrola składni i metryki fizycznego tekstu |
| `measurements` | Status, błąd i pełne szczegóły każdego z trzech narzędzi |
| `metric_values` | Jedna liczba dla artefaktu, narzędzia i nazwy metryki |
| `function_results` | Funkcje, moduł i klasy raportowane przez narzędzia |
| `detections` | Detektor, decyzja, status, p-value i pełny wynik JSON; także hash ponownego ACW |
| `watermark_runs` | Surowe wyniki pierwotnego znakowania |
| `profiles` | Definicje wszystkich pięciu etapów |
| `transformations` | Zmiana bajtów, liczby linii i AST po znakowaniu lub Ruffie |
| `audit_stages` | Poprawność kodu po poszczególnych regułach ACW |
| `audit_artifacts` | Dokładny kod po Sourcery i bezpośrednio przed konwersją tabulatorów |
| `findings` | Ustalenia, ograniczenia i poprawione błędy analizy |
| `metadata` | Wersje, parametry i proweniencja przebiegów |

`code_blobs` zawiera też wyniki ponownego ACW, aby test identyczności dało
się sprawdzić bez zewnętrznych plików. Hash `NULL` oznacza brak artefaktu,
a nie pusty kod. W CSV brak decyzji jest pustą komórką ze statusem błędu.

## Widoki do analizy

- `v_artifact_code`: kod dołączony do opisu artefaktu jako BLOB.
- `v_quality`: wszystkie wyniki i statusy, także niepełna diagnostyka błędnej składni.
- `v_watermark_pairs`: porównanie oryginału i oznakowanego kodu na tym samym
  zadaniu i etapie; wymaga `ok` obu pomiarów.
- `v_common_watermark_pairs`: dodatkowo wymaga dostępności obu metod.
- `v_ruff_quality_pairs`: skutek Ruffa dla tej samej wersji kodu.
- `v_detection_transitions`: utrzymane, utracone, nowe wykrycia i braki porównania.
- `v_ruff_diagnostics`: komunikaty Ruffa rozwinięte z JSON, z regułą i położeniem.
- `v_transformations`: dokładne zmiany źródła wraz z zadaniem i wersją.

## Metryki Ruffa

`default.violations`, `all.violations`: liczba diagnostyk odpowiedniego
zestawu reguł. `default.safe_fixable`, `all.safe_fixable`: liczba diagnostyk
udostępniających poprawkę oznaczoną przez Ruff jako bezpieczna.
Nie są to liczby rzeczywiście wykonanych poprawek ani naruszenia formattera.
Zakres zmian formattera/lintera jest w `transformations`.

## Metryki Complexipy

| Nazwa | Definicja |
|---|---|
| `total` | Łączna złożoność poznawcza zwrócona przez narzędzie |
| `functions_total` | Suma złożoności funkcji z wyłączeniem `<module>` |
| `module` | Złożoność kodu modułu |
| `function_count` | Liczba rekordów funkcji, bez `<module>` |
| `function_max` | Maksimum wśród tych funkcji; 0 przy pustym zbiorze |
| `function_mean` | Średnia wśród tych funkcji; 0 przy pustym zbiorze |

Pełne rekordy per funkcja obejmują też złożoność per linia w `details_json`.
To granularność API Complexipy; nie wymuszamy innego podziału funkcji zagnieżdżonych.

## Metryki Radona

`cc.function_total`, `cc.function_count`, `cc.function_max`, `cc.function_mean`
dotyczą funkcji i metod, z funkcjami zagnieżdżonymi, bez ponownego dodawania
agregatów klas. `cc.class_count` podaje liczbę rekordów klas, a `cc.module`
wynik odwiedzenia kodu modułu. CC funkcji ma bazę 1, także bez rozgałęzień.

`mi`: indeks utrzymywalności Radona, zwykle 0–100; wyżej oznacza lepszy
wynik tej miary. Dla znikomej objętości Halsteada wynik może wynosić 100,
więc indeks bywa mało czuły na krótkich fragmentach. Wieloliniowe napisy
są uwzględniane zgodnie z `multi=True`.

`raw.loc`, `raw.lloc`, `raw.sloc`, `raw.comments`, `raw.multi`, `raw.blank`,
`raw.single_comments` to surowe statystyki Radona: linie fizyczne, logiczne,
źródłowe, komentarze, linie napisów wieloliniowych, puste i samodzielne komentarze.
Sposób liczenia odpowiada przypiętej implementacji Radona, nie prostemu sumowaniu znaków nowej linii.

Halstead: `halstead.h1`, `h2`, `N1`, `N2` to odpowiednio liczby różnych
operatorów, różnych operandów, wszystkich operatorów i wszystkich operandów.
Pozostałe nazwy mają prefiks `halstead.`:

| Nazwa | Wzór / znaczenie |
|---|---|
| `vocabulary` | h1 + h2 |
| `length` | N1 + N2 |
| `calculated_length` | h1·log2(h1) + h2·log2(h2), z obsługą zer przez Radon |
| `volume` | length·log2(vocabulary) |
| `difficulty` | h1·N2/(2·h2), z obsługą zera |
| `effort` | difficulty·volume |
| `time` | effort/18; modelowa miara, nie zmierzony czas wykonania |
| `bugs` | volume/3000; modelowa estymata, nie liczba znalezionych błędów |

Cały fragment i raporty Halsteada per funkcja są w szczegółach pomiaru.
Zagnieżdżenie tych raportów odpowiada API Radona; liczby per funkcja nie
muszą tworzyć prostego podziału całkowitej objętości.

## Przykładowe zapytania

```sql
-- Wszystkie błędy i braki zamiast zastępowania ich zerami
SELECT variant,stage,tool,status,COUNT(*)
FROM artifacts JOIN measurements USING(artifact_id)
GROUP BY variant,stage,tool,status;

-- Porównanie tej samej populacji na konkretnej metryce
SELECT method,COUNT(*) n,AVG(delta) mean_delta
FROM v_common_watermark_pairs
WHERE stage='before' AND tool='complexipy' AND metric='functions_total'
GROUP BY method;

-- Zadania, na których formatter usunął wykrycie SEW
SELECT task_id FROM v_detection_transitions
WHERE variant='sew' AND detector='sew' AND stage='ruff_default' AND transition='lost';

-- Najczęstsze reguły Ruffa po znakowaniu, w poprawnym kodzie
SELECT a.variant,r.code,COUNT(*)
FROM v_ruff_diagnostics r JOIN artifacts a USING(artifact_id)
WHERE a.stage='before' AND a.syntax_valid=1 AND r.profile='all'
GROUP BY a.variant,r.code ORDER BY COUNT(*) DESC;
```
