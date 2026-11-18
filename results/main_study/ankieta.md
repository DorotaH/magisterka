# Projekt ankiety do akceptacji

## Instrukcja dla uczestnika

W każdej próbie zobaczysz dwie wersje fragmentu Pythona. Przeczytaj obie. W każdej z poniższych odpowiedzi możesz wybrać lewy fragment, prawy fragment lub „bez różnicy”.

1. Który kod bardziej Ci się podoba?
2. Który kod byłoby Ci łatwiej utrzymać?
3. Który kod bardziej wygląda na zmodyfikowany automatycznie?

Zaznacz doświadczenie w programowaniu: brak, mniej niż rok, 1–2 lata, 3–5 lat lub ponad 5 lat. Kod jest wyświetlany tą samą czcionką o stałej szerokości. Tabulator ma szerokość czterech spacji.

## Przydział

Tabela prób przydziela każdemu oceniającemu jedną z sześciu par dla każdego fragmentu. W blokach po sześciu oceniających każda para przypada raz na fragment. Strona prezentacji równoważy się między kolejnymi blokami. Wiersze oznaczone `human_eligible=0` są domyślnie wyłączone. Slot z błędem składni pozostaje w pakiecie LLM. Domyślnie uczestnik ocenia 14 fragmentów. Uzyskanie 15 ekspozycji na uczestnika wymaga akceptacji pokazywania slotu G albo włączenia osobno zatwierdzonego bodźca zastępczego. Surowa i sformatowana wersja są warunkami do oddzielnego przydziału.

Wiersze odpowiedzi powinny zawierać identyfikator uczestnika, fragment, warunek, stronę, trzy odpowiedzi i doświadczenie. Klucz wariantów pozostaje dostępny dla prowadzącej analizę. Decyzji „bez różnicy” raportujemy osobno. Model preferencji uwzględni uczestnika i fragment jako efekty losowe.

## Orientacyjna moc

Dla preferencji 65:35, dwustronnego poziomu 0,05 i mocy 0,80 potrzeba około 90 niezależnych rozstrzygnięć na parę. Każdy pełny blok sześciu osób daje 14 rozstrzygnięć na parę przy braku remisów i kompletności danych. Plan startowy 60 osób daje 140 zaplanowanych ekspozycji na parę w jednym warunku. Moc w modelu mieszanym zależy dodatkowo od korelacji w obrębie osoby i fragmentu oraz częstości remisów. Po pierwszej serii można parametryzować symulację na podstawie pilotażu ankiety.
