# C12: square reducibility and a girth-five root reduction

candidate_id: candidate:opg434-a01-c12-square-reduction
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 1d1ebd196e965bd3f0bc2472c04e076ec05cdd9b

This is a paper induction step inside the actual triangle-free subcubic
domain. It is not an assertion that every prescribed exterior map extends.
Notation s_i and ij is inherited from C06; neighborhoods in B are open.
C06-C07 supply pair transitivity, the common-neighbor counts 5/0/2, and:
any at most three pairwise nonadjacent target labels have a common neighbor;
a three-element such set has exactly one common neighbor.
No graph enumeration or mathematical verifier was executed.

## 1. Exact four-pin extension relation

Let x_0,x_1,x_2,x_3 be arbitrary target labels, with repetitions permitted.
Say R4(x) holds when there are labels y_0,...,y_3 such that
y_i is adjacent to x_i and to y_{i+1}, with indices modulo four.

### claim:opg434-c12-square-relation
R4 fails exactly in either of these situations:
(A) some consecutive pins are equal;
(B) all four pins are distinct and their induced target graph is 2K2,
    with its two edges being the DIAGONALS x_0x_2 and x_1x_3.

Proof. Equality of consecutive pins would give a closed three-step walk
x_i-y_i-y_{i+1}-x_i, impossible in B.

Assume consecutive pins differ. Define
D=N(x_0) minus (N(x_1) union N(x_3) union {x_2}).
Then R4 holds exactly when D is nonempty.
For necessity, y_0 lies in N(x_0), is nonadjacent to x_1 and x_3 because
of their common neighbors y_1,y_3, and is not x_2, as otherwise
y_0-y_1-y_2-x_2 would be a closed three-step walk.

For sufficiency take t in D and put y_0=t. Choose
y_1 in (N(t) intersect N(x_1)) minus N(x_2).
If t=x_1 this first set has five elements and at most two are excluded.
Otherwise t,x_1 are distinct nonadjacent labels, so the first set has
two elements; x_2 is distinct from both and their triple intersection
has at most one element. Thus y_1 exists. The same argument chooses
y_3 in (N(t) intersect N(x_3)) minus N(x_2).
Now y_1,y_3 share t and hence are nonadjacent; each is nonadjacent to x_2.
C07 supplies y_2 adjacent to x_2,y_1,y_3. These four labels are the extension.

To classify emptiness of D, translate x_0 to zero. Each intersection
N(0) intersect N(x_1) or N(x_3) has at most two elements. Covering the
five elements of N(0) using those sets and the singleton {x_2} therefore
requires two disjoint two-element intersections and the missing fifth
neighbor x_2. Write x_1=ij, x_3=kl. Their index pairs must be disjoint;
if m is the remaining index, x_2=s_m. The four pins are precisely an
induced diagonal 2K2. Conversely, for this configuration the five neighbors
are all excluded. Up to translation and generator permutation its normal
form is (0,12,s_5,34). This proves both directions, including repeated pins.

## 2. A low-degree edge has a cycle of feasible ordered images

### claim:opg434-c12-flexible-edge-six-cycle
Let H have a B-homomorphism, and let pq be an edge with both endpoints
of H-degree at most two. Fix the labels on every other vertex.
The feasible ordered images of p,q contain all alternately oriented edges
of a simple six-cycle in B.

If the endpoints have exterior neighbors besides each other, write their
labels as alpha,beta. They cannot be equal: the existing labels on the
three-step walk alpha-p-q-beta would otherwise give a closed odd walk
of length three in B. Normalize the ordered pair by a target automorphism.
The following six-cycles have their alternating p-side in N(alpha)
and q-side in N(beta):

| alpha,beta | six-cycle, starting at a p-side vertex |
|---|---|
| 0,s_1 | s_1,12,s_2,0,s_3,13,s_1 |
| 0,12 | s_3,34,s_4,45,s_5,35,s_3 |

Each row has six distinct vertices, and every consecutive difference is
a generator. The inverse normalization returns feasible labels respecting
the actual fixed exterior neighbors. The six-cycle need not be induced.
When a neighbor is missing, impose an arbitrary additional fictitious
exterior label distinct from the other one; this only restricts choices,
and the displayed cycle still consists of feasible actual assignments.

In particular, p,q can be relabeled avoiding any at most two forbidden
target vertices: each forbidden vertex meets at most two edges of the
six-cycle, so at least one cycle edge survives. Orient it according to
the alternating p-side and q-side. No other source label is changed.

## 3. A target cycle always has an edge compatible with a fixed edge

Two target edges are called compatible here when they are vertex-disjoint
and their four endpoints do not induce 2K2; at least one cross edge exists.

### claim:opg434-c12-cycle-edge-compatibility
For every target edge e and every simple target cycle C, C has an edge
compatible with e.

Write e=rs. If a vertex x of C outside {r,s} is adjacent to an endpoint,
it is adjacent to at most one of them by triangle-freeness. At least one
of its two cycle neighbors y is therefore outside {r,s}. Edge xy is the
required edge. If C contains r or s, it has a cycle neighbor outside this
pair, reducing to the same argument.

If no compatible edge existed, C would consequently lie entirely among
the common nonneighbors of r,s, excluding the endpoints. Normalize
r=0,s=s_5. This remaining induced graph has vertices ij with
i,j in {1,2,3,4}; adjacency pairs each set with its complement. It is 3K2
and contains no cycle, a contradiction.

Combining Sections 2-3, a low-degree source edge can be relabeled to a
target edge compatible with any fixed target edge, while all other
source labels remain fixed. The fixed target edge can come from a
different source edge; no independence of their exterior neighborhoods
is assumed.

## 4. The full square reduction

### claim:opg434-c12-square-reducibility
Let G be finite, simple, triangle-free and subcubic. Suppose every
triangle-free subcubic graph with fewer vertices than G maps to B.
If G contains a four-cycle, then G maps to B.

Let its vertices be v_0,v_1,v_2,v_3 in cyclic order. There are no chords.
Each v_i has at most one outside neighbor x_i; it may be absent.
Opposite positions may have the same outside vertex, but the two parity
groups P={x_0,x_2 present} and Q={x_1,x_3 present} are disjoint.
An outside vertex in both groups would create a triangle.

Case 1: neither P nor Q consists of two distinct adjacent vertices.
Identify v_0,v_2 to U and v_1,v_3 to V, retain all outside edges, and
simplify parallel edges. The four cycle edges become the one edge UV.
The resulting graph G' has |V(G)|-2 vertices and maximum degree at most
three. It is simple after simplification, with no loops.
A new triangle U-V-z would put z in both P and Q. A new triangle U-p-q
would require two distinct adjacent members of P; the corresponding
argument holds for V and Q. These possibilities were excluded, and any
other triangle would already be in G. Hence G' is triangle-free.
By the induction premise it maps to B; compose with the quotient map
to obtain a map of G. Repeated or absent outside neighbors cause no problem.

Case 2: after rotating the square if necessary, P={p=x_0,q=x_2}
consists of distinct adjacent vertices. Put H=G-V(C).
Both p and q have H-degree at most two and are disjoint from Q.

2a. If Q has at most one distinct vertex w, take any B-map of H.
By Section 2 relabel pq avoiding f(w), if w exists.
Fill the missing Q pins with f(w). If Q is empty, fill both pins with
any label different from the two pq images.
The four pins now have unequal consecutive entries and equal Q-diagonal
entries. Neither forbidden configuration of Section 1 occurs, so extend
over C. A fictitious pin merely imposes an optional extra requirement.

2b. Suppose Q={w,z} has two distinct vertices, wz is absent in H, and
w,z have a common neighbor in H. Take any B-map of H. Their images are
nonadjacent (possibly equal), so the Q diagonal is not a target edge.
By Section 2 relabel pq avoiding both images. Consecutive pins are now
unequal and the diagonals cannot form 2K2. Section 1 extends over C.
Any edges from pq to fixed exterior vertices remain satisfied.

2c. In all other cases with Q={w,z} distinct, use H'=H if wz already
exists, and H'=H+wz if it does not. In the latter situation w,z have
no common H-neighbor, so adding wz creates no triangle.
Each lost one square neighbor, so their new degrees are at most three.
Thus H' is a smaller triangle-free subcubic graph and has a B-map.
The labels f(w),f(z) form a fixed target edge. The source edge pq still
has endpoints of degree at most two, because p,q are disjoint from w,z.
Apply Sections 2-3 to relabel pq to a compatible target edge.
The four pin labels are now distinct and their diagonals are not induced
2K2. Section 1 extends over C. If wz was artificial, discard it.

This exhausts missing pins, repetitions, existing edges, absent edges
with a common neighbor, and absent edges with none. Every invoked smaller
graph has been checked for the actual domain and has strictly fewer
vertices. No step requires a planar drawing or a prescribed initial map.

## 5. Conditional minimality and girth-preserving cubic completion

### claim:opg434-c12-no-square-minimum
A vertex-minimum non-B-mappable triangle-free SUBCUBIC graph, if one exists,
has girth at least five.

Otherwise the induction premise holds by its chosen minimality, and
Section 4 supplies its missing map. The minimum is not being taken only
among cubic graphs.

C06 additionally gives minimum degree two and no adjacent degree-two
vertices for this same minimum M. Its degree-two set D is therefore
independent. If D is nonempty, take two copies of M and join corresponding
vertices in D. This is C05's two-layer completion specialized to this
separated deficiency pattern, and it is cubic. A fixed layer is M.

### claim:opg434-c12-separated-completion
The specialized completion has girth at least five.

Triangle-freeness follows either from C05's odd-girth projection or
directly from the matching between layers. A four-cycle with no vertical
edges would be an old square. A four-cycle with two vertical edges would
require an old edge between two members of D, impossible because D is
independent. Four vertical edges cannot form a cycle because those edges
are a matching. These are all possibilities, since a closed walk switches
layers an even number of times.

This does NOT upgrade C05 to an arbitrary girth-preserving completion.
The previous C17 example has adjacent degree-two vertices and is excluded
by the new hypothesis.

### claim:opg434-c12-girth-five-domain
The frozen root is equivalent to its restriction to finite simple cubic
graphs of ordinary girth at least five.

The forward direction is inclusion of domains. For the reverse, assume
all cubic graphs of girth at least five map to B, and suppose the root
failed. Select a vertex-minimum triangle-free subcubic non-B-mappable M;
such a graph exists because the root counterexample itself is subcubic.
C06 and Section 4 apply. If M is cubic it directly contradicts the
assumption. Otherwise the specialized completion above is a cubic graph
of girth at least five, hence maps to B; restriction to a fixed layer
then maps M, again a contradiction.

This is an equivalence of universal statements, not a proof of either.
It makes no claim that a vertex-minimum cubic counterexample and the
chosen subcubic minimum have the same order or regularity.

## 6. Adversarial checks, reproducibility and next obstruction

The tuple (0,12,s_5,34) is an exact nonextendable fixed square boundary.
It explicitly blocks a false assertion that all exterior maps extend.
Case 2 instead constructs a suitable map of a smaller graph.

Audit the singleton exclusion {x_2} in Section 1; omitting it loses the
diagonal 2K2 obstruction. Audit the ordered alternating sides of the two
six-cycles in Section 2; do not interchange endpoint labels arbitrarily.
In Section 4, test all missing/repeated pins and ensure the virtual edge
does not create a triangle or a degree-four vertex.
In Section 5, the independence of D is essential.

Internal claim dependencies:
C06+C07 -> square-relation and flexible-edge-six-cycle;
C06 -> cycle-edge-compatibility;
these three -> square-reducibility -> no-square-minimum;
C06+C05+no-square-minimum -> separated-completion -> girth-five-domain.

These are paper candidate dependencies, not newly admitted DAG nodes.
The source note is
research/artifacts/source-notes/opg434-a01-c12-reduction-comparison.md.
No finite instance sweep, SAT result, Lean command or kernel receipt is
claimed. best_verified_result=none; best_verified_candidate=none.
Both admitted obligations remain open.

Next unique obstacle: obtain a valid induction step for a pentagon or a
more global replacement. C09's full five-pin relation cannot be replaced
by three-terminal projections. The square result does not automatically
generalize to five-cycles, and a frozen-boundary failure is not a graph
counterexample. A three-edge matching-cut compatibility refinement is
also available as a separate conditional reduction, not as root closure.
