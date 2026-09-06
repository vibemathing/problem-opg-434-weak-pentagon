# C07: triple neighborhoods and the exact one-star obstruction

candidate_id: candidate:opg434-a01-c07-star-obstructions
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 5da7be8676a1074b3607012e943db6b441cbd5eb

This is a paper derivation extending C02/C06, not an execution receipt.
The source graph is always finite and simple. The root has no planarity assumption.
No graph enumerator, SAT solver or proof-assistant kernel was run.

## 1. Frozen local question and notation

Use C06's generators s_1,...,s_5 in F_2^4; S is their set, their sum is zero,
and this is their only nonzero F_2-linear relation. Adjacency in B means difference
in S. Write ij for s_i+s_j when convenient. N is an OPEN neighborhood, so a vertex
is nonadjacent to itself. We do not change the target or re-prove its equivalence.

For triangle-free subcubic G, let v have three distinct neighbors u_1,u_2,u_3.
Given an actual homomorphism f:G-v -> B, a one-star repair is a homomorphism of G
agreeing with f at every vertex outside {v,u_1,u_2,u_3}. All three neighbors may change.
This is stronger than requiring one good choice of f and is NOT the root assertion.

## 2. claim:opg434-c07-triple

For any labels x,y,z, N(x) intersect N(y) intersect N(z) is nonempty if and only
if their distinct labels form an independent set in B.
Its cardinality is 5 for one distinct label, 2 for two distinct nonadjacent labels,
and 1 for three distinct pairwise nonadjacent labels. Any adjacent pair makes it empty.

Proof. Necessity follows from triangle-freeness of B. The one/two-label cases are C06.
For three distinct labels translate x to 0. Nonadjacency to 0 writes y=ij and z=kl.
These two index pairs are distinct. If disjoint, y+z is the remaining generator,
contrary to their nonadjacency. Hence their intersection is one index, say
y=ij and z=ik. N(0) intersect N(ij)={s_i,s_j}, and only s_i is adjacent to ik.
Thus the common neighbor is unique, namely s_i, before undoing the translation.

Up to label permutation and the affine symmetries of C06 the cases are:
| representative | common neighbors | ordered triples in the full label space |
|---|---:|---:|
| (0,0,0) | 5 | 16 |
| (0,0,s_1) | 0 | 240 |
| (0,0,12) | 2 | 480 |
| (0,12,13) | 1 | 960 |
| (0,s_1,23), exactly one edge | 0 | 1440 |
| (0,s_1,s_2), two-edge path | 0 | 960 |

These counts are combinatorial, not enumeration output. The first three are
16, 3*16*5, 3*16*10. Each independent triple has its unique common neighbor,
so there are 16*binom(5,3)=160 unordered ones. Each edge has 6 vertices nonadjacent
to both ends, giving 40*6=240 one-edge triples. There are 16*binom(5,2)=160
two-edge triples. Multiply the last three counts by 6. They sum to 4096=16^3.

For degree-three vertex restoration with fixed neighbor labels this table is exact.
In particular a common neighbor fails only through an adjacent pair, not through
a fourth hidden orbit of three mutually nonadjacent labels.

## 3. claim:opg434-c07-star-criterion

Put A_i={f(w): w in N_G(u_i) minus {v}} and D=A_1 union A_2 union A_3.
Each A_i has at most two labels. Its labels are pairwise nonadjacent because f(u_i)
is already a common neighbor. Triangle-freeness of G means no edges join different u_i.

A one-star repair exists if and only if
    B minus union_{a in D} N_B(a) is nonempty.                         (1)

More exactly the possible center labels are precisely that set. For a proposed
center t the available labels at u_i are N_B(t) intersect intersection_{a in A_i}N_B(a).
By Section 2 this is nonempty precisely when t is nonadjacent to all of A_i.
For A_i empty, N_B(t) has five elements. Choices at distinct u_i do not interfere:
there are no edges between them. All other edges were already checked by f.
This proves both necessity and sufficiency, including repeated/shared exterior vertices.

The number of completions fixing all exterior labels is exactly the sum over the
t in (1) of the products of those three intersection cardinalities. Thus (1) is
a complete finite boundary relation, not just a necessary test.

Equivalently, repair fails precisely when D totally dominates B: every target vertex,
including vertices of D themselves, has a neighbor in D. Closed domination is not meant.
Degree-two source vertices with at most three exterior labels cannot create this
one-star obstruction; the precise scope remains the frozen repair rule above.

## 4. claim:opg434-c07-minimum-boundary

At least four distinct exterior labels are necessary for failure, since three
open neighborhoods have total size at most 15 < 16. Four suffice.

Moreover a four-element set D totally dominates B if and only if B[D] is a C4.
Here is a full small-set audit. For four distinct labels let F=B[D], let w be the
sum of binom(deg_F(a),2), and let q be the number of common neighbors of all four.
Inclusion-exclusion and Section 2 give
    |union_{a in D} N(a)| = 12+w-q.
Indeed each nonedge pair contributes 2 to the pair intersections, each independent
triple contributes 1, and the number of independent triples is 4-2|E(F)|+w.
Since F is triangle-free, its possible forms yield:
| F | union size |
|---|---:|
| empty | 11 or 12 (q=1 or 0) |
| one edge and two isolated vertices | 12 |
| two disjoint edges | 12 |
| P3 and an isolated vertex | 13 |
| P4 | 14 |
| K1,3 | 15 |
| C4 | 16 |

For F with an edge q=0. For F empty, q is 0 or 1 by the triple theorem.
The listed forms exhaust triangle-free graphs on four vertices.

## 5. claim:opg434-c07-minimum-tree-witness

Take eight vertices v,u_1,u_2,u_3,a,b,c,d and exactly the seven edges
v-u_1, v-u_2, v-u_3, u_1-a, u_1-b, u_2-c, u_2-d.
This is a planar triangle-free subcubic tree. Freeze
    f(a)=0, f(b)=12, f(c)=s_1, f(d)=s_2,
and take f(u_1)=s_1, f(u_2)=0, f(u_3)=0 on G-v.
Every present edge has a generator difference, so this is a genuine homomorphism.

In every proposed repair the first two neighbor lists are respectively
    L_1={s_1,s_2},  L_2={0,12}.
Every element of L_1 is adjacent to every element of L_2. They cannot both be
neighbors of one target vertex. Allowing u_3 to change arbitrarily cannot help.
The four frozen labels induce the target C4 (0,s_1,12,s_2,0).

This is vertex-minimum for the stated repair rule among triangle-free subcubic
graphs with degree-three center: with at most seven vertices there are at most
three vertices outside the four-vertex star, so Section 4 makes failure impossible.
It is also minimum in the number of distinct exterior labels.
No minimum-order assertion is made for CUBIC witnesses or for root counterexamples.
The tree itself maps to any edge of B by its ordinary bipartition.

## 6. claim:opg434-c07-cubic-witness

The failure can be realized with f defined on ALL of G-v in a 48-vertex connected
planar triangle-free cubic graph which itself has a B-homomorphism.

Start with the preceding tree, whose five leaves are u_3,a,b,c,d.
For each leaf w attach eight new vertices A_0,...,A_3,B_0,...,B_3.
Take the cube C4 square K2 on these eight vertices, delete A_0A_1, and add
wA_0,wA_1. Leaves now have degree three; all new vertices also have degree three.
The added piece together with w is a subdivided cube edge. It is triangle-free
and planar, and pieces attach at single tree vertices. Hence the whole graph
is simple, connected, planar, triangle-free and cubic, with 8+5*8=48 vertices.

For complete label data define a target pentagon
z_0=0, z_1=s_1, z_2=12, z_3=s_4+s_5, z_4=s_5, in this cyclic order.
In each piece set
    w:z_1;
    (A_0,A_1,A_2,A_3):(z_0,z_2,z_3,z_4);
    (B_0,B_1,B_2,B_3):(z_4,z_3,z_2,z_3).
Each piece edge joins consecutive pentagon labels. Translate all labels of that
piece by f(w)+z_1 to match any prescribed value f(w).
Apply this to the Section 5 map on the tree minus v. This gives a homomorphism
on the entire 47-vertex graph G-v. The same two incompatible lists at u_1,u_2
remain, so repairing the closed star while fixing the exterior is impossible.
In fact the exterior labels immediately adjacent to u_3 add only s_1,s_2.

Independently, map the ORIGINAL tree to an edge of B and extend each piece by
the same translation recipe. This explicitly supplies a homomorphism of G.
Thus even planarity plus triangle-freeness plus cubicity does not validate
arbitrary one-star repair. This example has bridges and is NOT a witness against
a version additionally restricted to 3-edge-connected source graphs.

## 7. Additional boundary attack and next obligation

Four labels are the minimum but not the only obstruction pattern:
{0,s_1,s_2,s_3,s_4} is a five-element total dominating set inducing K1,4.
The neighborhood of 0 covers all five generators, and the neighborhoods of
s_1,...,s_4 cover 0 and all ten pair sums. Deleting a leaf leaves only 15 covered
vertices; deleting 0 leaves four independent generators and is not total dominating.
Six exterior slots can realize this obstruction as pairs (0,0),(s_1,s_2),(s_3,s_4).
Consequently searching only target C4 subsets would miss other failed stars.

Failed auxiliary hypothesis: every f:G-v -> B extends after changing only N_G[v].
It has the exact witnesses above. This does not invalidate the admitted
five-transversal equivalence route and does not close the root.

The next substantive step is NONLOCAL repair: allow translations on components
after deleting two generator colors, and audit which obstructing terminal
adjacencies those switches can remove. Also freeze the exact five-cycle attachment
relation. No new obligation IDs, truth records, or verification status are asserted.

Reproduction: check the generator relation from C06, the six triple cases,
inclusion-exclusion, the seven tree edges and the displayed cube-piece labels.
All proofs use finite graph theory and finite combinatorics only.
best_verified_result: none
best_verified_candidate: none
