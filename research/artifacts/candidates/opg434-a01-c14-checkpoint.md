# C14 resumed checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c14-pentagon-reduction
open_obligations: obligation:opg434-five-transversals-equivalence; obligation:opg434-root
failed_routes: [] in the fresh main ledger; auxiliary failures remain in their candidate files.
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 44c810241c927303ece47a666d9a0f3d3b3031ac
branch: web/attempt-opg434-a01-c14-pentagon-reduction
initial_branch_head: e8261cab85832ae010f3ed3d208cbf4207d5bac5
packet: research/artifacts/web-inbox/opg434-a01-c14.packet.json
pull_request: not created at this frozen checkpoint; final binding will be in the packet and Issue #3.
checks: not observed yet for the completed packet; no merge claimed here.

## Frozen candidate and audit

research/artifacts/candidates/opg434-a01-c14-pentagon-reduction.md
SHA-256: 75ec5d375fe8141a6565fda38dc80dc51ff6418895affe9e330f295bd7aa2afa
Git blob: f5ac52ac4407936357eb0ef7887f2e282c0a7d6a
The original 11851-byte candidate is retained unchanged. Its pin witnesses and virtual-edge reductions received paper self-review; the fresh source comparison is research/artifacts/source-notes/opg434-a01-c14-audit-comparison.md, commit d737ac9673ef64c3f397a9e1b148b48573e84e74.

## Substantive progress and limits

The exact oriented two-pin-edge relation requires only the remaining three consecutive inequalities. It gives a genuine reduction for two nonadjacent degree-two vertices on a pentagon. One degree-two vertex forces three exterior common-neighbor conditions in a hypothetical subcubic minimum. The resulting belt and cubic pentagon cases remain open. No mathematical program, kernel, or verifier ran; byte hashing is not such a run.

## Next action

Finish this one packet, open the linked candidate PR, backfill its number and URL, inspect all three required checks on the final head, review the full candidate-only diff, and squash-merge only after the gates pass. Then fresh-read main and start the next immutable packet on the same admitted Route/Obligation.

Next bounded mathematical target: audit a quantified uniform bounded-radius repair claim using recursively pinned trees. A usable negative candidate must supply both a genuine exterior homomorphism that cannot be repaired within radius r and a separate explicit full homomorphism of the entire positive graph. It must audit finite size, maximum degree, triangle-freeness, and every claimed distance; it must not be labeled a root counterexample or a failure of the admitted equivalence route.
