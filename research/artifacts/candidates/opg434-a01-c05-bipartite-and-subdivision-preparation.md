# OPG434: bipartite terminal distance and subdivision preparation

Status: candidate_only. Supplemental c05 preparation, not a new packet, admitted obligation, verifier receipt or universal cubic existence proof. No mathematical execution and no novelty claim. Exact content digest and registration remain pending readable transport receipts.

Problem: problem:opg-434-weak-pentagon. Attempt: attempt:web-20260906-opg434-a01. Route: route:odd-cycle-transversal-equivalence-v1. Graph: graph:opg434-initial-v1. Target: obligation:opg434-five-transversals-equivalence. Root remains open. Primary owner: math-derivation.

Dependencies: c01 equivalence, c02 even-five-bit target, and the supplemental path-signature derivation. Define H on even vectors of F_2^5, adjacency differences s_i=J+e_i. Put n_ij=e_i+e_j. Z/A/N mean equal/adjacent/distinct nonadjacent images. A path of length d has relation R_0=Z, R_1=A, R_2=Z union N, R_3=A union N, and R_d=U for d>=4.

## 1. Exact signatures of any bipartite two-terminal graph

Let B be bipartite, with terminals x,y in the same component at distance d>=1. Its exact H terminal relation is R_d, not merely a subset.

One inclusion follows by restricting a homomorphism to a shortest x-y path. For the reverse inclusion, let h(v)=dist_B(x,v) on that component and define a map to the vertex set {0,...,d} of P_d by

f(v)=h(v) if h(v)<=d;
f(v)=d if h(v)>d and h(v) has the parity of d;
f(v)=d-1 otherwise.

For adjacent vertices their distances from x differ by exactly one: the general difference bound is at most one, and equality of distances would violate bipartiteness. At levels below d the displayed map preserves this unit difference. Above d it alternates d,d-1; crossing the threshold also gives consecutive values. Thus f is a graph homomorphism B->P_d with f(x)=0 and f(y)=d. Other components can be mapped to the edge {0,1}. Composing with any path homomorphism realizes every pair in R_d.

If the terminals coincide, the relation is exactly Z because B is H-colorable. If they lie in different components, the relation is U: bipartite components map to a target edge, and even translations permit any chosen target image at each marked vertex separately.

Consequences. Distinct nonadjacent terminals of a bipartite piece always permit type N. The only bipartite piece that can force singleton Z has repeated terminals. If two bipartite pieces are joined by two cross edges, their only possible incompatible signatures are repeated terminals on one side and adjacent terminals on the other; this makes a triangle in the joined graph. Hence a triangle-free such two-edge join of bipartite pieces is H-colorable. This conclusion does not cover arbitrary larger separators or nonbipartite pieces.

## 2. Any triangle-free subdivision of K4 is H-colorable

The short-edge graph on the four branch vertices records exactly those branch paths of length one. It must be triangle-free whenever the subdivision is triangle-free. The target H contains an induced copy of every triangle-free simple graph on four vertices. Explicit representatives for its seven isomorphism types are as follows; unlisted edges within each chosen set are absent because their differences have weight zero or two.

| four-vertex type | target vertices |
| --- | --- |
| empty | s_1,s_2,s_3,s_4 |
| one edge and two isolated vertices | 0,s_1,n_23,n_24 |
| two disjoint edges | 0,s_1,n_23,n_45 |
| a two-edge path and an isolated vertex | 0,s_1,s_2,n_34 |
| a three-edge path | 0,s_1,n_12,n_34 |
| a three-leaf star | 0,s_1,s_2,s_3 |
| a four-cycle | 0,s_1,n_12,s_2 |

To check completeness of this list, a triangle-free graph on four vertices with maximum degree three is either the star when a degree-three vertex is present, or has maximum degree at most two and consists of paths/cycles, giving the other six types. An additional edge between leaves of the degree-three vertex would create a triangle.

Inject the four branch vertices into the appropriate displayed copy of their short-edge graph. A length-one branch path is then an edge of H. All other endpoint pairs are distinct and nonadjacent: they are in N, which is allowed for length two, length three, and every greater length by the path-signature formula. Fill each internally disjoint path separately. This proves the claim for arbitrary subdivision lengths, not only odd lengths. It is not a theorem for arbitrary cubic graphs with more branch vertices.

## 3. Any subdivision of K_{3,n} is H-colorable

Let the three branch vertices on the size-three side be x_1,x_2,x_3, and map them to s_1,s_2,s_3. For a branch vertex y on the other side let T be the subset of {1,2,3} for which the x_i-y branch path has length one. Choose its image from this table:

| T | image of y |
| --- | --- |
| empty | n_45 |
| {1} | n_14 |
| {2} | n_24 |
| {3} | n_34 |
| {1,2} | n_12 |
| {1,3} | n_13 |
| {2,3} | n_23 |
| {1,2,3} | 0 |

A weight-two vertex n_jk is adjacent to s_i exactly when i is in {j,k}; zero is adjacent to all three. No entry in the right column equals s_1,s_2 or s_3. Consequently the chosen endpoint pair is A precisely for short paths, and N for every other path. All longer paths can be filled independently, as above. Reusing the same target image for different y vertices is permitted because there are no edges between them in the skeleton and no prescribed injectivity requirement.

The argument applies to all n, but the original degree-three domain includes this whole subdivision family only when the branch degrees are at most three (in particular K_{3,3}). It must not be described as a cubic construction for n>3. These subdivisions have no triangles, since any cycle projects to a skeleton cycle of length at least four.

## 4. Why the next kernel is not automatic

The four-branch induced-copy argument cannot simply be extended to all five-vertex triangle-free short-edge graphs: H has exactly two common neighbors for each distinct nonadjacent pair, so it contains no injective K_{2,3}. The separate 13-vertex odd subdivision of K5 in the domain-boundary preparation uses this obstruction, with long paths preventing the needed identifications. That graph has branch degree four and is outside the frozen domain.

These are exact restricted-class constructions and terminal refinements. They do not exclude every hypothetical triangle-free cubic counterexample, register new obligations, or supply executable/formal verification. Next audit: verify each small label table, the bipartite distance-fold map, and the distinction between injective branch placement used in part 2 and arbitrary homomorphisms used elsewhere. Only freeze them in a uniquely bound future packet after recovering real main, PR head and check receipts.
