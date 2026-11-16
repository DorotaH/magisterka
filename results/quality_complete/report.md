# Porównanie jakości kodu

Delta = po − przed. Tylko kompletne pary.
Wyniki nie potwierdzają poprawności funkcjonalnej.

## ACW

Pary: 12; błędy: 8; odmowy osadzenia: 0; zmienione: 12.

| Metryka | Średnia przed | Średnia po | Średnia delta |
|---|---:|---:|---:|
| ruff.default.violations | 0.2500 | 0.0000 | -0.2500 |
| ruff.default.remaining | 0.0833 | 0.0000 | -0.0833 |
| ruff.default.changed | 1.0000 | 1.0000 | +0.0000 |
| ruff.default.lines_removed | 7.3333 | 7.2500 | -0.0833 |
| ruff.default.lines_added | 8.6667 | 7.2500 | -1.4167 |
| ruff.strict.violations | 19.1667 | 18.0000 | -1.1667 |
| ruff.strict.remaining | 7.6667 | 7.5000 | -0.1667 |
| ruff.strict.changed | 1.0000 | 1.0000 | +0.0000 |
| ruff.strict.lines_removed | 7.3333 | 7.2500 | -0.0833 |
| ruff.strict.lines_added | 8.5833 | 7.2500 | -1.3333 |
| cognitive.total | 2.5833 | 2.1667 | -0.4167 |
| cognitive.functions | 1.3333 | 1.3333 | +0.0000 |
| cognitive.max | 2.4167 | 2.0833 | -0.3333 |
| cognitive.mean | 2.2292 | 1.8750 | -0.3542 |
| cc.total | 3.4167 | 3.2500 | -0.1667 |
| cc.max | 2.9167 | 2.8333 | -0.0833 |
| cc.mean | 2.7917 | 2.6875 | -0.1042 |
| cc.functions | 1.3333 | 1.3333 | +0.0000 |
| maintainability_index | 73.4744 | 74.2587 | +0.7843 |
| raw.loc | 8.9167 | 9.3333 | +0.4167 |
| raw.lloc | 9.2500 | 8.3333 | -0.9167 |
| raw.sloc | 8.9167 | 8.0000 | -0.9167 |
| raw.comments | 0.0000 | 0.0000 | +0.0000 |
| raw.multi | 0.0000 | 0.0000 | +0.0000 |
| raw.blank | 0.0000 | 1.3333 | +1.3333 |
| raw.single_comments | 0.0000 | 0.0000 | +0.0000 |
| halstead.h1 | 2.5000 | 2.5000 | +0.0000 |
| halstead.h2 | 6.4167 | 6.4167 | +0.0000 |
| halstead.N1 | 5.4167 | 5.4167 | +0.0000 |
| halstead.N2 | 10.5833 | 10.5833 | +0.0000 |
| halstead.vocabulary | 8.9167 | 8.9167 | +0.0000 |
| halstead.length | 16.0000 | 16.0000 | +0.0000 |
| halstead.calculated_length | 23.9708 | 23.9708 | +0.0000 |
| halstead.volume | 57.4667 | 57.4667 | +0.0000 |
| halstead.difficulty | 1.9742 | 1.9742 | +0.0000 |
| halstead.effort | 164.7259 | 164.7259 | +0.0000 |
| halstead.time | 9.1514 | 9.1514 | +0.0000 |
| halstead.bugs | 0.0192 | 0.0192 | +0.0000 |

## SEW

Pary: 20; błędy: 0; odmowy osadzenia: 0; zmienione: 20.

| Metryka | Średnia przed | Średnia po | Średnia delta |
|---|---:|---:|---:|
| ruff.default.violations | 0.4500 | 0.4500 | +0.0000 |
| ruff.default.remaining | 0.1000 | 0.1000 | +0.0000 |
| ruff.default.changed | 1.0000 | 1.0000 | +0.0000 |
| ruff.default.lines_removed | 5.2500 | 6.2000 | +0.9500 |
| ruff.default.lines_added | 6.5500 | 7.5000 | +0.9500 |
| ruff.strict.violations | 14.7000 | 14.4000 | -0.3000 |
| ruff.strict.remaining | 7.1000 | 7.1500 | +0.0500 |
| ruff.strict.changed | 1.0000 | 1.0000 | +0.0000 |
| ruff.strict.lines_removed | 5.2500 | 6.2000 | +0.9500 |
| ruff.strict.lines_added | 6.5000 | 7.4500 | +0.9500 |
| cognitive.total | 1.5500 | 1.6000 | +0.0500 |
| cognitive.functions | 1.2000 | 1.2000 | +0.0000 |
| cognitive.max | 1.4500 | 1.5000 | +0.0500 |
| cognitive.mean | 1.3375 | 1.3875 | +0.0500 |
| cc.total | 2.4500 | 2.4500 | +0.0000 |
| cc.max | 2.1500 | 2.1500 | +0.0000 |
| cc.mean | 2.0750 | 2.0750 | +0.0000 |
| cc.functions | 1.2000 | 1.2000 | +0.0000 |
| maintainability_index | 81.6558 | 80.6538 | -1.0020 |
| raw.loc | 6.7500 | 6.7000 | -0.0500 |
| raw.lloc | 7.0000 | 6.9500 | -0.0500 |
| raw.sloc | 6.7500 | 6.7000 | -0.0500 |
| raw.comments | 0.0000 | 0.0000 | +0.0000 |
| raw.multi | 0.0000 | 0.0000 | +0.0000 |
| raw.blank | 0.0000 | 0.0000 | +0.0000 |
| raw.single_comments | 0.0000 | 0.0000 | +0.0000 |
| halstead.h1 | 1.6500 | 1.7000 | +0.0500 |
| halstead.h2 | 4.1500 | 4.2000 | +0.0500 |
| halstead.N1 | 3.4000 | 3.4500 | +0.0500 |
| halstead.N2 | 6.6500 | 6.7000 | +0.0500 |
| halstead.vocabulary | 5.8000 | 5.9000 | +0.1000 |
| halstead.length | 10.0500 | 10.1500 | +0.1000 |
| halstead.calculated_length | 14.6825 | 14.6825 | +0.0000 |
| halstead.volume | 35.1932 | 35.2932 | +0.1000 |
| halstead.difficulty | 1.2595 | 1.2845 | +0.0250 |
| halstead.effort | 99.1922 | 99.2422 | +0.0500 |
| halstead.time | 5.5107 | 5.5135 | +0.0028 |
| halstead.bugs | 0.0117 | 0.0118 | +0.0000 |

## Błędy składni ACW

8 wyników ACW ma błędną składnię po transformacji wcięć upstream. Wykluczono je z metryk; zachowano kod i opis błędu. ID: 2, 4, 7, 8, 10, 13, 15, 17.
