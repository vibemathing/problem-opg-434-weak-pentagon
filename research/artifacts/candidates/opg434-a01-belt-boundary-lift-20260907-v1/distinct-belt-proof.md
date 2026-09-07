# Exact distinct-hub belt relation and a two-path replacement

candidate_id: candidate:opg434-a01-distinct-belt-boundary-lift-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
root_obligation: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only

This is a paper proof candidate, not an execution receipt or trusted verification. Counts stated below are logical counts of a proved candidate relation, not claimed observations from unreadable computation replies. No original candidate is overwritten and the Weak Pentagon root remains open.

## 1. Core and boundary statement

The twelve core vertices are v0,v1,v2,v3,v4,A,B,C,D,r,z,t. Edges are the central pentagon, four spokes v0-A,v2-B,v3-C,v4-D, and the six-edge path B-r-C-z-D-t-A. There are fifteen core edges. The ordered boundary ports are A,B,r,z,t, with prescribed external target labels a,b,rho,zeta,tau respectively. Vertex v1 has no external incidence.

Candidate exact relation:

    extension over the twelve-vertex core exists
    if and only if a != tau and b != rho.

All five external labels may otherwise repeat. The actual source outside endpoints may coincide whenever the stated source remains simple and triangle-free. The proof is about fixed boundary constraints; the later smaller-source construction chooses its entire exterior map globally.

## 2. Target facts and notation

The target is the graph on even vectors of F_2^5, with s_i=J+e_i, i=1,...,5, as the five allowed edge differences. Write ij=s_i+s_j. As follows directly from this definition: 0~s_i; s_i~jk exactly when i is in {j,k}; ij~kl exactly when the index pairs are disjoint; and distinct generators are nonadjacent. The graph is loopless and triangle-free, has degree five, and any distinct nonadjacent pair has exactly two common neighbors. Translations and index permutations preserve adjacency.

We use 'nonadjacent' to allow equality. A common-neighbor set of equal vertices has size five; for distinct nonadjacent vertices it has size two. Two distinct members of any one neighborhood are nonadjacent. If two distinct nonadjacent vertices have two common neighbors u,v, then those two common neighbors in turn have precisely the original pair as their common neighbors. Three distinct vertices cannot have two common neighbors, because those two would have at least three common neighbors, contrary to the preceding property.

## 3. A four-pin pentagon lemma with an edgeless first triple

Suppose x0,x1,x2 are pairwise nonadjacent, x0!=x1 and x1!=x2, while x2,x3 are nonadjacent and different. Then a pentagon can be mapped to the target with four consecutive vertex images yi adjacent to xi, i=0,...,3. The fifth vertex has no pin.

Translate x1 to zero and normalize x0=12. Since x2 is nonadjacent to both x0 and zero, it is either 12 or, after a coordinate permutation preserving this normalization, 13. The following table gives a four-vertex target path (y0,y1,y2,y3) respecting the four pins, with endpoints distinct and nonadjacent.

| x2 | x3 representative | y0,y1,y2,y3 |
|---|---|---|
| 12 | 0 | 34,s_3,35,s_5 |
| 12 | s_3 | 34,s_4,45,13 |
| 12 | 13 | 34,s_3,35,24 |
| 13 | 0 | 34,s_4,24,s_2 |
| 13 | s_2 | 34,s_4,45,23 |
| 13 | s_4 | 35,s_5,25,34 |
| 13 | 12 | 34,s_4,24,s_2 |
| 13 | 14 | 34,s_4,24,35 |
| 13 | 23 | 34,s_4,24,s_2 |
| 13 | 34 | 45,s_4,24,15 |

These are complete representatives, not a sample. For x2=12, a distinct nonneighbor x3 is zero, a generator outside {1,2}, or a pair meeting {1,2} in one index; the stabilizer of {1,2} gives the first three rows. For x2=13 the stabilizer fixes indices 1,2,3 and can interchange 4,5. Distinct nonneighbors of 13 have exactly the seven listed orbits: 0; s_2; s_4 or s_5; 12; 14 or 15; 23; 34 or 35.

Every displayed adjacency, pin incidence and endpoint nonadjacency follows by the rules of Section 2. Add any common neighbor of y0,y3 as y4. It cannot equal y1 or y2, because that would make a triangle on three consecutive path vertices; it cannot equal either endpoint because there are no loops. Thus the path closes to the required pentagon. Undo the normalization. No C14 theorem or general pentagon boundary enumeration is assumed here.

## 4. A common-neighbor selection lemma

Let target labels r,t,z,b satisfy: r is nonadjacent to b and z; t is nonadjacent to z; and b!=z. Then one can choose

    B in N(r) intersect N(b),
    C in N(r) intersect N(z),
    D in N(t) intersect N(z),

such that B,C,D are pairwise nonadjacent, B!=C and C!=D. B=D is allowed.

All three displayed lists have at least two entries. Denote them LB,LC,LD. The B-C and C-D nonadjacencies follow automatically from their shared neighbors r and z. We need ensure the two inequalities and B nonadjacent to D.

If r=z, then B,D lie in N(z). Choose C in the five-set N(z) avoiding B,D; all three labels lie in this edgeless neighborhood.

If r=b, choose C in LC and D in LD different from C. Since r is nonadjacent to z and D belongs to N(z), D!=r. At most two members of the five-set N(r) neighbor D. Choose B outside N(D) and different from C.

If t=z, choose C in LC and B in LB different from C. B!=z, since B~r while r is nonadjacent to z. At most two members of N(z) neighbor B. Choose D in N(z) outside N(B) and different from C.

In the remaining case r differs from b,z and t differs from z. LB,LC,LD each have exactly two elements. LB and LC have at most one common element, since r,b,z are distinct and three distinct vertices cannot have two common neighbors. Pick C0 in LC minus LB.

If LD contains a D outside {C0,b}, use that D and set C=C0. Also D!=r because D~z and r is nonadjacent to z. The two elements of LB have exactly r,b as common neighbors; D is neither. Thus at least one B in LB is nonadjacent to D. It differs from C0 since C0 is not in LB.

Otherwise LD={C0,b}. Let C1 be the other member of LC and set C=C1,D=C0. If C1 is not in LB, the same common-neighbor argument chooses B in LB nonadjacent to C0, and it differs from C1.

Finally suppose C1 is in LB. Let B1 be its other member. If B1 were adjacent to C0, it would be a common neighbor of C0 and b. Since LD={C0,b}=N(t) intersect N(z), their two common neighbors are exactly t,z. B1 cannot be z, because B1~r and r is nonadjacent to z. If B1=t, then r,t,C0 form a triangle: B1~r, C0~r by LC, and C0~t by LD. This is impossible. Hence B1 is nonadjacent to C0. Set B=B1. All required conditions hold.

This proves the selection lemma, including coincidences r=b, r=z, t=z, t=r and any other allowed equality. It is a finite graph-theoretic construction, not a measured search result.

## 5. Exact five-boundary relation

Necessity follows from the two disjoint internal edges A-t and B-r. If a=tau, the boundary path a-A-t-tau is a closed three-step target walk; if b=rho, the path b-B-r-rho is one. Both are impossible.

For sufficiency assume a!=tau and b!=rho. Choose

    z in N(zeta) minus {rho,tau,b}.

There are at least two choices, since the target degree is five. Next choose

    r in N(rho) minus (N(b) union N(z)),
    t in N(tau) minus (N(a) union N(z)).

These choices exist. In the first line rho differs from both b and z, so each excluded intersection with the five-set N(rho) has size at most two. At most four entries are removed. The second line is the same calculation using tau!=a,z. These selections give r nonadjacent to b,z and t nonadjacent to a,z. In particular the hypotheses of Section 4 hold, including z!=b.

Use Section 4 to obtain B,C,D. Choose A in N(t) intersect N(a), different from D; this list has at least two members. D,A are nonadjacent because both neighbor t. The ordered four pins (B,C,D,A), at central vertices (v2,v3,v4,v0), now satisfy Section 3: the first three are pairwise nonadjacent, their consecutive values differ, and the last pair D,A is nonadjacent and different. Section 3 supplies the central pentagon, including the unpinned v1.

Every off-cycle edge is satisfied by construction: B-r-C-z-D-t-A, and the five boundary edges to b,rho,zeta,tau,a. The central cycle and four spokes are supplied by Section 3. This checks all fifteen core edges and all five prescribed incidences. Therefore the exact relation is precisely a!=tau and b!=rho.

After translating a to zero, this relation has 15*16*15*16=57600 feasible ordered states among 16^4=65536 normalized states, and 7936 infeasible states. These counts follow from the displayed relation; they are not a claim that any particular execution has completed. Repeated labels are included, not quotiented away.

## 6. Smaller-source replacement with coincident outside endpoints

Let a finite simple triangle-free subcubic graph contain this induced core. Vertex v1 has total degree two; only A,B,r,z,t may have outside edges, at most one each. Allow the four- and five-boundary-edge cases of C16, as well as other missing boundary incidences.

Delete the twelve core vertices. For each of the two pairs of ports (A,t) and (B,r), do the following: if both ports had outside edges, join their actual outside endpoints by a fresh three-edge path with two new internal vertices. If either outside edge was absent, insert no path for that pair. The two new paths have separate fresh interiors.

Within either pair the two outside endpoints are distinct, because equality would make a source triangle with the existing core edge. Endpoints from different pairs may coincide. The number of new incidences at every outside vertex is at most the number of incidences removed from it. Hence degrees remain at most three. The new paths cannot create triangles: their interiors have no other neighbors and each path has distinct ends. An old edge between its endpoints produces a four-cycle, which is allowed in the triangle-free subcubic induction domain. Coinciding endpoints across the two paths do not create loops, parallel edges or triangles.

If m paths were inserted, the new graph has |V(M)|-12+2m vertices, with 0<=m<=2. Thus the vertex count decreases by at least eight. Any map of this smaller graph assigns different labels to the ends of each inserted length-three path. For a missing boundary incidence choose a fictitious label to satisfy its corresponding inequality; each inequality involves a separate pair and the target has sixteen labels. A missing zeta pin can be chosen arbitrarily. Restrict the smaller map to the actual exterior and apply Section 5 to restore the core. No initially given exterior map is required to be preserved or locally repaired.

Therefore the distinct-hub C16(B) block is reducible under the same smaller triangle-free subcubic graph premise. Both its four-edge and five-edge boundary possibilities are covered without assuming distinct exterior endpoints globally.

## 7. Root-facing corollary and remaining frontier

Together with merged-belt-proof.md, this removes both C16 belt topologies from a hypothetical vertex-minimum non-B-mappable triangle-free subcubic graph, when the earlier C06/C12/C14/C16 candidate reductions are used as their explicitly stated dependencies. Combined with the earlier reduction of a pentagon containing two degree-two vertices, the remaining pentagons of that hypothetical minimum must have all five vertices of degree three.

This is not a universal existence proof and supplies no root counterexample. The local patch theorems in Sections 1-6 are self-contained; the broader minimum-counterexample corollary explicitly depends on the earlier paper candidates and still needs their trusted audit. The all-degree-three pentagon boundary and graphs without pentagons remain open. A finite pentagon relation table alone will not settle the set of boundary states globally realizable by an arbitrary exterior.

Invariant: every list used above is an actual neighbor intersection with explicit witnesses. Symmetry: only translations and index permutations are used, with all stabilizer cases listed. Termination: all target selections are over a fixed sixteen-element set; the source induction strictly decreases order by at least eight. No randomness, asymptotic extrapolation, proper edge-coloring assumption, or hidden injectivity condition is used.

Requested checks: verify the ten four-pin rows with a target representation different from the construction; enumerate the normalized five-pin relation with complete witnesses; check those witnesses with a separate edge-only consumer; validate the smaller-source domain and all endpoint coincidences. Executed controls must be read from their real versioned outputs, not inferred from this prose. best_trusted_result=none; root remains open; verdict=candidate_only.
