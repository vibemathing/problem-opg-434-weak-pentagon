# C12 source and statement comparison

verdict: candidate_only
retrieval_date: 2026-09-06

## Primary high-girth comparison
Matt DeVos and Robert Samal,
High-girth cubic graphs are homomorphic to the Clebsch graph,
arXiv:math/0602580v2 (23 October 2009).
https://arxiv.org/abs/math/0602580

The primary HTML abstract was reopened in this cycle. It reports a
computer-assisted sufficient condition at ordinary girth at least seventeen
for maximum-degree-three graphs. C12 does not replay that proof, lower its
numerical threshold by citation, or replace ordinary girth by odd girth.
Instead C12 proves a paper conditional square-reduction step and an
equivalence between the original universal question and its girth-five
cubic restriction. That restricted universal question remains unresolved
by the present candidate.

## Search coverage
Queries included:
"Clebsch" "4-cycles" "subcubic";
"Clebsch graph" "4-cycle" "homomorphism";
"weak pentagon" "girth five".

No exact primary-source match for the complete four-pin and low-degree-edge
reduction proof was identified in the retrieved material. This is not
a novelty assertion or an exhaustive literature audit. General encyclopedia
hits and unrelated representation-theory results were not used as evidence.
No PDF was analyzed in this cycle.

## Candidate reuse and fidelity
At base 1d1ebd196e965bd3f0bc2472c04e076ec05cdd9b:
C06 provides pair symmetries and the conditional subcubic minimum's
minimum degree and separated degree-two vertices.
C07 provides the common-neighborhood theorem for at most three labels.
C05 supplies the general completion for comparison, not unrestricted
ordinary-girth preservation. C09 records the distinct pentagon boundary
obligation that remains after squares are reduced.

The new proof separately checks:
(1) exact acceptance of a FIXED four-pin tuple;
(2) relabeling a low-degree edge with all other labels fixed;
(3) existence of a map chosen via a smaller source graph;
(4) girth-five preservation only for separated degree-two deficiencies.
None of these four quantifier layers is silently substituted for another.
