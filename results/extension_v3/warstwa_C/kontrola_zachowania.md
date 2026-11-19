# Kontrole uzupełniające zachowania

## Czas w TimeUtils

W przebiegu głównym dla zadania `ClassEval_87` porównania zwrotów odnotowały 11 różnic w pięciu odpowiedziach obu modeli. W powtórzeniu zastosowano to samo zamrożenie czasu we wszystkich wariantach i oryginałach, do 1 stycznia 2024 r. o godz. 12:00:00 UTC. Wszystkie 15 śladów wariantów zrównało się z odpowiadającymi oryginałami, a testy nadal przechodziły. Tabele główne zawierają wyniki przebiegu z pierwotnym adapterem. [Kontrola czasu](summary/kontrola_czasu.csv)

## Reguła 36 w SQLQueryBuilder

W odpowiedzi Qwena `ClassEval_80_1` oryginał i zapis po Sourcery zaliczyły wszystkie 25 testów. Po samej regule 36 przestało przechodzić 16 z nich. Ten sam wynik wystąpił w obu końcowych wariantach ACW. W metodach budujących zapytania reguła przestawiła operandy konkatenacji, przenosząc literał ` WHERE ` za złożony warunek. [Kontrola reguły 36](summary/kontrola_reguly_36.csv)
