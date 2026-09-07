# Exact merged-belt boundary and a liftable path replacement

candidate_id: candidate:opg434-a01-merged-belt-boundary-lift-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
root_obligation: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only

This is a paper proof candidate about an explicitly defined patch. It is not a trusted verifier receipt. The original Weak Pentagon existence question remains open. No assertion about a computation's completion follows from this document. The source topology is C16(A); the proof below supplies its own finite-target lemmas instead of assuming the old boundary-table classification.

## 1. Frozen source and exact relation

The core has vertices v0,v1,v2,v3,v4,A,B,C,D,Y,T. Its fourteen edges are the central cycle vi-v(i+1) (indices modulo five), the spokes v0-A,v2-B,v3-C,v4-D, and Y-B,Y-C,Y-D,D-T,T-A. The four boundary edges join A,B,C,T to external vertices carrying labels a,b,c,d, respectively. These four labels need not be different.

Define R(a,b,c,d) to mean that these prescribed labels extend over the core to a homomorphism into the target defined below.

**Candidate theorem.** For every a,b,c,d in the target,

    R(a,b,c,d) if and only if a != d.

The external vertices are initially formal distinct ports. Identifying external vertices with equal prescribed images does not change the constraint relation, provided the resulting source is in the stated graph domain. In the reduction below the external ends at A and T must be physically distinct, because otherwise A-T and their two boundary edges form a source triangle.

## 2. Target facts proved from its definition

Let Btarget have the even vectors in F_2^5 as vertices. Put J=(1,1,1,1,1), s_i=J+e_i for i=1,...,5, and ij=s_i+s_j for distinct indices. Adjacency means that the difference is one of the five s_i. The labels are 0, the five s_i, and the ten unordered pairs ij.

The elementary rules are: 0 is adjacent to each s_i; generators are pairwise nonadjacent; s_i is adjacent to jk exactly when i is in {j,k}; and ij is adjacent to kl exactly when their pairs are disjoint. The only zero sum of a nonempty subset of generators uses all five. Thus the target is loopless and triangle-free. Translations and permutations of the five indices are automorphisms. Distinct nonadjacent target vertices have exactly two common neighbors: after normalization to 0,ij these are s_i,s_j. Equal vertices have five common neighbors.

### 2a. A flexible ordered target edge

For any distinct external labels a,d, the feasible ordered pairs (u,v) satisfying a~u~v~d contain the alternately oriented edges of a simple six-cycle. Normalize a to zero and d to s_1 or 12. Suitable cycles, starting on the u-side, are

    d=s_1: s_1,12,s_2,0,s_3,13,s_1;
    d=12 : s_3,34,s_4,45,s_5,35,s_3.

The u-side is adjacent to zero and the v-side to d in both rows. All six vertices are distinct and every displayed edge follows from the rules above. Undo the normalization. Each forbidden target vertex excludes at most two of the six cycle edges, so some feasible edge avoids any given two target vertices.

For a fixed target edge bc, call another edge compatible when its ends avoid b,c and at least one cross adjacency exists. Every simple target cycle has a compatible edge. Indeed, a cycle vertex outside {b,c} adjacent to an endpoint has a cycle neighbor outside that pair, since it cannot neighbor both endpoints in a triangle-free graph. This supplies a compatible cycle edge. A cycle meeting b or c also supplies such an outside neighbor. The only remaining case would put the cycle entirely among the common nonneighbors of b,c, excluding b,c themselves. Normalize bc to 0-s_5: that induced graph is the six pairs on {1,2,3,4}, with only complementary pairs adjacent, namely 3K2. It has no cycle.

Consequently the feasible six-cycle contains an ordered (u,v) avoiding b,c, and, when b~c, it can be chosen compatible with bc. Orientation always follows the fixed alternating u/v sides; no arbitrary endpoint swap is used.

### 2b. The neighborhood exclusion test

Suppose u~v and u,v avoid b,c. Set

    L = N(u) minus (N(b) union N(c) union {v}).

If L is empty, normalize u=0. Each of N(0) intersect N(b) and N(0) intersect N(c) has at most two elements because b,c differ from zero. Covering the five generators using these two intersections and the singleton {v} requires two disjoint two-element intersections and the remaining fifth generator v. Hence b=ij and c=kl for four different indices, and v=s_m for the fifth. The four vertices induce exactly the two edges uv and bc, with no cross edge. Conversely that configuration does cover N(u).

Thus L is nonempty whenever b,c are nonadjacent, or whenever uv was chosen compatible with edge bc. Repeated b=c is covered: a repeated two-element intersection cannot cover five elements together with a singleton.

### 2c. A pentagon with all pins in one neighborhood

Suppose five target pins x_i lie in N(q) and consecutive pins differ. There is a target pentagon y_i with y_i~x_i for all i. Translate q to zero and write x_i=s_{a_i}. We need two-element index sets P_i containing a_i and disjoint at consecutive positions.

Every index occurs at most twice in the proper cyclic word a_0,...,a_4. Up to cyclic reflection/rotation and index renaming the only multiplicity types are the following. Lowercase letters in each row denote distinct indices; letters unused by the pin word fill out the five indices.

    pin word (a,b,c,d,e): pairs (ac,bd,ce,da,eb);
    pin word (a,b,a,c,d): pairs (ac,be,ad,cb,de);
    pin word (a,b,a,b,c): pairs (ae,bc,ad,be,dc).

Every required index is present and every consecutive pair, including the closing pair, is disjoint. These rows cover all proper length-five cyclic words: multiplicities can only be 1+1+1+1+1, 2+1+1+1, or 2+2+1; each repeated index occurs in nonconsecutive positions. The resulting pair labels give the required target pentagon. Undo the translation.

## 3. Constructive proof of the exact relation

Necessity: if a=d, the boundary path a-A-T-d would be a closed three-step walk in a loopless triangle-free target, impossible.

For sufficiency assume a!=d. Use Section 2a to choose u,v with a~u~v~d, avoiding b,c, and compatible with bc when b~c. Section 2b supplies

    q in N(u) minus (N(b) union N(c) union {v}).

The distinct vertices q,v both neighbor u and hence are nonadjacent. Their two common neighbors are u and another vertex w; in particular w!=u. Assign A=u,T=v,D=w,Y=q.

Since q is nonadjacent to c (equality permitted), N(q) intersect N(c) has at least two elements. Choose C in that intersection different from w. Similarly choose B in N(q) intersect N(b), different from C. All of A,B,C,D now lie in N(q), with A!=D, D!=C and C!=B. Choose a fictitious pin x_1 in N(q) different from A and B. Then the five pins (A,x_1,B,C,D) lie in one neighborhood and are unequal consecutively. Section 2c supplies the central pentagon with all five prescribed incidences. The fictitious pin only adds an optional constraint at v1; the actual patch has no edge to it.

All core edges have been checked: the central cycle and four spokes by Section 2c, Y-B/Y-C/Y-D by the choices, D-T from the common-neighbor pair, and T-A from the initial flexible edge. The four actual boundary edges follow from a~u, B~b, C~c and v~d. This proves sufficiency for every ordered quadruple, with repeated labels retained.

The proof is finite and constructive. Target normalization, choosing a six-cycle edge, choosing neighbors, and one of the three pair rows all have fixed finite search bounds. No probabilistic or asymptotic argument is used.

## 4. A genuine smaller-graph replacement, allowing global rechoice

Let M be finite, simple, triangle-free and subcubic. Suppose it contains the specified induced eleven-vertex core, with v1 of total degree two and exactly the four boundary edges at A,B,C,T. Let their actual external endpoints be alpha,beta,gamma,delta. They can coincide except that alpha!=delta: otherwise alpha-A-T-alpha is a triangle.

Delete the core and insert two fresh vertices p,q and the path alpha-p-q-delta. Call the resulting graph M'. It has exactly |V(M)|-9 vertices. It is simple and triangle-free: the new internal vertices have no edges beyond this three-edge path, and its endpoints are distinct. An old alpha-delta edge would produce a four-cycle, not a triangle. Degrees stay at most three. At each old vertex, the number of new incidences is no greater than the number of removed boundary incidences; coincidences among beta,gamma and the path endpoints therefore cause no degree problem.

Every homomorphism M'->Btarget assigns different labels to alpha and delta, since the new path has length three and the target has no closed three-step walk. Restrict the map to M minus the core. Section 3 extends that map over the core. Thus

    M' maps to Btarget  implies  M maps to Btarget.

This implication concerns a freely chosen map of the smaller graph. It does not promise a bounded repair of every initially given exterior map. It is consequently not contradicted by the layered-pentagon family.

In a vertex-minimum non-Btarget-mappable triangle-free subcubic graph, if such a graph exists, M' maps by minimality. The implication is a contradiction. Therefore the merged-hub C16(A) configuration cannot occur in that hypothetical minimum. Minimality is over the entire subcubic domain, not just cubic graphs; the original existence question and this minimum-order device are not conflated.

## 5. Explicit remaining root obligation and negative knowledge

This eliminates one of the two C16 belt topologies, not every pentagon and not the Weak Pentagon root. The remaining C16(B) block has twelve vertices and five potential boundary ports (x0,x2,r,z,t); outside endpoints can coincide and four or five edges may leave. A proposed exact relation for that block must be tested and proved separately. The present theorem supplies no such relation and makes no assertion about an unobserved computation of it.

The uniformly local/bounded-edit repair rule for arbitrary exterior maps is an excluded auxiliary strategy at candidate level, witnessed by the previously stored positive layered family. The route still allowed is to choose a whole exterior map through a smaller valid graph, as done here. Only a trusted importer can append a failed-route truth record; none is written by this file.

Audit dependencies: target definition -> six-cycle flexibility and exclusion test; target definition -> three explicit common-neighborhood pentagon rows; these -> exact four-port relation; exact relation + source path replacement -> conditional merged-belt reducibility. The only decreasing parameter in the source reduction is vertex count, by nine. General root closure, trusted statement-faithfulness, formalization and trusted admission remain open.

Reproduction: enumerate all 4096 normalized quadruples with a=0, checking a complete core map for each of the 3840 cases d!=0 and the explicit closed-three-walk obstruction for the other 256. A certificate consumer need only check the fourteen listed core edges, four boundary edges, domain, coverage and target Hamming-distance-four adjacency. Translation then covers all ordered quadruples. These are requested checks, not execution receipts stated by this document.
