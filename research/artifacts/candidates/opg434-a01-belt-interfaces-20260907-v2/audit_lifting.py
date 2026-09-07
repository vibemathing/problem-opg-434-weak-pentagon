#!/usr/bin/env python3
"""Finite structural pressure checks of the universal lifting proof.
Exhaust all identifications of boundary vertices and all exterior edges on
those vertices, for four/five exiting edges. Not a substitute for the proof.
"""
import collections, hashlib, itertools, json, pathlib
spec=json.loads(pathlib.Path('patches.json').read_text()); reports=[]
def canonical_edges(edges): return {tuple(sorted(e)) for e in edges}
def legal(n,edges):
    edges=list(edges)
    if len(edges)!=len(canonical_edges(edges)) or any(u==v for u,v in edges): return False
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v); adj[v].add(u)
    if any(len(a)>3 for a in adj): return False
    return not any(adj[u]&adj[v] for u,v in edges)
def partitions(k):
    def step(a):
        if len(a)==k: yield a; return
        for v in range(1+max(a,default=-1)+1): yield from step(a+[v])
    if k==0: yield []
    else: yield from step([0])
for tag in ('r11','r12'):
    p=spec['patches'][tag]; n=len(p['vertices']); ports=p['ports']; m=len(ports)
    masks=[tuple(range(m))] if tag=='r11' else [tuple(range(m))]+[tuple(i for i in range(m) if i!=j) for j in range(m)]
    admitted=0; coincidences=0; exterior_edge_cases=0; reductions=collections.Counter(); trace=hashlib.sha256()
    for present in masks:
        for part in partitions(len(present)):
            q=max(part)+1; ends={slot:n+part[i] for i,slot in enumerate(present)}
            all_outside=list(itertools.combinations(range(n,n+q),2))
            exiting=[(ports[i],ends[i]) for i in present]
            for bits in range(1<<len(all_outside)):
                ext=[e for i,e in enumerate(all_outside) if bits>>i&1]
                original=p['edges']+exiting+ext
                if not legal(n+q,original): continue
                replacement=[]; nv=n+q
                for i,j in p['inequalities']:
                    if i in ends and j in ends:
                        assert ends[i]!=ends[j]
                        replacement += [(ends[i],nv),(nv,nv+1),(nv+1,ends[j])]; nv+=2
                # Relabel exterior and newly added vertices down by n.
                reduced=[(u-n,v-n) for u,v in ext+replacement]
                assert legal(nv-n,reduced)
                delta=(n+q)-(nv-n)
                assert delta==(9 if tag=='r11' else 12-len(replacement)//3*2)
                assert delta>= (9 if tag=='r11' else 8)
                admitted+=1; coincidences+=len(set(part))<len(part); exterior_edge_cases+=bool(ext); reductions[delta]+=1
                trace.update(json.dumps([present,part,ext,reduced],separators=(',',':')).encode()+b'\n')
    reports.append({'patch':tag,'admissible_boundary_exterior_cases':admitted,
                    'cases_with_endpoint_coincidences':coincidences,'cases_with_exterior_edges':exterior_edge_cases,
                    'order_decrease_histogram':dict(reductions),'complete_case_stream_sha256':trace.hexdigest()})
# Countercontrol to unsafe direct-edge replacement: an exterior two-edge path
# between critical terminals creates a triangle if a direct edge is added.
p=spec['patches']['r11']; n=11; ext=[(11,15),(15,14)]
original=p['edges']+list(zip(p['ports'],[11,12,13,14]))+ext
assert legal(16,original)
assert not legal(5,[(u-11,v-11) for u,v in ext+[(11,14)]])
# Actual three-edge replacement is legal, including when an old endpoint edge exists.
assert legal(7,[(0,4),(4,3),(0,5),(5,6),(6,3)])
assert legal(6,[(0,3),(0,4),(4,5),(5,3)])
report={'status':'finite_lifting_stress_pass','verdict':'candidate_only','cases':reports,
        'unsafe_direct_edge_control':'triangle detected','old_endpoint_edge_control':'four-cycle allowed',
        'limitations':'Exhaustion covers only exterior edges on boundary vertices; the universal proof covers arbitrary exteriors.'}
pathlib.Path('checks/lifting.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report))
