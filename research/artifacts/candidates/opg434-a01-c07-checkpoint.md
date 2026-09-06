# C07 checkpoint (before PR creation)
verdict: candidate_only
route_status: active
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg434-a01-c07-star-obstructions
base_revision: 5da7be8676a1074b3607012e943db6b441cbd5eb
branch: web/attempt-opg434-a01-c07-star-obstructions
issue: https://github.com/vibemathing/problem-opg-434-weak-pentagon/issues/3
packet: research/artifacts/web-inbox/opg434-a01-c07.packet.json
pull_request: not yet created when this file was frozen
checks: not yet observed on the final PR-bound head

## Frozen artifacts
- research/artifacts/candidates/opg434-a01-c07-star-obstructions.md
  SHA-256: fd78075093647c0034396f58c90ee62267b59dca11028a5c24a807dfd2552978
- research/artifacts/source-notes/opg434-a01-c07-source-comparison.md
  SHA-256: 69090c91843281c1ed79ac9a2ecd65c163f30fe3d85faabc4c71313e632e7933

## Persisted mathematical state
The 4096 ordered triples are covered by six proved cases, not an executed enumeration.
The whole-star boundary relation is exact: repair fails precisely for total domination
by the exterior labels. Four distinct labels suffice and are necessary; in size four
the induced target graph is C4. An eight-vertex tree is minimum for this repair rule.
A 48-vertex planar triangle-free cubic realization has both the bad prescribed partial
map and a separate full homomorphism. Neither is a root counterexample.
The K1,4 five-label boundary warns that four-cycle-only tests miss larger obstructions.

## Open work
Both obligation:opg434-five-transversals-equivalence and obligation:opg434-root remain open.
Registered failed routes checked: []; one auxiliary-rule failure is proposed, not admitted.
Cubic-graph enumeration performed: none.
SAT/UNSAT or kernel certificates produced: none.
Next unique obstacle: nonlocal recoloring must change a total-dominating boundary;
a whole-component automorphism alone preserves all target adjacencies.
Next action: prove and audit two-generator cut switches, then pentagon boundary extension.
Complete this PR's three transport checks and append final head/run/merge data to Issue #3.

## Transport correction
The remote candidate includes the second Markdown table separator; the original
local hashing string omitted that separator. Its Git blob was matched exactly,
and the packet and this checkpoint now bind the actual remote bytes. No mathematical
claim or gate was changed. The failed validation is not a mathematical result.
