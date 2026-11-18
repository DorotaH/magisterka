# Uzasadnienie doboru fragmentów

Pula liczy 60 jednostek. Wykluczenia: {}.
Dobór celowy według slotów z ograniczeniem 4–6 fragmentów na zbiór. Rangi minimalizowano łącznie.
SLOC, CC, Complexipy i podobieństwo odnoszą się do prezentowanego fragmentu. Liczba miejsc SEW, detekcja i wyniki testów dotyczą całej jednostki.

## F01, slot A

Źródło mercury_eval / `find-mode-in-binary-search-tree`. Kryterium blisko środka rozkładu SLOC i Complexipy. Ranga 1.
Percentyle: {'sloc': 43.333333333333336, 'complexipy': 71.66666666666667, 'cc_max': 79.16666666666667, 'sew_similarity': 21.666666666666668, 'acw_similarity': 96.66666666666667, 'tab_fraction': 56.66666666666667}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'binary-tree-level-order-traversal-ii'}, {'dataset': 'mercury_eval', 'sample_id': 'combination-sum'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F02, slot A

Źródło classeval / `ClassEval_27`. Kryterium blisko środka rozkładu SLOC i Complexipy. Ranga 1.
Percentyle: {'sloc': 70.83333333333334, 'complexipy': 30.833333333333336, 'cc_max': 45.833333333333336, 'sew_similarity': 91.66666666666667, 'acw_similarity': 86.66666666666667, 'tab_fraction': 61.66666666666667}.
Rezerwa: [{'dataset': 'classeval', 'sample_id': 'ClassEval_49'}, {'dataset': 'classeval', 'sample_id': 'ClassEval_10'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F03, slot A

Źródło apps / `2416`. Kryterium blisko środka rozkładu SLOC i Complexipy. Ranga 1.
Percentyle: {'sloc': 49.16666666666667, 'complexipy': 56.66666666666667, 'cc_max': 70.83333333333334, 'sew_similarity': 43.333333333333336, 'acw_similarity': 48.333333333333336, 'tab_fraction': 67.5}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2276'}, {'dataset': 'apps', 'sample_id': '1025'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F04, slot B

Źródło classeval / `ClassEval_30`. Kryterium SLOC między p10 a p25. Ranga 1.
Percentyle: {'sloc': 16.666666666666668, 'complexipy': 7.5, 'cc_max': 16.666666666666668, 'sew_similarity': 100.0, 'acw_similarity': 96.66666666666667, 'tab_fraction': 21.666666666666668}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'reverse-words-in-a-string'}, {'dataset': 'mercury_eval', 'sample_id': 'evaluate-reverse-polish-notation'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F05, slot B

Źródło apps / `4480`. Kryterium SLOC między p10 a p25. Ranga 2.
Percentyle: {'sloc': 20.833333333333336, 'complexipy': 63.333333333333336, 'cc_max': 79.16666666666667, 'sew_similarity': 58.333333333333336, 'acw_similarity': 56.66666666666667, 'tab_fraction': 11.666666666666668}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'reverse-words-in-a-string'}, {'dataset': 'mercury_eval', 'sample_id': 'evaluate-reverse-polish-notation'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F06, slot C

Źródło classeval / `ClassEval_41`. Kryterium Complexipy między p75 a p90. Ranga 2.
Percentyle: {'sloc': 83.33333333333334, 'complexipy': 84.16666666666667, 'cc_max': 60.833333333333336, 'sew_similarity': 1.6666666666666667, 'acw_similarity': 81.66666666666667, 'tab_fraction': 90.0}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'interleaving-string'}, {'dataset': 'mercury_eval', 'sample_id': 'permutation-sequence'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F07, slot C

Źródło apps / `3929`. Kryterium Complexipy między p75 a p90. Ranga 1.
Percentyle: {'sloc': 79.16666666666667, 'complexipy': 84.16666666666667, 'cc_max': 93.33333333333334, 'sew_similarity': 36.66666666666667, 'acw_similarity': 36.66666666666667, 'tab_fraction': 43.333333333333336}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'interleaving-string'}, {'dataset': 'mercury_eval', 'sample_id': 'permutation-sequence'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F08, slot D

Źródło mercury_eval / `decode-ways`. Kryterium małe podobieństwo liniowe SEW. Ranga 3.
Percentyle: {'sloc': 16.666666666666668, 'complexipy': 63.333333333333336, 'cc_max': 16.666666666666668, 'sew_similarity': 5.0, 'acw_similarity': 53.333333333333336, 'tab_fraction': 95.0}.
Rezerwa: [{'dataset': 'classeval', 'sample_id': 'ClassEval_28'}, {'dataset': 'classeval', 'sample_id': 'ClassEval_90'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F09, slot D

Źródło mercury_eval / `longest-consecutive-sequence`. Kryterium małe podobieństwo liniowe SEW. Ranga 5.
Percentyle: {'sloc': 96.66666666666667, 'complexipy': 100.0, 'cc_max': 100.0, 'sew_similarity': 8.333333333333334, 'acw_similarity': 21.666666666666668, 'tab_fraction': 100.0}.
Rezerwa: [{'dataset': 'classeval', 'sample_id': 'ClassEval_28'}, {'dataset': 'classeval', 'sample_id': 'ClassEval_90'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F10, slot E

Źródło apps / `1984`. Kryterium małe podobieństwo liniowe ACW bez reguły 45. Ranga 1.
Percentyle: {'sloc': 3.3333333333333335, 'complexipy': 21.666666666666668, 'cc_max': 33.333333333333336, 'sew_similarity': 64.16666666666667, 'acw_similarity': 1.6666666666666667, 'tab_fraction': 82.5}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2149'}, {'dataset': 'apps', 'sample_id': '2469'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F11, slot E

Źródło apps / `2629`. Kryterium małe podobieństwo liniowe ACW bez reguły 45. Ranga 2.
Percentyle: {'sloc': 96.66666666666667, 'complexipy': 42.5, 'cc_max': 60.833333333333336, 'sew_similarity': 80.0, 'acw_similarity': 3.3333333333333335, 'tab_fraction': 96.66666666666667}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2149'}, {'dataset': 'apps', 'sample_id': '2469'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F12, slot F

Źródło mercury_eval / `search-in-rotated-sorted-array-ii`. Kryterium duży udział tabulatorów i różnica między wariantami ACW. Ranga 5.
Percentyle: {'sloc': 38.333333333333336, 'complexipy': 88.33333333333334, 'cc_max': 93.33333333333334, 'sew_similarity': 13.333333333333334, 'acw_similarity': 40.0, 'tab_fraction': 98.33333333333334}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'generate-parentheses'}, {'dataset': 'mercury_eval', 'sample_id': 'combination-sum'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F13, slot F

Źródło classeval / `ClassEval_44`. Kryterium duży udział tabulatorów i różnica między wariantami ACW. Ranga 1.
Percentyle: {'sloc': 79.16666666666667, 'complexipy': 93.33333333333334, 'cc_max': 96.66666666666667, 'sew_similarity': 38.333333333333336, 'acw_similarity': 90.0, 'tab_fraction': 90.0}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'generate-parentheses'}, {'dataset': 'mercury_eval', 'sample_id': 'combination-sum'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F14, slot G

Źródło apps / `3988`. Kryterium błąd składni pełnego ACW. Ranga 1.
Percentyle: {'sloc': 90.83333333333334, 'complexipy': 86.66666666666667, 'cc_max': 79.16666666666667, 'sew_similarity': 28.333333333333336, 'acw_similarity': 15.0, 'tab_fraction': 20.0}.
Rezerwa: []. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F15, slot H

Źródło classeval / `ClassEval_97`. Kryterium mała ingerencja obu metod. Ranga 3.
Percentyle: {'sloc': 70.83333333333334, 'complexipy': 98.33333333333334, 'cc_max': 84.16666666666667, 'sew_similarity': 93.33333333333334, 'acw_similarity': 80.0, 'tab_fraction': 86.66666666666667}.
Rezerwa: [{'dataset': 'classeval', 'sample_id': 'ClassEval_84'}, {'dataset': 'classeval', 'sample_id': 'ClassEval_91'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.
