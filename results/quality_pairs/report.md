# Porównanie jakości kodu

Delta = po − przed. Tylko kompletne pary.
Wyniki nie potwierdzają poprawności funkcjonalnej.

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
