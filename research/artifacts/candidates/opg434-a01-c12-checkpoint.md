# C12 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c12-square-reduction
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 1d1ebd196e965bd3f0bc2472c04e076ec05cdd9b
branch: web/attempt-opg434-a01-c12-square-reduction
packet: research/artifacts/web-inbox/opg434-a01-c12.packet.json
pull_request: not yet created at checkpoint freeze
required_checks: not yet observed on this branch

## Frozen artifacts
- research/artifacts/candidates/opg434-a01-c12-square-reduction.md
  SHA-256: baeed87d6e03eee9c6107004bff161a7098399348c31cf85d7fee822f8e54a72
- research/artifacts/source-notes/opg434-a01-c12-reduction-comparison.md
  SHA-256: 3290dac4610fc0e521309db0cc2b7199e642322099f3882f0c59456ac7317254

## Substantive progress
The exact four-pin square relation fails only at equal consecutive pins
or an induced diagonal 2K2. A low-degree source edge has an explicit
six-cycle of feasible ordered images. This yields a complete square
reducibility proof, including missing and repeated exterior pins.
A vertex-minimum triangle-free subcubic counterexample is square-free.
Separated degree-two vertices allow a two-copy cubic completion preserving
girth five. Consequently the root is equivalent to its cubic girth-five
restriction; that universal restricted problem is NOT proved here.
All claims are paper candidates; no mathematical execution was performed.

## Open obligations
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

## Failed auxiliary directions preserved
C07-C09 prohibit universal one-star repair, arbitrary single cut-switch
repair, and replacing the full pentagon boundary by triple projections.
C11 excludes the degree-free three-apex extension, but not the cubic root.
C12 does not claim that every fixed square boundary extends.
No failed-route truth ledger was changed.

## Next unique mathematical obstacle
Finish C12 transport. Then fresh-read main and pursue a valid pentagon or
global replacement. The exact three-edge matching-cut compatibility proof
can strengthen cyclic connectivity, but is not root closure.
The oriented pentagon boundary, rather than the already settled pair
table, is the unresolved local extension step.
