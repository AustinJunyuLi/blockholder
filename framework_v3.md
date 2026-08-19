# Framework v3.1 — Repositioning "Liquidity, Activism Disclosure, and Takeover Premia" (revised after referee round)

**Date:** 2026-08-19 · **Status:** for owner approval (Stage 2 deliverable, revised; editing `draft_v2.tex` waits for sign-off)
**Evidence base:** 9 literature briefs + draft digest + empirical feasibility audit in `research/`; referee round of 2026-08-19 (5 referee agents + 3 verifiers + orchestrator checks) in `research/review_v3/` and `quality_reports/reports/2026-08-19_framework_v3_referee_report.md`. This `.md` mirrors `framework_v3.qmd` / `framework_v3.pdf` (the rendered PDF is canonical). The pre-review v3 text is archived at `quality_reports/rewrites/framework_v3_pre-review_2026-08-19.qmd`.

---

# The Angle {#sec-angle}

## The repositioning in one paragraph

Move from *"a static microstructure model of the exit–voice margin with numerically verified
comparative statics"* to **"the 13D disclosure rule as a policy lever on revelatory price
efficiency in the market for corporate control."** The disclosure rule — its threshold and its
filing window — splits market inference about activism into a *disclosed* branch (engagement is
common knowledge) and an *inferred* branch (engagement must be read from order flow), and a
potential bidder prices the takeover off both. Pre-disclosure accumulation under a *fixed*
disclosure horizon is well understood (Kyle and Vila 1991; Back, Collin-Dufresne, Fos, Li and
Ljungqvist 2018, *Econometrica*; Cetemen, Cisternas, Kolb and Viswanathan 2026, *JF*), as is
post-disclosure intervention choice *given* a toehold (Burkart and Lee 2022, *RFS*). What no paper
does — theoretically or structurally — is make the disclosure *rule* the state variable that
determines how liquidity maps into the takeover premium: Ordóñez-Calafi and Bernhardt (2022,
*JFQA*) design the threshold without a bidder; Cetemen et al. stop at the crossing; Albuquerque,
Fos and Schroth (2022), Johnson and Swem (2021) and Celentano and Levine (2025) estimate activism
outcomes with no order-flow inference; Corum (2025) has liquidity and regulation but no premium.
The empirical literature links liquidity to premia in reduced form (Massa and Xu 2013, *JFQA*;
Huang, Maharjan and Nanda 2024, *JCF*) and the theory literature links liquidity to the *mode* of
intervention (Maug 1998; Mello and Repullo 2004, "Shareholder Activism is Non-Monotonic in Market
Liquidity"). We are the first to make the rule the partition and to price the premium off it.

*(v3.1: the v3 sentences "the first formalization of how the market learns about activism-driven
control events" and "Nobody … links market liquidity or the disclosure rule to takeover premia" were
overclaims — see the referee report, §2 — and are replaced by the paragraph above.)*

## Why this angle wins

1. **The gap is quotable, verbatim.** Back et al. (2018, p. 1454): "we assume that the horizon at
   which the activist's stake is disclosed is fixed and common knowledge … it might be interesting
   to endogenize the horizon" (the 5% threshold is the institutional context). Burkart and Lee
   (2022, p. 1891): "we do not endogenize the acquisition of the toehold in anonymous,
   predisclosure markets … We leave an analysis of how predisclosure and post-disclosure decisions
   interact to future work." Note the sentence in between — the toehold problem "has been
   comprehensively studied by Back et al. (2018)" — which is why our claim is the *partition and the
   rule*, not market learning per se.
2. **Frontier taste.** The closest recent top-3 theory papers (Burkart–Lee RFS 2022;
   Levit–Malenko–Maug JF 2024 and JF 2026; Kakhbod–Loginova–Malenko–Malenko RFS 2023;
   Burkart–Lee–Voss, ECGI WP 956/2024, 2025 ECGI prize; Corum–Levit JFE 2019) are analytical and
   one-mechanism; most, not all, close with an empirical-implications section (Burkart–Lee ends
   on concluding remarks). Levit–Malenko–Maug (2024) price shares off the marginal shareholder with
   Walrasian clearing — a published precedent that a non-Kyle trading technology is acceptable, not
   a "proof" of it. Brouwer existence plus honestly labeled numerical uniqueness is acceptable
   *only if the headline comparative statics are proved* — which Section 3 treats as the binding
   constraint, not a formality.
3. **The policy hook is live — and the first-stage fact is already public.** The SEC's
   Modernization of Beneficial Ownership Reporting (Rel. 33-11253; adopted October 10, 2023;
   effective **February 5, 2024**) shortened the initial 13D window from 10 calendar days to 5
   business days. Trivedi (SSRN 6866499, June 2026) already runs a pre-registered
   difference-in-differences on this change (13G filers as control): +0.35 in the share filed
   within five business days, with nulls on mean lag, bid–ask spread and an illiquidity proxy.
   Polk, Buchheit, Riley and Stone ("Shrinking the 13D disclosure window will benefit non-activist
   investors", *J. Financial Regulation and Compliance* 32(4):516–538, 2024) measure delay-period
   abnormal returns on pre-2024 data and project the effect of the shorter window.
   Corum (2025, SSRN 4319599, "The Stick or the Carrot?") theorizes liquidity, regulation and
   activist short-termism (no premium). Bishop, Fos, Jiang and Partnoy (2026, SSRN 6061814) show
   activists avoid targets where a toehold would trigger HSR disclosure before the 13D. None has a
   takeover-premium object or the deadline as a lever on inference; the triple *deadline ×
   liquidity × equilibrium premium* is open. Treat the window as ~12 months, not "open but closing".
4. **Differentiation from the most dangerous competitor.** Celentano and Levine (2025, R&R at *RFS*
   per the authors' CV, dated Oct. 2025) estimate activism's equilibrium effect on M&A with **no
   order-flow inference and no price impact** — liquidity enters only as a reduced-form entry cost —
   and a stake fixed at the 5% statutory threshold. One sentence on page 1: *they take prices as
   given; we make liquidity and the disclosure rule the state variables, and the takeover premium an
   equilibrium object of order-flow inference and tender free-riding.*

## Framing device

Following Bond, Edmans and Goldstein (2012, *ARFE*) and Goldstein (2023, *Review of Finance*), the
paper studies **revelatory** price efficiency (RPE) — what the price reveals to a specific
decision-maker, the bidder — rather than forecasting efficiency. A disclosure *rule* is a policy
lever on RPE. Goldstein (2023, §5.2) lists RPE-oriented measurement as an open problem; the
feedback–corporate-control interaction is Edmans, Goldstein and Jiang (2012, *JF*), whose discrete
order-flow technology (EGJ 2015, *AER*) is the methodological precedent — with the caveat that EGJ
prove uniqueness *analytically over parameter regions* (AER Prop. 1); we adopt their region-wise
posture, not a "numerical uniqueness following EGJ" (draft_v2 l. 702, 2235 must be rewritten).

# The Simplified Model {#sec-model}

## Notation (new in v3.1)

$v$ firm value; $s = v + \varepsilon$ the blockholder's signal with $\sigma_s^2 = \sigma_v^2 +
\sigma_\varepsilon^2$; $(q,a)$ order and engagement; $z$ noise order; $X = q + z$; $D$ disclosure
flag; $\kappa$ noise intensity; $C(s)$ engagement cost, strictly positive and decreasing (A2);
$\Delta_{\mathrm{eng}}$ the value improvement from engagement, $\rho$ its success probability,
$\tilde\Delta = \rho\Delta_{\mathrm{eng}}$; realized bid premium $m^R(a)$ with $m^R(0) = m_0$,
$m^R(1) = m_1$, and $\tilde m = \mathbb{E}[m^R(1)] \le m_1$; $\bar m(X,D) = m_0 + \pi(X,D)(\tilde m -
m_0)$ the expected premium; $\pi(X,D) = \Pr(a = 1 \mid X, D)$; $\omega_E, \omega_H, \omega_Q,
\omega_P$ ex-ante region masses; $h(\pi) = \pi\, p(\pi)$; $\bar p_1$ the disclosed-branch bid
probability; $\bar S, K, \sigma_\xi$ the bidder's synergy scale, entry cost and synergy dispersion;
$\Delta^{\min} = \mathbb{E}[m^R(a)\mathbf 1\{\text{bid}\}]$ expected minority takeover gains,
$\Delta^{\mathrm{act}} = (\tilde m - m_0)\Pr(a = 1, \text{bid})$ its activism component; D7 tender
game: $r$ fringe-raid probability, $\gamma$ portability, $\phi$ dilution ($\varphi$ is the normal
density in D7), $\psi$ pivotality factor, $\lambda$ appropriability. (v3 mislabeled the dilution and
pivotality symbols and overloaded $q$; fixed.)

## Players, timing, and information

All players are risk neutral. There is one blockholder ($B$), one noise trader, one competitive
market maker ($M$), and one potential bidder.

- **$t=0$.** Nature draws firm value $v \sim \mathcal{N}(\mu_v, \sigma_v^2)$. The blockholder
  privately observes $s = v + \varepsilon$, $\varepsilon \sim \mathcal{N}(0, \sigma_\varepsilon^2)$,
  and holds an initial stake normalized to one share.
- **$t=1$ (trade and disclose).** The blockholder chooses an action $(q, a)$ from the
  three-branch menu
  $$
  (q, a) \in \{ \underbrace{(-1, 0)}_{\text{Exit}},\; \underbrace{(0, 1)}_{\text{Quiet}},\;
  \underbrace{(+1, 1)}_{\text{Public}} \},
  $$
  where $q$ is the order and $a \in \{0,1\}$ engagement. The four-branch menu of draft_v2 is pruned
  under **(A2$'$)**: the engagement net benefit dominates the cost on the whole non-exit region,
  $A(Q) - A(H) \ge C(s)$ for all $s \ge k_1$ (equivalently $C(k_1) \le A(Q) - A(H)$ given (A2)), so
  Quiet weakly dominates Hold and the menu is $\{E, Q, P\}$. *(v3 said "Hold folds into the trading
  decision; it collapses at baseline anyway": the collapse is a baseline numerical fact — draft_v2
  l. 1010; the text after Prop. cutoffs says the region "may collapse" — not a theorem. The prune sets $\bar\pi = \omega_Q/(\omega_H + \omega_Q) \equiv 1$,
  which makes the chord condition (C\*) a genuinely primitive inequality, $h(1) < 2h(1/2)$; the
  baseline numerics must be re-solved on the three-branch model before any D8 number is
  re-quoted.)* Noise demand $z \in \{-1, 0, +1\}$ with
  $$
  \Pr(z = 0) = 1 - \kappa, \qquad \Pr(z = +1) = \Pr(z = -1) = \tfrac{\kappa}{2},
  $$
  so $\kappa \in [0,1]$ is the liquidity/noise intensity. The market maker observes total order
  flow $X = q + z \in \{-2, \dots, +2\}$ and the disclosure flag $D$ (defined in §2.3), and sets
  $$
  P(X, D) = \delta\, \mathbb{E}[Y \mid X, D],
  $$
  with $\delta$ a normalization. *(v3.1: draft_v2 uses $\delta = 0.95$ in §5 and
  `numerical/params.py`, and $\delta = 1$ in the transfer-netting lemma; pick one and, if $\delta =
  1$, redo the (A5a) margin arithmetic.)*
- **$t=1.5$ (bidder entry).** The bidder observes $(P, D)$ and a private synergy shock
  $\xi \sim \mathcal{N}(0, \sigma_\xi^2)$, and enters iff
  $$
  \Pi_B = \bar{S} - P + \xi - \bar{m}(P, D) - K \;\geq\; 0, \qquad \bar m(P,D) \equiv
  \mathbb{E}[m^R \mid P, D],
  $$
  so the entry probability is
  $$
  p(P, D) = \Phi\!\left( \frac{\bar{S} - P - \bar{m}(P, D) - K}{\sigma_\xi} \right),
  \qquad \frac{\partial p}{\partial P} < 0
  \quad \text{(bid monotonicity, proved at fixed } \bar m).
  $$
  Because $(P, D)$ is a sufficient statistic for the payoff-relevant pair $(\hat V, \bar m)$ — the
  three disclosed cells share one price *and* one posterior, so their pooling is payoff-irrelevant,
  and the $D = 0$ cells carry generically distinct prices — conditioning on $(P,D)$ coincides with
  conditioning on $(X,D)$. *(This replaces draft_v2's Lemma dropA7, whose "injectivity at any
  nondegenerate calibration" is contradicted by the paper's own Appendix B: $P^*(x,1)$ is identical
  for $x \in \{0,1,2\}$.)*
- **$t=2$ (payoffs).** If a bid occurs, $Y = P + m^R(a)$; otherwise $Y = v + a\tilde{\Delta}$.
  The premium wedge $m_1 > m_0$ is microfounded in the appendix tender game (D7): with fringe-raid
  probability $r$, portability $\gamma$, dilution $\phi$ and pivotality factor $\psi$,
  $$
  \lambda \;=\; 1 - r\,(1 - \gamma)\,\psi \;\in\; [0, 1] \quad \text{(proved, closed form)}.
  $$

## Disclosure strictness as a model primitive — two margins {#sec-tau}

In draft_v2 the flag is $D = \mathbf 1\{q = +1\}$ and $\omega_P = 1 - \Phi(\alpha_D)$ is an
*equilibrium mass* pinned by the cutoff $k_D$; "$\omega_P(\tau)$ with $\omega_P'(\tau) > 0$" (v3)
was therefore a relabeling, not a primitive. v3.1 makes strictness explicit and separates the two
institutional margins, because they enter the model differently and — see §3.2 — carry different
signs. (Symbol hygiene: draft_v2 already uses $\tau$ for the discount horizon, $\delta = e^{-r\tau}$,
l. 335; rename that one.)

- **Threshold margin $\tau_\theta \in [0,1]$** (5% vs 3%; who must file). A Quiet engagement is
  publicly disclosed with probability $\tau_\theta$: $D = \mathbf 1\{q = +1\} \vee \mathbf 1\{a = 1,
  \zeta \le \tau_\theta\}$, $\zeta \sim U[0,1]$ independent. Then the disclosed mass is $\omega_P +
  \tau_\theta\omega_Q$ (so $\partial/\partial\tau_\theta > 0$ genuinely), the $D=0$ masses become
  $(\omega_E, \omega_H, (1-\tau_\theta)\omega_Q)$, and the closed-form $D=0$ posteriors of Prop.
  posteriors go through with $\omega_Q \mapsto (1-\tau_\theta)\omega_Q$. Disclosed-branch
  $\kappa$-invariance survives: in both disclosed sub-blocks ($X = 1 + z$ and $X = z$),
  conditioning on $X$ reveals only the noise draw.
- **Window/timing margin $\tau_w \in [0,1]$** (10 calendar days vs 5 business days; *when* the
  market learns). The Public buy is flagged before the market maker prices it with probability
  $\tau_w$; with probability $1 - \tau_w$ it is priced from order flow alone. $\tau_w = 1$ is
  draft_v2; $\tau_w = 0$ is draft_v2's no-disclosure benchmark (§8.2 there). Back et al. (2018,
  pp. 1452–1453): "what matters is $\sigma^2 T$ … reducing the trading horizon $T$ is isomorphic to
  reducing noise trading volatility" — i.e., a shorter window also maps into **lower $\kappa$**, not
  only into higher $\tau_w$. The February 2024 shock is therefore a *joint* movement $(d\kappa < 0,
  d\tau_w > 0)$ and must be presented as one; the clean single-margin experiment is the
  cross-country threshold contrast ($\tau_\theta$).

Both margins move mass from the inferred to the disclosed branch. Only the threshold margin does so
by removing *engaged* mass from the pool the market must read; the window margin removes the *buy*
order, which is intrinsically informative ($X = +2$ is reachable only from $q = +1$) even without a
flag. This is why their comparative statics differ (§3.2).

## Equilibrium

A perfect Bayesian equilibrium consists of (i) a weakly ordered cutoff strategy $k_1 \leq k_D$
over the signal $s$ (with $k_0 = k_1$ under (A2$'$)); (ii) Bayes-consistent posteriors $\pi(X, D)$;
(iii) the bidder's entry rule; (iv) the competitive price fixed point $P = \delta\,\mathbb{E}[Y \mid
X, D]$. Existence follows from Brouwer's theorem on the cutoff polytope $\Theta$ under (A1), (A2),
(A4) **and (A5a)** — the maintained single-valuedness of the inner price fixed point on each cell,
without which the best-response map is a correspondence. (A5a) is an assumption, not a theorem: v3
called existence "unconditional", which it is not; draft_v2's own Remark A5margins (l. 696) says
the baseline *fails* the conservative sufficient bound ($0.805 + 0.947 > 1$), while §5 (l. 1010)
says it *satisfies* the (A5) sufficient condition ($\delta/\sigma_\xi = 2.375 < 2.507$) — the two
statements must be reconciled before draft_v3 says anything about (A5). Uniqueness is stated as a
labeled numerical regularity (multistart convergence), never as a theorem — the EGJ (2015) posture
of region-wise characterization rather than global uniqueness claims.

# Main Results and Proof Plan {#sec-results}

## Proved objects already in hand

The posterior block is closed form: the disclosed branch is degenerate, $\pi(X, 1) = 1$, and
$\kappa$-invariant (proved, modulo (A5a) for the inner fixed point); the inferred branch satisfies
$\pi(-2, 0) = 0$ with $\pi(X, 0)$ rational in $(\omega, \kappa)$ (proved). Bid monotonicity, the
dominance lemma pruning the action menu, and existence (as qualified above) are proved. Endpoint
symmetry
$$
\Delta^{\min}(0^{+}) \;=\; \Delta^{\min}(1^{-})
$$
is proved **at fixed cutoffs** (noise symmetry plus disjoint $D=0$ supports at $\kappa \to 1$; the
proof does not use Hold, so it survives the prune); the step that lifts it to full equilibrium
("the equilibrium indifference system is identical at the two extremes", draft_v2 l. 815–817) is
asserted and numerically checked (gap $6.9\times10^{-7}$), and must be labeled as such or proved.

## T2 — Disclosure attenuation (the headline comparative static), stated as far as it is proved

At fixed cutoffs, the activism component decomposes across the two branches as
$$
\Delta^{\mathrm{act}}(\kappa; \tau)
\;=\;
(\tilde{m} - m_0)\Big[ \omega_P^{\mathrm{disc}}(\tau)\, \bar{p}_1
\;+\; \big(1 - \omega_P^{\mathrm{disc}}(\tau)\big)\, \mathbb{E}_{D=0}\big[h(\kappa;\tau)\big] \Big],
$$
where $\bar{p}_1$ is the disclosed-branch bid incidence ($\kappa$-invariant, proved) and the
inferred-branch term carries all inference sensitivity. Hence
$$
\left| \frac{\partial \Delta^{\mathrm{act}}}{\partial \kappa} \right|
\;=\;
(\tilde{m} - m_0)\,\big(1 - \omega_P^{\mathrm{disc}}(\tau)\big)\,
\left| \frac{\partial}{\partial \kappa} \mathbb{E}_{D=0}\big[h(\kappa;\tau)\big] \right| ,
$$
and the $\tau$-derivative of the right-hand side is a **two-term** product rule: a weight term
$-\partial_\tau\omega_P^{\mathrm{disc}} \cdot |\partial_\kappa \mathbb{E}_{D=0}h| < 0$ (this is what v3
called "one line") **and** a composition term $(1-\omega_P^{\mathrm{disc}})\,\partial_\tau
|\partial_\kappa \mathbb{E}_{D=0}h|$, because the $D=0$ posteriors are homogeneous of degree zero in
$(\omega_E, \omega_H, \omega_Q)$ and therefore invariant to $\tau$ *only* under a proportional
rescaling of all three non-disclosed masses — which no disclosure rule does. The status of T2 is
therefore:

1. **Threshold margin $\tau_\theta$ — attenuation holds, a fortiori, pending one lemma.** Moving Quiet
   engagement into the disclosed branch lowers $\bar\pi(\tau_\theta) = (1-\tau_\theta)\omega_Q /
   (\omega_H + (1-\tau_\theta)\omega_Q)$, and by the chord identity of Lemma d1-jensen the interior
   $\kappa$-motion of $\mathbb{E}[h]$ is the probability-weighted chord gap of $h$ on $[0,\bar\pi]$,
   which vanishes as $\bar\pi \downarrow 0$; numerically at baseline masses,
   $|\partial_\kappa\mathbb{E}_{D=0}h|$ falls from $0.0153$ ($\tau_\theta = 0$) to $0.00014$
   ($\tau_\theta = 0.95$). Both terms are negative. **To prove:** $\partial|\partial_\kappa
   \mathbb{E}_{D=0}h| / \partial\bar\pi \ge 0$ (two paragraphs from Lemma d1-jensen). Consistent
   check with the repo model: lowering $k_D$ at fixed $(k_1,k_0)$ lowers the total variation of
   $\Delta^{\mathrm{act}}$ over $\kappa \in [0.15, 0.85]$ monotonically ($0.0176 \to 0.0040$ as
   $\omega_P$: $0.037 \to 0.50$; independently reproduced) — but most of that fall occurs *without
   any flag* (no-disclosure regime: $0.0165 \to 0.0106$), because the buy is intrinsically revealing. Once proved, T2 on this
   margin is close to an accounting identity — sell it as the policy statement it is (a rule is a
   lever on revelatory efficiency), not as a discovered mechanism.
2. **Window margin $\tau_w$ — attenuation is *not* a partial-equilibrium theorem.** Comparing the
   flagged regime ($\tau_w = 1$) with the pooled regime ($\tau_w = 0$) at fixed cutoffs with the
   repo model, the $\kappa$-sensitivity of $\Delta^{\mathrm{act}}$ (total variation over
   $\kappa \in [0.15,0.85]$) is **higher** under disclosure for disclosed masses up to $\approx 0.29$
   (ratio disc/no-disc $= 1.06$ at the baseline $\omega_P = 0.037$; $1.19$ at $0.13$; $1.14$ at
   $0.29$) and lower only at $\omega_P = 0.50$ (ratio $0.38$); pointwise, disclosure is steeper at
   $\kappa \ge 0.7$ for $\omega_P \le 0.29$. The sign is calibration-dependent. This is the margin
   the February 2024 shock moves, so H1 (§4) cannot be called "the flagship test of T2" until the
   sign of the *disclosure-jump* liquidity slope (item 4) is derived under $(d\kappa<0, d\tau_w>0)$.
3. **Magnitude at the paper's own baseline is negligible.** With $k_D = 2.26$, $\mu = 1$, $\sigma_s
   = 0.707$, the disclosed mass is $\omega_P \approx 0.037$; the two curves of draft_v2's Figure
   "disclosure" (`disclosure_attenuation.csv`) have ranges $0.01107$ vs $0.01117$ over $\kappa \in
   [0.15, 0.85]$ — a difference below 1%, and by mean $|$slope$|$ the *disclosed* regime is slightly
   more sensitive ($0.0251$ vs $0.0236$). The calibration must be re-anchored so that the disclosed
   share of engagement is empirically meaningful (13D-disclosed vs behind-the-scenes engagement),
   and the paper must report the attenuation *elasticity*, not only its sign.
4. **The model object that H1 tests must be defined.** T2 concerns the ex-ante expected activism
   premium; the 13D announcement return is a different object. Define the *disclosure jump*
   $J(X) = P(X, 1) - P_{ND}(X)$: the price with the flag minus the pooled price at the same order
   flow (the no-disclosure price is the pre-flag price). $J$ is well defined; at baseline
   $\mathbb{E}[J \mid D = 1]$ increases in $\kappa$ ($0.33$ at $\kappa = 0.2$, $0.39$ at $0.5$,
   $0.42$ at $0.8$) and $J(2) = 0$ (the buy is already revealed at $X = +2$). Its liquidity slope
   and how $\tau_w$ and $\kappa$ jointly move it are the derivation H1 rests on. Same object gives
   the run-up share of H2 ($[P_{ND}(X) - \mu] / [P(X,1) - \mu]$).
5. **T3 — general-equilibrium region version: a to-do, not a result.** No GE attenuation derivation
   exists in the repo (v3 wrote it in the indicative). D8's inversion-free bound controls $dk/d\kappa$
   only; a cross-partial would need $d^2k/d\kappa\,d\tau$, which no contraction modulus reaches, and
   `prop:d8-counter` warns that GE can overturn a PE sign here. The statement to aim for compares two
   *first* derivatives: for $\tau' > \tau$, if the fixed-cutoff slope gap exceeds $\bar B(\kappa;\tau)
   + \bar B(\kappa;\tau')$ on $[\kappa_{lo}, \kappa_{hi}]$ (with $\bar B$ the D8 bound at each
   $\tau$), then $|d\Delta^{\mathrm{act}}/d\kappa|(\kappa;\tau') < |d\Delta^{\mathrm{act}}/d\kappa|
   (\kappa;\tau)$ there — a triangle inequality that reuses D8 twice. Requires $\tau$ in
   `numerical/` first: a few days.

## T4 — The liquidity hump, honestly stated

The hump is **not** the headline. It is presented as three objects, in descending order of
strength (and it must be distinguished from Mello and Repullo 2004, whose non-monotonicity is in
intervention incentives, ours in the premium through the inference partition):

1. **Endpoint symmetry (proved at fixed cutoffs; equilibrium limit asserted + numerically checked):**
   $\Delta^{\min}(0^{+}) = \Delta^{\min}(1^{-})$.
2. **Certified region (computed, machine-checked):** strict single-peakedness of
   $\Delta^{\min}(\kappa)$ is certified on $\kappa \in [0.35, 0.825]$ (inversion-free bound;
   $[0.30, 0.85]$ under exact IFT) with contraction modulus $L \le 0.836$, under the checkable
   conditions (R1) pointwise dominance and (R2) integral control (D8). Channel (A) is single-peaked
   at fixed cutoffs if the chord condition
   $$
   \mathcal{C}(\bar{\pi}) \;=\; h(0) - 2 h\!\left(\tfrac{\bar{\pi}}{2}\right) + h(\bar{\pi}) \;<\; 0,
   \qquad h = \pi \cdot p,
   $$
   holds (proved; $\mathcal C > 0$ gives a trough; $\mathcal C = 0$ is not covered). **Honesty note
   carried over from draft_v2 (Remark d5-vacuous), which v3 omitted:** on the paper's calibration
   family (C\*) cannot fail, so it selects nothing there — the hump/trough orientation is produced
   entirely by the GE cutoff-shift channel, and the chord second difference is retained only as a
   16/20-cell diagnostic. Under the three-branch prune $\bar\pi \equiv 1$ and (C\*) becomes the
   primitive inequality $h(1) < 2h(1/2)$; whether it can fail on the re-solved family is open.
3. **Falsifiable prediction (numerical elsewhere):** the interior peak $\kappa^\dagger \approx 0.58$
   (full-equilibrium argmax in `baseline_series.csv`, 0.0206 grid; 0.60 on D8's coarser 0.025 grid —
   a grid-resolution spread; v3's 0.59 was a solver-check value between grid points) and the
   certified trough at $\sigma_\xi =
   0.60$ are featured as an *economic boundary*: the hump lives where bidder entry is
   premium-sensitive (Remark d8-boundary). Non-monotonicity as an identification device is an
   *analogy* to Corum–Levit (2019, Prop. 4 — non-monotonicity in board private benefits separates
   selection from treatment), not the same device.

## T5 — The premium wedge (appendix microfoundation)

The disagreement-node tender game delivers $\lambda = 1 - r(1-\gamma)\psi$ in closed form
(MC-verified), and the boundary of the wedge assumption is characterized: $m_1 > m_0$ holds iff not
(certain raids $\wedge$ $\gamma = 0$ $\wedge$ unblockable offers), given $\theta < 1$ and
$\rho\Delta_{\mathrm{eng}} > 0$ — all proved. The measured-premium reversal $M(\pi) = \bar{m}/P$
strictly decreasing in $\pi$ (fixed cutoffs) holds for $\lambda < \lambda_{\mathrm{crit}} \approx
0.07$ (D7 JSON), whereas the baseline calibration sits at $\lambda \approx 0.86$; D7 aims the result
at Albuquerque–Fos–Schroth's cross-sectional predictions. Whether it also accounts for
Celentano–Levine's $-13.7\%$ ($-5.2$pp) is a separate mapping question — their estimand is a
selection-corrected treatment effect, $M(\pi)$ a cross-sectional ratio — so v3's "rationalizes" is
withdrawn: either move the calibration below $\lambda_{\mathrm{crit}}$ or state the reversal as a
low-appropriability regime.

## No-manipulation discipline

EGJ (2015, *AER*) Case 2 — a corrective action makes value non-monotone in the state, so a
positively informed trader may sell to induce it; their sufficient condition against manipulation
is $R_H - R_L > \tfrac{4}{3}x$ (verified in the published text). Here the profile is *infeasible*
rather than unprofitable: Exit liquidates the entire unit stake (Lemma dominance (i)), and Public
Voice buys, so no action shorts the firm while retaining exposure to the bidder's decision. One
sentence in draft_v3, not a lemma; it becomes substantive only if partial exit is added.

# Empirical Design {#sec-empirics}

**Discipline.** One dated shock, one signed prediction per test; institutional facts as
anchoring, never as "tests" without exogenous variation; announcement CARs are *disclosure price
impact*, never labeled value creation (preempting Ben-David, Bhattacharya, Huang and Jacobsen, JF
2026: "CAR is an unreliable measure of expected value creation"). **v3.1 addition:** every US 13D
filer is treated on the same date, so H1 is a *before/after* comparison with rich controls; the word
"difference-in-differences" is used only where a second difference exists (the bindingness dose in
H1; the within-event window contrast in H2).

## What the referee round found in the disk data (must be absorbed, not argued with)

- **No break in the outcome at the rule date.** Half-year median 13D CAR (WRDS market-model output,
  2,285 events): 2022H1 4.4%, 2022H2 3.0%, 2023H1 1.7%, 2023H2 0.4%, **2024H1 1.0%**, 2024H2 6.0%,
  2025H1 2.8%, 2025H2 0.8%. The v3 "1.6% → 2.6%" pre/post medians reproduce exactly but come from
  2024H2 (outside the main post window and straddling the 13G change) and from a **21-day** CAR
  window (`nrets` = 21), not $[-1,+1]$; one post event has a 2,899% CAR. Start the pre window in 2022
  and the sign flips.
- **Sample arithmetic.** 9,234 is the filing count; 4,638 have parsed event dates (0.68/0.66/0.64
  for 2022/2023/2024, **0.00 for 2025** — structured-era parser); the memo's own windows (post Feb 5–Aug
  31, 2024; pre 2023-01-01–2024-02-04) give ≈990 matched events in the existing WRDS output (301
  post, in 7 month-clusters; 1,226 post-window filings before matching).
- **F1 rests on 188 parsed filings** (98 pre / 90 post; parse rates 0.68/0.64); Manski bounds on the
  share filed within 5 bd are $[-7.9, +60.1]$pp and overlap — a parse rate above ≈0.72 signs the
  effect under the worst case. F1 **replicates on the full universe with a clean pre-trend**: median
  delay 7.0 / 7.0 / 5.0 bd and share within 5 bd 31.9% / 35.7% / 70.6% for 2022 / 2023 / 2024.
- **Two parser bugs.** `pct_of_class` regex cannot match a three-digit percentage (100.0% → 0.0) and
  takes the first reporting person's row (understating group stakes): 438 filings (7.1% of the 6,189
  parsed) sit at exactly 2.59%, 307 at 0.0, and 22.9% below 5% — not usable for F2 until fixed.
  `np.busday_count` ignores federal holidays.

## Facts section (facts the model must match)

- **F1 (executed):** the five-business-day deadline binds. On the full 2022–2025 universe of SC 13D
  originals the median disclosure delay is 7.0 business days in 2022 and 2023 and 5.0 in 2024; the
  share filed within five business days moves 31.9% → 35.7% → 70.6% — flat before the rule, a break
  at it. Report delays on a US-federal-holiday calendar, per-quarter parse rates (0.64–0.68) rather
  than silent drops, worst-case bounds, the bunching mass at exactly five days and the halving of
  the right tail (p90 23 → 11.1). Confounds to state: the EDGAR filing cut-off moved to 10 p.m. ET
  on the same date (a clock change can move a compliance share); 2024Q4 sits after the 13G retiming
  (report 2024Q2–Q3 as the clean post window). Extend to 2025 after the structured-era parser fix.
  Trivedi (2026) reports +0.35 on the same share with 13G controls — cite as corroboration.
- **F2 (gated on the parser fix):** stake-at-first-13D distribution; target moments from
  Collin-Dufresne–Fos (2015): median 6.2%, mean 7.68% (screened 2001–2010 activist sample —
  replicate their screens; the raw 2022–2025 all-filer median is 9.55%); bunching just above 5%. Unit
  stake in the model → this is a motivating exhibit, not a calibration target. **The sharpest
  post-rule prediction is the intermediate outcome: does the disclosed stake fall after February
  2024?** (CDF: ~23% of the final stake is accumulated between trigger and filing.) Fewer confounds
  than any CAR test; executable on disk data once the regex is fixed.
- **F3 (a signed prediction, not a fact):** the disclosure jump. A shorter window means less of the
  activist's presence is impounded before filing, so the $D=0 \to D=1$ jump should be larger; the
  confound is the smaller disclosed stake, which pushes it down. Report $[-1,+1]$ CARs (not 21-day
  windows) by half-year and within stake deciles; state that the current half-year series shows no
  break; report quantiles, not means.
- **F4 (deferred, 1–3 weeks):** campaign→takeover transition via EDGAR submissions API
  (SC TO-T / DEFM14A / 8-K). Benchmarks: Greenwood–Schor (2009): 18.1% of activist targets acquired
  within 12 months vs 7.2% for matched firms and 12.6% for non-activist 13D filers (≈ +11pp);
  Boyson, Gantchev and Shivdasani (2017, JFE): over one-third of targets receive a bid within two
  years (22% on the risk-arbitrage-excluded "activism merger" measure). *(v3's "70% within 2 years"
  was wrong.)*

## H1 — Attenuation of the liquidity slope (a before/after test, with a dose)

**Hypothesis.** Shortening the accumulation window moves information release from pre-filing
inference to the filing event; the sensitivity of 13D announcement returns to pre-event
liquidity should change after February 5, 2024. **The sign is not yet a theorem** (§3.2, items 2
and 4): T2 signs the ex-ante premium's sensitivity on the threshold margin; the disclosure jump's
liquidity slope under the joint window shock $(d\kappa < 0, d\tau_w > 0)$ must be derived first
and the prediction pre-registered in the paper before the estimate is reported.

**Specification.**
$$
\mathrm{CAR}_i[-1, +1] \;=\;
\beta_1\, \mathrm{Amihud}_i \;+\;
\beta_2\, (\mathrm{Amihud}_i \times \mathrm{Post}_i) \;+\;
\gamma\, \mathrm{Post}_i \;+\; \delta' X_i \;+\; \mathrm{FE} \;+\; \varepsilon_i,
$$
with the derived sign restriction on $\beta_2$; also on $\mathrm{CAR}[-10, +1]$ and in quantile
regressions (medians are the honest summary). Identification rests on three things, reported in
this order: (i) a **calendar-time coefficient figure** ($\hat\beta_1$ by quarter, 2022Q1–2025Q4,
with CIs) — the pre-trend test; (ii) a **bindingness dose**: for each filer, the pre-2024
leave-one-out median disclosure delay (≥3 pre-period filings); filers already inside five days are
plausibly untreated, giving a genuine triple difference $\mathrm{Amihud} \times \mathrm{Post} \times
\mathrm{Dose}$ with its own first stage; (iii) **randomization inference over placebo rule dates**
(every month-start; February of 2022, 2023, 2025) — the answer to 7 post month-clusters, not a
month-clustered SE. Cluster by firm (403 repeat firms, max 9 events). State the minimum detectable
effect: with $n \approx 990$, post share 0.30 and CAR SD $\approx 0.15$, $\mathrm{SE}(\beta_2) \approx
1.0$pp per SD of Amihud, so $t = 2$ needs $\approx 2.1$pp/SD — larger than the entire Amihud level
loading AFS estimate (+0.9pp/SD). H1 may end as a bounded null; say so in advance.

**Sample and data.** All SC 13D originals 2022-01-01 to 2025-12-31 (9,234 filings; ≈65% CRSP match
projected, not yet executed on the full sample), US common stocks (shrcd 10/11); event day = first
trading session after the EDGAR *acceptance* timestamp (the 10 p.m. ET cut-off change re-maps
filing dates for exactly the treated period; `accepted_after_4pm` is already parsed). CARs from the
on-disk CRSP daily snapshot (2021–2025, 14,092 PERMNOs) with Ken French factors; events and stakes
from the repo's EDGAR pipeline; filer type from a hand-coded random 150 with reported
precision/recall (a name regex is not a classifier); attrition table pre and post separately
(filings → originals → CUSIP → CRSP → common stock → valid Amihud → final).

**Illiquidity.** Amihud (2002) as a **pre-event average over trading days $[-250, -11]$** relative
to filing (excluding the accumulation window: CDF show Amihud falls ~46% on filer trade days),
$\mathrm{ILLIQ}_i = D_i^{-1}\sum_t |r_{i,t}|/\mathrm{DVOL}_{i,t}$ with $D_i \ge 100$; use $\ln(1 +
\mathrm{ILLIQ})$ winsorized at 1/99; log-cap and log-turnover throughout; report the Amihud–log-cap
correlation; preferred specification uses within-industry-and-size-decile ranks so $\beta_1$ is not
a size slope.

**Confound handling (full list, replacing v3's four items).** Same date (2024-02-05): 13D initial
deadline (the shock); 13D amendment deadline "promptly" → 2 business days (flag events with a 13D/A
inside the window); 13G→13D switch timing; **EDGAR cut-off 10 p.m. ET** (event-day realignment
above); cash-settled derivatives and group-formation guidance (flag). Later: 13G retiming
2024-09-30 (main post window ends 2024-08-31; kills 13G as a control), structured data 2024-12-18
(measurement break). Inside the post window: T+1 settlement 2024-05-28 (report Feb–May and Jun–Aug
halves separately; a dummy is not identified). Before: universal proxy (meetings after
2022-08-31; costs half the pre window if 2023-start is kept — show 2022-start as robustness);
**anticipation** (proposed 2022-02-10, adopted 2023-10-10 — donut Oct 2023 → Feb 2024). Throughout:
the 2022–23 hiking / 2024 easing cycle and activism-volume cycle (month FE where identified; a
non-event matched-firm-quarter Amihud slope as the background-slope control). Reverse causality
(activism deteriorates target liquidity: Meles et al. 2026) is why Amihud is measured strictly
pre-event.

**Selection honesty.** Filing is a choice and the marginal filer changes with the rule; report
filer-mix diagnostics pre/post; interpret $\beta_2$ as a reduced-form information-content change,
with an AFS-style selection correction as robustness, not headline. 13G filers are a *composition
diagnostic* (13D/13G share), not a placebo (different population, own treatment on 2024-09-30).

## H2 — Run-up to jump shift (the Collin-Dufresne–Fos template), in levels

The 10-to-5-day compression should shift returns from the pre-filing run-up into the filing-day
jump. **Do not use a ratio of signed CARs** (v3's $\rho$ has a denominator that is negative for
~40% of events and no finite mean). Anchor on the parsed *event* (crossing) date and stack three
windows per event — run-up $\mathrm{CAR}[-40,-1]$ (event-anchored), the crossing→filing segment
whose *length is the treatment*, and the jump $\mathrm{CAR}[-1,+1]$ (filing-anchored):
$$
\mathrm{CAR}_{iw} = a + b\,\mathrm{Post}_i + c\,\mathbf 1\{w = \mathrm{Jump}\} + d\,(\mathrm{Post}_i
\times \mathbf 1\{w = \mathrm{Jump}\}) + \delta' X_i + \varepsilon_{iw},
$$
clustered by event and firm; $d$ is the differential post-rule change in the jump relative to the
run-up — the one genuine within-event difference-in-differences in the design. Benchmark: the
published Collin-Dufresne–Fos (JF 2015, 1994–2010) report a run-up of about 3% over $(-60,-1)$ and a
two-day filing jump of about 2.5%; the 7% / 3% figures quoted in v3 are from the 2012 NBER WP
(18452, 2001–2010) — cite whichever version is used, not both. CDF's finding that Kyle's
$\lambda$, PIN and Amihud *fall* during accumulation is the load-bearing institutional fact for the
model's architecture. Sample = events with parsed crossing dates (none in 2025 until the parser
fix).

## H3 — The hump as a falsifiable cross-section (a prediction the theory offers; not promised)

For 13D-target deals receiving a bid within 12 months, hand-collect offer prices (SC TO-T /
8-K Item 1.01 / DEFM14A) and compute
$$
\mathrm{Premium}_i \;=\; \frac{P^{\mathrm{offer}}_i}{P^{\mathrm{unaffected}}_i} - 1,
$$
with $P^{\mathrm{unaffected}}$ at $-42$ trading days (Schwert 1996) and SDC's $-1$d/$-1$w/$-4$w as
robustness, using $\min(-42\text{d}, \text{day before the 13D})$ because the 13D typically precedes
the bid. The model counterpart is $\Delta^{\min}$ *conditional on a takeover* — the premium given a
bid, not the announcement return; the unconditional analogue is $p \cdot \Delta^{\min}$, so report
$\Pr(\text{bid} \mid q)$ alongside (conditioning on a bid conditions on the outcome $\kappa$ moves).
Test the non-monotone prediction with terciles or a quadratic in Amihud and the Lind–Mehlum (2010)
U-test with a Fieller interval for the turning point; the v3 statement $\theta_3 > \theta_1 \wedge
\theta_3 > \theta_5$ is an intersection–union hypothesis, not a Wald test, and five quintiles on a
few hundred deals (~60 per cell, premium SD ≈ 35pp) give $t \approx 1.25$ for an 8pp hump — state
the MDE. Separate the channels: control for acquirer−target Amihud where the acquirer is public
(Huang–Maharjan–Nanda's currency channel is stock-deal-specific and null in cash deals — **require the
hump in both cash and stock**), split public vs private acquirers (Massa–Xu's channel is
public-bidder-specific), keep the Amihud level (AFS +0.9pp/SD loading on both filing types) so the
hump is identified off curvature. Anchors: Massa–Xu (2013, JFQA): +10% premium per SD of target
liquidity; Huang–Maharjan–Nanda (2024, JCF): −4.5pp per SD of acquirer−target liquidity difference,
stock deals only; Celentano–Levine (2025): mean premium 36.6%, activism interaction −5.2pp.
**Status:** weeks-to-months of hand collection with a selection problem — offered as the falsifiable
prediction with the design spelled out; not promised in the submission draft.

## Calibration moments (split into what the model can produce)

**Panel A — targeted in calibration (model object in brackets).**

| Moment | Value | Source |
|---|---|---|
| 13D announcement CAR level [disclosure jump $\mathbb E[J\mid D=1]$] | $6.34\%$ (level only; the 75.2% treatment share has no model counterpart) | Albuquerque–Fos–Schroth 2022 |
| Mean bid premium [$\Delta^{\min}\mid$ bid; pins $(m_0,m_1)$ / D7 primitives] | $36.6\%$ | Celentano–Levine 2025 |
| Activism $\to$ premium interaction [$\Delta^{\min}\mid D{=}1$ vs $D{=}0$; say which of the two numbers is matched] | $-13.7\%$ ($-5.2$pp) | Celentano–Levine 2025 |
| Takeover prob. lift from activism [bidder entry $p$; a calibration input if $p$ is a primitive] | $+11$pp (12m: 18.1% vs 7.2% matched); $+7.7\%$ relative | Greenwood–Schor 2009; C&L 2025 |

**Panel B — signs the model must reproduce.**

| Moment | Value | Source |
|---|---|---|
| Liquidity $\to$ targeting sign [$\partial \Pr(\text{engage})/\partial\kappa$] | positive (baseline probit: $0.33\% \to 0.73\%$; IV "somewhat larger", not quantified) | Norli–Østergaard–Schindele 2015 |
| Voice$\to$exit mode shift in liquidity [$\partial\Pr(P)/\partial\kappa$ vs $\partial\Pr(E)/\partial\kappa$] | $-6.9$pp on 13D share per SD | Edmans–Fang–Zur 2013 |

**Panel C — motivating facts the static, unit-stake model does not target.**

| Moment | Value | Source |
|---|---|---|
| Run-up vs filing-day jump | JF 2015 (1994–2010): $\sim 3\%$ over $(-60,-1)$ vs $\sim 2.5\%$ two-day jump; NBER WP 18452 (2001–2010): $\sim 7\%$ vs $\sim 3\%$ | Collin-Dufresne–Fos 2015 / 2012 |
| Stake at first 13D | median $6.2\%$, mean $7.68\%$ | Collin-Dufresne–Fos 2015 |
| Pre-announcement accumulation | $54\%$ of block, $8.5\%$ trading profit | Norli–Østergaard–Schindele 2015 |
| Campaign costs by stage | negotiations \$2.9M / board seat \$1.8M / proxy contest \$5.9M | Gantchev 2013 |

# Edit Map: draft_v2 $\to$ draft_v3 {#sec-editmap}

| Area | Action |
|---|---|
| Title / abstract / intro | Reframe around the disclosure rule as a lever on revelatory efficiency; institutional hook first (1968$\to$2024 compression; the Feb-2024 shock); abstract states exactly what is proved where — no "theorem" for region-certified or to-do objects; the narrower checkable claim in the abstract, the "revelation technology" phrase (if kept) only in the introduction |
| Literature | Fix misattributions: the $-13.7\%$ premium finding is **Celentano–Levine 2025, not AFS** (rename `prop:d7-afs`); delete the unsupported Johnson–Swem window-isomorphism sentence (attribute the $\sigma^2T$ mapping to Back et al. 2018, pp. 1452–1453); reframe EGJ 2015 (analytic region-wise uniqueness, AER Prop. 1 — cite the posture, not "numerical uniqueness"); **add** Kyle–Vila 1991 (RAND), Mello–Repullo 2004 (FRL), Burkart–Lee 2022 (missing from `bibliography.bib`), Burkart–Lee–Voss (ECGI 956/2024), Levit–Malenko–Maug (JF 2024, JF 2026), Cetemen et al. (JF 2026), Bebchuk–Brav–Jackson–Jiang 2013, Massa–Xu 2013, Huang–Maharjan–Nanda 2024, Ben-David–Bhattacharya–Huang–Jacobsen (JF 2026, four authors; also missing from `bibliography.bib`), Trivedi 2026, Polk et al. 2024, Corum 2025, Bishop–Fos–Jiang–Partnoy 2026, Meles et al. 2026 |
| Model | Three-branch menu under (A2$'$); $\tau_\theta$ and $\tau_w$ as explicit primitives (§2.3); bidder conditions on $(P,D)$ as a sufficient statistic (replaces `lem:dropA7`); one-sentence no-manipulation remark; ternary noise + flag defended as the *minimal* technology partitioning inference (LMM 2024 as precedent, not proof); D7 symbols relabeled ($r,\gamma,\phi,\psi$); resolve $\delta$ (0.95 vs 1) and the (A5) contradiction (l. 696 vs l. 1010) |
| Equilibrium | Compact; T2 stated as the two-term product rule with the threshold-margin lemma proved and the window-margin sign left as a calibration statement; T3 (GE region version) added only if the first-derivative comparison is proved; existence under (A1),(A2),(A4),(A5a); meta-material collapsed to one remark |
| Comparative statics | R1 repackaged as endpoint lemma (fixed cutoffs) + certified region + falsifiable prediction; Remark d5-vacuous kept verbatim; sensitivity figures trimmed; the disclosure figure re-drawn at a calibration with meaningful $\omega_P$ and with the elasticity reported |
| Testable implications | Five $\to$ four numbered predictions, each mapped to a dataset and to a model object (the disclosure jump for CARs; $\Delta^{\min}\mid$bid for premia); cross-country thresholds as the out-of-sample agenda and the clean $\tau_\theta$ experiment |
| Welfare | Halved: first-best subsection cut; disclosure-wedge proposition downgraded to a remark (its hypothesis (ii) is admittedly untested); positive framing only — optimal-threshold welfare language belongs to Ordóñez-Calafi–Bernhardt |
| Extensions | Benchmark regimes become the $\tau_w \in \{0,1\}$ endpoints; noisy rumors kept as the wolf-pack bridge, labeled numerical |
| Empirical section (new) | Facts + H1 + H2 per Section 4 (before/after with dose; stacked-window levels); H3 as the offered prediction; confound table; attrition table; pre-registration box; calibration panels A/B/C |
| Appendices | D7/D8 stay as microfoundation/region-theorem records; bargaining appendix compressed to ~2 pages; duplicated curvature and endpoint proofs folded; **honesty labels preserved verbatim — never weakened** |

# Journal Targets and Risks {#sec-targets}

| Target | Fit | Key risk |
|---|---|---|
| **JF / RFS** (primary) | Theory-forward + institutional anchor + one clean shock; matches the Levit–Malenko–Maug / Burkart–Lee taste | T2 must become a real theorem on a stated margin with a non-trivial magnitude; the hump must be honestly labeled; differentiate from Celentano–Levine, Cetemen et al. and Corum on page 1 |
| **JFE** (alternative) | If the empirical section grows toward 30–35% (premium subsample + transitions) | JFE's activism space is structural-estimation-dominated; the before/after must carry the dose design and the placebo-date inference |
| JFQA / RAPS (fallback) | Certain fit | — |

**Risk register (revised).** (i) The first-stage fact is already public (Trivedi 2026; Polk et al.
2024) and Fos–Jiang–Partnoy are working the disclosure-friction margin — the differentiator must be
the premium object and the model, not the shock alone; execute F1 (universe) + the stake-at-filing
test + the H1 calendar-time figure first. (ii) The disk data show no CAR break at the rule date — plan
for H1 as a possibly bounded null and say so in the paper. (iii) T2's sign is margin-dependent and its
baseline magnitude is negligible — the theory work must precede any claim that the shock "tests T2".
(iv) The R1 counterexample invites "the hump is fragile" — preempt by featuring the economic boundary
and Remark d5-vacuous. (v) CAR-critique referees — CARs are only ever disclosure price impact; premia
come from hand-collected offer prices. (vi) "Too many moving parts" — the three-branch cut and appendix
exiles are the answer, but note that the honest $\tau_\theta$ device re-splits the disclosed branch. (vii)
Reproducibility: the Fact-2 execution code and the parser fixes must be committed; the gitignored CRSP
snapshot must be backed up off-repo. (viii) Reverse causality (activism → liquidity) — Amihud strictly
pre-event.

**Execution sequence (post-approval, revised).** (1) Owner approves the angle and chooses the paper's
primary margin ($\tau_\theta$ vs $\tau_w$); (2) theory: add $\tau$ to `numerical/`, re-solve the
three-branch model, derive the disclosure-jump slope, prove the threshold-margin lemma, resolve
(A5)/$\delta$, re-anchor the calibration; (3) empirics: parser fixes (percent regex, holidays,
structured era) → F1 universe → stake-at-filing → event-day realignment → H1 calendar-time figure →
dose design and placebo inference → H2 stacked levels; (4) premium subsample only if resourced; (5)
compile gates (0 errors, 0 undefined references) plus `make clean && make all`. Time estimate for (3):
weeks, not "3–4 days".

# Change log v3 $\to$ v3.1 (2026-08-19) {#sec-changelog}

Referee round: five parallel referee agents (theory, literature/originality, novelty scan, empirical
design with execution on disk data, facts verification) plus two adversarial verifiers; full report at
`quality_reports/reports/2026-08-19_framework_v3_referee_report.md`; agent reports in
`research/review_v3/`. Edits: (1) §1 originality claims restated; competitors named (Trivedi, Polk et
al., Corum, Bishop et al., Cetemen et al., Kyle–Vila, Mello–Repullo). (2) §2 notation block; (A2$'$)
for the prune; bidder information set as a sufficient statistic; $\tau$ split into $\tau_\theta$ and
$\tau_w$ with the Back-et-al. $\kappa$-mapping; existence assumption list; $\delta$ and (A5)
contradictions flagged. (3) §3 T2 restated as a two-term product rule with numeric evidence (threshold
margin attenuates; window margin does not at fixed cutoffs; baseline magnitude <1%); disclosure-jump
object introduced; T3 labeled to-do; T4 with Remark d5-vacuous, $\kappa^\dagger = 0.58$, Mello–Repullo;
T5 $\lambda_{\mathrm{crit}}$ caveat and C&L "rationalizes" withdrawn; no-manipulation reduced. (4) §4
rewritten around what the disk data show; F1 universe numbers and bounds; F2 parser gate and
stake-at-filing test; F3 as a signed prediction; F4 Boyson corrected; H1 as before/after with dose,
calendar-time figure, placebo inference, MDE, full confound table; H2 in stacked levels; H3 demoted;
Amihud definition; calibration panels; numbers corrected (+7.7% relative; Norli baseline probit; CDF
window). (5) Edit map, targets, risks and execution sequence updated. Honesty labels preserved or
strengthened throughout.
