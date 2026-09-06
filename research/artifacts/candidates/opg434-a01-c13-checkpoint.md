# C13 checkpoint

verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c13-three-terminal-gluing
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
base_revision: 0817fc9a53c65ebc2f162714143974f51daec3d2
branch: web/attempt-opg434-a01-c13-three-terminal-gluing
packet: research/artifacts/web-inbox/opg434-a01-c13.packet.json
pull_request: not yet created at checkpoint freeze
required_checks: not yet observed on this branch

## Frozen candidate
research/artifacts/candidates/opg434-a01-c13-three-terminal-gluing.md
SHA-256: 44d39b499ae7a184b25304a20c7a28de9d9eaa69638c84ee03f9f2021e2b0296

## Paper progress
The exact three-terminal affine matching relation has only the pairwise
equal-versus-adjacent obstruction, with all repeated-label cases covered.
Three low-degree ports can be reselected to make any matching of two
colorable pieces compatible. A vertex-minimum triangle-free subcubic
counterexample therefore has no cyclic cut of size at most three.
Together with C12, this same conditional minimum has girth at least five.
Cubic completion is not asserted to preserve cyclic connectivity.

## Boundary not to cross
For four terminals, the constant tuple and (0,12,13,23) pass every triple
projection but have no common affine matching. This does not constitute
a source graph counterexample and does not forbid recoloring the ports.
No graph enumeration, solver, or kernel was executed.
No truth record or old packet was changed.

## Open obligations
obligation:opg434-five-transversals-equivalence
obligation:opg434-root

## Next unique action
Complete C13 transport, then fresh-read main and save the stronger
pentagon two-edge pin relation and its degree-two-vertex reductions.
That step must prove a suitable whole-graph extension, not merely
reuse the pair table or declare separator cleanup to be completion.
