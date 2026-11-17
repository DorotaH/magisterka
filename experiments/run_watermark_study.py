#!/usr/bin/env python3
"""Reproducible pilot: set PYTHONPATH and PATH to installed dependencies."""
import ast, contextlib, io, json, os, shutil, subprocess, sys, tempfile
from collections import Counter
from pathlib import Path
import pyarrow.parquet as pq
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'SEW'),str(ROOT/'ACW/source')]
from sew import embed, detect
from one_rule_format import reorder_process, reformatting_process, tab_convert_process
KEY=bytes.fromhex('76'*16)
OUT=ROOT/'results/watermark_study'
DATA=Path(os.environ.get('WATERMARK_DATA','/tmp/watermark-data'))
LIMIT=int(os.environ.get('WATERMARK_LIMIT','20'))
def run(args):
    return subprocess.run(args, text=True, capture_output=True, timeout=60)
def local_acw(path):
    # Same locally available steps as RQ1 process; Sourcery step is absent.
    with contextlib.redirect_stdout(io.StringIO()):
        for i in range(36,40): reorder_process(i,str(path))
        for i in range(40,45): reformatting_process(i,str(path))
        tab_convert_process(45,str(path))
def acw_detect(code):
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'sample.py'; p.write_text(code,encoding='utf-8'); local_acw(p)
        return {'fixed_point':p.read_text(encoding='utf-8')==code, 'scope':'partial ACW: rules 36-45 only'}
def rows():
    b=pq.read_table(DATA/'bigcode.parquet',columns=['task_id','complete_prompt','canonical_solution']).to_pylist()
    yield 'bigcodebench',[(x['task_id'],x['complete_prompt']+x['canonical_solution']+'\n') for x in b[:LIMIT]]
    selection=json.loads((ROOT/'SEW/scripts/codecontests_selection.json').read_text())['python'][:LIMIT]
    tables={s:pq.read_table(DATA/(s+'.parquet'),columns=['solutions']).to_pylist() for s in ['valid','test']}
    data=[]
    for pid,k in selection:
        _,split,index=pid.split('/'); sol=tables[split][int(index)]['solutions']; assert sol['language'][k]==3
        data.append((pid,sol['solution'][k]))
    yield 'codecontests',data

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    results=[]
    for dataset, entries in rows():
      for idx,(ident,code) in enumerate(entries):
       base=OUT/dataset/f'{idx:03d}'; base.mkdir(parents=True,exist_ok=True)
       (base/'original.py').write_text(code,encoding='utf-8')
       for method in ['sew','acw_partial']:
        folder=base/method; folder.mkdir(exist_ok=True)
        p=folder/'watermarked.py'; p.write_text(code,encoding='utf-8')
        item={'dataset':dataset,'id':ident,'method':method,'original':str((base/'original.py').relative_to(OUT))}
        try:
         ast.parse(code)
         if method=='sew':
          e=embed(code,'python',KEY); p.write_text(e.pop('code'),encoding='utf-8'); item['embedding']=e
         else:
          local_acw(p); item['embedding']={'changed':p.read_text(encoding='utf-8')!=code,'scope':'partial ACW: rules 36-45; no Sourcery'}
         marked=p.read_text(encoding='utf-8'); item['changed']=marked!=code
         try: ast.parse(marked); item['watermarked_valid_python']=True
         except SyntaxError as ex: item['watermarked_valid_python']=False; item['syntax_error']=str(ex)
         detector= (lambda x:detect(x,'python',KEY)) if method=='sew' else acw_detect
         item['detection_before']=detector(marked)
         item['ruff']={}
         for profile in ['default','strict']:
          target=folder/f'ruff_{profile}.py'; target.write_text(marked,encoding='utf-8')
          opts=['--isolated']+(['--select','E,F,W,I,B,UP,SIM'] if profile=='strict' else [])
          check=run(['ruff','check',*opts,'--output-format','json',str(target)])
          if check.returncode not in (0,1): raise RuntimeError('ruff check: '+check.stderr)
          diagnostics=json.loads(check.stdout)
          (folder/f'ruff_{profile}_diagnostics.json').write_text(json.dumps(diagnostics,ensure_ascii=False,indent=2),encoding='utf-8')
          fix=run(['ruff','check',*opts,'--fix',str(target)])
          fmt=run(['ruff','format','--isolated',str(target)])
          after=target.read_text(encoding='utf-8')
          item['ruff'][profile]={'diagnostics':len(diagnostics),'codes':dict(Counter(x['code'] for x in diagnostics)),'changed_by_ruff':after!=marked,'detection_after':detector(after),'fix_stdout':fix.stdout,'format_stdout':fmt.stdout,'fix_exit':fix.returncode,'format_exit':fmt.returncode,'fix_stderr':fix.stderr,'format_stderr':fmt.stderr}
         for tool,cmd in [('radon_cc',['radon','cc','-j',str(p)]),('radon_mi',['radon','mi','-j',str(p)]),('radon_raw',['radon','raw','-j',str(p)]),('complexipy',['complexipy','--isolated','--no-ignore','--output-format','json','--output',str(folder/'complexipy.json'),str(p)])]:
          x=run(cmd); (folder/(tool+'.out')).write_text(x.stdout,encoding='utf-8'); (folder/(tool+'.err')).write_text(x.stderr,encoding='utf-8'); item[tool+'_exit']=x.returncode
        except Exception as ex: item['error']=repr(ex)
        results.append(item)
       print(dataset,idx+1,ident,flush=True)
       (OUT/'results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
if __name__=='__main__': main()
