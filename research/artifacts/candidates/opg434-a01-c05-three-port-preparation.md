# OPG434: exact three-port alignment and its four-port boundary

Status: candidate_only. Supplemental preparation during the unconfirmed c05 transaction, not a second packet, a closed obligation or an executed verification. Primary owner: math-derivation. No novelty claim; source comparison beyond the existing target-model note remains pending.

Binding: problem:opg-434-weak-pentagon / attempt:web-20260906-opg434-a01 / route:odd-cycle-transversal-equivalence-v1 / graph:opg434-initial-v1 / obligation:opg434-five-transversals-equivalence. Root obligation:opg434-root remains open.

Dependencies: c01 fixed-coloring equivalence; c02 target/normalization candidate; the two-port supplemental preparation. This note concerns chosen graph-homomorphism certificates and target automorphisms. It does not promise to preserve an arbitrary original edge assignment.

## 1. Target and automorphism facts

Let H have even vectors in F_2^5 as vertices. Write s_i=J+e_i, n_ij=e_i+e_j. Its edge differences are the five s_i. Z/A/N mean equal/adjacent/distinct nonadjacent pairs, respectively. Every even translation and coordinate permutation preserves H.

Two ordered triples are related by such an automorphism exactly when their equality and adjacency relations agree. To see sufficiency, translate their first entries to zero. The other two differences have weights zero, two or four. Their individual weights and mutual difference weight determine the sizes of their supports and their intersection. A coordinate permutation matches the four regions of the two supports. This also covers coincident entries. Necessity is immediate.

Any independent set of at most three vertices in H has a common neighbor. For three distinct vertices, translate one to zero; the other two are weight-two vectors whose supports meet in exactly one index i, since they are distinct and nonadjacent. The vertex s_i is their common neighbor and the only common neighbor of all three. For two distinct nonadjacent vertices, translation reduces to zero and n_ij, whose common neighbors are s_i,s_j. The one-vertex case uses any of its five neighbors.

## 2. Exact three-port theorem

For ordered triples a=(a_1,a_2,a_3), b=(b_1,b_2,b_3) of target vertices, an automorphism beta of the displayed translation/permutation form satisfies a_i adjacent beta(b_i) for every i if and only if there are no indices i<j with either

(a_i=a_j and b_i adjacent b_j), or
(b_i=b_j and a_i adjacent a_j).

Thus the two-port forbidden pair Z/A, in either direction, applied to all three pairs of positions is also sufficient for THREE ports. This is a claim about the exact target H, not an arbitrary triangle-free target.

Necessity: either forbidden pattern would give a target triangle after alignment.

For sufficiency, simultaneous permutations of port positions, target automorphisms on a, and exchange of the two sides preserve existence of an alignment. Exchange is justified by using the inverse alignment and the undirected edges. The cases below exhaust the equality patterns.

### Case A: both triples have distinct entries

Let I denote the independent ordered triple (s_1,s_2,s_3), E the triple (0,s_1,n_23) with edge 1-2, and P the triple (s_1,0,s_2) with center 2. The following nine rows cover all relative induced-graph types up to the above symmetries. Each row supplies b' in the required orbit of b and has a_i adjacent b'_i for every i.

| a | required type/position for b | b' |
| --- | --- | --- |
| I | independent | (n_14,n_24,n_34) |
| I | one edge, 1-2 | (n_14,n_25,0) |
| I | path, center 2 | (n_14,n_25,n_34) |
| E | one edge, 1-2 | (s_2,n_12,s_3) |
| E | one edge, 1-3 | (s_4,n_12,n_14) |
| E | path, center 3 | (s_4,n_12,n_45) |
| E | path, center 1 | (s_4,n_14,n_45) |
| P | path, center 2 | (n_13,s_3,n_23) |
| P | path, center 1 | (n_13,s_1,n_24) |

Each entry can be checked by adding the displayed vectors and obtaining a generator. Completeness: a distinct target triple has either zero, one or two edges; a triangle is impossible. If one triple is independent, all port permutations of it are equivalent, giving the first three rows. For two single-edge triples the edges either coincide or differ. For an edge and a path, the path center is either the isolated position of the edge triple or one of its two edge positions. For two paths, their centers coincide or differ. These are exactly the remaining six rows. The preceding automorphism fact converts the supplied representatives into an alignment of the original triples.

### Case B: one triple is constant

The pairwise condition says that the distinct entries of the other triple form an independent set. It has at most three vertices, so it has a common neighbor w by section 1. Translate w to the constant entry of the first triple. This aligns all three edges. The reverse orientation follows by symmetry.

### Case C: a has exactly two equal entries, b has three distinct entries

Permute ports and normalize a to (0,0,z), where z=s_1 (type A) or z=n_12 (type N). The pairwise condition requires b_1,b_2 to be nonadjacent. The possible distinct-triple types for b are independent, one edge incident to position 3, or a path with center 3. Swapping positions 1 and 2 covers the two single-edge positions. Explicit aligning representatives are:

| z | type of b | b' |
| --- | --- | --- |
| s_1 | independent | (s_3,s_4,n_12) |
| s_1 | edge 1-3 | (s_2,s_3,n_12) |
| s_1 | path center 3 | (s_1,s_2,n_12) |
| n_12 | independent | (s_3,s_4,s_1) |
| n_12 | edge 1-3 | (s_3,s_1,n_34) |
| n_12 | path center 3 | (s_3,s_4,n_34) |

The same vector checks and orbit argument prove the case.

### Case D: each triple has exactly two equal entries

If the repeated positions coincide on both sides, the three constraints reduce to two constraints between distinct pairs. Their pair types are A or N, and all four combinations are compatible by the two-port sum-of-generators calculation S+S={0} union {n_ij:i!=j}.

If the repeated positions differ, write a=(x,x,z), b=(y,t,y). The pairwise condition forces x,z to have type N and y,t to have type N. Normalize x=0,z=n_12 and choose y'=s_1,t'=s_2. Then 0-s_1, 0-s_2, and n_12-s_1 are all target edges. This proves sufficiency. It completes the equality-pattern cases.

For an actual graph obtained from two disjoint pieces by three cross edges, apply this theorem to the images of the three ordered boundary vertices. Repeated boundary vertices are allowed subject to the actual cross edges being distinct in a simple graph. Taking ALL realizable triple types on both pieces gives an exact existential gluing test. A failed test on ONE pair of side homomorphisms is not a graph-uncolorability certificate.

## 3. Four ports: pairwise and even three-wise tests are insufficient

Set a=(0,0,0,0) and b=(0,n_12,n_13,n_23). The four entries of b are distinct and pairwise nonadjacent. Thus every pair avoids the forbidden pattern, and every three-port subproblem is alignable by the theorem.

However b has no common neighbor. A neighbor of zero is s_i. To be adjacent to n_12 and n_13, its index must lie in {1,2} intersect {1,3}={1}. But s_1 is not adjacent to n_23. No automorphism can put all four entries of b in the neighborhood of zero: applying its inverse would provide a common neighbor of the original b. Therefore the four-port alignment fails.

This counterexample concerns chosen boundary certificates, not existence of any homomorphism of the joined graph. It can even be realized with triangle-free subcubic pieces whose join is bipartite. Take two disjoint paths A_0...A_6 and B_0...B_6, with ports at positions 0,2,4,6. Give their target label sequences

A: (0,s_1,0,s_1,0,s_1,0),
B: (0,s_1,n_12,s_1,n_13,s_3,n_23).

Every consecutive pair in each sequence is an edge of H. Join A_i to B_i only at the four even positions. The 14-vertex joined graph is bipartite, using vertex parity i plus a flip on one path, and has maximum degree three. Hence it certainly has valid five-edge assignments. Nevertheless these two particular side homomorphisms cannot be joined by applying one target automorphism to the B side while keeping the A labels fixed. Rechoosing side certificates can repair the situation; declaring the graph uncolorable from this alignment failure would be wrong.

## 4. Audit and next step

Review every row of the two tables, the ordered-triple orbit argument, all repeated-port cases, and the common-neighbor calculation for four ports. These are symbolic paper checks, not an executed enumeration. Four-port signatures need information beyond just pairwise equality/adjacency: independent quadruples may differ in whether they have a common neighbor. Source attribution and executable/formal verification remain separate tasks. Freeze only in a correctly bound later packet after real main, current c05 head and transport receipts are recovered.
