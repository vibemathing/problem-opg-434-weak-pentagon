# C08: exact cut switches and an obstruction inside a 3-edge-connected cubic graph

candidate_id: candidate:opg434-a01-c08-cut-switches
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 958a4f78550b01a043dc90a91747804c9d6031ff

This advances C07 by allowing changes outside a closed star. All results below
are paper derivations. No graph enumeration, SAT solver or kernel was executed.
Use C06's five generators S={s_1,...,s_5}, whose only nonzero linear relation
is their total sum zero. Write ij=s_i+s_j. Neighborhoods are open.

## 1. Frozen operation and exact legality

Let f:H -> B be an actual homomorphism, and label each edge uv by its unique
generator c(uv)=f(u)+f(v) in S. For X subset V(H) and d in F_2^4, define
f_{X,d}(u)=f(u)+d on X and f(u) otherwise. This is one uniform subset
translation. It is not arbitrary recoloring, not a whole-star repair, and
not signed-graph switching.

### claim:opg434-c08-switch-classification
For every edge of the cut delta_H(X), its new difference is c(e)+d.
All other edge differences are unchanged. Consequently:
- d=0: every X is legal.
- d=s_k: legality is equivalent to delta_H(X) being empty.
- d=ij, i!=j: legality is equivalent to every cut edge having color s_i or s_j.

Proof. S intersect (S+s_k) is empty by the generator relation. Also
S intersect (S+ij)={s_i,s_j}: these two generators are exchanged, and
s_k+si+sj for a different k is a pair sum, not a generator.
The vectors 0, the five generators and the ten pair sums exhaust the group.

For d=ij let H_{ij} retain precisely the OTHER THREE generator colors.
The permitted X are exactly unions of connected components of H_{ij}.
For d=s_k they are unions of connected components of H.
In particular the components to use are NOT the bichromatic i/j components.
The rule is an exact test on an existing map, not an existence theorem.

## 2. The complete one-switch test for three terminals

Suppose H=G-v and the three neighbors of v have a bad label triple.
C07 classifies every such triple, up to terminal reordering and an affine
target automorphism, into the three forms in the following table.
A nontrivial split of three terminals moves one terminal or its complementary
pair. These have the same effect on pair differences up to a global translation.
Thus it suffices to list the singleton terminal to be separated.

### claim:opg434-c08-one-switch-table

| terminal labels (x,y,z) | singleton to move | allowed generator shifts | allowed pair shifts |
|---|---|---|---|
| (0,0,s_1) | z | s_1,s_2,s_3,s_4,s_5 | 23,24,25,34,35,45 |
| (0,s_1,23) | x | s_1,s_4,s_5 | 23,24,25,34,35 |
| (0,s_1,23) | y | s_1,s_2,s_3 | 24,25,34,35,45 |
| (0,s_1,s_2) | x | s_1,s_2,s_3,s_4,s_5 | 34,35,45 |

No omitted choice of singleton works. Moving it would leave an adjacent pair
among the two unchanged terminals. Each displayed shift works at the label
level, allowing two resulting labels to coincide.

For example in the second row a pair shift ij must avoid index 1 so that
x+ij is nonadjacent to y=s_1. It must also meet {2,3}, so that ij+23 is
not a generator. This gives exactly its five displayed pairs.
For generator shifts in that row, indices 2,3 fail and the other three work.
For the third row the difference to z is 45+ij, giving the other five pairs.
The first and last rows follow by avoiding respectively index 1 and both
indices 1,2 in a pair shift. The generator cases follow directly by addition.

To turn the table into an exact graph-level ONE-SWITCH criterion, impose:
for a pair shift ij, the chosen singleton terminal is in a different component
of H_{ij} from EACH of the other two terminals; for a generator shift use H.
This condition is necessary and sufficient for a legal X realizing that split.
After it holds, C07 supplies a common neighbor and hence a label for v.
If it fails for every row/shift, no one uniform subset translation repairs f.
This does not exclude a sequence of switches or another homomorphism.

## 3. An invariant that obstructs every one-step choice

### claim:opg434-c08-monochromatic-path-lock
If x and y are joined in H by an odd-length path all of whose edges have the
same generator s_k, their labels remain adjacent after ANY one legal uniform
subset translation f_{X,d}.

Indeed f(x)+f(y)=s_k. If both endpoints lie on the same side of X, this
difference does not change. Otherwise the path has a cut edge of color s_k.
The classification in Section 1 then forces d=kj for some j!=k, and the new
endpoint difference is s_k+kj=s_j. It is still a generator.

This covers supports of arbitrary size and the entire list of possible d.
Applying a global target automorphism before or after the switch does not
help: automorphisms preserve adjacency and permute generator directions.
The assertion is for ONE step. A first switch can destroy monochromaticity,
after which a later switch need not preserve the old terminal adjacency.

## 4. A six-vertex witness, with an explicit two-step cure

Take vertices v,x,a,b,y,z and precisely edges
vx,vy,vz,xa,ab,by. This is a pentagon with a pendant vertex z.
On H=G-v prescribe
f(x)=0, f(a)=s_1, f(b)=0, f(y)=s_1, f(z)=23.
This is a homomorphism on all of H. The path x-a-b-y has three edges of
color s_1, so Section 3 prevents any one-switch extension at v.

Nevertheless two legal switches suffice:
1. Translate {a} by 12. Its two cut edges have color s_1.
   The new label is s_2, and xa,ab now have color s_2.
2. Translate {x} by 23. Its only cut edge xa now has color s_2.
   The new label of x is 23.

The terminal labels become (23,s_1,23). Set f(v)=14.
Its differences to 23 and s_1 are respectively s_5 and s_4.
All edges of G are now valid. This is a concrete distinction between a
one-step obstruction and a persistent obstruction.

### claim:opg434-c08-six-vertex-minimality
Six vertices are minimum for failure of this one-switch rule among
triangle-free subcubic graphs with a degree-three deleted vertex.

With at most five vertices, H has three mutually nonadjacent terminals and
at most one other vertex. Each nontrivial component of H is a star centered
at that other vertex. Terminal labels in a common component are pairwise
nonadjacent because they have a common neighbor label.
For a bad repeated-adjacent triple, the unique differently labeled terminal
therefore lies apart from the other two. For a two-edge-path triple its center
label lies apart from both others. For a one-edge triple its two adjacent
terminals lie in different components; at least one of their components
does not contain the third terminal. The table always has a generator shift
for that separated singleton. Translating its whole component repairs the
triple. This proves the lower bound, including isolated vertices.

This minimum concerns one uniform subset translation, not C07's different
closed-star operation and not cubic or root counterexamples.

## 5. A cubic witness with the connectivity already sought in C06

### claim:opg434-c08-cubic-one-switch-failure
Let G be the pentagonal prism with top a_0,...,a_4, bottom b_0,...,b_4,
cycle edges in each layer (indices modulo 5), and spokes a_j b_j.
Delete v=a_0. Define on ALL nine remaining vertices
(a_1,a_2,a_3,a_4) = (0,s_1,0,s_1),
(b_0,b_1,b_2,b_3,b_4) = (23,s_2,0,s_1,14).

The three surviving top edges have color s_1.
The bottom cycle colors, starting with b_0 b_1, are
(s_3,s_2,s_1,s_4,s_5).
The four surviving spokes j=1,2,3,4 have colors
(s_2,s_1,s_1,s_4).
These lists check every edge of G-v. The neighbor labels of v are
(0,s_1,23). The odd monochromatic top path a_1-a_2-a_3-a_4 implies that
NO one legal uniform subset translation, regardless of support, allows v
to be restored.

The source graph is simple, planar, triangle-free and cubic.
Here is also a direct 3-edge-connectivity proof without planar reasoning.
For a vertex subset U let A,C be its index sets in the two layers. Then
|delta_G(U)| equals the number of transitions around C5 for A, plus that
number for C, plus |A symmetric_difference C|.
Each nontrivial proper layer subset has at least two transitions.
If both are proper nonempty, the cut has size at least 4. If just one is,
the cut has size at least 2+1=3. If neither is, a nonempty proper U must
be one entire layer, whose cut has size 5. Thus every nontrivial cut has
size at least 3, and a vertex cut has size 3. No bridge or two-edge cut
explains this particular one-step failure.

For avoidance of a false root conclusion, an explicit FULL map of G is:
z_0=0, z_1=s_1, z_2=12, z_3=45, z_4=s_5,
a_j maps to z_j, b_j maps to z_{j+1}.
The z_j form a target pentagon with successive generator differences
s_1,s_2,s_3,s_4,s_5. Every layer edge and spoke is therefore valid.
This full map need not agree with the prescribed partial one.

## 6. Limitations, reproducibility and the next unique obstacle

The failed auxiliary assertion is universal ONE-SWITCH repair of a prescribed
map after deletion of a degree-three vertex. It is not the admitted equivalence
route, not arbitrary finite-sequence repair, and not the universal root claim.
The 10-vertex witness does not assert failure of the different one-star rule.

Reproduce on paper by checking the unique generator relation, the table's
four rows, the six-vertex edge list and both prism maps. No installed solver,
enumeration output, runtime version or verifier receipt is asserted.

C01-C07 remain candidate dependencies. Sources and switching distinctions are
recorded in research/artifacts/source-notes/opg434-a01-c08-switch-comparison.md.
Both admitted obligations remain open; best_verified_result=none and
best_verified_candidate=none.

Next: freeze the exact boundary extension relation for a five-cycle, then
seek a multi-step recoloring argument that changes boundary feasibility.
The missing global step is to show that SOME reachable partial map extends,
not that every given partial map is repairable by one operation.
