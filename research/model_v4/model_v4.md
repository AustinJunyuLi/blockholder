# The Two-Round Blockholder Disclosure Model — a standalone model note

**v4 theory lane, ticket 30 (T2j). Card stamp 2026-08-21, post-ledger regeneration.**

Markdown mirror of `research/model_v4/model_v4.tex` (same content, same order).

This note states the v4 two-round model in one place: primitives, timing, the partition the
disclosure rule induces, the equilibrium notion, the standing hypotheses, and the eight-result
ledger with its honesty labels. It then records what the v4 model takes from the frozen manuscript
`draft_v2.tex`, what it simplifies, and what it drops; and it lists the executed evidence, failures
included. Every statement of content here is transcribed from `research/model_v4/MODEL_CARD.md`
(version stamp 2026-08-21, post-ledger regeneration) and `research/model_v4/LABEL_LEDGER.md`. The
card is the single source of truth: where a proof file and the card differ, the card wins. The
conditionality attached to each result is not decoration. It is the result.

---

## 1. Position and object

The disclosure rule *is* the market's partition. The model asks how liquidity $\kappa$ moves bidder
entry and the expected takeover premium when a stake threshold $\tau$ and a filing window $T$ split
control-node histories into a **flagged** cell (the filing has landed before the control decision)
and a **pooled** cell (it has not).

The control-outcome object is the expected engagement-related premium $\Delta^{\mathrm{act}}(\kappa,\tau,T)$.
The price-path objects are the run-up path $R_d$, the cumulative run-up $R$, and the filing-day jump
$J$. Lower $\tau$ means a tighter threshold margin; lower $T$ means a tighter window margin.

Throughout, $\kappa \in [0,1]$ is *noise-trading intensity* — never depth, volume or turnover.
Upright $T$ is the filing window; $\mathcal{T}$ is the outer best-response map. Bare $\lambda$ is not
available (it is the appropriability coefficient of the tender-game appendix), and neither is a bare
$C$, $W$, $\mathcal{S}$, $u$ or $g$: every one of those letters is overloaded in this project and
always carries its subscript.

---

## 2. Primitives

### Fundamentals, signal, bidder

- $v \sim N(\mu_v,\sigma_v^2)$ is the target's standalone value; the blockholder observes
  $s = v + \varepsilon$ with $\varepsilon \sim N(0,\sigma_\varepsilon^2)$ independent of $v$. The
  Gaussian projection coefficient is $\beta = \sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2) \in (0,1)$,
  so $\mathbb{E}[v \mid s] = \mu_v + \beta(s-\mu_v)$. (The letter is $\beta$, the frozen manuscript's
  name; bare $\lambda$ is reserved.)
- The bidder draws a private synergy shock $\xi \sim N(0,\sigma_\xi^2)$ independent of $(v,s)$;
  $\bar S$ is mean bidder synergy and $K>0$ the entry cost.
- $m_0, m_1$ are the takeover premia without and with engagement, with $m_1 > m_0$ **and**
  $m_0 \ge 0$; $\Delta_m = m_1 - m_0 > 0$ is the premium wedge, and $\Delta_V \ge 0$ is the
  non-takeover value engagement creates. The restriction $m_0 \ge 0$ is load-bearing: it is what
  makes the inner pricing fixed point exist, be unique and be continuous (§5, A5).

### Trading, stakes, the legal clock

- Noise is a ternary mark of size $\bar z > 0$: $\Pr(z_d = 0) = 1-\kappa$,
  $\Pr(z_d = \pm\bar z) = \kappa/2$.
- $b_0$ and $\bar b$ are the initial and maximum stake, $0 \le b_0 \le \bar b$, with $b_0 < \tau$
  maintained: a pre-existing crossing is outside the core.
- $\mathcal{J}$ is a finite ordered menu of complete contingent plans, least to most aggressive,
  $|\mathcal{J}| = J < \infty$; $a_j \in \{0,1\}$ is the engagement attached to plan $j$, with
  $a_j = 1$ for Voice plans and $0$ for Exit and Hold.
- $B_j(s,d) \in [0,\bar b]$ is the cumulative pooled stake at business day $d$, with
  $B_j(s,-1) = b_0$; for Voice plans $\partial_d B_j \ge 0$ and $\partial_s B_j \ge 0$, Hold is
  constant and Exit weakly decreasing. For *every* plan and every $d$, $s \mapsto B_j(s,d)$ is Borel
  — automatic for Voice and Hold, a genuine requirement for Exit, and needed because pooled pricing
  integrates over every type including Exit types.
- $b_j^*(s) = B_j(s,H)$ is the terminal target stake; $H$ is the finite control-decision horizon in
  business days.
- $c_j(s;\tau) = \inf\{d : B_j(s,d) \ge \tau\}$ is the threshold-crossing date ($+\infty$ if it never
  happens); $f_j = c_j + T$ is the legal filing date; the flag lands iff $f_j \le H$, equivalently
  iff $B_j(s,H-T) \ge \tau$.
- $D_j(s;\tau,T) = \mathbf{1}\{a_j = 1,\ c_j < \infty,\ f_j \le H\}$; $D = 1 \Rightarrow a = 1$.
  $B_j^F = B_j(s,f_j)$ is the stake at filing and $Q_j^F = b_j^*(s) - B_j^F \ge 0$ the flagged-round
  order for a Voice plan.
- $\Gamma$ is a finite ordered coarsening from stake increment to pooled order mark,
  $q_{jd}(s) = \Gamma(B_j(s,d) - B_j(s,d-1))$, and observed pooled order flow is $X_d = q_{jd} + z_d$.
  ($\Gamma$, not $\psi$: $\psi$ is tender-game pivotality and $\chi$ is the frozen manuscript's cost
  parameter.)

### Information, prices, control outcome

$\mathcal{H}_d^P = (X_0,\dots,X_d;\ \text{flag landed by } d)$ is the pooled public history, finite.
$F = (B^F, a=1)$ is the truthful filing message and $\mathsf{S}_F = (B^F, Q^F, a{=}1)$ is $F$
augmented by the flagged-round order. The control-node information set is

$$\mathcal{I}_H = \mathcal{H}_H^P \text{ on the pooled cell } \{D=0\}, \qquad
\mathcal{I}_H = \mathsf{S}_F \text{ on the flagged cell } \{D=1\},$$

the bidder's own $\xi$ being private. The engagement posterior is
$\pi(\mathcal{I}) = \Pr(a=1 \mid \mathcal{I})$, equal to $1$ on the flagged cell; entry probability is
$p(\mathcal{I}) = 1 - \Phi\big((P + K + m_0 + \pi\Delta_m - \bar S)/\sigma_\xi\big) \in (0,1)$; and
with entry indicator $\mathsf{B}$ the terminal shareholder payoff is

$$Y = (1-\mathsf{B})(v + a\Delta_V) + \mathsf{B}(P + m_0 + a\Delta_m).$$

Prices are competitive, $P(\mathcal{I}) = \mathbb{E}[Y \mid \mathcal{I}]$, with the convention
$P_{-1}^P := \mathbb{E}[Y]$ for the pre-trading pooled price (needed whenever $c = 0$, which $T = H$
forces on every flagged history). The genuine fixed point sits at control nodes: at an earlier pooled
date $d < H$ the price is a tower expectation of already-solved control-node values, with no
self-reference. $P_{\mathrm{ND}}(\mathcal{H}_{f^-}^P) = P_{f^-}^P$ is the *not-yet-disclosed* price at
the same realised order flow — not a never-disclosed counterfactual, under which reading the
run-up/jump identity acquires a residual term. Then

$$R_d = P_d^P - P_{c^-}^P, \qquad R = P_{f^-}^P - P_{c^-}^P, \qquad J = P^F - P_{\mathrm{ND}},
\qquad P^F - P_{c^-}^P = R + J \ \text{ exactly}.$$

$J$ is **not** claimed $\kappa$-invariant.

### The blockholder's objective

$$U_j(s) = \mathbb{E}\big[\, b_j^*(s)\,Y - \mathcal{C}_j^{\mathrm{trade}} - a_j C_j(s) \,\big|\, s, j \,\big],$$

the expected terminal value of the position the plan builds, net of what it costs to build and to
engage: $\mathcal{C}_j^{\mathrm{trade}}$ is the execution outlay (increments valued at the pooled
prices $P_d^P$ up to the plan's last pooled date, plus $Q_j^F(s)P^F$ when $D_j = 1$) and
$C_j(s) \ge 0$ the engagement cost. Only two properties of $U_j$ are ever used: **plan-locality** —
$U_j$ depends on $j$ only through the executed stake path, the prices paid on it, the terminal stake,
the engagement flag and the cost — and **integrability**, $\mathbb{E}[\max_j |U_j|] < \infty$.

### Premium and sensitivity objects

- $h(\mathcal{I}) = \pi(\mathcal{I})\,p(\mathcal{I})$, with $h \ge 0$ and $h(0) = 0$;
  $\Delta^{\mathrm{act}} = \Delta_m\,\mathbb{E}[h(\mathcal{I}_H)] \ge 0$.
- $M_F = \Delta_m \mathbb{E}[h \mid D=1]$, $M_P = \Delta_m \mathbb{E}[h \mid D=0]$;
  $\Omega = \Pr(D=1) = \Pr(a=1)\,\omega_a$.
- $\mathcal{S} = |\partial_\kappa \Delta^{\mathrm{act}}|$, $\mathcal{S}_P = |\partial_\kappa M_P|$;
  $C_h(\bar\pi) = h(0) - 2h(\bar\pi/2) + h(\bar\pi)$.

$\omega_a = \Pr(D=1 \mid a=1)$ is the disclosed share of engagements, the calibration target;
$\Omega$ is the unconditional flagged weight and is the frozen manuscript's $\omega_P$. $\bar\pi$ is
the **upper support point** of the pooled engagement posterior in the A($\tau$) representation — *not*
the pooled engagement share. The share is the mean $\mathbb{E}[\Pi_\kappa]$, which under A($\tau$) is
$\kappa$-invariant (a mean-preserving spread) and is strictly below $\bar\pi$ in any non-degenerate
case, equalling $\bar\pi/2$ only under level symmetry $A_0 = A_1$. Reading $\bar\pi$ as the mean forces
a point mass at $\bar\pi$ with $A'_\kappa = 0$ and zero interior motion — degenerate, and excluded.
$A'_\kappa$ is the common derivative of the A($\tau$) weights ($A_0' = A_1' = A'_\kappa$,
$A_{1/2}' = -2A'_\kappa$). Weight-effect ratios are $W_\tau, W_T$ (e.g.
$W_T = (1-\Omega(\tau,5))/(1-\Omega(\tau,10))$) and composition-effect ratios are $C_\tau, C_T$ (e.g.
$C_T = \mathcal{S}_P(\tau,5)/\mathcal{S}_P(\tau,10)$), unsigned.

For the general-equilibrium certificate: $k = (k_1 \le \dots \le k_{J-1})$ is the cutoff vector on the
compact ordered polytope $\Theta$ with parameter vector $\vartheta$; $\mathcal{T}(k;\vartheta)$ the
outer best-response map; $L_{\mathcal{R}} = \sup_{\mathcal{R}} \lVert D_k \mathcal{T} \rVert$ the
contraction bound; $r_\tau = -\tau$, $r_T = -T$ the strictness coordinates (higher $r$ = tighter);
$g_r^{PE} = -\mathrm{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{act}}$
the direct fixed-policy attenuation margin;
$\bar k_x = |\partial_x \mathcal{T}|/(1-L_{\mathcal{R}})$ and $\bar k_{\kappa r}$ the inversion-free
derivative bounds;

$$\mathcal{B}_r^{GE} = |\Delta_{\kappa k}|\bar k_r + (|\Delta_{kr}| + |\Delta_{kk}|\bar k_r)\bar k_\kappa
+ |\Delta_k|\bar k_{\kappa r}, \qquad \eta_r = g_r^{PE} - \mathcal{B}_r^{GE}$$

the GE remainder bound and the slack on a certified region $\mathcal{R}_r$.

---

## 3. Timing: the two rounds

1. Nature draws $v$ and the blockholder's signal $s$; the blockholder picks one complete contingent
   plan $j$ from the finite ordered menu $\mathcal{J}$.

2. **Round 1 — pooled trading.** The plan's stake path executes over business days $d = 0,\dots,H$.
   Market makers see pooled order flow and set $P_d^P = \mathbb{E}[Y \mid \mathcal{H}_d^P]$. There is
   **no within-window re-optimisation**, and hence no feedback from realised order flow or prices into
   the path: $B_j(s,d)$, $q_{jd}(s)$ and $Q_j^F$ are functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone.
   This is a numbered hypothesis, not a modelling aside: two steps of L2 fail without it.

3. **Disclosure node.** The flag lands iff $D = 1$, i.e. iff the plan engages, crosses $\tau$ at some
   date $c < \infty$, and $c + T \le H$. The filing reveals $F = (B^F, a=1)$. **The flag terminates
   the pooled round.** Pooled trading stops when the filing lands; the flagged round follows it and
   the bidder acts after that. Without this reading $Q^F = b_j^*(s) - B_j^F(s)$ is not the
   blockholder's whole residual position, and the flagged-round step of P1 fails.

4. **Round 2 — flagged trading, then the bidder.** If $D = 1$ the blockholder submits $Q^F$, the
   market prices $P^F = P(F,Q^F)$, and then the bidder decides. If $D = 0$ there is no flagged round
   and the bidder acts on the pooled history.

Sequence: pooled round → flag or no flag → flagged round if applicable → bidder decision.

---

## 4. The partition

The disclosure indicator $D = \mathbf{1}\{a=1,\ c(\tau)+T \le H\}$ maps every control-node history
into exactly one of two cells, $\mathcal{C}_F$ (flagged) and $\mathcal{C}_P$ (pooled), exclusive and
exhaustive by construction. The cells are keyed by the disclosure rule and by nothing else:

- On $\mathcal{C}_F$ the control-node information set is the flagged tuple
  $\mathsf{S}_F = (B^F, Q^F, a{=}1)$: the market knows engagement happened, $\pi = 1$, and the pooled
  residual is (under A7′) pure noise conditional on $\mathsf{S}_F$.
- On $\mathcal{C}_P$ the control-node information set is the pooled public history $\mathcal{H}_H^P$:
  the market has an inference problem, and the posterior $\pi(\mathcal{H}_H^P)$ is where $\kappa$
  enters.
- The clock equivalence: for every Voice plan, $f_j \le H \iff B_j(s,H-T) \ge \tau$. A tighter
  threshold (lower $\tau$) or a tighter window (lower $T$) moves histories from $\mathcal{C}_P$ into
  $\mathcal{C}_F$ and nowhere else.
- Each flagged history yields $B^F$, $R_d$, $R$, $J$, with $P^F - P_{c^-}^P = R + J$ exactly.
- $\Omega = \Pr(D=1)$ is the cell weight; A8 asks for $0 < \Omega < 1$, which is required only for
  positive cell mass, never for the structural partition itself.

---

## 5. Equilibrium notion, and standing hypotheses

### Equilibrium notion

**Cutoff perfect Bayesian equilibrium**: (i) a weakly ordered cutoff vector
$k = (k_1 \le \dots \le k_{J-1})$ mapping $s$ into a plan; (ii) sequentially optimal pooled and
flagged components; (iii) Bayes-consistent beliefs on path; (iv) competitive pooled and flagged prices
at their fixed points; (v) the bidder-entry rule; (vi) off-path beliefs as limits of full-support
perturbations. Weak inequalities permit collapsed action regions, Hold included. Existence is Brouwer
on the compact ordered polytope $\Theta$ for the outer map $\mathcal{T}(k;\vartheta)$, i.e.
$k = \mathcal{T}(k;\vartheta)$. **Uniqueness is not claimed.**

### Standing hypotheses

**A1 Independent primitives.** $v, \varepsilon, \xi$ and all $z_d$ mutually independent; all variances
strictly positive.

**A2′ Finite model, amended boundedness.** Finiteness is unchanged: the plan menu $\mathcal{J}$, the
image of $\Gamma$, the noise support $\{-\bar z, 0, +\bar z\}$ and the horizon $H$ are all finite. The
old flat boundedness clause was *false* and is replaced by: prices and payoffs are locally bounded in
$(s,\vartheta)$ on the maintained parameter set, and $\mathbb{E}[\max_{j \in \mathcal{J}} |U_j|] < \infty$
for every $k \in \Theta$. Flat global boundedness is inconsistent with the rest of the model — $v$ is
Gaussian and the flagged region is unbounded in $s$ under A7′, so $Y$, prices and $U_j$ are unbounded.
Integrability is all any proof consumes.

**A3 Ordered plans, single crossing.** At every belief/price system, adjacent-plan payoff differences
cross zero at most once in $s$, and the preferred plan is weakly increasing in $s$.

**A4 Legal-clock discipline.** $c$ is the first date the path reaches $\tau$; the filing lands exactly
at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in the core.

**A5 Inner pricing regularity, mostly demoted to a theorem.** Each public-history pricing map has a
unique fixed point, continuous in beliefs, cutoffs and parameters. *Under $m_0 \ge 0$ — a card
restriction — existence, uniqueness and continuity of the inner fixed point are theorems, not
assumptions*: with $\bar y(\mathcal{I}) = \mathbb{E}_\mu[v] + \pi\Delta_V$ and
$\bar m(\mathcal{I}) = m_0 + \pi\Delta_m$, the pricing map is
$P \mapsto \bar y + \bar m\,p(P)/(1-p(P))$, strictly decreasing in $P$ wherever $\bar m \ge 0$, so it
crosses the identity exactly once. A5 is retained only as its continuity clause: the pricing family is
continuous in the cutoff vector and the parameters and measurable in the flagged tuple. Because the
flagged information sets are continuum-indexed, "unique fixed point" must be read as a measurably
selected *family*, not a finite list.

**A6 Compact outer self-map.** All best-response cutoffs lie in a common compact ordered polytope
$\Theta$; $\mathcal{T}$ is continuous and maps $\Theta$ into itself.

**A7 / A7′ Filing sufficiency.** On flagged histories $(B^F, Q^F, a=1)$ identifies the informed
component of the selected plan; conditional on it the pooled order-flow residual is pure noise,
independent of $(v,s,\xi)$. *L2's proof uses the injective form and the weak wording is not
sufficient* — it permits two $(j,s)$ pairs with different pooled paths, which is L2's first failure
case. The injective form is A7′: on the flagged set the composed terminal target
$s \mapsto b^*_{j(s)}(s)$ is strictly increasing *for every cutoff vector $k \in \Theta$*; for a menu
this amounts to each $b_j^*$ strictly increasing with no backtracking across any admissible plan
switch. Strictness of $B^F$ is neither necessary (it fails at crossing-date jumps on the pro-rata menu)
nor sufficient (multi-Voice backtracking). Injectivity forces $B^F$ continuum-valued; injective plus
measurable already gives a measurable inverse. *Satisfiability is resolved*: A7′ plus a fixed cutoff
policy plus $\Omega > 0$ deliver the on-path injective form with an explicit inverse, and a satisfying
menu exists (the pro-rata single-Voice menu with terminal target strictly increasing on all of
$\mathbb{R}$, which also satisfies the joint $(j,s)$ form). Failure boundary: a binding stake cap,
quantized stakes, a composed target repeating values across Voice-plan switches, $\Omega = 0$, and
policy-dependence when the condition is stated at only one equilibrium's cutoffs. A7′ menus are fully
separating on the flagged set, so the burden moves to incentive compatibility rather than away.

**A8 Interior crossing.** $0 < \Omega(\kappa,\tau,T) < 1$.

**A($\tau$) Threshold chord restriction.** The pooled posterior law has the symmetric ternary
representation

$$\mathbb{E}[h] = A_0(\kappa)h(0) + A_{1/2}(\kappa)h(\bar\pi/2) + A_1(\kappa)h(\bar\pi),
\qquad A_0' = A_1' = A'_\kappa, \quad A_{1/2}' = -2A'_\kappa,$$

with maintained orientation $C_h(\bar\pi) \le 0$ and $|C_h|$ weakly increasing in $\bar\pi$. Two
clauses:

- **(τ-i) The kernel depends on the information set only through the engagement posterior:**
  $h(\mathcal{I}) = h(\pi(\mathcal{I}))$, so $h(0)$, $h(\bar\pi/2)$, $h(\bar\pi)$ are well defined and
  $\kappa$-free. This is a restriction, not a reading: $h = \pi p$ and $p$ depends on the price as well
  as on $\pi$, so in the model $h = \pi\,p(\hat v,\pi)$ is a function of *two* scalars. The clause says
  the standalone-value channel and the engagement channel do not co-move inside the pooled cell in a
  way that moves $h$ at a fixed posterior.
- **(τ-ii) The support and $\bar\pi$ are $\kappa$-free; only the weights move.** Without the second
  half, L3's conclusion is **false**: the derivative gains a term first order in $\bar\pi$ and the
  vanishing fails.

*Where the bite is*: given a $\kappa$-invariant three-point support, the derivative restrictions are
*equivalent* to $\kappa$-invariance of the pooled block's total mass and of its unnormalised engagement
moment, both of which the model delivers at fixed policies. A($\tau$)'s entire remaining content is the
support condition. A one-round ternary-noise market with informed mark $2\bar z$ and pre-order
engagement share $\tfrac12$ satisfies it; the frozen manuscript's own no-disclosure structure (informed
mark $\bar z$) does **not** — its pooled law has four atoms, two of which move with $\kappa$. **Whether
the two-round pooled cell of the timing above satisfies the support condition is OPEN.** Every
A($\tau$)-conditional result — and therefore L4 leg 3 and T1 Part B — inherits that conditionality.

**A(br) Chord–sensitivity bridge.** Consumed by L4 leg 3 and T1 Part B, and by nothing else. For two
compared thresholds $\tau' < \tau$ at fixed policies and a common $\kappa$:

- **(br-i) Representation at both policies.** A($\tau$)'s symmetric ternary representation holds for
  the pooled class under $\tau$ *and* under $\tau'$, with endpoints $\bar\pi(\tau)$, $\bar\pi(\tau')$
  and coefficients $A'_\kappa(\tau)$, $A'_\kappa(\tau')$.
- **(br-ii) $\kappa$-localisation.** At fixed policies all $\kappa$-dependence of $M_P$ sits in the
  A($\tau$) weights, so $\partial_\kappa M_P = \Delta_m A'_\kappa C_h(\bar\pi)$ exactly, with no
  composition-through-$\kappa$ remainder. Written against the honest reading $h = \pi\,p(\hat v,\pi)$,
  this repairs an ambiguity rather than adding a fourth independent restriction; the trailing "hence"
  is derivable, not assumed.
- **(br-iii) Coefficient stability across the threshold margin.**
  $|A'_\kappa(\tau')| \le |A'_\kappa(\tau)|$; weakest sufficient form is equality — reclassification
  changes *which* histories are pooled, not the $\kappa$-responsiveness of the pooled weights. *This is
  the clause with the least justification behind it; it is the one to attack first.*
- **(br-iv) Endpoint linkage.** $\bar\pi$ is A($\tau$)'s chord endpoint — the upper support point — and
  is a weakly increasing function of the pooled prior engagement share
  $\bar\pi_{\mathrm{pr}} = \Pr(a=1 \mid D=0)$, the same function at $\tau$ and $\tau'$. The identity
  branch $\bar\pi = \bar\pi_{\mathrm{pr}}$ is excluded as degenerate.
- **(br-v) Comparability of the chord functional across thresholds.** $C_h(\cdot)$ — and the kernel $h$
  it is built from — are the same functions of the posterior at both compared thresholds. Without it,
  leg 3 compares $|C_h|$ across two different functionals and the comparison is meaningless. Required
  independently by three agents, and confirmed not implied by (br-i)–(br-iv).

*Sharpening on file, recorded not assumed*: $\bar\pi = \bar\pi_{\mathrm{pr}}/\rho$ with
$\rho := \tfrac12 A_{1/2} + A_1$ provably $\kappa$-free, so (br-iv) is equivalent to
$\rho(\tau')/\rho(\tau) \ge \bar\pi_{\mathrm{pr}}(\tau')/\bar\pi_{\mathrm{pr}}(\tau)$. Under the
level-symmetric reading $\rho = \tfrac12$ and $\bar\pi = 2\bar\pi_{\mathrm{pr}}$, forcing
$\bar\pi_{\mathrm{pr}} \le 1/2$ — an inherited restriction on A($\tau$)'s domain that is not resolved.

**AGE GE differentiability and contraction.** On a candidate region $\mathcal{R}$ the outer map is
twice continuously differentiable, $L_{\mathcal{R}} < 1$, and the sign of the equilibrium liquidity
derivative is constant on $\mathcal{R}$.

---

## 6. The result ledger

Seven of eight results carry two-pass evidence — an adversarial proof-read PASS *and* an independent
statements-only re-derivation PASS, by different agents — and are labelled PROVED with their
conditionality written into the label. C1 is CONJECTURE. Labels are transcribed from
`LABEL_LEDGER.md`; each statement is the amended one, with its hypothesis set named in full. Nothing
was weakened silently.

| ID | Statement, with its full hypothesis set | Label |
|---|---|---|
| **D1** | Under **A1, A2′, A4, A5, the primitive/plan table restrictions, the cutoff selection map, and the pricing conventions** ($P_{-1}^P = \mathbb{E}[Y]$; $P_{\mathrm{ND}} = P^P_{f^-}$), plus two hypotheses this regeneration wrote onto the card — **Borel regularity of $s \mapsto B_j(s,d)$ for every plan including Exit** (needed only for part (c), since pooled pricing integrates over all types) and **a content for $\mathcal{I}_H$** — the indicator $D = \mathbf{1}\{a=1,\ c(\tau)+T \le H\}$ is **measurable** and maps every control-node history into exactly one cell; for every Voice plan $f_j \le H \iff B_j(s,H-T) \ge \tau$; and each flagged history yields $B^F, R_d, R, J$ with $P^F - P_{c^-}^P = R + J$. | **PROVED** |
| **L1** | Under **D1, the premium definitions, A5** (which pins *the* version of $\mathbb{E}[Y \mid \mathcal{I}]$), **A2′ with $\Delta_m$ finite, and A1** (one probability space): whenever $0 < \Omega < 1$, $\Delta^{\mathrm{act}} = \Omega M_F + (1-\Omega)M_P$; at $\Omega = 1$ it degenerates to $\Delta^{\mathrm{act}} = M_F$ and at $\Omega = 0$ to $\Delta^{\mathrm{act}} = M_P$, the null-cell average being *undefined rather than imputed* — proved as a non-identification statement, not asserted. | **PROVED** |
| **L2** | At fixed cutoff and execution policies, under **A1; A2′ with the primitive/plan table restrictions; A4; A5; A7′ in its on-path injective form, consumed almost surely on the flagged set; D1; the no-feedback timing; and $\Omega > 0$** — together with an explicit bidder-entry rule carried as bookkeeping: $(B^F,Q^F,a{=}1)$ makes the pre-filing pooled history conditionally independent of $(v,s,\xi)$ on the flagged set, so the flagged posterior, price, entry probability and $M_F$ are invariant to $\kappa$. ("Almost surely" is the only coherent reading once $B^F$ is continuum-valued, since then no individual flagged tuple has positive probability.) | **PROVED** |
| **L3** | **Under A($\tau$)** — including (τ-i) kernel-through-posterior and (τ-ii) $\kappa$-free support *and* $\kappa$-free $\bar\pi$ — plus $h(0)=0$; $\kappa$-free pooled mass and engagement moment at fixed policies; D1 by statement; minimal regularity ($h$ continuous on $[0,\bar\pi]$, twice differentiable on the open interval — Darboux does the rest, no continuity of $h''$); for the small-$\bar\pi$ corollary only, a second-order Peano expansion of $h$ at $0+$ and one and the same kernel along the shrinking family; and, for the seam where L4 consumes L3, $|A'_\kappa|$ bounded *uniformly in $\bar\pi$*. Then $\partial_\kappa \mathbb{E}_\kappa[h] = A'_\kappa C_h(\bar\pi)$ exactly; $C_h(\bar\pi) = \tfrac14 \bar\pi^2 h''(\zeta)$ for some $\zeta \in (0,\bar\pi)$ — an identity, not an approximation; and $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, so the interior motion vanishes at rate $\bar\pi^2$. **An "if", never an "iff"** ($A'_\kappa = 0$ also kills the motion). Whether the two-round pooled cell satisfies A($\tau$)'s support condition is **OPEN**. | **PROVED** under A($\tau$) |
| **L4** | At fixed policies, for $b_0 < \tau' < \tau$ at a common window $T$ and common $\kappa$, with $\Omega(\tau',T) < 1$: **(leg 1, unconditional)** $\mathcal{C}_F(\tau,T) \subseteq \mathcal{C}_F(\tau',T)$ with every newly flagged history generated by a Voice plan, hence $\Omega(\tau',T) \ge \Omega(\tau,T)$; **(leg 2, unconditional)** the pooled engagement *share* falls, $\bar\pi_{\mathrm{pr}}(\tau') \le \bar\pi_{\mathrm{pr}}(\tau)$, with an exact identity for the gap; **(leg 3, under A(br))** $\mathcal{S}_P(\tau',T) \le \mathcal{S}_P(\tau,T)$, with equality whenever $C_h(\bar\pi(\tau)) = 0$. Legs 1–2 need only **D1's clock equivalence, the no-feedback timing, fixed policies, $b_0 < \tau' < \tau$ imposed at both thresholds, A1, A4, $D=1 \Rightarrow a=1$, and $\Omega(\tau') < 1$** — the "nestedness" clauses are *conclusions, not hypotheses*. Leg 3 additionally needs **L3 by statement, A($\tau$)'s maintained magnitude monotonicity of $|C_h|$** (the sign half $C_h \le 0$ is never used at this leg) **and A(br) (br-i)–(br-v)**. | **PROVED** (legs 1–2 outright; leg 3 **under A(br)**) |
| **P1** | Under **A1, A2′, A3, A4, A6, A7′ (on-path injective), D1 by statement, the no-feedback timing read with the flag-terminates-the-pooled-round clause, the definitional round-2 action-set hypothesis** (the flagged-round action set *is* the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements agreeing with $j$ on everything already played — *not* a closure condition, which is jointly unsatisfiable with finiteness by cardinality), **$m_0 \ge 0$, and the blockholder-objective definition $U_j$**: a cutoff PBE over complete contingent plans exists — $k^\star \in \Theta$ with $k^\star = \mathcal{T}(k^\star;\vartheta)$, prices at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs as limits of full-support perturbations over *plans*, the entry rule, and a sequentially optimal flagged component. **A5 is not assumed**: its existence and uniqueness content is derived from $m_0 \ge 0$. **At any such equilibrium at which A8 holds**, both cells carry strictly positive probability and are on path; for A8's restatement as a single signal threshold add **H-ord** (Voice stake monotonicity across plans) and the upper-set engagement-flag hypothesis. A8 is a condition *on the fixed point exhibited*: existence of an equilibrium *at which* A8 holds is not claimed. Uniqueness is not claimed. | **PROVED** |
| **T1** | At fixed plan and cutoff policies, with $0 < \Omega < 1$ and $\mathcal{S}_P > 0$: **(A)** $\mathcal{S} = (1-\Omega)\mathcal{S}_P$ exactly, and the same factorisation holds for the total-variation aggregate of $\Delta^{\mathrm{act}}$ over any $\kappa$-grid with no differentiability required; **(B)** threshold tightening attenuates — $\mathcal{S}(\tau')/\mathcal{S}(\tau) = W_\tau C_\tau \le 1$ because *both* ratios lie in $[0,1]$, no dominance condition needed; **(C)** window tightening attenuates **iff** $W_T C_T \le 1$, where $W_T \le 1$ is *proved* (from D1's clock equivalence and the monotone Voice stake path) and $C_T$ is *unsigned* — "equivalently $\partial_{r_T}\mathcal{S}_P/\mathcal{S}_P \le \Omega_{r_T}/(1-\Omega)$" holds **on average along the tightening path** (integrated over $[-T,-T']$), exactly in the infinitesimal limit, and is **false read pointwise**. Hypotheses: **fixed policies; A8 at each compared policy; $\mathcal{S}_P > 0$; L1; L2 (its own hypotheses travelling); D1; PE-$\Omega$ ($\partial_\kappa\Omega = 0$ at fixed policies — derivable, not assumed, and it fails in GE, which is C1's term); $\kappa$-differentiability of $M_P$ (no card hypothesis supplies this — carried in-proof); A($\tau$) at both compared policies with the $\bar\pi$ ruling; L3; A(br) (br-i)–(br-v) at the threshold pair; L4; the no-feedback timing; a smooth window interpolation for the local form; threshold-side smoothness (confirmed non-load-bearing)**. **No unconditional window sign is claimed.** | **PROVED** at fixed policies |
| **C1** | On a named region where $L_{\mathcal{R}} < 1$ and $g_r^{PE} > \mathcal{B}_r^{GE}$, the fixed-policy attenuation sign survives in equilibrium. The certificate theorem is **two-pass complete** — an adversarial proof-read PASS (0 FAIL, 13 repairs, 7 observations) and an independent statements-only re-derivation PROVED-WITH-CHANGES (a norm convention and two-sided openness of $\mathcal{R}_r$ added; at $J-1 \ge 2$ the bare $|\cdot|$ in $\mathcal{B}_r^{GE}$ is not well defined and a mismatched reading makes part (B) false) — and the executed 80-node certification returns a **nonempty region: 18 nodes certified**, slack $\eta_r$ from $0.0595$ (min) through $0.3467$ (median) to $1.7227$ (max), $L_{\mathcal{R}} \le 0.5008$ at every node. **The ledger decision is pending**, so the label does not move. | CONJECTURE |

Remaining aspiration, not a claim: C1 PROVED on a named nonempty region, NUMERICAL off-region,
dropped if the region is empty.

### Labels

**PROVED** — a complete proof, independently re-derived and proof-read. **NUMERICAL** — verified on a
grid by an executed, committed check script with committed output. **ESTIMATED** — an empirical
estimate with a standard error and a stated design. **CONJECTURE** — everything else, including
anything whose proof is deferred. Region-certified is not a fifth label: it is PROVED with the region
named in the hypothesis. Labels are never weakened by editing; only an executed check or an
independent re-derivation may move one.

### Three known facts on file

These are facts the record carries, not claims the model makes. They are the reason the labels above
are written with their conditions attached.

**1. The window analogue of L4 leg 3 is refuted at the O-1 calibration.** Since $W_T \le 1$ is proved,
the O-1 evaluations

$$W_T C_T = 1.06397 \,/\, 1.18373 \,/\, 1.13631 \qquad \text{at} \qquad \Omega = 0.037252 \,/\, 0.128950 \,/\, 0.285804$$

force $C_T \ge W_T C_T > 1$: window tightening *raises* pooled sensitivity at those nodes, the opposite
of leg 3's threshold-side direction. At $\Omega = 0.50$ the criterion holds ($W_T C_T = 0.37798$), with
the boundary located by bisection at $\Omega^\star \approx 0.3428$ ($k_D^\star = 1.28618$). Both
branches occur inside the maintained parameter set, which is the sharpest possible content of "no
unconditional window sign". Provenance: this is the referee's O-1 experiment run on the *repo* model
(the frozen manuscript's static structure, fixed cutoffs, partial equilibrium), re-executed in
`quality_reports/fixes/t1_o1_rerun_check.py` with every committed number reproducing to the last
printed digit; it is not the two-round build.

**2. The implemented two-round pooled cell FAILS A($\tau$) at baseline.** Two executed checks measure
the same gap, and both report it rather than smoothing it.

- `t2_l2_check.json`, check `l2_placebo_M_P_sign_A_tau`: **FAIL**. The enumerated pooled $M_P$ is
  *hump-shaped* in $\kappa$ — 10 of 18 increments positive, one sign change, peak near $\kappa = 0.55$
  — so $\partial_\kappa M_P \le 0$, the orientation A($\tau$)'s maintained $C_h \le 0$ would give, does
  not hold globally. The JSON's own words: a failed hypothesis about A($\tau$)'s orientation on the
  enumerated two-round pooled law, not a statement about L2.
- `t2_t1_check.json`, check `t1_block3_chord_magnitude`: **FAIL**. The residual
  $\big|\mathcal{S}_P - \Delta_m |A'_\kappa|\,|C_h(\bar\pi)|\big|$ is $0.006279$ ($0.6279$ premium
  percentage points) against a predicted $10^{-10}$ — the gap between the *enumerated* two-round pooled
  sensitivity and A($\tau$)'s three-atom closed form. (The companion clause of the same check passed:
  the ratio $|C_h|/\bar\pi^2$ is constant to $0.48\%$ between the two smallest $\bar\pi$ nodes, well
  inside the $5\%$ criterion.)

This is exactly the open question flagged under A($\tau$) above, now with a number attached: the
representation's support condition is not satisfied by the implemented pooled law at this calibration.
It is a failed hypothesis, not a wiring error — the same gap is measured analytically on the frozen
manuscript's four-atom law by `t2_l3_check.py` block 5b.

**3. L4's sign predictions hold numerically with zero violations.** `t2_l4_check.json` reports 10
checks, 0 failures. Across all 16 tightening steps and both windows: $\Omega$ rises at every step (0
violations, minimum increment $+0.02263$); $\bar\pi_{\mathrm{pr}}$ falls at every step (0 violations,
largest increment $-0.018766$); and $\mathcal{S}_P$ falls at every step (0 violations, largest
increment $-9.47 \times 10^{-5}$) — and, as the JSON notes, a single violation would be a failed
hypothesis rather than sampling error, because nothing in that computation is sampled. $\Omega$ and
$\bar\pi_{\mathrm{pr}}$ are flat in $\kappa$ to exactly zero across 71 grid points, which is what the
no-feedback timing predicts.

**What the pair of facts means.** The chord mechanism is **hypothesis-bound**: it needs A($\tau$), and
A($\tau$) is not satisfied by the implemented two-round pooled cell at baseline. The threshold
phenomenon is **not**: the reclassification legs of L4 are unconditional, and they hold numerically
without exception.

---

## 7. What this note does not claim

A global window-margin attenuation sign; $\kappa$-invariance of $J$; equilibrium uniqueness; a nonempty
GE-certified region *as a theorem* (the 18 certified nodes are an executed record, and C1's ledger
decision is pending); endogenous filing before the deadline; noisy or partially revealing flagged-round
trading; continuous-time execution; welfare or optimal rule design; that the frozen manuscript's hump
result survives; that the prior calibration ($\Omega \approx 0.037$) is economically meaningful; any
empirical value for $\omega_a$.

Three items are explicitly open:

1. **Whether the two-round pooled cell satisfies A($\tau$) — OPEN.** L3 proves the representation's
   entire remaining bite is the support condition, exhibits a one-round market that satisfies it and
   the frozen manuscript's own no-disclosure structure that does not, and names the weakest sufficient
   conditions. L3, L4 leg 3 and T1 Part B are all conditional on A($\tau$), so this is the largest
   single conditionality the ledger carries — and the executed checks of fact 2 above show it failing
   on the implemented law at baseline.
2. **Whether an equilibrium in which the blockholder chooses the fully separating plan exists on a
   given calibration — OPEN, and P1-adjacent.** A7′ menus are fully separating on the flagged set, so
   the burden did not disappear when A7 satisfiability was resolved; it *moved* to incentive
   compatibility, which P1 does not settle.
3. **The window-margin analogue of L4 leg 3 is refuted at the O-1 calibration** (fact 1 above).

---

## 8. What v4 takes from `draft_v2`, what it simplifies, what it drops

The frozen manuscript `draft_v2.tex` is a record the supervisor has seen; it is not edited and it is
not cross-referenced here. The table below describes its objects rather than citing them.

| `draft_v2` object | Verdict | What carries over, what changes |
|---|---|---|
| Four-action structure: Exit, Hold, Quiet Voice, Public Voice, with weakly ordered cutoffs $(k_1,k_0,k_D)$; and the dominance lemma making the four-action menu a result rather than an assumption (engaged exit and silent buy are never chosen). | **REUSE** | Becomes the *special case* of the v4 ordered plan menu: $\mathcal{J}$ finite and ordered with $J \ge 3$, cutoff vector $k = (k_1,\dots,k_{J-1})$, which maps to $(k_1,k_0,k_D)$ exactly when the menu is the four named actions. What changes: menu elements are now *complete contingent plans* over the calendar $d = 0,\dots,H$, not single one-shot $(q,a)$ pairs, and A3's single crossing is stated for adjacent plans. The dominance argument survives as the reason the menu is ordered and finite. |
| Brouwer existence architecture: boundedness of best responses, the self-map and order-preservation lemma, and existence of a monotone equilibrium by Brouwer on a nonempty compact convex $\Theta$. | **REUSE** | Reused whole as P1's architecture: $\Theta$ compact, ordered, convex; $\mathcal{T}$ continuous $\Theta \to \Theta$; $k^\star = \mathcal{T}(k^\star;\vartheta)$; collapse faces permitted (the manuscript's own baseline collapses Hold). What changes: the fixed point ranges over plans; off-path beliefs are limits of full-support perturbations *over plans*; and the inner pricing fixed point is no longer an assumption (see the A5 row). |
| The (C\*) chord condition $\mathcal{C}(\bar\pi) = h(0) - 2h(\bar\pi/2) + h(\bar\pi)$, and the lemma signing the posterior/pricing channel under it. | **REUSE** | Is v4's $C_h(\bar\pi)$, same expression, same maintained orientation $C_h \le 0$ with $|C_h|$ weakly increasing in $\bar\pi$. What changes: in `draft_v2` it selects hump versus trough in $\kappa$; in v4 it is the magnitude that drives pooled sensitivity through L3's exact identity $\partial_\kappa \mathbb{E}_\kappa[h] = A'_\kappa C_h(\bar\pi)$, and the A($\tau$) representation that licenses that identity is stated as a restriction whose support condition is open. |
| The tender-game microfoundation of the premium wedge (the disagreement-node continuation deriving the appropriability coefficient $\lambda = 1 - q(1-\gamma)\psi$ and the resulting wedge). | **REUSE** | Kept as the *input* that supplies $(m_0,m_1)$. v4 takes $m_0, m_1$ as primitives with $m_1 > m_0$ and $m_0 \ge 0$ and does not re-derive them; the tender game is where those numbers come from and why $\Delta_m > 0$ is not free. Its symbols are reserved and unavailable: bare $\lambda$ is the appropriability coefficient, $\psi$ is pivotality. |
| The GE dominance-check pattern: contraction modulus $L$ along the path, an inversion-free Neumann bound $\bar B$, pointwise dominance off a ball plus a ball-integral condition, a certified interval, and a counterexample showing the global claim false. | **REUSE** | Is C1's precedent. $\mathcal{B}_r^{GE}$ is the *cross-derivative* analogue of $\bar B$; $\eta_r = g_r^{PE} - \mathcal{B}_r^{GE}$ is the slack; certification is node by node on a named region, and an empty region is a reportable outcome that would drop C1. What changes: the object bounded is a cross-derivative in $(\kappa,r)$ rather than a single-argument profile, and the strictness coordinate $r_T = -T$ is not differentiable because the window is an integer. |
| Stake-triggered disclosure as the market's partition, with the flag a function of the order ($D = \mathbf{1}\{q = +1\}$: a buy cannot be concealed). | **REUSE** | The idea that the rule *is* the partition is the whole v4 position. What changes is the trigger: $D = \mathbf{1}\{a=1,\ c(\tau)+T \le H\}$, a stake threshold plus a filing window on a business-day calendar, with D1's clock equivalence $f \le H \iff B(s,H-T) \ge \tau$. The window $T$ becomes a genuine primitive instead of a flag that is either on or off. |
| Assumption (A2)'s flat boundedness of prices and payoffs. | **SIMPLIFY** | Replaced by A2′: finiteness clauses kept verbatim; boundedness weakened to local boundedness plus integrability $\mathbb{E}[\max_j |U_j|] < \infty$. The flat bound was *false* in this model ($v$ Gaussian, flagged region unbounded in $s$), and no proof ever used it. |
| Assumption (A5)'s inner pricing regularity (existence, uniqueness and continuity of the price fixed point, assumed, with a $\delta/\sigma_\xi < 1/\phi(0)$ style regularity condition). | **SIMPLIFY** | Demoted to a theorem under $m_0 \ge 0$: the pricing map is strictly decreasing in $P$ wherever $\bar m \ge 0$ and crosses the identity exactly once. A5 survives only as its continuity clause, read as a measurably selected family because the flagged information sets are continuum-indexed. Three independent confirmations, including executed counterexamples that produce zero roots and three roots once $m_0 < 0$. |
| The discount factor $\delta$ inside the pricing fixed point $P = \delta[(1-p)\hat V + p(P+\bar m)]$, and the sensitivity analysis around it. | **DROP** | v4 prices are undiscounted conditional expectations $P(\mathcal{I}) = \mathbb{E}[Y \mid \mathcal{I}]$. The regularity work $\delta$ was doing is done instead by $m_0 \ge 0$. |
| The one-round pooled posterior: $\pi(X,0)$ in closed form from a single order-flow draw $X \in \{-2,-1,0,1\}$ with $p_0 = 1-\kappa$, $p_1 = \kappa/2$ and the action weights $(\omega_E,\omega_H,\omega_Q)$; Hold and Quiet Voice pooling because both trade $q = 0$. | **DROP** | Replaced by a pooled history $\mathcal{H}_H^P$ over $H+1$ business days with plans, $\Gamma$-coarsened increments and a flag that can land mid-calendar. The closed-form posteriors do not survive the calendar. Consequential: L3 shows the manuscript's own no-disclosure structure (informed mark $\bar z$) yields a *four-atom* pooled law, two of whose atoms move with $\kappa$, so it lies outside A($\tau$) — the one-round posterior is not merely superseded, it is a named example of the representation failing. |
| The hump headline: $\Delta^{\min}(\kappa)$ single-peaked in liquidity, as the conditional-hump proposition and the paper's first main result. | **DROP** | Not claimed anywhere in v4; the card states outright that it does not claim the hump survives. The v4 headline is the partition and the attenuation factorisation $\mathcal{S} = (1-\Omega)\mathcal{S}_P$, not a shape in $\kappa$. Note the hump has not been *refuted* either: the enumerated two-round $M_P$ is itself hump-shaped in $\kappa$ at baseline (peak near $0.55$) — it is simply no longer the result being sold, and its role now is to break A($\tau$)'s orientation clause. |
| The unconditional attenuation claim: $|\partial\Delta^{\mathrm{act}}/\partial\kappa|$ decreasing in $\omega_P$, asserted as a monotone consequence of shifting mass to the disclosed cell, with no composition term and no margin distinction. | **DROP** | Split and conditioned. The weight effect is kept and proved ($W_T \le 1$, $W_\tau$ likewise), but the composition effect is a separate ratio: T1(B) gets threshold attenuation *unconditionally* because *both* $W_\tau$ and $C_\tau$ lie in $[0,1]$; T1(C) makes the window margin an **iff**, $W_T C_T \le 1$, with $C_T$ unsigned — and the O-1 numbers put three of four calibrated nodes on the *failing* side. An unconditional window sign is not available. |
| Equilibrium uniqueness as a numerical regularity (a 30-seed multistart converging to one fixed point per $\kappa$, labelled a regularity rather than a theorem). | **DROP** | v4 does not claim uniqueness at all, as a theorem or as a regularity. The multistart survives only as an existence diagnostic in the check scripts, and it does not always clear its own binding criterion (§9, P1). |
| The welfare apparatus: transfer netting and the present-value form of total surplus, the liquidity planner's wedge $\kappa^{\ast}$ versus $\kappa^{\dagger}$, the disclosure-threshold planner, the first-best benchmark. | **DROP** | Out of scope by the card's own statement: no welfare, no optimal rule design. Note this is also why a bare $W$ is unavailable as a symbol — it was total surplus there, and it is the weight-effect ratio $W_\tau, W_T$ here. |

---

## 9. Evidence

### The check-script inventory

Eight scripts, each with committed JSON output, in `quality_reports/fixes/`. Verdicts are as the JSON
reports them, failures included. "Wiring" and "substantive" are the design's own classification: a
wiring check runs both sides of an identity through the same enumeration and is therefore *not*
evidence for the result, only for the code.

| Script | Verdict | What it establishes, and what it does not |
|---|---|---|
| `t2_d1_check` | **PASS** — 9 checks, 0 FAIL, 1 vacuous | Clock equivalence by three independent routes (date-by-date scan, one evaluation at $H-T$, closed-form crossing date) agreeing to exactly $0$; partition exclusivity and exhaustion at $0$ residual; the $T = H$ corner; robustness at $H = 12$. 50 nodes. *Vacuous*: the $Q^F$ window-monotonicity check, because $\max Q^F = 0$ at the implemented calibration — the flagged round carries no residual order there, so the prediction has nothing to bite on. |
| `t2_l1_check` | **PASS** — 4 checks, 0 FAIL | Decomposition residual $\Delta^{\mathrm{act}} - (\Omega M_F + (1-\Omega)M_P)$ at $0$, both degenerate endpoints, and the non-evaluability of the null-cell average. *All four are classified WIRING by the design*: both sides run through the same enumeration, so the residual is machine noise by construction and is **not evidence for L1**. |
| `t2_l2_check` | **FAIL** (1 of 5) | L2's own content passes exactly: the flagged range of $M_F$ over 19 $\kappa$ values is $0$ and its $\kappa$-derivatives are $0$ — the flagged path never touches the $\kappa$-dependent array. Two placebos confirm the pooled side does move. **The failure is the fifth check**, an *ancillary* A($\tau$)-orientation placebo: see §6, fact 2. It is a failed hypothesis about A($\tau$) on the enumerated pooled law, not a failure of L2. |
| `t2_l3_check` | **PASS** — 10 checks, 0 FAIL | The derivative identity, the mean-value form $C_h = \tfrac14 \bar\pi^2 h''(\zeta)$, the quadratic rate as $\bar\pi \downarrow 10^{-4}$, the affine-kernel zero-chord case, and three failure witnesses (a tent kernel with no root, the four-atom Example B gap, an unbounded-$h''$ witness). *Scope*: it runs on the three- and four-atom analytic laws and the standalone chord module — it does *not* enumerate the two-round model, so it verifies L3's mathematics, not A($\tau$)'s applicability. |
| `t2_l4_check` | **PASS** — 10 checks, 0 FAIL | All three sign legs with **zero violations** over 16 tightening steps (§6, fact 3); the exact reclassification identity at $10^{-16}$; flatness in $\kappa$ at exactly $0$ over 71 nodes; the $\tau$-grid spanning a ninefold range in $\omega_a$; L3's quadratic corollary within $2.1\%$. Prediction 5 (the size of the $A'_\kappa$ channel) is *reported, not gated*, by the request's own instruction: median absolute residual $0.0352$, max $0.1213$. |
| `t2_p1_check` | **FAIL** (1 of 10) | Nine substantive checks pass: inner-root single crossing and transversality, the flagged family single-valued with the right slope, sequential optimality of the flagged component, both cells on path, the threshold reformulation, monotonicity of $\Omega$ in $(\tau,T)$, and *existence at the core nodes* under the full 30-seed multistart. **The failure is the grid sweep**: 23 of 27 policy nodes met the binding payoff-scale criterion ($10^{-9}$) and 4 did not, at best payoff scales $1.5\times10^{-3}$, $1.1\times10^{-3}$, $4.0\times10^{-4}$, $3.1\times10^{-4}$ — all four at extreme liquidity $\kappa \in \{0.15, 0.85\}$ on policies whose pooled prior engagement share is exactly zero (every Voice type files). Seed coverage is *ruled out* as the cause: the check re-ran all four nodes at the full 30 seeds and found identical best residuals, with most seeds landing on the same cutoff vector. All 27 nodes do converge on the cutoff-scale criterion. The cause is undiagnosed — candidates are a failure of A3's single crossing at those corners (the adjacent-plan payoff gap is a sawtooth on this menu; single crossing is a calibration fact, not structural) or a genuine boundary non-existence outside P1's hypothesis set; either way P1's theorem is untouched (its hypotheses include A3) and the four nodes are named, not smoothed. |
| `t2_t1_check` | **FAIL** (1 of 9) | The factorisation $\mathcal{S} = (1-\Omega)\mathcal{S}_P$ holds pointwise to $1.2\times10^{-16}$ and in total variation to $2.2\times10^{-19}$; $\Omega$ is flat in $\kappa$ at $0$ residual; the threshold margin, the window margin, the O-1 benchmark and the composition factors all pass; $H=12$ robustness passes. **The failure is block 3**, the chord-magnitude route: see §6, fact 2. One check is *vacuous* (the local form, which needs a smooth window interpolation the integer calendar does not provide). |
| `t2_c1_region_check` | **PASS** — 12 checks, 0 FAIL, region *nonempty* | 80 nodes ($8\ \kappa \times 5\ \tau \times 2\ T$), 2.9 hours of wall time. Two gated verdicts, both PASS with 0 violations: the bound contains the four-corner re-solve remainder at the 8 validation nodes (max ratio $0.511$), and it contains the implicit-function remainder at all 80 (max ratio $1.0$). **18 nodes certified**, all at $T = 5$ and the upper three $\tau$ percentiles; $\eta_r \in [0.0595,\ 1.7227]$, median $0.3467$; $L_{\mathcal{R}} \in [0.264, 0.501]$ with no node at $L \ge 1$. *Failure attribution*, recorded not hidden: 56 nodes have $g_r^{PE} = 0$ to $10^{-10}$ because the implemented legal clock quantises the crossing date, so $\Omega(\tau)$ is locally constant and the cross-derivative vanishes identically there; 4 are positive but dominated; 2 are negative; 40 nodes (all $T = 10$) are degenerate on flagged mass below $0.01$. The sharper, non-inversion-free bound would certify 22 rather than 18 — reported as a measure of the Neumann step's price, and certifying nothing. No tolerance was weakened to make the region nonempty. |

**Provenance caveat.** Seven of the eight scripts record the card stamp *2026-08-20* in their
provenance block; only `t2_c1_region_check` was run against the 2026-08-21 stamp. The card changes
between those stamps are hypothesis-explicitness moves, not model changes, but the mismatch is on the
record and is not papered over here.

### The `numerical_v4` package: smoke facts

The implementation is `numerical_v4/` (modules `params`, `menu`, `policy`, `flagged`, `pooled`,
`premium`, `solver`, `smoke`), with committed output in `numerical_v4/smoke_output.txt`. At the smoke
configuration $H = 10$, $T = 5$, $M = 2$ order marks, $J = 3$ plans, $b_0 = 0.03$, $\bar b = 0.1$, seed
$\tau = 0.05$ (the statutory 13D 5%):

- **Enumeration gate**: $4{,}194{,}304$ histories, $826{,}686$ feasible, $N_\theta = 12$; feasible
  $\times\ N_\theta = 9.92 \times 10^6$ against a gate limit of $10^8$. PASS. One evaluation takes
  $0.372$ s; the whole smoke runs in $64.8$ s.
- **$\tau$ freezing**: the seed equilibrium is $k = (1.31246481,\ 1.41888743)$ with
  $|k - \mathcal{T}(k)| = 1.34 \times 10^{-11}$; the median Voice $b^*(s)$ is $0.09076406$, and $\tau$
  is frozen there at every node.
- **Baseline equilibrium** ($\kappa = 0.5$): $k = (1.2405757283,\ 1.5310222869)$; outer residual
  $2.60 \times 10^{-11}$ on the diagnostic cutoff scale and *exactly zero* on the binding payoff scale.
- **Masses**: $\Omega = 13.84\%$, $\Pr(a=1) = 22.63\%$, $\omega_a = 61.15\%$,
  $\bar\pi_{\mathrm{pr}} = 10.21\%$. *Note $\omega_a = 61\%$ here is a property of the calibration, not
  an estimate*: the card claims no empirical value for $\omega_a$, and the empirical anchor for it is
  absent from the literature.
- **Premium objects**: $M_F = 0.5528$ pp, $M_P = 0.2228$ pp, $\Delta^{\mathrm{act}} = 0.2685$ pp; L1's
  decomposition residual is $0$ (wiring).
- **Price path**: mean run-up $R = 389.18$ bp, mean filing jump $J = 2590.52$ bp, D1 identity residual
  $0$ against a $10^{-12}$ tolerance.
- **A7 certificate**: passes — minimum $|db^*/ds|$ on the flagged set is $2.20 \times 10^{-4}$ (gate
  $10^{-8}$), no flat sub-intervals, no $(B^F,Q^F)$ collisions, no cross-plan collisions, 10 flagged
  atoms of 19.
- **Numerical hygiene**: pooled mass error $2.2 \times 10^{-16}$; maximum inner price residual
  $2.2 \times 10^{-16}$; maximum $b^*$ inversion error $5.9 \times 10^{-14}$; GL-20 versus GL-40
  quadrature on $M_F$ differing by $2.6 \times 10^{-18}$; **zero multiple-root nodes** anywhere, which
  is the structural consequence of $m_0 \ge 0$.
- **L2 verdict, substantive**: the range of $M_F$ across the frozen-policy $\kappa$ sweep is *exactly*
  $0$.
- **The shape that breaks A($\tau$)**: $M_P$ is hump-shaped in $\kappa$ with its peak near
  $\kappa = 0.55$, so $\mathcal{S}_P = |\partial_\kappa M_P|$ is V-shaped about that peak, ranging from
  $4.99 \times 10^{-3}$ to $2.66 \times 10^{-1}$ premium pp per unit $\kappa$; at the peak
  $\mathcal{S} = (1-\Omega)\mathcal{S}_P = 6.37 \times 10^{-2}$.
- **Chord module**: $C_h \le 0$ at every $\bar\pi$ tested, and $|C_h|/\bar\pi^2$ settles at
  $\approx 0.2219$ as $\bar\pi$ falls from $10^{-1}$ to $10^{-4}$ — L3's quadratic rate, on the
  standalone route.
- **One structural caveat**: $\max Q^F = 0$ at this calibration. The flagged round exists in the timing
  and in the code, but carries no residual order here, which is why the $Q^F$ monotonicity check is
  vacuous.

---

*Sources, all in the `v4-theory` worktree: `research/model_v4/MODEL_CARD.md` (stamp 2026-08-21,
post-ledger regeneration) for §§1–6; `research/model_v4/LABEL_LEDGER.md` for the labels;
`research/model_v4/proofs/` and `research/model_v4/rederive/` for the two-pass evidence chains;
`research/model_v4/HANDOFF_sign.md` and `quality_reports/fixes/t1_o1_rerun_check.json` for the O-1
numbers; `quality_reports/fixes/t2_*_check.json` for the check inventory;
`numerical_v4/smoke_output.txt` for the smoke facts.*
