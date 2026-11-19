# Rozszerzenie badania ACW i SEW

Warstwa A mierzy statycznie kod ludzki bez wymagania testów. Warstwa B to [badanie główne](../main_study/README.md). Warstwa C obejmuje gotowe odpowiedzi Qwena i Llamy na zadania ClassEval, pomiary statyczne i testy. Kryteria i plan analizy opisuje [zamrożony protokół](protokol.md). Liczebności wejściowe i decyzje o kwalifikacji są w [spisie zbiorów](spis_zbiorow/spis_zbiorow.md).

## Odtworzenie selekcji

Polecenia zakładają wykonanie z katalogu głównego repozytorium, Python 3.14.4 i narzędzia w wersjach z [environment.json](../main_study/environment.json). Dodatkowe pakiety i Bubblewrap opisano w badaniu głównym. Katalog testowy `$deps` ma zawierać pakiety używane w testach, m.in. pandas i freezegun.

Przygotuj poniższe źródła w katalogu `$data`. Tabela kandydatów zawiera SHA-256 plików warstwy A, a plik selekcji ClassEval zawiera SHA-256 danych do warstwy C.

| Nazwa lokalna | Źródło |
|---|---|
| `mercury-train.parquet` | [Mercury train](https://huggingface.co/datasets/Elfsong/Mercury/resolve/98946f8e1ab656b7acdbd308d0de1eade9b2aefe/data/train-00000-of-00001.parquet) |
| `leetcode-train.jsonl` | [LeetCodeDataset train](https://huggingface.co/datasets/newfacade/LeetCodeDataset/resolve/215604aeed660029df7de2fea5a4d7b6ed476a08/LeetCodeDataset-train.jsonl) |
| `leetcode-test.jsonl` | [LeetCodeDataset test](https://huggingface.co/datasets/newfacade/LeetCodeDataset/resolve/215604aeed660029df7de2fea5a4d7b6ed476a08/LeetCodeDataset-test.jsonl) |
| `taco-test.parquet` | [TACO test](https://huggingface.co/datasets/BAAI/TACO/resolve/d593ed0a2becbbc952230bb89be09189bf1056dc/ALL/test-00000-of-00001.parquet) |
| `effibench-data.jsonl` | [EffiBench Git LFS](https://media.githubusercontent.com/media/huangd1999/EffiBench/main/dataset.jsonl) |
| `repoexec.parquet` | [RepoExec full context](https://huggingface.co/datasets/Fsoft-AIC/RepoExec/resolve/42bdbd800720bdbdd1f00b98ce88fee5557d6e2e/data/full_context-00000-of-00001.parquet) |
| `deveval-source.tar.gz` | [DevEval Source_Code](https://huggingface.co/datasets/LJ0815/DevEval/resolve/16ff740d87f5fa97567d6dffd4bcbf299231211c/Source_Code.tar.gz) |
| `deveval-metadata.tar.gz` | [DevEval metadata](https://raw.githubusercontent.com/seketeam/DevEval/main/data.tar.gz) |
| `apps-test.jsonl` | [APPS test](https://huggingface.co/datasets/codeparrot/apps/resolve/21e74ddf8de1a21436da12e3e653065c5213e9d1/test.jsonl) |
| `classeval.json` | [ClassEval z testami](https://raw.githubusercontent.com/FudanSELab/ClassEval/master/data/ClassEval_data.json) |

```bash
extension=results/extension_v3
run=.extension-v3-run
python3.14 experiments/restore_study_files.py
python3.14 experiments/profile_extension_candidates.py "$data" "$extension/spis_zbiorow/kandydaci.csv"
python3.14 experiments/select_extension_references.py "$data"
python3.14 experiments/select_extension_classeval.py --classeval "$data/classeval.json"
(cd "$extension" && sha256sum -c protokol.sha256)
```

Selekcja warstwy C odtwarza pliki `generations.jsonl` z zapisanych części gzip i sprawdza hashe. Ponowne pobieranie modeli i generowanie odpowiedzi jest zbędne.

## Odtworzenie pomiarów i raportu

Sourcery wymaga uwierzytelnionej sesji CLI. Uruchomienia klas w warstwie C korzystają z Bubblewrap, bez dostępu do sieci w procesie testowym.

```bash
python3.14 experiments/run_extension_v3.py --inputs "$data" --output "$run" --layer warstwa_A --workers 4 --parallel-batches 3
python3.14 experiments/run_extension_v3.py --inputs "$data" --output "$run" --layer warstwa_C \
    --deps "$deps" --correctness
OPENBLAS_NUM_THREADS=1 python3.14 experiments/analyze_extension_v3.py "$run"
python3.14 experiments/report_extension_v3.py
python3.14 experiments/archive_extension_measurements.py "$run"
```

`run_extension_v3.py` wznawia pomiar w tym samym katalogu i sprawdza sumy kontrolne. Analiza warstwy C podaje przedziały bootstrap średnich zmian oraz proporcji. Pola tabel dotyczące testów Wilcoxona, TOST i przedziałów mediany pozostają puste dla warstwy C.

Po zapisaniu archiwów odtwórz surowe pomiary poleceniem `python3.14 experiments/restore_study_files.py --manifest results/extension_v3/split_files/measurements.json`. Odtworzony CSV ma tę samą strukturę długą co w badaniu głównym.

## Wyniki

- [Porównanie do pracy](porownanie.md) i [wykresy](figures/).
- [Warstwa A](warstwa_A/podsumowanie.md) oraz [warstwa C](warstwa_C/podsumowanie.md).
- [Kontrole zachowania](warstwa_C/kontrola_zachowania.md) i [ograniczenia](ograniczenia.md).

W tabelach `reguly_ast.csv` podano zmiany strukturalne po kolejnych regułach lokalnych i po całym etapie Sourcery. Tabele `reguly_sourcery.csv` pokazują zgłoszone przez to narzędzie reguły oraz ich współwystępowanie z różnicą AST pliku.

Niezależną kontrolę wybranych wierszy CSV z surowymi wynikami uruchamia `python3.14 experiments/verify_extension_v3.py "$run"`.
