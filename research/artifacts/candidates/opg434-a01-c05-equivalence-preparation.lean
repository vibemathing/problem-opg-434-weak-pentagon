/-
OPG434 conditional formalization preparation.
Status: candidate_only. This file has NOT been built or kernel-verified.
It is supplemental preparation, not a new packet or an admitted theorem.
The BipartiteCycleCriterion premise is an unresolved dependency: the final
application must supply the actual graph theorem and audit its assumptions.
No arbitrary cycle carrier is substituted for the graph's cyclic sequences.
Problem: problem:opg-434-weak-pentagon
Target: obligation:opg434-five-transversals-equivalence
-/
import Std

universe u

namespace OPG434Preparation

structure SGraph (V : Type u) where
  Adj : V → V → Prop
  symm : ∀ {v w : V}, Adj v w → Adj w v
  loopless : ∀ v : V, ¬ Adj v v

structure EdgeColoring {V : Type u} (G : SGraph V) where
  color : ∀ {v w : V}, G.Adj v w → Fin 5
  symm : ∀ {v w : V} (h : G.Adj v w), color h = color (G.symm h)

/-- The vertex type is unchanged: this is a spanning edge-deleted graph. -/
def retained {V : Type u} (G : SGraph V) (c : EdgeColoring G)
    (i : Fin 5) : SGraph V where
  Adj := fun v w => ∃ h : G.Adj v w, c.color h ≠ i
  symm := by
    intro v w hRet
    cases hRet with
    | intro h hne =>
      refine ⟨G.symm h, ?_⟩
      intro heq
      exact hne ((c.symm h).trans heq)
  loopless := by
    intro v hRet
    cases hRet with
    | intro h hne => exact G.loopless v h

/-- A actual cyclic sequence, with distinct vertices before its closing step. -/
structure CycleFrame (V : Type u) where
  length : Nat
  length_ge_three : 3 ≤ length
  vertex : Nat → V
  closed : vertex length = vertex 0
  injective_before_close : ∀ j k : Nat,
    j < length → k < length → vertex j = vertex k → j = k

def IsCycle {V : Type u} (G : SGraph V) (C : CycleFrame V) : Prop :=
  ∀ j : Nat, j < C.length → G.Adj (C.vertex j) (C.vertex (j + 1))

def OddLength (n : Nat) : Prop := ∃ k : Nat, n = 2 * k + 1

def NoOddCycles {V : Type u} (G : SGraph V) : Prop :=
  ∀ C : CycleFrame V, OddLength C.length → ¬ IsCycle G C

def Bipartite {V : Type u} (G : SGraph V) : Prop :=
  ∃ b : V → Bool, ∀ {v w : V}, G.Adj v w → b v ≠ b w

def UsesColor {V : Type u} {G : SGraph V} (c : EdgeColoring G)
    (i : Fin 5) (C : CycleFrame V) : Prop :=
  ∃ j : Nat, ∃ hj : j < C.length,
    ∃ h : G.Adj (C.vertex j) (C.vertex (j + 1)), c.color h = i

/-- The same cyclic sequence survives exactly when all its edges avoid i. -/
theorem retained_cycle_iff {V : Type u} (G : SGraph V)
    (c : EdgeColoring G) (i : Fin 5) (C : CycleFrame V) :
    IsCycle (retained G c i) C ↔ IsCycle G C ∧ ¬ UsesColor c i C := by
  constructor
  · intro hCycle
    constructor
    · intro j hj
      cases hCycle j hj with
      | intro h hne => exact h
    · intro hUses
      cases hUses with
      | intro j hRest =>
        cases hRest with
        | intro hj hRest2 =>
          cases hRest2 with
          | intro h heq =>
            cases hCycle j hj with
            | intro h' hne => exact hne heq
  · intro hBoth
    intro j hj
    let h := hBoth.1 j hj
    refine ⟨h, ?_⟩
    intro heq
    exact hBoth.2 ⟨j, hj, h, heq⟩

theorem no_odd_retained_iff {V : Type u} (G : SGraph V)
    (c : EdgeColoring G) (i : Fin 5) :
    NoOddCycles (retained G c i) ↔
      ∀ C : CycleFrame V, OddLength C.length → IsCycle G C →
        UsesColor c i C := by
  constructor
  · intro hNo C hOdd hCycle
    exact Classical.byContradiction (fun hAvoid =>
      hNo C hOdd ((retained_cycle_iff G c i C).2 ⟨hCycle, hAvoid⟩))
  · intro hHit C hOdd hCycle
    have hBoth := (retained_cycle_iff G c i C).1 hCycle
    exact hBoth.2 (hHit C hOdd hBoth.1)

/-- This is an explicit theorem dependency, not an assumption-free conclusion. -/
def BipartiteCycleCriterion (V : Type u) : Prop :=
  ∀ G : SGraph V, Bipartite G ↔ NoOddCycles G

theorem fixed_color_equivalence {V : Type u}
    (criterion : BipartiteCycleCriterion V) (G : SGraph V)
    (c : EdgeColoring G) (i : Fin 5) :
    Bipartite (retained G c i) ↔
      ∀ C : CycleFrame V, OddLength C.length → IsCycle G C →
        UsesColor c i C :=
  (criterion (retained G c i)).trans (no_odd_retained_iff G c i)

theorem five_color_equivalence {V : Type u}
    (criterion : BipartiteCycleCriterion V) (G : SGraph V)
    (c : EdgeColoring G) :
    (∀ i : Fin 5, Bipartite (retained G c i)) ↔
      ∀ i : Fin 5, ∀ C : CycleFrame V,
        OddLength C.length → IsCycle G C → UsesColor c i C := by
  constructor
  · intro h i
    exact (fixed_color_equivalence criterion G c i).1 (h i)
  · intro h i
    exact (fixed_color_equivalence criterion G c i).2 (h i)

/-- Ordered edge tokens; the symmetry theorem below permits quotient descent. -/
abbrev OrientedEdge {V : Type u} (G : SGraph V) :=
  {p : V × V // G.Adj p.1 p.2}

def edgeColor {V : Type u} {G : SGraph V} (c : EdgeColoring G)
    (e : OrientedEdge G) : Fin 5 := c.color e.property

def Fiber {V : Type u} {G : SGraph V} (c : EdgeColoring G)
    (i : Fin 5) (e : OrientedEdge G) : Prop := edgeColor c e = i

theorem one_fiber_per_edge {V : Type u} {G : SGraph V}
    (c : EdgeColoring G) (e : OrientedEdge G) :
    ∃ i : Fin 5, Fiber c i e ∧ ∀ j : Fin 5, Fiber c j e → j = i := by
  refine ⟨edgeColor c e, rfl, ?_⟩
  intro j hj
  exact hj.symm

def reverseEdge {V : Type u} (G : SGraph V)
    (e : OrientedEdge G) : OrientedEdge G :=
  ⟨(e.val.2, e.val.1), G.symm e.property⟩

theorem fiber_reverse {V : Type u} (G : SGraph V)
    (c : EdgeColoring G) (i : Fin 5) (e : OrientedEdge G) :
    Fiber c i (reverseEdge G e) ↔ Fiber c i e := by
  change c.color (G.symm e.property) = i ↔ c.color e.property = i
  constructor
  · intro h
    exact (c.symm e.property).trans h
  · intro h
    exact (c.symm e.property).symm.trans h

end OPG434Preparation
