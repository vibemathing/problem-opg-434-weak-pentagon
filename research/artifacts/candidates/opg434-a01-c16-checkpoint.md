# C16 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c16-belt-frontier
base_revision: ede8f67c666b8aedfe6fa5f5414161863c283ff7
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
branch: web/attempt-opg434-a01-c16-belt-frontier
packet: research/artifacts/web-inbox/opg434-a01-c16.packet.json
pull_request: not created when this checkpoint was frozen; final binding will be in the packet and Issue #3.
checks: not yet observed for the completed packet; no merge claim.

## Frozen artifact

research/artifacts/candidates/opg434-a01-c16-belt-frontier.md
SHA-256: 6fe0973febae9ee2f06367356825fc69f2d033f1718c202ed8a09b3eafc1b3d2
Expected Git blob: 01b713dbc49407a86e61180d862766bcae81bd06
Candidate creation commit: e258e1b7f5a99d651ef75e7b812c94609b1f6032

## Progress and negative knowledge

For a hypothetical vertex-minimum triangle-free subcubic non-B-mappable graph, a pentagon with one degree-two vertex has only two possible induced belt topologies: an eleven-vertex four-boundary-edge block, or a twelve-vertex block with four or five boundary edges. Hub/old-port coincidences and every possible additional internal edge are excluded by explicit positive maps and actual small-exterior gluing. The remaining four/five-port blocks are not proved reducible, and outside boundary endpoints are not presumed distinct.

A pre-submission labeling draft incorrectly used 34 adjacent to s_5. It was discarded before writing, and the explicit table rows were rebuilt from the target adjacency rules. This is a candidate-table error, not a source-graph obstruction. No automated graph/table enumeration, solver or verifier ran. Byte hashing is integrity processing only.

failed_routes: [] in the fresh ledger; auxiliary failures remain recorded in candidates.
open_obligations: obligation:opg434-five-transversals-equivalence; obligation:opg434-root.

## Next action

Complete this one packet/PR, backfill PR identity, inspect the three required checks on the final head, self-review the full allowed diff, and squash-merge only after the gates pass. Then fresh-read main and continue on the same admitted Route/Obligation.

Retain the exact four/five-port belt frontier. The next candidate will audit a global quotient formulation from the explicit four-cycle product model of B. In particular, contraction loops must be retained and any maximum-cut shortcut must be tested on a connected nonbipartite positive graph before it is used as an existence argument.
