# Review Memo: `fix.md` vs `draft_v2.tex` (Theory)

Date: 2026-03-03

Scope:
- Compare proposed patch plan in [`fix.md`](../../fix.md) against current manuscript source [`draft_v2.tex`](../../draft_v2.tex).
- Cross-check against the *current implemented theory code* under `numerical/` (not changing any files; this memo is descriptive).

Key files referenced:
- `directory/fix.md`
- `directory/draft_v2.tex`
- `directory/numerical/model.py`
- `directory/numerical/params.py`

## Executive Summary

1. `draft_v2.tex` still reflects the *old* model engine:
- bidder observes `(P(X,D), D)` and uses a **price-contingent** entry probability `p(P,D)` (Normal CDF),
- takeover offer is `b(X,D,a)=P(X,D)+m^R(a)`,
- prices are defined by a **pricing fixed point** with an explicit “bounded feedback” assumption (A5),
- noise probabilities are the *old* `p0=1-kappa, p1=kappa/2`.

2. `fix.md` proposes a *new* engine:
- bidder arrival `lambda_B`, bidder observes `(X,D)` directly (no injectivity assumption),
- bid probability is **decoupled from P**, and pricing becomes feed-forward,
- noise probabilities changed to `p0=1-2kappa/3, p1=kappa/3` to avoid `p0 -> 0` at `kappa -> 1`,
- plus additional changes: Logistic synergy, and an activism-induced synergy term `Delta_S`.

3. Current `numerical/` code already implements a subset consistent with the “atomic bundle” approach:
- new noise probabilities `p0=1-2kappa/3, p1=kappa/3`,
- bid probability decoupled from price and scaled by `lambda_B`,
- feed-forward/direct pricing.

But the code does *not* implement the Logistic/`Delta_S` parts of `fix.md`, and its bidder entry threshold is materially different from `fix.md` (details below).

Bottom line: the core direction of `fix.md` (decouple from P, feed-forward pricing, noise fix, lambda_B) is coherent and matches the implemented direction. However, some `fix.md` components (Logistic, `Delta_S`, and the “Quiet Accumulation dominance” lemma as written) are either (a) inconsistent with current code, (b) internally inconsistent in the economic definitions, or (c) likely incorrect without stronger assumptions / careful equilibrium-beliefs handling.

## Compatibility Matrix (Current State)

Legend: OK = consistent, MISMATCH = conflicts, TBD = depends on spec choice.

- Fix 2 (noise probs): `fix.md` vs `draft_v2.tex` = MISMATCH. `fix.md` vs code = OK.
- Fix 1.1 (bidder observes (X,D), lambda_B): `fix.md` vs `draft_v2.tex` = MISMATCH. `fix.md` vs code = OK in spirit.
- Fix 1.3/1.5/1.6/1.8/1.9 (feed-forward pricing, remove A7, drop price fixed point): `fix.md` vs `draft_v2.tex` = MISMATCH. `fix.md` vs code = mostly OK.
- Fix 1.2 / Priority 3 (Logistic synergy + `Delta_S` + entry rule depending on `hat V`): `fix.md` vs `draft_v2.tex` = MISMATCH. `fix.md` vs code = MISMATCH.
- Fix 4 (Quiet Accumulation lemma): `fix.md` vs `draft_v2.tex` = draft currently *implicitly* ignores QA; `fix.md` tries to justify it. Logical correctness of the lemma = questionable as currently stated (see below).

## Detailed Notes by `fix.md` Item

### Fix 1.1 (Timeline / bidder arrival `lambda_B`)

Proposed in `fix.md`:
- bidder arrives with probability `lambda_B` and observes `(X,D)` directly.

Assessment:
- This is a clean way to target realistic bid rates without forcing extreme parameter values.
- Observing `(X,D)` directly is also a clean way to drop “price injectivity” (A7) and avoid conditioning on `(P,D)` altogether.

Consistency:
- Draft currently says bidder observes `(P(X,D), D)` and needs A7 on `D=0` to infer `X`. This would need to change if Fix 1.1 is adopted.

### Fix 1.2 (Bidder entry + payout overhaul)

This is the highest-risk part of `fix.md` as written.

Core good idea:
- Remove `P` from the bidder entry probability to eliminate recursive pricing and the “premium-on-premium” issue.

But there are two conceptual issues to reconcile.

Issue A: What does `bar S` represent (incremental synergy vs total value)?
- In `draft_v2.tex`, bidder surplus is `Pi_B = bar S - P + xi - bar m - K`, which reads like `bar S` is an incremental synergy term (net of paying the target’s market value `P`).
- In `fix.md`, bidder surplus becomes `Pi_B = (bar S + pi Delta_S) + xi - b(X,D) - K`, where `b(X,D)` includes `hat V(X,D)`.

If `bar S` is an incremental synergy term (the natural reading), then subtracting `hat V` in the surplus is not standard because `hat V` should also enter the bidder’s benefit and cancel out. If instead `bar S` is *total* post-merger value (unusual given prior notation), then the model needs a re-definition so `hat V` appearing in the threshold is coherent.

Issue B: Entry threshold depends on `hat V` (and Logistic CDF), which is a different mechanism than current code.
- `fix.md` makes `tilde p(X,D)` depend on `(hat V + bar m + K - (bar S + pi Delta_S))/s_xi`, and uses Logistic `Lambda`.
- Current `numerical/model.py` (as of 2026-03-03) uses Normal and makes bid probability depend only on `m_XD` (the expected premium wedge) and constants: threshold `T = (m_XD + K - S_bar)/sigma_xi`, then `p_bid = lambda_B * Pr(xi > T)`.

These are *not equivalent*. In the implemented direction, fundamentals `E[v|X,D]` do not affect bid probability directly; only the premium wedge does. In `fix.md`, fundamentals (through `hat V`) directly deter bids.

This matters because it changes the paper’s bid-incidence comparative statics:
- In the code-style entry rule: `dp/dpi < 0` comes from `m_XD` increasing in `pi`.
- In the `fix.md` rule: `dp/dpi < 0` also includes `tilde Delta` (via `hat V`) and includes `Delta_S` offsets, and depends on whether you want “sale facilitation” vs “deterrence” in the *entry rule*.

Recommendation (discussion-level):
- Decide which mechanism you want:
  - (A) “premium wedge drives entry” (matches current code and preserves the clean feed-forward pricing)
  - (B) “fundamentals deter entry through efficient pricing” (closer to classic takeover feedback stories, but requires coherent definitions so `hat V` belongs in bidder surplus).
- Only after that choice should the exact entry equation be finalized.

### Fix 1.3 + Fix 1.5/1.6 (Terminal payoff and feed-forward pricing)

Proposed in `fix.md`:
- Replace takeover payout from `P+m^R(a)` to `hat V + m^R(a)`.
- Derive feed-forward pricing `P^*(X,D) = delta( hat V(X,D) + p(X,D) bar m(X,D) )`.

Assessment:
- Algebraically correct if (i) bid probability does not depend on `P`, and (ii) takeover payout is not written as `P + ...` inside `Y`.
- This is consistent with the implemented direction in `numerical/model.py`, which uses a direct pricing formula of the same structure.

Practical caution:
- If you adopt this in the paper, you must consistently update interpretation language: `m0, m1` are no longer “premia above the market price P”; they become additive “deal wedge” terms in the takeover payout relative to standalone value.

### Fix 1.7 (Bid-incidence narrative)

`fix.md` ties `dp/dpi` to `tilde Delta + (tilde m-m0) - Delta_S` under Logistic entry.

Assessment:
- This is correct only for the specific entry threshold formula proposed in Fix 1.2.
- It does not match the implemented “bid prob depends only on m_XD” direction.

If you keep the code-style entry rule, the narrative should instead emphasize:
- higher inferred engagement increases expected premium wedge `m_XD`,
- this raises the bidder’s required payout and reduces bid incidence,
- no need to invoke `tilde Delta` in the entry threshold.

### Fix 1.8 / 1.9 / 1.10 / 1.11 (Existence/uniqueness and proof updates)

Assessment:
- Once pricing is feed-forward, the old A5 “bounded feedback” and the fixed-point uniqueness discussion should be removed/rewritten.
- Existence becomes mechanically easier: given cutoffs, beliefs and prices are computed in sequence.
- Uniqueness of the cutoff fixed point still generally needs either (i) a contraction-type condition or (ii) numerical verification.

Caution:
- Some proof patches in `fix.md` appear to assert conditional-independence statements too casually (e.g., “conditionally independent of the noise realization”), which should be checked carefully because `z` is part of `X` and conditioning matters.

### Priority 2 (Noise distribution fix)

Assessment:
- Strongly recommended if the goal is to avoid the `kappa -> 1` limit degenerating into disjoint support / perfect separation.
- Must be updated consistently across:
  - main-text definition of noise,
  - the `p0,p1` shorthand,
  - posterior formulas in the appendix,
  - limit arguments in any asymptotic/endpoint lemma.

Status:
- Draft has the old values in many places, including Appendix derivations.
- Code already uses the new values.

### Priority 3 (Logistic synergy distribution)

Assessment:
- Not necessary to achieve “feed-forward pricing”; it is an optional modeling choice.
- If adopted, it must be reflected consistently across:
  - entry rule equation,
  - any sufficient-condition bounds (old `phi(0)` stuff disappears anyway),
  - calibration table (replace `sigma_xi` with `s_xi`),
  - any numerical routines (code is currently Normal-based).

### Priority 4 (Quiet Accumulation domination lemma)

As written, this looks logically fragile.

Problem:
- The proof sketch assumes that under `D=1`, prices/bid probs are identical for `QA=(+1,0)` and `P=(+1,1)` because `D=1` is the same.
- But if `QA` is on-path with positive probability, then `D=1` does *not* necessarily imply `a=1`; beliefs and thus prices on `D=1` would change. Treating them as identical is close to circular.

Possible ways to make this rigorous (spec choice):
- Restrict the action space by assumption (treat `q=+1` as “public activism” which includes engagement).
- Or include `QA` explicitly and prove it is dominated under a parametric restriction that is stated as an assumption, and handle off-path beliefs carefully.

Given current numerical code excludes `QA` entirely, the simplest paper-consistent move is to state the action space as four actions and justify the restriction (rather than claiming general dominance without conditions).

## Suggested Next Decision (Discussion)

Pick one target spec for the paper so the “fix plan” becomes coherent:

Option A (Align paper to current implemented direction):
- Keep Normal synergy.
- Keep `p_bid(X,D) = lambda_B * Pr( xi > (m_XD + K - S_bar)/sigma_xi )`.
- Use feed-forward pricing and new noise probs.
- Drop A7 and rewrite bidder observation as `(X,D)`.
- Do not add `Delta_S` unless you also want to re-interpret entry surplus.

Option B (Adopt `fix.md` fully, including Logistic + `Delta_S`):
- Requires re-defining `bar S` / surplus carefully so the entry threshold’s `hat V` term is coherent.
- Requires updating numerical code to match the new entry rule.

This memo does not choose between A/B; it records the consistency issues so the next step can be an explicit design choice.

---

## Session Update: Production Pipeline Run & Visual Audit (2026-03-03 17:45+)

### Context
User updated all four Python files (`model.py`, `params.py`, `solver.py`, `export_data.py`) to implement **Option B** from fix.md: Logistic CDF via `expit()`, V̂-based bid threshold with Δ_S, S̄=1.44, s_ξ=0.15, λ_B=0.05. User requested: "revert to python drawing, review, run, draw, audit, deploy agents."

### What was done
1. **Pipeline run**: `python -m numerical.export_data` → 14 CSVs generated, no errors
2. **Python/matplotlib figure script**: Created `figures_matplotlib.py` replacing R/ggplot2 pipeline. All 13 figures render cleanly.
3. **Code audit agent**: Deployed background agent comparing every equation in `model.py` to `draft_v3.tex`. **Result: ALL PASS.** No equation mismatches found. Code matches paper exactly on all 16 parameters, all payoff branches, all posteriors, pricing formula, bid probability.
4. **Visual audit**: Inspected all 13 PDF figures.

### Key Findings

#### Code Correctness: PASS
All equations match draft_v3.tex. Agent verified: noise_probs, bid_probability (Logistic), compute_price_direct (feed-forward), all 4 payoff branches (EXIT/HOLD/QUIET/PUBLIC), posteriors, conditional means, minority gains decomposition, welfare, bidder surplus (Logistic softplus), all 16 params + 4 derived quantities vs Table C.3.

#### Economics: FAIL — Calibration Produces Degenerate Results

| Issue | Description | Root Cause |
|-------|-------------|-----------|
| No hump | Δ^min peaks at κ=0.15 (left boundary), not interior | λ_B=0.05 crushes takeover channel |
| Hold collapsed | k₀=k₁ everywhere, ω_H=0 | δΔ̃=0.214 > C(k₁)≈0.151 |
| Disclosure inert | Baseline vs no-disclosure identical in Fig 6 | k_D≈5.24 (>6σ), Public Voice ω_P≈0 |
| Tiny Δ^min | Range [0.0068, 0.0076], ~0.7% of μ | Weak takeover channel |

#### Root Cause Analysis
- **Hold collapse**: The standalone improvement benefit δ(1-p)Δ̃ ≈ 0.208 exceeds C₀=0.12 at ALL non-exit signals. Engagement always dominates holding.
- **No hump**: With p_bid ∈ [0.02, 0.05], the takeover channel (p_bid × premium) generates only ~0.001-0.003 variation — too small to create the hump.
- **kD extreme**: Public Voice requires buying a share at high price for only marginal benefit. The cost of disclosure far exceeds benefit at all realistic signals.

### Decision Point: Hold Region Collapse
User asked whether to (A) argue theoretically that Hold is dominated, or (B) state honestly that it collapses under baseline calibration. **Recommendation: Option B** — the collapse is parameter-dependent (sensitivity sweep shows Hold exists at C₀≥0.21), not structural. Add a Remark to Proposition 1 characterizing the collapse condition.

### Open Issues
1. **Recalibration needed** for hump shape and disclosure effect
2. Hold collapse defensible but other issues (no hump, inert disclosure) require parameter changes
3. Makefile not yet updated for Python-only figure pipeline

