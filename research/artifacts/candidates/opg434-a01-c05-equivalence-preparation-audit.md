# OPG434 conditional Lean preparation: dependency and faithfulness audit

Status: candidate_only. The companion file `research/artifacts/candidates/opg434-a01-c05-equivalence-preparation.lean` is an unbuilt formalization candidate. Neither a successful build nor any axiom or statement-faithfulness receipt has been observed. It is supplemental preparation, not a second Web packet or a closed obligation.

Binding: problem:opg-434-weak-pentagon / attempt:web-20260906-opg434-a01 / route:odd-cycle-transversal-equivalence-v1 / graph:opg434-initial-v1 / obligation:opg434-five-transversals-equivalence. Root obligation:opg434-root remains open. The main research owner remains math-derivation; this preparation uses the previously read formalization interface discipline.

## What the code actually says

`SGraph V` has a symmetric irreflexive adjacency relation. `EdgeColoring G` assigns a `Fin 5` value to each adjacency proof and requires the same value after reversing an edge. Proof arguments live in propositions, so proof irrelevance is relevant to the equality used in `retained_cycle_iff`; it must be checked by the actual kernel, not merely assumed from the paper outline.

`retained G c i` has exactly the SAME vertex type V. Its adjacency consists of original edges whose color differs from i. Symmetry of the coloring is used explicitly to prove that this retained graph is still undirected.

`CycleFrame V` is not an unconstrained external carrier. It specifies a natural-number length at least three, a vertex sequence, closure at that length, and injectivity on indices before closure. `IsCycle G C` asserts every successive edge in this cyclic sequence is an actual edge of G. Values of the sequence after the closing index are ignored; they do not affect any predicate. Ordinary cycle witnesses can be extended arbitrarily beyond their closing index, and conversely the restricted sequence is a genuine simple cycle. This correspondence still needs a formal transport proof to the verifier's adopted graph library.

`retained_cycle_iff` proves that this exact cycle frame is a cycle in the retained graph if and only if it is an original cycle and uses no edge of color i. Length, vertex sequence, closure and simplicity are literally unchanged. `no_odd_retained_iff` then proves the odd-cycle hitting formulation, using classical contradiction explicitly.

## The essential unresolved theorem premise

`fixed_color_equivalence` and `five_color_equivalence` take a parameter

`criterion : BipartiteCycleCriterion V`.

That parameter states the actual graph theorem `Bipartite G` if and only if `NoOddCycles G`, for graphs on V using these definitions. It is not supplied or proved in this candidate. The formal results are CONDITIONAL on it. An accepted result for the frozen target must either prove it in this representation or transport an already proved version from the pinned graph library. A kernel build of the present file alone does not supply that missing premise and must not close the target.

This is a deliberate named dependency, not an arbitrary definition of bipartiteness by the conclusion being proved. `Bipartite` is independently defined as a Bool vertex partition crossing every edge. The exact missing theorem, its assumptions and its encoding transport remain visible.

## Partition and color-label boundary

`one_fiber_per_edge` proves that each oriented edge token belongs to exactly one of the five labeled fibers. It does not require nonempty fibers or properness. `fiber_reverse` proves membership is unchanged by reversing orientation, providing the necessary ingredient for descending to unordered edges. The actual quotient construction and comparison to the canonical edge set remain to be completed or imported faithfully.

`Fin 5` uses labels 0,...,4; the contract names colors 1,...,5. These sets are related by the explicit renaming i to i.val+1. The mathematical property is invariant under this bijection, but a statement-faithfulness wrapper must record it rather than pretend the literal index sets are identical.

The code does not use cubicity, triangle-freeness or finiteness in the conditional transformation. This is appropriate for the general equivalence. Application to the canonical problem still requires the wrapper fixing a finite simple triangle-free cubic input and the canonical coloring representation. No universal existence theorem is present: the coloring c is fixed as an input throughout.

The rainbow 5-cycle consequence is in the paper candidate c01, not yet formalized in this file. It must not be reported as a theorem built by this preparation.

## Requested verification procedure, not an executed command

First freeze and read the actual candidate bytes and their SHA-256. Resolve the admitted Lean environment from the fixed repository's `fixtures/lean-proof/lean-toolchain`, `lakefile.toml`, and `lake-manifest.json`, recording their actual versions and digests. No version is inferred here from past documentation, and the channel's lack of command-execution admission has not been bypassed.

A verifier operating in that authorized fixture could test the file from the fixture directory with the planned command:

```sh
lake env lean ../../research/artifacts/candidates/opg434-a01-c05-equivalence-preparation.lean
```

The intended working directory is `fixtures/lean-proof`, not an absolute host path. This command has NOT been run. The verifier must confirm the actual runner's path convention and use bounded execution, for example one CPU thread, a 120-second timeout, a 1-GiB memory limit and at most 1 MiB of retained output, or stricter limits imposed by its admitted runtime. These are proposed limits, not measured usage or permissions.

If the file elaborates, inspect the printed axiom dependencies of the conditional theorems and the actual definition of `Classical.byContradiction`. Then separately instantiate the graph criterion and complete cycle/color/edge-quotient faithfulness. A build error is a candidate code defect to repair in allowed paths, not a mathematical counterexample. A build success is only a check of the conditional encoded statements, not a verification of an uninstantiated dependency or of the universal existence problem.

## Continuation

Before registering this preparation, recover actual main and c05 PR head, verify the requested file writes, and compute digests from the retrieved bytes. Select it for a later uniquely bound packet after transport is restored. Do not change the verifier registry, Harness, schema, fixed Lean fixture, records or admission state from this candidate branch. Both admitted obligations remain open until their actual evidence and admission gates are satisfied.
