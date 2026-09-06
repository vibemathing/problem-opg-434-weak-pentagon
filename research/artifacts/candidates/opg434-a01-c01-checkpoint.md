# OPG434 c01 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c01-equivalence
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: aa9fc64c4e7b9c9d841f2a53c480169038b18bdf
branch: web/attempt-opg434-a01-c01-equivalence
packet: research/artifacts/web-inbox/opg434-a01-c01.packet.json
pull_request: not created when this checkpoint was frozen
required_checks: not observed yet; no merge claim

## Artifacts
- research/artifacts/candidates/opg434-a01-c01-equivalence.md
  SHA-256: fdf9906237d573600ce8d693303da0807158b1a68713de7d82499b6c8775db02
- research/artifacts/source-notes/opg434-a01-c01-statement-comparison.md
  SHA-256: 3d22694048f0c085beb42d906223ee2c5ff14b8e0f5a7a12aa0366b8f5e34a35

## Progress and limitations
The paper derivation covers both directions, spanning-cycle correspondence,
empty color classes, and the rainbow 5-cycle consequence.
K3,3 defeats a fixed-coloring surjectivity/properness requirement.
The 7-prism has a proper five-color assignment passing the vacuous 5-cycle
test but failing an odd-cycle test. Neither is a counterexample to the root.
No executable mathematical verification was performed.
Registered failed-route IDs checked: [].

## Open obligations
- obligation:opg434-five-transversals-equivalence
- obligation:opg434-root

## Next action
Complete this PR's candidate gates. Then fresh-read main and produce a new
immutable packet on the same admitted target, supplying the missing
transversal-to-cut-complement normalization and a fixed-coloring counterexample
to their direct identification. Continue all status updates in Issue #3.
