#!/usr/bin/env python3
"""Generate an explicit witness for EVERY normalized allowed belt boundary.
Candidate-only. No imported solver or checker. Run with an external resource limit.
"""
import argparse, hashlib, itertools, json, pathlib, time

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--spec',required=True)
    ap.add_argument('--patch',choices=['r11','r12'],required=True)
    ap.add_argument('--out',required=True); args=ap.parse_args()
    raw=pathlib.Path(args.spec).read_bytes(); spec=json.loads(raw)
    P=spec['patches'][args.patch]; n=len(P['vertices']); edges=P['edges']; ports=P['ports']
    B=[x for x in range(32) if x.bit_count()%2==0]; ix={x:i for i,x in enumerate(B)}
    S=set(spec['target']['generators']); adj=[sum(1<<j for j,y in enumerate(B) if x^y in S) for x in B]
    unions=[0]*65536
    for m in range(1,65536):
        bit=m & -m; unions[m]=unions[m^bit] | adj[bit.bit_length()-1]
    def propagate(ds):
        change=True
        while change:
            change=False
            for u,v in edges:
                for a,b in ((u,v),(v,u)):
                    z=ds[a] & unions[ds[b]]
                    if not z: return False
                    if z!=ds[a]: ds[a]=z; change=True
        return True
    nodes=0
    def search(ds):
        nonlocal nodes
        nodes+=1
        if not propagate(ds): return None
        choices=[v for v in range(n) if ds[v].bit_count()>1]
        if not choices: return tuple(d.bit_length()-1 for d in ds)
        u=min(choices,key=lambda v:(ds[v].bit_count(),v)); m=ds[u]
        while m:
            bit=m & -m; m^=bit; child=ds.copy(); child[u]=bit
            answer=search(child)
            if answer is not None: return answer
        return None
    transforms=[]
    for perm in itertools.permutations(range(5)):
        transforms.append([ix[sum(1<<perm[i] for i in range(5) if x & (1<<i))] for x in B])
    def states():
        for rest in itertools.product(range(16),repeat=len(ports)-1):
            a=(0,)+rest
            if all(a[i]!=a[j] for i,j in P['inequalities']): yield a
    witnesses={}; seeds=[]; started=time.monotonic()
    for pins in states():
        if pins in witnesses: continue
        domains=[65535]*n
        for port,label in zip(ports,pins): domains[port] &= adj[label]
        witness=search(domains)
        if witness is None:
            out={'status':'first_failed_boundary','patch':args.patch,'pins_indices':pins,
                 'pins_masks':[B[i] for i in pins],'patch_object':P,'search_nodes':nodes,
                 'scope':'first failed tuple in lexicographic normalized allowed enumeration; no root conclusion'}
            pathlib.Path(args.out).mkdir(parents=True,exist_ok=True)
            pathlib.Path(args.out,'first_failure.json').write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps(out)); return 2
        seeds.append({'pins':pins,'witness':witness})
        for transform in transforms:
            key=tuple(transform[x] for x in pins)
            witnesses.setdefault(key,tuple(transform[x] for x in witness))
    lines=[''.join(format(x,'x') for x in witnesses[a])+'\n' for a in states()]
    assert len(lines)==P['normalized_rows']==len(witnesses)
    out=pathlib.Path(args.out); out.mkdir(parents=True,exist_ok=False)
    table=''.join(lines).encode('ascii'); assert len(table)<=1048576
    (out/(args.patch+'.witnesses.txt')).write_bytes(table)
    seedraw=(json.dumps(seeds,separators=(',',':'))+'\n').encode()
    (out/(args.patch+'.seeds.json')).write_bytes(seedraw)
    report={'status':'all_normalized_boundaries_have_witness','verdict':'candidate_only',
            'patch':args.patch,'rows':len(lines),'orbit_seeds':len(seeds),'csp_nodes':nodes,
            'target_masks':B,'row_order':'lexicographic pins=(0,...) in target-index order; retain specified inequalities',
            'row_encoding':'one lowercase hex target index per internal vertex, followed by LF',
            'spec_sha256':hashlib.sha256(raw).hexdigest(),'table_sha256':hashlib.sha256(table).hexdigest(),
            'table_bytes':len(table),'seed_sha256':hashlib.sha256(seedraw).hexdigest(),
            'elapsed_seconds':time.monotonic()-started,'first_failed_boundary':None}
    (out/'generation.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report)); return 0
if __name__=='__main__': raise SystemExit(main())
