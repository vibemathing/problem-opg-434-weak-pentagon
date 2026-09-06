# C09: pentagon boundary arity, exact certificates and controlled extension

candidate_id: candidate:opg434-a01-c09-pentagon-boundary
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 779270194fe878240f7cf3de1244a3cdaad858eb

Use the generators and notation ij=s_i+s_j of C06-C08 without changing the
frozen graph-homomorphism problem. All classifications and counts here have
paper proofs; no enumeration or kernel execution is reported.

## 1. Exact five-terminal relation

Let v_0,...,v_4 form an indexed 5-cycle. At positions in P subset {0,...,4},
an exterior neighbor has prescribed label x_i. A completion consists of labels
y_i for all five cycle vertices such that y_i is adjacent to y_{i+1} and,
for each i in P, y_i is adjacent to x_i. Indices are modulo five.
For an actual graph, all existing edges outside this cycle must already
satisfy the supplied map. Repeated exterior vertices impose equal labels;
they are not silently treated as distinct free variables.

### claim:opg434-c09-exact-relation
Every completion has a unique description
y_i=t+p_i, where p_0=0 and p_i=sum_{j=0}^{i-1} s_{pi(j)},
for a permutation pi of the five generators and t in B. Therefore its
existence is exactly
OR over pi in S_5 of [ intersection_{i in P} N(x_i+p_i) is nonempty ],
and its number is the sum of the cardinalities of these 120 intersections.
For P empty the intersection is B.

Proof. The five edge differences sum to zero. Their multiplicity parity vector
must be zero or all ones, by the unique generator relation. Since five is odd,
it is all ones, and each generator occurs exactly once. Conversely any
permutation closes after five edges and no proper interval of its edges sums
to zero. Thus it gives a simple target 5-cycle and the stated unique labels.
The exterior constraints become precisely t in N(x_i+p_i).

There are 16*120=1920 maps of the indexed cycle before exterior constraints.
With at least one pin, rotate that position to 0. Only five values of t need
be tested per permutation: at most 600 candidates, without an unbounded search.
A positive certificate is (pi,t). A negative certificate may specify, for
each of these 600 candidates, a pinned position whose adjacency test fails.
This is an exact certificate specification, not a claim that a program ran.

## 2. Two-terminal projections, including exact counts

Call a pin assignment pair-compatible when every restriction to at most two
pinned positions extends. Two adjacent positions require distinct exterior
labels; two nonadjacent positions impose no restriction on their labels.

### claim:opg434-c09-pair-counts

| cyclic separation of pins | equal labels | adjacent labels in B | distinct nonadjacent labels |
|---|---:|---:|---:|
| 1 | 0 | 312 | 144 |
| 2 | 240 | 144 | 204 |

Here the counts are of completed indexed 5-cycles for the given pins.
To verify them let A be the adjacency matrix of B, J the all-ones matrix
and I the identity. C06's common-neighbor counts give
A^2=3I-2A+2J and AJ=5J, hence A^3=7A-6I+6J.
For neighboring internal vertices, every ordered target edge is completed
in 4!=24 ways. The number of such ordered edges between N(x) and N(z) is
(A^3)_{xz}, giving the first row.
For internal separation two, every ordered distinct nonadjacent pair has
2!*3!=12 completions. The corresponding pair count is
[A(J-I-A)A]_{xz}=[3I-5A+17J]_{xz}, giving the second row.
A single pin has 5*120=600 completions. These formulas also check that
summing either two-pin row over all 16 values of the second pin gives 3000,
which is 600 times five choices for its exterior label.

## 3. Three-terminal projections are still insufficient

### claim:opg434-c09-three-pins-extend
For any at most three pinned positions, pair-compatibility is sufficient
for extension. In particular the only restrictions are unequal labels on
pinned consecutive positions.

For three pins there are two positional types, up to a cycle symmetry.

Type A: positions 0,1,2. Choose
y_1 in N(x_1) minus [N(x_0) union N(x_2)].
Because x_1 differs from x_0 and x_2, each excluded intersection has size
at most two. N(x_1) has five elements, so a choice remains.
Now N(y_1) intersect N(x_0) and N(y_1) intersect N(x_2) each have size at
least two. Choose different y_0 and y_2 in these sets. They are nonadjacent
as both neighbor y_1. The two edge generators on y_0-y_1-y_2 are different;
the other three generators in any order finish the pentagon.

Type B: positions 0,1,3. Only x_0!=x_1 is required. Choose
t=y_3 in N(x_3) minus {x_0,x_1}; at least three choices remain.
We need adjacent y_0,y_1 which respectively neighbor x_0,x_1 and are
distinct nonneighbors of t. Translate t to zero. The two prescribed labels
p,q are distinct and nonzero. The following representatives, plus swapping
p,q and permuting generator indices, cover all cases. The entries r,w
are disjoint index pairs, so they are adjacent in B and nonadjacent to zero.

| p | q | r (neighbor of p) | w (neighbor of q) |
|---|---|---|---|
| s_1 | s_2 | 13 | 24 |
| s_1 | 12 | 12 | 34 |
| s_1 | 23 | 12 | 45 |
| 12 | 13 | 35 | 24 |
| 12 | 34 | 34 | 15 |

Take y_0,y_1 to be these r,w translated back. Choose y_2 from
N(y_1) intersect N(t), and y_4 from N(y_0) intersect N(t).
Each set has size two. They are disjoint because y_0,y_1 are adjacent.
All five required cycle edges now hold, as do all three pinned edges.
This proves the two cases and the assertion.

### claim:opg434-c09-four-pin-obstruction
Pin precisely
x_0=0, x_1=34, x_2=s_5, x_4=12.
All four labels are distinct, so every two-terminal restriction passes.
Every three-terminal restriction extends by the preceding theorem.
Nevertheless the four pins cannot extend together.

Any y_0 must lie in S=N(0). It cannot be adjacent to x_1=34, since
y_0-y_1-x_1-y_0 would be a triangle. Similarly it cannot be adjacent to
x_4=12. These conditions eliminate respectively s_3,s_4 and s_1,s_2,
forcing y_0=s_5. But x_2=s_5 then makes y_0-y_1-y_2-y_0 a triangle.
This is impossible in B.

Thus four is the minimum number of pins for a pair-compatible nonextendable
pentagon boundary; indeed all its three-pin projections pass. A five-pin
version with ALL exterior labels distinct is
(0,34,s_5,s_1,12). The same four-pin certificate rejects it.
This rejects a three-terminal-only boundary compression without additional
correlation data; it does not reject the root.

A concrete source realization is a 5-cycle with pendant exterior vertices
at these four positions. The prescribed map on the four isolated exterior
vertices is genuine. The whole nine-vertex triangle-free subcubic graph is
feasible: map its cycle by the generator sequence s_1,...,s_5 and each pendant
vertex to the label of its cycle neighbor plus s_1. Hence the failure is
only for the frozen boundary, not graph-level nonexistence.

## 4. Complete characterization for independent exterior labels

### claim:opg434-c09-independent-boundary
Suppose the DISTINCT labels among x_0,...,x_4 are pairwise nonadjacent in B.
Then extension exists if and only if consecutive exterior labels differ.

There are two geometric cases.

Case A: all exterior labels lie in N(q) for some q. Translate q to zero,
so x_i=s_{a_i}. Every internal y_i belongs to {0} union the index pairs
containing a_i. It cannot equal zero: its next cycle neighbor would then
have to belong to S and also neighbor x_{i+1} in S, which is impossible.
Thus all y_i are two-element index sets containing a_i; consecutive ones
must be disjoint.

Every index occurs in at most two of the five y_i, as those positions are
nonadjacent in C5. There are ten incidences in total, so each of the five
indices occurs exactly twice. Its two positions form a chord of C5.
Two indices cannot occupy the same chord, as that would repeat an internal
target label, impossible for a map of C5. Consequently the five indices
are assigned bijectively to the five chords of the indexed pentagon.
Conversely such a chord assignment gives disjoint pairs at consecutive
positions and hence a valid completion. Pin a_i demands that the chord
assigned index a_i be incident with position i.

If consecutive a_i differ, no index occurs more than twice. The only
multiplicity patterns and their numbers of valid chord assignments are:
- 1+1+1+1+1: two. They are the two perfect matchings of the cyclic
  vertex-edge incidence graph of the chord pentagon.
- 2+1+1+1: four. The repeated index fixes one chord. Removing it leaves
  a four-edge path; its three internal vertices have the three singleton
  indices. Assigning each to a different incident edge has exactly four
  choices, after which the unused index occupies the remaining edge.
  To count these, left/right choices cannot contain a right-then-left
  collision, so they are 000,001,011,111 along the path.
- 2+2+1: four. The two repeated indices fix disjoint chords. The singleton
  position has two available incident chords; the other two indices can
  be assigned in either order.

This proves existence and exact counts in Case A.

Case B: there is no such common neighbor q. Translate one exterior label
to zero. Other labels are pair sums, and pairwise nonadjacency says their
index pairs intersect. A pairwise intersecting family of two-element sets
either has a common index or is exactly a triangle of three pairs:
after 12 and 13, the only pair missing index 1 that meets both is 23,
and no fourth different pair can meet all three. The common-index case
would put all labels in one N(s_i). Therefore Case B consists exactly of
the four labels {0,12,13,23}.

With consecutive labels unequal one label repeats at two nonadjacent positions.
By translation, cycle symmetry and an index permutation, the boundary is
(0,12,0,13,23).
It has the two completions
(s_4,45,s_5,25,14) and (s_5,45,s_4,24,15).
To check completeness, y_0=s_i,y_2=s_j are distinct generators.
Their common neighbor y_1 must be ij rather than zero, because it neighbors
12. Hence {i,j} is a subset of {3,4,5}. On the other side of the pentagon
write y_3=s_j+s_k and y_4=s_i+s_l, where k,l are distinct remaining indices.
Adjacency to 13 forces j,k to avoid 1,3; adjacency to 23 forces i,l to
avoid 2,3. Thus {i,j}={4,5}, k=2, l=1, yielding exactly the two displayed
completions. Necessity of unequal consecutive pins is already Section 2.

The independent-boundary theorem is a conditional reducibility rule for a
5-cycle with a fixed exterior map. It does not assert that arbitrary exterior
maps can always be moved into this favorable class.

## 5. Exact controlled ear extension

### claim:opg434-c09-pentagon-ear
Let an already mapped graph H contain a simple path P of length r, 1<=r<=3.
Add a path Q of length 5-r with the same endpoints and fresh internal vertices,
and no other edges incident to those new vertices.
For the given map of H, extension exists if and only if the r generator
colors on P are distinct. When they are distinct there are exactly (5-r)!
extensions, obtained by ordering the remaining generators along Q.
The sum relation guarantees the prescribed endpoint is reached; necessity
comes from the new pentagon's five different generators.

In particular every map of one pentagon extends over a second pentagon
sharing a connected path of length 1,2 or 3 and otherwise disjoint, provided
there are no additional constraints on the new vertices.
This is an actual constructive class, not a cycle-basis hitting shortcut.
If H is triangle-free and P lies in a pentagon, adding Q creates no triangle:
only a length-two Q could do so, but its endpoints already have a
length-two route in the old pentagon and cannot be adjacent in H.
To stay subcubic, its two endpoints must have degree at most two before
the addition. No claim is made that all cubic graphs have this decomposition.

## 6. Audit and next obligation

The exact relation is a conjunction of adjacency atoms with existential
internal labels. Its three-terminal projections do not determine it.
The four-pin witness is a negative boundary certificate only.
The count table, independent-boundary cases and ear counts were derived on
paper, not measured by a program. Old candidates remain immutable.

Sources and comparison scope:
research/artifacts/source-notes/opg434-a01-c09-extension-comparison.md.
Required future checks remain kernel_check, axiom_escape_audit and
statement_faithfulness. No EvidenceLink or root closure is supplied.
best_verified_result=none; best_verified_candidate=none.

The next unique obstacle is global reachability of a feasible boundary state:
in a putative counterexample, every map of the exterior avoids this relation.
Next investigate a bipartization-based simultaneous two-switch construction,
with an explicit structural hypothesis rather than an unsupported universal
repair claim.
