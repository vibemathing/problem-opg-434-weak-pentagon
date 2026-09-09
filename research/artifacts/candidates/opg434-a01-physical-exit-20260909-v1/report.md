# Source-valid EXIT: a four-row criterion and two proved subclasses

candidate_id: candidate:opg434-a01-physical-exit-20260909-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
best_verified_result: none
base_revision: 6e702ed29bbc11072ac3376c1c3300cb9958419d

## 0. Scope, provenance and what is not claimed

The current main and Issue #3 confirm PR30's merge. This candidate starts a
new immutable packet from that main, rather than changing the merged packet.
The prior EXIT report and six manifest-bound physical files were read and
matched; its bounded integrity decoder restored 29 logical files. No prior
mathematical producer was executed. The fixed graph22 input is copied from
that exact payload. No R11/R12, h1, old graph22 cut/a census, smaller K2,3
replacement or universal seven-terminal replacement was repeated.

We prove two subclasses of the requested EXIT, not the general statement:
(A) any triangle-free subcubic source cut whose same-side edges are a matching
of size at most three extends to a B-map inducing that exact cut;
(B) for a triangle-free cubic source maximum cut, if the smaller side of its
matching-component quotient has at most four vertices, its GF(2) system has
some successful a. Thus its negative-circuit forbidden sets cannot cover all a.
The second theorem uses actual source incidence degrees and the W restriction,
not an arbitrary signed graph with a similar degree bound. No eligible actual
source counterexample was found in the bounded controls. No minimum-order
claim about the tested family, and no general EXIT or root closure, is made.

## 1. Physical quotient, signs, and the exact algebra

All source graphs are finite and simple. B consists of the even masks in
F_2^5, with adjacency difference t_i=J+e_i (five generators). Let s be a
source cut and F its same-side edges, assumed to be a matching. A component
of (V,F) is either a singleton S or a pair P. At a singleton set theta=0;
on a pair give its two physical endpoints theta=0,1. Retain EACH cross source
edge uv as a quotient row (C(u),C(v),t_uv), with t_uv=theta(u)+theta(v).

The quotient is bipartite, since each component has constant source side s.
It has no loops. A singleton has quotient incidence degree 3 in the cubic
case; a pair has degree 4. These degrees count multiplicity, not just distinct
neighbors. There are no parallel S-S edges by source simplicity, and no
parallel P-S edges: two such edges plus the pair edge would be a source
triangle. Parallel P-P edges, if present, must use disjoint physical endpoints
and hence have the SAME sign. More than two would create a source triangle.
Identical parallel equations may therefore be coalesced for an algebraic
construction, but physical degrees and verification always retain every row.

With D the GF(2) incidence matrix, a successful fixed a has potentials b,z:
    D z + diag(D a) D b = t.                                  (1)
Define y_i=z_i+a_i b_i and q_i=(a_i,b_i). Then every row is exactly
    t_ij = y_i+y_j+a_i b_j+b_i a_j.                            (2)
In particular the product is not being treated as linear before fixing a.

To lift a solution, at source vertex v set e=z_C(v)+theta(v), and put
    x(v)=(e,a_C+e,b_C+e,s(v)+a_C+b_C+e) in F_2^4.
The linear map x -> sum_{i=0}^3 x_i t_i sends weight-one and weight-four
differences to B generators. A same-side matching edge changes all four
coordinates; (1) makes every cross edge have weight-one difference. This
constructs a B-map of the original source and preserves its s coordinate.
Conversely, normalizing the fixed s coordinate of a B-map gives these equations.
This is the prior exact fixed-cut encoding, not a new root acceptance rule.

The checker separately inverts the physical five-bit labels: s=bit4,
a=bit1+bit0, b=bit2+bit0, e=bit0+s, and checks all values against the listed
potentials and endpoint theta. A valid map from a different parameter choice
is not accepted as the stated parameter-to-source witness.

## 2. An exact seven-test criterion for any four-row signed instance

Let a signed bipartite graph have left vertices 0,1,2,3, with any finite
right side. Opposite-sign parallel rows are first rejected. For a nonempty
even subset I of the four left vertices define, at each column j whose
neighbor set contains I,
    p_I(j)=sum_{i in I} t_ij.
There are exactly seven such I (six pairs and the four-set).

THEOREM 1. Equation (2) is solvable iff, for some nonempty even I, p_I(j)
is constant across all columns containing I. An empty column family imposes
no restriction. The statement permits arbitrary missing edges and imposes
no restriction on the number of right vertices.

Necessity. In any solution consider the four row vectors
    r_i=(1,b_i,a_i) in F_2^3.
They have a nonzero linear dependence. Its support I is even because the
first coordinate of each r_i is one. Summing (2) over I at any column
containing I gives p_I(j)=sum_{i in I} y_i, a constant.

Sufficiency. If |I|=4 choose the four distinct q_i in F_2^2. The row vectors
have rank three and their only dependence is the four-set. If I={u,v}, set
q_u=q_v=(0,0) and give the other two positions (1,0),(0,1). Again the rank is
three and the dependence space is exactly spanned by the indicator of I.
Choose the four y_i so their sum on I equals the given constant. For each
right column the three unknowns (y_j,a_j,b_j) satisfy equations with row
vectors r_i and right sides t_ij+y_i. A restricted row set is dependent
only when it contains all of I; the required sum is then zero by construction.
Thus every column's system is consistent. Choose its solution independently;
together they satisfy ALL edges at once. Set z=y+ab to obtain (1).

A useful special case: if all columns adjacent to ALL FOUR rows have the
same total sign parity, use I={0,1,2,3}. Columns with at most three distinct
neighbors never obstruct the construction. This is a simultaneous global
solution, not a test only of previously negative cycles.

In the canonical full 4-by-4 case, switching sets the first row and column
signs to zero, leaving nine free bits. All 512 patterns are retained in the
bounded control; a separate column-span calculation agrees on 344 solvable
and 168 nonsolvable patterns. These abstract patterns are not claimed to be
maximum-cut source quotients.

## 3. An arbitrary-order sparse-matching EXIT theorem

THEOREM 2. Let G be any finite simple triangle-free subcubic graph. If a cut
s has a same-side matching F with |F|<=3, there is a B-map inducing s.
Neither maximum-cut status nor a bound on |V(G)| is required.

Proof. Orient the quotient bipartition L,R so at most one paired component
lies in R. A right singleton has at most three incident source edges. No
such singleton can meet both endpoints of one left pair, by triangle-freeness.

If R has no pair, give all left singletons one common q and y=0, and give
each of the at most three left pairs its own distinct remaining q, with y=0.
At a right singleton there are at most three distinct q row types. Repeated
singleton types have identical right sides because singleton-singleton
signs are zero. The row vectors (1,b,a) of any at most three distinct points
of F_2^2 are linearly independent. Hence each right singleton can be solved
independently as in Section 2.

If R has one pair R*, give it q=(0,0), y=0. There are at most two left pairs.
For a left singleton adjacent to R*, set delta equal to that edge's sign;
there is at most one such edge. Use delta=0 if it is not adjacent. Give these
singletons two types q=(delta,0), y=delta. Give the two left pairs distinct
q types (0,1),(1,1). Set a left pair's y to its edge sign to R*, if any, and
otherwise to zero. Multiple P-P rows have identical signs, so this is well
defined. All rows to R* now satisfy (2). Each remaining right vertex is a
singleton, and the preceding three-distinct-row argument applies: repetitions
are only singleton types with the same y and zero source sign. Solve each
one and lift. This completes every possible distribution of <=3 pairs.

The implementation tests the explicit connected cubic family made from the
Petersen source and k disjoint K3,3 graphs by two-edge splicings along cross
edges. A splicing removes one cross edge from each piece and inserts the two
crossed connections with the same s orientation. It preserves simplicity,
triangle-freeness, cubic degrees, connectedness and the original three F edges.
The construction works for every k>=0; the 10,16,22,70-vertex controls are
finite checks of the formula, not an induction inferred from examples.
No maximum-cut claim is made for these spliced controls.

## 4. Source-valid EXIT with a quotient side of size at most four

For a maximum cut, F is a matching: a vertex with at least two same-side
neighbors would improve the cut under a singleton flip. Let W be the physical
endpoints of F. The exact all-subset cut identity is
    gain(U)=wt(gamma)-wt(D beta+H gamma),                       (MC)
where 1_U(v)=beta_C+gamma_C theta(v). It gives MC* for all beta,gamma.
For three vertices forming a cross-edge path inside W, triangle-freeness
forces all three F edges out of the set, while just two C edges leave it;
(MC) gives gain one. Consequently Delta(C[W])<=1. A paired quotient component
has at most TWO incidences to paired components; if it has two, they use
its distinct physical endpoints. This is where maximum-cut/source information
enters. A signed graph with maximum degree four alone does not suffice.

THEOREM 3. For any finite simple triangle-free cubic G, and ANY maximum cut
s, if the smaller bipartition side of Q has size at most four, (1) is solvable.
Equivalently its negative-circuit forbidden-pattern family is not a cover.

For sides of size at most three, the earlier small-side construction applies
after coalescing only identical parallel rows. For completeness, complete the
missing edges arbitrarily, set a(L0)=a(L1)=0 and a(L2)=1, and set
 a(Rj)=t_(L0,j)+t_(L1,j). In each phase the first two rows have constant sign
difference on their columns, so all their rectangles are positive; the third
row is a disjoint star. Thus both phases are balanced. Restrict to the original
graph. Smaller left sides may be padded with dummy rows.

Now let |L|=4 and |R|=k>=4. Let r and u be the counts of paired components
on L and R. The full incidence degrees give
    m=12+r=3k+u,  0<=r<=4, 0<=u<=k.
Thus k<=5. If k=5 then u=r-3. The case r=4,u=1 is impossible: that right
pair would have all four incidences to pairs, contrary to the at-most-two
restriction. In the remaining case r=3,u=0, every right vertex is a singleton
and has three distinct neighbors. The four-set construction of Theorem 1
has no full-column restrictions and supplies a solution.

If k=4, then r=u. Values r>=3 are impossible: each left pair has at most two
incidences to pairs and at most 4-r incidences to singletons, totaling at most
three. For r<=1 there is at most one degree-four right column. Its parity
can always be the constant chosen in Theorem 1.

The only remaining case is r=u=2. Each pair has precisely two incidences to
the opposite pairs and two to the opposite singletons; the latter meet both
singletons. Each physical endpoint of the pair has one P-P and one P-S edge.
Only the two right pairs can be full columns. If at most one is full there
is no parity conflict. If both are full, P-P is a simple K2,2. For a full
column Rj,
    sum_{i in L} t_ij = sum_{left pairs Pi} theta(Pi, edge Pi-Rj),
because all singleton theta are zero and the four incidences on Rj have two
of each theta. For each left pair, its edges to the two right pairs use
opposite endpoints. The difference of the two column parities is therefore
1+1=0. The four-set criterion again solves every column.

All cases are covered. The construction retains every original physical edge
when it lifts. In particular multiple P-P rows are not assigned separate
incompatible endpoint choices, and the conclusion is about the prescribed
maximum cut, not a switch to an unverified cut.

This theorem discharges the source-admissibility gap for small quotient sides;
it is NOT a proof that every maximum cut has a small quotient side. A genuinely
non-B-mappable source must have at least four F edges (Theorem 2) and at least
five quotient components on EACH side in every maximum cut (Theorem 3).
In particular it would have at least 10+4=14 source vertices. No assertion of
existence at this lower bound is made.

## 5. Why the old eight-vertex abstract obstruction cannot embed

In the prior thirteen-edge obstruction, the four degree-four quotient vertices
1,3,5,6 must be pairs in any cubic source supergraph. Vertices 5 and 6 already
have two paired neighbors 1,3, so their other neighbors 0,2 must be singletons.
Both pairs 5 and 6 use opposite physical endpoints at their edges to 0 and 2.
Hence the sign sum of cycle (0,5,2,6) MUST be zero, including after switching.
But in the frozen abstract obstruction it is one. Thus no sign-switching copy
of that signed subsystem is present in a maximum-cut source quotient. This
excludes the old obstruction even as a signed subgraph, not only its particular
nonmaximum sixteen-vertex lift. Larger negative-cylinder covers remain possible
in the unresolved analysis; none is asserted to be source-admissible here.

## 6. Bounded controls, source mapping and negative tests

No old large census was replayed. New controls are:
* 512 canonical complete signed four-row patterns, checked by 27,588 separately
  constructed column systems (27,244 inconsistent); 344 versus 168 cases.
* All 96 canonical physical lifts of the saturated r=u=2 case: three P-P
  degree-two multigraph patterns, two singleton matchings, and 2^4 endpoint
  orientation choices. Swapping a pair's endpoints fixes its first P-P incidence
  at theta=0; the second is theta=1. Its two P-S choices remain free. This proves
  coverage up to these explicit source isomorphisms, without assuming that
  differently coded cases are nonisomorphic. Every full graph/quotient/map is
  retained. The producer builds through quotient incidences; the checker builds
  the physical edge patterns separately. All 96 maps pass. Their chosen cut has
  size14; direct exhaustive cuts find maxima16 in76 cases and18 in20 cases.
  Thus this saturated finite class is not an eligible maximum-cut obstruction.
* Five defined cubic sources with vertices Ai,Bi and edges AiAi+1,AiBi,BiBi+k,
  for (n,k)=(5,2),(7,2),(8,3),(9,2),(9,4). Their actual maximum cuts are
  12,17,24,22,22; all normalized maximum-cut sets (5,21,1,27,27 cuts) are saved
  and separately checked. All81 fixed-cut systems have explicit solutions.
  This is a bounded family search, NOT an enumeration of all graphs of those
  orders. No failing cut or eligible root candidate was found.
* MC is verified on all16,384 source subsets for one fixed fourteen-vertex
  maximum cut. This is the complete beta/gamma range for that source only.
* The old graph22's fixed bad3074/good1618 systems are checked once, together
  with their exact physical rows. Column elimination produces dual mask16853728
  for the bad system; the good one has a full map. No old cut/a census is rerun.
* The sparse-complement construction has four explicit positive controls of
  orders10,16,22,70, checked by column elimination and full physical maps.

The consumer imports no production or prior mathematical module. It uses
coordinate sets for B, direct binary source cuts, explicit physical edges and
column-space elimination, as opposed to the producer's Gray-code cut scan,
even-support construction and signed traversal. All listed parameter triples
are checked against the inverse of their physical five-bit map. The final
mutation suite has19 negative controls and5 positives. An earlier18-negative
suite lacks only the added wrong-parameter/valid-map test; its exact output is
retained as mutation-results-v1.json. Do not add the overlapping suites and
claim37 distinct negative tests.

Seven bounded mathematical processes completed, all with exit0 and no timeout:
producer, consumer, mutations, final consumer, final mutations, sparse producer,
sparse consumer. Exact immutable earlier versions remain. CPython3.13.5,
standard library, deterministic seed0, one CPU, CPU35/36s, wall40s, 512MiB
address space, 1MiB per regular file/stream. Every declared read set is hashed
before and rechecked after execution. All streams and output bytes are bound.
The runner's outputs field is explicitly a post-run JSON inventory excluding
listed inputs, not a system-call write trace. Aggregate output is audited at
freeze, not claimed as a hard filesystem quota. A network read attempt failed
before computations; connector reads supplied the source. That is not a
mathematical failure. No solver, Lean or registered verifier executed.

## 7. Remaining general EXIT and verification request

The remaining source-valid cover problem has at least five quotient components
on each side and at least four paired components in total. The seven even-support
tests solve an arbitrary four-row system but do not scale by simply checking
all four-row projections: separate projections need not share one assignment.
The actual maximum-cut inequalities for every gamma must still be used to
exclude larger covers, or to prove an equal-maximum source exchange or a
context-aware lifting for the full exterior joint relation. No such universal
bridge is claimed. No distance to an unproved exit is introduced.

The trusted request is to check the universal sparse-complement/four-side proofs,
the full physical/parallel-edge semantics, and the frozen finite consumers under
the registered acceptance capabilities. A request is not a receipt. The source
ProblemContract, statement-faithfulness, general EXIT and trusted closure all
remain open. No truth, EvidenceLink, Result, Solution, schema, Harness, workflow
or registry is modified; all results retain candidate_only.
