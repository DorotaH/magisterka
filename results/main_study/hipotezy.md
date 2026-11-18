# Pytania badawcze i hipotezy

Zaakceptowane przez autorkę 18 listopada 2026 r. przed pilotażem v2. Status H1–H12: nierozstrzygnięte przed pomiarami.

**Pytania badawcze**

- **PB1:** Czy znakowanie zachowuje poprawność składni i działanie kodu?
- **PB2:** Jak zmienia się złożoność i utrzymywalność kodu (Radon CC, MI, raw, Halstead; Complexipy)?
- **PB3:** Jak zmienia się liczba i rodzaj diagnostyk Ruffa? Które rodziny reguł i które metody odpowiadają za zmianę?
- **PB4:** Jak bardzo znakowanie ingeruje w kod (podobieństwo, liczba zmienionych linii, zmiana AST)?
- **PB5:** Czy znak przeżywa `ruff check --fix` i `ruff format`; który z nich go niszczy; jak zależy to od rozmiaru i struktury kodu?
- **PB6:** Jaki jest wpływ reguły 45 ACW (tabulatory) na PB1–PB5?
- **PB7:** Czy ludzie odróżniają i preferują kod oryginalny, SEW, ACW? Czy preferencje zgadzają się z metrykami statycznymi i z oceną LLM-as-judge?

**Hipotezy wstępne** (do zamrożenia)

| ID | Hipoteza | Metryka i test |
|---|---|---|
| H1 | SEW nie powoduje błędów składni; `acw_full` powoduje je w niezerowym odsetku próbek, głównie w skryptach. `acw_notab` nie powoduje. | odsetek błędów składni, przedział Wilsona; test McNemara dla par wariantów |
| H2 | SEW i ACW bez reguły 45 zachowują działanie w warstwie poprawności. Ewentualne regresje pełnego ACW wiążą się ze zmianą wcięć. | Wyniki na tych samych wejściach, odsetek rozbieżności z przedziałem Wilsona. |
| H3 | Złożoność cyklomatyczna (Radon CC) jest praktycznie niezmieniona przez SEW i ACW (pilotaż: bez zmian w 1140/1140 plikach SEW). | test równoważności TOST, margines ±0,5 CC na plik (do uzgodnienia) |
| H4 | Complexipy i MI zmieniają się nieznacznie, ale mierzalnie; ACW zmniejsza Complexipy częściej niż SEW (pilotaż: spadek w 35 plikach po ACW). | test Wilcoxona dla par, mediana różnic z CI, TOST dla marginesu ±1 (Complexipy), ±2 (MI) |
| H5 | SEW zwiększa liczbę diagnostyk Ruffa (pilotaż: +323 i +340 w profilu domyślnym); ACW w profilu domyślnym ich nie zwiększa. | różnica diagnostyk na plik, Wilcoxon; rozkład wg rodzin |
| H6 | Zwiększenie diagnostyk po `acw_full` w profilu rozszerzonym wynika niemal w całości z reguł formatujących (W191); po usunięciu W191 i `acw_notab` różnica znika lub jest mała. | porównanie `acw_full` vs `acw_notab` vs `original`, widok bez reguł formatujących |
| H7 | Zanik znaku SEW po Ruffie zależy od rozmiaru kodu: krótsze próbki tracą znak częściej (lub rzadziej: kierunek do ustalenia po profilowaniu, hipoteza dwustronna). | regresja logistyczna zanik ~ log(SLOC) + zbiór, wykres z przedziałami Wilsona |
| H8 | Za zanik znaku SEW odpowiada przede wszystkim formatter (`ruff format`), nie `check --fix`. | porównanie czterech trybów Ruffa, McNemar |
| H9 | Detekcja ACW (punkt stały łańcucha) ma wysoki odsetek „wykryć” także na **oryginałach**, więc nie jest wiarygodną miarą; SEW ma niski odsetek fałszywych alarmów. | odsetek na oryginałach, przedział Wilsona |
| H10 | Ludzie preferują kod oryginalny nad `acw_full` (tabulatory); różnica między oryginałem a `acw_notab` i SEW jest mała. | model mieszany (efekty losowe: oceniający, fragment); test równoważności dla porównań oryginał–SEW |
| H11 | Wyniki LLM-as-judge zgadzają się z preferencjami ludzi lepiej niż jakakolwiek pojedyncza metryka statyczna. | κ Cohena, ρ Spearmana, porównanie z metrykami |
| H12 | Reguły ACW 36–39 mogą zmieniać działanie kodu. | Przegląd reguł i odtworzenie rozbieżności przy tej samej parze wejść przed i po pojedynczej regule. |

Każdą hipotezę należy dodatkowo raportować **osobno dla każdego zbioru** i dla warstw (sekcja 6), bo wnioski mogą się różnić.

## Reguły decyzji

Podstawą porównań są te same pliki w obu wariantach. Analiza różnicowa obejmuje próbki, w których oryginał wykonał się na tych samych wejściach. Regresje względem oficjalnego werdyktu liczymy wśród oryginałów przechodzących testy. Testy nie wpływają na dobór próby statycznej. APPS call-based raportujemy opisowo, bez odrębnych testów hipotez. Raportujemy liczebności, wykluczenia, wyniki dla zbiorów i warstw oraz 95% przedziały ufności. Dla grup powiązanych testów korygujemy wartości p metodą Holma przy progu 0,05.

| ID | Populacja, metryka i reguła decyzji |
|---|---|
| H1 | Parsowalne oryginały. McNemar dla wzrostu częstości błędów po ACW, osobno dla skryptów. Brak zaobserwowanych błędów po SEW i ACW bez tabulatorów raportujemy z górną granicą Wilsona. |
| H2 | Oryginały, które dały wynik na utrwalonych wejściach. Zliczamy różne wyniki i błędy wariantu. Podajemy odsetek z przedziałem Wilsona i osobny wynik względem testów oficjalnych. Każda potwierdzona różnica po SEW lub ACW bez reguły 45 przeczy hipotezie w próbie. Przypisanie różnicy regule 45 wymaga porównania z tym samym kodem przed jej zastosowaniem. |
| H3 | Pliki z definiowalną średnią CC w obu stanach. TOST dla średniej różnicy parowanej w granicach ±0,5 CC. |
| H4 | Pliki z wynikiem MI i średnią Complexipy w porównywanych stanach. Ocenimy jednocześnie zmianę testem Wilcoxona oraz równoważność TOST w granicach ±1 dla Complexipy i ±2 dla MI. Częstszy spadek Complexipy po ACW sprawdzimy testem McNemara. |
| H5 | Pliki z wynikiem Ruffa w obu stanach. Dodatnią parowaną zmianę dla SEW bada Wilcoxon. Dla ACW oceniamy górną jednostronną granicę ufności dla średniego wzrostu względem proponowanego marginesu 0,1 diagnostyki na plik. |
| H6 | Pary z odczytem rozszerzonego Ruffa. Propozycja progu: W191 stanowi ≥ 90% dodanych diagnostyk po pełnym ACW. Dla pozostałych reguł proponowany zakres równoważności dla średniej różnicy to ±0,1 diagnostyki na plik. |
| H7 | Próbki z wykrywalnym SEW przed Ruffem. Dwustronny test współczynnika log(SLOC) w regresji logistycznej utraty po `fix+format`, z uwzględnieniem zbioru i osobno dla obu profili. |
| H8 | Te same wykrywalne próbki SEW. Test McNemara dla częstszego zaniku po samym formatowaniu niż po samej naprawie. |
| H9 | Parsowalne oryginały z rozstrzygniętą detekcją. Proponowane progi: dolna granica Wilsona dla punktu stałego ACW > 10%, górna granica dla fałszywych alarmów SEW < 5%. Abstencje raportujemy osobno. |
| H10 | Porównania ludzi, model z efektami losowymi oceniającego i fragmentu. Preferencję oryginału ponad 50% oraz równoważność dla SEW i ACW bez tabulatorów w granicach 45–55% oceniamy na podstawie przedziałów modelu. Remisy raportujemy osobno. |
| H11 | Te same pary fragmentów ocenione przez ludzi i LLM. Wynik κ oraz ρ porównamy ze zgodnością z osobno zdefiniowanymi predyktorami statycznymi. Wynik popiera hipotezę, gdy dolna granica bootstrapowego CI różnicy względem najlepszego predyktora przekracza zero. |
| H12 | Jednostki z potwierdzoną zmianą po regule 36–39 i odtwarzalnym wynikiem oryginału. Jedna różnica powtórzona na tym samym wejściu po izolowanej regule potwierdza możliwość zmiany semantyki. Częstość w próbie raportujemy osobno z przedziałem Wilsona. Brak przypadku w próbie pozostawia hipotezę o możliwości nierozstrzygniętą na tych danych. |
