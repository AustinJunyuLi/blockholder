# MODEL CARD — v4 two-round blockholder disclosure model

**Version stamp: 2026-08-20 · commit `0c9185b`.** An answer written against a stale stamp is
re-asked, not accepted. Regenerated from `threads/thread1_turn1_answer.md` after the turn-1 audit
(`threads/thread1_turn1_audit.md`), then revised after the turn-2 proof-read
(`threads/thread1_turn2_audit.md`). Vocabulary is `CONTEXT.md`.

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
| $m_0, m_1$ | takeover premia without / with engagement | $m_1 > m_0$ |
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
| $B_j(s,d)$ | cumulative pooled stake at day $d$; $B_j(s,-1) = b_0$ | $\in [0,\bar b]$; for Voice: $\partial_d B_j \ge 0$ and $\partial_s B_j \ge 0$; Hold constant, Exit weakly decreasing. **Continuum-valued** — A2's finiteness covers the plan menu, $\Gamma$'s image, the noise support and the calendar, *not* the stake level. On the flagged set, $s\mapsto(B_j^F,b_j^*)$ must be **strictly** increasing for Voice, or A7's injective form fails on any flat interval (turn-2 audit L2-R1) |
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
| $\mathcal I_H$ | control-node information set | — |
| $\mathcal C_F, \mathcal C_P$ | flagged / pooled cells | exclusive and exhaustive by construction |
| $\pi(\mathcal I) = \Pr(a=1\mid\mathcal I)$ | engagement posterior | $\in[0,1]$; $=1$ on $\mathcal C_F$ |
| $p(\mathcal I)$ | bidder-entry probability $1 - \Phi\big((P+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)$ | $\in(0,1)$ |
| $\mathsf B$, $Y$ | entry indicator; terminal shareholder payoff $ (1-\mathsf B)(v + a\Delta_V) + \mathsf B(P + m_0 + a\Delta_m)$ | — |
| $P_d^P$, $P^F$ | competitive pooled price; flagged price $P(F,Q^F)$ | $P(\mathcal I) = \mathbb E[Y\mid\mathcal I]$ (inner fixed point). **Convention $P_{-1}^P := \mathbb E[Y]$**, the pre-trading pooled price — needed whenever $c=0$, which $T=H$ forces on every flagged history (turn-2 audit D1-R3) |
| $P_{\mathrm{ND}}(\mathcal H_{f^-}^P)$ | counterfactual pooled price at the **same realised order flow**, no flag | $= P_{f^-}^P$ by construction |
| $R_d = P_d^P - P_{c^-}^P$, $R = P_{f^-}^P - P_{c^-}^P$ | run-up path, cumulative run-up | unsigned |
| $J = P^F - P_{\mathrm{ND}}$ | filing-day jump | unsigned; **not** claimed $\kappa$-invariant |
|  | identity: $P^F - P_{c^-}^P = R + J$ | exact |

### 4.4 Premium and comparative statics

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $h(\mathcal I) = \pi(\mathcal I)p(\mathcal I)$ | engagement-premium kernel | $h \ge 0$, $h(0) = 0$ |
| $\Delta^{\mathrm{act}} = \Delta_m\,\mathbb E[h(\mathcal I_H)]$ | expected engagement-related premium | $\ge 0$ |
| $M_F$, $M_P$ | $\Delta_m\mathbb E[h\mid D=1]$, $\Delta_m\mathbb E[h\mid D=0]$ | defined when the cell has mass |
| $\Omega = \Pr(D=1)$ | unconditional flagged weight; $\Omega = \Pr(a=1)\,\omega_a$ | $\in[0,1]$; **$\Omega$ is draft_v2's $\omega_P$ — the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the $\approx 0.29$ cut are all $\Omega$-type** |
| $\omega_a = \Pr(D=1\mid a=1)$ | disclosed share of engagements; the calibration target | $\in[0,1]$; **renamed from bare $\omega$** |
| $\bar\pi$ | pre-order pooled engagement share in the chord | $\in[0,1]$ |
| $\mathcal S = \lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$, $\mathcal S_P = \lvert\partial_\kappa M_P\rvert$ | liquidity-sensitivities | $\ge 0$; $\mathcal S = (1-\Omega)\mathcal S_P$ under L2 + fixed policies |
| $C_h(\bar\pi) = h(0) - 2h(\bar\pi/2) + h(\bar\pi)$ | the chord | **= draft_v2's $\mathcal C(\bar\pi)$, condition (C\*), `lem:d1-jensen`**; maintained $\le 0$, $\lvert C_h\rvert$ weakly increasing in $\bar\pi$ |
| $A'_\kappa$ | common derivative of the A(τ) weights ($A_0' = A_1' = A'_\kappa$, $A_{1/2}' = -2A'_\kappa$) | bounded on $[0,1]$; **renamed from $a_\kappa$; $a$ is engagement** |
| $W_\tau, W_T$ | weight-effect ratios, e.g. $W_T = (1-\Omega(\tau,5))/(1-\Omega(\tau,10))$ | $\le 1$ when $\Omega$ rises |
| $\eta_r$ | C1 slack (see §4.5) | $>0$ on certified nodes |
| $C_\tau, C_T$ | composition-effect ratios, e.g. $C_T = \mathcal S_P(\tau,5)/\mathcal S_P(\tau,10)$ | unsigned; kept (CONTEXT.md's "composition effect") — but $C$ is overloaded: $C_h$ chord, $C_j(s)$ engagement cost, $\mathcal C_F/\mathcal C_P$ cells. Always keep the margin subscript |

### 4.5 Equilibrium and GE certification

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
| $\mathcal R_r$, $\eta_r = g_r^{PE} - \mathcal B_r^{GE}$ | certified region; slack | $\eta_r > 0$ on certified nodes; region may be empty |

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
- **A2 Finite model.** Plan menu, order-mark support, noise support and calendar horizon finite;
  prices and payoffs bounded on the maintained parameter set.
- **A3 Ordered plans, single crossing.** At every belief/price system, adjacent-plan payoff
  differences cross zero at most once in $s$, and the preferred plan is weakly increasing in $s$.
- **A4 Legal-clock discipline.** $c$ is the first date the path reaches $\tau$; filing lands exactly
  at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in the core.
- **A5 Inner pricing regularity.** Each public-history pricing map has a unique fixed point,
  continuous in beliefs, cutoffs and parameters.
- **A6 Compact outer self-map.** All best-response cutoffs lie in a common compact ordered polytope
  $\Theta$; $\mathcal T$ is continuous and maps $\Theta$ into itself.
- **A7 Filing sufficiency.** On flagged histories $(B^F,Q^F,a=1)$ identifies the informed component
  of the selected plan; conditional on it, the pooled order-flow residual is pure noise, independent
  of $(v,s,\xi)$. Stronger convenient form: $(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ is injective on the
  flagged set.
  *Note (turn-2 proof-read).* **L2's proof uses the injective form and the weak wording is not
  sufficient** — it permits two $(j,s)$ pairs with different pooled paths, which is exactly L2's
  first failure case. Injectivity needs the strict-monotonicity row in §4.2 and forces $B^F$
  continuum-valued. Whether it is *satisfiable* on a plan menu is open and is Thread 2's target.
  Injective + measurable already gives the measurable inverse (standard Borel spaces); no separate
  assumption is needed.
- **A8 Interior crossing.** $0 < \Omega(\kappa,\tau,T) < 1$. Required only for positive cell mass,
  never for the structural partition.
- **A($\tau$) Threshold chord restriction.** The pooled posterior law has the symmetric ternary
  representation $\mathbb E[h] = A_0(\kappa)h(0) + A_{1/2}(\kappa)h(\bar\pi/2) + A_1(\kappa)h(\bar\pi)$
  with $A_0' = A_1' = A'_\kappa$ and $A_{1/2}' = -2A'_\kappa$; maintained orientation
  $C_h(\bar\pi)\le 0$ with $\lvert C_h\rvert$ weakly increasing in $\bar\pi$. (draft_v2's (C\*) is
  the strict version; the $C_h = 0$ case must be handled explicitly.)
- **AGE GE differentiability and contraction.** On a candidate region $\mathcal R$ the outer map is
  twice continuously differentiable, $L_{\mathcal R} < 1$, and the sign of the equilibrium liquidity
  derivative is constant on $\mathcal R$.

## 6. Result ledger

Label for all eight: **CONJECTURE**. D1, L1, L2 now have full proofs on file that passed the Opus
proof-read; the protocol still requires **independent re-derivation PASS *plus* proof-read PASS**
before PROVED, so they stay CONJECTURE until Thread 2 answers. P1 and L3–C1 remain statements only.

| ID | Statement | Label | Evidence |
|---|---|---|---|
| D1 | $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is **measurable** and maps every control-node history into exactly one cell; for every Voice plan $f_j\le H \iff B_j(s,H-T)\ge\tau$; and each flagged history yields $B^F, R_d, R, J$ with $P^F - P_{c^-}^P = R + J$. | CONJECTURE | statement `threads/thread1_turn1_answer.md`; **proof on file (`threads/thread1_turn2_answer.md`); Opus proof-read: PASS 2026-08-20** (3 non-blocking repairs: uncited public-flag bridge, $B^F$ continuum-valued not finite, $P_{-1}^P$ convention); **awaiting Thread 2 re-derivation** |
| P1 | Under A1–A7 a cutoff PBE over complete contingent plans exists; under A8 both cells are on path. | CONJECTURE | `threads/thread1_turn1_answer.md` |
| L1 | Whenever $0<\Omega<1$, $\Delta^{\mathrm{act}} = \Omega M_F + (1-\Omega)M_P$; at $\Omega=1$ it degenerates to $\Delta^{\mathrm{act}}=M_F$ and at $\Omega=0$ to $\Delta^{\mathrm{act}}=M_P$, the null-cell average being undefined rather than imputed. | CONJECTURE | statement `threads/thread1_turn1_answer.md`; **proof on file (`threads/thread1_turn2_answer.md`); Opus proof-read: PASS 2026-08-20** (clean; one cosmetic repair); **awaiting Thread 2 re-derivation** |
| L2 | At fixed cutoff and execution policies, under A1, A4, A5, **A7 in its injective form**, the no-feedback timing of §2, and **$\Omega>0$**: $(B^F,Q^F,a{=}1)$ makes the pre-filing pooled history conditionally independent of $(v,s,\xi)$ on the flagged set, so the flagged posterior, price, entry probability and $M_F$ are invariant to $\kappa$. | CONJECTURE | statement `threads/thread1_turn1_answer.md`; **proof on file (`threads/thread1_turn2_answer.md`); Opus proof-read: PASS 2026-08-20** (4 non-blocking repairs; largest open risk is whether injective A7 is satisfiable — audit L2-R1); **awaiting Thread 2 re-derivation** |
| L3 | Under A($\tau$) the pooled cell's interior $\kappa$-motion is proportional to $C_h(\bar\pi)$, and $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, so it vanishes as $\bar\pi\downarrow 0$. | CONJECTURE | `threads/thread1_turn1_answer.md` |
| L4 | At fixed policies a lower $\tau$ weakly raises $\Omega$, weakly lowers $\bar\pi$ in the pooled class, and — under L3 and monotone $\lvert C_h\rvert$ — weakly lowers $\mathcal S_P$. | CONJECTURE | `threads/thread1_turn1_answer.md` |
| T1 | At fixed policies threshold tightening attenuates $\mathcal S$; window tightening attenuates it **iff** its weight effect dominates its composition effect ($W_T C_T \le 1$, equivalently $\partial_{r_T}\mathcal S_P/\mathcal S_P \le \Omega_{r_T}/(1-\Omega)$). | CONJECTURE | `threads/thread1_turn1_answer.md` |
| C1 | On a named region where $L_{\mathcal R}<1$ and $g_r^{PE} > \mathcal B_r^{GE}$, the fixed-policy attenuation sign survives in equilibrium. | CONJECTURE | `threads/thread1_turn1_answer.md` |

Intended final labels (aspirations, not claims): D1, P1, L1, L2 PROVED; L3 PROVED under A($\tau$);
L4 PROVED under nested reclassification; T1 PROVED at fixed policies; C1 PROVED on a named nonempty
region, NUMERICAL off-region, dropped if the region is empty.

## 7. LABELS

- **PROVED** — a complete proof, independently re-derived and proof-read.
- **NUMERICAL** — verified on a grid by an executed, committed check script with committed output.
- **ESTIMATED** — an empirical estimate with a standard error and a stated design.
- **CONJECTURE** — everything else, including anything whose proof is deferred.

Region-certified is **not** a fifth label: it is PROVED with the region named in the hypothesis.
**Labels are never weakened by editing.** Only an executed check or an independent re-derivation may
move a label — never prose. Every move is logged as
`ID | old→new | evidence path | who | date | commit`.

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
nonempty GE-certified region; endogenous filing before the deadline; noisy or partially revealing
flagged-round trading; continuous-time execution; welfare or optimal rule design; that draft_v2's
hump result survives; that the prior calibration ($\Omega \approx 0.037$) is economically
meaningful; any empirical value for $\omega_a$.
