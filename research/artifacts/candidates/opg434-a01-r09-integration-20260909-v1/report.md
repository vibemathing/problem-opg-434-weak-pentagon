# R09 integration: complete (6,2,2), class-(6,3,3) cut exclusion, and parameter frontier

candidate_id: candidate:opg434-a01-r09-integration-20260909-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
verdict: candidate_only
best_verified_result: none
base_revision: fa39349a6ec4fba957c97157b8fd79ca5b3a625c

This candidate transports and deduplicates two complete local candidates:
(1) class (m,k,r,u)=(6,6,2,2), with complete source-valid normalization,
full 155-kernel domain, explicit common-h/B-map witnesses, and complete MC
subset checks on its finite normalized range; and
(2) class (6,6,3,3), excluded from maximum cuts by an explicit cut-improvement
theorem, with separate full-kernel/MC controls on the six residual positive
fixtures.

Exact original report SHA-256 values:
- (6,2,2): c18a6893cfccb2711334ab868f38b65c1b302f57ba0506b4cbff6d2128d3c978
- (6,3,3): e691d0ad0aac41ad7949d51bf859a2d078dc0f26befc8f729d20999c035b9420

## S13 deduplication

For a genuine maximum-cut 6+6 quotient, degree counting gives r=u. Physical
maximum-cut endpoint restrictions give r<=3. The class-(6,3,3) cut theorem
excludes r=3, hence r=u<=2. This is exactly the S13 conclusion and therefore
adds no independent dependency. r<=1 is covered by the <=3-matching theorem,
and r=2 by the complete (6,2,2) candidate.

## S07 audit boundary

The fresh main, Issue #3, failed-route ledger, and available local integration
inputs contain no fixed S07 7+7/F=4 artifact, manifest, full-kernel certificate
or MC receipt. The claimed S07 result is therefore not silently admitted here.
Its arithmetic scope is exactly (m,k,r,u)=(7,7,2,2), order 18; the parameter-
frontier candidate records both the repository-current frontier and the
conditional frontier after a future fixed-byte S07 validation.

No finite result is extrapolated to a different parameter class. General EXIT,
the root ProblemContract, statement-faithfulness and trusted closure remain open.
