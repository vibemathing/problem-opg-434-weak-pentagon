#!/usr/bin/env python3
"""Restore exact per-state witness tables and retained run records; no CSP search.
The small coordinate-permutation templates are a lossless representation of
this particular generated table. The separate checker verifies every restored row.
"""
import argparse, base64, hashlib, itertools, json, lzma, pathlib

def digest(b): return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--bundle',default='certificates.bundle.json')
    ap.add_argument('--spec',default='patches.json'); ap.add_argument('--out',default='decoded'); a=ap.parse_args()
    dst=pathlib.Path(a.out)
    if dst.is_absolute() or '..' in dst.parts or dst.exists(): raise ValueError('fresh relative output directory required')
    bundle=json.loads(pathlib.Path(a.bundle).read_text()); specraw=pathlib.Path(a.spec).read_bytes()
    if digest(specraw)!=bundle['spec_sha256']: raise ValueError('spec digest')
    spec=json.loads(specraw); packed=base64.b64decode(bundle['xz_base64'],validate=True)
    dec=lzma.LZMADecompressor(memlimit=67108864); raw=dec.decompress(packed,max_length=2097153)
    if len(raw)>2097152 or not dec.eof or dec.unused_data: raise ValueError('bounded payload decode')
    objects=json.loads(raw); expected={q['path']:q for q in bundle['files']}
    if set(objects)!=set(expected): raise ValueError('payload path coverage')
    out={}
    for name,text in objects.items():
        path=pathlib.PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts: raise ValueError('unsafe logical path')
        b=text.encode(); q=expected[name]
        if len(b)!=q['bytes'] or digest(b)!=q['sha256']: raise ValueError('logical file digest')
        out[name]=b
    B=[m for m in range(32) if m.bit_count()%2==0]; index={v:i for i,v in enumerate(B)}
    actions=[[index[sum(1<<pi[i] for i in range(5) if m>>i&1)] for m in B]
             for pi in itertools.permutations(range(5))]
    for tag in ('r11','r12'):
        p=spec['patches'][tag]; seeds=json.loads(out[tag+'/'+tag+'.seeds.json']); dictionary={}
        for seed in seeds:
            for pi in actions:
                pins=tuple(pi[v] for v in seed['pins']); witness=tuple(pi[v] for v in seed['witness'])
                dictionary.setdefault(pins,witness)
        rows=[]
        for rest in itertools.product(range(16),repeat=len(p['ports'])-1):
            pins=(0,)+rest
            if all(pins[i]!=pins[j] for i,j in p['inequalities']):
                rows.append(''.join(format(v,'x') for v in dictionary[pins])+'\n')
        b=''.join(rows).encode(); want=bundle['expanded_tables'][tag]
        if len(rows)!=want['rows'] or len(b)!=want['bytes'] or digest(b)!=want['sha256']: raise ValueError('expanded table digest')
        out[tag+'/'+tag+'.witnesses.txt']=b
    if any(len(b)>1048576 for b in out.values()) or sum(map(len,out.values()))>5242880: raise ValueError('output budget')
    dst.mkdir()
    for name,b in out.items():
        path=dst/name; path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(b)
    print(json.dumps({'status':'exact_restore_pass','verdict':'candidate_only','files':len(out),
                      'bytes':sum(map(len,out.values())),'tables':bundle['expanded_tables']}))
if __name__=='__main__': main()
