# C11: a degree-four obstruction and the limit of bipartization induction

candidate_id: candidate:opg434-a01-c11-degree-budget
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: bcbe66a0033c7853a9589c59365f42bc7b72a1d5

The auxiliary statement tested is: every finite simple triangle-free graph
with vertex bipartization number at most three maps to B, WITHOUT a degree
bound. This is not the root statement. The explicit obstruction below has
five vertices of degree four. No mathematical program or kernel was run.

## 1. A three-edge path implements disequality

### claim:opg434-c11-path-disequality
For prescribed endpoints x,y in B, a walk of length three from x to y
exists exactly when x!=y.

A closed three-step walk would be a triangle in the loopless target, so
equality is impossible. If x+y=s_i, use x,y,x,y. If x+y=ij, take the
three complementary generators, in any order, as the successive differences.
Their sum is ij by the unique five-generator relation. This covers all
distinct pairs. Intermediate images may repeat; that is allowed for a
source path homomorphism. No injectivity requirement is imposed.

## 2. Exact source graph and no-homomorphism certificate

Define J on thirteen vertices:
a,b,c,u,w,ab1,ab2,ac1,ac2,bc1,bc2,uw1,uw2.
Its edges are the six edges joining {u,w} to {a,b,c}, together with the
four internally disjoint length-three paths
a-ab1-ab2-b, a-ac1-ac2-c, b-bc1-bc2-c, u-uw1-uw2-w.
There are no other edges. A machine-readable edge list is in
research/artifacts/candidates/opg434-a01-c11-obstruction.json.

### claim:opg434-c11-source-audit
J is simple, triangle-free and connected, with 13 vertices and 18 edges.
Exactly a,b,c,u,w have degree four; the eight internal vertices have degree two.
Deleting {a,b,c} leaves the path u-uw1-uw2-w and three separate edges,
hence a bipartite graph. Its ordinary girth is four, from the retained K2,3;
its odd girth is five, for instance a-ab1-ab2-b-u-a.

The retained K2,3 is triangle-free. Any cycle that uses an internal path
vertex must use the whole three-edge path; its endpoints have no direct
edge, so this cannot form a triangle. This proves the asserted triangle
restriction without confusing ordinary and odd girth.

### claim:opg434-c11-no-map
There is no homomorphism J -> B.

Suppose f were one. The images of a,b,c are pairwise nonadjacent, because
each pair has u as a common neighbor. They are pairwise distinct by the
three length-three paths and Section 1. C07's exact triple theorem says
that three distinct pairwise nonadjacent target vertices have a UNIQUE
common neighbor. Both f(u) and f(w) must be this common neighbor, so
f(u)=f(w). The length-three u-w path contradicts Section 1. This finishes
a finite paper certificate for graph-level nonexistence on this J, not
merely failure of one prescribed partial map.

By C10, which covers all triangle-free graphs with vertex bipartization
number at most two, J's vertex bipartization number is exactly three.
This last equality has C10 as a candidate dependency; the no-map proof
itself only uses C06-C07.

## 3. Minimality within this witness, not minimum order

### claim:opg434-c11-edge-critical
Deleting ANY one edge of J yields a B-homomorphism. Consequently every
proper subgraph of this J maps to B. No claim is made that J is a
minimum-order obstruction among all graphs of maximum degree four.

The symmetries permuting a,b,c and interchanging u,w reduce edge deletion
to three types. Give the five branch-vertex labels as follows.

| deleted edge type | a | b | c | u | w |
|---|---|---|---|---|---|
| any edge of the a-b path | 0 | 0 | 12 | s_1 | s_2 |
| any edge of the u-w path | s_1 | s_2 | s_3 | 0 | 0 |
| retained edge u-a | s_1 | s_2 | s_3 | 23 | 0 |

In each row every retained direct branch edge has generator difference.
Every intact length-three path has distinct nonadjacent endpoint images,
so its internal labels are supplied by the complementary-three-generator
recipe of Section 1. A broken path leaves rooted paths or isolated vertices;
extend them successively along any target edge. The displayed assignments
therefore check all edge-deletion types, including middle-path edges.
A vertex deletion is a subgraph of an incident-edge deletion, so it also
maps to B. All remaining proper subgraphs follow by restriction.

## 4. The degree budget cannot be discarded

### claim:opg434-c11-twin-reduction
If x,y are distinct nonadjacent vertices of a source graph and
N(x) is a subset of N(y), every homomorphism of G-x extends by f(x)=f(y).
This is checked on each restored edge xz using the already present yz.

In a subcubic graph, two vertices both adjacent to three distinct vertices
have exactly those three neighbors. They are twins, so this configuration
cannot occur in a vertex-minimum non-B-mappable triangle-free subcubic graph.

J defeats that copy-label extension by adding a fourth incident path at
each of u,w. Its three remaining branch vertices also have degree four.
Thus J does not contradict the frozen cubic question or a still-unproved
three-apex SUBCUBIC theorem. C05's cubic completion takes maximum degree
AT MOST THREE as an input condition, so it cannot turn J into a root
counterexample. Splitting degree-four vertices would require an additional
proved homomorphism-preserving gadget; none is supplied here.

## 5. Source boundary and next action

Suppressing J's eight internal degree-two vertices recovers K5. Therefore
this example has a K5 minor and lies outside the triangle-free K5-minor-free
positive class reported in the primary source note. No planar argument is used.

This file precisely defeats only the degree-free extension of C10 from two
to three deleted vertices. Save that failed auxiliary statement, not the
admitted equivalence route, in the failed-route proposal. All prior packets
remain immutable; no truth ledger is changed.

Reproduce on paper from the edge list, the three-step path rule, C07's
unique common-neighbor lemma and the three edge-deletion rows. The JSON
is an input witness, not a solver result or verifier receipt.
best_verified_result=none; best_verified_candidate=none.
Both admitted obligations remain open.

Next: square reducibility within the ACTUAL degree-three class. The pending
proof uses the exact four-pin relation, a feasible six-cycle for recoloring
a low-degree source edge, and smaller triangle-free subcubic replacements.
