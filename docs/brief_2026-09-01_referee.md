# Referee brief for the v5 paper (from the 2026-09-01 referee pass on the inherited draft)

This file is input for the rewrite, not a rulebook. Section numbers below refer to the inherited draft in `inherited/draft_v3/`. Read `.scratch/v5-paper/spec.md` for what the v5 paper is.

## 3. What a listener will carry out of the room, and what the main text currently leads with

**3.1 Lead with the partition and the factorisation.** The introduction's first substantive paragraph on results is existence, followed immediately by the two failed hypotheses and the four unresolved sweep nodes. A listener hears "the model may have no equilibrium" before hearing what the model says. Existence is standing ground, as §4 itself says. Give it one sentence in the introduction and one paragraph in the body, and lead with D1, L2 and T1(A), which are the paper's clean economics: liquidity acts on the premium only through the hidden cell, and the disclosure rule sets the weight on that cell. That is a memorable result and it is unconditional.

**3.2 The word "unconditionally."** The abstract says "a tighter threshold reduces that sensitivity unconditionally," and §1 and §7 repeat the claim. Inside the card's vocabulary this means "no dominance condition is needed because both ratios lie in [0,1]." To an outside reader it says Theorem 1(B) has no antecedent. It has fifteen, and the ones that carry the composition ratio are A(τ) at both policies plus the five bridge clauses, of which the paper itself says (br-iii) is "the clause with the least justification behind it." This is prose promoting a label, which the project's own rules forbid. Replace "unconditionally" with "without any dominance condition" in all three places, and say in the abstract that the threshold result is conditional on a support restriction the implemented calibration does not satisfy. The abstract currently says nothing about A(τ) at all, which the 08-30 review already flagged.

**3.3 The hypothesis lists belong in the appendix.** The main text prints (P-1) to (P-13) with a footnote, (T-1) to (T-15), and (C-1) to (C-7), plus a paragraph called "Two readings." No seminar listener, and few journal referees, will follow that. The card needs the lists; the paper needs one sentence per result naming the sufficient conditions in words, with a pointer. Sentences like "the sign-coherence hypothesis is confirmed unused" and "(T-15) threshold-side smoothness, which has been confirmed non-load-bearing" are audit trail, not exposition.

**3.4 The window margin has no economics in the body.** Theorem 1(C) says window tightening attenuates iff W_T·C_T ≤ 1 with C_T unsigned. The calibration says the product is 0.18 to 0.77 and the composition leg does almost all of it. Nowhere in the main text does the paper say in words who leaves the pooled cell when T shortens (the late crossers, whose order flow was the most revealing) and why removing them lowers the pool's sensitivity here, or what a case with C_T > 1 looks like. The appendix says "three reasons block a window analogue of that chain" and stops. A two-type worked example in which C_T exceeds one would make the "iff" the most quotable piece of theory in the paper, and it is the kind of thing a December audience will ask for. It is also cheap: the machinery is in `numerical_v4`.

**3.5 A(τ) is the largest conditionality in the stack, and it looks knife-edge.** A three-point posterior support {0, π̄/2, π̄} after H+1 days of ternary noise over a continuum signal is a very special structure. The appendix shows it holds in a one-round market with an all-or-nothing informative mark and fails for the implemented two-round menu at every node, with 23 to 767 support points. The paper calls the two-round case "open." My reading is that it is open in the sense that no one has proved it impossible, and that the presentation should not rest on it. Section 6 proposes a replacement route.

**3.6 Existence.** Two hypotheses of Proposition 1 fail at the calibration, the outer map is measured discontinuous, and four of 27 sweep nodes do not converge. The paper says so plainly. A journal referee will still ask why the paper computes at a calibration where its own existence result asserts nothing. The appendix names two repairs (a t-constrained Kakutani route and a cutoff-indexed concentration family) and executes neither. For December, one sentence and a pointer suffice. For the paper, one calibration or menu at which the antecedents of P1 and A(τ) both hold, even a toy one, would change the epistemic status of the whole stack from "proved on an empty set at the calibration shown" to "proved, and here is where it applies."

---

## 7. Minor items

- Figure 1 has no data between κ ≈ 0.45 and κ ≈ 0.72. Nothing in the caption or the text says why. Its title reads "Disclosure Attenuation of Liquidity Sensitivity" while the caption says the comparison refutes attenuation at that weight. Fix the title and explain or fill the gap.
- Table 1: rows 0.1 and 0.3 are identical to four digits because the τ ladder does not bite there. Say so in the caption or drop one row.
- Title: "A Theory of Exit, Voice, and Corporate Control" oversells. Exit and voice are a menu ordering in this model and there is no welfare section. Name the clock and the partition.
- The bibliography has no Mello and Repullo (2004), which the 08-19 framework report listed as must-engage for the non-monotonicity strand. I found no ruling that dropped it. If the hump result is gone for good, dropping it is defensible; say which.
- §2.1 says the 2024 acceleration is "a treatment rather than a formality." The paper then says, correctly, that it estimates no treatment effect. Pick a word that does not promise one.
- §3.1 introduces the run-up and the jump; §5.1 introduces them again. Once is enough.
- "Near-census" appears four times. It is a census of the two windows with 14 unresolved rows. Say census and give the 14.
- The "How the proof goes" paragraphs after Theorem 1 and Proposition 2 are good. The one after Proposition 1 is a page long and lists six disclaimers; cut it to the route and leave the disclaimers to the appendix.
- The conclusion's list of nine things the paper does not claim is honest and reads as a plea. Keep three (window sign, uniqueness, welfare) and move the rest to the appendix's non-claims.

---

## 8. A December structure

Six slides of content, in this order.

1. The clock partitions the market's information: flagged versus pooled, threshold versus window.
2. Liquidity acts only through the hidden cell: L2 and S = (1−Ω)·S_P. One picture.
3. The two margins differ: threshold shifts weight toward the insulated cell; the window also changes who stays hidden, and that can go either way. The two-type example.
4. At the implemented calibration the window cut attenuates and composition does the work. Table 1.
5. The clock moved: E1's CDF, with the corrected cut-off, plus the stake-at-filing and run-up/jump results if they land.
6. What is open: the support condition, existence at the calibration, endogenous timing.

Do not present the hypothesis lists. Do not present the four unresolved sweep nodes on a slide; answer the question if it is asked.

---

