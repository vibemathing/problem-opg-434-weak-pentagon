# OPG434: exact two-edge gluing preparation

Status: candidate_only. This is a supplemental derivation prepared while the c05 transport transaction remains unconfirmed. It is not a second Web attempt packet, an admitted obligation, a verifier receipt, or a root-existence proof. It must be audited and frozen with a digest before inclusion in a later packet.

Problem: problem:opg-434-weak-pentagon
Attempt: attempt:web-20260906-opg434-a01
Route: route:odd-cycle-transversal-equivalence-v1
Graph: graph:opg434-initial-v1
Target: obligation:opg434-five-transversals-equivalence
Root remains open: obligation:opg434-root
Primary owner: math-derivation

## Dependencies and scope

Use the candidate equivalence and normalization in `research/artifacts/candidates/opg434-a01-c01-equivalence.md` and `research/artifacts/candidates/opg434-a01-c02-normalization.md`. Those arguments relate existence of a legal five-edge assignment to existence of a graph homomorphism into the target below. They do not identify an arbitrary fixed original assignment with a fixed target homomorphism; normalization may recolor edges. The statements here concern homomorphisms and existence, not preservation of prescribed edge colors.

All graphs are finite and simple. A homomorphism may identify nonadjacent vertices. The two pieces below have disjoint vertex sets, with exactly two specified cross edges and no additional cross-edge constraints. Internal degrees and triangle-freeness are not needed for the gluing theorem. No mathematical program or solver has been executed for this preparation.

## Explicit target, avoiding reliance on its name

Let H have vertex set the even-parity vectors in F_2^5. Let J=(1,1,1,1,1), let e_i be the ith unit vector, and put s_i=J+e_i for i in {1,...,5}. Distinct vertices x,y are adjacent exactly when x+y is in S={s_1,...,s_5}. Thus every edge difference has weight four.

Translations by even vectors and permutations of the five coordinates preserve H. These automorphisms are transitive on ordered vertex pairs of each of the following three types:

- Z: equal, difference weight zero;
- A: adjacent, difference weight four;
- N: distinct and nonadjacent, difference weight two.

Indeed translate the first vertex to zero, then permute the support of the difference. These are all possible differences of even five-bit vectors.

The set of sums of two generators is exactly

S+S = {0} union {e_i+e_j : i != j}.

For equal indices the sum is zero. For distinct indices the two copies of J cancel. Conversely each displayed weight-two vector is s_i+s_j. In particular H has no triangle: a sum of two edge differences cannot be a generator.

## Theorem 1: exact compatibility of two fixed side homomorphisms

Let f:A->H and g:B->H be homomorphisms. The terminal lists are (a_1,a_2) in A and (b_1,b_2) in B; repeated terminals within a piece are allowed. Form G by adding the two edges a_1 b_1 and a_2 b_2. For a simple graph these must be distinct edges; this excludes the case in which both terminal lists repeat the same vertex.

There is an automorphism alpha consisting of a translation and a coordinate permutation such that f on A and alpha composed with g on B define a homomorphism G->H if and only if the two terminal-image types are not (Z,A) or (A,Z).

The compatibility table is:

| A-side type / B-side type | Z | A | N |
| --- | --- | --- | --- |
| Z | yes | no | yes |
| A | no | yes | yes |
| N | yes | yes | yes |

Proof. Translate all target labels so f(a_1)=0, and write d=f(a_1)+f(a_2). A permutation of B's coordinate differences changes g(b_1)+g(b_2) to a vector e of the same weight. After a freely chosen translation, the B terminal images can be t and t+e. The two cross edges are respected precisely when t is in S and t+e+d is in S. Equivalently d+e is in S+S.

For Z/Z, A/A and N/N, choose the permutation so e=d, and then choose any t in S. For Z/N or N/Z, d+e has weight two, hence is in S+S. For A/N, permute the support of the weight-two difference to a two-element subset of the support of the weight-four difference; their sum then has weight two. The N/A case is symmetric: arrange that the weight-four support contains the weight-two support. For Z/A or A/Z their sum necessarily has weight four, which is not in S+S. This proves necessity and sufficiency.

The forbidden case also has a direct check. If the A images coincide and the B images are adjacent, their common A image would have to be adjacent to both endpoints of a target edge, producing a triangle in H. The symmetric case is identical.

Boundary tests. A homomorphism need not be injective, so two cross edges may have the same target image; this is why Z/Z is allowed. Repeated terminals simply force type Z on that piece. The claim concerns two cross edges only; more cross edges can impose additional constraints that this table does not encode.

## Theorem 2: exact terminal-signature test for existence

For a graph A with ordered terminals define Sigma(A) to be the subset of {Z,A,N} realized by the terminal images over all homomorphisms A->H. Sigma(A) may be empty. Define Sigma(B) similarly.

For the above two-edge join, G->H exists if and only if there are p in Sigma(A), q in Sigma(B) with a yes entry in the table.

Sufficiency follows by choosing side homomorphisms with these types and applying Theorem 1. For necessity restrict a homomorphism of G to each piece. Its two realized types cannot be a forbidden pair, by the target's triangle-free property or the generator calculation above.

If both signature sets are nonempty, failure of existence is therefore equivalent to exactly one of

Sigma(A)={Z}, Sigma(B)={A};
Sigma(A)={A}, Sigma(B)={Z}.

Proof of this last reduction. Type N is compatible with every type, so neither signature can contain N when all pairs fail. Among Z and A the only forbidden pairs are the unequal ones. If either signature contains both Z and A, then one of its entries equals any chosen entry of the other signature and gives a compatible pair. Hence both signatures are singletons and they must differ.

Crucial limitation: the proof gives the exact shape of a possible separator obstruction. It does not show that terminal signatures of triangle-free subcubic pieces cannot be these opposite singletons. It does not construct such pieces either. A failure for two chosen side homomorphisms does not imply failure for all side homomorphisms.

## Further elementary consequences, conditional on the normalization candidate

One-edge gluing is always possible for two H-colorable pieces: translate one image so its terminal is any neighbor of the other terminal image. Gluing at a single identified vertex is also possible: translate one terminal image to equal the other. Disjoint unions are H-colorable exactly when every component is.

Consider a hypothetical counterexample with the fewest vertices among finite simple triangle-free graphs of maximum degree at most three. This is the subcubic class, not a smallest counterexample restricted only to cubic graphs. Its existence would be equivalent to failure in the cubic class by the c05 completion candidate, but that equivalence does not identify their minimum orders.

Such a smallest subcubic counterexample must be connected, have minimum degree at least two, and have no bridge. Connectivity follows by restricting to a failing component. An isolated vertex can be assigned any target image. A degree-one vertex can be reattached at any neighbor of its neighbor's target image. Deleting a bridge gives two smaller pieces, each colorable by minimality, and the one-edge gluing argument applies.

It also has no cut vertex. In a connected bridgeless graph, every component remaining after deleting a cut vertex must send at least two edges to that vertex; one edge would be a bridge. Two or more such components require degree at least four, contradicting the maximum degree bound three. Minimum degree at least two in a finite simple graph excludes orders one and two, so the graph is 2-vertex-connected.

For a two-edge cut that splits this hypothetical minimal graph into two smaller connected pieces, both signature sets are nonempty by minimality. The separator obstruction must consequently be one of the two opposite-singleton patterns in Theorem 2. This is a restriction on a hypothetical minimal counterexample, not a proof that no counterexample exists.

## Audit and next action

Audit the target-model conversion from c02 and the coordinate permutation construction, especially the distinction between fixed side certificates, all side certificates, and a fixed original five-edge assignment. Check repeated terminals, empty signature sets, and the degree-three cut-vertex argument. Only then freeze this supplemental derivation as a uniquely named candidate in the next cycle from a freshly read main.

Next mathematical test: determine exact terminal signatures for paths, and test whether long degree-two chains force a flexible signature. No signature enumeration, solver run, kernel check, source novelty claim, or EvidenceLink is claimed here.
