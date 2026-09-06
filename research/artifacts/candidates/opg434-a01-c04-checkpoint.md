# OPG434 c04 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c04-formal-interface
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 1c0918daa98e45a7f96cb70dcee9c8e0ef9d0623
branch: web/attempt-opg434-a01-c04-formal-interface
packet: research/artifacts/web-inbox/opg434-a01-c04.packet.json
pull_request: not created when this checkpoint was frozen
required_checks: not yet observed for this branch

## Artifact
- research/artifacts/candidates/opg434-a01-c04-formal-interface.md
  SHA-256: 1b82897e16e02aa36f82bb7b6f31634c913b71a3d873db5f1169a59ed94a28a6

## Progress and limitations
A spanning-forest parity proof exactly recognizes complete cuts.
Four parity conditions per fundamental cycle suffice for normalized colorings.
An explicit proper coloring of an 8-vertex theta graph shows why hitting every
basis cycle is not an original-coloring verifier. This witness is subcubic,
not cubic, and is not a root counterexample.
The formalization interface keeps concrete cycle coverage and bipartiteness
as explicit unimplemented bridge requirements. A vacuous abstract-cycle
countermodel explains the remaining statement-faithfulness risk.
No Lean installation probe, code execution or kernel result is claimed.

## Open obligations and next action
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

Finish c04 transport, then fresh-read main and study a domain-faithful cubic
completion of triangle-free subcubic graphs. Check both coloring directions
and distinguish preservation of triangle-freeness from preservation of girth.
c03 merged as PR #6, commit 1c0918daa98e45a7f96cb70dcee9c8e0ef9d0623; all three transport checks passed.
Further status belongs to Issue #3. No truth records changed.
