# General EXIT: exact maximum-cut energy, complete circuit obstruction, and an admissibility gate

candidate_id: candidate:opg434-a01-exit-cover-20260908-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
best_verified_result: none
base_revision: ea7cad35e16393f02a6b5a265e929bca389625a1
reuse_branch: web/attempt-opg434-a01-list-separators-20260907-v1

## 0. Scope and exact verdict

The supplied cycle7-descent package has 20 physical files. All 19 non-self
manifest entries matched before bounded integrity-only restoration of its
137 logical files (5,357,028 bytes). No R11/R12 enumeration, h1, old plateau
census, K2,3 gadget search or universal sevenpole search was rerun.
Only two fixed graph22 a-systems and source subsets of size at most three
are checked anew. The distinct remote extremal-cycle variant is not assigned
these local input hashes or receipts.

The main remains the base above. At fresh read the pending list-separators
branch was 40e53715be3239142ab2e786a42250cbac5a18b4, with its one packet blob
4350bcac81dbb934c21db486228fcc1b16801156. Its earlier list-separators,
smallcut-linear and extremal-cycle material is reused. Issue #3 is unchanged
as the sole coordination issue. The truth failed-route ledger is empty.

General EXIT is NOT proved or disproved here. We prove exact conditions it
must satisfy, a small-side sufficient theorem, a new necessary maximum-cut
structure, and a controlled equal-maximum-cut exchange. A vertex-minimum
ABSTRACT signed bipartite obstruction is completely certified for all subset
flips. Its explicit cubic triangle-free source lift uses a NONMAXIMUM cut;
an explicit larger cut eliminates it from the requested extremal setup.
It is not a root counterexample or an eligible counterexample to general EXIT.

## 1. Quantifiers before a descent claim

For fixed source cut s and c quotient components, a ranges over F_2^c. If a
move may flip any component subset X, every a' is reachable in one move:
X=support(a+a'). Thus the arbitrary-subset state graph is complete, modulo
the redundant global complement. At a global minimum mu(s)=min_a Psi(s,a),
there is no move with lower Psi by definition. A proof that a positive global
minimum has an exit must genuinely use source structural constraints to
contradict its positivity. Defining a distance to an unproved exit is not
such a proof. Refining ties by shortest negative fundamental cycles does
not alter this logical requirement.

The zero condition Psi=0 is basis invariant. The nonzero count is not: we
retain the earlier rule of scanning original source rows in order and
forming a forest separately in each edge phase. Each move recomputes these
forests and all newly formed cycles. We do not resurrect strict single-flip
progress. A same-maximum source-cut exchange changes the quotient and needs
a new system, not a permutation of old columns without a bridge.

## 2. Exact maximum-cut inequalities in quotient coordinates

Let G be cubic and triangle-free, and let s be a maximum cut. Its same-side
edges F form a matching: a vertex with at least two same-side neighbors
would increase the cut under a singleton flip. Write C=E(G) minus F.
Each F-component is a singleton or a pair. Choose theta=0 at its first
vertex and theta=1 at its second vertex, if present.

For any source subset U write its indicator uniquely as
  1_U(v)=beta_C(v)+gamma_C(v)*theta(v),
where gamma exists only for paired components; it is zero for singletons.
For each cross edge uv define D's incidence row at components C(u),C(v),
and H's row with the two corresponding endpoint theta contributions in
the paired-component columns. Repeated columns cancel over GF(2).

The change in cut size is EXACTLY
  cut(s+1_U)-cut(s)=wt(gamma)-wt(D beta+H gamma).                 (MC)
Every split matching edge becomes crossing and gains one; every old cross
edge whose endpoints have different U indicators ceases crossing and loses
one. All other edges are unchanged. This proves (MC) without a probabilistic
or local approximation. Consequently s is maximum iff
  min_beta wt(D beta+H gamma) >= wt(gamma) for EVERY gamma.    (MC*)
The full quantifier over beta and gamma must not be replaced by singleton
flips. Equality describes exactly the cut-size-preserving exchanges.

### A new three-vertex consequence

Let W be the set of endpoints of matching edges F. In the crossing graph
(V,C), the induced graph on W has maximum degree at most one.
If a vertex v in W had two crossing neighbors u,w in W, the three vertices
would form a crossing path. There can be no edge uw by triangle-freeness,
and none of their matching partners is inside this path. The subset
U={u,v,w} therefore has three same-side boundary edges and two cross boundary
edges. Formula (MC) gives gain 3-2=1, contrary to maximality.

Thus the paired-component vertices of the quotient induce maximum degree
at most two. When a paired component has two such neighbors, the two
incidences use different endpoints of its matching edge. This endpoint
condition matters; an arbitrary signed maximum-degree-four bipartite graph
need not satisfy it.

### A controlled equal-maximum exchange

If uv is a crossing edge with both endpoints in W, let uu',vv' be their
matching edges. Let x,y be their respective other crossing neighbors.
By the preceding consequence x,y are outside W. Triangle-freeness makes
x,y distinct, and the old partners are distinct. Flip exactly {u,v}.
The two matching edges uu',vv' become cross edges; ux,vy become matching
edges; uv stays crossing. Hence the cut size is unchanged and the new
same-side edges are again a matching. This is a valid general source move,
not a proof that Psi decreases. A joint new-system test is still required.

## 3. All-subset EXIT as a complete negative-circuit condition

For fixed s, the signed quotient Q is bipartite, with side bit inherited
from s. Its rows retain every cross source edge, with sign
  t_e=theta(u)+theta(v).
For fixed a, the equations are
  M_a(z,b)=t,  M_a=[D | diag(Da)D].
Setting w=z+b splits them into
  z_C+z_D=t_e if a_C=a_D,
  w_C+w_D=t_e if a_C!=a_D.
Each phase is consistent iff every one of its cycles has sign-sum zero.
Loops are zero incidence rows; a negative loop is immediately inconsistent.
Two parallel rows with opposite signs are inconsistent in either phase.
No such row is dropped in our checkers or in offset systems.

For a simple bipartite signed Q, it suffices to consider its negative
INDUCED cycles. An a-monochromatic negative cycle with a chord splits into
two cycles of which at least one is negative. If its phase is zero, all its
vertices have the same a, so the chord has phase zero too. If its phase is
one, a agrees with the bipartition bit up to one constant on the cycle;
every chord also has phase one. Repeated chord splitting ends in a negative
induced cycle of the same phase. This proves the sufficiency of the finite
fixed circuit family; it does not use a different basis after each flip.

For each negative induced cycle K, exactly four vertex patterns on K are
forbidden: two constant a patterns and two a patterns equal to the source
bipartition bit up to complement. Thus
  M_a consistent iff a avoids all these forbidden cylinder sets.          (CC)
An arbitrary flip X replaces a by a+1_X in EVERY constraint in (CC).
This simultaneously accounts for new cycles; it is not a test of the old
negative cycles alone. Its complementary obstruction certificate can give,
for every X, a negative single-phase cycle lambda_X with
  lambda_X^T M_(a+X)=0 and lambda_X^T t=1.

A general sufficient EXIT condition follows immediately. If the sum over
negative induced cycles K of 2^(2-|K|) is strictly less than one, their
forbidden sets cannot cover all a. (A uniformly chosen a belongs to each
set with that probability; add the probabilities.) Then a successful a'
exists and the allowed arbitrary-subset move X=a+a' goes directly to Psi=0.
This is a conditional existence theorem, not a claim that the sum bound
holds for every cubic source. Conversely, an all-a obstruction must have
this sum at least one. Our smallest abstract control fails the bound.

## 4. Small-side theorem and a vertex-minimum signed obstruction

Every SIMPLE signed bipartite graph with a bipartition side of size at most
three has some a making both phases balanced. Add missing edges arbitrarily
to a complete bipartite supergraph; restricting a solution is valid.
For rows L0,L1,L2 set a(L0)=a(L1)=0, a(L2)=1 and for each column j set
  a(R_j)=t_(L0,j)+t_(L1,j).
For either phase, the block using L0,L1 has their sign difference constant
across its columns, so every rectangle is positive and the block is balanced.
The block using L2 is a star. They are disjoint blocks. With one or two rows,
use the corresponding restriction or dummy rows. This proves all right-side
sizes, not only the finite K3,4 controls. Every bipartite graph on at most
seven vertices has such a bipartition side. Therefore a SIMPLE signed
obstruction needs at least eight vertices.

The following eight-vertex, thirteen-edge signed graph is an obstruction.
Sides are {0,1,2,3} and {4,5,6,7}; rows are (u,v,t):
 (0,5,0),(0,6,0),
 (1,4,0),(1,5,1),(1,6,0),(1,7,1),
 (2,4,0),(2,5,0),(2,6,1),
 (3,4,0),(3,5,1),(3,6,0),(3,7,0).
The complete 256-subset certificate starts at a-mask22. Every new M_(22+X)
is retained together with its 0=1 cycle. All scores are positive. Modulo
complement the histogram is 1:62, 2:42, 3:18, 4:6. The global minimum is one;
at X=0 its one negative fundamental cycle has length four, also the minimum
possible in this simple bipartite class. Thus this is a genuine closed
positive global level in the ABSTRACT algebraic class, not the old graph22
single-flip local minimum. Every one-edge deletion has a saved successful
a and two potential vectors. Edge-minimality is certified; no least-edge
claim among all eight-vertex obstructions is made.

For each of all 256 X, a second implementation also builds the retained
phase graphs. If retained cycles are negative it records that reason;
otherwise it contracts each retained balanced component and saves ALL new
offset equations
  z_C+z_D=t_uv+p(u)+p(v).
There are 32 retained-negative cases and 224 inconsistent-new-offset cases.
Every one agrees with full GF(2) row elimination. This includes loops and
parallel equations created by contraction.

This abstract obstruction is NOT asserted to satisfy (MC*).

## 5. An explicit cubic lift, and why it does NOT refute requested EXIT

Add the three omitted edges (0,4,0),(0,7,0),(2,7,0), obtaining signed K4,4
with rows of the sign matrix
  0000
  0101
  0010
  0100.
The preceding thirteen-row obstruction remains as a subsystem for every a.
Split each quotient vertex i into source vertices 2i,2i+1 with a matching
edge. On the four left components use theta=1 at incidence columns
 {0,1}, {0,1}, {1,3}, {1,2}, respectively. On the right endpoint use the
left theta plus the edge sign. Each half has exactly two crossing incidences.
This gives the complete sixteen-vertex cubic triangle-free source:
 (0,1),(0,12),(0,14),(1,9),(1,11),(2,3),(2,12),(2,15),
 (3,9),(3,10),(4,5),(4,8),(4,13),(5,11),(5,15),(6,7),
 (6,8),(6,14),(7,10),(7,13),(8,9),(10,11),(12,13),(14,15).
Its cut {0,...,7}|{8,...,15} has sixteen edges and is matching-normalized.
All a choices on this cut fail. Nevertheless it is NOT a maximum cut:
U={0,12,14} has matching-boundary size three and cross-boundary size two,
so the three-vertex consequence of (MC) rejects it immediately.
The exact maximum is 21, checked over all 32768 normalized source cuts.
All 65536 source subsets were independently checked against (MC); the
largest positive gain is five. The 256 gamma coset minima are saved.
An explicit B-map (even five-bit target masks on vertices0,...,15) is
 [12,17,10,23,6,24,0,23,27,12,0,15,23,9,27,5].
All24 edges are checked; a successful maximum-cut system reconstructs it.
A shortest negative quotient four-cycle lifts to the actual source five-cycle
 (1,9,3,10,11). It is not called reducible just because it is short.
The source cut is eliminated by a strict cut improvement instead.

Accordingly, this proves only that matching-normalization plus the signed
GF(2) equations is insufficient for general EXIT. The MAXIMUM-cut premise
excludes this control. It is neither a root counterexample nor a counterexample
to the user's genuine minimum-non-B extremal implication. We did not find an
eligible closed-positive maximum-cut quotient and do not fabricate one.

## 6. Fixed graph22 checks, without its old census

The supplied graph22 remains a positive B-mappable graph. Its frozen maximum
cut is mask700074. Only a=3074 (inconsistent) and a=1618 (consistent) are
newly checked. X=3074 XOR1618 is a permitted arbitrary-subset jump; full new
offset equations and direct GF(2) agree on consistency. The maximum-cut
three-vertex necessary condition holds for the supplied cut.
The pair exchange {10,21} has exact cut gain zero and produces another
matching-normalized cut. Its old/new matching edge lists are saved. We also
check (MC) on all1794 source subsets of size at most three. The previous
2^21 cut census and 2^17 a-state census were NOT repeated or claimed as new.
The older policy, R11/R12 and sevenpole certificates remain scoped to their
original bytes and receipts.

## 7. Execution and reproduction

Four current bounded processes exited zero: produce.py, check.py,
mutations.py, and energy_v2.py. One earlier energy.py invocation exited one
because its source-edge membership test compared lists with tuples. This
was a code/representation error before testing the energy identity, not a
mathematical counterexample. Its unchanged source, receipt and sanitized
stderr are retained; energy_v2.py fixes representation and computes gain
with an explicit signed indicator. No failed run is counted as success.

The producer uses parity forests for phase systems. The consumer imports
no producer or old generator; it uses column-wise GF(2) elimination, direct
subset cut counts, source/quotient edge substitution and explicit cycle
checks. All 256 subset systems, their cycle duals and their new offset
systems are checked. The arbitrary-right-side small-part construction also
passes every one of the4096 K3,4 sign matrices. The mutation consumer imports
only this new checker, whose hash is in its pre-execution read set.
Twenty-two negative controls and six positives have their expected outcome;
they include dropped/changed rows, invalid cycles/duals, opposite parallel
rows, negative/positive loops, OR instead of XOR at a loop, fake maximum
cuts, reversed cut gains, wrong source signs, false root flags and ignoring
newly created offset contradictions. Positives include row orientation,
a complement, same-sign parallel duplication, target translation and gauge.

Actual runtime: CPython3.13.5, standard library, deterministic seed0, one CPU,
CPU soft/hard35/36 seconds, wall40 seconds, address space512MiB and regular
file/stream1MiB. Input hashes are bound before execution and rechecked after;
actual UTC starts/ends, wall and child-CPU differences, exit codes and stream
hashes are saved. No SAT/Lean/trusted verifier was invoked. The failed
traceback's host paths are removed from its retained text; its raw digest
and explicit omission record remain. Output aggregate is audited at freeze.
Implementation separation is not a separate registered verifier trust domain.


## 8. Remaining EXIT statement and next obligation

A genuine minimum non-B-mappable cubic triangle-free graph would supply a
maximum cut satisfying ALL of (MC*), the endpoint restriction in Section2,
and the admitted source assumptions, while every a must still fail.
The unresolved bridge is to prove that such source-valid data cannot cover
all a by the forbidden negative-circuit cylinders, or to derive a valid
equal-maximum-cut move/contextual larger reduction from that complete cover.
The abstract eight-vertex control is inadmissible at precisely this bridge.
Our small-side theorem and probability sufficient criterion discharge
subclasses, not the general statement. No distance to an unproved exit is
introduced, and no universal seven-terminal substitute is sought.

The first open structural lemma remains general EXIT with maximum-cut and
minimum-non-B premises. Root, statement-faithfulness and registered trusted
closure remain open. Preserve the one pending packet, including all earlier
candidate identities, and append this bounded candidate and its exact scope.
No EvidenceLink, Result, Solution, schema, workflow, registry or truth ledger
is written by this work.
