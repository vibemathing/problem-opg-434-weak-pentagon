# R09: joint list-boundary states, verified separators and a cubic-preserving cap reduction

candidate_id: candidate:opg434-a01-list-separators-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
base_revision: ea7cad35e16393f02a6b5a265e929bca389625a1

## 1. Fixed inputs and scope

All seven root-structure attachments were read completely. Their filenames,
lengths, SHA-256 and field dispositions are in inputs-audit.json. The supplied
35-file ZIP has 34 non-self manifest entries; all match. This turn does NOT
repeat R11/R12 enumeration, C10, h=1 or older archive reconstruction.

The old execution-summary records seven exit-zero CPython 3.13.5 runs. Its
R11 interface has 3840 complete normalized witnesses, first_failure=null;
R12 separately has 57600, first_failure=null. Its generator uses bitset search,
while its consumer uses coordinate subsets and separately transcribed edges,
with 24 negative and four positive controls. Those are historical receipts,
not fresh runs here. The different already-remote variant has 22+2 controls.

The old graph22 input includes the full edge set, names, two target-label
representations, girth/odd-cycle/small-cut witnesses and a quotient assignment.
Here the frozen even-five-bit model is used, not the four-bit labels mixed
with another adjacency rule. The old failed-route proposal rejects only:
structural cubic, nonbipartite, girth>=5, three-vertex-connectivity and trivial
three-edge cuts imply the existence of a pentagon. It does NOT reject an
implication with an additional minimum-non-B-mappability premise. Graph22 is
explicitly B-mappable. The old obligation matrix leaves universal quotient
satisfiability and trusted closure open. Its old main/PR checkpoint is stale:
fresh reads confirm PR29 merged to ea7cad35e16393f02a6b5a265e929bca389625a1.
No immutable merged packet is edited; Issue3 is reused for the next cycle.

C06 and C13 were freshly read at this base before proving separators. Their
unrestricted two/three-port results are prior candidates, not new discoveries
or trusted premises. This turn gives complete finite transport certificates,
clarifies list scope, and supplies the standalone arguments below.

## 2. Definitions: retain joint states and all internal choices

B has the sixteen even vectors of F2^5. Its edge differences are
S={t_i=J+e_i:0<=i<5}={30,29,27,23,15}; p_ij=e_i+e_j. The only nonempty subset
of S summing to zero is S itself: the coordinate equations force all five
coefficients equal. In particular there is no closed three-step walk.
Every vertex has five neighbors. Equal vertices have five common neighbors,
adjacent vertices have none, and distinct nonadjacent vertices x,x+p_ij have
exactly x+t_i,x+t_j as their common neighbors. This follows by comparing
sums of two generators using the unique relation.

For a finite graph H, lists L(v) subset V(B), and ordered ports p_1,...,p_k,
define Sigma(H,L;p) to be ALL tuples (f(p_1),...,f(p_k)) attained by a
list-homomorphism f of the WHOLE piece. Empty lists are permitted and mean
impossibility. Repeated physical ports impose equality at their occurrences.
A table row must be jointly realizable. Unary projections are insufficient.

For two disjoint pieces joined by edges p_i q_i, exact feasibility is
  exists a in Sigma_A, b in Sigma_D: for all i, a_i ~ b_i.
Necessity is restriction of one global map; sufficiency is union of the two
witness maps, since their only new constraints are exactly the crossing edges.
Additional retained ports can be included and projected after this join.
This proves relational composition without assuming independently selectable
port labels. Existential elimination decreases the number of uneliminated
vertices; it can introduce a higher-arity factor and is NOT automatically a
smaller source graph in the root's class.

A removed vertex with pins a_i has the exact internal list
  L(v) intersect (intersection_i N(a_i)).
A removed adjacent pair u,v with remaining pins (a,b) and (c,d) has ALL pairs
  (x,y) in [L(u) intersect N(a) intersect N(b)]
           x [L(v) intersect N(c) intersect N(d)] with x~y.
Missing neighbors omit factors. These formulas prove necessity and attainment
for every listed choice, not just existence of one preferred target label.

Fresh tables include all normalized 256 three-pin vertex cases (91 nonempty)
and all 4096 four-pin edge-patch cases (1455 nonempty). The consumer checks
EVERY possible internal label/pair directly from the actual star/five-edge
patch, so the table preserves all internal choices. Extra lists filter these
sets; they are not discarded or relaxed.

## 3. Exact affine transport across two or three matching edges

For k=2 or 3 and arbitrary ordered target tuples a,b (repetitions allowed),
there exists a target automorphism alpha(x)=pi(x)+z with a_i~alpha(b_i) for
all i iff no position pair is equal in one tuple and adjacent in the other.
Here pi permutes the five coordinates, and z is an even vector.

The obstruction is necessary because two adjacent labels cannot share the
same neighbor. For sufficiency the complete finite certificate is exhaustive:
normalize a_0=b_0=0 by separate translations; enumerate all 16^(2k-2) tails;
for every positive row store an actual coordinate permutation and translation.
For a negative row store a position pair with the forbidden equality/edge.
Undo normalization by alpha'(x)=a_0+alpha(x+b_0). Coordinate permutations and
translations preserve adjacency by the definition of B. Thus normalized
coverage plus every-row witness proves the finite implication on all tuples.

Actual checked rows:
- k=2: 256 total, 246 positive, 10 forbidden.
- k=3: 65536 total, 58156 positive, 7380 forbidden.
All 120 coordinate permutations were separately checked as automorphisms.
Tables and row-order encoding are frozen in the bundle. No random sampling
or unreported solver is involved. Consumer code uses coordinate sets and
checks each witness; it does not import the bitset producer or its search.
This is algorithmic separation, not a separate trusted verification domain.

For unrestricted lists, Sigma is closed under all target automorphisms, so
affine alignment legitimately supplies another whole-piece map. With fixed
lists it generally does NOT. One must use the actual two signatures, or
restrict to automorphisms that preserve the piece's lists. The following
reductions state which of these situations applies.

## 4. Strict graph reductions and minimality domains

### 4.1 Arbitrary-list dominated-vertex deletion

Let u!=v be nonadjacent, N_H(v) subset N_H(u), and L(u) subset L(v).
Delete v. Every list-map of H-v extends by f(v)=f(u): all neighbors of v
are also neighbors of u, and f(u) belongs to L(v). Conversely restriction
always gives a list-map of H-v. Therefore ALL feasible assignments to the
remaining vertices are preserved, and the order decreases by exactly one.
Deletion preserves simplicity, triangle-freeness and maximum degree three.
It need not preserve cubic regularity. The adjacency and list inclusions
are essential hypotheses, not implicit assumptions about arbitrary twins.

A three-vertex path u-w-v with L(u)={0}, L(v)={3}, L(w)={30} has the complete
map (0,30,3). Identifying u,v and intersecting their incomparable lists makes
the merged list empty. This is a complete minimal twin-path obstruction to
that stronger rule, not a root counterexample. The true dominated-list
control preserves every retained map and was checked by factor elimination.

### 4.2 Bridge and two-edge-cut reductions, unrestricted target lists

Work first with a vertex-minimum non-B-mappable graph M in the entire finite
simple triangle-free SUBCUBIC class, if one exists. Cubic root failure implies
this class contains a counterexample, but its vertex-minimum need not be cubic.
Every proper induced piece of M is smaller and B-mappable by this minimality.

Disconnected pieces join freely. For a bridge uv separating A,D, normalize
a map of A and translate a map of D so that its v image is f_A(u)+t_0.
All edges on both sides and the bridge are valid. At a cut vertex, translate
each smaller piece to agree at that vertex. These exclude bridges and cut
vertices from M. Isolated/degree-one vertices extend directly; M has minimum
degree at least two.

For a given B-map and a vertex of degree at most two, keeping all other
labels fixed leaves at least two feasible labels: respectively 16,5,5 or2
according as it has zero neighbors, one, two equally labeled, or two
unequally labeled neighbors. The latter two labels must have a common
neighbor, hence cannot be adjacent. In particular two distinct low-degree
ports can be made to have different labels, by changing one if necessary.

If a two-edge cut has sides of order at least two, its endpoints are distinct
on each side; otherwise the repeated endpoint is a cut vertex. The endpoints
have internal degree at most two. Each side can therefore attain a distinct
pair. The affine table shows any two distinct pairs are compatible. Each
side is strictly smaller, so the join excludes such a cut in M. Only a cut
isolating a degree-two vertex can remain in this subcubic argument.

### 4.3 Three low-degree ports and cyclic three-edge cuts

For three distinct ports of internal degree at most two in a positive piece,
keep all nonports fixed. If the ports contain an edge plus an isolated vertex,
keep the edge and choose the third label outside its two adjacent images:
a feasible two-element list is nonadjacent, and any larger list has enough
choices. If the ports form a two-edge path, keep the center and one endpoint,
and choose the other endpoint different from its counterpart. The remaining
case is an edgeless port set, with independently selectable lists each of
size at least two. Three distinct representatives exist unless the union
has size two. To prove this directly, choose distinct entries in two lists;
if the third has no unused entry it is exactly those two, and an outside
entry from either of the first lists frees one. In the exceptional case
all three lists are one common two-element nonadjacent pair, and any selected
pair of positions can be the duplicated positions.

For two such pieces, if both obtain distinct triples, affine transport
always aligns them. If one is exceptional, the other triple has a pair of
nonadjacent (possibly equal) entries because B has no triangle. Duplicate
those positions on the exceptional side. Its entries have no adjacent pair,
so neither direction of the equal-versus-adjacent obstruction occurs.
The exact three-terminal table now aligns the two actual piece maps.

A three-edge cut with a cycle on each side in M has connected induced sides:
two components on a side each have boundary at least two after bridges are
excluded, which would exceed three. Its crossing edges form a matching.
If two meet v on one side, v is a leaf of that connected cyclic side;
removing v leaves a cyclic side and a two-edge cut with both sides of order
at least two, already impossible. Three meeting v would make that side a
singleton. Thus each side has three distinct ports of internal degree<=2.
Both smaller pieces are positive and the preceding gluing contradicts M.
If M is cubic, an acyclic connected side with n vertices has boundary n+2,
so a three-edge cut with an acyclic side isolates a single vertex.

Each decomposition strictly reduces side order; the monotone quantity is
vertex count. These arguments do not prove an unavoidable cut or positivity
of an irreducible terminal graph. For a minimum taken ONLY over cubic graphs,
its noncubic induced sides are not automatically positive. The next cap
reduction instead stays in the cubic class directly.

## 5. A strictly cubic-preserving K2,3 cap reduction

Let P be induced K2,3 with degree-three vertices r,s and degree-two ports
p_1,p_2,p_3, each having one exterior neighbor u_i. All lists in P are full.
Its exterior relation is ALL of B^3. Indeed, for any a_1,a_2,a_3, choose
c outside N(a_1) union N(a_2) union N(a_3). The union has size at most15<16.
Thus c is equal or nonadjacent to each a_i. Choose y_i in N(c) intersect
N(a_i), which is nonempty by the common-neighbor facts. Map r=s=c and
p_i=y_i. All six internal and three crossing edges are respected.
This is a uniform constructive proof; 256 normalized tuples with complete
five-label maps were separately checked (4096 actual exterior triples).

Assume G is simple triangle-free CUBIC, the P occurrence has only those
three exits, and u_1,u_2,u_3 are pairwise DISTINCT and pairwise NONADJACENT.
Delete the five vertices of P and add a single fresh vertex z with neighbors
u_1,u_2,u_3. The three old endpoints each lose and gain one edge; z has
degree three. Freshness and distinctness preserve simplicity. A new triangle
would require an edge between two u_i, excluded. Consequently G' is simple,
triangle-free and cubic, and |V(G')|=|V(G)|-4. Every G' map supplies an
exterior tuple, which extends over P by the universal construction above.
The exterior is preserved. In a vertex-minimum non-B-mappable CUBIC graph,
this occurrence is therefore impossible, by a smaller graph in exactly the
same cubic class. There is no proof that every such minimum has the cap.
Graph22 has girth six and hence no K2,3, so structural cap inevitability
would also fail on a positive graph.

This is one-way lifting, NOT equality of boundary relations. For example
(0,30,0) extends over P but cannot be the neighbor labels of a target vertex.
The replacement star imposes a stronger boundary condition. For unrestricted
subcubic minimality, one could simply delete the universally extendible cap;
that observation does not justify an arbitrary-list or cubic-only deletion.

Explicit assumption controls are complete positive source graphs:
- A 12-vertex cubic triangle-free graph with the cap, three distinct outside
  endpoints, and an edge between two of them creates triangle (z,5,6) after
  replacement. Edges and full B-map are in cap-condition-witnesses.json.
  Within this setup it is smallest: the exterior order is odd; order1 cannot
  give three distinct ends; order3 requires a triangle; an order5 exterior
  has six edges and degrees (3,3,2,2,2). It must be bipartite (an odd cycle
  would be C5 and its sixth edge creates a triangle), so it is K2,3 and its
  degree-two port vertices are nonadjacent. Thus at least seven exterior
  vertices are needed, attained by the given 12-vertex graph.
- K3,3 on six vertices has the three cap ports sharing their third neighbor.
  Replacing the cap gives three parallel edges, or degree one if deduplicated.
  This is smallest among simple triangle-free cubic sources by the elementary
  order/degree bound. It does not satisfy the distinctness hypothesis.
The positive 10-to-6 vertex control is two copies of K2,3 with matched ports;
replacing one cap yields K3,3. Both complete maps and all edges were checked.

## 6. Minimal listed-boundary failures and exact fixed-graph signatures

The bundle stores complete input lists, edges, boundary maps and exact
factor-elimination traces, not only a SAT label.
- A two-edge path has endpoint relation 176 of256 pairs, although both unary
  endpoint projections are all16 labels. The first spurious Cartesian-product
  pair is (0,15); the80 spurious pairs are exactly target edges.
- On P4=0-1-2-3 with L(0)=L(3)={0} and other lists full, cut the matching
  edges01 and23. Both pieces are positive, but the full listed source has
  zero states: it would give a closed three-step target walk. Four source
  vertices are minimal for two crossing edges with distinct endpoints on
  both sides. This does not contradict unrestricted two-piece gluing.
- A six-vertex fixture has crossing matching03,14,25, a path3-4-5 on one
  side, and isolated ports0,1,2 fixed to0 on the other. Both pieces are
  positive but their join is not: adjacent path labels would both lie in
  N(0). Six vertices are the minimum possible for a three-edge matching
  with distinct endpoints. The side of three isolated pins is not a cyclic
  connected piece; no claim about cyclic-cut reduction is negated.

Graph22 itself was rebuilt from a source all-pairs predicate in the new
consumer, checking all33 mapped edges,254 vertex deletions of sizes1/2 and
6017 edge deletions of sizes1..3, with exactly22 trivial cuts. The new full
source one-hot/support CNF has352 variables and3719 clauses. The consumer
reconstructs every expected clause and checks equality with actual DIMACS,
then checks the entire model. This is a positive fixed-instance check.

There are also complete freshly checked signatures for that SAME graph:
Sigma(G22-0;1,10,11)=B^3, and Sigma(G22-edge01;0,1)=B^2.
The first has256 normalized witness rows, the second16; all7680/512 present
edge instances are checked separately. Target translations recover all4096/
256 actual tuples. The source predicates and ordered ports are reconstructed
by the consumer, with no search-module import. All positive tuples have full
maps, so no solver completeness assumption is used for these conclusions.
In particular G22 is not a minimum non-B counterexample; its full signature
contains many choices compatible with restoring the deleted vertex or edge.

## 7. Execution, mutations, known unsuccessful probe and reproducibility

Current finite results are from SEVEN exit-zero candidate processes: table
producer, separate table/factor consumer, mutations, cap witness/lift control,
cap-assumption controls, improved fixed-graph projection search, and separate
projection consumer. CPython3.13.5, standard library, seed0, one CPU affinity,
CPU35/36 seconds, outer wall40 seconds, address space512MiB, regular-file
limit1MiB. Per-stream and aggregate5MiB budgets are checked after exit.
They are not falsely described as an enforced aggregate filesystem quota.

A preliminary eighth mathematical process stopped with exit1 after exceeding
its 200000-node search cap. It is recorded UNKNOWN, not UNSAT, not a family
counterexample, and not a passed control. Its exact code and process receipt
are preserved; stderr is stored only after host-path redaction, with the
original-byte digest retained and the transformation explicit. One wrapper
invocation omitted --receipt and was rejected before any child computation;
the corrected invocation is the actual successful projection-v2 run.
The improved search adds arc consistency and justified target-permutation
orbit normalization: 14/3 representative searches,234/56 nodes, followed by
checking every expanded tuple independently of those optimizations.

Twenty negative and four positive mutations pass. They include corrupted
permutation/shift witnesses, missing or fabricated states, lost feasible
internal labels, wrong ports/lists/maps, damaged CNF and source edges,
missing total witness, unsafe unary compression, unsafe twin-list intersection,
and applying unrestricted cut gluing to fixed lists. Positive controls retain
valid edge orientations, simultaneous target/list translation, dominated-list
deletion and a cubic matched-cap map. All exact tests and witnesses are stored.

The decoder checks each saved input/code/output length and SHA-256 with a
bounded expansion. Executable request code runs the consumer and mutations
on the frozen results; it is not a trusted verifier. No computation proves
universal root satisfiability. No attempt/Evidence/Result ledger is changed.

## 8. Root frontier and explicit dependency boundary

Dependencies: target definition -> common-neighbor and affine facts;
exact signatures -> relational joins and safe list elimination;
finite affine witnesses + low-degree flexibility -> unrestricted cut gluing;
list inclusions -> dominated-vertex fold;
16>3*5 and common-neighbor facts -> universal cap -> cubic n-4 reduction.
The frozen prior R11/R12 successes are read, not used to infer any new table.
C06/C13 provide attribution; their key graph arguments are included above.
Extremal minimality is over explicitly stated nonempty finite graph classes.
No probability or asymptotic sampling is used. Reduction vertex counts are
strictly decreasing; this is termination, not positivity of every remainder.

First open structural obligation: use actual non-B-mappability/minimality to
handle graphs with no bridge, nontrivial two/cyclic-three cut or applicable
list-dominated/cubic cap reduction. Their higher-arity realizable signatures
must be joined simultaneously; compatibility of all lower projections is
not sufficient. Graph22 disproves only structural-only unavoidability, not
this conditional. Trusted faithfulness, kernel/axiom audit and root closure
remain open. best_verified_result=none; root_closed=false. This checkpoint
has no implication of background execution after the response.
