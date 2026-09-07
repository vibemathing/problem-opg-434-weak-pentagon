# Further candidate audit and equivalent formulations

verdict: candidate_only
Transport: local preparation only; no successful remote preflight, registered candidate, PR, check, or merge is asserted.
Target: obligation:opg434-five-transversals-equivalence
The root obligation is not closed by any claim below.

## A. A nonbipartite cubic example with a feasible nonproper colouring

Take the pentagonal prism C_5 square K_2. Its vertices are (j,b) with j modulo 5 and b in {0,1}. Give each horizontal edge (j,b)(j+1,b) colour j+1, and every vertical edge (j,0)(j,1) colour 1. This graph is simple, cubic and triangle-free and contains a horizontal 5-cycle, hence is not bipartite.

For i=2,3,4,5, deleting colour i removes the same one horizontal link in each layer. The remaining graph is P_5 square K_2, a ladder: along the resulting path coordinate t=0,...,4, the parity of t+b gives a bipartition. For i=1, deleting its class removes one horizontal link from each layer and all vertical edges. The result is two copies of P_5, also bipartite. This is therefore a feasible five-label colouring.

It is not proper: at vertex (0,0), the horizontal edge to (1,0) and the vertical edge to (0,1) both have colour 1. This separates the frozen condition from proper edge colouring even when odd cycles exist and all five labels occur.

## B. Checking only induced odd cycles of the original graph is unsound

Use the heptagonal prism G=C_7 square K_2. Let C be the following 9-cycle, with its first vertex repeated only to display closure:

(0,0), (0,1), (1,1), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (0,0).

Every consecutive pair is an edge of the displayed prism, and the nine vertices before closure are distinct. The original edge (0,0)(1,0) is a chord of C. Define F=E(G)\E(C).

Any cycle avoiding F lies entirely in the graph consisting of the nine cycle edges E(C) and the other isolated vertices. The only simple cycle in that graph is C itself. Since C has a chord in G, it is not an induced cycle of G. Hence every induced odd cycle of the original G meets F, yet G-F contains the odd cycle C and is not bipartite.

G lies in the frozen class: it is finite, simple and cubic; no triangle is possible in the Cartesian prism over C_7, as also follows from the signed-horizontal-step argument in the main draft. This is a counterexample to the proposed single-class shortcut, not a counterexample to the root existence question. Checking induced odd cycles of the CURRENT complement H_i would be a different statement; the mistake is using only cycles induced in the ORIGINAL G.

## C. Packing and bipartite-cover formulations

For any finite simple G, the following three existence statements are equivalent, permitting empty labelled sets:

(P) There is a partition into five labelled odd-cycle edge transversals F_1,...,F_5.
(Q) There are five pairwise edge-disjoint odd-cycle edge transversals T_1,...,T_5, not necessarily covering E(G).
(R) There are five bipartite spanning subgraphs B_1,...,B_5 such that every edge of G belongs to at least four of them.

P implies Q by taking T_i=F_i. Q implies P by distributing every unassigned edge in E(G)\(T_1 union ... union T_5) to any one labelled class. Adding edges to a hitting set cannot destroy its intersection with any odd cycle. The resulting sets are disjoint, cover E(G), and remain transversals.

Q implies R: take B_i=(V(G),E(G)\T_i). The main equivalence proves B_i bipartite. Pairwise disjointness of the T_i says each edge is omitted from at most one B_i.

R implies Q: set T_i=E(G)\E(B_i). Bipartiteness and the main equivalence make each T_i a transversal. Membership of every edge in at least four B_i says it is in at most one T_i; therefore the T_i are pairwise disjoint. This closes the equivalence without requiring a common bipartition for all B_i.

In particular, feasibility can be described as a fivefold bipartite spanning cover of edge multiplicity at least four. This is an equivalent reformulation, not a proof that such a cover exists on every graph in the root domain.

## D. A necessary size bound, with its scope retained

Let tau_e(G) be the minimum size of an odd-cycle EDGE transversal. Under P, every F_i has size at least tau_e(G), and their sizes sum to m=|E(G)|. Therefore 5*tau_e(G)<=m. Equivalently some deletion yielding a bipartite spanning graph removes at most floor(m/5) edges. For a cubic graph with n vertices, m=3n/2, yielding tau_e(G)<=floor(3n/10).

This is a necessary consequence of the partition, not a replacement for the packing requirement. In general graphs the bound alone is insufficient: take the disjoint union of a triangle and two isolated edges. Then m=5 and tau_e=1, but every transversal must meet the three edges of the triangle, so five pairwise disjoint transversals cannot exist. This latter example is OUTSIDE the triangle-free cubic domain; no converse failure within that domain is claimed.

## Review status

All arguments above are proposed finite combinatorial derivations. No computation, external review, source match, or formal checker execution is reported. Precise primary-source comparison to named pentagon conjectures remains pending. The heptagonal-prism witness in B is suitable for a future regression test of algorithms that incorrectly enumerate only original induced odd cycles.
