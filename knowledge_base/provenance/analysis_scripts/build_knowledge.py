#!/usr/bin/env python3
"""Build a self-contained SQLite research database and reviewable CSV exports."""
import argparse
import ast
import csv
import difflib
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3

from run_mbpp import write_json


SCHEMA = '''
PRAGMA foreign_keys=ON;
CREATE TABLE metadata(key TEXT PRIMARY KEY, value_json TEXT NOT NULL);
CREATE TABLE tasks(task_id INTEGER PRIMARY KEY, prompt TEXT, tests_json TEXT NOT NULL,
 test_setup_code TEXT, challenge_tests_json TEXT NOT NULL, raw_json TEXT NOT NULL);
CREATE TABLE profiles(stage TEXT PRIMARY KEY, description TEXT NOT NULL);
CREATE TABLE code_blobs(sha256 TEXT PRIMARY KEY, content BLOB NOT NULL, bytes INTEGER NOT NULL);
CREATE TABLE artifacts(artifact_id TEXT PRIMARY KEY, task_id INTEGER NOT NULL REFERENCES tasks,
 variant TEXT NOT NULL, stage TEXT NOT NULL REFERENCES profiles, status TEXT NOT NULL,
 sha256 TEXT REFERENCES code_blobs, origin TEXT, syntax_valid INTEGER, syntax_error TEXT,
 source_metrics_json TEXT NOT NULL, UNIQUE(task_id,variant,stage));
CREATE TABLE measurements(artifact_id TEXT NOT NULL REFERENCES artifacts, tool TEXT NOT NULL,
 status TEXT NOT NULL, seconds REAL, error TEXT, details_json TEXT NOT NULL,
 PRIMARY KEY(artifact_id,tool));
CREATE TABLE metric_values(artifact_id TEXT NOT NULL, tool TEXT NOT NULL, metric TEXT NOT NULL,
 value REAL NOT NULL, PRIMARY KEY(artifact_id,tool,metric),
 FOREIGN KEY(artifact_id,tool) REFERENCES measurements);
CREATE TABLE function_results(artifact_id TEXT NOT NULL, tool TEXT NOT NULL, kind TEXT NOT NULL,
 ordinal INTEGER NOT NULL, name TEXT NOT NULL, line_start INTEGER, line_end INTEGER,
 complexity REAL, details_json TEXT NOT NULL, PRIMARY KEY(artifact_id,tool,kind,ordinal),
 FOREIGN KEY(artifact_id,tool) REFERENCES measurements);
CREATE TABLE detections(artifact_id TEXT NOT NULL REFERENCES artifacts, detector TEXT NOT NULL,
 status TEXT NOT NULL, detected INTEGER, verdict TEXT, p REAL, n_grades INTEGER,
 error TEXT, reapplied_sha256 TEXT REFERENCES code_blobs, raw_json TEXT NOT NULL,
 PRIMARY KEY(artifact_id,detector),
 CHECK(detected IS NULL OR detected IN (0,1)),
 CHECK((status='ok' AND detected IS NOT NULL) OR (status<>'ok' AND detected IS NULL)));
CREATE TABLE watermark_runs(task_id INTEGER NOT NULL REFERENCES tasks, method TEXT NOT NULL,
 status TEXT NOT NULL, changed INTEGER, raw_json TEXT NOT NULL, PRIMARY KEY(task_id,method));
CREATE TABLE audit_stages(task_id INTEGER NOT NULL REFERENCES tasks, stage TEXT NOT NULL,
 valid INTEGER NOT NULL, error TEXT, PRIMARY KEY(task_id,stage));
CREATE TABLE audit_artifacts(task_id INTEGER NOT NULL REFERENCES tasks, stage TEXT NOT NULL,
 sha256 TEXT NOT NULL REFERENCES code_blobs, PRIMARY KEY(task_id,stage));
CREATE TABLE transformations(kind TEXT NOT NULL, before_id TEXT NOT NULL REFERENCES artifacts,
 after_id TEXT NOT NULL REFERENCES artifacts, status TEXT NOT NULL, bytes_changed INTEGER,
 lines_removed INTEGER, lines_added INTEGER, ast_equal INTEGER, byte_delta INTEGER,
 PRIMARY KEY(kind,before_id,after_id));
CREATE TABLE findings(finding_id TEXT PRIMARY KEY, severity TEXT NOT NULL,
 title TEXT NOT NULL, explanation TEXT NOT NULL, evidence TEXT NOT NULL);
CREATE INDEX artifacts_group ON artifacts(variant,stage,task_id);
CREATE INDEX metric_group ON metric_values(tool,metric,artifact_id);
CREATE INDEX detection_group ON detections(detector,status,detected);
CREATE VIEW v_artifact_code AS SELECT a.*,b.content AS code FROM artifacts a
 LEFT JOIN code_blobs b USING(sha256);
CREATE VIEW v_quality AS SELECT a.task_id,a.variant,a.stage,m.tool,m.status,
 v.metric,v.value FROM artifacts a JOIN measurements m USING(artifact_id)
 LEFT JOIN metric_values v ON v.artifact_id=m.artifact_id AND v.tool=m.tool;
CREATE VIEW v_watermark_pairs AS
 SELECT a.task_id,a.variant AS method,a.stage,x.tool,x.metric,y.value AS before,
 x.value AS after,x.value-y.value AS delta
 FROM artifacts a JOIN artifacts b ON b.task_id=a.task_id AND b.variant='original' AND b.stage=a.stage
 JOIN metric_values x ON x.artifact_id=a.artifact_id
 JOIN metric_values y ON y.artifact_id=b.artifact_id AND y.tool=x.tool AND y.metric=x.metric
 JOIN measurements mx ON mx.artifact_id=a.artifact_id AND mx.tool=x.tool AND mx.status='ok'
 JOIN measurements my ON my.artifact_id=b.artifact_id AND my.tool=x.tool AND my.status='ok'
 WHERE a.variant IN ('acw','sew');
CREATE VIEW v_common_watermark_pairs AS SELECT p.* FROM v_watermark_pairs p
 WHERE EXISTS(SELECT 1 FROM v_watermark_pairs q WHERE q.task_id=p.task_id AND q.stage=p.stage
 AND q.tool=p.tool AND q.metric=p.metric AND q.method<>p.method);
CREATE VIEW v_ruff_quality_pairs AS
 SELECT a.task_id,a.variant,a.stage,x.tool,x.metric,y.value AS before,x.value AS after,
 x.value-y.value AS delta FROM artifacts a JOIN artifacts b
 ON b.task_id=a.task_id AND b.variant=a.variant AND b.stage='before'
 JOIN metric_values x ON x.artifact_id=a.artifact_id
 JOIN metric_values y ON y.artifact_id=b.artifact_id AND y.tool=x.tool AND y.metric=x.metric
 JOIN measurements mx ON mx.artifact_id=a.artifact_id AND mx.tool=x.tool AND mx.status='ok'
 JOIN measurements my ON my.artifact_id=b.artifact_id AND my.tool=x.tool AND my.status='ok'
 WHERE a.stage<>'before';
CREATE VIEW v_detection_transitions AS
 SELECT a.task_id,a.variant,a.stage,x.detector,y.status AS before_status,x.status AS after_status,
 y.detected AS before_detected,x.detected AS after_detected,
 CASE WHEN y.status<>'ok' OR x.status<>'ok' THEN 'unavailable'
 WHEN y.detected=1 AND x.detected=0 THEN 'lost'
 WHEN y.detected=0 AND x.detected=1 THEN 'gained'
 WHEN y.detected=1 AND x.detected=1 THEN 'retained'
 ELSE 'not_detected_both' END AS transition
 FROM artifacts a JOIN artifacts b ON b.task_id=a.task_id AND b.variant=a.variant AND b.stage='before'
 JOIN detections x ON x.artifact_id=a.artifact_id
 JOIN detections y ON y.artifact_id=b.artifact_id AND y.detector=x.detector
 WHERE a.stage<>'before';
CREATE VIEW v_ruff_diagnostics AS
 SELECT m.artifact_id,profile.key AS profile,json_extract(d.value,'$.code') AS code,
 json_extract(d.value,'$.message') AS message,
 json_extract(d.value,'$.location.row') AS line,
 json_extract(d.value,'$.location.column') AS column_number,d.value AS raw_json
 FROM measurements m,json_each(m.details_json) profile,
 json_each(profile.value,'$.diagnostics') d WHERE m.tool='ruff';
CREATE VIEW v_transformations AS SELECT b.task_id,a.variant,a.stage,t.* FROM transformations t
 JOIN artifacts b ON b.artifact_id=t.before_id JOIN artifacts a ON a.artifact_id=t.after_id;
'''


def encode(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False)


def export_query(db, path, query):
    result = db.execute(query)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow([column[0] for column in result.description])
        writer.writerows(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True, help='Watermarked MBPP dataset')
    parser.add_argument('--detections', type=Path, required=True)
    parser.add_argument('--quality', type=Path, required=True)
    parser.add_argument('--audit', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root, detection, quality, audit, out = [getattr(args, name).resolve()
        for name in ('input', 'detections', 'quality', 'audit', 'out')]
    dmeta = json.loads((detection / 'metadata.json').read_text())
    qmeta = json.loads((quality / 'metadata.json').read_text())
    if dmeta['input'] != str(root) or qmeta['input'] != str(detection):
        parser.error('Input provenance differs')
    if qmeta['task_ids'] != dmeta['task_ids']:
        parser.error('Different task selections')
    selected_ids=set(dmeta['task_ids'])
    if not (quality / 'summary.json').exists() or not (detection / 'summary.json').exists():
        parser.error('Measurements/detections are not finished')
    out.mkdir(parents=True, exist_ok=False)
    (out / 'exports').mkdir()
    (out / 'provenance').mkdir()
    db_path = out / 'knowledge.sqlite'
    db = sqlite3.connect(db_path)
    db.executescript(SCHEMA)
    for key, value in [('dataset', json.loads((root/'metadata.json').read_text())),
                       ('detections', dmeta), ('quality', qmeta),
                       ('audit', json.loads((audit/'summary.json').read_text()))]:
        db.execute('INSERT INTO metadata VALUES (?,?)', (key, encode(value)))
    for line in (root/'dataset.jsonl').read_text().splitlines():
        task = json.loads(line)
        if task['task_id'] not in selected_ids:
            continue
        db.execute('INSERT INTO tasks VALUES (?,?,?,?,?,?)',
                   (task['task_id'],task['text'],encode(task['test_list']),task.get('test_setup_code'),
                    encode(task.get('challenge_test_list',[])),encode(task)))
    for stage, description in dmeta['profiles'].items():
        db.execute('INSERT INTO profiles VALUES (?,?)', (stage,description))
    inventory = json.loads((quality/'artifacts.json').read_text())
    completed = {row['artifact_id']:row for row in
                 map(json.loads,(quality/'measurements.jsonl').read_text().splitlines())}
    if set(completed) != {a['artifact_id'] for a in inventory}:
        raise RuntimeError('Measurement inventory is incomplete')
    for index, artifact in enumerate(inventory,1):
        row = completed[artifact['artifact_id']]
        if row['sha256'] != artifact['sha256']:
            raise RuntimeError(f'Changed measured artifact: {artifact["artifact_id"]}')
        if artifact['status']=='available':
            data = Path(artifact['path']).read_bytes()
            if hashlib.sha256(data).hexdigest()!=artifact['sha256']:
                raise RuntimeError(f'Changed source bytes: {artifact["path"]}')
            db.execute('INSERT OR IGNORE INTO code_blobs VALUES (?,?,?)',
                       (artifact['sha256'],data,len(data)))
        db.execute('INSERT INTO artifacts VALUES (?,?,?,?,?,?,?,?,?,?)',
            (artifact['artifact_id'],artifact['task_id'],artifact['source'],artifact['stage'],
             artifact['status'],artifact['sha256'],artifact['path'],row['syntax']['valid'],
             row['syntax'].get('error') or artifact.get('error'),encode(row['source_metrics'])))
        for result in row['measurements']:
            tool = result['tool']
            details = result.get('details',{})
            db.execute('INSERT INTO measurements VALUES (?,?,?,?,?,?)',
                (artifact['artifact_id'],tool,result['status'],result['seconds'],
                 result.get('error'),encode(details)))
            for metric, value in result['metrics'].items():
                db.execute('INSERT INTO metric_values VALUES (?,?,?,?)',
                           (artifact['artifact_id'],tool,metric,value))
            for kind in ('functions','classes'):
                for ordinal, function in enumerate(details.get(kind,[])):
                    db.execute('INSERT INTO function_results VALUES (?,?,?,?,?,?,?,?,?)',
                        (artifact['artifact_id'],tool,kind,ordinal,function['name'],
                         function['line_start'],function['line_end'],function['complexity'],encode(function)))
        if index % 2000==0:
            print(f'Imported {index}/{len(inventory)} artifacts',flush=True)
    for line in (detection/'results.jsonl').read_text().splitlines():
        row = json.loads(line)
        artifact_id = f'{row["source"]}:{row["stage"]}:{row["task_id"]}'
        actual = db.execute('SELECT sha256 FROM artifacts WHERE artifact_id=?',(artifact_id,)).fetchone()
        if actual is None or actual[0]!=row['input_sha256']:
            raise RuntimeError(f'Detection hash differs: {artifact_id}')
        if row.get('reapplied_file'):
            data = (detection/row['reapplied_file']).read_bytes()
            if hashlib.sha256(data).hexdigest()!=row['reapplied_sha256']:
                raise RuntimeError(f'Changed detection output: {artifact_id}')
            db.execute('INSERT OR IGNORE INTO code_blobs VALUES (?,?,?)',
                       (row['reapplied_sha256'],data,len(data)))
        db.execute('INSERT INTO detections VALUES (?,?,?,?,?,?,?,?,?,?)',
            (artifact_id,row['detector'],row['status'],row['detected'],row.get('verdict'),
             row.get('p'),row.get('n_grades'),row.get('error'),row.get('reapplied_sha256'),encode(row)))
    for line in (root/'results.jsonl').read_text().splitlines():
        row=json.loads(line)
        if row['task_id'] not in selected_ids:
            continue
        db.execute('INSERT INTO watermark_runs VALUES (?,?,?,?,?)',
                   (row['task_id'],row['method'],row['status'],row.get('changed'),encode(row)))
    for line in (audit/'results.jsonl').read_text().splitlines():
        row=json.loads(line)
        if row['task_id'] not in selected_ids:
            continue
        for stage, value in row['phases'].items():
            db.execute('INSERT INTO audit_stages VALUES (?,?,?,?)',
                       (row['task_id'],stage,value['valid'],value.get('error')))
        for stage,path in [('sourcery',root/'stages/embed/input'/f"{row['task_id']}.py"),
                           ('before_tabs',audit/'before_tabs'/f"{row['task_id']}.py")]:
            data=path.read_bytes()
            sha=hashlib.sha256(data).hexdigest()
            db.execute('INSERT OR IGNORE INTO code_blobs VALUES (?,?,?)',(sha,data,len(data)))
            db.execute('INSERT INTO audit_artifacts VALUES (?,?,?)',(row['task_id'],stage,sha))
    blobs={sha:bytes(data) for sha,data in db.execute('SELECT sha256,content FROM code_blobs')}
    ast_cache={}
    for artifact_id,task_id,variant,stage,sha,valid in db.execute(
            'SELECT artifact_id,task_id,variant,stage,sha256,syntax_valid FROM artifacts').fetchall():
        if stage=='before' and variant=='original':
            continue
        kind='watermark' if stage=='before' else 'ruff'
        before_id=f'original:before:{task_id}' if kind=='watermark' else f'{variant}:before:{task_id}'
        before_sha,before_valid=db.execute('SELECT sha256,syntax_valid FROM artifacts WHERE artifact_id=?',
                                          (before_id,)).fetchone()
        if sha is None or before_sha is None:
            values=('preprocessing_error',None,None,None,None,None)
        else:
            before,after=blobs[before_sha],blobs[sha]
            removed=added=0
            for tag,i,j,k,end in difflib.SequenceMatcher(None,before.splitlines(keepends=True),
                                                         after.splitlines(keepends=True),autojunk=False).get_opcodes():
                if tag!='equal':
                    removed+=j-i
                    added+=end-k
            equal=None
            if valid and before_valid:
                for key in (before_sha,sha):
                    if key not in ast_cache:
                        ast_cache[key]=ast.dump(ast.parse(blobs[key]),include_attributes=False)
                equal=ast_cache[before_sha]==ast_cache[sha]
            values=('ok',before!=after,removed,added,equal,len(after)-len(before))
        db.execute('INSERT INTO transformations VALUES (?,?,?,?,?,?,?,?,?)',
                   (kind,before_id,artifact_id,*values))
    findings = [
        ('acw_tabs','limitation','395 błędów powstaje w konwersji wcięć',
         'Reguła 45 usuwa resztę z dzielenia liczby początkowych spacji przez 4. Bibliotek nie naprawiano.',
         'audit_stages; results/acw_stage_audit/diagnosis.md'),
        ('acw_sourcery','limitation','Dwa pliki są błędne już po Sourcery',
         'ID 323 i 515; nie ustalono jeszcze konkretnej reguły Sourcery odpowiedzialnej za zmianę.', 'audit_stages'),
        ('acw_config','limitation','Konfiguracja ACW jest rekonstrukcją',
         'Brak oryginalnej .sourcery.yaml. Wyniki dotyczą zapisanej implementacji i konfiguracji, nie pełnej replikacji publikacji.',
         'provenance/acw.sourcery.yaml; metadata'),
        ('reference_code','scope','Znakowano rozwiązania referencyjne MBPP',
         '974 gotowe rozwiązania; nie wygenerowano kodu LLM. Nie wykonywano testów funkcjonalnych.', 'tasks; metadata'),
        ('sew_minimum','corrected','Wykrycie SEW wymaga pełnego werdyktu',
         'Samo p<0.01 zawyżało licznik z 708 do 908. Obecne dane respektują minimum pięciu obserwacji i zachowują Insufficient evidence.',
         'detections; results/mbpp_full_complete/detection_count_correction.json'),
        ('exact_bytes','corrected','CRLF/LF muszą pozostać niezmienione przy odczycie',
         'Wszystkie kanoniczne pomiary i detekcje odnoszą się do zapisanych bajtów i SHA-256, bez normalizacji read_text.',
         'code_blobs; artifacts; metadata'),
        ('ruff_profiles','scope','Formatter i linter to osobne interwencje',
         'Nazwy ruff_default i ruff_strict pochodzą z wcześniejszego planu. Pierwsza oznacza tylko formatter. '
         'Nowe profile ruff_lint_* nie formatują. Repo-max używa obecnych prefiksów repozytorium, nie historycznego zestawu 369 reguł.',
         'profiles'),
    ]
    db.executemany('INSERT INTO findings VALUES (?,?,?,?,?)',findings)
    assert not db.execute('PRAGMA foreign_key_check').fetchall()
    assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
    db.commit()
    exports = {
        'quality_values.csv': 'SELECT * FROM v_quality ORDER BY task_id,variant,stage,tool,metric',
        'watermark_quality_pairs.csv': 'SELECT * FROM v_watermark_pairs ORDER BY stage,tool,metric,method,task_id',
        'ruff_quality_pairs.csv': 'SELECT * FROM v_ruff_quality_pairs ORDER BY stage,tool,metric,variant,task_id',
        'tool_statuses.csv': 'SELECT a.task_id,a.variant,a.stage,m.tool,m.status,m.error FROM artifacts a JOIN measurements m USING(artifact_id) ORDER BY a.task_id,a.variant,a.stage,m.tool',
        'detections.csv': 'SELECT a.task_id,a.variant,a.stage,d.detector,d.status,d.detected,d.verdict,d.p,d.n_grades,a.syntax_valid,a.sha256,d.error FROM detections d JOIN artifacts a USING(artifact_id) ORDER BY a.task_id,a.variant,a.stage,d.detector',
        'detection_transitions.csv': 'SELECT * FROM v_detection_transitions ORDER BY task_id,variant,stage,detector',
        'functions.csv': 'SELECT a.task_id,a.variant,a.stage,f.tool,f.kind,f.name,f.line_start,f.line_end,f.complexity FROM function_results f JOIN artifacts a USING(artifact_id) ORDER BY a.task_id,a.variant,a.stage,f.tool,f.kind,f.ordinal',
        'syntax_failures.csv': 'SELECT task_id,variant,stage,syntax_error FROM artifacts WHERE syntax_valid=0 ORDER BY task_id,variant,stage',
        'transformations.csv': 'SELECT * FROM v_transformations ORDER BY task_id,variant,stage',
    }
    for name, query in exports.items():
        export_query(db,out/'exports'/name,query)
    for src,name in [(root/'acw.sourcery.yaml','acw.sourcery.yaml'),
                     (Path('SEW/sew/q_table.json'),'sew_q_table.json'),
                     (Path('ACW/source/ruff.toml'),'ruff_repo.toml'),
                     (detection/'metadata.json','detection_metadata.json'),
                     (quality/'metadata.json','quality_metadata.json'),
                     (audit/'summary.json','acw_audit_summary.json')]:
        shutil.copy2(src,out/'provenance'/name)
    runtime = json.loads((quality/'metadata.json').read_text())['implementation_sha256']
    if hashlib.sha256(Path('research_metrics.py').read_bytes()).hexdigest()!=runtime:
        raise RuntimeError('Measurement implementation changed after execution')
    source_files = sorted(Path('.').glob('*.py'))+sorted(Path('.').glob('requirements*.txt'))
    source_files += sorted(Path('SEW/sew').rglob('*.py'))+[Path('SEW/sew/q_table.json')]
    source_files += [Path('ACW/source')/name for name in ('base_ast.py','one_rule_format.py','formatting.py','refact_list.py')]
    source_hashes = {}
    for path in source_files:
        target=out/'provenance/source_snapshot'/path
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,target)
        source_hashes[str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
    write_json(out/'provenance/source_hashes.json',source_hashes)
    inputs={str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in [
        root/'dataset.jsonl',root/'results.jsonl',detection/'results.jsonl',
        quality/'measurements.jsonl',audit/'results.jsonl']}
    write_json(out/'provenance/input_hashes.json',inputs)
    counts={name:db.execute(f'SELECT COUNT(*) FROM {name}').fetchone()[0]
            for name in ('tasks','artifacts','code_blobs','measurements','metric_values',
                         'function_results','detections','watermark_runs','audit_stages',
                         'audit_artifacts','transformations')}
    write_json(out/'build.json',dict(counts=counts,database_sha256=hashlib.sha256(db_path.read_bytes()).hexdigest(),
               reports_complete=False,validation_complete=False))
    db.close()
    print(json.dumps(counts,indent=2),flush=True)


if __name__=='__main__':
    main()
