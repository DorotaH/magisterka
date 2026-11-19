# Protokół rozszerzenia v3

Rozszerzenie ma charakter eksploracyjny. Warstwa A obejmuje statyczne pomiary ludzkich rozwiązań, a warstwa C pilotaż na kodzie wygenerowanym przez modele. Warstwa B to opublikowane badanie główne. Hipotezy H1–H12 zachowują swoją oryginalną sumę kontrolną. Seed procedur losowych wynosi 20261118.

## Dobór warstwy A

Zastosowano kryteria z badania głównego z pominięciem wymogu testów. Zbiór musi spełnić wszystkie progi: mediana SLOC ≥ 15, odsetek próbek z funkcją lub metodą ≥ 80%, parsowalność w Pythonie 3.14 ≥ 90%, co najmniej 100 jednostek po filtrze i deduplikacji oraz zgoda licencyjna na użycie badawcze. Pomiary profilowe dotyczą pierwszego rozwiązania. Liczba kandydatów Mercury i TACO uwzględnia pierwsze kwalifikujące się rozwiązanie każdego zadania. Dla APPS analizowano pierwsze rozwiązanie. Progi na poziomie jednostki to kompilowalność oraz co najmniej 15 SLOC według Radona. Skrypty mają osobną kategorię.

Do pomiarów zakwalifikowano Mercury-train i LeetCodeDataset test. Wybieramy pierwsze kwalifikujące się rozwiązanie każdego zadania, w kolejności źródeł Mercury-train, LeetCodeDataset test. Duplikaty określamy po SHA-256 dokładnych bajtów kodu. Odrzucamy kod z badania głównego i kolejne wystąpienia identycznego kodu w rozszerzeniu. Nie losujemy podpróby. APPS nie spełnia progu funkcji. Zadania już wykorzystane w badaniu głównym oznaczono w wykazie wykluczeń.

- Mercury-train oraz ClassEval mają deklarację CC BY-NC 4.0 dla danych. Użycie w pracy jest niekomercyjne. [Mercury](https://huggingface.co/datasets/Elfsong/Mercury) · [ClassEval](https://github.com/FudanSELab/ClassEval#license)
- LeetCodeDataset i TACO deklarują Apache License 2.0. Dla EffiBench tę samą licencję podała autorka badania. EffiBench oraz LeetCodeDataset train odpadają przez medianę SLOC, a TACO przez odsetek funkcji. [LeetCodeDataset](https://huggingface.co/datasets/newfacade/LeetCodeDataset) · [TACO](https://huggingface.co/datasets/BAAI/TACO/blob/main/README.md) · [EffiBench](https://github.com/huangd1999/EffiBench)
- RepoExec i APPS deklarują MIT. RepoExec odpada przez medianę SLOC i liczebność. [RepoExec](https://huggingface.co/datasets/Fsoft-AIC/RepoExec) · [APPS](https://huggingface.co/datasets/codeparrot/apps)
- Archiwum DevEval deklaruje CC BY 4.0, a rozwiązania pochodzą z projektów zachowujących własne licencje. DevEval odpada przez medianę SLOC. [Archiwum DevEval](https://huggingface.co/datasets/LJ0815/DevEval) · [Repozytorium DevEval](https://github.com/seketeam/DevEval)

## Dobór warstwy C

Oba archiwa zawierają po 500 odpowiedzi dla tych samych 100 zadań ClassEval. Klucz rekordu to para `task_id` i `sample_index`. Sprawdzamy rewizje modeli, hashe rekordów i zgodność pliku ClassEval z badaniem głównym. Analizujemy wyłącznie pole `code` przy statusie `ok`. Pozostałe statusy i wykluczenia składniowe oraz długościowe zapisujemy w CSV. Funkcje i klasy są główną grupą, a skrypty mają osobną kategorię.

- `hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4`, rewizja `db1f81ad4b8c7e39777509fac66c652eb0a52f91`.
- `Qwen/Qwen2.5-Coder-7B-Instruct-AWQ`, rewizja `8e8ed243bbe6f9a5aff549a0924562fc719b2b8a`.

Temperatura 0.7, top-p 0.95, limit 2048 tokenów, base_seed 20261118. Wspólne prompty zapisano niżej w postaci JSON.

```json
{
  "system_prompt": "You are an expert Python programmer.",
  "user_template": "Complete the following Python class. Implement every method so that it matches its docstring. Return the whole class, including the imports it needs, in one ```python code block. Do not add tests, usage examples or explanations.\n\n{skeleton}"
}
```

## Pomiary i analiza

- E1. Częstość modyfikacji i wielkość zmiany jakości kodu mogą zależeć od wariantu znakowania oraz pochodzenia kodu.
- E2. Wykrywalność znaku może maleć po przetworzeniu przez Ruffa. Wielkość różnicy oceniamy dla każdego wariantu, profilu i trybu.
- E3. Błędy składni i regresje w testach mogą występować z różną częstością w zależności od wariantu i modelu.

Znakowanie i pomiary wykorzystują `analyze_batch` z `run_main_study.py`. Warianty to SEW, ACW bez reguły 45 i pełne ACW. Badamy Ruff default i strict z trybami check, fix, format oraz fix_format. Zbieramy diagnostyki, CC, Complexipy, MI, SLOC, podobieństwa, składnię, wykrywalność oraz fałszywe alarmy na oryginałach. Przeżywalność raportujemy warunkowo wśród próbek wykrytych przed przetwarzaniem oraz podajemy wykrywalność ogólną z mianownikami.

Porównujemy poprawnie kompilujące się AST bez atrybutów lokalizacji, zachowując kolejność instrukcji, nazwy i literały. Komentarze i formatowanie nie należą do AST. Porównanie obejmuje zapis po Sourcery i audytowane kroki reguł lokalnych. Zgodność AST jest wskaźnikiem statycznym.

Testy ClassEval dla oryginału i wariantów wykonujemy w Bubblewrap z limitami z badania głównego. Zaliczenie oryginału raportujemy osobno. Porównanie regresji dotyczy oryginałów zaliczających test i wariantów z porównywalną obserwacją. Błędy wykonania i limity czasu mają własne kategorie. Statystyki statyczne obejmują również kod z niezaliczonym oryginałem.

W parowanych tabelach porównujemy każdy wariant z oryginałem tej samej jednostki. W warstwie A używamy procedur badania głównego i grupowania według zbioru. W warstwie C stosujemy losowanie bootstrap całych zadań ze zwracaniem, 10 000 powtórzeń i przedziały percentylowe 95%. W wyniku łącznym losujemy ten sam zestaw zadań dla obu modeli. W analizie porównawczej podajemy osobno wyniki ludzkiego ClassEval, całego badania głównego, warstwy A i obu modeli. Puste mianowniki oznaczamy jako brak oszacowania.
