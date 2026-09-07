# R11 and R12: complete boundary certificates and smaller-graph lifting

candidate_id: candidate:opg434-a01-belt-interfaces-20260907-v2
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
primary_owner: math-proof
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
base_revision: 798cdf4f220a7c419a07e937507ebc5f5f5cb0fd

## 1. Fixed source and exact statement

The resumed branch was found at 61b40705084eee400b482ff9129c32928ba5a576.
Its sole extra file was the conditional lifting candidate
research/artifacts/candidates/opg434-a01-belt-lifting-20260907-v1.md,
Git blob cf8edb6174d1cff87a3df835a8f724bbc502ba84. That file is retained unchanged.
It did not contain a boundary table or execution receipt. PRs 27 and 28 are
merged; the earlier h=1 archives are not reconstructed or rerun here.

The source of both patches is C16 at this fixed main, Git blob
01b713dbc49407a86e61180d862766bcae81bd06. patches.json freezes the literal
vertex orders, edge tables, port orders and proposed predicates. Its SHA-256 is
8a0701c13fa235e3190ead9a9c10072469acd3b0f8c9a4e34a6ddc0a97da9d56.
The separately written checker reconstructs named edges to compare this input
with the stated C16 configurations, rather than silently accepting missing edges.

B consists of the even vectors of F_2^5. Adjacency is difference t_i=J+e_i,
i=0,...,4. The generator masks are (30,29,27,23,15). A B-map need not be
injective, and no proper edge-coloring condition is added. Target names s_1,...,s_5
in earlier files correspond to t_0,...,t_4 by shifting the index, not the graph.

R11(a,b,c,d) means existence of a complete internal B-map of the eleven-vertex
patch with an extra prescribed neighbor at each ordered port (x0,x2,x3,t).
R12(a,b,c,d,e) uses the twelve-vertex patch with ordered ports (x0,x2,r,z,t).
Pins are target labels; repetitions are allowed. Each actual outside vertex
retains a single label when several physical endpoints coincide.

### claim:opg434-belt-r11-exact
For every a,b,c,d in B, R11(a,b,c,d) iff a != d.

### claim:opg434-belt-r12-exact
For every a,b,c,d,e in B, R12(a,b,c,d,e) iff a != e and b != c.

These are finite certificate-backed candidate lemmas, not trusted admissions.
They were checked separately; R12 is not inferred from R11.

## 2. Necessity, normalization, and the finite proof bridge

The generator relation has no nonempty vanishing proper subset, so B has no
closed three-step walk. A three-edge path therefore cannot have equal images
at its endpoints. Conversely every distinct pair is realizable: a difference
t_i uses (t_i,t_j,t_j), while p_ab=e_a+e_b uses the three generators indexed
by the complement of {a,b}. Thus its exact endpoint relation is inequality.

The internal edge x0-t in R11 gives the path a-x0-t-d and forces a!=d.
For R12, edges x0-t and x2-r give a!=e and b!=c. The checker confirms that
these edges are actually present, and computes the three-step relation from
its separately constructed target. It obtains all 240 ordered unequal pairs
and no equal pair. Thus excluded tuples are ruled out by actual source edges,
not by taking the proposed sufficient conditions as definitions.

Translation by any even vector preserves target adjacency. Translate all
labels by a to set the first pin to zero; after finding an internal map,
translate it back. This covers every original tuple without restrictions on
coincident pin labels. The checker tests all 16 translations on all target
pairs. The only normalized universes are 16^3=4096 and 16^4=65536 tuples.

For each allowed tuple the retained table contains one label for EVERY
internal vertex. In vertex order from patches.json, a row contains 11 or 12
lowercase hexadecimal target indices and a line feed. Target indices enumerate
the increasing even masks (0,3,5,6,9,10,12,15,17,18,20,23,24,27,29,30).
Rows are in lexicographic order of (0,b,c,d) or (0,b,c,d,e), retaining exactly
the displayed inequalities. This is a per-state witness, not just a pass count.

For R11 the checker visits all 4096 normalized tuples: 3840 positive rows,
256 negative tuples, 53760 internal-edge tests and 15360 pin-edge tests.
For R12 it visits all 65536 tuples: 57600 positive rows, 7936 negative tuples,
864000 internal-edge tests and 288000 pin-edge tests. No allowed tuple fails.
For excluded tuples it verifies the stated path obstruction separately.

The search uses integer bit domains and arc consistency, then branching.
It saves 85 / 785 representative witnesses and expands coordinate permutations.
The checker imports no search module. It constructs B as coordinate sets,
uses symmetric-difference cardinality four for adjacency, reconstructs the
named source edges, and checks every row directly. Consequently its positive
conclusion does not depend on the correctness or completeness of search pruning
or on trusting an orbit-count formula. Complete row coverage plus valid
witnesses supplies the existential proof for every tuple.

Raw table SHA-256:
R11: 9312539a11c20351d2c964ce6982f90c29385d448c9699fdfdab6361aa98c9a8 (46080 bytes).
R12: c8b6bdbf778b20dead848708aa118c55e69b863453820bfc7754d9128690ae08 (748800 bytes).

For a concrete R11 row, pins (0,0,0,3) have internal mask labels
(0,15,17,10,23,15,15,29,9,18,20).
For R12, pins (0,0,3,0,3) have labels
(0,15,17,12,23,15,15,3,9,20,30,20).
These examples emphasize that distinct pins are NOT being assumed; the full
tables, rather than these examples alone, prove sufficiency.

## 3. Universal eleven-vertex lifting

### claim:opg434-belt-r11-lifting
Let G be finite, simple, triangle-free and subcubic. Suppose it contains the
INDUCED eleven-vertex patch, with exactly one exiting edge at each of its four
ports and no other exiting edges. In particular v1 has total degree two.
Write their outside endpoints uA,uB,uC,uT, allowing other coincidences.
Since x0-t is an internal edge, uA=uT would create the source triangle
uA-x0-t-uA. Hence uA and uT are distinct physical vertices.

Delete the patch. Add fresh vertices p,q and edges uA-p,p-q,q-uT, obtaining G'.
The order decreases by exactly 11-2=9. Each exterior vertex loses one incidence
for every removed exiting edge and gains no more than the number of those
incidences. This remains true when other outside endpoints coincide.
The two fresh vertices have degree two. Thus G' remains subcubic.

Fresh interiors prevent loops, duplicate edges, or unintended intersections.
A triangle in the old exterior would already be in G. A triangle containing
p or q would require uA=uT, since their only neighbors are specified by the
three-edge path. This is excluded. An old exterior edge uA-uT makes a
four-cycle, which is permitted in the required triangle-free class.

Now take ANY map g:G'->B. The new three-edge path forces g(uA)!=g(uT).
Apply R11 to the tuple (g(uA),g(uB),g(uC),g(uT)). Keep g on the ENTIRE
exterior, remove p,q, and use the resulting eleven-label internal witness.
The edge partition into exterior, internal and exiting edges proves that
this union is a B-map of G. No further exterior change is necessary.

Conversely, any B-map of G forces its two critical outside labels to differ,
so the exact three-edge-path relation extends its exterior restriction to G'.
Thus these two graphs have exactly the same feasible exterior restrictions,
not merely an implication for one selected exterior map.

Minimality must be over ALL finite simple triangle-free subcubic graphs.
Neither cubicity, girth at least five, nor three-connectivity is promised for
G'. Minimality in any of those narrower classes would not justify the step.
The well-founded measure for a repeated applicable reduction is vertex count,
which strictly drops by nine; deleting a patch is not by itself a root proof.

## 4. Universal twelve-vertex lifting, with missing ports

### claim:opg434-belt-r12-lifting
Suppose the induced twelve-vertex patch has only the indicated exiting edges,
at most one at each of its five possible ports. The C16 use has four or five.
Call a port present when its exiting edge is present. For each complete
critical pair (x0,t) or (x2,r), replace the pair of exits by a fresh three-edge
path between its two outside endpoints after deleting the patch. Use disjoint
new interiors for different paths. Their endpoints are distinct WITHIN each
pair, by the same triangle argument as above. Cross-pair coincidences are allowed.

If q is the number of complete critical pairs, this adds 2q<=4 vertices;
order drops by 12-2q>=8. Each new exterior incidence is paid for by a distinct
removed incidence. Even if both paths join the same two outside vertices,
their new interiors are distinct: the graph is simple and the resulting
six-cycle is not a triangle. Every possible triangle containing a fresh
vertex would force equality within its own critical pair. Old exterior
triangles cannot appear. Hence G' is again simple, triangle-free and subcubic.

Any B-map of G' satisfies the inequality for each complete pair. Supply
fictitious labels at missing pins as follows: if one endpoint of a critical
pair is missing, choose its label different from its present mate; if both
are missing, choose two distinct labels. These choices do not interact,
since the pairs are disjoint positions. A missing z-pin is arbitrary.
Apply the independently checked R12 relation to the completed five-tuple,
and retain only actual exiting constraints. This lifts the exterior map.
Conversely an original map satisfies each present critical inequality and
extends across each new path separately. Feasible exterior restrictions
are therefore preserved in both directions, including all endpoint coincidences.

With four or five exiting edges, q is one or two, so the actual reductions
are by ten or eight vertices. The exact two-inequality relation, not just
its necessary half and not the R11 table, is essential here.

## 5. Adversarial and structural controls

For EACH table eleven negative mutations are rejected: remove a row; add a
row; collapse an internal edge in a witness; set the first port equal to its
pin; corrupt a delimiter; use a non-target token; exchange ordered ports;
omit the internal necessity edge; insert an extra patch edge; change the
boundary predicate; and change a target generator. Two positive controls
translate pins and witness together, each checking all sixteen translations.
These 22 rejections and two acceptances have actual recorded outcomes.
They are corrupted-certificate controls, not counterexamples to the two lemmas.

An additional structural enumerator checks all boundary-vertex identifications
and all permitted exterior edges on those vertices, for the stated four/five
exit patterns. It checks 73 admissible R11 hosts and 852 R12 hosts. Of these,
36 / 434 have endpoint coincidences, and 63 / 778 have exterior edges.
All R11 cases drop nine vertices; 560 R12 cases drop eight and 292 drop ten.

A deliberate direct-edge replacement instead of a three-edge path fails when
the critical outside vertices already share an exterior neighbor: it creates
a triangle. The proper three-edge replacement passes that control and the
old-endpoint-edge control. These finite cases pressure-test, but do not replace,
the universal degree and triangle proofs in Sections 3 and 4.

## 6. What this changes about the root, and what stays open

Conditional on the earlier C14/C16 candidate reductions, the surviving
one-deficiency pentagon belts are now reducible. C14 permits at most one
degree-two vertex on a pentagon in the chosen minimum; C16 reduces the
one-degree-two case to these two induced patches. The new lifting theorems
exclude both. Thus the candidate dependency chain implies that every vertex
on a pentagon of that hypothetical minimum has degree three.

This consequence still depends on those earlier candidate proofs; no trusted
evidence for them is synthesized here. A minimum graph with an all-degree-three
pentagon, or a graph without pentagons, has not been excluded. The root is open.

The layered family excludes uniformly local or bounded-edit repair of EVERY
given exterior map. It does not exclude coloring a smaller graph globally
afresh and then lifting. That auxiliary failure is proposed only in candidate
metadata; research/records/failed-routes.jsonl remains untouched.

Next boundary: determine a genuinely reducible all-degree-three pentagon
patch, starting with its five distinct outside ports and possible common-
neighbor belts, while retaining hub coincidences and missing/extra edges.
For an actual exterior H, the goal is Sigma(H) intersect R5 nonempty, where
Sigma ranges over ALL exterior maps. A failure of one fixed tuple is not root
nonexistence. No high-girth case or global state-selection theorem is closed.

## 7. Execution, reproducibility and assurance

Six actual bounded child processes (R11 generation/check, R12 generation/check,
mutations, lifting stress) exit zero under CPython 3.13.5, standard library,
seed 0, one-core affinity, CPU 35/36 seconds, wall 42 seconds, 512 MiB address
space and a 1 MiB per-file/stream limit. The 5 MiB total-output budget is
checked after exit, not enforced by a filesystem quota. Run receipts preserve
commands, input/output bytes and hashes, stdout/stderr hashes and actual times.
No timeout or UNKNOWN is accepted. Same generating trust domain throughout.

certificates.bundle.json retains 26 logical output/receipt/template files.
restore_certificates.py expands each ordered coordinate-permutation template
without CSP search and reconstructs the exact full row files above; their
byte lengths and SHA-256 must match. This expansion was actually executed.
It is a lossless table representation, not a fresh mathematical search.
The generator, checker, mutation code, structure checker and wrapper are
separate directly readable source files. No h=1 reconstruction is involved.

From this candidate directory in an authorized scoped runtime:
python restore_certificates.py --out decoded
python check_interfaces.py --spec patches.json --patch r11 --table decoded/r11/r11.witnesses.txt --out check-r11.json
python check_interfaces.py --spec patches.json --patch r12 --table decoded/r12/r12.witnesses.txt --out check-r12.json
Use run_bounded.py for each computation; verifier_request.json supplies the
required separation, limits and further semantic review. It is a request,
not a receipt from a registered verifier. CI and merge check transport only.

best_verified_candidate=none; best_verified_result=none.
No EvidenceLink, Result, Solution, truth record, schema, Harness or workflow is changed.
