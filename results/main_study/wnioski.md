# Wnioski badania v2

Tabela podaje decyzje dla dostępnych pomiarów według zamrożonego protokołu.

| Hipoteza | Zbiór | Status | Podstawa |
|---|---|---|---|
| H1 | Mercury-eval | nierozstrzygnięta | liczebności regresji w binary.csv, hipoteza także dotyczy przewagi przypadków w skryptach |
| H1 | ClassEval | nierozstrzygnięta | liczebności regresji w binary.csv, hipoteza także dotyczy przewagi przypadków w skryptach |
| H1 | APPS | niepoparta | odnotowano błąd po SEW lub ACW bez reguły 45 |
| H2 | Mercury-eval | niepoparta | rozbieżność po SEW lub ACW bez reguły 45, zob. F9 |
| H2 | ClassEval | niepoparta | rozbieżność po SEW lub ACW bez reguły 45, zob. F9 |
| H2 | APPS | niepoparta | rozbieżność po SEW lub ACW bez reguły 45, zob. F9 |
| H3 | Mercury-eval | poparta | TOST po korekcie Holma, zob. F11 i paired.csv |
| H3 | ClassEval | poparta | TOST po korekcie Holma, zob. F11 i paired.csv |
| H3 | APPS | poparta | TOST po korekcie Holma, zob. F11 i paired.csv |
| H4 | Mercury-eval | nierozstrzygnięta | równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11 |
| H4 | ClassEval | nierozstrzygnięta | równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11 |
| H4 | APPS | nierozstrzygnięta | równoważność w paired.csv i częstość spadków w binary.csv, zob. F2 i F11 |
| H5 | Mercury-eval | poparta | kierunkowa zmiana SEW i górna granica dla obu wariantów ACW, zob. F4 |
| H5 | ClassEval | poparta | kierunkowa zmiana SEW i górna granica dla obu wariantów ACW, zob. F4 |
| H5 | APPS | nierozstrzygnięta | diagnostyki profilu domyślnego w F4 i paired.csv |
| H6 | Mercury-eval | nierozstrzygnięta | udział W191 w dodanych diagnostykach 98.3%, równoważność w paired.csv, zob. F5 |
| H6 | ClassEval | nierozstrzygnięta | udział W191 w dodanych diagnostykach 98.8%, równoważność w paired.csv, zob. F5 |
| H6 | APPS | nierozstrzygnięta | udział W191 w dodanych diagnostykach 97.4%, równoważność w paired.csv, zob. F5 |
| H7 | Mercury-eval | poparta | co najmniej jeden profil z dwustronnym p < 0,025, zob. F8 i logistic.csv |
| H7 | ClassEval | poparta | co najmniej jeden profil z dwustronnym p < 0,025, zob. F8 i logistic.csv |
| H7 | APPS | poparta | co najmniej jeden profil z dwustronnym p < 0,025, zob. F8 i logistic.csv |
| H8 | Mercury-eval | poparta | parowane porównanie obu profili, zob. F7 |
| H8 | ClassEval | poparta | parowane porównanie obu profili, zob. F7 |
| H8 | APPS | poparta | parowane porównanie obu profili, zob. F7 |
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

- **Mercury-eval, `sew`**. Błędy składni 0/242. Różnice działania 0/241 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +0.54 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.64. Wykrycie po samej naprawie Ruffa default 233/237, po samym formacie 108/237 wśród wykryć przed Ruffem.
- **Mercury-eval, `acw_notab`**. Błędy składni 0/242. Różnice działania 17/241 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.14 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.83. Wykrycie po samej naprawie Ruffa default 220/221, po samym formacie 218/221 wśród wykryć przed Ruffem.
- **Mercury-eval, `acw_full`**. Błędy składni 6/242. Różnice działania 23/241 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.05 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.13. Wykrycie po samej naprawie Ruffa default 214/215, po samym formacie 0/215 wśród wykryć przed Ruffem.
- **ClassEval, `sew`**. Błędy składni 0/99. Różnice działania 0/93 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +0.97 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.63. Wykrycie po samej naprawie Ruffa default 91/95, po samym formacie 39/95 wśród wykryć przed Ruffem.
- **ClassEval, `acw_notab`**. Błędy składni 0/99. Różnice działania 4/93 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.28 na plik. Mediana zmiany CC +0.00 i Complexipy -0.14. Mediana podobieństwa liniowego 0.89. Wykrycie po samej naprawie Ruffa default 94/94, po samym formacie 87/94 wśród wykryć przed Ruffem.
- **ClassEval, `acw_full`**. Błędy składni 0/99. Różnice działania 5/93 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.28 na plik. Mediana zmiany CC +0.00 i Complexipy -0.14. Mediana podobieństwa liniowego 0.21. Wykrycie po samej naprawie Ruffa default 94/94, po samym formacie 0/94 wśród wykryć przed Ruffem.
- **APPS, `sew`**. Błędy składni 0/600. Różnice działania 1/582 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +1.16 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.60. Wykrycie po samej naprawie Ruffa default 578/596, po samym formacie 457/596 wśród wykryć przed Ruffem.
- **APPS, `acw_notab`**. Błędy składni 3/600. Różnice działania 28/582 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default -0.18 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.80. Wykrycie po samej naprawie Ruffa default 504/505, po samym formacie 481/505 wśród wykryć przed Ruffem.
- **APPS, `acw_full`**. Błędy składni 33/600. Różnice działania 57/582 porównywalnych przypadków. Średnia zmiana diagnostyk Ruffa default +0.02 na plik. Mediana zmiany CC +0.00 i Complexipy +0.00. Mediana podobieństwa liniowego 0.31. Wykrycie po samej naprawie Ruffa default 478/478, po samym formacie 0/478 wśród wykryć przed Ruffem.

- SEW. PB1–PB2: zob. podsumowanie, F2 i F9. PB3–PB4: zob. F4 i F6. PB5: porównanie trybów w F7–F8.
- ACW bez reguły 45. PB1–PB2: zob. podsumowanie, F2 i F9. PB3–PB4: zob. F4 i F6. Punkt stały uwzględnia wyjściową częstość na oryginałach w F10.
- Pełne ACW. PB6: porównanie tej samej jednostki przed regułą 45 i po niej przedstawia F5. Ocena regresji uwzględnia porównanie z wariantem pośrednim. PB1–PB5: zob. F2, F4, F6–F7 i F9–F10.
- PB7 oczekuje na oceny. Pakiet jest przeznaczony do późniejszego badania.
