# C11 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c11-degree-budget
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: bcbe66a0033c7853a9589c59365f42bc7b72a1d5
branch: web/attempt-opg434-a01-c11-degree-budget
packet: research/artifacts/web-inbox/opg434-a01-c11.packet.json
pull_request: not yet created at checkpoint freeze
required_checks: not yet observed on this branch

## Artifacts
- research/artifacts/candidates/opg434-a01-c11-degree-budget.md
  SHA-256: effd1e2b82efe2ab81ebdabcd09ac45fe56b4ba8ca19484c1ce4080f40ea3110
- research/artifacts/candidates/opg434-a01-c11-obstruction.json
  SHA-256: b021a452eacee1d0b4f9f9fd768010b05df6c987fda9ba9c1c3ecb467b4d314d
- research/artifacts/source-notes/opg434-a01-c11-degree-comparison.md
  SHA-256: 853d70a771659ebc8f2f575959b7ab7c4d60da19707799fee1bd3c1f965ec986

## Exact progress
A thirteen-vertex graph J is triangle-free, has maximum degree four,
vertex bipartization number three, and no B-homomorphism by a short
unique-common-neighbor argument. Every single-edge deletion has an
explicit map in one of three symmetry classes.
The failure is for the degree-free three-apex extension, not the cubic root.
The explicit JSON is graph input, not an executed UNSAT certificate.
No graph enumeration, SAT solver or kernel was run.

## Failed auxiliary direction
Fingerprint: 43e8faa03532a75223c3782121ec35c15f50a66abd5dc03a008eafb05a60e14e
Do not extend C10 from two to three deleted vertices without a degree bound.
Do not feed a degree-four graph to C05's subcubic completion.
The admitted route itself is not failed; the truth ledger was not modified.

## Open obligations and next unique action
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

Complete C11 candidate transport, then fresh-read main and save the square
reducibility proof: exact four-pin relation, low-degree edge six-cycle,
and smaller triangle-free subcubic replacements. Its conditional conclusion
is that a vertex-minimum subcubic counterexample has girth at least five.
After that, attack a genuine pentagon/global extension step.
