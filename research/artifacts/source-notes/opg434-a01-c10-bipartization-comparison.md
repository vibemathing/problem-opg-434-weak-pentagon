# C10: bipartization and switching statement comparison
verdict: candidate_only
Retrieval date: 2026-09-06

## C5 versus the frozen root
Matt DeVos and Robert Samal, High-girth cubic graphs are homomorphic to the
Clebsch graph, Journal of Graph Theory 66 (2011), 241-259:
https://doi.org/10.1002/jgt.20580
https://arxiv.org/abs/math/0602580
The primary abstract distinguishes its B conclusion at ordinary girth at
least 17 from Nesetril's question about a C5 target at sufficiently high girth.
C10's Petersen argument rejects the stronger ALL triangle-free cubic C5
statement only. It is neither a counterexample to that high-girth question
nor a counterexample to the frozen B/Weak Pentagon root.

## Independent set plus forest is a different certificate
Marthe Bonamy, Konrad K. Dabrowski, Carl Feghali, Matthew Johnson and
Daniel Paulusma, Recognizing graphs close to bipartite graphs with an
application to colouring reconfiguration:
https://arxiv.org/abs/1707.09817
https://doi.org/10.1002/jgt.22683
The publisher's searchable article text, Section 1.1 Theorem 1, attributes
to Catlin and Lai an independent-set/forest decomposition for connected
subcubic graphs other than K4, with a maximum-size independent set.
The paper's own algorithmic result drops the maximum-size demand when
finding such a decomposition efficiently. Neither statement requires the
open neighborhood of the independent set to be independent.
C10 proves its stronger-neighborhood condition exactly characterizes a C5
image, and uses the Petersen tree complement to display the difference.

The publisher full-HTML open request returned an internal error, while its
search-returned theorem text and the arXiv abstract were readable. No figure,
PDF, implementation or theorem-prover replay is claimed. C10's forest
cut-switch connectivity is separately proved and is not the paper's
single-vertex proper-coloring reconfiguration theorem.

No novelty claim is made. These sources do not supply the missing general
extension step. All stored derivations and source comparisons remain candidates.
