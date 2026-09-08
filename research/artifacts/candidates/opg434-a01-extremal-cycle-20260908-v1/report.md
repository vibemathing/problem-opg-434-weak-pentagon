# Maximum-cut cycle interfaces and the failure of one-step strict defect descent

candidate_id: candidate:opg434-a01-extremal-cycle-20260908-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
base_revision: ea7cad35e16393f02a6b5a265e929bca389625a1

## 0. Fixed inputs, mathematical disposition, and assurance

The seven supplied smallcut-linear documents and the 41-file ZIP were read;
all 40 non-self manifest entries matched. This is integrity checking, not
re-execution of their mathematical runs. No R11/R12 3840/57600 enumeration,
h1 replay, C10 reconstruction, or search for a smaller exact cubic K2,3 cap
was performed. R11/R12 keep their earlier candidate witness status. Graph22
has a full B-map in input.json and is never a root counterexample.

Fresh main is the PR29 merge. The still-unmerged list-separators transaction
already advanced to eae6cce044535d630c36a7ee3ba494a5f827ad35 and contains a
DIFFERENT smallcut-linear implementation. Its packet, existing candidates,
and file bytes are retained. The present computation consumes the supplied
fixed graph/system data, not that other variant's code or receipts.

New bounded runs establish finite candidate facts: all 2^21 source cuts;
all 2^17 normalized a states of one chosen maximum cut; a complete 67,200-row
internal C7 boundary relation; all 2,940 attachment assignments for the four
smaller no-wire sevenpole types; an actual 20-vertex mapped replacement
whose exterior cannot be extended across the original cycle; and a checked
descent forest reaching a zero-defect state from every a of this fixed cut.
The uniform single-component STRICT-descent rule fails on this positive
source. The general root and trusted closure remain open.

## 1. Exact target, quotient system, and the extremal quantifiers

All graphs are finite, simple and undirected unless the quotient is explicitly
a multigraph. B has the 16 even vectors in F2^5, with edge differences
T=(30,29,27,23,15), t_i=J+e_i. An adjacency is a difference of weight four.
Target-label repetition is permitted. The only nonempty generator subset
summing to zero is all five; in particular B is triangle-free. Projection
x -> (x0+x4,x1+x4,x2+x4,x3+x4) gives the four-bit model with edge weights
one or four. Its inverse has x4 equal to the four-bit parity.

A maximum source cut s exists by finiteness. In a cubic graph, if any vertex
has at least two same-side incident edges, flipping it increases the cut.
Thus EVERY maximum cut is matching-normalized: its same-side graph F is a
matching plus isolated vertices. Consequently maximizing over normalized
cuts gives the same maximum cut size as maximizing over all cuts. This is
not a claim that an arbitrary maximum cut admits a target map.

Write a target four-bit label as (e,a+e,b+e,s+a+b+e). Direct substitution into
the five allowed differences gives: same-side edges require equal a,b and
opposite e; crossing edges require e_u+e_v=(a_u+a_v)(b_u+b_v).
Let the components of F be C, choose their bipartition theta, and put
(a_v,b_v)=(a_C,b_C), e_v=z_C+theta(v). Give the quotient one row for EACH
crossing source edge, including parallel rows, with incidence matrix D and
t_e=theta(u)+theta(v). The exact equations are
  D z + diag(D a) D b = t.                                  (1)
They are linear in (z,b) ONLY AFTER s AND a are fixed.
Writing w=z+b separates (1) into signed incidence systems on
E0={uv:a_u=a_v} and E1={uv:a_u!=a_v}. Each has a solution iff all its cycles
have sign sum zero. Tree propagation proves sufficiency; cancellation proves
necessity. No parallel row is removed. Matrix dependency witnesses are kept.

To define the requested number of negative FUNDAMENTAL cycles unambiguously,
order quotient edges by their original sorted source edge. In each E0,E1,
greedily build a spanning forest in that order. Let nu_s(a) be the number
of nonforest edges whose fundamental cycle has sign one. The forest is
recomputed after every a change. Then nu_s(a)=0 iff (1) is consistent.
The number is basis-dependent; its particular deterministic basis is part
of this candidate, not silently treated as an invariant of a signed graph.

If a hypothetical graph has no B-map, every normalized s and every a fails.
One may choose s of maximum cut size and then a minimizing nu_s(a), breaking
finite ties deterministically. Its minimum is positive. A proof still needs
an operation contradicting that choice, or another argument producing a map.
The concrete positive graph below does NOT satisfy the hypothetical nonmap
premise; its positive one-flip trap is NOT a global minimum over all a.
This distinction is essential to what the counterexample does and does not do.

## 2. Maximum-cut and complete a-state census on graph22

Graph22 has vertices 0..21, edges Ai-A(i+1), Ai-Bi, Bi-B(i+3), modulo 11,
with Ai=i, Bi=i+11. The complete input includes its explicit B-map.
The producer inspected every 2^21 cut with s0=0 by Gray updates; the consumer
used binary order and a direct sum over all 33 edges. Both yield maximum
cut size 29 and exactly eleven maximum cuts modulo complement. The chosen
cut is the first bitmask in increasing integer order:
  s=[0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0].
Its same-side matching is (9,10),(11,19),(12,20),(18,21), giving 18 components
and 29 quotient rows. maxcut-result.json records all eleven masks and the
entire cut-size histogram, not just a claimed upper bound.

Fix a0=0; encode a by integer k with a_j=bit_(j-1)(k) for j>=1. A flip of
component zero, renormalized by global complement, sends k to k XOR(2^17-1).
All other component flips toggle the corresponding bit. The complete energy
array has 131,072 entries. Its histogram is
  nu=0:34216, 1:60640, 2:31756, 3:4218, 4:190, 5:44, 6:8.
The producer uses signed union/forest operations. The consumer independently
eliminates every original matrix row of (1) over GF(2) for every a. Sequential
row independence selects exactly the same ordered forests after the invertible
change w=z+b; dependent-row sign one is the counted fundamental-cycle defect.
Thus comparison covers every entry, including failures, not just SAT examples.

The first strictly-positive state with no strictly improving ONE-component
flip is k=1537, a=[0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0], nu=1.
Its eighteen neighbor defects, for components 1..17 then 0, are
  [3,1,1,1,2,1,1,1,1,2,2,1,1,1,1,1,1,1].
There are 406 such positive one-flip traps in this complete finite domain.
This is a counterexample to the UNIFORM lemma that every nonzero state at a
maximum normalized cut has a strictly improving single-component flip.
It is not a counterexample to existence of a good a, nor to the stronger
premise that a is a globally minimum positive defect of a nonmap graph.

## 3. The first extracted configuration and its complete joint relation

At k=1537, the shortest negative signed quotient cycle has SIX edges, not
four. Its ordered component vertices are (3,2,12,17,14,4,3), with row indices
(5,6,24,26,10,7), all in E0. The consumer checks these rows sum to zero on
all coefficients and to one on the right-hand side; parity-state BFS checks
there is no shorter negative cycle. Its exact source-edge lift is
  C=(3,2,13,21,18,15,4).
The outside neighbor order is (14,1,16,10,7,12,5). C is induced and these
seven outside vertices are distinct. Full graph/cut identities are checked.

Generally a simple negative quotient 2k-cycle lifts through disjoint matching
components to a simple source cycle of length 2k+r, where r is odd and
1<=r<=2k-1. A quotient four-cycle therefore lifts to C5 or C7; a six-cycle
can lift to C7,C9,C11. NO uniform bound forcing the first cycle to be C5/C7
has been proved. Here r=1 and the specific lifted cycle is C7.

For this induced C7, every internal vertex is a port. Its FULL INTERNAL
joint relation is Sigma_C7={(x0,...,x6):x_i adjacent x_(i+1)}. All 67,200
ordered rows are stored in cycle7-sigma.txt, one hexadecimal target INDEX
per vertex using the sorted 16-label alphabet. The consumer checks every
row and uniqueness, and computes trace(A_B^7)=67,200 by independent matrix
multiplication. Containment plus exact cardinality proves full coverage.
It is not a tuple count inferred from unary lists or a sample.
The EXTERNAL-neighbor relation is
  R_C7(b)=exists x in Sigma_C7: x_i adjacent b_i for all i.       (2)
List-transfer elimination in the consumer computes (2) without assuming
that every proper boundary tuple extends. In particular b_i=b_(i+1)
forces an impossible triangle in B, so consecutive equal pins are rejected.

## 4. No universally liftable smaller isolated seven-terminal replacement

Here the scope is precise: keep the seven distinct exterior vertices and
their other edges fixed; consume exactly one free incidence at each terminal;
use fewer than seven NEW internal vertices, all of final degree three;
require simplicity and triangle-freeness. Permit repeated internal endpoints,
disconnected internal gadgets, and optional wires joining pairs of terminals.
The replacement is intended to lift EVERY accepted exterior map, i.e.
R_replacement is contained in (2). This is stronger than merely showing
existence of some map of a given exterior. Exterior-specific extra constraints,
changes to other exterior edges, larger patches and global rechoice are NOT
excluded by the following result.

First consider no wires. If the internal graph has n vertices and m edges,
3n-2m=7. For n<7 only n=3,m=1 or n=5,m=4 are possible. Triangle-free
maximum-degree-three graphs in those cases have exactly four isomorphism types:
an edge and isolate; P5; the five-vertex tree with arm lengths (1,1,2);
and C4 plus isolate. A connected forest at n=5 is a tree and excludes the
four-leaf star by the degree bound; a cyclic case can only be C4 plus isolate.
The independent labeled census gives n=3:3 and n=5:135, split into P5:60,
fork:60,C4+isolate:15. No other smaller order works.

Every such internal graph P is bipartite. An attachment map phi from the
seven cycle positions to V(P) therefore has some consecutive positions i,i+1
whose internal endpoints are equal or not adjacent. Otherwise phi would
send an odd closed walk to a bipartite graph.
For every equal/nonadjacent pair u,v in each listed P there is a P->B map
whose images have a common neighbor. Here is a uniform proof. In the same
bipartition class, map their component to a single target edge, identifying
u,v. For different components align their target maps by translation. In
a tree, opposite-class nonadjacent vertices have distance three (the only
remaining case); map the three-edge path along three consecutive edges of
a target pentagon. Its endpoint images have a common neighbor along the
remaining two pentagon edges. Extend the hanging tree edges arbitrarily.
C4 has no remaining opposite-class nonedge case.

Choose equal external pins at i,i+1 to be that common neighbor, and give
all other terminals any neighbor of their mapped internal endpoint. The
replacement accepts this complete tuple, but (2) rejects it. Thus no listed
attachment map gives the required inclusion. The data contain full internal
maps and rejected seven-pin tuples for ALL 2,940 attachment assignments:
210 for edge+isolate, 1260 for P5, 630 for fork, 840 for C4+isolate. The
consumer derives attachments from the degree deficits and checks exact coverage,
every internal and pin edge, and zero extensions over the original C7.

If a wire is present, its two terminals lie in a separate replacement
component. Some consecutive positions on the boundary C7 must lie in different
replacement components. Each small component is B-mappable: with at most five
vertices the triangle-free maximum-degree-three possibilities are bipartite
or C5, all map to B. Translate separate component maps, including their
terminal labels, to make these two external pins equal. Again (2) rejects.
Thus wires do not evade the negative result in this fixed-incidence model.
This is a new C7-interface obstruction, not a rerun of the prohibited K2,3
small-cap search.

## 5. A concrete failed lifting on the actual exterior

The abstract interface failure also has a complete fixed-source witness.
Take the actual fifteen-vertex exterior H of C above. Replace C by a path
P5 on new internal vertices 0..4, attaching the seven exterior vertices in
order (14,1,16,10,7,12,5) to path positions
  (1,0,3,0,2,4,4).
The result has 20 vertices, is simple, triangle-free and cubic, and so strictly
reduces the source order by two. Its full 30-edge table and full map are
stored in exterior-result.json. The path map is (0,15,17,6,9).
The simultaneous actual exterior labels are
  b=(0,27,27,15,6,6,6).
The full H-map is stored on its sorted vertex set. The consumer reconstructs
H and the replacement graph directly from graph22, verifies all maps and
all structural properties, then computes (2) as false. Positions one and
two have the same pin 27 and correspond to adjacent original cycle vertices.
Hence this particular map of the smaller cubic graph cannot lift while H
is kept fixed. No assertion of minimum order or lexicographic minimum among
all possible tuples is made. Both graphs are positive; no root nonmap follows.
The other 2,940 table separators need not themselves be realizable on this H;
only this separately checked witness claims actual exterior realizability.

## 6. Plateau pivot, new cycles, and an honest well-founded quantity

A flip of component 2 sends 1537 to 1539. The previous negative six-cycle
ceases to be monochromatic in its edge-class, but nu stays one. The new
shortest negative cycle has row indices (9,10,26,24,23,12), again in E0.
checked-systems.json contains every matrix row, rank, dependency witness
and the new negative cycle at each step. No count subtracts the old cycle
without recomputing cycles created by the move. Flipping component 5 next
sends 1539 to 1555 and nu becomes zero. It reconstructs a full B-map on all
22 vertices, independently checked on all 33 edges. The sequence is
  (1537,nu=1) -> (1539,nu=1) -> (1555,nu=0).

For the WHOLE chosen-cut a-state space, reverse breadth-first search from
all 34,216 zero states along every nonincreasing single-component move gives
a parent forest covering all 131,072 states. Its greatest depth is four;
depth counts are 34216,73808,22564,482,2 for depths 0..4. The complete parent
array is retained. The consumer checks every parent edge is a legitimate
single-component flip, recomputes nu on the entire domain, verifies nonincrease,
excludes parent cycles, and verifies every root is a zero-state.
Let d(a) be depth in this certified parent forest. Then the lexicographic
pair (nu(a),d(a)) decreases at every selected step: if nu falls the first
coordinate decreases, otherwise parent depth decreases by one. This proves
finite termination with a total map for this FIXED cut of this FIXED graph.
It does not assume that nu strictly falls at each step, and accounts for
all newly created fundamental cycles by recomputation.

For a GENERAL graph the analogous escape property of positive plateaus
has not been proved. Defining d as distance to a zero-state cannot itself
prove that a zero-state exists. A conditional theorem is valid: if every
positive level-connected plateau has an exit to a lower level, the finite
state graph has a zero-state and a lexicographic descent forest. Proving
that condition from the hypothetical nonmap minimality, or proving a weaker
existence result across cut changes, is the current missing lemma.
A one-vertex source s flip cannot preserve a maximum cut in a cubic graph:
its gain is odd and cannot be zero; maximality makes it negative. Multi-vertex
moves preserving maximum cut and reidentifying quotient components require
new analysis. Neither the fixture's plateau forest nor the C7 obstruction
closes this structural step.

## 7. Execution, mutations, dependencies and trusted request

Eight current bounded processes completed with exit zero: maximum-cut census,
a-state census, parent forest, C7/gadget interfaces, initial consumer, actual
exterior witness search, mutations/exterior consumer, and final consumer.
The final consumer adds direct source-to-quotient-cycle/port bridges and the
complete labeled smaller-core census; check_extremal_v1.py preserves the
first consumer's exact bytes. No earlier receipt is assigned to later code.
No solver, Lean process, or trusted verifier was used. CPython is 3.13.5;
seed zero; standard library; one CPU affinity; CPU soft/hard 35/36 seconds;
wall alarm 40 and supervisor 42 seconds; address space 512 MiB; 1 MiB regular
file/stream cap. Aggregate size is audited at artifact freeze (after exit),
not a claimed enforced aggregate filesystem quota. All input/code/output and
stdout/stderr SHA-256 values and actual start/end observations are retained.
There was one failed direct raw-file network read (name resolution) before
mathematical work; it is not a mathematical failure or a GitHub write denial.

Twenty-two negatives and five positives pass. They cover bad matrix source
rows, dropped parallel constraints, corrupt solutions/dependencies/maps,
nonmaximum cuts, falsely strict plateau steps, lost newly created cycles,
parent cycles/non-single moves/false roots, corrupt full boundary objects,
wrong exterior pins/ports/replacement edges/order drop, target mutation and
root-scope conflation. Positives include the actual two-step plateau path,
target translation, same-sign parallel rows, reversed edges and signed gauge.
The main consumer imports no producer or old generator. It uses direct binary
cut enumeration, original-coordinate GF(2) elimination, transfer/matrix list
relations and complete labeled graph masks rather than producer Gray updates,
signed union-find, walk generation and local search. This is implementation
separation, NOT a distinct registered verifier trust domain.

Dependency chain: fixed target/source -> maximum cut and exact matrix ->
complete nu/negative cycle -> exact source lift and Sigma -> bounded gadget
classification/noninclusion; complete nu + parent forest -> fixed-instance
termination. Infinite claims have the proofs and limits in Sections 1,4,6;
finite counts do not prove the original root. No novelty claim is made.
Executable replay and semantic/kernel review are requested separately; no
EvidenceLink, Result, Solution, truth record, schema, workflow, registry or
Harness file is edited. best_verified_result=none. The root remains open.
