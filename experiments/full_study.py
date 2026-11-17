#!/usr/bin/env python3
"""Full corpus experiment, staged so Sourcery is applied identically for ACW detection."""
import ast, contextlib, io, json, os, shutil, subprocess, sys, tempfile, concurrent.futures, traceback, threading
from collections import Counter
from pathlib import Path
import pyarrow.parquet as pq
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'SEW'),str(ROOT/'ACW/source')]
from sew import embed, detect
from one_rule_format import tab_convert_process
from base_ast import transform_operations_add, transform_operations_mult, transform_comparison_LG, transform_comparison_LGE
from refact_list import refactoring_list
import autopep8
OUT=ROOT/'results/full_watermark_study'; DATA=Path(os.environ.get('WATERMARK_DATA','/tmp/watermark-data'))
WORKERS=int(os.environ.get('WATERMARK_WORKERS','8')); KEY=bytes.fromhex('76'*16)
CONFIG=OUT/'acw_sourcery.yaml'
ACW_LOCK=threading.Lock()

def command(args,timeout=120):
 return subprocess.run(args, stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=timeout)
def valid(code):
 try: ast.parse(code); return None
 except (SyntaxError,ValueError,TypeError) as e: return str(e)
def acw_local(p):
 logs=io.StringIO()
 with ACW_LOCK, contextlib.redirect_stdout(logs),contextlib.redirect_stderr(logs):
  # The published wrapper passes obsolete arguments; call its actual CST functions.
  for transform in (transform_operations_add, transform_operations_mult, transform_comparison_LG, transform_comparison_LGE): transform(str(p))
  # These are the same five select groups and default options as ACW's autopep8 CLI.
  groups=['E225,E226,E227,E228,E241,E242,E251,E252,E231','E27','E123','W292','E301,E302,E305,E306']
  for select in groups:
   c=p.read_text(encoding='utf8'); p.write_text(autopep8.fix_code(c,options={'select':select.split(',')}),encoding='utf8')
  tab_convert_process(45,str(p))
 return logs.getvalue()
def specimens():
 b=pq.read_table(DATA/'bigcode.parquet',columns=['task_id','complete_prompt','canonical_solution']).to_pylist()
 for i,x in enumerate(b): yield 'bigcodebench',i,x['task_id'],x['complete_prompt']+x['canonical_solution']+'\n'
 sel=json.loads((ROOT/'SEW/scripts/codecontests_selection.json').read_text())['python']
 tabs={s:pq.read_table(DATA/(s+'.parquet'),columns=['solutions']).to_pylist() for s in ('valid','test')}
 for i,(ident,k) in enumerate(sel):
  _,s,n=ident.split('/'); sol=tabs[s][int(n)]['solutions']; assert sol['language'][k]==3
  yield 'codecontests',i,ident,sol['solution'][k]
def parallel(fn,items,label):
 print(label, 'total',len(items),flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
  for n,result in enumerate(pool.map(fn,items),1):
   if n%100==0 or n==len(items): print(label,n,'/',len(items),flush=True)
def sourcery(path,label):
 print('Sourcery',label,flush=True)
 p=command(['sourcery','review','--config',str(CONFIG),'--fix',str(path)],timeout=7200)
 (OUT/(label+'.stdout.txt')).write_text(p.stdout,encoding='utf8'); (OUT/(label+'.stderr.txt')).write_text(p.stderr,encoding='utf8')
 if p.returncode: raise RuntimeError(f'Sourcery {label} returned {p.returncode}: {p.stderr[-1000:]}')
def prep(row):
 ds,i,ident,code=row; base=OUT/ds/f'{i:04d}'; base.mkdir(parents=True,exist_ok=True)
 (base/'original.py').write_text(code,encoding='utf8')
 for method in ('sew','acw'):(base/method).mkdir(exist_ok=True)
 item={'dataset':ds,'index':i,'id':ident,'original_syntax_error':valid(code)}
 (base/'meta.json').write_text(json.dumps(item,ensure_ascii=False),encoding='utf8')
 # Sourcery gets a flat folder with stable filenames for all public samples.
 if item['original_syntax_error'] is None:
  (OUT/'acw_embedding'/f'{ds}_{i:04d}.py').write_text(code,encoding='utf8')
 return row

def analyze(row):
 ds,i,ident,code=row; base=OUT/ds/f'{i:04d}'; key=f'{ds}_{i:04d}.py'
 for method in ('sew','acw'):
  folder=base/method; item={'dataset':ds,'id':ident,'index':i,'method':method,'original_syntax_error':valid(code)}
  try:
   if item['original_syntax_error']:
    item['status']='invalid_original'; (folder/'result.json').write_text(json.dumps(item,ensure_ascii=False,indent=2)); continue
   if method=='sew':
    emb=embed(code,'python',KEY); marked=emb.pop('code'); item['embedding']=emb
   else:
    source=OUT/'acw_embedding'/key; shutil.copyfile(source,folder/'watermarked.py')
    (folder/'acw_local.log').write_text(acw_local(folder/'watermarked.py'),encoding='utf8')
    marked=(folder/'watermarked.py').read_text(encoding='utf8'); item['embedding']={'sourcery_applied':True}
   p=folder/'watermarked.py'; p.write_text(marked,encoding='utf8'); item['changed']=marked!=code
   item['syntax_error']=valid(marked)
   if method=='sew': item['detection_before']=detect(marked,'python',KEY)
   for tool,cmd in [('radon_cc',['radon','cc','-j',str(p)]),('radon_mi',['radon','mi','-j',str(p)]),('radon_raw',['radon','raw','-j',str(p)]),('complexipy',['complexipy','--isolated','--no-ignore','--output-format','json','--output',str(folder/'complexipy.json'),str(p)])]:
    z=command(cmd); (folder/(tool+'.out')).write_text(z.stdout,encoding='utf8'); (folder/(tool+'.err')).write_text(z.stderr,encoding='utf8'); item[tool+'_exit']=z.returncode
   item['ruff']={}
   for profile in ('default','strict'):
    target=folder/f'ruff_{profile}.py'; target.write_text(marked,encoding='utf8')
    opts=['--isolated']+(['--select','E,F,W,I,B,UP,SIM'] if profile=='strict' else [])
    z=command(['ruff','check',*opts,'--output-format','json',str(target)])
    if z.returncode not in (0,1): raise RuntimeError('ruff check: '+z.stderr)
    findings=json.loads(z.stdout); (folder/f'ruff_{profile}_diagnostics.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2),encoding='utf8')
    fix=command(['ruff','check',*opts,'--fix',str(target)]); fmt=command(['ruff','format','--isolated',str(target)])
    after=target.read_text(encoding='utf8'); result={'diagnostics':len(findings),'codes':dict(Counter(x['code'] for x in findings)),'fix_exit':fix.returncode,'format_exit':fmt.returncode,'fix_stderr':fix.stderr,'format_stderr':fmt.stderr,'syntax_error':valid(after)}
    if method=='sew': result['detection_after']=detect(after,'python',KEY)
    item['ruff'][profile]=result
   item['status']='ok'
  except Exception:
   item['status']='error'; item['error']=traceback.format_exc()
  (folder/'result.json').write_text(json.dumps(item,ensure_ascii=False,indent=2),encoding='utf8')

def prepare_detection(row):
 ds,i,ident,code=row; base=OUT/ds/f'{i:04d}'; folder=base/'acw'; item=json.loads((folder/'result.json').read_text())
 if item['status']!='ok':return
 for name,source in [('before','watermarked.py'),('default','ruff_default.py'),('strict','ruff_strict.py')]:
  p=folder/source
  if valid(p.read_text(encoding='utf8')) is None: shutil.copyfile(p,OUT/f'acw_detect_{name}'/f'{ds}_{i:04d}.py')
def finish_detection(row):
 ds,i,ident,code=row; folder=OUT/ds/f'{i:04d}'/'acw'; item=json.loads((folder/'result.json').read_text()); key=f'{ds}_{i:04d}.py'
 if item['status']!='ok': return
 for name,source in [('before','watermarked.py'),('default','ruff_default.py'),('strict','ruff_strict.py')]:
  p=OUT/f'acw_detect_{name}'/key
  if p.exists():
   log=acw_local(p); (folder/f'acw_detect_{name}.log').write_text(log,encoding='utf8')
   d={'fixed_point':p.read_bytes()==(folder/source).read_bytes(),'syntax_error_after_reapply':valid(p.read_text(encoding='utf8'))}
  else: d={'fixed_point':None,'reason':'invalid syntax before detection'}
  if name=='before':item['detection_before']=d
  else:item['ruff'][name]['detection_after']=d
 (folder/'result.json').write_text(json.dumps(item,ensure_ascii=False,indent=2),encoding='utf8')

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 CONFIG.write_text("version: '1'\nrule_settings:\n  enable:\n"+''.join('  - '+x+'\n' for x in refactoring_list),encoding='utf8')
 for name in ['acw_embedding','acw_detect_before','acw_detect_default','acw_detect_strict']:(OUT/name).mkdir(exist_ok=True)
 rows=list(specimens())
 if not os.environ.get('WATERMARK_REUSE_EMBEDDING'):
  parallel(prep,rows,'przygotowanie'); sourcery(OUT/'acw_embedding','sourcery_embedding')
 else:
  if not (OUT/'sourcery_embedding.stdout.txt').exists(): raise RuntimeError('Missing completed embedding stage')
 parallel(analyze,rows,'analiza'); parallel(prepare_detection,rows,'przygotowanie_detekcji')
 for name in ('before','default','strict'):sourcery(OUT/f'acw_detect_{name}',f'sourcery_detection_{name}')
 parallel(finish_detection,rows,'detekcja')
 result=[]
 for ds,i,ident,_ in rows:
  for method in ('sew','acw'):result.append(json.loads((OUT/ds/f'{i:04d}'/method/'result.json').read_text()))
 (OUT/'results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf8')
 print('DONE',len(result),flush=True)
if __name__=='__main__':main()
