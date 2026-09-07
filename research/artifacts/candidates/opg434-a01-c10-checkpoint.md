# C10 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c10-two-vertex-bipartization
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 048a5a5f0ddb8bc3f822eacd5770721f4e9ac968
branch: web/attempt-opg434-a01-c10-two-vertex-bipartization
packet: research/artifacts/web-inbox/opg434-a01-c10.packet.json
pull_request: not yet created at checkpoint freeze
required_checks: not yet observed on this branch

## Frozen artifacts
- research/artifacts/candidates/opg434-a01-c10-two-vertex-bipartization.md
  SHA-256: 8a72dd2ff2b000fbdb1fe4acaa12786c6e87b7dcac4023377ea15700fc356c7a
- research/artifacts/source-notes/opg434-a01-c10-bipartization-comparison.md
  SHA-256: ffb91c84125b6d885afe38e9410dbe8f00d7dfd96e486bf878e666f70cf66c75

## Substantive progress
Whole-graph maps are constructed for every finite simple triangle-free graph
made bipartite by deleting at most two vertices, with no degree bound.
The one-apex case has two explicit commuting legal cut switches from a
specified bipartite base map. Two tables handle nonadjacent/adjacent apices.
The attainable pair relation is exact, not just a sufficient constraint.
An eight-vertex cubic example has a displayed B map but no C5 map.
A hypothetical root counterexample therefore needs at least three
vertex deletions to become bipartite. No graph search or kernel was run.

## Open obligations
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

## Failed auxiliary directions
C07 and C08 exclude universal one-star and single cut-switch repair of a
prescribed map. C09 excludes reducing the pentagon relation to its
three-terminal projections. C10's construction does not repeat these routes.
Registered failed-route ledger remains empty; no truth record was modified.

## Next unique obstacle
Complete C10 transport, then fresh-read main. Investigate the three-apex
case with degree budgets explicit. Test a putative universal degree-free
extension first, and distinguish any maximum-degree-four obstruction from
a legitimate cubic root counterexample. Continue all checkpoints in Issue #3.
