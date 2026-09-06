# OPG434: sharp domain and properness boundary preparation

Status: candidate_only. Supplemental preparation, not a second c05 Web packet, not a verifier receipt, and not a counterexample to the frozen cubic problem. No mathematical program has been executed. A new packet, exact digest and source-faithfulness review are still required before registering these supplemental claims. No novelty claim is made.

Problem: problem:opg-434-weak-pentagon. Attempt: attempt:web-20260906-opg434-a01. Route: route:odd-cycle-transversal-equivalence-v1. Graph: graph:opg434-initial-v1. Target: obligation:opg434-five-transversals-equivalence. Root obligation:opg434-root remains open. Primary owner: math-derivation.

Dependencies: the fixed-coloring equivalence in `research/artifacts/candidates/opg434-a01-c01-equivalence.md`, and the existence/normalization/target-model candidate in `research/artifacts/candidates/opg434-a01-c02-normalization.md`. Edge deletion and vertex deletion are different parameters throughout this note.

## A. Properness cannot be carried through cut normalization

Let G=K_{3,3}, with partite sets {l_0,l_1,l_2} and {r_0,r_1,r_2}. It is finite, simple, triangle-free and cubic. The assignment c(l_i r_j)=1+((i+j) mod 3) is proper. To use all five colors as well, change l_0 r_0 to color 4 and l_1 r_1 to color 5. Properness remains true because the two new colors occur on single edges. Every assignment on this bipartite graph satisfies the frozen deletion condition: deleting edges cannot introduce an odd cycle.

Nevertheless no assignment on K_{3,3} can simultaneously be proper and have every color class equal to a complement of a complete cut. Suppose it could. Write E=delta(L) for the original bipartition cut. If a color class F is E minus delta(U), then F=delta(L) symmetric-difference delta(U)=delta(L symmetric-difference U), a complete cut. A proper color class is a matching. At least one class is nonempty, so this would give a nonempty complete cut that is a matching.

There is no such matching cut. If M is any matching of K_{3,3}, every left vertex has at least two neighbors after deletion of M. Any two left vertices then share a right neighbor because two two-element subsets of a three-element set intersect. Thus all left vertices lie in one component. Every right vertex still has at least two neighbors and joins that component. Hence K_{3,3}-M is connected. Deleting a nonempty complete cut would disconnect the graph, a contradiction.

This is a fixed-domain counterexample to the extra proper-normalization requirement, not to the frozen problem. It shows more than that one normalization procedure may destroy properness: no proper normalized assignment exists for this G at all.

## B. Positive candidate theorem: vertex odd-cycle transversal at most two

Claim. Every finite simple triangle-free graph G for which deleting at most two vertices leaves a bipartite graph has a homomorphism to the even-five-bit target H, and consequently admits the frozen type of five-edge assignment by the c02 existence equivalence. No maximum-degree assumption is needed for this restricted-class theorem.

Define H explicitly: vertices are the even vectors in F_2^5; s_i=J+e_i for the all-one vector J; adjacency differences are s_1,...,s_5. Write n_ij=e_i+e_j. The displayed labels below are even vectors.

For one deleted vertex w, a still stronger direct construction maps G to C_5. Let (L,R) bipartition G-w. Map w to 0, N(w) intersect L to 1, R minus N(w) to 2, L minus N(w) to 3, and N(w) intersect R to 4, with residues modulo 5. Triangle-freeness forbids edges between the two neighbor classes. Every other possible edge goes between consecutive displayed classes, so this is a homomorphism to C_5. Empty classes and disconnected components are allowed.

For two deleted vertices u,v, choose a bipartition (L,R) of G-{u,v}. For T a subset of {u,v}, write L_T and R_T for vertices in that part whose neighbors among {u,v} are exactly T. An edge between L_T and R_U can occur only if T and U are disjoint; otherwise that edge and a common special neighbor form a triangle.

### Case 1: u,v are not adjacent

Assign all vertices of each class the following label:

| vertex/class | target label |
| --- | --- |
| u | 0 |
| v | n_12 |
| L_empty | n_23 |
| R_empty | n_14 |
| L_{u} | s_4 |
| R_{u} | s_3 |
| L_{v} | n_35 |
| R_{v} | n_45 |
| L_{u,v} | s_1 |
| R_{u,v} | s_2 |

Every possible special-vertex incidence is respected. For u its four neighboring class labels are generators. For v the differences to L_v,R_v,L_uv,R_uv are respectively s_4,s_3,s_2,s_1.

There are exactly nine possible disjoint-subset cross-class pairs. In the order

(L_empty,R_empty), (L_empty,R_u), (L_empty,R_v), (L_empty,R_uv),
(L_u,R_empty), (L_v,R_empty), (L_uv,R_empty),
(L_u,R_v), (L_v,R_u),

the target differences are respectively

s_5, s_2, s_1, s_3, s_1, s_2, s_4, s_5, s_5.

These are direct vector identities. No other cross-class pair can be an edge of G. Identifications within a class are permitted in a graph homomorphism.

### Case 2: u,v are adjacent

No vertex can be adjacent to both, so the uv-neighbor classes are empty. Use

| vertex/class | target label |
| --- | --- |
| u | 0 |
| v | s_5 |
| L_empty | n_23 |
| R_empty | n_14 |
| L_u | s_1 |
| R_u | s_2 |
| L_v | n_25 |
| R_v | n_15 |

The special edge has difference s_5. The incidences from u to its classes have differences s_1,s_2; those from v to its classes have differences s_2,s_1. The seven permitted cross-class pairs, in order

(L_empty,R_empty), (L_empty,R_u), (L_empty,R_v),
(L_u,R_empty), (L_v,R_empty), (L_u,R_v), (L_v,R_u),

have differences s_5,s_3,s_4,s_4,s_3,s_5,s_5. Again these list all possibilities, proving the homomorphism claim. Cases with fewer than two vertices in a transversal were handled separately or are already bipartite.

Important scope: this concerns a VERTEX odd-cycle transversal of size at most two, not an edge transversal of size at most two. It is a restricted-class existence theorem and does not say every triangle-free cubic graph has such a vertex set.

## C. A 13-vertex out-of-domain obstruction

Construct X from K_5 with branch vertices p,q,a_1,a_2,a_3. Keep the six p-a_i and q-a_i edges unsubdivided. Replace p-q, a_1-a_2, a_1-a_3 and a_2-a_3 by internally vertex-disjoint paths of length three, using two new vertices per replaced edge. No other edges occur.

Then X has 13 vertices and 18 edges. Its five branch vertices have degree four and its eight subdivision vertices have degree two. It is therefore NOT cubic and NOT subcubic. The c05 completion theorem for maximum degree at most three does not apply to it.

X is triangle-free: its unsubdivided edges form K_{2,3}; every other branch-to-branch edge uses a length-three path, whose internal degree-two vertices cannot lie on a triangle. Its ordinary girth is FOUR, not five, because p-a_1-q-a_2-p is a 4-cycle. Its odd girth is five: the path replacing p-q together with p-a_i-q gives a 5-cycle, and there are no triangles.

### Direct five-cycle contradiction

Suppose a five-edge assignment on X satisfied the deletion condition. By c01 every 5-cycle would be rainbow. Let the colors on the three edges of the p-q path be A,B,C. Each cycle formed by that path and p-a_i-q is a 5-cycle, so A,B,C are distinct, and the two edges p-a_i and a_i-q receive the same remaining pair of colors D,E, in some order, for every i.

There are three indices i but only two choices for the color on p-a_i. Choose distinct i,j with c(p-a_i)=c(p-a_j). The two edges p-a_i, a_j-p together with the length-three path replacing a_i-a_j form another 5-cycle. Its two equal-colored edges contradict the rainbow requirement. Thus X has no such five-edge assignment.

This contradiction rejects the strengthened claim with maximum degree FOUR, or the unrestricted triangle-free claim; it is not a counterexample to the frozen cubic statement. No failed-route record about the admitted equivalence route should be inferred from it.

### Independent-in-method arithmetic check, not a verification-status claim

Let tau_e(X) be the minimum number of edges whose deletion makes X bipartite. By the elementary bipartite/odd-cycle equivalence, tau_e(X)=|E(X)|-MaxCut(X).

For any bipartition of X, consider the five branch-vertex sides. Among the ten unordered branch pairs at most floor(25/4)=6 are separated; at least four pairs are on the same side. Every branch-to-branch path has odd length. For each same-side branch pair its path must contain at least one noncrossing edge. These ten paths are edge-disjoint, so there are at least four noncrossing edges and the cut has size at most 18-4=14.

Conversely partition the branch vertices into sets of sizes two and three. On every odd-length branch path with separated endpoints assign internal sides alternately, obtaining no noncrossing edge; for same-side endpoints alternate except for one consecutive equal-side pair, obtaining exactly one. The internal paths are disjoint, so these choices are simultaneous. There are four same-side branch pairs. This gives a cut of size 14, proving MaxCut(X)=14 and tau_e(X)=4 as a paper derivation.

Five disjoint edge transversals would therefore require at least 5*4=20 edges, more than the actual 18. This supplies a second concise argument for the same out-of-domain obstruction. It is not an executed computation, external review, or verifier receipt.

### Exact vertex-deletion parameter

Deleting a_1,a_2,a_3 leaves the p-q path and the three disjoint edges formed by the interiors of the other subdivided paths. Hence the vertex odd-cycle-transversal number tau_v(X) is at most three.

Deleting any two vertices cannot suffice. If t of the deleted vertices are branch vertices, the remaining intact branch skeleton contains K_{5-t} with at most 2-t edges destroyed by deletion of internal vertices. For t=2 it contains K_3; for t=1, K_4 minus at most one edge still contains a triangle; for t=0, K_5 minus at most two edges still contains a triangle. One direct check of the last case is that each edge lies in three of the ten triangles, so two removed edges hit at most six. The surviving skeleton triangle lifts to an odd cycle because every constituent path has odd length and is intact. Deleting zero or one vertex is covered by enlarging the deletion set to two. Thus tau_v(X)=3.

Consequently the threshold two in part B cannot simply be replaced by three for all triangle-free graphs. This sharpness statement is still about the larger degree-unrestricted class, not about the cubic problem.

X is also 3-vertex-colorable: give p,q color 0 and all a_i color 1. On a length-three path with equally colored endpoints use the other two colors on the internal vertices in order. Its odd 5-cycle shows that two vertex colors do not suffice. Ordinary vertex 3-colorability therefore does not imply the frozen five-edge property in the larger class.

## D. A conditional properness consequence from the edge parameter

For any graph with a legal five-edge assignment, each color class has size at least tau_e(G), so 5*tau_e(G)<=|E(G)|. If equality holds, every class is a minimum edge transversal. A minimum edge transversal F is the complement of a maximum complete cut: choose a bipartition after deleting F, whose crossing-edge set contains E minus F; strict containment would give a smaller transversal.

In a cubic graph a maximum cut has at least two crossing edges at each vertex, because flipping a vertex with zero or one crossing incident edge would strictly increase the cut. Its complement is consequently a matching. Under the EXTRA equality hypothesis 5*tau_e(G)=|E(G)|, every legal five-edge assignment on a cubic graph is therefore proper and normalized. This does not contradict part A, since K_{3,3} has tau_e=0 and does not satisfy that equality.

## Review and continuation

Check the two explicit homomorphism tables edge by edge, the distinction tau_v versus tau_e, all odd/even path arguments, and the actual degree FOUR and ordinary girth FOUR of X. The direct rainbow proof only rules out the stated larger-domain strengthening. Do not relabel it as a root counterexample, apply the subcubic completion to X, or claim that a prior-art search or these paper arguments close an obligation. Freeze only after recovering exact transport state and obtaining a new candidate digest and correct packet binding.
