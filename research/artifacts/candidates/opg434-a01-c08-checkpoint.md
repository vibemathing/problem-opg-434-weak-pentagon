# C08 checkpoint (frozen before PR creation)
verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c08-cut-switches
base_revision: 958a4f78550b01a043dc90a91747804c9d6031ff
branch: web/attempt-opg434-a01-c08-cut-switches
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
packet: research/artifacts/web-inbox/opg434-a01-c08.packet.json
pull_request: not yet created at checkpoint freeze
required_checks: not yet observed for a finalized PR-bound head

## Artifacts
- research/artifacts/candidates/opg434-a01-c08-cut-switches.md
  SHA-256: 77e809385a2b12a8bcd9b54cd89affec1593313204e3d5ce5c9e0881d514240c
  Matched remote Git blob: 42b18543f2f41a0391f7774f0e4e5c57297737ce
- research/artifacts/source-notes/opg434-a01-c08-switch-comparison.md
  SHA-256: 6ff579aefecd5246e7d341273d4684c270e1576755521c21973af495c2c7fb35

## New mathematical state
The exact nonlocal cut-translation rule and terminal repair table are frozen.
An odd monochromatic terminal path blocks every single legal translation.
Six vertices are minimum for this one-step failure in the subcubic class;
the same example has an explicit successful two-step sequence.
A 10-vertex planar triangle-free cubic prism is 3-edge-connected and also has
a bad prescribed partial map. A separate full map prevents a false root claim.
These conclusions do not assert one-star failure on that prism.

## Open state and continuation
Both admitted obligations remain open. No SAT/UNSAT or kernel certificate.
Cubic graph enumeration performed: none.
The auxiliary one-step repair rule has a failed-route proposal, not a truth record.
Next unique obstacle: obtain a multi-step repair or a compatible pentagon boundary.
Next action: after C08 transport, fresh-read main and freeze the exact five-cycle
boundary relation, its failure witnesses and its controlled ear-extension cases.
All final PR/head/check/merge observations must be appended to Issue #3.
