# The Two-Round Blockholder Disclosure Model — a standalone model note

**v4 theory lane, ticket 30 (T2j). Card stamp 2026-08-29, polish-pass audit + wording repairs +
off-path verification + A3 curation.**

Markdown mirror of `research/model_v4/model_v4.tex` (same content, same order).

This note states the v4 two-round model in one place: primitives, timing, the partition the
disclosure rule induces, the equilibrium notion, the standing hypotheses, and the eight-result
ledger with its honesty labels. It then records what the v4 model takes from the frozen manuscript
`draft_v2.tex`, what it simplifies, and what it drops; and it lists the executed evidence, failures
included. Every statement of content here is transcribed from `research/model_v4/MODEL_CARD.md`
(**Version stamp: 2026-08-29 · polish-pass audit + wording repairs + off-path verification + A3
curation · commit `<pending-orchestrator-hash>`.**) and
`research/model_v4/LABEL_LEDGER.md`. The card is the single source of truth: where a proof file
and the card differ, the card wins. The conditionality attached to each result is not decoration.
It is the result.

Six card events since the 2026-08-23 stamp are carried below. **P1 is restored to PROVED** on
2026-08-25 on its ticket-35 repair — the statement amended to the hypotheses the proof actually
needs (A7-J in place of A7′, the continuation-cost clause, the $\kappa$ boundary handled by
extension) and the two-pass gate satisfied afresh by an adversarial proof-read PASS and an
independent statements-only re-derivation PASS-WITH-CHANGES, both 2026-08-25 and both by agents
who did not write the proof. **A($\tau$)'s block gained ticket 33's dated evidence note** on
2026-08-25: the support condition FAILS at the implemented calibration. **On 2026-08-27** the A6
panel ruling (Austin-authorized, opposed-brief panel) added dated evidence notes to A6 and A3 and
a fourth open item — answered in substance, locus corrected, **no label moves**. **On 2026-08-28**
two standing follow-ups landed (again no label moves): the A6 panel's decisive probes are curated
into executed t2 checks (§5's A6 note, curation note — two wordings corrected, the numbers intact)
and the ticket-34 candidate account is swept over its other three nodes — the account HOLDS at all
three (§5's A3 note, sweep note). **Later the same day** GPT Pro's re-review returned and was
audited (`threads/2026-08-28_gpt_rereview.md`, filed verbatim;
`threads/2026-08-28_gpt_rereview_audit.md`, finding-by-finding): **all eleven labels STAND, zero
demotions**; the audit upheld three wording-grade card repairs, applied at this stamp — the P1
row's A5-continuity clause corrected in place, a §5 A5 evidence note, the A($\tau$) note's lead
sentence — again **no label moves**. **On 2026-08-29** the polish round closed and the off-path
verification landed, again **no label moves**: the polish response and its in-house audit are
filed (`threads/2026-08-29_gpt_p1_polish.md`, `threads/2026-08-29_gpt_p1_polish_audit.md`; 19
findings), the audit's wording repairs P1-R36–R39, R41–R42 and R46–R53 are applied to the proof
and independently verified, as are the auditor's same-day seam follow-ons P1-R54–R56, drafted
after application review and filed as `threads/2026-08-29_p1_polish_audit_addendum.md`;
P1-R43/R44 pending the two-pass gate; P1-R45 behind the F5 route; and the
F5 demotion question recorded OPEN on the P1 row, before Austin); the off-path-family
verification (20 gates, 0 failed) amends the A6 and A3 notes — the `OFF_PATH_EPS` sentence
superseded (Amendment A), locus (i) scoped under both off-path families (Amendment B), the
`type_reference` gap recorded (Amendment C), the Step-18 pointer corrected — and the A3 curation
note records the executed `t2_a3_ordered_plans_check` (17 gates; both loci reproduce), with the
A3 note's bare selection-set symbol replaced by prose.

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

For the general-equilibrium dominance-and-contraction node: $k = (k_1 \le \dots \le k_{J-1})$ is the cutoff vector on the
compact ordered polytope $\Theta$ with parameter vector $\vartheta$; $\mathcal{T}(k;\vartheta)$ the
outer best-response map; $L_{\mathcal{R}} = \sup_{\mathcal{R}} \lVert D_k \mathcal{T} \rVert$ the
contraction bound; $r_\tau = -\tau$, $r_T = -T$ the strictness coordinates (higher $r$ = tighter);
$g_r^{PE} = -\mathrm{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{act}}$
the direct fixed-policy attenuation margin;
$\bar k_x = |\partial_x \mathcal{T}|/(1-L_{\mathcal{R}})$ and $\bar k_{\kappa r}$ the inversion-free
derivative bounds;

$$\mathcal{B}_r^{GE} = |\Delta_{\kappa k}|\bar k_r + (|\Delta_{kr}| + |\Delta_{kk}|\bar k_r)\bar k_\kappa
+ |\Delta_k|\bar k_{\kappa r}, \qquad \eta_r = g_r^{PE} - \mathcal{B}_r^{GE}$$

the GE remainder bound and the slack on a dominance-and-contraction region $\mathcal{R}_r$.

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

*Evidence note added 2026-08-27 (A6 panel, in passing — a separate finding, deliberately not folded
into the A6 note).* At the implemented calibration **A3 itself fails, at two independently-found
loci, upstream of A6.** (i) At $(\kappa{=}0.5, \tau_{50}, T{=}5)$ with $k_2$ on an **open set** above
cell edge 6 (verified at offsets $10^{-9}$ through $2\times10^{-2}$), $U_V - U_H$ has **three strict
sign changes** ($s = 1.5754434 / 1.5833333 / 1.5902426$; middle excursions
$2.4$–$2.8\times10^{-4}$ against a $10^{-9}$ payoff tolerance), the pointwise argmax runs H,V,H,V
single-valued on each interval, so **no weakly increasing selection exists** — the
weakly-increasing-selection set is empty and Step 13's $\mathcal T$ is **undefined** there, not
merely discontinuous. (ii) At $(\kappa{=}0.15, 0.05, 5)$ — a ticket-34 UNRESOLVED node — the argmax
reverses **VOICE $\to$ HOLD** across cell edge $s = 1.659062163$ at **both** located fixed points:
the preferred plan decreases in $s$. The route is the $s$-direction step of $U_{VOICE}$ ($n(s)$ is
integer-valued — Step 15(i) / WHERE IT FAILS 4's card-legal counterexample, instantiated by the
solver's own `N_GRID` note) interacting with the off-path price snap. **No conflict with ticket
34's "the A3 and A6 proxies pass at every achieving seed"**: those proxies are local screens — the
A3 proxy tests residual slope signs at the two candidate cutoffs and the A6 proxy tests
$\Theta$-corner non-pinning at the closest seed (`t2_p1_fournode_recheck.py`) — and neither measures
argmax monotonicity over $s$ nor continuity of $\mathcal T$ in $k$, so both are silent on these
findings. **Candidate mechanical account of ticket 34's four UNRESOLVED nodes**, on file and
UNCHECKED beyond the one node probed: at the $\kappa = 0.15$ node one fixed point sits exactly on
the edge where $U_H - U_V$ **jumps through zero without crossing it**, and the panel's residuals
(payoff $3.06\times10^{-4}$–$1.77\times10^{-3}$ at cutoff residuals of $10^{-11}$-grade) **bracket
ticket 34's recorded range exactly**; the $k$-direction jump mechanism does **not** explain those
nodes (no proximity correlation — the substantiate panellist's own recorded negative). *Swept
2026-08-28 over the other three nodes (`quality_reports/fixes/t2_t34_account_sweep.py`/`.json`,
pre-registered three-way rule): the account **HOLDS at all three**. At $(\kappa{=}0.15, 0.075, 1)$
and $(\kappa{=}0.85, 0.075, 1)$ a located fixed point sits on an $n(s)$ cell edge —
$1.460178993$ (offset ${\sim}10^{-13}$, where 10 of the 30 recheck seeds land) and $1.517932397$
(offset ${\sim}10^{-12}$, reached by **no** seed and found only by the direct edge test) — with
$U_H - U_V$ **jumping through zero without crossing**. Neither pin is its node's achieving basin:
their payoff residuals, $1.398\times10^{-3}$ and $1.314\times10^{-3}$, sit above the recorded bests
$1.059\times10^{-3}$ and $3.061\times10^{-4}$, each equalling the larger one-sided jump to at most
$2.7\times10^{-4}$ relative — a recorded, non-gating quantity. At $(\kappa{=}0.85, 0.05, 5)$ **no
pin was found at any candidate edge in $[1.29, 2.11]$**; the achieving basin's worst deviation
instead sits in the cell immediately above edge $1.583333333$ ($0.0250\,\sigma_s$ from it), where
the same jump through zero occurs, at a deviation/jump ratio of $0.366$ — inside the pre-registered
factor of 3. Every pin is $n(s)$-family; the $\tau$-crossing pullbacks yielded none. Probe 5(b)'s
distances replicate ($0.0258/0.0437/0.0295\,\sigma_s$ vs $0.026/0.044/0.030$). **No node yields a
second independent fixed point, so node 15's residual bracket does not recur** — criterion (ii)
rests on reproduction of every recheck basin alone. Diagnostic evidence at one calibration;
existence at these nodes stays neither claimed nor denied.* No label moves — A3 is a hypothesis; P1
stays PROVED as a conditional. Records: the same panel files as the A6 note.

*Curated 2026-08-29 into a dedicated executed check
(`quality_reports/fixes/t2_a3_ordered_plans_check.py`/`.json`, 17 gates pre-registered on this
note's numbers and the panel's filed values — one gate's comparison form restructured after run 1
to the source's 3 s.f., declared in `known_discrepancies`; no measured number moved;
deterministic, re-run identical modulo the timing field): both loci **REPRODUCE** — (i) three sign
changes at all five ladder offsets ($10^{-9}$, $10^{-4}$, $10^{-3}$, $5\times10^{-3}$,
$2\times10^{-2}$), located at the filed $+10^{-9}$ offset at 1.5754434 / 1.5833333 / 1.5902426
(7 dp exact), argmax H,V,H,V strictly single-valued, the weakly-increasing-selection set empty;
(ii) the VOICE $\to$ HOLD reversal and all twelve filed payoffs at both fixed points, the pinned
residuals bit-exact. One wording note, numbers intact: the quoted middle excursions reproduce
($2.80\times10^{-4}$ / $2.40\times10^{-4}$ at their filed precision) but are the panel's
6001-point grid maxima — refined per-interval maxima $3.07\times10^{-4}$ /
$2.69\times10^{-4}$, so the single-crossing failure is larger than recorded. No label moves — A3
is a hypothesis.*

*Off-path-family scope note added 2026-08-29 (independent verifier; probes
`quality_reports/fixes/p1_route_probes_2026-08-29/v_offpath_locus1_ladder.py`/`.json`, 10 gates,
0 failed, whose shipped rows reproduce this note's counts at every ladder offset and its three
$7$-dp crossing locations exactly).* Locus (i)'s failure is recorded **under the implemented
off-path family**, whose floor is uniform across dead types where Step 9(b)'s $\Lambda_u$ is
mass-proportional (A6 note, 2026-08-29 verification note). Under a **Step-9(b)-faithful
mass-proportional family** the failure at this node is **relocated, not removed**: over the
offsets quoted above ($10^{-9}$ through $2\times10^{-2}$) the count falls to **one** sign change
and the pointwise argmax becomes **weakly increasing**, so the weakly-increasing-selection set is
nonempty there — but at offsets $4\times10^{-2}$ through $10^{-1}$, where the **shipped** family
gives one, it is **three**, with the argmax **non-monotone across the crossings** in the same
$\ldots$V,H,V pattern, so the weakly-increasing-selection set is empty on an open set of $k_2$ at
this node under **both** families. The two families are **exactly complementary** over the eleven
offsets tested and flip at the **same** boundary, between $+3\times10^{-2}$ and
$+4\times10^{-2}$: the family does not switch the failure off, it swaps which half of the ladder
carries it. The driver is the **reference measure**, not the perturbation's continuity: a
continuous fixed-$t$ blend with a uniform reference tracks the shipped switch and one with the
Step 9(b) reference tracks the mass-proportional switch, at every
$\varepsilon\in\{10^{-14},10^{-9},10^{-6}\}$. **Locus (ii) is untouched**: the VOICE $\to$ HOLD
reversal holds at **both** located fixed points under the shipped family, under the exact Step
9(b) family at both scales, and under every family at $\varepsilon=$ `OFF_PATH_EPS`, with all ten
family $\times$ scale rows reversing at the pinned point (`v_offpath_locus2_node15.py`/`.json`,
5 gates, 0 failed) — **A3's verdict at this calibration does not depend on the family.**
`t2_a3_ordered_plans_check.py`/`.json` **remains valid as the shipped-family record and nothing in
it is withdrawn.** No label moves — A3 is a hypothesis; P1 stays PROVED as a conditional.

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

*Evidence note added 2026-08-28 (re-review audit finding 1;
`threads/2026-08-28_gpt_rereview_audit.md`).* **The retained continuity clause is an assumption
about the *composed* family, and it is measured to fail at the implemented calibration.** Two
continuities must be kept apart, because only one of them is a theorem. (i) Continuity of the
inner root **in its belief summaries** $(\hat v,\pi)$ follows from $m_0\ge0$ —
`proofs/P1_proof.md` Steps 7–8, two independent routes on file. (ii) Continuity of the
**composition** $k\mapsto(\hat v,\pi)\mapsto P$ **in the cutoff vector** is what the clause above
retains, and no step derives it: the $k$-dependence runs through the conditioning, not through the
pricing map (`proofs/P1_proof.md` Step 7, closing paragraph). The A6 note below measures exactly
that composition jumping — the price system is discontinuous on
$\bigcup_h\partial\{k:\Lambda_k(h)>0\}$, with $\mathcal T_2$ jumps of $6.33\times10^{-3}$ /
$1.09\times10^{-2}$ / $2.83\times10^{-2}$ at $(\kappa{=}0.5,\tau_{50},T{=}5)$
(`quality_reports/fixes/t2_a6_edge_jump_check.json`). Clause (ii) and A6's continuity clause
therefore fail together, at one locus, for the declared construction. **Where each citing row
stands:** D1 cites A5 for a unique competitive price at every public history and L2 for one
flagged fixed point — the existence/uniqueness content, released above to $m_0\ge0$; L1 cites it
to pin *the* version of $\mathbb E[Y\mid\mathcal I]$. **No result row consumes clause (ii)**, so
no row is touched. **No label moves and none is licensed** — A5 is a hypothesis.

**A6 Compact outer self-map.** All best-response cutoffs lie in a common compact ordered polytope
$\Theta$; $\mathcal{T}$ is continuous and maps $\Theta$ into itself.

*Evidence note added 2026-08-27 (A6 panel, Austin-authorized; ruling at §7 item 4).* Two
opposed-brief agents (substantiate / defuse) examined the re-derivation's withheld change 6 (N11)
and **converged**; the orchestrator's adjudication is on file. **The continuity clause fails for the
declared construction, and the locus is not the one N11 named.** All $k$-dependence of $U_j$ runs
through the pooled price vector (the flagged layer is $k$-free under A7-J), and Step 9(b) gives
Bayes where $\Lambda_k(h) > 0$ but a $k$-free plan-uniform posterior on the frontier, so the price
system can be discontinuous exactly on $\bigcup_h \partial\{k : \Lambda_k(h) > 0\}$ — a set inside
(the finitely many **cell-edge hyperplanes** $\{k_i = a\}$) $\cup$ (the **collapse faces whose dying
plan is the sole generator** of some reachable pooled history). The jump **reaches $\mathcal T$ with
non-vanishing weight**: $U_j$ integrates those prices against the deviator's own noise law (weight
$\ge \min(\kappa/2, 1-\kappa)^{d+1}$, independent of the dying plan's population mass), so the
vanishing-mass defusal is **refuted — by both panellists, independently**; the
largest-weakly-increasing-selection tie-break is pointwise in $k$ and passes the jump through; and
no $k$-independent perturbation family reconciles the limits (at fixed $n$ the system is continuous
in $k$; the discontinuity is created only as $t_n \to 0$ — an order-of-limits problem the family
choice cannot fix). On collapse faces proper: for $J \ge 3$ menus where a middle plan owns a
reachable **exclusive** pooled history entering some $U_j$, the interior limit
$\mu_v + \beta(c - \mu_v)$ varies over the face while any $k$-free family supplies one constant, so
continuity fails at **every face point but at most one** (continuum-face lemma — single-pass panel
derivation, **not gate-checked**). The implemented menu is **not** in that class: Exit and Hold pool
perfectly in order flow, and its Hold-collapse face is **measured clean** (pooled prices within
$4.4\times10^{-16}$ and $\mathcal T$ bit-identical as $k_1$ sweeps to full collapse). At the
implemented calibration the failure is live at the **interior $n(s)$ cell edges** instead: measured
$\mathcal T_2$ jumps of $6.33\times10^{-3}$ / $1.09\times10^{-2}$ / $2.83\times10^{-2}$ across
$\le 2\times10^{-9}$ steps in $k_2$ at $(\kappa{=}0.5, \tau_{50}, T{=}5)$ — **measured independently
by both panellists with separate scripts, agreeing to 3 s.f.**, the belief snap matching the
Step 9(b) prediction to $\sim10^{-8}$, surviving-type controls $\sim3\times10^{-9}$, robust at
$1000\times$ the breakpoint-merge tolerance; at $(\kappa{=}0.15, 0.05, 5)$ jumps reach $0.16$ and a
diagonal crossing of $\mathcal T_2$ is **destroyed**. A chamber-interior
$\Theta^+ = [1.23, 1.245] \times [1.5253, 1.5506]$ (exhibited) is compact, self-mapping and jump-free
at the baseline — Brouwer runs verbatim on it and it contains $k^\star$ — but it is **not the
$\Theta$ Steps 13–14 construct** (they build from the bracket $[s_{lo}, s_{hi}]$, which contains the
edges), cannot be exhibited without approximately locating the fixed point first, and **no such
chamber exists at the $\kappa = 0.15$ node**, where a fixed point sits exactly on the edge
$k_2 = 1.659062163$. **No label moves and none is licensed** — A6 is a hypothesis; P1 stays PROVED
as a conditional, in the A($\tau$) pattern: what is on record is that its antecedent, read with the
$\Theta$ the proof constructs, is not satisfied by the implemented calibration. Repairs on file,
both outside the equilibrium notion's declared Brouwer-with-one-fixed-family route: the
$t$-constrained game + Kakutani + $t \downarrow 0$ (`proofs/P1_proof.md` Step 18; *pointer
corrected 2026-08-29, polish-pass audit with P1-R46 applied to the file: Step 18 as it stands is
a scoped remark — its Kakutani conclusion is withdrawn as unestablished, and it carries no
$t$-constrained game and no $t\downarrow 0$ limit — so this route is a sketch, not a repair on
file, and Step 18's standard repair is not shipped, per the 2026-08-29 verification note at the
end of this bullet*), and a $k$-indexed concentration family (constructible; its $0/0$ corner
unresolved). The implementation's
`OFF_PATH_EPS` $= 10^{-14}$ **is** the fixed-$t$ constrained game — the standard repair already
shipped, with the switch relocated by $\sim10^{-9}$ rather than removed. Coverage: probes at one
node per claim class plus the 27-node census, **not swept over $(\kappa, \tau, T)$**; nonexistence
is neither claimed nor shown ($23/27$ sweep nodes converge; a discontinuous self-map may still have
fixed points). Records: `threads/2026-08-27_A6_panel_substantiate.md`,
`threads/2026-08-27_A6_panel_defuse.md`; probes `quality_reports/fixes/a6_panel_probes_2026-08-27/`
(analysis-grade, not curated t2 checks).

*Curation note added 2026-08-28.* The three decisive measurements are now executed t2 checks:
`quality_reports/fixes/t2_a6_edge_jump_check.py`/`.json` (both panellists' routes replayed at their
own filed brackets — $\mathcal T_2$ jumps $6.33\times10^{-3}$ / $1.09\times10^{-2}$ /
$2.83\times10^{-2}$, agreeing across routes to a relative $1.3\times10^{-4}$, controls
$2.8$–$3.6\times10^{-9}$, $\pm10^{-6}$ robustness intact), `t2_a6_node15_check.py`/`.json` (jump
$0.1647$, destroyed crossing $+1.0\times10^{-7}\to-6.70\times10^{-2}$, edge fixed point to
$1.06\times10^{-12}$) and `t2_a6_collapse_face_check.py`/`.json` (pooled prices within
$4.441\times10^{-16}$). **Every figure these checks touch reproduces; two wordings above are
corrected, the numbers are not.** The belief snap matches the Step 9(b) prediction to
$\sim10^{-8}$ at all three edges at the truncation/cancellation crossover bracket $10^{-8}$; at
the probes' own $10^{-9}$ bracket the first edge still holds ($4.0\times10^{-8}$, Analyst A's
"7–8 dp"), but the second and third are $1.2\times10^{-7}$ and $1.7\times10^{-7}$ —
floating-point cancellation over a $10^{-9}$-wide sliver, not a gap in the prediction. And
"$\mathcal T$ bit-identical" holds for $U$ but not for $\mathcal T_2$, which moves
$6.66\times10^{-16}$ (3 ulps) at the one $k_1$ where the price signature itself deviates most
($4.441\times10^{-16}$); invariance holds at the map's own root-finder resolution. The analytic
weight bound $\min(\kappa/2,1-\kappa)^{d+1}$ is **not** curated — no probe computes it; its
measured counterpart (the jump entering the adjacent-plan payoff difference undiminished) is.
**No label moves and none is licensed.**

*Off-path-family verification note added 2026-08-29 (independent verifier who did not write the
route exploration; probes `quality_reports/fixes/p1_route_probes_2026-08-29/v_offpath_*`, 20 gates
across three checks, 0 failed).* **The sentence above beginning "The implementation's
`OFF_PATH_EPS` $= 10^{-14}$ **is** the fixed-$t$ constrained game" is superseded: its first half
is wrong, its hedge is right and now has a measured mechanism.** What `numerical_v4/pooled.py`
`:225–235` ships is a **hard switch** — `if Wm[t] > 0.0: continue` floors a type only where its
alive mass is **exactly** zero, so $k\mapsto W^m$ is discontinuous on $\{k:W[t]=0\}$, where Step
9(b)'s $w_n(j\mid s)=(1-t_n)\mathbf 1\{j=j_k(s)\}+t_n/J$ perturbs every type at every $k$ and is
continuous in $k$. Three measurements: (a) at $t=$ `OFF_PATH_EPS` a genuine fixed-$t$ blend and
the shipped switch are **indistinguishable** — $\mathcal T_2$ across the edge(8) $\pm10^{-8}$
bracket agrees to $2.4\times10^{-9}$ and the local step to five significant figures
($6.3338\times10^{-3}$ both); the blend smooths only at $t=10^{-6}$ ($6.78\times10^{-6}$); (b) the
window in which the fixed-$t$ game differs from its own $t\downarrow0$ limit has half-width
$\varepsilon m_\theta/(J\varphi_s) = 2.26\times10^{-16}$ at $\varepsilon=10^{-14}$ — **one
double-precision ulp** at edge(8), and $4\times10^{6}$ times narrower than `menu.breakpoints`'
$10^{-9}$ merge tolerance; (c) the floor is **uniform across dead types** where $\Lambda_u$ is
**mass-proportional**, so the shipped $t\downarrow0$ limit is not Step 9(b)'s: at
$(\kappa{=}0.5,\tau_{50},T{=}5)$, $k_2=\text{edge}(6)+10^{-4}$, **157 464** dead-only pooled
histories at $d=H$ are reachable by two or more dead types and on them the two $\hat v$ differ by
up to $0.31$ — an $\varepsilon$-free gap, hence not a fixed-$t$-versus-limit question. **The hedge
stands and is now measured:** the switch is relocated, not removed, and the relocation is
`menu.breakpoints`' near-duplicate merge (`menu.py:244`, `np.diff > 1e-9`) — the dying type's
alive mass is $4.01\times10^{-10}$ at $k_2=\text{edge}(8)-10^{-9}$ and **exactly $0.0$** at
$\text{edge}(8)-9.9\times10^{-10}$. **Read the corrected claim as: Step 18's standard repair is
*not* shipped; what is shipped is the $t=0$ limit of a uniform-floor family, and the
$\Theta$-continuity the $t$-constrained game would buy is absent from the implementation at every
resolvable scale.** **What does and does not move above:** the belief-snap agreement and the
`type_reference` verification stand — they sit at **type-exclusive** histories, where the floor
cancels and `type_reference` **is** Step 9(b)'s limit — and the continuity clause still fails
under the proof-faithful family, so **the A6 conclusion is family-robust**. Its *numbers* are not:
at the same edge(8) $\pm10^{-8}$ bracket a Step-9(b)-faithful fixed-$t$ blend at $t=10^{-14}$
gives a local step of $7.05\times10^{-3}$ against the shipped $6.33\times10^{-3}$, **+11.4%**,
with $\mathcal T_2$ above the edge moving $7.2\times10^{-4}$. The filed jump magnitudes above —
and the curated `t2_a6_*` checks that replay them — are therefore **shipped-family records**,
valid as such and not withdrawn. (Measured at the first edge only; the $1.09\times10^{-2}$ and
$2.83\times10^{-2}$ figures were not re-measured under the proof-faithful family.) No label moves
and none is licensed — A6 is a hypothesis. *Recorded 2026-08-29, unverified beyond a cell scan:*
`menu.type_reference` reads one midpoint clock per $n(s)$ cell, and at $(\kappa{=}0.15, 0.05, 5)$
type 11's cell is **not** $(D,f)$-constant (it spans $[-3.2426407, 1.4082483]$ with
$D\in\{0,1\}$, $f\in\{9,\dots,15, \infty\}$) while carrying the dominant plan-uniform mass
$0.742$ — a **third** gap between the implementation's off-path construction and Step 9(b)'s
$\Lambda_u$, common to every family tested and therefore orthogonal to the
uniform-versus-mass-proportional finding. Size not measured; nothing above depends on it.

**A7 / A7′ / A7-J Filing sufficiency.** On flagged histories $(B^F, Q^F, a=1)$ identifies the informed
component of the selected plan; conditional on it the pooled order-flow residual is pure noise,
independent of $(v,s,\xi)$. L2 uses A7′ on path; the weak wording is not sufficient — it permits two
$(j,s)$ pairs with different pooled paths, which is exactly L2's first failure case. The two injective
forms are distinct. **A7′ (on-path composed target)**
requires the composed terminal target $s \mapsto b^*_{j(s)}(s)$ to be strictly increasing on the
flagged signal region, quantified over every cutoff vector $k \in \Theta$; strictness is required only
for flag-capable composed targets, with no backtracking across admissible Voice-plan switches. **A7-J
(joint tuple injectivity)** requires the full map $(j,s) \mapsto (B_j^F,Q_j^F,a_j)$ to be injective on
the full flagged-pair set, including pairs not selected on path. A7-J is stronger than on-path A7′ and
is the form consumed by the pre-review P1 proof. Strictness of $B^F$ is neither necessary (it fails at
crossing-date jumps on the pro-rata menu) nor sufficient (multi-Voice backtracking). Under A7′ the
flagged tuple is continuum-valued as a tuple: injectivity forces $(B^F,Q^F)$ to be continuum-valued,
while the coordinates may trade the burden. Injectivity plus measurability already gives the measurable
inverse (standard Borel spaces); no separate assumption is needed. *Satisfiability is resolved for A7′*:
A7′ plus a fixed cutoff policy plus $\Omega > 0$ deliver the on-path injective form with an explicit
inverse, and the pro-rata
single-Voice menu with terminal target strictly increasing on all of $\mathbb{R}$ also satisfies A7-J.
A7-J additionally needs strict increase off the Voice region; a target flat below the Voice cutoff
breaks A7-J while leaving A7′ intact. Failure boundary: a binding stake cap, quantized stakes, a
composed target repeating values across Voice-plan switches, $\Omega = 0$, and policy-dependence when
the condition is stated at only one equilibrium's cutoffs. A7′-satisfying menus are fully separating on
the flagged set, so the burden moves to incentive compatibility rather than away.

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

*Evidence note added 2026-08-25 (ticket 33; **lead sentence corrected 2026-08-28** on re-review
audit finding 2 — every number, bullet and verdict below is unchanged).* **At the implemented
calibration A($\tau$) FAILS. The decisive representation failure is already established by the
support condition alone; the derivative pattern also fails, and independently.** The support half
carries the verdict because it is A($\tau$)'s entire remaining content (see the bite paragraph
above); the derivative-pattern bullet is a second and independent failure, of which only the
$A_{1/2}'$ residual is inherited from the support. *(The superseded lead read "it fails on the
support, not on the derivative pattern", which the third bullet below contradicts on its own
terms.)* The pooled cell's engagement-posterior law was enumerated exactly (all $4^{H+1} = 4{,}194{,}304$ order-flow paths, the
same law `pooled_premium` integrates) at **200 nodes**: $\kappa\in\{0.05,\dots,0.95\}$ × the five
frozen $\tau$ percentiles × $T\in\{1,2,5,10\}$, frozen policies, $H=10$. Two gates pass first, so
the object measured is A($\tau$)'s own: an independent re-enumeration reproduces `pooled_pass` to
**0.0 exactly**, and the enumerated mean $\mathbb E[\Pi]$ equals the pooled share
$\bar\pi_{\mathrm{pr}} = \Pr(a=1\mid D=0)$ to $1.7\times10^{-16}$. Neither Example A's
$\lvert A'_\kappa\rvert = 0.25$ nor level symmetry is imposed anywhere, and $\bar\pi$ is read as the
upper support point throughout, per the binding ruling. **20 nodes are degenerate**
($\bar\pi_{\mathrm{pr}} = 0$ at $T\in\{1,2\}$ with $\tau$ at the 10th percentile: no engaging atom
survives into the pooled cell, the law is the point mass at $0$, $M_P = 0$ and $C_h(0) = 0$, so
A($\tau$) holds vacuously and the node decides nothing). At **all 180 non-degenerate nodes A($\tau$)
fails**; at none does it hold.

- **(τ-ii), support half — FAILS, by some eleven orders of magnitude.** The support carries
  **23–767 distinct posterior values**, never three (0 of 180 nodes), and there is **no mass at
  $\bar\pi/2$ at any node** ($A_{1/2}\equiv 0$). Between **0.57% and 91.8% of the pooled mass sits
  off $\{0,\bar\pi/2,\bar\pi\}$** — 13.9% at the median node ($T=5$, median $\tau$, $\kappa=0.55$:
  107 atoms, $A_0 = 0.768$, $A_1 = 0.093$). The atoms are not dust: coarsening the cluster tolerance
  to $10^{-3}$ still leaves **6–332** of them, and the floor-free law (the $\varepsilon\downarrow 0$
  limit of clause (vi) of the equilibrium notion, the law reported here) counts at most 51 atoms
  fewer than the floored law the package prices. The interior atoms move with $\kappa$: the
  two-sided Hausdorff distance between adjacent-$\kappa$ support sets reaches **0.4608** — unchanged
  when restricted to atoms carrying mass $\ge 10^{-6}$ — against A($\tau$)'s predicted $<10^{-12}$,
  at **0 of 18** series. This refutes L3 Step 18's (S1) and (S2) together at this calibration.
- **(τ-ii), $\bar\pi$ half — HOLDS.** $\bar\pi = 1$ to $1.5\times10^{-13}$ at every non-degenerate
  node, and $\kappa$-free to the same order (18 of 18 series). This is a separate finding and it is
  not a partial rescue: $\bar\pi = 1$ is the **one-round** outcome L3 Step 18 derives from the card's
  §4.2 mark structure, and that step's conjecture that "the two-round timing … leav[es] the pooled
  cell with a top atom strictly below $1$" is **false at this calibration** — unflagged Voice types
  still generate fully revealing order flows. $\bar\pi\in\{0,1\}$ across the whole grid and never
  interior, so L3's small-$\bar\pi$ corollary has no instance here either.
- **Derivative pattern — FAILS, and independently of the support.** $A_0' = A_1'$ holds at **0 of
  180** nodes: $\lvert A_0'-A_1'\rvert\in[0.041,\,2.306]$ against a predicted $<10^{-10}$, with
  $A_0'\in[-2.146,\,2.374]$ against $A_1'\in[-0.014,\,0.429]$ — an order of magnitude apart in level,
  and both change sign over the grid, which independently corroborates that $A'_\kappa$ carries no
  sign (audit finding 2). $A_{1/2}' = -2A'_\kappa$ also fails at all 180, but with
  $A_{1/2}\equiv 0$ that residual is exactly $2\lvert A_0'\rvert$ and is recorded as **inherited** —
  a restatement of the support failure, not a second piece of evidence.
- **Chord identity — FAILS.**
  $\lvert\mathcal S_P - \Delta_m\lvert A'_\kappa\rvert\lvert C_h(\bar\pi)\rvert\rvert$, with
  $A'_\kappa$ **recovered** from the enumerated weights and $\bar\pi$ the **actual** upper support
  point, is **0.0013–0.0717 (up to 7.17 premium pp)** against $<10^{-10}$, at 0 of 180 nodes and on
  the most favourable of three kernel conventions. Recovered
  $\lvert A'_\kappa\rvert\in[0.042,\,2.374]$; the value the identity would *require* is
  $[0.00023,\,0.392]$, **disjoint** from block 3's implied $[0.997,\,1.158]$ — which is a different
  object (mean absolute slope over the $\kappa$ grid, and the level-symmetric
  $\bar\pi = 2\bar\pi_{\mathrm{pr}}$), and the distance between the two measures what the
  level-symmetry assumption was doing.
- **(τ-i), reported as a diagnostic and not part of the verdict.** Within a $\Pi$-cluster ($\Pi$
  constant to $10^{-12}$) the enumerated entry probability still spreads by up to **0.085**, and $h$
  by up to **0.018** mass-weighted. The kernel does not reach the information set only through the
  posterior at this calibration either.

**What this changes, and what it does not.** NUMERICAL-class **applicability** evidence at one
calibration; **no label moves**, and none is licensed — A($\tau$) is an assumption, not a labelled
claim. L3, L4 leg 3 and T1 Part B stay **PROVED as conditionals** with their proofs untouched; what
is now on record is that their antecedent is **not satisfied by the implemented pooled cell at this
calibration**, so at this calibration those legs say nothing about the implemented cell. The
question stated above stays open as a question about A($\tau$)'s **domain** — a different menu, a
different $H$, or a different calibration could still satisfy (S1)–(S2) — and the two prior
"failures" remain misformulated tests; this is the first test that measures A($\tau$)'s own object.
Coverage caveats carried forward: the 18 non-degenerate series are only **6 distinct pooled cells**
($T=1$ and $T=2$ induce identical $D$-partitions at every $\tau$; $T=5$ joins them at the three
highest $\tau$ percentiles and repeats itself at the two lowest; all five $T=10$ quantiles
coincide), and all six fail; the 50 $T=10$ nodes sit at $\Omega = 0.000681$, below `MIN_CELL_MASS`
(`HANDOFF_sign.md` §8.1). Script and record:
`quality_reports/fixes/t2_atau_support_check.py` → `t2_atau_support_check.json` (200 nodes, 920
pooled enumerations, 1002 s; top-level `verdict` field `FAILS at calibration`).

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

**All eight results now carry two-pass evidence** — an adversarial proof-read PASS *and* an
independent statements-only re-derivation PASS, by different agents — and are labelled PROVED with
their conditionality written into the label. (C1 moved on 2026-08-22, after its own proof-read,
re-derivation, and the independent re-run of every check script — ALL REPRODUCE,
`quality_reports/fixes/t2_rerun_verify_note.md`; **P1 was demoted on 2026-08-23 and restored on
2026-08-25** on a fresh pair of passes over the amended statement.) The protocol (the *Labels*
subsection below) requires both passes, by different agents, before a label moves. That gate is
satisfied for D1, L1, L2, L3, L4, T1, C1 and — as of 2026-08-25 — P1 again. **P1's 2026-08-21 chain
never satisfied it**: the proof consumed A7-J while the row and re-derivation carried A7′, so the
two passes covered two different statements, which is what the 2026-08-23 demotion turned on. The
pair on file now is `threads/2026-08-25_P1_proofread_retry.md` (0 FAIL) and
`rederive/P1_rederivation_2026-08-25.md` (PASS-WITH-CHANGES, changes folded into the row). Labels
are transcribed from `LABEL_LEDGER.md`; every statement below is the *amended* statement — the
hypothesis sets are named in full and descriptively, and **no statement was weakened silently**:
each difference from the pre-regeneration row is traceable to the named finding beside it.

| ID | Statement, with its full hypothesis set | Label |
|---|---|---|
| **D1** | Under **A1, A2′, A4, A5, the primitive/plan table restrictions, the cutoff selection map, and the pricing conventions** ($P_{-1}^P = \mathbb{E}[Y]$; $P_{\mathrm{ND}} = P^P_{f^-}$), plus two hypotheses this regeneration wrote onto the card — **Borel regularity of $s \mapsto B_j(s,d)$ for every plan including Exit** (needed only for part (c), since pooled pricing integrates over all types) and **a content for $\mathcal{I}_H$** — the indicator $D = \mathbf{1}\{a=1,\ c(\tau)+T \le H\}$ is **measurable** and maps every control-node history into exactly one cell; for every Voice plan $f_j \le H \iff B_j(s,H-T) \ge \tau$; and each flagged history yields $B^F, R_d, R, J$ with $P^F - P_{c^-}^P = R + J$. | **PROVED** |
| **L1** | Under **D1, the premium definitions, A5** (which pins *the* version of $\mathbb{E}[Y \mid \mathcal{I}]$), **A2′ with $\Delta_m$ finite, and A1** (one probability space): whenever $0 < \Omega < 1$, $\Delta^{\mathrm{act}} = \Omega M_F + (1-\Omega)M_P$; at $\Omega = 1$ it degenerates to $\Delta^{\mathrm{act}} = M_F$ and at $\Omega = 0$ to $\Delta^{\mathrm{act}} = M_P$, the null-cell average being *undefined rather than imputed* — proved as a non-identification statement, not asserted. | **PROVED** |
| **L2** | At fixed cutoff and execution policies, under **A1; A2′ with the primitive/plan table restrictions; A4; A5; A7′ in its on-path injective form, consumed almost surely on the flagged set; D1; the no-feedback timing; and $\Omega > 0$** — together with an explicit bidder-entry rule carried as bookkeeping: $(B^F,Q^F,a{=}1)$ makes the pre-filing pooled history conditionally independent of $(v,s,\xi)$ on the flagged set, so the flagged posterior, price, entry probability and $M_F$ are invariant to $\kappa$. ("Almost surely" is the only coherent reading once $B^F$ is continuum-valued, since then no individual flagged tuple has positive probability.) | **PROVED** |
| **L3** | **Under A($\tau$)** — including (τ-i) kernel-through-posterior and (τ-ii) $\kappa$-free support *and* $\kappa$-free $\bar\pi$ — plus $h(0)=0$; $\kappa$-free pooled mass and engagement moment at fixed policies; D1 by statement; minimal regularity ($h$ continuous on $[0,\bar\pi]$, twice differentiable on the open interval — Darboux does the rest, no continuity of $h''$); for the small-$\bar\pi$ corollary only, a second-order Peano expansion of $h$ at $0+$ and one and the same kernel along the shrinking family; and, for the seam where L4 consumes L3, $|A'_\kappa|$ bounded *uniformly in $\bar\pi$*. Then $\partial_\kappa \mathbb{E}_\kappa[h] = A'_\kappa C_h(\bar\pi)$ exactly; $C_h(\bar\pi) = \tfrac14 \bar\pi^2 h''(\zeta)$ for some $\zeta \in (0,\bar\pi)$ — an identity, not an approximation; and $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, so the interior motion vanishes at rate $\bar\pi^2$. **An "if", never an "iff"** ($A'_\kappa = 0$ also kills the motion). Whether the two-round pooled cell satisfies A($\tau$)'s support condition is **OPEN**. | **PROVED** under A($\tau$) |
| **L4** | At fixed policies, for $b_0 < \tau' < \tau$ at a common window $T$ and common $\kappa$, with $\Omega(\tau',T) < 1$: **(leg 1, unconditional)** $\mathcal{C}_F(\tau,T) \subseteq \mathcal{C}_F(\tau',T)$ with every newly flagged history generated by a Voice plan, hence $\Omega(\tau',T) \ge \Omega(\tau,T)$; **(leg 2, unconditional)** the pooled engagement *share* falls, $\bar\pi_{\mathrm{pr}}(\tau') \le \bar\pi_{\mathrm{pr}}(\tau)$, with an exact identity for the gap; **(leg 3, under A(br))** $\mathcal{S}_P(\tau',T) \le \mathcal{S}_P(\tau,T)$, with equality whenever $C_h(\bar\pi(\tau)) = 0$. Legs 1–2 need only **D1's clock equivalence, the no-feedback timing, fixed policies, $b_0 < \tau' < \tau$ imposed at both thresholds, A1, A4, $D=1 \Rightarrow a=1$, and $\Omega(\tau') < 1$** — the "nestedness" clauses are *conclusions, not hypotheses*. Leg 3 additionally needs **L3 by statement, A($\tau$)'s maintained magnitude monotonicity of $|C_h|$** (the sign half $C_h \le 0$ is never used at this leg) **and A(br) (br-i)–(br-v)**. | **PROVED** (legs 1–2 outright; leg 3 **under A(br)**) |
| **P1** | Under **A1, A2′, A3, A4, A6, A7-J (joint tuple injectivity — the joint $(j,s)$ form of A7 above, on the whole flagged-pair set $\{(j,s):D_j=1\}$ *including pairs no cutoff vector selects*; strictly stronger than the on-path A7′, and the form the proof consumes where it pins *off-path* flagged beliefs. Amended from A7′ 2026-08-25: the pre-review row carried the on-path form while `proofs/P1_proof.md` h.7 consumed the joint form, so the two 2026-08-21 passes covered two different statements), D1 by statement *with its own hypotheses travelling*, the no-feedback timing read with the flag-terminates-the-pooled-round clause, the definitional round-2 action-set hypothesis** (the flagged-round action set **is** the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements agreeing with $j$ on everything already played — *not* a closure condition; the closure form is jointly unsatisfiable with finiteness by cardinality), **continuation-cost equivalence on that same set** (the proof's h.16, added 2026-08-25: menu elements sharing $j$'s pooled path up to $f_j(s)$ with $a_{j'}=a_j$ carry the same engagement cost, $C_{j'}(s)=C_j(s)$. **Trivially true on any single-Voice menu**, where that set is a singleton. What it buys, **under the plan-completion reading of the $C_j(s)$ timing convention below** — under the sunk reading the continuation is constant on the deviation set with no clause at all and h.16 is not consumed, so the hypothesis is listed because the row does not commit to a reading, and it is what makes the conclusion hold under both: on that set the flagged price does not move and the order cancels, so the engagement cost is the only thing that can differ between staying and deviating — and at a flagged pair the cutoff vector does **not** select there is no date-0 optimality to fall back on, so without this clause the deviator takes the class member with the smallest cost and item (ii) of the equilibrium notion fails at that node. Live only on menus with two or more Voice plans sharing a pooled path), **$m_0\ge0$, the card's §4.3 blockholder-objective definition $U_j$** (whose $-a_jC_j(s)$ display `proofs/P1_proof.md` h.14 now carries verbatim, which is what the row's "displayed there in full" asserts; **timing convention, stated here because the card's §4.3 does not date $C_j(s)$**: the engagement cost may be booked either on completing the plan or as sunk once the filing has landed — the two give the same round-2 comparison on the round-2 deviation set, which is what the continuation-cost clause above buys, so the result does not depend on the choice), **and the card's §4.1–§4.3 table restrictions the argument consumes — in particular §4.3's $Y$ row with the price convention $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ and the entry row for $p(\mathcal I)$; §4.2's Borel-regularity clause for *every* plan including Exit (needed directly, not via D1, whose conclusion is measurability of $D$ and the cell map); §4.2's $D=1\Rightarrow a=1$, the $c/f/B^F/Q^F/b^*$ definitions and $\partial_sB_j\ge0$ for Voice; and §4.1's distributional forms with $\Delta_m>0$**: **at every $\kappa\in[0,1]$**, a cutoff PBE over complete contingent plans exists — $k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, prices at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs as limits of **one** full-support perturbation family over **plans — fixed once and used to define the price system at every $k\in\Theta$, not only at $k^\star$, since the deviation payoffs that define $\mathcal T$ read off-path pooled histories — at every pooled history reachable *with positive probability* under some plan profile** (at the boundary values $\kappa\in\{0,1\}$ the card's §4.1 noise support degenerates to $\{0\}$ and to $\{\pm\bar z\}$ respectively; a pooled history needing a mark outside it is null under *every* profile, so it is off nature's path rather than off the players', carries no clause-(vi) requirement, and is read by no step. This is the extension route, not the restriction one: no cut to $\kappa\in[0,1)$ is taken, and the pre-repair claim of a belief at *every* pooled history — false at $\kappa=1$ — is withdrawn); **flagged-tuple beliefs supplied by A7-J** at every tuple in the image of the flagged-pair map $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$ — on path and off, since the image includes tuples generated by pairs the cutoff vector does not select — as the point mass at the unique generating pair, which is a **version** of the conditional law at every image tuple (the signal is continuous, so a version is what a conditional law is; any a.e.-equal version serves clauses (iii)/(vi) of the equilibrium notion equally) and is the version this equilibrium selects, with no tuple outside that image arising because the round-2 action-set hypothesis leaves no off-menu order to produce one; the card's §4.3 entry rule; and **a sequentially optimal flagged component at every flagged pair $(j,s)$, whether or not the cutoff vector selects it** — the flagged price is invariant across the round-2 deviation set (A7-J pins the belief at the same $s$ and $\pi=1$), so the order cancels out of the continuation and the continuation-cost clause makes what remains constant. **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$; its continuity content **in the belief summaries $(\hat v,\pi)$** from the same scalar reduction (`proofs/P1_proof.md` Step 7(iii)'s strict $\varrho'<0$ at every root, with Step 8's implicit-function bound $\partial P/\partial\hat v\in(0,1]$ as a second recorded route — the proof file records both as valid and names neither as the only one); and its measurable-selection content from A7-J plus the card's §4.2 Borel clause. **What is *not* derived is A5's cutoff clause** — continuity of the *composed* pooled price family in the cutoff vector $k$, which runs through the conditioning $(\hat v,\pi)$ rather than through the pricing map (`proofs/P1_proof.md` Step 7, closing paragraph; the struck h.5(c), which marks Step 15's cutoff-continuity citation non-load-bearing). That continuity enters only through **A6 as read**, and §5's A6 evidence note records it **measured to fail** at the implemented calibration (see A5). *Clause corrected in place 2026-08-28 on re-review audit finding 1 (`threads/2026-08-28_gpt_rereview_audit.md`); the hypothesis set, the conclusion and the label are unchanged.* **A6 is read** as asserting that $\mathcal T$ — under a named tie-break-and-corner selection, without which a correspondence cannot be called continuous — is a well-defined single-valued continuous self-map of $\Theta$, with $\Theta$ nonempty per the card's §4.5. **At any such equilibrium at which A8 holds**, both cells carry strictly positive probability and are on path; for A8's restatement as a single signal threshold add **H-ord** (Voice stake monotonicity across plans — the writer's h.13, **renamed here to avoid collision with the objective row**) and the upper-set engagement-flag hypothesis. A8 is a condition *on the fixed point exhibited*: existence of an equilibrium *at which* A8 holds is not claimed. Uniqueness is not claimed. **Evidence.** Statement `threads/thread1_turn1_answer.md`; proof `proofs/P1_proof.md` (repairs applied through P1-R35, ticket 35 rounds 1–2, close-out and confirm-pass sweep); **proof-read PASS 2026-08-25** `threads/2026-08-25_P1_proofread_retry.md` (**0 FAIL**; 3 REPAIRs + 4 OBSERVATIONs, all applied; the reader verified the Step 12 lemma part by part on the merits and records that his own round-1 FAIL witness is refuted — round-1 FAIL and the sanctioned repair round at `threads/2026-08-25_P1_proofread_round1.md`); **re-derivation PASS-WITH-CHANGES 2026-08-25** `rederive/P1_rederivation_2026-08-25.md` (fresh agent, card row alone; changes 1–5 folded into this statement cell — the card's §4.1–§4.3 citation block, D1's hypotheses travelling with the three-part A5 sentence, the one-family/every-$k$/positive-probability off-path clause, A6's tie-break-and-corner reading, the $C_j$ timing convention; **change 6 withheld for Austin** — a proposed OPEN item on whether A6's continuity of $\mathcal T$ is satisfiable at the collapsed cutoff vectors the equilibrium notion admits; **ruled 2026-08-27**: answered rather than filed OPEN — §7 item 4 and §5's A6/A3 evidence notes carry the panel record, no label moved). **The 2026-08-21 chain is retained below and did not satisfy the gate for the recorded statement**: proof-read PASS 2026-08-21 `threads/2026-08-21_batch1_proofread_audit.md` §4 (0 FAIL; P1-R1…R8; inner fixed point executed on 20k random draws — 0 multiplicity, 0 sign failures) and re-derivation PASS 2026-08-21 (PROVED-WITH-CHANGES) `rederive/P1_rederivation.md` (changes C1–C8) covered **two different statements** — the proof's h.7 consumed the joint injective form of A7 while the row and re-derivation carried the on-path form — which is what the 2026-08-23 demotion turned on, together with Step 12's missing continuation-cost clause and the false positivity claim at $\kappa=1$; all three are repaired and independently reproduced by the 2026-08-25 re-derivation. **Numerical status, stated honestly and separately from the label (ticket 34, `quality_reports/fixes/t2_p1_fournode_recheck.json`):** the four sweep-unresolved nodes ($\kappa\in\{0.15,0.85\}\times(\tau,T)\in\{(0.05,5),(0.075,1)\}$) remain **STILL UNRESOLVED after 30 seeds each** — best payoff-scale residual $3.1\times10^{-4}$–$1.5\times10^{-3}$ against a $10^{-9}$ criterion, best cutoff-scale residual $10^{-14}$–$10^{-11}$; the A3 and A6 proxies pass at every achieving seed. **UNCHECKED**: existence at those four nodes is neither claimed nor denied by this evidence, and the label rests on the proof plus the two 2026-08-25 passes, not on the grid. **2026-08-29 (polish pass, audited; wording repairs applied; demotion question OPEN before Austin):** the GPT Pro polish response `threads/2026-08-29_gpt_p1_polish.md` and its in-house audit `threads/2026-08-29_gpt_p1_polish_audit.md` are on file (19 findings: 16 UPHELD, 3 with scope, 2 NARROWED, 0 REJECTED). The audit's wording-grade repairs P1-R36–R39, P1-R41–R42 and P1-R46–R53, and the auditor's same-day seam follow-ons P1-R54–R56 (`threads/2026-08-29_p1_polish_audit_addendum.md`, drafted after application review), are applied to the proof, verbatim from the drafted texts and independently verified by fresh agents — no hypothesis or step conclusion moved, and the two-pass gate was not re-run, per the lane rule for wording repairs. P1-R43 and P1-R44 (statement-preserving new derivation) are drafted and pending the two-pass gate; P1-R45 is drafted behind the F5 route. **The demotion question is OPEN:** the audit upholds finding F5 at antecedent level — under the printed corner coding, Step 13's representation claim fails on a positive-probability Gaussian tail for card-legal menus with a dominated top plan — and wording repairs cannot close it. Routes on file: **P1-R40-A** (drafted in full, including an unapplied card-side clause for this row's "A6 is read" sentence) and **P1-R40-B** (sketched; would edit card §3). The route choice, and any label consequence, are Austin's; the label stays PROVED until he rules — on the 2026-08-25 change-6 precedent for recording an open question in this cell. | **PROVED** |
| **T1** | At fixed plan and cutoff policies, with $0 < \Omega < 1$ and $\mathcal{S}_P > 0$: **(A)** $\mathcal{S} = (1-\Omega)\mathcal{S}_P$ exactly, and the same factorisation holds for the total-variation aggregate of $\Delta^{\mathrm{act}}$ over any $\kappa$-grid with no differentiability required; **(B)** threshold tightening attenuates — $\mathcal{S}(\tau')/\mathcal{S}(\tau) = W_\tau C_\tau \le 1$ because *both* ratios lie in $[0,1]$, no dominance condition needed; **(C)** window tightening attenuates **iff** $W_T C_T \le 1$, where $W_T \le 1$ is *proved* (from D1's clock equivalence and the monotone Voice stake path) and $C_T$ is *unsigned* — "equivalently $\partial_{r_T}\mathcal{S}_P/\mathcal{S}_P \le \Omega_{r_T}/(1-\Omega)$" holds **on average along the tightening path** (integrated over $[-T,-T']$), exactly in the infinitesimal limit, and is **false read pointwise**. Hypotheses: **fixed policies; A8 at each compared policy; $\mathcal{S}_P > 0$; L1; L2 (its own hypotheses travelling); D1; PE-$\Omega$ ($\partial_\kappa\Omega = 0$ at fixed policies — derivable, not assumed, and it fails in GE, which is C1's term); $\kappa$-differentiability of $M_P$ (no card hypothesis supplies this — carried in-proof); A($\tau$) at both compared policies with the $\bar\pi$ ruling; L3; A(br) (br-i)–(br-v) at the threshold pair; L4; the no-feedback timing; a smooth window interpolation for the local form; threshold-side smoothness (confirmed non-load-bearing)**. **No unconditional window sign is claimed.** | **PROVED** at fixed policies |
| **C1** | On a named region where $L_{\mathcal{R}} < 1$ and $g_r^{PE} > \mathcal{B}_r^{GE}$, the fixed-policy attenuation sign survives in equilibrium. The dominance-and-contraction implication is **two-pass complete** — an adversarial proof-read PASS (0 FAIL, 13 repairs, 7 observations) and an independent statements-only re-derivation PROVED-WITH-CHANGES (a norm convention and two-sided openness of $\mathcal{R}_r$ added; at $J-1 \ge 2$ the bare $|\cdot|$ in $\mathcal{B}_r^{GE}$ is not well defined and a mismatched reading makes part (B) false) — and the executed 80-node run returns **18 pointwise dominance-and-contraction nodes**, slack $\eta_r$ from $0.0595$ (min) through $0.3467$ (median) to $1.7227$ (max), $L_{\mathcal{R}} \le 0.5008$ at every node. These nodes verify the pointwise inequalities and supporting diagnostics only; they do not verify the full C1 antecedent or a named nonempty region. | PROVED |

Remaining aspiration, not a claim: promotion from pointwise dominance-and-contraction nodes to a
named nonempty region, which would require the D8 $\varepsilon$-ball and integral-control pattern.

### Labels

**PROVED** — a complete proof, independently re-derived and proof-read. **NUMERICAL** — verified on a
grid by an executed, committed check script with committed output. **ESTIMATED** — an empirical
estimate with a standard error and a stated design. **CONJECTURE** — everything else, including
anything whose proof is deferred. A **dominance-and-contraction node** is not a fifth label: it records
pointwise $L_{\mathcal R}<1$ and $\eta_r>0$ with supporting diagnostics, not verification of the full
C1 antecedent. A named-region promotion is not claimed. Labels are never weakened by editing; only an
executed check or an independent re-derivation may move one.

### Three known facts on file

These are facts the record carries, not claims the model makes. They are the reason the labels above
are written with their conditions attached.

**1. O-1 is a disclosure-regime analogy, not a window-margin test.** This is a known fact on file,
not a claim the model note makes: O-1 compares the public buy flagged versus pooled at fixed policies
in the static repo model. Its ratios

$$1.06397 \,/\, 1.18373 \,/\, 1.13631 \,/\, 0.37798 \qquad \text{at} \qquad
\Omega = 0.037252 \,/\, 0.128950 \,/\, 0.285804 \,/\, 0.50$$

are regime-comparison composition outcomes, not $W_T C_T$ and not a window pair. The analogy is
useful because it shows that a composition factor can exceed one, motivating T1's genuine
window-margin iff. The genuine window-margin record is `t2_t1_check` block 4: $W_T C_T<1$ at every
checked node at this calibration. The O-1 boundary $\Omega^\star \approx 0.3428$ remains a
disclosure-regime boundary, not a window boundary. Provenance: this is the referee's O-1 experiment
run on the *repo* model (the frozen manuscript's static structure, fixed cutoffs, partial equilibrium),
re-executed in `quality_reports/fixes/t1_o1_rerun_check.py` with every committed number reproducing
to the last printed digit; it is not the two-round build.

**2. Whether the implemented two-round pooled cell satisfies A($\tau$): at the implemented
calibration it FAILS.** Two executed diagnostics are informative but neither decides the support
condition, and both are retained without smoothing.

- `t2_l2_check.json`, check `l2_placebo_M_P_sign_A_tau`: **FAIL** as a sign placebo. The enumerated
  pooled $M_P$ is *hump-shaped* in $\kappa$ — 10 of 18 increments positive, one sign change, peak
  near $\kappa = 0.55$. But A($\tau$)'s maintained $C_h(\bar\pi)\le0$ does not sign $A'_\kappa$;
  the card's own Example A has $A'_\kappa=-1/4$. The demanded sign is therefore not implied by
  A($\tau$), and the placebo is misformulated rather than a refutation of the support representation.
- `t2_t1_check.json`, check `t1_block3_chord_magnitude`: **FAIL** for the hard-coded Example-A
  coefficient. The residual $\big|\mathcal{S}_P - \Delta_m |A'_\kappa|\,|C_h(\bar\pi)|\big|$ is
  $0.006279$ ($0.6279$ premium percentage points) against a predicted $10^{-10}$ — the implied
  coefficient is **$|A'_\kappa|\in[0.997,1.158]$**, while the check hard-coded $0.25$. The ratio
  $|C_h|/\bar\pi^2$ remains constant to $0.48\%$ between the two smallest $\bar\pi$ nodes, well
  inside the $5\%$ criterion. This rejects the hard-coded calibration, not A($\tau$)'s general
  support representation.

The decisive support-enumeration check is ticket 33, and it has landed: at the implemented
calibration the support condition **FAILS**, at every non-degenerate node, while the $\bar\pi$ half
of (τ-ii) holds. The measurement is §5's A($\tau$) evidence note, and it moved no label. The two
diagnostics above remain test-design artifacts, not a wiring error or a theorem failure — and
neither of them is the test that decided it. What stays open is A($\tau$)'s **domain**: a different
menu, a different $H$ or a different calibration could still satisfy the support condition (§7,
item 1).

**3. L4's sign predictions hold numerically with zero violations.** `t2_l4_check.json` reports 10
checks, 0 failures. Across all 16 tightening steps and both windows: $\Omega$ rises at every step (0
violations, minimum increment $+0.02263$); $\bar\pi_{\mathrm{pr}}$ falls at every step (0 violations,
largest increment $-0.018766$); and $\mathcal{S}_P$ falls at every step (0 violations, largest
increment $-9.47 \times 10^{-5}$) — and, as the JSON notes, a single violation would be a failed
hypothesis rather than sampling error, because nothing in that computation is sampled. $\Omega$ and
$\bar\pi_{\mathrm{pr}}$ are flat in $\kappa$ to exactly zero across 71 grid points, which is what the
no-feedback timing predicts.

**What the pair of facts means.** The chord mechanism is **hypothesis-bound**: it needs A($\tau$),
whose applicability at the implemented pooled cell is now answered — it **fails** at this
calibration, no label moved, so L3, L4 leg 3 and T1 Part B stay PROVED as conditionals that say
nothing about the implemented cell here; whether A($\tau$) has a domain that fits stays open. The
threshold phenomenon is **not** hypothesis-bound: the reclassification legs of L4 are
unconditional, and they hold numerically without exception.

---

## 7. What this note does not claim

A global window-margin attenuation sign; $\kappa$-invariance of $J$; equilibrium uniqueness; a named
nonempty GE region *as a theorem* (the 18 pointwise dominance-and-contraction nodes are an executed
record, not verification of the full C1 antecedent); endogenous filing before the deadline; noisy or partially revealing flagged-round
trading; continuous-time execution; welfare or optimal rule design; that the frozen manuscript's hump
result survives; that the prior calibration ($\Omega \approx 0.037$) is economically meaningful; any
empirical value for $\omega_a$.

Three items are explicitly open *(a fourth, item 4, added 2026-08-27)*:

1. **Whether the two-round pooled cell satisfies A($\tau$) — OPEN.** L3 proves the representation's
   entire remaining bite is the support condition, exhibits a one-round market that satisfies it and
   the frozen manuscript's own no-disclosure structure that does not, and names the weakest sufficient
   conditions. L3, L4 leg 3 and T1 Part B are all conditional on A($\tau$), so this is the largest
    single conditionality the ledger carries — and the executed diagnostics of fact 2 above do not
    decide it at baseline; the support-enumeration check is ticket 33.
2. **Whether an equilibrium in which the blockholder chooses the fully separating plan exists on a
   given calibration — OPEN, and P1-adjacent.** A7′ menus are fully separating on the flagged set, so
   the burden did not disappear when A7 satisfiability was resolved; it *moved* to incentive
   compatibility, which P1 does not settle.
3. **O-1 is a disclosure-regime analogy, not a window-margin test** (fact 1 above). The genuine
   window-margin record is `t2_t1_check` block 4, with $W_T C_T<1$ at every checked node at this
   calibration.
4. **Whether A6's continuity of $\mathcal T$ holds for the declared construction — ANSWERED IN
   SUBSTANCE 2026-08-27 (panel evidence; locus corrected; the open remainder is scoped below).**
   The re-derivation's withheld change 6 proposed filing this as OPEN at collapsed cutoff vectors.
   Ruled on Austin's 2026-08-27 authorization after a two-agent opposed-brief panel (substantiate
   vs defuse) with orchestrator adjudication — the briefs **converged on every load-bearing point**
   and **cross-replicated the decisive measurement** (the same three $\mathcal T_2$ jumps,
   independent scripts, 3 s.f. agreement). *Answered:* the discontinuity mechanism is real and
   reaches $\mathcal T$ with non-vanishing weight (the vanishing-mass defusal is refuted, twice
   independently); the locus is the **cell-edge hyperplanes $\cup$ sole-generator collapse faces**,
   not the collapsed vectors as such; the implemented menu's Hold-collapse face is measured clean,
   while A6 read with the $\Theta$ Steps 13–14 construct **fails at the implemented calibration**
   (measured $\mathcal T_2$ jumps $6.3\times10^{-3}$–$2.83\times10^{-2}$ at the baseline node, up
   to $0.16$ at $\kappa = 0.15$, against a $10^{-10}$ tolerance); and on $J \ge 3$ menus where a
   middle plan owns a reachable exclusive pooled history, **no $k$-independent perturbation family**
   restores continuity at more than one collapse-face point (continuum-face lemma; panel
   derivation, not gate-checked), so on that menu class P1 asserts nothing — the A($\tau$) pattern.
   *Still OPEN:* (a) whether a constructive $\Theta$ — or the Step 18 $t$-constrained Kakutani
   route already on file, which removes h.6's continuity half — replaces h.6 in the statement; the
   repair is identified, not executed; (b) the complementary menu class (every middle plan's
   histories shared with a survivor — the implemented menu is one such for its collapse face),
   where the collapse-face clause may be satisfiable; (c) nonexistence, which is neither claimed
   nor shown anywhere — $23/27$ sweep nodes converge and two fixed points survive even at the worst
   probed node. *Separately recorded, deliberately not folded in* (different hypothesis, different
   route): A3's own failure at this calibration and the candidate ticket-34 account — §5's A3
   evidence note. **No label moves on any of this**; P1's label rests on the proof and the two
   2026-08-25 passes and is untouched. Evidence: §5's A6 note;
   `threads/2026-08-27_A6_panel_substantiate.md` / `threads/2026-08-27_A6_panel_defuse.md`;
   `quality_reports/fixes/a6_panel_probes_2026-08-27/`. Follow-ups: the decisive-probe curation
   landed 2026-08-28 (§5's A6 note, curation note; the `t2_a6_*` checks); gate-check the
   continuum-face lemma only if it is ever promoted.

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
| The GE dominance-check pattern: contraction modulus $L$ along the path, an inversion-free Neumann bound $\bar B$, pointwise dominance off a ball plus a ball-integral condition, a certified interval, and a counterexample showing the global claim false. | **REUSE** | Is C1's precedent. $\mathcal{B}_r^{GE}$ is the *cross-derivative* analogue of $\bar B$; $\eta_r = g_r^{PE} - \mathcal{B}_r^{GE}$ is the slack; the executed record names pointwise dominance-and-contraction nodes, not a verified region, and a named-region promotion remains open. What changes: the object bounded is a cross-derivative in $(\kappa,r)$ rather than a single-argument profile, and the strictness coordinate $r_T = -T$ is not differentiable because the window is an integer. |
| Stake-triggered disclosure as the market's partition, with the flag a function of the order ($D = \mathbf{1}\{q = +1\}$: a buy cannot be concealed). | **REUSE** | The idea that the rule *is* the partition is the whole v4 position. What changes is the trigger: $D = \mathbf{1}\{a=1,\ c(\tau)+T \le H\}$, a stake threshold plus a filing window on a business-day calendar, with D1's clock equivalence $f \le H \iff B(s,H-T) \ge \tau$. The window $T$ becomes a genuine primitive instead of a flag that is either on or off. |
| Assumption (A2)'s flat boundedness of prices and payoffs. | **SIMPLIFY** | Replaced by A2′: finiteness clauses kept verbatim; boundedness weakened to local boundedness plus integrability $\mathbb{E}[\max_j |U_j|] < \infty$. The flat bound was *false* in this model ($v$ Gaussian, flagged region unbounded in $s$), and no proof ever used it. |
| Assumption (A5)'s inner pricing regularity (existence, uniqueness and continuity of the price fixed point, assumed, with a $\delta/\sigma_\xi < 1/\phi(0)$ style regularity condition). | **SIMPLIFY** | Demoted to a theorem under $m_0 \ge 0$: the pricing map is strictly decreasing in $P$ wherever $\bar m \ge 0$ and crosses the identity exactly once. A5 survives only as its continuity clause, read as a measurably selected family because the flagged information sets are continuum-indexed. Three independent confirmations, including executed counterexamples that produce zero roots and three roots once $m_0 < 0$. |
| The discount factor $\delta$ inside the pricing fixed point $P = \delta[(1-p)\hat V + p(P+\bar m)]$, and the sensitivity analysis around it. | **DROP** | v4 prices are undiscounted conditional expectations $P(\mathcal{I}) = \mathbb{E}[Y \mid \mathcal{I}]$. The regularity work $\delta$ was doing is done instead by $m_0 \ge 0$. |
| The one-round pooled posterior: $\pi(X,0)$ in closed form from a single order-flow draw $X \in \{-2,-1,0,1\}$ with $p_0 = 1-\kappa$, $p_1 = \kappa/2$ and the action weights $(\omega_E,\omega_H,\omega_Q)$; Hold and Quiet Voice pooling because both trade $q = 0$. | **DROP** | Replaced by a pooled history $\mathcal{H}_H^P$ over $H+1$ business days with plans, $\Gamma$-coarsened increments and a flag that can land mid-calendar. The closed-form posteriors do not survive the calendar. Consequential: L3 shows the manuscript's own no-disclosure structure (informed mark $\bar z$) yields a *four-atom* pooled law, two of whose atoms move with $\kappa$, so it lies outside A($\tau$) — the one-round posterior is not merely superseded, it is a named example of the representation failing. |
| The hump headline: $\Delta^{\min}(\kappa)$ single-peaked in liquidity, as the conditional-hump proposition and the paper's first main result. | **DROP** | Not claimed anywhere in v4; the card states outright that it does not claim the hump survives. The v4 headline is the partition and the attenuation factorisation $\mathcal{S} = (1-\Omega)\mathcal{S}_P$, not a shape in $\kappa$. Note the hump has not been *refuted* either: the enumerated two-round $M_P$ is itself hump-shaped in $\kappa$ at baseline (peak near $0.55$) — it is simply no longer the result being sold, and its role now is to break A($\tau$)'s orientation clause. |
| The unconditional attenuation claim: $|\partial\Delta^{\mathrm{act}}/\partial\kappa|$ decreasing in $\omega_P$, asserted as a monotone consequence of shifting mass to the disclosed cell, with no composition term and no margin distinction. | **DROP** | Split and conditioned. The weight effect is kept and proved ($W_T \le 1$, $W_\tau$ likewise), but the composition effect is a separate ratio: T1(B) gets threshold attenuation *unconditionally* because *both* $W_\tau$ and $C_\tau$ lie in $[0,1]$; T1(C) makes the window margin an **iff**, $W_T C_T \le 1$, with $C_T$ unsigned. O-1 is a disclosure-regime analogy whose composition ratio can exceed one; it is not a window measurement. The genuine window comparison is `t2_t1_check` block 4. An unconditional window sign is not available. |
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
| `t2_l2_check` | **FAIL** (1 of 5) | L2's own content passes exactly: the flagged range of $M_F$ over 19 $\kappa$ values is $0$ and its $\kappa$-derivatives are $0$ — the flagged path never touches the $\kappa$-dependent array. Two placebos confirm the pooled side does move. **The failure is the fifth check**, an *ancillary* A($\tau$)-orientation placebo: see §6, fact 2. Because A($\tau$) does not sign $A'_\kappa$ (Example A has $A'_\kappa=-1/4$), the placebo is misformulated and does not decide A($\tau$)'s support condition; it is not a failure of L2. |
| `t2_l3_check` | **PASS** — 10 checks, 0 FAIL | The derivative identity, the mean-value form $C_h = \tfrac14 \bar\pi^2 h''(\zeta)$, the quadratic rate as $\bar\pi \downarrow 10^{-4}$, the affine-kernel zero-chord case, and three failure witnesses (a tent kernel with no root, the four-atom Example B gap, an unbounded-$h''$ witness). *Scope*: it runs on the three- and four-atom analytic laws and the standalone chord module — it does *not* enumerate the two-round model, so it verifies L3's mathematics, not A($\tau$)'s applicability. |
| `t2_l4_check` | **PASS** — 10 checks, 0 FAIL | All three sign legs with **zero violations** over 16 tightening steps (§6, fact 3); the exact reclassification identity at $10^{-16}$; flatness in $\kappa$ at exactly $0$ over 71 nodes; the $\tau$-grid spanning a ninefold range in $\omega_a$; L3's quadratic corollary within $2.1\%$. Prediction 5 (the size of the $A'_\kappa$ channel) is *reported, not gated*, by the request's own instruction: median absolute residual $0.0352$, max $0.1213$. |
| `t2_p1_check` | **FAIL** (1 of 10) | Nine substantive checks pass: inner-root single crossing and transversality, the flagged family single-valued with the right slope, sequential optimality of the flagged component, both cells on path, the threshold reformulation, monotonicity of $\Omega$ in $(\tau,T)$, and *existence at the core nodes* under the full 30-seed multistart. **The failure is the grid sweep**: 23 of 27 policy nodes met the binding payoff-scale criterion ($10^{-9}$) and 4 did not, at best payoff scales $1.5\times10^{-3}$, $1.1\times10^{-3}$, $4.0\times10^{-4}$, $3.1\times10^{-4}$ — all four at extreme liquidity $\kappa \in \{0.15, 0.85\}$, at $\tau \in \{0.05, 0.075\}$ and $T \in \{5, 1\}$ (the independent re-run corrected an earlier gloss here: these are *not* zero-engagement-share or $T{=}H$ corner nodes — every actual corner row converged, and the recorded pooled prior engagement share is $0.102$). Seed coverage is *ruled out* as the cause: the check re-ran all four nodes at the full 30 seeds and found identical best residuals, with most seeds landing on the same cutoff vector. All 27 nodes do converge on the cutoff-scale criterion. The cause is undiagnosed — candidates are a failure of A3's single crossing at those $\kappa$ extremes (the adjacent-plan payoff gap is a sawtooth on this menu; single crossing is a calibration fact, not structural) or a genuine boundary non-existence outside the repaired P1 hypothesis set. The check is retained as it ran, and **P1 is PROVED**: it was demoted on 2026-08-23 on the form-mismatch, sunk-cost and $\kappa=1$ review findings, and restored on 2026-08-25 on its ticket-35 repair, the amended statement carried through a fresh two-pass gate; the 2026-08-21 chain is retained and did not satisfy the gate for the recorded statement. The four nodes are named, not smoothed. |
| `t2_t1_check` | **FAIL** (1 of 9) | The factorisation $\mathcal{S} = (1-\Omega)\mathcal{S}_P$ holds pointwise to $1.2\times10^{-16}$ and in total variation to $2.2\times10^{-19}$; $\Omega$ is flat in $\kappa$ at $0$ residual; the threshold margin, the window margin, the O-1 benchmark and the composition factors all pass; $H=12$ robustness passes. **The failure is block 3**, the chord-magnitude route with hard-coded Example-A coefficient $0.25$: see §6, fact 2. It is not a refutation of A($\tau$)'s general support representation. One check is *vacuous* (the local form, which needs a smooth window interpolation the integer calendar does not provide). |
| `t2_c1_region_check` | **PASS** — 12 checks, 0 FAIL, pointwise nodes *nonempty* | 80 nodes ($8\ \kappa \times 5\ \tau \times 2\ T$), 2.9 hours of wall time. Two gated verdicts, both PASS with 0 violations: the bound contains the four-corner re-solve remainder at the 8 validation nodes (max ratio $0.511$), and it contains the implicit-function remainder at all 80 (max ratio $1.0$). **18 pointwise dominance-and-contraction nodes**, all at $T = 5$ and the upper three $\tau$ percentiles; $\eta_r \in [0.0595,\ 1.7227]$, median $0.3467$; $L_{\mathcal{R}} \in [0.264, 0.501]$ with no node at $L \ge 1$. These nodes verify the two inequalities and supporting diagnostics only, not the full C1 antecedent or a named region. *Failure attribution*, recorded not hidden: 56 nodes have $g_r^{PE} = 0$ to $10^{-10}$ because the implemented legal clock quantises the crossing date, so $\Omega(\tau)$ is locally constant and the cross-derivative vanishes identically there; 4 are positive but dominated; 2 are negative; 40 nodes (all $T = 10$) are degenerate on flagged mass below $0.01$. The sharper, non-inversion-free bound would certify 22 rather than 18 — reported as a measure of the Neumann step's price, and certifying nothing. No tolerance was weakened to make the pointwise node set nonempty. |

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

*Sources, all in the `v4-theory` worktree: `research/model_v4/MODEL_CARD.md` (stamp 2026-08-28,
re-review audit repairs) for §§1–6; `research/model_v4/LABEL_LEDGER.md` for the labels;
`research/model_v4/proofs/` and `research/model_v4/rederive/` for the two-pass evidence chains;
`research/model_v4/HANDOFF_sign.md` and `quality_reports/fixes/t1_o1_rerun_check.json` for the O-1
numbers; `quality_reports/fixes/t2_*_check.json` for the check inventory;
`numerical_v4/smoke_output.txt` for the smoke facts.*
