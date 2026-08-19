# P1 — Window length and the takeover premium

## 1. Object
The takeover premium wedge \(m_1-m_0\) between engaged and unengaged targets as a function of how long the law lets a blockholder trade after crossing 5%.

## 2. Margin
The **window margin** (filing-window length \(T\)): a **LEVEL** in theory (\(\partial\,\text{premium}/\partial T\) signed), the Feb-2024 **CHANGE** (10 calendar days→5 business days) empirically.

## 3. Anchor
Rule 13d-1(a): filing due "within five business days" of crossing 5%, effective 2024-02-05 (`_institutional_sec_33_11253.md` §1). It binds: 20% of activist-type campaigns had not completed accumulating by the five-business-day deadline (SEC Table 3, p. 189).

## 4. Main result to be proved
**Statement.** With deadline length \(T\): the stake at the flag \(\alpha^\*(T,\kappa)\) is strictly increasing in \(T\) and noise intensity \(\kappa\); the wedge \(m_1-m_0=(1-\theta)\lambda(\alpha^\*)\rho\Delta_{\mathrm{eng}}\) is weakly increasing in \(T\), strictly and *discontinuously* where \(\alpha^\*\) crosses the pivotality boundary \(1-\tau_c\); and \(\partial^2(m_1-m_0)/\partial T\partial\kappa\ge0\): the window's premium effect is larger in liquid targets.

**Tool.** Tender-offer game theory: the D7 disagreement-node game fed by a pooled-state accumulation block.

**Proof route.** (i) Crossing starts the clock; a \(T\)-period linear-Gaussian Kyle problem gives a square-root law—\(\alpha^\*\)'s window-dependent component scales with \(\sqrt{\kappa T}\), \(\partial\alpha^\*/\partial T\) rising in \(\kappa\)—and post-flag buying at the flagged price is dominated. (ii) \(\lambda(\alpha)=1-q(1-\gamma)\psi(\alpha)\) is weakly increasing with an upward jump at \(1-\tau_c\), PROVED and check-verified (Prop. d7:lambda; `d7_takeover_game_check.py`); the jump survives composition since \(\alpha^\*\) is continuous in \(T\) while pivotality is a regime. The partition is load-bearing: the window bites only because the pooled state trades cheaply.

**Expected honesty label.** PROVED—on D7's stated primitives (equal-treatment offers, Grossman–Hart tie-breaking, exogenous \((\phi,\tau_c)\)) plus the linear-Gaussian Kyle class.

**Biggest technical risk.** The *measured* premium divides by a price already capitalizing the run-up (Prop. d7:afs): the theorem is stated over standalone value.

## 5. Empirical design
**Object and sample.** Offer-price premium (hand-collected from SC TO-T / DEFM14A / 8-K, ≤300 deals) over the unaffected price at −42 days, for 13D targets bid within 12 months (rate ≈ 18%: `greenwood_schor_2009_jfe.md`), in the parsed 13D universe 2022–2025 (9,234 filings; 2025 parser fix first) matched to the on-disk CRSP 2021–25 snapshot. **Tests.** (i) *Level (primary, pre-period):* premium on stake-at-filing relative to the blocking threshold (10% short-form blocking; pill triggers as alternative), standard controls. (ii) *Change (secondary):* premium pre/post 2024-02-05 interacted with pre-period Amihud liquidity: predicted post-rule decline, larger in liquid names. No control group exists (13G filers disclaim control intent; selection into 13D is window-responsive—W2): (ii) is a bounded, model-calibrated before/after, not a DiD. **Confounds:** EDGAR cut-off 5:30→10 p.m. same date; 13G compliance 2024-09-30 and the structured-data mandate cap the post window (Feb–Aug 2024); T+1 and universal-proxy dummies; BBJJ's defence-speed channel (opposite sign) via their low-trigger-pill split; Ben-David et al.—offer-price premia, never CARs. **Power/MDE.** ~300 bids, SD ≈ 25 pp: level test detects ≈ 0.7 pp premium per pp of stake; change-test MDE ≈ 7–8 pp, a bound (SEC Table 3 caps the constrained share at 3–20%). **Placebo:** bids preceding the 13D or >18 months out; premium re-based post-filing. **Run by December:** all of it.

## 6. What is new vs the competitor map
Claims **W1** ("window length as a determinant of the takeover premium, in theory—**CLEAR**"), with **W12** as mechanism ("premium wedge microfounded from the partition—CLEAR on mechanism"). Back et al. have the window but no premium, collapsing \(T\) into \(\sigma^2T\) (p. 1453); ours acts at the pivotality boundary, a discontinuity no variance-rescaling produces. Burkart & Lee's premium is degenerate (Lemma 2, p. 1877); they hand the pre-/post-disclosure interaction to future work (p. 1891, Q1); their IA Prop. 1 wedge runs through legal risk \(\varepsilon\)—"a wedge exists" is cited to them, ours comes from the partition (R21, §7). GMM own the endogenous stake path ending in a lumpy full acquisition (Prop. 7, p. 28); our contribution sits in the partition and the control outcome, never the stake path. Celentano–Levine own "activism→premium" (−13.69% marginal, −0.60% GE); we differentiate on the *rule*, never the sign. Not claimed: W8b (D7 entry is state-blind, \(q=H(\phi)\)); standing risk: BLV is cited from ECGI WP 956/2024, the Dec-2025 revision unobtained.

## 7. Deliverability by December
Theory: the D7 half is proved and verified; the accumulation block is new work (3–4 weeks). Numerics: the `params_with_endogenous_wedge` hook exists; add \(T\) as a primitive mapping to \(\alpha\) (1 week). Empirics: parser fix, first stage, hand-collection, regression (≈ 8–10 of ~19 weeks). Failure modes: accumulation monotonicity outside linear-Gaussian (fallback: NUMERICAL; the tender-game half stands); premium subsample <150 (fallback: level test plus calibrated bound).

## 8. Supervisor continuity
Recognisable from draft_v2: the wedge \((m_1-m_0)\), the D7 tender game (now fed by the window), \(\kappa\) as driver, the disclosure rule as partition. Dropped: the four-action menu (collapsed to the accumulation margin per CONTEXT.md), the hump R1 (Maug Prop. 7; Edmans Prop. 3; LMM Prop. 7 own it), R2 as headline (now the cross-partial corollary), welfare §7 and the D8 GE machinery.

## 9. Self-assessed weakest point
The strict part leans on the pivotality jump: at realistic 13D stakes (6–10%) pivotality requires reading \(\tau_c\) as a blocking/squeeze-out threshold, not majority control, and a referee can call the jump an artifact of the equal-treatment, one-shot-fringe primitives. Empirically the deadline is porous (SEC late rate ≈29% post Rule 0-3, p. 178 n. 695), the window binds for a small tail, and the change test has no control group—honest quantification, not a causal design. The paper stands or falls on not reading as Kyle–Vila plus Burkart–Lee stapled together.
