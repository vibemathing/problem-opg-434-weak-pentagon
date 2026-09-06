# C10: simultaneous global switches, forest reachability and the C5 boundary

candidate_id: candidate:opg434-a01-c10-global-switching
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 048a5a5f0ddb8bc3f822eacd5770721f4e9ac968

This candidate moves from one prescribed local state to a construction on an
entire graph. The scope of that construction is proved exactly and attacked
by an explicit Petersen example. All arguments are on paper; no solver,
graph enumeration or kernel execution is claimed. Use C06-C08's generators.

## 1. A sufficient structural condition and two simultaneous switches

Let G be a finite simple graph and let X be a vertex subset such that:
(a) X is independent;
(b) its open neighborhood W=N_G(X) is independent;
(c) H=G-X is bipartite.
The empty X is allowed. No degree or planarity assumption is needed.

### claim:opg434-c10-global-two-switch
Under (a)-(c), a full G -> B map can be built by two legal subset translations
of any two-label map of H, followed by the simultaneous addition of X.

Choose a bipartition (A,D) of H and map A to 0, D to s_1.
Put U=W intersect D and T=N_H(U). Then T is contained in A and disjoint
from W: an edge from U to W would contradict (b).

First translate T by 12. Every cut edge initially has color s_1, so this
is legal by C08. All edges incident to U now have color s_2, since their
other endpoints lie in T. Next translate U by 23, also legal by C08.
The resulting labels are
A minus T -> 0, D minus U -> s_1, T -> 12, U -> 45.
Every neighbor of X lies either in A minus T or in U. Assign s_4 to every
vertex of X. Its differences to the two possible neighbor labels 0,45
are respectively s_4,s_5. There are no edges inside X. Thus all edges of G
are valid, including when some sets or components are empty.

For a direct audit, the only possible edges between the five displayed
classes follow the target cycle
0 -- s_1 -- 12 -- 45 -- s_4 -- 0.
Its five edge generators are s_1,s_2,s_3,s_5,s_4. Therefore the construction
actually maps G into a C5 subgraph of B, a stronger conclusion than the root.

### claim:opg434-c10-single-deletion
If G is triangle-free and G-v is bipartite for some vertex v, then G maps
to C5, regardless of its maximum degree.
Take X={v}; triangle-freeness makes N(v) independent.

More generally, in a triangle-free graph any bipartizing set X whose distinct
vertices have pairwise distance at least four satisfies (a)-(b), so the same
construction works. The distance condition is sufficient, not necessary;
the exact hypotheses remain (a)-(c). A hypothetical counterexample to the
root cannot have a one-vertex odd-cycle transversal.

## 2. Exact strength of the structural certificate

### claim:opg434-c10-c5-characterization
For every finite simple G:
G -> C5 if and only if there exists X satisfying (a)-(c).

The forward construction from X was given above. Conversely, given a map
g:G -> C5, let X be the preimage of one vertex of the target cycle.
Its fiber is independent. W maps into the two neighbors of that target
vertex, which are nonadjacent, so W is independent too. The graph G-X maps
to the remaining P4, and hence is bipartite. An empty fiber causes no problem.

Consequently searching for this structural certificate universally would
replace the B problem by a strictly stronger C5 problem. The next section
gives a concrete graph separating them. This is not a new formulation of
the root and is not Nesetril's sufficiently-high-girth Pentagon Problem.

## 3. A full Petersen separation, not a root counterexample

### claim:opg434-c10-petersen-separation
Define P on a_j,b_j for j modulo five, with edges a_j a_(j+1), a_j b_j
and b_j b_(j+2). It has no homomorphism to C5, but has an explicit map to B.

For nonexistence to C5, a map of the outer pentagon into C5 is a bijection:
a closed walk of length five in C5 must take all five steps in the same
orientation, since a sum of five signs is divisible by five only if it is
5 or -5. Normalize the images of a_j to j modulo five.
The spoke condition forces g(b_j)=j+epsilon_j with epsilon_j in {-1,1}.
For every inner edge b_j b_(j+2), the difference is
2+epsilon_(j+2)-epsilon_j, which is 0,2 or 4 modulo five.
Only 4 is an edge difference in C5, forcing epsilon_j=-1 and
epsilon_(j+2)=1 for every j. The requirements for j=0 and j=2 conflict.
This is a paper contradiction for the C5 target only.

For the full B map, use this index-pair table:
(a_0,a_1,a_2,a_3,a_4) -> (12,34,15,23,45);
(b_0,b_1,b_2,b_3,b_4) -> (35,25,24,14,13).
Two disjoint index pairs differ by the remaining generator. The displayed
outer edges, spokes and inner edges all join disjoint pairs, so every edge
maps correctly. Conversely, on all ten index pairs, disjointness gives
exactly these edges: each pair has three disjoint pairs. Thus P is finite,
simple and cubic. A triangle would need three disjoint two-element sets
inside a five-element set, impossible.

It follows that P has no X satisfying (a)-(c), despite satisfying the B
homomorphism condition. We have not contradicted the Weak Pentagon root
or the sufficiently-high-girth C5 conjecture.

One explicit independent bipartizing set in this P is
X={12,13,14} in the pair presentation. The remaining graph is the tree
with center 15 and three length-two branches
15-23-45, 15-24-35, 15-34-25.
Its boundary W consists of the six noncentral vertices and induces the
three edges 23-45, 24-35, 34-25. This pinpoints the violated hypothesis (b).
Independence of X plus a forest complement alone is not enough for the
particular two-switch construction, even though P itself is feasible.

## 4. Arbitrary forest maps lie in one cut-switch component

### claim:opg434-c10-forest-reachability
Let F be a finite forest with k components. For any two maps f,g:F -> B,
one can transform f into g by at most |E(F)|+k legal uniform subset
translations. No claim is made about the cost of maintaining other external
constraints while these translations are performed.

Root every component. Translate each entire component so its root has the
g-label. Such a translation has an empty edge cut. For each oriented tree
edge uv with child v, compare its current generator s_i with the desired
one s_j=g(u)+g(v). If they differ, translate the entire subtree at v by ij.
Its only cut edge is uv and the move changes its generator from s_i to s_j.
Every other edge generator and each component root are unchanged.
After all edges are correct, their path sums from the roots show equality
of all vertex labels with g. At most one nontrivial move per edge is used.
Isolated vertices are covered by the component translations.

The desired extendible map g is an INPUT to this statement. Connectivity
of the forest-map space does not prove that an extendible g exists after
the deleted vertices and their coupled boundary constraints are restored.
This distinction is essential when importing near-bipartite decompositions.

## 5. The cubic C08 obstruction has a two-step cure

### claim:opg434-c10-prism-two-step
Return to C08's prescribed map of the pentagonal prism with a_0 removed:
(a_1,a_2,a_3,a_4)=(0,s_1,0,s_1),
(b_0,...,b_4)=(23,s_2,0,s_1,14).
Translate the singleton {a_2} by 12. Its three incident edges initially
have generator s_1, and they now have generator s_2.
Next translate {a_1} by 23; its two incident edges now both have s_2.
The terminal labels at a_1,a_4,b_0 become (23,s_1,23).
Give a_0 label 14. Its incident differences are s_5,s_4,s_5.
This restores the full graph and checks every changed edge.
C08's one-step failure therefore does not persist for two steps even in
its 3-edge-connected cubic witness.

## 6. Scope, source comparison and the next obstruction

Sources are compared in
research/artifacts/source-notes/opg434-a01-c10-bipartization-comparison.md.
The cited near-bipartite theorem concerns an independent set and a forest
complement, not an independent OPEN NEIGHBORHOOD and not a B extension.
C10 does not assume that theorem to prove any of its constructions.

Reproduce by checking the two switch cuts, all five label classes, the
C5-fiber converse, the two explicit Petersen descriptions, the forest edge
updates, and the two prism singleton moves. No runtime receipt is supplied.
Both admitted obligations remain open; best_verified_result=none and
best_verified_candidate=none.

Next: use the full ordered triple relation, including repeated labels and
low-degree list flexibility, to settle gluing across a three-edge cut.
Then confront four-terminal configurations where C09 already proves that
lower-arity projections alone can lose the obstruction.
