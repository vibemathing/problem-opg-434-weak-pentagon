#!/usr/bin/env python3
"""Alternate finite check: subset target, pairwise source construction and full CSP.
No imports from the earlier control. Executed only under run_bounded.py.
All counts/certificates cover finite input; this is not a registered verifier.
"""
from __future__ import annotations
import argparse, copy, hashlib, itertools as it, json
from collections import deque
from pathlib import Path

VERSION='subset-csp-control-1.0'
class CheckFailure(Exception): pass
def require(ok, message):
    if not ok: raise CheckFailure(message)
def code(s): return sum(2**i for i in s)
def subset(x): return frozenset(i for i in range(5) if x & 2**i)
V=tuple(sorted((frozenset(c) for k in (0,2,4) for c in it.combinations(range(5),k)),key=code))
TARGET={code(s):{code(t) for t in V if len(s^t)==4} for s in V}
ALL=frozenset(range(5)); GEN=[ALL-{i} for i in range(5)]
def pair(a,b):return frozenset({a%5,b%5})
def add(values):
    ans=frozenset()
    for s in values: ans=ans^s
    return ans

def source(h=1):
    require(type(h) is int and h==1,'unsupported height')
    # Build from a relation on all 4950 unordered source pairs, not by an edge-add loop.
    def adjacent(u,v):
        j,a,k=u;l,b,m=v
        if j==l:
            return ((k==m==0 and (a-b)%5 in (1,4)) or
                    (a==b and {k,m} in ({0,1},{1,2},{1,3})))
        return a==b and k==m and k in (2,3) and (j-l)%5 in (1,4)
    coords=list(it.product(range(5),range(5),range(4)))
    edges=[[i,j] for i,j in it.combinations(range(100),2) if adjacent(coords[i],coords[j])]
    z=[add(GEN[:j]) for j in range(5)]
    full={};partial={};pins={}
    for v,(j,a,k) in enumerate(coords):
        phi=z[a] if k!=1 else z[a]^GEN[0]
        full[v]=code(phi^z[j])
        if k:
            root=add(GEN[(a+b)%5] for b in range(j))
            partial[v]=code(root^(frozenset() if k==1 else GEN[k-2]))
            if j==0 and k>1:pins[v]=partial[v]
        elif j:
            a1,a2=((a,a+2),(a+2,a+4),(a,a+2),(a+4,a+1))[j-1]
            partial[v]=code(pair(a1,a2))
    return dict(n=100,edges=edges,hole=[4*a for a in range(5)],total_map=full,partial_map=partial,pins=pins)

def adjlist(n,edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def distances(n,edges,starts,removed=()):
    a=adjlist(n,edges);ban=set(removed);d={v:0 for v in starts if v not in ban};q=deque(d)
    while q:
        u=q.popleft()
        for v in sorted(a[u]-ban):
            if v not in d:d[v]=d[u]+1;q.append(v)
    return d

def check_map(n,edges,labels,removed=(),pins=None,target=TARGET):
    require(set(labels)==set(range(n))-set(removed),'map domain mismatch')
    require(all(x in target for x in labels.values()),'label outside target')
    for u,v in edges:
        if u in labels and v in labels:require(labels[v] in target[labels[u]],f'bad mapped edge:{u},{v}')
    if pins is not None:require(all(labels[v]==c for v,c in pins.items()),'pin disagreement')

def graph_check(data):
    n=data['n'];edges=data['edges'];a=adjlist(n,edges)
    require(n==100 and len(edges)==150,'wrong graph counts')
    require(len(set(map(tuple,edges)))==len(edges) and all(0<=u<v<n for u,v in edges),'not simple')
    require(all(len(x)==3 for x in a),'not cubic')
    # Edge-deletion shortest paths: independently establish shortest cycle length.
    gs=min(distances(n,[f for f in edges if f!=e],[e[0]])[e[1]]+1 for e in edges)
    require(gs==5,'wrong girth')
    q=data['hole'];require(len(q)==5 and all(sum(v in q for v in a[u])==2 for u in q),'hole not induced pentagon')
    require(len(distances(n,edges,[0]))==n,'disconnected')
    for r in it.chain(((i,) for i in range(n)),it.combinations(range(n),2)):
        s=next(v for v in range(n) if v not in r)
        require(len(distances(n,edges,[s],r))==n-len(r),'vertex separator')
    check_map(n,edges,data['total_map'])
    check_map(n,edges,data['partial_map'],q,data['pins'])
    return dict(vertices=n,edges=len(edges),girth=gs,total_edges_checked=150,partial_edges_checked=140,
                vertices_deleted_checked=100,vertex_pairs_deleted_checked=4950)

def negative_target(g):
    for a,b,c in it.combinations(sorted(g),3):
        if b in g[a] and c in g[a] and c in g[b]:return [a,b,c]
    return None

# Complete full-graph target-domain search. A deletion is sound iff it has
# no support at an actual neighboring source vertex in the CURRENT domain.
def csp_proof(data):
    arcs=[(u,v) for a,b in data['edges'] for u,v in ((a,b),(b,a))]
    ds=[set(TARGET) for _ in range(data['n'])]
    for v,c in data['pins'].items():ds[v]={c}
    nodes=0;prunes=0
    def visit(dom):
        nonlocal nodes,prunes
        nodes+=1;require(nodes<=20000,'search node budget exceeded')
        log=[];changed=True
        while changed:
            changed=False
            for u,v in arcs:
                bad=sorted(x for x in dom[u] if not (TARGET[x]&dom[v]))
                for x in bad:
                    dom[u].remove(x);log.append([u,x,v]);prunes+=1;changed=True
                if not dom[u]:return dict(deletions=log,empty=u)
        variable=next((v for v in range(len(dom)) if len(dom[v])>1),None)
        if variable is None:raise CheckFailure('full pinned graph SAT: '+str([next(iter(s)) for s in dom]))
        children=[]
        for x in sorted(dom[variable]):
            nd=[s.copy() for s in dom];nd[variable]={x}
            children.append(dict(value=x,node=visit(nd)))
        return dict(deletions=log,split=variable,children=children)
    tree=visit(ds)
    return dict(format='full-graph-arc-branch-unsat-v1',n=data['n'],edges=data['edges'],pins=data['pins'],
                target_adjacency={str(x):sorted(y) for x,y in TARGET.items()},tree=tree,
                search_statistics=dict(nodes=nodes,domain_deletions=prunes),
                scope='All assignments of all 100 source vertices to all 16 target vertices under exactly ten pins; exhaustive sound pruning and complete branches.')

def semantic_bridge(data,certificate):
    a=adjlist(data['n'],data['edges']);q=data['hole'];qs=set(q);roots=[];leaves=[];trace=[]
    for c in q:
        rs=a[c]-qs;require(len(rs)==1,'wrong central spoke');r=next(iter(rs));roots.append(r)
        ls=a[r]-{c};require(len(ls)==2 and all(v in data['pins'] for v in ls),'two pinned children missing')
        leaves+=sorted(ls)
        allowed=[x for x in TARGET if all(data['pins'][v] in TARGET[x] for v in ls)]
        central=[y for y in TARGET if any(y in TARGET[x] for x in allowed)]
        require(allowed==[0,3],'actual graph elimination does not yield A')
        witness={str(y):next(x for x in allowed if y in TARGET[x]) for y in central}
        trace.append(dict(central=c,root=r,leaves=sorted(ls),root_domain=allowed,central_domain=central,attainment=witness))
    require(len(set(leaves))==10 and len(set(roots))==5 and not(set(leaves)&set(roots)|set(roots)&qs),'overlapping core')
    core=set(q+roots+leaves);ce=[e for e in data['edges'] if set(e)<=core]
    require(len(core)==20 and len(ce)==20,'wrong core edges')
    U=set(trace[0]['central_domain']);side={x:int(len(subset(x))==2) for x in U}
    require(all(side[x]!=side[y] for x in U for y in TARGET[x]&U),'side map is not edge preserving')
    clauses=[]
    for i in range(5):
        require(q[(i+1)%5] in a[q[i]],'missing original central cycle edge')
        clauses.extend([[i+1,(i+1)%5+1],[-(i+1),-((i+1)%5+1)]])
    require(certificate['clauses']==clauses,'CNF not mapped from actual source edges')
    # Independent truth-table verification of every resolution consequence.
    cdict={i+1:c for i,c in enumerate(clauses)}
    for step in certificate['resolution']:
        left,right=(cdict[i] for i in step['parents']);r=step['resolvent'];p=step['pivot']
        require((p in left and -p in right) or (-p in left and p in right),'wrong resolution pivot')
        expected=(set(left)|set(right))-{p,-p}
        require(set(r)==expected and step['id'] not in cdict,'wrong resolution row')
        for bits in it.product((False,True),repeat=5):
            truth=lambda cl:any(bits[abs(l)-1]==(l>0) for l in cl)
            require(not(truth(left) and truth(right)) or truth(r),'unsound resolution implication')
        cdict[step['id']]=r
    require(cdict[19]==[],'not an empty clause')
    return dict(core_vertices=sorted(core),core_edges=ce,eliminations=trace,side=side,
                proof='Full source -> subgraph on these 20 vertices -> exact rooted eliminations -> side CNF. Other-layer constraints are relaxed, not replaced by an equivalence.',
                resolution_steps=9,truth_assignments_per_resolution_step=32)

def released_map():
    centers=[pair(0,3),GEN[3],pair(2,3),GEN[2],pair(2,4)]
    roots=[pair(1,2),frozenset(),pair(0,1),frozenset(),pair(0,1)]
    z=[add(GEN[:j]) for j in range(5)];out={}
    for v,(j,a,k) in enumerate(it.product(range(5),range(5),range(4))):
        val=[centers[a],roots[a],GEN[2] if a==0 else GEN[0],GEN[1]][k]
        out[v]=code(val^z[j])
    return out

def mutations(data,parity):
    results=[]
    def rejected(name,fn,expected,witness):
        try:fn()
        except CheckFailure as e:
            require(expected in str(e),'wrong failure for '+name+': '+str(e))
            results.append(dict(name=name,expected=expected,observed=str(e),status='expected_rejection',witness=witness));return
        raise CheckFailure('mutation unexpectedly accepted: '+name)
    gens=[code(s) for s in GEN];bad=gens[:-1]+[3]
    mutated={x:{y for y in TARGET if code(subset(x)^subset(y)) in bad} for x in TARGET}
    tri=negative_target(mutated);require(tri is not None,'generator mutation no triangle')
    results.append(dict(name='M1_change_generator',status='expected_rejection',observed='target_triangle',witness=tri))
    partial={v:x for v,x in data['partial_map'].items() if v not in [20+4*a for a in range(5)]}
    rejected('M2_omit_central_layer',lambda:check_map(100,data['edges'],partial,data['hole']),'domain mismatch',{'missing':[20+4*a for a in range(5)]})
    release=released_map();keep={v:c for v,c in data['pins'].items() if v!=2}
    check_map(100,data['edges'],release,pins=keep);require(release[2]!=data['pins'][2],'no released disagreement')
    results.append(dict(name='M3_release_one_leaf_pin',status='positive_witness_pass',observed='total map satisfies all edges and other nine pins',free_vertex=2,total_map=release))
    rejected('M4_height_zero',lambda:source(0),'unsupported height',{'height':0,'height_zero_message':[0],'required_pair':[0,3]})
    minus=[e for e in data['edges'] if e!=[2,22]];adj=adjlist(100,minus)
    require([i for i in range(100) if len(adj[i])!=3]==[2,22],'edge-deletion degree guard')
    check_map(100,minus,data['total_map']);check_map(100,minus,data['partial_map'],data['hole'])
    results.append(dict(name='M5_delete_vertical_edge',status='expected_rejection',observed='not cubic; both maps still valid',edge=[2,22],degree_two_vertices=[2,22]))
    union=lambda ss:set().union(*(TARGET[x] for x in ss))
    common=lambda ss:set(TARGET).intersection(*(TARGET[x] for x in ss))
    good=union({0,3})&union({30,27});badmsg=common({0,3})&common({30,27})
    require(good=={12,20} and badmsg==set(),'message direction guard missing')
    results.append(dict(name='M6_UNION_to_COMMON',status='expected_rejection',observed='lost attainable parent labels',expected_message=sorted(good),mutated_message=[]))
    badgraph=copy.deepcopy(data);badgraph['edges']=[e for e in data['edges'] if e!=[2,82]]+[[2,42]]
    require(all(e in badgraph['edges'] for e in ([2,22],[22,42],[2,42])),'missing mutated triangle')
    rejected('M7_break_leaf_cycle',lambda:graph_check(badgraph),'not cubic',{'removed':[2,82],'inserted':[2,42],'triangle':[2,22,42]})
    swapped={}
    for v,x in data['partial_map'].items():
        j,r=divmod(v,20);jj={1:2,2:1}.get(j,j);swapped[20*jj+r]=x
    rejected('M8_swap_label_layer_indices',lambda:check_map(100,data['edges'],swapped,data['hole']),'bad mapped edge',{'label_layers_swapped':[1,2],'graph_not_relabelled':True})
    d=distances(100,data['edges'],data['hole']);wrong=distances(100,data['edges'],[0]);wit=next(v for v in range(100) if d[v]!=wrong[v])
    rejected('M9_wrong_distance_origin',lambda:require(d==wrong,'distance-source mismatch'),'distance-source mismatch',{'vertex':wit,'correct_from_Q':d[wit],'wrong_from_single_vertex':wrong[wit]})
    def present_witness(obj):
        require('total_map' in obj,'missing total witness');check_map(obj['n'],obj['edges'],obj['total_map'])
    badgraph=copy.deepcopy(data);badgraph.pop('total_map')
    rejected('M10_delete_total_map_witness',lambda:present_witness(badgraph),'missing total witness',{'missing_field':'total_map'})
    # Mutation of a true graph input while retaining the valid abstract parity proof.
    wrongpins=copy.deepcopy(data);wrongpins['pins'][2]=27
    rejected('M11_stale_parity_graph_bridge',lambda:semantic_bridge(wrongpins,parity),'does not yield A',{'changed_pin':2,'old':30,'new':27,'abstract_parity_clauses_unchanged':True})
    return results

def cut_identity_controls(data):
    n=data['n'];edges=data['edges'];base=[e for e in edges if e[1]<20]
    def identity(W):
        masks=[{j for j in range(5) if 20*j+v in W} for v in range(20)]
        horizontal=sum(len(masks[u]^masks[v]) for u,v in base)
        vertical=sum(sum((j in masks[l])!=((j+1)%5 in masks[l]) for j in range(5)) for l in range(20) if l%4 in (2,3))
        direct=sum((u in W)!=(v in W) for u,v in edges)
        require(direct==horizontal+vertical,'cut identity mismatch')
    count=0
    for W in it.chain([set(),set(range(n))],({i} for i in range(n)),(set(x) for x in it.combinations(range(n),2))):identity(W);count+=1
    # Exercise unicyclic selected components and partial leaf fibers, with complements.
    for mask in range(32):
        for typ in ('central','leaf','layer'):
            if typ=='central':W={20*j+4*a for j in range(5) if mask>>j&1 for a in range(5)}
            elif typ=='leaf':W={20*j+2 for j in range(5) if mask>>j&1}
            else:W={20*j+v for j in range(5) if mask>>j&1 for v in range(20)}
            identity(W);identity(set(range(n))-W);count+=2
    return dict(subsets_checked=count,scope='finite controls only; the all-subset identity follows by edge-type partition')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--original-json',required=True);ap.add_argument('--parity',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
    def save(name,obj):
        b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();require(len(b)<=1048576,'output limit');(out/name).write_bytes(b)
    try:
        d=source();old=json.loads(Path(a.original_json).read_text())
        for key in ('total_map','partial_map','pins'):old[key]={int(v):x for v,x in old[key].items()}
        require(d==old,'alternate construction differs from original output')
        stats=graph_check(d);require(negative_target(TARGET) is None,'target triangle')
        parity=json.loads(Path(a.parity).read_text());bridge=semantic_bridge(d,parity)
        proof=csp_proof(d);muts=mutations(d,parity);cuts=cut_identity_controls(d)
        save('full_graph_unsat_certificate.json',proof);save('graph_to_parity_bridge.json',bridge);save('mutations.json',muts)
        save('summary.json',dict(verdict='candidate_only',status='alternate_control_pass',version=VERSION,
             constructed_graph_equal=True,structural=stats,full_graph_csp=proof['search_statistics'],pin_obstruction='UNSAT',
             semantic_bridge=True,mutations=len(muts),cut_identity=cuts,first_failed_family_lemma=None,
             limitations=['h=1 finite control; arbitrary height is a separately supplied proof','same generating trust domain; no EvidenceLink']))
        print(json.dumps(dict(status='alternate_control_pass',nodes=proof['search_statistics']['nodes'],mutations=len(muts))))
        return 0
    except CheckFailure as e:
        save('failure.json',dict(status='control_failure',first_assertion=str(e),verdict='candidate_only'))
        print(json.dumps(dict(status='control_failure',first_assertion=str(e))));return 1
if __name__=='__main__':raise SystemExit(main())
