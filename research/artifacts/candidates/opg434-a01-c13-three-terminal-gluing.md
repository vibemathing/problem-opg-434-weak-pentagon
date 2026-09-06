# C13: exact triple transport and cyclic three-edge-cut reduction

candidate_id: candidate:opg434-a01-c13-three-terminal-gluing
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 0817fc9a53c65ebc2f162714143974f51daec3d2

This paper candidate reuses C06-C07's explicitly defined target, generator
notation s_i, ij, affine symmetries, and common-neighbor facts.
It strengthens the boundary-state induction after C12's square reduction.
No mathematical computation, enumeration, kernel or external verifier ran.

## 1. The exact transport relation for two ordered triples

### claim:opg434-c13-triple-transport
Let A=(a_0,a_1,a_2) and B'=(b_0,b_1,b_2) be arbitrary target triples,
including repetitions. There exists an affine target automorphism g
with a_i adjacent to g(b_i) for every i if and only if no pair of
positions is equal in one triple and adjacent in the other.

Necessity: equality on one side would make the two adjacent labels on
the other side share a common neighbor, creating a target triangle.

For sufficiency choose a generator-permuting linear automorphism L and
put d_i=a_i+L(b_i). A translation t completes the matching edges exactly
when t is a common neighbor of d_0,d_1,d_2. By C07, it suffices that the
d_i be pairwise nonadjacent, with equality permitted. Translation of
either initial triple, independent normalization, and a simultaneous
permutation of positions do not change the question.

Every triple of distinct target labels induces one of three types:
I = an independent triple, represented by (0,12,13);
P = a two-edge path, represented by (0,s_1,s_2), center at position 0;
E = one edge plus an isolated vertex, represented by (0,s_1,23), edge 01.
C06's generator permutations are transitive on each such ordered
positional pattern. For I, the two pair indices after translation must
overlap in one index; disjoint pairs would make the third pair adjacent.
For P normalize its two edge differences. For E the isolated label's
two indices avoid the edge index. These also prove the asserted orbit
coverage without assuming it from a graph name.

When both triples have distinct entries, equal types with the same
positional edge pattern can be aligned identically, giving all d_i=0.
The remaining cases, up to interchanging the two triples and positions,
are the following. The last column lists d_0+d_1,d_0+d_2,d_1+d_2;
zero or a pair ij is nonadjacent, as required.

| A | chosen B' representative | differences of d |
|---|---|---|
| (0,s_1,23) | (0,23,s_1) | 45,45,0 |
| (0,s_1,s_2) | (s_3,0,s_4) | 13,15,35 |
| (0,12,13) | (0,s_3,s_2) | 45,45,0 |
| (0,12,13) | (0,s_5,13) | 34,0,34 |
| (0,s_1,s_2) | (0,s_3,45) | 13,13,0 |
| (0,s_1,s_2) | (s_3,0,12) | 13,13,0 |

The first two rows handle differing E-edge positions and P-center positions.
The last two distinguish whether the E-edge meets the P-center or lies
opposite it. Thus all distinct-entry cases are covered.

If a triple is constant, the pairwise condition says the other triple
is pairwise nonadjacent. Its common neighbor, supplied by C07, gives
the required translated map directly.

Otherwise suppose A has exactly two values and normalize it to
(0,0,h), with h=s_1 or h=12. If the other triple has the same duplicate
positions, the claim is exactly C06's two-terminal compatibility table.
If it has different duplicate positions, the pairwise condition forces
both unequal-value differences to be type 2. Normalize the other
triple to (0,12,0) or (0,12,12), matching h=12; the resulting d triple
is pairwise nonadjacent.

It remains that B' has three distinct values. Its entries in positions
0 and 1 must be nonadjacent. Its possible types are I, P centered at 2,
or E with its edge incident to 2. Interchanging positions 0 and 1
handles the two E positions. The following rows finish these cases:

| A | type of B' | chosen B' | differences of d |
|---|---|---|---|
| (0,0,s_1) | P | (0,12,s_1) | 12,0,12 |
| (0,0,s_1) | E | (0,12,s_3) | 12,13,23 |
| (0,0,s_1) | I | (0,23,24) | 23,35,25 |
| (0,0,12) | P | (0,34,s_3) | 34,45,35 |
| (0,0,12) | E | (0,14,s_3) | 14,45,15 |
| (0,0,12) | I | (0,23,13) | 23,23,0 |

Each chosen representative has exactly the required ordered type.
C07 now gives the common translation in every allowed case.
Undoing the normalizations proves the full if-and-only-if statement.

## 2. Three low-degree ports can be made compatible

### claim:opg434-c13-three-port-flexibility
Let H already map to B, and let p_0,p_1,p_2 be DISTINCT source vertices
of H-degree at most two. Keeping every other vertex label fixed, either
the three port labels can be made all distinct, or the ports have no
edges between them and their feasible lists are the same two-element
nonadjacent target pair. In that exceptional case any chosen pair of
port positions can be the duplicated positions, and no two port labels
are adjacent.

Here a feasible list is the intersection of the neighborhoods of its
fixed exterior neighbors, or all target labels if there are no such
neighbors. It has at least two entries by the existing map and C06.
A list of exactly two entries is a nonadjacent pair. A no-neighbor list
is all of B; it is not incorrectly assumed to be independent.

If the three ports induce one edge and an isolated port, keep that
edge's labels. The isolated port's list is not contained in these two
adjacent labels: a two-element list is nonadjacent and a larger list
has more than two elements. Choose a third label outside the edge.

If they induce a two-edge path, keep the center and one endpoint,
then relabel the other endpoint to avoid its counterpart using its
at-least-two-entry list. Adjacency already prevents equality with the
center. They cannot induce a triangle in a graph that maps to B.

If the ports induce no edges, their lists can be chosen independently.
Three sets of size at least two admit three distinct representatives
unless their union has size two. For a direct proof, choose different
entries u,v from the first two lists. If the third list has an entry
outside {u,v}, finish. Otherwise it is {u,v}; if the union is larger,
move whichever of the first two choices has an available outside entry
and use the freed entry for the third list.
Failure therefore means all three lists are exactly the same pair,
which is nonadjacent. This proves the asserted alternative.

### claim:opg434-c13-three-matching-gluing
Take two disjoint source graphs that each map to B, with three distinct
ports on each side, each of internal degree at most two. Adding any
matching between the two port triples yields another graph mapping to B.

Apply the preceding flexibility result to each piece. If both can obtain
distinct triples, Section 1 immediately gives an affine alignment.
If one side has the exceptional common two-element list, the other
side's three labels always have some pair that is nonadjacent, since
B has no triangle. Choose that pair as the duplicated positions in the
exceptional side. Its labels have no adjacent pair, so the reverse
equal-versus-adjacent obstruction is also absent. Section 1 applies again.
This includes the case when both sides have the exceptional lists.

Only the port labels are changed locally before a single whole-piece
affine automorphism is used for alignment. The argument does not claim
that every pair of preassigned port triples is already compatible.

## 3. Cyclic connectivity of a hypothetical minimum counterexample

### claim:opg434-c13-no-cyclic-three-cut
A vertex-minimum non-B-mappable triangle-free SUBCUBIC graph M, if one
exists, has no edge cut of size at most three with a cycle on each side.

C06 already supplies connectedness, no bridge, and no two-edge cut
whose two sides each contain at least two vertices. Thus only a
three-edge cut delta(U) separating two cyclic sides needs consideration.

Both induced sides are connected. Otherwise each of at least two
components on one side has a nonempty boundary of size at least two,
since M is connected and has no bridge. Their disjoint boundaries
would total at least four edges, impossible.

The three cut edges are a matching. If two were incident with a vertex
v in U, connectedness of the cyclic side forces v to have exactly one
internal neighbor; it is a leaf in M[U]. Removing v from U preserves
a cycle and changes the boundary to a two-edge cut, contrary to C06.
If all three cut edges met v, connectedness would force U={v}, which
has no cycle. The same reasoning applies on the other side.

Each side is a smaller triangle-free subcubic graph and hence maps to B
by the chosen minimality. Its three cut endpoints are distinct ports
of internal degree at most two. The matching-gluing lemma gives M a
B map, the required contradiction.

This is cyclic edge-connectivity at least four, not ordinary four-edge
connectivity: cubic vertices themselves have three-edge boundaries.
If this subcubic minimum happens to be cubic, every nontrivial
three-edge cut would be cyclic. Indeed, a connected acyclic side with
k cubic vertices has boundary 3k-2(k-1)=k+2; a boundary of size three
then forces k=1. Hence only trivial cubic three-edge cuts can remain.

C12 additionally supplies girth at least five for the same subcubic
minimum. The regularization from C12 is not asserted to preserve this
cyclic connectivity, nor is cubic minimality silently substituted for
subcubic minimality.

## 4. A precise four-terminal obstruction to overgeneralization

### claim:opg434-c13-four-terminal-limit
The pairwise equal-versus-adjacent test is insufficient for four terminals,
even when every three-terminal projection can be affinely aligned.

Take A=(0,0,0,0) and B'=(0,12,13,23). All entries of B' are pairwise
nonadjacent, so no forbidden pair occurs. Every triple has a common
neighbor by C07. But the full four-set has none:
the first three have the unique common neighbor s_1, which is not
adjacent to 23. Existence of a common neighbor is preserved by every
target automorphism, so no affine alignment of the full tuples works.

This is a fixed-tuple transport obstruction. It is not a graph-level
counterexample, and it does not preclude changing the four port labels.
It specifically prevents using Section 1 verbatim for larger cuts or
replacing a genuinely higher-arity boundary relation by all its triples.

## 5. Audit and continuation

The twelve short representative rows, the constant and duplicate cases,
the three-port list argument, and the matching nature of the cyclic
three-edge cut form a complete paper audit path. There is no hidden
finite-search result behind the tables.
Sources reused at the frozen base:
research/artifacts/candidates/opg434-a01-c06-separator-gluing.md
research/artifacts/candidates/opg434-a01-c07-star-obstructions.md
research/artifacts/candidates/opg434-a01-c12-square-reduction.md
They remain candidates and no novelty is asserted for this refinement.

best_verified_result=none; best_verified_candidate=none.
The target and root obligations remain open; no truth records changed.
The next unique obstruction is the oriented pentagon replacement.
An exact compatible three-terminal interface is now available, but the
four-terminal example and C09 prevent treating it as automatic five-pin
or global closure. The next step must construct a suitable whole-graph
map rather than merely accept every triple projection.
