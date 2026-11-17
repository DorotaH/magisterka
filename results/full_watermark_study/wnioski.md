# Wnioski z eksperymentu SEW i ACW

## 1. Oryginalny kod już zawierał diagnostyki Ruffa

Przed znakowaniem Ruff zgłosił w konfiguracji domyślnej 1593 diagnostyki dla 1140 próbek BigCodeBench oraz 745 dla 203 próbek CodeContests. W konfiguracji rozszerzonej było ich odpowiednio 7908 i 2849. Nie można więc przypisywać wszystkich diagnostyk kodu oznakowanego samemu znakowaniu.

Po SEW sumy diagnostyk wzrosły w obu profilach i obu zbiorach. Po ACW suma w profilu domyślnym nieznacznie spadła, a w rozszerzonym wzrosła: w BigCodeBench z 7908 do 21 653, a w CodeContests z 2849 do 9776. Są to zmiany netto, nie liczby nowo wprowadzonych problemów. Ruff zgłasza również kwestie stylu, które nie muszą oznaczać błędu działania.

## 2. Głównym źródłem diagnostyk ACW w profilu rozszerzonym są tabulatory

Wzrost liczby diagnostyk o kodzie W191 wyniósł 13 945 w BigCodeBench i 7428 w CodeContests. To przede wszystkim skutek stosowanej przez ACW reguły zamieniającej wcięcia na tabulatory. Wzrost samego W191 jest nawet większy od wzrostu łącznej liczby diagnostyk, ponieważ liczby innych kodów w części spadły. Duża suma diagnostyk w tym wariancie nie oznacza więc automatycznie równie dużej liczby niezależnych błędów logicznych.

## 3. W tym przebiegu ACW uszkodziło składnię części kodu

W 11 z 203 próbek CodeContests (5,4%) kod po ACW miał niepoprawną składnię; w 1140 próbkach BigCodeBench tego nie zaobserwowano. We wszystkich 11 przypadkach dodatkowa kontrola potwierdziła poprawną składnię bezpośrednio przed regułą 45. Reguła usuwa resztę spacji, jeśli wcięcie nie jest wielokrotnością czterech, przez co może usunąć wymagane wcięcie. Kod i lista błędów są w [diagnozie ACW](diagnoza_acw.md) i [podsumowaniu](podsumowanie.md).

Dla SEW nie wykryto błędów składni po znakowaniu. Poprawna składnia nie dowodzi jednak, że program zachował działanie — nie uruchamiano testów funkcjonalnych.

## 4. Znak często przestawał być wykrywany po poprawkach i formatowaniu Ruffa

Spośród próbek SEW wykrytych przed Ruffem detekcja zanikła w 1100/1136 (96,8%) plikach BigCodeBench przy profilu domyślnym i 1083/1136 (95,3%) przy rozszerzonym. Dla CodeContests było to odpowiednio 101/189 (53,4%) i 51/189 (27,0%). Jest więc wyraźna różnica między zbiorami oraz wariantami w tym konkretnym przebiegu.

W przyjętej implementacji ACW detekcja zanikła we wszystkich poprawnych składniowo próbkach, które były wykryte przed Ruffem: 1137/1137 BigCodeBench i 154/154 CodeContests, dla obu profili. Detekcja ACW oznacza tu brak zmian po ponownym zastosowaniu transformacji. Jedenaście niepoprawnych składniowo próbek wyłączono z detekcji ACW.

Oba warianty Ruffa obejmowały `check --fix` **i** `format`. Wynik dotyczy ich łącznego działania i nie wskazuje, czy zanik spowodował sam linter, formatter, czy ich połączenie. Różnica między profilami SEW nie dowodzi również, że dodatkowe reguły chronią znak: oba warianty inaczej modyfikują kod i wymagają osobnej analizy zmian.

## 5. Wykrywalność przed Ruffem nie była jednakowa

SEW wykryto przed Ruffem w 1136/1140 plików BigCodeBench i 189/203 CodeContests. W CodeContests jedna próba osadzania zakończyła się statusem `abstain:not_converged`. Dla ACW warunek braku zmian po ponownym zastosowaniu transformacji spełniło 1137/1140 poprawnych plików BigCodeBench oraz 154/192 poprawnych plików CodeContests. Tych wyników nie należy traktować jako pełnego pomiaru skuteczności detektora: nie wyznaczono odsetka fałszywych alarmów na oryginalnym kodzie ani progu skalibrowanego dla tych zbiorów.

## 6. Złożoność: porównanie z oryginałami

Na parach tych samych plików średnia złożoność cyklomatyczna bloków w pliku pozostawała najczęściej bez zmian: po SEW w 1140/1140 plikach BigCodeBench i 100/101 plikach CodeContests zawierających bloki; po ACW odpowiednio w 1137/1140 i 87/98 plikach. Pozostałe poprawne pliki CodeContests nie zawierały bloków uwzględnionych przez Radona w tym porównaniu.

Średnia złożoność poznawcza funkcji według Complexipy zmieniła się w niewielu plikach BigCodeBench: po SEW wzrosła w 66, spadła w 5, a po ACW spadła w 35. W CodeContests po ACW spadła w 35 z 98 porównanych plików z funkcjami. To wynik statycznej metryki, a nie dowód poprawności czy łatwości utrzymania.

Szczegółowe średnie dla tych samych par plików, MI i SLOC znajdują się w [porównaniu złożoności przed znakowaniem i po nim](zlozonosc_przed_i_po.md). Wyłączono 11 niepoprawnych składniowo wyników ACW. Średnie w tym porównaniu liczone są na poziomie plików; wcześniejsze zestawienie liczyło średnie dla wszystkich bloków lub funkcji i dlatego może dawać inne liczby.

## Ograniczenia

- BigCodeBench objęto w całości w wersji v0.1.4; CodeContests obejmuje 203 rozwiązania Python wybrane w repozytorium SEW, a nie cały pierwotny zbiór. Są to rozwiązania referencyjne i ludzkie, a nie próbki wygenerowane przez wybrany model.
- Brakowało oryginalnej konfiguracji Sourcery autorów ACW; odtworzono ją z listy reguł. Dodatkowo pominięto wadliwy wrapper i wywołano cztery funkcje CST bezpośrednio. Wynik dotyczy tak odtworzonego łańcucha, który może różnić się od eksperymentu autorów.
- Nie badano zachowania programu, fałszywych alarmów, wpływu samego lintowania bez formatowania. Te pomiary są potrzebne do szerszych wniosków o jakości, bezpieczeństwie i odporności metod.

Dane liczbowe: [podsumowanie pełnego eksperymentu](podsumowanie.md) i [Ruff przed znakowaniem i po nim](ruff_przed_znakowaniem.md).
