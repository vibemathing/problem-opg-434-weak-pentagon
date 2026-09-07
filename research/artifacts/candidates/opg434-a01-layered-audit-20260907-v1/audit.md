# R09 layered-pentagon family: adversarial paper audit

candidate_id: candidate:opg434-a01-layered-audit-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-proof
verdict: candidate_only
status: NONTERMINAL_CHECKPOINT
base_revision: 08a8bce1a183c8feaa6fe139cc90b0cc58cfac6d

## 0. Frozen input, assurance and first outstanding obligation

Audited input: research/artifacts/candidates/opg434-a01-layered-pentagon-repair-20260907-v1.md
SHA-256: c0e9115a80eb09f692fb3c83a52c8002766219b1154970ad21cc29442a5ba9aa
Git blob: 47194660177840c621a279f8147ac911edbc3e0f
The main file was freshly read. A local text copy was used only after its
computed Git blob matched this main blob, including byte length 14694.
Historical delivery prose inside that file is not present repository state.
C01, C14, C15, C16 and the empty failed-route ledger were freshly read too.

This audit supplies a self-contained paper proof and a hand-derived h=1
negative certificate. The companion program has NOT been run. No generated
100-vertex JSON, enumeration output, measured model count, process exit code,
Lean result or verifier receipt is asserted. The live Web profile has
command_execution=false; the computation skill's scripts/compute_plan.py
was also absent on the frozen main (404). No executable permission is
inferred from channel audit labels or from the user's central-launch premise.
The first outstanding requested check is the actual bounded h=1 replay,
including complete-map checks, certificate replay and mutations. Local
text serialization, hashing and syntax inspection do not discharge it.

## 1. Quantifiers and meaning of repair

Take R,K in the nonnegative integers and h=max(1,R,K). For nonnegative REAL
bounds use h=max(1,ceil(R),ceil(K)); this resolves the unstated integer-height
convention without narrowing the claimed bounds. All vector indices are
modulo five. All graphs are finite, simple and undirected.

The claim concerns a full new map g:V(G)->V(B), allowed to disagree with a
specified map f on old vertices V(G) minus V(Q). It is NOT a literal extension
required to equal f everywhere; phrasing the latter as 'every extension'
could be vacuous. We prove existence of a total map separately, and prove
that EVERY total map has at least h+1 disagreements, one at distance h+1.
The edits count TARGET VERTEX labels, not original edge colors.

## 2. Reconstructed target and the obstructing eight-set

B has all even five-bit vectors. Put t_i=31 XOR (1<<i), so in integer form
(t_0,...,t_4)=(30,29,27,23,15), and p_ij=(1<<i) XOR (1<<j).
Adjacency is x XOR y in {t_0,...,t_4}. Distinct generators are nonzero.
A subset I sums to (|I| mod 2)J + sum_{i in I}e_i; it vanishes exactly for
the empty subset or all five indices. Three generator occurrences cannot
sum to zero: cancellation leaves a subset of odd size at most three.
Thus there is no triangle, including any purported closed three-step walk.

Useful exhaustive adjacency rules are 0~t_i; t_i~p_jk iff i is j or k;
p_ij~p_kl iff the index pairs are disjoint; no generator-generator edges.
The 16 labels consist of 0, five generators and ten pairs, so these rules
cover every label type.

Write U(X) for the UNION of the open neighborhoods of X, not their
intersection. For A={0,p_01},
U(A)={t_0,t_1,t_2,t_3,t_4,p_23,p_24,p_34}.
Its bipartition is the five generators versus the three pair labels.
The generator vertices t_0,t_1 are isolated in this induced graph; the
other six vertices form a six-cycle. In particular it has no odd cycle.
Also, with C={t_0,t_2},
U(C)={0,p_01,p_02,p_03,p_04,p_12,p_23,p_24},
so U(A) intersect U(C)={p_23,p_24}=D. The two elements of D are nonadjacent.

## 3. Exact message lemma, with all attaining assignments

For a rooted binary tree with prescribed leaf labels, let M(v) consist
of ALL labels attained at v by maps of its descendant subtree respecting
those pins. At a leaf M(v) is its singleton pin. At an internal vertex
with disjoint child subtrees,
M(v)=U(M(v0)) intersect U(M(v1)).
Necessity follows from the two child edges. For sufficiency, choose a
neighbor in each child set, then choose each realizing subtree map.
Disjointness makes these choices simultaneous. No other constraints on
these subtree maps are being silently imposed.

Claim: every distinct nonadjacent pair P can be the exact root message
of a full binary tree of EVERY integer height h>=1.
Base h=1: write P={u,u+p_ij}; pin the two children u+t_i,u+t_j. A common
neighbor w gives (w+u+t_i)+(w+u+t_j)=p_ij. The only two ordered generator
pairs summing to p_ij are (t_i,t_j),(t_j,t_i), so exactly u,u+p_ij work.
Both are actual maps of the three-vertex tree.

Induction: assume the assertion for an arbitrary allowed height h and
all such P. Take height-h trees with messages A and C from Section 2.
A new root has exactly D, including attainment, by the exact recurrence.
Translate and permute coordinates to send D to the desired P.
Explicitly, write P={u,u+p_ij}, choose a permutation pi sending 3 to i
and 4 to j, and set alpha(x)=u+pi(x+p_23). Then alpha(p_23)=u and
alpha(p_24)=u+p_ij. Apply alpha to every pin and realizing map.
This proves the step h->h+1 and covers all h>=1, not just test heights.

Fix message A at each of five copies, and choose a realizing map f_a
with root 0. The construction can choose the first valid child label
in a fixed order at each node. Recursion decreases remaining height,
and top-down realization decreases distance to a leaf: both terminate.
The number of tree vertices is 2^(h+1)-1. Each f_a(v) belongs to M(v).

## 4. Source, total map and the complete exterior map

Let T_h be a central five-cycle c_a, with one such binary tree attached
by an edge to c_a for each a. This connected unicyclic graph has
5*2^(h+1) vertices, equally many edges, and 5*2^h leaves. All nonleaves
have degree three and each leaf has degree one. Its unique cycle has length 5.

Take five layers j of T_h. For every original leaf l add the five edges
(l,j)(l,j+1). These are the ONLY interlayer edges. Let G_h be the result,
and Q={ (c_a,0): a=0,...,4 }. The order is 25*2^(h+1); the size is
75*2^h. Degrees are three, edges have different endpoints, duplicate
edge types do not occur, and a leaf fiber connects all layers.

Define z_0=0 and z_j=sum_{k<j}t_k. The z_j form a target pentagon.
Set phi(c_a)=z_a; along every edge away from the central cycle add t_0.
Then Phi(w,j)=phi(w)+z_j is a TOTAL B-map: horizontal differences are
those of phi, and every vertical difference is a generator.

Define q_(a,0)=0, q_(a,j)=sum_{k<j}t_(a+k). At every branch vertex put
f(w,j)=f_a(w)+q_(a,j). All tree and vertical leaf edges are valid.
The root label is q_(a,j). At the central vertices of layers j=1,2,3,4
use respectively
  y_(a,1)=p_(a,a+2), y_(a,2)=p_(a+2,a+4),
  y_(a,3)=p_(a,a+2), y_(a,4)=p_(a+4,a+1).
Within every row consecutive pairs are disjoint, including a=4 to a=0.
Their differences are generators. For j=1,4 the pair y contains the
index of the generator q; for j=2,3 the pair y is disjoint from pair q.
Thus EVERY spoke in the four retained central layers is valid as well.
Every cyclic closing edge a=4 to a=0 and every spoke in all four
retained central layers is included by these modular formulas. No central
vertex of another layer is omitted. The domain of f is exactly V(G_h)\V(Q).

## 5. Girth and the complete small-cut argument

No short cycle is wholly horizontal because T_h has girth five. On a
closed walk with fewer than five steps, the signed vertical displacement
is zero as an integer, hence the number of vertical steps is even.
Four vertical steps in a four-cycle would be inside a single leaf C5,
which has no four-cycle. With two vertical and two horizontal steps,
the projected horizontal walk is a single base edge traversed twice.
If the vertical steps occur at the same endpoint, they immediately
reverse at that leaf fiber and repeat a vertex. Otherwise both endpoints
of the base edge would be leaves, impossible. Two vertical steps and one
horizontal step cannot have a closed base projection. These exhaust
triangles and four-cycles. The central and leaf cycles give girth exactly
five; Q is induced, since its only edges are its five cycle edges.

For any vertex subset W put A_w={j:(w,j) in W}. Partitioning edges into
the two construction types gives the exact identity
|delta(W)| = H+V,
H=sum_{uv in E(T_h)} |A_u symmetric_difference A_v|,
V=sum_{l leaf} |delta_C5(A_l)|.
Every partial leaf set costs at least two in V. Assume W nonempty and
proper with boundary at most three.

Case V=0. Every leaf set is empty or full. Along a base path from an
empty leaf to a full leaf the sum of successive symmetric differences
is at least five. Hence all leaf sets are the same; complement W to
make them empty. Selected components now lie in individual layers and
use only base nonleaves. A tree component of order k has boundary k+2,
because every selected vertex has ambient degree three. A unicyclic
component has boundary k, but includes the base pentagon, so k>=5.
Boundary contributions of disjoint selected components add. Therefore
there is exactly one singleton selected component if the boundary is at
most three. This also excludes a union of several isolated components.

Case V>0. There is exactly one partial leaf fiber l, V=2 and H<=1.
All other leaves are empty or full and cannot have differing constants,
by the same path inequality. Complement W to make them empty. There is
another leaf since h>=1. A path from l to such a leaf gives |A_l|<=H<=1,
so A_l={j0}, H=1. The sole horizontal cut is in layer j0: that layer
contains a selected leaf and an unselected leaf. In every other layer
there is no horizontal cut, so connectedness of T_h and its empty leaf
sets force the entire layer to be unselected. The selected vertices
in layer j0 form ONE connected proper component S, since every proper
selected component in a connected layer has a nonempty boundary and
only one horizontal cut is available.

S contains l and no other original leaf. If it has k nonleaves, its
ambient base degree sum is 3k+1. If S is a tree, its k internal edges
and one exiting edge give 3k+1=2k+1, so k=0. If S is unicyclic, its
k+1 internal edges give 3k+1=2(k+1)+1, so k=2. This would be a simple
unicyclic graph on THREE vertices, contradicting base girth five.
No multicyclic case exists because T_h is unicyclic. Again W is a singleton.

Undo complementation: every cut of size at most three is the boundary
of one vertex or its complement, and its size is exactly three. In
particular there are no one-/two-edge cuts or nontrivial three-edge cuts.

A cut vertex of this cubic graph would leave at least two components,
one sending at most one edge to it, a forbidden small cut. For a two-
vertex cut {u,v}, every remaining component has boundary at least three.
The total is six if uv is absent, four if present. Thus uv is absent
and there are exactly two components with boundary three. Each must
be a singleton: its complement contains u,v and the other component.
But a singleton cannot have three distinct neighbors among only u,v.
Contradiction. The graph has more than three vertices, so it is
three-vertex-connected. No appeal to cubic minimal-counterexample
lemmas or to C16 is needed in this argument.

## 6. The forced path and strict inequalities

At least one layer-0 branch root leaves A in any total map g: otherwise
every central image lies in U(A), mapping Q into a bipartite induced graph.
At an internal branch vertex leaving M(v), at least one child leaves
its own M, by the exact recurrence and the two present edges. Descend
until a leaf. All vertices on this root-to-leaf path disagree with f,
since f(v) is in M(v). Remaining height strictly decreases at each step.

There are h+1 OLD vertices on this path. Their distances to Q are
exactly 1,...,h+1: projection of a G_h walk to T_h collapses vertical
steps and cannot beat base distance, while the horizontal path attains it.
Consequently there are at least h+1>K disagreements, including one at
distance h+1>R. This is a claim about all total maps, not just maps in
a particular reconfiguration component. Phi proves it is nonvacuous.

## 7. A fully specified h=1 control and a short negative certificate

Vertex IDs are id(j,a,k)=20j+4a+k, where j,a=0,...,4 and k=0,1,2,3
means central, root, left leaf, right leaf. Edges are:
- id(j,a,0)--id(j,a+1,0) and id(j,a,0)--id(j,a,1);
- id(j,a,1)--id(j,a,2) and id(j,a,1)--id(j,a,3);
- id(j,a,k)--id(j+1,a,k) for k=2,3.
All a,j arithmetic is modulo five. This defines all 100 vertices and
150 edges with no unspecified choices. Q={0,4,8,12,16}. The exterior
has 95 vertices and 140 edges. These counts are paper-derived expectations.

Take f_a(root)=0, f_a(left)=t_0, f_a(right)=t_1. Use Section 4 for f.
For Phi use z=(0,30,3,24,15): on k=0,2,3 put z_a+z_j and on k=1 put
z_a+t_0+z_j. Thus both complete finite label tables are specified by
bounded formulas, not by a promise of a later graph search.

Fix the ten layer-0 leaf labels. Exact elimination of each two-leaf
branch gives root list A. Eliminating these roots gives central lists
U(A). This is EXACT for the 20-vertex layer-0 core, since the branches
are disjoint and the message lemma includes attainment. Unsatisfiability
of this subgraph is sufficient for the entire 100-vertex problem; no
reverse correspondence with arbitrary constraints in other layers is claimed.

Each central image has a side bit b_a in the bipartition of U(A), and
its two incident central edges require b_a XOR b_(a+1)=1. The companion
JSON supplies the ten 2-CNF clauses and nine resolution steps ending
in the empty clause. This is a hand-derived UNSAT certificate of a
SOUND parity abstraction, with its full graph-to-abstraction bridge
above. It is not mislabeled as a solver-generated proof of a bijective
CNF encoding. Direct enumeration of all 8^5=32768 projected central
tuples is also implemented in the unexecuted control program.

## 8. Mutations, with precise expected outcomes rather than fake runs

M1 Replace t_4 by p_01 but keep t_0,t_1. The mutated target contains
triangle (0,t_0,t_1). It must fail the triangle-free target check.

M2 Omit the central images in layer 1 from f. Five required old vertices
are now unassigned. A domain-exact checker must reject this before it
checks edges. Physically deleting that central layer instead makes its
five branch roots degree two, so that variant is not cubic either.

M3 Release ONLY the pin at id(0,0,2), retaining the other nine layer-0
leaf pins. A genuine full map is now available. On T_1 take central
labels (p_03,t_3,p_23,t_2,p_24), roots (p_12,0,p_01,0,p_01), every left
leaf t_0 except the released one t_2, and every right leaf t_1.
Every listed edge follows the adjacency rules; lifting by +z_j gives
a full G_1 map preserving exactly the nine retained pins. This is a
positive mutation control, not another obstruction assertion.

M4 h=0 is outside the exact TWO-ELEMENT message lemma. A height-zero
tree has one pinned vertex and a singleton feasible message, not A.
Reject the unsupported height in the control constructor. This does
not assert that no useful graph or different theorem exists at height zero.

M5 Delete vertical edge id(0,0,2)--id(1,0,2). Exactly these two endpoints
have degree two. Both old maps remain homomorphisms, since an edge was
deleted; the structural cubic check, not the homomorphism check, must fail.

Additional direction guard: replacing U by COMMON neighborhoods in the
induction gives (N(0) intersect N(p_01)) intersect
(N(t_0) intersect N(t_2))={t_0,t_1} intersect {0,p_02}=empty,
not D. This catches the union/intersection reversal directly.

## 9. Audit disposition and reasoning discipline

The paper audit found no counterexample to the family as formulated
with integer h and with edits of target vertex labels. It explicitly
fills the selected-component and unicyclic steps of the cut proof,
separates real thresholds from integer height, and supplies the one-pin
positive mutation witness. No claim of a new theorem's novelty is made.

Dependencies: target identities -> exact messages -> source maps;
source structure -> girth -> cut identity -> edge/vertex connectivity;
exact messages + bipartite U(A) -> violating root -> forced path;
explicit total map + forced path -> nonvacuous strategy obstruction.
C01 provides definition comparison only. C14 uses existential state
selection, C15 has bridges, and C16 has an unresolved belt frontier.
None is used as an unproved premise of the new connectivity audit.

Invariant: each subtree message is its exact attainable root set.
Monovariant: remaining height in construction and violation descent.
Symmetry: the affine pair transport is explicit and preserves adjacency.
Scale: finite order 25*2^(h+1) is derived, not measured or extrapolated.
Extremal/probability arguments: not used; no minimality or randomness
assumption enters this family. Degenerate h=0 and all five prescribed
mutations are dealt with explicitly at the paper level.

Remaining checks are the actual authorized h=1 run, certificate replay,
mutation run, and the trusted faithfulness/assurance process. The companion
Python source is pending/unverified, and its future results must carry
actual versions, resource limits, exit status and input/output hashes.
best_verified_candidate=none; best_verified_result=none.
The admitted target and original weak-pentagon ProblemContract remain open.
