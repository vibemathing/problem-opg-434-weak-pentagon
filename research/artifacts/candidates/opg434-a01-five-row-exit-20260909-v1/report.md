# Five-row EXIT candidate: exact-byte recovery and theorem scope

candidate_id: candidate:opg434-a01-five-row-exit-20260909-v1
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-root
verdict: candidate_only
state: NONTERMINAL_CHECKPOINT
best_verified_result: none
base_revision: 6e702ed29bbc11072ac3376c1c3300cb9958419d

## 1. Recovery, not a new computation receipt

PR31's former three payload files did not match its former index. They must not be used as the intended mathematical certificate. The repair replaces them, adds two payload parts, and replaces the index and decoder using the exact 37 logical files supplied in opg434-five-row-exit-recovery.zip. The ZIP SHA-256 is c07f8d1930f475b3b99e4e331a14fe5e4059b94bfe9541dc807816325e270950. All original logical file bytes are preserved, including the immutable producer, consumer, result and execution variants. This report is a current wrapper, not a rewrite of an old execution record.

Run `python restore.py` in this directory. It checks five part lengths, SHA-256 and Git blob IDs, compressed and decoded identities, bounded XZ EOF, 37 unique safe names, all file hashes and the total 476175 logical bytes. It restores into a new `restored/` directory and executes no archived program. The raw JSON is 501309 bytes, SHA-256 1704c78881bb86a19877225d7fbd0cbd465ec72e44b18cdc6c523c9c8788205c. The XZ is 30040 bytes, SHA-256 a43aa451f485c925e6d50770785dc049ccd2abe994f8f556c6c7fc913a798417.

The full original self-contained proof is `restored/report.md`: 15794 bytes, SHA-256 bf21f5fb4226525db6324d0c0a6abbb0b3a9d2275781510279082b5edae143af. This repair actually decoded and hash-checked all 37 files. This is an integrity execution only, not another mathematical replay. The separately preserved physical-exit40 and source-admissibility36 collections retain their own code and receipts; none is relabeled as this recovery37 variant.

## 2. Exact five-row shared-kernel statement

For a bipartite signed instance with five left vertices, write its edge equation as
`t_ij = h_i + h_j + a_i*b_j + a_j*b_i`, over GF(2).
Let E5 be the even subspace of GF(2)^5. For each of its 35 two-dimensional subspaces K, impose on one SHARED left vector h every equation
`u.h = sum_i u_i*t_ij`
for every column j and every u in K whose support lies in that column's neighbor set. The original instance is solvable exactly when one such common system is consistent.

Necessity: row vectors (1,b_i,a_i) have a kernel of dimension at least two inside E5; choose a two-dimensional K. Summing the original equations on any supported dependency gives the displayed common equation. Sufficiency: K-perpendicular has dimension three and contains the all-ones vector. Extend that vector to a basis (1,b,a). These row vectors have kernel exactly K. Every dependency in each column then has zero right-hand sum, so its three-unknown linear system can be solved with the already fixed shared left h. Solving all columns and putting z=h+ab yields every original edge equation. Low-rank initial solutions are covered by choosing a subspace of their larger kernel.

The joint condition cannot be replaced by independently checking each support. The supports 15,23,24 sum to zero, so assigning their right-hand parities 0,0,1 is inconsistent even when each support appears in only one column. Equal parallel rows remain separate physical checks; opposite parallel signs or a negative loop are not discarded.

## 3. Physical five-side theorem and finite dependency

The preserved proof considers finite simple triangle-free cubic sources and cuts whose same-side edges form a matching F and whose crossing edges on the endpoints W satisfy maximum degree at most one. A maximum cut has these properties, but they do not characterize maximum cuts.

If the smaller quotient side has five components, the raw degree identity is `15+r=3k+u`, where r,u count paired components and k is the other side size. Thus k is five or six. For k=6 the only possible distribution is r=3,u=0; explicit distinct affine row types solve every column. For k=5, r=u<=3. The preserved report gives explicit simultaneous constructions for r=0,1 and a balanced-phase proof for r=3. The remaining r=2 case has a COMPLETE finite certificate: 1155 matrices, 16 type-preserving matrix orbits and 401 endpoint configurations, each with a full physical graph, quotient rows, parameters and B-map. The r=3 control independently records 21 matrices, 3 orbits and 192 endpoint configurations. These are not counts of nonisomorphic cubic graphs.

The retained consumer reconstructs the reduced domain by a different block census, checks equality of the complete case sets, uses column-space elimination and verifies all source edges plus the inverse map-to-parameter bridge. The recorded result is 593 positive configurations, 13029 physical edge checks, 10273 raw GF rows, no failed configuration. The retained controls record 21 negative and five positive outcomes. These are HISTORICAL frozen receipts, not reexecuted during this transport repair, and not a registered trusted domain.

Consequently the candidate theorem excludes a maximum-cut obstruction with a quotient side of size at most five. Its residual r=2 step depends on the complete finite certificate; this is not a purely handwritten universal proof without a finite dependency. No property of a particular W-valid sample is silently promoted to actual maximum-cut status.

## 4. Boundary for the next obligation

For m>=3 left rows the same equivalence uses (m-3)-dimensional K inside the (m-1)-dimensional even space. The number is the Gaussian binomial [m-1 choose 2]_2. Five rows give 35; SIX rows give 155, not 35. A six-row argument must handle one common h across all columns and every supported member of the same K. Separately feasible five-row projections do not supply that h.

General EXIT for actual quotients with both sides at least six remains open. No assertion that one of the 155 systems must be consistent is made. No root counterexample, root proof, statement-faithfulness receipt or trusted closure is claimed. No old belt, h1, graph22 census or rejected gadget search was repeated. The sole live transaction is PR31's existing physical-exit packet; no second active packet is introduced.
