# C10: global construction with two-vertex bipartization

candidate_id: candidate:opg434-a01-c10-two-vertex-bipartization
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 048a5a5f0ddb8bc3f822eacd5770721f4e9ac968

Use B, s_1,...,s_5 and ij=s_i+s_j from C06-C09.
This is a constructive paper proof for an infinite class of source graphs,
not another fixed-boundary test. No mathematical program or kernel was run.

## 1. The new global statement and its scope

Let tau_v(G) be the minimum number of VERTICES whose deletion leaves a
bipartite graph. This is not an edge transversal number.

### claim:opg434-c10-global-two-apices
Every finite simple triangle-free graph G with tau_v(G)<=2 maps to B.
No degree bound, connectedness or planarity assumption is required.

The maps below are constructed from a chosen bipartition of the remainder;
they need not agree with an arbitrary previously prescribed homomorphism.
The conclusion gives the root's five-color assignment through C02, but only
on this stated subclass. It does not establish that every cubic graph
belongs to the subclass.

## 2. One deletion vertex: an explicit commuting two-switch construction

### claim:opg434-c10-one-apex-two-switch
Suppose H=G-v is bipartite with parts A,D. Map H initially by
f_0(A)=45 and f_0(D)=12, so every edge difference is s_3.
Put X=A intersect N_G(v) and Y=D intersect N_G(v).
There are no edges between X and Y, since G is triangle-free.

First translate the labels on X by 23, then those on Y by 34.
Each cut initially consists only of s_3-colored edges, so each translation
is legal by C08. The two supports have no edge between them; consequently
the first translation does not change the colors on the second cut,
and the two operations also commute.

The final map, including v, is:
v -> 0;
A intersect N(v) -> s_1;
D intersect N(v) -> s_5;
A minus N(v) -> 45;
D minus N(v) -> 12.

For the surviving H-edges, the only possible label pairs are
(45,12), (s_1,12), (45,s_5), with differences s_3,s_2,s_4.
The omitted pair (s_1,s_5) would require an edge between X and Y.
All edges at v have difference s_1 or s_5.
These five image vertices form a C5, so this proves the stronger
one-apex conclusion G -> C5 -> B.

This is a two-switch construction from the displayed base map, not a claim
that every map of H can be repaired by two switches. Thus it does not
silently replace the quantified repair questions of C07 or C08.

## 3. Two nonadjacent deletion vertices

Suppose a!=b, ab is not an edge, and H=G-{a,b} has bipartition A,D.
For each u in H set T(u)=N_G(u) intersect {a,b}.
Triangle-freeness implies T(u) intersect T(w) is empty for every H-edge uw.
Indeed a common apex together with uw would be a triangle.

Set f(a)=0 and f(b)=12. Use the following table:

| T(u) | u in A | u in D |
|---|---|---|
| empty | 24 | 13 |
| {a} | s_3 | s_4 |
| {b} | 45 | 35 |
| {a,b} | s_1 | s_2 |

This assigns every vertex, including isolated vertices, a definite label.
All permitted cross-type edges are audited in the following list; the
last column is their generator difference:

| A type | D type | difference |
|---|---|---|
| empty | empty | s_5 |
| empty | {a} | s_2 |
| empty | {b} | s_1 |
| empty | {a,b} | s_4 |
| {a} | empty | s_1 |
| {a} | {b} | s_5 |
| {b} | empty | s_2 |
| {b} | {a} | s_5 |
| {a,b} | empty | s_3 |

These nine entries exhaust the pairs of disjoint subsets of {a,b}.
For edges at a, the possible other labels s_3,s_4,s_1,s_2 are generators.
For edges at b=12, differences to 45,35,s_1,s_2 are respectively
s_3,s_4,s_2,s_1. Hence every edge of G maps to an edge of B.

In particular a and b can be prescribed ANY two distinct nonadjacent
target labels: apply the affine pair symmetry from C06 to the whole map.

## 4. Two adjacent deletion vertices

Suppose instead ab is an edge. No vertex in H can neighbor both a and b.
Set f(a)=0, f(b)=s_1 and use:

| T(u) | u in A | u in D |
|---|---|---|
| empty | 34 | 25 |
| {a} | s_2 | s_3 |
| {b} | 13 | 12 |

The seven possible cross-type edges have differences:

| A type | D type | difference |
|---|---|---|
| empty | empty | s_1 |
| empty | {a} | s_4 |
| empty | {b} | s_5 |
| {a} | empty | s_5 |
| {a} | {b} | s_1 |
| {b} | empty | s_4 |
| {b} | {a} | s_1 |

Edges at a have differences s_2,s_3; edges at b have differences s_3,s_2;
the edge ab has difference s_1. This checks every edge.
By C06's symmetries, any prescribed adjacent images of a,b can be used.

Sections 2-4 prove Section 1. If no deletion is needed, use any target edge
and a bipartition. Graphs too small to contain two distinct apices are
covered by this case or Section 2. Disconnected graphs require no extra
argument: a bipartition can be chosen on every remaining component.

## 5. The complete attainable relation at a bipartizing pair

### claim:opg434-c10-pair-relation
Let G be finite, simple and triangle-free, let a!=b, and suppose G-{a,b}
is bipartite. Define Sigma(G;a,b) using ALL homomorphisms, with types
0=equal, 1=adjacent, 2=distinct nonadjacent as in C06.

If ab is an edge, Sigma={1}.
If ab is not an edge, then:
- type 2 always belongs to Sigma;
- type 1 belongs to Sigma exactly when a,b have no common neighbor;
- type 0 belongs to Sigma exactly when there is no SIMPLE LENGTH-THREE
  path from a to b in G.

The first assertion and type 2 follow from the tables.
A common neighbor makes adjacent images impossible because B has no triangle.
If there is no common neighbor, adding ab keeps the graph triangle-free,
does not change its bipartite remainder, and Section 4 gives type 1.

For type 0, a length-three path would map to a closed three-step walk in B,
which is impossible in a loopless triangle-free graph.
Conversely, when ab is absent and no such path exists, identify a and b
to a single vertex q and replace any parallel edges by one edge.
There are no loops. The quotient is triangle-free: any new triangle
q-u-w-q would either lift to an old triangle or to a simple path a-u-w-b.
Deleting q leaves the same bipartite remainder. Section 2 maps this
quotient to C5, and pulling the map back realizes equal images of a,b.

The criterion is existence of a length-three simple path, not a condition
only on the shortest-path distance. For example, a pair may have both a
length-two path and a length-three path.

## 6. Why the two-apex conclusion cannot be upgraded to C5

### claim:opg434-c10-cubic-c5-boundary
There is an explicit eight-vertex triangle-free cubic graph with a
two-vertex bipartizing set which maps to B but not to C5.

Take vertices a,b,A0,D0,Aa,Da,Ab,Db and precisely the twelve edges:
ab, aAa, aDa, bAb, bDb,
A0D0, A0Da, A0Db, AaD0, AaDb, AbD0, AbDa.

The bipartite remainder has parts {A0,Aa,Ab} and {D0,Da,Db};
its types are those indicated by the names.
The edge list gives degree three at all eight vertices. It is triangle-free:
the remainder is bipartite, no remainder edge has a shared apex type,
and no remainder vertex is adjacent to both a and b.
The table of Section 4 is an explicit full B-homomorphism.

Suppose a map to C5 existed. By a cycle symmetry set a->0 and b->1
in cyclic labels 0,1,2,3,4.
Every homomorphism of a 5-cycle into C5 is a bijection: its five +/-1
steps must sum to a multiple of five, forcing all steps to have one sign.
The 5-cycle a-Aa-D0-Ab-b-a thus forces Aa->4, D0->3, Ab->2.
The 5-cycle a-Da-A0-Db-b-a forces Da->4, A0->3, Db->2.
But the edge AaDb would join labels 4 and 2, which are nonadjacent in C5.
This contradiction concerns only the stronger C5 target, not B or the root.

## 7. Consequence, reproducibility and remaining obstacle

### claim:opg434-c10-counterexample-filter
Any counterexample to the frozen root, or to its triangle-free subcubic
version, must have tau_v(G)>=3. This uses actual constructed whole-graph
maps, not selected boundary failures and not separator cleanup.

Given a deletion set of size at most two and a verified bipartition of
the remainder, the tables can be applied in O(|V|+|E|) elementary work.
This is an algorithmic consequence of the paper construction, not a
runtime measurement or claim of an executed graph search.

Audit the five image values in Section 2; all nine and seven cross-type
entries in Sections 3-4; the quotient in the type-0 proof; and both
5-cycles and the extra edge in the eight-vertex witness.
Only C02 and the explicit generator facts of C06 are needed for the global
theorem; C08 is used to identify the two-switch interpretation.

Source comparison: research/artifacts/source-notes/opg434-a01-c10-bipartization-comparison.md.
All claims remain candidates; no old artifact or truth record is changed.
best_verified_result=none; best_verified_candidate=none.
Both admitted obligations remain open.

The next unique mathematical obstacle is the degree-sensitive three-apex
case. A useful next attack is to identify exactly why extending the
two-apex type-table construction to three apices can force a forbidden
target relation, and whether subcubic degree budgets exclude that relation.
