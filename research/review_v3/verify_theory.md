# Verification — theory findings (framework_v3 review)

Adversarial pass. Verifier saw the claims only, not the referee's reasoning.
Repo state: branch `proposal`, 2026-08-19.

## Tally

15 claims checked. **CONFIRMED 14 · MISCITED 1 · WRONG 0 · UNCHECKED 0.**

The single MISCITED is C-T10 (a label on a d8 JSON field, not the substance).
Two claims (C-T6, O-1/O-2) were additionally refuted-attempts that failed:
independent execution reproduced the referee's numbers to 4 significant figures.

## Table

| id | claim (short) | verdict | evidence (file:line / executed output) | note |
|---|---|---|---|---|
| C-T1 | π(X,0) homogeneous deg-0 in (ω_E,ω_H,ω_Q); memo's one-line cross-partial is incomplete | CONFIRMED | `draft_v2.tex:450-456` "π(1,0) = ω_Q/(ω_H+ω_Q)", "π(−1,0) = ω_Q p₁/((ω_H+ω_Q)p₁+ω_E p₀)"; App. table `draft_v2.tex:2262-2270` (π(X,0) ∈ {0, Qp₁/T₋, Qp₀/T₀, Q/B}) | Every entry is a ratio of forms linear-homogeneous in (A,B,Q)=(ω_E, ω_H+ω_Q, ω_Q), so deg-0. Cell weights (pooled mass ÷ total D=0 mass) are likewise deg-0. Hence invariance to a common rescale, and **non**-invariance to a Q→P shift, which changes Q/B. Memo `framework_v3.qmd:168-175` writes \|∂Δ^act/∂κ\| = (m̃−m₀)(1−ω_P(τ))\|∂_κ E_{D=0}h(κ)\| and calls it "strictly decreasing in τ … one line". Incomplete: τ moves ω_Q at fixed ω_H+ω_E, so E_{D=0}h and its κ-derivative both carry a τ-dependence. A second term ∂_τ(∂_κ E_{D=0}h) is dropped, and its sign is unsigned. |
| C-T2a | existence relies on (A5)/(A5a) | CONFIRMED | `draft_v2.tex:617-619` "Under Assumptions (A1), (A2), (A4), an equilibrium in (weakly ordered) cutoff strategies exists"; but `draft_v2.tex:2015` "By Assumption (A5), this fixed point admits a unique solution" | T is cutoffs→prices→cutoffs; the inner price map must be single-valued for T to be a function at all. `draft_v2.tex:566` opens the section "Under Assumptions (A1)–(A5), any monotone-cutoff PBE must satisfy … the pricing fixed point". The memo's "unconditional under (A1),(A2),(A4)" (`framework_v3.qmd:137-138`) overstates. |
| C-T2b | internal contradiction l.696 vs l.1009 | CONFIRMED | `draft_v2.tex:1009` "The baseline parameters satisfy the sufficient condition for Assumption (A5): δ/σ_ξ = 0.95/0.40 = 2.375 < 1/φ(0) ≈ 2.507" vs `draft_v2.tex:696` "δ[p*+(ii)] ≈ 0.805+0.947>1, so the displayed feedback number does not by itself establish \|Ψ′\|<1 … which the baseline does not satisfy under this conservative sufficient rule" | They are two *different* conditions — and that is the problem. §5's rule is exactly term (ii) alone: δφ(0)/σ_ξ = 0.95×0.39894/0.40 = 0.9475, the same 0.9474 the appendix reports. §5 calls the partial rule "the sufficient condition for (A5)" while the appendix says the full rule fails. A reader cannot hold both sentences. |
| C-T3 | no GE attenuation theorem anywhere in repo | CONFIRMED | `draft_v2.tex:987` `\begin{proposition}[Disclosure Attenuation (Partial Equilibrium)]`; `draft_v2.tex:1788` "established a partial-equilibrium result … However, in general equilibrium"; `draft_v2.tex:1799` "the indirect (cutoff-shift) terms admit no general closed-form sign … stated as an exact decomposition with signed channels rather than a signed net effect" | `grep -rn "attenuat" quality_reports/` returns only prose in prompts/rewrites plus D7:260, which *cites* prop:disclosure-attenuation as a fixed-cutoff object. D8 (`d8_ge_dominance_check.json`) supplies `L_max_on_path = 0.8358` and `dk_dkappa_inf` — a bound on ‖dk/dκ‖ only. No dk/dτ and no d²k/dκdτ exist in the repo. The abstract (`draft_v2.tex:84`) nonetheless calls it "a disclosure-attenuation theorem". |
| C-T4 | λ_crit = 0.07 vs calibration λ = 0.8614; D7 targets AFS not Celentano–Levine | CONFIRMED | `d7_takeover_game_check.json`: `"lambda_crit_numeric": 0.07`; `"lambda": 0.8614452513529636` present in the same file; `D7_takeover_game_microfound.tex:273` "Activism then lowers measured bid premia exactly as in \citet{AlbuquerqueFosSchroth2022}"; §head `D7…tex:254` "Rationalizing the Albuquerque--Fos--Schroth sign" | Celentano–Levine appears exactly once in the repo, `draft_v2.tex:130` (lit review). Zero hits in `quality_reports/fixes/`. The reversal region λ<0.07 is ~12× below the calibrated λ. |
| C-T5 | D = 1{q=+1}, ω_P pinned by k_D; no τ in the model | CONFIRMED | `draft_v2.tex:401` "D = 1 if and only if q = +1 (Public Voice)"; `draft_v2.tex:424` "ω_P ≡ P(s ≥ k_D) = 1 − Φ(α_D)" | Added nuance: τ *is* a live symbol in draft_v2 — but as the discount horizon, `draft_v2.tex:335` "δ = exp(−rτ) … τ is the time between these dates", repeated at l.1870 and l.2893. Disclosure-strictness τ appears only in the discussion, l.1734 and l.1792, with no primitive definition. The memo (`framework_v3.qmd:120-124`) is candid that τ is new ("the key architectural change from draft_v2"), but defines it solely by the reduced-form ω_P′(τ)>0 — so the symbol clash with δ=exp(−rτ) is unresolved. |
| C-T6 | lem:dropA7 injectivity vs disclosed-branch price invariance | CONFIRMED | `draft_v2.tex:667` "the map (X,D) ↦ P is injective on the realized support at any nondegenerate calibration"; `draft_v2.tex:2016` "this fixed point admits a unique solution, so P*(x,1) is the same for all x ∈ {0,1,2}"; **executed**: P(0,1)=P(1,1)=P(2,1)=1.89921 at κ=0.2, 0.5, 0.8 | They conflict as written. The lemma's escape hatch — "On the measure-zero set where two cells share a price" (l.669) — is false here: the coincident set is the *entire* disclosed branch, probability ω_P>0. The lemma's *conclusion* nonetheless survives, since m̄(X,1)=m̃ and V̂(X,1) are constant on D=1 (l.2013-2015), so E[m^R\|P]=E[m^R\|X,D] holds by degeneracy rather than by injectivity. Fix is a premise swap, not a result loss. |
| C-T7 | Back et al.: window ↔ noise volume, not disclosure strictness | CONFIRMED | `tmp_extract/Back-ACTIVISMSTRATEGICTRADING-2018.txt:985-987` "what matters is [σ²T] — the cumulative amount of noise trading over the entire trading pe-riod. So from the perspective of a potential activist, reducing the trading horizon T is isomorphic to reducing noise trading volatility" | Direction as claimed: T maps into σ² (κ in the memo's notation), i.e. into the *inferred* branch's noise, not into ω_P. The memo half-concedes this at `framework_v3.qmd:126-127` ("the window length maps to inferred-branch noise through the Back et al. isomorphism") yet at l.121-124 has the same window move ω_P(τ). One instrument is being spent twice. |
| C-T8 | curvature condition cannot fail; orientation entirely GE; chord 16/20 | CONFIRMED | `draft_v2.tex:2803-2804` "The curvature condition cannot fail anywhere in {…} … Consequently the hump/trough orientation in the paper's calibration is produced entirely by the general-equilibrium cutoff-shift channel"; `draft_v2.tex:2829` "it matches the realized hump/trough orientation in 16/20 cells (against 8/20 for pointwise curvature) … a 16/20 correlation is a diagnostic, not a proof" | Both quotes exact. Note the 16/20 line sits in `rem:d5-conditional`, not `rem:d5-vacuous`; the referee's line ref (~2829) is right. Same remark also concedes "(GE-dom) is a stated, numerically maintained hypothesis, not a theorem". |
| C-T9 | Hold collapse is numerical, not a theorem | CONFIRMED | `draft_v2.tex:1009` "Under this parameterization, the Hold region collapses (k₀=k₁)"; `draft_v2.tex:418` "When engagement costs are constant (i.e., χ=0), the Hold region **may** collapse" | Also `draft_v2.tex:623` (proof of prop:existence) "The fixed point may lie on a collapse face … this is precisely the baseline (k₁=k₀, Hold collapses)". "May" throughout; nothing proves it must. The "may collapse" sentence is at l.418, in prose after prop:cutoffs, not inside the proposition — within the referee's "~l.410". |
| C-T10 | κ† = 0.5824 not 0.59; d8 channel-(A) peak 0.60 | **MISCITED** | **executed** on `numerical_output/data/baseline_series.csv`: argmax Δ_min at κ = 0.5823529412 (Δ_min = 0.0775535), runner-up 0.6029 (0.0775451); **executed** on `d8_ge_dominance_check.json`: argmax `chanA` is at **κ = 0.30** (chanA = 0.031268) — the grid's left edge, not 0.60 | Substance holds, the label does not. κ=0.60 is the argmax of **`Dmin`** on d8's coarser grid (Dmin = 0.0775502, step 0.025), and the `total_deriv` sign flip lands between 0.575 and 0.60. So the right statement is "d8's Δ_min peak is 0.60 on a 0.025 grid vs 0.5824 on the CSV's 0.0206 grid" — a grid-resolution spread, with the paper's "≈0.59" (`draft_v2.tex:2830`) sitting between two grid points that neither file reports. Do not call 0.60 a channel-(A) peak. |
| C-T11 | memo mislabels D7's φ, ψ, q | CONFIRMED | `D7…tex:70` "with q the equilibrium probability of a fringe raid, γ the portability … and ψ a pivotality factor"; `D7…tex:73` "reserve φ for the dilution parameter below"; `D7…tex:249` "From λ=1−q(1−γ)ψ with q=H(φ)" vs `framework_v3.qmd:113` "free-rider floor φ, entry probability q, and dilution ψ" | ψ is flatly wrong (pivotality, not dilution). φ is wrong as stated (D7 says dilution; the free-rider floor is the *derived* object y−φ, and D7 explicitly warns φ is not the normal density either). q ("entry probability" vs "fringe-raid probability") is loose but defensible — it is the probability a fringe raider enters. Two of three labels are wrong, and one of them (ψ) swaps a symbol the memo simultaneously assigns to φ. |
| C-T12 | δ: memo says 1, model uses 0.95 | CONFIRMED | `framework_v3.qmd:99` "δ a normalization (unit share mass, δ = 1 in the baseline)"; `draft_v2.tex:1009` "δ/σ_ξ = 0.95/0.40"; `draft_v2.tex:2893` "Discount factor & δ & 0.95"; `numerical/params.py:130` `delta: float = 0.95` | δ=1 does appear in draft_v2 but only as a *welfare accounting* device, `lem:transfer-netting`, `draft_v2.tex:1184-1190`: "Measure all t=1 and t=2 flows in common present-value units, i.e. set δ=1 … a units choice that affects no comparative static". The memo promotes a local welfare normalization to the baseline calibration. Not innocuous: the whole (A5) margin discussion is δ-scaled. |
| C-T13 | LMM JF 2024: Walrasian, no noise trader, no market maker | CONFIRMED | `research/txt/levit_malenko_maug_jf2024.txt:154` "a continuum of shareholders first trade their shares in a competitive market and then vote"; l.161 "the signal is public and there is no asymmetric information"; l.444-448 "buy any number of shares up to a fixed finite quantity x>0 … In equilibrium, the market must clear; we denote the market-clearing share price by p"; l.681-683 "the total demand for shares is D(p)=x Pr[b>b_a] … The market clears if and only if D(p)=S(p)" | **executed**: `grep -ic "noise trader"` → **0**; `grep -ic "market maker"` → **0**; `grep -i "order flow"` → no hits. Bounded trade size x is the friction; there is no order-flow inference object at all. |
| **O-1** | κ-sensitivity NOT lower under disclosure for ω_P ≲ 0.29 | CONFIRMED | **executed**, own script, 41-point grid κ∈[0.15,0.85] | Every number reproduced (table below). ω_P(baseline) = 0.03725. Ratios 1.0640 / 1.1837 / 1.1363 / 0.3780 against the claimed 1.06 / 1.19 / 1.14 / 0.38. Total-variation and mean-\|slope\| ratios agree to 4 dp (the grid is uniform, so they must). |
| **O-2** | disclosure jump increasing in κ, zero at X=2 | CONFIRMED | **executed**, own script | E[P(X,1)−P_ND(X) \| D=1] = 0.33130 / 0.39132 / 0.42070 at κ = 0.2 / 0.5 / 0.8, against the claimed ≈0.33 / 0.39 / 0.42. Jump at X=2 is 0.000000 to machine precision at all three κ (X=2 is off the D=0 support, so the pooled price coincides with the disclosed one). |

## Executed checks (key output)

Scripts: `…/scratchpad/o1.py`, `…/scratchpad/o2.py`, run with
`PYTHONPATH=/Users/austinli/Projects/blockholder .venv/bin/python`.
Both written from the claim text alone; neither reuses repo export code.

```
=== O-1: omega_P at baseline cutoffs (k1=k0=0.8217375899, kD=2.2611270960) ===
  (omega_E, omega_H, omega_Q, omega_P) = (0.40048, 0, 0.56227, 0.03725)

=== O-1: kappa-sensitivity, disclosure vs no-disclosure, kappa in [0.15,0.85], n=41 ===
    kD  omega_P    TV_disc  TV_nodisc  ratio_TV ratio_meanslope
 2.261   0.0373   0.017594   0.016537    1.0640          1.0640
 1.800   0.1289   0.015981   0.013500    1.1837          1.1837
 1.400   0.2858   0.012110   0.010658    1.1363          1.1363
 1.000   0.5000   0.003988   0.010550    0.3780          0.3780
   -> disclosure is MORE kappa-sensitive, not less, for omega_P <= 0.286.
      Attenuation appears only at kD=1.0 (omega_P = 0.50), far off calibration.

=== O-1b: exported numerical_output/data/disclosure_attenuation.csv, kappa in [0.15,0.85] ===
  n=35  range_disc=0.011070  range_nodisc=0.011170  ratio=0.9910
  max|A-B|/|B| = 0.0248     TV_disc=0.017587  TV_nodisc=0.016537  TV ratio=1.0635
   -> the two plotted curves differ by <=2.5% pointwise and 0.9% in range.
      The figure that is supposed to display attenuation displays coincidence.

=== C-T10: peak location ===
  baseline_series.csv  argmax Delta_min : kappa=0.5823529412  (0.0775535329)
                       runner-up        : kappa=0.6029411765  (0.0775451118)
  d8_ge_dominance_check.json  argmax Dmin  : kappa=0.60   (0.0775501970)
                              argmax chanA : kappa=0.30   (0.0312683712)  <-- grid edge
                              total_deriv sign flip between kappa 0.575 and 0.600

=== O-2: disclosed vs pooled-no-disclosure price at baseline cutoffs ===
 kappa   X    P(X,1)   P_ND(X)      jump
  0.20   0   1.89921   1.34205   0.55716
  0.20   1   1.89921   1.55473   0.34448
  0.20   2   1.89921   1.89921   0.00000     E[jump|D=1] = 0.33130
  0.50   0   1.89921   1.24821   0.65100
  0.50   1   1.89921   1.44206   0.45715
  0.50   2   1.89921   1.89921  -0.00000     E[jump|D=1] = 0.39132
  0.80   0   1.89921   1.09607   0.80314
  0.80   1   1.89921   1.40200   0.49721
  0.80   2   1.89921   1.89921   0.00000     E[jump|D=1] = 0.42070
   -> increasing in kappa, zero at X=2, as claimed.
   -> side effect: P(X,1) is IDENTICAL across X = 0,1,2 at every kappa,
      which is an executed refutation of lem:dropA7's injectivity premise (C-T6).
```

## Attempted refutations that failed

- **O-1** — tried to break it by suspecting the referee had used the exported CSV
  rather than the model. Rebuilt from `compute_minority_gains` /
  `compute_minority_gains_no_disclosure_given_strategy` on an independent grid.
  Same answer, and the CSV independently agrees.
- **C-T6** — tried to save `lem:dropA7` via its measure-zero caveat. The caveat
  does not apply: the disclosed branch has mass ω_P > 0 and all three of its cells
  share one price numerically (1.89921). The lemma's conclusion survives on other
  grounds; its stated premise does not.
- **C-T2b** — tried to read l.696 and l.1009 as two compatible conditions. They are
  two conditions, but l.1009's is term (ii) of l.696's, and δφ(0)/σ_ξ = 0.9475
  reproduces the appendix's own 0.9474. Calling the partial rule "the sufficient
  condition for (A5)" while the full rule fails is not reconcilable.
