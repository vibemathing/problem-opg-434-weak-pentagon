# OPG434 parameter frontier through order 20

candidate_id: candidate:opg434-a01-parameter-frontier-20260909-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
verdict: candidate_only
best_verified_result: none

Let G be a finite simple triangle-free cubic graph, and let s be a maximum cut. Let F be the same-side edges. Maximum-cut singleton flips imply F is a matching. Contract components of (V(G),F). Let the quotient bipartition have component counts m<=k, with r paired components on the m-side and u paired components on the k-side.

The physical source satisfies

    |V(G)| = m+k+r+u,      |F|=r+u,      3m+r = 3k+u.       (DEG)

Singleton quotient components have physical crossing degree 3 and pairs degree 4. In a simple triangle-free source there are no parallel S-S or P-S quotient edges. For a maximum cut, the retained MC consequence Delta(C[W])<=1 holds on endpoints W of F.

## Six-by-six deduplication

For m=k=6, (DEG) gives r=u. The physical endpoint restriction gives r<=3. The audited class-(6,3,3) cut-improvement theorem excludes r=3 by an explicit source flip of cut gain +1. Hence every genuine 6+6 maximum cut has r=u<=2. This is exactly the claimed S13 conclusion, so it is not a new independent dependency. Cases r<=1 have |F|<=2 and are covered by the <=3-matching theorem; r=2 is the complete class-(6,2,2) candidate. Thus no 6+6 maximum cut survives as a candidate non-B source.

## S07 boundary

For m=k=7, (DEG) gives r=u. The condition |F|=4 is exactly r=u=2 and |V(G)|=18. No fixed S07 artifact, manifest, complete 155-kernel certificate, or MC receipt was found in the fresh main, Issue #3, failed-route ledger, or available local integration inputs. This candidate therefore does not silently admit that specialist conclusion. If such a fixed certificate is later hash-checked, it removes precisely (m,k,r,u)=(7,7,2,2).

## Parameter frontier theorem through order 20

Assume G has no B-homomorphism. Use the retained candidates: quotient side <=5 implies a B-map; |F|<=3 implies a B-map; class (6,6,3,3) cannot be maximum; class (6,6,2,2) is B-mappable.

For m=6, write u=18+r-3k.
- k=6 is already eliminated as above.
- k=7 gives u=r-3. r=3 has |F|=3. If r>=5, then u>0 but a paired component on the k-side needs at least two distinct singleton neighbours on the m-side, while m-r<=1; impossible. The only unresolved tuple is (6,7,4,1).
- k=8 gives u=r-6 and 0<=r<=6, hence only (6,8,6,0).
- k>=9 gives u<0.

For m=7 and |V(G)|<=20:
- k=7 gives r=u and |V(G)|=14+2r. r<=1 has |F|<=2; r=2 is exactly the unverified S07 7+7/F=4 class at order18; r=3 gives the order20 class (7,7,3,3).
- k=8 gives u=r-3 and |V(G)|=12+2r. r=3 has |F|=3; the only unresolved order<=20 case is (7,8,4,1).
- k>=9 and u>=0 force r>=6, hence |V(G)|>=22.

For m=8 and |V(G)|<=20:
- k=8 gives r=u and |V(G)|=16+2r. r<=1 has |F|<=2; the only unresolved order20 case is (8,8,2,2).
- k=9 gives u=r-3 and |V(G)|=14+2r. The only order<=20 possibility is r=3, hence |F|=3, already covered. Larger k exceed the order bound.

For m>=9 and |V(G)|<=20, m+k>=18. If |F|>=4 then |V(G)|=m+k+|F|>=22; otherwise the <=3-matching theorem applies.

Therefore, without importing S07, the repository-audited frontier through order20 is:
- order18: (6,7,4,1), (7,7,2,2);
- order20: (6,8,6,0), (7,7,3,3), (7,8,4,1), (8,8,2,2).

Conditional only on a future fixed-byte validation of S07, the order18 tuple (7,7,2,2) disappears. Then the first non-excluded class is

    (m,k,r,u)=(6,7,4,1),

or shorthand (k,r,u)=(7,4,1) when m=6 is fixed. The order20 frontier is exactly (6,8,6,0), (7,7,3,3), (7,8,4,1), (8,8,2,2); the last three are the three order20 classes with minimum quotient side at least seven.

No remaining class is asserted empty or B-mappable. No finite kernel result is extrapolated. General EXIT, root, statement-faithfulness and trusted closure remain open.
