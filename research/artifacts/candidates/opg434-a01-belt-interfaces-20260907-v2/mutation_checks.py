#!/usr/bin/env python3
"""Adversarial certificate checks. Imports only the simple certificate checker,
not the CSP generator; tests semantic guards rather than just a checksum."""
import copy, hashlib, itertools, json, pathlib
import check_interfaces as C

spec=json.loads(pathlib.Path('patches.json').read_text())
results=[]
for patch in ('r11','r12'):
    raw=pathlib.Path(patch,patch+'.witnesses.txt').read_bytes(); n=len(spec['patches'][patch]['vertices'])
    def rejected(name, data=raw, obj=spec):
        try: C.check(obj,patch,data)
        except C.Rejected as e:
            results.append({'patch':patch,'mutation':name,'outcome':'rejected','first_assertion':str(e)}); return
        raise AssertionError('mutation survived: '+patch+'/'+name)
    rejected('delete_one_state',raw[:-(n+1)])
    rejected('append_extra_state',raw+raw[:n+1])
    bad=bytearray(raw); bad[1]=bad[0]; rejected('collapse_internal_edge',bytes(bad))
    bad=bytearray(raw); bad[spec['patches'][patch]['ports'][0]]=ord('0'); rejected('pin_port_equals_pin',bytes(bad))
    bad=bytearray(raw); bad[n]=ord(' '); rejected('change_row_delimiter',bytes(bad))
    bad=bytearray(raw); bad[0]=ord('g'); rejected('invalid_target_symbol',bytes(bad))
    obj=copy.deepcopy(spec); obj['patches'][patch]['ports'][0:2]=obj['patches'][patch]['ports'][1::-1]
    rejected('exchange_ordered_ports',obj=obj)
    obj=copy.deepcopy(spec); obj['patches'][patch]['edges'].pop(); rejected('omit_necessity_edge',obj=obj)
    obj=copy.deepcopy(spec); obj['patches'][patch]['edges'].append([0,2]); rejected('insert_extra_patch_edge',obj=obj)
    obj=copy.deepcopy(spec); obj['patches'][patch]['inequalities'][0]=[0,1]; rejected('wrong_boundary_predicate',obj=obj)
    obj=copy.deepcopy(spec); obj['target']['generators'][-1]=3; rejected('change_target_generator',obj=obj)
    # Positive control: arbitrary translation of BOTH pins and witness is valid.
    names,edges,ports,neq=C.source(patch,spec['patches'][patch]); sets,near,walks=C.target(spec)
    pins=next((0,)+t for t in itertools.product(range(16),repeat=len(ports)-1)
              if all(((0,)+t)[i]!=((0,)+t)[j] for i,j in neq))
    labels=[int(chr(v),16) for v in raw[:n]]
    for shift in sets:
        move=lambda v: sets.index(sets[v].symmetric_difference(shift))
        g=list(map(move,labels)); q=list(map(move,pins))
        assert all(near(g[u],g[v]) for u,v in edges)
        assert all(near(g[u],q[i]) for i,u in enumerate(ports))
    results.append({'patch':patch,'mutation':'translate_pins_and_witness','outcome':'accepted','translations':16})
report={'verdict':'candidate_only','status':'mutation_suite_pass','negative_mutations':22,
        'positive_mutations':2,'results':results,
        'table_mutations_are_not_family_counterexamples':True}
pathlib.Path('checks/mutations.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report))
