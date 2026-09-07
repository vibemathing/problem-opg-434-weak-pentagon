# Layered pentagon repair obstruction: strong connectivity and unbounded changes

candidate_id: candidate:opg434-a01-layered-pentagon-repair-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
preparation_base_revision: d8220b87d903640d1abd2d835aba2f01a32f23dc
transport_status: local preparation; PR #18 is the current observed transport cycle; no new branch or packet claimed

This strengthens the extra-strategy obstruction in the observed C15 candidate
to a graph without nontrivial small edge cuts and a deleted induced PENTAGON. It does not contradict C14, whose
induction constructs a suitable exterior map rather than preserving every
given exterior map within a bounded repair region.

## 1. Precise theorem

Define B on the even vectors of F_2^5. Let J be the all-ones vector and
t_a=J+e_a for a in Z/5Z. Two target vertices are adjacent when their
difference is one of the five t_a. All indices below are modulo five.
For distinct a,b put p_ab=t_a+t_b. Its 16 labels are 0, the five t_a,
and the ten p_ab. A subset I of generators sums to |I|*J+sum_{a in I}e_a;
this is zero exactly when I is empty or is all five indices. This proves
the generator relation used below, including the absence of triangles.

### claim:opg434-layered-repair-pentagon-hole
For every R,K>=0 there exist a finite connected simple cubic graph G,
an induced five-cycle Q, and a homomorphism f:G-V(Q) -> B such that:

1. G has ordinary girth exactly five, is nonbipartite and
   three-vertex-connected, and every three-edge cut is trivial.
2. G has an explicit TOTAL homomorphism to B.
3. Every total homomorphism F:G -> B changes f at more than K old
   vertices and changes f at some vertex at distance greater than R
   from V(Q). In fact the changed vertices include all vertices of
   a layer-0 geodesic from a neighbor of Q to a distant leaf.

Thus a uniform radius or a uniform edit count cannot guarantee repair
of EVERY prescribed exterior map around a pentagon, even in positive
graphs satisfying these strong connectivity restrictions.

## 2. The half-target obstruction and pinned binary branches

Let A={0,p_01}, and U(A)=N(0) union N(p_01).
The induced graph B[U(A)] is bipartite. Both neighborhoods are independent
because B is triangle-free. Their intersection has no neighbors within
their union. A bipartition is N(0) and N(p_01) minus N(0).
Directly, its non-isolated part is the six-cycle between
{t_2,t_3,t_4} and {p_23,p_24,p_34}; t_0 and t_1 are isolated.
Only bipartiteness is needed below.

Here is the full message lemma, including attainment. For every h>=1
and every pair P of distinct nonadjacent target labels, a full rooted
binary tree of height h has a leaf assignment whose exact root list is P.

At height one, write P={u,u+p_ij} and pin the two leaves to u+t_i and
u+t_j. Their common neighbors are exactly u and u+p_ij. At the induction
step take disjoint child trees with exact root lists {0,p_01} and
{t_0,t_2}. Direct target adjacency gives
U({0,p_01})={t_0,...,t_4,p_23,p_24,p_34},
U({t_0,t_2})={0,p_01,p_02,p_03,p_04,p_12,p_23,p_24}.
Their intersection is the nonadjacent pair {p_23,p_24}.
These are UNION neighborhoods: the new root needs a neighbor in each
child's allowed list, not a common neighbor of every element of a list.

Translations and permutations of the indices act transitively on ordered
nonadjacent pairs: translate the first label to zero and permute the two
indices of the difference. Apply such an automorphism to all pins to
obtain any desired pair P. Every listed root value has compatible child
values and their inductive realizing maps; the child trees are disjoint.
This proves exactness and attainment at each height. This lemma agrees
with the recursive-pair argument in the observed C15 candidate, but is
included here so the construction has no omitted message dependency.

In particular take P=A. Choose a realizing map f_a with root image 0.
Take five disjoint copies, indexed by a. Only leaves are pinned; source
vertices remain distinct even when their images coincide.

Build F_h from a central cycle c_0,...,c_4 and the five branches:
join c_a to the root of branch a. All non-leaves of F_h have degree
three, all leaves degree one. It is connected, unicyclic, and its only
cycle is the central pentagon. All leaves have distance D=h+1 from
the central cycle.

There is no full map of F_h respecting all of these leaf pins.
Such a map would put each branch root in A and hence put every central
vertex in U(A), mapping the odd cycle into a bipartite induced subgraph.
But the disjoint union of the five pinned branches is mappable by the f_a.

The order of F_h is 5+5(2^(h+1)-1)=5*2^(h+1).

## 3. Five-layer cubic graph and an explicit total map

Make five copies of F_h, indexed by j in Z/5Z. At every leaf l add
(l,j)(l,j+1) for all j, creating a five-cycle in that leaf fiber.
No other inter-copy edges are added. Let G_h denote the resulting graph
and Q the central pentagon in layer 0.

G_h is finite, simple, cubic, and connected. Internal vertices retain
their degree-three horizontal edges; each leaf acquires two different
vertical neighbors in addition to its tree edge. No edge types overlap.
A single leaf fiber connects all five connected layers.

There are no triangles or four-cycles. In a closed walk of length less
than five, the signed sum of vertical steps must be zero, not a nonzero
multiple of five. Thus it has an even number of vertical edges.
With zero, a short cycle would already occur in F_h. With four, a
four-cycle would have to lie in a leaf C5. With two, a hypothetical
simple four-cycle has two horizontal edges which project to the same
base edge in opposite directions; its two vertical edges must occur
at different endpoints, making both endpoints leaves. F_h has no
leaf-to-leaf edge. Two vertical edges in a triangle would leave only
one horizontal step and could not close the base projection.
These cases exclude all shorter cycles. The old central cycle gives
girth exactly five, and Q remains induced.

Here is a TOTAL homomorphism without the problematic leaf pins.
Put z_0=0 and z_j=sum_{k=0}^{j-1} t_k, for j=1,...,4.
The sequence z_0,...,z_4 is a target five-cycle.
Map the central cycle of F_h by phi(c_a)=z_a, and extend into branch a
by alternating the added difference t_0 along every successive tree edge.
Thus phi:F_h -> B is explicit. Set

  F_total(w,j)=phi(w)+z_j.                                (1)

Horizontal edges preserve the phi edge difference; vertical leaf edges
have difference z_j+z_{j+1}, a generator. Formula (1) is a total map.
It does not have to agree with any of the prescribed leaf pins.

The order of G_h is 25*2^(h+1). Its leaf cycles and central cycles
are odd, so this graph is genuinely nonbipartite.

## 4. A valid map with ONLY the layer-0 central pentagon missing

A partial map of the five pinned branches alone is not enough. All
vertices in the other four layers, including their central pentagons,
must be assigned compatible images.

For branch a set
q_(a,0)=0 and q_(a,j)=sum_{k=0}^{j-1} t_(a+k), 1<=j<=4.
For a fixed a these five translations form a target five-cycle.
In layer j map every branch vertex w of branch a to f_a(w)+q_(a,j).
Its root therefore has image q_(a,j), and all horizontal branch edges
are valid. At a leaf, all five vertical edges are valid because consecutive
q translations differ by a generator.

It remains to map the central pentagons in layers 1,2,3,4.
The following table gives their images y_(a,j):

| layer j | branch-root pin q_(a,j) | central image y_(a,j) |
|---|---|---|
| 1 | t_a | p_(a,a+2) |
| 2 | p_(a,a+1) | p_(a+2,a+4) |
| 3 | p_(a+3,a+4) | p_(a,a+2) |
| 4 | t_(a+4) | p_(a+4,a+1) |

Each row is a genuine target five-cycle as a varies: consecutive displayed
pairs have disjoint index sets, so their difference is a generator.
The central-to-branch edge is also valid in every row. In rows 1 and 4
the pair contains the generator index of its pin. In rows 2 and 3
the two pair index sets are disjoint.

These statements check every edge of G_h-V(Q): branch horizontal edges,
central horizontal edges in the other four layers, all spokes in those
layers, and every vertical leaf edge. There is no central-to-central
vertical edge. Thus the formula defines a genuine partial homomorphism f,
not just a partial assignment on several disconnected fragments.

In layer 0 the branch maps are exactly the f_a, retaining their original
pinned leaves. This is where the obstruction in Section 2 survives.

## 5. Strong connectivity, with the unicyclic case audited

For a subset W of G_h let A_w={j:(w,j) belongs to W}. The exact cut identity, now on F_h and its leaf C5 fibers, is:

  |delta(W)| =
    sum_{uv in E(F_h)} |A_u symmetric_difference A_v|
    + sum_{l leaf} |delta_C5(A_l)|.                      (2)

Suppose W is nonempty and proper with boundary at most three.
At most one leaf fiber can have a nonempty proper layer subset, since
each such fiber costs at least two vertical cut edges.

If all leaf fibers are constant, different constants at two leaves
would cost at least five horizontal cut edges along a base path.
Hence they all agree; complement W so they are all empty.
The components of G_h[W] then lie within separate layers and contain
only original degree-three non-leaves. Each component is a tree or is
unicyclic. A tree component of order k has boundary k+2. A unicyclic
component has boundary k, but contains a five-cycle, so k>=5.
A total boundary at most three therefore forces a singleton W.

If one leaf l has a partial subset, the horizontal cut sum is at most
one. All other leaf fibers agree; complement W so they are empty.
A path to any other leaf shows |A_l|<=1, so A_l is a singleton {j_0}.
There is exactly one horizontal cut edge, all in layer j_0; every
other layer is entirely unselected. The selected component S in that
layer contains l and no other original leaf and has one outgoing edge.

If S contains k original internal vertices, its degree sum in F_h is
3k+1. When S is a tree, it has k internal edges, giving
3k+1=2k+1 and hence k=0. If S is unicyclic, it has k+1 internal edges,
giving 3k+1=2(k+1)+1 and hence k=2. That would make S a three-vertex
unicyclic simple graph, impossible in a graph of girth five.
So S is just l and W again is a singleton.

This proves no one- or two-edge cut, and only trivial three-edge cuts.
Three-vertex-connectivity follows directly. A cut vertex has degree
three and at least two components beyond it; one component would have
edge boundary at most one, which is impossible. If deleting u and v
disconnects the graph, every remaining component has boundary at least
three. Their total is at most six, and at most four when uv is an edge.
There must therefore be exactly two components, uv absent, with three
boundary edges each. Each component must be a singleton because its
complement includes u, v and the other component. A singleton in a simple
cubic graph cannot have three neighbors among only u and v. This rules
out a two-vertex cut.
Consequently cyclic edge-connectivity is at least four.
No claim of ordinary four-edge-connectivity or of a higher exact cyclic
connectivity is being made.

## 6. Arbitrarily distant, arbitrarily many changed labels

Choose h=max(1,R,K), so D=h+1>R and D>K.
Every layer-0 leaf has distance exactly D from V(Q):
projection to F_h cannot shorten the base distance to its central cycle,
and a horizontal branch path attains that distance.

If a total map F keeps all layer-0 leaf pins, every branch-root image
lies in A. Its layer-0 central cycle would map into B[U(A)], which is
bipartite. Therefore EVERY total map changes at least one such leaf.

There is also a full forced path of changes. At least one branch root
must leave its exact message A. At an internal branch vertex its exact
message equals the intersection of the unions of neighborhoods of its
two child messages, as proved in Section 2. Leaving the parent message forces
one child to leave its own message. Descend to a leaf. Every vertex on
this root-to-leaf branch path leaves its prescribed message and hence
differs from f, which always belongs to that message.

The path has D already mapped vertices, at distances 1,...,D from V(Q).
This proves both the radius and edit-count conclusions with the explicit
order bound 25*2^(max(1,R,K)+1). No program or measured search result is
needed for the quantifiers.

## 7. Limits, decision-relevant conclusion, and next action

This is a counterexample family to the EXTRA claim that every exterior
map of a pentagon in this graph class has a bounded-radius or bounded-edit
repair. It is not a counterexample to the graph's five-color existence:
formula (1) explicitly supplies that existence.

The counted edits are target vertex-label changes, not a number of changed
original edge colors. Simultaneous changes are allowed. This is distinct
from frozen full colorings under single-vertex reconfiguration.
The construction can contain other pentagons and does not assert that
the hole is the unique pentagon or that the graph is a minimum obstruction.

An induction may still deliberately construct a globally suitable exterior
map. What fails is obtaining that guarantee solely by a universal bounded
repair of an arbitrary exterior map. C14's exact pin relation and its valid
source reductions remain untouched. The unresolved one-deficiency belt
and all-degree-three pentagon need an actual global state-selection argument,
not an appeal to such a repair bound.

Paper audit: neighborhood-union bipartiteness; exact branch messages with
root 0 attainable; both total and partial global map formulas; all four
rows of the central-cycle table; short-cycle exclusions; the unicyclic
case in (2); and the forced message-violation path.

Sources compared: the repository's C09/C14 pentagon definitions and
the exact C15 candidate at commit 7d278210fe9f751b260b6f5a10584273375a468c,
research/artifacts/candidates/opg434-a01-c15-radius-obstruction.md.
C15 uses one-port attachments and has bridges. The new layer construction
and explicit multi-layer partial map remove that limitation. The required
message and cut proofs are fully included above. No external theorem supplies this construction,
and no novelty is asserted. No truth record, extra packet, remote branch,
PR, verifier receipt, or admission was created.
best_verified_result=none; best_verified_candidate=none.
Both admitted obligations remain open.
