# OPG434 c03 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c03-certificates
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 3f43a8cfbd895f55be52d2219c25727a93c9e154
branch: web/attempt-opg434-a01-c03-certificates
packet: research/artifacts/web-inbox/opg434-a01-c03.packet.json
pull_request: not created when this checkpoint was frozen
required_checks: not yet observed for this branch

## Artifact
- research/artifacts/candidates/opg434-a01-c03-certificates.md
  SHA-256: f2ff682510e26210e0d4b89233209f18e386f1674439cb30d9cb95e6edb86243

## Progress
The fixed-coloring certificate is exactly five vertex bipartitions;
a failed fixed coloring has a missing-color odd-cycle witness.
Two existence encodings are proved on paper:
5(n+m) Boolean variables with 21m clauses, or 4(n+m) variables with 22m clauses.
The 10-vertex pentagonal prism defeats omission of the fifth fixed-coloring test.
No BFS, SAT solver, generated-instance enumeration or kernel was executed.

## Open obligations
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

## Next action
Complete c03 transport. Then fresh-read main and produce a portable formalization
interface for the target equivalence, explicitly separating the pure logical
argument from the concrete graph/no-odd-cycle bridge and its future verification.
Retain candidate_only; do not promote positive CI or an unexecuted Lean file.
c02 merged as PR #5, commit 3f43a8cfbd895f55be52d2219c25727a93c9e154; its three transport checks passed.
All further coordination checkpoints go to Issue #3.
