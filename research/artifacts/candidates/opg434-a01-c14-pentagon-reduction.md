# C14: oriented pentagon pins and degree-two pentagon reductions

candidate_id: candidate:opg434-a01-c14-pentagon-reduction
problem_id: problem:opg-434-weak-pentagon
attempt_id: attempt:web-20260906-opg434-a01
route_id: route:odd-cycle-transversal-equivalence-v1
graph_id: graph:opg434-initial-v1
obligation_id: obligation:opg434-five-transversals-equivalence
primary_owner: math-derivation
verdict: candidate_only
base_revision: 44c810241c927303ece47a666d9a0f3d3b3031ac

Use C06's target notation: S={s_1,...,s_5}, sum S=0, and ij=s_i+s_j.
This is a paper construction, not an executed table search or kernel check.
The new positive boundary relation is restricted by TWO SPECIFIED PIN EDGES;
it does not replace C09's general five-pin relation.

## 1. Exact two-edge pin theorem

Write R5(a,b,c,d,z) when there is a cyclically ordered target five-cycle
(y_0,...,y_4), with each y_i adjacent to its corresponding pin.
Repeated pins are allowed; the two given target edges can share endpoints.

### claim:opg434-c14-two-edge-pentagon
If a is adjacent to b and c is adjacent to d, then
R5(a,b,c,d,z) holds if and only if b!=c, z!=a and z!=d.

The inequalities are necessary: equal consecutive pins would produce a
closed three-step walk in the loopless triangle-free target.
Below is a complete constructive proof of sufficiency. Every displayed
five-tuple is in cyclic order and respects the first four pins.
Let N(K) mean the union of neighborhoods of the elements of K. To permit
the fifth pin z, it suffices that an available last entry belongs to N(z).

### Case A: a adjacent to d

Normalize a=0,d=s_5. For every pair ij contained in {1,2,3,4}, choose
k among the other two indices. The five-tuple
(s_i,0,s_5,5k,ij)
works for the first four pins: its entries at positions 1 and 2 are
a and d, so the unspecified given pins b and c are automatically respected.
Its five successive differences are the five distinct generators.
The six possible last entries ij have neighborhood union exactly
V(B) minus {0,s_5}. Thus every z other than a,d works.

### Case B: a=d and b!=c

Normalize (a,b,c,d)=(0,s_1,s_2,0).
A last entry 0 is realized by (s_3,13,24,s_4,0).
Every last entry ij is also possible: orient i,j and choose distinct k,l
outside {i,j} so that 1 belongs to {i,k} and 2 belongs to {j,l}.
Then use (s_i,ik,jl,s_j,ij).

Such a choice always exists. If the pair is 12, take i=1,j=2.
If it contains just 1, put i=1,l=2; if just 2, put j=2,k=1.
If it contains neither, put k=1,l=2. Choose any remaining needed index
different from those already used.
The available last entries are therefore 0 and all ten pairs.
Their neighborhood union is V(B) minus {0}, so every allowed z works.

If some other equality occurs among a,b,c,d, it is either the excluded
b=c, or a=c, or b=d. The latter two imply a adjacent to d and were
already covered by Case A. Thus only four distinct pins remain.

### Case C: four distinct pins, a nonadjacent to d, and b adjacent to c

Triangle-freeness forces an induced four-vertex path. Normalize the pins
to (0,s_1,12,34). The following last entries are available:
K={34,35,45,0,13,14}.

For r in {34,35,45}, choose i in r and use
(s_i,0,s_1,12,r).
For r=0,13,14 use respectively
(s_1,12,34,s_3,0),
(s_1,12,34,s_3,13),
(s_1,12,34,s_4,14).
The neighborhood union N(K) is V(B) minus {0,34}.
For a direct check, 0 covers all five generators, and every pair other
than 34 is disjoint from at least one of the listed pair entries.
This gives all allowed fifth pins.

### Case D: four distinct pins, neither a-d nor b-c is an edge

The remaining possible cross edges are a-c and b-d. Three cases remain.

D1. Neither cross edge exists: normalize to (0,s_5,12,34).
Last entries r=34,35,45 are obtained from (s_i,0,s_1,12,r), i in r.
Last entry 0 is obtained from (s_5,15,34,s_3,0).
Their neighborhood union contains all generators and
{12,13,14,15,23,24,25}. The only additional allowed fifth pins are 35,45.
For them use respectively
(s_2,0,s_1,15,24) and (s_2,0,s_1,15,23).
These two cases differ by interchanging indices 3 and 4.

D2. Exactly one cross edge exists. Reflect the cyclic positions if needed
so it is a-c; normalize to (0,s_1,s_2,23).
Last entries 0,12,13 are realized by
(s_1,14,23,s_2,0),
(s_1,14,23,s_2,12),
(s_1,14,23,s_3,13).
Their neighborhood union contains all generators and {24,25,34,35,45}.
The remaining allowed fifth pins and suitable inner cycles are:
z=12: (s_3,13,24,15,34);
z=13: (s_4,14,23,s_2,24);
z=14 or z=15: (s_3,13,24,s_2,23).

D3. Both cross edges exist: normalize to (0,s_1,s_2,12).
For any generator fifth pin use (s_1,13,24,s_2,0).
For z in {34,35,45}, use (s_1,14,23,s_2,12).
For z=13 use (s_4,14,23,s_2,24).
Permutations of {3,4,5} and the combination of translation by 12
with the reflection i -> 3-i modulo five preserve the ordered four pins.
They take this last case to each of
13,14,15,23,24,25. Thus all allowed z except 0,12 are covered.

The unique generator relation verifies all displayed adjacencies.
For four distinct labels, two disjoint edges induce only 2K2, an induced
path or a four-cycle; the listed cross-edge alternatives cover their
ordered placements. The case analysis therefore proves the theorem.

## 2. Three sparse pins and a genuine pentagon reduction

### claim:opg434-c14-sparse-three-pins
A pentagon with prescribed pins only at positions 0,2,4 extends exactly
when its prescribed labels at 0 and 4 differ.

For sufficiency write these pins a,c,z. Choose a fictitious pin
b in N(a) minus {c}, and d in N(c) minus {z}.
Each choice is available since every target degree is five.
Section 1 applies to (a,b,c,d,z). Necessity is consecutive-pin inequality.

### claim:opg434-c14-two-degree-two-reduction
Suppose every smaller triangle-free subcubic graph maps to B.
If a triangle-free subcubic graph G has a five-cycle with two nonadjacent
degree-two vertices, then G maps to B.

Put the degree-two vertices at positions v_1,v_3, and delete the cycle.
Take a map of the smaller remainder H. The outside neighbors at v_0
and v_4, when both present, are distinct physical vertices, since equality
would create a source triangle. They have H-degree at most two.
If their images coincide, they are not adjacent in H; recolor one port
to a different feasible label using C06's at-least-two-choice lemma.
If one or both pins are missing, supply fictitious different labels.
The pin at v_2 is unrestricted and can also be fictitious if absent.
Section 2's sparse relation now restores the whole cycle.

Opposite source ports may coincide, and recoloring them changes both
occurrences together. This does not harm the sparse relation, whose only
constraint is on the physically distinct consecutive ports 0 and 4.
Thus repetitions and additional degree-two cycle vertices are covered.

By C06, a hypothetical vertex-minimum triangle-free subcubic counterexample
has no adjacent degree-two vertices. Consequently every five-cycle in
that same minimum has at most ONE degree-two vertex.

## 3. One degree-two vertex forces a belt of adjacent pentagons

### claim:opg434-c14-one-deficiency-belt
Let G have ordinary girth at least five, maximum degree at most three,
and a five-cycle v_0,...,v_4 on which v_1 has degree two and the other
four vertices have degree three. Write x_i for their outside neighbors
(i=0,2,3,4), and H=G-V(C).

Under the smaller triangle-free subcubic induction hypothesis, G maps
to B if at least one of the pairs
(x_2,x_3), (x_3,x_4), (x_4,x_0)
has no common neighbor in H.

All four ports are physically distinct: a shared port at consecutive
cycle positions creates a triangle, and one at distance two creates
a square. Each of the three listed pairs is nonadjacent in H, since
an edge between consecutive outside ports would create a source square.
Add an edge at the chosen pair. With no common neighbor this creates
no triangle; each endpoint had H-degree at most two, so degrees remain
at most three. The resulting H' is strictly smaller than G and maps to B.

Here are the three extension cases. Recoloring is always on the two
other actual ports, leaving the endpoints of the added edge fixed.

If the added edge is x_2x_3, use the ordered pins
(a,b,c,d,z)=(f(x_0), fictitious, f(x_2), f(x_3), f(x_4)).
Ports x_0,x_4 are nonadjacent in H', so their lists can be chosen
independently: choose z!=d, then a!=z. Choose b in N(a) minus {c}.
This satisfies Section 1.

If the added edge is x_4x_0, rotate the pins to
(a,b,c,d,z)=(f(x_4),f(x_0),fictitious,f(x_2),f(x_3)).
Ports x_2,x_3 are nonadjacent. Choose z!=a, then d!=z;
choose c in N(d) minus {b}. Again Section 1 applies.

If the added edge is x_3x_4, rotate to
(a,b,c,d,z)=(f(x_3),f(x_4),f(x_0),fictitious,f(x_2)).
If x_0,x_2 are nonadjacent, select c!=b and z!=a independently.
If they are adjacent, their H' degrees are at most two; C12's feasible
six-cycle lets that source edge avoid both fixed labels a,b.
In either event choose d in N(c) minus {z}. Section 1 applies.
The arbitrary relabeling of adjacent ports is NOT treated as independent;
that case explicitly uses the low-degree edge lemma.

Discard the virtual edge, and the constructed map is a map of G.
This proves all three cases without assuming an initially favorable map.

Thus, in the minimum counterexample from C12, a pentagon with one
degree-two vertex must have an exterior common neighbor for EACH of
the three listed consecutive port pairs. Each common neighbor creates
another five-cycle sharing the corresponding edge of the first pentagon.
No claim is made that these extra vertices or extra cycles are all
disjoint. The joint belt configuration, not an arbitrary drawing of it,
is the next unresolved local case.

## 4. Adversarial checks and precise limits

The target has four-cycles. Therefore a three-step walk between adjacent
endpoints need not backtrack: (0,s_2,12,s_1) is a counterexample to that
shortcut. The proofs above use actual five-cycles instead.

The boundary (0,s_5,12,34,35) EXTENDS by
(s_2,0,s_1,15,24). It must not be recorded as a failed pentagon boundary.
This positive fixture guards the same incorrect backtracking inference.

C13's checkpoint observation that two pin edges alone are insufficient
means the missing consecutive inequalities still matter. Section 1
now shows that, with those inequalities, the two oriented edge
constraints are sufficient. No previously merged mathematical claim
is silently changed.

The theorem does not say that all five low-degree ports of an arbitrary
cubic pentagon can be made to satisfy the two-edge pin hypothesis.
Nor does it settle the one-deficiency belt or the all-degree-three
pentagon. A fixed-boundary obstruction is still not root nonexistence.

## 5. Audit, dependencies and next action

Audit the cyclic order and all pin adjacencies in every displayed tuple,
then the complete ordered cross-edge classification. In Section 2
track repeated physical ports. In Section 3 distinguish adjacent
free ports from independent ones, and check the virtual-edge domain.

Candidate dependencies:
C06 target symmetries and low-degree flexibility;
C09 definition and full scope of the pentagon relation;
C12 low-degree edge six-cycle and ordinary-girth-five minimum.
No external theorem, executable search or hidden computation is invoked.
No novelty is asserted, and the source comparison remains the earlier
bounded literature review rather than a new exhaustive search.

best_verified_result=none; best_verified_candidate=none.
Both admitted obligations remain open. No truth records changed.

Next: audit the possibility of a bounded-radius repair strategy itself.
A proposed infinite pinned-tree construction may force a remote
boundary obstruction even in positive cubic girth-five graphs.
That requires an explicit full map, an explicit obstructed partial map,
and an exact distance/connectivity audit before it is usable.
