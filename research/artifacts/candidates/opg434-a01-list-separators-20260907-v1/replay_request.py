#!/usr/bin/env python3
"""Explicit candidate replay request, not a registered verifier or admission gate."""
import argparse,json,subprocess,sys
from pathlib import Path
from restore import restore
p=argparse.ArgumentParser();p.add_argument('--execute',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
if not a.execute:p.error('explicit --execute required in an authorized runtime')
root=Path(__file__).resolve().parent;print(json.dumps(restore(root,a.out)))
commands=[('check',['check.py','--generated','generated','--graph','graph22.input.json','--out','replayed-check.json']),('mutations',['mutations.py']),('projections',['check_projections.py']),('cap',['cap_lift.py']),('cap-pressure',['cap_pressure.py'])]
receipts=[]
for name,cmd in commands:
 receipt='new-replay/'+name+'.json';inp=[cmd[0],'graph22.input.json']
 argv=[sys.executable,'run_bounded.py','--receipt',receipt,'--inputs',*inp,'--',*cmd]
 r=subprocess.run(argv,cwd=a.out,timeout=45,capture_output=True,text=True)
 if r.returncode!=0:raise SystemExit('Replay did not pass: '+name)
 receipts.append(receipt)
print(json.dumps({'status':'candidate_replay_pass','receipts':receipts,'trusted_verifier':False,'root_closed':False,'verdict':'candidate_only'}))
