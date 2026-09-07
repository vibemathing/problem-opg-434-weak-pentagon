# C16: exact source-belt frontier around a degree-two pentagon vertex

candidate_id: candidate:opg434-a01-c16-belt-frontier
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: ede8f67c666b8aedfe6fa5f5414161863c283ff7

This is a conditional minimum-counterexample reduction using C06/C07/C13/C14
as candidate dependencies. No mathematical program or verifier ran. It neither
asserts the existence of the minimum below nor changes the root or admitted DAG.

## 1. Precise setup and conclusion

Suppose M is a vertex-minimum non-B-mappable finite simple triangle-free
SUBCUBIC graph. Use the explicit target B of C06, with labels 0,s_i,ij
and generator differences S. The minimum is over the entire subcubic
class, not merely over cubic graphs.

The candidate reductions already give:
(P1) M is connected, has no bridge, has minimum degree two, has no
adjacent degree-two vertices, and no two-edge cut with both sides of
size at least two (C06).
(P2) M has girth at least five (C12).
(P3) No cut of size at most three has a cycle on both sides; three
distinct ports of internal degree at most two in each of two positive
pieces can be joined by any matching (C13).
(P4) A pentagon with only v_1 of degree two, written v_0...v_4 cyclically,
has distinct external neighbors x_0,x_2,x_3,x_4. In M minus the pentagon,
each of the pairs x_2,x_3; x_3,x_4; x_4,x_0 has a common neighbor (C14).

Fix that pentagon and write r,z,t for those three common neighbors,
respectively. They are unique: two common neighbors for the same
distinct pair would create a four-cycle. Consecutive external vertices
x_2,x_3; x_3,x_4; x_4,x_0 cannot themselves be adjacent, also by girth.

### claim:opg434-c16-frontier
None of r,z,t is one of the four old ports. Also r!=t. Up to the
reflection v_j -> v_(2-j mod 5), the induced belt is exactly one of:

(A) r=z=y, with t different: eleven vertices, the pentagon, four
spokes, and edges yx_2,yx_3,yx_4,tx_4,tx_0. Exactly four edges leave
this induced subgraph, one at each of x_0,x_2,x_3,t.

(B) r,z,t distinct: twelve vertices, the pentagon, four spokes, and
edges rx_2,rx_3,zx_3,zx_4,tx_4,tx_0. There are four or five edges leaving
this induced subgraph, at distinct vertices among x_0,x_2,r,z,t.

No extra internal edges occur in either case. Outside endpoints of
the four or five edges are NOT presumed distinct. We do not prove
that either surviving block is reducible.

## 2. Two small-complement tools

### claim:opg434-c16-small-exterior
Let U induce a connected subgraph containing a cycle in M, and put
b=|delta_M(U)|<=3. If V(M) minus U is nonempty, then b is two or three
and the exterior is a tree on at most four vertices.

There cannot be two exterior components: each would have a nonempty
boundary of size at least two by (P1), totaling at least four. The
connected exterior has no cycle by (P3). For this tree let n_3 be its
number of vertices whose degree in M is three. All other degrees in
M are two, so the tree degree sum gives b=2+n_3.
If b=2, n_3=0, and the prohibition of adjacent degree-two vertices
forces a single exterior vertex.
If b=3, n_3=1. Removing that unique degree-three vertex leaves at most
three components, each consisting of at most one degree-two vertex.
Thus the exterior is a star with zero, one, two or three leaves.
For two or three leaves its three boundary edges have distinct ends
on the exterior. Whenever they also have distinct ends in U, (P3)
can glue any positive U to this exterior.

We will only use the last assertion with explicitly positive U and
ports of internal degree two. A cut with an acyclic side is not being
silently called a cyclic cut; the acyclic possibilities were just listed.

A useful target fact from C07 is:
two distinct nonadjacent labels have exactly two common neighbors,
and three distinct pairwise nonadjacent labels have exactly one.

Consequently, suppose three distinct ports have distinct pairwise
nonadjacent labels a,b,c in an explicit map of U. A single exterior
vertex can attach to any two or all three of them. If the exterior is
an edge wu, with w attached to the first two and u to the third,
choose w from N(a) intersect N(b) but outside N(c). Such a choice
exists because the first intersection has size two and the triple
intersection size one. Then choose u in N(w) intersect N(c), which
is nonempty. This realizes every ordering of the three ports.
One may use this together with the matching case above.

## 3. Hub/old-port coincidences are completely excluded

### claim:opg434-c16-no-old-port-hub
z cannot be an old port: x_0 is not adjacent to x_4, and x_2 is not
adjacent to x_3; endpoints cannot be their own common neighbors.
Similarly r can only be x_0 and t can only be x_2 if they are old ports.

If r=x_0, then x_0 already has neighbors v_0,x_2,x_3. A common neighbor
t of x_0,x_4 must be one of these three. It cannot be v_0, which would
make the triangle v_0,v_4,x_4, and cannot be x_3, since x_3x_4 is
forbidden. Hence t=x_2. Reflection proves the converse implication.

The ten vertices consisting of the pentagon, four ports and z now
have all degrees saturated except v_1, which is fixed at two, and z,
which has internal degree two. Their boundary has size at most one.
There is no possible extra internal edge: only z has remaining
capacity, since v_1 is required to have degree two. Connectedness and
the absence of a bridge imply that these ten vertices are all of M.

Here is an explicit B-map, with each symbol ij a target pair label:
(v_0,v_1,v_2,v_3,v_4)=(12,35,24,13,45),
(x_0,x_2,x_3,x_4,z)=(34,15,25,23,14).
All listed source edges join disjoint pairs. This contradicts the
choice of M and excludes both old-port coincidences.

Now all hubs are outside the ports. Equality r=t would require a
single vertex adjacent to all four distinct ports, violating degree
three. The only possible hub equality is r=z or z=t; both cannot
hold. The two cases are exchanged by the stated reflection.

## 4. The eleven-vertex merged-hub block

Assume r=z=y and call the indicated eleven-vertex subgraph U.
Put A=x_0, B=x_2, C=x_3, T=t. All vertices except these four and v_1
already have degree three in the displayed block. A,B,C,T each have
internal degree two, and v_1 has fixed total degree two.

The edge AT is already present. An extra edge BC would make a
triangle through y. Extra edges TB or TC would make a four-cycle
through x_4,y. Therefore the ONLY possible extra internal edges
are AB or AC, and at most one can be present.

Use these two explicit B-maps of the displayed block:
| map | (v_0,v_1,v_2,v_3,v_4) | (A,B,C,x_4,y,T) |
|---|---|---|
| I | (25,s_5,15,24,13) | (14,s_1,s_2,s_3,0,35) |
| II | (s_4,45,13,25,34) | (24,s_1,s_2,s_3,0,35) |

All edges are checked by the generator/pair adjacency rules. Map I
also satisfies extra edge AB; map II also satisfies extra edge AC.

If AB is present, only C,T retain external capacity, so b<=2. By (P1)
the exterior is empty or a single degree-two vertex joined to C,T.
Map I extends to that vertex with label 12. If AC is present, the
same argument applies to B,T and map II extends with label 12.
These also cover an empty exterior. Thus neither extra edge is
possible in M.

It remains to exclude b<=3 for the displayed block without extra edges.
The empty exterior is already covered by I. By Section 2 any nonempty
exterior is one of the small stars. Two or three leaves give a genuine
three-edge matching and are handled by (P3), using positivity of U.

For a one-vertex exterior of degree two, its two neighbors cannot be
A,T (triangle) or B,C (four-cycle). The four remaining possibilities
are explicitly covered as follows:
| two attached ports | map | exterior label |
|---|---|---|
| A,B | II | 13 |
| A,C | I | 23 |
| T,B | I | 12 |
| T,C | I | 12 |

A one-vertex exterior of degree three is impossible: every three of
A,B,C,T include A,T or B,C, creating a triangle or a four-cycle.

The remaining exterior is an edge wu, with w of degree three and u of
degree two in M. Its three boundary endpoints in U are distinct.
The pair attached to w must take one from {A,T} and one from {B,C}.
If u attached to the other member of {A,T}, the existing edge AT and
the path through w,u would form a four-cycle. Thus u attaches to the
other member of {B,C}. These four cases have explicit extensions:
| ports at w | port at u | map | (w,u) |
|---|---|---|---|
| A,B | C | II | (13,24) |
| A,C | B | I | (23,14) |
| T,B | C | I | (14,23) |
| T,C | B | I | (24,13) |

Every possible exterior with b<=3 has therefore been excluded.
Since at most four boundary edges are available, b=4, proving (A).

## 5. The twelve-vertex distinct-hub block

Assume r,z,t are distinct and let U contain the twelve indicated
vertices. Put A=x_0 and B=x_2. The five potential boundary vertices
are A,B,r,z,t, each of internal degree two. All other displayed
vertices except the fixed degree-two v_1 have degree three.

Among the five potential ports, At and Br are already edges.
An extra edge from z to r or t creates a triangle through x_3 or x_4.
An extra edge from z to A or B creates a four-cycle through t,x_4 or
r,x_3. Therefore all possible extra internal edges are
AB, Ar, Bt, rt.
They join the two existing edges At and Br. Two sharing an endpoint
violate degree three, and either disjoint pair produces a four-cycle.
Hence at most one extra edge can occur.

The following maps check the base block and the specified extra edge:
| map | (v_0,v_1,v_2,v_3,v_4) | (A,B,x_3,x_4,r,z,t) | extra edge |
|---|---|---|---|
| D1 | (25,s_5,15,24,13) | (14,s_1,s_2,s_3,0,23,35) | AB |
| D2 | (24,s_4,45,23,s_2) | (13,s_5,s_3,12,0,34,s_1) | rt |
| D3 | (12,35,24,13,45) | (s_1,s_2,s_3,s_4,0,34,14) | Ar |

The Bt case is the reflection of Ar. For each row the THREE remaining
potential boundary vertices receive distinct pairwise nonadjacent labels:
D1 gives (r,z,t)=(0,23,35);
D2 gives (A,B,z)=(13,s_5,34);
D3 gives (B,z,t)=(s_2,34,14).
One can verify nonadjacency by intersecting index pairs or checking
whether a generator index belongs to a pair.

With an extra internal edge there are at most three boundary edges.
An empty exterior is handled by the displayed map. A one-vertex or
one-edge exterior is handled by the independent-triple argument in
Section 2 (using the subset of ports when b=2). The two remaining
small stars have matching boundary and are handled by (P3).
Thus no extra internal edge is possible.

For the base block without extra edges, suppose again b<=3.
An empty exterior is handled by D2. A single exterior vertex of degree
two cannot attach to At or Br, because these are edges of U. For every
other pair of potential ports, D2 makes the labels nonadjacent except
for the pair r,t; D1 makes r,t nonadjacent. Hence all these cases extend.

For a one-vertex degree-three exterior, its three attached ports can
contain neither At nor Br, or there would be a triangle.
For a one-edge exterior of total degrees three and two, the same
restriction holds: an existing edge within the two ports at its
degree-three endpoint makes a triangle, and an existing edge between
a double-attached and single-attached port makes a four-cycle.

A triple from {A,B,r,z,t} avoiding both At and Br must be exactly one of
{A,B,z}, {A,r,z}, {B,t,z}, {r,t,z}.
D2 gives distinct pairwise nonadjacent labels on the first three;
D1 does on the fourth. Section 2 supplies the required extension
for either exterior shape. The other two small stars have a matching
boundary and are handled by (P3). This exhausts b<=3.

There are at most five boundary edges, so b is four or five.
The base block is induced. This proves (B) and the stated frontier.

## 6. Scope, reproduction and next obligation

The map tables are explicit paper certificates. They were checked
using: 0~s_i; s_i~jk iff i is in {j,k}; and ij~kl iff the pairs are
disjoint. No table was claimed to be produced by an executed search.
Their purpose is existential: no arbitrary outside homomorphism is
promised to be preserved. C15 explicitly rules out such unrestricted
bounded-radius repair.

The result reduces source topology and boundary size. Four-/five-edge
boundary compatibility remains open; neither C13's three-edge theorem
nor C14's two specified target edges can be silently applied to it.
The surviving blocks have distinct INSIDE boundary endpoints; the
outside endpoints may coincide or interact, which must be retained.

Candidate dependencies at the fixed base:
research/artifacts/candidates/opg434-a01-c06-separator-gluing.md
research/artifacts/candidates/opg434-a01-c07-star-obstructions.md
research/artifacts/candidates/opg434-a01-c12-square-reduction.md
research/artifacts/candidates/opg434-a01-c13-three-terminal-gluing.md
research/artifacts/candidates/opg434-a01-c14-pentagon-reduction.md
research/artifacts/candidates/opg434-a01-c15-radius-obstruction.md

A rejected pre-submission table used 34 adjacent to s_5, which is
false because 5 is not in {3,4}. The displayed I/II/D1 tables were
rebuilt using the stated adjacency rules; the rejected table is not
a source-graph obstruction. No automated checking is implied.

All hub/port coincidences, the two merged-hub edge choices, and
the four distinct-hub edge choices are accounted for. The proof
does not assume that the full minimum is cubic. It uses the original
five-transversal/B-map equivalence only at its declared candidate level.
No root proof, graph counterexample, EvidenceLink or Result is produced.
best_verified_result=none; best_verified_candidate=none.
Both admitted obligations remain open.

Next action: retain these exact four-/five-port frontiers and audit
a global quotient formulation suggested
by the four-cycle product model of B, rather than revive unrestricted
local repair. Any maximum-cut shortcut in that formulation must first
pass a connectedness/loop test on a nonbipartite positive graph.
