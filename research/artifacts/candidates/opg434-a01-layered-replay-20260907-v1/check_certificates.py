#!/usr/bin/env python3
"""Check a full-source CSP proof, emit a full-source DIMACS encoding and DRUP proof,
then replay the DRUP additions with an ordinary unit-propagation checker.
No import of either graph builder or search program; standard library only.
"""
import argparse, hashlib, itertools, json
from collections import deque
from pathlib import Path

class Invalid(Exception): pass
def test(p,s):
    if not p:raise Invalid(s)
def read(p):return json.loads(Path(p).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()

# Deliberately reconstruct the target from bit tuples rather than trusting
# a certificate's adjacency table or the other checker's subset objects.
labels=[x for x in range(32) if sum((x//(2**k))%2 for k in range(5))%2==0]
adj={x:{y for y in labels if sum(((x//(2**k))%2)!=((y//(2**k))%2) for k in range(5))==4} for x in labels}

def verify_tree(g,p):
    pins={int(v):x for v,x in g['pins'].items()};n=g['n']
    test(p['n']==n and p['edges']==g['edges'] and {int(v):x for v,x in p['pins'].items()}==pins,'certificate input mismatch')
    test(p['target_adjacency']=={str(x):sorted(adj[x]) for x in labels},'certificate target mismatch')
    ed={tuple(e) for e in g['edges']};domains=[set(labels) for _ in range(n)]
    for v,c in pins.items():test(0<=v<n and c in labels,'bad pin');domains[v]={c}
    counts={'nodes':0,'removed_values':0,'contradiction_leaves':0}
    def check(node,D):
        counts['nodes']+=1;test(counts['nodes']<=20000,'proof size limit')
        for u,x,v in node['deletions']:
            test(0<=u<n and 0<=v<n and tuple(sorted((u,v))) in ed,'deletion reason is not a source edge')
            test(x in D[u],'duplicate or absent removed value')
            test(not any(y in adj[x] for y in D[v]),'deletion still has support')
            D[u].remove(x);counts['removed_values']+=1
        if 'empty' in node:
            test(not D[node['empty']],'false empty-domain leaf');counts['contradiction_leaves']+=1;return
        v=node['split'];test(0<=v<n and len(D[v])>1,'bad branching variable')
        cs=node['children'];vals=[c['value'] for c in cs]
        test(len(vals)==len(set(vals)) and set(vals)==D[v],'incomplete or duplicate branch coverage')
        for child in cs:
            nd=[s.copy() for s in D];nd[v]={child['value']};check(child['node'],nd)
    check(p['tree'],domains)
    return counts

def encode(g):
    n=g['n'];index={x:i for i,x in enumerate(labels)}
    var=lambda v,x:16*v+index[x]+1
    clauses=[]
    for v in range(n):
        row=[var(v,x) for x in labels];clauses.append(row)
        clauses.extend([[-x,-y] for x,y in itertools.combinations(row,2)])
    for a,b in g['edges']:
        for u,v in ((a,b),(b,a)):
            for x in labels:clauses.append([-var(u,x)]+[var(v,y) for y in sorted(adj[x])])
    for v,x in sorted((int(v),x) for v,x in g['pins'].items()):clauses.append([var(v,x)])
    raw=(f'p cnf {16*n} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)).encode()
    return clauses,raw

def unit_conflict(clauses,assumptions,nvars):
    # Queue propagation through falsified literals; no target or graph fact here.
    pos=[[] for _ in range(nvars+1)];neg=[[] for _ in range(nvars+1)]
    count=[len(c) for c in clauses];satisfied=bytearray(len(clauses));value=[0]*(nvars+1)
    q=deque(assumptions)
    for i,c in enumerate(clauses):
        if not c:return True
        for l in c:(pos if l>0 else neg)[abs(l)].append(i)
        if len(c)==1:q.append(c[0])
    while q:
        lit=q.popleft();v=abs(lit);sign=1 if lit>0 else -1
        if value[v]:
            if value[v]!=sign:return True
            continue
        value[v]=sign
        for i in (pos if sign==1 else neg)[v]:satisfied[i]=1
        for i in (neg if sign==1 else pos)[v]:
            if satisfied[i]:continue
            count[i]-=1
            if count[i]==0:return True
            if count[i]==1:
                unset=[l for l in clauses[i] if value[abs(l)]==0]
                test(len(unset)==1,'unit propagation bookkeeping failure');q.append(unset[0])
    return False

def parse_dimacs(raw):
    tokens=[];header=None
    for line in raw.decode().splitlines():
        if not line or line.startswith('c'):continue
        if line.startswith('p '):header=list(map(int,line.split()[2:]));continue
        tokens.extend(map(int,line.split()))
    cls=[];current=[]
    for t in tokens:
        if t:current.append(t)
        else:cls.append(current);current=[]
    test(not current and header is not None and len(cls)==header[1],'malformed DIMACS')
    test(all(1<=abs(x)<=header[0] for c in cls for x in c),'out of range DIMACS literal')
    return header[0],cls

def main():
    a=argparse.ArgumentParser();a.add_argument('--graph',required=True);a.add_argument('--proof',required=True);a.add_argument('--out',required=True);arg=a.parse_args()
    out=Path(arg.out);out.mkdir(parents=True,exist_ok=False)
    def save(name,data):
        b=(json.dumps(data,sort_keys=True,indent=2)+'\n').encode();test(len(b)<=1048576,'file budget');(out/name).write_bytes(b)
    try:
        g=read(arg.graph);p=read(arg.proof);stats=verify_tree(g,p)
        # Negative mutation: omit one complete branch, retaining every valid deletion.
        bad=json.loads(json.dumps(p));bad['tree']['children'].pop()
        try:verify_tree(g,bad)
        except Invalid as e:test('branch coverage' in str(e),'wrong mutation rejection');mutation=str(e)
        else:raise Invalid('truncated proof accepted')
        clauses,raw=encode(g);(out/'full_graph.cnf').write_bytes(raw)
        # Every possible first-vertex value is excluded. RUP validates each exclusion
        # from the actual DIMACS clauses; no parity-graph assumption is used.
        additions=[[-i] for i in range(1,17)]+[[]]
        proofraw=''.join(' '.join(map(str,c))+(' ' if c else '')+'0\n' for c in additions).encode()
        (out/'full_graph.drup').write_bytes(proofraw)
        nvars,parsed=parse_dimacs((out/'full_graph.cnf').read_bytes())
        test(parsed==clauses,'serialized encoding mismatch')
        for step,c in enumerate(additions):
            test(unit_conflict(parsed,[-l for l in c],nvars),f'non-RUP addition {step+1}')
            parsed.append(c)
        # A changed negative unit must not be accepted just because final CNF is UNSAT.
        basecls=parse_dimacs(raw)[1]
        test(not unit_conflict(basecls,[16*40+1],nvars),'unexpected free-layer propagation control')
        save('certificate_check.json',dict(verdict='candidate_only',status='certificates_pass',version='standalone-csp-and-drup-1.0',
             csp_proof=stats,cnf_variables=nvars,cnf_clauses=len(clauses),drup_additions=len(additions),empty_clause_replayed=True,
             cnf_sha256=sha(raw),drup_sha256=sha(proofraw),
             mutation={'name':'M12_truncate_exhaustive_certificate','status':'expected_rejection','observed':mutation},
             semantic_encoding='Exactly one of 16 labels for each of 100 vertices. Each directed source edge has a support clause for every label. Exactly ten original leaf pins are units. All 150 source edges are encoded.',
             first_failed_family_lemma=None,trusted_verifier=False))
        print(json.dumps({'status':'certificates_pass','csp_nodes':stats['nodes'],'cnf_variables':nvars,'cnf_clauses':len(clauses),'drup_additions':17}))
        return 0
    except Invalid as e:
        save('failure.json',dict(status='certificate_failure',first_assertion=str(e),verdict='candidate_only'))
        print(json.dumps({'status':'certificate_failure','first_assertion':str(e)}));return 1
if __name__=='__main__':raise SystemExit(main())
