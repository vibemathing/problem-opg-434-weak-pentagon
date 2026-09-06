# C15 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c15-radius-obstruction
base_revision: d8220b87d903640d1abd2d835aba2f01a32f23dc
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
branch: web/attempt-opg434-a01-c15-radius-obstruction
packet: research/artifacts/web-inbox/opg434-a01-c15.packet.json
pull_request: not created at this frozen checkpoint; final binding belongs to the packet and Issue #3.
checks: not observed yet for the completed packet; no merge claim.

## Artifact and claims

research/artifacts/candidates/opg434-a01-c15-radius-obstruction.md
SHA-256: bd44c2b8b44ed7556941d5e4396f8e9ea8397fed4e413b7065d5e53512c3945f
Git blob expected from local text integrity processing: 887e8c40035ab15a487c3e47e884c5d90c115414

The finite family uses recursively pinned binary trees, an explicit 11-vertex positive one-port gadget, and bridge attachments. For each r, h=max(1,r) yields a connected cubic girth-five graph with 12*2^(h+2)+10 vertices, an explicit full B-map, and a genuine punctured map that cannot be repaired within radius r. Both the realizing maps and the obstruction are proved on paper. No graph program, solver, proof assistant, or verifier ran.

## Negative knowledge and open obligations

Uniform finite-radius repair for every punctured map of every positive cubic girth-five graph is the failed auxiliary rule. C07's fixed-star example alone was not enough for this stronger quantifier. These new witnesses have bridges, so they do not attack a connectivity-restricted repair theorem. They also do not prove that any graph violates the root.

failed_routes: [] in the fresh main ledger; auxiliary failure recorded in this candidate only.
open_obligations: obligation:opg434-five-transversals-equivalence; obligation:opg434-root.

## Next action

Finish the C15 packet/PR, backfill PR identity, inspect all three checks on the final head, and squash-merge only after a candidate-only diff review. Then fresh-read main. Continue with the one-deficiency pentagon belt or a precise connectivity-restricted boundary statement; do not reuse unrestricted local repair. Any such belt argument must retain possible coincidences among exterior common neighbors and must build a compatible whole-graph map, not only separate boundary projections.
