# Checkpoint 0 (2026-09-02, before batch 1)

Opus attacked the three committed proof files. Verdict records: `runs/02-attack`, `runs/03-attack`,
`runs/04-attack`. This note carries what batch 1 must do (step 0) and what ticket 11 must know.

## Verdicts

| Proof | Verdict | Outcome |
|---|---|---|
| `proofs/02_garbling.tex` (garbling lemma, threshold theorem) | PASS | gate passed; wording nits below |
| `proofs/03_caught.tex` (who gets caught) | PASS | gate passed; wording nits below |
| `proofs/04_inherited.tex` (four inherited results) | FAIL on the clock theorem, the other three hold | one fix in batch 1, attack 2 at checkpoint 1 |

## Step 0 of batch 1

**`04-fix` (RESULT).** Theorem "The clock dial" (`thm:clock`, `proofs/04_inherited.tex` near
line 656). The hypothesis list assumes only fixed κ, τ, plan and cutoff policies,
0 < Ω(τ,T) < 1, 0 < Ω(τ,T') < 1 and S_P(κ,τ,T) > 0, but clauses (ii) and (iii) invoke
`prop:factorisation` at both clocks, whose two extra hypotheses (κ-invariance of the flagged
endpoint M_F, differentiability of κ → M_P) are assumed at neither, and S_P(κ,τ,T') is used in
the definition of C_T without anything making it exist. Counterexample with everything affine
in κ and Ω κ-free and interior at both clocks: Ω(τ,T) = 0.4, Ω(τ,T') = 0.6, ∂_κ M_F(T) = 0,
∂_κ M_P(T) = 1, ∂_κ M_F(T') = 10, ∂_κ M_P(T') = 1 gives S(T) = 0.6, S(T') = 6.4, W_T C_T = 2/3,
so clauses (ii) and (iii) fail as stated. Fix once: add to the theorem's hypotheses that the
hypotheses of `prop:factorisation` hold at both clocks and that κ → M_P(κ,τ,T') is
differentiable, exactly as clause (iii) of `lem:threshold-weight` already gates on the
proposition at both thresholds, and cite them where the proof says "By the factorisation".
Do not change the proof's logic. Apply the 04 wording nits below in the same edit. Say in the
summary what changed.

**`02-nits` and `03-nits` (RESULT each).** Wording only, no label changes, no new claims. The
checkpoint diff confirms that only wording moved.

02 nits (`proofs/02_garbling.tex`): (i) state, at `eq:g-kernel`, that the map h(ν) = h(π(ν),
v̂(ν)) carries no κ, since Lemma g3(a) rests on it; (ii) the proof of Theorem (B) says it used
b_0 < τ'; it did not (c(τ') ≤ c(τ) follows from the set inclusion for any τ' < τ), so drop that
sentence.

03 nits (`proofs/03_caught.tex`): (1) the hypothesis list (C-1) to (C-3) should name or
cross-reference the standing conditions it consumes: the single-place entry of κ (S11) for part
(ii) and the pinned kernel version (S8) for part (iii); (2) the gloss near line 102 and part
(iii)'s "the sensitivity of what it takes out" read as s̃_B; say that s_B is the derivative of
Λ_T minus Λ_T', which carries the survivors' re-pricing; (3) in part (vi)(b) "share a sign"
reads s_A s_B > 0, since (a) owns s_B = 0; (4) part (vi)(c) does not need φ > 0 to force a
common sign, ρ ≥ 1 > 0 suffices; (5) add a half-sentence that (C-3)'s clause 0 < Ω(τ,T) is
there so that the clock theorem applies; (6) qualify the Reading paragraph's "a cut that takes a
small share of the pool faces only the first two requirements" by the condition (vi)(e) states.

04 nits (`proofs/04_inherited.tex`, with the fix): (1) `thm:clock` and `lem:threshold-weight`
consume b_0 < τ, Voice date-monotonicity (S4) and "only Voice plans cross" (S5) through the
clock equivalence; make those visible in each statement so extraction into the appendix loses
nothing; (2) `lem:partition` Step 6 says the history-to-cell map is onto {C_F, C_P} while Step 7
allows Ω in {0, 1}; reconcile; (3) note that M_P being defined rests on (S8) granting that prices
exist, since (S4) states Borel regularity for Voice paths only; (4) S = |∂_κ Δ^act| is the noise
sensitivity of the expected engagement premium, not of a price; say so where both weight-leg
proofs say "price"; (5) `prop:factorisation` Step 5 speaks of differentiability "in a policy
coordinate", but T is an integer; drop it; (6) `eq:flagged-MF` cites the partition result stated
later in the file; pin the reference so the appendix reads in order; (7) the closing sentence of
`lem:threshold-weight` is circular as written; the intended reading is the ceiling
C_τ ≤ 1/W_τ.

## Label scope, for checkpoint 1 and ticket 11

- Threshold dial (02). PROVED: the factorisation, the weight leg (Ω rises), the closed form of
  S_P in κ (Lemma g3), the garbling lemma. NUMERICAL: the composition leg. Condition D is
  equivalent to C_τ ≤ 1, so it is the conclusion restated, not a condition on primitives; it
  holds at every node of the grid κ in [0.15, 0.85], mark 2, H 10, with the tightest margin
  W_τ C_τ = 0.772, and it fails just below the grid (the T = 5 pair q0.5 → q0.3 has W_τ C_τ > 1 on
  κ in [0.1440, 0.1485]). The paper names the grid at the point of claim and never says "for
  every κ". At T = 10 the τ ladder reclassifies nothing at this calibration (Ω = 0.00068 at all
  five quantiles, below the code's degenerate-cell floor), so the threshold content rests on the
  four T = 5 pairs; the numerical section states this. Lemma g3(c)'s curvature hypothesis fails at
  every node and Remark `rem:g-Dstar`'s κ-free form holds at no pair: the garbling machinery is a
  proved result in its own right and contributes to neither leg on this grid. Conditional on the
  04 attack 2 for the two imported results.
- Who gets caught (03). PROVED: the cut identity and the two-sided characterisation of C_T ≤ 1
  in s_B (between s_A and (2 minus φ)/φ times s_A). The one-sided shorthand is not what is
  proved; the paper states the corollary. Any directional sentence about what the clock catches
  is NUMERICAL off the who-gets-caught grid record.
- Inherited results (04). The partition and factorisation, the flagged cell's κ-invariance and
  the weight leg pass. The clock theorem's label waits on attack 2.

## Records

`runs/02/result.txt` and `runs/03/result.txt` are the attack-gate outcomes; `runs/04/result.txt`
records the FAIL and the pending fix. The Condition D check is committed (`ac9ac72`).
