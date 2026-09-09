# Joint five-row EXIT and the complete physical five-side case

candidate_id: candidate:opg434-a01-five-row-exit-20260909-v1
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

## Claim and exact scope

A maximum-cut quotient of a finite simple triangle-free cubic graph with a
bipartition side of size at most FIVE admits a compatible B-homomorphism.
The <=4 part is retained from the existing PR31 candidate; the five-side part
is new here. This does not prove general EXIT. Any remaining actual cover has
at least SIX components on each side; no minimum source-order claim is made.

For an arbitrary signed bipartite system with five left vertices and any
finite right side, feasibility is equivalent to consistency of at least one
of exactly35 JOINT linear systems described below. This does not say that
one of them is always consistent. Separate lower-row projections do not give
a common global solution.

## Exact algebra and reconstruction

Keep every physical cross edge as a signed quotient row. Its endpoints are
components of the same-side matching F, and sign t=theta(u)+theta(v), where
paired source endpoints have theta0,1. With h=z+ab, the complete edge equation is
 t_ij=h_i+h_j+a_i b_j+a_j b_i.
A physical source map is reconstructed by e_v=z_C+theta(v),
 x_v=(e_v,a_C+e_v,b_C+e_v,s(v)+a_C+b_C+e_v),
then sending coordinate basis0..3 to five-bit generators30,29,27,23.
No physical parallel row is omitted from checking or lifting.

Let E5 be the even subspace of GF(2)^5. For each two-dimensional K<=E5 impose
on ONE shared row-potential h the equations
 u.h = sum_i u_i t_ij
for every column j and every nonzero u in K supported on N(j). There are35
choices of K, because (15*14)/(3*2)=35. The original system is feasible iff
one such joint system is consistent.

For necessity, the five vectors(1,b_i,a_i) have an even dependence space of
dimension at least2. Choose K inside it and sum each supported dependence.
For sufficiency, K-perpendicular has dimension3 and contains all-ones. Complete
all-ones to a basis(1,b,a); the resulting row matrix has dependence space
exactly K. For each column solve the three unknowns(h_j,a_j,b_j). Every row
dependence is supported in that column and has zero right-side sum by the
SAME h system. Thus all columns solve simultaneously. Set z=h+ab and lift.
This covers row rank below3 in the necessary direction without assuming it.

A diagnostic fixed-K conflict is K={0,15,23,24}, with column supports15,23,24
requiring h.15=0, h.23=0, h.24=1. Each individual support parity is constant,
but their sum is0=1. It is not an all-K or root counterexample.

## Physical completeness of the five-side reduction

The full MC identity is gain(U)=wt(gamma)-wt(D beta+H gamma). Maximum cut
implies matching F and Delta(C[W])<=1. The latter makes each paired quotient
vertex have at most two incidences to pairs, at opposite physical endpoints.
Singletons have raw degree3, pairs degree4. Parallel rows occur only between
pairs, at most twice, with the same sign. Physical rows are retained.

Let the smaller side have five vertices, with r pairs; let the other side
have k>=5 vertices and u pairs. Counting raw incidences gives15+r=3k+u, hence
k<=6. If k=6, u=r-3; r=4 or5 makes a right pair's possible degree at most3
or2 by the pair-incidence restriction. Thus r=3,u=0. Give left pairs the
three distinct nonzero q=(a,b), left singletons q=0, and all left h=0.
Each right singleton sees at most three distinct affine row types; repeated
singleton rows have the same zero sign/right side. These row equations solve.

If k=5 then r=u, and r>=4 is impossible since a pair could have at most
2+(5-r)<4 incidences. For r<=1 the explicit one-right-pair construction in
the full report solves all columns: right P has q=0,h=0; left S gets
q=(delta,0),h=delta from its sign to right P; left P gets q=01 and h equal
to its sign to right P, or0 if absent. Remaining right S columns have at
most three distinct row types and consistent repetitions.

For r=3 all P have exactly two P incidences and meet both opposite S.
Set a=1 on P, a=0 on S. Equal-a cycles lie in balanced P-P or zero-signed
S-S graphs. Unequal-a graphs are two K3,2: each P contributes sign difference1,
so their only simple cycles, of length4, are positive. Thus both phases solve.

For r=2 a complete finite residual lemma supplies the solution. The producer
enumerates all nonnegative5x5 matrices of row/column degrees(4,4,3,3,3), with
P-P entries0..2, others0..1, and P-P row/column sum<=2. It yields1155 matrices,
16 orbits under row/column permutations within P/S, and401 endpoint partitions.
Every four-incidence P is partitioned into two pairs, with its first incidence
fixed at end0 and its P-P incidences separated. These are ALL endpoint choices.
All401 have full source maps. Any actual object is one of these after P/S
permutations, ordering parallel copies and swapping matched endpoints; inverse
transformations lift the representative map. No larger graphs are inferred
from a sample. The r=3 case has21 matrices/3 orbits/192 extra endpoint controls.

A second consumer enumerates P-P blocks, then P-S/S-P subsets and S-S margin
blocks, rather than producer row recursion. It reconstructs all endpoint
bit-patterns, verifies COMPLETE expected/observed set equality, checks every
physical source edge, and solves the raw GF system by COLUMN elimination.
All593 cases pass:13029 physical edge checks and10273 raw GF rows. No first
failure. Kernels are independently recovered from1024 affine point tuples:
840 rank-three assignments give exactly35 kernels. Forty arbitrary signed
controls agree with exhaustive-a column solving(24 positive,16 negative);
they are not physical root instances. Twenty-one negative/five positive
mutations cover graph, sign, kernel, potential, loop, parallel and joint-h errors.

## Reproducibility and assurance

Run `python restore.py` for integrity-only restoration of33 logical files,
462158 bytes. It executes no stored mathematical code. The archived full
proof is restored/report.md, SHA-256
79e28df755d0aed18a71d57d6af654eed7118712088e64f7029b911881aa7d6f.
Then run the bounded commands in restored/verifier-request.json. Input/code/
output hashes and six detailed receipts are included; an initial count-only
probe has limited metadata and is not the definitive receipt. Two final
consumer runs occurred in a directory without either producer, both exit0.
The complete work has seven child runs including the limited initial probe.

CPython3.13.5, standard library; one CPU; CPU35/36s, wall40s, address space512MiB,
regular-file1MiB. Stream sizes are checked after exit, not a hard pipe quota.
Generic control seed is4340509; other runs are deterministic seed0. The initial
runner incorrectly put default0 in one control receipt; immutable v1 bytes
and that receipt are retained, and final_controls records4340509. No mathematical
result is altered. All stderr streams are empty. Different logic is not a
registered separate trust domain. No solver/kernel/trusted closure is claimed.

The same PR31 and its sole packet retain the earlier physical-exit candidate
and distinct original archive. No old packet, truth, schema, registry, Harness,
workflow, EvidenceLink, Result or Solution is changed. No R11/R12, h1, graph22
census or rejected universal gadget search was repeated.

First open lemma: for source-valid quotients with both parts>=6, use FULL MC
and endpoint structure to exclude failure of all shared kernel systems, or
obtain an equal-maximum exchange whose ENTIRE rebuilt GF system improves.
The35-kernel criterion is not this missing existence proof. General EXIT,
root, statement-faithfulness and trusted closure remain open.
