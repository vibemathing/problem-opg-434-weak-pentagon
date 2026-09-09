# Six-row joint-kernel audit after PR31 exact recovery

candidate_id: candidate:opg434-a01-six-kernel-audit-20260909-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
best_verified_result: none
base_revision: 6e702ed29bbc11072ac3376c1c3300cb9958419d
transaction: existing PR31 / physical-exit packet only

## 1. Recovery and assurance boundary

The three COMPLETE archives at fixed head ca025e6b1138840fce011110f1c06d1a490e9abb
were bounded-decoded and every logical entry hash checked: physical-exit40,
239821 bytes; source-admissibility36,377733 bytes; repaired five-row37,476175
bytes. Total113 files/1093729 bytes. The physical payload text was fetched at
that commit. Source/five payloads reconstructed from the exact supplied ZIPs
matched the current Git blob IDs before bounded decoding. The new integrity
consumer audit_pr31_archives.py repeats the checks without installing or
executing any archived program. Its recorded exit is0. This is transportation
integrity, not another run of the five-row census or trusted verification.

Four unindexed six-row-density fragments were already at that head. They have
no bound index, decoder, report or mathematical claim. They are excluded from
this PR's active diff, with immutable recovery pointers retained in checkpoint.json; this
is not a claim they were decoded or their research completed. No force push
or ref deletion is used. The current candidate is a separately named plain-
text audit, not a reconstruction of those unknown fragments.

The recovered five-row theorem still has its exact historical finite dependency.
None of its old counts is relabeled as a new execution. R11/R12, h1, graph22
censuses and rejected generic replacement searches were not repeated.

## 2. The exact kernel theorem needs 155 choices, not35, for six rows

Let a signed bipartite instance have m>=3 left vertices and any finite right
side. Keep every signed edge equation
 t_ij=h_i+h_j+a_i*b_j+a_j*b_i
in GF(2). Equal parallel equations can be coalesced only for this algebraic
construction, with every physical row checked afterward. Opposite parallel
signs reject immediately. Actual matching-cut quotients have no loops; a
negative loop in a general incidence system is a separate0=1 constraint.

Let E_m be the even subspace of GF(2)^m. For every (m-3)-dimensional subspace
K of E_m impose on ONE common h in GF(2)^m all equations
 u.h = sum_i u_i*t_ij
for every column j and every u in K supported on its neighbor set.

THEOREM. The original instance is feasible iff at least one of these common
systems is feasible. Necessity: the m rows(1,b_i,a_i) have a dependence space
of dimension at least m-3, contained in E_m; select K inside it. Summing
edge equations on each supported dependence gives the common system with
the original h. This includes rank-one and rank-two original row systems.
Sufficiency: K-perpendicular has dimension3 and contains the all-ones vector.
Complete that vector to a basis(1,b,a). Its row dependence space is exactly K.
Fix one common h solution. In each column, every restricted row dependence
has zero right-hand sum; its three-unknown system for(h_j,a_j,b_j) is therefore
consistent. Solve all columns using the SAME previously chosen left values.
Set z=h+ab. Every original equation is satisfied simultaneously.

The number of choices is the Gaussian binomial [m-1 choose2]_2, namely
 ((2^(m-1)-1)*(2^(m-1)-2))/6.
For m=5 this is35 two-dimensional kernels; for m=6 it is155 three-dimensional
kernels. For m>6 even155 is no longer the full domain. Nothing in this count
asserts that a successful kernel always exists for a physical source.

For six rows the155 kernels have a concrete complete classification by the
multiplicities of row points q_i=(a_i,b_i) in GF(2)^2:
  (3,1,1,1):20; (2,2,1,1):45; (4,1,1):15;
  (3,2,1):60; (2,2,2):15.
Any three distinct affine points span the affine plane. Its affine group acts
as all24 permutations of its four points. Thus row partitions using three or
four points give precisely these kernels, with no additional orbit condition.
For physical columns of degree<=4, only supported dependencies of weights2
and4 need be imposed, but they must STILL be jointly consistent in the same h.
Relations between these equations cannot be tested one support at a time.

## 3. A valid source where one natural 35-kernel restriction loses every solution

Vertices are0,...,15. For i modulo8 include edges
 i--(i+1), i--(8+i), (8+i)--(8+i+2 mod8).
Take the cut s=(0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0).
Its four same-side edges are(1,9),(2,10),(5,13),(6,14).
This source is simple, triangle-free and cubic. Actual exhaustive cut checking
finds maximum20 among24 edges, with14 cuts modulo complement. All65536 source
subsets also satisfy the exact MC gain identity and the maximum-cut inequality.
The physical W restriction is checked directly. This is a genuine maximum-cut
fixture, NOT a minimum non-B source and NOT a root counterexample.

The ordered left components are
 [(2,10),(6,14),(4),(11),(15),(0)],
and the right components are
 [(1,9),(5,13),(3),(7),(8),(12)].
They give an actual6+6 quotient. The complete source edge table, every raw
quotient row, and all155 kernel verdicts are in certificate.json.
Exactly14 kernels are feasible and141 are not. Every feasible record includes
a shared h and all right-column solutions; every infeasible record includes
a0=1 linear-combination certificate for its full common system.

Consider specifically the35 kernels containing e0+e5 (mask33), equivalently
forcing q_0=q_5. Columns0 and4 impose respectively
 h_0+h_5=0 and h_0+h_5=1.
Consequently every one of these35 kernels fails. Their count is [4 choose2]_2=35.
This proves that this PARTICULAR attempt to carry a five-row family into six
rows by duplicating a fixed row is incomplete even for an eligible maximum
cut. It does not say every possible collection of35 choices fails, nor does
it disprove the correct155-choice criterion.

An explicit total B-map in vertex order is
 [15,17,10,23,12,17,10,20,24,30,5,0,27,30,5,3].
Here B is the16 even five-bit masks with generator differences30,29,27,23,15.
The columns0,4 contradiction is the negative quotient rectangle which lifts
to the actual source pentagon(2,1,0,8,10). No claim that this pentagon is a
universal reducible patch is made.

## 4. Density audit of the first remaining physical side size

Let the smaller raw quotient side have6 components, r of them paired, and
let the other have k>=6 components, u paired. Counting EACH physical crossing
edge gives18+r=3k+u, so k<=8. Each pair has at most two incidences to pairs
and hence at least two to singletons. P-S parallel incidences are forbidden
by source triangle-freeness.

If k=6 then r=u and2r<=3(6-r), so r<=3. If k=7 then u=r-3; the possibilities
r=5,u=2 and r=6,u=3 are impossible because each right pair requires at least
two distinct left singletons, whereas fewer than two exist. The remaining
possibilities are(r,u)=(3,0),(4,1). If k=8, necessarily(r,u)=(6,0).
The retained sparse-matching theorem handles total pair count<=3. Thus the
UNRESOLVED raw parameter cases with smaller side6 reduce to
 (k,r,u)=(6,2,2),(6,3,3),(7,4,1),(8,6,0),
corresponding to source orders16,18,18,20. These are parameter classes, NOT
an exhaustive graph census and NOT assertions that every class is maximal-cut
realizable. The present source checks only one member of the first class.
Minimum side>=7 remains another open range. No global impossibility of a CC
cover, and no general decreasing equal-maximum exchange, follows from this
arithmetic or from the14 successful kernels of one positive graph.

## 5. Executions and next obligation

There are five fully receipted mathematical executions: producer, checker,
mutations, then checker and mutations again in a directory containing NO
producer. All exit0. A preliminary bounded orientation probe selected this
fixture; it has no detailed receipt and is not used as proof evidence. The
formal producer rebuilds the source, maximum-cut result and complete kernel
certificate from its fixed code.

The producer enumerates kernels by triples in the even vector space and uses
row elimination. The consumer recovers the domain from all4^6 affine point
assignments, uses COLUMN-space elimination, rebuilds the graph by an all-pairs
adjacency predicate and tests target edges through coordinate sets. It checks
all155 records, all336 physical edge instances from positive kernel records,
all65536 source subsets, exact maximum-cut count14 and the35 rejected kernels.
It imports no production module. This is different implementation logic, NOT
a registered trusted domain. No solver, Lean or closure action was used.

Seventeen negative and two positive mutation outcomes match expectations;
replays do not increase the count of distinct mutations. They cover source
edges/loops, cut/F/owner identity, signs/omitted rows, truncated or duplicate
kernels, an odd kernel vector, zero dual, fabricated feasible status, wrong
shared h, invalid/collapsed target labels and false maximum. Positives are
record permutation and a whole-map target translation.

CPython3.13.5; stdlib; deterministic seed0; one CPU; CPU35/36s; wall40s;
address-space512MiB; file1MiB; stream size audited after exit. Declared code
and data read sets are hashed before and after each execution. Receipts and
exact stdout/stderr are preserved separately. The integrity-only archive
consumer has its own CPU10/11s and wall15s receipt; it is not a mathematical
replay. Final file-count/size and input/output digests are in manifest.json.

General EXIT/root, statement-faithfulness and trusted closure remain open.
Next: prove a common kernel exists in all four residual six-side parameter
classes using FULL MC and physical endpoint incidences, or find an eligible
all-kernel-negative SOURCE with a true maximum-cut certificate. Preserve the
entire common-h system, every physical parallel row and all newly formed
cycles in any proposed exchange. Do not substitute35 kernels or separately
feasible five-row projections. best_verified_result=none.
