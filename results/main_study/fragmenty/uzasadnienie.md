# Uzasadnienie doboru fragmentów

Pula liczy 913 jednostek. Wykluczenia: {'length_or_missing_match': 25, 'other_invalid': 3}.
Dobór celowy według slotów z ograniczeniem 4–6 fragmentów na zbiór. Rangi minimalizowano łącznie.
SLOC, CC, Complexipy i podobieństwo odnoszą się do prezentowanego fragmentu. Liczba miejsc SEW, detekcja i wyniki testów dotyczą całej jednostki.

## F01, slot A

Źródło mercury_eval / `reverse-vowels-of-a-string`. Kryterium blisko środka rozkładu SLOC i Complexipy. Ranga 1.
Percentyle: {'sloc': 40.85432639649507, 'complexipy': 65.11500547645126, 'cc_max': 78.42278203723987, 'sew_similarity': 8.433734939759036, 'acw_similarity': 96.27601314348301, 'tab_fraction': 67.25082146768894}.
Rezerwa: [{'dataset': 'mercury_eval', 'sample_id': 'combination-sum'}, {'dataset': 'mercury_eval', 'sample_id': 'falling-squares'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F02, slot A

Źródło classeval / `ClassEval_15`. Kryterium blisko środka rozkładu SLOC i Complexipy. Ranga 1.
Percentyle: {'sloc': 61.829134720700985, 'complexipy': 33.077765607886086, 'cc_max': 24.15115005476451, 'sew_similarity': 19.49616648411829, 'acw_similarity': 26.834611171960567, 'tab_fraction': 97.2617743702081}.
Rezerwa: [{'dataset': 'classeval', 'sample_id': 'ClassEval_50'}, {'dataset': 'classeval', 'sample_id': 'ClassEval_47'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F03, slot A

Źródło apps / `2353`. Kryterium blisko środka rozkładu SLOC i Complexipy. Ranga 1.
Percentyle: {'sloc': 53.88828039430449, 'complexipy': 39.75903614457831, 'cc_max': 24.15115005476451, 'sew_similarity': 87.23986856516977, 'acw_similarity': 84.77546549835706, 'tab_fraction': 7.0098576122672505}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '48'}, {'dataset': 'apps', 'sample_id': '2584'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F04, slot B

Źródło mercury_eval / `cherry-pickup`. Kryterium SLOC między p10 a p25. Ranga 1.
Percentyle: {'sloc': 13.581599123767798, 'complexipy': 4.874041621029573, 'cc_max': 0.10952902519167579, 'sew_similarity': 37.02081051478642, 'acw_similarity': 15.443592552026287, 'tab_fraction': 89.26615553121577}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '4512'}, {'dataset': 'mercury_eval', 'sample_id': 'integer-to-english-words'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F05, slot B

Źródło apps / `540`. Kryterium SLOC między p10 a p25. Ranga 2.
Percentyle: {'sloc': 13.581599123767798, 'complexipy': 86.4184008762322, 'cc_max': 70.59145673603504, 'sew_similarity': 7.940854326396495, 'acw_similarity': 79.3537787513691, 'tab_fraction': 84.00876232201533}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '4512'}, {'dataset': 'mercury_eval', 'sample_id': 'integer-to-english-words'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F06, slot C

Źródło mercury_eval / `minimum-window-substring`. Kryterium Complexipy między p75 a p90. Ranga 1.
Percentyle: {'sloc': 61.829134720700985, 'complexipy': 84.44687842278204, 'cc_max': 84.88499452354874, 'sew_similarity': 93.48302300109529, 'acw_similarity': 76.28696604600219, 'tab_fraction': 76.94414019715224}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '3929'}, {'dataset': 'mercury_eval', 'sample_id': 'strange-printer'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F07, slot C

Źródło apps / `2745`. Kryterium Complexipy między p75 a p90. Ranga 2.
Percentyle: {'sloc': 92.71631982475355, 'complexipy': 84.44687842278204, 'cc_max': 70.59145673603504, 'sew_similarity': 82.69441401971523, 'acw_similarity': 12.048192771084336, 'tab_fraction': 94.74260679079956}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '3929'}, {'dataset': 'mercury_eval', 'sample_id': 'strange-printer'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F08, slot D

Źródło apps / `2263`. Kryterium małe podobieństwo liniowe SEW. Ranga 2.
Percentyle: {'sloc': 0.21905805038335158, 'complexipy': 4.874041621029573, 'cc_max': 3.8335158817086525, 'sew_similarity': 0.4928806133625411, 'acw_similarity': 96.27601314348301, 'tab_fraction': 0.32858707557502737}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '689'}, {'dataset': 'apps', 'sample_id': '2319'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F09, slot D

Źródło apps / `1926`. Kryterium małe podobieństwo liniowe SEW. Ranga 1.
Percentyle: {'sloc': 4.654983570646221, 'complexipy': 12.705366922234392, 'cc_max': 12.814895947426066, 'sew_similarity': 0.4928806133625411, 'acw_similarity': 53.45016429353778, 'tab_fraction': 67.25082146768894}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '689'}, {'dataset': 'apps', 'sample_id': '2319'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F10, slot E

Źródło classeval / `ClassEval_85`. Kryterium małe podobieństwo liniowe ACW bez reguły 45. Ranga 4.
Percentyle: {'sloc': 12.048192771084336, 'complexipy': 59.52902519167579, 'cc_max': 36.801752464403066, 'sew_similarity': 9.967141292442497, 'acw_similarity': 0.43811610076670315, 'tab_fraction': 53.285870755750274}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '689'}, {'dataset': 'apps', 'sample_id': '1984'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F11, slot E

Źródło apps / `4518`. Kryterium małe podobieństwo liniowe ACW bez reguły 45. Ranga 1.
Percentyle: {'sloc': 0.21905805038335158, 'complexipy': 4.874041621029573, 'cc_max': 24.15115005476451, 'sew_similarity': 0.4928806133625411, 'acw_similarity': 0.21905805038335158, 'tab_fraction': 0.32858707557502737}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '689'}, {'dataset': 'apps', 'sample_id': '1984'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F12, slot F

Źródło classeval / `ClassEval_34`. Kryterium duży udział tabulatorów i różnica między wariantami ACW. Ranga 4.
Percentyle: {'sloc': 12.048192771084336, 'complexipy': 12.705366922234392, 'cc_max': 12.814895947426066, 'sew_similarity': 5.312157721796276, 'acw_similarity': 96.27601314348301, 'tab_fraction': 97.2617743702081}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2319'}, {'dataset': 'apps', 'sample_id': '2660'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F13, slot F

Źródło classeval / `ClassEval_36`. Kryterium duży udział tabulatorów i różnica między wariantami ACW. Ranga 2.
Percentyle: {'sloc': 24.315443592552025, 'complexipy': 19.112814895947427, 'cc_max': 12.814895947426066, 'sew_similarity': 71.46768893756845, 'acw_similarity': 96.27601314348301, 'tab_fraction': 97.2617743702081}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2319'}, {'dataset': 'apps', 'sample_id': '2660'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F14, slot G

Źródło mercury_eval / `stickers-to-spell-word`. Kryterium błąd składni pełnego ACW. Ranga 1.
Percentyle: {'sloc': 79.84665936473165, 'complexipy': 89.10186199342826, 'cc_max': 60.514786418400874, 'sew_similarity': 40.69003285870755, 'acw_similarity': 36.473165388828036, 'tab_fraction': 88.4446878422782}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2223'}, {'dataset': 'apps', 'sample_id': '3988'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.

## F15, slot H

Źródło classeval / `ClassEval_83`. Kryterium mała ingerencja obu metod. Ranga 2.
Percentyle: {'sloc': 9.912376779846658, 'complexipy': 4.874041621029573, 'cc_max': 3.8335158817086525, 'sew_similarity': 99.39759036144578, 'acw_similarity': 96.27601314348301, 'tab_fraction': 69.44140197152245}.
Rezerwa: [{'dataset': 'apps', 'sample_id': '2098'}, {'dataset': 'apps', 'sample_id': '1461'}]. Ustąpiła kandydatom w zadaniu z ograniczeniami liczności.
