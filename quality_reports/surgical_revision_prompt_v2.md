# Surgical Revision of "Liquidity, Activism Disclosure, and Takeover Premia"

**I have attached the full PDF of the paper. Read it carefully before producing any output.**

You are a financial economics theorist. Your task is to produce **exact, implementable revisions** to the attached paper by Austin Li that would bring it to the standard of a top-3 finance journal (JF, RFS, or JFE). Read the full paper first, then produce each deliverable below in order.

**Paper structure (for navigation):**
- Section 1: Introduction (pp. 2--3)
- Section 2: Related Literature (pp. 3--4), subsections 2.1--2.4
- Section 3: Model (pp. 4--9), subsections 3.1--3.9
- Section 4: Equilibrium Characterization (pp. 9--15), subsections 4.1--4.8
- Section 5: Numerical Illustration (pp. 15--16), subsections 5.1--5.3
- Section 6: Comparative Statics (pp. 16--18), subsections 6.1--6.3
- Section 7: Extensions (pp. 18--20), subsections 7.1--7.3
- Section 8: Conclusion (pp. 20--21)
- Appendix A: Proofs and Derivations (pp. 22--30)
- Appendix B: Tables (pp. 30--32)
- Appendix C: Figures (pp. 33--36)
- Appendix D: Notation (pp. 37--38)

Assumptions (A1)--(A7) are the "Standing Assumptions" introduced across footnotes and inline text in Sections 3--4. Assumption (A6) (contraction) and (A8) (boundary conditions for nonmonotonicity) are introduced in footnote 5 (p. 9) and Section 4.7 respectively.

---

## A. PAPER SUMMARY (for quick reference; the attached PDF is authoritative)

### A.1 Setup
A blockholder observes private signal $s = v + \varepsilon$ about firm fundamental $v \sim \mathcal{N}(\mu, \sigma_v^2)$, with $\varepsilon \sim \mathcal{N}(0, \sigma_\varepsilon^2)$. Posterior mean: $\hat{v}(s) = \mu + \beta(s - \mu)$, $\beta = \sigma_v^2/(\sigma_v^2 + \sigma_\varepsilon^2)$.

She chooses $(q, a) \in \{(-1,0), (0,0), (0,1), (+1,1)\}$ corresponding to Exit, Hold, Quiet Voice, Public Voice. Disclosure $D = \mathbf{1}\{q = +1\}$. Noise trader: $z \in \{-1,0,+1\}$ with $\Pr(z=0) = 1-\kappa$, $\Pr(z=\pm 1) = \kappa/2$. Order flow: $X = q + z$.

Engagement cost: $C(s) = C_0 \exp(-\chi(s-\mu)/\sigma_s)$. Success probability $\rho$; standalone improvement $\Delta$; premium wedge $m_1 > m_0$. Expected values: $\tilde{\Delta} = \rho\Delta$, $\tilde{m} = m_0 + \rho(m_1 - m_0)$.

### A.2 Pricing and Bidder Entry
Bidder surplus: $\Pi_B = \bar{S} - P(X,D) + \xi - m(X,D) - K$, with $\xi \sim \mathcal{N}(0, \sigma_\xi^2)$.
Bid probability: $p(P,D) = 1 - \Phi\bigl((m(X,D) + K - \bar{S} + P)/\sigma_\xi\bigr)$.
Competitive price fixed point:
$$P = \delta\bigl((1-p)\hat{V}(X,D) + p(P + m(X,D))\bigr)$$
where $\hat{V}(X,D) = \mathbb{E}[v \mid X,D] + \tilde{\Delta}\pi(X,D)$ and $\pi(X,D) = \Pr(a=1 \mid X,D)$.

### A.3 Key Results (7 Propositions)
1. **Prop 1 (Monotone Cutoffs):** Three cutoffs $k_1 \leq k_0 \leq k_D$ partition the signal space. Proof via single-crossing of $U(q,a \mid s) = A_{q,a} + B_{q,a}\hat{v}(s) - a \cdot C(s)$. Existence via Banach fixed-point theorem on cutoff mapping $T$, invoking Assumption (A6) that $T$ is a contraction.

2. **Prop 2 (Posteriors):** Disclosed: $\pi(X,1) = 1$. Nondisclosed: $\pi(1,0) = \omega_Q/(\omega_H + \omega_Q)$ (independent of $\kappa$), plus formulas for $\pi(-1,0)$, $\pi(0,0)$, $\pi(-2,0) = 0$.

3. **Prop 3 (Price Decomposition):** Activism premium has a standalone channel $(1-p^*)\tilde{\Delta}\pi$ and a takeover channel $p^*(\tilde{m}-m_0)\pi$.

4. **Prop 4 (Nonmonotonicity):** $\Delta^{\min}(\kappa) = \mathbb{E}[m(a) \cdot \mathbf{1}\{\text{bid}\}]$ has an interior maximizer $\kappa^\dagger \in (0, \bar{\kappa})$. Proof uses Weierstrass theorem under Assumption (A8) (boundary conditions on the endogenous object).

5. **Prop 5 (Disclosure Attenuation):** Partial equilibrium: holding cutoffs fixed, shifting mass toward $D=1$ attenuates liquidity sensitivity of $\Delta^{\text{act}}(\kappa)$.

6. **Prop (Within-Regime Liquidity):** $\partial\pi(1,0)/\partial\kappa = 0$, $\partial\pi(-1,0)/\partial\kappa \geq 0$, $\partial\pi(0,0)/\partial\kappa \leq 0$.

7. **Prop (Takeover Comparative Statics):** $\partial p/\partial \bar{S} > 0$, $\partial p/\partial K < 0$, $\partial p/\partial P < 0$.

### A.4 Baseline Calibration
$\mu=1$, $\sigma_v = 0.5$, $\sigma_\varepsilon = 0.5$, $\delta = 0.95$, $\Delta = 0.25$, $C_0 = 0.12$, $\chi = 0.5$, $\kappa = 0.5$, $m_0 = 0.10$, $m_1 = 0.30$, $\bar{S} = 1.44$, $K = 0.15$, $\sigma_\xi = 0.40$, $\rho = 0.9$. Equilibrium cutoffs: $k_1 = k_0 \approx 0.82$, $k_D \approx 2.26$ (Hold region collapses).

### A.5 Known Weaknesses (identified by editorial review)

**Critical:**
- **Prop 4 proof is tautological.** Assumption (A8) imposes endpoint conditions on the endogenous object $\Delta^{\min}(\kappa)$, then applies Weierstrass. This is mathematically correct but economically vacuous. A top journal would demand that the endpoint behavior be derived from primitives.
- **Assumption (A6) is never proven analytically.** The contraction property that guarantees equilibrium existence/uniqueness is verified only numerically. For a theory paper, this is a gap.
- **No testable predictions.** The paper lacks a consolidated list of unique, falsifiable predictions that distinguish it from existing models.

**Major:**
- **Prop 5 is partial equilibrium only.** Holding cutoffs fixed when analyzing disclosure policy ignores the endogenous response of the blockholder. In GE, stricter disclosure may deter activism.
- **Sensitivity analysis is incomplete.** Only $C_0$ and $(m_1 - m_0)$ are varied. Key parameters $\rho$, $\sigma_\xi$, $\delta$ are not.
- **Noisy rumor extension is underdeveloped.** One paragraph for the most empirically relevant extension.
- **No welfare analysis.** Focuses on minority gains without analyzing total surplus.

**Minor:**
- Introduction front-loads policy before establishing academic contribution.
- Literature review is verbose for a theory paper.
- No timeline/game-tree figure in the model section.
- Premium notation is overloaded: $m(a)$, $m(X,D)$, $m(P,D)$, $\tilde{m}$.

---

## B. MATHEMATICAL CAUTIONS (read before writing any proofs)

1. **$B_P - B_Q > 0$ in the cutoff proof.** The correct objects are $B_{q,a} = \delta h \cdot \mathbb{E}_z[1-p(X,D)]$, where for Quiet Voice: $X = z$, $D=0$, $h=1$; and for Public Voice: $X = 1+z$, $D=1$, $h=2$. The expectations over $z$ are taken over *different* probability-weighted sums of bid probabilities. Do NOT simplify to $B_P = \delta(2)(1-p_P)$. The conclusion ($B_P > B_Q$) holds because $h_P = 2 > 1 = h_Q$ and $(1-p) > 0$ for all reached states, but the intermediate algebra must use the expectation-over-$z$ formulation.

2. **$\rho = 0.9$ is defensible.** In this model, $\rho$ is the success probability of engagement *conditional on the blockholder choosing to engage*. This is selection-conditioned: a blockholder who selectively engages only when her signal is favorable could plausibly succeed 90% of the time. Do NOT claim this is unrealistic. The sensitivity analysis should cover lower $\rho$ for robustness, but the baseline is reasonable.

3. **Figures are in Appendix C, not inline.** All 8 figures are in Appendix C (pp. 33--36). When referencing them, use labels like `Figure C.2` (the nonmonotonicity figure) or `Figure C.3` (the decomposition figure), matching the paper's `\thefigure` format which uses appendix-section numbering.

4. **Proving endpoint behavior of $\omega_Q$ as $\kappa \to 0$ requires care.** $\omega_Q = \Phi(\alpha_D) - \Phi(\alpha_0)$ depends on *equilibrium* cutoffs $k_0, k_D$ that are themselves endogenous functions of $\kappa$. The argument must show that the equilibrium cutoffs converge ($k_0 \to k_D$ as $\kappa \to 0$), not merely that a payoff comparison reverses at a fixed cutoff vector. The mechanism is: as $\kappa \to 0$, $\Pr(z=0) \to 1$, so $X \to q$ a.s., which means the market perfectly separates $q = -1$ from $q = 0$. Prices under $q = 0$ then pool Hold and Quiet Voice, but the pool itself makes the marginal engager's return shrink because the market already prices in the expected engagement improvement. This drives $k_0 \to k_D$.

---

## C. OUTPUT FORMAT

For each change below, provide one of two formats:

- **LaTeX code** for straightforward edits (rewrites of existing prose, new paragraphs, notation changes). Use the paper's commands: `\E` for $\mathbb{E}$, `\PP` for $\mathbb{P}$, `\1` for $\mathbf{1}$. Citations use `\citet{}` and `\citep{}` (biblatex authoryear).
- **Prose + math** for conceptual changes (new proofs, new propositions). Provide the full mathematical argument with all equations. I will translate to LaTeX.

**Formatting rules:**
- NEVER use em dashes (---). Use commas, semicolons, colons, or parentheses.
- Emphasis via `\emph{}`, not `\textit{}` in running prose.
- Theorem environments: `\begin{proposition}`, `\begin{lemma}`, `\begin{definition}`.
- Proofs: `\begin{proof}...\end{proof}`.
- Packages available: `amsmath, amssymb, amsthm, enumitem, booktabs, graphicx, float, hyperref, biblatex`.

---

## D. DELIVERABLES (produce in this order)

### D1. REWRITTEN ABSTRACT [LaTeX]

Sharpen the contribution statement. Lead with the gap (no existing model combines endogenous governance choice, order-flow inference, AND takeover feedback). State the nonmonotonicity result crisply. Add one sentence on the unique testable prediction (cross-country disclosure threshold variation). Keep under 200 words.

Output: Full `\begin{abstract}...\end{abstract}` block.

---

### D2. RESTRUCTURED INTRODUCTION [LaTeX]

The current introduction (pp. 2--3) has 7 paragraphs. The problem: the policy discussion (US vs. UK thresholds) appears in para 5 before the reader fully grasps the academic contribution, and the "gap in the literature" paragraph (para 3) is separated from the model description (para 4) by too much distance. Restructure:

- Para 1: The exit-vs-voice problem (current paras 1 and 2 condensed into one tighter paragraph). End with: "No existing framework combines these three forces in a single model."
- Para 2: What this paper does (current para 4, mostly intact; model description with the four actions).
- Para 3: Main results (nonmonotonicity, disclosure attenuation). State the *one* key testable prediction clearly: "The model predicts that the sensitivity of takeover premia to liquidity is lower in strict-disclosure jurisdictions."
- Para 4: Policy implications (US 5% vs. UK 3% thresholds; move current para 5's content here).
- Para 5: Empirical motivation (Brav et al. 2008, Greenwood and Schor 2009; keep current para 6).
- Para 6: Roadmap (keep current para 7 as is, but update section numbers if they change).

Output: Full rewritten introduction from `\section{Introduction}` to the roadmap.

---

### D3. TRIMMED LITERATURE REVIEW [LaTeX]

Cut by ~30%. Specific instructions:
- Section 2.1 (Exit vs. Voice): Keep Hirschman, Maug, Edmans (2009), Edmans/Manso, Edmans/Fang/Zur. Move the continuous-trading departure point discussion to a footnote.
- Section 2.2 (Microstructure): Keep Kyle, Glosten/Milgrom, EGJ (2015), EGJ (2012), BEG (2012). Move Dow/Goldstein/Guembel (2017) to a footnote.
- Section 2.3 (Activism & Takeovers): Keep Brav et al. (2008), Greenwood/Schor (2009), Grossman/Hart (1980). Move Back et al. (2018) discussion to a footnote.
- Section 2.4 (Relation): Keep all three differentiating points, tighten prose.

Output: Full rewritten Section 2.

---

### D4. TIMELINE FIGURE [LaTeX]

Add a simple annotated timeline figure in the Model section (Section 3.1, after the current enumerate timeline on p. 4--5). Show four stages ($t = 0, 1, 1.5, 2$) as labeled nodes on a horizontal line. Below each node, annotate: (a) what happens, (b) who observes what. Keep it clean; a horizontal node sequence is sufficient. The paper already loads `\usepackage{graphicx}` and `\usepackage{float}` but does NOT currently load `tikz`. If you use TikZ, note that `\usepackage{tikz}` must be added to the preamble.

Output: A `\begin{figure}[H]...\end{figure}` block.

---

### D5. ENGAGEMENT COST MICRO-FOUNDATION [LaTeX]

The paper already has a brief one-sentence justification on p. 6: "a blockholder with more favorable private information finds it easier to build a compelling case for change." **Expand** this into a full paragraph (4--5 sentences) placed right after the $C(s) = C_0 \exp(\cdots)$ equation and its surrounding text (Section 3.6, p. 6). The expanded micro-foundation should include: (i) the economic mechanism (favorable signal means the blockholder can point to concrete operational improvements, peer comparisons, or undervaluation evidence, lowering the cost of persuading the board); (ii) a note that the exponential form is chosen for analytical convenience but the results require only strict positivity and monotone decrease in $s$; (iii) a brief mention that if costs were increasing in $s$ (e.g., because high-value firms have entrenched management harder to dislodge), the cutoff ordering would potentially invert, which is why the monotonicity assumption is economically substantive.

Output: One LaTeX paragraph that replaces/extends the existing one-sentence justification.

---

### D6. STRENGTHENED PROPOSITION 4 (Nonmonotonicity) [Prose + math] -- PRIORITY 1

This is the most important fix. The current proof (Appendix A.8, pp. 29--30) uses Assumption (A8) (introduced on p. 14), which imposes endpoint conditions on the endogenous $\Delta^{\min}(\kappa)$, then applies the Weierstrass extreme value theorem. The problem: (A8) essentially assumes the shape of the result. Replace this with:

**(a) New Lemma (Endpoint Behavior from Primitives).**

**Left endpoint ($\kappa \to 0$):** As noise trading vanishes, $\Pr(z=0) \to 1$, so $X \to q$ a.s. The market maker perfectly infers $q$ from $X$, collapsing the blockholder's information advantage. Formally:
- When $D = 0$ and $X = 0$, the market knows $q = 0$, pooling Hold and Quiet Voice. The price $P(0,0)$ incorporates $\pi(0,0) = \omega_Q/(\omega_H + \omega_Q)$ (which simplifies to $\omega_Q/(\omega_H + \omega_Q)$ because $\kappa \to 0$ means the $X=0$ state is dominated by $z=0$, i.e., $P(X=0, D=0)$ reflects the pooled posterior).
- The marginal type $k_0$ (indifferent between Hold and Quiet Voice) faces: the market already prices in expected engagement at $\pi(0,0)$, so the incremental benefit of engaging shrinks. The indifference condition $U_H(k_0) = U_Q(k_0)$ yields $k_0 \to k_D$, collapsing the Quiet Voice region.
- With $\omega_Q \to 0$, the activism-driven component $\Delta^{\text{act}} \to 0$, and $\Delta^{\min}(\kappa) \to m_0 \cdot \Pr(\text{bid})$.

The key technical step: Show that in the $\kappa \to 0$ limit, the expected payoff difference $U_Q(s) - U_H(s) \to -C(s) < 0$ for all $s$, because the price under $q = 0$ already impounds the engagement effect, leaving the blockholder paying $C(s)$ for zero incremental benefit. **Important:** This must account for the fact that the pooling posterior $\pi(0,0)$ itself depends on $\omega_Q$, creating a fixed-point argument. As $\omega_Q \to 0$, $\pi(0,0) \to 0$, so the price no longer reflects engagement, but then engaging becomes individually rational again. Show that the unique equilibrium resolution is $\omega_Q \to 0$ by verifying that the fixed point collapses.

**Right endpoint ($\kappa \to 1$):** As noise dominates, $z$ is uniform on $\{-1, 0, +1\}$ with probability $1/2, 0, 1/2$. Order flow $X$ becomes nearly uninformative. Posteriors converge to prior probabilities (e.g., $\pi(X, 0)$ becomes independent of $X$). The blockholder cannot profit from her information advantage, so engagement incentives collapse. Formally, show that prices converge across all $(X, D=0)$ states, eliminating the adverse-selection rents that make engagement profitable.

**(b) Revised Proposition 4.** Restate using the new lemma to replace (A8)(i) and (A8)(ii). Keep (A8)(iii) as a verifiable sufficient condition (existence of $\tilde{\kappa}$ with $\Delta^{\min}(\tilde{\kappa}) > m_0$), but note it can be checked from primitives via the numerical solver.

**(c) Remark on shape.** The Weierstrass argument guarantees at least one interior peak but not uniqueness. State that the calibration confirms a single peak (Figure C.2 in Appendix C). Briefly discuss conditions under which a W-shape could arise (e.g., if the Quiet Voice region has a non-convex response to $\kappa$).

Output: Full mathematical argument for (a), (b), and (c), with all equations and explicit references to which assumptions are used at each step.

---

### D7. SUFFICIENT CONDITIONS FOR (A6) CONTRACTION [Prose + math] -- PRIORITY 1

Preferred option: Derive an analytical sufficient condition on primitives $(\delta, \sigma_\xi, \sigma_v, \sigma_\varepsilon, C_0, \chi)$ that guarantees the spectral radius of the Jacobian of the cutoff mapping $T$ is less than 1.

If a clean bound is not feasible, provide instead: (i) an acknowledgment of the gap; (ii) a rigorous argument for why numerical verification is the best available approach for this model class; (iii) a comparison to how Edmans, Goldstein, and Jiang (2015) handle the same issue (they also verify equilibrium properties numerically in their discrete-order-flow model); (iv) a weaker existence result via Brouwer's fixed-point theorem on a compact convex set, which gives existence without uniqueness.

Output: Full mathematical argument or rigorous discussion.

---

### D8. NEW SUBSECTION: TESTABLE IMPLICATIONS [LaTeX] -- PRIORITY 1

Add a new subsection at the end of Section 6 (Comparative Statics, pp. 16--18), as Section 6.4. This goes before Section 7 (Extensions). Produce 4--5 numbered predictions, each with: formal model statement, empirical proxy/data source, identification challenge.

The predictions:

1. **Cross-country disclosure attenuation:** Sensitivity of takeover premia to stock liquidity is lower under strict disclosure (UK 3%) than loose disclosure (US 5%). Proxy: regress premia on Amihud illiquidity $\times$ UK/US indicator. Data: SDC + CRSP/Compustat + LSE.

2. **Order-flow inference and bid prediction:** In nondisclosed states, the model predicts specific orderings of $\pi(X, 0)$ across order-flow bins. Check: under the baseline, $\pi(0,0) > \pi(-1,0)$ because $X=0$ is more likely generated by Hold/Quiet Voice (high prior on $z=0$). This implies zero abnormal volume predicts higher engagement probability than moderate selling. Proxy: sort target firms by pre-bid abnormal volume; test whether zero-volume firms have higher subsequent bid rates.

3. **Nonmonotone liquidity effect on premia:** Across firms, the relationship between market liquidity and takeover premia (conditional on bid) is hump-shaped. Proxy: bin firms by Amihud illiquidity quintiles; plot average premia. Data: SDC + CRSP.

4. **Activism premium in pre-bid prices:** Target stock prices embed an activism premium that is larger when engagement is inferred ($D=0$) than when directly observed ($D=1$), after controlling for fundamentals. Wait, this needs care: the model says $\pi(X,1) = 1 > \pi(X,0)$ for all states, so the activism premium is actually *higher* in disclosed states. The testable prediction is about the *price response to disclosure*: a 13D filing reveals $\pi = 1$, causing a discrete price jump that reflects the gap between inferred and known engagement. Proxy: 13D event study abnormal returns. Data: EDGAR + CRSP.

5. **Bid deterrence under disclosure:** Public Voice ($D=1$) deters bids more than Quiet Voice because $m(X,1) = \tilde{m} > m(X,0)$. Prediction: firms with 13D filings receive fewer but higher-premium bids. Proxy: match 13D filers to M&A bids. Data: SharkRepellent + SDC.

Output: Full LaTeX subsection with `\paragraph{}` or numbered list for each prediction.

---

### D9. GENERAL-EQUILIBRIUM DISCLOSURE RESULT [Prose + math, then LaTeX] -- PRIORITY 2

The current Proposition 5 (Disclosure Attenuation, Section 4.8, p. 15) is explicitly partial equilibrium: "Hold the blockholder's strategy constant: fix the cutoffs $(k_1, k_0, k_D)$." Add a new Proposition (as a companion result in Section 7 Extensions, or as a new Section 6.3 within Comparative Statics) characterizing the GE effect of lowering the disclosure threshold. Two opposing forces:
- **Transparency effect** (Prop 5's PE result): more $D=1$ mass attenuates inference channel.
- **Deterrence effect:** stricter thresholds reduce expected returns to quiet engagement, potentially shrinking $\omega_Q + \omega_P$.

State the ambiguity formally. Provide sufficient conditions under which each effect dominates (e.g., transparency dominates at moderate $\kappa$ and low $C_0$; deterrence dominates at high $\kappa$ and high $C_0$). If a clean analytical result is not possible, state the proposition with conditions and supplement with a numerical illustration.

Output: Proposition statement and proof sketch (prose + math), then a LaTeX discussion paragraph.

---

### D10. EXPANDED SENSITIVITY ANALYSIS [LaTeX] -- PRIORITY 2

Add discussion and figure descriptions for three new parameter sweeps:

- **$\rho$ sensitivity** ($\rho \in \{0.5, 0.7, 0.9\}$): Lower $\rho$ flattens the hump because $\tilde{\Delta}$ and $\tilde{m} - m_0$ shrink. Note: $\rho = 0.9$ is defensible as selection-conditioned (blockholder engages only on favorable signals), but lower values are important for robustness.
- **$\sigma_\xi$ sensitivity** ($\sigma_\xi \in \{0.25, 0.40, 0.60\}$): Higher bidder heterogeneity raises average bid incidence but also relaxes the regularity condition (A5). Discuss the interaction between $\sigma_\xi$ and the feedback loop.
- **$\delta$ sensitivity** ($\delta \in \{0.85, 0.90, 0.95\}$): Lower discount factors reduce all present values, shrinking engagement incentives. Note interaction with (A5): $\delta/\sigma_\xi < 1/\phi(0)$.

For each: describe the expected qualitative effect, what the figure should show ($\Delta^{\min}(\kappa)$ for each parameter value), and the economic interpretation.

Output: LaTeX paragraphs for Section 5.3 (Sensitivity Analysis, p. 16), plus figure descriptions (captions and content).

---

### D11. EXPANDED NOISY RUMOR EXTENSION [LaTeX] -- PRIORITY 2

Expand Section 7.3 (pp. 19--20, currently a single paragraph titled "An Intermediate Regime: Stake Disclosure Plus Noisy Rumors") into a full subsection:
- Write out the posterior formulas $\pi(X, 0, R)$ explicitly in the main text (they are currently only in the appendix derivations).
- Describe a figure showing how $\Delta^{\min}(\kappa)$ flattens as rumor precision $(\eta_1 - \eta_0)$ increases. Compare: no rumor ($\eta_1 = \eta_0$), moderate ($\eta_1 = 0.75, \eta_0 = 0.25$), precise ($\eta_1 = 0.95, \eta_0 = 0.05$).
- Add a paragraph connecting to empirical literature: Fang and Peress (2009, media coverage and returns), the role of Bloomberg/Reuters in leaking activist positions, and 13F filings as noisy quarterly signals.

Output: Full LaTeX subsection.

---

### D12. WELFARE ANALYSIS [Prose + math, then LaTeX] -- PRIORITY 2

Add a new subsection as Section 7.4 (after the expanded noisy rumor extension, before Section 8 Conclusion) on welfare. Define:
- Minority welfare: $W_{\text{min}}(\kappa) = \Delta^{\min}(\kappa)$ (already defined).
- Blockholder welfare: $W_B(\kappa) = \mathbb{E}[U(q^*, a^* \mid s)]$.
- Bidder welfare: $W_{\text{bid}}(\kappa) = \mathbb{E}[\max(\Pi_B, 0)]$.
- Total surplus: $W(\kappa) = W_{\text{min}} + W_B + W_{\text{bid}}$.

Discuss: Does the nonmonotonicity in $\Delta^{\min}$ extend to total surplus, or is it distributional (moderate liquidity redistributes toward minorities at the expense of bidders)? If the planner maximizes total surplus, does $\kappa^*$ differ from $\kappa^\dagger$?

Output: Mathematical definitions and arguments (prose + math), then LaTeX discussion paragraphs.

---

### D13. NOTATION STREAMLINING [Table] -- PRIORITY 3

The premium notation is overloaded. Currently:
- $m(a) = m_0 + a(\tilde{m} - m_0)$: realized premium (function of action)
- $m(X,D) = m_0 + (\tilde{m} - m_0)\pi(X,D)$: expected premium conditional on observables
- $m(P,D)$: same as $m(X,D)$ via the injective price schedule
- $\tilde{m}$: expected premium under engagement ($= m(a=1)$)

Propose a cleaner scheme. One option: $m^R(a)$ for realized, $\bar{m}(X,D)$ for conditional expectation, keep $\tilde{m}$. Or propose your own. Goal: a reader never needs to check which "$m$" they are looking at.

Output: Old-to-new mapping table, plus a list of every equation number that needs updating.

---

### D14. REWRITTEN CONCLUSION [LaTeX]

The current conclusion is Section 8 (pp. 20--21), approximately 3 paragraphs. Rewrite to:
- Restate the contribution crisply (echo the sharpened abstract from D1).
- Summarize the testable implications (from the new Section 6.4, deliverable D8).
- Mention the welfare implications (from the new Section 7.4, deliverable D12).
- Keep the future extensions paragraph (dynamic model, wolf packs, endogenous info acquisition) but connect wolf packs to the noisy rumor extension (Section 7.3).
- Same approximate length as the current conclusion (~3 paragraphs).

Output: Full LaTeX for the `\section{Conclusion}`.

---

## E. GLOBAL INSTRUCTIONS

1. **Never use em dashes (---)** anywhere. Use commas, semicolons, colons, or parentheses.
2. **Formal academic tone** throughout. This targets JF/RFS/JFE.
3. **Be fully specific.** When you say "add a paragraph," write the paragraph. When you say "revise the proof," write the entire revised proof. Vague suggestions are useless.
4. **Cross-references:** When adding propositions or sections, state where they fit in the existing numbering and flag any cross-references that need updating.
5. **For new proofs and propositions:** Provide the complete mathematical argument with every step. Precision over brevity.
6. **For LaTeX code:** Ensure compatibility with `amsmath, amssymb, amsthm, enumitem, booktabs, graphicx, float, hyperref, biblatex`.
7. When referencing the paper's existing equations, use the labels from the paper: `\eqref{eq:pricing}`, `\eqref{eq:bid-prob}`, `\eqref{eq:price-fp}`, `\eqref{eq:minority}`, `\eqref{eq:decomp}`, etc.
