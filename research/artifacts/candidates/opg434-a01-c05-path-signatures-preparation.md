# OPG434: path signatures and two-terminal series-parallel preparation

Status: candidate_only. Supplemental preparation during the unconfirmed c05 transport transaction, not a second packet or an admitted new obligation. No mathematical execution or verifier receipt is claimed. These statements need a subsequent frozen candidate, digest, and audit.

Problem: problem:opg-434-weak-pentagon. Attempt: attempt:web-20260906-opg434-a01. Route: route:odd-cycle-transversal-equivalence-v1. Graph: graph:opg434-initial-v1. Target: obligation:opg434-five-transversals-equivalence. Root obligation:opg434-root stays open. Primary owner: math-derivation.

Dependencies: c01 equivalence and c02 normalization at `research/artifacts/candidates/opg434-a01-c01-equivalence.md` and `research/artifacts/candidates/opg434-a01-c02-normalization.md`. The target is explicitly defined here, so no graph-name identification is required. This is an existence interface, not a transformation preserving prescribed original edge colors. No novelty claim is made; a literature comparison of this restricted-class result remains pending.

## 1. Target and signature convention

Let H have the even vectors of F_2^5 as vertices, and let S={s_i=J+e_i : 1<=i<=5}, where J is the all-one vector. Adjacency means that the difference is in S. Write Z for the diagonal relation, A for adjacency, N for distinct nonadjacency, and U=Z union A union N for the universal relation. Their vector differences have weights zero, four, and two, respectively. Even translations and coordinate permutations act transitively on ordered pairs of each type.

A terminal relation of a graph with two ordered terminals records ALL target-image pairs extendible to a homomorphism of the graph, not one chosen pair or one chosen edge coloring. By the displayed automorphisms it is a union of types. Distinct graph terminals may have equal images.

## 2. Exact relation of a path

For a path of length l (l edges), its endpoint relation R_l is:

| l | R_l |
| --- | --- |
| 0 | Z |
| 1 | A |
| 2 | Z union N |
| 3 | A union N |
| every l>=4 | U |

The l=0 entry describes the identity walk, not a graph with two distinct terminals and no edge.

Proof. A homomorphic image of a path is a walk; endpoints differ by a sum of l generators. A generator used an even number of times cancels. If T is the set of generators with odd multiplicity, the difference is (|T| mod 2)J + sum_{i in T} e_i, where |T|<=l and |T| has the parity of l. The possible weights for |T|=0,1,2,3,4,5 are respectively 0,4,2,2,4,0. Every such set T of the permitted size can be realized, padding by two repeated occurrences of any generator. Coordinate symmetry realizes every vector of the indicated weight, not just one representative.

For an explicit check of l=4: zero is obtained by s_i+s_i+s_j+s_j; a weight-two vector e_i+e_j by s_i+s_j+s_k+s_k; and s_i by the sum of the other four generators, because the sum of all five generators is zero. Thus R_4=U. If R_l=U, then R_{l+1}=U as well: for any required endpoint y choose one of its neighbors w and take an l-step walk from the starting vertex to w, followed by w-y. H has five neighbors at every vertex. This proves all l>=4 without an enumeration.

Attacks: a length-two path cannot join adjacent images since that would create a target triangle; a length-three path cannot have equal images since it would give an odd closed walk of length three in a loopless triangle-free target. Length four is therefore the first unrestricted length. A target walk is allowed to repeat vertices: imposing injectivity here would be a different problem.

## 3. Threads and a hypothetical minimal subcubic counterexample

A thread has a sequence v_0,...,v_l with pairwise distinct internal vertices, every internal vertex of degree two in the whole graph, and no internal vertex equal to an endpoint. Endpoints may coincide only in the explicitly closed-thread case; there are no extra edges incident with internal vertices. If l>=4, any homomorphism of the graph after deletion of the internal vertices extends across the thread by R_l=U. This also covers equal prescribed endpoint images and closed threads.

Consequently a smallest-order hypothetical counterexample among finite simple triangle-free graphs of maximum degree at most three has no such thread of length at least four. Its smaller vertex-deleted graph is in the same subcubic class, so minimality supplies a homomorphism, which the path relation extends. This argument must NOT be applied directly to minimum order within the cubic-only class: deleting vertices does not preserve degree three.

For a graph obtained by replacing the edges of a skeleton with internally disjoint paths, homomorphism existence is exactly the simultaneous satisfaction of the appropriate R_l at skeleton endpoints. Internal paths can be filled separately once endpoint images are fixed. Length one requires A, length two requires Z union N, length three requires A union N (inequality), and length at least four imposes no endpoint restriction. Parallel skeleton edges are separate paths and impose intersected relations. The original graph must still satisfy the stipulated simplicity/triangle-free conditions; suppression does not make those conditions automatic for a multigraph skeleton.

## 4. Elementary relation algebra

Relational composition is denoted by a circle: (x,z) is in P circle Q when some y has (x,y) in P and (y,z) in Q. Direct calculation gives

A circle A = Z union N;
A circle N = N circle A = A union N;
N circle N = U.

The first identity follows from S+S={0} union {e_i+e_j:i!=j}. For the second, equality is impossible because a difference cannot have both weights two and four. If z-x=s_i, choose the first step s_j with j!=i; the remaining difference is e_i+e_j of weight two. If z-x=e_i+e_j, choose a first step s_k with k outside {i,j}; the remaining difference has weight two. These give every allowed A or N pair.

For N circle N, translate x to zero. If z=0, choose any weight-two y. If z=e_i+e_j, choose y=e_i+e_k with k distinct from i,j, leaving y+z=e_j+e_k. If z has weight four, partition its four-element support into two pairs; choose y to be one pair, leaving the other pair for y+z. These cover all pairs.

Let B=Z union N and C=A union N. For the five nonempty relations A,N,B,C,U, all compositions are U except

A circle A = B;
A circle N = N circle A = C;
A circle B = B circle A = C.

This follows by distributing composition over unions, with Z the identity and with every relation in the list having nonempty fibers at every vertex. In particular U composed on either side with any listed nonempty relation is U. Intersections stay in {A,N,B,C,U,empty}. The only intersections of two listed nonempty relations that are empty are A intersect N and A intersect B, in either order. These are finite symbolic identities, not reported solver output.

## 5. A restricted-class theorem with a constructive signature proof

Define two-terminal series-parallel graphs recursively from one edge with distinct terminals. Series composition identifies the second terminal of one piece with the first terminal of another and leaves all other vertices disjoint. Parallel composition identifies the corresponding two terminals and otherwise keeps the interiors disjoint. Work with the underlying simple graph if duplicate terminal edges are produced. Final terminals remain distinct. No assertion about equivalence to any broader minor-closed graph class is needed here.

Claim: every triangle-free graph so obtained has a homomorphism to H. Its terminal relation belongs to {A,N,B,C,U}; in particular it can never be the singleton equality relation Z.

Proof by induction on an expression for the construction, carrying two witness invariants whenever the terminal relation is nonempty:

(1) If the relation is A, the graph contains the edge between its terminals.
(2) If the relation is B or N, the graph contains a two-edge path between its terminals.

The edge has relation A and satisfies (1). In series composition, independently choosing and then gluing homomorphisms gives exactly relational composition, since the pieces share only the joined vertex. The above table yields a nonempty relation. The only output B is A circle A; both pieces then have their terminal edges by (1), which together give the required two-edge path through the joining vertex. Series composition never outputs A or N. Hence both invariants persist.

In parallel composition the relation is the intersection, since side homomorphisms agree precisely on the two fixed terminal images and the interiors are disjoint. If the intersection is A, at least one input is A, supplying the actual terminal edge. If the intersection is B, an input is B. If the intersection is N, either an input is N, or the inputs include B and C. Thus in the latter two cases an input B or N supplies an actual terminal two-edge path, proving (2).

The intersection cannot be empty in a triangle-free final graph. The only empty cases pair A with B or N. By the two invariants, the union would then contain both the terminal edge and a terminal two-edge path, hence a triangle. Every recursive piece is a subgraph of the final triangle-free graph, so the induction applies at every node. This proves the claim and the witness invariants.

This supplies a constructive procedure from a given series/parallel expression: compute relation types bottom-up by the displayed tables, then choose compatible intermediate labels top-down using the explicit composition witnesses. It is a paper procedure; no implementation, execution count, performance benchmark, or verification receipt is claimed.

Connection to the two-edge-separator preparation: a colorable piece expressible in this two-terminal series-parallel sense cannot force the type {Z} at distinct terminals. If both sides have such expressions, neither opposite-singleton obstruction ({Z},{A}) can occur, so their two-edge join is H-colorable. One series-parallel side alone does NOT remove all obstructions: it could force {A} while the other side forces {Z}.

## 6. Limits and next review

These are restricted-class and separator statements, not the universal cubic existence claim. A literature search must compare exact domains before attaching a known theorem name or claiming novelty. Inspect the definition of two-terminal composition, whether terminal pairs represent walks rather than injective paths, the relation/witness induction, and the subcubic minimum-order scope. Neither target nor root obligation is closed by this preparation. Freeze and register only through a new correctly bound candidate packet after transport recovers.
