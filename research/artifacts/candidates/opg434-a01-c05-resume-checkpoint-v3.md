# OPG434 continuation checkpoint v3

verdict: candidate_only
state: nonterminal
best_verified_result: none
best_verified_candidate: none
primary_owner: math-derivation

Repository: vibemathing/problem-opg-434-weak-pentagon
Problem: problem:opg-434-weak-pentagon
ProblemContract SHA-256: 60124bd981c32b7e5ba91955bbdaa76e2dfebf984722e144a589fceace0f7ba5
Harness: 1.1.2
Harness snapshot SHA-256: f7c2791de06bb0581e1e591b73638e70206fb34a0ff7282925627607be8d8a7a
Attempt: attempt:web-20260906-opg434-a01
Route: route:odd-cycle-transversal-equivalence-v1
Graph: graph:opg434-initial-v1
Open obligations: obligation:opg434-five-transversals-equivalence; obligation:opg434-root
Persistent Issue: #3. Reuse it; do not create another research Issue.

## Confirmed history versus current uncertainty

The last confirmed history carried into this continuation is: PRs #4–#7 merged; main 64e6a1edc3cb43ac5664d6df800c3b6b9925adc3; c05 PR #8 open on web/attempt-opg434-a01-c05-cubic-completion at creation head 3409af1d9c4967b8bffc98c8a84a0edf7a0be626.

Core c05 candidate: research/artifacts/candidates/opg434-a01-c05-cubic-completion.md.
Core SHA-256: 93785d22ccbddfc4036274319da426d3e7b74fff4ac9e61c535b2163b680f9d3.
Packet: research/artifacts/web-inbox/opg434-a01-c05.packet.json.
A PR-number/URL backfill to #8 was requested using the previously read packet blob 76410723822c9e04d9a8794b4811e6fc2df491fe. Its success, subsequent commit hashes, current main and all exact-head check results remain unconfirmed in readable outputs.

The continuation repeatedly attempted read-only recovery through the connected GitHub tools, the known response resource, and the public GitHub API. Their return bodies were not readable in this continuation. No HTTP status, permission change, missing object, quota exhaustion, or successful write is inferred from that presentation failure. A local JSON-decoding recovery attempt was not a mathematical computation or verifier run. No merge of PR #8 was requested.

All supplemental file/comment writes below are REQUESTED OPERATIONS until confirmed by fresh reads. Do not assign a stale successful CI result to a later head. Do not report these requested writes as committed merely because their content is described here.

## Supplemental paths to recover and hash

Previously requested preparations:

- research/artifacts/candidates/opg434-a01-c05-separator-preparation.md
- research/artifacts/candidates/opg434-a01-c05-path-signatures-preparation.md
- research/artifacts/candidates/opg434-a01-c05-domain-boundary-preparation.md
- research/artifacts/candidates/opg434-a01-c05-bipartite-and-subdivision-preparation.md
- research/artifacts/candidates/opg434-a01-c05-three-port-preparation.md
- research/artifacts/candidates/opg434-a01-c05-resume-checkpoint-v2.md

Newly requested preparations:

- research/artifacts/candidates/opg434-a01-c05-petersen-signatures-preparation.md
- research/artifacts/candidates/opg434-a01-c05-petersen-coloring-benchmark.md
- research/artifacts/candidates/opg434-a01-c05-general-port-certificate-preparation.md
- research/artifacts/candidates/opg434-a01-c05-equivalence-preparation.lean
- research/artifacts/candidates/opg434-a01-c05-equivalence-preparation-audit.md
- this checkpoint

Their current existence, contents, blob identifiers and SHA-256 digests are unconfirmed; no synthetic digest is supplied. They are supplemental preparations in an unresolved c05 transaction, not additional Web attempt packets or newly admitted obligations. Include every actual changed file in the eventual diff audit. Simplify the alternate-counting subsection heading in the domain-boundary preparation to 'Second counting argument' when its actual blob is available; it was intended to denote a second paper proof, not any verifier status.

## Best current paper candidates, none externally verified

The c01–c04 candidates remain the previously transported foundation: exact fixed-coloring equivalence; cut-complement normalization and even-five-bit target; fixed-coloring positive/negative certificates and CNF interfaces; cycle-space/actual-graph formalization interface.

The c05 core preserves arbitrary fixed legal colors under the at-most-eightfold subcubic-to-cubic completion. It preserves odd girth but not ordinary girth. It is not a universal existence proof.

Earlier supplemental progress includes exact two-port and three-port target alignment; universal path relation from length four; bipartite terminal relations by distance; explicitly defined two-terminal series-parallel graphs and subdivisions of K4/K3,n; vertex odd-cycle transversal at most two; and the carefully OUT-OF-DOMAIN 13-vertex maximum-degree-four obstruction. The K3,3 proper-normalization obstruction concerns an extra requirement, not the frozen problem. The root remains open.

New exact finite candidates:

1. Let P be the graph on two-subsets of [5] with disjoint pairs adjacent, and M=P minus one vertex. With three ordered degree-two ports, every H homomorphism of M is, up to a target automorphism, a fixed induced six-cycle plus three binary choices n_i4 or n_i5. Its terminal graph is exactly an edgeless triple or a two-edge path, with any center; never a single edge plus an isolated port.
2. Let D=P minus one edge, with the edge endpoints as terminals. Its exact terminal relation is universal: same, adjacent and distinct nonadjacent target images all occur. Thus it cannot force terminal equality. A copy attached by one external edge at each terminal can be filled for arbitrary outside images and is a reducible configuration for a minimum-order hypothetical subcubic counterexample.
3. Symbolic counts: 7680 maps M->H; 7680 maps D->H; for fixed terminal pairs of D there are 120 extensions for an equal pair and 24 each for an adjacent or distinct nonadjacent pair. P has 1920 maps to H.
4. P has exactly twelve pentagons, four through each edge, so its minimum edge transversal size is three. Every legal five-edge assignment is proper and normalized. There are exactly 120 legal labeled assignments, precisely global permutations of the missing-element coloring. P has no homomorphism to C5. For the unbroken c03 five-bipartition encoding the predicted model count is 3840; for the four-bit target encoding it is 1920 when its auxiliary variables are uniquely fixed. These are paper-derived expected values, NOT observed solver counts.
5. All automorphisms of H are even translations followed by coordinate permutations. Arbitrary fixed boundary-tuple alignment has a 120-permutation criterion: normalize at the first port, form w_j=d_j+pi(e_j), reject weight-four values, and require one common coordinate in all nonzero weight-two supports. A positive certificate is pi and that coordinate. A negative certificate gives a verified small rejection witness for each of all 120 permutations. This is not a graph-uncolorability certificate when the side maps can change.
6. A square with four leaves gives a simultaneous-extension failure despite separately satisfiable length-three boundary paths. Prescribed leaf labels (0,n_12,s_5,n_34) force all four spoke generator indices to be 5, while every consecutive pair must be distinct. The graph itself is bipartite and colorable; only those boundary labels fail.
7. The new Lean file defines symmetric loopless graphs, symmetric five-edge assignments, retained spanning graphs and actual cyclic vertex sequences. It supplies conditional proofs of the fixed-color equivalence and unique fiber membership. Its BipartiteCycleCriterion parameter is explicitly UNRESOLVED. It has not been built; the graph-library transport, finite canonical wrapper, unordered-edge quotient, color-label renaming, criterion theorem and axiom audit still need verification. A build of the conditional file would not by itself close the target.

No mathematical command, solver, exhaustive search, Lean build, axiom-audit receipt, EvidenceLink or Result has been produced in this continuation. All model counts and finite tables above are paper derivations. The admitted failed-route ledger was last read empty and was not changed. Failed strengthenings are only candidate-level negative knowledge, not newly registered failed-route IDs.

## Unique next recovery action

Fresh-read Issue #3 and comments, PR #8, real main, c05 packet, and the complete changed-file list. Confirm which requested writes actually exist before retrying any creation. Complete PR binding only after reading its actual blob. Audit and hash all actual supplemental files; correct only candidate-path defects. Obtain web-attempt-packet, web-harness-snapshot and web-pr-diff-boundary on the exact final head, self-review without elevating evidence, and squash merge only when protection permits it. Append the real head/check/merge receipts to Issue #3.

Then immediately read the new main, open obligations, evidence links and prior packets, create a new unique web/attempt-* branch from that actual main, and ONE new immutable packet freezing a bounded selection of the supplemental results. The finite Petersen oracle or the conditional Lean interface are precise next verification targets. Do not duplicate the existing Issue, reuse stale base forever, invent supplemental hashes, treat the degree-four witness as cubic, or treat a conditional theorem parameter as already discharged.
