#!/usr/bin/env python3
"""Bounded deterministic restoration; no archived source is executed."""
import argparse,base64,hashlib,itertools,json,lzma
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);a=ap.parse_args()
base=Path(__file__).resolve().parent;idx=json.loads((base/'bundle-index.json').read_text())
payload=''.join((base/p).read_text() for p in idx['parts'])
dec=lzma.LZMADecompressor();raw=dec.decompress(base64.b64decode(payload,validate=True),max_length=idx['max_decoded_bytes']+1)
assert dec.eof and not dec.unused_data and len(raw)<=idx['max_decoded_bytes']
assert hashlib.sha256(raw).hexdigest()==idx['decoded_json_sha256']
files=json.loads(raw);assert set(files)=={r['path'] for r in idx['files']}
out=Path(a.out);assert not out.exists();out.mkdir(parents=True)
for entry in idx['files']:
    name=entry['path'];rel=Path(name);assert not rel.is_absolute() and '..' not in rel.parts
    v=files[name]
    if isinstance(v,dict):
        assert v['codec']=='cnf-recipe-v1' and name=='global-example.cnf'
        n=v['n'];edges=v['edges'];assert n==24 and len(edges)==36
        B=[x for x in range(32) if x.bit_count()%2==0];S=[31^(1<<i) for i in range(5)]
        var=lambda u,c:16*u+c+1
        clauses=[]
        for u in range(n):
            clauses.append([var(u,c) for c in range(16)])
            clauses.extend([[-var(u,c),-var(u,d)] for c,d in itertools.combinations(range(16),2)])
        for u,w in edges:
            for x,y in ((u,w),(w,u)):
                for c,b in enumerate(B):clauses.append([-var(x,c)]+[var(y,d) for d,e in enumerate(B) if b^e in S])
        clauses.append([1]);v='p cnf 384 '+str(len(clauses))+'\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)
    data=v.encode();assert len(data)==entry['bytes'] and hashlib.sha256(data).hexdigest()==entry['sha256']
    p=out/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
print(json.dumps({'status':'integrity_restore_pass','files':len(files),'verdict':'candidate_only'}))
