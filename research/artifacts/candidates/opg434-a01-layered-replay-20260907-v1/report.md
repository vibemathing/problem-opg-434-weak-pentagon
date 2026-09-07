# Layered family: actual h=1 replay and full-graph certificate

candidate_id: candidate:opg434-a01-layered-replay-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-proof
verdict: candidate_only
status: RESULT_CANDIDATE_READY / layered-family-audited
base_revision: bc0d53de15bb21236483b4d671dda376309c8177

## 1. Frozen claim and assurance boundary

For integers R,K >= 0 let h=max(1,R,K). The frozen family has
25*2^(h+1) vertices, an induced pentagon Q, a total map to the explicit
16-vertex target B, and a map f on exactly V(G) minus V(Q). Every new total
map differs from f along a layer-0 root-to-leaf path of h+1 OLD vertices;
its last vertex is at distance h+1 from Q. Thus both strict bounds hold.
For real bounds use h=max(1,ceil(R),ceil(K)). Edits are target VERTEX labels,
not original edge colors. Total maps exist; this is not a vacuous statement
about literal extensions which must agree with all of f.

This package closes the previous candidate's missing actual h=1 control.
It does not close the weak-pentagon existence ProblemContract, confer
trusted-verifier status, or create an EvidenceLink/Result/Solution.
No novelty claim is made. PR #26's six files and the original family are
unchanged. The current user's explicit bounded-replay request authorized
these local candidate checks in the supplied CPython runtime. The Web
profile remains unchanged, including command_execution=false: no claim
is made that its transport lane acquired trusted execution authority.
The previously missing compute-plan script is not fabricated or bypassed
as a registered verifier; these small integer/set checks use one CPU.

## 2. Actual runs

All four runs used CPython 3.13.5, standard library only, deterministic
seed convention 0, one CPU affinity and one child, 512 MiB address-space
limit, CPU soft/hard limits 35/36 seconds, and outer wall limit 43 seconds.
The unchanged original additionally enforces its own 40-second alarm.
Per-file/stdout/stderr limits are 1 MiB and aggregate retained-output
limit is 4 MiB per supervised run. No timeout or UNKNOWN is counted as pass.

| Run | Actual exit | Wall seconds | Child user seconds | Child max RSS KiB |
|---|---:|---:|---:|---:|
| unchanged PR26 control | 0 | 1.880595 | 1.629887 | 96436 |
| alternate subset/CSP implementation | 0 | 1.730709 | 1.520451 | 94648 |
| CSP certificate plus full-graph CNF/DRUP check | 0 | 1.412495 | 1.184153 | 105944 |
| separate DIMACS/DRUP file replay | 0 | 1.378605 | 1.221543 | 99256 |

These measurements are from the local supervising process, not GitHub
Actions. All stderr files are empty. Exact commands, CPython build, input
and output bytes/SHA-256, stdout/stderr hashes, CPU/system times and limits
are in the four process_receipt.json files preserved losslessly in
outputs.bundle.json. The codec and unpack_outputs.py verify every raw hash.
There are 26 raw files totaling 382703 bytes. The whole DIMACS file, not
only its hash, is retained in the lossless bundle. No raw host path,
credential, session data, chat transcript, or hidden reasoning is stored.

## 3. Rebuilt finite objects and observed results

The unchanged code matched frozen SHA-256
c6410cfc72d4df236bcb508fec6f43624deda9bf3bc85730580ec64763a08022.
The source family and parity input also matched their fresh-main Git blobs
and SHA-256 values; no historical delivery label was treated as state.

The alternate program imports neither the original generator nor its
checker. It defines B as even subsets of a five-element set, adjacency by
symmetric-difference cardinality four; source edges are selected by a
predicate on all unordered source pairs. Its complete graph, hole, total
map, partial map and pins equal the original generated JSON exactly.

Observed: B has 16 vertices and 40 edges, G has 100 vertices and 150 edges,
Q={0,4,8,12,16}, f has 95 vertices and 140 edges, and the full witness has
all 100 vertices. Both maps and all ten specified pins were checked edge
by edge. Both implementations find girth 5. All 100 one-vertex and 4950
two-vertex deletions remain connected. The original enumerates every pair
of deleted edges (11175 pairs), checks residual bridges, and obtains
exactly the 100 trivial three-edge cuts. This covers every three-edge cut:
without a smaller cut, its third edge is a residual bridge after removing
the other two. The alternate also checks the cut identity on 5244 explicit
subsets, including singletons, pairs, whole layers, central pentagons and
partial leaf fibers. Those subset controls alone are not a universal proof.

The original tests all 80 distinct nonadjacent target pairs at heights
1,2,3: 240 exact messages, both attaining root values in every case.
All 32768 projected central tuples are rejected. The actual generated
100-vertex graph/map JSON has SHA-256
da03b19074756fdab7583a5d3429e3abfbf4428d3b7abed414c0f606d1cad03d.

## 4. Two non-circular pin-obstruction certificates

### Full source, with no appeal to the parity abstraction

The alternate exhaustive CSP starts every one of 100 vertices with all
16 target labels, imposing exactly the ten leaf pins. A recorded value
removal is justified by one actual neighboring source vertex having no
remaining support. It branches over EVERY remaining value of the selected
variable. The complete search has 7 nodes, 706 value removals and 6
contradiction leaves. This is exhaustive search with sound pruning, not
a claim to visit 16^100 complete assignments individually.

check_certificates.py independently checks every deletion against the
actual 150-edge graph and reconstructed target, every branch's exact
coverage and every empty-domain leaf. A missing branch is rejected.

The full graph is also encoded by 1600 Boolean variables X_(v,label).
Exactly-one constraints are one 16-literal clause plus 120 binary clauses
per vertex. For each directed source edge u-v and each label x, use
NOT X_(u,x) OR the disjunction of X_(v,y) over target neighbors y of x.
Add the ten actual pin units. This gives 16910 clauses. With exactly one
label per source vertex these edge clauses are equivalent to a graph
homomorphism; there is no symmetry-breaking assumption or omitted layer.

The saved DRUP proof adds the sixteen negative units excluding every
label at source vertex 0, then the empty clause: 17 additions. Each is
RUP-checked against the actual full-source CNF. A separate program reads
back the DIMACS and DRUP BYTES, reconstructs the encoding directly from
the graph, and replays all steps using a different unit-propagation
implementation. Both replays passed; no external solver is claimed.
CNF SHA-256: a2e123c04d85ce38b0080908034c01e6bbe024d61e21015357fe0c23c680cd04
DRUP SHA-256: 8115f71a53335f6c63d8230e8fbfd602c440ab6a35ee79328eca47bc3e7a2a22

### Original ten-clause parity certificate, with the source bridge

The alternate checker extracts each root and its two pinned children
from the ACTUAL source adjacency. It verifies disjointness, all 20 core
vertices/edges, exact root sets {0,3}, and every attainable central label
with a specific compatible root witness. It reconstructs the side map on
U({0,3}), checks all its edges cross sides, and associates each of the ten
clauses to a present original central-cycle edge. Every one of nine
resolution steps is checked, additionally against all 32 Boolean truth
assignments. Changing an original pin while keeping the abstract parity
proof unchanged is rejected at the source-to-core bridge. Soundness is
full graph -> its pinned 20-vertex subgraph -> exact root elimination ->
parity abstraction; the abstraction is not claimed to encode the other
four layers bijectively.

## 5. Thirteen actual mutations

M1: replace one generator by p01; triangle 0,29,30 is exposed.
M2: omit five layer-1 central labels; exact-domain validation rejects.
M3: release leaf pin 2; the explicit total map preserves all other nine
pins, changes pin 2, and satisfies all 150 edges (positive control).
M4: h=0 is rejected by the constructor; its singleton pinned message is
not the two-element message required by the h>=1 lemma.
M5: delete vertical edge 2-22; exactly these two degrees drop to two,
while both maps remain valid on the edge-deleted graph.
M6: replace UNION by COMMON neighborhoods; the correct message {12,20}
becomes empty, losing its attaining values.
M7: replace closing leaf edge 2-82 by chord 2-42; cubicity fails and
actual edges exhibit triangle 2-22-42-2.
M8: swap label layers 1 and 2 without relabeling the source; an actual
vertical edge fails the homomorphism check. A simultaneous graph/map
isomorphism is not being called an error.
M9: compute distance from vertex 0 instead of the whole Q; comparison
with the correct multi-source distances rejects the substituted metric.
M10: omit the total-map witness; the nonvacuity check rejects the package.
M11: mutate pin 2 from 30 to 27 but retain the parity certificate; the
source bridge no longer gives the claimed A and rejects.
M12: omit a full CSP-proof branch; branch-coverage validation rejects.
M13: submit an unsupported early RUP unit; the file replayer rejects it
at that step. This is a proof-format/control failure, not a claim that
an UNSAT formula fails to entail that clause in unrestricted logic.

Exact minimal affected vertices/edges and full positive witnesses are
in the retained mutation files. No failure was found on the unmutated
family or its h=1 semantic bridge; no family claim is withdrawn.

## 6. General-proof recheck (not extrapolation from h=1)

B's only generator subset relations are empty/all five. Hence it has no
triangle. The eight-set U(A) has a six-cycle plus two isolated vertices.
For any pinned binary subtree M(v)=U(M(v0)) intersect U(M(v1)): necessity
uses its two edges; sufficiency chooses compatible roots AND their
attaining child maps, possible simultaneously on disjoint subtrees.
The height-one case is an exact two-common-neighbor calculation. Assuming
all pairs at height h, combine A and {t0,t2}, then translate/permutate the
result {p23,p24} to an arbitrary nonadjacent pair. This proves h+1 and
attainment; it is structural induction, not finite testing.

The base T_h is unicyclic with all nonleaves degree three and leaves
degree one. Adding a leaf C5 across the five layers is simple and cubic.
A shorter cycle has zero, two or four vertical steps; these reduce to
a forbidden short base/fiber cycle or a base edge joining two leaves.
The total map and the four retained central-layer formulas satisfy every
edge type uniformly in h. These maps do not depend on an unproved C16
minimality assertion.

Partitioning actual edges proves the cut identity for ALL subsets W.
If no leaf fiber is partial, distinct empty/full leaves cost at least
five horizontal edges; complement so all are empty. Selected components
lie in single layers: tree order k costs k+2 boundary edges; a unicyclic
one costs k>=5. Their contributions add, so boundary <=3 isolates one
vertex. If one leaf fiber is partial, vertical cost is two and horizontal
budget one. All other leaves agree and can be made empty. Exactly one
selected layer/component remains, with one original leaf, k nonleaves
and one outgoing base edge. A tree gives 3k+1=2k+1, hence k=0. A unicyclic
component gives 3k+1=2(k+1)+1, hence k=2: three vertices would contradict
girth five. No multicyclic case exists in T_h. Thus only trivial cuts
of size three occur; sizes one/two cannot occur.

A cut vertex or a two-vertex separator would force such a small edge
cut. In the two-vertex case there must be two components each with three
exiting edges and therefore each a singleton; a simple cubic singleton
cannot have three neighbors among only the two deleted vertices. This
proves 3-vertex-connectivity for all h>=1.

Any full map has a layer-0 root outside A, otherwise Q maps into the
bipartite U(A). Leaving an exact parent message forces a child to leave
its message. Remaining height decreases strictly until a leaf. All h+1
visited OLD labels differ from f. Projection to T_h proves their distances
are at least 1,...,h+1, while the horizontal path attains these distances.
For h=max(1,R,K), h+1 is strictly larger than both thresholds. The separate
total witness makes the strategy counterexample nonvacuous.

The machine-readable general_obligations.json separates these general
arguments from their finite controls. Required trusted semantic/axiom/kernel
admission remains pending. best_verified_candidate=none;
best_verified_result=none; first_failed_family_lemma=none.

## 7. Trusted request and continuation

The fresh registry contains fixture-scoped verifier identities, while the
only workflow is the candidate transport gate. No compatible launchable
graph/DRUP verifier action was found. verifier_request.json provides exact
commands, hashes, resource bounds and the gate requirements for another
trust domain. Do not dispatch an unrelated action or rewrite governance.
No new root or Evidence/Result record was written. The bounded audit task
is candidate-ready; root existence remains open. The next admission task
is trusted replay plus statement/axiom/formal auditing, not more evidence
being inferred from this PR's transport checks.
