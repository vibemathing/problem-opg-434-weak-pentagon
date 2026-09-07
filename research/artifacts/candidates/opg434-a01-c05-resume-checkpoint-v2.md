# OPG434 continuation checkpoint v2

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
Persistent Issue: #3 (reuse; do not create another)

## Last confirmed transport carried into this continuation

PRs #4–#7 were merged. Main was 64e6a1edc3cb43ac5664d6df800c3b6b9925adc3.
Current c05 branch: web/attempt-opg434-a01-c05-cubic-completion.
PR #8 was open at creation head 3409af1d9c4967b8bffc98c8a84a0edf7a0be626.
Packet: research/artifacts/web-inbox/opg434-a01-c05.packet.json.
Core candidate: research/artifacts/candidates/opg434-a01-c05-cubic-completion.md.
Core candidate SHA-256: 93785d22ccbddfc4036274319da426d3e7b74fff4ac9e61c535b2163b680f9d3.

The continuation requested PR-number/URL backfill and supplemental file writes. Their final commit hashes and exact-head CI state could not be confirmed from readable tool replies in this continuation. These are requested operations, not asserted successful writes. No merge of #8 was requested. No existing or future check result may be assigned to a different head.

## Supplemental paths to inspect, hash and audit

- research/artifacts/candidates/opg434-a01-c05-separator-preparation.md
- research/artifacts/candidates/opg434-a01-c05-path-signatures-preparation.md
- research/artifacts/candidates/opg434-a01-c05-domain-boundary-preparation.md
- this checkpoint

Their existence, current contents, blob SHAs and SHA-256 digests require fresh reads. No digest is invented here. They are preparations within the still-unconfirmed c05 transaction, not additional Web attempt packets or admitted new obligations. Before any merge, include all actually changed files in the diff audit.

## New paper derivations preserved in the requested preparations

1. Even-five-bit target: Z/A/N terminal-image types. Two-edge gluing fails for chosen side homomorphisms exactly for Z/A and A/Z. With all realizable side signatures, the only obstruction between two colorable pieces is opposite singleton signatures {Z} and {A}.
2. Path endpoint relations: length 0 gives Z; length 1 gives A; length 2 gives Z or N; length 3 gives A or N; every length at least 4 is unrestricted. Long degree-two threads can therefore be filled for arbitrary endpoint images. Minimum-order statements use the subcubic class, not cubic-only minimality.
3. A relation-and-witness induction gives H-colorability for triangle-free two-terminal series-parallel graphs as explicitly recursively defined, and excludes singleton equality at distinct terminals. No broader minor-closed equivalence or novelty claim was made.
4. K_{3,3} admits a proper surjective five-edge assignment satisfying deletion bipartiteness, but no proper assignment whose every color class is a complete-cut complement. Proof: such a class would be a nonempty matching cut; deleting any matching leaves K_{3,3} connected.
5. Explicit class-label tables give H-colorability for every triangle-free graph with vertex odd-cycle-transversal number at most two, without a degree assumption. One deleted vertex even gives a direct C5 homomorphism. Vertex deletion is not edge deletion.
6. Out-of-domain witness X: K5 with its six K2,3 edges kept short and the remaining four edges replaced by length-three paths. It has 13 vertices, 18 edges, maximum degree FOUR, ordinary girth FOUR, odd girth five, edge transversal number four, and vertex transversal number three. Three rainbow pentagons force three p-a_i colors into two choices; another pentagon gives the contradiction. Equivalently MaxCut(X)=14 implies five edge transversals require 20>18 edges. X is not a counterexample to the cubic problem and the subcubic completion must not be applied to it.
7. Extra hypothesis 5*tau_e(G)=|E(G)| forces every legal assignment in a cubic graph to be proper and normalized, by minimum transversals and the local maximal-cut flip argument. This is conditional, not an added assumption on the contract.

All of these remain generated paper arguments. No mathematical command, solver, exhaustive enumeration, kernel verification, EvidenceLink or Result is asserted. The arithmetic-check subsection of the domain-boundary preparation is a second proof argument, not a verifier-status designation; simplify that heading during audit to avoid any possible status ambiguity.

## Failed directions and blocker

Last-read admitted failed-route ledger was empty; no ledger write occurred. The rejected strengthenings above are supplemental candidate conclusions only. The admitted equivalence route is not declared dead.
Current operational blocker: unreadable final tool receipts prevent reliable confirmation of remote head, packet binding and exact-head checks. No HTTP status, permission change or quota exhaustion is inferred. The blocker is nonterminal and is not mathematical evidence.

## Unique next recovery action

Fresh-read Issue #3 and PR #8, the actual main ref, c05 packet and full changed-file list. Confirm or complete PR binding; inspect all supplemental contents and compute their digests from the retrieved bytes. Correct any status-ambiguous headings. Audit the candidate-only diff, then require web-attempt-packet, web-harness-snapshot and web-pr-diff-boundary on the exact final head. Only then self-review and squash merge under protection. Append confirmed head/check/merge receipts to Issue #3.

After merge, fresh-read main, the two open obligations, evidence links and existing packets. Create a new unique branch from that real main and ONE new immutable packet freezing the separator/path/domain-boundary claims selected for audit. Do not duplicate c01–c04, create a second Issue, use a stale base forever, or promote any transport event to mathematical evidence.
