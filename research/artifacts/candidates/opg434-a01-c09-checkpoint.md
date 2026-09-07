# C09 checkpoint (frozen before PR creation)
verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c09-pentagon-boundary
base_revision: 779270194fe878240f7cf3de1244a3cdaad858eb
branch: web/attempt-opg434-a01-c09-pentagon-boundary
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
packet: research/artifacts/web-inbox/opg434-a01-c09.packet.json
pull_request: not yet created at checkpoint freeze
required_checks: not observed for a finalized PR-bound head

## Frozen artifacts
- research/artifacts/candidates/opg434-a01-c09-pentagon-boundary.md
  SHA-256: d601daef15ea297181a85557c62c376169b73bda6da732e5e2030535c90e638f
  Matched remote Git blob: 8536fcb176ca68e59d7e63772664525efbb4b075
- research/artifacts/source-notes/opg434-a01-c09-extension-comparison.md
  SHA-256: 7390f22b661484c940a9c4a55c6998b1bb299193c7ad82309afbc60d2d07ac6d

## New mathematical state
The full ordered pentagon-boundary relation and exact two-pin counts are given.
At most three pins extend exactly when consecutive pinned labels differ.
Four distinct pins (0,34,s_5,12) at positions 0,1,2,4 fail together although
every three-pin restriction extends. The minimum is for this boundary arity,
not for cubic counterexamples. An explicit full graph map is supplied.
Pairwise nonadjacent exterior labels have a complete extension characterization,
and gluing a fresh pentagon ear has an exact factorial extension count.

## Open state and continuation
Both admitted obligations remain open. No cubic graph enumeration, SAT/UNSAT
or kernel certificate has been produced. The auxiliary three-projection
compression fails; the admitted route does not.
Next unique obstacle: choose a globally attainable exterior state in the
feasible boundary relation, rather than check projections of one bad state.
Next action: audit simultaneous two-switch construction after bipartization;
separate its sufficient structural condition from the full B problem.
Append final PR/head/check/merge observations to Issue #3.
