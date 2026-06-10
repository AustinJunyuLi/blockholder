---
date: 2026-06-10
type: research
status: DECISION-SUPPORT
branch: jmp-upgrade-2026-05
title: "Two-Path Feasibility — Harder Theory vs Structural Estimation (decision report)"
method: 4-agent draft read + deep-research workflow (wf_2d9b0371-986; ~74 agents, 63 claims → 3-vote adversarial verification, 63 survived / 0 killed). Synthesis written by hand from the verified-claim journal after the workflow's own synthesis step was lost to a session interrupt.
---

# Two-Path Feasibility — Decision Report

> Builds on the 2026-06-06/08 deep-research passes (direction-level verdict: convert the apparatus into a structural paper; D1 = estimate the two-channel price-impact decomposition) and resolves their open **gating scoop checks**. The headline news is in §1 — it changes the strategy.

---

## 1. Bottom line (read this first)

The gating scoop checks came back **occupied, and more crowded than the prior passes assumed.** Three live competitors now sit on the structural-activism direction, two of them squarely on the exact seam this paper was going to convert into:

1. **Celentano & Levine, "Shareholder Activism, Takeovers, and Managerial Discipline"** (SSRN / SFI RP 25-81, posted **Oct 2025**) — **structurally estimates an equilibrium model of activism + takeovers + managerial discipline.** It is **R&R at the *Review of Financial Studies*** (top-3 finance) per Levine's Jan-2026 CV, and a 2025 FMA Best-Paper-in-Corporate-Finance semifinalist. This is the single most dangerous competitor: same three nouns as this paper (activism, takeovers, governance), already structural, already at a top-3 journal.
2. **Johnson & Swem** (structural dynamic activism) — a dynamic reputation model (Kreps–Wilson / Milgrom–Roberts chain-store), and critically it **maps the Schedule 13D filing window to the noise-trading parameter via the exact σ²·T isomorphism** — i.e. "shortening the days between crossing the threshold and filing" *is* a change in cumulative noise trading. **That is precisely the 2024 SEC-acceleration anchor this project was eyeing.** Someone is already pulling that lever. (It does *not* structurally estimate trading/liquidity/price-impact/disclosure-timing — accumulation is collapsed to a reduced-form lognormal cost draw — so the *estimation* of those objects is still open, but the framing is taken.)
3. **Albuquerque, Fos & Schroth (JFE 2022)** — structurally estimate the **static binary 13D-vs-13G filing choice** by MLE on the joint distribution of filing choice + announcement returns. They claim first-mover status on structural estimation of activism *value creation* and explicitly differentiate from Gantchev (JFE 2013). Two facts that directly bear on this paper:
   - their cost of activism is a **single constant scalar** — **no engagement-cost *distribution* is estimated** (a gap this paper could fill);
   - their estimates imply activism **LOWERS** takeover bid premia by **13.7% (5.2pp)** vs a no-activist counterfactual — **the opposite sign of this model's assumed engaged-premium wedge `m1 > m0`.** This is an empirical threat to the paper's least-defensible assumption, not just a scoop.

**What survived as genuinely open:** the **Back–Collin-Dufresne–Fos–Li–Ljungqvist (Econometrica 2018) two-channel price-impact decomposition** (asymmetric-information vs governance/moral-hazard) has been **confirmed never structurally estimated** — BCDFLL is pure closed-form theory with no estimation/calibration; CDF (JF 2015) is reduced-form; AFS and Johnson–Swem both explicitly do *not* model trading/price-impact. So prior research's D1 seam is still vacant — but it is the *hardest* of all the options to execute and the competitors are converging on its neighbourhood.

**Recommendation (revised by this evidence): a hybrid, theory-led paper — NOT a pure structural pivot, and NOT a pure theory push.**
Lead with **one sharp new theorem that fixes the worst assumption** (microfound the premium wedge `m1>m0` from a takeover game, OR endogenize the disclosure rule), and attach a **disciplined calibration / limited structural leg** on the BCDFLL two-channel object using the 2024 13D XML — framed so AFS's negative-premium finding becomes a *quantity your model explains* rather than a contradiction. Rationale in §4. This dominates because (a) the pure-structural lane is now contested by an RFS-R&R paper and a σ²T-anchor paper, and (b) a pure junior-solo theory paper rarely clears top-3 finance (§3a).

---

## 2. Verified evidence map (what the scoop checks returned)

All claims below survived 3-vote adversarial verification (0 refutations).

**Structural-activism landscape (gating check 2a):**
- **Celentano–Levine** (SFI RP 25-81, Oct 2025): structural equilibrium model of activism/takeovers/managerial-discipline; **R&R at RFS**; FMA 2025 CF semifinalist. *(closest competitor)*
- **AFS (JFE 2022):** static binary 13D/13G choice, MLE on joint filing-choice + announcement-return distribution; cost = **constant scalar (no distribution)**; **activism lowers premia 13.7%/5.2pp**; does **not** estimate BCDFLL two-channel / no trading / stake exogenous; first-mover claim vs Gantchev. Headline decomposition: 6.34% avg 13D announcement return ≈ 75% treatment (4.77pp) + ~12% stock-picking + sample selection.
- **Johnson–Swem:** structural **dynamic reputation** activism model (chain-store lineage); **does not** structurally estimate trading/liquidity/price-impact/disclosure-timing (accumulation → reduced-form lognormal cost draw); **maps 13D window ↔ noise-trading via σ²T isomorphism** (the 2024-acceleration anchor). Fixes act/disclosure date T; endogenous T declared an open extension.
- **Gantchev (JFE 2013):** statistical, non-strategic sequential cost-stage model of a single campaign.
- **BCDFLL (Econometrica 2018, 86(4):1431–1463):** pure theory, closed-form for general (binary + continuous) activism tech; **no empirical/calibration/structural content** (confirmed in both the ECTA version and the 2016 NBER w22893 revision). Info-asymmetry channel = activist *intentions* (endogenous effort/moral hazard), giving the counter-Kyle result that **more noise trading can raise activism**.
- **CDF (JF 2015):** reduced-form (identifies informed trades from 13D Item 5(c)), not structural.

**Theory-bar / technique signals:**
- The **liquidity–efficiency sign is theoretically ambiguous** (depends on activism technology/parameters) — *theory alone cannot settle it*; identifying the technology/parameters is exactly what a structural leg buys. This is the strongest single argument that this paper's question is fundamentally an *identification* question, not a pure-theory one.
- **Maug (1998)'s** canonical result (noise trading raises activism iff initial stake below a threshold) is shown to hold **only in binary-activism models** and **fail for continuous activism technology** — directly relevant to this paper's binary-engagement defect: going continuous is not cosmetic, it can flip the comparative static.

---

## 3. Per-path verdicts

### PATH 1 — Harder theory push
**Feasibility:** moderate. The cleanest single upgrade is **microfounding the premium wedge** via a takeover game (Grossman–Hart free-rider / Bagnoli–Lipman tender / Burkart–Gromb–Panunzi) so `m1>m0` becomes a *theorem* with a sign that depends on transparent primitives — this also lets you engage AFS's negative-sign result head-on. Second cleanest: **endogenize the disclosure rule** (Verrecchia/Dye discretionary disclosure or a Kamenica–Gentzkow / Bergemann–Morris information-design reframing where the *regulator* designs the threshold). The continuous-time Kyle–Back embed ("Track B") remains the highest-ceiling but highest-risk option, and its documented gaps (Gaussian-filter vs discrete-target type mismatch; T→0 equilibrium-selection convergence; underived C†) are real; the Maug-fails-for-continuous result above is both an opportunity (novelty) and a warning (your discrete results may not survive the continuous limit).
- **Tools to learn:** monotone comparative statics / lattice (Milgrom–Shannon, Quah–Strulovici) to *sign the unproven GE channel* — this is the highest-value, lowest-cost upgrade and could convert the conditional hump into a theorem; optimal-stopping/free-boundary for disclosure timing (Track B only); concavification for the info-design route.
- **Placement ceiling (evidence-backed):** **3a — pure junior-solo theory clearing top-3 finance is rare.** The verified signal is that even the strong structural competitor (Celentano–Levine) is co-authored and is at RFS via *estimation*, and the liquidity-efficiency sign is explicitly "theory can't settle it." A pure-theory version realistically caps **top-10/15 finance**, not top-3/top-5-econ, for a solo junior. Best as the *core* of a hybrid, not the whole paper.
- **Scooping risk:** medium. The microfoundation and MCS upgrades are defensible and not obviously being done; the continuous-time disclosure-timing object is being approached (Johnson–Swem fix-T-then-endogenize).
- **9-month milestone:** a clean theorem microfounding the wedge + an MCS proof (or sharp counterexample) for the GE channel — i.e. kill the two worst "asserted" results. Genuinely deliverable in 9 months and independently presentable.

### PATH 2 — Structural estimation (pure pivot)
**Feasibility of the *clean* version: now low-to-medium, because the lane is contested.** The two most natural anchors are each partly taken: the 2024-acceleration / σ²T isomorphism (Johnson–Swem) and the 13D/13G structural choice (AFS). The one un-estimated structural object — the **BCDFLL two-channel decomposition** — is the hardest to identify (jointly separating an asymmetric-information channel from a governance/moral-hazard channel that move on distinct latent states) and sits next to where the competitors are converging.
- **Altered model / what it identifies that reduced-form can't:** the **engagement-cost *distribution*** (AFS only get a scalar — this is the cleanest white space), the disclosure-cost/timing parameter, and counterfactual threshold/deadline policy experiments (welfare of the 2024 acceleration). NNE (Wei–Jiang 2025) or SMM/indirect inference fit a model that is easy to simulate but hard to estimate classically.
- **Data:** the parsed 2024 13D/G structured XML (free, mandatory Dec 2024) + WRDS (CRSP/Compustat/daily-TAQ Amihud) + Bloomberg for M&A deal/premia and ownership history is sufficient for the *descriptive + reduced-form* leg; the structural leg is credible only on the cost-distribution object, not the full two-channel object, within 9 months. *(Bloomberg-specific function detail was not reached before the synthesis step was lost — flag as an open item to confirm: 13D/G filing history, holdings/ownership history, MA<GO> deal database, corporate actions, tick-history export caps.)*
- **Placement ceiling:** the pure structural pivot now realistically caps **top-15 finance** *unless* it estimates the un-touched two-channel object — and that is a 2–3-year, high-execution-risk bet with live neighbours.
- **Scooping risk:** **HIGH** (this is the decisive change vs prior passes). Celentano–Levine at RFS; Johnson–Swem on the anchor; AFS on the static choice.
- **9-month milestone:** parsed 13D XML descriptives + one clean reduced-form fact on the 2024 acceleration + an NNE prototype validated on model-simulated data. Feasible, but risks being a worse-positioned version of Johnson–Swem.

### HYBRID (recommended)
Theory core (microfound the wedge **or** endogenize disclosure; sign the GE channel via MCS) **+** a disciplined calibration / partial structural leg (engagement-cost distribution on the 2024 13D XML), framed so AFS's negative-premium estimate is an *equilibrium quantity your model rationalizes*. This is the dominant strategy because it (a) sidesteps the now-crowded pure-structural lane, (b) clears the "pure theory doesn't place top-3 solo" bar, and (c) turns the two biggest threats (AFS's sign; Johnson–Swem's anchor) into engagement points rather than scoops.

---

## 4. Recommendation & phased plan

**Pick the HYBRID, theory-led.** Within it, the **first 9 months are pure theory** (no data-access dependency, fully in the author's comparative advantage, independently presentable at the March-2027 milestone), with the structural leg de-risked in parallel.

- **0–9 months (milestone deliverable):**
  1. Theorem A: microfound `m1>m0` from a takeover game → engage AFS's negative-sign result directly.
  2. Theorem B: sign the GE cutoff-shift channel via monotone comparative statics (or a clean counterexample) → upgrade the conditional hump.
  3. De-risk: parse the 2024 13D/G XML; one descriptive + one reduced-form event-study fact; **confirm the Celentano–Levine and Johnson–Swem scope in full** (read both papers) before committing the structural leg.
  *Milestone talk = "two new theorems + a data fact + a sharp positioning vs three named competitors."*
- **9–24 months:** build the estimable model around the **engagement-cost distribution** (the AFS white space) on 13D XML; NNE/SMM prototype → real estimates; counterfactual on the 2024 deadline acceleration.
- **24–36 months:** decide whether to reach for the **BCDFLL two-channel** estimation (the high-ceiling, still-open object) as a second paper or a final section, contingent on whether the competitors have taken it.

**Risk register:** scooping is now the binding risk (Fos is a coauthor on both BCDFLL *and* AFS — he sits on both the theory and the structural side of this exact space; Levine/Celentano at RFS). Execution risk concentrated in the two-channel object. Data-access risk low for the cost-distribution leg. The 9-month theory-first plan is robust to all three because it ships value with zero data dependency.

---

## 5. Honest gaps in this report
- The workflow's own synthesis step was lost to a session interrupt; this was hand-synthesized from the 63 verified-claim journal. Claims are verified; the *narrative weighting* is mine.
- **Bloomberg-specific function inventory (2d) was not reached** — confirm before relying on it.
- Path-1 "pure theory caps top-10/15 finance" rests on the *absence* of verified junior-solo top-3 pure-theory exemplars in this search, plus the liquidity-sign-ambiguity claim — it is an inference, not a directly verified placement statistic.
- "BCDFLL two-channel never structurally estimated" is verified as of this search but is exactly the kind of claim a 2026 JMP could already be invalidating; re-check before betting the 2–3-year arc on it.
