# MODEL CARD — v4 two-round blockholder disclosure model

**Version stamp: 2026-08-23 · post-review repairs · commit `<pending-orchestrator-hash>`.** An answer written against a stale stamp is
re-asked, not accepted. Regenerated from `threads/thread1_turn1_answer.md` after the turn-1 audit
(`threads/thread1_turn1_audit.md`), revised after the turn-2 proof-read
(`threads/thread1_turn2_audit.md`), surgically edited for ticket 24's A7 construction, and
regenerated here after the 2026-08-23 post-review repair batch. Seven result rows moved from
CONJECTURE to PROVED on 2026-08-21 (commit `627642c`); C1 moved on 2026-08-22 (commit `403ac8e`);
and P1 was demoted on 2026-08-23 after the GPT end review and its audit (commit `43a45f8`). Every §4/§5 change below is traceable
to a named audit or re-derivation finding; the label moves are logged in
`research/model_v4/LABEL_LEDGER.md`. Vocabulary is `CONTEXT.md`.

## 1. Position and object

The disclosure rule *is* the market's partition. The model asks how liquidity $\kappa$ moves bidder
entry and the expected takeover premium when a stake threshold $\tau$ and a filing window $T$ split
control-node histories into a **flagged** cell (the filing has landed before the control decision)
and a **pooled** cell (it has not). The control-outcome object is the expected engagement-related
premium $\Delta^{\mathrm{act}}(\kappa,\tau,T)$; the price-path objects are the run-up path $R_d$,
the cumulative run-up $R$, and the filing-day jump $J$. Lower $\tau$ = tighter threshold margin;
lower $T$ = tighter window margin.

## 2. Timing (the two rounds)

1. Nature draws $v$ and the blockholder's signal $s$; the blockholder picks one complete contingent
   plan $j$ from a finite ordered menu.
2. **Round 1 — pooled trading.** The plan's stake path executes over business days
   $d = 0,\dots,H$. Market makers see pooled order flow and set $P_d^P = \mathbb E[Y \mid
   \mathcal H_d^P]$. **No within-window re-optimisation** — hence no feedback from realised order
   flow or prices into the path: $B_j(s,d)$, $q_{jd}(s)$ and $Q_j^F$ are functions of $(j,s,d)$ and
   $(j,s,\tau,T)$ alone. L2 Steps 3 and 6 fail without this; cite it as a numbered hypothesis.
3. **Disclosure node.** The flag lands iff $D = 1$, i.e. iff the plan engages, crosses $\tau$ at
   some date $c < \infty$, and $c + T \le H$. The filing reveals $F = (B^F, a = 1)$.
   **The flag terminates the pooled round.** Pooled trading stops when the filing lands; the flagged
   round follows it and the bidder acts after that. Without this reading
   $Q^F = b^*_j(s) - B^F_j(s)$ is not the blockholder's whole residual position and P1's
   flagged-round step fails (P1 re-derivation change C5, `rederive/P1_rederivation.md` Step 2).
4. **Round 2 — flagged trading, then the bidder.** If $D = 1$ the blockholder submits $Q^F$, the
   market prices $P^F = P(F, Q^F)$, then the bidder decides. If $D = 0$ there is no flagged round
   and the bidder acts on the pooled history.

Sequence: pooled round $\to$ flag or no flag $\to$ flagged round if applicable $\to$ bidder decision.

## 3. Equilibrium notion

**Cutoff perfect Bayesian equilibrium.** (i) a weakly ordered cutoff vector
$k = (k_1 \le \dots \le k_{J-1})$ mapping $s$ into a plan; (ii) sequentially optimal pooled and
flagged components; (iii) Bayes-consistent beliefs on path; (iv) competitive pooled and flagged
prices at their fixed points; (v) the bidder-entry rule; (vi) off-path beliefs as limits of
full-support perturbations. Weak inequalities permit collapsed action regions (including Hold).
Existence is Brouwer on the compact ordered polytope $\Theta$ for the outer map
$\mathcal T(k;\vartheta)$; $k = \mathcal T(k;\vartheta)$. Uniqueness is **not** claimed.

## 4. Symbol table

### 4.1 Primitives

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $v$ | target standalone value | $v \sim N(\mu_v,\sigma_v^2)$ |
| $s = v + \varepsilon$ | blockholder's private signal | $\varepsilon \sim N(0,\sigma_\varepsilon^2)$, $\perp v$ |
| $\beta$ | Gaussian projection in $\mathbb E[v\mid s] = \mu_v + \beta(s-\mu_v)$; $\beta = \sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)$ | $\beta \in (0,1)$ — **draft_v2's name; the turn-1 answer wrote $\lambda_s$. Bare $\lambda$ is reserved for D7.** |
| $\xi$ | bidder's private synergy shock | $\xi \sim N(0,\sigma_\xi^2)$, $\perp (v,s)$ |
| $\bar S$, $K$ | mean bidder synergy; bidder entry cost | $K > 0$ |
| $m_0, m_1$ | takeover premia without / with engagement | $m_1 > m_0$; **and $m_0 \ge 0$** — adopted from P1's h.12, so $\bar m(\mathcal I) = m_0 + \pi(\mathcal I)\Delta_m \ge 0$. This is what makes the inner pricing fixed point exist, be unique and be continuous (see A5). Dropping it produces both nonexistence and three-root multiplicity in executed counterexamples (`proofs/P1_proof.md` Step 7; `rederive/P1_rederivation.md` Lemma 2, Checks A/B) |
| $\Delta_m = m_1 - m_0$ | premium wedge | $\Delta_m > 0$ |
| $\Delta_V$ | non-takeover value created by engagement | $\Delta_V \ge 0$ |
| $\kappa$ | **noise-trading intensity** (= liquidity; never depth/volume/turnover) | $\kappa \in [0,1]$ |
| $\bar z$ | size of a ternary noise mark; $\Pr(z_d = 0) = 1-\kappa$, $\Pr(z_d = \pm\bar z) = \kappa/2$ | $\bar z > 0$ |
| $\tau$ | stake threshold | lower $\tau$ = tighter |
| $T$ | filing window, business days | $T \in \{1,\dots,H\}$; lower $T$ = tighter |
| $H$ | control-decision horizon (business days) | $H$ finite |
| $b_0, \bar b$ | initial and maximum stake | $0 \le b_0 \le \bar b$; **maintained $b_0 < \tau$** — a pre-existing crossing is outside the core (turn-2 audit D1-O1) |

### 4.2 Plans and legal timing

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $\mathcal J$, $j$ | finite ordered plan menu, least to most aggressive; plan index | $|\mathcal J| = J < \infty$ |
| $a_j$ | engagement attached to plan $j$ | $a_j \in \{0,1\}$; $a_j = 1$ for Voice, $0$ for Exit/Hold |
| $B_j(s,d)$ | cumulative pooled stake at day $d$; $B_j(s,-1) = b_0$ | $\in [0,\bar b]$; for Voice: $\partial_d B_j \ge 0$ and $\partial_s B_j \ge 0$; Hold constant, Exit weakly decreasing. **And, for every plan and every $d$, $s \mapsto B_j(s,d)$ is Borel** — automatic for Voice (monotone in $s$) and Hold (constant), but a **genuine addition for Exit**, where the card supplied monotonicity in $d$ only; without it the pooled prices in D1's part (c) are not defined, because pooled pricing integrates over every type including Exit types (`rederive/core_D1_L1_L2_rederivation.md` §A hypothesis H9 and consolidated finding 1 — the re-derivation makes D1's PROVED label conditional on this clause being on the card). **Continuum-valued** — A2′'s finiteness covers the plan menu, $\Gamma$'s image, the noise support and the calendar, *not* the stake level. On the flagged set the **composed terminal target** $s \mapsto b^*_{j(s)}(s)$ must be strictly increasing **for every cutoff vector $k \in \Theta$** (hypothesis **A7′ (on-path composed target)**, `proofs/A7_construction.md`). This strictness applies only to flag-capable composed targets: passive plans that never flag need not have strictly increasing $b_j^*$, and there must be no backtracking of $b_j^*$ across admissible Voice-plan switches. The stronger **A7-J (joint tuple injectivity)** is the condition $(j,s) \mapsto (B_j^F,Q_j^F,a_j)$ is injective on the full flagged-pair set; it is distinct from A7′'s on-path condition. Strictness of $B^F$ is neither necessary (it fails at crossing-date jumps on the pro-rata menu) nor sufficient (multi-Voice backtracking). Replaces the 2026-08-20 strict-pair patch (turn-2 audit L2-R1) per ticket 24 |
| $b_j^*(s) = B_j(s,H)$ | terminal target stake | $\in [0,\bar b]$ |
| $c_j(s;\tau) = \inf\{d : B_j(s,d) \ge \tau\}$ | threshold-crossing date | $+\infty$ if never |
| $f_j = c_j + T$ | legal filing date | flag lands iff $f_j \le H \iff B_j(s,H-T) \ge \tau$ |
| $D_j(s;\tau,T)$ | disclosure indicator $\mathbf 1\{a_j=1,\ c_j<\infty,\ f_j \le H\}$ | $\in\{0,1\}$; $D=1 \Rightarrow a=1$ |
| $B_j^F = B_j(s,f_j)$ | stake at filing | $T' < T \Rightarrow B^F(T') \le B^F(T)$ at fixed policies |
| $Q_j^F = b_j^*(s) - B_j^F$ | flagged-round order | $Q^F \ge 0$ for Voice plans; $T' < T \Rightarrow Q^F(T') \ge Q^F(T)$ |
| $\Gamma$ | finite ordered coarsening, stake increment $\to$ pooled order mark | **renamed from the answer's $\psi$; $\psi$ is D7 pivotality, $\chi$ is draft_v2's cost parameter** |
| $q_{jd}(s) = \Gamma(B_j(s,d) - B_j(s,d-1))$ | informed pooled order mark | ordered in the increment |
| $z_d$, $X_d = q_{jd} + z_d$ | noise order; observed pooled order flow | $z_d \in \{-\bar z, 0, +\bar z\}$ |

### 4.3 Information, prices, control outcome

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $\mathcal H_d^P$ | pooled public history: $(X_0,\dots,X_d;$ flag landed by $d)$ | finite |
| $F = (B^F, a=1)$ | filing message | truthful (A4) |
| $\mathcal I_H$ | **control-node information set, now filled** (the row read "—" until this regeneration): the *public* information at the control node — $\mathcal I_H = \mathcal H_H^P$ on the pooled cell $\{D=0\}$, and the flagged tuple $\mathsf S_F = (B^F, Q^F, a{=}1)$ on the flagged cell $\{D=1\}$. The bidder's own $\xi$ is private, else §4.3's $p(\mathcal I)$ would be an indicator | fill required by D1's cell-map clause and by L2's posterior clause, both of which are claims *about* $\mathcal I_H$ (`rederive/core_D1_L1_L2_rederivation.md`, reading RD-1 and consolidated finding 2). RD-1 states the flagged fill as $(\mathcal H_{f^-}^P, F, Q^F)$; **L2 is exactly the statement that the two are informationally equivalent on the flagged set** (conditional on $\mathsf S_F$ the pooled residual is pure noise), and L2 was re-derived in a form robust to either fill |
| $\mathcal C_F, \mathcal C_P$ | flagged / pooled cells | exclusive and exhaustive by construction |
| $\pi(\mathcal I) = \Pr(a=1\mid\mathcal I)$ | engagement posterior | $\in[0,1]$; $=1$ on $\mathcal C_F$ |
| $p(\mathcal I)$ | bidder-entry probability $1 - \Phi\big((P+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)$ | $\in(0,1)$ |
| $\mathsf B$, $Y$ | entry indicator; terminal shareholder payoff $ (1-\mathsf B)(v + a\Delta_V) + \mathsf B(P + m_0 + a\Delta_m)$ | — |
| $P_d^P$, $P^F$ | competitive pooled price; flagged price $P(F,Q^F)$ | $P(\mathcal I) = \mathbb E[Y\mid\mathcal I]$ (inner fixed point). **Convention $P_{-1}^P := \mathbb E[Y]$**, the pre-trading pooled price — needed whenever $c=0$, which $T=H$ forces on every flagged history (turn-2 audit D1-R3). **The genuine fixed point sits at control nodes.** At an earlier pooled date $d<H$ the price is a *tower expectation* of already-solved control-node values, with no self-reference; only the control-node map is a fixed point to be solved (batch-1 audit P1-R8, `proofs/P1_proof.md` Step 5, split (a)/(b)) |
| $P_{\mathrm{ND}}(\mathcal H_{f^-}^P)$ | the **not-yet-disclosed** price at $f^-$ — the last pre-filing pooled price, at the **same realised order flow** (its history already carries "flag not landed by $f-1$"). **Not** a never-disclosed counterfactual: under that reading D1's identity acquires a residual term | $= P_{f^-}^P$ by construction (`rederive/core_D1_L1_L2_rederivation.md`, reading RD-3 and consolidated finding 7) |
| $R_d = P_d^P - P_{c^-}^P$, $R = P_{f^-}^P - P_{c^-}^P$ | run-up path, cumulative run-up | unsigned |
| $J = P^F - P_{\mathrm{ND}}$ | filing-day jump | unsigned; **not** claimed $\kappa$-invariant |
|  | identity: $P^F - P_{c^-}^P = R + J$ | exact |
| $U_j(s)$ | **the blockholder's objective** (new row; both passes flagged the card had none). The expected terminal value of the position the plan builds, net of what it costs to build and to engage: $U_j(s) = \mathbb E\bigl[b_j^*(s)\,Y - \mathcal C_j^{\mathrm{trade}} - a_j C_j(s) \bigm\vert s, j\bigr]$, with $\mathcal C_j^{\mathrm{trade}}$ the execution outlay (increments valued at the pooled prices $P_d^P$ up to the plan's last pooled date, plus $Q^F_j(s)P^F$ when $D_j=1$) and $C_j(s)\ge 0$ the engagement cost | **Definition is `proofs/P1_proof.md` h.14** (displayed there in full; `rederive/P1_rederivation.md` H12 writes the same object out term by term). Only two properties are ever used: **plan-locality** — $U_j$ depends on $j$ only through the executed stake path, the prices paid on it, the terminal stake, the engagement flag and the cost — and **integrability**, $\mathbb E[\max_j\lvert U_j\rvert] < \infty$ under A2′. Card gap closed here per batch-1 audit P1-R6 and P1 re-derivation change C2 |

### 4.4 Premium and comparative statics

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $h(\mathcal I) = \pi(\mathcal I)p(\mathcal I)$ | engagement-premium kernel | $h \ge 0$, $h(0) = 0$ |
| $\Delta^{\mathrm{act}} = \Delta_m\,\mathbb E[h(\mathcal I_H)]$ | expected engagement-related premium | $\ge 0$ |
| $M_F$, $M_P$ | $\Delta_m\mathbb E[h\mid D=1]$, $\Delta_m\mathbb E[h\mid D=0]$ | defined when the cell has mass |
| $\Omega = \Pr(D=1)$ | unconditional flagged weight; $\Omega = \Pr(a=1)\,\omega_a$ | $\in[0,1]$; **$\Omega$ is draft_v2's $\omega_P$ — the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the $\approx 0.29$ cut are all $\Omega$-type** |
| $\omega_a = \Pr(D=1\mid a=1)$ | disclosed share of engagements; the calibration target | $\in[0,1]$; **renamed from bare $\omega$** |
| $\bar\pi$ | **upper support point of the pooled engagement posterior in the A($\tau$) representation** (corrected here; the old gloss "pre-order pooled engagement share in the chord" was wrong and generated the L3/L4 collision) | $\in[0,1]$. **The pooled engagement share is the *mean* $\mathbb E[\Pi_\kappa]$, not $\bar\pi$.** Under A($\tau$) that share is $\kappa$-**invariant** (a mean-preserving spread), so it cannot be the quantity whose $\kappa$-motion L3 describes; it is **strictly below $\bar\pi$ in any non-degenerate case**, and equals $\bar\pi/2$ only under level symmetry $A_0=A_1$, where the martingale property gives $\mathbb E[\Pi_\kappa]=\bar\pi/2$. Reading $\bar\pi$ as the mean forces a point mass at $\bar\pi$ with $A'_\kappa=0$ and zero interior motion for every kernel — degenerate, and excluded. Binding orchestrator ruling 2026-08-21; flagged independently by both writers (`proofs/L4_proof.md` head block; `proofs/L3_proof.md` Step 19) and re-derived independently (`rederive/L3_rederivation.md` CH1, Step 11; `rederive/L4_rederivation.md` CHANGE 8) |
| $\mathcal S = \lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$, $\mathcal S_P = \lvert\partial_\kappa M_P\rvert$ | liquidity-sensitivities | $\ge 0$; $\mathcal S = (1-\Omega)\mathcal S_P$ under L2 + fixed policies |
| $C_h(\bar\pi) = h(0) - 2h(\bar\pi/2) + h(\bar\pi)$ | the chord | **= draft_v2's $\mathcal C(\bar\pi)$, condition (C\*), `lem:d1-jensen`**; maintained $\le 0$, $\lvert C_h\rvert$ weakly increasing in $\bar\pi$ |
| $A'_\kappa$ | common derivative of the A(τ) weights ($A_0' = A_1' = A'_\kappa$, $A_{1/2}' = -2A'_\kappa$) | bounded on $[0,1]$; **renamed from $a_\kappa$; $a$ is engagement** |
| $W_\tau, W_T$ | weight-effect ratios, e.g. $W_T = (1-\Omega(\tau,5))/(1-\Omega(\tau,10))$ | $\le 1$ when $\Omega$ rises |
| $\eta_r$ | C1 slack (see §4.5) | $>0$ on dominance-and-contraction nodes |
| $C_\tau, C_T$ | composition-effect ratios, e.g. $C_T = \mathcal S_P(\tau,5)/\mathcal S_P(\tau,10)$ | unsigned; kept (CONTEXT.md's "composition effect") — but $C$ is overloaded: $C_h$ chord, $C_j(s)$ engagement cost, $\mathcal C_F/\mathcal C_P$ cells. Always keep the margin subscript |

### 4.5 Equilibrium and GE dominance/contraction

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $k = (k_1,\dots,k_{J-1})$ | cutoff vector | $k_1 \le \dots \le k_{J-1}$; maps to draft_v2's $(k_1,k_0,k_D)$ when the menu is the four named actions |
| $\Theta$, $\vartheta$ | compact ordered cutoff polytope; parameter vector | $\Theta$ nonempty, compact, convex |
| $\mathcal T(k;\vartheta)$ | outer cutoff best-response map (**always calligraphic** — upright $T$ is the window) | continuous, $\Theta \to \Theta$ |
| $L_{\mathcal R} = \sup_{\mathcal R}\lVert D_k\mathcal T\rVert$ | contraction bound on region $\mathcal R$ | $< 1$ required by AGE |
| $r_\tau = -\tau$, $r_T = -T$ | strictness coordinates | higher $r$ = tighter |
| $g_r^{PE} = -\mathrm{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{act}}$ | direct fixed-policy attenuation margin (**the sign is written inline; no symbol $\sigma_\kappa$**) | $> 0$ required by C1 |
| $\bar k_x = \lvert\partial_x\mathcal T\rvert/(1-L_{\mathcal R})$, $\bar k_{\kappa r}$ | inversion-free derivative bounds | $\ge 0$ |
| $\mathcal B_r^{GE} = \lvert\Delta_{\kappa k}\rvert\bar k_r + (\lvert\Delta_{kr}\rvert + \lvert\Delta_{kk}\rvert\bar k_r)\bar k_\kappa + \lvert\Delta_k\rvert\bar k_{\kappa r}$ | GE remainder bound (cross-derivative analogue of D8's $\bar B$) | $\ge 0$; C1 needs $g_r^{PE} > \mathcal B_r^{GE}$ |
| $\mathcal R_r$, $\eta_r = g_r^{PE} - \mathcal B_r^{GE}$ | dominance-and-contraction region; slack | $\eta_r > 0$ at dominance-and-contraction nodes; region may be empty |

### 4.6 Proof-local notation (turn-2 rulings, binding)

L2's proof symbols, after the turn-2 notation audit: $\Xi := (v,s,\xi)$ (**renamed from $W$** — $W$ is
draft_v2's total surplus *and* its D5 wedge *and* the card's $W_\tau/W_T$; **never a bare $W$**);
$\Upsilon_{j,s}$, noise $\to$ pre-filing pooled history (**renamed from $G$** — draft_v2's $G_{EH},
G_{HQ}, G_{QP}$ payoff gaps and D7's bargaining surplus); $\mathsf Z$ **dropped** (write "each object
listed"); $\mathsf S_F=(B^F,Q^F,a{=}1)$ kept, introduced once as "$F$ augmented by $Q^F$", **never
bare**; $\mathcal H^P$ kept as shorthand for $\mathcal H_{f^-}^P$, subscript written at first use in
every proof; $\mathbf z^H$ kept, $z_{0:H}$ preferred; $\iota_F$ free; $u_1,u_2$ proof-local, never a
bare $u$.

## 5. Standing hypotheses

- **A1 Independent primitives.** $v,\varepsilon,\xi$ and all $z_d$ mutually independent; all
  variances strictly positive.
- **A2′ Finite model, amended boundedness** (was A2; the boundedness clause was **false**). The
  finiteness clauses are unchanged: plan menu $\mathcal J$, the image of $\Gamma$ (order-mark
  support), the noise support $\{-\bar z,0,+\bar z\}$ and the calendar horizon $H$ are finite. The
  boundedness clause is **replaced** by: *prices and payoffs are locally bounded in $(s,\vartheta)$
  on the maintained parameter set, and $\mathbb E\bigl[\max_{j\in\mathcal J}\lvert U_j\rvert\bigr]
  < \infty$ for every $k\in\Theta$.*
  *Why (P1 re-derivation change C1, `rederive/P1_rederivation.md` H2, Steps 3 and 12; adjudicated
  2026-08-21).* Flat global boundedness is **inconsistent** with the rest of the card: $v$ is
  Gaussian (§4.1) and the flagged region is unbounded in $s$ under A7′, so $Y$ — and with it prices
  and $U_j$ — is unbounded. Integrability is all any proof actually consumes. Every prior citation
  of "A2" in the proofs on file should be read as A2′; nothing in D1, L1, L2, L3, L4, P1 or T1 used
  the flat bound.
- **A3 Ordered plans, single crossing.** At every belief/price system, adjacent-plan payoff
  differences cross zero at most once in $s$, and the preferred plan is weakly increasing in $s$.
- **A4 Legal-clock discipline.** $c$ is the first date the path reaches $\tau$; filing lands exactly
  at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in the core.
- **A5 Inner pricing regularity, mostly demoted to a theorem.** Each public-history pricing map has a
  unique fixed point, continuous in beliefs, cutoffs and parameters.
  *Note (ticket 27, 2026-08-21).* **Under $m_0 \ge 0$ — now a card restriction, §4.1 — existence,
  uniqueness and continuity of the *inner* fixed point are THEOREMS, not assumptions.** The pricing
  map reduces to a scalar equation in two belief summaries: with $\bar y(\mathcal I) =
  \mathbb E_\mu[v] + \pi\Delta_V$ and $\bar m(\mathcal I) = m_0 + \pi\Delta_m$, the right-hand side
  is $P \mapsto \bar y + \bar m\,p(P)/(1-p(P))$ — the ticket-25 build writes the same map as
  $P = \hat V + \tilde m\,p/(1-p)$ — and it is strictly decreasing in $P$ wherever $\bar m \ge 0$,
  so it crosses the identity exactly once. **Three independent confirmations**: `proofs/P1_proof.md`
  Step 7; `rederive/P1_rederivation.md` Lemma 2 (with an executed counterexample producing zero
  roots, and another producing three, once $m_0<0$); and the ticket-25 build, whose
  `multiple_root_nodes` counter is structurally $0$ for the same reason (`impl_design.md` §13 and
  the smoke output). **A5 is retained only as its continuity clause** — the pricing family is
  continuous in the cutoff vector and the parameters, and measurable in the flagged tuple (the
  flagged information sets are continuum-indexed, so "unique fixed point" must be read as a
  measurably selected *family*, not a finite list). Where a proof cites A5 for existence or
  uniqueness, it may now cite §4.1's $m_0\ge0$ instead.
- **A6 Compact outer self-map.** All best-response cutoffs lie in a common compact ordered polytope
  $\Theta$; $\mathcal T$ is continuous and maps $\Theta$ into itself.
- **A7 Filing sufficiency.** On flagged histories $(B^F,Q^F,a=1)$ identifies the informed component
  of the selected plan; conditional on it, the pooled order-flow residual is pure noise, independent
  of $(v,s,\xi)$. The weak identification wording is not enough for L2. The two injective forms are
  named separately:
  * **A7′ (on-path composed target).** At a fixed cutoff policy, the composed terminal target
    $s\mapsto b^*_{j(s)}(s)$ is strictly increasing on the flagged signal region. The card's §4.2
    row quantifies this over every cutoff vector $k\in\Theta$; strictness is required only for
    flag-capable composed targets, with no backtracking across admissible Voice-plan switches.
  * **A7-J (joint tuple injectivity).** The full map
    $(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ is injective on the flagged-pair set, including flagged pairs
    that are not selected on path. This is stronger than the on-path A7′ form and is the form the
    pre-review P1 proof consumed.
  *Note (turn-2 proof-read).* **L2 uses A7′ on path; the weak wording is not sufficient** — it permits
  two $(j,s)$ pairs with different pooled paths, which is exactly L2's first failure case. Under A7′,
  the flagged tuple is continuum-valued as a tuple: injectivity forces $(B^F,Q^F)$ to be
  continuum-valued, while the coordinates may trade the burden. Injectivity plus measurability
  already gives the measurable inverse (standard Borel spaces); no separate assumption is needed.
  *Note (ticket 24, 2026-08-21).* **Satisfiability is resolved for A7′.** A7′ + a fixed cutoff
  policy + $\Omega > 0$ deliver the on-path injective form (positive-probability flagged tuples) with
  an explicit inverse; a satisfying menu exists — the pro-rata single-Voice menu with terminal target
  strictly increasing on all of $\mathbb R$, which also satisfies A7-J
  (`proofs/A7_construction.md`; adversarial attack verdict SURVIVES WITH REPAIRS,
  `proofs/A7_attack_verdict.md`, repairs applied 2026-08-21). A7-J additionally needs $b^*$ strictly
  increasing off the Voice region — a target flat below the Voice cutoff breaks it (40-collision
  executed check) while leaving A7′ intact. Failure boundary: a binding stake cap, quantized stakes,
  a composed target repeating values across Voice-plan switches, $\Omega = 0$, and policy-dependence
  when the condition is stated only at one equilibrium's cutoffs. A7′-satisfying menus are fully
  separating on the flagged set — the burden moves to P1's incentive compatibility, not away.
- **A8 Interior crossing.** $0 < \Omega(\kappa,\tau,T) < 1$. Required only for positive cell mass,
  never for the structural partition.
- **A($\tau$) Threshold chord restriction.** The pooled posterior law has the symmetric ternary
  representation $\mathbb E[h] = A_0(\kappa)h(0) + A_{1/2}(\kappa)h(\bar\pi/2) + A_1(\kappa)h(\bar\pi)$
  with $A_0' = A_1' = A'_\kappa$ and $A_{1/2}' = -2A'_\kappa$; maintained orientation
  $C_h(\bar\pi)\le 0$ with $\lvert C_h\rvert$ weakly increasing in $\bar\pi$. (draft_v2's (C\*) is
  the strict version; the $C_h = 0$ case must be handled explicitly.)
  **Two clauses added at this regeneration, each established by both L3 passes:**
  * **(τ-i) The kernel depends on the information set only through the engagement posterior.**
    $h(\mathcal I) = h(\pi(\mathcal I))$, so the three numbers $h(0)$, $h(\bar\pi/2)$, $h(\bar\pi)$
    are well defined and $\kappa$-free. This is a **restriction, not a reading**: §4.4 defines
    $h = \pi p$ and §4.3's entry row makes $p$ depend on the price as well as on $\pi$, so in the
    model $h = \pi\,p(\hat v, \pi)$ is a function of *two* scalars. The clause says the
    standalone-value channel and the engagement channel do not co-move inside the pooled cell in a
    way that moves $h$ at a fixed posterior. (`proofs/L3_proof.md` Hypothesis 8, batch-1 audit
    L3-R1; `rederive/L3_rederivation.md` CH3.)
  * **(τ-ii) The support and $\bar\pi$ are $\kappa$-free; only the weights move.** The three points
    $\{0, \bar\pi/2, \bar\pi\}$ do not vary with $\kappa$, and $\bar\pi$ itself is $\kappa$-free at
    fixed $(\tau,T)$. **Without the second half L3's conclusion is FALSE** — the derivative gains a
    term that is first order in $\bar\pi$ and the vanishing fails. (`rederive/L3_rederivation.md`
    CH2, the one omission the re-deriver said could sink the result;
    `proofs/L3_proof.md` Hypothesis 1.)

  *Where A($\tau$)'s bite actually is (L3's finding, both passes).* The derivative restrictions
  $A_0'=A_1'=A'_\kappa$, $A_{1/2}'=-2A'_\kappa$ are **not** an extra assumption: given a
  $\kappa$-invariant three-point support they are **equivalent** to $\kappa$-invariance of the
  pooled block's total mass and of its unnormalised engagement moment, both of which the model
  delivers at fixed policies. **A($\tau$)'s entire remaining content is the support condition.**
  A one-round ternary-noise market with informed mark $2\bar z$ and pre-order engagement share
  $\tfrac12$ satisfies it; the frozen manuscript's own no-disclosure structure (informed mark
  $\bar z$) does **not** — its pooled law has four atoms, two of which move with $\kappa$.
  **Whether the two-round pooled cell of §2 satisfies the support condition is OPEN**
  (`proofs/L3_proof.md` Part IV, Steps 16–18, with the weakest sufficient conditions named there).
  Every L3-conditional result — and therefore L4 leg 3 and T1 Part B — inherits that conditionality.

- **A(br) Chord–sensitivity bridge.** *(NEW at this regeneration. Consumed by L4 leg 3 and by T1
  Part B, and by nothing else. Statement transcribed from `proofs/L4_proof.md`'s top block as
  repaired on 2026-08-21, with (br-v) appended.)* For two compared thresholds $\tau' < \tau$ at
  fixed policies and a common $\kappa$:
  * **(br-i) Representation at both policies.** A($\tau$)'s symmetric ternary representation holds
    for the pooled class under $\tau$ *and* under $\tau'$, with chord endpoints $\bar\pi(\tau)$,
    $\bar\pi(\tau')$ and weight-derivative coefficients $A'_\kappa(\tau)$, $A'_\kappa(\tau')$.
  * **(br-ii) $\kappa$-localisation.** At fixed policies all $\kappa$-dependence of $M_P$ sits in
    the A($\tau$) weights: the three support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$
    *as a function of the posterior* do not move with $\kappa$. Hence
    $\partial_\kappa M_P = \Delta_m A'_\kappa C_h(\bar\pi)$ exactly, with no
    composition-through-$\kappa$ remainder. (Against the card's *literal* A($\tau$) display this
    would restate (br-i); it is written against the honest reading $h = \pi\,p(\hat v,\pi)$, and it
    is the clause that repairs that ambiguity rather than a fourth independent restriction — it
    names the same object as A($\tau$)(τ-i). The trailing "hence" is **derivable**, not assumed:
    `rederive/L4_rederivation.md` CHANGE 4, Step 16.)
  * **(br-iii) Coefficient stability across the threshold margin.**
    $\lvert A'_\kappa(\tau')\rvert \le \lvert A'_\kappa(\tau)\rvert$. Weakest sufficient form:
    equality — reclassification changes *which* histories are pooled, not the
    $\kappa$-responsiveness of the pooled weights.
  * **(br-iv) Endpoint linkage.** $\bar\pi$ is A($\tau$)'s chord endpoint — the **upper support
    point** of the pooled posterior law — and it is a weakly increasing function of the pooled
    prior engagement share $\bar\pi_{\mathrm{pr}} = \Pr(a=1\mid D=0)$, **the same function at
    $\tau$ and at $\tau'$**. (Support-point form, per the binding $\bar\pi$ ruling; the identity
    branch $\bar\pi = \bar\pi_{\mathrm{pr}}$ is excluded as degenerate, `proofs/L3_proof.md`
    Step 19.)
  * **(br-v) Comparability of the chord functional across thresholds.** $C_h(\cdot)$ — and the
    kernel $h$ it is built from — are the **same functions of the posterior** at both compared
    thresholds. Without it, leg 3 compares $\lvert C_h\rvert$ across two different functionals and
    the comparison is meaningless; $h = \pi p$ with $p$ priced off a cell whose composition the
    threshold moves, so $\tau$-invariance of $h$ is real content, not bookkeeping.
    **Independently required by three agents**: the T1 proof-reader (as "(br-v)", batch-2 audit),
    the L4 re-deriver (as "(br-ii′)", `rederive/L4_rederivation.md` CHANGE 3), and the T1
    re-deriver, who confirmed it is required **and** not implied by (br-i)–(br-iv)
    (`rederive/T1_rederivation.md`, Part B verdict). Canonical name is **(br-v)**; T1's proof
    carries it as H17.

  *Sharpening on file, recorded not assumed (`rederive/L4_rederivation.md` CHANGE 8, Steps 22–24).*
  $\bar\pi = \bar\pi_{\mathrm{pr}}/\rho$ with $\rho := \tfrac12 A_{1/2} + A_1$ provably
  $\kappa$-free, so (br-iv) $\iff$
  $\rho(\tau')/\rho(\tau) \ge \bar\pi_{\mathrm{pr}}(\tau')/\bar\pi_{\mathrm{pr}}(\tau)$. Under the
  level-symmetric reading $\rho = \tfrac12$ and $\bar\pi = 2\bar\pi_{\mathrm{pr}}$, which forces
  $\bar\pi_{\mathrm{pr}} \le 1/2$ — an inherited restriction on A($\tau$)'s domain that L4 does not
  resolve. (br-iii) is the clause with the least justification behind it; it is the one to attack
  first.
- **AGE GE differentiability and contraction.** On a candidate region $\mathcal R$ the outer map is
  twice continuously differentiable, $L_{\mathcal R} < 1$, and the sign of the equilibrium liquidity
  derivative is constant on $\mathcal R$.

## 6. Result ledger

**Seven of eight results now carry two-pass evidence** (C1 moved on 2026-08-22, after its own
proof-read, re-derivation, and the independent re-run of every check script — ALL REPRODUCE,
`quality_reports/fixes/t2_rerun_verify_note.md`). The protocol (§7) requires an adversarial
proof-read PASS **and** an independent statements-only re-derivation PASS, by different agents,
before a label moves. That gate is satisfied for D1, L1, L2, L3, L4, T1 and C1. **P1 is
CONJECTURE after the 2026-08-23 GPT end review and audit demotion**; its earlier two-pass chain did
not cover the same statement because the proof consumed A7-J while the row and re-derivation carried
A7′. Every statement below is the *amended*
statement — the hypothesis sets are named in full and descriptively, and **no statement was weakened
silently**: each difference from the pre-regeneration row is traceable to the named finding beside
it. The label moves themselves are logged in `research/model_v4/LABEL_LEDGER.md`.

| ID | Statement (amended), with its full hypothesis set | Label | Evidence chain |
|---|---|---|---|
| D1 | Under **A1, A2′, A4, A5, the §4.1/§4.2 table restrictions, §3(i)'s cutoff selection map, the §4.3 conventions ($P_{-1}^P=\mathbb E[Y]$; $P_{\mathrm{ND}}=P^P_{f^-}$)**, and two hypotheses this regeneration wrote into the card — **Borel regularity of $s\mapsto B_j(s,d)$ for *every* plan including Exit** (now a §4.2 clause; needed only for part (c), since pooled pricing integrates over all types) and **a content for $\mathcal I_H$** (now filled in §4.3) — $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is **measurable** and maps every control-node history into exactly one cell; for every Voice plan $f_j\le H \iff B_j(s,H-T)\ge\tau$; and each flagged history yields $B^F, R_d, R, J$ with $P^F - P_{c^-}^P = R + J$. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `threads/thread1_turn2_answer.md`; **proof-read PASS 2026-08-20** `threads/thread1_turn2_audit.md` (3 non-blocking repairs: uncited public-flag bridge, $B^F$ continuum-valued, $P_{-1}^P$ convention); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/core_D1_L1_L2_rederivation.md` §A — the two added hypotheses are its changes, and both are now card rows, so the row no longer rests on anything the card lacks |
| L1 | Under **D1, the §4.3/§4.4 definitions, A5 (which pins *the* version of $\mathbb E[Y\mid\mathcal I]$), A2′ with §4.1 ($\Delta_m$ finite), and A1 (one probability space)**: whenever $0<\Omega<1$, $\Delta^{\mathrm{act}} = \Omega M_F + (1-\Omega)M_P$; at $\Omega=1$ it degenerates to $\Delta^{\mathrm{act}}=M_F$ and at $\Omega=0$ to $\Delta^{\mathrm{act}}=M_P$, the null-cell average being **undefined rather than imputed** — proved as a non-identification statement, not asserted. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `threads/thread1_turn2_answer.md`; **proof-read PASS 2026-08-20** `threads/thread1_turn2_audit.md` (clean; one cosmetic repair); **re-derivation PASS 2026-08-21, PROVED-AS-STATED** `rederive/core_D1_L1_L2_rederivation.md` §B — no change to the statement |
| L2 | At fixed cutoff and execution policies, under **A1; A2′ *with* the §4.1/§4.2 table restrictions; A4; A5; A7′ in its on-path injective form, consumed almost surely on the flagged set; D1; the no-feedback timing of §2; and $\Omega>0$** — together with an explicit bidder-entry rule (§4.3's, or any rule with the two properties named in the proof), carried as bookkeeping: $(B^F,Q^F,a{=}1)$ makes the pre-filing pooled history conditionally independent of $(v,s,\xi)$ on the flagged set, so the flagged posterior, price, entry probability and $M_F$ are invariant to $\kappa$. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `threads/thread1_turn2_answer.md`; **proof-read PASS 2026-08-20** `threads/thread1_turn2_audit.md` (4 non-blocking repairs; its largest flagged risk — A7 satisfiability — was closed by ticket 24, `proofs/A7_construction.md` + `proofs/A7_attack_verdict.md`); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/core_D1_L1_L2_rederivation.md` §C. **Statement changes, all traceable and none a weakening of the conclusion**: A2′, D1 and the entry rule were *used but not enumerated* in the old row (finding 3); "almost surely" is the re-derivation's own *permissive* reading of A7′, and it is the only coherent one when $B^F$ is continuum-valued, since then no individual flagged tuple has positive probability |
| L3 | **PROVED under A($\tau$)** — including its two new clauses (τ-i) kernel-through-posterior and (τ-ii) $\kappa$-free support **and $\kappa$-free $\bar\pi$** — plus: $h(0)=0$; $\kappa$-free pooled mass and engagement moment at fixed policies; D1 by statement; regularity *stated minimally* ($h$ continuous on $[0,\bar\pi]$, twice differentiable on the open $(0,\bar\pi)$ — Darboux does the rest, no continuity of $h''$); for the small-$\bar\pi$ corollary only, a second-order Peano expansion of $h$ at $0+$ and one and the same kernel along the shrinking family; and, for the seam where L4 consumes L3, $\lvert A'_\kappa\rvert$ bounded **uniformly in $\bar\pi$** along the limit. Then $\partial_\kappa\mathbb E_\kappa[h] = A'_\kappa C_h(\bar\pi)$ exactly; $C_h(\bar\pi) = \tfrac14\bar\pi^2 h''(\zeta)$ for some $\zeta\in(0,\bar\pi)$ — an identity, not an approximation; $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, so the interior motion vanishes at rate $\bar\pi^2$ as $\bar\pi\downarrow 0$. **An "if", never an "iff"** ($A'_\kappa=0$ also kills the motion). **Conditional**: whether the two-round pooled cell satisfies A($\tau$)'s support condition is OPEN (§5, §9). | **PROVED** under A($\tau$) | statement `threads/thread1_turn1_answer.md`; proof `proofs/L3_proof.md` (repairs applied 2026-08-21); **proof-read PASS 2026-08-21** `threads/2026-08-21_batch1_proofread_audit.md` §2 (0 FAIL; L3-R1…R5 applied; executed checks reproduce to $\le 2\times10^{-18}$); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/L3_rederivation.md`. **Changes CH1–CH7 are all hypothesis-explicitness**, folded into A($\tau$)/§4.4 above; CH2 ($\kappa$-free $\bar\pi$) is the one whose omission would have made the conclusion false, and it is now a card clause |
| L4 | At fixed policies, for $b_0 < \tau' < \tau$ at a common window $T$ and a common $\kappa$, with $\Omega(\tau',T)<1$: **(leg 1, unconditional)** $\mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T)$ with every newly flagged history generated by a Voice plan, hence $\Omega(\tau',T)\ge\Omega(\tau,T)$; **(leg 2, unconditional)** the pooled engagement **share** falls, $\bar\pi_{\mathrm{pr}}(\tau')\le\bar\pi_{\mathrm{pr}}(\tau)$, with an exact identity for the gap; **(leg 3, PROVED under A(br))** $\mathcal S_P(\tau',T)\le\mathcal S_P(\tau,T)$, with equality whenever $C_h(\bar\pi(\tau))=0$. Legs 1–2 need only **D1's clock equivalence, the §2 no-feedback timing, fixed policies, $b_0<\tau'<\tau$ imposed at *both* thresholds, A1, A4, §4.2's $D=1\Rightarrow a=1$, and $\Omega(\tau')<1$** — the two "nestedness" clauses the old row implied are **conclusions, not hypotheses**. Leg 3 additionally needs **L3 by statement, A($\tau$)'s maintained *magnitude* monotonicity of $\lvert C_h\rvert$ (the sign half $C_h\le0$ is never used at this leg), and A(br) clauses (br-i)–(br-v)**. | **PROVED** (legs 1–2 outright; leg 3 **under A(br)**) | statement `threads/thread1_turn1_answer.md`; proof `proofs/L4_proof.md` (repairs applied 2026-08-21); **proof-read PASS 2026-08-21** `threads/2026-08-21_batch1_proofread_audit.md` §3 (0 FAIL; L4-R1…R5 applied); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/L4_rederivation.md`. **Traceable changes**: the old row's "under nested reclassification" is replaced by "under A(br)" because nestedness is a *conclusion* (L4 writer's deletion of turn-1 H1–H3, audit L4-R5); the old row's "$\bar\pi$" is replaced by the **share** $\bar\pi_{\mathrm{pr}}$ per the binding $\bar\pi$ ruling; (br-v) is added on three independent findings |
| P1 | Under **A1, A2′, A3, A4, A6, A7′ (on-path injective), D1 by statement, the §2 no-feedback timing read with the flag-terminates-the-pooled-round clause, the definitional round-2 action-set hypothesis** (the flagged-round action set **is** the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements agreeing with $j$ on everything already played — *not* a closure condition; the closure form is jointly unsatisfiable with finiteness by cardinality), **$m_0\ge0$, and the §4.3 blockholder-objective definition $U_j$**: a cutoff PBE over complete contingent plans exists — $k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, prices at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs as limits of full-support perturbations over **plans**, the §4.3 entry rule, and a sequentially optimal flagged component. **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$ (see A5). **At any such equilibrium at which A8 holds**, both cells carry strictly positive probability and are on path; for A8's restatement as a single signal threshold add **H-ord** (Voice stake monotonicity across plans — the writer's h.13, **renamed here to avoid collision with the objective row**) and the upper-set engagement-flag hypothesis. Uniqueness is not claimed. | **CONJECTURE** | statement `threads/thread1_turn1_answer.md`; proof `proofs/P1_proof.md` (repairs applied 2026-08-21); **proof-read PASS 2026-08-21** `threads/2026-08-21_batch1_proofread_audit.md` §4 (0 FAIL; P1-R1…R8 applied; inner fixed point executed on 20k random draws — 0 multiplicity, 0 sign failures); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/P1_rederivation.md` (changes C1–C8). **The old evidence chain is retained, but it did not satisfy the two-pass gate for the recorded statement: the proof's h.7 consumes the joint injective form of A7, while the card row and re-derivation carried the on-path form (form mismatch). The GPT end review and audit additionally identified a missing continuation-cost clause in Step 12 (sunk-cost gap, live for multi-Voice menus) and a false positivity claim at $\kappa=1$. Ticket 35 owns the repair and any future re-promotion.** |
| T1 | At fixed plan and cutoff policies, with $0<\Omega<1$ and $\mathcal S_P>0$: **(A)** $\mathcal S = (1-\Omega)\mathcal S_P$ exactly, and the same factorisation holds for the total-variation aggregate of $\Delta^{\mathrm{act}}$ over any $\kappa$-grid with no differentiability required; **(B)** threshold tightening attenuates — $\mathcal S(\tau')/\mathcal S(\tau) = W_\tau C_\tau \le 1$ because **both** ratios lie in $[0,1]$, no dominance condition needed; **(C)** window tightening attenuates **iff** $W_T C_T \le 1$, where $W_T\le1$ is **proved** (from D1's clock equivalence and the monotone Voice stake path) and $C_T$ is **unsigned** — "equivalently $\partial_{r_T}\mathcal S_P/\mathcal S_P \le \Omega_{r_T}/(1-\Omega)$" holds **on average along the tightening path** (integrated over $[-T,-T']$), exactly in the infinitesimal limit, and is **false read pointwise**. Hypotheses: **fixed policies; A8 at each compared policy; $\mathcal S_P>0$; L1; L2 (its own hypotheses travelling); D1; PE-$\Omega$ ($\partial_\kappa\Omega=0$ at fixed policies — derivable, not assumed, and it fails in GE, which is C1's term); $\kappa$-differentiability of $M_P$ (no card hypothesis supplies this — carried in-proof); A($\tau$) at both compared policies with the $\bar\pi$ ruling; L3; A(br) (br-i)–(br-v) at the threshold pair; L4; the §2 no-feedback timing; a smooth window interpolation for the local form; threshold-side smoothness (confirmed non-load-bearing)**. No unconditional window sign is claimed. | **PROVED** at fixed policies | statement `threads/thread1_turn1_answer.md`; proof `proofs/T1_proof.md`; **proof-read** `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15, non-propagating) → **fix round CLOSED**, `threads/2026-08-21_T1_fix_recheck.md` (T1-F1 discharged by H18; items N1–N4 applied; boxed displays byte-identical) → **PASS-equivalent**; **re-derivation PASS 2026-08-21** `rederive/T1_rederivation.md` (all parts PROVED-AS-STATED except the "equivalently" quantifier, PROVED-WITH-CHANGES). **Traceable change**: the old row's unqualified "equivalently" is false pointwise; the quantifier **"on average along the tightening path"** is added on the re-deriver's S28(ii) and matches what the fix round adopted |
| C1 | **The dominance-and-contraction implication, region carried as a named hypothesis.** Under: AGE's along-the-path contraction $L_{\mathcal R}<1$ **in one fixed norm convention** (an induced operator norm with its dual pairings — the re-derivation's N1; a mismatched pairing silently voids the implication); $\mathcal R_r$ relatively open in *both* coordinates with $\kappa\notin\{0,1\}$ (N2); an interior single-branch equilibrium; twice continuous differentiability of $\Delta^{\mathrm{act}}$ in $(k,\kappa,r)$; a non-vanishing **equilibrium** liquidity derivative (the equilibrium sensitivity $\mathcal S^{GE}$, distinguished from §4.4's fixed-policy $\mathcal S$); strict dominance $g_r^{PE} > \mathcal B_r^{GE}$ on the region; and the **threshold margin $r_\tau$ only** (the window coordinate is an integer — nothing local is claimed there): the fixed-policy attenuation sign survives in equilibrium on the region, $\partial_r\mathcal S^{GE} \le -\eta_r < 0$. The sign-coherence hypothesis is confirmed unused in the boxed conclusion. | **PROVED** (dominance-and-contraction implication; region-as-hypothesis) — **plus NUMERICAL node evidence**: 18 of 80 grid nodes are **pointwise dominance-and-contraction nodes** (largest contiguous block $T{=}5$, $\tau$-pct $\{50,70,90\}$, $\kappa\in\{0.65,0.75,0.85\}$; $\eta_r$ min 0.0595, median 0.3467; $L_{\mathcal R}\in[0.264,0.501]$ everywhere), by the executed committed check independently re-run 2026-08-22 (ALL REPRODUCE). These nodes verify the two pointwise inequalities and supporting diagnostics only; they do **not** verify the full C1 antecedent or a named nonempty region. The D8 $\varepsilon$-ball + integral-control pattern is the template for any future promotion. | proof `proofs/C1_proof.md` (repairs applied 2026-08-21, 13/13); **proof-read PASS 2026-08-21** `threads/2026-08-21_C1_proofread_audit.md` (0 FAIL); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES: N1, N2 added; H8 unused; bonus $\mathcal B_r^{GE} = O((1-L_{\mathcal R})^{-3})$ — dominance-and-contraction nodes are cubically bounded away from $L_{\mathcal R}=1$) `rederive/C1_rederivation.md`; check `quality_reports/fixes/t2_c1_region_check.py/.json` + re-run verify note. T1's PE-$\Omega$ hypothesis is exactly what fails in GE, so C1's remainder term is the object it bounds |

The old aspiration line ("C1 PROVED on a named nonempty region, NUMERICAL off-region") is
**retired as structurally undeliverable as worded** (the C1 proof-read's ruling): the deliverables
are the three objects the C1 row now carries — the implication PROVED with the region as a
hypothesis, the dominance-and-contraction nodes NUMERICAL, and a named-region promotion an open question with
the D8 ε-ball pattern as its template.

## 7. LABELS

- **PROVED** — a complete proof, independently re-derived and proof-read.
- **NUMERICAL** — verified on a grid by an executed, committed check script with committed output.
- **ESTIMATED** — an empirical estimate with a standard error and a stated design.
- **CONJECTURE** — everything else, including anything whose proof is deferred.

Dominance-and-contraction node is **not** a fifth label: it is pointwise numerical evidence for
$L_{\mathcal R}<1$ and $\eta_r>0$, with supporting diagnostics, not verification of the full C1
antecedent. A named-region promotion is not claimed. **Labels are never weakened by editing.** Only
an executed check or an independent re-derivation may move a label — never prose. Every move is logged as
`ID | old→new | evidence path | who | date | commit`, in
**`research/model_v4/LABEL_LEDGER.md`** (created 2026-08-21 with the seven ticket-27 moves).

## 8. Standing rules

1. The theorist cannot see the repo. Every input arrives pasted in the message.
2. Cite only IDs that appear in this card. No draft_v2 lemma numbers, no `\ref`, no citation the
   card does not carry.
3. **NOTATION DELTA is mandatory** in every answer: list every symbol used that is not in §4.
4. **Do not renumber or re-key any card symbol.** In particular: $\kappa$ is noise-trading
   intensity, never "liquidity depth"; bare $\lambda$ is D7's appropriability coefficient
   $1 - q(1-\gamma)\psi$ and is not available; $\psi$ is D7 pivotality; upright $T$ is the window and
   $\mathcal T$ is the best-response map.
5. State what you did **NOT** claim, in every answer.
6. Answer template, exactly these headings: `CLAIM` · `HYPOTHESES` (numbered, each used) · `PROOF`
   (numbered steps, each citing a hypothesis or an earlier step) · `WHERE IT FAILS` (≥2 concrete
   cases) · `LABEL CLAIMED` + why · `NUMERICAL CHECK REQUEST` (formula, grid, predicted sign *and*
   magnitude) · `NOTATION DELTA` · `NOT CLAIMED`.
7. No "clearly", "it follows", "standard", "obviously" in a proof step. Such a line is bounced with
   "show the step".

## 9. What the card does not claim

A global window-margin attenuation sign; $\kappa$-invariance of $J$; equilibrium uniqueness; a
nonempty GE region as a theorem; endogenous filing before the deadline; noisy or partially revealing
flagged-round trading; continuous-time execution; welfare or optimal rule design; that draft_v2's
hump result survives; that the prior calibration ($\Omega \approx 0.037$) is economically
meaningful; any empirical value for $\omega_a$.

**A7 satisfiability is no longer on this list** — it was never listed here, and it is now **resolved**
(§5's A7 note, ticket 24). Three items are **added** at this regeneration:

1. **Whether the two-round pooled cell of §2 satisfies A($\tau$) — OPEN.** L3 proves the
   representation's entire remaining bite is the *support* condition, exhibits a one-round market
   that satisfies it and the frozen manuscript's own no-disclosure structure that does not, and
   declares the two-round case open with the weakest sufficient conditions named
   (`proofs/L3_proof.md` Part IV, Steps 16–18). **L3, L4 leg 3 and T1 Part B are all conditional on
   A($\tau$)**, so this is the largest single conditionality the ledger carries.
2. **Whether an equilibrium in which the blockholder chooses the fully separating plan exists on a
   given calibration — OPEN, and P1-adjacent.** A7′ menus are fully separating on the flagged set,
   so the burden did not disappear when ticket 24 resolved satisfiability; it **moved** to incentive
   compatibility, which P1 does not settle (`proofs/A7_attack_verdict.md`, sharpest new failure
   case; `proofs/P1_proof.md`; `rederive/P1_rederivation.md` NOT CLAIMED 3). Relatedly, P1 does not
   claim that an equilibrium satisfying A8 exists — only that A8 holding *at* an exhibited
   equilibrium puts both cells on path.
3. **O-1 is a disclosure-regime analogy, not a window-margin test.** This is a **known fact on file,
   not a claim the card makes**: O-1 compares the public buy flagged versus pooled at fixed policies
   in the static repo model. Its ratios $1.06397 / 1.18373 / 1.13631 / 0.37798$ at
   $\Omega = 0.037252 / 0.128950 / 0.285804 / 0.50$ are regime-comparison composition outcomes;
   they are not $W_TC_T$ and measure no window pair. The analogy is useful because it shows that a
   composition factor can exceed one, motivating T1's genuine window-margin iff. The genuine
   window-margin record is `t2_t1_check` block 4: $W_TC_T<1$ at every checked node at this
   calibration (with the $H=10$ corner caveat recorded in `HANDOFF_sign.md` §8.1). The O-1 cut
   $\Omega^\star \approx 0.343$ remains a disclosure-regime boundary, not a window boundary
   (`HANDOFF_sign.md` §3; `quality_reports/fixes/t1_o1_rerun_check.py`).
