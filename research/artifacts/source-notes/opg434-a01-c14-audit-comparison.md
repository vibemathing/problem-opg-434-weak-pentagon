# C14 continuation audit and source comparison

verdict: candidate_only
primary_owner: math-derivation
base_revision: 44c810241c927303ece47a666d9a0f3d3b3031ac
existing_candidate_commit: e8261cab85832ae010f3ed3d208cbf4207d5bac5
existing_candidate_blob: f5ac52ac4407936357eb0ef7887f2e282c0a7d6a
existing_candidate_sha256: 75ec5d375fe8141a6565fda38dc80dc51ff6418895affe9e330f295bd7aa2afa

## Frozen-file audit

The existing C14 branch was reused rather than recreated. Its 11851 UTF-8 bytes were reconstructed from the retrieved text; the Git blob SHA-1 agrees with the fetched blob. The SHA-256 above was calculated on those bytes, including the final newline. This is artifact integrity processing, not graph computation or a verifier receipt.

The paper audit uses these adjacency rules in the explicit target: 0 is adjacent to s_i; s_i is adjacent to jk exactly when i is one of j,k; two distinct pair labels are adjacent exactly when the index pairs are disjoint. No pair of generators is adjacent. Translation and permutation of generator indices preserve these rules.

In Case A, the cycle differences of (s_i,0,s_5,5k,ij) are s_i,s_5,s_k,s_l,s_j, where l is the remaining index. The six possible last pairs on {1,2,3,4} cover by their neighborhoods precisely the allowed fifth pins, excluding 0 and s_5.

In Case B, the two index pairs ik and jl are disjoint; the missing index gives their generator difference. A nonzero pair has a disjoint pair, while a generator neighbors 0, so the proposed last-entry set covers all fifth pins except 0.

The C/D tables were checked using the same rules. For the easily misclassified positive fixture (0,s_5,12,34,35), the displayed inner tuple (s_2,0,s_1,15,24) is a cycle, and its last entry 24 is adjacent to 35 because those pairs are disjoint. It is not a negative fixture.

In the graph reductions, recoloring two ports separately is used only when they are physically nonadjacent. Shared other neighbors are fixed and do not introduce an extra constraint between the ports. When x_0 and x_2 are adjacent, the feasible-edge six-cycle from C12 is used instead. Virtual edges join different vertices with no common neighbor in the remainder, so they create neither a loop nor a triangle; the endpoint degree bound is checked after deleting the pentagon. Missing pins impose no actual source edge, and repeated physical pins are not split into independent variables.

This generator self-review leaves the candidate status unchanged. No graph enumeration, SAT solver, proof assistant, or mathematical verification service ran.

## Refreshed primary-source comparison

Retrieved through web search and page reads on 2026-09-07:

1. Robert Samal, Weak pentagon problem, Open Problem Garden, posted 2007-07-13.
   https://www.openproblemgarden.org/op/weak_pentagon_problem
   Locator: Conjecture, reformulations, and Proposition.
   The graph-level existential condition agrees with the frozen contract and is related there to a Clebsch homomorphism. It is not a universal extension theorem for prescribed boundary labels. C14 is a conditional local extension/induction statement within that model, not a proof of the universal conjecture.

2. Matt DeVos and Robert Samal, High-girth cubic graphs are homomorphic to the Clebsch graph, arXiv:math/0602580v2, revised 2009-10-23.
   https://arxiv.org/abs/math/0602580
   Locator: abstract and version history only in this refresh.
   The abstract's positive result assumes maximum degree three and ordinary girth at least 17, and explicitly permits improper edge colorings. The C14 configurations contain five-cycles, so the high-girth theorem does not settle these cases. Its computer-assisted proof was not replayed here. No PDF analysis was used in this refresh.

The search also returned an AI-reviewed secondary status page; it is not used as mathematical authority. No exhaustive novelty or current-resolution claim is made. The present note neither upgrades source statements into repository EvidenceLinks nor changes the root quantifiers.

## Remaining obligations

Both obligation:opg434-five-transversals-equivalence and obligation:opg434-root remain open. Required future capabilities remain kernel_check, axiom_escape_audit and statement_faithfulness. The all-degree-three pentagon and the one-deficiency belt are not settled by C14. The next bounded candidate should test a precisely quantified bounded-radius repair claim, not repeat the excluded one-star rule or infer graph nonexistence from a frozen-boundary failure.
