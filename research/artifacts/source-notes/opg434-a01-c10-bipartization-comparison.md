# C10 source and statement comparison

verdict: candidate_only
retrieval_date: 2026-09-06
scope: bounded source comparison, not novelty certification or mathematical admission

## Primary sources actually read

1. Robert Samal, Weak pentagon problem, Open Problem Garden, posted 2007-07-13.
https://www.openproblemgarden.org/op/weak_pentagon_problem
Read the conjecture and reformulations on the HTML page. The source asks for
triangle-free cubic graphs and the B/Clebsch target, not a prescribed partial
homomorphism and not a vertex-deletion bound. C10 proves its conclusion on
the extra subclass tau_v<=2 and also permits higher source degrees there.

2. Matt DeVos and Robert Samal, High-girth cubic graphs are homomorphic to
the Clebsch graph, arXiv:math/0602580v2, revised 2009-10-23.
https://arxiv.org/abs/math/0602580
Publisher record: Journal of Graph Theory 66(3), 241-259 (2011).
https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20580
The arXiv HTML abstract and publisher indexed abstract were read.
Their sufficient hypothesis is maximum degree three and ordinary girth
at least seventeen. C10 uses a different sufficient hypothesis: deleting
at most two vertices makes the graph bipartite. C10's eight-vertex witness
has short cycles and is not covered by that high-girth hypothesis.
No part of the computer-assisted proof was replayed here.

No PDF analysis is claimed in this cycle. The present tables and their
generator differences have self-contained paper proofs.

## Search coverage and limits

Queries included:
- "Clebsch" "bipartization"
- "Clebsch" "two vertices" "triangle-free"
- "triangle-free subcubic" "Clebsch"
- "triangle-free cubic" "Clebsch" conjecture
- "Weak Pentagon" solved

No exact source for C10's two-apex table theorem was identified in the
retrieved primary material. This is not a claim that the theorem is new,
nor a claim of exhaustive literature coverage or a proof of current open status.
An automated conjecture-status page was not used as mathematical authority.
Leads concerning K5-minor-free graphs and planar projective-cube bounds
require further primary-source checking; direct requests for DOI
10.1016/j.disc.2009.04.032 and the Wiley abstract for 10.1002/jgt.21708
returned Cache miss and 403 respectively. They are not substituted for C10's proof.

## Exact terminology and quantifiers

tau_v counts deleted vertices. The admitted five transversals consist of
edges. Their sizes and packing properties are not equated.

C10 constructs SOME whole-graph homomorphism from a bipartition. It does
not promise to extend EVERY map of the remaining graph. Its two legal
subset translations start from a specified monochromatic bipartite map.
The complete pair relation ranges over all maps and records both
length-two and length-three path obstructions without a shortest-distance shortcut.

The eight-vertex cubic example rejects only the stronger C5 target.
Its displayed B map explicitly prevents its use as a root counterexample.

## Candidate dependencies

At base 048a5a5f0ddb8bc3f822eacd5770721f4e9ac968:
research/artifacts/candidates/opg434-a01-c02-normalization.md
research/artifacts/candidates/opg434-a01-c06-separator-gluing.md
research/artifacts/candidates/opg434-a01-c08-cut-switches.md

These remain candidates. No EvidenceLink, independent review or kernel
receipt is inferred from a citation, table, PR, check or merge.
