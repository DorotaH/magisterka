# Watermarkowanie a jakość kodu — baza badania

Kanoniczne wyniki i instrukcja czytania: **[knowledge_base/README.md](knowledge_base/README.md)**.

Badanie obejmuje 974 rozwiązania referencyjne MBPP, znakowanie ACW/SEW,
Ruff, Complexipy, Radon oraz detekcję przed i po pięciu jawnie opisanych
stanach przetwarzania. Kod, wyniki per funkcja, diagnostyka i błędy są
połączone identyfikatorami zadań i SHA-256.

- [Wyniki jakości](knowledge_base/RESULTS.md)
- [Wyniki detekcji](knowledge_base/DETECTION.md)
- [Metody i ograniczenia](knowledge_base/METHODS.md)
- [Przykłady](knowledge_base/EXAMPLES.md)
- [Odtworzenie badania](knowledge_base/REPRODUCE.md)
- [Definicje danych i metryk](knowledge_base/SCHEMA.md)

Szybki podgląd bez dodatkowych bibliotek:

```bash
python query_research.py overview
python query_research.py task 2
```

`results/` zachowuje surowe przebiegi, próby kontrolne i wcześniejsze wersje
analiz. Baza kanoniczna wskazuje, które dane wykorzystano. Starsze liczniki
oparte wyłącznie na p-value i wcześniejsze przebiegi normalizujące CRLF/LF
są udokumentowane jako historyczne.

Biblioteki ACW i SEW pozostawiono bez zmian. Konfiguracja uruchomienia ACW
jest rekonstrukcją; 397 błędów składni jest osobnym wynikiem audytu tej
implementacji, a nie dowodem wiernego odtworzenia publikacji.
