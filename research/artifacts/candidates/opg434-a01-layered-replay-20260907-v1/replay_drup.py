#!/usr/bin/env python3
"""Small standalone DRUP replayer. Reads actual DIMACS/proof bytes and checks
encoding against the full graph. Does not import the encoder or CSP checker.
"""
import argparse,hashlib,itertools,json
from pathlib import Path

def read_dimacs(raw):
    lines=raw.decode().splitlines();header=next(l for l in lines if l.startswith('p '))
    nv,nc=map(int,header.split()[2:]);cls=[]
    for l in lines:
        if not l or l[0] in 'cp':continue
        row=list(map(int,l.split()));assert row[-1]==0 and 0 not in row[:-1]
        cls.append(tuple(row[:-1]))
    assert len(cls)==nc and all(1<=abs(x)<=nv for c in cls for x in c)
    return nv,cls

def contradiction(cls,assumptions):
    values={}
    for x in assumptions:
        if abs(x) in values and values[abs(x)]!=(x>0):return True
        values[abs(x)]=(x>0)
    while True:
        old=len(values)
        for cl in cls:
            if any(values.get(abs(l))==(l>0) for l in cl if abs(l) in values):continue
            live=[l for l in cl if abs(l) not in values]
            if not live:return True
            if len(live)==1:values[abs(live[0])]=(live[0]>0)
        if len(values)==old:return False

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--graph',required=True);ap.add_argument('--cnf',required=True);ap.add_argument('--drup',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    raw=Path(a.cnf).read_bytes();proof=Path(a.drup).read_bytes();graw=Path(a.graph).read_bytes();g=json.loads(graw)
    nv,cls=read_dimacs(raw)
    bit=lambda x:tuple((x//2**i)%2 for i in range(5))
    labs=sorted(x for x in range(32) if sum(bit(x))%2==0);assert len(labs)==16
    var=lambda v,i:16*v+i+1
    expected=[]
    for v in range(g['n']):
        expected.append(tuple(var(v,i) for i in range(16)))
        expected.extend((-var(v,i),-var(v,j)) for i,j in itertools.combinations(range(16),2))
    for x,y in g['edges']:
        for u,v in ((x,y),(y,x)):
            for i,c in enumerate(labs):
                ns=[j for j,d in enumerate(labs) if sum(b!=e for b,e in zip(bit(c),bit(d)))==4]
                expected.append(tuple([-var(u,i)]+[var(v,j) for j in ns]))
    expected.extend((var(int(v),labs.index(c)),) for v,c in sorted(g['pins'].items(),key=lambda z:int(z[0])))
    assert cls==expected and nv==16*g['n']
    # An unjustified early addition must fail, even though the full formula is UNSAT.
    assert not contradiction(cls,[641])
    steps=0;empty=False
    for line in proof.decode().splitlines():
        ls=list(map(int,line.split()));assert ls[-1]==0 and all(1<=abs(x)<=nv for x in ls[:-1])
        c=tuple(ls[:-1]);assert contradiction(cls,[-x for x in c]),f'non-RUP row {steps+1}'
        cls.append(c);steps+=1;empty|=not c
    assert empty
    out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
    report={'verdict':'candidate_only','status':'standalone_drup_pass','version':'substitution-rup-1.0','variables':nv,'initial_clauses':len(expected),'proof_additions':steps,'empty_clause':empty,'full_graph_encoding_matches':True,'graph_sha256':hashlib.sha256(graw).hexdigest(),'cnf_sha256':hashlib.sha256(raw).hexdigest(),'drup_sha256':hashlib.sha256(proof).hexdigest(),'mutation':{'name':'M13_unjustified_RUP_addition','candidate_clause':[-641],'status':'expected_rejection'},'registered_verifier':False}
    (out/'replay.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n');print(json.dumps({'status':report['status'],'proof_additions':steps}));return 0
if __name__=='__main__':raise SystemExit(main())
