# Layered repair obstruction: terminology and source-faithfulness note

verdict: candidate_only
retrieval_date: 2026-09-07
scope: bounded primary-source comparison, not a comprehensive prior-art search

## The frozen root

Robert Samal, "Weak pentagon problem", Open Problem Garden:
https://www.openproblemgarden.org/op/weak_pentagon_problem
The original five-color deletion condition matches the repository's frozen
root: it asks for existence of an edge assignment, not extension of every
partial target homomorphism. Both the C15 construction and the layered construction explicitly admit
a total map, so they supply no negative instance of that root.

## A related but distinct literature notion

Richard C. Brewster, Jae-Baek Lee, Benjamin Moore, Jonathan A. Noel,
and Mark Siggers, "Graph Homomorphism Reconfiguration and Frozen H-Colourings".
arXiv:1712.00200:
https://arxiv.org/abs/1712.00200
Journal of Graph Theory 94(3), 398-420 (2020); DOI 10.1002/jgt.22530:
https://doi.org/10.1002/jgt.22530

The consulted abstracts study reconfiguration by changing the image of one
vertex at a time. Their frozen coloring is a FULL homomorphism with no
available such single-vertex move. Full paper proofs were not consulted.

The repository's C15 starts with a homomorphism of G minus one vertex.
The new layered candidate deletes an induced pentagon instead and works
in three-vertex-connected cubic girth-five graphs with only trivial
three-edge cuts. It forbids a completion agreeing outside a fixed ball
and also bounds below how many old vertex labels any completion changes.
Simultaneous changes anywhere are allowed; no sequence of valid
single-vertex moves is required.

The quantities, quantifiers, and input states therefore differ. The paper's
title is not a theorem citation establishing the layered candidate; no novelty,
complexity classification, or full frozen-coloring conclusion is inferred.
The primary abstracts provide terminology only.

## What supplies the new claims

The neighborhood identities, exact tree-message induction, five-layer
completion, full and partial map formulas, cut formula and forced-edit
path are proved in the self-contained local candidate. It remains a
paper candidate. The bridge-based C15 proof was separately read from
PR #18 and is not being republished or overwritten.
The source materials are locators and bounded paraphrases only; no paper,
figure, search-result dump, private data, or conversation was mirrored.
