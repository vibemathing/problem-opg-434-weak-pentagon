# C10 global-switching transport recovery

verdict: candidate_only
mode: transport_only; new mathematical research paused
source_branch: web/attempt-opg434-a01-c10-global-switching
source_head: 81f035f9f128211f4a87a35252062786db96e4bd
base_revision: d13c8a34c782675a09a70ac3d462139ed6766d44
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
target: obligation:opg434-five-transversals-equivalence
root: obligation:opg434-root
best_verified_candidate: none
best_verified_result: none

## Existing candidate and source-name collision

The global-switching draft was present on the orphan branch but absent from main. It is not the already-merged C10 two-vertex-bipartization candidate. This transaction reuses the original orphan branch, merges the current main without force, and adds one new packet.

The old source note at research/artifacts/source-notes/opg434-a01-c10-bipartization-comparison.md has blob ad0a0c59259e487a69fe442231f92dc4fc3f90ac. Main already has a DIFFERENT source note at that path, blob 730cfac7c4dbb0e315d4a29efe0391b9e21012de, which is left unchanged. The old source text is retained byte-for-byte at research/artifacts/source-notes/opg434-a01-c10-global-switching-comparison-recovered-20260907.md.

The recovered proof has exactly one textual change: its source-note locator is replaced by the new archival path. No mathematical statement, proof argument, count or status has been changed. Original proof at the source head: 8847 bytes, SHA-256 9d0c287c9f7678637c6647885e7796d26d7350e5b523565ca75239e758679bc0, Git blob 07cce19354623a74a31dd334f7cb83cc55d203a4.

## Delivered file identities

- research/artifacts/candidates/opg434-a01-c10-global-switching.md
  Bytes: 8869
  SHA-256: 3479315a20be8ff609ca0281710c4042e099c38e38ca8742bdc367d11654d7d2
  Git blob: ea0da181f65477c981489629b9efa146c9785644
- research/artifacts/source-notes/opg434-a01-c10-global-switching-comparison-recovered-20260907.md
  Bytes: 2073
  SHA-256: 121268e8b04c2e5afc0bdb7bcb8f1d0251654155da8e02323d27f8bec6b9d46c
  Git blob: ad0a0c59259e487a69fe442231f92dc4fc3f90ac

All source retrieval statements describe the original 2026-09-06 comparison, not a new search in this transportation round. No source full text, private data or hidden reasoning transcript is stored. Candidate arguments and source-faithfulness remain pending. No mathematical program or verifier was run; local hashing is integrity processing only.

## Open transport queue

After this PR's final binding/checks/squash merge, re-read main and handle the two local archives. The old nonpacket JSON in web-inbox must be relocated to a candidate archival path rather than passed off as a valid packet. Both admitted obligations remain open. This index is not mathematical Evidence or a final all-current receipt.
