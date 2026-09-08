# R09: the exact five-vertex replacement limit and conditional linear quotient systems

candidate_id: candidate:opg434-a01-smallcut-linear-20260908-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
base_revision: ea7cad35e16393f02a6b5a265e929bca389625a1

## 0. Frozen scope and predecessor integrity

The supplied cut-signatures ZIP has 57 files. All 56 non-self manifest entries
matched their bytes and SHA-256. Its archive hash is
550540f8c86406b6b12ed4ccb801e0a59436564c24acb57d3e55fcc6c16274e0.
The prior six successful and two unsuccessful processes remain historical.
No 3840/57600 belt enumeration, h1 replay, C10 reconstruction or old certificate
regeneration was done. R11 and R12 remain complete at candidate level with no
failed allowed state. The frozen graph22 is positive, not a root counterexample.
The supplied 57-file variant is different from the existing remote
list-separators branch; neither its code hashes nor its receipts are assigned
to that other variant. The raw original ZIP remains an attachment; this
candidate binds its integrity and transports its own new code and results.

Fresh main and PR29 confirmed the latter is merged. The existing unmerged
web/attempt-opg434-a01-list-separators-20260907-v1 branch and its sole packet are
reused for this continuation. No immutable merged packet or truth file is edited.

Throughout, B has even five-bit vectors, edge differences
S=(30,29,27,23,15), corresponding to t_i=J+e_i. Lists, where present, constrain
actual vertex labels; repeated port occurrences are the same source variable.
Sigma(P;p) is the complete jointly attainable tuple on INTERNAL ports. For
replacement across cut edges the applicable EXTERNAL-neighbor relation is
R_P(b)=exists x in Sigma(P;p): x_i adjacent b_i for every i. They are not the
same relation. All gadget vertices below have unrestricted lists.

## 1. Connected sides of a three-edge cut with at most five vertices

If U is a side in a cubic graph and |delta(U)|=3, then
  3|U|-2|E(U)|=3.
Hence |U| is odd. A one-vertex side is the trivial three-cut. A three-vertex
side would have three internal edges, necessarily a triangle, and is excluded.
A five-vertex triangle-free side has six edges. If it is not bipartite, its
shortest odd cycle is C5; every sixth edge would then be a chord of C5 and
would make a triangle. Thus it is bipartite. A 1+4 partition admits at most
four edges, so it has partition 2+3 and all six possible edges: it is K2,3.
Its three cut ends are distinct degree-two vertices. This proves the small
connected-side classification, not a claim that a particular cut is unavoidable.
The independent finite check enumerates every simple graph on n=1,...,5,
including disconnected candidates, with degree at most three and total deficit
three. Counts are 1,0,0,0,10; the ten labeled five-vertex graphs are copies of K2,3.

## 2. The stronger exact smaller-gadget proposal fails

A replacement gadget P' is a simple triangle-free graph with three specified
attachment incidences (repetition of their internal endpoint is allowed), such
that every vertex becomes cubic after these three attachments and no other
exterior edges are added or changed. Necessarily
  sum_v (3-deg_P'(v))=3, so 3|P'|-2|E(P')|=3.
For |P'|<5 the only possibility is one vertex with all three incidences.
Order three would again require a forbidden triangle; even orders are ruled
out by parity. Zero vertices cannot support the attachments. The argument does
not assume distinct gadget endpoints, and therefore covers the more permissive
model. With three distinct endpoints there is no smaller gadget at all.

For K2,3, write the two hubs 0,1 and its ports 2,3,4. Its internal Sigma has
1456 triples: exactly those with a common neighbor. Its external relation is
all 4096 tuples B^3. To prove the latter for ANY (b0,b1,b2), choose w outside
N(b0) union N(b1) union N(b2). The union has size at most 15, while |B|=16.
Then w equals or is nonadjacent to each b_i. The common-neighbor rules of B give
x_i in N(w) intersect N(b_i): equality has five choices; for difference
t_i+t_j the two choices are w+t_i and w+t_j. Uniqueness follows because
the five generators have only the one all-five linear relation. Map both hubs to w and each port to x_i.
This checks all six internal and all three cut edges with attainment.

For the one-vertex star, R_star(b0,b1,b2)=N(b0) intersect N(b1) intersect N(b2)
being nonempty. It has only 1456 tuples. Full relation elimination from the
actual five/eight-vertex and one/four-vertex edge tables confirms these counts,
not merely their unary projections. The first difference in increasing even-mask
lexicographic order is (0,0,15). K2,3 admits hub/port map
  [3,3,29,29,20]
for these external pins. The star has no map: N(0) intersect N(15) is empty,
since 0 and 15 are adjacent. The full relation and all 4096 K2,3 witnesses
are saved in gadget-result.json.

Consequently no smaller gadget in this exact cubic three-attachment model
realizes the same R as this legitimate five-vertex cut side. This is the minimal
nontrivial triangle-free small side and the complete smaller-order obstruction.
It does not rule out a replacement which changes the exterior, a larger local
patch, a merely one-way lifting, or global rechoice. The prior valid replacement
of K2,3 by a single star at DISTINCT PAIRWISE NONADJACENT outside endpoints still
reduces order by four and lifts every smaller-graph map; it is not exact R
preservation and is not withdrawn. No original weak-pentagon claim is negated.

## 3. Nonmatching three-cuts expose a smaller edge cut

Assume G is connected and cubic with no edge cut of size one or two. A side of
a three-cut is connected: two components would each have boundary at least
three, exceeding the budget. If two of the cut edges meet v on that side, v has
one internal edge. For the nonempty side U-v,
  |delta(U-v)|=3-2+1=2,
a contradiction. If all three meet v, connectedness of the side makes it the
singleton {v}. Thus every NONTRIVIAL three-cut in this precise domain is a
matching. This is a structural implication, not application of cubic minimality
to noncubic pieces. Without the absence of one/two-cuts, nonmatching cuts are
not silently discarded: move v and retain the complete two-port relation.

A saved 12-vertex simple triangle-free cubic fixture uses two copies of K3,3
minus edge03, connected by edges0--9 and3--6. U={0,...,6} has cut
  {0--9,6--10,6--11}.
Removing v=6 from that side gives exactly {0--9,3--6}. The new checker verifies
both cut edge sets, simplicity, cubic degrees and absence of triangles.
This example is positive and is not a root counterexample.

For a connected cubic graph, a connected acyclic side of a three-cut has
boundary 3n-2(n-1)=n+2, hence n=1. Thus when one/two-cuts and nontrivial
three-cuts are absent the remaining difficulty is genuinely cyclically
four-edge-connected. Neither the gadget obstruction nor this observation
proves colorability of that core. The known >=7-side cap decomposition remains
valid; no failed exact five-side replacement is used as its missing proof.

## 4. Exact quotient coordinates and all parallel rows

Identify the four-bit model with the even-five-bit B by
  L(x0,x1,x2,x3)=sum_{i=0}^3 x_i t_i.
Its edge differences have four-bit weight one or four. Parametrize bijectively
  x(s,a,b,e)=(e,a+e,b+e,s+a+b+e).
Direct substitution yields, for distinct source endpoints:
- s_u=s_v: a_u=a_v, b_u=b_v and e_u+e_v=1;
- s_u!=s_v: e_u+e_v=(a_u+a_v)(b_u+b_v).
All sums/products in this section are in GF(2). All 256 target endpoint pairs
were checked independently using coordinate sets/Hamming distance four.

Fix a vertex partition s. Let F contain exactly the same-s edges. If some
F-component is not bipartite, this partition is impossible. Otherwise choose
one bipartition theta in each component C. The first edge rule forces
  a_v=a_C, b_v=b_C, e_v=z_C+theta(v).
Conversely these formulas satisfy all F edges. Contract F to a MULTIGRAPH Q,
retaining every crossing edge with its original edge ID and endpoints. For
e=uv from C to D put d_e=theta(u)+theta(v). It gives the exact equation
  z_C+z_D+(a_C+a_D)(b_C+b_D)=d_e.                         (1)
For an incidence matrix D_Q over GF(2), with one row for EACH crossing edge,
  D_Q z + diag(D_Q a) D_Q b = d.                          (2)
This is a linear system in (z,b) AFTER a is fixed. It is NOT advertised as
jointly linear in all of a,b,z. With q=(a,b) fixed, the usual smaller system is
D_Q z=d+diag(D_Q a)D_Q b. Neither form deletes parallel rows.

Each original B-map gives a solution of these equations with its own s; each
solution gives a full map through the displayed coordinate formulas, covering
all internal and crossing edges. Therefore unrestricted global existence is
exactly: exists s with F bipartite, exists a such that (2) is consistent.
No arbitrary partition, local optimum or chosen a is asserted sufficient.

## 5. Linear-system decomposition, complete dependencies and certificates

Let Q0 contain edges with a_C=a_D and Q1 contain the other crossing edges.
Put y=z+b. This invertible change of unknowns splits (2) into
  D_Q0 z=d0,                 D_Q1 y=d1.                  (3)
For either block, a solution exists iff every cycle has even d-sum. Necessity
follows by summing equations along a cycle. Sufficiency follows by assigning
one free root value per connected component, propagating along a spanning
forest and checking EVERY nonforest edge. Parallel edges form two-edge cycles
and are included. A disagreeing pair of parallel rows is a real contradiction.

Thus rank of (2) is 2c-kappa(Q0)-kappa(Q1), including isolated component
vertices in both kappas. When consistent, there are exactly
2^(kappa(Q0)+kappa(Q1)) solutions (z,b). A failed row propagation produces a
cycle whose equations XOR to 0=1; a minimum-cardinality such dependency is a
negative simple cycle in one block. More generally Gaussian provenance rows
provide a directly replayable dependence certificate, not a solver status.
The producer uses bitmask Gaussian elimination with row provenance. Its new
consumer uses two signed graphs and propagation, and separately verifies every
saved row dependence by set symmetric difference. No producer is imported.

For C5 with s=(0,0,0,1,1), the two F components are a three-vertex path and an
edge. Its quotient has two parallel crossing edges with RHS0 and RHS1. For
both a patterns up to global complement the coefficient rows coincide, so
no q or z can fix that s. Keeping only one edge would falsely accept it.
The source C5 still maps to B under another s. This guards the quantifier.

## 6. A useful matching partition and an exact short-cycle extraction

A strictly improving single-vertex cut process terminates: a flip increases
the integer number of crossing edges, bounded by |E|. At termination in a
subcubic graph each vertex has at most one same-side neighbor. Hence F is a
matching plus isolated vertices. This gives a useful search class, NOT a proof
that restricting all root searches to such partitions is complete.

If G is triangle-free and F is a matching, two quotient edges with the same
component pair cannot have opposite d. Such opposite parities would mean their
source edges have the same endpoint in one component and opposite endpoints
of the matching edge in the other; those three edges make a triangle.
Thus this entire two-edge obstruction is excluded in this class. It does NOT
exclude negative longer cycles.

For a negative simple quotient cycle of length k, join the entering/exiting
source endpoints inside each component along its F path. The components are
disjoint, so the resulting source cycle is simple. In the matching case each
joining path has length0 or1. Their total has odd parity, since its parity is
the sum of d on the quotient cycle. Q is bipartite by s, so k is even. The
source cycle has odd length between k+1 and 2k-1. In a triangle-free source k=2
has just been excluded. A negative four-cycle therefore lifts to an actual
simple five- or seven-cycle. The saved seven-cycle is induced because its
source has girth six; inducedness is not asserted for every triangle-free source.
This is a short local configuration, NOT by itself a reducible patch.

The fresh graph22 local-cut fixture has 18 components and 29 crossing edges.
For constant a=0 it has a minimum-length negative quotient four-cycle on
components [8,16,13,10], edges [19,26,21,17]. Its lifted source cycle is
  [8,9,20,17,14,11,19].
The seven outside neighbors, in this order, are [7,10,12,6,3,0,16]. Its edge
boundary has size seven, not three. The code inspected 404 a patterns in a
fixed order and found a solution at the last; every earlier inconsistency
has its saved XOR row certificate. A different consumer checked all 404.
This is a finite successful search, not enumeration of all possible a for
all graphs. Its explicit full B-map on 0,...,21 is
[23,0,23,0,23,0,27,0,27,20,10,10,23,12,29,0,27,6,30,5,9,17].
All 33 source edges and all 29 equations pass. Graph22 remains a positive graph.

## 7. The next boundary retains the full joint cycle relation

For a source cycle C_l with external pins p_i, its exact extension count is
  trace(product_{i=0}^{l-1}(diag(1_{N(p_i)}) A_B)).
Expanding the trace sums over all x_0,...,x_{l-1}, checking each pin and each
cycle edge, including the final edge x_{l-1}--x_0. Nonzero count is exactly
membership in R_C_l. This compact representation retains the correlated
boundary; it is not a product of unary lists or independent path messages.

For the extracted seven-cycle, the displayed full graph22 map induces pins
[0,10,23,27,0,23,27]. Integer transfer multiplication and a separate exhaustive
DFS both find exactly 22 internal maps. A closing-edge mutation uses C5 pins
[0,23,0,29,0]: the open chain has 329 maps, while the true cycle has zero.
The whole transfer matrix and a positive internal witness are retained.
No universal seven-port lifting is inferred from this one realized tuple.

## 8. Execution, reproducibility and nonterminal disposition

Six local bounded processes exited zero: producer, consumer, mutation suite,
input-frozen consumer repeat, input-frozen mutation repeat, and cycle-boundary
check. The current suite rejects20 negative mutations and accepts3 positives;
a separate closing-edge control rejects the open-chain substitution above.
Mutations cover graph/port/target semantics, false internal/external signatures,
missing tuples, parallel-edge deletion, RHS or phase corruption, false linear
rank/dependence, invalid cycle lifts, full-map damage, arbitrary-a acceptance,
nonmatching-cut arithmetic and incorrect cubic degree deficits.

Runtime is CPython3.13.5, standard library only, deterministic seed0. Limits:
one CPU affinity, CPU35/36s, wall40s, address space512MiB, per-file/stream1MiB;
5MiB aggregate is checked after exit. No timeout or UNKNOWN counts as success.
The early runner's input list omitted non-input-prefixed JSON read by consumers;
these early receipts are preserved and not represented as exhaustive read sets.
The definitive check-final and mutations-final receipts hash their two actual
JSON inputs BEFORE execution; all imported code is separately bound. Runner
versions v1/v2/current are retained to match historical code hashes. No input
or old receipt was retroactively changed. Different implementations are not
separate trusted verification domains. Neither CI nor a local exit0 closes root.

The exact smaller-five-side rule has failed in its declared gadget model and
is saved as a candidate failed-route proposal. No failed-route truth record is
edited. Nonmatching cuts expose lower cuts under the stated hypotheses. The
conditional linear systems, their full row dependencies, and the short odd-cycle
lift are proved above. Still open: use genuine minimum non-B-mappability to
force a valid smaller-graph replacement for every remaining core, OR prove the
existence of a suitable s and a for all contract graphs. In particular the
seven-port correlated relation is not yet guaranteed to intersect every actual
exterior relation. No EvidenceLink, Result, Solution or trusted closure is made.
best_verified_result=none; root_closed=false.
