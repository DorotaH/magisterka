# Przebieg kontrolny — końce linii normalizowane

Ten przebieg odczytywał pliki przez `read_text`, co zamieniało CRLF na LF.
Z tego powodu nie należy traktować go jako końcowej detekcji na dokładnych
bajtach plików. Ostateczne wyniki: [poprawiony raport](../detection_ruff_exact/report.md).
Dane pozostawiono do audytu. Detekcje oznaczonego kodu ACW, którego pliki
miały już LF, można wykorzystać przy pełnej zgodności hashy.
