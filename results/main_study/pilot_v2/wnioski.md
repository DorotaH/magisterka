# Wnioski badania v2

Tabela podaje decyzje dla dostępnych pomiarów według zamrożonego protokołu.

| Hipoteza | Zbiór | Status | Podstawa |
|---|---|---|---|
| H1 | Mercury-eval | nierozstrzygnięta | liczebności regresji w binary.csv, hipoteza także dotyczy przewagi przypadków w skryptach |
| H1 | ClassEval | nierozstrzygnięta | liczebności regresji w binary.csv, hipoteza także dotyczy przewagi przypadków w skryptach |
| H1 | APPS | nierozstrzygnięta | liczebności regresji w binary.csv, hipoteza także dotyczy przewagi przypadków w skryptach |
| H2 | Mercury-eval | niepoparta | rozbieżność po SEW lub ACW bez reguły 45, zob. F9 |
| H2 | ClassEval | nierozstrzygnięta | raport odsetków w F9 |
| H2 | APPS | nierozstrzygnięta | raport odsetków w F9 |
| H3 | Mercury-eval | poparta | TOST po korekcie Holma, zob. F11 i paired.csv |
| H3 | ClassEval | poparta | TOST po korekcie Holma, zob. F11 i paired.csv |
| H3 | APPS | poparta | TOST po korekcie Holma, zob. F11 i paired.csv |
| H4 | Mercury-eval | nierozstrzygnięta | równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11 |
| H4 | ClassEval | nierozstrzygnięta | równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11 |
| H4 | APPS | nierozstrzygnięta | równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11 |
| H5 | Mercury-eval | nierozstrzygnięta | diagnostyki profilu domyślnego w F4 i paired.csv |
| H5 | ClassEval | poparta | kierunkowa zmiana SEW i górna granica dla obu wariantów ACW, zob. F4 |
| H5 | APPS | nierozstrzygnięta | diagnostyki profilu domyślnego w F4 i paired.csv |
| H6 | Mercury-eval | nierozstrzygnięta | udział W191 w dodanych diagnostykach 99.1%, równoważność w paired.csv, zob. F5 |
| H6 | ClassEval | nierozstrzygnięta | udział W191 w dodanych diagnostykach 99.6%, równoważność w paired.csv, zob. F5 |
| H6 | APPS | nierozstrzygnięta | udział W191 w dodanych diagnostykach 98.8%, równoważność w paired.csv, zob. F5 |
| H7 | Mercury-eval | nierozstrzygnięta | modele i przypadki niewyznaczalne w logistic.csv, wspólny model na F8 |
| H7 | ClassEval | nierozstrzygnięta | modele i przypadki niewyznaczalne w logistic.csv, wspólny model na F8 |
| H7 | APPS | nierozstrzygnięta | modele i przypadki niewyznaczalne w logistic.csv, wspólny model na F8 |
| H8 | Mercury-eval | poparta | parowane porównanie obu profili, zob. F7 |
| H8 | ClassEval | poparta | parowane porównanie obu profili, zob. F7 |
| H8 | APPS | nierozstrzygnięta | pary rozbieżne w binary.csv |
| H9 | Mercury-eval | nierozstrzygnięta | przedziały względem progów w F10 |
| H9 | ClassEval | nierozstrzygnięta | przedziały względem progów w F10 |
| H9 | APPS | nierozstrzygnięta | przedziały względem progów w F10 |
| H10 | Mercury-eval | nierozstrzygnięta | oczekuje na odpowiedzi ludzi i LLM |
| H10 | ClassEval | nierozstrzygnięta | oczekuje na odpowiedzi ludzi i LLM |
| H10 | APPS | nierozstrzygnięta | oczekuje na odpowiedzi ludzi i LLM |
| H11 | Mercury-eval | nierozstrzygnięta | oczekuje na odpowiedzi ludzi i LLM |
| H11 | ClassEval | nierozstrzygnięta | oczekuje na odpowiedzi ludzi i LLM |
| H11 | APPS | nierozstrzygnięta | oczekuje na odpowiedzi ludzi i LLM |
| H12 | Mercury-eval | poparta | próba kontrolna oraz potwierdzone zmiany konkatenacji w Mercury, zob. przegląd reguł |
| H12 | ClassEval | nierozstrzygnięta | pełne oszacowania w tabelach i figurach |
| H12 | APPS | nierozstrzygnięta | pełne oszacowania w tabelach i figurach |

## Odpowiedzi na PB1–PB6 według zbioru i wariantu

- **Mercury-eval, `sew`**. Błędy składni 0/20. Różnice działania 0/20 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +0.65 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.57. Wykrycie po samej naprawie Ruffa default 19/20, po samym formacie 11/20 wśród wykryć przed Ruffem.
- **Mercury-eval, `acw_notab`**. Błędy składni 0/20. Różnice działania 3/20 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.20 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.82. Wykrycie po samej naprawie Ruffa default 17/17, po samym formacie 17/17 wśród wykryć przed Ruffem.
- **Mercury-eval, `acw_full`**. Błędy składni 0/20. Różnice działania 3/20 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.20 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.16. Wykrycie po samej naprawie Ruffa default 17/17, po samym formacie 0/17 wśród wykryć przed Ruffem.
- **ClassEval, `sew`**. Błędy składni 0/20. Różnice działania 0/19 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +0.70 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.72. Wykrycie po samej naprawie Ruffa default 18/19, po samym formacie 5/19 wśród wykryć przed Ruffem.
- **ClassEval, `acw_notab`**. Błędy składni 0/20. Różnice działania 0/19 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.05 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.90. Wykrycie po samej naprawie Ruffa default 19/19, po samym formacie 17/19 wśród wykryć przed Ruffem.
- **ClassEval, `acw_full`**. Błędy składni 0/20. Różnice działania 0/19 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.05 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.23. Wykrycie po samej naprawie Ruffa default 19/19, po samym formacie 0/19 wśród wykryć przed Ruffem.
- **APPS, `sew`**. Błędy składni 0/20. Różnice działania 0/19 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +1.50 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.55. Wykrycie po samej naprawie Ruffa default 19/20, po samym formacie 15/20 wśród wykryć przed Ruffem.
- **APPS, `acw_notab`**. Błędy składni 0/20. Różnice działania 0/19 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.10 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.67. Wykrycie po samej naprawie Ruffa default 11/11, po samym formacie 11/11 wśród wykryć przed Ruffem.
- **APPS, `acw_full`**. Błędy składni 1/20. Różnice działania 1/19 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.05 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.31. Wykrycie po samej naprawie Ruffa default 10/10, po samym formacie 0/10 wśród wykryć przed Ruffem.

- SEW. PB1–PB2: zob. podsumowanie, F2 i F9. PB3–PB4: zob. F4 i F6. PB5: porównanie trybów w F7–F8.
- ACW bez reguły 45. PB1–PB2: zob. podsumowanie, F2 i F9. PB3–PB4: zob. F4 i F6. Punkt stały uwzględnia wyjściową częstość na oryginałach w F10.
- Pełne ACW. PB6: porównanie tej samej jednostki przed regułą 45 i po niej przedstawia F5. Ocena regresji uwzględnia porównanie z wariantem pośrednim. PB1–PB5: zob. F2, F4, F6–F7 i F9–F10.
- PB7 oczekuje na oceny. Pakiet jest przeznaczony do późniejszego badania.
