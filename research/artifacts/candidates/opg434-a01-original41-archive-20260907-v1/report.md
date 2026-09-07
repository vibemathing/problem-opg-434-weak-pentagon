# Exact preservation of the original 41-file h=1 replay archive

candidate_id: candidate:opg434-a01-original41-archive-20260907-v1
verdict: candidate_only
base_revision: 5f9e62b066b48a696dfb5c77272a244dcbade665
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence

## Two distinct immutable byte versions

Fresh reads found and repaired PR #27, whose thirteen files contain a different
replay implementation and a lossless bundle. Its final head was
ced786649c1519a8de822acc81968bb1992dca15; its squash merge is this packet's base.
The only repair removed an unadmitted requested capability from its packet.
No old source, mathematical output, or verifier policy was changed.

The original chat ZIP contains 41 logical files, 714578 uncompressed bytes.
Its SHA-256 is a4e5979dd893a3bbf8a215d18af802427ef098be05d439759790c6837c4c5d51.
It is NOT byte-identical to the PR #27 variant. In particular the original
CNF has 38510 clauses and a 707-addition DRUP; PR #27 describes a different
16910-clause encoding with 17 additions. Their receipts must never be mixed.

## Exact archived representation, not overwriting live paths

The seven payload files, index.json and restore_original41.py preserve every
original logical file byte-for-byte. The index records each original path,
byte length and SHA-256. Most entries are UTF-8 text; the canonical DIMACS
entry is losslessly represented by bounded column-delta integers. This is
serialization, not replacing or regenerating a mathematical certificate.

The decoder was actually run in verify-only mode and returned integrity_pass,
41 files and 714578 bytes. Each of the seven remote payload Git blob hashes
was compared with the locally hashed intended byte string and matched.
This verifies transport integrity, not the archived mathematical claims.

The archived packet is historical data INSIDE the archive. It is not installed
as a second active packet, and it never overwrites PR #27's real PR-bound packet.
The sole active new packet is the original41-archive packet for this transaction.
A requested extraction must use a fresh directory beneath candidates; the
historical logical paths are reconstructed below that directory only.

Run from a repository copy:
python3 research/artifacts/candidates/opg434-a01-original41-archive-20260907-v1/restore_original41.py
The default command verifies without extracting or executing archived code.

## Status and next action

Historical local_only, missing-tool and ready-status prose is retained as an
immutable record of its drafting time, not as current GitHub or root status.
No claim that all forty-one logical files occupy their old direct paths is made:
all their exact bytes are persisted in this distinct, independently decodable
candidate-path archive. Existing live mathematical files remain untouched.

Next: check the archived full-source graph/maps/CNF/DRUP with a separately
implemented checker, record the auxiliary uniform-repair failed-route proposal,
and investigate a smaller pentagon-belt replacement whose boundary relation
lifts after a global rechoice of the exterior homomorphism. The original
weak-pentagon root is not closed. No EvidenceLink or Result is produced.
