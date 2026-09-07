#!/usr/bin/env python3
"""UNEXECUTED candidate control. Invoke only in an authorized bounded runtime.

Run from the repository root, after separately granting execution permission:
python3 research/artifacts/candidates/opg434-a01-layered-audit-20260907-v1/h1_control.py --execute --out research/artifacts/candidates/opg434-a01-layered-audit-20260907-v1/replay

No external packages, networking, subprocesses, or repository-control writes.
This program is not a registered verifier and never creates EvidenceLinks.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import platform
import signal
import sys
import time

SOURCE = 'research/artifacts/candidates/opg434-a01-layered-pentagon-repair-20260907-v1.md'
SOURCE_SHA = 'c0e9115a80eb09f692fb3c83a52c8002766219b1154970ad21cc29442a5ba9aa'
T = (30, 29, 27, 23, 15)
B = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
LIMITS = {'wall_seconds': 40, 'cpu_seconds': 35, 'address_space_bytes': 536870912,
          'threads': 1, 'processes': 1, 'max_files': 8, 'max_file_bytes': 1048576,
          'max_total_output_bytes': 2097152}

class AuditError(Exception):
    pass

def need(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)

def p(i: int, j: int) -> int:
    return (1 << (i % 5)) ^ (1 << (j % 5))

def near(x: int, y: int, generators=T) -> bool:
    return (x ^ y) in generators

def union_neighborhood(xs) -> set[int]:
    return {y for x in xs for y in B if near(x, y)}

def ident(j: int, a: int, k: int) -> int:
    return 20 * (j % 5) + 4 * (a % 5) + k

def build(h: int = 1):
    if isinstance(h, bool) or not isinstance(h, int) or h < 1:
        raise ValueError('height must be an integer at least one')
    if h != 1:
        raise ValueError('this bounded full-graph control covers h=1 only')
    edges = set()
    def add(u, v):
        need(u != v, 'source loop')
        e = tuple(sorted((u, v)))
        need(e not in edges, 'duplicate source edge')
        edges.add(e)
    for j, a in product(range(5), repeat=2):
        add(ident(j,a,0), ident(j,a+1,0))
        add(ident(j,a,0), ident(j,a,1))
        for k in (2,3):
            add(ident(j,a,1), ident(j,a,k))
            add(ident(j,a,k), ident(j+1,a,k))
    hole = {ident(0,a,0) for a in range(5)}
    z = (0,30,3,24,15)
    full, partial = {}, {}
    for j, a in product(range(5), repeat=2):
        q = 0
        for k in range(j):
            q ^= T[(a+k) % 5]
        for k in range(4):
            full[ident(j,a,k)] = z[a] ^ z[j] ^ (T[0] if k == 1 else 0)
        partial[ident(j,a,1)] = q
        partial[ident(j,a,2)] = q ^ T[0]
        partial[ident(j,a,3)] = q ^ T[1]
        if j:
            central = {1:p(a,a+2), 2:p(a+2,a+4), 3:p(a,a+2), 4:p(a+4,a+1)}[j]
            partial[ident(j,a,0)] = central
    pins = {ident(0,a,k): partial[ident(0,a,k)] for a in range(5) for k in (2,3)}
    return sorted(edges), hole, full, partial, pins

def check_map(vertices: set[int], edges, labels: dict[int,int], generators=T) -> int:
    need(set(labels) == vertices, 'map domain mismatch')
    need(all(x in B for x in labels.values()), 'target label outside B')
    count = 0
    for u,v in edges:
        if u in vertices and v in vertices:
            need(near(labels[u], labels[v], generators), f'bad mapped edge {u},{v}')
            count += 1
    return count

def adjacency(n, edges):
    out = [[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        out[u].append((v,i)); out[v].append((u,i))
    return out

def connected(adj, removed=frozenset()):
    remaining = set(range(len(adj))) - set(removed)
    if not remaining:
        return True
    start = min(remaining); seen={start}; queue=[start]
    for v in queue:
        for w,_ in adj[v]:
            if w in remaining and w not in seen:
                seen.add(w); queue.append(w)
    return seen == remaining

def bridges_after_deleting(adj, removed):
    stamp=[-1]*len(adj); low=[0]*len(adj); tick=0; bridges=[]
    def visit(u, parent_edge):
        nonlocal tick
        stamp[u]=low[u]=tick; tick+=1
        for v,e in adj[u]:
            if e in removed or e == parent_edge:
                continue
            if stamp[v] < 0:
                visit(v,e); low[u]=min(low[u],low[v])
                if low[v] > stamp[u]:
                    bridges.append(e)
            else:
                low[u]=min(low[u],stamp[v])
    visit(0,-1)
    return tick == len(adj), bridges

def exact_small_cuts(adj, edges):
    ok, one = bridges_after_deleting(adj,set())
    need(ok and not one, 'disconnected source or a bridge')
    cuts=set()
    # Completeness: any 3-edge cut leaves its third edge as a bridge after
    # deleting the other two, unless a smaller edge cut was already found.
    for a,b in combinations(range(len(edges)),2):
        ok, last = bridges_after_deleting(adj,{a,b})
        need(ok, 'edge cut of size at most two')
        for c in last:
            cuts.add(tuple(sorted((a,b,c))))
    trivial={tuple(sorted(e for _,e in adj[v])) for v in range(len(adj))}
    need(cuts == trivial, 'missing trivial cut or nontrivial 3-edge cut')
    return sorted(cuts)

def girth(adj):
    best=len(adj)+1
    for s in range(len(adj)):
        dist=[-1]*len(adj); parent=[-1]*len(adj); dist[s]=0; queue=deque([s])
        while queue:
            u=queue.popleft()
            for v,_ in adj[u]:
                if dist[v] < 0:
                    dist[v]=dist[u]+1; parent[v]=u; queue.append(v)
                elif parent[u] != v:
                    best=min(best,dist[u]+dist[v]+1)
    return None if best > len(adj) else best

def permute(x, pi):
    y=0
    for i in range(5):
        if x & (1<<i):
            y ^= 1<<pi[i]
    return y

def pair_tree(h, pair):
    need(h >= 1 and len(pair) == 2, 'bad pair tree input')
    u,v=sorted(pair); support=[i for i in range(5) if (u^v) & (1<<i)]
    need(len(support) == 2, 'pair is not distinct nonadjacent')
    if h == 1:
        return ({'pin':u^T[support[0]]}, {'pin':u^T[support[1]]})
    pi={3:support[0],4:support[1]}
    for a,b in zip((0,1,2), sorted(set(range(5))-set(support))):
        pi[a]=b
    def alpha(x):
        return u ^ permute(x ^ p(2,3), pi)
    left={alpha(0),alpha(p(0,1))}; right={alpha(T[0]),alpha(T[2])}
    return (pair_tree(h-1,left),pair_tree(h-1,right))

def message(tree):
    if isinstance(tree,dict):
        return {tree['pin']}
    return union_neighborhood(message(tree[0])) & union_neighborhood(message(tree[1]))

def attain(tree, root):
    if isinstance(tree,dict):
        need(root == tree['pin'], 'wrong realizing leaf')
        return
    for child in tree:
        choices=sorted(x for x in message(child) if near(root,x))
        need(bool(choices), 'missing attainment witness')
        attain(child,choices[0])

def verify_resolution(cert):
    clauses={i+1:set(c) for i,c in enumerate(cert['clauses'])}
    need(len(clauses) == 10, 'wrong parity clause count')
    for entry in cert['resolution']:
        a,b=entry['parents']; pivot=entry['pivot']; c1=clauses[a]; c2=clauses[b]
        if pivot in c1 and -pivot in c2:
            derived=(c1-{pivot}) | (c2-{-pivot})
        elif -pivot in c1 and pivot in c2:
            derived=(c1-{-pivot}) | (c2-{pivot})
        else:
            raise AuditError('invalid resolution pivot')
        need(derived == set(entry['resolvent']), 'wrong resolvent')
        need(entry['id'] not in clauses, 'duplicate resolution ID')
        clauses[entry['id']]=derived
    need(clauses[19] == set(), 'no empty clause')

class Output:
    def __init__(self, root):
        self.root=root; self.count=0; self.total=0; self.files=[]
        root.mkdir(parents=True,exist_ok=True)
    def put(self, name, value):
        raw=(json.dumps(value,sort_keys=True,indent=2)+'\n').encode()
        need(len(raw)<=LIMITS['max_file_bytes'], 'per-file output budget')
        need(self.count < LIMITS['max_files'], 'file count budget')
        need(self.total+len(raw)<=LIMITS['max_total_output_bytes'], 'total output budget')
        target=self.root/name
        need(not target.exists(), 'output exists; use a fresh output directory')
        target.write_bytes(raw); self.count+=1; self.total+=len(raw)
        self.files.append({'path':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})

def run(out):
    need(len(B)==16 and len(set(T))==5, 'bad target dimensions')
    need(not any(near(x,y) and near(y,z) and near(z,x) for x,y,z in combinations(B,3)), 'target triangle')
    need([m for m in range(32) if xor(T[i] for i in range(5) if m & (1<<i)) == 0] == [0,31], 'generator relation')
    A={0,p(0,1)}; U=union_neighborhood(A); pair_side={p(2,3),p(2,4),p(3,4)}
    need(U == set(T)|pair_side, 'wrong union neighborhood')
    need(all((x in pair_side)!=(y in pair_side) for x,y in combinations(U,2) if near(x,y)), 'U not bipartite')
    trees_checked=0
    for h in (1,2,3):
        for u,v in combinations(B,2):
            if not near(u,v):
                tr=pair_tree(h,{u,v}); need(message(tr)=={u,v}, 'message mismatch')
                attain(tr,u); attain(tr,v); trees_checked+=1
    edges,hole,full,partial,pins=build(1); vertices=set(range(100)); adj=adjacency(100,edges)
    need(len(edges)==150 and all(len(a)==3 for a in adj), 'source count/degree mismatch')
    need(sum(u in hole and v in hole for u,v in edges)==5, 'hole not induced C5')
    total_edges=check_map(vertices,edges,full)
    exterior_edges=check_map(vertices-hole,edges,partial)
    need(total_edges==150 and exterior_edges==140, 'edge coverage mismatch')
    need(girth(adj)==5, 'source girth mismatch')
    for u in vertices:
        need(connected(adj,{u}), 'cut vertex')
    for u,v in combinations(range(100),2):
        need(connected(adj,{u,v}), 'two-vertex cut')
    cuts=exact_small_cuts(adj,edges)
    distances={u:0 for u in hole}; queue=list(sorted(hole))
    for u in queue:
        for v,_ in adj[u]:
            if v not in distances:
                distances[v]=distances[u]+1; queue.append(v)
    need(all(distances[v]==2 for v in pins), 'pin distances')
    root_list={x for x in B if near(x,T[0]) and near(x,T[1])}
    need(root_list==A, 'h1 root list')
    rejection=[]; histogram=Counter()
    for ys in product(sorted(U),repeat=5):
        bad=next((i for i in range(5) if not near(ys[i],ys[(i+1)%5])),None)
        need(bad is not None, 'pinned core has a model')
        rejection.append(str(bad)); histogram[bad]+=1
    cert=json.loads(Path(__file__).with_name('h1_parity_certificate.json').read_text())
    expected=[[i+1,(i+1)%5+1] for i in range(5)]
    expected=[c for pair in ((c,[-v for v in c]) for c in expected) for c in pair]
    need(cert['clauses']==expected, 'parity CNF faithfulness')
    verify_resolution(cert)
    mutations=[]
    bad_T=(*T[:4],p(0,1))
    need(near(0,T[0],bad_T) and near(T[0],T[1],bad_T) and near(T[1],0,bad_T), 'generator mutation not exposed')
    mutations.append({'name':'generator','result':'triangle','witness':[0,T[0],T[1]]})
    missing={ident(1,a,0) for a in range(5)}
    try:
        check_map(vertices-hole,edges,{v:x for v,x in partial.items() if v not in missing})
    except AuditError:
        mutations.append({'name':'omitted_central_layer','result':'domain_rejected','missing':sorted(missing)})
    else:
        raise AuditError('omitted layer accepted')
    central=(p(0,3),T[3],p(2,3),T[2],p(2,4)); roots=(p(1,2),0,p(0,1),0,p(0,1))
    z=(0,30,3,24,15); released={}
    for j,a in product(range(5),repeat=2):
        vals=(central[a],roots[a],T[2] if a==0 else T[0],T[1])
        for k in range(4):
            released[ident(j,a,k)]=vals[k]^z[j]
    check_map(vertices,edges,released); free=ident(0,0,2)
    need(all(released[v]==x for v,x in pins.items() if v!=free), 'released-pin witness changed another pin')
    need(released[free]!=pins[free], 'released pin unchanged')
    mutations.append({'name':'release_one_pin','result':'full_map_exists','free_vertex':free})
    try:
        build(0)
    except ValueError:
        mutations.append({'name':'height_zero','result':'domain_rejected'})
    else:
        raise AuditError('height zero accepted')
    deleted=tuple(sorted((ident(0,0,2),ident(1,0,2))))
    modified=[e for e in edges if e!=deleted]; madj=adjacency(100,modified)
    need([v for v in range(100) if len(madj[v])!=3]==list(deleted), 'vertical-edge mutation degrees')
    check_map(vertices,modified,full); check_map(vertices-hole,modified,partial)
    mutations.append({'name':'delete_vertical_edge','result':'not_cubic_but_maps_still_valid','edge':list(deleted)})
    common=lambda xs: {y for y in B if all(near(x,y) for x in xs)}
    need(not (common(A)&common({T[0],T[2]})), 'common-neighborhood negative guard')
    out.put('h1_graph_and_maps.json',{'n':100,'edges':edges,'hole':sorted(hole),'total_map':full,'partial_map':partial,'pins':pins})
    out.put('projected_core_rejections.json',{'ordered_domain':sorted(U),'tuple_order':'lexicographic product of five domains','first_bad_edge_digits':''.join(rejection),'histogram':dict(histogram),'scope':'exact layer-0 core projection; subgraph UNSAT suffices for full graph'})
    out.put('h1_trivial_three_cuts.json',{'edge_index_order':edges,'cuts':cuts})
    out.put('released_pin_total_map.json',{'free_vertex':free,'map':released})
    out.put('mutations.json',mutations)
    return {'target_vertices':16,'target_edges':40,'vertices':100,'edges':150,'partial_vertices':95,'partial_edges_checked':exterior_edges,'total_edges_checked':total_edges,'girth':5,'vertex_pairs_tested':4950,'three_edge_cuts':len(cuts),'all_three_edge_cuts_trivial':True,'message_trees_checked':trees_checked,'projected_core_assignments_rejected':len(rejection),'resolution_empty_clause':True,'mutations_checked':len(mutations)}

def xor(values):
    result=0
    for value in values:
        result ^= value
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute',action='store_true')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if not args.execute:
        parser.error('explicit --execute required after runtime authorization')
    import resource
    resource.setrlimit(resource.RLIMIT_AS,(LIMITS['address_space_bytes'],LIMITS['address_space_bytes']))
    resource.setrlimit(resource.RLIMIT_CPU,(LIMITS['cpu_seconds'],LIMITS['cpu_seconds']+1))
    resource.setrlimit(resource.RLIMIT_FSIZE,(LIMITS['max_file_bytes'],LIMITS['max_file_bytes']))
    def timed_out(_sig,_frame):
        raise TimeoutError('bounded runtime exhausted')
    signal.signal(signal.SIGALRM,timed_out); signal.signal(signal.SIGXCPU,timed_out)
    signal.alarm(LIMITS['wall_seconds'])
    started=time.monotonic(); out=Output(args.out); status='not_completed'; result={}; exit_code=1
    try:
        need(hashlib.sha256(Path(SOURCE).read_bytes()).hexdigest()==SOURCE_SHA,'frozen source digest mismatch')
        result=run(out); status='candidate_control_pass'; exit_code=0
    except TimeoutError as error:
        status='timeout'; result={'error':str(error)}; exit_code=124
    except (AuditError,ValueError,KeyError,OSError) as error:
        status='control_failure'; result={'error_type':type(error).__name__,'error':str(error) if isinstance(error,AuditError) else 'input or output failure'}
    finally:
        signal.alarm(0)
    report={'verdict':'candidate_only','status':status,'exit_code':exit_code,'python_version':platform.python_version(),'implementation':platform.python_implementation(),'dependencies':'Python standard library only','source_sha256':SOURCE_SHA,'certificate_sha256':hashlib.sha256(Path(__file__).with_name('h1_parity_certificate.json').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limits':LIMITS,'elapsed_seconds':round(time.monotonic()-started,6),'result':result,'output_files':out.files.copy(),'limitations':['finite h=1 graph check and heights 1..3 message controls do not prove the infinite family','no trusted verifier or admission authority','compressed negative certificate has a separately stated graph-to-parity bridge']}
    out.put('execution.json',report)
    print(json.dumps({'status':status,'exit_code':exit_code,'verdict':'candidate_only'}))
    return exit_code

if __name__ == '__main__':
    sys.exit(main())
