# OPG434 c06 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c06-separator-gluing
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 4049a626c0db0228fda5d3866eb462564357f5d0
branch: web/attempt-opg434-a01-c06-separator-gluing
packet: research/artifacts/web-inbox/opg434-a01-c06.packet.json
pull_request: not created when this checkpoint was frozen
required_checks: not yet observed for this branch

## Artifact
- research/artifacts/candidates/opg434-a01-c06-separator-gluing.md
  SHA-256: a02f696a539246e0eef1b2b4d5951e8cb2523cde738980743ade680fbe3402b7

## Progress and limitations
A three-type boundary classification gives an exact two-edge compatibility table.
Degree-at-most-two flexibility excludes the only obstruction for two distinct
terminals, yielding matching-two-edge gluing. Conditional minimum-counterexample
consequences are stated in the triangle-free subcubic class: no bridges, cut
vertices or nontrivial two-edge cuts; degree2 vertices cannot be adjacent.
A failed pair of partial homomorphisms is not a graph nonexistence certificate.
No graph computation or formal kernel was run.

## Open obligations and next action
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

Finish c06 transport, then fresh-read main and attack the one-star local-repair
rule while freezing the distance-two labels. Record any failed auxiliary rule
without declaring the admitted equivalence route or the root false.
c05 merged as PR #8, commit 4049a626c0db0228fda5d3866eb462564357f5d0; its three transport checks passed.
Further coordination belongs to Issue #3; no truth records changed.
