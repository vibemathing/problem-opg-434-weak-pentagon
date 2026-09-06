# C07 source/statement comparison
verdict: candidate_only
Access date: 2026-09-06

Fresh repository base: 5da7be8676a1074b3607012e943db6b441cbd5eb.
C01-C06, Issue #3, PR #9, failed-route ledger, Attempt and ObligationGraph were read.
The failed-route ledger was empty. Issue #3 mentions a proposed ten-vertex tree
attack but does not supply a submitted C07 proof. This C07 gives an eight-vertex
minimum witness and a separate explicit cubic realization; it does not rely on
a completion automatically extending a coloring through other missing centers.

Primary external sources checked:
1. Robert Samal, Weak pentagon problem, Open Problem Garden:
https://www.openproblemgarden.org/op/weak_pentagon_problem
The original five-color statement and the vertex-homomorphism formulation match
the frozen contract. Neither says that EVERY prescribed partial map extends.
The page's displayed date is July 13, 2007; it is not a current verification receipt.

2. Matt DeVos and Robert Samal, High-girth cubic graphs are homomorphic to the
Clebsch graph, arXiv:math/0602580:
https://arxiv.org/abs/math/0602580
The abstract explicitly assumes maximum degree 3 and ordinary girth at least 17.
This is a stronger input assumption than triangle-free, not a proof of the root.
Only abstract metadata/text is used here, not an unexamined PDF figure.

3. Reza Naserasr, Yared Nigussie and Riste Skrekovski, Homomorphisms of triangle-free
graphs without a K5-minor, Discrete Mathematics 309 (2009), 5789-5798:
https://doi.org/10.1016/j.disc.2009.04.032
https://www.sciencedirect.com/science/article/pii/S0012365X09002581
Publisher abstract states a Clebsch-homomorphism result for triangle-free K5-minor-free
graphs. The missing K5-minor exclusion in the root cannot be silently inserted.
This is an abstract-level comparison, not a replay of the proof.

No primary source resolving the full root was located in these bounded searches.
This search outcome is not a proof that no later resolution exists.
No novelty claim is made for the target's finite neighborhood properties.
The triple table, star criterion, minimality and explicit witnesses are proved
in the companion candidate instead of being credited to an unrun enumeration.
