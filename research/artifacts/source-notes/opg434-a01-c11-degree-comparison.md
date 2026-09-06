# C11 source and scope comparison

verdict: candidate_only
retrieval_date: 2026-09-06

## Primary source recovered
Reza Naserasr, Yared Nigussie and Riste Skrekovski,
Homomorphisms of triangle-free graphs without a K5-minor,
Discrete Mathematics 309(18), 5789-5798, 28 September 2009.
DOI: 10.1016/j.disc.2009.04.032
https://www.sciencedirect.com/science/article/pii/S0012365X09002581

The publisher's indexed abstract explicitly reports that all triangle-free
graphs without a K5 minor map to the Clebsch graph. This read recovers an
abstract for the DOI whose direct URL previously produced Cache miss.
The full proof was not replayed, and no PDF analysis is claimed here.
The automated conjecture-status page was only a discovery lead, not
mathematical authority.

Comparison: J in C11 is a subdivision of K5 and therefore has that minor.
It is outside this positive class and also outside the maximum-degree-three
root domain. Thus its no-map argument does not conflict with the source's
stated theorem. We do not use the source theorem to prove J's no-map claim.

## Candidate dependencies and reuse
At base bcbe66a0033c7853a9589c59365f42bc7b72a1d5:
- C06, explicit five-generator relation.
- C07, unique common neighbor of a three-element independent target set.
- C10, whole-graph maps when at most two vertex deletions make the source bipartite.

C11 combines these into an explicit thirteen-vertex witness and a short
paper nonexistence certificate. Its edge-criticality is proved using three
symmetry classes and constructive path extensions, not measured by a search.
No novelty or global minimum-order claim is made.

Queries in this cycle included "Clebsch" "subdivision" "K5",
"Clebsch" "4-cycles" "subcubic", and the exact paper title.
No exact primary-source identification of this thirteen-vertex witness
was established by these bounded searches. A citation match is not needed
for the self-contained certificate, but attribution remains open.
