# Root-facing belt lifting: exact scope and conditional finite interface

candidate_id: candidate:opg434-a01-belt-lifting-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
status: NONTERMINAL_CHECKPOINT

This file proves the lifting implication below. It does not assert that an unobserved computation passed. The separately prepared finite boundary tables require their actual bytes, hashes and checker receipts before their hypotheses may be discharged. No original candidate or truth record is replaced.

## 1. Target and a replacement relation

Let B be the graph on even vectors of F_2^5, with t_i=J+e_i for i=0,...,4 and adjacency difference in {t_i}. The endpoint relation of a three-edge path is exactly inequality.

Equal endpoints would give a closed three-step walk in a loopless triangle-free target, impossible. For unequal endpoints with difference t_i, the generator sequence (t_i,t_j,t_j) realizes the difference. For difference p_ab=e_a+e_b, use the three different generators indexed by the complement of {a,b}; their sum is p_ab. These exhaust the nonzero even differences. Intermediate target vertices need not be distinct; this is a homomorphism, not an embedding.

## 2. Eleven-vertex patch and the finite obligation

Use internal vertex order (v0,v1,v2,v3,v4,x0,x2,x3,x4,y,t). Its edges are the central five-cycle, spokes v0-x0,v2-x2,v3-x3,v4-x4, and y-x2,y-x3,y-x4,t-x4,t-x0. There are eleven vertices and fourteen edges. Its four ports, in order, are (x0,x2,x3,t); v1 has total degree two in the intended occurrence.

Write R11(a,b,c,d) when the internal graph has a B-map respecting an additional neighbor of each port with those four prescribed labels. A necessary condition is a!=d: otherwise a-x0-t-d would map to a closed three-step walk. The precise remaining finite obligation is

  a!=d implies R11(a,b,c,d), for all a,b,c,d in V(B).

Translation sets a=0. There are exactly 15*16*16=3840 normalized tuples to cover. A positive certificate is one complete eleven-label internal map for every such tuple; a checker must verify coverage, every internal edge, all four spoke constraints, and translation invariance. This cardinality is the enumeration domain, not a claim that a particular execution succeeded.

## 3. A genuine root-valid lifting theorem

Assume the finite obligation in Section 2. Let G be finite, simple, triangle-free and subcubic, containing the indicated INDUCED eleven-vertex patch. Suppose its only exiting edges are one at each of x0,x2,x3,t. Denote their outside endpoints uA,uB,uC,uT. Other coincidences are allowed, but uA!=uT: equality would form the source triangle uA-x0-t-uA.

Delete all eleven patch vertices. Add two fresh vertices p,q and the three edges uA-p,p-q,q-uT. Call the new graph G'. It has |V(G)|-9 vertices. Every old endpoint loses at least as many patch incidences as it gains replacement incidences, even if other outside endpoints coincide. The fresh vertices have degree two. Therefore G' is subcubic.

G' is simple because p,q are fresh and uA!=uT. A triangle wholly in the old exterior was already in G. A triangle using p or q would require uA=uT, since their only neighbors are specified by the new three-edge path. Thus G' is triangle-free. An existing exterior edge uA-uT creates a four-cycle, not a triangle, and is allowed.

Take ANY B-map of G'. The new three-edge path forces the two outside labels a=f(uA),d=f(uT) to differ. Set b=f(uB),c=f(uC). Section 2 supplies an internal patch map for these four labels. Keep the entire exterior map unchanged, discard p,q and restore the patch. Every old exterior edge, every patch edge and every exiting edge is respected. This constructs a B-map of G.

Consequently, conditional on the finite boundary certificate, the eleven-vertex C16 merged-hub patch cannot occur in a vertex-minimum non-B-mappable triangle-free SUBCUBIC graph. Minimality is not taken in the cubic-only class. This is a valid smaller-instance lifting argument, not a claim that an arbitrary original exterior map admits bounded local repair. The smaller graph is colored afresh before lifting.

## 4. Twelve-vertex candidate interface

The distinct-hub patch has internal order (v0,v1,v2,v3,v4,x0,x2,x3,x4,r,z,t), edges the central cycle and four spokes, plus r-x2,r-x3,z-x3,z-x4,t-x4,t-x0. Its possible ports are (x0,x2,r,z,t). The internal port edges force the necessary outside-label inequalities a!=e and b!=c.

The separate finite question is whether these two inequalities are sufficient for every five-tuple (a,b,c,d,e). It has 57600 normalized tuples after a=0. This sufficiency is not assumed proved here.

If it holds, replace each fully present critical port pair by a fresh three-edge path. The two paths have disjoint new internal vertices. At most four vertices are added after deleting twelve, so order strictly decreases by at least eight. The endpoints in each pair are physically distinct by source triangle-freeness. Cross-pair coincidences are harmless: freed incidences pay for new incidences, and length-three fresh paths create no triangle. Missing port pins can be assigned fictitious labels after a smaller map is chosen; a path is needed only for a pair whose two exterior endpoints are present. The fifth pin imposes no additional replacement edge. This proves the analogous lifting implication IF the full finite relation is certified.

A failing five-tuple would reject that replacement rule only. It would not prove graph nonexistence, since a different exterior map may still lie in the patch relation. Any negative record must include the full patch, ordered ports, actual pin tuple and a complete rejection certificate.

## 5. Quantifier boundary and next open state

For an actual exterior H let Sigma(H) be the set of ALL simultaneously realizable ordered port-image tuples. Whole-graph colorability asks whether Sigma(H) intersects R11 or R12, not whether one chosen tuple extends. A replacement K is sufficient when its boundary relation is contained in the patch relation. Failure of this stronger inclusion is not failure of the root.

The layered-pentagon family excludes uniform bounded-radius/bounded-edit repair of EVERY prescribed exterior map. It does not exclude global rechoice of a map of G', nor either conditional lifting theorem above. A failed-route proposal belongs only in candidate artifacts; the admitted equivalence route and root remain open.

First finite interface awaiting a readable frozen certificate in this file: the 3840-state R11 sufficiency table. The next root frontier after any certified belt reductions is the all-degree-three central pentagon, including possible hub coincidences and actual exterior-state correlations. No trusted verifier, EvidenceLink, Result or Solution is created by this file. best_verified_result=none.
