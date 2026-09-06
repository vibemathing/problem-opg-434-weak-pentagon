# OPG434: a fully specified finite coloring benchmark

Status: candidate_only. This is a paper-derived benchmark prepared during the unconfirmed c05 transport transaction. It is not an executed solver result, verification receipt, additional Web packet, or solution of the universal cubic problem. Content hashing, source comparison and later packet registration are pending readable transport state. No novelty claim is made.

Binding: problem:opg-434-weak-pentagon / attempt:web-20260906-opg434-a01 / route:odd-cycle-transversal-equivalence-v1 / graph:opg434-initial-v1 / obligation:opg434-five-transversals-equivalence. Root remains open. Primary owner: math-derivation.

Dependencies: c01 equivalence; c02 cut normalization and target model; the supplemental exact Petersen-fragment classification. All graphs and maps below are explicitly defined. Five color names are labeled, and arbitrary edge assignments are considered before any properness is derived.

## 1. The graph and an explicit legal assignment

Let P have the ten two-subsets of [5] as vertices, with disjoint pairs adjacent. Every vertex has three neighbors, so P is cubic with 15 edges. Three pairwise disjoint two-subsets cannot fit in [5], so it is triangle-free. It is connected: intersecting distinct two-subsets have their complementary two-subset as a common neighbor.

For adjacent A,B, their union has four elements. Color AB by the unique element i outside A union B. This is a proper assignment: for a fixed A, its three neighboring pairs leave three different elements of [5] minus A unused. Each color occurs three times, corresponding to the three partitions of [5] minus {i} into two unordered pairs.

After deleting color i, every remaining edge has i in exactly one of its two endpoint subsets. Membership of i is thus an explicit bipartition. This verifies the fixed assignment by direct inspection of the definition, with no appeal to a solver or to properness as an assumption.

## 2. Twelve pentagons, and a minimum transversal size of three

Every vertex belongs to exactly six 5-cycles. It suffices, by permutations of [5], to consider the vertex {1,2}, whose neighbors are {3,4},{3,5},{4,5}. Choose an unordered pair of these neighbors. For the pair {3,4},{3,5}, the two length-three paths between them avoiding {1,2} are

{3,4}, {1,5}, {2,4}, {3,5};
{3,4}, {2,5}, {1,4}, {3,5}.

There are no others: the first inner vertex is {1,5} or {2,5}, the second is {1,4} or {2,4}, and disjointness permits exactly the two displayed choices. The other two unordered neighbor pairs are equivalent under coordinate permutations. Each path together with the two edges through {1,2} gives one 5-cycle, so there are 3 times 2=6 through that vertex.

Counting vertex-cycle incidences gives 10 times 6 divided by 5=12 pentagons. Permutations of [5] are transitive on edges. Counting edge-cycle incidences then gives 12 times 5 divided by 15=4 pentagons through each edge.

An odd-cycle edge transversal must meet all twelve pentagons; two edges can meet at most eight of them. Hence every such transversal has size at least three. The displayed color classes have size three and are transversals, so tau_e(P)=3. Equivalently MaxCut(P)=12, using tau_e=|E|-MaxCut. This is a counting proof, not an observed computation.

## 3. Every legal five-edge assignment on P is proper and normalized

Let c be any assignment satisfying the frozen deletion condition. Each color fiber is an edge transversal by c01, so each has size at least three. Since their disjoint union has 15 edges, all five fibers have size exactly three and are minimum transversals.

A minimum transversal F is a complete-cut complement. Choose a bipartition of P-F and let D be the complete cut in P associated with it. Then E minus F is contained in D. Strict containment would make E minus D a smaller transversal, contradicting minimality. Thus F=E minus D, and D is a maximum cut.

In a cubic graph, a maximum cut has at least two crossing edges at every vertex: flipping a vertex with at most one crossing incident edge would increase the cut size by 3 minus twice that number. Its complement is therefore a matching. All five color fibers of c are consequently matchings. Properness is derived for this graph; it was not part of the contract and must not be imposed on arbitrary input graphs.

## 4. Exact number of legal labeled colorings: 120

Use H, the even five-bit target with edge differences s_i=J+e_i. The Petersen-fragment preparation proves that P has exactly 1920 homomorphisms to H: removing one vertex gives the nine-vertex fragment M, its ordered terminal triple must be of type I in order to restore the deleted vertex, there are 1920 such maps of M, and each has one common-neighbor extension.

For completeness, that number does not arise from a program. An ordered independent triple in H can be chosen in 16 times binomial(5,3) times 6=960 ways, since every such triple has exactly one common neighbor. In the normal form of M, the six degree-three vertex labels are forced by this choice, and its three degree-two labels are n_i4 or n_i5. Exactly the two uniform choices give an independent terminal triple. Restoring the vertex gives 960 times 2=1920 maps of P.

Every legal c on P is normalized by section 3. Its five cut bipartitions give five-bit labels for which an edge of color i has difference s_i. Label parity is constant over the connected graph because each s_i has even weight; a global flip of one coordinate if necessary makes all labels even. Thus every legal c is obtained from a homomorphism to H.

For a fixed c, fixing the label of one vertex determines all other labels by the edge equations. Existence was just shown, and any of the 16 even labels at that vertex is possible by a global translation. Hence precisely 16 homomorphisms induce each c, and there are 1920 divided by 16=120 legal labeled edge assignments.

The explicit coloring in section 1 uses all five colors. Its 5!=120 global color permutations are distinct and legal. Therefore these are ALL legal assignments on this fixed labeled graph P. This exact classification is a candidate theorem with a displayed finite proof, not a claim of formal verification.

## 5. Why a C5 vertex homomorphism is a different condition

P has no homomorphism to any triangle-free graph with fewer than ten vertices, in particular none to C5. To see this, consider distinct vertices A,B of P. If adjacent, they cannot be identified by a homomorphism into a loopless graph. If nonadjacent, a permutation reduces them to A={1,2}, B={1,3}. They have a length-three path

{1,2}, {3,4}, {2,5}, {1,3}.

Identifying the endpoints under a homomorphism would create a closed walk of length three in the target, impossible for a loopless triangle-free graph. Hence every such homomorphism is injective. Moreover, nonadjacent pairs in P have a common neighbor, so their images cannot become adjacent in a triangle-free target. Such a homomorphism is an induced embedding.

Thus a legal five-edge assignment, even a proper one, cannot be replaced by a C5 vertex-homomorphism requirement. This example has girth five and does not address any separate conjecture restricted to sufficiently large girth. A literature comparison must retain those quantifiers rather than infer a statement from the word pentagon.

## 6. Expected finite-model counts for a later exact checker

These are predicted audit values, NOT outputs from a run. They apply only to the labeled graph P just defined and to encodings without added symmetry-breaking constraints.

- Legal five-edge assignments: 120.
- Homomorphisms to the 16-vertex target H: 1920.
- Homomorphisms P->C5: 0.
- Models of the c03 five-bipartition encoding: 3840, provided all vertex and one-hot edge variables are counted and no extra free variables are introduced.

For the last count, under the explicit coloring, deleting color i leaves the subdivision of K4: the four two-subsets containing i are its degree-three branch vertices, and the other six vertices give the unique subdividing vertex for each pair of branches. It is connected and bipartite, so exactly two bit assignments are its bipartitions. All legal colorings are global permutations of this one. Consequently each c has 2^5=32 choices of its five bipartition vectors, and the total is 120 times 32=3840.

The same argument predicts 1920 models for the c03 four-bit target encoding when its edge auxiliary variables are uniquely fixed by endpoint labels. Any checker must confirm its actual encoding and variable convention before comparing counts. A discrepancy is an encoding or candidate-audit question, not automatically a counterexample to the universal statement.

## 7. Review boundary

Audit the six pentagons through one vertex, edge transitivity, the minimum-transversal argument, the use of even five-bit parity, and whether a model count includes bipartition flips. Confirm the exact source/definition of any software encoding before execution. No commands, installed versions, stdout, solver model counts, verification receipts, or EvidenceLinks are reported. Both admitted obligations remain open pending their prescribed verification and admission gates.
