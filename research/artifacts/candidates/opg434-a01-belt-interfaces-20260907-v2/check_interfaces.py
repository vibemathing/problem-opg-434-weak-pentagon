#!/usr/bin/env python3
"""Check complete belt witness tables without importing the CSP generator.
Target adjacency is set-symmetric-difference cardinality, not the generator's
XOR/bit-domain solver. Coverage is reconstructed directly from all boundary tuples.
"""
import argparse, hashlib, itertools, json, pathlib

class Rejected(Exception): pass

def need(ok, why):
    if not ok: raise Rejected(why)

def source(patch, P):
    names=(['v0','v1','v2','v3','v4','x0','x2','x3','x4']+
           (['y','t'] if patch=='r11' else ['r','z','t']))
    pairs=[('v'+str(i),'v'+str((i+1)%5)) for i in range(5)]
    pairs += [('v0','x0'),('v2','x2'),('v3','x3'),('v4','x4')]
    if patch=='r11':
        pairs += [('y','x2'),('y','x3'),('y','x4'),('t','x4'),('t','x0')]
        ports=['x0','x2','x3','t']; neq=[(0,3)]
    else:
        pairs += [('r','x2'),('r','x3'),('z','x3'),('z','x4'),('t','x4'),('t','x0')]
        ports=['x0','x2','r','z','t']; neq=[(0,4),(1,2)]
    need(P['vertices']==names,'source vertex names/order')
    actual=[frozenset((names[u],names[v])) for u,v in P['edges']]
    need(len(actual)==len(set(actual)) and all(len(e)==2 for e in actual),'source not simple')
    need(set(actual)=={frozenset(e) for e in pairs},'source edge table mismatch')
    need([names[v] for v in P['ports']]==ports,'ordered ports mismatch')
    need([tuple(e) for e in P['inequalities']]==neq,'boundary predicate mismatch')
    return names, [(names.index(a),names.index(b)) for a,b in pairs], P['ports'], neq

def target(spec):
    sets=[frozenset(i for i in range(5) if (m//(2**i))%2) for m in range(32)]
    sets=[a for a in sets if len(a)%2==0]
    near=lambda a,b: len(sets[a].symmetric_difference(sets[b]))==4
    masks=[sum(2**i for i in a) for a in sets]
    need(spec['target']['coordinates']==5 and spec['target']['generators']==[30,29,27,23,15],'target definition drift')
    need(len(sets)==16,'target size')
    need(not any(near(a,b) and near(b,c) and near(c,a) for a,b,c in itertools.combinations(range(16),3)),'target triangle')
    walks={(a,d):(b,c) for a in range(16) for b in range(16) if near(a,b)
           for c in range(16) if near(b,c) for d in range(16) if near(c,d)}
    need(set(walks)=={(a,b) for a in range(16) for b in range(16) if a!=b},'three-edge path relation')
    # Check the normalization action for ALL target labels and target edges.
    for shift in sets:
        f=[sets.index(a.symmetric_difference(shift)) for a in sets]
        need(all(near(a,b)==near(f[a],f[b]) for a in range(16) for b in range(16)),'translation faithfulness')
    return sets, near, walks

def check(spec, patch, data):
    P=spec['patches'][patch]; names,edges,ports,neq=source(patch,P)
    sets,near,walks=target(spec); n=len(names); count=0; forbidden=0
    expected=3840 if patch=='r11' else 57600
    need(P['normalized_rows']==expected,'declared row count')
    need(len(data)==expected*(n+1),'table byte length/coverage')
    for suffix in itertools.product(range(16),repeat=len(ports)-1):
        pins=(0,)+suffix
        if any(pins[i]==pins[j] for i,j in neq):
            forbidden+=1
            # The corresponding ports really ARE joined by an internal edge.
            for i,j in neq:
                if pins[i]==pins[j]:
                    need(frozenset((ports[i],ports[j])) in {frozenset(e) for e in edges},'false necessity bridge')
                    need((pins[i],pins[j]) not in walks,'forbidden state has a length-three walk')
            continue
        row=data[count*(n+1):(count+1)*(n+1)]
        need(row[-1:]==b'\n','row delimiter')
        need(all(c in b'0123456789abcdef' for c in row[:-1]),'invalid target token')
        values=[int(chr(c),16) for c in row[:-1]]
        for u,v in edges:
            need(near(values[u],values[v]),'internal edge at row '+str(count)+': '+str((u,v)))
        for j,u in enumerate(ports):
            need(near(values[u],pins[j]),'pin edge at row '+str(count)+': '+str(j))
        count+=1
    need(count==expected,'missing or excess state')
    return {'status':'complete_relation_witness_check_pass','verdict':'candidate_only','patch':patch,
            'positive_normalized_states':count,'negative_normalized_states':forbidden,
            'internal_edge_tests':count*len(edges),'boundary_edge_tests':count*len(ports),
            'three_edge_path_endpoint_pairs':len(walks),'translation_actions_checked':16,
            'first_failed_boundary':None,'table_sha256':hashlib.sha256(data).hexdigest()}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--spec',required=True)
    ap.add_argument('--patch',choices=['r11','r12'],required=True); ap.add_argument('--table',required=True)
    ap.add_argument('--out',required=True); a=ap.parse_args()
    try:
        raw=pathlib.Path(a.spec).read_bytes(); result=check(json.loads(raw),a.patch,pathlib.Path(a.table).read_bytes())
        result['spec_sha256']=hashlib.sha256(raw).hexdigest(); code=0
    except (Rejected,ValueError,IndexError,KeyError) as e:
        result={'status':'certificate_rejected','error':str(e),'verdict':'candidate_only'}; code=2
    pathlib.Path(a.out).write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result)); return code
if __name__=='__main__': raise SystemExit(main())
