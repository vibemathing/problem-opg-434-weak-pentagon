# R09: rechecked belt interfaces, structural-inevitability obstruction, global continuation

candidate_id: candidate:opg434-a01-root-global-20260907-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
primary_owner: math-proof
base_revision: 798cdf4f220a7c419a07e937507ebc5f5f5cb0fd

## 1. Actual input and finite-interface rechecks

The five user-supplied belt documents were read in full. All 57 non-self
manifest entries of the supplied 58-file ZIP matched their byte counts and
SHA-256. Its reported R11 and R12 domains were not accepted by count alone.
Four new bounded executions consumed its actual witnesses, checked mutations,
and checked lifting controls. No h1, C10 or older archive was reconstructed.

R11: 3840/3840 normalized positive tuples, 53760 internal edge and 15360 pin
edge checks, first_failure=null. R12: 57600/57600, 864000 internal edge and
288000 pin edge checks, first_failure=null. The excluded normalized counts
are 256 and 7936. These negatives follow from actual internal port edges
and triangle-freeness of the target, not an assumed converse.

The attached generator uses bit-domain CSP propagation/backtracking. The
consumer uses coordinate subsets, Hamming distance four and separately
transcribed source adjacency lists; it imports no generator. It checks every
pin and internal edge, duplicates, missing states and all translations.
Its SHA-256 is b61b76351ce52879871d81ca6b1f614b53df4cf2e6c015272e30965d9853fe9d.
Twenty-four negative controls and four positive controls passed. Finite
lifting controls covered 73/1008 exterior configurations; they do not replace
the arbitrary-exterior proof below. All four current replay processes exited 0.

The fresh existing branch head was 732b463f6df20527c06f092bb0b78ef1c8783518,
not the older 61b4070 head. It contains another implementation under
opg434-a01-belt-interfaces-20260907-v2, with compressed full witness tables
and its own recorded runs. These variants have DIFFERENT bytes and mutation
counts: attachment 24+4, remote variant 22+2. This report does not assign a
receipt for one variant to the other. Existing remote artifacts are reused.
The replay bundle retains the current attachment-consumer source, specification,
run results and receipts. Exact witness inputs remain bound by the original
attachment manifest; generate.py is retained to reproduce its deterministic
rows, while the separate checker must consume and check those rows.

## 2. Self-contained lifting statement

All graphs are finite, simple and undirected. B consists of the 16 even
vectors of F_2^5; t_i=J+e_i, i=0,...,4, are its five edge differences.
The only nonempty subset of the t_i summing to zero is the whole set of
five. In particular B has no closed three-step walk. Its three-edge-path
endpoint relation is exactly inequality: difference t_i is realized by
(t_i,t_j,t_j), and difference e_a+e_b by the three complementary generators.
These exhaust its nonzero even differences. Repeated images are allowed.

Both patches have cycle v0-v1-v2-v3-v4-v0 and spokes v0-x0,v2-x2,v3-x3,v4-x4.
P11 adds y-x2,y-x3,y-x4,t-x4,t-x0, has 11 vertices/14 edges, and ordered ports
(x0,x2,x3,t). P12 adds r-x2,r-x3,z-x3,z-x4,t-x4,t-x0, has 12 vertices/15 edges,
and ports (x0,x2,r,z,t). A port pin is the image of its EXTERIOR neighbor.
The exact finite relations certified above are
R11(a,b,c,d) iff a!=d;
R12(a,b,c,d,e) iff a!=e and b!=c.
Translation by a reduces to first pin zero and preserves all edges. Thus
3840 and 57600 cover the entire respective finite domains, not samples.
Necessity uses the length-three paths through internal edges x0-t and x2-r;
sufficiency uses the complete positive rows, with R12 checked separately.

Suppose an induced P11 in G has exactly one outgoing edge at each port and
no others. Put H=G-V(P11), and call the outside endpoints uA,uB,uC,uD.
They may coincide except uA!=uD: otherwise uA-x0-t-uA is a triangle.
Add two fresh vertices p,q and path uA-p-q-uD to H, obtaining G'.
Every new edge has a fresh endpoint, so no loop or repeated edge is created.
A triangle on old vertices was already in H. One using p or q would force
uA=uD. An old edge uA-uD creates a four-cycle, which is permitted.
At every exterior vertex the new incidences are paid for by its removed
port incidences, including multiplicities from endpoint coincidences;
p,q have degree two. Hence G' is subcubic and |V(G')|=|V(G)|-9.

For every h:H->B, h extends to G exactly when h(uA)!=h(uD), by R11;
it extends to G' under precisely the same condition, by the path relation.
For any given G' map, normalize its pins, use the witness row, undo the
translation and restore the patch without changing h. All internal,
external and crossing edges are covered. The reverse extension uses the
three-step walk. Thus the whole SET of extendible exterior maps is preserved.
This is not a claim that every exterior map extends to either graph.

For P12, allow any subset of its five outgoing edges, at most one per port,
and no other outgoing edge. Replace a pair by a fresh three-edge path only
when both ports in (x0,t), respectively (x2,r), are active. The endpoints
within either active pair are physically distinct by triangle-freeness.
New interiors of the two paths are disjoint; cross-pair OLD coincidences
are allowed. Each added old incidence is charged to a removed incidence.
No fresh triangle is possible. For m paths, order drops by 12-2m>=8.
Complete missing pins by differing from their partners, or use any unequal
pair if both are absent; a missing z pin is arbitrary. The two pairs are
disjoint, so these choices do not conflict. R12 proves for EVERY h:H->B the
same extension equivalence. Five active ports give a drop of eight; with
four ports a missing z gives eight and another missing port gives ten.

Neither replacement preserves cubic regularity, girth>=5 or connectivity.
Indeed v1 has degree two under the occurrence hypotheses, so these exact
occurrences cannot occur in a cubic graph directly. The valid minimality
class is ALL triangle-free subcubic graphs. If the cubic root fails, that
class has a vertex-minimum non-B-map. Each replacement is smaller in the
same class, so its colorability lifts and excludes the occurrence there.
This does not prove that such a minimum must contain either occurrence.
The strictly decreasing vertex count proves reduction termination, not
colorability of every terminal graph.

## 3. Precise structural route that fails

Tested auxiliary statement S: every finite connected simple nonbipartite
cubic graph of girth at least five which is 3-vertex-connected and has only
trivial 3-edge-cuts contains a pentagon (and hence can start a pentagon-belt
reduction). S is false. The witness has vertices Z/24, a Hamiltonian cycle,
and chords i -> i+(-12,7,-7)[i mod 3], modulo 24.

The twelve distinct chord pairs are
(0,12),(1,8),(2,19),(3,15),(4,11),(5,22),(6,18),(7,14),(9,21),(10,17),(13,20),(16,23).
Together with all consecutive cycle edges these specify the entire graph.
A seven-cycle is (0,1,2,3,4,11,12). The complete finite control finds girth
exactly seven, so there is no pentagon or P11/P12. The graph is cubic.
All 24 one-vertex and 276 two-vertex deletions preserve connectivity.
The generator's edge-pair/Tarjan check and a separate exhaustive deletion
checker agree: among all 7806 edge subsets of sizes one through three,
exactly the 24 vertex stars disconnect. The separate girth check uses
shortest paths with one edge deleted, not the generator's cycle enumeration.

An explicit B-map on vertices 0,...,23 is
[0,15,0,15,17,6,24,5,18,12,27,6,27,5,10,17,10,20,3,29,10,23,9,23].
All 36 edges pass the subset/Hamming check. Therefore this is NOT a root
counterexample and NOT a counterexample to an implication having the premise
'G is a minimum non-B-mappable graph'. It defeats only deriving inevitability
from S's stated structural properties. The stronger minimum-counterexample
implication remains open; non-B-mappability must do essential additional work.
No smallest-order assertion about this witness is made.

## 4. Immediate global pivot: exact simultaneous constraints

For a connected graph G choose any spanning tree T and root r. Assign each
tree edge one generator t_i. Define x(r)=0 and x(v) as the sum on its unique
root path. A B-map exists iff the tree generators can be chosen so that
for EVERY chord uv, the sum on the T-path from u to v is a generator.
Necessity follows from edge differences of a map normalized at r. For
sufficiency the path potentials give valid tree edges and the simultaneous
chord conditions give every remaining edge. This is an exact finite-domain
system with n-1 five-valued variables and m-n+1 chord constraints. The
constraints must hold simultaneously; one choice per constraint is invalid.
For disconnected G work separately on each component.

Equivalently, assign generator colors to all edges. Potential integrability
holds iff the XOR on every fundamental cycle is zero. The only generator
relation implies that on each such cycle all five color-count parities are
equal; their common value is the cycle length modulo two. A spanning-tree
potential proves the cycle-basis criterion in both directions. This is an
encoding of B-maps/normalized existence, not preservation of every arbitrary
original legal five-edge coloring. No new equivalence or novelty is claimed.

The explicit global CNF uses X[v,a] for all 16 labels, exactly one per
vertex, and for each directed version of an edge uv and every a the clause
not X[u,a] OR (OR_{b adjacent a} X[v,b]). A root-zero unit clause removes
translation only. Exactly-one and these clauses are satisfied iff the
selected labels form a B-map; each direction is direct substitution.
Our 24-vertex fixture has 384 variables, 4057 clauses, 23 spanning-tree
edges and 13 chord constraints. Its total-map witness satisfies ALL clauses
and every fundamental-cycle parity equation. A second implementation
reconstructs the complete expected clause set and checks equality with the
actual DIMACS plus the complete assignment, not just a few clauses.
No SAT-solver UNSAT or universal graph-family result is inferred from this
positive finite fixture. It starts a global search lane retaining exterior
state correlations instead of assuming arbitrary local repair.

## 5. Execution and state

The four fresh belt replays and the two new global runs all exited 0 under
CPython 3.13.5, deterministic seed zero, standard library only. Bounds:
one CPU affinity, CPU soft/hard 35/36 seconds, wall 40 seconds, address space
512 MiB, regular-file size 1 MiB. Stream caps and aggregate output counts
are checked after exit, not claimed as enforced aggregate filesystem quotas.
Each code/input/output and stdout/stderr has a stored SHA-256. The global
producer used 16 search nodes; the verifier imports none of its core logic.
This algorithm separation is not verifier trust-domain separation.

A bounded decoder restores the bundled text and fixed DIMACS recipe and
checks each exact raw file hash. The recipe is lossless for this frozen
file, not an alternative solver. No raw host paths, session identifiers,
credentials or hidden reasoning are included. Existing packet and branch
are reused; only one inbox packet is permitted in the final PR.

Source comparison is stored separately. DeVos-Samal's primary abstract
states maximum degree three and ordinary girth at least 17 suffices for a
B-map. Importing that theorem would bound a putative counterexample's girth
by 16, not force girth five. We did not replay its computer-assisted proof.
C12's square exclusion, if accepted, gives the lower bound five. Thus
lengths 6,...,16 cannot be dropped on a false inevitability premise.

R11/R12 first failed allowed state: null/null. First open structural lemma:
use the genuinely non-B-mappable minimality premise to obtain a suitable
unavoidable reduction or simultaneous global chord assignment for every
remaining graph, including pentagon-free cases. Neither S's counterexample
nor finite table success discharges this. Next: global boundary/CSP study
on short-cycle minimal candidates, with a fixed full-source certificate on
any proposed negative instance. No trusted closure, EvidenceLink, Result or
Solution was produced; best_verified_result=none.
