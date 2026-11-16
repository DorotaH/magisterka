# Porównanie jakości kodu

Delta = po − przed. Tylko kompletne pary.
Wyniki nie potwierdzają poprawności funkcjonalnej.

## ACW

Pary: 577; błędy: 397; odmowy osadzenia: 0; zmienione: 577.

| Metryka | Średnia przed | Średnia po | Średnia delta |
|---|---:|---:|---:|
| ruff.default.violations | 0.4107 | 0.2461 | -0.1646 |
| ruff.default.remaining | 0.2617 | 0.1837 | -0.0780 |
| ruff.default.changed | 0.9983 | 1.0000 | +0.0017 |
| ruff.default.lines_removed | 5.3310 | 6.3085 | +0.9775 |
| ruff.default.lines_added | 5.8804 | 6.3692 | +0.4887 |
| ruff.strict.violations | 14.8354 | 16.0659 | +1.2305 |
| ruff.strict.remaining | 7.2236 | 6.9567 | -0.2669 |
| ruff.strict.changed | 1.0000 | 1.0000 | +0.0000 |
| ruff.strict.lines_removed | 5.4385 | 6.3258 | +0.8873 |
| ruff.strict.lines_added | 5.7903 | 6.3258 | +0.5355 |
| cognitive.total | 3.1092 | 2.6135 | -0.4957 |
| cognitive.functions | 1.0711 | 1.0711 | +0.0000 |
| cognitive.max | 3.0572 | 2.5806 | -0.4766 |
| cognitive.mean | 2.9568 | 2.4809 | -0.4759 |
| cc.total | 3.4055 | 3.2530 | -0.1525 |
| cc.max | 3.2842 | 3.1404 | -0.1438 |
| cc.mean | 3.2149 | 3.0709 | -0.1440 |
| cc.functions | 1.0763 | 1.0763 | +0.0000 |
| maintainability_index | 74.7788 | 76.3738 | +1.5949 |
| raw.loc | 7.7730 | 7.3276 | -0.4454 |
| raw.lloc | 7.7816 | 6.8458 | -0.9359 |
| raw.sloc | 7.7470 | 6.8475 | -0.8995 |
| raw.comments | 0.0017 | 0.0017 | +0.0000 |
| raw.multi | 0.0000 | 0.0000 | +0.0000 |
| raw.blank | 0.0260 | 0.4801 | +0.4541 |
| raw.single_comments | 0.0000 | 0.0000 | +0.0000 |
| halstead.h1 | 2.8960 | 2.8475 | -0.0485 |
| halstead.h2 | 6.4506 | 6.2565 | -0.1941 |
| halstead.N1 | 5.0329 | 4.8752 | -0.1577 |
| halstead.N2 | 9.8596 | 9.5303 | -0.3293 |
| halstead.vocabulary | 9.3466 | 9.1040 | -0.2426 |
| halstead.length | 14.8925 | 14.4055 | -0.4870 |
| halstead.calculated_length | 26.7178 | 25.7542 | -0.9636 |
| halstead.volume | 57.3905 | 55.1651 | -2.2254 |
| halstead.difficulty | 2.2372 | 2.1961 | -0.0411 |
| halstead.effort | 245.0406 | 237.3665 | -7.6741 |
| halstead.time | 13.6134 | 13.1870 | -0.4263 |
| halstead.bugs | 0.0191 | 0.0184 | -0.0007 |

## SEW

Pary: 974; błędy: 0; odmowy osadzenia: 0; zmienione: 964.

| Metryka | Średnia przed | Średnia po | Średnia delta |
|---|---:|---:|---:|
| ruff.default.violations | 0.4456 | 0.5688 | +0.1232 |
| ruff.default.remaining | 0.2546 | 0.3758 | +0.1211 |
| ruff.default.changed | 0.9990 | 1.0000 | +0.0010 |
| ruff.default.lines_removed | 4.8142 | 5.5862 | +0.7721 |
| ruff.default.lines_added | 5.4589 | 6.2515 | +0.7926 |
| ruff.strict.violations | 12.6776 | 12.3881 | -0.2895 |
| ruff.strict.remaining | 7.0400 | 7.1006 | +0.0606 |
| ruff.strict.changed | 1.0000 | 1.0000 | +0.0000 |
| ruff.strict.lines_removed | 4.8676 | 5.6304 | +0.7628 |
| ruff.strict.lines_added | 5.3193 | 6.1068 | +0.7875 |
| cognitive.total | 2.4097 | 2.4343 | +0.0246 |
| cognitive.functions | 1.0524 | 1.0524 | +0.0000 |
| cognitive.max | 2.3655 | 2.3901 | +0.0246 |
| cognitive.mean | 2.2901 | 2.3148 | +0.0246 |
| cc.total | 2.9384 | 2.9415 | +0.0031 |
| cc.max | 2.8439 | 2.8470 | +0.0031 |
| cc.mean | 2.7926 | 2.7957 | +0.0031 |
| cc.functions | 1.0565 | 1.0565 | +0.0000 |
| maintainability_index | 78.7803 | 78.1674 | -0.6129 |
| raw.loc | 6.6961 | 6.6704 | -0.0257 |
| raw.lloc | 6.7495 | 6.7218 | -0.0277 |
| raw.sloc | 6.6756 | 6.6499 | -0.0257 |
| raw.comments | 0.0031 | 0.0031 | +0.0000 |
| raw.multi | 0.0000 | 0.0000 | +0.0000 |
| raw.blank | 0.0195 | 0.0195 | +0.0000 |
| raw.single_comments | 0.0010 | 0.0010 | +0.0000 |
| halstead.h1 | 2.2587 | 2.3634 | +0.1047 |
| halstead.h2 | 5.0965 | 5.2146 | +0.1181 |
| halstead.N1 | 3.8357 | 3.9466 | +0.1109 |
| halstead.N2 | 7.5103 | 7.6283 | +0.1181 |
| halstead.vocabulary | 7.3552 | 7.5780 | +0.2228 |
| halstead.length | 11.3460 | 11.5749 | +0.2290 |
| halstead.calculated_length | 20.0100 | 20.6675 | +0.6574 |
| halstead.volume | 42.5037 | 43.5496 | +1.0460 |
| halstead.difficulty | 1.6791 | 1.7376 | +0.0585 |
| halstead.effort | 170.9975 | 179.3767 | +8.3792 |
| halstead.time | 9.4999 | 9.9654 | +0.4655 |
| halstead.bugs | 0.0142 | 0.0145 | +0.0003 |

## Kompletność i błędy

Przetworzono 974 zadania i 1948 par. Metryki obejmują 577 par ACW oraz 974 pary SEW. 397 wyników ACW ma błędną składnię i nie wchodzi do średnich; oryginały i wyniki SEW są poprawne składniowo. Szczegóły: [opis przebiegu](../mbpp_full_complete/README.md), [błędy składni](../mbpp_full_complete/syntax_failures.csv).
