# Exact source-admissibility attachment archive

candidate_id: candidate:opg434-a01-source-admissibility-archive-20260909-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
verdict: candidate_only
best_verified_result: none
base_revision: 6e702ed29bbc11072ac3376c1c3300cb9958419d

## Exact bytes, not substituted receipts

This archive preserves all 36 files (377733 logical bytes) in the user-supplied
opg434-source-admissibility-20260909-v1.zip. Original ZIP SHA-256:
93f8fc0e317c4bf7b6faea1b5e5e7595bb1f13560dee17237e8fda16a04db08b.
The ZIP container is not reproduced; its uncompressed file bytes are exact.
It is a DIFFERENT implementation from PR31 physical-exit. No computation or
mutation count from one variant is attributed to the other.

The original report SHA-256 is
af40885b37310eff4a3de8f154ee01582b0b5edec373cd6b1337416ded969f1e.
It records a candidate proof for physical quotient sides of size at most four,
an endpoint obstruction to embedding the old abstract cover, and prior bounded
computations. Its original branch/PR/local_only prose is historical metadata,
not current GitHub state. Root, general EXIT and trusted closure remain open.

Four numbered payload text parts encode base64(XZ(JSON entries)). Every entry
contains the original relative path, byte count, SHA-256 and full UTF-8 content.
Decoded JSON SHA-256:
00a763b6f8c2062f1c8ea5da7d0fb6e54490c08ceab6e406da8f4a70c4d49918.
Compressed SHA-256:
26f61b33877795b3fbf838ff0a2c9357c3de5540d0d4e7603575c21802088772.

## Integrity-only reproduction

Run `python restore_archive.py` in this candidate directory. The decoder checks
every part, the bounded decompression, all 36 per-file hashes and total bytes,
then restores under its own `restored/` directory. It refuses an existing
destination and executes no restored code. The original inbox packet is only
inactive archived data under that isolated directory, not a second live packet.
The sole live transaction is PR31 physical-exit's existing inbox packet.

An actual local decoder invocation returned integrity_pass for 36 files and
377733 bytes. The four remote Git blob IDs matched the exact intended bytes.
This verifies delivery integrity only, not a new mathematical replay.
All stored UTF-8 was scanned for credential markers and absolute host paths;
no matching markers were found. No full chat or hidden reasoning is retained.

Decoder SHA-256:
32b27ac66ab3f3e20cec16fb7606a432d3d849fb8ac60c8993778149dafebc49.
The original files preserve their own code versions, failed runs, corrected
runs, input/output hashes, theorem scope and pending trusted-verifier request.
Do not rerun old R11/R12 or h1 producers as part of this archive restoration.
