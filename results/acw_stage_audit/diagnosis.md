# Diagnoza niepoprawnego kodu po ACW

Audyt odtworzył etapy po zapisanym przebiegu Sourcery na kopiach wszystkich
974 plików. Wyniki końcowe są identyczne ze wszystkimi zapisanymi plikami ACW.
Kod sprawdzano przez compile(..., 'exec'), bez wykonywania rozwiązań.

| Etap | Niepoprawne pliki |
|---|---:|
| Oryginały MBPP | 0 |
| Po Sourcery | 2 |
| Po każdej z reguł 36–39 | 2 |
| Po każdym z pięciu przebiegów autopep8 | 2 |
| Po regule 45: konwersja wcięć | 397 |

395 nowych błędów powstaje w regule 45. Dwa wcześniejsze dotyczą zadań
323 i 515 i są już obecne w zapisanym wyjściu Sourcery. Nie ustalono jeszcze,
która reguła Sourcery je powoduje ani czy zależy to od konfiguracji.

W `ACW/source/one_rule_format.py`, wiersze 110–112:

```python
tabs = leading_spaces // spaces_per_tab
new_line = '\t' * tabs + line.lstrip(' ')
```

Dwa początkowe odstępy dają zero tabulatorów i są całkowicie usuwane.
Przykład: `before_tabs/2.py` zawiera poprawnie wcięty return, a
`../mbpp_full_complete/acw/2.py` ma return bez wcięcia. Adapter uruchamia tę
regułę także na fragmentach z takim formatowaniem, podobnie jak lokalny
`ACW/source/RQ1-get-results.py`. Nie dodano sprawdzenia bezpiecznej
stosowalności przed regułą. Reguła pozostaje niezmieniona w źródłach ACW.

Wnioski z porównania z dostarczonym 2402.07518v5.pdf:

- Strony 3–5: metoda zakłada transformacje zachowujące semantykę i idempotentne.
  Udokumentowana konwersja wcięć tego założenia nie spełnia dla części wejść.
- Strona 6: autorzy znakują kod wygenerowany przez GPT-4, GPT-4o i Qwen na
  zadaniach MBPP. My znakowaliśmy referencyjne rozwiązania benchmarku.
  Różny styl wcięć może ujawniać problem niewidoczny na kodzie modeli;
  jest to wyjaśnienie możliwe, nie zmierzony rozkład wcięć generacji autorów.
- Strona 7: autorzy ustawiają n=|T|, czyli używają wszystkich stosowalnych reguł.
  Samo użycie wielu reguł nie wyjaśnia błędów. Brakuje jednak oryginalnej
  `.sourcery.yaml`; nasza konfiguracja została odtworzona z refact_list.
  Nie potwierdzono identycznego zestawu aktywnych reguł i kolejności.
- Strona 10: podstawowy/maksymalny atak Ruff obejmuje 103/369 transformacji
  lintera. Nasze próby obejmowały formatter i, w wersji rygorystycznej,
  wszystkie obecne reguły z bezpiecznymi poprawkami plus formatter.
  Nie są to identyczne protokoły; 0 wykryć po formatterze nie odtwarza
  bezpośrednio wyniku odporności z artykułu.

397 błędów należy opisywać jako wynik uruchomionej wersji implementacji
z naszą konfiguracją na referencyjnym MBPP, nie jako replikację wyników publikacji.
Nie zmieniano bibliotek ACW/SEW ani istniejących wyników.

Szczegóły: summary.json, results.jsonl, stages.csv i before_tabs/.
Skrypt odtwarzający: ../../audit_acw_stages.py.
