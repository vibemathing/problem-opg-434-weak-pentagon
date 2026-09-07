# C08 source and statement comparison
verdict: candidate_only
Retrieval date: 2026-09-06

## Repository dependencies
At 958a4f78550b01a043dc90a91747804c9d6031ff, C06 fixes the generators
and affine automorphisms; C07 proves the triple-neighborhood and fixed-exterior
one-star tests. C08 studies a different operation, one uniform subset translation.
Its witnesses do not contradict the C06/C07 candidates.

## Primary-source comparison
Matt DeVos and Robert Samal, High-girth cubic graphs are homomorphic to the
Clebsch graph, arXiv:math/0602580 (abstract and version record):
https://arxiv.org/abs/math/0602580
The stated theorem concerns maximum degree three and ordinary girth at least 17.
It does not apply to the pentagonal prism or prove the root's triangle-free
case. C08 uses neither that theorem nor a proper source edge-coloring hypothesis.

Meirun Chen, Reza Naserasr and Alessandra Sarti, Signed projective cubes,
a homomorphism point of view, arXiv:2406.10814v1:
https://arxiv.org/html/2406.10814v1
Published version: Journal of Graph Theory 113 (2026), 38-56,
first published 2026-04-21, DOI 10.1002/jgt.70046:
https://doi.org/10.1002/jgt.70046
The arXiv HTML and publisher search excerpt were accessible. The paper defines
signed switching by reversing signs on a cut and discusses projective-cube
Cayley definitions and signature packing. This is NOT the operation used in C08:
we keep an ordinary graph and require all edge differences to remain in S.
The extra cut-color condition in C08 is proved directly; a signed switching
definition alone cannot justify it. A natural proper coloring of the TARGET
does not make a pulled-back source coloring proper.

The inspected sources supplied no theorem closing the frozen root. This is
a statement about this limited source review, not a claim to have exhaustively
searched all literature or certified the problem's present status.
No PDF, figure, or table was used in this cycle, and no novelty claim is made.
