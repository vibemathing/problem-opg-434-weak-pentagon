# OPG434: exact signatures of two Petersen fragments

Status: candidate_only. Supplemental preparation in the still-unconfirmed c05 transport transaction, not another Web attempt packet, admitted obligation, verification receipt, or root proof. No mathematical execution, exhaustive enumeration, or novelty claim is made. The symbolic counts below are consequences of the displayed proofs. A later packet must freeze the actual retrieved bytes and their digest after transport state is readable.

Binding: problem:opg-434-weak-pentagon / attempt:web-20260906-opg434-a01 / route:odd-cycle-transversal-equivalence-v1 / graph:opg434-initial-v1 / obligation:opg434-five-transversals-equivalence. Root obligation:opg434-root remains open. Primary owner: math-derivation.

Dependencies: the c01 fixed-coloring equivalence and c02 target-model candidate. The positive decoder is elementary: for a homomorphism to the target below, color an edge i when its image difference is s_i; after deleting color i, the ith coordinate flips on every remaining edge and supplies a bipartition. The present statements concern existence of homomorphisms, not preservation of prescribed original edge colors.

## 1. Explicit graphs and elementary target facts

Let H have as vertices the even vectors in F_2^5. Write J for the all-one vector, s_i=J+e_i, and n_ij=e_i+e_j. Adjacency differences are exactly the five s_i. Pair types Z,A,N mean equal, adjacent, and distinct nonadjacent; their difference weights are 0,4,2. Translations by even vectors and coordinate permutations are automorphisms.

H is triangle-free because the sum of two generators is zero or a weight-two vector, never another generator. Two distinct nonadjacent vertices have exactly two common neighbors: translate them to 0,n_ij and the common neighbors are s_i,s_j. Any three pairwise distinct nonadjacent vertices have exactly one common neighbor. After translating the first to zero, the other two differences are distinct two-subsets with a one-element intersection; the generator at that shared coordinate is the unique common neighbor. Translations and coordinate permutations are transitive on ordered independent triples: the two intersecting supports and their ordering can be mapped to any other such pair. Here independent refers only to a vertex-set property, not to any verifier or review status.

Define P explicitly as the graph on the ten two-element subsets of {1,2,3,4,5}, with edges between disjoint subsets. This is the conventional Petersen graph. Each vertex has three neighbors; three pairwise disjoint two-subsets cannot fit in a five-element set, so P is triangle-free. Sending {i,j} to n_ij is a homomorphism into H.

Remove the vertex {4,5} from P. The resulting nine-vertex graph M has vertices x_i,y_i,p_i for i=1,2,3, with edges

x_i y_j for i != j; and x_i p_i, p_i y_i for each i.

Indeed identify x_i={i,4}, y_i={i,5}, and p_i={1,2,3} minus {i}. The x/y vertices have degree three and the p_i have degree two. Thus M is also K_{3,3} with the three edges of one perfect matching replaced by paths of length two.

Finally let D be obtained from M by adding a vertex v and just the two edges v p_1 and v p_2. It is P with the edge v p_3 deleted. Its terminals v,p_3 have degree two and every other vertex has degree three. Both M and D are finite, simple and triangle-free. These definitions, rather than any source name, specify the objects used below.

## 2. All homomorphisms of M: a rigid six-cycle and three binary choices

Claim. Up to a target automorphism, every homomorphism M->H has

x_1=s_1, x_2=s_2, x_3=s_3;
y_1=n_23, y_2=n_13, y_3=n_12;
p_i in {n_i4,n_i5}, independently for i=1,2,3.

Proof. For distinct i,j let k be the third index. The vertices x_i,x_j have the common neighbor y_k, so their images cannot be adjacent in the triangle-free target. They also have a length-three path x_i,p_i,y_i,x_j. A loopless triangle-free graph has no closed walk of length three, so their images cannot coincide. Hence the three x-images are pairwise distinct and nonadjacent. The same argument applies to the y-images.

Each missing pair x_i,y_i has a length-two path through p_i, so its images are not adjacent. They cannot coincide either: if their common image were z, then for j != i the edge y_i x_j would make z adjacent to x_j, contradicting the nonadjacency of the x-images. Thus the six x/y images form an induced six-cycle with exactly the prescribed cross edges.

Use transitivity on ordered independent triples to normalize the x-images to s_1,s_2,s_3. For {i,j,k}={1,2,3}, a common neighbor of s_j,s_k is either 0 or n_jk. The y_i image must be such a common neighbor, but cannot be 0 because it is not adjacent to x_i=s_i. Thus y_i=n_jk.

The difference x_i+y_i is n_45. Its two common neighbors are x_i+s_4=n_i4 and x_i+s_5=n_i5. There are no edges among the p_i, so their choices are independent. Conversely every displayed choice respects all graph edges. This proves the full classification without a search.

Consequences. All nine vertex images are distinct. For i != j, the p_i,p_j images are nonadjacent when their second indices agree, and adjacent when those indices differ. The exact ordered terminal graph on (p_1,p_2,p_3) is therefore either an independent triple I, or a two-edge path P with any one of the three positions as its center. A single edge plus an isolated terminal E is impossible. Equivalently, the ports are distinct and the number of target adjacencies among them is even (zero or two).

The repeated use of the word independent in this graph-theoretic classification means an edgeless vertex set only. All research status remains candidate_only.

## 3. The two-terminal relation of D is universal

A homomorphism of D is a homomorphism of M together with an image for v that is a common neighbor of the p_1,p_2 images.

If the port type is I, there are exactly two such common neighbors. One is also adjacent to p_3, by the unique-common-neighbor property for the independent triple; the other is distinct from and nonadjacent to p_3. Thus the terminal pair (v,p_3) can have types A and N.

If the port graph is a path centered at p_3, the common neighbors of p_1,p_2 are p_3 itself and one other vertex. They give terminal types Z and N. The other common neighbor is not adjacent to p_3, since two adjacent common neighbors together with p_1 would form a triangle.

If the path is centered at p_1 or p_2, then p_1,p_2 are adjacent and have no common neighbor, so this M homomorphism does not extend to D.

Explicit representatives, using the normal form above, remove any existence ambiguity:

| type of (v,p_3) | (p_1,p_2,p_3) | v |
| --- | --- | --- |
| A | (n_14,n_24,n_34) | s_4 |
| N | (n_14,n_24,n_34) | n_35 |
| Z | (n_14,n_24,n_35) | n_35 |

All required differences are generators. Target automorphisms are transitive on ordered pairs of each type, so every prescribed pair of H vertices, not just these representatives, is realizable at the terminals. Thus Sigma(D)=U=Z union A union N.

This explicitly rules out using D as a gadget that forces equal terminal images, or one that forces an edge or a nonedge. It is a transparent two-terminal piece for existence, despite containing odd cycles. It is not a counterexample to the cubic conjecture.

## 4. A reducible configuration in a hypothetical smallest subcubic counterexample

Suppose a triangle-free graph G of maximum degree at most three contains a copy of D whose only connections to the rest of G are one edge from each of its two terminals. The two external endpoints may coincide when this does not violate the stated graph conditions. No internal vertex of D has any additional incident edge.

Every homomorphism of G after deleting the ten vertices of D extends to G. Choose any neighbor in H of each external endpoint image and assign these chosen labels to the corresponding D terminals. Their ordered pair is arbitrary, and the universal terminal relation just proved supplies a homomorphism of all of D. The two added connection edges are then respected. No original edge-color assignment is asserted to remain fixed under the target-model conversion.

Consequently a minimum-order hypothetical counterexample in the class of finite simple triangle-free subcubic graphs cannot contain this configuration: vertex deletion stays in the subcubic class, minimality supplies the outside homomorphism, and the extension contradicts failure. This minimum-order assertion is not silently transferred to a cubic-only minimum-order graph. The c05 completion candidate relates the two existence questions but not their minimum orders.

## 5. Symbolic counts as an audit, not executed enumeration

There are 960 ordered independent triples in H. Every unordered independent triple has exactly one common neighbor, and each of the 16 vertices has five pairwise nonadjacent neighbors, giving 16 times binomial(5,3)=160 unordered triples and then 160 times 6=960 ordered triples.

For each ordered x-triple the y-images in M are forced, and the three p-images have two choices each. Hence M has exactly 960 times 8=7680 homomorphisms to H. For each fixed x-triple, two choices give port type I, and two choices give a path with each specified center. There are therefore 1920 maps of each of the four ordered port types.

For D, only the I maps and the path maps centered at p_3 extend, each in two ways. It follows that D has 7680 homomorphisms: 1920 with terminal type A, 1920 with type Z, and 3840 with type N. There are respectively 80,16,160 ordered target pairs of types A,Z,N, and automorphisms act transitively on each class. Therefore the numbers of D homomorphisms with one fixed ordered terminal pair are 24 for A, 120 for Z, and 24 for N.

Adding the missing edge v p_3 selects exactly the A maps, yielding 1920 homomorphisms P->H. These numbers were derived from the classification and multiplication above; no program, runtime, enumeration output, or verifier receipt is claimed.

## 6. Scope and next audit

Check the two explicit paths used to force the x/y images distinct, the induced-six-cycle argument, all three common-neighbor choices, and ordered rather than unordered counting. Compare any future literature hit against the explicit graphs M,D and homomorphism target, not merely the name Petersen or a proper edge-coloring gadget. The existence decoder gives candidate five-edge assignments; it does not certify an arbitrary supplied coloring or close the admitted target/root. Source novelty review and formal or external verification remain pending. Freeze the selected results only in a correctly bound later packet after exact main/head/check receipts are recovered.
