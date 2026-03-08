# Presentation Preparation Documents — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Produce two presentation preparation documents for a career-important 20-25 min finance faculty seminar on Monday.

**Architecture:** Two independent documents produced in parallel by agent team. Document 1 (lecture notes) requires deep reading of draft_v3.tex for full derivations. Document 2 (presenter's companion) requires reading presentation.tex, slides.bib, and diagnosis/ for Q&A prep.

**Tech Stack:** Markdown documents with LaTeX math notation.

---

## Task 1: Comprehensive Lecture Notes

**Files:**
- Create: `pres/lecture_notes.md`
- Read: `draft_v3.tex` (full manuscript, 1462 lines — primary source for all derivations)
- Read: `pres/presentation.tex` (slide structure to align notes with talk flow)
- Read: `numerical/model.py` (core economic functions)
- Read: `numerical/params.py` (baseline calibration values)
- Read: `numerical/solver.py` (equilibrium solver details)
- Read: `diagnosis/gptpro/2026-03-04/round_2_reply.md` (known theory gaps)
- Read: `diagnosis/fix4.md` (Gemini fix proposals)

**Step 1: Read all source material**

Read draft_v3.tex completely. Read presentation.tex for slide ordering. Read model.py, params.py, solver.py for numerical details. Read diagnosis files for known weak spots.

**Step 2: Write lecture notes**

Write `pres/lecture_notes.md` with these sections (each section should be thorough with full math):

### Section structure:

1. **Model Primitives & Assumptions**
   - State space: v ~ N(mu, sigma_v^2), signal s = v + epsilon
   - All 7 assumptions A1-A7 with economic motivation for each
   - Feasible action set {(-1,0), (0,0), (0,1), (+1,1)} with economic meaning
   - Noise trading distribution: z in {-1,0,+1} with probabilities
   - Disclosure rule: D = 1{q=+1} and its institutional basis (Schedule 13D)

2. **Timeline & Information Structure**
   - All 5 stages (t=0, 1, 1.2, 1.5, 2) with full description
   - Who knows what at each stage
   - The two-stage inference problem: anonymous execution -> disclosure
   - Why this creates strategic value for the blockholder

3. **Equilibrium Theory (Propositions 1 & 4)**
   - Prop 1: Monotone cutoff structure — full proof sketch
     - Payoffs affine in v-hat(s), single-crossing argument
     - Why k1 <= k0 <= kD must hold
     - Lemma 1 (QA domination): why quiet accumulation is dominated
     - The Lemma 1 gap (D5): what's the issue, what's the fix (GPT Pro Patch 1)
   - Prop 4: Existence via Brouwer fixed point
     - Compact domain Theta, continuous best-response map T
     - Numerical uniqueness (A6): multi-start verification, not analytic proof

4. **Bayesian Inference (Proposition 2)**
   - Full posterior derivations for all (X,D) pairs
   - Disclosed branch: D=1 => pi(X,1) = 1 for all X (trivial)
   - Nondisclosed branch: Bayes rule step by step
     - pi(1,0) = omega_Q / (omega_H + omega_Q) — kappa-invariant
     - pi(-1,0): full formula with noise probabilities
     - pi(0,0): full formula
     - pi(-2,0) = 0 (impossible under D=0)
   - Within-regime comparative statics: d_kappa pi(1,0) = 0, d_kappa pi(-1,0) >= 0, d_kappa pi(0,0) <= 0
   - Conditional means via inverse Mills ratios (Lemma 3)

5. **Pricing (Proposition 3)**
   - Feed-forward structure: cutoffs -> signals -> beliefs -> prices (no fixed point!)
   - Engagement cost: C(s) = C0 * exp(-chi * (s-mu)/sigma_s)
   - Engagement technology: rho parameter, tilde-Delta, tilde-m
   - Standalone value: V-hat(X,D) = E[v|X,D] + tilde-Delta * pi(X,D)
   - Bid probability: p(X,D) = lambda_B * (1 - Lambda(Gamma)), derive Gamma
   - Post-disclosure price: P_post(X,D) = delta * (V-hat + p * m-bar)
   - Execution price: P_trade(X) = E[P_post | X] (averaging over D)
   - Three price channels: fundamentals + standalone + takeover
   - Why D=1 prices are flat in X (complete derivation)
   - Net deterrence (A5): why d_pi(p) < 0

6. **Main Results (Proposition 5)**
   - Minority takeover gains: Delta^min(kappa) = E[m^R(a) * 1{bid}]
   - Hump shape: why nonmonotone?
     - Channel 1: kappa up -> more camouflage -> lower adverse selection -> more bids (extensive margin)
     - Channel 2: kappa up -> weaker inference -> activism premium erodes (intensive margin)
   - Decomposition: Delta^min = Delta^base + Delta^act
     - Delta^base(kappa) = m_0 * P(bid) — extensive margin, monotone increasing
     - Delta^act(kappa) = (tilde-m - m_0) * E[pi * 1{bid}] — intensive margin, monotone decreasing
   - Full derivation of decomposition from m^R(a) = m_0 + (tilde-m - m_0) * a
   - Endpoint behavior (Lemma 2):
     - kappa -> 0: perfect inference, X = q a.s.
     - kappa -> 1: uniform noise, but engagement survives in Public Voice
     - Key numerical facts: omega_Q -> 0 at kappa=0.99, but omega_P = 0.362
   - Interior peak: Weierstrass + endpoint separation -> max is interior
     - Caveat: single-peakedness is numerical, not analytic

7. **Disclosure & Policy (Propositions 6 & 7)**
   - Prop 6 (PE, Disclosure Attenuation):
     - Hold cutoffs fixed, vary kappa through inference only
     - Only nondisclosed component depends on kappa
     - Shifting mass to disclosed attenuates |d Delta^act / d kappa|
     - Three regimes: baseline, full disclosure, no disclosure
   - Prop 7 (GE, Disclosure Trade-off):
     - Transparency (+): D=1 removes inference discount, pi=1, full capitalization
     - Deterrence (-): stricter thresholds force early disclosure, maximizes bid deterrence
     - Heuristic decomposition: d Delta^act / d tau ≈ partial(transparency) + partial(deterrence)
     - Net effect depends on primitives
   - Noisy rumors extension: auxiliary signal flattens kappa-sensitivity

8. **Welfare**
   - Delta^min as welfare metric: Grossman-Hart free-rider justification
   - Total surplus W_tot includes bidder surplus (transfers cancel)
   - Key tension: Delta^min can peak at kappa-dagger while W_tot keeps increasing
   - Policy implication: maximizing minority gains != maximizing efficiency

9. **Calibration & Numerical Details**
   - All 16 baseline parameters with economic justification
   - Net deterrence check: tilde-Delta + (tilde-m - m_0) - Delta_S = 0.24 > 0
   - Solver: damped fixed-point iteration + brentq, multi-start with collapsed-hold fallback
   - Convergence tolerance: 1e-6, residual quality gate: 5e-3
   - Key numerical landmarks:
     - kappa-dagger ≈ 0.24 (hump peak)
     - Quiet Voice collapse at kappa ≈ 0.63
     - Delta^act -> 0.00020 (not zero!) at kappa = 0.99

10. **Known Weak Spots & Theory Repair Status**
    - D5 (Lemma 1): "a fortiori" gap, belief-free lower-bound fix available
    - D1 (Lemma 2): omega_Q -> 0 claim is unproved GE result
    - D2 (Prop 5): monotonicities are numerical, not analytic
    - A6 (uniqueness): numerical verification only
    - Status of all fixes: D3, D4, D6 resolved; D1, D2 partially resolved; D5 new fix available

**Step 3: Verify completeness**

Check that every proposition (1-7), every lemma (1-3), every assumption (A1-A7), and every figure referenced in the slides has a corresponding detailed treatment in the notes.

---

## Task 2: Presenter's Companion

**Files:**
- Create: `pres/presenter_companion.md`
- Read: `pres/presentation.tex` (slide structure, timing)
- Read: `pres/slides.bib` (all 25 bibliography entries)
- Read: `draft_v3.tex` (for equation verification)
- Read: `diagnosis/gptpro/2026-03-04/round_2_reply.md` (known gaps for danger zones)
- Read: `diagnosis/gptpro/2026-03-04/round_2_meeting_notes.md` (audit consensus)

**Step 1: Read all source material**

Read presentation.tex, slides.bib, relevant sections of draft_v3.tex, and all diagnosis files.

**Step 2: Write presenter's companion**

Write `pres/presenter_companion.md` with these sections:

### Section 1: Talk Map (1 page)

For each of the 16 main slides:
- Slide number and title
- Time target (cumulative, e.g., "by 3:00")
- One-line key message to deliver
- Transition phrase to next slide
- Mark which slides are "speedable" if running long

Target pacing for 20 minutes:
- Act I (Slides 1-4, Motivation): ~4 min
- Act II (Slides 5-10, Theory): ~8 min
- Act III (Slides 11-14, Results): ~5 min
- Act IV (Slides 15-16, Policy): ~3 min

### Section 2: Key Objects Cheat Sheet (0.5 page)

The 10 most important expressions, written large and clear:
1. Action set: {(-1,0), (0,0), (0,1), (+1,1)}
2. Order flow: X = q + z
3. Disclosure: D = 1{q=+1}
4. Cutoffs: k1 <= k0 <= kD
5. Posteriors: pi(X,D) key formulas
6. Post-disclosure price: P_post(X,D) = delta(V-hat + p * m-bar)
7. Delta^min = E[m^R(a) * 1{bid}]
8. Decomposition: Delta^min = Delta^base + Delta^act
9. Delta^base = m_0 * P(bid), Delta^act = (tilde-m - m_0) * E[pi * 1{bid}]
10. GE heuristic: d Delta^act / d tau ≈ transparency(+) + deterrence(-)

### Section 3: Interrupt Recovery Guide (0.5 page)

For each act of the talk:
- **If interrupted during Motivation (slides 1-4):** "Great question — let me show you exactly how the model captures that. [advance to relevant theory slide]"
- **If interrupted during Theory (slides 5-10):** "The math is in the backup — let me note your question and come back to it. The punchline is..." [state result, continue]
- **If interrupted during Results (slides 11-14):** Engage — this is the meat, answer inline
- **If interrupted during Policy (slides 15-16):** "That connects to the GE trade-off — [slide B15]"
- **General recovery phrase:** "Let me bookmark that and make sure I get to it — the next slide actually speaks to this."

### Section 4: Anticipated Q&A (1.5 pages)

Organize by category:

**Likely inline interruptions (during talk):**
1. "Why discrete trade sizes?" — Tractability; continuous Kyle model doesn't yield closed-form posteriors with disclosure
2. "Why not continuous noise?" — Same; bounded noise gives exact Bayesian updating
3. "Is the hump robust?" — Yes, show sensitivity panels (B9, B10)
4. "What about multiple blockholders?" — Extension noted in summary; Edmans-Manso (2011) is closest
5. "How do you get uniqueness?" — Numerical, not analytic (A6); multi-start solver converges to same fixed point
6. "Why is kappa the right measure of liquidity?" — Maps directly to noise trading intensity; higher kappa = more noise = more camouflage

**Likely end-of-talk questions:**
7. "What's the empirical prediction?" — Four testable predictions on slide 15; most distinctive is the hump test
8. "How does this differ from Edmans (2009)?" — Edmans has exit threat only, no voice; we unify exit+voice+takeover
9. "How does this differ from Maug (1998)?" — Maug has voice but no order-flow inference; we add microstructure
10. "What about the free-rider problem?" — Grossman-Hart (1980); our Delta^min is exactly the minority premium
11. "Is disclosure endogenous?" — No, it's a regulatory parameter tau; endogenizing it is future work
12. "What's the welfare implication?" — Slide B18; minority gains and total surplus can diverge
13. "How sensitive is kappa-dagger to calibration?" — Shifts but hump persists; see sensitivity panels
14. "Can you connect to 13D event studies?" — Prediction 4: filing CARs should be larger for high-liquidity stocks
15. "What about short-selling constraints?" — Not modeled; would remove Exit action, compressing to 3 actions

**Hardball questions (for a tough audience):**
16. "Isn't uniqueness just assumed?" — "Yes, A6 is a maintained assumption verified numerically. We haven't found a counterexample. The multi-start solver with 50+ initial points always converges to the same cutoffs."
17. "Your hump is numerical, not analytic — how is this a theorem?" — "We prove existence of an interior peak analytically (Weierstrass + endpoint separation). The decomposition is analytic. The single-peakedness is a numerical finding we label honestly."
18. "The Lemma 1 proof has a gap" — "You're right — the original proof compared prices across regimes. We have a fix using a belief-free lower bound that avoids that comparison entirely. Happy to discuss offline."

### Section 5: Literature Synopses (1 page)

**Cited papers (10):**

1. **Brav, Jiang, Partnoy, Thomas (2008)** — "Hedge Fund Activism, Corporate Governance, and Firm Performance," JF. Empirical study of 1,059 hedge fund activist events (2001-2006). Find activists earn 7% abnormal returns, with gains concentrated in events leading to M&A. *Your paper's connection:* Motivates the takeover channel — activism and corporate control are linked empirically.

2. **Greenwood & Schor (2009)** — "Investor Activism and Takeovers," JFE. Show that a large fraction of activist returns come from takeover outcomes specifically, not from operational improvements. Activists serve as catalysts for M&A. *Connection:* Supports the claim that minority takeover gains are the right welfare object.

3. **Back, Collin-Dufresne, Fos, Li, Ljungqvist (2018)** — "Activism, Strategic Trading, and Liquidity," Econometrica. Model strategic activist who trades before intervention. Activist exploits private information about future engagement. Empirically, pre-filing trading patterns confirm informational advantage. *Connection:* Motivates the order-flow inference mechanism — markets try to learn from activist trading.

4. **Maug (1998)** — "Large Shareholders as Monitors: Is There a Trade-Off Between Liquidity and Control?" JF. Classic liquidity-governance paper. More liquid markets make it easier for blockholders to acquire stakes, but also easier to exit rather than monitor. Finds liquidity can be net positive for governance. *Connection:* Your paper adds order-flow inference and takeover feedback to Maug's framework.

5. **Edmans (2009)** — "Blockholder Trading, Market Efficiency, and Managerial Myopia," JF. Blockholder disciplines management through exit threat: selling on bad news depresses stock price, which managers care about. No voice/engagement — governance is purely through trading. *Connection:* Your paper extends from exit-only to exit+voice, showing the interaction matters.

6. **Edmans & Manso (2011)** — "Governance Through Trading and Intervention: A Theory of Multiple Blockholders," RFS. Multiple blockholders can coordinate on trading (exit threat) or intervention (voice). Shows complementarity between blockholders. *Connection:* Your paper focuses on single blockholder but unifies the exit/voice choice with takeover outcomes.

7. **Kyle (1985)** — "Continuous Auctions and Insider Trading," Econometrica. Foundational microstructure model. Informed trader submits orders that are camouflaged by noise trading. Market maker sets prices based on order flow. *Connection:* Your model's order-flow inference mechanism is a discrete-action analog of Kyle's framework.

8. **Glosten & Milgrom (1985)** — "Bid, Ask and Transaction Prices," JFE. Adverse selection model: market maker faces informed and uninformed traders. Spread reflects information asymmetry. *Connection:* Your market maker's pricing problem is Glosten-Milgrom style — competitive, zero-profit, Bayesian updating from order flow.

9. **Edmans, Goldstein, Jiang (2012)** — "The Real Effects of Financial Markets: The Impact of Prices on Takeovers," JF. Prices aggregate information and feed back to real decisions (takeover entry). Bidder learns from stock price whether target is worth acquiring. *Connection:* Your bidder conditions on (X,D) — direct feedback channel from market to takeover decision.

10. **Bond, Edmans, Goldstein (2012)** — "The Real Effects of Financial Markets," Annual Review. Survey of price-to-fundamentals feedback literature. Prices guide investment, takeover, and governance decisions. *Connection:* Your model is a specific instance of this feedback paradigm.

11. **Grossman & Hart (1980)** — "Takeover Bids, the Free-Rider Problem, and the Theory of the Corporation," Bell JE. Small shareholders free-ride on bidder's improvements, demanding full value in tender offer. *Connection:* Justifies Delta^min as welfare metric — minority shareholders capture value through takeover premia.

**Important uncited papers (know these for Q&A):**

12. **Hirschman (1970)** — Exit, Voice, and Loyalty. The original framework: dissatisfied members of an organization can exit (leave) or voice (complain/engage). Your paper is a formal game-theoretic version applied to financial markets.

13. **Coffee (1991)** — "Liquidity Versus Control," Columbia Law Review. Legal perspective on the trade-off: liquid markets let institutional investors sell easily (exit) but weaken incentives to monitor (voice). Your model formalizes this legal intuition.

14. **Bhide (1993)** — "Hidden Costs of Stock Market Liquidity," JFE. Argues liquid markets have hidden costs: they enable free-riding and reduce monitoring incentives. Your hump-shaped result partially validates this — too much liquidity can hurt.

15. **Brav, Dasgupta, Mathews (2022)** — "Wolf Pack Activism," Management Science. Multiple activists coordinate implicitly through trading. Relates to your single-blockholder setting — extending to wolf packs is natural future work.

### Section 6: Danger Zones (0.5 page)

**Do NOT say:**
- "We prove uniqueness" — you don't. Say "we verify uniqueness numerically"
- "The hump is always single-peaked" — it's single-peaked in baseline. Say "in all calibrations we examine"
- "Voice vanishes at high kappa" — it doesn't. Quiet Voice collapses but Public Voice survives
- "omega_Q goes to zero" — this is an unproved GE claim. Say "Quiet Voice probability becomes negligible"

**Known weaknesses and deflections:**
- **Lemma 1 gap:** "We have a strengthened proof using a belief-free lower bound. Happy to discuss the details offline."
- **Numerical uniqueness:** "A6 is maintained and verified computationally. We're transparent about this."
- **Discrete trade sizes:** "This is a tractability choice. The qualitative forces — camouflage vs inference erosion — would survive in a continuous model."
- **No dynamics:** "This is a one-shot model. Adding dynamics is important future work but the cross-sectional predictions are already testable."
- **Single blockholder:** "Extending to multiple blockholders would combine our framework with Edmans & Manso (2011). The single-blockholder case isolates the core mechanism."

**Step 3: Verify completeness**

Ensure every backup slide is referenced in the Q&A section. Ensure all 10 cited papers + 5 key uncited papers have synopses. Ensure timing adds to 20 minutes.

---

## Execution Strategy

These two tasks are **fully independent** — execute as parallel agents:
- Agent 1: Task 1 (lecture notes) — needs deep reading of draft_v3.tex
- Agent 2: Task 2 (presenter's companion) — needs presentation.tex + slides.bib + diagnosis/

Both agents write to `pres/` directory.
