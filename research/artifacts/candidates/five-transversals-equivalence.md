# Five colour classes and odd-cycle edge transversals

Status: candidate_only. This is a locally prepared mathematical draft, not a registered Candidate, verifier receipt, EvidenceLink, or admitted result. No remote preflight or submission is asserted by this document.

Problem: problem:opg-434-weak-pentagon
Attempt (user-supplied binding, not revalidated here): attempt:web-20260906-opg434-a01
Route (user-supplied binding): route:odd-cycle-transversal-equivalence-v1
Graph (user-supplied binding): graph:opg434-initial-v1
Target: obligation:opg434-five-transversals-equivalence
Root remains outside the conclusion: obligation:opg434-root
ProblemContract SHA-256 supplied by the user: 60124bd981c32b7e5ba91955bbdaa76e2dfebf984722e144a589fceace0f7ba5
Primary method: math-derivation; finite-graph-basic and finite-combinatorics.

## Frozen domain, quantifiers and definitions

The root question quantifies over every finite simple triangle-free cubic graph G, then asks for a map c:E(G)->{1,2,3,4,5}, such that for every label i, the spanning graph H_i=(V(G),E(G)\F_i) is bipartite, where F_i=c^{-1}({i}). Properness and surjectivity of c are not assumed.

The present equivalence is more general: fix any finite simple graph G and any such map c. A set F of edges is an odd-cycle edge transversal when it meets the edge set of every odd cycle of G. A cycle here is a simple cycle. Deleting edges retains all vertices, including resulting isolated vertices.

## Atomic claim A: correspondence of cycles

For any F subset of E(G), and H=(V(G),E(G)\F), the odd cycles of H are exactly the odd cycles C of G with E(C) intersect F empty.

Indeed, a cycle of H has distinct vertices and precisely the same consecutive edges in G, and none of those edges is in F; its length and odd parity do not change. Conversely, a cycle of G avoiding F retains every consecutive edge and every vertex in H. It is therefore the same cycle in H. Whether H contains chords of this cycle is irrelevant: the assertion concerns all simple cycles, not only induced cycles. Isolated vertices produce no additional cycles.

## Atomic claim B: fixed-colour equivalence

For every i in {1,2,3,4,5},

H_i bipartite  iff  for every odd cycle C of G, E(C) intersect F_i is nonempty.

Forward direction. Use the theorem that a graph is bipartite if and only if it contains no odd cycle. If H_i is bipartite and an odd cycle C of G avoided F_i, claim A would put C in H_i, contradicting this theorem.

Reverse direction. Suppose F_i meets every odd cycle of G. If H_i contained an odd cycle D, claim A would make D an odd cycle of G avoiding F_i, a contradiction. Thus H_i contains no odd cycle. By the same bipartite-if-and-only-if-no-odd-cycle theorem, H_i is bipartite.

Both directions use the spanning graph with vertex set V(G), not an induced subgraph obtained by deleting vertices.

## Atomic claim C: five classes and the existence reformulation

The fibres F_1,...,F_5 of a map c are pairwise disjoint and their union is E(G), because each edge has exactly one label. Applying claim B separately to each i gives

(for every i, H_i is bipartite)
iff
(for every i, F_i is an odd-cycle edge transversal).

Conversely, any five labelled pairwise disjoint subsets F_1,...,F_5 whose union is E(G), each meeting every odd cycle, determine the map c(e)=i for the unique containing class. Claim B gives all five bipartite complements. Consequently the existence statements are equivalent for each G, and remain equivalent after quantifying over the frozen class of triangle-free cubic graphs.

Terminological qualification: these are five labelled parts, possibly empty. Under the convention that a partition has only nonempty blocks, the nonempty fibres are a partition into at most five blocks. The frozen colouring definition does not require five nonempty blocks. If G has an odd cycle, however, claim B forces all five classes to be nonempty. If G is bipartite, the empty set is an odd-cycle edge transversal by vacuity. This avoids accidentally adding surjectivity or excluding an empty graph.

## Direct consequences, not a solution of the root existence question

1. In a colouring satisfying the condition, every odd cycle uses every one of the five labels. Therefore its length is at least five.
2. On any 5-cycle, each label occurs at least once on exactly five edges. Hence every label occurs exactly once. This is a necessary consequence, not a construction of a colouring of an arbitrary graph.
3. If G has an odd cycle, all five labels are used. If G is bipartite, every edge-label assignment satisfies the condition, proper or not.
4. A bridge belongs to no cycle. Recolouring a bridge changes no odd-cycle hitting condition and preserves feasibility. The condition can be checked componentwise.
5. The equivalence proof uses neither triangle-freeness nor cubicity. Those assumptions delimit the root question; they are not hidden prerequisites for claims A-C.

## Adversarial boundary checks

### Proper edge colouring is not implied

Take K_{3,3} with parts {a_0,a_1,a_2} and {b_0,b_1,b_2}, and edges a_j b_k for all j,k. It is finite, simple, cubic and triangle-free. Give every edge label 1. Deleting class 1 gives an edgeless spanning graph. Deleting any of classes 2-5 leaves K_{3,3}, which is bipartite by its displayed parts. Thus the required condition holds, although incident edges have the same label and four classes are empty.

### Rainbow 5-cycles alone are insufficient, inside the frozen domain

Let G=C_7 square K_2, with vertices (j,b), j modulo 7 and b in {0,1}. Edges are (j,b)(j+1,b) and (j,0)(j,1). This explicitly gives a finite simple cubic graph.

A closed walk of odd length less than 7 cannot occur: the number of vertical steps is even, since the second coordinate must return to itself. Thus the number h of horizontal steps is odd and h<7. Each horizontal step changes the first coordinate by +1 or -1, so their signed sum is an odd integer of absolute value at most h<7. It cannot be 0, nor any other multiple of 7, contradicting return to the initial first coordinate. In particular the graph has no triangles and no 5-cycles. It has the horizontal 7-cycle with b=0.

Give every edge label 1. The statement that every 5-cycle is rainbow is vacuously true. For label 2 the complement is the entire graph and retains the displayed odd 7-cycle, so the required condition fails. This is a counterexample only to replacing all-odd-cycle constraints by 5-cycle constraints; it is not a counterexample to the root existence question.

### Missing and unnecessary assumptions

Disconnected graphs and isolated vertices cause no problem: bipartitions can be chosen on each connected component, and an isolated vertex can be placed on either side. Edge transversals are not vertex transversals. A class need not be a matching, a minimum transversal, or an inclusion-minimal transversal.

## Self-contained audit of the standard bipartiteness theorem

A bipartition forces the side of a walk to alternate at every step, so a closed cycle has even length. Conversely, take a breadth-first-search spanning tree rooted separately in each connected component of a graph without odd cycles. Put a vertex on the side given by the parity of its tree distance from the root. If some edge uv joined vertices of equal distance parity, the unique tree path from u to v would have positive even length; adjoining uv would give an odd simple cycle. The tree path is unique and its vertices are distinct, and uv cannot be a tree edge because tree-edge depths differ by one. This is a contradiction. Every edge therefore joins opposite sides and the graph is bipartite.

## Reproduction and limitations

A reviewer can audit claims A-C by tracking the two containments in the cycle correspondence and the two uses of the bipartiteness theorem. The two explicit graph examples can be checked directly from their edge definitions. No finite enumeration, solver, theorem prover, or CI execution is reported. No external literature claim is used as a proof dependency; the requested terminology/source comparison remains to be checked against accessible primary sources. This draft does not establish existence of a suitable colouring for every triangle-free cubic graph.

Next mathematical review: statement-faithfulness of the labelled-partition convention and an external review of claims A-C. Next transport action: recover readable live GitHub responses, validate the updated bindings and output schema, reuse the single research Issue, and submit an immutable packet on an allowed branch.
