# P2 — The rule is the partition: the 13D trigger-plus-deadline as the market's information structure

**Family:** information design × the partition itself (Proposer 2).

## 1. Object

The takeover premium—expected, and decomposed into pre-filing run-up and filing-day jump—with bidder entry as the mechanism through which the market's information cell moves it.

## 2. Margin

The **partition** itself: the on-path flagged/pooled split of what the price-setting market observes, keyed by the stake threshold (5%) *and* the legal date (filing deadline). The keys (τ, T) are LEVEL primitives in the theory; the Feb-2024 acceleration (10 → 5 business days) is the empirical CHANGE tightening the date key.

## 3. Anchor

Rule 13d-1(a) as amended (SEC Release 33-11253): crossing 5% starts a legal clock; the flag must arrive within five business days (`_institutional_sec_33_11253.md` §1, pp. 1, 10). Maug's only disclosure sentence splits publicity into pre-trade (kills liquidity) and post-trade ("do not affect F's trading strategy")—a 13D rule is **neither** (`maug_1998_jf.md` §6, Q5, p. 73). The pooled cell is measurably real: the run-up begins "precisely on the trigger date" (`zeng_2026_ras.md` §8, Q5, p. 1310).

## 4. Main result to be proved

**Statement.** In the cutoff equilibrium of a minimal Kyle-type model (blockholder with private signal, noise intensity κ, market maker, one bidder), the rule (τ, T) imposes a two-cell partition on the market's information at the control-decision node, present in every parameter configuration. The expected premium decomposes across the cells; the flagged cell is κ-invariant; the pooled cell carries the premium's entire κ-derivative; tightening either key shifts mass onto the flagged cell and attenuates the premium's liquidity-sensitivity.

**Tool:** information design—the rule as an exogenous, state-and-date-keyed partition of histories, bidder entry a functional of the partition—on the draft_v2 cutoff base rebuilt clean (ADR-0002).

**Proof route.** (i) A cutoff equilibrium with an interior crossing region exists (Brouwer; draft_v2 `prop:existence` machinery) ⇒ both cells on path under a stated interiority condition; (ii) flagged-cell posterior degenerate ⇒ flagged-cell price and bidder entry κ-invariant (draft_v2's disclosed-branch invariance, re-derived); (iii) E[premium] = ω·flagged + (1−ω)·pooled is an accounting identity; (iv) at fixed cutoffs the attenuation cross-partial signs in one line, the flagged component being κ-free (digest §6: "days, not weeks"); (v) GE response certified on a checkable region via D8-type bounds—no global sign claimed.

**Expected honesty label:** PROVED for (i)–(iv) at fixed cutoffs; region-certified PROVED in GE; NUMERICAL off-region.

**Biggest technical risk:** the interior-crossing condition—if the crossing region collapses at some κ (draft_v2's baseline collapses Hold), the partition is a property of the information structure, not of positive cell mass; the GE response can also flip the pooled cell's interior κ-sign (D8 counterexample logic).

## 5. Empirical design

**Sharp implication: a timing split**—low κ (illiquid) ⇒ informative pooled-cell order flow ⇒ larger run-up, smaller filing jump; high κ ⇒ the reverse; the Feb-2024 tightening compresses the pooled cell, so the run-up share falls post-2024 and its liquidity slope flattens.

- **Object / sample.** Run-up CAR[TD−1, FD−1] and filing CAR[FD−1, FD+1]; all SC 13D originals 2022–2025 with parsed event date + CUSIP (~2,849 pre / ~1,048 post; the ~1-day 2025 parser fix doubles the post leg—feasibility §1.2–1.3); Amihud six months pre-trigger (SEC convention) from on-disk CRSP 2021–25.
- **Identification.** `run-up CAR ~ Amihud × Post + log-cap + filer-type + year-quarter FE`, firm/month-clustered; same for filing CAR. No 13G control (selection on intent; map W2). Placebo: pseudo-triggers at TD − 63 trading days must show zero Amihud slope; 13Gs descriptive only (Zeng card R1).
- **Confounds (handled).** EDGAR cut-off (same-date); anticipation (pre-trigger CAR control); T+1 (dummy); 13G compliance 2024-09-30 and XML mandate 2024-12-18 (post window Feb–Dec 2024); Zeng's 1–13-day screen (business-day windows); BBJJ faster defences (p. 28) → premium-leg pill heterogeneity.
- **Power / MDE.** Window-CAR SD ≈ 10–15%; N ≈ 2,800 pre ⇒ MDE ≈ 0.8 pp slope, inside occupied magnitudes (CDF ~3%; Zeng 2.8%); post × Amihud (N ≈ 1,000–2,000) MDE ≈ 1.5–2 pp (feasibility §5.1). Nearest cut: Zeng's IA.2 size split—insignificant, opposite sign (card §7.2).
- **By December:** the split leg runs on data in hand (~1 week); **only specified:** the premium leg—≤300 hand-collected offer prices for 13D targets with a bid within 12 months, premium on Amihud × Post (ADR-0003 quantified leg).

## 6. What is new vs the competitor map

**Cell claimed: W3—rated "CLEAR (with a named boundary)"** (`competitor_map.md` Part 3 W3). Both boundary wordings respected verbatim: Kyle–Vila own the un-keyed pooled/revealed split—ours is "imposed by a legal trigger and a legal deadline, present in every parameter configuration"; Zeng owns the insider leak—our pooled state is "pooled for the price-setting market". **Extension: W11 ("NARROW—OCB own the architecture on the threshold")**—extension only, OCB Prop. 4 (p. 2847) cited as template; the map's own new clause: the window, unlike the level, lets the blockholder keep buying after crossing, so the three-party ordering over the deadline need not match the ordering over the threshold.

Nearest rows, none occupying W3: **CCKV**—one permanently pooled state ("No agent in the model ever learns that a blockholder holds a block", p. 11); **Corum–Levit**—flagged state off path on assumed belief μ(α) = 1 (p. 14); **OCB**—crossing reveals instantly, activist never crosses (p. 2836); **Corum**—purpose partition proved irrelevant (p. 19); **Back et al.**—window collapsed into σ²T, a rescaling not a partition (p. 1453); **CDF (2016)**—insider's presence common knowledge, named future work (p. 1464). Maug assumes disclosure away by timing (p. 73), Burkart–Lee hand the pre-/post-disclosure interaction to future work (p. 1891), and the author's proposal runs a window-CHANGE dose DiD with no partition object (map Part 1 row 11). **Standing risk:** Chabakauri et al. (2022), uncarded, named live W3 refuter (map sweep (d)); card it before draft_v3.

## 7. Deliverability by December

Core rebuild + partition theorem 3–4 weeks (reuses draft_v2's proved posteriors, decomposition, invariance, existence); fixed-cutoff attenuation days; GE region certification 1–2 weeks (D8 template); split empirics ~1 week on disk data; premium hand-collection 1–3 weeks; W11 extension 1 week, strictly last. **What could fail:** interior crossing at baseline (theorem carries the condition, grid-verified); GE sign off-region (ship fixed-cutoff + region-certified); premium slippage (December ships with the split leg plus the pre-specified premium spec). **Fallback:** representation + fixed-cutoff attenuation + split empirics is already a full draft.

## 8. Supervisor continuity

Recognizable from draft_v2: κ as the driving variable; the disclosed/non-disclosed branch structure, now derived from the rule's two keys rather than the ad-hoc D = 1{q = +1}; the bidder-entry channel; the D7 wedge (λ = 1 − q(1−γ)ψ) as the flagged-cell premium microfoundation; the honesty labels. **Dropped:** the four-action menu as identity (CONTEXT.md: machinery, not identity); the hump R1 headline—Maug Prop. 7 (p. 83), Edmans Prop. 3 (p. 2496), LMM Prop. 7 own liquidity humps (map Part 2 item 1)—surviving, if at all, as a *pooled-cell* property; the §7 welfare planner, reborn only as the W11 extension.

## 9. Self-assessed weakest point

The fixed-cutoff attenuation is nearly mechanical—the flagged cell is κ-invariant, so moving mass onto it attenuates; a referee may call the headline a decomposition, not a mechanism. The content must live in the pooled cell, where the GE cutoff response can flip signs (D8 counterexample), CCKV's Theorem 1 (p. 17) warns order-flow inference need not be monotone, and the empirical split prediction inherits the same assumption; the position is honest—region-certified, not global.
