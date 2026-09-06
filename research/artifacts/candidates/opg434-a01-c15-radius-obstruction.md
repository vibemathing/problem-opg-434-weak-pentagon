# C15: arbitrary-radius repair obstruction in positive cubic girth-five graphs

candidate_id: candidate:opg434-a01-c15-radius-obstruction
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: d8220b87d903640d1abd2d835aba2f01a32f23dc

This is a paper construction auditing a proposed way of using the C02
homomorphism equivalence. It does not change the admitted target or assert
a counterexample to the root. No graph program or mathematical verifier ran.

## 1. The precise auxiliary statement being attacked

Let B have vertex set the even vectors in F_2^5. Put J=(1,1,1,1,1),
s_i=J+e_i, and S={s_1,...,s_5}. Two vertices are adjacent exactly when
their difference belongs to S. Write ij=s_i+s_j. These are exactly the
16 labels 0, the five generators, and the ten pairs.

For r>=0, an r-repair of f:G-v -> B is a homomorphism g:G -> B agreeing
with f on every vertex w satisfying dist_G(v,w)>r. All labels within
the closed radius-r ball may change simultaneously and arbitrarily.
The distance is measured in the full source graph, not in G-v.

### claim:opg434-c15-no-uniform-radius
For every integer r>=0 there is a finite simple connected cubic graph G_r
of ordinary girth exactly five and a vertex v such that G_r maps to B,
but some genuine homomorphism f:G_r-v -> B has no r-repair.

The universal rule negated here quantifies over EVERY given punctured map.
The frozen root asks for ONE suitable whole-graph coloring. These are
different quantifiers. The witness graphs below have bridges; no version
restricted to cyclically four-edge-connected graphs is ruled out.

## 2. Exact two-state lists propagated down binary trees

For X subset V(B), let N(X) be the UNION of its open neighborhoods.
In particular N(X) is not the set of common neighbors of X.

The adjacency rules follow directly from the generator relation:
0 neighbors exactly S; no two generators are adjacent; s_i neighbors jk
exactly when i belongs to {j,k}; two pair labels are adjacent exactly
when their index pairs are disjoint. Define the four nonadjacent pairs
K={24,25}, A={s_1,s_2}, C={0,13}, D={0,12}.

These explicit identities use only the preceding rules:
N(s_2) intersect N(13) = K;
N(A) = {0,12,13,14,15,23,24,25};
N(C) = S union {24,25,45};
N(D) = S union {34,35,45}.
Consequently N(A) intersect N(C)=K, but N(A) intersect N(D) is empty.

Translations and permutations of the five generator indices are
automorphisms. They act transitively on ordered distinct nonadjacent
pairs: translate the first entry to zero, permute the two indices in
the nonzero pair difference, and translate back. Thus an affine image
of any rooted pinned tree whose feasible root set is K can have feasible
root set equal to any specified distinct nonadjacent pair.

### claim:opg434-c15-recursive-pair
For each h>=1 there is a full rooted binary tree P_h of height h, with
only its leaves pinned to B-labels, whose feasible root labels are
EXACTLY K. Every label in K is realized by an actual extension of all
the leaf pins to the whole tree. The tree has 2^(h+1)-1 vertices.

For h=1 pin the two children to s_2 and 13, and use the first identity.
For h+1 take two disjoint copies of P_h. Apply to all leaf labels in
one copy an affine automorphism taking K to A, and in the other one
an affine automorphism taking K to C. Join their roots to a new root.
A new-root label t is feasible exactly when it has a neighbor in each
child's feasible root set, that is, exactly when
t belongs to N(A) intersect N(C)=K.
The children live in disjoint trees, so their choices and realizing
extensions can be made separately. This proves both exclusion and
attainment, rather than just an upper bound on the feasible list.
Height and vertex count follow by the same recursion.

For reproducibility one may choose the first admissible affine map in
a fixed lexicographic order on translations and generator permutations.
This is a finite definition, not a claim of an executed search. The
transitivity proof guarantees that such a choice exists at every use.
Internal nonroot vertices have degree three, the root degree two, and
leaves degree one. Different leaves are different source vertices even
when they receive the same label.

## 3. A finite tree with an arbitrarily remote obstruction

Take two affine copies of P_h with feasible root lists A and D. Add a
new vertex v and join it to the two roots. Call the resulting tree T_h.
Prescribe only the inherited leaf labels.

### claim:opg434-c15-tree-obstruction
The leaf assignment extends to T_h-v but not to T_h. Every pinned leaf
has distance exactly h+1 from v, and T_h has n=2^(h+2)-1 vertices.

Each component of T_h-v has a nonempty root list and a realizing map,
so the punctured map is genuine. A map of the whole tree preserving
the pins would require the center label in N(A) intersect N(D), which
is empty. There are no constraints on intermediate labels beyond the
tree edges, so the obstruction already permits arbitrary simultaneous
changes on every nonleaf vertex.

Without the leaf constraints, T_h maps to any edge of B by its ordinary
bipartition. Thus this obstruction is not an uncolorable source graph.

## 4. A positive one-port cubic-completion gadget

Use ten source vertices indexed by two-element subsets of {1,...,5},
joining two when the subsets are disjoint. Subdivide the source edge
between 12 and 34 by a new vertex w. Denote this 11-vertex graph by Q.

### claim:opg434-c15-positive-port
Q is simple and connected; w has degree two and every other vertex
has degree three. Its girth is exactly five, and it maps to B.

A two-element subset has exactly three disjoint two-element subsets.
Two overlapping subsets share a common neighbor, namely the complement
of their three-element union; disjoint ones are already adjacent. This
also proves connectedness of the unsubdivided graph. No triangle can
use three disjoint pairs on five indices. There is no four-cycle:
adjacent pairs have no common neighbor, while different nonadjacent
pairs have exactly one, so no two opposite vertices can have two
distinct common neighbors. Subdivision preserves the absence of cycles
of length less than five. The five-cycle
12,35,24,13,45,12
avoids the subdivided edge and remains, proving girth exactly five.

Here is an explicit full map q:Q -> B. Map every pair vertex to its own
pair label EXCEPT the source vertex 12, which is mapped to s_5; map w
to 15. The unchanged neighbors of source vertex 12 are 35 and 45,
both adjacent to s_5. The subdivided path maps to s_5,15,34, whose two
edges are valid. Every other source edge still joins disjoint pair
labels. This checks every type of edge of Q.

If a new bridge joins an outside vertex of prescribed B-label a to w,
translate q by a+s_1+15. The port label becomes a+s_1, adjacent to a.
Thus attaching Q imposes no restriction on the outside label.

## 5. Completing the tree without shortening distances

At each u in T_h attach 3-deg_T_h(u) disjoint copies of Q, using one
new bridge from u to each new port w. Let the completed graph be G_h.

### claim:opg434-c15-completion
G_h is finite, simple, connected, cubic, and has ordinary girth five.
Distances between original vertices of T_h are unchanged, and
|V(G_h)|=12*2^(h+2)+10.

Degrees become exactly three at each old vertex and each port, and
all other gadget vertices already have degree three. Every added
connecting edge is a bridge, since its gadget has no other attachment.
Every cycle consequently lies in a copy of Q; T_h itself is a tree.
There is at least one attached copy, so girth is exactly five.

A shortest path between two tree vertices cannot enter a gadget and
return through the same attachment: that would repeat a vertex.
Hence their distance is exactly their tree distance.
For a tree on n vertices the total missing degree is
sum_u(3-deg(u))=3n-2(n-1)=n+2.
There are n+2 disjoint 11-vertex gadgets, so the total is
n+11(n+2)=12n+22=12*2^(h+2)+10.

Map the tree to an edge of B, and extend across each bridge by the
translation recipe. This explicitly proves G_h itself maps to B.

For a genuine map f:G_h-v -> B, first use the two prescribed-leaf
maps of Section 3. Extend every gadget attached to u!=v by its
translation recipe. The gadget attached to v is a separate component
after v is deleted, so simply give it q. Every present edge of G_h-v
has now been checked. No label is prescribed at the missing vertex.

Set h=max(1,r). Every original leaf is at distance h+1>r from v.
Any r-repair must keep these leaf labels. Restricting such a repair
to T_h contradicts Section 3, regardless of changes elsewhere in the
radius-r ball or in the gadgets. This proves the theorem in Section 1.

## 6. Rejected shortcut, limits and statement comparison

C07 excluded repair confined to the closed star, using a fixed finite
boundary. The new quantifier is: for EACH r, a finite positive cubic
girth-five example defeats repair within radius r. The recursive
two-state lists and the distance-preserving port completion are what
extend the old obstruction; merely repeating its fixed witness would
not prove this claim.

The Q completion also works for a general subcubic graph H of girth
at least five: attaching one Q per missing degree gives a cubic
girth-at-least-five graph with |V(H)|+11(3|V(H)|-2|E(H)|) vertices.
Any given B-map of H extends, and any full map restricts to H.
The induced original H and its internal distances are preserved.
If no gadget is needed, its girth need not be exactly five.
This is not a claim that a given unnormalized five-edge assignment
extends with exactly the same colors: C02's passage to B can recolor.

The completion has bridges and does not preserve higher connectivity.
C13's minimal-counterexample cyclic-cut restriction is not contradicted.
The candidate does not exclude global recoloring, an existential choice
of a favorable punctured map, or a repair theorem proved only for
minimal non-B-mappable graphs. Our graphs are explicitly B-mappable.
No computational complexity lower bound for deciding the root follows.

No new external theorem or novelty assertion is required. The source
comparison is against these frozen candidate dependencies:
research/artifacts/candidates/opg434-a01-c02-normalization.md
research/artifacts/candidates/opg434-a01-c07-star-obstructions.md
research/artifacts/candidates/opg434-a01-c13-three-terminal-gluing.md
The original contract remains at
problem-library/records/canonical-problems.jsonl.
These are candidate dependencies, not admitted evidence.

## 7. Audit and next action

Audit the distinction between union neighborhoods and common neighbors,
the attainment part of the recursive root lists, every edge affected
by the subdivision map, and the single-attachment distance argument.
Check the smallest r=0,1 case by the same formulas (h=1), not by assuming
an experiment was run. No graph enumeration, solver, kernel or verifier
receipt was generated; all stated counts follow from the formulas.

Auxiliary failed hypothesis: one fixed finite radius repairs every
punctured B-map of every positive connected cubic girth-five graph.
The admitted equivalence route is not failed, and no failed-route
truth ledger is modified. Both admitted obligations remain open.
best_verified_result=none; best_verified_candidate=none.

Next action: return to the one-deficiency pentagon belt or prove a
genuinely connectivity-restricted boundary lemma. Another uniform
local-repair claim on all cubic graphs must not be used. For the belt,
preserve possible common-neighbor coincidences and distinguish real
source-edge constraints from freely chosen target labels.
