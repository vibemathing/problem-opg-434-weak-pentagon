# OPG434: general boundary alignment certificates and target rigidity

Status: candidate_only. Supplemental preparation, not a new Web attempt packet, an executed check or a mathematical admission. Actual artifact digest and transport head remain to be confirmed. Primary owner: math-derivation. No novelty claim or source-search success is asserted.

Binding: problem:opg-434-weak-pentagon / attempt:web-20260906-opg434-a01 / route:odd-cycle-transversal-equivalence-v1 / graph:opg434-initial-v1 / obligation:opg434-five-transversals-equivalence. Root obligation:opg434-root remains open.

## 1. Explicit target and all its automorphisms

Let H be the graph on even vectors of F_2^5, with generator set S={s_i=J+e_i:1<=i<=5}. Write n_ij=e_i+e_j. Nonzero vertex differences have weight two or four, corresponding respectively to distinct nonadjacency and adjacency.

Every automorphism is an even translation followed by a permutation of the five coordinates. Translations and coordinate permutations plainly preserve the generator set. Conversely translate the image of zero back to zero. An automorphism fixing zero permutes its five neighbors s_i, so compose with the inverse coordinate permutation and fix all five. The common neighbors of s_i,s_j for i!=j are exactly 0,n_ij. Therefore every n_ij is fixed as well. These are all sixteen vertices, proving the assertion. There are 16 times 5!=1920 automorphisms.

H has no noninjective homomorphism into any loopless triangle-free target. An adjacent pair cannot be identified. For a nonadjacent pair, normalize it to 0,n_12; there is a length-three path

0, s_3, n_34, n_12,

whose three differences are s_3,s_4,s_5. Identifying its endpoints would produce a closed walk of length three, impossible in a loopless triangle-free graph. Also every nonadjacent pair has a common neighbor, so its images cannot become adjacent. Thus every such homomorphism is an induced embedding. In particular every endomorphism of H is one of the automorphisms just classified. This is a graph-theoretic rigidity claim with a displayed proof, not a verifier-status assertion.

## 2. Exact criterion for any number of prescribed ports

Let a_1,...,a_r and b_1,...,b_r be ordered tuples of H vertices. They can be images of boundary vertices under two fixed side homomorphisms. Repetitions are allowed. For r>=1, define d_j=a_j+a_1 and e_j=b_j+b_1, so d_1=e_1=0.

There is an automorphism beta with a_j adjacent beta(b_j) for every j if and only if there are a coordinate permutation pi and an index k such that every

w_j=d_j+pi(e_j)

is either zero or a weight-two vector whose support contains k.

Proof. Write beta(x)=t+pi(x). The first port requires a_1+t+pi(b_1)=s_k for some k, so t=a_1+s_k+pi(b_1). At any other port,

a_j+beta(b_j)=s_k+d_j+pi(e_j)=s_k+w_j.

This is a generator exactly when w_j=0 or w_j=e_k+e_l for some l!=k. Both directions follow, including an explicit beta from a successful certificate.

Equivalently, for each fixed pi reject it if any w_j has weight four. Otherwise intersect the supports of all nonzero w_j. The permutation succeeds precisely when this intersection is nonempty; when all w_j vanish, every k succeeds. At r=0 there are no constraints and the identity suffices.

This is a finite exact search over 120 coordinate permutations and at most five choices for k, rather than an unspecified solver. A direct candidate checker uses at most 600 times r port tests. An implementation can instead compute the support intersection for each permutation. No such implementation has been executed here.

## 3. Bounded positive and negative certificates

A positive certificate consists of pi and k. A checker must verify that pi is a genuine permutation, k lies in [5], every input label is an even five-bit vector, the two tuple lengths agree, and every displayed w_j satisfies the condition. The translation is then reconstructed by the formula above. This certifies alignment of the specified tuples only.

A negative certificate can contain one row for each of the 120 distinct permutations pi. Each row supplies either:

- one port with w_j of weight four; or
- at most three ports whose nonzero weight-two supports have empty intersection.

The second bound is elementary. If two supports are disjoint, they suffice. Otherwise the supports form a pairwise-intersecting family of two-subsets. Choose two distinct supports {a,b},{a,c}. If their common index a is not shared by the whole family, a support avoiding a must be {b,c}. These three already have empty intersection. If there are no two distinct supports, their common two-element support is nonempty and this row cannot be a negative witness.

The checker must recompute these supports from the frozen input tuples, reject duplicate or missing permutation rows, and verify every rejection witness. This proves that none of the 120 permutations has a valid k, hence that no target automorphism aligns the fixed tuples. It is not a certificate that the underlying graph has no homomorphism: the side homomorphisms may be replaced by different ones.

The certificate should bind the exact ordered tuples and side-certificate artifacts by their actual digests when frozen. A list of failing rows detached from its input or missing some permutations is not an exhaustive negative certificate.

## 4. Why four-port information appears

An independent vertex set in H can be translated to include zero. Its remaining vertices are weight-two vectors whose supports pairwise intersect. Such a family is either contained in a star, meaning all supports contain one index, or is the three supports of a triangle {a,b},{a,c},{b,c}.

In the star case the vertex set is contained in a neighborhood

N(s_i)={0} union {n_ij:j!=i},

and has a common neighbor s_i. In the triangle case the four-set {0,n_ab,n_ac,n_bc} has no common neighbor and is maximal. Consequently the maximum independent-set size of H is five; every independent triple has a unique common neighbor, but some independent quadruples have none. Here independent is used solely in its standard graph sense of an edgeless vertex set.

There are sixteen maximal independent five-sets, the neighborhoods. There are forty maximal independent four-sets of the triangle form: sixteen choices of translated base vertex and ten choices of a three-coordinate set, divided by the four possible base vertices of each set. The other eighty independent four-sets are the five four-subsets of each of the sixteen neighborhoods. Four-subsets cannot belong to two distinct neighborhoods because distinct nonadjacent vertices have only two common neighbors and adjacent ones have none. These are symbolic counts from the classification, not enumeration output.

For a FIXED coordinate permutation, the alignment failure is witnessed by at most four ports including the chosen first port. This does NOT establish a four-port criterion when the coordinate permutation is allowed to change separately for every tested subset. The quantifier order is important: one common permutation must work for all ports.

## 5. An additional extension failure for a square with prescribed leaf images

Consider a four-cycle x_1 x_2 x_3 x_4 x_1, with a distinct leaf a_i attached to each x_i. This graph is bipartite and subcubic. Prescribe the leaf labels

(a_1,a_2,a_3,a_4)=(0,n_12,s_5,n_34).

Adjacent leaf positions have distinct labels. Each individual length-three path a_i,x_i,x_{i+1},a_{i+1} can be mapped to H with these endpoints, but the four paths cannot be filled simultaneously.

To prove this, write the spoke differences as x_i+a_i=s_{c_i}. If consecutive leaf labels differ by n_ab, the three generator differences along their length-three path must be the three distinct generators with indices outside {a,b}. Indeed a sum of three generators has weight two only when its three odd-multiplicity indices are distinct; that sum is the complement of their three-element index set. In particular c_i and c_{i+1} must be distinct and both outside {a,b}.

For the prescribed tuple, the four consecutive differences are n_12,n_34,n_12,n_34. Thus at each cycle vertex the spoke index must lie in {3,4,5} intersect {1,2,5}={5}. All c_i are therefore 5, contradicting the required distinctness across any consecutive pair. No extension of those leaf labels exists.

This is a failure of a prescribed boundary certificate, not an uncolorable graph: the square with leaves is bipartite and has many valid assignments. It demonstrates that individually satisfiable short-path constraints must still be checked for simultaneous compatibility. It also does not contradict the path-length-four universal relation, which concerns one internally disjoint path after its endpoints have been fixed.

## 6. Next audit and scope

Review the proof that the displayed automorphisms exhaust all automorphisms, the normalizing translation, the empty-support convention, negative-certificate coverage of all permutations, and the square-spoke parity calculation. Implementing the proposed checker requires a separately admitted bounded runtime with actual input hashes and output receipts. Neither its specification nor these paper proofs close an admitted obligation or establish the universal cubic existence statement. Freeze the selected claims in a new unique packet only after current main, branch head and exact-head transport receipts are readable again.
