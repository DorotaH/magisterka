# Ograniczenia

- Konfigurację 35 reguł Sourcery odtworzono z listy ACW. Dla reguł 36–39 wywołano funkcje CST bezpośrednio, zgodnie z wcześniejszym pilotażem. Oryginalny wrapper ma niezgodną sygnaturę wywołania.
- Reguły 36–39 mogą zmienić działanie programu. Reguła 45 może zmienić składnię, znaczenie wcięć i treść literałów. Detekcja ACW sprawdza punkt stały z częstością odniesienia zmierzoną na oryginałach.
- Jednostki są rozwiązaniami referencyjnymi. Autorstwo każdego rozwiązania oraz analogiczne efekty w kodzie wygenerowanym przez model pozostają poza zakresem danych.
- Filtr co najmniej 15 SLOC zawęża populację. Pilotaż BigCodeBench dostarcza odrębnego materiału o krótkich fragmentach.
- APPS i CodeContests mają częściowo wspólne źródła problemów. Porównano skróty kodu i odrzucono ewentualne bezpośrednie duplikaty. To nie wyklucza wspólnego zadania z inną implementacją.
- Wynik różnicowy dotyczy ograniczonego zestawu wejść. Mercury wykorzystuje zapisane przypadki i wejścia z generatora, które mogą mieć ograniczenia konwersji. W APPS badano do 20 przypadków. W ClassEval obserwowane są zwroty wywołań kodu badanego i osobno oficjalne asercje. Czas kalendarza zamrożono identycznie dla wariantów.
- Python 3.14 może powodować trudności zależności w starszych rozwiązaniach. Pakiet gensim 4.4.0 nie zbudował się z dostępnym ABI 3.14. Wyniki techniczne i odsetki przebadanych próbek mają odrębne mianowniki.
- Wybór 15 fragmentów do oceny jest celowy. Wynik preferencji opisze ten zestaw bodźców. Potrzebny jest odrębny zbiór odpowiedzi ludzi i LLM.
- Wszystkie metryki dla tej samej jednostki porównuje się parami. Różnice pomiędzy profilami Ruffa nie izolują działania dowolnej pojedynczej reguły.

W próbie APPS 2147 oryginał sam tasuje stan przez `random.shuffle`, a nieziarnowany przebieg daje różne dopuszczalne permutacje w stdout. Pierwotny pomiar pozostaje w tabeli różnicowej. W dodatkowym odtworzeniu z tym samym ziarnem każdy wariant miał identyczny wynik z oryginałem na 7 z 7 wejść. [Odtworzenie z kontrolą losowości](apps/2147/randomness_audit/result.json)
