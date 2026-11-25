# Scripts

This folder contains command-line tools for watermarking Python files, detecting
watermarks, and applying Ruff formatting profiles. Commands accept either a
Python file or a directory, as described below.

## Watermarking

Outputs are written under `--output`, preserving original filenames and
relative directory layout. The console shows errors and progress every 250
files.

```bash
python watermarking/run_watermarking_sew.py --input path/to/input.py --output path/to/watermarked
python watermarking/run_watermarking_acw.py --input path/to/input.py --output path/to/watermarked --variant acw_notab
```

For directory input, pass directory paths to both flags. SEW accepts `--key`
as a hexadecimal key. ACW calls `one_rule_format.single_process_file` from the
ACW repository for each rule and requires the Sourcery CLI with an
authenticated session. ACW supports `acw_notab` and `acw_full` (the latter
includes rule 45, tabs). Reports are JSON Lines files.

## Detection

`--output` is the JSONL report path, with one record per input file. Positive
detections use `positive: 1`; negative detections or insufficient evidence use
`positive: 0`.

```bash
python detection/run_detection_sew.py --input path/to/watermarked.py --output sew-detection.jsonl
python detection/run_detection_acw.py --input path/to/watermarked.py --output acw-detection.jsonl --variant acw_notab
```

SEW accepts the same hexadecimal `--key` used for embedding. ACW detection uses
the selected transform's fixed-point behavior, supports `acw_notab` and
`acw_full`, and requires the Sourcery CLI/session.

## Ruff formatting

Both commands take `--input` as a file or directory and `--output` as a
directory. Original filenames and directory structure are preserved. Actions
are `check` (copy and report), `fix` (Ruff lint autofixes), `format` (Ruff
formatter), and `fix-format`.

```bash
python formatting/run_formatter_default.py --input path/to/source --output path/to/formatted --action format
python formatting/run_formatter_strict.py --input path/to/source --output path/to/fixed --action fix-format --report ruff.jsonl
```

The default profile uses `formatting/config/ruff.default.toml`; the strict
profile uses `formatting/config/ruff.strict.toml`. The supplied rule set is
retained as `ruff.extended.toml` for an optional third profile. Use `--ruff` to
override the Ruff executable path, which defaults to `ACW/.tools/local/bin/ruff`.
