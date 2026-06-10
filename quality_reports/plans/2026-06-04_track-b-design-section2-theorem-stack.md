---
date: 2026-06-04
type: plan
status: DESIGN
branch: jmp-upgrade-2026-05
title: "Track B — Design Section 2: The Theorem Stack (Joint Disclosure–Takeover Model, Benchmark-First)"
authors: lead author (Track B)
supersedes: none (new design doc; builds on locked Track-B decisions)
related:
  - quality_reports/plans/2026-04-21_three-paths-jmp-strategy.md
  - quality_reports/plans/2026-05-02_structural-disclosure-law-jmp-gptpro-brief.md
  - quality_reports/plans/2026-05-30_jmp-upgrade-critique-and-roadmap.md
  - draft_v2.tex (the static paper = the Section-2 sharp benchmark / special case)
---

# Track B — Design Section 2: The Theorem Stack

> **Honesty contract (job-market paper).** This document is prod-grade and adversarial-by-design. Where a result is inherited, it says so with page/equation citations. Where a result is genuinely new, it says so and demonstrates orthogonality rather than asserting it. Where a claim rests on an unproven regularity assumption or is conjectural, it is **labelled as such in-line and in the assumption ledger**. A wrong claimed theorem in a JMP is fatal; an honestly-flagged open item is not. Nothing in this document fabricates a closed form or a clean sign.

---

## 1. Executive summary + contribution statement

### 1.1 What this section does

Section 2 of the Track-B paper is the **theorem stack** for a *full joint* continuous-time model of an activist blockholder who (a) trades a stake inconspicuously into a market with order-flow-based pricing, (b) crosses a stake-triggered disclosure threshold $\theta_D$ (the 13D 5% rule) at a random stopping time $\tau_D$, and (c) faces a Poisson takeover bidder who bargains over synergy surplus. The section is organized **benchmark-first**: a sharp closed-form benchmark carries the load, and the existing static paper (`draft_v2.tex`) is re-cast as the **single-period degeneration** of that benchmark — a rigorous special case, not a separate model. This is what protects the prior 6–8 months of work.

The stack contains the following theorems (full statements in §4):

- **T1 — Sharp closed-form benchmark + static-paper-as-special-case.** Under constant bidder intensity and the resolved hybrid two-stage information structure, the pre-disclosure regime inherits Back–Collin-Dufresne–Fos–Li–Ljungqvist (2018) [hereafter **Back-CDF**] in closed form, and the static paper is recovered exactly as the $T\downarrow 0$ single-tick limit.
- **T2 — Disclosure-attenuation (the HEADLINE).** Stricter / earlier disclosure (smaller $\theta_D$ ⇒ earlier $\tau_D$) makes the takeover premium **less sensitive to market liquidity**. This is the result EGJ (2015) and Back-CDF (2018) provably cannot generate.
- **T3 — Premium-hump (SUPPORTING).** The expected minority takeover premium is **single-peaked** in liquidity in the benchmark, recovering the static paper's hump $\Delta^{\min}(\kappa)$ as the limit.
- **T4 — Free-boundary / verification theorem** for the joint model with the disclosure stopping time and the Poisson bidder (the elegance-without-closed-form fallback).
- **C† — one transparent primitive sufficient condition** under which T2's sign is unconditional (the "C-dagger" condition mandated by the locked design).

### 1.2 The one-paragraph contribution statement

> *I embed a stake-triggered disclosure threshold and a Poisson takeover bidder into the continuous-time Kyle/Back model of an activist trader, and show that **stricter disclosure attenuates the sensitivity of takeover premia to market liquidity**. The mechanism is a stopping-time split of order-flow inference: before the stake hits the 13D threshold the activism/takeover premium is *inferred* from order flow and is therefore liquidity-sensitive; after disclosure it is *observed* and is liquidity-insensitive. Lowering the threshold moves probability mass into the observed regime, compressing the liquidity channel. This headline cannot be produced by Back-CDF (2018) — whose stake is never disclosed and which has no bidder — nor by Edmans-Goldstein-Jiang (2015) — whose blockholder acquires no stake and so crosses no threshold; the result is generated entirely by the interaction of the two new layers with the inherited microstructure machinery. The existing static four-action (Exit / Hold / Quiet / Public) model is the single-period degeneration of the benchmark, so it survives as the paper's sharp special case rather than being discarded.*

---

## 2. D0.1 decision record (the information-structure fork)

### 2.1 The fork as posed

> Is the activist's private information **(A)** her own stake $X_0$ (pure Back-CDF), or **(B)** a fundamental signal $s$ about firm value (the static paper), or **(C)** a hybrid?

### 2.2 Resolution — **(C) hybrid, two-stage**, with a deterministic upstream map

**RECOMMENDATION: C (hybrid / two-stage)**, constructed so that A is the *literal Section-2 benchmark* and B is the *conceptual content*, joined by a **deterministic map** $s \mapsto x^*(s)$ rather than a second latent state.

**Key insight that dissolves the tractability objection.** Both models are *one-dimensional-sufficient-statistic* models. The static paper's entire architecture (slopes `eq:slopes`, line 577 of `draft_v2.tex`; the monotone best-response Lemma, line 607) is generated by a single scalar — the posterior mean $\hat v(s)=\mu+\beta(s-\mu)$ entering payoffs affinely with totally ordered slopes $B(E)=0 < B(H)=B(Q)=1 < B(P)=1+\eta$. Back-CDF likewise reduce their information structure to one scalar latent $U_t$ with a single signal-to-noise object $\Lambda = 1+\sqrt{1+\sigma_x^2/(\sigma^2 T)}$ and a Riccati that solves in closed form. The hybrid exploits this: the fundamental signal $s$ realizes **first** ($t=0$), and is **fully consumed upstream** by the activist's static optimization, which pins a *target terminal stake* $x^*(s)$. On the trading subgame the market maker filters *only that scalar target* from order flow — exactly the Back-CDF problem, one-dimensional and Gaussian. **$s$ is never a second thing the market maker filters.** This is the device (Lemma U / R4) that keeps the filtering tractable.

### 2.3 Tradeoff matrix

| Option | Hosts 4-action menu? | Filtering stays 1-D Gaussian? | Recovers static paper exactly? | Generates disclosure-attenuation headline? | Closed form available? | Verdict |
|---|---|---|---|---|---|---|
| **A — stake only (pure Back-CDF)** | **No** — activist has no "news," so Exit-on-bad / Public-on-good is meaningless | Yes | No (would have to bolt $s$ back on = the hybrid) | **No** — engagement premium has no inferred-vs-observed content without private $s$ | Yes | **Reject** |
| **B — stake + separately-filtered $s$** | Yes | **No** — two latent states ⇒ a non-scalar filter, Riccati no longer closed-form; existence/uniqueness fragile | Yes (in principle) | Yes | **Unlikely** | **Reject (the dangerous fork)** |
| **C — hybrid, $s$ upstream ⇒ scalar target $x^*(s)$** | **Yes** | **Yes** (Lemma U: $s$ consumed at $t=0$) | **Yes (exact, as $T\downarrow 0$ limit)** | **Yes** | **Yes for benchmark** | **ADOPT** |

### 2.4 Why not pure A; why not pure B (the load-bearing rationale)

- **Not pure A.** It cannot host the four-action menu honestly. In Back-CDF the activist has no fundamental view, so the Exit/Hold/Quiet/Public partition has no informational content. You would have to add a fundamental signal back in anyway — which *is* the hybrid. Pure A also cannot produce the headline, because attenuation keys off the activist's *engagement premium* being inferred-vs-observed, and engagement only has content when the activist knows something ($s$) the bidder does not.
- **Not pure B (the genuinely dangerous fork).** If $s$ is a *second* latent state the market maker filters jointly with $X_t$, the inference problem ceases to be one-dimensional Gaussian. The Back-CDF Riccati closes only because the latent is scalar; a two-state filter generically loses the closed-form $\Sigma(t)=(T-t)a^2/T$, and equilibrium existence/uniqueness becomes a numerical hope rather than a theorem. Option B trades the entire tractability of the benchmark for nothing the hybrid does not already deliver.
- **The resolution's cost.** The hybrid buys tractability at the price of one structural assumption (Lemma U / R4): that $s$ acts on the trading subgame *only* through the scalar $x^*(s)$. This holds by construction of the timing (s realizes and is consumed at $t=0$), but it does forbid the activist from *learning* about her own $s$ from order flow during $[0,\tau_D]$ — an acceptable simplification flagged in the ledger.

---

## 3. Foundation: what we stand on (Back-CDF) vs. what is orthogonal/new

### 3.1 Inherited from Back-CDF (2018), with citations

The pre-disclosure regime is **transported verbatim** from Back-CDF under the scalar-target reduction. The inherited objects:

| Object | Back-CDF location | Form |
|---|---|---|
| Model setup (single strategic trader = activist; noise; competitive market makers) | §3, pp. 1434–1438 | continuous-time Kyle (1985) generalized via Back (1992) |
| Activist's only private info = her own position $X_t$ | p. 1435 | information structure |
| Effort problem ⇒ convex conjugate $G(x)=\sup_{v'}\{v'x-C(v')\}$, $V=G'$ | eqs. 1–3, pp. 1435–1436 | $V$ = marginal value of shares; $V$ convex/concave governed by $G'''$ (not signable) |
| Signal-to-noise constant $\Lambda=1+\sqrt{1+\sigma_x^2/(\sigma^2 T)}$ | eq. 8, p. 1437 | the SNR object |
| Pricing rule $P(t,y)=\mathbb E[V(\mu_x+\Lambda Z_T)\mid Z_t=y]$ | eq. 10, p. 1437 | Gaussian conditional expectation |
| Trading rate $\theta_t=\frac{1}{T-t}\frac{X_t-\mu_x-\Lambda Y_t}{\Lambda-2}$ (linear, **cost-independent**) | eq. 11 | the strategy |
| Price impact $\lambda(t,y)=\partial_y P$, a **martingale** on $[0,T-\delta]$ | eq. 13 | $\mathbb E[\bar\lambda]=\lambda(0,0)$ |
| Terminal position $X_T=\mu_x+\Lambda Y_T$ a.s. | eq. 14, p. 1440 | over-reacts to noise: coeff on $-Z_T$ is $\Lambda/(\Lambda-1)>1$ |
| Kalman–Bucy / Kallianpur filter | Lemma 1 + App. A, pp. 1439, 1454–1455 | Kallianpur (1980) 10.5.9, 10.5.10 |
| Riccati ODE $\dot\Sigma=-\Sigma^2/((T-t)^2\sigma^2)+2b\Sigma/(T-t)$, **closed form** $\Sigma(t)=(T-t)a^2/T$ | eq. A.3 | conditional variance collapses linearly to 0 at $T$ |
| HJB verification: $-P+J_x+J_y=0$; $J_t+\tfrac12\sigma^2 J_{yy}=0$ | App. B, eqs. 19, 20a–b, pp. 1455–1456 | any strategy enforcing price=marginal-value at $T$ is optimal |

### 3.2 What is orthogonal / new (the contribution surface)

Four layers Back-CDF does **not** have, established as facts from the anchor extraction:

1. **Upstream signal + target-stake map $x^*(s)$.** Back-CDF's activist has *no* fundamental view (anchor fact: her only private info is her own position). The Exit/Hold/Quiet/Public menu and $x^*(s)$ require the new signal layer.
2. **Stake-hitting disclosure time $\tau_D=\inf\{t: X_t\ge\theta_D\}$.** Back-CDF's stake is **never disclosed** — their $T$ is the anonymity window (anchor fact ii). Back-CDF §8, p. 1454, item 1 *explicitly* lists endogenizing the 13D horizon as future work and names the 5% rule. We answer their open question.
3. **Poisson bidder + Nash-bargaining premium wedge.** There is **no takeover** in Back-CDF (anchor fact iv). The wedge $m_1-m_0=(1-\theta)\lambda_{\mathrm{app}}\rho\Delta_{\mathrm{eng}}$ reuses the static paper's bargaining micro-foundation (Theorem `thm:bg-A3`, `draft_v2.tex` line 284).
4. **Liquidity comparative static via $\kappa$.** Back-CDF's liquidity-efficiency result is a *convexity sign* of $V$ via Jensen (anchor fact i), **not** the discrete liquidity comparative static. The bridge $\kappa=\Xi(\sigma_x^2/(\sigma^2 T))$ that makes the static paper a limit is new.

**Orthogonality must be demonstrated, not assumed.** Each theorem below carries a `requires_new_layer` clause spelling out precisely which of layers 1–4 it depends on, and a one-line proof-by-construction that Back-CDF (or EGJ, or OCB) *cannot* reach the claim by varying their own parameters.

---

## 4. The theorem stack

Notation throughout: $Z$ = Brownian noise order flow, $\mathrm{Var}(Z_t)=\sigma^2 t$, $Z_0=0$; $X_t$ = activist cumulative shares; $Y_t=X_t-X_0+Z_t$ = observable flow; $\Lambda=1+\sqrt{1+\sigma_x^2/(\sigma^2 T)}$; $b=1/(\Lambda-2)$; $a=\sigma\sqrt{(2b+1)T}$; $\theta_D$ = disclosure threshold; $\tau_D=\inf\{t:X_t\ge\theta_D\}$; $\hat v(s)=\mu+\beta(s-\mu)$, $\beta\in(0,1)$.

---

### T1 — Sharp closed-form benchmark; the static paper as the single-period degeneration

**Informal statement.** Under constant bidder intensity (benchmark) and the hybrid two-stage information structure, on the pre-disclosure regime $\{t<\tau_D\}$ the joint model has a sharp closed form inherited from Back-CDF: (i) linear cost-independent trading rate; (ii) closed-form Riccati $\Sigma(t)=(T-t)a^2/T$, conditional variance collapsing linearly to 0; (iii) martingale price impact and the inferred-premium Gaussian conditional expectation $P(t,y)=\mathbb E[V(\mu_x+\Lambda Z_T)\mid Z_t=y]$. **(iv)** The static paper is the single-period ($T\downarrow 0$, three-point tick $z\in\{-1,0,+1\}$) degeneration: the static pricing fixed point $P^*(X,D)$, the four-action indifference system (`eq:k1`–`eq:kD`, lines 548–550), and the minority premium $\Delta^{\min}(\kappa)$ are recovered exactly, with the discrete liquidity index identified as $\kappa=\Xi(\sigma_x^2/(\sigma^2 T))$.

**Formal statement (compressed).** With $\Lambda,b,a$ as above, on $\{t<\tau_D\}$:
$$\theta_t=\frac{1}{T-t}\frac{X_t-\mu_x-\Lambda Y_t}{\Lambda-2},\quad \Sigma(t)=\frac{(T-t)a^2}{T},\ \Sigma(T^-)=0,\quad X_T=\mu_x+\Lambda Y_T\ \text{a.s.},$$
$$P(t,y)=\mathbb E[V(\mu_x+\Lambda Z_T)\mid Z_t=y],\quad \lambda(t,y)=\partial_y P\ \text{a martingale},\ \mathbb E[\bar\lambda]=\lambda(0,0).$$
**(iv)** Collapse $[0,T]$ to one tick ($T\downarrow 0$) with $\Pr(z=0)=1-\kappa,\ \Pr(z=\pm1)=\kappa/2$, under $\kappa=\Xi(\sigma_x^2/(\sigma^2 T))=\Xi((\Lambda-1)^2-1)$, $\Xi:[0,\infty)\to(0,1)$ a fixed continuous strictly decreasing bijection (R2). Then the reduced-form pricing operator converges to the static fixed point $P(X,D)=\delta\,\mathbb E[Y\mid X,D]$, the indifference system $U_E=U_H(k_1),\ U_H(k_0)=U_Q(k_0),\ U_Q(k_D)=U_P(k_D)$ is recovered exactly, and $\Delta^{\min}_{\mathrm{joint}}(\kappa)\to\Delta^{\min}(\kappa)$ for all $\kappa\in(0,1)$.

**Assumptions.** (A0)–(A4) static primitives (Gaussian fundamental; interior weakly-ordered cutoffs $k_1\le k_0\le k_D$; premium wedge $\tilde m>m_0$; bidder-entry bounds + price-feedback non-explosiveness). (R1) Back-CDF information structure (effort cost l.s.c., superlinear; $G=C^*$ convex; $V=G'$). (R2) liquidity-identification bijection $\Xi$ — **ASSUMED** functional form. (R3) equilibrium-selection convergence as $T\downarrow0$ — **ASSUMED, load-bearing gap**. (R4) Lemma U scalar-sufficiency — holds by construction.

**Proof strategy.** Four parts, one load-bearing lemma each. (1) *Lemma U / R4*: the static optimization is a monotone step map $s\mapsto x^*(s)\in\{0,1,2\}$ (by `eq:slopes` totally-ordered slopes), so $X_0=x^*(s)$ is a sufficient statistic — collapses two latent states to one. (2) *Closed-form Riccati* (Back-CDF Lemma 1 + App. A) — the only reason a closed form exists. (3) *HJB verification* (Back-CDF App. B) certifies (i) optimal. (4) *Degeneration* (the new, delicate part): show the continuous Gaussian conditional expectation degenerates cell-by-cell to the discrete competitive price under $\kappa=\Xi(\cdot)$; verify the four-action system and $\Delta^{\min}$ are exact limits. **Honesty:** object convergence is structural; **selection convergence is assumed (R3).**

**Requires-new-layer.** Back-CDF alone cannot produce (iv), the disclosure split, or the bidder-conditioned premium: no fundamental view ⇒ no $x^*(s)$; stake never disclosed ⇒ no $\tau_D$; no bidder ⇒ no $\Delta^{\min}$. The benchmark is the *union* of Back-CDF machinery (i)–(iii) with the new scalar-target reduction and limit identification.

#### Referee verdict — T1
- **Overall: ACCEPT WITH FIXES.** Parts (i)–(iii) are airtight (inherited). The novelty and the risk both live in (iv).
- **Objection 1 (R3, load-bearing).** "You prove the *objects* converge, not the *equilibrium selection*. A referee will ask whether the limit fixed point is actually the static PBE you claim, or merely a fixed point that shares its reduced form." **Required fix:** either (a) prove selection convergence under a refinement (e.g., monotone/D1), or (b) keep R3 explicit and mirror the static paper's own honest treatment of uniqueness as a numerical regularity (`draft_v2.tex` line 372 footnote; Remark `numreg`). Current plan: (b), with a numerical convergence study as corroboration.
- **Objection 2 (R2 functional form).** "$\Xi$ is asserted, not derived. The headline's $\kappa$-comparative static could be an artifact of the chosen $\Xi$." **Required fix:** prove all qualitative results are *invariant to the choice of $\Xi$ within the monotone-bijection class* (only endpoints and monotonicity are used, never the exact shape). This is achievable and should be elevated to a lemma.
- **Objection 3 (Gaussian approx of $x^*(s)$).** $X_0$ is a 3-point step variable but is treated as $\mathcal N(\mu_x,\sigma_x^2)$ for the filter. **Required fix:** state the Gaussian-approximation explicitly as a modeling device; show the limit (iv) does not depend on it (the 3-point law is what survives at $T\downarrow0$).
- **Current confidence: 0.80.** High on inherited parts; the discount is entirely R3 + R2-shape.

---

### T2 — Disclosure-attenuation (THE HEADLINE)

**Informal statement.** Stricter / earlier disclosure (smaller $\theta_D$ ⇒ stochastically earlier $\tau_D$) makes the takeover premium **less sensitive to market liquidity**. Formally, the liquidity-sensitivity of the expected premium, $\partial_\kappa \mathbb E[\text{premium}]$ (equivalently $\partial \mathbb E[\text{premium}]/\partial \bar\lambda$ in continuous-time form), is **decreasing in magnitude as $\theta_D$ falls**. The mechanism: the premium is *inferred* from order flow on $\{t<\tau_D\}$ (liquidity-sensitive, governed by $\Sigma(t)$) and *observed* on $\{t\ge\tau_D\}$ (liquidity-insensitive). Lowering $\theta_D$ shifts probability mass from the inferred regime to the observed regime, compressing the liquidity channel.

**Formal statement (conditional-variance / Kallianpur form — the elegant packaging).** Let $\pi(\theta_D)=\Pr(\tau_D<T)$ be the disclosure probability and write the expected premium as a convex combination
$$\mathbb E[\Pi] = \mathbb E\big[\Pi^{\text{inf}}\,\mathbf 1\{\tau_D\ge T\}\big] + \mathbb E\big[\Pi^{\text{obs}}\,\mathbf 1\{\tau_D< T\}\big],$$
where the inferred premium carries the liquidity loading through the filter conditional variance $\Sigma(t)$ and the observed premium does not. Then
$$\left|\frac{\partial}{\partial \kappa}\,\mathbb E[\Pi]\right| \ \text{is non-increasing in}\ (-\theta_D),\ \text{i.e. decreasing as } \theta_D \downarrow,$$
**provided** the inferred-regime premium is more liquidity-sensitive than the observed-regime premium pointwise — the content of condition **C†** below. The sign is *unconditional* under C†; absent C† the result is signed numerically in the benchmark and stated as the leading comparative static.

**Assumptions.** All of T1's, plus: (D1) $\tau_D$ stochastically decreasing in $\theta_D$ (immediate from $\tau_D=\inf\{t:X_t\ge\theta_D\}$ and a.s. continuity of $X$). (D2) the observed-regime premium does **not** load on $\Sigma(t)$ (definitional: post-disclosure the stake is public). (C†) — see §5.

**Proof strategy.** Decompose $\mathbb E[\Pi]$ into inferred + observed branches at $\tau_D$. The inferred branch's $\kappa$-derivative routes entirely through $\Sigma(t)$ and the SNR object $\Lambda$ (which depends on $\kappa$ via R2); the observed branch's $\kappa$-derivative is zero by D2. Lowering $\theta_D$ raises $\pi(\theta_D)$ (D1), reweighting toward the $\kappa$-insensitive branch. The remaining step — that the *magnitude* of the inferred branch's sensitivity dominates — is C†. **Two packagings, per the locked design:** (a) the conditional-variance/Kallianpur form above (preferred, elegant, no closed form needed); (b) a closed-form benchmark sign via the $T\downarrow0$ degeneration, where T2 reduces *exactly* to the static paper's disclosure-attenuation statement (the static abstract, line 97: "Lowering the disclosure threshold ... compressing the activism premium into the observable regime and making it less sensitive to liquidity").

**Requires-new-layer.** This is the theorem that **cannot exist** without layers 2 (disclosure $\tau_D$) and 3 (bidder/premium). Back-CDF has no premium object and no disclosure ⇒ the statement is not even expressible in their model. EGJ (2015) has no stake acquisition ⇒ no threshold-crossing event (anchor: the blockholder acquires no stake; confirmed `draft_v2.tex` line 134). OCB (2022) has no continuous-time order-flow fixed point and no bidder-entry channel ⇒ cannot route a premium through inference. **The headline is the interaction of the two new layers with the inherited filter — not a special case of any competitor.**

#### Referee verdict — T2
- **Overall: ACCEPT WITH FIXES (conditional on C†); REJECT if asserted unconditionally without C†.** The mechanism is clean and genuinely novel; the danger is overclaiming the *sign* in the full (non-benchmark) model.
- **Objection 1 (the sign is not free).** "The reweighting argument shows the *composition* shifts toward the insensitive branch, but the inferred branch's own sensitivity could in principle rise as $\theta_D$ falls (selection: only high-$X$ paths disclose early), partially or fully offsetting." **This is the central adversarial objection and it is correct.** **Required fix:** isolate the offsetting selection effect explicitly; C† is precisely the condition that bounds it. Do **not** claim the unconditional sign without C† — label the general case "signed in the benchmark; C† gives the unconditional sign."
- **Objection 2 (continuous-time vs discrete sensitivity object).** "Is liquidity-sensitivity $\partial_\kappa$ (discrete) or $\partial/\partial\bar\lambda$ (continuous)? They must be shown to be the same comparative static under R2." **Required fix:** state the sensitivity object in continuous-time form ($\bar\lambda=\lambda(0,0)$) as primary and recover $\partial_\kappa$ via R2 in the limit; prove they co-move (monotone $\Xi$).
- **Objection 3 (jump at $\tau_D$ / well-posedness).** The premium process has a jump in its informational regime at $\tau_D$. A referee will worry about existence/optimality of the activist's strategy *across* the disclosure boundary (the post-$\tau_D$ continuation changes her trading incentive, feeding back pre-$\tau_D$). **Required fix:** this is genuinely subtle and is handled by T4 (free-boundary/verification). T2 in the benchmark *assumes* the pre-$\tau_D$ regime is Back-CDF up to $\tau_D$ with a value-matching condition at the boundary; the full free-boundary existence is T4's job and is currently a verification theorem, not a constructive proof.
- **Current confidence: 0.62 (conditional sign under C†); 0.45 (unconditional sign in full model).** This is the paper's contribution and also its largest open risk. The conditional-variance packaging plus C† is the honest, defensible version.

---

### T3 — Premium-hump (SUPPORTING)

**Informal statement.** The expected minority takeover premium is **single-peaked** (hump-shaped) in liquidity: low liquidity ⇒ informative order flow ⇒ inferred activism deters bids and suppresses voice; high liquidity ⇒ exit is cheap ⇒ engagement incentives collapse; the peak is at intermediate liquidity where voice is both incentive-compatible and partially concealed. In the benchmark this recovers the static $\Delta^{\min}(\kappa)$ with interior peak and endpoint symmetry $\Delta^{\min}(0^+)=\Delta^{\min}(1^-)$.

**Formal statement.** $\Delta^{\min}_{\mathrm{joint}}(\kappa)$ is continuous on $(0,1)$, with $\Delta^{\min}(0^+)=\Delta^{\min}(1^-)$ and a unique interior maximizer $\kappa^\star\in(0,1)$, recovering the static object in the $T\downarrow0$ limit (T1.iv).

**Assumptions.** T1's, plus the static D5 robustness result: the hump's interior peak survives *any* cost profile in the persuasion regime $C'(s)<\Lambda(s)$, including flat cost $\chi=0$ (`draft_v2.tex` lines 266, 268; Appendix D5). Endpoint symmetry derives from the noise law.

**Proof strategy.** In the benchmark, transport the static hump via T1.iv. The endpoint symmetry is a property of the three-point noise law at $\kappa\to0,1$; the interior peak follows from the opposing inference-deterrence and exit-cheapness forces. **Honesty:** in the *full* (non-benchmark) model the hump is currently a *numerical* comparative static, not a proved theorem — single-peakedness away from the limit is conjectural and labelled so.

**Requires-new-layer.** Needs the bidder layer (premium object) and the upstream signal (voice incentive). Back-CDF's liquidity result is a *convexity sign of $V$* via Jensen (anchor fact i), a monotone-in-convexity statement, **not** a hump in a liquidity index — they cannot generate single-peakedness in $\kappa$.

#### Referee verdict — T3
- **Overall: ACCEPT (benchmark) / ACCEPT WITH FIXES (full model).** This is supporting, not headline, so the bar is lower; but it must not be over-stated.
- **Objection 1 (uniqueness of the peak).** "Single-peakedness is asserted; in the full model it is numerical." **Required fix:** state benchmark single-peakedness as a proposition (via the limit), and the full-model hump as a numerically-verified comparative static with the static paper's D5 robustness cited. Do not claim a full-model uniqueness theorem.
- **Objection 2 (don't let the hump steal the headline).** A referee may say "the hump is the EGJ-style result; what's new?" **Required fix:** keep T3 explicitly *supporting* and route all novelty claims through T2. The hump's role is to show the benchmark reproduces the established economics; the contribution is the *attenuation of* that hump's liquidity channel by disclosure.
- **Current confidence: 0.78 (benchmark); 0.60 (full-model single-peakedness).**

---

### T4 — Free-boundary / verification theorem for the joint model

**Informal statement.** The joint model with the disclosure stopping time $\tau_D$ and the Poisson bidder admits a verification theorem: a value function $J$ satisfying the HJB with the inconspicuous-trading condition on $\{t<\tau_D\}$, a value-matching/smooth-pasting condition at the free boundary $\tau_D$, and the bidder's Poisson generator term, certifies the candidate strategy as optimal. This is the "elegance without closed form" fallback mandated by the locked design — it makes the joint model rigorous even where T2's full-model sign is only numerical.

**Formal statement (schematic).** There exist $J$ and a stopping/trading strategy such that on $\{t<\tau_D\}$: $-P+J_x+J_y=0$ and $J_t+\tfrac12\sigma^2 J_{yy}+\mathcal A^{\text{bid}}J=0$ (Back-CDF HJB + Poisson generator $\mathcal A^{\text{bid}}$), with value-matching $J(\tau_D^-,\cdot)=J^{\text{obs}}(\tau_D,\cdot)$ at the disclosure boundary; the strategy attaining $J$ is optimal.

**Assumptions.** T1's; plus regularity of the free boundary (smoothness/transversality at $\tau_D$), and integrability of the Poisson-compensated premium.

**Proof strategy.** Extend Back-CDF's App. B verification by (a) adding the Poisson generator term for the constant-intensity bidder, (b) imposing value-matching at the disclosure free boundary, (c) checking the transversality/no-arbitrage condition across the regime switch. **Honesty:** this is a *verification* theorem (sufficiency given a candidate), not a *constructive existence* proof; constructive existence with the free boundary is flagged conjectural.

**Requires-new-layer.** The free boundary at $\tau_D$ and the Poisson term are new (layers 2, 3). Back-CDF's verification has neither.

#### Referee verdict — T4
- **Overall: ACCEPT WITH FIXES.** Verification theorems are standard and credible; the risk is the free boundary.
- **Objection 1 (existence vs verification).** "A verification theorem assumes a candidate exists. Where is existence?" **Required fix:** be explicit that T4 is sufficiency; cite the benchmark (T1) as the regime where a candidate is constructed in closed form; flag full-model constructive existence as open.
- **Objection 2 (smooth-pasting at $\tau_D$).** The value can have a kink at the disclosure boundary (regime switch in information). **Required fix:** state value-matching (continuity of $J$) as the boundary condition and *check* whether smooth-pasting ($C^1$) holds or whether only $C^0$ matching is available; do not assert smooth-pasting without verifying it.
- **Current confidence: 0.55.** Standard machinery, but the free boundary + jump make this the most technically demanding theorem; it is the insurance policy for T2.

---

## 5. Consolidated assumption ledger, C†, and cross-theorem consistency

### 5.1 Assumption ledger

| ID | Statement | Status | Used by | Risk |
|---|---|---|---|---|
| A0 | Static primitives (Gaussian fundamental, 3-point noise law indexed by $\kappa$, stake-triggered disclosure) | CLEAR (inherited from `draft_v2.tex`) | T1–T4 | low |
| A1 | Interior, weakly-ordered cutoffs $k_1\le k_0\le k_D$ | CLEAR (static A1) | T1, T3 | low |
| A2 | Engagement cost $C(s)>0$, monotone (persuasion regime); flat $\chi=0$ admissible | CLEAR (static A2, D5) | T1, T3 | low |
| A3 | Premium wedge $\tilde m>m_0$ from Nash bargaining, $\theta\in(0,1)$ | CLEAR (static `thm:bg-A3`, line 284) | T2, T3 | low |
| A4 | Bidder-entry bounds + price-feedback non-explosiveness $\delta\sup|\partial p/\partial P|<1$ | CLEAR (static A4–A5) | T1–T4 | low |
| R1 | Back-CDF information structure ($C$ l.s.c. superlinear; $V=G'$) | CLEAR (Back-CDF eqs. 1–3) | T1–T4 | low |
| **R2** | Liquidity bijection $\Xi:[0,\infty)\to(0,1)$ mapping SNR $\to\kappa$ | **ASSUMED (functional form)** | T1, T2 | **medium — fix: prove $\Xi$-shape-invariance** |
| **R3** | Equilibrium-selection convergence as $T\downarrow0$ | **ASSUMED (load-bearing gap)** | T1.iv | **medium-high — the static-paper-as-limit hinge** |
| R4 | Lemma U: $s$ acts only through scalar $x^*(s)$ | CLEAR by construction (D0.1) | T1–T4 | low (but forbids self-learning from flow) |
| D1 | $\tau_D$ stochastically decreasing in $\theta_D$ | CLEAR (definition of $\tau_D$) | T2 | low |
| D2 | Observed-regime premium does not load on $\Sigma(t)$ | CLEAR (definitional: stake public post-disclosure) | T2 | low |
| **C†** | (below) | **TRANSPARENT PRIMITIVE SUFFICIENT CONDITION** | T2 (unconditional sign) | **the headline's sign hinges here** |

### 5.2 The C-dagger condition (C†)

**C† (one transparent primitive sufficient condition for the unconditional disclosure-attenuation sign).**

> *The marginal value of activism $V=G'$ is **convex** (equivalently, the activism cost $C$ is such that $G'''\ge0$ on the relevant range), AND the appropriability coefficient $\lambda_{\mathrm{app}}$ in the premium wedge is constant in the stake.*

**Why this is the right C†.** Convexity of $V$ is exactly the "economically natural" case Back-CDF single out (anchor fact i; their footnote 19, p. 1442: $V'$ cannot be concave because it is nonnegative hence bounded below). Under convex $V$, the inferred-premium branch's liquidity loading is monotone in $\Sigma(t)$, which bounds the offsetting selection effect (Objection 1 to T2): the high-$X$ paths that disclose early carry *more* value but the convexity makes the inferred premium's $\kappa$-sensitivity dominate the composition shift cleanly. Constant $\lambda_{\mathrm{app}}$ removes a second-order interaction between the wedge and the disclosed stake. **Under C†, T2's sign is unconditional.** Absent C†, T2 is signed numerically in the benchmark and stated as the leading comparative static. C† is *one* condition, *primitive* (a property of the cost technology $C$ and one bargaining coefficient), and *transparent* — exactly what the locked design demands.

**Honesty note.** C† is *sufficient, not necessary*. It mirrors the static paper's own D5 logic (sufficient-but-not-necessary cost conditions, `draft_v2.tex` line 266). It must not be sold as "the" condition.

### 5.3 Cross-theorem consistency notes

- **R3 is the single shared hinge.** T1.iv, and hence the "static-paper-as-special-case" framing, depend on R3. If R3 fails, the static paper is still a *closely related* model but not a literal limit — the framing weakens from "special case" to "discrete analog." Mitigation: numerical convergence study; honest labelling.
- **C† vs R2.** C† concerns the cost technology; R2 concerns the liquidity index. They are independent. The $\Xi$-shape-invariance fix (Referee Obj. 2 to T1) must be proved *before* C† is invoked, so the headline does not silently inherit an $\Xi$-shape dependence.
- **T2 ↔ T4.** T2's well-posedness across $\tau_D$ (Referee Obj. 3) is discharged by T4. T4 is the insurance: if the full-model sign in T2 stays numerical, T4 still delivers a rigorous joint-model verification theorem, so the paper has a theorem even in the worst case.
- **Benchmark consistency.** All four theorems reduce, at $T\downarrow0$ under R2–R3, to objects in `draft_v2.tex`. This is the internal-consistency check: every benchmark claim must match a labelled static result (T1↔fixed point; T2↔abstract line 97; T3↔$\Delta^{\min}$ + D5; T4↔static existence via Brouwer, line 372).

---

## 6. Positioning & scooping-insulation

### 6.1 What each competitor owns and provably cannot generate

- **Back-CDF (2018, Econometrica).** *Owns:* the canonical closed-form continuous-time activist-trading model; the sign-ambiguous liquidity-efficiency result governed by convexity of $V$; bidirectional liquidity-activism feedback. *Cannot generate:* (i) stake is never disclosed (anonymity window, not a hitting time); (ii) no takeover/premium object; (iii) liquidity-efficiency is a convexity sign, not a disclosure comparative static — they cannot produce "stricter disclosure ⇒ premium less liquidity-sensitive" because the premium does not exist; (iv) no four-action menu, no two-branch inference split, no 13D-threshold comparative static. *They explicitly invite the disclosure extension* (§8, p. 1454, item 1) — we answer it.
- **EGJ (2015).** *Owns:* discrete order-flow model with price-feedback into takeover decisions; tractable Bayesian price fixed points. *Cannot generate:* exogenous-information blockholder who does not choose a governance mode; no stake acquisition ⇒ no threshold-crossing ⇒ no disclosure split; no endogenous voice ⇒ no liquidity-premium nonmonotonicity and no attenuation (confirmed `draft_v2.tex` line 134).
- **OCB (2022, JFQA).** *Owns:* normative disclosure-threshold-*level* design (adverse-selection vs disciplining-benefit tradeoff). *Cannot generate:* no continuous-time order-flow market-maker fixed point ⇒ no inferred-vs-observed premium; no bidder-entry channel ⇒ no liquidity-sensitivity of premia; no four-action menu.
- **Cetemen–Cisternas–Kolb–Viswanathan (multi-activist timing).** *Owns:* leader-follower activist timing. *Cannot generate:* no disclosure threshold, no bidder layer, no static-paper limit.

### 6.2 Three orthogonal differentiation dimensions

Track B is orthogonal in three *independent* dimensions, none reachable by varying a competitor's parameters: (1) a **stake-hitting disclosure layer** $\tau_D$ that partitions inference into liquidity-sensitive (pre) and liquidity-insensitive (post) branches; (2) a **Poisson bidder + Nash-bargaining premium**; (3) the **headline (T2)** generated *only* by the interaction of (1) and (2) with the inherited filter. The static `draft_v2.tex` becomes the Section-2 sharp benchmark.

### 6.3 Scooping insulation

- **Answer the open question first, by name.** Frame the abstract and intro around Back-CDF §8 item 1 (13D horizon, named). Whoever scoops must also answer that question; we plant the flag with the disclosure-attenuation headline.
- **The headline is a *negative-interaction* result** (disclosure *attenuates* a sensitivity), not just "another comparative static." It is harder to stumble into and easy to attribute.
- **Benchmark-first packaging** means even a partial scoop of the headline leaves the closed-form benchmark + static-paper-as-special-case contribution intact.
- **The C† condition** ties the unconditional sign to the convexity of $V$ — Back-CDF's own object — making the result legible as a *direct extension* of the canonical model, which strengthens the citation moat.

---

## 7. Phased writing plan (~10–12 months)

| Phase | Months | Deliverable | Exit criterion |
|---|---|---|---|
| **P1 — Benchmark + Lemma U + T1(i)–(iii)** | 1–3 | Pre-disclosure closed form transported from Back-CDF under scalar-target reduction; Lemma U proved; numerical filter check | T1(i)–(iii) written + a working numerical solver reproducing $\Sigma(t)=(T-t)a^2/T$ and martingale $\lambda$ |
| **P2 — Degeneration T1(iv) + R2 $\Xi$-invariance + T3 benchmark** | 3–6 | The static-paper-as-limit theorem; $\Xi$-shape-invariance lemma; benchmark hump | T1(iv) reduces cell-by-cell to `draft_v2.tex` fixed point in a numerical convergence study; T3 benchmark proposition |
| **P3 — Headline T2 + C† + T4 verification** | 6–10 | Conditional-variance packaging of attenuation; C† derived; free-boundary verification | T2 signed unconditionally under C† and numerically in benchmark; T4 verification theorem with value-matching at $\tau_D$ |
| **P4 — Full-model robustness + writeup + adversarial pass** | 10–12 | Full-model numerical T2/T3; intro/positioning; internal referee pass on every theorem | every theorem has a green/amber/red confidence tag; no red on T1/T2 headline statements; honesty labels in place |

**Critical path:** P1 (Lemma U + closed-form transport) → P2 (degeneration, the R3 hinge) → P3 (T2 + C†). T4 runs *parallel* to P3 as insurance. The single most fragile link is **P2's R3** (selection convergence) and **P3's C†** (the unconditional sign).

**First concrete next step (do this first).** Write and verify **Lemma U** plus a minimal numerical harness that (a) instantiates the scalar-target map $x^*(s)$ from the existing static solver (`numerical/solver.py`, the cutoff system), and (b) checks the Back-CDF Riccati closed form $\Sigma(t)=(T-t)a^2/T$ numerically against the ODE integrator. This is low-risk, validates the D0.1 resolution operationally, and produces the figure for T1(ii). It touches only new files; it does **not** modify `draft_v2.tex` or the static model.

---

## 8. Risk register

| Risk | Theorem(s) | Severity | Likelihood | Mitigation |
|---|---|---|---|---|
| **Closed-form failure in full model** (free boundary breaks Back-CDF closed form) | T2 (full), T4 | high | medium | Locked design permits no closed form: fall back to (a) conditional-variance/Kallianpur packaging of T2, (b) sharp closed-form *benchmark* only, (c) T4 verification theorem, (d) C†. The benchmark contribution survives regardless. |
| **Jump / existence subtlety at $\tau_D$** (strategy optimality across the regime switch; smooth-pasting may fail, only $C^0$ matching) | T2 (Obj. 3), T4 | high | medium-high | T4 verification with *value-matching* (not assuming smooth-pasting); flag constructive existence as open; benchmark handles it via boundary value-matching. Do not assert $C^1$ pasting unverified. |
| **R3 selection-convergence gap** (static paper not a literal limit) | T1.iv framing | medium | medium | Numerical convergence study; honest re-label "special case" → "discrete analog" if R3 unprovable; mirrors static paper's own numerical-uniqueness honesty (line 372). |
| **C† too strong / sign fails without it** (the headline's unconditional sign collapses) | T2 (headline) | high | medium | Present unconditional sign *only under C†*; numerical sign in benchmark otherwise; never overclaim. C† is sufficient-not-necessary (mirrors static D5). |
| **R2 $\Xi$-shape dependence** (headline an artifact of chosen $\Xi$) | T1, T2 | medium | low-medium | Prove $\Xi$-shape-invariance lemma in P2 *before* invoking C†; use only monotonicity + endpoints. |
| **Scooping** (someone else answers Back-CDF §8 item 1) | all | medium | low-medium | Plant flag now: frame around the named open question; headline is a negative-interaction result (harder to stumble into); benchmark-first packaging is partially scoop-proof. |
| **Clock / JMP timeline** (12 months is tight for a free-boundary theorem) | T4, P3 | medium | medium | T4 is *insurance*, runs parallel; if it slips, the paper still has T1 (benchmark) + T2 (conditional-variance form + C†) + T3. Prioritize benchmark + headline-under-C† over full-model generality. |
| **Over-claiming the headline** (referee reads T2 as unconditional) | T2 | fatal-if-realized | low (with discipline) | Strict honesty labels; verdict subsections kept in the paper's internal notes; never state T2's full-model sign as a theorem. A wrong JMP theorem is fatal; an honest open item is fine. |

---

## Appendix — confidence summary (author-facing)

| Theorem | Benchmark confidence | Full-model confidence | Verdict |
|---|---|---|---|
| T1 (closed form + special case) | 0.90 | — | ACCEPT WITH FIXES (R3, R2-shape) |
| **T2 (headline, disclosure-attenuation)** | **0.75 (under C†)** | **0.45 (unconditional)** | **ACCEPT WITH FIXES under C†; REJECT if asserted unconditionally** |
| T3 (premium-hump, supporting) | 0.78 | 0.60 | ACCEPT (benchmark) / WITH FIXES (full) |
| T4 (free-boundary verification) | 0.55 | 0.55 | ACCEPT WITH FIXES (existence is open; verify value-matching) |

---

## 9. Completeness review — gaps to close BEFORE drafting (adversarial pass)

> This section is the output of an independent completeness critic run *after* §1–§8 were written. It is intentionally harsh and is not reconciled into the optimistic prose above. **Resolve §9.1 first — it is the document's central unaddressed problem.**

### 9.1 The framing contradiction (must resolve first)

The doc claims **both** (a) the static paper is a *literal special case* of the joint benchmark (T1.iv, $T\downarrow0$ limit), **and** (b) the disclosure-attenuation result T2 is a *hard new headline* at confidence 0.45 unconditional. These cannot both hold. The static paper **already proves disclosure-attenuation** as `prop:disclosure-attenuation` ("Disclosure Attenuation (Partial Equilibrium)", `draft_v2.tex` line 962) and brands it "the central result" (abstract line 84, intro line 134). So either T2 is *inherited* (it is the limit of an already-proven static proposition, hence not new), or T1.iv is *false* (the static result is not recoverable as a limit). **The honest resolution:** the static attenuation is *partial-equilibrium and discrete*; the genuinely new content must be the **continuous-time, full-equilibrium, free-boundary version with $\tau_D$ a true stopping time and endogenous accumulation** — and the doc must state *precisely what the continuum buys that the static proposition does not* (reweighting probability mass across an endogenous hitting time; the $\theta_D$ cross-partial as a continuous object). Until this is on paper, the stack has no defensible novelty claim.

### 9.2 The single biggest hole: no welfare/planner theorem for $\theta_D$

The stack (T1–T4, C†) contains **zero welfare content**. The static paper *already has* a disclosure-threshold planner (`sec:welf-kD`), signs the wedge $\kappa^\ast-\kappa^\dagger$ (`prop:planner-wedge`), and characterizes **underdisclosure** against a first-best benchmark (`sec:welf-fb`). A continuous-time joint model that drops the welfare analysis the static paper already proves is a **strict regression**, and it cedes the normative high ground to OCB (2022) — who own the optimal-threshold question but have *no* takeover feedback, exactly where Track B could dominate. **Add a T5: continuous-time optimal-$\theta_D$ / planner theorem** (the social value of moving probability mass across $\tau_D$; sign whether the privately-chosen disclosure crossing is socially under- or over-used).

### 9.3 C† is currently a hope dressed as a sufficient condition

C† ("$V$ convex AND $\lambda_{\mathrm{app}}$ constant") is *asserted* to bound the offsetting selection effect in T2, but §5.2 gives **no derivation** — no Jensen step, no inequality, no bound. "Convexity makes the inferred premium's $\kappa$-sensitivity dominate the composition shift cleanly" is hand-waving. Worse, C† **may duplicate or conflict with** the static paper's existing condition **(C\*)** (secant-concavity of $h$, `draft_v2.tex` line 840), which plays the identical sign-the-result role. Convex-$V$ vs secant-concave-$h$ are opposite curvature words on different objects. **Fix:** either derive C† (produce the actual inequality), or adopt (C\*) directly and prove C† reduces to it in the limit. Inventing a second transparent condition that contradicts your own paper's reads as not having read your own paper.

### 9.4 The $\theta_D$ (stake) vs $k_D$ (signal) type mismatch

T1.iv claims the static cutoff $k_D$ — a **signal** cutoff (threshold on $s$, `eq:kD`) — is recovered in the limit, while $\tau_D=\inf\{t:X_t\ge\theta_D\}$ uses $\theta_D$ as a **cumulative-stake** level. These are different mathematical objects; there is no lemma mapping $\theta_D\leftrightarrow k_D$. Without it the "static = special case" claim is **not even type-correct**, and the static welfare section (which sets $k_D$ as the disclosure control) does not connect to $\theta_D$. **Fix:** an explicit limit lemma mapping the stake-hitting threshold to the signal cutoff as $T\downarrow0$.

### 9.5 The Gaussian-vs-3-point prior gap (deepest technical risk, sits under the headline)

The Back-CDF closed form $\Sigma(t)=(T-t)a^2/T$ requires a **Gaussian** latent. The target $x^*(s)$ is a **3-point** step variable $\{0,1,2\}$ treated as $\mathcal N(\mu_x,\sigma_x^2)$ for the filter. With a genuine 3-point prior the conditional law is a finite mixture and the Kalman–Bucy filter is **not** closed-form — the entire "sharp closed form" (and the martingale $\lambda$, and T1(i)–(iii)) collapses. **Fix:** either (a) prove the filtered objects are invariant to the Gaussian-vs-3-point prior, or (b) honestly restrict T1's closed form to a genuinely Gaussian target (which then weakens the exact link to the discrete static partition). Currently a substitution with no error control.

### 9.6 D1 is asserted falsely for endogenous trading

D1 ("$\tau_D$ stochastically decreasing in $\theta_D$") is called "immediate from the definition and a.s. continuity of $X$." This is **false for endogenous $X$**: lowering $\theta_D$ changes the activist's optimal accumulation policy (she may slow down to avoid early disclosure), so the path is not held fixed. D1 is the **engine of the headline** and must be *proven* for the equilibrium accumulation path, not asserted from the hitting-time definition. (Related: D2 — "observed-regime premium does not load on $\Sigma(t)$" — is called definitional but depends on the bidder's information set at $\tau_D$, which is not specified. D2 is the linchpin of the mechanism and is currently assumed, not modeled.)

### 9.7 The constant-$\lambda$ benchmark may kill the hump and the cross-partial

The benchmark fixes bidder intensity **constant**, but the locked design has intensity $\lambda(P)$ **decreasing in price**, and that price-responsiveness is the bid-incidence force generating the static hump. Constant intensity may remove one of the two opposing forces T3 (hump) and T2 (attenuation cross-partial) rely on — i.e. **the benchmark may not even produce a hump.** Stress-test whether T2/T3 survive constant $\lambda$; if not, the benchmark must use $\lambda(P)$ from the start. (Also: the price-impact Kyle-$\lambda(t,y)$ and the bidder intensity $\lambda$ are both written "$\lambda$" and must be disambiguated in every formal statement.)

### 9.8 Internal inconsistency in the D0.1 resolution itself

The hybrid's Lemma U says $s$ is "fully consumed upstream at $t=0$" and the maker filters *only* the scalar target $X_0$ whose law it already knows. But T2's mechanism requires a *rich pre-$\tau_D$ inference channel* carrying liquidity sensitivity. **If the only thing in the flow is a scalar whose law is known, what is being "inferred" that is liquidity-sensitive?** R4 (scalar already-summarized target) and T2 (rich inferred premium) pull in opposite directions; reconcile how a one-dimensional consumed signal still produces a liquidity-sensitive inferred premium.

### 9.9 Missing existence theorem + missing competitor positioning

- **No equilibrium-existence theorem for the joint model.** T4 is *verification* (sufficiency) only and punts existence; the static paper proves existence unconditionally via Brouwer (`prop:existence`, line 610). The headline rests on an equilibrium nobody has shown exists. Add a fixed-point existence statement for the combined trading + disclosure-stopping + bidder-entry game.
- **Positioning omits the canonical liquidity-governance papers** that are *in `lit/`*: **Maug (1998)**, **Kahn–Winton (1998)**, **Edmans–Fang–Zur (2013)**, **Corum–Levit (2019)**. Since the hump (T3) is precisely a liquidity-governance nonmonotonicity, their absence is a hole a referee will hit. Also unaddressed: the obvious one-step scoop (a continuous-time Back-CDF + 13D threshold *without* the four-action menu) — the orthogonality argument defends against competitors used as-is, not against the extension a competitor would actually attempt.

### 9.10 Prioritized pre-drafting checklist (from the critic)

1. **Resolve the §9.1 framing contradiction** (PE-discrete static vs full-eq-continuous-stopping-time new content). Nothing else matters until this is settled.
2. **Add T5: continuous-time $\theta_D$ planner theorem** (§9.2) — port and strengthen the static welfare section; this is the move that beats OCB.
3. **Reconcile C† with the static (C\*)** (§9.3) — derive the inequality or adopt (C\*) and show reduction.
4. **Prove the $\theta_D\leftrightarrow k_D$ limit lemma** (§9.4) — without it "special case" is not type-correct.
5. **Resolve Gaussian-vs-3-point** (§9.5) before claiming any closed form.
6. **Prove D1 for the equilibrium path** (§9.6) — the engine of the headline.
7. **Stress-test the constant-$\lambda$ benchmark** (§9.7) — confirm it still yields the hump and cross-partial; disambiguate the two $\lambda$'s.
8. **Reconcile Lemma U with T2's inference channel** (§9.8).
9. **Add joint-model existence** (§9.9) and **position against Maug / Kahn–Winton / Edmans–Fang–Zur / Corum–Levit**.
10. **Resolve the $\Lambda$ (SNR) vs $\Lambda(s)$ (value-slope) notation collision** before any cross-referencing draft.

**Honest net assessment.** The headline is *defensible only in its conditional form* — the conditional-variance/Kallianpur packaging signed under a properly-derived C†, with the unconditional sign left numerical (mirroring the static paper's own (C\*)+Hypothesis discipline). The two structural risks that could sink Track B are **§9.1 (framing/novelty)** and **§9.5 (Gaussian-vs-3-point under the closed form)**; the biggest *value-add opportunity* missed is **§9.2 (the welfare theorem)**. None of these is fatal; all are addressable in P1–P2 before committing to the writeup.
