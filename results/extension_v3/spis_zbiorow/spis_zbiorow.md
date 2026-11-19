# Spis zbiorów warstwy A

Tabela [kandydaci.csv](kandydaci.csv) zawiera ponowne pomiary w Pythonie 3.14. Mediana SLOC dotyczy pierwszego dostępnego rozwiązania, a kandydaci zagregowani są na poziomie zadania. Osobna kolumna pokazuje zadania, których kwalifikujące się rozwiązania są skryptami. Przy APPS mianownik profilu obejmuje zadania z opublikowanym rozwiązaniem.

| Zbiór | Decyzja | Uzasadnienie |
|---|---|---|
| Mercury-train | Przyjęty | Spełnia wszystkie progi. |
| LeetCodeDataset test | Przyjęty | Spełnia wszystkie progi. Po deduplikacji część kodu odrzucono. |
| LeetCodeDataset train | Odrzucony | Mediana 13 SLOC. |
| TACO test | Odrzucony | Funkcja w 548 z 1000 profilowanych rozwiązań. |
| EffiBench | Odrzucony | Mediana 13 SLOC. |
| RepoExec | Odrzucony | Mediana 7 SLOC i 71 kandydatów. |
| DevEval | Odrzucony | Mediana 8 SLOC. Funkcje wycięto według pozycji podpisu i ciała w metadanych. |
| APPS | Odrzucony | Funkcja w 1162 z 3765 profilowanych rozwiązań. Lista wykluczeń oznacza zadania objęte już badaniem głównym. |

Wcześniej wykluczone MBPP, HumanEval, DS-1000 i CRUXEval zachowały status z [badania głównego](../../main_study/spis_zbiorow/spis_zbiorow.md).
