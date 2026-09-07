# Auxiliary-route disposition and the root-facing pivot

verdict: candidate_only
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
admitted_route_id: route:odd-cycle-transversal-equivalence-v1
admitted_target: obligation:opg434-five-transversals-equivalence
root_obligation: obligation:opg434-root
registration_status: proposal_only; trusted importer required for any failed-route truth entry

## Rejected auxiliary strategy, with exact quantifiers

The proposed repair strategy asserts a uniform finite radius R, or a uniform finite edit budget K, sufficient to repair every homomorphism f:G-V(Q)->B into a total homomorphism, for every finite simple cubic girth-five source in the strong-connectivity class and every specified induced pentagon Q. Edits are disagreements of target vertex labels on the old vertices. The radius is measured from the whole set V(Q) in the full source graph, not from one chosen vertex and not in the punctured graph.

The stored layered construction supplies, for each pair of finite bounds R,K, an explicitly positive source G and a genuine exterior f such that every total map changes more than K old vertices and changes one farther than R from Q. Its explicit total map is essential: the negative statement is about preservation of an arbitrary exterior map, not nonexistence of a graph homomorphism. The all-height construction and the finite h=1 controls are separate inputs. No finite DRUP file alone proves the infinite family.

Source locators:
- research/artifacts/candidates/opg434-a01-layered-pentagon-repair-20260907-v1.md
- research/artifacts/candidates/opg434-a01-layered-audit-20260907-v1/audit.md
- research/artifacts/candidates/opg434-a01-layered-replay-20260907-v1/report.md
- research/artifacts/candidates/opg434-a01-layered-replay-20260907-v1/outputs.bundle.json
- research/artifacts/candidates/opg434-a01-original41-archive-20260907-v1/index.json

The PR27 and original41 encodings are different byte-level artifacts. Their model encodings, proof lengths, mutation lists and process receipts must never be mixed. Both remain candidate inputs, not signed trusted evidence.

## What remains allowed and is actually used next

The root asks for existence of one suitable total map. It is still permissible to select an entirely different exterior map by constructing a smaller triangle-free subcubic graph and applying minimality to it. Failure of arbitrary-map repair says nothing against this existential operation.

The companion merged-belt-proof.md uses exactly that operation. Its exact four-port relation is a!=d. Replacing the eleven-vertex core by a length-three path imposes the same necessary inequality in every smaller-graph map and decreases source order by nine. The proof retains physical endpoint coincidences and checks triangle-freeness and degree budgets. This is a liftable patch lemma, not an assertion of the rejected uniform repair strategy.

## Current nonterminal obligations

The twelve-vertex distinct-hub C16(B) patch has ordered potential boundary ports (x0,x2,r,z,t), with necessary inequalities p0!=p4 and p1!=p2. Neither their sufficiency nor a replacement relation is assumed from the four-port proof. A complete finite relation certificate must include all normalized states or a fully specified first rejected state with a sound nonextension certificate. Its source-lifting step must then be checked separately.

The all-degree-three pentagon case and the Weak Pentagon root remain open. No truth record, EvidenceLink, Result, Solution, schema, Harness or workflow is changed. best_trusted_result=none. Transport and candidate checks do not close any mathematical obligation.
