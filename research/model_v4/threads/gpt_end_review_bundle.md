# GPT Pro End Review Bundle — v4 two-round blockholder disclosure model

## 1. THE ASK

Adversarial end review of the v4 two-round blockholder disclosure model's complete theorem stack.

You are reviewing everything the theory lane has produced: a model card, a label ledger, eight
complete proofs, nine raw executed-check JSON files, and one independent re-run verdict. Nothing
else exists — you see no repository, no source code, no earlier chat history. Everything you need
to render a verdict is in this single paste, in the order it appears below.

**How to score each claim.** For every claim you examine, return exactly one of three verdicts:

- **WRONG** — a cited source in this bundle, or a check you can execute or re-derive from the
  numbers given, contradicts the claim.
- **MISCITED** — the claim itself stands, but the citation attached to it (a proof step, a check
  name, a file) is wrong, mismatched, or does not say what it is cited as saying.
- **UNCHECKED** — you could not check it with what is in this paste. Return the claim itself, not
  a count, and do not silently downgrade a decision-critical claim to low priority just because it
  is unchecked.

**Labels can only move down.** This bundle's LABEL LEDGER (§3) already records the moves earned
inside this lane, with the two passes that earned each one. Your review can DEMOTE a label — send
a PROVED row back to CONJECTURE if you find a hole — but it cannot PROMOTE anything. Only an
executed check plus an independent re-derivation earns PROVED or NUMERICAL, and those passes have
to run inside the lane, never from your prose alone.

**The card's own rules bind your answer, too.** MODEL CARD §4 (Symbol table) is the only notation
you may use — do not renumber or re-key a symbol, and flag any notation you introduce that is not
already in §4. MODEL CARD §8 (Standing rules) governs how you write your answer: no "clearly", "it
follows", "standard", or "obviously" without showing the step; cite only IDs that already appear in
this card.

**Three findings are already on record — attack them, don't just re-report them.** All three
reproduced bit-identical on an independent re-run (§6) and are recorded as findings, not bugs:

1. L2's A(τ)-orientation placebo — `t2_l2_check.json`; L2's proof is in
   `threads/thread1_turn2_answer.md`.
2. T1's chord-magnitude bridge — `t2_t1_check.json`; `proofs/T1_proof.md`.
3. P1's four κ-extreme nodes — `t2_p1_check.json`; `proofs/P1_proof.md`.

**C1's label is a deliberate three-way split — challenge whether the split itself is honest**, not
just the arithmetic behind it: the implication is labeled PROVED with the region named as a
hypothesis (its nonemptiness is not proved); the 18 grid nodes checked against that hypothesis are
labeled NUMERICAL, not PROVED; and the card explicitly does NOT claim region-level certification.
Is that split doing real epistemic work, or is it a way to borrow PROVED-adjacent language for
something that isn't proved?

**Answer in the card's own §8 template** — CLAIM · HYPOTHESES · PROOF · WHERE IT FAILS · LABEL
CLAIMED + why · NUMERICAL CHECK REQUEST · NOTATION DELTA · NOT CLAIMED — for every claim you rule
on. NOTATION DELTA and NOT CLAIMED are both mandatory, every time, even when the verdict is
UNCHECKED.

---

## 2. MODEL CARD

FILE: research/model_v4/MODEL_CARD.md (verbatim, complete)

# MODEL CARD — v4 two-round blockholder disclosure model

**Version stamp: 2026-08-21 · post-ledger regeneration · commit `627642c`.** An answer written against a stale stamp is
re-asked, not accepted. Regenerated from `threads/thread1_turn1_answer.md` after the turn-1 audit
(`threads/thread1_turn1_audit.md`), revised after the turn-2 proof-read
(`threads/thread1_turn2_audit.md`), surgically edited for ticket 24's A7 construction, and
regenerated here after **two-pass evidence closed on all seven results** (adversarial proof-read
PASS *plus* statements-only re-derivation PASS for D1, L1, L2, L3, L4, P1, T1). Every §4/§5 change
below is traceable to a named audit or re-derivation finding; the label moves are logged in
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
| $B_j(s,d)$ | cumulative pooled stake at day $d$; $B_j(s,-1) = b_0$ | $\in [0,\bar b]$; for Voice: $\partial_d B_j \ge 0$ and $\partial_s B_j \ge 0$; Hold constant, Exit weakly decreasing. **And, for every plan and every $d$, $s \mapsto B_j(s,d)$ is Borel** — automatic for Voice (monotone in $s$) and Hold (constant), but a **genuine addition for Exit**, where the card supplied monotonicity in $d$ only; without it the pooled prices in D1's part (c) are not defined, because pooled pricing integrates over every type including Exit types (`rederive/core_D1_L1_L2_rederivation.md` §A hypothesis H9 and consolidated finding 1 — the re-derivation makes D1's PROVED label conditional on this clause being on the card). **Continuum-valued** — A2′'s finiteness covers the plan menu, $\Gamma$'s image, the noise support and the calendar, *not* the stake level. On the flagged set the **composed terminal target** $s \mapsto b^*_{j(s)}(s)$ must be strictly increasing **for every cutoff vector $k \in \Theta$** (hypothesis A7′, `proofs/A7_construction.md`) — for a menu this amounts to each $b_j^*$ strictly increasing and no backtracking of $b^*_j$ across any admissible plan switch. Strictness of $B^F$ is neither necessary (it fails at crossing-date jumps on the pro-rata menu) nor sufficient (multi-Voice backtracking). Replaces the 2026-08-20 strict-pair patch (turn-2 audit L2-R1) per ticket 24 |
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
  of $(v,s,\xi)$. Stronger convenient form: $(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ is injective on the
  flagged set.
  *Note (turn-2 proof-read).* **L2's proof uses the injective form and the weak wording is not
  sufficient** — it permits two $(j,s)$ pairs with different pooled paths, which is exactly L2's
  first failure case. Injectivity needs the A7′ row in §4.2 and forces $B^F$
  continuum-valued. Injective + measurable already gives the measurable inverse (standard Borel
  spaces); no separate assumption is needed.
  *Note (ticket 24, 2026-08-21).* **Satisfiability is resolved.** A7′ + a fixed cutoff policy +
  $\Omega > 0$ deliver the **on-path** injective form (positive-probability flagged tuples) with an
  explicit inverse; a satisfying menu exists — the pro-rata single-Voice menu with terminal target
  strictly increasing on all of $\mathbb R$, which also satisfies the joint $(j,s)$ form
  (`proofs/A7_construction.md`; adversarial attack verdict SURVIVES WITH REPAIRS,
  `proofs/A7_attack_verdict.md`, repairs applied 2026-08-21). The joint form additionally needs
  $b^*$ strictly increasing off the Voice region — a target flat below the Voice cutoff breaks it
  (40-collision executed check) while leaving the on-path form intact. Failure boundary: a binding
  stake cap, quantized stakes, a composed target repeating values across Voice-plan switches,
  $\Omega = 0$, and policy-dependence when the condition is stated only at one equilibrium's
  cutoffs. A7′ menus are fully separating on the flagged set — the burden moves to P1's incentive
  compatibility, not away.
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

**All eight now carry two-pass evidence** (C1's moved 2026-08-22, after its own proof-read,
re-derivation, and the independent re-run of every check script — ALL REPRODUCE,
`quality_reports/fixes/t2_rerun_verify_note.md`). The protocol (§7) requires an
adversarial proof-read PASS **and** an independent statements-only re-derivation PASS, by different
agents, before a label moves. That gate is now satisfied for D1, L1, L2, L3, L4, P1 and T1. **C1 is
untouched and stays CONJECTURE** (ticket 29 in flight). Every statement below is the *amended*
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
| P1 | Under **A1, A2′, A3, A4, A6, A7′ (on-path injective), D1 by statement, the §2 no-feedback timing read with the flag-terminates-the-pooled-round clause, the definitional round-2 action-set hypothesis** (the flagged-round action set **is** the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements agreeing with $j$ on everything already played — *not* a closure condition; the closure form is jointly unsatisfiable with finiteness by cardinality), **$m_0\ge0$, and the §4.3 blockholder-objective definition $U_j$**: a cutoff PBE over complete contingent plans exists — $k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, prices at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs as limits of full-support perturbations over **plans**, the §4.3 entry rule, and a sequentially optimal flagged component. **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$ (see A5). **At any such equilibrium at which A8 holds**, both cells carry strictly positive probability and are on path; for A8's restatement as a single signal threshold add **H-ord** (Voice stake monotonicity across plans — the writer's h.13, **renamed here to avoid collision with the objective row**) and the upper-set engagement-flag hypothesis. Uniqueness is not claimed. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `proofs/P1_proof.md` (repairs applied 2026-08-21); **proof-read PASS 2026-08-21** `threads/2026-08-21_batch1_proofread_audit.md` §4 (0 FAIL; P1-R1…R8 applied; inner fixed point executed on 20k random draws — 0 multiplicity, 0 sign failures); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/P1_rederivation.md` (changes C1–C8). **Traceable changes from the old row's "Under A1–A7"**: that phrasing *overstated* — A2 had to become A2′ (C1), A5 is dropped as a hypothesis and derived (C3, three independent confirmations), and three hypotheses the card did not carry are now named (round-2 action set, $m_0\ge0$, the objective). A8 is honestly a condition **on the fixed point exhibited** (C6); existence of an equilibrium *at which* A8 holds is not claimed |
| T1 | At fixed plan and cutoff policies, with $0<\Omega<1$ and $\mathcal S_P>0$: **(A)** $\mathcal S = (1-\Omega)\mathcal S_P$ exactly, and the same factorisation holds for the total-variation aggregate of $\Delta^{\mathrm{act}}$ over any $\kappa$-grid with no differentiability required; **(B)** threshold tightening attenuates — $\mathcal S(\tau')/\mathcal S(\tau) = W_\tau C_\tau \le 1$ because **both** ratios lie in $[0,1]$, no dominance condition needed; **(C)** window tightening attenuates **iff** $W_T C_T \le 1$, where $W_T\le1$ is **proved** (from D1's clock equivalence and the monotone Voice stake path) and $C_T$ is **unsigned** — "equivalently $\partial_{r_T}\mathcal S_P/\mathcal S_P \le \Omega_{r_T}/(1-\Omega)$" holds **on average along the tightening path** (integrated over $[-T,-T']$), exactly in the infinitesimal limit, and is **false read pointwise**. Hypotheses: **fixed policies; A8 at each compared policy; $\mathcal S_P>0$; L1; L2 (its own hypotheses travelling); D1; PE-$\Omega$ ($\partial_\kappa\Omega=0$ at fixed policies — derivable, not assumed, and it fails in GE, which is C1's term); $\kappa$-differentiability of $M_P$ (no card hypothesis supplies this — carried in-proof); A($\tau$) at both compared policies with the $\bar\pi$ ruling; L3; A(br) (br-i)–(br-v) at the threshold pair; L4; the §2 no-feedback timing; a smooth window interpolation for the local form; threshold-side smoothness (confirmed non-load-bearing)**. No unconditional window sign is claimed. | **PROVED** at fixed policies | statement `threads/thread1_turn1_answer.md`; proof `proofs/T1_proof.md`; **proof-read** `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15, non-propagating) → **fix round CLOSED**, `threads/2026-08-21_T1_fix_recheck.md` (T1-F1 discharged by H18; items N1–N4 applied; boxed displays byte-identical) → **PASS-equivalent**; **re-derivation PASS 2026-08-21** `rederive/T1_rederivation.md` (all parts PROVED-AS-STATED except the "equivalently" quantifier, PROVED-WITH-CHANGES). **Traceable change**: the old row's unqualified "equivalently" is false pointwise; the quantifier **"on average along the tightening path"** is added on the re-deriver's S28(ii) and matches what the fix round adopted |
| C1 | **The certificate implication, region carried as a named hypothesis.** Under: AGE's along-the-path contraction $L_{\mathcal R}<1$ **in one fixed norm convention** (an induced operator norm with its dual pairings — the re-derivation's N1; a mismatched pairing silently voids certificates); $\mathcal R_r$ relatively open in *both* coordinates with $\kappa\notin\{0,1\}$ (N2); an interior single-branch equilibrium; twice continuous differentiability of $\Delta^{\mathrm{act}}$ in $(k,\kappa,r)$; a non-vanishing **equilibrium** liquidity derivative (the equilibrium sensitivity $\mathcal S^{GE}$, distinguished from §4.4's fixed-policy $\mathcal S$); strict dominance $g_r^{PE} > \mathcal B_r^{GE}$ on the region; and the **threshold margin $r_\tau$ only** (the window coordinate is an integer — nothing local is claimed there): the fixed-policy attenuation sign survives in equilibrium on the region, $\partial_r\mathcal S^{GE} \le -\eta_r < 0$. The sign-coherence hypothesis is confirmed unused in the boxed conclusion. | **PROVED** (certificate implication; region-as-hypothesis) — **plus NUMERICAL node evidence**: 18 of 80 grid nodes certify (largest contiguous block $T{=}5$, $\tau$-pct $\{50,70,90\}$, $\kappa\in\{0.65,0.75,0.85\}$; $\eta_r$ min 0.0595, median 0.3467; $L_{\mathcal R}\in[0.264,0.501]$ everywhere), by the executed committed check independently re-run 2026-08-22 (ALL REPRODUCE). **"PROVED on a named nonempty region" is NOT claimed** — it needs a modulus of continuity and a genuine supremum for $L_{\mathcal R}$, which no grid run supplies; the D8 $\varepsilon$-ball + integral-control pattern is the template for any future promotion. | proof `proofs/C1_proof.md` (repairs applied 2026-08-21, 13/13); **proof-read PASS 2026-08-21** `threads/2026-08-21_C1_proofread_audit.md` (0 FAIL); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES: N1, N2 added; H8 unused; bonus $\mathcal B_r^{GE} = O((1-L_{\mathcal R})^{-3})$ — certified nodes are cubically bounded away from $L_{\mathcal R}=1$) `rederive/C1_rederivation.md`; check `quality_reports/fixes/t2_c1_region_check.py/.json` + re-run verify note. T1's PE-$\Omega$ hypothesis is exactly what fails in GE, so C1's remainder term is the object it bounds |

The old aspiration line ("C1 PROVED on a named nonempty region, NUMERICAL off-region") is
**retired as structurally undeliverable as worded** (the C1 proof-read's ruling): the deliverables
are the three objects the C1 row now carries — the implication PROVED with the region as a
hypothesis, the certified nodes NUMERICAL, and region-level certification an open promotion with
the D8 ε-ball pattern as its template.

## 7. LABELS

- **PROVED** — a complete proof, independently re-derived and proof-read.
- **NUMERICAL** — verified on a grid by an executed, committed check script with committed output.
- **ESTIMATED** — an empirical estimate with a standard error and a stated design.
- **CONJECTURE** — everything else, including anything whose proof is deferred.

Region-certified is **not** a fifth label: it is PROVED with the region named in the hypothesis.
**Labels are never weakened by editing.** Only an executed check or an independent re-derivation may
move a label — never prose. Every move is logged as
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
nonempty GE-certified region; endogenous filing before the deadline; noisy or partially revealing
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
3. **The window-margin analogue of L4 leg 3 is REFUTED at the O-1 calibration.** This is a **known
   fact on file, not a claim the card makes**: since $W_T\le1$ is proved, the O-1 evaluations
   $W_TC_T = 1.06397 / 1.18373 / 1.13631$ at $\Omega = 0.037 / 0.129 / 0.286$ force $C_T \ge W_TC_T
   > 1$ — window tightening **raises** pooled sensitivity at those nodes, the opposite of leg 3's
   direction. At $\Omega = 0.50$ the criterion holds ($W_TC_T = 0.37798$), with the boundary at
   $\Omega^\star \approx 0.343$. Both branches occur inside the maintained parameter set, which is
   the sharpest possible content of "no unconditional window sign"
   (`rederive/T1_rederivation.md` S26; `HANDOFF_sign.md` §3; `quality_reports/fixes/t1_o1_rerun_check.py`).

---

## 3. LABEL LEDGER

FILE: research/model_v4/LABEL_LEDGER.md (verbatim, complete)

# LABEL LEDGER — v4 two-round blockholder disclosure model

The log of label moves required by `MODEL_CARD.md` §7. One line per move, in the format

`ID | old→new | evidence paths (proof; audit; re-derivation; fix/recheck if any) | who | date | commit`

**Rules this file obeys** (§7 of the card). Only an executed check or an independent re-derivation
moves a label — never prose. A move needs **both** passes: an adversarial proof-read PASS *and* an
independent statements-only re-derivation PASS, written by different agents, the re-deriver working
from the card statement alone with `proofs/` and `threads/` unopened. Labels are never weakened by
editing. Region-certified is not a label: it is PROVED with the region named in the hypothesis.

**Two standing notes.**

* **C1 is pending.** It has no proof on file and no pass of either kind; ticket 29 is in flight. It
  stays CONJECTURE and does not appear below.
* **GPT Pro's end review may demote, never promote.** A finding from that review can send any row
  below back to CONJECTURE. It cannot move anything *to* PROVED — that needs the two passes, run
  inside this lane, on file.

---

## Moves — ticket 27, theory-lane batch, 2026-08-21

D1 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §A (PASS as PROVED-WITH-CHANGES, 2026-08-21; its two added hypotheses are now card clauses — §4.2 Borel rider, §4.3 $\mathcal I_H$ fill) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L1 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §B (PASS as PROVED-AS-STATED, 2026-08-21) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L2 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §C (PASS as PROVED-WITH-CHANGES, 2026-08-21 — hypothesis set re-enumerated, A7′ consumed a.s. on the flagged set); satisfiability of A7 closed by `proofs/A7_construction.md` + `proofs/A7_attack_verdict.md` (ticket 24) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L3 | CONJECTURE→PROVED under A($\tau$) | proof `proofs/L3_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §2 (PASS, 0 FAIL, L3-R1…R5 applied 2026-08-21); re-derivation `rederive/L3_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; CH1–CH7 folded into card §4.4 and A($\tau$)) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L4 | CONJECTURE→PROVED (legs 1–2 outright; leg 3 under A(br)) | proof `proofs/L4_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §3 (PASS, 0 FAIL, L4-R1…R5 applied 2026-08-21); re-derivation `rederive/L4_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; (br-v) added, (br-iv) sharpened) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

P1 | CONJECTURE→PROVED | proof `proofs/P1_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §4 (PASS, 0 FAIL, P1-R1…R8 applied 2026-08-21); re-derivation `rederive/P1_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; changes C1–C8 — A2→A2′, A5 derived from $m_0\ge0$, objective row added) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

T1 | CONJECTURE→PROVED at fixed policies | proof `proofs/T1_proof.md`; audit `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15, non-propagating); fix/recheck `threads/2026-08-21_T1_fix_recheck.md` (T1-F1 discharged by H18; N1–N4 applied; fix round CLOSED → proof-read PASS-equivalent); re-derivation `rederive/T1_rederivation.md` (PASS, 2026-08-21; PROVED-AS-STATED except the "equivalently" quantifier, now written as *on average along the tightening path*) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

---

## Not moved

C1 | CONJECTURE (unchanged as of 2026-08-21) | no proof on file; ticket 29 in flight | — | 2026-08-21 | — **(superseded by the 2026-08-22 move below)**

## Move — ticket 29 close-out, 2026-08-22

C1 | CONJECTURE→PROVED (certificate implication, region-as-hypothesis; 18 certified nodes NUMERICAL evidence; region-level certification NOT claimed) | proof `proofs/C1_proof.md` (repairs 13/13); audit `threads/2026-08-21_C1_proofread_audit.md` (PASS, 0 FAIL); re-derivation `rederive/C1_rederivation.md` (PASS as PROVED-WITH-CHANGES: N1 norm convention, N2 two-sided openness; H8 unused); executed check `quality_reports/fixes/t2_c1_region_check.py/.json`, independently re-run 2026-08-22 ALL REPRODUCE (`quality_reports/fixes/t2_rerun_verify_note.md`) | theory-lane batch (Fable orchestrating) | 2026-08-22 | commit: 403ac8e

## Evidence note — independent re-run of every check script, 2026-08-22

All eight `t2_*` scripts (D1, L1, L2, L3, L4, T1, P1, C1-region) were re-run in full by a fresh
agent that wrote none of them: **ALL REPRODUCE** — every fresh JSON bit-identical to its committed
twin except wall-clock timing fields; zero numeric differences at any magnitude. One MISCITED
gloss corrected (the P1 failing-node description; the numbers were never wrong). Verdict:
`quality_reports/fixes/t2_rerun_verify_note.md`. The three substantive FAILs (L2's A(τ)-orientation
placebo, T1's chord-magnitude bridge, P1's four κ-extreme nodes) reproduce exactly and stand as
findings, not as errors.

---

## 4. PROOFS

### FILE: threads/thread1_turn2_answer.md (the D1/L1/L2 proofs)

D1 — Rule-keyed partition and timing-split representation
CLAIM
Under the model-card plan, calendar, legal-clock, and pricing definitions, (D_j(s;\tau,T)) is a measurable binary function of the realised complete history whose observed value assigns every control-node public history to exactly one of (\mathcal C_F) and (\mathcal C_P); for every Voice plan, (f_j(s;\tau,T)\le H) if and only if (B_j(s,H-T)\ge\tau); and every flagged history yields well-defined (B^F,R_d,R,J) satisfying (P^F-P_{c^-}^P=R+J).
HYPOTHESES

1. Finite plan and public-history structure. A2 holds; (T\in{1,\ldots,H}); (\Gamma) has finite image; and the model-card plan restrictions hold, including that (s\mapsto B_j(s,d)) and (d\mapsto B_j(s,d)) are weakly increasing for every Voice plan.
2. Legal-clock discipline. A4 holds: (c_j(s;\tau)) is the first date in ({0,\ldots,H}) at which (B_j(s,d)\ge\tau), with (c_j=+\infty) if the set is empty; (f_j=c_j+T), with (+\infty+T=+\infty); only Voice plans cross in the core; and the filing lands exactly at (f_j).
3. Well-defined prices. A5 holds, so every pooled or flagged public history used below has a unique competitive price.
4. Price-path definitions. On a flagged history, (P_{\mathrm{ND}}(\mathcal H_{f^-}^P)) is defined as the pooled price at the same realised order-flow history under no flag and therefore equals (P_{f^-}^P); (R_d=P_d^P-P_{c^-}^P), (R=P_{f^-}^P-P_{c^-}^P), and (J=P^F-P_{\mathrm{ND}}(\mathcal H_{f^-}^P)).

PROOF

1. Fix a Voice plan (j) and a date (d). Hypothesis 1 makes (s\mapsto B_j(s,d)) weakly increasing, so the set ({s:B_j(s,d)\ge\tau}) is an upper interval, possibly empty or all of the signal line, and is therefore Borel measurable. (Hypothesis 1.)
2. The event ({c_j(s;\tau)\le H-T}) equals the finite union
[
\bigcup_{d=0}^{H-T}{B_j(s,d)\ge\tau}.
]
Step 1 makes each member measurable, and Hypothesis 1 makes the union finite. (Hypotheses 1–2; Step 1.)
3. Because (f_j=c_j+T) and (T\le H), (f_j\le H) is equivalent to (c_j\le H-T), including the case (c_j=+\infty), for which both inequalities are false. (Hypothesis 2.)
4. Suppose (c_j\le H-T). The date set is finite, so the infimum in Hypothesis 2 is a minimum and (B_j(s,c_j)\ge\tau); weak increase in the calendar date gives
[
B_j(s,H-T)\ge B_j(s,c_j)\ge\tau.
]
(Hypotheses 1–2; Step 3.)
5. Suppose (B_j(s,H-T)\ge\tau). Then (H-T) belongs to the nonempty set whose first element defines (c_j), so (c_j\le H-T), and Step 3 gives (f_j\le H). (Hypothesis 2; Step 3.)
6. Steps 4–5 do not require a strict crossing: when (B_j(s,c_j)=\tau) and the path is flat at (\tau) through date (H-T), (c_j) remains the first hitting date and (B_j(s,H-T)=\tau), so both sides of the equivalence remain true. (Steps 4–5.)
7. By Hypothesis 2, non-Voice plans do not cross and have (D_j=0); for Voice plans, Steps 3–5 give
[
D_j(s;\tau,T)
\mathbf 1{a_j=1},
\mathbf 1{B_j(s,H-T)\ge\tau}.
]
Step 1 makes the second indicator measurable, while (a_j) is fixed by the finite plan index. Hence (D_j) is a well-defined measurable map from every realised history to ({0,1}). (Hypotheses 1–2; Steps 1 and 3–5.)
8. Hypothesis 1 makes every pre-filing pooled-history alphabet finite: each (q_{jd}(s)) lies in the finite image of (\Gamma), each (z_d) has three values, the flag coordinate has two values, and the calendar has finitely many dates. Steps 1–5 make (f_j) a measurable finite-valued function on the flagged set; hence (B_j^F=B_j(s,f_j)) and (Q_j^F=b_j^*(s)-B_j^F) are measurable there. A flagged control-node history augments one finite pooled history by the measurable tuple ((B^F,Q^F,a=1)), so the full control-node history space is a finite union of measurable pooled and flagged components and its observed flag coordinate is measurable. (Hypothesis 1; Steps 1–7.)
9. Define
[
\mathcal C_F
{\text{control-node histories}:D=1},
\qquad
\mathcal C_P
{\text{control-node histories}:D=0}.
]
A history cannot satisfy (D=1) and (D=0) simultaneously, so
[
\mathcal C_F\cap\mathcal C_P=\varnothing.
]
Every binary value is either zero or one, so
[
\mathcal C_F\cup\mathcal C_P
]
is the entire control-node history set. Measurability follows because both cells are preimages of singleton subsets of ({0,1}) under the measurable map in Step 7. (Steps 7–8.)
10. No probability restriction entered Steps 7–9. The partition therefore exists even when (\Pr(D=1)=0) or (\Pr(D=1)=1); A8 is needed only when both cells must have positive mass. (Step 9.)
11. On a flagged history, Step 7 and Hypothesis 2 give (c_j<\infty) and (f_j\le H). Thus (B_j^F=B_j(s,f_j)) is evaluated at a date in the model calendar, the pooled dates from (c_j) through (f_j^-) are finite, and Hypothesis 3 supplies the prices entering (R_d,R,J). (Hypotheses 2–3; Step 7.)
12. Add and subtract the same-order-flow counterfactual from Hypothesis 4:
[
\begin{aligned}
P^F-P_{c^-}^P
&=
\bigl[
P^F-P_{\mathrm{ND}}(\mathcal H_{f^-}^P)
\bigr]

* 

\bigl[
P_{\mathrm{ND}}(\mathcal H_{f^-}^P)-P_{c^-}^P
\bigr]
\
&=
J+\bigl[P_{f^-}^P-P_{c^-}^P\bigr]
\
&=
J+R.
\end{aligned}
]
(Hypothesis 4; Step 11.)

13. The measurable binary map, cell exclusivity and exhaustion, and legal-clock equivalence in Steps 1–10 carry representational content. The existence of the named price-path objects in Step 11 uses the model’s timing and unique pricing. The equality in Step 12 is definitional bookkeeping—an exact accounting identity produced by the same-order-flow definition of (P_{\mathrm{ND}}), not an economic sign theorem. (Steps 1–12.)

WHERE IT FAILS

1. If a Voice stake path may fall after first reaching (\tau), then (c_j\le H-T) need not imply (B_j(s,H-T)\ge\tau); for example, the path can hit (\tau) at date zero and fall below it before (H-T).
2. If filing occurs at a discretionary date unrelated to (c_j+T), then (f_j\le H\iff c_j\le H-T) is unavailable, so the window cannot be represented by (B_j(s,H-T)\ge\tau).
3. If (P_{\mathrm{ND}}) is evaluated at a different order-flow history rather than the same realised one, then the second bracket in Step 12 is not (R) and the stated timing split does not hold.
4. If A5 fails and a public history supports multiple selected prices, the cells still partition histories, but (R_d,R,J) are not single-valued without an additional price-selection rule.

LABEL CLAIMED
PROVED — CONJECTURE (\rightarrow) PROVED. Steps 1–13 independently derive the measurable partition, the Voice-path clock equivalence including a flat-at-(\tau) path, and the exact timing split. The label does not rely on a numerical run; the pending script is a separate implementation check. The structural partition does not require A8.
NUMERICAL CHECK REQUEST
Run one history-enumeration script over
[
\kappa\in{0.15,0.35,0.55,0.75,0.85},
\qquad
T\in{5,10},
]
and thresholds equal to the 10th, 30th, 50th, 70th, and 90th percentiles of the equilibrium Voice stake paths. For every grid node, compute
[
\max_{j,s:a_j=1}
\left|
\mathbf 1{f_j(s;\tau,T)\le H}
\mathbf 1{B_j(s,H-T)\ge\tau}
\right|,
]
the number of histories with (D\notin{0,1}), the overlap mass
[
\Pr(\mathcal C_F\cap\mathcal C_P),
]
the exhaustion residual
[
\left|
\Pr(\mathcal C_F)+\Pr(\mathcal C_P)-1
\right|,
]
and
[
\max_{D=1}
\left|
P^F-P_{c^-}^P-R-J
\right|.
]
The predicted signed discrepancies are all zero. The required numerical magnitudes are zero binary/equivalence violations and residuals below (10^{-12}). Under the interiority calibration, the predicted minimum mass of each cell is at least the chosen grid floor (0.01); outside that calibration, only the zero partition and timing-split residuals are predicted.
NOTATION DELTA
None.
NOT CLAIMED
Positive mass in both cells without A8; a sign for (R), (J), or any (R_d); (\kappa)-invariance of (J); endogenous filing before the deadline; or a causal interpretation of the accounting timing split.
L1 — Premium cell decomposition
CLAIM
For every integrable engagement-premium kernel, (0<\Omega<1) implies
[
\Delta^{\mathrm{act}}
\Omega M_F+(1-\Omega)M_P;
]
at (\Omega=1) the identity degenerates to (\Delta^{\mathrm{act}}=M_F), and at (\Omega=0) it degenerates to (\Delta^{\mathrm{act}}=M_P).
HYPOTHESES

1. Binary measurable partition. D1 holds, so (D\in{0,1}) is measurable and ({D=1},{D=0}) are disjoint and exhaustive.
2. Integrability. (\Delta_m h(\mathcal I_H)) is measurable and integrable:
[
\mathbb E!\left[
\left|
\Delta_m h(\mathcal I_H)
\right|
\right]<\infty.
]
In the model card this condition is automatic because (0\le\pi\le1), (0<p<1), (h=\pi p\in[0,1]), and (\Delta_m) is finite.

PROOF

1. Because (D) is binary,
[
\mathbf 1{D=1}
+
\mathbf 1{D=0}
1
]
on every history. (Hypothesis 1.)
2. Multiply Step 1 by the integrable variable (\Delta_m h(\mathcal I_H)) and take expectations:
[
\Delta^{\mathrm{act}}
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=1}
\right]
+
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=0}
\right].
]
Both expectations are finite. (Hypothesis 2; Step 1.)
3. If (0<\Omega<1), the defining property of conditioning on an event with positive probability gives
[
\begin{aligned}
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=1}
\right]
&=
\Pr(D=1),
\Delta_m
\mathbb E[h(\mathcal I_H)\mid D=1]
\
&=
\Omega M_F,
\end{aligned}
]
and
[
\mathbb E!\left[
\Delta_m h(\mathcal I_H)\mathbf 1{D=0}
\right]
(1-\Omega)M_P.
]
(Hypotheses 1–2; Step 2.)
4. Substituting the two equalities from Step 3 into Step 2 yields
[
\Delta^{\mathrm{act}}
\Omega M_F+(1-\Omega)M_P.
]
(Steps 2–3.)
5. If (\Omega=1), then (D=1) almost surely, the second expectation in Step 2 is zero, and the positive-mass conditional average (M_F) satisfies
[
\Delta^{\mathrm{act}}=M_F.
]
The ordinary conditional average (M_P) is not defined because (\Pr(D=0)=0). (Hypotheses 1–2; Step 2.)
6. If (\Omega=0), then (D=0) almost surely, the first expectation in Step 2 is zero, and the positive-mass conditional average (M_P) satisfies
[
\Delta^{\mathrm{act}}=M_P.
]
The ordinary conditional average (M_F) is not defined because (\Pr(D=1)=0). (Hypotheses 1–2; Step 2.)
7. At either boundary, no convention is needed for the degenerate identity in Steps 5–6. If the equilibrium’s full-support perturbations assign a finite off-path cell average, that value may be inserted into the zero-weight term, but it is a convention rather than an identified conditional expectation. (Steps 5–6.)

WHERE IT FAILS

1. If the purported cells overlap or omit histories, Step 1 is false and the two-term decomposition double-counts or loses probability mass.
2. If (\Delta_m h(\mathcal I_H)) is not integrable, the expectations in Step 2 need not be finite and the decomposition may be undefined as an equality of real numbers.
3. At (\Omega\in{0,1}), treating the null-cell average as uniquely identified is invalid; only the positive-mass degenerate identity is intrinsic.

LABEL CLAIMED
PROVED — CONJECTURE (\rightarrow) PROVED. Steps 1–7 give a complete independent derivation, including the two boundary cases and the status of null-cell conditional averages. The result is an accounting identity, not a comparative-static theorem.
NUMERICAL CHECK REQUEST
Using the D1 grid
[
\kappa\in{0.15,0.35,0.55,0.75,0.85},
\qquad
T\in{5,10},
]
with (\tau) at the 10th, 30th, 50th, 70th, and 90th percentiles of equilibrium Voice stake paths, compute (\Delta^{\mathrm{act}}) once by direct summation over all histories and once as
[
\Omega M_F+(1-\Omega)M_P
]
at every interior node.
Also run one all-pooled policy with (\Omega=0) and one all-flagged policy with (\Omega=1) and verify the degenerate identities, recording the zero-mass cell average as undefined rather than imputing it.
The predicted signed residual is zero in every case; the required absolute residual is below (10^{-12}). Report (\Delta^{\mathrm{act}},M_F,M_P) in premium percentage points, not normalized indices.
NOTATION DELTA
None.
NOT CLAIMED
A sign for (M_F-M_P); positive mass in both cells without A8; a causal interpretation of the cell decomposition; or a uniquely identified conditional average for a zero-mass cell.
L2 — Flagged-cell direct liquidity-invariance
CLAIM
At fixed cutoff and execution policies, under A1, A4, A5, A7 in its injective-recoverability form, and (\Omega>0), ((B^F,Q^F,a=1)) makes the pre-filing pooled history conditionally independent of ((v,s,\xi)) on the flagged set, so the flagged posterior, unique price (P^F), bidder-entry probability, and (M_F) are constant in noise-trading intensity (\kappa).
HYPOTHESES

1. Independent primitives. A1 holds: the full noise vector is independent of ((v,\varepsilon,\xi)), and hence of ((v,s,\xi)) because (s=v+\varepsilon).
2. Finite histories. A2 holds, so the calendar and pooled public-history support are finite and every pre-filing history is a measurable function of finitely many order-flow observations.
3. Truthful flagged purpose. A4 holds, so (D=1) implies (a=1), the filing truthfully reports (F=(B^F,a=1)), and (f) is determined by the selected plan and signal.
4. Unique flagged price. A5 holds, so the flagged competitive-pricing map has one fixed point at every on-path flagged information set.
5. Injective filing sufficiency. A7 is used in its recoverability form: on the flagged set the measurable map
[
(j,s)
\mapsto
\bigl(
B_j(s,f_j(s;\tau,T)),
Q_j^F(s;\tau,T),
a_j
\bigr)
]
is injective and the plan-and-signal pair ((j,s)) is measurable with respect to the observed tuple; equivalently, the map has a measurable inverse on its image.
6. Fixed-policy direct comparison. As (\kappa) varies, the cutoff mapping from (s) to (j), every (B_j(s,d)), every (Q_j^F(s;\tau,T)), (\tau), (T), and all non-noise primitives are held fixed; the flagged-round order is observed without an additional (\kappa)-dependent noise term; (\kappa) parameterizes only the law of the pooled (z_d) draws.
7. Positive flagged mass. (\Omega=\Pr(D=1)>0), so conditioning on the flagged cell and the cell average (M_F) are defined under the ordinary equilibrium probability law.

PROOF

1. On the flagged set define
[
\mathsf S_F:=(B^F,Q^F,a=1)
]
and write
[
\mathcal H^P:=\mathcal H_{f^-}^P.
]
Hypothesis 5 supplies a measurable inverse (\iota_F) on the image of (\mathsf S_F), so
[
(j,s)=\iota_F(\mathsf S_F)
]
on every flagged history. Thus (\mathsf S_F) identifies the plan and signal, not merely the broad action class. (Hypothesis 5.)
2. Conditional on a fixed pair ((j,s)), Hypotheses 2–3 and 6 determine (f), each informed order mark (q_{jd}(s)), and every pre-filing flag coordinate. Since
[
X_d=q_{jd}(s)+z_d,
]
there is a deterministic measurable map (G_{j,s}) such that
[
\mathcal H^P
G_{j,s}(z_0,\ldots,z_{f-1}).
]
(Hypotheses 2–3 and 6.)
3. Let
[
W:=(v,s,\xi),
\qquad
\mathbf z^H:=(z_0,\ldots,z_H).
]
Hypothesis 1 makes (\mathbf z^H) independent of (W). Under Hypothesis 6, the selected (j), the event (D=1), and (\mathsf S_F) are functions of (W) and fixed policy objects, not of (\mathbf z^H). Therefore, at each fixed (\kappa) and for every measurable set of noise vectors, almost surely on (D=1),
[
\begin{aligned}
&\mathbb E!\left[
\mathbf 1{\mathbf z^H\text{ is in that set}}
\mid W,\mathsf S_F,D=1
\right]
\
&\qquad=
\Pr(\mathbf z^H\text{ is in that set})
\
&\qquad=
\mathbb E!\left[
\mathbf 1{\mathbf z^H\text{ is in that set}}
\mid\mathsf S_F,D=1
\right].
\end{aligned}
]
The middle probability may vary with (\kappa); the equality shows that pooled noise remains independent of (W) after conditioning on the flagged event and tuple. (Hypotheses 1 and 6; Step 1.)
4. Let (u_1) and (u_2) be bounded measurable test functions. Using Steps 1–3 and iterated conditioning,
[
\begin{aligned}
&\mathbb E[
u_1(W)u_2(\mathcal H^P)
\mid\mathsf S_F,D=1
]
\
&=
\mathbb E!\left[
u_1(W)
\mathbb E!\left[
u_2!\left(
G_{\iota_F(\mathsf S_F)}(\mathbf z^H)
\right)
\mid W,\mathsf S_F,D=1
\right]
\middle|
\mathsf S_F,D=1
\right]
\
&=
\mathbb E!\left[
u_1(W)
\mathbb E[
u_2(\mathcal H^P)
\mid\mathsf S_F,D=1
]
\middle|
\mathsf S_F,D=1
\right]
\
&=
\mathbb E[
u_1(W)\mid\mathsf S_F,D=1
]
,
\mathbb E[
u_2(\mathcal H^P)\mid\mathsf S_F,D=1
].
\end{aligned}
]
The second equality uses the independence in Step 3; the final equality uses that the second conditional expectation is measurable with respect to (\mathsf S_F). This factorization proves the required conditional-independence statement
[
(v,s,\xi)
\ \perp!!!\perp
\mathcal H^P
\ \big|
(B^F,Q^F,a=1)
\qquad
\text{under the conditional law given }D=1.
]
(Steps 1–3.)
5. The conditional independence in Step 4 implies, for every measurable event concerning ((v,s,\xi)),
[
\Pr!\left(
(v,s,\xi)\in\cdot
\mid
\mathsf S_F,\mathcal H^P,D=1
\right)
\Pr!\left(
(v,s,\xi)\in\cdot
\mid
\mathsf S_F,D=1
\right).
]
The pooled history therefore supplies no posterior refinement once (\mathsf S_F) is observed. (Step 4.)
6. Hypothesis 6 makes (\mathsf S_F) and (D) functions of the fixed policy and ((j,s)), while Hypotheses 1 and 6 place (\kappa) only in the law of (\mathbf z^H). The joint law of
[
(W,\mathsf S_F,D)
]
is therefore the same for every (\kappa), so the right-hand conditional law in Step 5 can be chosen identically across (\kappa), up to conditional null sets. The distribution of (\mathcal H^P) conditional on (\mathsf S_F) generally does vary with (\kappa), but Step 5 removes that distribution from the flagged posterior. (Hypotheses 1 and 6; Steps 1 and 5.)
7. Step 5 gives the full flagged posterior of ((v,s,\xi)), including
[
\mathbb E[
v\mid
\mathsf S_F,\mathcal H^P,D=1
],
]
as a function of (\mathsf S_F) alone; Step 6 makes that posterior independent of (\kappa). Hypothesis 3 also makes (a=1) part of the truthful flagged information, so
[
\pi(\mathsf S_F,\mathcal H^P)
\Pr(
a=1
\mid
\mathsf S_F,\mathcal H^P,D=1
)
   1. 
]
(Hypothesis 3; Steps 5–6.)
8. At a fixed flagged tuple, the competitive price solves
[
P
\mathbb E!\left[
(1-\mathsf B)(v+\Delta_V)
+
\mathsf B(P+m_1)
\mid
\mathsf S_F,\mathcal H^P,D=1
\right],
]
where, because Step 7 gives (\pi=1),
[
\mathsf B
\mathbf 1
{
\bar S+\xi-K-P-m_1\ge0
}.
]
Steps 5–7 make the conditional law entering the right-hand side independent of (\mathcal H^P) and (\kappa); Hypothesis 6 excludes a second (\kappa)-dependent noise source in (Q^F). Thus the flagged pricing map is the same for every (\kappa). (Hypothesis 6; Steps 5–7.)
9. Hypothesis 4 gives that the (\kappa)-independent pricing map in Step 8 has one fixed point, so its selected solution
[
P^F=P(F,Q^F)
]
is constant in (\kappa). Without uniqueness, an extraneous fixed-point selection could vary with (\kappa) even when the map itself does not. (Hypothesis 4; Step 8.)
10. Substituting Step 7 and the (\kappa)-invariant price from Step 9 into the bidder rule gives the flagged entry probability
[
p
1-\Phi!\left(
\frac{
P^F+K+m_1-\bar S
}{
\sigma_\xi
}
\right),
]
which is constant in (\kappa). (Steps 7 and 9.)
11. Under Hypotheses 1 and 6, the joint law of ((\mathsf S_F,D)) is independent of (\kappa), because both are functions of the (\kappa)-invariant signal/plan policy rather than of (z_d). Hypothesis 7 makes the flagged conditional law well defined; Step 7 gives (h=\pi p=p) on (D=1); and Step 10 makes that integrand (\kappa)-invariant. Hence
[
M_F
\Delta_m,
\mathbb E[p\mid D=1]
]
is constant in (\kappa). (Hypotheses 1, 6–7; Steps 7 and 10.)
12. The only direct entry point for (\kappa) is the probability law of the pooled noise draws in Hypothesis 6. Step 4 removes the resulting pooled-history variation from the flagged posterior; Steps 8–11 then remove it from price, entry, and (M_F). If equilibrium cutoffs or execution paths move with (\kappa), Hypothesis 6 no longer applies and those policy and composition responses are GE channels outside this result. (Hypothesis 6; Steps 4 and 8–11.)

WHERE IT FAILS

1. If two distinct pairs ((j,s)) produce the same ((B^F,Q^F,a=1)) but different pooled informed-order paths, then (\mathcal H^P) can distinguish those pairs; its likelihood depends on the (z_d) law and the flagged posterior can depend on (\kappa).
2. If the flagged-round order is mixed with an unobserved noise order whose distribution is indexed by (\kappa), then the flagged information itself retains a direct (\kappa) channel.
3. If A5 permits multiple flagged price fixed points and the selection rule varies with (\kappa), the posterior can be invariant while the selected (P^F) is not.
4. If cutoffs, plan choice, stake paths, or (Q^F) respond to (\kappa), then the theorem’s fixed-policy hypothesis fails; (M_F) can move through flagged-cell composition even when each fixed-tuple posterior remains directly invariant.
5. If purpose is not truthful or passive plans can be flagged without being distinguished, then (\pi) need not equal one on (\mathcal C_F).
6. If (\Omega=0) and no full-support limiting belief is specified, the flagged conditional law and (M_F) are not identified by the equilibrium probability law.

LABEL CLAIMED
PROVED under A7’s injective-recoverability form — CONJECTURE (\rightarrow) PROVED. Step 4 proves the required conditional-independence statement rather than assuming it; Steps 5–11 transmit that result through the posterior, unique pricing fixed point, bidder rule, and flagged-cell average. The weaker verbal phrase “identifies the informed component” is not sufficient if it permits multiple ((j,s)) pairs with different pooled paths; the proof uses the card’s injective A7 in its measurable-recoverability meaning. The ordinary conditional-independence and (M_F) statements require (\Omega>0); a zero-mass flagged cell would need a separately specified off-path limiting belief. No numerical output is used for this label.
NUMERICAL CHECK REQUEST
Freeze one equilibrium cutoff and execution policy at each
[
T\in{5,10}
]
and at thresholds equal to the 10th, 30th, 50th, 70th, and 90th percentiles of equilibrium Voice stake paths. Vary
[
\kappa\in{0.05,0.10,\ldots,0.95}.
]
For every on-path flagged tuple and for (M_F), compute
[
\operatorname{range}_{\kappa}\mathsf Z
\max_{\kappa}\mathsf Z
\min_{\kappa}\mathsf Z
]
for each flagged engagement posterior, each conditional-value posterior used by pricing, (P^F), bidder-entry probability (p), and (M_F), and compute central finite-difference derivatives in (\kappa).
The predicted sign is zero and the predicted economic magnitude is exactly zero for every object. Numerical acceptance requires every range below (10^{-10}) and every finite-difference derivative below (10^{-8}) in absolute value.
NOTATION DELTA
(\mathsf S_F=(B^F,Q^F,a=1)) is the full observed flagged tuple; (\mathcal H^P=\mathcal H_{f^-}^P) is shorthand for the pre-filing pooled history on a flagged path; (W=(v,s,\xi)); (\mathbf z^H=(z_0,\ldots,z_H)); (\iota_F) is the measurable inverse supplied by injective A7; (G_{j,s}) is the deterministic map from pooled noise draws to the pre-filing public history; (u_1,u_2) are bounded measurable test functions used only to establish conditional independence; and (\mathsf Z) is a generic scalar object in the numerical range check.
NOT CLAIMED
GE invariance when cutoffs or execution policies move with (\kappa); (\kappa)-invariance of the filing-day jump (J); invariance under noisy or partially revealing flagged-round trading; any off-path flagged posterior or cell average when (\Omega=0) without a specified limiting belief; or equilibrium uniqueness beyond the unique inner price imposed by A5.

### FILE: proofs/A7_construction.md

# A7 satisfiability — the on-path construction (ticket 24, T2d)

Author: Fable (session model), 2026-08-21, per the ADR-0008 grant (the hardest theory
bits go to Fable). Written against `MODEL_CARD.md` stamp 2026-08-20 · `0c9185b`
(ledger unchanged at HEAD `42ef47a`). Spec: `threads/thread1_msg3.md` §1 (the
L2-R1 block) and ticket 24. Status: **attack complete — SURVIVES WITH REPAIRS**
(`proofs/A7_attack_verdict.md`, 2026-08-21: nothing mathematically refuted;
witness table reproduced in exact rational arithmetic; two wording-level
contradictions and nine repairs R1–R9). **All repairs applied in this revision
(2026-08-21)**; the card's A7 note and §4.2 patch row are updated per the
repaired CLAIM (iv). Not a ledger row; no label moves here.

## CLAIM

Four parts.

**(i) Tuple equivalence.** On the flagged set, the flagged tuple
$\mathsf S_F = (B^F, Q^F, a{=}1)$ (the filing message $F$ augmented by the flagged
order $Q^F$) is informationally equivalent to $(B^F,\, b_j^*(s),\, a{=}1)$: the map
between them is a linear bijection, and in particular the sum $B^F + Q^F$ reveals
the terminal target $b_j^*(s)$ exactly.

**(ii) On-path sufficiency of composed-target strictness (A7′).** Fix a cutoff
policy $s \mapsto j(s)$ (L2's fixed-policy setting), assume $\Omega =
\Pr(D=1) > 0$ (A8; hypothesis 7 below), and let
$S_{\mathrm{fl}} := \{s : D_{j(s)}(s;\tau,T) = 1\}$ be the flagged signal region.
Define the **composed terminal target** $b^{\circ}(s) := b^*_{j(s)}(s)$ on
$S_{\mathrm{fl}}$.

> **A7′ (composed terminal-target separation).** $b^{\circ}$ is strictly
> increasing on $S_{\mathrm{fl}}$.

Under A7′ the on-path flagged-tuple map $s \mapsto \mathsf S_F(s)$ is injective on
$S_{\mathrm{fl}}$, with the explicit inverse $s = (b^{\circ})^{-1}(B^F + Q^F)$ and
$j = j(s)$; the inverse is Borel (monotone), and continuous when $b^{\circ}$ is
continuous. Both clauses of A7 then hold in the form L2 consumes: the tuple
identifies the informed component, and conditional on it the pooled order-flow
residual is exactly the noise sequence, independent of $(v,s,\xi)$.

**(iii) Satisfiability.** The **pro-rata three-plan menu** below (Exit / Hold /
one Voice family whose terminal target is continuous and strictly increasing
**on all of $\mathbb R$** — attack repair R5) satisfies A7′ for every
$(\tau, T)$ with $b_0 < \tau$ and every cutoff policy, and is conformant with
every card §4.2 row **except the strict-pair patch sentence itself, which
CLAIM (iv) shows must be replaced** (the menu violates it while delivering
injectivity). With the globally strict target, the menu satisfies not only the
on-path form but the card's **joint** $(j,s)$ form on the flagged set
$\{(j,s) : D_j(s;\tau,T) = 1\}$: only the Voice plan ever flags, and $b^*$
separates every signal (Step 7). Hence injective A7 is **satisfiable**. What
this closes is the *existence of a qualifying menu* (turn-2 audit L2-R1, msg3
§1); the residual open risk is **relocated to P1**, not eliminated — an
A7′-satisfying menu is fully separating on the flagged set, and whether an
equilibrium in which the blockholder chooses such a revealing plan exists is
P1's burden (WHERE IT FAILS case 8).

**(iv) The card's §4.2 patch must be replaced — it and A7′ are non-nested, and
the patch is neither necessary nor sufficient.** Not necessary: the pro-rata
menu **violates** the patch — $B^F$ is generically non-monotone in $s$, with a
downward jump at every crossing-date boundary (numeric witness in Step 9) —
while delivering injectivity through the sum coordinate. Not sufficient: with
two or more Voice plans each satisfying the patch within-plan, a backtracking
composed target across a plan switch breaks A7′ and injectivity with it (WHERE
IT FAILS case 3). On a **single**-Voice menu the patch's $b_j^*$-coordinate
strictness does imply A7′; the implication fails in general. A7′ is the
condition L2 actually consumes. Proposed card edits (quantified over policies —
attack repair R6):

- §4.2 `B_j(s,d)` row, replace the strict-monotonicity sentence with: "On the
  flagged set the **composed terminal target** $s \mapsto b^*_{j(s)}(s)$ must
  be strictly increasing **for every cutoff vector $k \in \Theta$** (hypothesis
  A7′, `proofs/A7_construction.md`) — for a menu this amounts to each $b_j^*$
  strictly increasing and no backtracking of $b^*_j$ across any admissible
  plan switch. Strictness of $B^F$ is neither necessary (it fails at
  crossing-date jumps on the pro-rata menu) nor sufficient (multi-Voice
  backtracking)."
- §5 A7 note, append: "A7′ + a fixed cutoff policy + $\Omega > 0$ deliver the
  **on-path** injective form (positive-probability flagged tuples) with an
  explicit inverse; a satisfying menu exists — the pro-rata single-Voice menu
  with terminal target strictly increasing on all of $\mathbb R$, which also
  satisfies the joint $(j,s)$ form (`proofs/A7_construction.md`; attack
  verdict SURVIVES WITH REPAIRS, repairs applied 2026-08-21). The joint form
  additionally needs $b^*$ strictly increasing off the Voice region; a target
  flat below the Voice cutoff breaks it (40-collision executed check in the
  attack verdict) while leaving the on-path form intact. Failure boundary: a
  binding stake cap, quantized stakes, a composed target repeating values
  across Voice-plan switches, $\Omega = 0$, and policy-dependence when the
  condition is stated only at one equilibrium's cutoffs. A7′ menus are fully
  separating on the flagged set — the burden moves to P1's incentive
  compatibility, not away."

## HYPOTHESES

1. Card §4.2 definitions: $B_j(s,d)$ with $B_j(s,-1) = b_0$, weak monotonicity
   for Voice ($\partial_d B_j \ge 0$, $\partial_s B_j \ge 0$), Hold constant,
   Exit weakly decreasing; $b_j^*(s) = B_j(s,H)$; $c_j(s;\tau) = \inf\{d :
   B_j(s,d) \ge \tau\}$; $f_j = c_j + T$; $B_j^F = B_j(s, f_j)$;
   $Q_j^F = b_j^*(s) - B_j^F$; $D_j = \mathbf 1\{a_j = 1,\ c_j < \infty,\ f_j \le H\}$.
2. Card §2 timing bullet 2 (no within-window re-optimisation): $B_j(s,d)$,
   $q_{jd}(s)$, $Q_j^F$ are functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone —
   never of realised order flow or prices.
3. A1: $v, \varepsilon, \xi$ and all $z_d$ mutually independent.
4. A4: filings truthful; only Voice plans cross in the core; the maintained
   $b_0 < \tau$ (card §4.1, turn-2 audit D1-O1).
5. Fixed cutoff policy: $s \mapsto j(s)$ is a fixed Borel (cutoff) map — L2's
   hypothesis 6 setting. On path, market makers know the policy functions
   (Bayes consistency, card §3(iii)).
6. D1's clock equivalence, cited by ledger statement: for every Voice plan,
   $f_j \le H \iff B_j(s, H-T) \ge \tau$; and D1's measurability line (its
   Step-8 repair in the turn-2 audit): monotone stake paths are Borel in $s$,
   $c_j$ is a first-hitting index over a finite calendar, and $B^F$, $Q^F$ are
   finite sums of measurable functions, hence measurable.
7. A8's interiority in the form $\Omega = \Pr(D = 1) > 0$ — required for the
   conditioning in Step 4 to be defined (attack repair R1; this is L2's h.7).
   When $S_{\mathrm{fl}} = \emptyset$, A7′ is vacuous and nothing here is
   claimed (WHERE IT FAILS case 5).

## PROOF / CONSTRUCTION

**Step 1 (equivalence — CLAIM i).** By hypothesis 1, $Q^F = b_j^*(s) - B^F$, so
$(B^F, Q^F) \mapsto (B^F, B^F + Q^F) = (B^F, b_j^*(s))$ is a linear bijection of
$\mathbb R^2$ (its inverse subtracts the first coordinate). The $a$-coordinate is
carried unchanged. Hence the two tuples generate the same σ-field and either
determines the other. In particular $B^F + Q^F = b_j^*(s)$: **the sum reveals the
terminal target.**

**Step 2 (the flagged region is a Voice region).** On $S_{\mathrm{fl}}$,
$D_{j(s)}(s) = 1$, and $D = 1 \Rightarrow a = 1$ by hypothesis 1's product form
with hypothesis 4 (only Voice plans cross). So $j(s)$ is a Voice plan and
$a = 1$ identically on $S_{\mathrm{fl}}$; the $a$-coordinate of the tuple is
constant there and carries no separating burden.

**Step 3 (A7′ ⟹ injectivity, with explicit inverse — CLAIM ii, first clause).**
Take $s \ne s'$ in $S_{\mathrm{fl}}$. By A7′, $b^{\circ}(s) \ne b^{\circ}(s')$.
By Step 1, $B^F + Q^F$ evaluated at $s$ equals $b^{\circ}(s)$ (the plan being
$j(s)$ by hypothesis 5), and likewise at $s'$. So the tuples differ in the sum
of their first two coordinates, hence differ. The map $s \mapsto \mathsf S_F(s)$
is injective on $S_{\mathrm{fl}}$, and the inverse is the composition
$\mathsf S_F \mapsto B^F + Q^F \mapsto (b^{\circ})^{-1}(B^F + Q^F) = s$, followed
by $s \mapsto j(s)$ (hypothesis 5) to recover the plan. A strictly increasing
function on a Borel subset of $\mathbb R$ has a strictly increasing inverse on
its image, and a monotone function is Borel; when $b^{\circ}$ is continuous the
image restricted to any interval of $S_{\mathrm{fl}}$ is an interval and the
inverse is continuous on it. The appeal to Lusin–Souslin is avoidable exactly
in that case — $b^{\circ}$ continuous and $S_{\mathrm{fl}}$ an interval (the
menu of Step 5), or when the inverse is claimed only a.e. under the flagged
law; for a general Borel $S_{\mathrm{fl}}$, Borel-ness of the image is
precisely the Lusin–Souslin content (attack repair R2; compare turn-2 audit
L2-O1).

**Step 4 (A7′ ⟹ the identification clause — CLAIM ii, second clause).** By
hypotheses 2 and 5, on $\{D = 1\}$ the tuple $\mathsf S_F$ is a *function* of
$s$ alone, and $\{D = 1\} = \{s \in S_{\mathrm{fl}}\}$ is an $s$-event;
measurability of that function is hypothesis 6's measurability line — card
§4.2's monotone rows plus D1's Step-8 sum decomposition (attack repair R4).
Hence $\sigma(\mathsf S_F, \mathbf 1\{D=1\}) \subseteq \sigma(s) \subseteq
\sigma(v, s, \xi) = \sigma(\Xi)$. The conditioning on $\{D=1\}$ is defined by
hypothesis 7. Now display the conditional-independence line (attack repair
R3): for every bounded Borel $u_1$ and every $A \in \sigma(\mathsf S_F,
\mathbf 1\{D=1\})$, hypothesis 3 gives $z_{0:H} \perp \Xi$ and $A \in
\sigma(\Xi)$, so $\mathbb E[u_1(z_{0:H})\,\mathbf 1_A] = \mathbb
E[u_1(z_{0:H})]\,\Pr(A)$; therefore $\mathbb E[u_1(z_{0:H}) \mid \mathsf S_F,
\mathbf 1\{D=1\}] = \mathbb E[u_1(z_{0:H})]$ a.s. — jointly, $z_{0:H} \perp
(\Xi, \mathsf S_F, \mathbf 1\{D=1\})$, which is the clause L2's Step 4
consumes ($\mathcal H_{f^-}^P \perp \Xi \mid \mathsf S_F$ on $\{D=1\}$). So
conditional on $(\mathsf S_F, D=1)$, $z_{0:H}$ has its unconditional law.
Moreover, writing
$\hat s = (b^{\circ})^{-1}(B^F + Q^F)$ (Step 3), on path $\hat s = s$, so the
observable residual $X_d - q_{j(\hat s) d}(\hat s) = X_d - q_{j(s)d}(s) = z_d$
for every $d$ — the pooled order-flow residual, computed from the tuple and the
known policy functions (hypothesis 5), is exactly the noise sequence,
independent of $(v, s, \xi)$. This is A7's identification clause in the form
L2's Steps 3–6 consume.

**Step 5 (the pro-rata menu — CLAIM iii, definitions).** Calendar
$d = 0, \dots, H$ (card §2). Fix an **accumulation schedule**
$\mathrm{sh} : \{-1, 0, \dots, H\} \to [0,1]$, weakly increasing, with
$\mathrm{sh}(-1) = 0$ and $\mathrm{sh}(H) = 1$ (example: $\mathrm{sh}(d) =
(d+1)/(H+1)$), and a **terminal-target function** $b^* : \mathbb R \to
(b_0, \bar b)$, continuous and **strictly increasing on all of $\mathbb R$**
(attack repair R5 — strictness must not be confined to a policy-dependent
Voice region: the menu is a primitive, cutoffs are equilibrium objects, and
P1's fixed-point argument needs the menu's properties at every candidate
$k \in \Theta$, repair R6; a target flat below the Voice cutoff also breaks
the card's joint $(j,s)$ form, the attack's 40-collision executed check). The
menu:

- **Exit** ($a = 0$): $B_E(s,d) = b_0 \cdot (1 - \mathrm{sh}(d))$.
- **Hold** ($a = 0$): $B_{\mathrm{Hold}}(s,d) = b_0$.
- **Voice** ($a = 1$): $B_V(s,d) = b_0 + (b^*(s) - b_0)\,\mathrm{sh}(d)$.

Card conformity, row by row (hypothesis 1): all paths lie in $[0, \bar b]$
(since $b^* < \bar b$); $B_j(s,-1) = b_0$ for all three; Exit is weakly
decreasing in $d$ and constant in $s$; Hold constant; Voice has
$\partial_d B_V = (b^*(s) - b_0)\,\Delta\mathrm{sh} \ge 0$ and
$\partial_s B_V = \mathrm{sh}(d)\, \partial_s b^* \ge 0$. By $b_0 < \tau$
(hypothesis 4) and their monotonicity, Exit and Hold never reach $\tau$ — A4's
"only Voice plans cross" is here **derived** from the menu, not assumed. The
menu is finite ($J = 3$; A2), ordered least to most aggressive by terminal
stake. The two $T$-comparative-static rows of §4.2 also hold on the menu
(attack repair R7): $c$ is $T$-free and $\mathrm{sh}$ is weakly increasing, so
for $T' < T$ at fixed policies $B^F(T') = b_0 + (b^*-b_0)\,\mathrm{sh}(c+T')
\le B^F(T)$ and $Q^F(T') = (b^*-b_0)(1-\mathrm{sh}(c+T')) \ge Q^F(T)$. The
one §4.2 sentence the menu does NOT satisfy is the strict-pair patch — that is
CLAIM (iv)'s point, not a conformity failure of the construction.

**Step 6 (crossing and flag structure).** For Voice,
$B_V(s,d) \ge \tau \iff \mathrm{sh}(d)\,(b^*(s) - b_0) \ge \tau - b_0$, so
$c(s) = \min\{d : \mathrm{sh}(d) \ge (\tau - b_0)/(b^*(s) - b_0)\}$, weakly
decreasing in $s$ (a larger target crosses weakly sooner), and by hypothesis 6
the flag lands iff $\mathrm{sh}(H-T)\,(b^*(s) - b_0) \ge \tau - b_0$. If
$\mathrm{sh}(H-T) > 0$ this reads $b^*(s) \ge b_0 + (\tau - b_0)/\mathrm{sh}(H-T)$,
and since $b^*$ is continuous and strictly increasing on the Voice region,
$S_{\mathrm{fl}}$ is an upper interval of the Voice region (possibly empty —
then A7′ holds vacuously and A8 fails, a separate hypothesis). Note every
flagged target satisfies $b^*(s) \ge b_0 + (\tau - b_0)/\mathrm{sh}(H-T) \ge \tau$.
If $\mathrm{sh}(H-T) = 0$, no history is flagged and the claim is vacuous.

**Step 7 (A7′ holds on the pro-rata menu — and so does the joint form).** On
$S_{\mathrm{fl}}$ the policy selects the single Voice plan (Step 2 plus Step
5's menu: Exit and Hold never cross, so never flag), so $b^{\circ}(s) =
b^*(s)$, strictly increasing on all of $\mathbb R \supseteq S_{\mathrm{fl}}$
by Step 5 (R5). A7′ holds — for every cutoff policy, since $b^*$'s strictness
nowhere references the cutoffs. By Steps 3–4, the on-path injective form of A7
holds on this menu. Moreover the card's **joint** form holds: the flagged set
$\{(j,s) : D_j(s;\tau,T) = 1\}$ contains only Voice pairs (Exit and Hold never
cross — this covers off-path pairs too, since $D_j$ is defined for every
$(j,s)$), and for two Voice pairs $(V,s) \ne (V,s')$ the sums $b^*(s) \ne
b^*(s')$ separate the tuples by Step 1. This proves CLAIM (iii).

**Step 8 (necessity of A7′ within the pro-rata family).** On the pro-rata menu
both flagged-tuple coordinates are functions of $s$ **only through**
$b^*(s)$: with $y := b^*(s) - b_0$, Step 6 gives $c = c(y)$, and
$B^F = b_0 + y\,\mathrm{sh}(c(y) + T)$, $Q^F = y\,(1 - \mathrm{sh}(c(y) + T))$
(hypothesis 1: $B^F = B_V(s, c+T)$, $Q^F = b^* - B^F$). By Step 1 the sum
recovers $y$, so the map $y \mapsto (B^F, Q^F)$ is injective for free; hence the
composite $s \mapsto \mathsf S_F$ is injective **iff** $s \mapsto b^*(s)$ is
injective on $S_{\mathrm{fl}}$, which for a weakly increasing $b^*$ (card §4.2)
is exactly strict monotonicity — A7′. So within the pro-rata family A7′ is not
merely sufficient but **necessary**: on any $b^*$-flat interval two distinct
signals produce an identical tuple, which is precisely the turn-2 audit's
L2-R1 generic failure.

**Step 9 (the patch violation — CLAIM iv; numeric witness).** On the pro-rata
menu, within any interval of $S_{\mathrm{fl}}$ where $c(s)$ is constant,
$B^F(s) = b_0 + (b^*(s) - b_0)\,\mathrm{sh}(c + T)$ is strictly increasing
(Step 6 showed $\mathrm{sh}(c) > 0$ at any crossing, and
$\mathrm{sh}(c+T) \ge \mathrm{sh}(c) > 0$). At a boundary where $c$ drops by
one, $\mathrm{sh}(c+T)$ drops, and $B^F$ jumps **down**. Witness with
$H = 9$, $\mathrm{sh}(d) = (d+1)/10$, $T = 2$, $\tau - b_0 = 1$:

| $b^*(s) - b_0$ | $c(s)$ | $\mathrm{sh}(c{+}T)$ | $B^F - b_0$ | $Q^F$ | sum |
|---|---|---|---|---|---|
| 2.4 | 4 | 0.7 | **1.68** | 0.72 | 2.4 |
| 2.6 | 3 | 0.6 | **1.56** | 1.04 | 2.6 |

(Flag check: $\mathrm{sh}(H{-}T) = \mathrm{sh}(7) = 0.8$, threshold
$(\tau - b_0)/0.8 = 1.25 \le 2.4, 2.6$ — both flagged; $c + T \le 9$ — both
file in time. $c$ computation: $c = \lceil 10/y \rceil - 1$ here.) As $s$ rises,
$b^*$ rises $2.4 \to 2.6$ while $B^F$ **falls** $1.68 \to 1.56$; the sum
recovers $b^*$ exactly. So $s \mapsto (B_j^F, b_j^*)$ is not strictly
increasing — not even componentwise monotone — on this menu, and the card's
§4.2 patch as written **excludes the canonical construction**, while A7′ holds
and injectivity is delivered by the sum coordinate alone. ($Q^F$ is not
monotone either in general: when $c + T = H$, $\mathrm{sh}(c{+}T) = 1$ and
$Q^F = 0$ identically on that interval.) Hence the patch must be replaced by
A7′, per CLAIM (iv). The two conditions are **non-nested** (attack repair
R-B): on a single-Voice menu the patch's $b_j^*$-coordinate strictness implies
A7′, but with two or more Voice plans a menu can satisfy the patch within each
plan while the composed target backtracks across a switch (WHERE IT FAILS
case 3) — so the patch implies A7′ only in the single-Voice case, and A7′
never implies the patch (this witness). The replacement is justified because
A7′ is what injectivity consumes, not because it is a weakening.

**Step 10 (consistency with D1-R2 — continuum-valued $B^F$).** On the pro-rata
menu, $b^*$ is continuous and strictly increasing on $S_{\mathrm{fl}}$, so on
each $c$-constant interval $B^F$ ranges over a nondegenerate interval:
$B^F$ is continuum-valued, exactly as D1 repair 2 requires (an injective map
out of a continuum of signals cannot land in a finite set — turn-2 audit,
locked findings D1-R2/L2-R1). The pooled alphabet stays finite (hypothesis 2's
$q_{jd}(s) = \Gamma(\cdot)$ coarsens increments to finitely many marks; A2)
while the filing reveals the exact stake — the two resolutions coexist by
design. And A5's reading over the flagged continuum is strictly easier here
(attack repair R8): A5's uniqueness means the flagged-price family is
**pinned, not chosen** — no selection principle is invoked; and continuity of
$P^F$ in $s$ follows by composition, since $s \mapsto (\hat v, \pi) = (\mu_v +
\beta(s - \mu_v), 1)$ is continuous and A5's pricing map is continuous in
beliefs.

## WHERE IT FAILS

1. **Binding stake cap.** If $b^*(s) = \bar b$ on a positive-measure subset of
   $S_{\mathrm{fl}}$ (the card allows $b^* \in [0, \bar b]$; the construction
   deliberately takes the image in $[b_0, \bar b)$), the composed target is flat
   there, and by Step 8 injectivity genuinely fails on the capped pool: the
   flagged tuple pools an interval of signals, the pooled history stays
   informative about $s$ within the pool, and L2's κ-invariance of $M_F$ can
   fail through the noise mixing. A7′ therefore carries a real economic
   restriction: **the cap must not bind on the flagged region.**
2. **Quantized stakes.** Integer share counts, tick sizes, or a discrete
   $b^*$-grid make $b^*$ a step function: flat intervals are generic and A7′
   fails literally. This is the discretisation risk for the numerical
   implementation (ticket 25): a discrete $s$-grid must re-read A7 as
   grid-injectivity (distinct grid nodes → distinct tuples), which holds iff
   the grid's $b^*$ values are pairwise distinct — arrangeable by
   construction, but it must be checked, not assumed.
3. **Multi-Voice menus with a backtracking composed target.** With two Voice
   plans $j < j'$ and a cutoff $k$ between them, if
   $b^*_{j'}(k^+) < b^*_j(k^-)$ then $b^{\circ}$ repeats values across the
   switch and A7′ fails; the tuple separates the pair only if $B^F$ happens to
   differ there (menu-specific, not guaranteed). A menu condition "composed
   target strictly increasing across plan switches" restores A7′.
4. **Feedback execution rules.** If the path reacts to realised order flow,
   $\mathsf S_F$ is no longer a function of $s$ alone and Step 4's σ-field
   inclusion collapses — but this violates hypothesis 2 (card §2's no-feedback
   timing), i.e., it is upstream of A7 (turn-2 audit L2-R2's territory).
5. **Empty flagged region ($\Omega = 0$).** Step 4's conditioning on $\{D=1\}$
   is undefined; A7′ holds vacuously and nothing here is claimed. Carried as
   hypothesis 7, mirroring L2's h.7 (attack repair R1).
6. **A target flat off the Voice region.** The on-path form survives (the
   fixed policy never selects Voice there) but the card's joint $(j,s)$ form
   fails: off-path Voice pairs whose paths would flag collapse to one tuple
   (the attack's executed check — 40 collisions on a legal pre-R5 menu).
   Repaired for this menu by R5's global strictness; the boundary stands for
   any menu that relaxes it.
7. **Policy-dependent menu definitions.** A hypothesis stated only at one
   equilibrium's cutoffs cannot feed P1's fixed-point argument, which needs it
   at every candidate $k \in \Theta$ (attack repair R6). A7′ as stated in
   CLAIM (iv) is therefore quantified over $\Theta$.
8. **Full separation — the relocated burden.** Every A7′-satisfying menu makes
   the filing reveal $s$ exactly. Existence of a qualifying menu is closed
   here; whether an equilibrium exists in which the blockholder *chooses* the
   fully revealing plan (and A3's single crossing survives on it) is open and
   is P1's burden. This is turn-2 audit L2-R1's consequence 2 taken one step
   further: the economic substance migrated from L2 to A7, and now from A7's
   satisfiability to P1's incentive compatibility.

## LABEL CLAIMED

None — A7 is a standing hypothesis, not a ledger row. Claimed: A7′ (as stated)
is sufficient on path, necessary within the pro-rata family, and satisfiable by
an explicit card-conformant menu. Status per protocol: this construction stands
only after the ticket-24 Opus adversarial attack and the ticket-27 proof-read;
the proposed card edits in CLAIM (iv) are applied only after the attack.

## NUMERICAL CHECK REQUEST

On the implemented menu (ticket 25's `numerical_v4/`, coordinate the plan menu
with this construction):

1. **Grid injectivity:** enumerate all flagged grid nodes $(s_i)$; assert all
   tuples $(B^F_i, Q^F_i)$ pairwise distinct; report the minimum pairwise
   separation. Predicted: separation $> 0$, of order the grid's $b^*$ spacing.
2. **Sum recovery:** $\max_i |(B^F_i + Q^F_i) - b^*(s_i)| = 0$ up to float
   arithmetic (predicted $< 10^{-12}$).
3. **Inverse recovery:** $\max_i |(b^{\circ})^{-1}(B^F_i + Q^F_i) - s_i| = 0$
   up to interpolation error on the grid (predicted $< 10^{-10}$ with exact
   inversion of the implemented $b^*$).
4. **Patch-violation witness:** count downward jumps of $s \mapsto B^F(s)$
   across the flagged grid; predicted $\ge 1$ whenever the flagged region
   spans at least two crossing dates; reproduce the table of Step 9 at
   $H = 9$, $\mathrm{sh}(d) = (d+1)/10$, $T = 2$, $\tau - b_0 = 1$ (predicted
   $B^F - b_0$: 1.68 then 1.56, sums 2.4 and 2.6, both exact).

## NOTATION DELTA

Symbols used that are not in card §4:

- $\mathrm{sh}(d)$ — the accumulation schedule (roman, word-like; chosen to
  avoid draft_v2's $\ell$ at ~872/2362, which is the secant line in the Jensen
  identity adjacent to L3's chord material; $\rho$, $\alpha$, $\phi$, $\varphi$,
  $\theta$ are all live in draft_v2; $\zeta$ is reserved for L3's mean-value
  point; $g$ for L3's chord function).
- $b^{\circ}(s) := b^*_{j(s)}(s)$ — the composed terminal target ($\beta$ is
  the card's Gaussian projection and is not available; $b^{\circ}$ has no card
  or draft_v2 usage).
- $S_{\mathrm{fl}}$ — the flagged signal region $\{s : D_{j(s)}(s;\tau,T)=1\}$.
  Roman $S$ with roman subscript; distinct from $\bar S$ (mean synergy) and
  from the sans-serif tuple $\mathsf S_F$; used only in this file.
- $y := b^*(s) - b_0$ — proof-local shorthand in Steps 8–9 only (lowercase;
  the card's $Y$ is the terminal payoff and is never written bare here).
- A7′ — the named hypothesis of CLAIM (ii).

## NOT CLAIMED

That the joint $(j,s)$ form holds beyond this menu (it is proved here only for
the single-Voice pro-rata menu with globally strict $b^*$; general menus get
A7′, the on-path form, quantified over $\Theta$); anything about the
conditional law on off-path *tuples* (pinned only up to null sets, as L2
already hedges); that A7′ is necessary outside the single-Voice pro-rata
family (Step 8's necessity is family-specific; in general the minimal
condition is bare injectivity of $s \mapsto (B^F, Q^F)$ on $S_{\mathrm{fl}}$,
which lacks a primitive menu reading); equilibrium existence or optimality of
the cutoff policy on this menu, including whether a blockholder would choose a
fully separating plan (P1's burden — WHERE IT FAILS case 8); that the flagged
region is nonempty (hypothesis 7 assumes it); κ-invariance itself (L2's
conclusion, not re-proved here); any uniqueness.

### FILE: proofs/A7_attack_verdict.md

# Adversarial attack on `A7_construction.md` — verdict (ticket 24, Opus attack half)

Attacker: fresh Opus subagent, theory lane, 2026-08-21, repo `blockholder_v4_theory` @ branch
`v4-theory` (no git run). Target: `research/model_v4/proofs/A7_construction.md`.
Context read: `MODEL_CARD.md` (stamp 2026-08-20 · `0c9185b`, in full),
`threads/thread1_turn2_audit.md` (in full), `threads/thread1_msg3.md` §1,
`threads/thread1_turn2_answer.md` L2 block (lines 236–477, to check what L2 actually consumes).
No other file in `proofs/` was opened.

Stance: refute. Three outcomes only — **WRONG** (a card row, an audit finding, or an executed check
contradicts it) · **MISCITED** (claim stands, citation does not) · **UNCHECKED** (could not check).
Everything not listed under one of those survived the attack.

Executed check: `a7_check.py` (scratchpad), exact rational arithmetic, rebuilt from the **card**
definitions (`c = inf{d : B_V(s,d) ≥ τ}` by brute-force search over the calendar, `f = c+T`,
`B^F = B_V(s,f)`, `Q^F = b^*−B^F`) — not from the construction's closed forms. Output verbatim in §3.

---

## 1. Verdict table

| # | Claim / step | Verdict | Evidence |
|---|---|---|---|
| C-i | Tuple equivalence; sum reveals the terminal target | **survives** | `Q^F = b^*−B^F` is card §4.2's definition; the shear map is a linear bijection of ℝ². Executed check 4: `max|(B^F+Q^F)−b^*| = 0` exactly over 17,501 flagged grid points. Identical to audit L2-R1's own observation — correctly attributed to §4.2, not over-claimed. |
| C-ii | A7′ ⟹ on-path injectivity + explicit inverse + A7's identification clause | **survives, 4 repairs** | Injectivity argument is valid (Step 3). Repairs R1–R4 below: missing `Ω>0`; the "no Lusin–Souslin needed" boast; conditional-independence asserted from an unconditional statement; "Borel" cited to hypotheses that give dependence, not measurability. |
| C-iii-a | The pro-rata menu satisfies A7′ | **survives** | Check 5: A7′ holds on the flagged set of the menu (`True`); Step 7's derivation (only Voice flags ⟹ `b° = b^*`) is correct given Step 5's `b_0 < τ`. |
| C-iii-b | "…and is **conformant with every card §4.2 row**" | **WRONG** | The strict-pair patch *is* a card §4.2 row (`B_j(s,d)` row: "On the flagged set, `s↦(B_j^F,b_j^*)` must be **strictly** increasing for Voice"). CLAIM (iv) of the same file says the menu **violates** it, and executed check 5 confirms the violation (`patch: False`). CLAIM (iii) and CLAIM (iv) contradict each other as written. Repair: "conformant with every card §4.2 row **except** the strict-pair patch sentence, whose replacement is CLAIM (iv)". |
| C-iii-c | "A7 … is satisfiable — the stack's largest open risk is closed" | **survives with a repair (R5)** | True for the **on-path** form, which is what L2 consumes (verified against `thread1_turn2_answer.md` Steps 1–12: every use of `ι_F` sits inside a conditional expectation under the equilibrium law, so only on-path tuples are non-null). But the card's A7 *as written* is the joint form `(j,s)↦(B_j^F,Q_j^F,a_j)` injective on the flagged set, and **the construction's own menu fails it** — executed check 6: 41 signals below the Voice cutoff whose Voice-plan history would flag collapse to **1** distinct tuple, 40 collisions. Free fix: require `b^*` strictly increasing on **all of ℝ**, not only on `[k_{J−1},∞)`. |
| C-iv-a | The pro-rata menu violates the §4.2 strict-pair patch (numeric witness) | **survives** | Check 1 reproduces the table exactly in rationals; check 3 finds **7** strict downward steps of `B^F` across the flagged region; check 5: patch `False`, A7′ `True`. |
| C-iv-b | "the replacement is a strict weakening that all previously conformant menus survive" (Step 9, last sentence) | **WRONG** | Contradicted by the file's own WHERE-IT-FAILS case 3: a two-Voice-plan menu with `b^*_{j'}(k^+) < b^*_j(k^-)` satisfies the per-plan patch and violates A7′. So patch ⇏ A7′, and (by the witness) A7′ ⇏ patch: the two conditions are **non-nested**, not ordered. The replacement is still the right edit — A7′ is the condition L2 needs — but it is a substitution, not a weakening, and a menu conformant under the patch can fail under A7′. |
| S-1 | Step 1 — linear bijection, same σ-field | survives | Bimeasurable bijection of ℝ²; `a` carried unchanged. |
| S-2 | Step 2 — flagged region is a Voice region | **MISCITED** | `D_j = 1{a_j=1, c<∞, f≤H}` forces `a=1` from its **own definition** (card §4.2 `D_j` row: "`D=1 ⇒ a=1`"). Hypothesis 4 (A4's "only Voice plans cross") is not needed for this and is cited anyway. Harmless; drop the A4 citation or cite the `D_j` row. |
| S-3 | Step 3 — A7′ ⟹ injectivity, explicit inverse | survives, repair R2 | Injectivity is right. "A strictly increasing function on a Borel subset of ℝ has a strictly increasing inverse on its image, and a monotone function is Borel" is correct as a *subspace*-measurability statement; what is not free is that the **image** is Borel in ℝ, which for a general Borel `S_fl` is exactly Lusin–Souslin. The boast "No appeal to Lusin–Souslin is needed" is safe only in the continuous case the menu supplies (`S_fl` an interval, `b°` continuous ⟹ image an interval) or if the inverse is only claimed a.e. under the flagged law. Say which. |
| S-4 | Step 4 — σ-field logic and the identification clause | survives, repairs R1/R3/R4 | The chain `σ(𝖲_F, 1{D=1}) ⊆ σ(s) ⊆ σ(v,s,ξ)` and A1 ⟹ `z ⊥ σ(𝖲_F,1{D=1})` is correct. "The market knows the policy functions" is **not** smuggled: card §3(iii) makes on-path beliefs Bayes-consistent with the strategy profile, and L2's own h.6 fixes the policies exogenously — this is the ordinary sufficient-statistic construction the audit already cleared (audit §3.2, "no circularity"). Three defects, all one-line: **(R1)** the step conditions on `{D=1}` with no `Ω>0` / A8 hypothesis, while Step 6 concedes `S_fl` may be empty — this is L2's h.7 and audit L2-R3, and it is missing from the hypothesis list. **(R3)** what L2 consumes is `𝓗^P ⊥ (v,s,ξ) | 𝖲_F`; the displayed logic delivers only `z ⊥ σ(𝖲_F,1{D=1})`, and the conditional statement is asserted in words. Add: A1 gives `z ⊥ (v,s,ξ)` jointly and `𝖲_F ∈ σ(s)`, so `z ⊥ (Ξ, 𝖲_F, 1{D=1})` jointly, whence the conditional independence. **(R4)** "the tuple `𝖲_F` is a **Borel** function of `s`" is cited to hypotheses 2 and 5, which give functional *dependence* on `(j,s,τ,T)`, not measurability; measurability comes from §4.2's monotonicity plus D1's Step-8 line (`B_j(s,f_j(s)) = Σ_d 1{f_j(s)=d+T}·B_j(s,d)`, audit D1-R2). |
| S-5 | Step 5 — the menu and its row-by-row card conformity | survives, repairs R6/R7 | Bounds, `B_j(s,−1)=b_0` for all three plans, Exit weakly decreasing, Hold constant, Voice `∂_dB ≥ 0`, `∂_sB ≥ 0`, A2 finiteness, ordering by terminal stake (`0 < b_0 < b^*(s)`), and A4's "only Voice crosses" **derived** from `b_0 < τ` — all check out against card §4.2. `b^* < b̄` strictly is *consistent* with the card's `b^*∈[0,b̄]` (a sub-interval), and is in fact forced by strict monotonicity on an unbounded Voice region. **(R7)** the conformity sweep omits the two comparative-static rows: `B_j^F` row (`T'<T ⇒ B^F(T') ≤ B^F(T)`) and `Q_j^F` row (`T'<T ⇒ Q^F(T') ≥ Q^F(T)`). I checked both: `c` is `T`-free and `sh` is weakly increasing, so both hold on the menu — no error, but the sweep claims completeness it does not have. **(R6)** see below — the menu is defined against `[k_{J−1},∞)`, a policy object. |
| S-6 | Step 6 — crossing and flag structure | survives, nit | `c(s) = min{d : sh(d) ≥ (τ−b_0)/(b^*(s)−b_0)}` divides by `y = b^*(s)−b_0` without noting `y>0` (true on the Voice region by Step 5) and writes `min` without the empty-set case (`c=+∞`). The flag condition matches D1's clock equivalence: `y·sh(H−T) ≥ τ−b_0 ⟺ c ≤ H−T`. "Every flagged target satisfies `b^* ≥ τ`" is correct (`sh ≤ 1`). Executed check 3: smallest flagged `y` on the grid is exactly 1.25, as Step 6 predicts. |
| S-7 | Step 7 — A7′ holds on the menu | survives | Follows from Steps 2, 5, 6. |
| S-8 | Step 8 — necessity of A7′ "within the pro-rata family" | survives for a **single-Voice** menu; **MISCITED** as stated | I could not build a counterexample inside the Step-5 menu: the entire Voice path is `b_0 + y·sh(d)`, so `c`, `B^F` and `Q^F` depend on `s` **only** through `y = b^*(s)−b_0`; equal `b^*` ⟹ identical tuple ⟹ the "iff" holds. But the word **family** is load-bearing and wrong: enlarge the family to two Voice plans (different schedules or targets) and necessity fails — the file's own WHERE-IT-FAILS case 3 says the tuple can separate a pair on which `b°` repeats. Restate as "within any single-Voice menu of the Step-5 form", which is what the body actually proves. |
| S-9 | Step 9 — the witness table and the down-jump | **arithmetic survives, exact** | Recomputed from the definitions, not the closed forms: `y=2.4 → c=4, sh(6)=0.7, B^F−b_0=1.68, Q^F=0.72, sum=12/5`; `y=2.6 → c=3, sh(5)=0.6, B^F−b_0=1.56, Q^F=1.04, sum=13/5`. Flag threshold `(τ−b_0)/sh(7) = 1.25`, both flagged; `f = 6, 5 ≤ 9`, both file in time. The closed form `c = ⌈10/y⌉−1` matches brute force at **4000/4000** grid points. `B^F` falls while `b^*` rises: confirmed. `Q^F ≡ 0` on the `c+T=H` interval: confirmed. 7 strict downward steps of `B^F` across the flagged region. Only the final sentence fails (C-iv-b above). |
| S-10 | Step 10 — continuum-valued `B^F`, A5 selection | survives, **MISCITED** + repair R8 | The menu-specific argument is right (`B^F−b_0 = y·sh(c+T)` with `sh(c+T)>0` fixed on each `c`-interval and `y` ranging over an interval). But the cited justification — "an injective map out of a continuum of signals cannot land in a finite set", audit D1-R2 / L2-R1 — proves only that the **tuple** is continuum-valued, not the `B^F` coordinate: on this very menu `Q^F ≡ 0` on the lowest `c`-interval (executed check 4), so the coordinates trade the burden. The same over-reach sits in the card's A7 note ("Injectivity … forces `B^F` continuum-valued"); the true statement is "forces `(B^F,Q^F)` continuum-valued". **(R8)** "the selected pricing fixed points can be chosen continuous in `s`": A5 gives *uniqueness*, so nothing is "chosen", and A5's continuity is in *beliefs, cutoffs and parameters*, not in the flagged-tuple index. Continuity in `s` is an extra property, asserted where it must be argued (card §8 rule 7). |
| W-1..4 | WHERE IT FAILS cases 1–4 | all genuine | Cap binding (the card does allow `b^*=b̄`), quantized stakes, multi-Voice backtracking, feedback execution (correctly identified as upstream, audit L2-R2's territory). Case 3 is the one that kills Step 9's last sentence. |
| W-miss | Missing failure cases | **4 a referee would find** | See §4. |
| Mech | Mechanical scan | 1 banned word | `trivially` at line 231 (WHERE IT FAILS case 2, not inside a numbered proof step). The audit's own scan standard was "0 hits across the whole answer". Zero `\ref`/`\cite`/lemma-number hits; no bare `W`, `λ`, `ψ`, or bare `𝖲`; all eight template headings present; all six hypotheses used. |

---

## 2. Repairs, in the order they should be applied

**R-A (blocking the CLAIM block as written).** CLAIM (iii) must not say "conformant with every card
§4.2 row" while CLAIM (iv) says the menu violates a §4.2 row. Write: "conformant with every card
§4.2 row except the strict-pair patch sentence, whose replacement is CLAIM (iv)."

**R-B (blocking Step 9's last sentence).** Delete "so the replacement is a strict weakening that all
previously conformant menus survive." Replace with: "The two conditions are non-nested — the patch
does not imply A7′ once the menu carries two or more Voice plans (WHERE IT FAILS case 3), and A7′
does not imply the patch (Step 9's witness). A7′ is the condition L2 consumes; the patch is neither
necessary nor sufficient for it."

**R1.** Add `Ω = Pr(D=1) > 0` (A8) as a numbered hypothesis and cite it at Step 4. Step 6 concedes
`S_fl` may be empty; L2 carries this as its h.7 and audit L2-R3 already flagged the identical gap.

**R2.** Step 3: qualify "No appeal to Lusin–Souslin is needed" — it is free when `b°` is continuous
and `S_fl` is an interval (the menu's case), or when the inverse is claimed only a.e. under the
flagged law. For a general Borel `S_fl`, Borel-ness of the *image* is exactly the Lusin–Souslin
content.

**R3.** Step 4: display the conditional-independence line (`A1` ⟹ `z ⊥ (Ξ, 𝖲_F, 1{D=1})` jointly ⟹
`𝓗^P ⊥ Ξ | 𝖲_F`), which is the clause L2 Step 4 consumes. As written the step asserts the
conditional statement from an unconditional one.

**R4.** Step 4: cite §4.2 monotonicity + D1's Step-8 measurability line for "Borel", not hypotheses
2 and 5.

**R5 (substantive — this one changes the menu).** Take `b^*` strictly increasing on **all of ℝ**,
not only on `[k_{J−1},∞)`. Cost: nothing — it is compatible with every §4.2 row (`b^*` enters only
the Voice plan's path; Exit's terminal target stays 0, Hold's stays `b_0`). Gain: two things at
once. (a) The card's A7 as literally written — `(j,s) ↦ (B_j^F,Q_j^F,a_j)` injective on the flagged
set `{(j,s) : D_j(s)=1}`, which contains off-path pairs since `D_j` is defined for every `(j,s)` —
then holds on the menu, because only Voice ever flags and `b^*` separates every signal. Without it
the menu fails the card's own A7: executed check 6, 40 collisions. (b) It removes R6.

**R6 (substantive — order of quantifiers, matters for P1).** Step 5 defines the menu against "the
Voice region `[k_{J−1},∞)`" — but the menu is a **primitive** and `k_{J−1}` is a policy/equilibrium
object. As written, the menu is tailored to the policy it is supposed to support; and P1's Brouwer
argument needs the hypothesis to hold at **every** candidate `k ∈ Θ`, not only at the fixed point.
R5's global strict monotonicity severs the dependence. Correspondingly, the proposed §4.2 card edit
("the composed terminal target `s ↦ b^*_{j(s)}(s)` must be strictly increasing") places a
policy-dependent condition in a row that restricts primitives — it must be quantified: "for every
cutoff vector `k ∈ Θ`", which for a menu amounts to each `b^*_j` strictly increasing **and** no
backtracking of `b^*_j` across any admissible plan switch.

**R7.** Step 5: add the two omitted §4.2 comparative-static rows to the conformity sweep (both hold;
verified here).

**R8.** Step 10: drop "can be chosen" (A5 gives uniqueness) and either argue continuity of `P^F` in
`s` or state it as an open regularity point. A5 as cited does not deliver continuity in the
flagged-tuple index.

**R9 (card-edit text, CLAIM iv).** The proposed §5 A7 note should read "the **on-path** injective
form (fixed cutoff policy, tuples of positive-probability histories)", and should record that the
card's stronger joint `(j,s)` form additionally needs `b^*` strictly increasing off the Voice region
(R5). Its failure-boundary list should gain `Ω = 0` and the policy-dependence of R6.

**Answering the ticket's target 6 directly — does replacing the patch with A7′ break anything D1's
or L2's proofs use?** No. Per the audit's step descriptions and the L2 text: D1 Steps 1–5 use only
weak `∂_dB_j ≥ 0` / `∂_sB_j ≥ 0` and finiteness of the calendar; D1 Step 7's product formula uses
A4; D1 Steps 8/11 use measurability and the `P_{−1}^P` convention. None of them touches the
strict-pair patch. L2 uses A7 only through `ι_F` inside conditional expectations under the
equilibrium law (Steps 1, 3, 4, 8), so it needs **on-path** recovery only, and null-set hedging
covers the rest — A7′ supplies exactly that. The one thing the patch supplies and A7′ does not is
strictness of the `B^F` coordinate, which no step in D1, L1 or L2 uses.

---

## 3. Executed check — verbatim output

Script: `/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4/d06ccee3-762c-4331-a587-d3581e6a875e/scratchpad/a7_check.py`
(exact `fractions.Fraction` arithmetic; `c` obtained by brute-force search over the calendar from the
card's `c_j = inf{d : B_j(s,d) ≥ τ}`, never from the file's closed form; `b_0` normalised to 0 so
`y = b^*`, `τ = 1`).

```
==========================================================================
CHECK 1 - Step 9 witness table recomputed from the definitions
==========================================================================
  y=b*-b0   c  sh(c+T)    B^F-b0     Q^F    sum  f<=H  flag closed-form c
   2.4000   4   0.7000    1.6800  0.7200 2.4000  True  True             4
   2.6000   3   0.6000    1.5600  1.0400 2.6000  True  True             3
sh(H-T)=sh(7) = 0.8, flag threshold (tau-b0)/sh(7) = 1.25
exact sums: 12/5 13/5
B^F falls while b* rises: True

==========================================================================
CHECK 2 - closed form c = ceil(10/y)-1 against brute force, y in (0,10]
==========================================================================
grid points tested: 4000   mismatches: 0   []

==========================================================================
CHECK 3 - flagged region structure, down-jumps of B^F, monotonicity of b*
==========================================================================
  down-jump at y=1.4290: B^F 1.4285 -> 1.2861  (c 7 -> 6), b* rose 1.4285 -> 1.4290
  down-jump at y=1.6670: B^F 1.4998 -> 1.3336  (c 6 -> 5), b* rose 1.6665 -> 1.6670
  down-jump at y=2.0000: B^F 1.5996 -> 1.4000  (c 5 -> 4), b* rose 1.9995 -> 2.0000
  down-jump at y=2.5000: B^F 1.7496 -> 1.5000  (c 4 -> 3), b* rose 2.4995 -> 2.5000
  flagged y-grid points: 17501   distinct c values: [0, 1, 2, 3, 4, 5, 6, 7]
  B^F strictly-down steps: 7   up steps: 17493
  smallest flagged y on grid: 1.2500 (Step 6 predicts 1.25)

==========================================================================
CHECK 4 - sum recovery and injectivity on the flagged grid
==========================================================================
  max |(B^F+Q^F) - b*| over flagged grid: 0  (exact rationals)
  duplicate (B^F,Q^F) tuples at distinct signals: 0
  Q^F == 0 identically on the lowest c-interval (c+T=H)? True

==========================================================================
CHECK 5 - componentwise patch vs A7': which holds on the menu
==========================================================================
  card 4.2 patch (B^F strictly increasing on flagged set): False
  A7' (composed target b* strictly increasing on flagged set): True

==========================================================================
CHECK 6 - menu-level A7 (card wording: (j,s) injective on the flagged set)
        b* weakly increasing everywhere, strictly only on the Voice region
==========================================================================
  signals below the Voice cutoff whose Voice-plan history WOULD flag: 41
  distinct flagged tuples they produce: 1   collisions: 40
  -> menu-level (j,s) injectivity on the flagged set: FAILS
     (A7' still holds: the fixed policy never selects Voice there.)
```

Check 6's `b^*` is a legal Step-5 instance: continuous, weakly increasing on ℝ, strictly increasing
on the Voice region `[1,∞)`, image in `[b_0,b̄)`, `b^*>b_0` on the Voice region — flat at 3.0 below
the cutoff, which Step 5 permits. Since `D_j(s;τ,T)` is defined for every `(j,s)` pair (card §4.2),
those off-path Voice pairs are in the card's flagged set, and the map collapses them.

---

## 4. Failure cases the file is missing (target 7)

The four listed cases are all genuine. Four more a referee will find:

5. **Empty flagged region / `Ω = 0`.** Step 6 concedes `S_fl` may be empty and calls A7′ vacuous
   there — but Step 4 conditions on `{D=1}` regardless. L2 carries this as its own WHERE-IT-FAILS
   case 6 and as h.7. It belongs here, not in a parenthesis.
6. **The card's joint `(j,s)` form fails on this very menu** (executed check 6) whenever `b^*` is
   flat off the Voice region. Currently only hinted at in NOT CLAIMED; it is a failure case, and R5
   is its one-line fix.
7. **The menu is defined against the policy it must support** (R6). A hypothesis stated on
   `b^*_{j(s)}` cannot be checked before the equilibrium is solved, and P1's Brouwer argument needs
   it on all of `Θ`.
8. **The economic one, and the one a referee will press hardest.** Every A7′-satisfying menu is
   *fully separating*: the filing reveals `s` exactly. The construction shows such a menu **exists**;
   it does not show that a blockholder who dislikes revealing `s` before the bidder moves would
   choose the plan carrying it, nor that A3's single crossing survives on it. The file is honest —
   NOT CLAIMED defers this to P1 — but CLAIM (iii)'s "the stack's largest open risk … is closed"
   should read "…is relocated from A7 to P1": what has been closed is *existence of a qualifying
   menu*, and what remains open is *whether an equilibrium on such a menu exists*. This is the
   audit's L2-R1 consequence 2 ("the economic substance of L2 has migrated into A7") one step
   further along.

---

## 5. Overall verdict

**SURVIVES WITH REPAIRS.**

Nothing in the construction is mathematically refuted. The Step 9 arithmetic is exact — every number
in the witness table reproduces from the card definitions under brute-force crossing search, and the
closed form `c = ⌈10/y⌉−1` matches at 4000/4000 grid points. Step 8's necessity holds inside the
single-Voice menu and I could not break it there. Step 3's injectivity and Step 4's σ-field logic are
sound, and "the market knows the policy functions" is a legitimate on-path PBE step, not a smuggled
assumption. Target 4 confirmed against the L2 text itself: L2 consumes only on-path recovery.

Two **WRONG**s, both wording-level contradictions inside the file, both repairable without touching
the mathematics:
- **C-iii-b** — "conformant with every card §4.2 row" contradicts CLAIM (iv) (the strict-pair patch
  is a §4.2 row and the menu violates it; check 5).
- **C-iv-b** — "the replacement is a strict weakening that all previously conformant menus survive"
  contradicts the file's own WHERE-IT-FAILS case 3; the two conditions are non-nested.

Repairs required before the CLAIM (iv) card edits are applied: **R-A, R-B, R1, R5, R6, R9**
(substantive) and **R2, R3, R4, R7, R8** (one-line). The two card edits themselves are endorsed in
substance — the strict-pair patch is over-strong relative to its own stated rationale (injectivity
fails only if **both** tuple coordinates are flat, not if `B^F` is non-monotone) and A7′ is the
condition L2 actually consumes — but the §4.2 replacement text must be quantified over policies
(R6) and the §5 note must say **on-path** (R9).

No label moves. A7 remains a standing hypothesis; this file remains a construction awaiting the
ticket-27 proof-read.

### FILE: proofs/L3_proof.md

# L3 — Chord-vanishing lemma: full proof

**Written against MODEL_CARD stamp 2026-08-20 · commit `0c9185b`.** Ticket 21 (T2a). Answer template
is the card's §8.6; every heading below is one of the eight required headings, in order. The ledger
label is untouched: L3 remains **CONJECTURE** in the card until an independent re-derivation and a
proof-read both pass.

---

## CLAIM

Fix the plan menu, the cutoff policy and the execution policies, and let $\kappa$ range over an open
interval $\mathcal K\subseteq(0,1)$.

**(i) Exact mean-value form of the chord.** For every $\bar\pi>0$ and every function
$g$ that is continuous on $[0,\bar\pi]$ and twice differentiable on $(0,\bar\pi)$ — in particular for
every $g\in C^2[0,\bar\pi]$ — there exists a point $\zeta\in(0,\bar\pi)$ with

$$C_g(\bar\pi)\;:=\;g(0)-2g\!\left(\tfrac{\bar\pi}{2}\right)+g(\bar\pi)\;=\;\tfrac14\,\bar\pi^{2}\,g''(\zeta).$$

This is an identity, not an approximation: there is no remainder term, and no differentiability of
$g$ at the endpoints $0$ or $\bar\pi$ is used.

**(ii) The pooled cell's interior $\kappa$-motion.** Under A($\tau$) the pooled block's expectation of
the engagement-premium kernel $h$ satisfies, at every $\kappa\in\mathcal K$,

$$\partial_\kappa\,\mathbb E_\kappa[h]\;=\;A'_\kappa\,C_h(\bar\pi),$$

so the interior $\kappa$-motion of the pooled block is proportional to the chord $C_h(\bar\pi)$, with
the constant of proportionality $A'_\kappa$ supplied by A($\tau$) and by nothing else.

**(iii) Vanishing.** Combining (i) and (ii),
$\partial_\kappa\mathbb E_\kappa[h]=\tfrac14 A'_\kappa\,\bar\pi^{2}h''(\zeta_{\bar\pi})$ exactly, with
$\zeta_{\bar\pi}\in(0,\bar\pi)$. If in addition $h''$ extends continuously to $0$ from the right, then
$C_h(\bar\pi)=\tfrac14h''(0)\bar\pi^{2}+o(\bar\pi^{2})$ as $\bar\pi\downarrow0$, and the interior
$\kappa$-motion vanishes at rate $\bar\pi^{2}$. Without that extra regularity the motion still
vanishes — mere continuity of $h$ at $0$ gives $C_h(\bar\pi)\to0$ — but the quadratic rate is not
available.

**(iv) The $C_h=0$ case, and why the statement is an "if".** If $C_h(\bar\pi)=0$ then
$\partial_\kappa\mathbb E_\kappa[h]=0$ exactly, at every $\kappa\in\mathcal K$: the pooled block's
expectation is constant in $\kappa$ on $\mathcal K$. The converse is **false** — zero interior motion
also arises when $A'_\kappa=0$ with $C_h(\bar\pi)\neq0$ — so the lemma is stated as an implication
and **never as an equivalence**.

**(v) Domain of A($\tau$), stated as a result.** Given a $\kappa$-invariant three-point support
$\{0,\bar\pi/2,\bar\pi\}$ and weights differentiable in $\kappa$, A($\tau$)'s derivative restrictions
$A_0'=A_1'=A'_\kappa$, $A_{1/2}'=-2A'_\kappa$ are **not** an additional assumption: they are
equivalent to $\kappa$-invariance of the pooled block's total mass and of its unnormalised engagement
moment, and both of those are consequences of the model at fixed policies. A($\tau$)'s entire content
is therefore the **support** condition. A one-round ternary-noise market with informed mark $2\bar z$
and pre-order engagement share $\tfrac12$ satisfies it (Example A, §PROOF Step 16). A one-round
ternary-noise market with informed mark $\bar z$ — which is the frozen manuscript's own no-disclosure
structure — does **not**: its pooled law has four atoms, two of which move with $\kappa$ (Example B,
Step 17). **Whether the two-round pooled cell of §2 is in the satisfying class is declared OPEN**
(Step 18), with the weakest sufficient condition named there.

---

## HYPOTHESES

Each is used at the step named; no hypothesis is carried unused.

1. **(A($\tau$), representation part.)** At fixed policies and for every $\kappa\in\mathcal K$, the
   pooled block's expectation of $h$ has the symmetric ternary representation
   $\mathbb E_\kappa[h]=A_0(\kappa)h(0)+A_{1/2}(\kappa)h(\bar\pi/2)+A_1(\kappa)h(\bar\pi)$, and the
   three evaluation points $0,\bar\pi/2,\bar\pi$ do not vary with $\kappa$. *(Card §5, A($\tau$).)*
   **Used at Steps 7, 8′, 14; Step 12 consumes it only through Step 8.**
2. **(A($\tau$), derivative part.)** $A_0,A_{1/2},A_1$ are differentiable on $\mathcal K$ with
   $A_0'=A_1'=A'_\kappa$ and $A_{1/2}'=-2A'_\kappa$, and $A'_\kappa$ is bounded on $[0,1]$.
   *(Card §5 A($\tau$) and §4.4 $A'_\kappa$ row.)* **Used at Steps 8, 12, 13, 14.**
3. **(Reading of $\bar\pi$ and of the weights.)** $\bar\pi$ is the right endpoint of the chord, i.e.
   the largest posterior in the support of the pooled block's engagement-posterior law; the $A_i$ are
   that block's atom masses, taken either conditionally on $\{D=0\}$ (summing to $1$) or unnormalised
   (summing to $1-\Omega$). **Used at Steps 9, 14, 19.**
4. **(Regularity for the exact form.)** $h$ is continuous on $[0,\bar\pi]$ and twice differentiable on
   the open interval $(0,\bar\pi)$. $h\in C^2[0,\bar\pi]$ implies this and is the form the card's
   surrounding statements use. **Used at Steps 1–6, 10.**
5. **(Extra regularity for the small-$\bar\pi$ corollary, and only for it.)** There is $\delta>0$ such
   that one and the same kernel $h$ serves the whole family $\{\bar\pi<\delta\}$ — the cell's
   non-engagement value component is held fixed as $\bar\pi$ varies — $h$ is twice differentiable on
   $[0,\delta)$, and $h''$ is continuous at $0$ from the right. **Used at Steps 11 and 12, and
   nowhere in Part I.**
6. **($\kappa$-free pooled mass and pooled engagement moment.)** At fixed policies $j=j(s)$,
   $a=a_{j(s)}$, and $D=\mathbf 1\{a_j=1\}\cdot\mathbf 1\{B_j(s,H-T)\ge\tau\}$, so $a$ and $D$ are
   functions of $s$ alone and carry no $\kappa$; the law of $s$ contains no $\kappa$. Hence
   $\Pr(D=0)$ and $\Pr(a=1,D=0)$ do not vary with $\kappa$. *(The product form of $D$ is Hypothesis 9
   (D1) by its card-ledger statement; card §2 no-feedback timing bullet; card §4.1, which puts
   $\kappa$ in the $z_d$ row and nowhere else.)* **Used at Steps 8′, 9, 15.**
7. **($h(0)=0$.)** *(Card §4.4, $h$ row.)* **Used at Step 13 and in the numerical check.**
8. **(Kernel is a function of the engagement posterior alone.) [ADDITION — not in the card as
   written.]** At fixed policies and for every $\kappa\in\mathcal K$, the premium kernel depends on the
   control-node information set **only through the engagement posterior**: $h(\mathcal I)=h(\pi(\mathcal
   I))$, so the three numbers $h(0)$, $h(\bar\pi/2)$, $h(\bar\pi)$ are $\kappa$-free. This is a
   restriction, not a reading. Card §4.4 gives $h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$ and card
   §4.3's entry row makes $p$ depend on the price $P(\mathcal I)$ as well as on $\pi$, so in the model
   $h=\pi\,p(\hat v,\pi)$ is a function of **two** scalars; the restriction says the standalone-value
   channel and the engagement channel do not co-move inside the pooled cell in a way that moves $h$ at
   a fixed posterior. Card §4.4's $C_h$ row and A($\tau$) both write $h$ with a single posterior
   argument and so commit the same elision, and L4's (br-ii) names this same object as an assumption it
   does not prove; this hypothesis prices the object the same way rather than consuming it silently.
   **Card gap, regeneration item: A($\tau$) should carry this clause explicitly at the card's next
   regeneration.** **Used at Step 7, and hence wherever Step 7 is consumed (Steps 8, 8′, 10–13).**
9. **(D1, by its card-ledger statement.)** $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is measurable and maps
   every control-node history into exactly one cell; for every Voice plan
   $f_j\le H\iff B_j(s,H-T)\ge\tau$. *(Card §6 ledger, D1 row.)* D1's own proof is neither read nor
   used, and D1 carries the card label **CONJECTURE**, so L3 inherits that conditionality.
   **Used inside Hypothesis 6 (the product form of $D$), and hence at Steps 8′, 9, 15.**

---

## PROOF

### Part I — the exact mean-value form (requirement (a))

Throughout Part I, $g$ denotes an arbitrary function satisfying Hypothesis 4 on $[0,\bar\pi]$ with
$\bar\pi>0$ fixed; $h$ is substituted for $g$ at Step 10. Write $\Delta_g$ for the proof-local
first-difference function defined at Step 2.

**Step 1.** By Hypothesis 4, $g$ is continuous on $[0,\bar\pi]$ and twice differentiable on
$(0,\bar\pi)$. Twice differentiable on $(0,\bar\pi)$ means $g'$ exists at every point of
$(0,\bar\pi)$ and is itself differentiable at every point of $(0,\bar\pi)$; a differentiable function
is continuous, so $g'$ is continuous on $(0,\bar\pi)$.

**Step 2.** Define, for $t\in[0,\bar\pi/2]$,
$$\Delta_g(t)\;:=\;g\!\left(t+\tfrac{\bar\pi}{2}\right)-g(t).$$
Evaluating at the two endpoints of that interval and subtracting,
$$\Delta_g\!\left(\tfrac{\bar\pi}{2}\right)-\Delta_g(0)
=\Big[g(\bar\pi)-g\!\left(\tfrac{\bar\pi}{2}\right)\Big]-\Big[g\!\left(\tfrac{\bar\pi}{2}\right)-g(0)\Big]
=g(0)-2g\!\left(\tfrac{\bar\pi}{2}\right)+g(\bar\pi)\;=\;C_g(\bar\pi).$$
All four evaluations of $g$ are at points of $[0,\bar\pi]$, where $g$ is defined by Hypothesis 4, so
each of the four terms is a real number and the cancellation is arithmetic: the value
$g(\bar\pi/2)$ appears once with a minus sign from the first bracket and once with a minus sign from
the second, leaving the coefficient $-2$.

**Step 3.** $\Delta_g$ is continuous on $[0,\bar\pi/2]$: for $t$ in that interval both $t$ and
$t+\bar\pi/2$ lie in $[0,\bar\pi]$, where $g$ is continuous by Step 1. $\Delta_g$ is differentiable on
the open interval $(0,\bar\pi/2)$: for $t$ there, both $t\in(0,\bar\pi/2)\subset(0,\bar\pi)$ and
$t+\bar\pi/2\in(\bar\pi/2,\bar\pi)\subset(0,\bar\pi)$ are points where $g'$ exists by Step 1, and the
derivative of a difference is the difference of derivatives, so
$\Delta_g'(t)=g'\!\left(t+\bar\pi/2\right)-g'(t)$.

**Step 4.** The mean value theorem applies to $\Delta_g$ on $[0,\bar\pi/2]$, its two hypotheses being
supplied by Step 3. There exists $t_1\in(0,\bar\pi/2)$ with
$$\Delta_g\!\left(\tfrac{\bar\pi}{2}\right)-\Delta_g(0)\;=\;\tfrac{\bar\pi}{2}\,\Delta_g'(t_1)
\;=\;\tfrac{\bar\pi}{2}\Big[g'\!\left(t_1+\tfrac{\bar\pi}{2}\right)-g'(t_1)\Big],$$
the second equality by the formula for $\Delta_g'$ in Step 3.

**Step 5.** Consider the closed interval $[\,t_1,\;t_1+\bar\pi/2\,]$. Since $0<t_1<\bar\pi/2$ (Step 4),
its left endpoint satisfies $t_1>0$ and its right endpoint satisfies
$t_1+\bar\pi/2<\bar\pi/2+\bar\pi/2=\bar\pi$; therefore
$[\,t_1,\;t_1+\bar\pi/2\,]\subset(0,\bar\pi)$. On $(0,\bar\pi)$, Step 1 gives that $g'$ is continuous
and differentiable. The mean value theorem applied to $g'$ on $[\,t_1,\;t_1+\bar\pi/2\,]$ therefore
yields a point $\zeta\in(t_1,\;t_1+\bar\pi/2)$ with
$$g'\!\left(t_1+\tfrac{\bar\pi}{2}\right)-g'(t_1)\;=\;\tfrac{\bar\pi}{2}\,g''(\zeta).$$

**Step 6.** Chaining Step 2, Step 4 and Step 5,
$$C_g(\bar\pi)\;=\;\tfrac{\bar\pi}{2}\cdot\tfrac{\bar\pi}{2}\,g''(\zeta)\;=\;\tfrac14\,\bar\pi^{2}\,g''(\zeta),
\qquad \zeta\in(t_1,\;t_1+\tfrac{\bar\pi}{2})\subset(0,\bar\pi),$$
which is CLAIM (i). Two features of this derivation are worth recording because the corollary at
Step 11 does not share them. First, the identity is exact — no term was discarded. Second, every use
of $g$ beyond continuity was at points of the **open** interval $(0,\bar\pi)$: neither $g'(0)$,
$g''(0)$, $g'(\bar\pi)$ nor $g''(\bar\pi)$ was invoked, so the hypothesis "$C^2$ on the interval"
is genuinely all that is consumed, and differentiability at zero is not.

### Part II — the $\kappa$-derivative under A($\tau$) (requirement for $\partial_\kappa\mathbb E[h]=A'_\kappa C_h$)

**Step 7.** Fix $\kappa\in\mathcal K$. By Hypothesis 1 the pooled block's expectation is the
three-term sum $\mathbb E_\kappa[h]=A_0(\kappa)h(0)+A_{1/2}(\kappa)h(\bar\pi/2)+A_1(\kappa)h(\bar\pi)$
in which the three numbers $h(0),h(\bar\pi/2),h(\bar\pi)$ do not vary with $\kappa$, because
Hypothesis 1 fixes the three evaluation points and **Hypothesis 8** makes $h$ a function of the
posterior value alone. Hypothesis 8 is load-bearing here and is not free: without it the
differentiation below carries the extra term $\sum_i A_i(\kappa)\,\partial_\kappa h(\pi_i)$ and
CLAIM (ii) is false. A finite sum of products (constant) $\times$ (differentiable function of $\kappa$) is
differentiable in $\kappa$, with derivative the corresponding sum, by Hypothesis 2's
differentiability of the weights:
$$\partial_\kappa\mathbb E_\kappa[h]\;=\;A_0'(\kappa)h(0)+A_{1/2}'(\kappa)h\!\left(\tfrac{\bar\pi}{2}\right)+A_1'(\kappa)h(\bar\pi).$$

**Step 8.** Substitute Hypothesis 2's restrictions $A_0'=A_1'=A'_\kappa$ and $A_{1/2}'=-2A'_\kappa$
into Step 7 and factor out the common $A'_\kappa$:
$$\partial_\kappa\mathbb E_\kappa[h]
=A'_\kappa h(0)-2A'_\kappa h\!\left(\tfrac{\bar\pi}{2}\right)+A'_\kappa h(\bar\pi)
=A'_\kappa\Big[h(0)-2h\!\left(\tfrac{\bar\pi}{2}\right)+h(\bar\pi)\Big]
=A'_\kappa\,C_h(\bar\pi),$$
the last equality being the card §4.4 definition of $C_h$. This is CLAIM (ii). The single place where
the three restrictions on the weight derivatives are used is this factorisation: they are exactly the
coefficient pattern $(+1,-2,+1)$ that the second difference $C_h$ carries, which is why the
proportionality constant is a scalar and not a triple.

**Step 8′ (the chord-gap route — same conclusion, mechanism displayed).** Let $\ell_h$ be the affine
function on $[0,\bar\pi]$ with $\ell_h(0)=h(0)$ and $\ell_h(\bar\pi)=h(\bar\pi)$. Write
$\mathbb E_\kappa[h]=\mathbb E_\kappa[\ell_h]+\mathbb E_\kappa[h-\ell_h]$, an identity because
$\ell_h$ and $h-\ell_h$ sum to $h$ pointwise. Under Hypothesis 1 the second term collapses to a
single product: $h-\ell_h$ vanishes at $0$ and at $\bar\pi$ by the definition of $\ell_h$, so only
the middle atom survives, and since $\ell_h(\bar\pi/2)=\tfrac12\big(h(0)+h(\bar\pi)\big)$ by
affinity,
$$\mathbb E_\kappa[h-\ell_h]=A_{1/2}(\kappa)\Big[h\!\left(\tfrac{\bar\pi}{2}\right)-\tfrac12\big(h(0)+h(\bar\pi)\big)\Big]
=-\tfrac12\,A_{1/2}(\kappa)\,C_h(\bar\pi).$$
Differentiating and using $A_{1/2}'=-2A'_\kappa$ (Hypothesis 2) returns
$\partial_\kappa\mathbb E_\kappa[h-\ell_h]=A'_\kappa C_h(\bar\pi)$. The first term contributes
nothing: $\mathbb E_\kappa[\ell_h]=\ell_h(0)\cdot(\text{total pooled mass})+\text{slope}\cdot(\text{pooled
engagement moment})$, and both of those are $\kappa$-invariant by Hypothesis 6, so
$\partial_\kappa\mathbb E_\kappa[\ell_h]=0$. Step 8′ agrees with Step 8 and adds two things: the
affine part of $h$ contributes no interior motion at all, and the whole motion is carried by the
mass of the single middle atom. It also locates where the three-point symmetry is used — it is what
collapses the chord-gap sum to one term. For a support with more than one interior atom the same
argument gives $\partial_\kappa\mathbb E_\kappa[h]=\sum_i A_i'(\kappa)\,(h-\ell_h)(\pi_i)$, which is
a weighted sum of chord gaps and is **not** proportional to $C_h(\bar\pi)$ in general; that is the
content of Example B at Step 17.

**Step 9 (which normalisation, and the bridge to $\mathcal S_P$ and $\mathcal S$).** By Hypothesis 3
the weights are the pooled block's masses under either normalisation. Under the conditional
normalisation, $\mathbb E_\kappa[h]=\mathbb E[h\mid D=0]$ and card §4.4 gives
$M_P=\Delta_m\,\mathbb E[h\mid D=0]$, so Step 8 yields
$$\partial_\kappa M_P=\Delta_m A'_\kappa C_h(\bar\pi),\qquad
\mathcal S_P=\Delta_m\,\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert .$$
Under the unnormalised normalisation the weights are $(1-\Omega)$ times the conditional ones, and
$1-\Omega$ does not vary with $\kappa$ by Hypothesis 6, so the two versions of Step 8 differ by the
$\kappa$-free factor $(1-\Omega)$ and the identity holds verbatim in both. Card §4.4's relation
$\mathcal S=(1-\Omega)\mathcal S_P$, which holds under L2 and fixed policies, then gives
$\mathcal S=(1-\Omega)\Delta_m\lvert A'_\kappa\rvert\lvert C_h(\bar\pi)\rvert$: the flagged block
contributes no $\kappa$-motion (that is L2, cited as a card ID, not re-proved here), so the pooled
chord is the only surviving channel.

### Part III — combining, and the two limits (requirements (a)-corollary and (b))

**Step 10.** Apply Part I with $g=h$; Hypothesis 4 is stated for $h$, so Step 6 delivers a point
$\zeta_{\bar\pi}\in(0,\bar\pi)$ with $C_h(\bar\pi)=\tfrac14\bar\pi^{2}h''(\zeta_{\bar\pi})$.
Substituting into Step 8,
$$\partial_\kappa\mathbb E_\kappa[h]\;=\;\tfrac14\,A'_\kappa\,\bar\pi^{2}\,h''(\zeta_{\bar\pi}),$$
exactly, for every $\bar\pi>0$ and every $\kappa\in\mathcal K$. No limit has been taken and no term
discarded.

**Step 11 (the small-$\bar\pi$ corollary, and the extra regularity it costs).** Assume Hypothesis 5
in addition. For $\bar\pi<\delta$, Step 10's $\zeta_{\bar\pi}$ lies in $(0,\bar\pi)$, so
$0<\zeta_{\bar\pi}<\bar\pi$ and $\zeta_{\bar\pi}\to0$ as $\bar\pi\downarrow0$. Then
$$\Big\lvert\,C_h(\bar\pi)-\tfrac14h''(0)\bar\pi^{2}\,\Big\rvert
=\tfrac14\bar\pi^{2}\,\big\lvert h''(\zeta_{\bar\pi})-h''(0)\big\rvert .$$
Hypothesis 5's one-sided continuity of $h''$ at $0$ makes the bracket tend to $0$ as
$\zeta_{\bar\pi}\to0$; dividing by $\bar\pi^{2}$, the left side divided by $\bar\pi^2$ tends to $0$,
which is the definition of $o(\bar\pi^{2})$. Hence
$$C_h(\bar\pi)=\tfrac14h''(0)\bar\pi^{2}+o(\bar\pi^{2}),\qquad \bar\pi\downarrow0 .$$
**Which extra regularity this costs.** Step 6 recorded that the exact form uses $h$ only at points of
$(0,\bar\pi)$ and never needs $h$ to be differentiable at $0$. The corollary needs $h''(0)$ to exist
and needs $h''$ to be continuous at $0$ from the right — both statements *at* the endpoint the exact
form avoided — and it needs the kernel $h$ to be the same across the family of shrinking $\bar\pi$,
which the exact form also does not need because it is a statement at one fixed $\bar\pi$. A different
sufficient condition, which does not run through Part I at all, is second-order Peano
differentiability at $0$: if $h(\pi)=h(0)+h'(0)\pi+\tfrac12h''(0)\pi^{2}+o(\pi^{2})$ then substituting
that expansion at the three evaluation points and cancelling gives the constant terms cancelling
($1-2+1=0$), the linear terms cancelling ($-2\cdot\tfrac12+1=0$), and the quadratic terms leaving
$\big(-2\cdot\tfrac18+\tfrac12\big)h''(0)\bar\pi^{2}=\tfrac14h''(0)\bar\pi^{2}$, with the three
$o(\bar\pi^{2})$ terms absorbed. That route assumes less about $h$ near $0$ and more at $0$; neither
route is implied by the other, and neither is needed for the exact form.

**Step 12 (vanishing, and how little it needs).** From Step 10 and Hypothesis 2's boundedness of
$A'_\kappa$,
$$\big\lvert\partial_\kappa\mathbb E_\kappa[h]\big\rvert
\;\le\;\tfrac14\,\sup_{[0,1]}\lvert A'_\kappa\rvert\;\bar\pi^{2}\,\sup_{(0,\bar\pi)}\lvert h''\rvert
\;\xrightarrow[\bar\pi\downarrow0]{}\;0$$
whenever the last supremum stays bounded, which Hypothesis 5 supplies on $[0,\delta)$. The vanishing
conclusion is more robust than the quadratic rate, and this is worth separating because the card's
maintained orientation is a weak one: by Step 8 the motion is $A'_\kappa C_h(\bar\pi)$, and
$C_h(\bar\pi)=h(0)-2h(\bar\pi/2)+h(\bar\pi)\to h(0)-2h(0)+h(0)=0$ using only continuity of $h$ at $0$,
Hypothesis 2's bound on $A'_\kappa$, and **Hypothesis 5's first clause** — one and the same kernel $h$
must serve the whole shrinking family, or the three evaluations being compared belong to different
functions and no limit statement is available. So the pooled cell's interior $\kappa$-motion vanishes
as $\bar\pi\downarrow0$ under continuity of $h$ at $0$ plus that one clause of Hypothesis 5;
Hypothesis 4 buys the exact mean-value representation and Hypothesis 5's remaining clauses buy the
$\bar\pi^{2}$ rate.

**Step 13 (the $C_h=0$ case, explicitly — requirement (b)).** Suppose $C_h(\bar\pi)=0$. Step 8 gives
$\partial_\kappa\mathbb E_\kappa[h]=A'_\kappa\cdot0=0$ at every $\kappa\in\mathcal K$, so
$\mathbb E_\kappa[h]$ is constant on $\mathcal K$ and, by Step 9, $\partial_\kappa M_P=0$ and
$\mathcal S_P=0$. The interior $\kappa$-motion is exactly zero — not small, not signed, zero — and
the lemma holds in that case as stated. Three consequences must be recorded.

  (a) **The result is an implication, never an equivalence.** $C_h(\bar\pi)=0$ implies zero interior
  motion (this step). Zero interior motion does **not** imply $C_h(\bar\pi)=0$: take any pooled law
  satisfying Hypothesis 1 whose weights happen to be locally constant in $\kappa$ on a subinterval of
  $\mathcal K$. There $A'_\kappa=0$, so Step 8 gives zero motion for **every** kernel $h$, including
  kernels with $C_h(\bar\pi)$ strictly negative. Writing L3 with "iff" would therefore assert
  something false, which is why the card's maintained orientation $C_h\le0$ is weak and why the
  statement is kept as an "if".

  (b) **$C_h(\bar\pi)=0$ does not make $h$ affine.** By Step 10, $C_h(\bar\pi)=0$ with $\bar\pi>0$
  forces $h''(\zeta_{\bar\pi})=0$ at the one point $\zeta_{\bar\pi}$ the mean value theorem produced,
  and at no other point. A kernel that is strictly concave on part of $[0,\bar\pi]$ and strictly
  convex on the rest can have $C_h(\bar\pi)=0$ exactly.

  (c) **A testable identity in the $C_h=0$ case.** By Hypothesis 7, $h(0)=0$, so $C_h(\bar\pi)=0$ is
  the identity $h(\bar\pi)=2h(\bar\pi/2)$ — the top of the chord is exactly twice the midpoint. This
  is the form the numerical check below uses to construct the case, rather than searching for it.

### Part IV — the domain of A($\tau$) (requirement (c))

**Step 14 (what A($\tau$) actually restricts).** Suppose the pooled block's posterior law is
supported on the three $\kappa$-invariant points $\{0,\bar\pi/2,\bar\pi\}$ (Hypothesis 1's support
clause) with weights $A_0,A_{1/2},A_1$ differentiable in $\kappa$ (Hypothesis 2), summing to a total
mass $\mathrm{m}(\kappa)$ and carrying an engagement moment
$\mathrm{r}(\kappa):=A_{1/2}(\kappa)\tfrac{\bar\pi}{2}+A_1(\kappa)\bar\pi$ (Hypothesis 3 identifies
the $A_i$ as masses, so these are the block's mass and its unnormalised first moment). Then:

$$\Big[\;\mathrm{m}'(\kappa)=0\ \text{ and }\ \mathrm{r}'(\kappa)=0\;\Big]
\qquad\Longleftrightarrow\qquad
\Big[\;A_0'=A_1'\ \text{ and }\ A_{1/2}'=-2A_1'\;\Big].$$

*Forward.* $\mathrm{r}'=0$ reads $A_{1/2}'\tfrac{\bar\pi}{2}+A_1'\bar\pi=0$; dividing by
$\bar\pi/2>0$ gives $A_{1/2}'=-2A_1'$. Substituting that into
$\mathrm{m}'=A_0'+A_{1/2}'+A_1'=0$ gives $A_0'=-A_{1/2}'-A_1'=2A_1'-A_1'=A_1'$.
*Reverse.* Given $A_0'=A_1'$ and $A_{1/2}'=-2A_1'$, sum: $A_0'+A_{1/2}'+A_1'=A_1'-2A_1'+A_1'=0$, so
$\mathrm{m}'=0$; and $A_{1/2}'\tfrac{\bar\pi}{2}+A_1'\bar\pi=-2A_1'\tfrac{\bar\pi}{2}+A_1'\bar\pi=0$,
so $\mathrm{r}'=0$. Writing $A'_\kappa$ for the common value $A_0'=A_1'$ recovers Hypothesis 2
verbatim.

**Step 15 (both conservation laws are theorems here, not assumptions).** By Hypothesis 6, at fixed
policies $\Pr(D=0)$ and $\Pr(a=1,D=0)$ do not vary with $\kappa$. The pooled block's total mass is
$\Pr(D=0)$ (unnormalised) or $1$ (conditional), so $\mathrm{m}'=0$. Its unnormalised engagement
moment is $\mathbb E[\pi(\mathcal I_H)\mathbf 1\{D=0\}]=\Pr(a=1,D=0)$ by the tower property applied
to the posterior $\pi(\mathcal I)=\Pr(a=1\mid\mathcal I)$ with $\{D=0\}$ a coordinate of the
conditioning information (card §4.3), so $\mathrm{r}'=0$; the conditional version divides by the
$\kappa$-free $\Pr(D=0)$ and inherits it. Combining with Step 14: **once the support condition holds,
A($\tau$)'s derivative restrictions are implied by the model at fixed policies and are not a separate
assumption.** All of A($\tau$)'s bite sits in the support condition — exactly three atoms, at
$0$, $\bar\pi/2$ and $\bar\pi$, none of them moving with $\kappa$.

**Step 16 (Example A — a structure that satisfies A($\tau$), inside the card's own primitives).**
One trading date, $d=0$. Engagement $a\in\{0,1\}$ with $\Pr(a=1)=\rho=\tfrac12$. The Voice plan's
pooled order mark is $q_0=2\bar z$ — admissible because card §4.2 puts $q_{jd}=\Gamma(\text{stake
increment})$ with $\Gamma$ a finite ordered coarsening and places no ceiling of $\bar z$ on its image
— and the non-engaging plan's mark is $q_0=0$ (card §4.2, Hold constant). Noise is the card's ternary
mark: $\Pr(z_0=0)=1-\kappa$, $\Pr(z_0=\pm\bar z)=\kappa/2$ (card §4.1). Observed flow is
$X_0=q_0+z_0$ (card §4.2). Enumerating:

| $a$ (prob) | $q_0$ | $X_0=-\bar z$ | $X_0=0$ | $X_0=\bar z$ | $X_0=2\bar z$ | $X_0=3\bar z$ |
|---|---|---|---|---|---|---|
| $1$ ($\tfrac12$) | $2\bar z$ | — | — | $\kappa/2$ | $1-\kappa$ | $\kappa/2$ |
| $0$ ($\tfrac12$) | $0$ | $\kappa/2$ | $1-\kappa$ | $\kappa/2$ | — | — |

The realised posteriors are therefore:

- $X_0\in\{2\bar z,3\bar z\}$: only $a=1$ contributes, so $\pi=1$; joint mass
  $\tfrac12(1-\kappa)+\tfrac12\cdot\tfrac{\kappa}{2}=\tfrac{2-\kappa}{4}$.
- $X_0\in\{-\bar z,0\}$: only $a=0$ contributes, so $\pi=0$; joint mass
  $\tfrac12\cdot\tfrac{\kappa}{2}+\tfrac12(1-\kappa)=\tfrac{2-\kappa}{4}$.
- $X_0=\bar z$: both contribute, each with $\tfrac12\cdot\tfrac{\kappa}{2}$, so
  $\pi=\dfrac{\tfrac12\cdot\tfrac{\kappa}{2}}{\tfrac12\cdot\tfrac{\kappa}{2}+\tfrac12\cdot\tfrac{\kappa}{2}}=\tfrac12$;
  mass $\tfrac{\kappa}{2}$.

Support $\{0,\tfrac12,1\}$, which is $\{0,\bar\pi/2,\bar\pi\}$ with $\bar\pi=1$, and every one of the
three points is free of $\kappa$: the two extreme cells are fully revealing at every $\kappa$, and
the middle cell's posterior is $\tfrac12$ because the two types reach $X_0=\bar z$ through noise
realisations of equal probability $\kappa/2$, which cancels. Weights:
$$A_1(\kappa)=\tfrac{2-\kappa}{4},\qquad A_{1/2}(\kappa)=\tfrac{\kappa}{2},\qquad A_0(\kappa)=\tfrac{2-\kappa}{4},$$
summing to $\tfrac{2-\kappa}{4}+\tfrac{\kappa}{2}+\tfrac{2-\kappa}{4}=\tfrac{4-2\kappa}{4}+\tfrac{\kappa}{2}=1$.
Differentiating: $A_1'=A_0'=-\tfrac14$ and $A_{1/2}'=+\tfrac12=-2\cdot(-\tfrac14)$. So Hypothesis 2
holds exactly with $A'_\kappa=-\tfrac14$, and Hypothesis 1 holds with $\bar\pi=1$. The moment check of
Step 14 confirms it: $A_{1/2}\tfrac12+A_1\cdot1=\tfrac{\kappa}{4}+\tfrac{2-\kappa}{4}=\tfrac12=\rho$,
free of $\kappa$. Economically, raising $\kappa$ moves mass out of the two revealing end cells and
into the single pooling cell, symmetrically and one-for-one, which is precisely the coefficient
pattern $(+1,-2,+1)$ that Step 8 factors.

Two features of Example A are load-bearing and neither is a normalisation. First, the informed mark
must be **strictly outside the reach of the uninformed mark plus noise** ($2\bar z>0+\bar z$), which
is what makes both end cells fully revealing and pins the support endpoints at $0$ and $1$ for every
$\kappa$. Second, the pre-order engagement share must be **exactly $\tfrac12$**, which is what puts
the pooling cell's posterior at the midpoint of the chord rather than somewhere else in it. The word
"symmetric" in A($\tau$) is carrying that second requirement.

*Example A′ (the same class, with $\bar\pi$ free, for the small-$\bar\pi$ check).* Example A has
$\bar\pi=1$ and so cannot be swept toward zero. A family with $\bar\pi$ free is obtained directly:
put atoms at $\{0,\bar\pi/2,\bar\pi\}$ with $A_1(\kappa)=A_0(\kappa)=\alpha-c\kappa$ and
$A_{1/2}(\kappa)=1-2\alpha+2c\kappa$, so $A'_\kappa=-c$ and Hypothesis 2 holds by inspection; taking
$\alpha=0.4$, $c=0.3$ keeps all three weights in $[0.1,0.8]$ for $\kappa\in[0,1]$. This is a genuine
information structure and not merely a list of numbers: for a binary state with prior
$\rho:=A_{1/2}\tfrac{\bar\pi}{2}+A_1\bar\pi$ (which Step 14's computation shows is $\kappa$-free,
here $\rho=\bar\pi/2$), the likelihoods
$$\Pr(\text{signal }i\mid a=1)=\frac{A_i\pi_i}{\rho},\qquad
\Pr(\text{signal }i\mid a=0)=\frac{A_i(1-\pi_i)}{1-\rho}$$
over the three signals $i\in\{0,\tfrac12,1\}$ with $\pi_i\in\{0,\bar\pi/2,\bar\pi\}$ are nonnegative,
sum to $\rho/\rho=1$ and $(1-\rho)/(1-\rho)=1$ respectively, and return the posteriors
$$\Pr(a=1\mid i)=\frac{\rho\cdot A_i\pi_i/\rho}{\rho\cdot A_i\pi_i/\rho+(1-\rho)\cdot A_i(1-\pi_i)/(1-\rho)}
=\frac{A_i\pi_i}{A_i\pi_i+A_i(1-\pi_i)}=\pi_i .$$

**Step 17 (Example B — a structure that does not satisfy A($\tau$), and it is the frozen
manuscript's own).** Same one trading date and the same ternary noise, but now the Voice plan's mark
is $q_0=+\bar z$ and the non-engaging mark is $q_0=0$, with $\Pr(a=1)=\rho\in(0,1)$. Then
$X_0\in\{-\bar z,0,\bar z,2\bar z\}$ and the cells are:

| $X_0$ | contributing $(q_0,z_0)$, unnormalised mass | posterior $\pi$ |
|---|---|---|
| $-\bar z$ | $(0,-\bar z)$: $(1-\rho)\tfrac{\kappa}{2}$ | $0$ |
| $0$ | $(\bar z,-\bar z)$: $\rho\tfrac{\kappa}{2}$; $(0,0)$: $(1-\rho)(1-\kappa)$ | $\pi_-(\kappa)=\dfrac{\rho\kappa/2}{\rho\kappa/2+(1-\rho)(1-\kappa)}$ |
| $\bar z$ | $(\bar z,0)$: $\rho(1-\kappa)$; $(0,\bar z)$: $(1-\rho)\tfrac{\kappa}{2}$ | $\pi_+(\kappa)=\dfrac{\rho(1-\kappa)}{\rho(1-\kappa)+(1-\rho)\kappa/2}$ |
| $2\bar z$ | $(\bar z,\bar z)$: $\rho\tfrac{\kappa}{2}$ | $1$ |

A($\tau$) fails twice over. The support has **four** points, not three. And the two interior points
**move with $\kappa$**: the likelihood ratio at $X_0=0$ is $\dfrac{\kappa/2}{1-\kappa}$, strictly
increasing in $\kappa$ on $(0,1)$, so $\pi_-$ is strictly increasing; the likelihood ratio at
$X_0=\bar z$ is $\dfrac{1-\kappa}{\kappa/2}$, strictly decreasing, so $\pi_+$ is strictly decreasing.
The consequence for L3 is exact and can be written down: differentiating
$\mathbb E_\kappa[h]=\sum_x\Pr(X_0=x)\,h(\pi(x))$ gives
$$\partial_\kappa\mathbb E_\kappa[h]
=\underbrace{\sum_x\big[\partial_\kappa\Pr(X_0=x)\big]h(\pi(x))}_{\text{the term A}(\tau)\text{ keeps}}
+\underbrace{\sum_x\Pr(X_0=x)\,h'(\pi(x))\,\partial_\kappa\pi(x)}_{\text{the term A}(\tau)\text{ has no room for}},$$
and the second sum is generically nonzero because $\partial_\kappa\pi_\pm\neq0$ by the monotonicity
just shown. Even the first sum is not proportional to $C_h(\bar\pi)$: by Step 8′ it equals
$\sum_i A_i'(h-\ell_h)(\pi_i)$ over four atoms, a weighted sum of chord gaps at two distinct interior
points, and no single scalar multiple of the second difference at the midpoint reproduces it.

This is not an artificial counterexample. It is the structure the frozen manuscript actually solves:
its no-disclosure order-flow enumeration has four cells with posteriors
$\{0,\ \pi(-1,0),\ \pi(0,0),\ \bar\pi\}$, the two middle ones written as ratios in which the noise
probabilities $p_0=1-\kappa$ and $p_1=\kappa/2$ appear in both numerator and denominator, so they
move with $\kappa$; only the two chord ends survive the $\kappa\to0^+$ and $\kappa\to1^-$ limits.
The manuscript's own route to the chord is therefore not A($\tau$)'s three-point representation but
the chord-gap identity of Step 8′ — the affine part contributes a $\kappa$-free constant because the
unnormalised engagement moment is pinned, and the interior motion is the motion of the gap between
$h$ and its chord. **Step 8′ is the part of this proof that transfers to the manuscript's structure;
Step 8's clean proportionality is not.** That is a limitation of A($\tau$), stated here rather than
discovered later.

**Step 18 (is the two-round pooled cell in the satisfying class? — declared OPEN).** I cannot settle
this and I do not claim it either way. What can be stated precisely is the following.

*Why it is not settled by Example A.* Example A produces $\bar\pi=1$, and this is forced, not
incidental: within the card's one-round primitives, non-engaging plans have marks that are weakly
negative or zero (card §4.2: Hold constant, Exit weakly decreasing) while Voice plans have positive
increments, so the largest order-flow realisation is attainable only by a Voice plan, and the top
posterior atom is $1$. Any one-round ternary-noise market with a non-degenerate pooled law therefore
has $\bar\pi=1$, and L3's $\bar\pi\downarrow0$ limit is empty in that class.

*Why the two-round structure is where $\bar\pi<1$ can come from.* On the flagged cell $\pi\equiv1$
(card §4.3). The two-round timing removes exactly the histories that would carry the revealing top
atom into the flagged cell, leaving the pooled cell with a top atom strictly below $1$; and card §4.4
records the maintained property that $\lvert C_h\rvert$ is weakly increasing in $\bar\pi$, with L4
asserting that a lower $\tau$ weakly lowers $\bar\pi$ in the pooled class. So the object L3's limit
is about is generated by the two-round partition, not by the one-round market.

*What would have to be shown, stated as the weakest sufficient condition I can name.* By Step 15,
it suffices to show the **support** condition alone: that the pooled cell's engagement-posterior law,
at fixed policies, is supported on exactly three points $0<\bar\pi/2<\bar\pi$ with none of them
varying with $\kappa$. By Step 16 that decomposes into two checkable requirements: (S1) every pooled
order-flow cell is either fully revealing of $a=0$, fully revealing of $a=1$ up to the pooled cell's
own ceiling $\bar\pi$, or a single cell whose posterior is $\bar\pi/2$; and (S2) that middle cell's
likelihood ratio is free of $\kappa$, which in Example A came from the two contributing types
reaching the cell through noise events of equal probability. Example B fails (S1) and (S2)
simultaneously. Whether a two-round plan menu can be built to satisfy (S1)–(S2) across a whole
window of $H$ trading dates — where the pooled history is the vector $(X_0,\dots,X_d)$ and the pooled
cell is itself carved out by the stake-path event $\{B_j(s,H-T)<\tau\}$ — I have not determined.
**Declared OPEN.** It sits next to the A7-satisfiability question as the second place where a
maintained hypothesis of this model has an unverified domain, and it is load-bearing for L3, L4 and
T1 jointly.

**Step 19 (a reading of $\bar\pi$ that must be fixed, or L3 is vacuous).** Hypothesis 3 reads
$\bar\pi$ as the **largest posterior in the pooled support**. The card's §4.4 gloss calls $\bar\pi$
the "pre-order pooled engagement share in the chord", and if that were read as *the mean of the
pooled posterior law*, L3 would be vacuous. The reason is a two-line consequence of Step 14: with
support $\{0,\bar\pi/2,\bar\pi\}$, conditional weights summing to $1$, and mean equal to $\bar\pi$,
the moment equation is $A_{1/2}\tfrac{\bar\pi}{2}+A_1\bar\pi=\bar\pi$, i.e.
$\tfrac{A_{1/2}}{2}+A_1=1$; combined with $A_0+A_{1/2}+A_1=1$ this gives $A_0=A_1-1\le0$, hence
$A_0=0$, $A_1=1$, $A_{1/2}=0$ — the law collapses to a point mass at $\bar\pi$, $A'_\kappa=0$, and
Step 8 returns zero motion for every kernel. A mean cannot equal the maximum of its own support
unless the law is degenerate.

The non-vacuous reading is the one the frozen manuscript uses, and it is internally consistent:
there $\bar\pi$ is the engagement share **within the sub-block that generates the top cell** — the
ratio of Quiet-Voice mass to the combined Hold-plus-Quiet mass — while the pooled cell's mean is
strictly smaller because the Exit mass sits at posterior $0$ and is counted in the mean but not in
$\bar\pi$. Under that reading $\rho<\bar\pi$ whenever the Exit block has positive mass, and nothing
degenerates. Example A illustrates the gap concretely: $\bar\pi=1$ while $\rho=\tfrac12$. This is a
card-reading clarification, not a change to the claim — L3 is true under either reading, but only
under Hypothesis 3's reading does it say anything.

---

## WHERE IT FAILS

1. **Four-atom pooled law with $\kappa$-moving interior atoms (Example B, Step 17) — the frozen
   manuscript's own no-disclosure structure.** A($\tau$)'s representation is false there: the support
   has four points and the two interior posteriors are strictly monotone in $\kappa$. Step 8's
   proportionality to $C_h(\bar\pi)$ fails, and the omitted term
   $\sum_x\Pr(X_0=x)h'(\pi(x))\partial_\kappa\pi(x)$ is generically nonzero. Step 8′'s chord-gap
   identity survives in the weaker form $\partial_\kappa\mathbb E_\kappa[h]=\sum_iA_i'(h-\ell_h)(\pi_i)$,
   which is a sum of chord gaps at two distinct interior points and is not a scalar multiple of the
   midpoint second difference.

2. **A kink in $h$ inside the chord — the exact form dies.** Take $\bar\pi=1$ and the tent kernel
   $h(\pi)=\pi$ on $[0,\tfrac12]$, $h(\pi)=1-\pi$ on $[\tfrac12,1]$. Then $C_h(1)=0-2(\tfrac12)+0=-1$,
   while $h''$ exists and equals $0$ at every point of $(0,1)$ other than $\tfrac12$, so
   $\tfrac14\bar\pi^{2}h''(\zeta)=0$ for every admissible $\zeta$ and there is **no** $\zeta$
   satisfying Step 6. Hypothesis 4's twice-differentiability on the open interval is therefore not
   decoration. Economically this is the case where the entry probability turns over sharply once the
   posterior is high enough for the price to impound the premium, so that $h=\pi p$ rises then falls
   with a corner between.

3. **$h''$ unbounded at zero — the exact form survives, the corollary dies.** Take $h(\pi)=\pi^{3/2}$
   on $[0,1]$. It is continuous on $[0,\bar\pi]$ and twice differentiable on $(0,\bar\pi)$, so
   Hypothesis 4 and Step 6 hold; but $h''(\pi)=\tfrac34\pi^{-1/2}\to\infty$ as $\pi\downarrow0$, so
   Hypothesis 5 fails. Direct computation gives
   $C_h(\bar\pi)=\bar\pi^{3/2}\big(1-2^{-1/2}\big)\approx0.2929\,\bar\pi^{3/2}$, which is of **exact
   order $\bar\pi^{3/2}$** — bounded above and below by positive multiples of $\bar\pi^{3/2}$ — and
   therefore **not** $\tfrac14h''(0)\bar\pi^{2}+o(\bar\pi^{2})$ for any
   finite constant. The vanishing conclusion of Step 12 still holds — $\bar\pi^{3/2}\to0$ — at a
   slower rate. This case separates CLAIM (i) from CLAIM (iii) cleanly and is the reason the two are
   stated apart.

4. **Weights not differentiable in $\kappa$.** If the pooled cell's composition changes discretely at
   some $\kappa_0$ — a plan entering or leaving the pooled class as noise intensity crosses a
   threshold — then $A_i$ has a corner or a jump at $\kappa_0$, Hypothesis 2 fails there, and
   $\partial_\kappa\mathbb E_\kappa[h]$ does not exist at $\kappa_0$. The lemma then holds only on the
   subintervals of $\mathcal K$ between such points, with $A'_\kappa$ possibly different on each.

5. **The kernel moving with $\bar\pi$ across the family.** Hypothesis 5 requires one $h$ for the whole
   shrinking family. If lowering $\bar\pi$ also changes the price schedule or the non-engagement value
   component that enters $p$, then $h$ is $h_{\bar\pi}$ and Step 11's comparison of
   $h''(\zeta_{\bar\pi})$ with $h''(0)$ compares two different functions. The exact form of Step 10
   is unaffected — it is a statement at one fixed $\bar\pi$ — but the $o(\bar\pi^{2})$ conclusion is
   not available.

6. **A($\tau$) holding only at a single $\kappa$.** The representation must hold on an open interval
   for Step 7's differentiation to be defined. A structure whose pooled law happens to be three-point
   symmetric at one value of $\kappa$ and not at neighbouring values supports no derivative statement.

---

## LABEL CLAIMED

**PROVED**, for CLAIM (i), (ii), (iii) and (iv), under Hypotheses 1–9 as listed — subject to the
lane's protocol, which is that the ledger entry stays **CONJECTURE** until an independent
re-derivation and a proof-read both pass. I have not touched the ledger.

*Why PROVED is the right claim for these four parts.* (i) is two applications of the mean value
theorem to explicitly named functions on explicitly named intervals, with the interval inclusions
verified by inequality at Step 5; nothing is approximated. (ii) is term-by-term differentiation of a
three-term finite sum plus one factorisation, carried out under Hypothesis 8's kernel restriction,
which is named rather than assumed silently. **Step 8′ is not offered as a second, independent
derivation of (ii), and must not be counted as one:** Step 8 consumes Hypothesis 2's three weight
restrictions, Step 8′ consumes $A_{1/2}'=-2A'_\kappa$ plus Hypothesis 6's two conservation laws, and
Step 14 proves those two input sets are **logically equivalent** — the routes share no *step*, but
they share their *content*. What Step 8′ genuinely adds is threefold and is claimed as that: it
displays the mechanism (the affine part of $h$ contributes no interior motion, and the whole motion is
carried by the mass of the single middle atom); it locates precisely where the three-point symmetry is
used (it is what collapses the chord-gap sum to one term); and it generalises to
$\partial_\kappa\mathbb E_\kappa[h]=\sum_iA_i'(h-\ell_h)(\pi_i)$, which is the form that transfers to
the multi-atom structure of Example B and hence to the frozen manuscript (Step 17), where Step 8's
clean proportionality does not. (iii) is a substitution plus a limit whose only ingredient beyond
(i) is the named extra regularity of Hypothesis 5. (iv) is arithmetic plus a counterexample that
rules out the converse.

**OPEN, and claimed as a result rather than a gap:** whether the two-round pooled cell of card §2
satisfies A($\tau$) (Step 18). The weakest sufficient condition is named there as (S1)–(S2), and the
reduction at Step 15 — that A($\tau$)'s derivative restrictions are implied by the model once the
support condition holds — narrows what has to be shown from three conditions to one.

**A card-reading finding requiring adjudication, not a claim:** Step 19's reading of $\bar\pi$. Under
the "mean of the pooled law" reading, L3 is true but vacuous; under Hypothesis 3's "top of the chord"
reading it has content. The frozen manuscript's structure supplies the second reading.

---

## NUMERICAL CHECK REQUEST

One script, five blocks, all executed at fixed policies. Kernel throughout:
$h(\pi)=\pi\,p(\pi)$ with $p(\pi)=1-\Phi\big((P(\pi)+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)$ (card
§4.3, §4.4), evaluated under the check's own convention $P(\pi)=m_0+\Delta_m\pi$ — a convention of
the check, not a model claim — at $m_0=0.10$, $\Delta_m=0.18$, $K=0.15$, $\bar S=1.44$,
$\sigma_\xi=0.40$.

**Block 1 — the derivative identity on Example A.** Weights $A_1=A_0=(2-\kappa)/4$,
$A_{1/2}=\kappa/2$, atoms $\{0,\tfrac12,1\}$, $\bar\pi=1$. Grid $\kappa\in\{0.05,0.10,\dots,0.95\}$.
Compare the central finite difference of $\mathbb E_\kappa[h]=A_0h(0)+A_{1/2}h(\tfrac12)+A_1h(1)$
(step $10^{-5}$) against $A'_\kappa C_h(1)$ with $A'_\kappa=-\tfrac14$.
*Predicted sign:* strictly positive, because $A'_\kappa=-\tfrac14<0$ and $C_h(1)<0$.
*Predicted magnitude:* $\partial_\kappa\mathbb E_\kappa[h]=+5.63\times10^{-3}$, constant across the
whole $\kappa$ grid, from $C_h(1)=h(1)-2h(\tfrac12)\approx0.9660-2(0.4943)=-2.25\times10^{-2}$.
*Acceptance:* pointwise residual below $10^{-10}$; range of
$\partial_\kappa\mathbb E_\kappa[h]$ across the $\kappa$ grid below $10^{-12}$, since Step 8 makes it
exactly constant when the weights are affine in $\kappa$.

**Block 2 — the mean-value form.** For each
$\bar\pi\in\{10^{-4},2\cdot10^{-4},5\cdot10^{-4},10^{-3},2\cdot10^{-3},5\cdot10^{-3},10^{-2},2\cdot10^{-2},5\cdot10^{-2},0.1,0.2,0.5,0.9,1.0\}$,
compute $C_h(\bar\pi)$ directly from the three evaluations and solve
$C_h(\bar\pi)=\tfrac14\bar\pi^{2}h''(\zeta)$ for $\zeta$ by bisection on $(0,\bar\pi)$ using the
closed-form $h''(\pi)=2p'(\pi)+\pi p''(\pi)$.
*Predicted sign:* $C_h<0$ and $h''(\zeta)<0$ at every grid point.
*Predicted magnitude:* a root $\zeta\in(0,\bar\pi)$ exists at every grid point, with
$\zeta/\bar\pi\to\tfrac12$ as $\bar\pi\downarrow0$.
*Acceptance:* $\lvert C_h(\bar\pi)-\tfrac14\bar\pi^{2}h''(\zeta)\rvert<10^{-14}$ at the returned root.

**Block 3 — the corollary and its rate.** On the same $\bar\pi$ grid, report
$C_h(\bar\pi)/\bar\pi^{2}$ and compare with $\tfrac14h''(0)=\tfrac12p'(0)$.
*Predicted sign:* negative throughout.
*Predicted magnitude:* $\tfrac14h''(0)\approx-4.38\times10^{-3}$; at $\bar\pi=10^{-2}$ this predicts
$C_h\approx-4.4\times10^{-7}$.
*Acceptance:* $\lvert C_h(\bar\pi)/\bar\pi^{2}\rvert$ differs between the two smallest $\bar\pi$
points by less than $5\%$, and the ratio to $\tfrac14h''(0)$ is within $2\%$ at
$\bar\pi\le10^{-3}$.

**Block 4 — the $C_h=0$ case, constructed rather than searched for.** Using Step 13(c), replace $h$
by the affine kernel $h(\pi)=c\pi$ with $c=0.5$, for which $C_h(\bar\pi)=0$ at every $\bar\pi$.
Recompute $\mathbb E_\kappa[h]$ on Example A across the $\kappa$ grid.
*Predicted sign:* none — the quantity is zero.
*Predicted magnitude:* $\partial_\kappa\mathbb E_\kappa[h]=0$ and the range of $\mathbb E_\kappa[h]$
across the whole $\kappa$ grid is $0$.
*Acceptance:* range below $10^{-14}$. A nonzero range refutes Step 8 or the weight algebra of
Step 16, not the kernel.

**Block 5 — the two failure witnesses, as refutation tests.** (a) Tent kernel of WHERE-IT-FAILS 2 at
$\bar\pi=1$: the script must report $C_h(1)=-1$ and **no** root $\zeta$ of
$C_h=\tfrac14h''(\zeta)$ on $(0,1)\setminus\{\tfrac12\}$, where $h''=0$. (b) Example B at
$\rho=0.5$: the script must report four distinct posteriors at every interior $\kappa$, with
$\pi_-$ strictly increasing and $\pi_+$ strictly decreasing in $\kappa$ on
$\{0.05,\dots,0.95\}$, and a nonzero gap between the directly computed
$\partial_\kappa\mathbb E_\kappa[h]$ and $A'_\kappa C_h(\bar\pi)$ for any scalar $A'_\kappa$ fitted to
the two end weights — confirming that A($\tau$) is a restriction with content and that the frozen
manuscript's own structure lies outside it.
*Predicted magnitude for (b):* at $\rho=0.5$, $\pi_-$ rises from near $0$ to $1$ and $\pi_+$ falls
from near $1$ to $0$ across $\kappa\in(0,1)$, so the moving-atom term is of the same order as the
weight term, not a rounding effect.

---

## NOTATION DELTA

Every symbol used above that is not in card §4, plus the one rename the card requires.

- **$C_h(\bar\pi)$ — a rename, not a new object.** $C_h(\bar\pi)=h(0)-2h(\bar\pi/2)+h(\bar\pi)$ is
  the card's §4.4 row and is character-for-character the chord second difference of the frozen
  manuscript, written there with a calligraphic C as $\mathcal C(\bar\pi)$ and carrying the maintained
  primitive condition labelled there with a starred C. $C_h$ inherits that object's history: the same
  three evaluation points, the same chord $[0,\bar\pi]$, the same role as the diagnostic for the
  interior motion of the no-disclosure block. The manuscript's calligraphic symbol is quoted here only
  to record the rename and is used nowhere as a live symbol. The card's rule that $C$ is overloaded is
  respected: the margin subscript is always written, and no bare $C$ appears.
- **$C_g(\bar\pi)$** — the same second difference applied to a generic function $g$ in Part I, so that
  Part I can be stated once and applied at Step 10. Subscripted, never bare.
- **$g$** — the generic function of Part I, reserved for the L3 mean-value form by the turn-2
  notation ruling. It never appears bare in a card sense: the card's $g_r^{PE}$ always carries both
  its subscript and its superscript, and it does not appear in this proof.
- **$\Delta_g$** — proof-local first-difference function, $\Delta_g(t)=g(t+\bar\pi/2)-g(t)$, defined
  at Step 2 and used only in Part I. Always carries the subscript $g$; no bare $\Delta$ appears, and
  the card's $\Delta_m,\Delta_V,\Delta^{\mathrm{act}},\Delta_{\kappa k},\Delta_{kr},\Delta_{kk},
  \Delta_k$ all carry their own distinct decorations.
- **$\zeta$, $\zeta_{\bar\pi}$** — the mean-value point of Step 5, and its value when Part I is
  applied to $h$ at chord width $\bar\pi$ (Step 10). Free in the card.
- **$t$, $t_1$** — running variable and first mean-value point in Part I. Not the signal, which is
  $s$; $s$ is not used as a running variable anywhere in this proof.
- **$\ell_h$** — the affine interpolant of $h$ on $[0,\bar\pi]$ with $\ell_h(0)=h(0)$,
  $\ell_h(\bar\pi)=h(\bar\pi)$, used at Step 8′ and Step 17. Subscripted; the card's $L_{\mathcal R}$
  is capital and distinct.
- **$\mathcal K$** — the open interval of $\kappa$ on which A($\tau$) is maintained and Step 7
  differentiates. Free in the card; the card's $K$ is the bidder entry cost, upright and capital.
- **$\rho$** — the pre-order engagement share $\Pr(a=1)$ of the block under discussion, which is the
  **mean** of the pooled posterior law and is distinct from $\bar\pi$, the top of its support (Step 19).
  Free in the card.
- **$\mathrm{m}(\kappa)$, $\mathrm{r}(\kappa)$** — the pooled block's total mass and its unnormalised
  engagement moment, Step 14. Upright, to keep them clear of $m_0,m_1$ (premia) and of $r_\tau,r_T$
  (strictness coordinates).
- **$\pi_i$, $\pi_-$, $\pi_+$** — support points of a posterior law; $\pi_\pm$ specifically the two
  interior atoms of Example B (Step 17). The card's $\pi(\mathcal I)$ is the posterior map, and these
  are values it takes, which is the card's own usage in the §4.4 chord row.
- **$\mathbb E_\kappa[h]$** — the pooled block's expectation of $h$ at noise-trading intensity
  $\kappa$, under whichever of Hypothesis 3's two normalisations is in force.
- **$\delta$** — the radius of the right-neighbourhood of $0$ in Hypothesis 5. Free in the card.
- **$\alpha$, $c$** — the two constants of the Example A′ weight family (Step 16). Proof-local.
- **Reading of $h$ as a function of a number.** $h$ is used as a function of the posterior *value*
  $\pi\in[0,1]$, $h(\pi)=\pi p(\pi)$. Card §4.4 already evaluates $h$ at the three numbers $0$,
  $\bar\pi/2$ and $\bar\pi$ in the $C_h$ row, so the *notation* is the card's; the *content* — that
  $h$ does not also move with the price at a fixed posterior — is **Hypothesis 8**, a named
  restriction, not a reading. Card gap, regeneration item.
- **Asymptotic notation.** Only small-$o$ is used, in the card's own sense ($f=o(\bar\pi^2)$ means
  $f/\bar\pi^2\to0$ as $\bar\pi\downarrow0$); exact orders are written in words ("of exact order
  $\bar\pi^{3/2}$", WHERE-IT-FAILS 3). **No Landau $\Theta$ or $O$ appears**: $\Theta$ is the card
  §4.5 compact ordered cutoff polytope and card §8 rule 4 forbids re-keying it, so it is never used
  as a growth-rate symbol in this file.

Card rules observed: no bare $C$, no bare $W$, no bare $\mathsf S$, no bare $u$, no bare $\lambda$;
$\kappa$ is noise-trading intensity throughout with no drift toward depth, volume or turnover;
$A'_\kappa$ never written $a_\kappa$; $\Gamma$ used for the order-mark coarsening and $\psi$ nowhere;
neither the upright window $T$ nor the best-response map $\mathcal T$ appears in this proof, and the
manuscript's signal-leverage object of the same shape is not used.

---

## NOT CLAIMED

1. **Not claimed: that the two-round pooled cell satisfies A($\tau$).** Declared OPEN at Step 18, with
   (S1)–(S2) named as the weakest sufficient condition I could find. I claim only that the derivative
   restrictions reduce to the support condition (Step 15), which narrows the question rather than
   answering it.
2. **Not claimed: any sign for $C_h(\bar\pi)$.** The card maintains $C_h\le0$ as an orientation, and
   this proof uses that orientation nowhere. Every statement above is sign-free in $C_h$: the
   proportionality of Step 8, the vanishing of Step 12, and the zero case of Step 13 all hold for
   $C_h$ of either sign or zero.
3. **Not claimed: an equivalence.** Zero interior motion does not imply $C_h=0$; Step 13(a) exhibits
   the counterexample. Nothing here should be restated with "iff".
4. **Not claimed: monotonicity of $\lvert C_h\rvert$ in $\bar\pi$.** The card maintains it in §4.4 and
   L4 consumes it. This proof neither uses it nor derives it. Whether it is derivable from Step 10 —
   which would need a sign and a monotonicity for $h''$ across the chord — is untouched here.
5. **Not claimed: anything about the flagged cell.** Step 9's use of card §4.4's relation
   $\mathcal S=(1-\Omega)\mathcal S_P$ cites L2 as a card ID for the flagged block's
   $\kappa$-invariance; no part of L2 is re-proved or strengthened.
6. **Not claimed: that $\Delta^{\mathrm{act}}$ is hump-shaped in $\kappa$**, that the frozen
   manuscript's hump survives, or anything about the general-equilibrium cutoff-shift channel. This is
   a fixed-policy statement about one block's interior derivative.
7. **Not claimed: that Example A is the model.** It is a witness that A($\tau$)'s class is nonempty
   and that it is nonempty **inside the card's own primitives**. It has $\bar\pi=1$, so it cannot
   itself carry the $\bar\pi\downarrow0$ limit; Example A′ carries that and is an abstract experiment.
8. **Not claimed: uniqueness of $\zeta$.** The mean value theorem asserts existence. Step 10's
   $\zeta_{\bar\pi}$ is one such point, and the corollary at Step 11 needs only that every choice lies
   in $(0,\bar\pi)$.
9. **Not claimed: a label change.** The card ledger is untouched. L3 stays CONJECTURE until an
   independent re-derivation and a proof-read both pass.

---

## Repairs applied (2026-08-21, batch-1 audit)

Source: `threads/2026-08-21_batch1_proofread_audit.md` (Opus proof-read, verdict PASS, no failing
steps). Every change below is a citation, a hypothesis lift, a wording fix or a notation
declaration. **No claim, hypothesis or step conclusion was altered in substance, and no step was
renumbered.** The label is untouched: L3 remains CONJECTURE.

| Finding | Change made |
|---|---|
| **L3-R1** | Added **Hypothesis 8** — the kernel depends on the control-node information set only through the engagement posterior — as a numbered [ADDITION], cited at Step 7 where it is consumed, with the extra term it excludes written out and the "card gap, regeneration item" flag on A($\tau$) recorded in the hypothesis and in the NOTATION DELTA. |
| **L3-R2** | LABEL CLAIMED reworded: the "two derivations that do not share a step" ground for (ii) is withdrawn (Step 14 proves the two input sets equivalent); Step 8′ is now claimed for what it adds — the mechanism, the location of the three-point symmetry, and the multi-atom form that transfers to Example B. |
| **L3-R3** | WHERE-IT-FAILS 3's Landau "$\Theta(\bar\pi^{3/2})$" replaced by "of exact order $\bar\pi^{3/2}$"; NOTATION DELTA now declares the asymptotic convention and records that $\Theta$ is the card §4.5 polytope and never a growth rate. |
| **L3-R4(a)** | Hypothesis-use table corrected: Hypothesis 1 now reads "Steps 7, 8′, 14; Step 12 consumes it only through Step 8"; Hypothesis 6 now lists Step 8′. |
| **L3-R4(b)** | **Hypothesis 9** added — D1 by its card-ledger statement — and Hypothesis 6's parenthetical now cites it instead of naming D1 inline, so D1's CONJECTURE status propagates visibly into L3. |
| **L3-R5** | Step 12's "under continuity alone" sentence now cites Hypothesis 5's first clause (one and the same $h$ across the shrinking family) alongside the continuity of $h$ at $0$. |
| **Notation scan** | NOTATION DELTA completed: asymptotic convention declared; the $h$-as-a-function-of-a-number bullet now points at Hypothesis 8 rather than calling the restriction "the card's own reading". |

Not applied here, by scope: L3-O1 … L3-O4 are OBSERVATIONs, not REPAIRs. L3-O4's recommendation
(the card should pin $A'_\kappa$ to the conditional normalisation) is a card edit and belongs to the
orchestrator's regeneration list, not to this file.

### FILE: proofs/L4_proof.md

# L4 — Threshold composition lemma (full proof)

**Card version stamp acted on: 2026-08-20 · commit `0c9185b`.** Ticket 22 (T2b). Written against
`research/model_v4/MODEL_CARD.md` §4 (notation), §5 (hypotheses), §8 (answer template), the turn-3
instruction `threads/thread1_msg3.md` §3 "L4", and the turn-1 statement
`threads/thread1_turn1_answer.md` §L4. D1 is cited **by its card-ledger statement only**. L3 is cited
by its card-ledger statement only **with one declared exception**: (br-iv) and Step 14 cite **L3's
Step 19** directly, by orchestrator adjudication of 2026-08-21 (batch-1 audit finding L4-R1), because
that step is what excludes one of the two $\bar\pi$ readings this file used to carry. That is the only
place in this file where L3's proof, rather than its ledger statement, is read.

---

## VERDICT UP FRONT — L4 is *not* provable as stated from the card alone

The three legs do not carry the same burden, and the card's own row hides that.

* **Leg 1 (a lower $\tau$ weakly raises $\Omega$) — proved outright.** No hypothesis beyond D1's
  clock equivalence, the §2 no-feedback timing, fixed policies, the maintained core restriction
  $b_0 < \tau$ imposed at *both* compared thresholds, and A1. No chord machinery is used.
* **Leg 2 (a lower $\tau$ weakly lowers the pooled engagement share) — proved outright,** on the same
  hypotheses plus $\Omega(\tau') < 1$. In particular the two "nestedness" hypotheses the turn-1
  statement carried are **not** hypotheses: they are conclusions (Steps 5 and 9), and they are
  deleted from the hypothesis list below with the deletion recorded.
* **Leg 3 (a lower $\tau$ weakly lowers $\mathcal S_P$) — carries the entire assumption burden,** and
  needs an extra hypothesis the card does not contain. L3's statement delivers a *chord proxy* for
  the pooled cell's **interior** $\kappa$-motion; $\mathcal S_P$ is defined in card §4.4 as
  $\lvert\partial_\kappa M_P\rvert$, the **total** $\kappa$-derivative of the pooled conditional mean,
  and the two are the same object only under conditions nobody has written down.

**The weakest extra hypothesis I could find, named here at the top:**

> **A(br) — Chord–sensitivity bridge.** For the two compared thresholds $\tau' < \tau$ at fixed
> policies:
>
> * **(br-i) Representation at both policies.** A($\tau$)'s symmetric ternary representation holds
>   for the pooled class under $\tau$ *and* under $\tau'$, with chord endpoints $\bar\pi(\tau)$,
>   $\bar\pi(\tau')$ and weight-derivative coefficients $A'_\kappa(\tau)$, $A'_\kappa(\tau')$.
> * **(br-ii) $\kappa$-localisation.** At fixed policies all $\kappa$-dependence of $M_P$ sits in the
>   A($\tau$) weights: the three support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$ *as a
>   function of the posterior* do not move with $\kappa$. Hence
>   $\partial_\kappa M_P = \Delta_m A'_\kappa C_h(\bar\pi)$ exactly, with no
>   composition-through-$\kappa$ remainder.
>   **What (br-ii) buys, stated exactly.** Read against the card's *literal* A($\tau$) display — in
>   which $\bar\pi$ and $h$ carry no $\kappa$ argument — (br-i) already localises every
>   $\kappa$-dependence in the weights and (br-ii) would be a restatement. (br-ii) is not written
>   against that reading. It is written against the **honest** one: in the model
>   $h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$ and card §4.3's entry row makes $p$ depend on the
>   price as well as on $\pi$, so $h=\pi\,p(\hat v,\pi)$ is a function of **two** scalars. "$h$ as a
>   function of the posterior is $\kappa$-free" is therefore real content that A($\tau$)'s notation
>   hides, and (br-ii) is the clause that repairs that card ambiguity rather than a fourth
>   independent restriction. L3's Hypothesis 8 names the same object and prices it the same way.
> * **(br-iii) Coefficient stability across the threshold margin.**
>   $\lvert A'_\kappa(\tau')\rvert \le \lvert A'_\kappa(\tau)\rvert$. Weakest sufficient form:
>   equality — reclassification changes *which* histories are pooled, not the $\kappa$-responsiveness
>   of the pooled weights.
> * **(br-iv) Endpoint linkage.** $\bar\pi$ is A($\tau$)'s chord endpoint — the **upper support
>   point** of the pooled posterior law — and it is a weakly increasing function of the pooled prior
>   engagement share $\bar\pi_{\mathrm{pr}} = \Pr(a=1\mid D=0)$, **the same function at $\tau$ and at
>   $\tau'$**.

**The $\bar\pi$ ruling (orchestrator adjudication, 2026-08-21, batch-1 audit L4-R1 — binding).**
$\bar\pi$ is the **upper support point** of the pooled posterior law in A($\tau$). The pooled
engagement share is the *mean* $\mathbb E[\Pi_\kappa]$, which is strictly below $\bar\pi$ in any
non-degenerate case. Card §4.4's gloss — "pre-order pooled engagement share in the chord" — is the
wording that generated the confusion and is flagged for adjudication at the card's next regeneration;
it must not be read as "$\bar\pi$ is the mean".

An earlier draft of this file offered two readings and declared them interchangeable. **The identity
branch — $\bar\pi = \bar\pi_{\mathrm{pr}}$, i.e. $\bar\pi$ read as the mean of the pooled law — is now
EXCLUDED**, on L3's Step 19 (cited directly per the exception declared at the head of this file): with
support $\{0,\bar\pi/2,\bar\pi\}$, conditional weights summing to $1$ and mean equal to $\bar\pi$, the
moment equation forces $A_0 = A_1 - 1 \le 0$, hence $A_0=0$, $A_1=1$, $A_{1/2}=0$ — a point mass at
$\bar\pi$ with $A'_\kappa = 0$ and zero interior motion for **every** kernel. Under that branch
$\mathcal S_P(\tau)=\mathcal S_P(\tau')=0$ identically, so leg 3 would hold only because both sides
vanish. A mean cannot equal the maximum of its own support unless the law is degenerate.

What survives is the non-degenerate reading, and (br-iv) is now stated only for it. Under the
level-symmetric reading $A_0 = A_1$ — which A($\tau$) does not state, it states only $A_0' = A_1'$ —
the martingale property of Bayesian posteriors gives
$\mathbb E[\Pi_\kappa] = A_{1/2}\bar\pi/2 + A_1\bar\pi = \bar\pi/2$, i.e.
$\bar\pi = 2\bar\pi_{\mathrm{pr}}$: the support point is twice the pooled share, which is exactly the
strict gap the ruling requires. L3's Example A instantiates it ($\bar\pi=1$, pooled share
$\tfrac12$). All (br-iv) itself needs, and all leg 3 consumes, is that the map
$\bar\pi_{\mathrm{pr}}\mapsto\bar\pi$ is weakly increasing and is the same map at both thresholds.
A side consequence worth recording: under the factor-two form, $\bar\pi \le 1$ forces
$\bar\pi_{\mathrm{pr}} \le 1/2$, which is a restriction on A($\tau$)'s domain that L4 inherits and
does not resolve.

Label is unchanged: **CONJECTURE**. The ledger is not touched.

---

## CLAIM

Fix the plan menu $\mathcal J$, the engagement labels $a_j$, the execution paths $B_j(s,\cdot)$ and
the cutoff vector $k$ — that is, hold policies fixed — and fix the window $T$. Let
$b_0 < \tau' < \tau$ and suppose $\Omega(\tau',T) < 1$. Then:

1. $\mathcal C_F(\tau,T) \subseteq \mathcal C_F(\tau',T)$, and every history in the difference
   $\mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T)$ is generated by a Voice plan;
2. $\Omega(\tau',T) \ge \Omega(\tau,T)$;
3. $\bar\pi_{\mathrm{pr}}(\tau') \le \bar\pi_{\mathrm{pr}}(\tau)$, with the exact identity
   $\bar\pi_{\mathrm{pr}}(\tau) - \bar\pi_{\mathrm{pr}}(\tau')
   = \frac{\nu}{\rho_P}\bigl(1 - \bar\pi_{\mathrm{pr}}(\tau')\bigr)$
   where $\nu = \Omega(\tau') - \Omega(\tau)$ and $\rho_P = 1-\Omega(\tau)$;
4. and, **under L3's statement, A($\tau$)'s maintained monotone $\lvert C_h\rvert$, and A(br)**,
   $\mathcal S_P(\tau',T) \le \mathcal S_P(\tau,T)$, with equality whenever
   $C_h(\bar\pi(\tau)) = 0$.

**Leg numbering, fixed once for the whole file** (batch-1 audit L4-R5; the file previously ran two
schemes). The three *legs* are the three results named in the VERDICT and in the Part headings:
**leg 1** = the $\Omega$ result (CLAIM item 2, Part II), **leg 2** = the $\bar\pi_{\mathrm{pr}}$
result (CLAIM item 3, Part III), **leg 3** = the $\mathcal S_P$ result (CLAIM item 4, Part IV).
CLAIM item 1 is the nested-reclassification inclusion of Part I, which is an input to legs 1 and 2
rather than a leg of its own. There is no "leg 4". Legs 1 and 2, and item 1, are unconditional given
the hypotheses below; **leg 3 alone is conditional on A(br)**.

---

## HYPOTHESES

Each is used at the step named. Nothing is carried that is not used.

1. **Fixed policies.** $\mathcal J$, the labels $a_j$, the execution paths $B_j(s,\cdot)$ and the
   cutoff vector $k$ (hence the selection map $j(s)$) are identical at $\tau$ and $\tau'$; the
   blockholder does not re-optimise when the threshold moves. *(Used: Steps 1, 5.)*
2. **No-feedback timing** (card §2, Round 1 bullet). $B_j(s,d)$, $q_{jd}(s)$ and $Q_j^F$ are
   functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone; there is no within-window re-optimisation and no
   dependence of the stake path on realised order flow or prices. *(Used: Steps 2, 4, 21.)*
3. **D1, clock-equivalence clause, by its card-ledger statement.** For every Voice plan,
   $f_j \le H \iff B_j(s,H-T) \ge \tau$. *(Used: Step 3.)*
4. **Core domain at both thresholds: $b_0 < \tau' < \tau$.** Card §4.2 maintains $b_0 < \tau$; a
   pre-existing crossing is outside the core (turn-2 audit ruling D1-O1). Because the comparison
   moves the threshold, the restriction must be imposed at the *tighter* threshold too, otherwise
   D1's equivalence is being cited off its domain at $\tau'$. *(Used: Step 3.)*
5. **A1 Independent primitives.** The joint law of $(v,\varepsilon,\xi,z_{0:H})$ is a primitive; it
   does not depend on the policy pair $(\tau,T)$, and $\kappa$ enters only the law of $z_{0:H}$,
   which is independent of $(v,\varepsilon,\xi)$. *(Used: Steps 7, 21.)*
6. **A4 Legal-clock discipline.** $c$ is the first date the path reaches $\tau$; the filing lands
   exactly at $c+T$, not earlier and not later; only Voice plans cross in the core. *(Used: Step 3 —
   this is what rules out the early/strategic-filing counterexample in WHERE IT FAILS case 3.)*
7. **Card §4.2's disclosure restriction $D=1 \Rightarrow a=1$.** *(Used: Step 9 — the step that
   consumes "every newly flagged history is Voice".)*
8. **A8 at the tighter threshold: $\Omega(\tau',T) < 1$** (which by **leg 1** — Step 7's
   $\Omega(\tau,T)\le\Omega(\tau',T)$ — also gives $\Omega(\tau,T) < 1$). *(Used: Steps 10, 11.)*
9. **L3, by its card-ledger statement.** Under A($\tau$) the pooled cell's interior $\kappa$-motion
   is proportional to $C_h(\bar\pi)$, and $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, so it
   vanishes as $\bar\pi \downarrow 0$. L3's *proof* is not read and not relied on. *(Used: Step 15.)*
10. **A($\tau$)'s maintained orientation: $C_h(\bar\pi)\le 0$ with $\lvert C_h(\bar\pi)\rvert$ weakly
    increasing in $\bar\pi$.** This is **used as the card's maintained hypothesis, not derived** —
    msg3 asked which it was, and the answer is: maintained. Nothing below attempts to establish it.
    *(Used: Steps 17, 20.)*
11. **A(br), the chord–sensitivity bridge**, clauses (br-i)–(br-iv) as stated at the top. This is the
    named extra hypothesis. *(Used: Steps 14, 16, 18.)*

### Hypotheses deleted from the turn-1 statement, with reasons (recorded in-file as instructed)

* **Turn-1 H1, "threshold reclassification is nested:
  $\tau'<\tau \Rightarrow \mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T)$" — DELETED.** It is the
  conclusion of Step 5, derived from D1's clock equivalence plus fixed policies. Carrying it as a
  hypothesis would assume the first leg of the lemma.
* **Turn-1 H2, "every history newly moved to the flagged cell is generated by a Voice plan" —
  DELETED.** It is the conclusion of Step 9, derived from card §4.2's $D=1 \Rightarrow a=1$ (which
  is a definitional property of the disclosure indicator, since the indicator carries the conjunct
  $a_j=1$). The *content* survives as a proved step and is consumed at Step 11; only its status as an
  assumption is deleted.
* **Turn-1 H3, "passive histories are not moved into the flagged cell" — DELETED, twice over.** It is
  the contrapositive of H2 restricted to $a=0$, so it is redundant given H2; and like H2 it is
  derived at Step 9 rather than assumed.
* **Turn-1 H4 ("preselected execution policies and signal cutoffs held fixed") is retained** as
  Hypothesis 1, and sharpened: the card's §4.2 notation already writes $B_j(s,d)$ with *no* $\tau$
  argument, so path-fixity is half built into the notation; the substantive half is that the cutoff
  vector $k$, hence the selection map $j(s)$, does not respond to $\tau$.
* **Turn-1 H5 ("L3 applies") is retained** as Hypothesis 9, restricted to L3's *statement*.
* **Turn-1 H6 ("$\lvert C_h\rvert$ weakly increasing") is retained** as Hypothesis 10, with its
  status declared: maintained, not derived.

---

## PROOF

### Part 0 — Setup

**Step 1.** By Hypothesis 1 the selection map $j(s)$ — the plan the frozen cutoff vector $k$ assigns
to signal $s$ — and the path family $B_j(s,\cdot)$ are the same objects at $\tau$ and at $\tau'$.
Card §4.2 writes the stake path as $B_j(s,d)$, carrying no $\tau$ argument, whereas $c_j(s;\tau)$,
$f_j$, $B_j^F$ and $D_j(s;\tau,T)$ all carry one. Therefore, in the comparison below, the *only*
objects that move when the threshold moves from $\tau$ to $\tau'$ are the crossing date, the filing
date, the stake at filing, and the disclosure indicator. The path itself is common to the two
environments.

**Step 2.** By Hypothesis 2, $B_j(s,d)$ is a function of $(j,s,d)$ alone. Composing with Step 1's
fixed selection map, the map $d \mapsto B_{j(s)}(s,d)$ is a function of $s$ and $d$ alone: it does
not depend on the noise draw $z_{0:H}$, on the realised pooled order flow $(X_0,\dots,X_H)$, on the
pooled prices $P_d^P$, or on $\kappa$.

**Step 3 (product form of the disclosure indicator).** For every plan $j \in \mathcal J$, every
signal $s$, and each of the two thresholds,
$$D_j(s;\tau,T) \;=\; \mathbf 1\{a_j = 1\}\cdot\mathbf 1\{B_j(s,H-T)\ge\tau\}.$$
Two cases, both written out.

*Case $a_j = 0$.* Card §4.2 defines $D_j(s;\tau,T)=\mathbf 1\{a_j=1,\ c_j<\infty,\ f_j\le H\}$. The
first conjunct fails, so the left side is $0$. On the right side the first factor is $0$, so the
product is $0$. The two sides agree.

*Case $a_j = 1$ (a Voice plan).* The left side reduces to
$\mathbf 1\{c_j<\infty,\ f_j\le H\}$. I first remove the conjunct $c_j<\infty$ as redundant: card
§4.2 sets $f_j = c_j + T$ with $T \in \{1,\dots,H\}$, hence $T$ finite, so $f_j \le H$ implies
$c_j = f_j - T \le H - T < \infty$; and conversely $\{c_j<\infty, f_j\le H\} \subseteq \{f_j\le H\}$
by set inclusion. Therefore $\{c_j<\infty,\ f_j\le H\} = \{f_j\le H\}$ as events. Now Hypothesis 3
(D1's clock-equivalence clause, quoted verbatim from the card ledger: *for every Voice plan
$f_j\le H \iff B_j(s,H-T)\ge\tau$*) converts $\{f_j\le H\}$ into $\{B_j(s,H-T)\ge\tau\}$. Hypothesis 4
puts the comparison inside D1's stated domain — the core, on which $b_0 < \tau$ holds — at both
thresholds, and Hypothesis 6 (A4) is what makes $c_j$ the *first* passage and pins the filing to
land exactly at $c_j+T$, which is what D1's equivalence is an equivalence about. The two sides
agree.

**Step 4.** Combining Steps 1–3, at fixed policies the disclosure indicator evaluated along the
selected plan is
$$D(s;\tau,T) \;=\; \mathbf 1\{a_{j(s)}=1\}\cdot\mathbf 1\{B_{j(s)}(s,H-T)\ge\tau\},$$
a function of the signal $s$ alone. It is measurable in $s$ (D1's measurability clause; and directly,
as a product of two indicators of preimages of half-lines under the fixed maps $s\mapsto a_{j(s)}$
and $s\mapsto B_{j(s)}(s,H-T)$). It does not depend on $z_{0:H}$ and it does not depend on $\kappa$.

### Part I — Nested reclassification

**Step 5 (the inclusion).** Fix any control-node history $(j,s,z_{0:H})$ with $D_j(s;\tau,T)=1$. By
Step 3 this means $a_j=1$ and $B_j(s,H-T)\ge\tau$. Since $\tau' < \tau$, the real-number inequality
$B_j(s,H-T)\ge\tau > \tau'$ gives $B_j(s,H-T)\ge\tau'$. The *same* number $B_j(s,H-T)$ appears in both
comparisons — this is exactly where Hypothesis 1 (fixed policies) and Step 1 are consumed: without
path-fixity, the left-hand side of the $\tau'$ comparison would be a different path's stake and the
implication would not go through. Applying Step 3 at $\tau'$ to the same $(j,s)$ therefore gives
$D_j(s;\tau',T)=1$. Since the history was arbitrary, and since the flagged cell is
$\mathcal C_F(\tau,T) = \{(j,s,z_{0:H}) : D_j(s;\tau,T)=1\}$ — card §4.3's $\mathcal C_F/\mathcal C_P$
row (the two cells are exclusive and exhaustive by construction) read together with card §4.2's
$D_j(s;\tau,T)$ row, which is where the indicator is defined; **the card has no §2.5**, and the
§2.5 that carries this display is a section of `threads/thread1_turn1_answer.md`, not of the card —
$$\mathcal C_F(\tau,T)\;\subseteq\;\mathcal C_F(\tau',T).$$

*Remark on the citation (not part of the proof).* Step 5 uses D1's equivalence only to convert a
statement about the filing date into a statement about a stake level. If the card's Voice-path
monotonicity $\partial_d B_j\ge 0$ (§4.2) were dropped, D1's equivalence would have to be restated as
$f_j\le H \iff \max_{d\le H-T} B_j(s,d)\ge\tau$, and the inclusion above would still go through
verbatim with $\max_{d\le H-T}B_j(s,d)$ in place of $B_j(s,H-T)$, because the argument uses only that
one $s$-measurable number is compared to two thresholds. The nestedness conclusion is therefore
robust to path non-monotonicity even though the cited form of D1 is not.

**Step 6.** Card §4.3 records that $\mathcal C_F$ and $\mathcal C_P$ are exclusive and exhaustive by
construction. Taking complements in Step 5,
$\mathcal C_P(\tau',T)\subseteq\mathcal C_P(\tau,T)$: tightening the threshold can only shrink the
pooled cell.

### Part II — Leg 1: a lower $\tau$ weakly raises $\Omega$

**Step 7.** By Hypothesis 5 (A1) the probability measure over $(v,\varepsilon,\xi,z_{0:H})$ is a
primitive and does not depend on $\tau$; the threshold enters only through the event $\{D=1\}$.
Monotonicity of a probability measure applied to Step 5's inclusion gives
$$\Omega(\tau',T)=\Pr\bigl(\mathcal C_F(\tau',T)\bigr)\;\ge\;\Pr\bigl(\mathcal C_F(\tau,T)\bigr)=\Omega(\tau,T).$$
This is leg 1. Note also, from Step 4, that $\Omega$ is a function of the law of $s$ and the frozen
policy alone, so at fixed policies $\partial_\kappa\Omega = 0$; this is used at Step 21 and is the
sharpest item in the numerical check.

### Part III — Leg 2: a lower $\tau$ weakly lowers the pooled engagement share

**Step 8.** Define the **newly flagged set** and its mass,
$$\mathcal N \;:=\; \mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T)
\;=\;\mathcal C_P(\tau,T)\setminus\mathcal C_P(\tau',T),
\qquad \nu:=\Pr(\mathcal N).$$
The second equality is Steps 5 and 6 together with exhaustiveness (card §4.3). Because
$\mathcal C_F(\tau,T)$ and $\mathcal N$ are disjoint with union $\mathcal C_F(\tau',T)$, finite
additivity gives $\nu = \Omega(\tau')-\Omega(\tau)\ge 0$, the inequality by Step 7. The same
decomposition read on the pooled side is the disjoint union
$$\mathcal C_P(\tau,T)\;=\;\mathcal C_P(\tau',T)\;\uplus\;\mathcal N .$$

**Step 9 — this is the step that consumes "every newly flagged history is Voice."** Every history in
$\mathcal N$ satisfies $D(\tau')=1$ by the definition of $\mathcal N$ in Step 8. Hypothesis 7 — card
§4.2's recorded restriction $D=1\Rightarrow a=1$, which holds because the disclosure indicator
carries $a_j=1$ as a conjunct — gives $a=1$ at every such history. Hence the engagement indicator is
identically $1$ on $\mathcal N$, and whenever $\nu>0$,
$$\Pr(a=1\mid\mathcal N)\;=\;1 .$$
This is a derived fact, not an assumption; that is why turn-1's H2 and H3 are deleted above. It is
consumed at Step 11 and its force is analysed at Step 13.

**Step 10 (well-definedness).** Hypothesis 8 gives $\Omega(\tau')<1$, so
$\Pr(\mathcal C_P(\tau',T)) = 1-\Omega(\tau')>0$. By Step 7, $\Omega(\tau)\le\Omega(\tau')<1$, so
$\rho_P:=\Pr(\mathcal C_P(\tau,T))=1-\Omega(\tau)>0$ as well. Both conditional shares
$$\bar\pi_{\mathrm{pr}}(\tau):=\Pr\bigl(a=1\mid D(\tau)=0\bigr),\qquad
\bar\pi_{\mathrm{pr}}(\tau'):=\Pr\bigl(a=1\mid D(\tau')=0\bigr)$$
are therefore defined. If instead $\Omega(\tau')=1$ the pooled cell at $\tau'$ is null and
$\bar\pi_{\mathrm{pr}}(\tau')$ is **undefined rather than imputed** — the same treatment L1's ledger
statement gives the null cell. This is failure case 5 below.

**Step 11 (the conditional-probability arithmetic).** Apply finite additivity to the event
$\{a=1\}\cap\mathcal C_P(\tau,T)$ along Step 8's disjoint union:
$$\Pr\bigl(\{a=1\}\cap\mathcal C_P(\tau,T)\bigr)
=\Pr\bigl(\{a=1\}\cap\mathcal C_P(\tau',T)\bigr)+\Pr\bigl(\{a=1\}\cap\mathcal N\bigr).$$
The first right-hand term is $\bar\pi_{\mathrm{pr}}(\tau')\bigl(\rho_P-\nu\bigr)$, using
$\Pr(\mathcal C_P(\tau',T)) = \rho_P-\nu$ from Steps 8 and 10. The second is $\nu\cdot 1$ **by
Step 9** — this is the point of consumption. The left-hand term is
$\bar\pi_{\mathrm{pr}}(\tau)\,\rho_P$. Dividing through by $\rho_P>0$ (Step 10):
$$\boxed{\;\bar\pi_{\mathrm{pr}}(\tau)\;=\;\Bigl(1-\tfrac{\nu}{\rho_P}\Bigr)\,\bar\pi_{\mathrm{pr}}(\tau')\;+\;\tfrac{\nu}{\rho_P}\cdot 1\;}$$

**Step 12 (leg 2).** By Step 8, $\mathcal N\subseteq\mathcal C_P(\tau,T)$, so
$0\le\nu\le\rho_P$ and the weight $\nu/\rho_P$ lies in $[0,1]$ (Step 10 gives $\rho_P>0$, so the
ratio is defined). Step 11 therefore exhibits $\bar\pi_{\mathrm{pr}}(\tau)$ as a convex combination
of $\bar\pi_{\mathrm{pr}}(\tau')$ and $1$. Rearranging Step 11,
$$\bar\pi_{\mathrm{pr}}(\tau)-\bar\pi_{\mathrm{pr}}(\tau')
=\frac{\nu}{\rho_P}\Bigl(1-\bar\pi_{\mathrm{pr}}(\tau')\Bigr)\;\ge\;0,$$
because $\nu\ge 0$, $\rho_P>0$, and $\bar\pi_{\mathrm{pr}}(\tau')\le 1$ since it is a conditional
probability. Hence $\bar\pi_{\mathrm{pr}}(\tau')\le\bar\pi_{\mathrm{pr}}(\tau)$. An equivalent
closed form, obtained by solving Step 11 for $\bar\pi_{\mathrm{pr}}(\tau')$ when $\rho_P>\nu$, is
$\bar\pi_{\mathrm{pr}}(\tau')=\bigl(\rho_P\bar\pi_{\mathrm{pr}}(\tau)-\nu\bigr)/(\rho_P-\nu)$, from
which the same difference reads
$\nu\bigl(1-\bar\pi_{\mathrm{pr}}(\tau)\bigr)/(\rho_P-\nu)\ge0$. This is leg 2.

**Step 13 (why engagement share $1$ delivers the inequality unconditionally).** Suppose Step 9 were
weakened, so that the newly flagged set had some engagement share
$\Pr(a=1\mid\mathcal N)\in[0,1]$ rather than exactly $1$. Step 11's arithmetic is unchanged except
that the last term becomes $\tfrac{\nu}{\rho_P}\Pr(a=1\mid\mathcal N)$, and Step 12 becomes
$$\bar\pi_{\mathrm{pr}}(\tau)-\bar\pi_{\mathrm{pr}}(\tau')
=\frac{\nu}{\rho_P}\Bigl(\Pr(a=1\mid\mathcal N)-\bar\pi_{\mathrm{pr}}(\tau')\Bigr),$$
whose sign is the sign of $\Pr(a=1\mid\mathcal N)-\bar\pi_{\mathrm{pr}}(\tau')$. The conclusion would
then be a *conditional* one, requiring the newly flagged histories to be at least as
engagement-intensive as the pool they leave — an assumption about **which** histories move, which is
precisely the kind of assumption this lane exists to refuse. Step 9 supplies
$\Pr(a=1\mid\mathcal N)=1$, and $1$ is the maximum value a conditional probability can take, so
$\Pr(a=1\mid\mathcal N)\ge\bar\pi_{\mathrm{pr}}(\tau')$ holds for **every** admissible value of
$\bar\pi_{\mathrm{pr}}(\tau')\in[0,1]$ with no further restriction whatever. That is the exact sense
in which "every newly flagged history is Voice" delivers leg 2 unconditionally. Two corollaries:
the inequality is an equality if and only if $\nu=0$ (no mass reclassified) or
$\bar\pi_{\mathrm{pr}}(\tau')=1$ (the tighter pool is already all-Voice); and no strict inequality is
available without assuming $\nu>0$, which the card does not supply and which this proof does not
claim.

**Step 14 (transfer to A($\tau$)'s chord endpoint).** Step 12 is a statement about the pooled prior
engagement share $\bar\pi_{\mathrm{pr}}$. A($\tau$)'s chord is written in the endpoint $\bar\pi$.
Hypothesis 11, clause (br-iv), says $\bar\pi$ — the **upper support point** of the pooled posterior
law — is a weakly increasing function of $\bar\pi_{\mathrm{pr}}$, the same function at both
thresholds. Applying that function to Step 12,
$$\bar\pi(\tau')\;\le\;\bar\pi(\tau).$$
Under the level-symmetric reading $A_0=A_1$ the function is $\bar\pi=2\bar\pi_{\mathrm{pr}}$, and the
pooled share $\mathbb E[\Pi_\kappa]=\bar\pi/2$ sits strictly below the support point. **The identity
map $\bar\pi=\bar\pi_{\mathrm{pr}}$ — $\bar\pi$ read as the mean of the pooled law — is excluded**, by
the binding ruling at the head of this file and by L3's Step 19: it forces the pooled law to a point
mass at $\bar\pi$ with $A'_\kappa=0$, under which Step 19 below returns
$\mathcal S_P(\tau)=\mathcal S_P(\tau')=0$ and leg 3 holds only because both sides vanish. So this
step is stated on the support-point reading alone, and leg 3 has content under it.

### Part IV — Leg 3: a lower $\tau$ weakly lowers $\mathcal S_P$

**Step 15 (L3, by its statement).** Hypothesis 9 gives: under A($\tau$) the pooled cell's interior
$\kappa$-motion is proportional to $C_h(\bar\pi)$. Writing that proportionality with A($\tau$)'s own
coefficients (card §5 and §4.4), differentiate the representation
$\mathbb E[h]=A_0(\kappa)h(0)+A_{1/2}(\kappa)h(\bar\pi/2)+A_1(\kappa)h(\bar\pi)$ in $\kappa$ at fixed
support points and substitute $A_0'=A_1'=A'_\kappa$ and $A_{1/2}'=-2A'_\kappa$:
$$A_0'h(0)+A_{1/2}'h(\bar\pi/2)+A_1'h(\bar\pi)
=A'_\kappa\bigl[h(0)-2h(\bar\pi/2)+h(\bar\pi)\bigr]=A'_\kappa\,C_h(\bar\pi).$$
So the constant of proportionality in L3's statement is $A'_\kappa$, and the object L3 controls is
the motion of the pooled mean **through the weights, at a fixed chord**. L3's *proof* is neither read
nor used.

**Step 16 (the bridge to the card's $\mathcal S_P$).** Card §4.4 defines
$\mathcal S_P=\lvert\partial_\kappa M_P\rvert$ with $M_P=\Delta_m\mathbb E[h(\mathcal I_H)\mid D=0]$ —
a **total** $\kappa$-derivative. Step 15 supplies only the weight channel. The gap is real: if the
support points or the kernel $h$ moved with $\kappa$, the total derivative would carry an extra term
of the form
$\bigl[\tfrac12 A_{1/2}h'(\bar\pi/2)+A_1h'(\bar\pi)\bigr]\partial_\kappa\bar\pi$ plus a term in
$\partial_\kappa h$, neither of which L3 bounds. Hypothesis 11, clauses (br-i) and (br-ii), close
exactly that gap and no more: (br-i) makes the representation available at both thresholds, and
(br-ii) localises all $\kappa$-dependence in the weights. The two are **not** independent under the
card's literal A($\tau$) display, where $\bar\pi$ and $h$ carry no $\kappa$ argument and (br-i)
already localises everything; what (br-ii) genuinely buys is stated at the head of this file — against
the honest reading $h=\pi\,p(\hat v,\pi)$, a function of two scalars, "$h$ as a function of the
posterior is $\kappa$-free" is real content that A($\tau$)'s notation hides, and (br-ii) is the clause
that repairs that card ambiguity. Together they give, at each threshold,
$$\partial_\kappa M_P=\Delta_m A'_\kappa\,C_h(\bar\pi),
\qquad\text{hence}\qquad
\mathcal S_P=\Delta_m\,\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert .$$
Partial support for (br-ii) — not a proof of it — comes from Steps 4 and 21: at fixed policies the
pooled *prior* share $\bar\pi_{\mathrm{pr}}$ is $\kappa$-free, so the $\partial_\kappa\bar\pi$ term
vanishes under (br-iv). What remains genuinely assumed in (br-ii) is that the kernel $h$, which
through $p(\mathcal I)$ depends on the price $P$ and hence in principle on $\kappa$, is $\kappa$-free
as a function of the posterior. I do not prove that and I do not claim it.

**Step 17 (chord monotonicity, used as maintained).** A($\tau$) maintains
$\lvert C_h(\bar\pi)\rvert$ weakly increasing in $\bar\pi$ (Hypothesis 10; card §5 and §4.4). This is
**used as the card's maintained orientation, not derived** — the question msg3 asked explicitly.
With Step 14,
$$\lvert C_h(\bar\pi(\tau'))\rvert\;\le\;\lvert C_h(\bar\pi(\tau))\rvert .$$

**Step 18 (the coefficient).** Hypothesis 11, clause (br-iii), gives
$\lvert A'_\kappa(\tau')\rvert\le\lvert A'_\kappa(\tau)\rvert$. This clause cannot be dispensed with:
$A'_\kappa$ is a property of the pooled information structure, and the pooled class at $\tau'$ is a
strictly different collection of histories from the pooled class at $\tau$ whenever $\nu>0$, so
nothing in the card ties the two coefficients together. Card §4.4 bounds $A'_\kappa$ on $[0,1]$ but
says nothing about how it moves with the policy.

**Step 19 (leg 3).** All four factors are nonnegative reals, and $\Delta_m>0$ (card §4.1). Multiplying
the two weak inequalities of Steps 17 and 18 and using Step 16 at each threshold,
$$\mathcal S_P(\tau',T)=\Delta_m\lvert A'_\kappa(\tau')\rvert\,\lvert C_h(\bar\pi(\tau'))\rvert
\;\le\;\Delta_m\lvert A'_\kappa(\tau)\rvert\,\lvert C_h(\bar\pi(\tau))\rvert=\mathcal S_P(\tau,T).$$
This is leg 3, and it is the only leg that rests on A(br).

**Step 20 (the $C_h=0$ case, handled explicitly).** The card maintains the **weak** orientation
$C_h\le 0$, so the boundary case must be stated rather than assumed away. If
$C_h(\bar\pi(\tau))=0$, then by Step 17 with Step 14,
$0\le\lvert C_h(\bar\pi(\tau'))\rvert\le\lvert C_h(\bar\pi(\tau))\rvert=0$, so
$C_h(\bar\pi(\tau'))=0$ too, and Step 16 gives
$\mathcal S_P(\tau')=\mathcal S_P(\tau)=0$. The conclusion holds with equality; no strictness is
claimed anywhere in leg 3, and the lemma must not be read as an "iff".

**Step 21 ($\kappa$-invariance of the composition objects, recorded for the check).** By Step 4,
$D(\cdot;\tau,T)$ is a function of $s$ alone; by Hypothesis 1 so is the engagement label
$a_{j(s)}$; by Hypothesis 5 (A1) the marginal law of $s$ does not depend on $\kappa$, since $\kappa$
parameterises only the law of $z_{0:H}$ and $z_{0:H}\perp(v,\varepsilon)$. Therefore $\Omega$, $\nu$,
$\bar\pi_{\mathrm{pr}}$, and Step 5's inclusion are all invariant to $\kappa$ at fixed policies. Legs
1 and 2 hold at every $\kappa$ simultaneously, not just on average. $\square$

---

## WHERE IT FAILS

1. **Endogenous re-optimisation at the margin (kills legs 1, 2 and 3).** Hypothesis 1 is the
   load-bearing one and it is the least innocent. Concretely: let a signal $s^\ast$ just above the
   top cutoff $k_{J-1}$ select the most aggressive Voice plan at $\tau$ and be flagged. At $\tau'$
   the flag becomes certain and earlier, so the pooled-round camouflage that made the plan worth its
   engagement cost is gone; the blockholder switches $s^\ast$ to Hold. Then $a=0$ at $s^\ast$ under
   $\tau'$, the history leaves $\mathcal C_F$ altogether, Step 5's inclusion fails, and $\Omega$ can
   *fall* with a tighter threshold. This is not a remote case — it is the whole content of the
   general-equilibrium cutoff response, which is why C1 exists as a separate result. L4 is a
   fixed-policy statement and must never be quoted as an equilibrium one.
2. **Pre-existing crossing: $b_0 \ge \tau'$ (kills leg 1's citation, hence legs 1–3).** Card §4.2
   sets $B_j(s,-1)=b_0$ and maintains $b_0<\tau$; the turn-2 audit ruling D1-O1 puts a pre-existing
   crossing outside the core. If the threshold is lowered past the initial stake — a realistic
   policy experiment, since the whole point of a tighter rule is to catch smaller positions — then at
   $\tau'$ the crossing date is $c=-1$ for *every* plan including Exit and Hold, A4's "only Voice
   plans cross in the core" fails, and D1's clock equivalence is being cited off its stated domain.
   Step 3's product form is then unavailable at $\tau'$ and the whole chain stops at Step 3.
3. **Threshold change bundled with a window change, or early/strategic filing (kills Step 5).**
   Suppose the tighter threshold $\tau'$ comes with a longer window $T+\Delta_T$, $\Delta_T\ge1$ — a
   de minimis easement of exactly the kind real rules carry. Take a history with
   $c(\tau)=H-T$, so it is flagged at $(\tau,T)$. At $\tau'$ the crossing is weakly earlier,
   $c(\tau')\le c(\tau)$, but the filing lands at $c(\tau')+T+\Delta_T$, which exceeds $H$ whenever
   $\Delta_T>c(\tau)-c(\tau')$. The history is flagged at $(\tau,T)$ and unflagged at
   $(\tau',T+\Delta_T)$: the inclusion of Step 5 fails outright. The same failure is produced by any
   departure from A4 that lets the filing date be chosen rather than pinned at $c+T$.
4. **The bridge fails at (br-iii): the reclassification reshapes the pooled weights (kills leg 3
   only).** Suppose the pooled class at $\tau$ contains a large mass of uninformative Hold histories
   whose posteriors barely move with $\kappa$, so $\lvert A'_\kappa(\tau)\rvert$ is small; and the
   Voice histories reclassified into $\mathcal N$ were the ones anchoring the low end of the pooled
   posterior distribution. The pool that survives at $\tau'$ can then have weights that swing more
   with $\kappa$: $\lvert A'_\kappa(\tau')\rvert > \lvert A'_\kappa(\tau)\rvert$ by a factor larger
   than the fall in $\lvert C_h\rvert$, and $\mathcal S_P$ **rises** with a tighter threshold even
   though legs 1 and 2 are intact. Nothing in the card excludes this, which is why (br-iii) is
   listed as an assumption rather than a lemma. This is the failure mode T1's composition ratio
   $C_\tau$ is built to expose.
5. **Null pooled cell: $\Omega(\tau')=1$ (kills legs 2 and 3 by undefinedness).** If the plan menu is
   effectively Voice-only — A3's weak inequalities permit collapsed action regions, including Hold —
   and $\tau'$ is low enough that every type crosses by $H-T$, then $\Pr(D(\tau')=0)=0$,
   $\bar\pi_{\mathrm{pr}}(\tau')$ and $\mathcal S_P(\tau')$ are undefined, and Step 10 fails.
   Following L1's ledger treatment, the null-cell average is left undefined rather than imputed, so
   the comparison has no right-hand side rather than a wrong one.
6. **A($\tau$)'s $\lvert C_h\rvert$ monotonicity fails (kills leg 3 only).** If $h$ has an inflection
   — convex on $[0,\bar\pi_1]$ and concave beyond — then $C_h$ changes sign and
   $\lvert C_h\rvert$ is non-monotone in $\bar\pi$, so a *lower* $\bar\pi(\tau')$ can sit at a
   *larger* $\lvert C_h\rvert$ and Step 17 reverses. Card §5 maintains the monotonicity rather than
   deriving it, and this proof does not improve on that.

---

## LABEL CLAIMED

**CONJECTURE.** Unchanged, and the ledger is not touched. Two reasons, both binding.

First, card §7: a proof on file is not enough — PROVED requires a complete proof that has been
**independently re-derived and proof-read**, and neither has happened to this file. The card's §6
note applies the same requirement to D1, L1 and L2, which already have proofs on file and passed a
proof-read, and they remain CONJECTURE pending Thread 2's re-derivation.

Second, and specific to L4: leg 3 is proved **under A(br)**, a hypothesis that is not in the card.
The card's own aspiration for L4 is "PROVED under nested reclassification", which the analysis above
shows is the wrong hypothesis to name — nested reclassification is a *conclusion* (Step 5), and the
real burden is the chord–sensitivity bridge. Even if the re-derivation and proof-read both pass, the
honest final label for L4 is **PROVED under A(br)**, with legs 1 and 2 proved outright and leg 3
region-restricted to wherever (br-i)–(br-iv) can be verified. Per card §7, "region-certified" is not
a fifth label: it is PROVED with the hypothesis named.

---

## NUMERICAL CHECK REQUEST

One script, one CSV, one JSON verdict, in the D-series pattern.

**Frozen inputs.** The equilibrium cutoff vector $k$ and the execution paths $B_j(s,\cdot)$ are
solved **once** at a reference threshold and then held fixed across the entire $\tau$ grid. If the
script re-solves the equilibrium at each $\tau$, it is testing T1/C1, not L4, and its output must be
discarded.

**Formulas evaluated at each grid point $(\tau,T,\kappa)$:**

$$\Omega(\tau,T)=\mathbb E_s\Bigl[\mathbf 1\{a_{j(s)}=1\}\,\mathbf 1\{B_{j(s)}(s,H-T)\ge\tau\}\Bigr],
\qquad
\bar\pi_{\mathrm{pr}}(\tau,T)=\frac{\Pr\bigl(a=1,\ D(\tau,T)=0\bigr)}{1-\Omega(\tau,T)},$$
$$\bar\pi=2\,\bar\pi_{\mathrm{pr}}\ \text{(level-symmetric form; report the directly enumerated
pooled support maximum in a second column. The identity map }\bar\pi=\bar\pi_{\mathrm{pr}}
\text{ is excluded — Step 14)},\qquad
C_h(\bar\pi)=h(0)-2h(\bar\pi/2)+h(\bar\pi),\qquad
\mathcal S_P=\Delta_m\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert .$$

**Grid.** $\tau$ at the 10th, 20th, …, 90th percentiles of the distribution of
$B_{j(s)}(s,H-T)$ over Voice signals — nine points, eight tightening steps.
$T\in\{5,10\}$ business days (the card's own $W_T$ example). $\kappa\in\{0.15,0.16,\dots,0.85\}$, 71
points. $H$ as in the calibration; report it in the JSON.

**Predicted signs.** For every tightening step $\tau\to\tau'$ (adjacent percentiles), at every one of
the 71 $\kappa$ values and both $T$, written as explicit differences rather than with a bare
difference operator:
$$\Omega(\tau')-\Omega(\tau)\ge 0,\qquad
\bar\pi_{\mathrm{pr}}(\tau')-\bar\pi_{\mathrm{pr}}(\tau)\le 0,\qquad
\mathcal S_P(\tau')-\mathcal S_P(\tau)\le 0.$$
These are exact set-theoretic and arithmetic consequences, not statistical tendencies. **A single
sign violation is a failed hypothesis, not sampling error** — it means the script re-optimised, or
$b_0\ge\tau'$ somewhere on the grid, or A(br) is being violated at (br-iii).

**Predicted magnitudes.**

1. *Step 11 is an accounting identity.* Residual
   $\bigl\lvert\bar\pi_{\mathrm{pr}}(\tau)-\bigl[(1-\nu/\rho_P)\bar\pi_{\mathrm{pr}}(\tau')+\nu/\rho_P\bigr]\bigr\rvert
   < 10^{-12}$ at every grid point. Machine precision is the right tolerance because nothing here is
   approximated.
2. *Step 21 predicts exact flatness in $\kappa$.* $\max_\kappa\lvert\Omega(\tau,T,\kappa)-\Omega(\tau,T,0.5)\rvert<10^{-12}$
   and the same for $\bar\pi_{\mathrm{pr}}$. A residual above $10^{-8}$ means the execution path is
   reading realised order flow, i.e. the no-feedback timing has been violated in the code.
3. *The $\tau$ grid must bite.* By construction $\omega_a(\tau_p)=\Pr(B\ge\tau_p\mid a=1)$, so
   $\omega_a$ should run from $\approx 0.9$ at the 10th percentile to $\approx 0.1$ at the 90th, and
   $\Omega=\Pr(a=1)\,\omega_a$ should span roughly a ninefold range. Deviation above $0.02$ in
   $\omega_a$ at any decile means the grid is not the percentile grid it claims to be.
4. *L3's quadratic corollary.* At the two smallest $\bar\pi$ points, $\mathcal S_P/\bar\pi^2$ should
   agree within 5%. This is the only prediction that needs $h\in C^2$ at zero; if it fails while
   predictions 1–3 pass, the failure is in $h$'s regularity, not in L4.
5. *This is the one that measures A(br).* Under the equality version of (br-iii),
   $C_\tau=\mathcal S_P(\tau')/\mathcal S_P(\tau)$ should equal
   $\lvert C_h(\bar\pi(\tau'))\rvert/\lvert C_h(\bar\pi(\tau))\rvert$ to within $10^{-12}$. Whatever
   residual the script reports **is** the size of the $A'_\kappa$ channel — that is, how much of the
   composition effect is coming from the pooled weights reshaping rather than from the chord
   shortening. Report the residual as a number, not a pass/fail: it is the empirical content of the
   bridge, and it is what T1's $C_\tau$ inherits.

---

## NOTATION DELTA

Symbols used above that are not in card §4. Nothing existing is renumbered or re-keyed.

| Symbol | Meaning | Collision check |
|---|---|---|
| $\tau'$ | the tighter threshold, $b_0<\tau'<\tau$ | in-family with the card's $T'$ usage in the $B^F$ and $Q^F$ rows |
| $j(s)$ | the plan the frozen cutoff vector $k$ selects at signal $s$ | $j$ is the card's plan index; $j(s)$ is that index as a function of the signal |
| $\mathcal N$ | newly flagged set $\mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T)$ | $\mathcal N$ free in card and manuscript; not $N(\cdot,\cdot)$, which is only used for the normal law |
| $\nu$ | $\Pr(\mathcal N)=\Omega(\tau')-\Omega(\tau)$ | free |
| $\rho_P$ | pooled mass at the looser threshold, $1-\Omega(\tau)$ | deliberately **not** $P_P$, which would collide with the card's pooled price $P_d^P$ |
| $\bar\pi_{\mathrm{pr}}$ | pooled **prior** engagement share $\Pr(a=1\mid D=0)$, kept distinct from the card's $\bar\pi$ (A($\tau$)'s chord endpoint) | subscripted, never a bare variant of $\bar\pi$ |
| A(br) | the chord–sensitivity bridge hypothesis, clauses (br-i)–(br-iv) | named in the A1–A8 / A($\tau$) / AGE family; deliberately not lettered "B", which would collide with $\mathsf B$ (entry indicator) and $B_j$ (stake) |
| $\Pi_\kappa$ | the pooled posterior random variable whose law A($\tau$) represents | appears in the turn-1 A($\tau$) block; used here only in the top-of-file remark on (br-iv) |
| $A'_\kappa(\tau)$, $A'_\kappa(\tau')$ | the card §4.4 coefficient $A'_\kappa$ **evaluated on the pooled class generated by the named threshold** — a card symbol given an argument, not re-keyed and not given a second meaning | the pooled class differs across thresholds, so the coefficient must be indexed to say which class it belongs to (Step 18); read throughout under the **conditional** normalisation, the one $\mathcal S_P=\lvert\partial_\kappa M_P\rvert$ requires |
| $\bar\pi(\tau)$, $\bar\pi(\tau')$ | likewise the card §4.4 chord endpoint evaluated on each threshold's pooled class; $\bar\pi$ is the **upper support point** of that class's posterior law, per the binding ruling at the head of this file | not a new symbol and not a second meaning; the argument names the class |
| $\Delta_T$ | window increment in WHERE IT FAILS 3, $\Delta_T\in\{1,\dots,H\}$, so the bundled policy is $(\tau',T+\Delta_T)$ | decorated, matching the card's uniformly decorated $\Delta$ family ($\Delta_m,\Delta_V,\Delta^{\mathrm{act}},\Delta_{\kappa k},\Delta_{kr},\Delta_{kk},\Delta_k$); $\Delta_T$ is free in the card |
| $s^\ast$ | one particular signal value, just above the top cutoff $k_{J-1}$, used only in WHERE IT FAILS 1 | $s$ is the card §4.1 signal; the star marks a named realisation, not a new variable |

Bare-symbol rules observed. The letter $C$ appears only as $C_h$, $C_\tau$, $\mathcal C_F$,
$\mathcal C_P$. **No bare $\Delta$ appears**: every $\Delta$ is decorated ($\Delta_m$, $\Delta_T$),
and the check block's predicted signs are written as explicit differences of named quantities rather
than with a difference operator — the same rule L3's notation delta declares.
The card's reserved bare letters — the sans-serif entry-indicator/filing-tuple pair,
the total-surplus letter, the utility letter, and D7's appropriability coefficient — do not appear
anywhere in this file in bare form, and the D7 coefficient does not appear at all. $\kappa$ is
noise-trading intensity throughout, with no drift toward depth, volume or turnover; upright $T$ is
the window, and the best-response map $\mathcal T$ does not appear.

---

## NOT CLAIMED

1. **Nothing about equilibrium.** Every statement is at fixed policies. The threshold comparison
   after cutoff responses is C1's business, and failure case 1 shows the sign can reverse there.
2. **No strict inequality anywhere.** $\nu>0$ is never assumed, so all three legs may hold with
   equality; in particular no claim that a tighter threshold *strictly* attenuates.
3. **A(br) is not claimed to hold.** It is named, not defended. (br-iii) in particular is an
   assumption about how the pooled weights respond to reclassification, and I have no argument for
   it.
4. **A($\tau$) is not claimed to be satisfiable on the two-round pooled cell.** msg3 §3 flags that as
   open for L3; L4 inherits the question and does not answer it. Nor is A($\tau$)'s
   $\lvert C_h\rvert$ monotonicity derived — it is used as maintained.
5. **The $\bar\pi$ reading is now fixed by ruling, and the card wording is not.** Per the binding
   adjudication of 2026-08-21, $\bar\pi$ is A($\tau$)'s **upper support point** and the pooled share
   is the strictly smaller mean $\mathbb E[\Pi_\kappa]$; the identity reading is excluded by L3's
   Step 19. What is **not** claimed here is that card §4.4's gloss ("pre-order pooled engagement
   share in the chord") has been corrected — that is a card edit and a regeneration item. Nor is the
   associated domain restriction $\bar\pi_{\mathrm{pr}}\le 1/2$ under the level-symmetric form
   resolved: it is flagged, not resolved.
6. **Nothing about the window margin.** The $T$ comparison is T1's iff condition and is untouched
   here; L4's $T$ is held fixed throughout.
7. **The decomposition $\mathcal S=(1-\Omega)\mathcal S_P$ is not used and not claimed.** It belongs
   to L1 + L2 + T1. L4 speaks only about $\Omega$, $\bar\pi$ and $\mathcal S_P$ separately, so a
   reader cannot conclude from L4 alone that $\mathcal S$ falls: $\Omega$ rising and $\mathcal S_P$
   falling both push the same way in that product, but assembling them is T1's step, not L4's.
8. **No claim about $\Delta^{\mathrm{act}}$'s own sign, the hump, $J$'s $\kappa$-invariance, or any
   calibration number.**
9. **No label move.** L4 remains CONJECTURE; the card ledger is not edited by this file.

---

## Repairs applied (2026-08-21, batch-1 audit)

Source: `threads/2026-08-21_batch1_proofread_audit.md` (Opus proof-read, verdict PASS, no failing
steps), together with the orchestrator's binding adjudications of the same date. Every change below
is a citation, a restatement of a hypothesis in the form the ruling fixes, a wording fix or a
notation declaration. **No claim, hypothesis or step conclusion was altered in substance, and no step
was renumbered.** The label is untouched: L4 remains CONJECTURE.

| Finding | Change made |
|---|---|
| **L4-R1** (with the binding $\bar\pi$ ruling) | The two-reading agnosticism is collapsed. $\bar\pi$ is now stated throughout as the **upper support point** of the pooled posterior law, with the pooled engagement share the strictly smaller mean $\mathbb E[\Pi_\kappa]$; (br-iv) is restated for that reading only; the **identity branch is excluded**, on L3's Step 19 (point mass, $A'_\kappa=0$, leg 3 identically zero). Recorded at the head of the file, at Step 14, in the check block, and in NOT CLAIMED 5; card §4.4's gloss is flagged as a regeneration item. |
| — citation discipline | The head-of-file discipline note now declares the **one exception**: (br-iv) and Step 14 cite L3's Step 19 directly, by orchestrator adjudication. Everywhere else L3 and D1 are still cited by ledger statement only. |
| **L4-R2** | (br-ii) restated to say what it actually buys: under the card's literal A($\tau$) display it would restate (br-i); against the honest reading $h=\pi\,p(\hat v,\pi)$ — two scalars — it is the clause that repairs a card ambiguity. Written into the A(br) block and into Step 16's framing. |
| **L4-R3** | Step 5's "card §2.5" removed: the display is now sourced to card §4.3's $\mathcal C_F/\mathcal C_P$ row plus card §4.2's $D_j$ row, with an inline note that the card has no §2.5 and that the §2.5 carrying this display belongs to `threads/thread1_turn1_answer.md`. |
| **L4-R4** | NOTATION DELTA completed. (a) **No bare $\Delta$**: WHERE IT FAILS 3's window increment is now the decorated $\Delta_T$ (declared), and the check block's predicted signs are written as explicit differences. (b) Threshold-indexed $A'_\kappa(\tau)$, $A'_\kappa(\tau')$, $\bar\pi(\tau)$, $\bar\pi(\tau')$ declared, with the conditional normalisation pinned. (c) $X_{0:H}$ removed in favour of $(X_0,\dots,X_H)$ at Step 2. (d) $s^\ast$ declared. |
| **L4-R5** | One leg-numbering scheme fixed in the CLAIM: leg 1 = $\Omega$, leg 2 = $\bar\pi_{\mathrm{pr}}$, leg 3 = $\mathcal S_P$, CLAIM item 1 = the Part I inclusion, no "leg 4". Hypothesis 8's parenthetical corrected from "leg 2" to "leg 1". |

Not applied here, by scope: L4-O1 … L4-O3 are OBSERVATIONs, not REPAIRs.

### FILE: proofs/P1_proof.md

# P1 — Cutoff PBE existence (full proof)

**Written against MODEL CARD v4, version stamp 2026-08-20 · commit `0c9185b`.**
Sources consumed: card §§2–5 and §8; `threads/thread1_turn1_answer.md` §P1 (the statement);
`threads/thread1_turn2_audit.md` (the D1 repairs, in particular D1-R2 on the flagged continuum,
and L2-R1/L2-R2 on the injective form of A7 and the no-feedback timing).

---

## CLAIM

Fix the parameter vector $\vartheta$. Under hypotheses h.1–h.12 and h.14 below — A1–A7 of card §5,
together with the card's §2 no-feedback timing, D1, the round-2 action-set stipulation h.11, the sign
convention h.12, and the blockholder payoff definition h.14 (a card gap: the card carries no payoff
row) — the two-round model has at least one **cutoff perfect Bayesian equilibrium over
complete contingent plans** in the sense of card §3: a weakly ordered cutoff vector
$k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, together with pooled and flagged
price families at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs
obtained as limits of full-support perturbations, the card §4.3 bidder-entry rule, and a
sequentially optimal flagged component. Under A8 evaluated at $k^\star$, both cells $\mathcal C_F$
and $\mathcal C_P$ carry strictly positive probability, hence both are on path.

h.13 and h.15 are not needed for either half of the claim; they are used only in Step 20, to turn A8
from an assumption about $\Omega$ into a statement about a single signal threshold.

Uniqueness of $k^\star$ is **not** claimed (card §3 and §9; see NOT CLAIMED).

---

## HYPOTHESES

Each is cited by number at the step that consumes it. Items marked **[ADDITION]** are not in card
§5; they are named here because a step needs them and the card as written does not supply them.

1. **h.1 = A1 (independent primitives).** $v,\varepsilon,\xi$ and all $z_d$ mutually independent,
   all variances strictly positive. *Used: Steps 4, 7, 9, 10.*
2. **h.2 = A2 (finite model).** Plan menu $\mathcal J$, the image of $\Gamma$, the noise support
   $\{-\bar z,0,+\bar z\}$ and the calendar horizon $H$ are finite; prices and payoffs bounded on
   the maintained parameter set. *Used: Steps 3, 9, 13, 16.*
3. **h.3 = A3 (ordered plans, single crossing).** At every belief/price system, adjacent-plan
   payoff differences cross zero at most once in $s$, and the preferred plan is weakly increasing
   in $s$. *Used: Steps 1, 13.*
4. **h.4 = A4 (legal-clock discipline).** $c$ is the first date the path reaches $\tau$; the filing
   lands exactly at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in
   the core; $D=1\Rightarrow a=1$. *Used: Steps 2, 6, 19.*
5. **h.5 = A5 (inner pricing regularity), consumed as a measurably selected family.** Each
   public-history pricing map has a unique fixed point, continuous in beliefs, cutoffs and
   parameters. Because the flagged information sets are continuum-indexed (D1-R2), the uniqueness
   clause is read here as delivering a **family** $\sigma_F\mapsto P^F(\sigma_F;k)$ that is
   measurable in the flagged tuple and continuous in $k$ — not a finite list of numbers.
   *Used: Steps 5, 6, 15.*
6. **h.6 = A6 (compact outer self-map).** All best-response cutoffs lie in a common compact ordered
   polytope $\Theta$; $\mathcal T$ is continuous and maps $\Theta$ into itself. Steps 13–15 split
   this into three parts and show only two of them are genuine assumptions. *Used: Steps 14, 15, 16.*
7. **h.7 = A7 in its injective form.** $(j,s)\mapsto (B_j^F(s),Q_j^F(s),a_j)$ is injective on the
   flagged set. Per card §5's turn-2 note, the weak wording ("identifies the informed component")
   is not sufficient, and injectivity forces $B^F$ continuum-valued. *Used: Steps 6, 10.*
8. **h.8 = A8 (interior crossing), evaluated at the fixed point.** $0<\Omega(\kappa,\tau,T)<1$ at
   $k^\star$. *Used: Step 19 only.*
9. **h.9 = D1 (rule-keyed partition and timing split).** $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is
   measurable and maps every control-node public history into exactly one cell; for every Voice
   plan $f_j\le H\iff B_j(s,H-T)\ge\tau$. D1 carries the card's label CONJECTURE, so P1 inherits
   that conditionality. *Used: Steps 2, 6, 19, 20.*
10. **h.10 = the card §2 no-feedback timing.** No within-window re-optimisation: $B_j(s,d)$,
    $q_{jd}(s)$ and $Q_j^F$ are functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone, never of realised
    order flow or realised prices. The turn-2 audit (L2-R2) required this to be lifted from prose
    into a numbered hypothesis for L2; P1 needs it at the same load-bearing places.
    *Used: Steps 2, 11, 12.*
11. **h.11 [ADDITION] — the round-2 action set is the plan-generated set.** For every
    $j\in\mathcal J$ and every $s$ on the flagged set, the blockholder's round-2 action set at
    $(j,s)$ **is** $\mathcal Q_j(s):=\{Q_{j'}^F(s):j'\in\mathcal J\text{ shares }j\text{'s pooled
    path up to }f_j(s)\text{ and }a_{j'}=a_j\}$ — the orders generated by menu elements that agree
    with $j$ on everything already played — rather than the full interval $[0,\bar b-B_j^F(s)]$.
    *Used: Step 12.*
    **Why this and not the closure form (batch-1 audit P1-R1).** An earlier draft stated h.11
    primarily as a *closure* condition: for every feasible $Q'\in[0,\bar b-B_j^F(s)]$ there is a menu
    element $j'$ delivering $Q_{j'}^F(s)=Q'$. **That form is jointly unsatisfiable with h.2 and is
    struck.** h.2 makes $\mathcal J$ finite, so $\{Q_{j'}^F(s):j'\in\mathcal J\}$ has at most
    $\lvert\mathcal J\rvert$ elements and cannot cover an interval of positive length; the closure
    form therefore forces $B_j^F(s)=\bar b$, i.e. $Q^F\equiv0$ and an empty round 2, contradicting
    card §4.2's $Q^F$ row (Voice plans have $Q^F\ge0$ with $T'<T\Rightarrow Q^F(T')\ge Q^F(T)$, so
    $Q^F$ genuinely varies). The surviving form above is consistent with h.2 and is all Step 12
    consumes — Step 12 runs on it verbatim. It is **not** a closure condition and is not called one:
    it is a modelling stipulation about what the round-2 action set *is*, which is a different and
    much weaker thing.
12. **h.12 [ADDITION] — nonnegative premia.** $m_0\ge 0$. Card §4.1 restricts only $m_1>m_0$ and
    $\Delta_m>0$; it does not sign $m_0$. With $\Delta_m>0$ and $\pi\in[0,1]$ this gives
    $\bar m(\mathcal I):=m_0+\pi(\mathcal I)\Delta_m\ge 0$. *Used: Steps 7, 8.*
13. **h.13 [ADDITION] — Voice stake monotonicity across plans.** For Voice plans $j'>j$,
    $B_{j'}(s,d)\ge B_j(s,d)$ for every $(s,d)$. Not in the card; the card orders the menu by
    "aggressiveness" without tying that order to the stake path. *Used: Step 20 only, for the
    threshold reformulation of A8 — not for existence.*
14. **h.14 [ADDITION — CARD GAP] — the blockholder's payoff.** For plan $j$ at signal $s$,
    $$U_j(s)=\mathbb E\bigl[b_j^*(s)\,Y-\mathcal C_j^{\mathrm{trade}}-C_j(s)\ \big\vert\ s,j\bigr],$$
    with $\mathcal C_j^{\mathrm{trade}}$ the plan's execution outlay (the prices paid across the
    pooled and flagged rounds) and $C_j(s)$ the engagement cost. **The card carries no blockholder
    payoff row**: `MODEL_CARD.md` has no §2.10, no $U_j$, no $\mathcal C_j^{\mathrm{trade}}$, and
    mentions $C_j(s)$ only inside §4.4's $C$-overload note. The object is stated here as this proof's
    own numbered definition, faithful to `threads/thread1_turn1_answer.md` §2.10 where it does live.
    **Card gap, regeneration item:** P1, L2 and every future best-response argument need this row;
    recommend the card absorb it into §4.2 or §2. *Used: Steps 11, 13, 14, 15 — it is the optimand of
    Steps 11–13 and the object Step 15 asks to be continuous.*
15. **h.15 [ADDITION] — engagement flags on an upper set of the menu.** $a_j=1$ exactly on an upper
    set of the ordered menu: there is $j_a$ with $a_j=1$ for $j\ge j_a$ and $a_j=0$ for $j<j_a$.
    Card §4.2 says $a_j=1$ for Voice and $0$ for Exit/Hold and orders the menu "least to most
    aggressive", but never ties the two; card §4.5's four-action gloss happens to satisfy this and a
    general finite menu need not. *Used: Step 20 only, alongside h.13 — not for existence.*

---

## PROOF

### Part A — the game at a fixed conjecture

**Step 1 (the conjecture induces a measurable plan-selection map).**
Fix $k=(k_1\le\cdots\le k_{J-1})\in\Theta$, where
$\Theta=\{k\in[\underline s,\overline s]^{J-1}:\underline s\le k_1\le\cdots\le k_{J-1}\le\overline s\}$
is card §4.5's compact ordered polytope, nonempty, compact and convex as the intersection of a cube
with the $J-2$ half-spaces $\{k_i\le k_{i+1}\}$. Define
$$
j_k(s)\;=\;1+\#\{i\in\{1,\dots,J-1\}:k_i\le s\}.
$$
$j_k$ is a weakly increasing step function of $s$ with values in $\mathcal J$, and it is Borel
measurable because each $\{s:k_i\le s\}$ is a half-line. This is the object card §3(i) calls "a
weakly ordered cutoff vector mapping $s$ into a plan", and h.3's second clause (preferred plan
weakly increasing in $s$) is what makes such a representation the right shape for a best response;
Step 13 returns to that.

**Step 2 (under h.10 every date-0 object is a deterministic measurable function of $(j,s)$).**
By h.10 the pooled path carries no feedback from realised order flow or prices, so for each
$j\in\mathcal J$ the objects $B_j(s,d)$ ($d=0,\dots,H$), $q_{jd}(s)=\Gamma(B_j(s,d)-B_j(s,d-1))$,
$c_j(s;\tau)$, $f_j(s)=c_j(s)+T$, $B_j^F(s)=B_j(s,f_j(s))$ and $Q_j^F(s)=b_j^*(s)-B_j^F(s)$ are
functions of $(j,s)$ and the policy pair $(\tau,T)$ alone. Measurability in $s$: $B_j(\cdot,d)$ is
monotone by card §4.2, hence Borel; $\Gamma$ is a finite ordered coarsening (h.2), hence Borel;
$c_j(\cdot;\tau)=\inf\{d:B_j(\cdot,d)\ge\tau\}$ is the pointwise minimum over the finite calendar
(h.2) of the indices of the Borel sets $\{B_j(\cdot,d)\ge\tau\}$, hence Borel with values in
$\{0,\dots,H\}\cup\{+\infty\}$; and — this is the D1-R2 repair written out —
$$
B_j^F(s)\;=\;\sum_{d=0}^{H-T}\mathbf 1\{f_j(s)=d+T\}\cdot B_j(s,d)
$$
is a finite sum of products of Borel functions, hence Borel, and likewise $Q_j^F$. By h.9 the
disclosure indicator is $D_j(s;\tau,T)=\mathbf 1\{a_j=1\}\cdot\mathbf 1\{B_j(s,H-T)\ge\tau\}$,
Borel in $s$. Composing with Step 1, all of these become Borel functions of $s$ alone at the fixed
conjecture $k$.

**Step 3 (the pooled public-history family is finite; the flagged family is not).**
Card §4.3 defines $\mathcal H_d^P=(X_0,\dots,X_d;\text{flag landed by }d)$ with
$X_d=q_{jd}+z_d$. By h.2 the image of $\Gamma$ is finite and $z_d\in\{-\bar z,0,+\bar z\}$, so each
$X_d$ takes values in a finite set; $d$ ranges over the finite calendar $\{0,\dots,H\}$; and the
flag coordinate is a single bit. Hence the collection of pooled public histories is finite. By
Step 2 the flagged tuple $\sigma_F:=(B^F,Q^F,a=1)$ — card §4.6's $\mathsf S_F$, the filing message
$F$ augmented by the flagged order $Q^F$ — is Borel but takes values in $[0,\bar b]^2\times\{1\}$,
a continuum: card §4.2 puts $B_j(s,d)\in[0,\bar b]$ with $s$ Gaussian and imposes monotonicity
only, and no card row discretises the stake level. This is exactly the D1-R2 finding, and it is
what forces the two layers of Part B to be treated differently.
*Note on scope.* The finiteness of the pooled family rests on the card's own §4.3 row, in which the
flag enters $\mathcal H_d^P$ as a bit and the filing content $B^F$ does not. Were the card to let
post-filing pooled histories carry $B^F$, the pooled family would join the continuum and the
selection argument of Step 6 would have to be run there too.

### Part B — inner prices

**Step 4 (every control-node pricing fixed point reduces to one scalar equation, and depends on the
information set only through the pair $(\hat v,\pi)$).**
Fix a control-node information set $\mathcal I$ and write $\hat v(\mathcal I)=\mathbb E[v\mid
\mathcal I]$, $\pi(\mathcal I)=\Pr(a=1\mid\mathcal I)$ and
$\bar m(\mathcal I)=m_0+\pi(\mathcal I)\Delta_m$. Card §4.3 gives
$Y=(1-\mathsf B)(v+a\Delta_V)+\mathsf B(P(\mathcal I)+m_0+a\Delta_m)$ and, from card §4.3's entry
row, $\mathsf B=\mathbf 1\{\xi\ge P(\mathcal I)+K+\bar m(\mathcal I)-\bar S\}$. Given $\mathcal I$,
the quantities $P(\mathcal I)$ and $\bar m(\mathcal I)$ are $\mathcal I$-measurable constants, so
$\mathsf B$ is a function of $\xi$ alone. By h.1, $\xi$ is independent of $(v,\varepsilon)$ and of
every $z_d$, hence independent of $(v,s,z_{0:H})$ and therefore of $(v,a,\mathcal I)$ jointly;
conditionally on $\mathcal I$, $\mathsf B$ is independent of $(v,a)$. Writing
$p=\Pr(\mathsf B=1\mid\mathcal I)$ and taking conditional expectations term by term,
$$
\mathbb E[Y\mid\mathcal I]
=(1-p)\bigl(\hat v+\pi\Delta_V\bigr)+p\,(P+m_0)+\Delta_m\,p\,\pi
=(1-p)\bigl(\hat v+\pi\Delta_V\bigr)+p\bigl(P+\bar m\bigr).
$$
With $\xi\sim N(0,\sigma_\xi^2)$ (h.1), $p=1-\Phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)$, which
is card §4.3's entry row verbatim and lies in $(0,1)$ for every finite $P$. Define the inner
pricing map
$$
\mathcal P_{\mathcal I}(P)\;=\;\bigl(1-p(P)\bigr)\bigl(\hat v+\pi\Delta_V\bigr)+p(P)\bigl(P+\bar m\bigr),
\qquad
p(P)=1-\Phi\!\Bigl(\tfrac{P+K+\bar m-\bar S}{\sigma_\xi}\Bigr).
$$
The card's requirement $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ is the scalar fixed-point equation
$\mathcal P_{\mathcal I}(P)=P$. **The map depends on $\mathcal I$ only through the two scalars
$(\hat v(\mathcal I),\pi(\mathcal I))$.** That is the fact Steps 5–7 use.

**Step 5 (pooled layer: A5 on a finite index set — stated in two parts, because only one of them is
a fixed point).**
By Step 3 there are finitely many pooled public histories. Step 4's map is derived at a **control
node**, which is where $\mathsf B$ is a function of $\xi$ alone given the conditioning, so the two
layers of the pooled family must be treated separately.

(a) *The pooled control-node cell ($D=0$ at date $H$).* Here $\mathcal I=\mathcal I_H$ is a control
node, Step 4 applies as derived, and h.5 supplies a unique fixed point of $\mathcal P_{\mathcal I}$,
continuous in beliefs and cutoffs. This is a genuine fixed point: the price appears on both sides
through the entry indicator.

(b) *Intermediate pooled dates $d<H$.* $\mathcal H_d^P$ is **not** a control node. Card §4.3's $Y$ row
writes the takeover branch as $\mathsf B(P+m_0+a\Delta_m)$ with $P$ unqualified; under the natural
economic reading — and it is the reading Step 4 itself adopts — that $P$ is the **control-node** price
$P(\mathcal I_H)$, so
$$P_d^P=\mathbb E\bigl[Y\mid\mathcal H_d^P\bigr]=\mathbb E\bigl[P(\mathcal I_H)\ \text{-branch value}\mid\mathcal H_d^P\bigr]$$
is, by the tower property, a plain conditional expectation of already-solved control-node values: **no
self-reference and no fixed point**. Under the other reading of §4.3's $Y$ row (the $P$ inside $Y$ is
the price at whichever information set is conditioning) part (a)'s fixed-point argument applies at
these dates too. **Card ambiguity, regeneration item: card §4.3's $Y$ row should pin which $P$ it
means** (batch-1 audit P1-R8).

The conclusion this step is used for survives on either reading, and that is why nothing downstream
turns on the adjudication: a finite family requires no selection argument, and the pooled price family
$k\mapsto (P_d^P(\mathcal H_d^P;k))_{\mathcal H_d^P}$ is a finite vector of continuous functions of
$k$ — at the control-node cell by (a) with h.5 and Step 7, and at $d<H$ by (b) as a finite-sum
conditional expectation of continuous functions — on those histories that carry positive probability
under the conjecture $k$. Histories of zero probability under $k$ are handled in Step 9.

**Step 6 (flagged layer: A5 consumed as a measurably selected family — the D1-R2 point).**
By Step 3 the flagged information sets are indexed by the continuum
$\sigma_F\in[0,\bar b]^2\times\{1\}$. A pointwise reading of h.5 — "at each $\sigma_F$ there is a
unique root" — does not by itself yield a *function* of $\sigma_F$ that the model can integrate
against, which is what card §4.4's $M_F=\Delta_m\mathbb E[h\mid D=1]$ and h.9's timing split both
require. The family is constructed as follows.

(a) On the flagged cell $\pi\equiv 1$: h.4 gives $D=1\Rightarrow a=1$ and h.9 makes $\{D=1\}$ an
event of the control-node history, so $\Pr(a=1\mid\sigma_F,D=1)=1$, matching card §4.3's row
"$\pi=1$ on $\mathcal C_F$". Hence $\bar m=m_0+\Delta_m=m_1$ on the whole flagged cell, a constant.

(b) By Step 4 the flagged pricing map therefore depends on $\sigma_F$ only through the single
scalar $\hat v(\sigma_F;k)=\mathbb E[v\mid\sigma_F,D=1]$. Write $\mathcal G_F(\cdot)$ for the map
sending a belief $\hat v$ to the unique root of $\mathcal P(\cdot)-\mathrm{id}$ at $(\hat v,\pi=1)$.
h.5's uniqueness clause makes $\mathcal G_F$ single-valued and h.5's continuity-in-beliefs clause
makes $\mathcal G_F$ continuous. (The symbol is $\mathcal G_F$ and not $g$: the turn-2 notation ruling
reserves $g$ for L3's mean-value form, and card §4.5 carries $g_r^{PE}$.)

(c) $\sigma_F\mapsto\hat v(\sigma_F;k)$ is Borel measurable. Two routes, both available: it is a
conditional expectation with respect to $\sigma(\sigma_F)$ and hence $\sigma(\sigma_F)$-measurable
by construction; and under h.7 the map $(j,s)\mapsto\sigma_F$ is injective on the flagged set and
Borel by Step 2, so — both $\mathcal J\times\mathbb R$ and $[0,\bar b]^2\times\{1\}$ being Borel
subsets of Polish spaces — Lusin–Souslin gives a Borel inverse $\iota_F$ on the image, and
$\hat v(\sigma_F;k)=\mu_v+\beta\bigl(\iota_F(\sigma_F)_s-\mu_v\bigr)$ with $\beta$ the card §4.1
projection coefficient. Injectivity plus measurability already delivers the measurable inverse; no
separate assumption is introduced.

(d) Therefore $P^F(\sigma_F;k)=\mathcal G_F\bigl(\hat v(\sigma_F;k)\bigr)$ is the composition of a Borel map
with a continuous map, hence Borel. **This is the measurably selected family that h.5 must be read
as supplying, and it is pinned rather than chosen: uniqueness at each $\sigma_F$ leaves no freedom,
so no selection principle is invoked and no two runs of the argument can produce different
families.** The turn-2 audit flagged (D1-R2) that D1 Step 11 and L2 Steps 8–9 both consume this
reading; P1 consumes it here, at the point where the flagged price enters the blockholder's payoff.

**Step 7 (under h.12 the inner root exists and is unique by derivation, so h.5's inner clause is not
carrying the weight it appears to).**
Write $A=\hat v+\pi\Delta_V$ and $\varrho(P)=\mathcal P_{\mathcal I}(P)-P=(1-p(P))(A-P)+p(P)\bar m$,
continuous in $P$ because $\Phi$ is. By h.12, $\bar m\ge 0$.

(i) *No root below $A$.* For $P<A$ both terms of $\varrho$ are nonnegative and the first is strictly
positive since $p(P)<1$ (Step 4), so $\varrho(P)>0$.

(ii) *A root exists.* $\varrho(A)=p(A)\bar m\ge 0$. If $\bar m=0$ then $P=A$ is a root. If $\bar m>0$,
then $\varrho(A)>0$; and as $P\to+\infty$, $p(P)\to 0$ while $(A-P)\to-\infty$, so $\varrho(P)\to-\infty$.
An explicit bracket: for $P\ge\bar S-K-\bar m+\sigma_\xi$ one has $p(P)\le 1-\Phi(1)<0.159$, whence
$\varrho(P)\le 0.159\,\bar m-0.841\,(P-A)\le 0$ once additionally $P\ge A+0.19\,\bar m$. The
intermediate value theorem on $[A,\max\{\bar S-K-\bar m+\sigma_\xi,\ A+0.19\bar m\}]$ gives a root.

(iii) *The root is unique.* $\varrho$ is differentiable with
$\varrho'(P)=p'(P)\bigl(P+\bar m-A\bigr)+p(P)-1$, and $p'(P)=-\phi\bigl((P+K+\bar
m-\bar S)/\sigma_\xi\bigr)/\sigma_\xi<0$. At any root, (i) gives $P\ge A$, so
$P+\bar m-A\ge\bar m\ge 0$ and the first term is $\le 0$; the second is $<0$ since $p<1$. Hence
$\varrho'<0$ **strictly at every root**. Suppose two roots $P_1<P_2$ with no root between them.
$\varrho'(P_1)<0$ forces $\varrho<0$ immediately to the right of $P_1$, and since $\varrho$ has no zero on
$(P_1,P_2)$ it is negative throughout that interval; $\varrho'(P_2)<0$ forces $\varrho>0$ immediately to
the left of $P_2$. The two conclusions contradict each other, so there is at most one root.

Consequently, on the maintained sign h.12 the existence-and-uniqueness half of h.5 is a theorem
rather than an assumption, and what h.5 genuinely contributes to P1 is *continuity in the
conjecture $k$*. Step 15 uses that and says where it, in turn, is assumed.

**Step 8 (the inner root is monotone and non-expansive in the belief, which is the object the
numerical check can hit).**
At the root, $\varrho'<0$ (Step 7(iii)), so the implicit function theorem applies to
$\varrho(P;\hat v)=0$ and yields
$$
\frac{\partial P}{\partial\hat v}
=\frac{1-p}{\,1-p+|p'(P)|\,(P+\bar m-A)\,}\;\in\;(0,1],
$$
the denominator being at least $1-p>0$ by h.12 and Step 7(i). The bound is used in NUMERICAL CHECK
REQUEST item 3.

### Part C — beliefs, on path and off

**Step 9 (pooled off-path beliefs as limits of full-support perturbations, using finiteness).**
Card §3(vi) requires off-path beliefs to be limits of full-support perturbations. Index the
perturbation by $n$: at stage $n$ every signal type plays every plan $j\in\mathcal J$ with weight at
least $1/n$, the remaining mass following $j_k$. By h.2 the plan menu is finite and by Step 3 the
pooled history alphabet is finite, so for each pooled history $\mathcal H_d^P$ the perturbed
posterior over plans is a ratio whose numerator and denominator are finite sums of terms
polynomial in $1/n$ with coefficients that do not depend on $n$; the denominator is strictly
positive for every $n$ because every plan carries weight at least $1/n$ and every noise mark
carries positive probability whenever $\kappa>0$, and at $\kappa=0$ because every achievable order
mark is generated by some plan. A ratio of polynomials in $1/n$ with a denominator that is nonzero
for all large $n$ converges as $n\to\infty$. Hence the limiting belief exists at every pooled
history, on path and off, and on path it agrees with the Bayes posterior. This is where h.2's
finiteness pays: with a continuum of pooled histories the limit would need a separate argument.

**Step 10 (flagged off-path beliefs are pinned by h.7, not chosen).**
By h.7 the map $(j,s)\mapsto\sigma_F$ is injective on the flagged set, so each flagged tuple in its
image is generated by exactly one pair $(j,s)$. Under the stage-$n$ perturbation of Step 9 that
pair has strictly positive weight, so the perturbed posterior at $\sigma_F$ places probability one
on $\iota_F(\sigma_F)$, independently of $n$; the limit is the same point mass. Therefore the
flagged belief is $\hat v(\sigma_F)=\mu_v+\beta(\iota_F(\sigma_F)_s-\mu_v)$ at every flagged tuple,
on path and off, and Step 6's family is simultaneously the on-path Bayes family and the off-path
limit family. **What "off path" covers here, said precisely (batch-1 audit P1-R3).** It covers flagged
tuples generated by $(j,s)$ pairs the conjecture $k$ does not select. It does *not* by itself cover
tuples outside the **image** of $(j,s)\mapsto\sigma_F$ — the tuples a round-2 deviation to an
off-menu order would produce — and no step assigns those a belief. This step stands on **h.11**: under
h.11 the round-2 action set is the plan-generated set, so no such tuple arises, and the image
exhausts the flagged tuples that can be reached. Step 17(vi) inherits the pinning on that reading and
on no other. Off-path beliefs at flagged nodes carry no free parameter — a consequence of h.7
worth recording, since it removes the usual arbitrariness in item (vi) of card §3 at exactly the
nodes the paper's disclosure mechanism runs through. By h.1 the pair $(v,\xi)$ remains conditionally
independent of the pooled residual given $s$, so nothing further is needed to price the node.

### Part D — sequential optimality

**Step 11 (the blockholder has exactly two decision points, and the flagged continuation is
deterministic given $(j,s)$).**
Card §2 places the plan choice at date 0 and, when $D=1$, the flagged order $Q^F$ in round 2, with
no within-window re-optimisation in between (h.10). So there is no pooled decision node after date
0: item (ii) of card §3, read on the pooled component, is satisfied by the timing itself rather
than by an argument, and the only genuine sequential-optimality requirement is the round-2 order.

On the flagged branch, by Step 2 the objects $B_j^F(s)$ and $Q_j^F(s)$ are deterministic in
$(j,s)$; by Step 6 the flagged price $P^F$ is a function of $\sigma_F$ alone and hence deterministic
in $(j,s)$; and by card §4.3 the control-node price on that branch is $P^F$. The blockholder payoff
of **h.14** — $U_j(s)=\mathbb E[b_j^*(s)Y-\mathcal C_j^{\mathrm{trade}}-C_j(s)\mid s,j]$, a numbered
definition of this proof because **the card has no blockholder payoff row (card gap, regeneration
item)** — therefore splits as
$$
U_j(s;k)\;=\;\underbrace{b_j^*(s)\,\mathbb E\bigl[Y\mid s,j,D=1\bigr]-P^F(\sigma_F)\,Q_j^F(s)-C_j(s)}_{\text{flagged continuation: deterministic in }(j,s)}
\;-\;\underbrace{\mathbb E_{z}\Bigl[\textstyle\sum_{d\le f_j}P_d^P\bigl(\mathcal H_d^P\bigr)\bigl(B_j(s,d)-B_j(s,d-1)\bigr)\Bigr]}_{\text{pooled execution: determined by the pooled path alone}} ,
$$
where the pooled expectation is over the noise $z_{0:H}$ only. The noise enters the first bracket
nowhere: $\mathbb E[Y\mid s,j,D=1]$ depends on $(v,\xi)$ and on $P^F$, and $\xi$ is independent of
$z$ by h.1 while $P^F$ is $z$-free by Step 6.

**Step 12 (h.11 makes the flagged component sequentially optimal, and nothing in A1–A7 does).**
Let $k$ be a conjecture and let $j=j_k(s)$ maximise $U_{\cdot}(s;k)$ over $\mathcal J$. Suppose some
round-2 order $Q'$ available at $(j,s)$ strictly improves the flagged continuation, holding the
market's flagged pricing schedule at the family of Step 6. By **h.11** the available orders are
exactly $\mathcal Q_j(s)$, the plan-generated set, so $Q'=Q_{j'}^F(s)$ for some $j'\in\mathcal J$ with
the same pooled path up to $f_j(s)$ and the same engagement flag. Identical
pooled paths give identical order marks $q_{j'd}=q_{jd}$ for $d\le f_j$ (h.10, Step 2), hence
identical realised pooled histories for every noise draw and therefore an identical second bracket
in Step 11's decomposition. The first bracket is strictly larger at $j'$ by assumption. So
$U_{j'}(s;k)>U_j(s;k)$, contradicting the optimality of $j$ at $s$. Hence no available flagged
deviation improves, which is sequential optimality of the flagged component.

The converse direction is the honest part. Without h.11 — i.e. if round 2 offers the full interval
$[0,\bar b-B_j^F(s)]$ — date-0 optimality over $\mathcal J$ constrains only those round-2 orders that
appear as the flagged component of some menu element paired with the same pooled path; an order
outside that set is never compared, so a fixed point of $\mathcal T$ can fail item (ii) of card §3 at
the flagged node while satisfying every other item. **Sequential optimality of the flagged component
does not follow from A1–A7 and is not a free consequence of complete contingent plans; h.11 is *a*
sufficient condition that delivers it, and it is a restriction on the round-2 action set rather than
on the menu.** The turn-1 statement of P1 listed "sequential optimality of the flagged component" as
its Hypothesis 6 without content; h.11 is one way of supplying that content.

**Not claimed: that h.11 is the *weakest* such condition (batch-1 audit P1-R2).** An earlier draft
said so, and the claim was not established. The textbook route to sequential rationality at an
unreached node is not a restriction on the action set at all — it is **off-path beliefs**. Card §3(vi)
requires off-path beliefs to be limits of full-support perturbations, and Step 9's perturbation
perturbs **only the plan menu** (each type plays each $j\in\mathcal J$ with weight $\ge1/n$). Round-2
orders outside the menu image are then reached at no $n$, so their limit beliefs are unconstrained by
that perturbation and the modeller may choose them. Whether some admissible choice deters every
off-menu deviation is a genuine question and not an obvious one — a punishing (high) off-path $P^F$
makes the deviation purchase dearer but also raises the takeover-branch value of $Y$ — and **no step
in this proof addresses it**. So: h.11 delivers Step 12; whether an off-path-belief route also
delivers item (ii), and whether it would be weaker, is **open**.

### Part E — the outer map and Brouwer

**Step 13 (h.3 gives a well-defined weakly ordered best-response map; A6's ordering content is a
consequence, not an assumption).**
Fix $k\in\Theta$. Steps 5, 6, 9 and 10 determine the pooled and flagged price families and the
belief system; Step 11 then determines $U_j(s;k)$ for every $j$ and $s$, finite and bounded by h.2.
By h.3 the preferred plan is weakly increasing in $s$, so there is a weakly increasing selection
$j^\star(\cdot;k)$ from $\arg\max_{j\in\mathcal J}U_j(\cdot;k)$. Define
$$
\mathcal T_i(k;\vartheta)\;=\;\inf\bigl\{s\in[\underline s,\overline s]:j^\star(s;k)\ge i+1\bigr\},
\qquad i=1,\dots,J-1,\qquad \inf\emptyset:=\overline s .
$$
Since $\{s:j^\star\ge i+2\}\subseteq\{s:j^\star\ge i+1\}$, the infima satisfy
$\mathcal T_1(k)\le\mathcal T_2(k)\le\cdots\le\mathcal T_{J-1}(k)$, and every component lies in
$[\underline s,\overline s]$ by construction. Hence $\mathcal T(k;\vartheta)\in\Theta$ for every
$k\in\Theta$, including on the collapse faces where consecutive components coincide and the
corresponding plan carries zero probability. **So the "maps $\Theta$ into itself" and
"weakly ordered" halves of h.6 are derived here from h.3's monotone-preferred-plan clause; what
remains genuinely assumed in h.6 is the bracket $[\underline s,\overline s]$ and the continuity of
$\mathcal T$.** Steps 14 and 15 take those two in turn.

**Step 14 (the bracket: derivable in the four-action specialisation, assumed at the card's level of
generality — said plainly).**
In the four-action version of this model that the frozen manuscript works with, the bracket is
proved rather than assumed: there the blockholder's payoff to each action is affine in the
posterior mean $\hat v(s)$ with intercepts that are bounded uniformly over conjectures (prices lie
in a bounded interval and the entry probability lies in $[0,1]$) and with totally ordered slopes,
zero for Exit, one for Hold and Quiet Voice, and strictly more than one for Public Voice; the
engagement cost is continuous, strictly positive and strictly decreasing with full range on the
half-line. Each adjacent indifference condition then equates two affine functions whose slope gap
is nonzero — except the Hold/Quiet pair, where the slopes tie and the comparison reduces to the
strictly decreasing cost schedule meeting a bounded constant — so every indifference signal is
finite and bounded uniformly in the conjecture, and taking the union over the finitely many
adjacent pairs gives one bracket that works for all of them. That argument uses the affine-in-$\hat
v$ payoff form with ordered slopes. Neither **h.14**'s payoff definition nor card §5's A3 imposes that
form on a general finite menu: A3 imposes single crossing and a monotone preferred plan only, and
h.14 fixes the accounting of the payoff without restricting its shape in $\hat v$. (The card imposes
nothing at all here — it carries no blockholder payoff row; card gap, regeneration item.) At the
card's level of generality the common bracket is
therefore **assumed**, and it is the first of the two things h.6 is doing.

**Step 15 (continuity: this is where h.6 assumes rather than derives, and here is exactly what it is
assuming).**
$U_j(s;k)$ is continuous in $k$ for each fixed $(j,s)$: by h.5 the pooled and flagged inner prices
are continuous in the cutoffs, and by Step 4 they enter $U_j$ only through $(\hat v,\pi)$, which are
ratios of integrals over signal intervals with endpoints $k$ and are continuous in $k$ wherever the
conditioning event has probability bounded away from zero; at histories of vanishing probability
the Step 9 perturbation limit supplies the value. **That is continuity in $k$ at fixed $(j,s)$, and it
is not enough**: continuity in $k$ at fixed $s$ together with continuity in $s$ at fixed $k$ is
strictly weaker than continuity in the pair, and it is the joint statement the crossing-point argument
below consumes (batch-1 audit P1-R4). Continuity of $\mathcal T$ in $k$ needs two more
things that the card does not supply:

 (i) *joint continuity*: $(s,k)\mapsto U_j(s;k)$ is continuous on
 $[\underline s,\overline s]\times\Theta$ for each $j$ — **stated as the condition, not inferred from
 the two separate continuities**. It is plausible from the structure (finitely many $j$ by h.2, inner
 prices continuous in $k$ by h.5, and $(\hat v,\pi)$ ratios of integrals over signal intervals with
 endpoints $k$), and what it needs in the signal direction is
 $s\mapsto\bigl(B_j(s,\cdot),b_j^*(s),C_j(s)\bigr)$ continuous, so
 that $s\mapsto U_j(s;k)$ is continuous. Card §4.2 imposes monotonicity on the stake path and
 nothing else; a plan that acquires a block discontinuously at a signal trigger is permitted by the
 card and makes $U_j(\cdot;k)$ jump, at which point the best-response cutoff is a jump point rather
 than a crossing point and moves discontinuously with $k$.

 (ii) *transversality*: for every adjacent pair $(i,i+1)$ and every $k\in\Theta$, the indifference
 set $\{s:U_{i+1}(s;k)=U_i(s;k)\}$ has empty interior. h.3 says the difference crosses zero "at
 most once", which does not exclude an interval on which it is identically zero; on such an
 interval the cutoff is indeterminate, and as the interval opens and closes with $k$ the selection
 $\mathcal T_i$ jumps.

**Under (i) and (ii), continuity of $\mathcal T$ follows from (i)'s joint continuity together
with the strict sign change of $U_{i+1}-U_i$ at each crossing: the sign change locates the crossing
and the joint continuity moves it continuously with $k$. That is a topological argument, not a
calculus one — the implicit function theorem is the wrong tool here, since it would need $U$
differentiable in $(s,k)$ and no hypothesis supplies that (batch-1 audit P1-R4). h.6 assumes the
conclusion instead: it asserts continuity of
$\mathcal T$ directly. That is the single largest assuming-rather-than-deriving step in this proof,
and (i)+(ii) is the weakest pair of conditions I can name that would replace it.** Note also that
(i) is not independent of h.7: a stake path that is flat on a signal interval destroys injectivity
there, which is the turn-2 audit's L2-R1 finding seen from the other side, so the card cannot buy
continuity by weakening monotonicity.

**Step 16 (Brouwer).**
By Step 1, $\Theta$ is nonempty, compact and convex. By Step 13, $\mathcal T(\cdot;\vartheta)$ maps
$\Theta$ into $\Theta$. By h.6 (as decomposed in Steps 14–15), $\mathcal T(\cdot;\vartheta)$ is
continuous on $\Theta$. Brouwer's fixed-point theorem gives $k^\star\in\Theta$ with
$k^\star=\mathcal T(k^\star;\vartheta)$. The fixed point may lie on a collapse face, in which case
the corresponding plan carries zero probability; card §3's weak inequalities admit this, and it is
the shape the frozen manuscript's baseline takes when the passive action collapses.

**Step 17 (assembling the six items of card §3).**
Take $k^\star$ from Step 16 and check the definition item by item.
(i) *Weakly ordered cutoff vector.* $k^\star\in\Theta$ by Step 16, and $j_{k^\star}$ of Step 1 is
the induced plan map.
(ii) *Sequentially optimal pooled and flagged components.* Pooled: no decision node after date 0
(Step 11). Flagged: Step 12 under h.11. Date-0 plan optimality: $k^\star$ is a fixed point of
$\mathcal T$, so $j_{k^\star}(s)\in\arg\max_j U_j(s;k^\star)$ for every $s$ off the finitely many
cutoff points, and at the cutoff points the two adjacent plans are indifferent (Step 13's
construction), so either choice is optimal.
(iii) *Bayes-consistent on-path beliefs.* Step 9 for pooled histories of positive probability under
$k^\star$; Step 10 for flagged tuples, where injectivity makes the posterior the point mass on
$\iota_F(\sigma_F)$.
(iv) *Competitive pooled and flagged prices at their fixed points.* Step 5 for the finite pooled
family, Step 6 for the measurable flagged family, both evaluated at the beliefs of (iii), both
solving $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ by Step 4.
(v) *Bidder-entry rule.* Card §4.3's $p(\mathcal I)$ is the entry probability implied by the same
$(P,\pi)$ at each control-node information set, by Step 4's derivation.
(vi) *Off-path beliefs as limits of full-support perturbations.* Steps 9 and 10.
All six hold, so the assembled object is a cutoff perfect Bayesian equilibrium.

**Step 18 (a strengthening that is not part of the claim: Kakutani removes h.6's continuity half).**
Define instead the best-response correspondence
$\mathfrak T(k)=\{k'\in\Theta:k'\text{ represents some optimal weakly increasing plan selection at
}k\}$. It is nonempty by h.3; its values are convex, because at an indifference plateau the
admissible values of a component form an interval and the ordering constraints cut the product of
those intervals by half-spaces; its values are compact, being closed subsets of the compact
$\Theta$; and its graph is closed by the maximum theorem, given that $U_j(s;k)$ is jointly
continuous in $(s,k)$ — which is exactly what Step 15(i) now states as a condition rather than
deriving. Kakutani's theorem then gives a fixed point without
Step 15(ii) and without h.6's continuity clause. This removes the transversality condition but
neither Step 15(i) nor Step 14's bracket. Card §3 fixes the Brouwer route for P1, so this is
recorded as a remark; see NOT CLAIMED.

### Part F — A8 and both cells on path

**Step 19 (A8 gives positive mass to both cells).**
At $k^\star$, h.9 makes $\mathcal C_F=\{D=1\}$ and $\mathcal C_P=\{D=0\}$ exclusive and exhaustive,
so $\Pr(\mathcal C_F)=\Omega(\kappa,\tau,T)$ and $\Pr(\mathcal C_P)=1-\Omega(\kappa,\tau,T)$ with
$\Omega$ evaluated under the equilibrium plan map $j_{k^\star}$. h.8 asserts
$0<\Omega<1$, so both probabilities are strictly positive: both cells are reached with positive
probability under the equilibrium, that is, both are on path. This is also the condition under
which card §4.4's $M_F$ and $M_P$ are defined, which is what the cell decomposition needs; h.4's
$D=1\Rightarrow a=1$ makes the flagged cell an engagement cell throughout.

**Step 20 (what A8 does and does not do — said plainly).**
h.8 is a restriction on an *equilibrium object*: $\Omega$ is computed at $k^\star$, not from
primitives. No step above rules out $\Omega(k^\star)\in\{0,1\}$, and P1 therefore does not produce
an equilibrium satisfying h.8; it states that if the constructed equilibrium satisfies h.8 then
both cells are on path. Read literally, Step 19 is close to a restatement of h.8, and its content
is the consistency check that h.9's partition is non-degenerate at the fixed point.

The reformulation that gives h.8 something to bite on: suppose in addition (a) **h.15** — the
engagement flags $a_j$ are $1$ exactly on an upper set of the ordered menu — (b) $\partial_s B_j\ge0$
on Voice plans (card §4.2), and (c) h.13. Of these only (b) is card-backed; (a) and (c) are both
[ADDITION]s, numbered as h.15 and h.13 and cited here, which is the one step that consumes them. Then
the flagged set
$\{s:a_{j_{k^\star}(s)}=1\text{ and }B_{j_{k^\star}(s)}(s,H-T)\ge\tau\}$ — the equivalence
$f_j\le H\iff B_j(s,H-T)\ge\tau$ is h.9 — is an upper interval of signals: the first condition is
an upper set because $j_{k^\star}$ is weakly increasing and h.15; within it, $s\mapsto
B_{j_{k^\star}(s)}(s,H-T)$ is weakly increasing because it increases in $s$ at fixed plan by (b) and
increases across plans by (c). Writing $s_F(k^\star)$ for the infimum of that upper interval,
$\Omega=1-\Phi_s\bigl(s_F(k^\star)\bigr)$ with $\Phi_s$ the signal c.d.f., and h.8 is equivalent to
$s_F(k^\star)$ being finite and strictly above $-\infty$. **Conditions (a) and (c) are h.15 and h.13,
neither of which is in the card**: the card orders the menu by aggressiveness without tying that order
either to the engagement flags (h.15) or to the stake path (h.13), so without them the flagged set
need not be an interval and $\Omega$ need not be a single-threshold object.

$\blacksquare$

---

## WHERE IT FAILS

1. **h.5 fails at the flagged layer only, and h.12 does not rescue it.** Let $m_0<0$ be large enough
   in absolute value that $\bar m=m_0+\Delta_m<0$ on the flagged cell. Then Step 7(i) breaks, roots
   below $A$ become possible, and $\varrho$ can dip below zero, rise, and fall again — three roots at a
   positive-measure set of flagged tuples. A measurable selection still exists (the root
   correspondence is closed-valued and measurable, so Kuratowski–Ryll-Nardzewski applies), but it is
   no longer unique. Distinct selections give distinct $\mathcal T$ and distinct fixed points, so P1
   becomes selection-dependent; worse for the paper, a selection that varies with $\kappa$ destroys
   the flagged-cell invariance that L2 needs, since L2's Step-9 analogue relies on the fixed point
   being pinned rather than picked.
2. **h.11 fails: round 2 offers orders the menu does not generate.** Suppose the model gives the
   blockholder the full interval $[0,\bar b-B^F]$ in round 2 rather than the plan-generated set
   $\mathcal Q_j(s)$. Take
   $\mathcal J=\{\text{Exit},\text{Hold},\text{one Voice plan}\}$ with the Voice plan's terminal
   target $b^*(s)$ chosen for its pooled-execution properties. The round-2 problem
   $\max_{Q}\ b^*Y-P(F,Q)Q$ has a first-order condition that the single plan-generated
   $Q^F=b^*-B^F$ generically does not satisfy, and the improving $Q'$ is now available. The fixed point of $\mathcal T$ then exists and satisfies items
   (i), (iii)–(vi) of card §3 but fails item (ii) at the flagged node: it is a date-0 equilibrium,
   not a PBE. This is the concrete case in which P1's claim is false as stated under A1–A7 alone.
3. **h.6's continuity fails through an indifference plateau (Step 15(ii)).** Let the engagement cost
   $C_j(s)$ be constant on a signal interval $[s_1,s_2]$ and let the conjecture be such that
   $U_{i+1}(\cdot;k)-U_i(\cdot;k)\equiv 0$ there. Every $k_i\in[s_1,s_2]$ represents a best
   response, and as $k$ moves the plateau opens and closes, so $\mathcal T_i$ jumps and Brouwer does
   not apply. The Kakutani route of Step 18 survives this case; the Brouwer route the card fixes
   does not.
4. **h.6's continuity fails through a discontinuous stake path (Step 15(i)).** A Voice plan that
   acquires a fixed block the moment $s$ exceeds a trigger $s_0$ is permitted by card §4.2's
   monotonicity-only restriction. Then $B_j(\cdot,d)$, $b_j^*$, $B^F$, $Q^F$ and $U_j(\cdot;k)$ all
   jump at $s_0$; the best response is defined by a jump rather than a crossing and $\mathcal T$ is
   not continuous. The same plan makes the flagged tuple constant on the flat stretches on either
   side of $s_0$, so h.7's injectivity fails there too — the two failures are one failure.
5. **h.3 fails: two crossings.** Suppose the engagement cost is non-monotone in $s$, so that Exit is
   optimal at very low signals, Hold in a middle band, Quiet Voice above it, but Exit again in a
   thin band where an execution cost spikes. The preferred plan is not weakly increasing, the best
   response is not a cutoff partition, and $\Theta$ is the wrong domain: Step 13's construction
   returns a vector that does not represent the best response, so its fixed point is not an
   equilibrium.
6. **h.8 fails at the fixed point.** Set $\tau>\bar b$. No plan can cross, so $D\equiv 0$,
   $\Omega(k^\star)=0$, the flagged cell is off path, $M_F$ is undefined, and Steps 6, 10 and 12 are
   vacuous. The equilibrium of Step 17 still exists; only the "both cells on path" half of the
   claim fails. Symmetrically, a menu on which every plan is Voice and crosses gives $\Omega=1$ and
   an empty pooled cell.

---

## LABEL CLAIMED

**CONJECTURE.** Three independent reasons, any one of which is sufficient.

1. Card §7: a label moves only on an executed check or an independent re-derivation, never on
   prose. This document is prose. The card's ledger carries P1 at CONJECTURE and this proof does not
   touch the ledger.
2. The proof consumes hypotheses that are not in the card — h.11 (the round-2 action set is the
   plan-generated set), h.12 ($m_0\ge0$) and h.14 (the blockholder payoff, which the card has no row
   for at all) — plus h.13 and h.15 for the Step 20 reformulation. Card §5 would have to absorb h.11
   and h.12, and the card would have to gain a blockholder payoff row for h.14,
   before "under A1–A7" in the card's P1 row is an accurate antecedent. As written, the card's P1
   row overstates what A1–A7 deliver, because sequential optimality of the flagged component
   (item (ii) of card §3) is not among their consequences (Step 12, WHERE IT FAILS 2).
3. The proof cites h.9 = D1, which itself carries the label CONJECTURE. P1 inherits that
   conditionality regardless of how this document is audited.

The intended final label remains PROVED, conditional on the card absorbing h.11, h.12 and h.14's
payoff row, and on D1 clearing its own re-derivation.

---

## NUMERICAL CHECK REQUEST

**Grid.** $\kappa\in\{0.05,0.10,\dots,0.95\}$ (19 nodes); $\tau\in\{0.03,0.05,0.075,0.10\}$;
$T\in\{1,2,5,10,H\}$; at each node also $\pm20\%$ perturbations of $\sigma_\xi$, of $\Delta_m$, and
of the engagement-cost scale, one at a time. All prices and premia reported in premium percentage
points, not normalised indices.

1. **Existence of the outer fixed point (Step 16).** At each node run a 30-seed multistart on
   $\Theta$ for $k=\mathcal T(k;\vartheta)$ and report
   $\min_{\text{seeds}}\lVert k-\mathcal T(k;\vartheta)\rVert_\infty$. *Predicted sign and
   magnitude:* at every node at least one seed converges with residual $<10^{-10}$; the median
   across nodes of the best-seed residual is predicted below $10^{-12}$. No prediction that seeds
   agree with one another, and disagreement across seeds is **not** a failure of this check.
2. **Inner root: existence, uniqueness, transversality (Step 7).** At each node and each
   information set — the finite pooled list of Step 3 and a sample of 5{,}000 flagged tuples drawn
   from the equilibrium flagged law — evaluate $\varrho(P)=\mathcal P_{\mathcal I}(P)-P$ on a
   2{,}001-point grid spanning $[\hat v-5\sigma_v,\ \hat v+5\sigma_v+m_1]$ and count sign changes.
   *Predicted sign and magnitude:* exactly one sign change at every information set; the reported
   fraction of information sets with two or more sign changes is predicted to be $0.000$ (upper
   bound $10^{-4}$ allowing grid artefacts). At the root, $\varrho'<0$ strictly, with
   $|\varrho'|\ge 1-p\ge 0.10$ at a baseline-like $p\approx0.85$; report the fifth percentile of
   $|\varrho'|$ across flagged tuples and predict it exceeds $0.05$.
3. **The flagged family is single-valued, measurable and non-expansive in the belief (Steps 6, 8).**
   Over the same 5{,}000 flagged tuples, regress the solved $P^F$ on $\hat v(\sigma_F)$ and also
   compute the analytic slope
   $\partial P/\partial\hat v=(1-p)/\bigl[1-p+|p'(P)|(P+m_1-\hat v-\Delta_V)\bigr]$.
   *Predicted sign and magnitude:* the map $\hat v\mapsto P^F$ is single-valued and strictly
   increasing with slope in $(0,1]$; at a baseline-like $p\approx0.85$ and
   $|p'|(P+m_1-\hat v-\Delta_V)\approx0.10$ the slope is predicted at
   $0.15/0.25=0.60\pm0.10$; the maximum absolute discrepancy between the numerical slope and the
   analytic formula is predicted below $10^{-6}$. Any tuple where two distinct $P^F$ values are
   returned by different solver initialisations refutes the Step 6 family.
4. **Flagged sequential optimality — a direct test of h.11 (Step 12).** At each node, for each
   on-path flagged $(j,s)$ in the sample, re-optimise the round-2 order over a 401-point grid on
   $[0,\bar b-B^F]$ holding the flagged pricing schedule at its equilibrium family, and report
   $\max_{Q'}\bigl[\text{continuation}(Q')-\text{continuation}(Q_j^F)\bigr]$. *Predicted sign and
   magnitude:* the gain is $\ge 0$ by construction (the grid contains $Q_j^F$ up to grid
   resolution). The sharp prediction is conditional: **under h.11 — round 2 restricted to the
   plan-generated set $\mathcal Q_j(s)$ — the maximum gain is $0$ to within $10^{-9}$ premium
   percentage points at every tuple; with round 2 opened to the full interval, a strictly positive
   gain of order $10^{-2}$ premium percentage points appears at a positive fraction of tuples.**
   Reporting a positive gain on the full interval therefore measures what h.11 is buying on that
   menu; it does not refute P1.
5. **Both cells on path (Step 19), and the threshold reformulation (Step 20).** Report
   $\Omega(k^\star)$ and, where h.13 holds by construction of the menu, the implied threshold
   $s_F(k^\star)$ with $\Omega=1-\Phi_s(s_F)$. *Predicted sign and magnitude:* $0<\Omega<1$ at every
   interior $(\tau,T)$ node, with $\Omega$ weakly increasing as $\tau$ falls and as $T$ falls;
   $\Omega$ in the range $0.03$ to $0.30$ at the card §4.4 calibration nodes; $\Omega=0$ exactly at
   $\tau>\bar b$. The two reported $\Omega$ values — direct simulation and $1-\Phi_s(s_F)$ — are
   predicted to agree to within $10^{-10}$ wherever h.13 holds, and to disagree wherever the menu
   violates h.13, which makes the check a test of h.13.

---

## NOTATION DELTA

Symbols used above that are not in card §4. Nothing in card §4 is renumbered or re-keyed; $\kappa$
is noise-trading intensity throughout, bare $\lambda$ does not appear, upright $T$ is the window and
$\mathcal T$ is the best-response map.

| Symbol | Meaning | Collision check |
|---|---|---|
| $j_k(s)=1+\#\{i:k_i\le s\}$ | the plan selected at signal $s$ under conjecture $k$ | card §4.2's $j$ is the plan index; the subscript $k$ marks the induced map |
| $U_j(s;k)$ | blockholder's conditional expected payoff to plan $j$ at signal $s$ under conjecture $k$; the object **defined at h.14** with the conjecture displayed | matches the frozen manuscript's blockholder utility; **never a bare $U$**. **Card gap:** the card has no blockholder payoff row and no §2.10 — the definition is h.14's, faithful to `threads/thread1_turn1_answer.md` §2.10. Regeneration item |
| $\mathcal C_j^{\mathrm{trade}}$ | plan $j$'s execution outlay, the prices paid across the pooled and flagged rounds (h.14) | calligraphic and always subscripted $j$ with the superscript written, so it is clear of card §4.4's $C_h$ (chord), $C_\tau/C_T$ (composition ratios) and $\mathcal C_F/\mathcal C_P$ (cells); **never a bare $C$**. Not in the card — see h.14 |
| $C_j(s)$ | plan $j$'s engagement cost at signal $s$ (h.14) | named in card §4.4's $C$-overload note but carried by no card row; subscripted, never bare |
| $\mathcal G_F(\hat v)$ | the flagged inner root as a function of the belief: the unique $P$ solving $\mathcal P(P)=P$ at $(\hat v,\pi=1)$ (Step 6b) | **replaces the bare $g$ of an earlier draft**: the turn-2 ruling reserves $g$ for L3's mean-value form, and card §4.5 carries $g_r^{PE}$. $\mathcal G$ has zero occurrences in card §4 and in the other batch-1 proofs; subscript $F$ matches $\mathcal C_F$, $\sigma_F$, $\iota_F$ |
| $s_1,s_2$ | endpoints of the indifference-plateau signal interval in WHERE IT FAILS 3 | **replaces $[\alpha,\beta]$**: $\beta$ is card §4.1's Gaussian projection coefficient, which this file also uses (Steps 6, 10), and one symbol may not carry both meanings. $s$ is the card's signal, so numbered signal values are in-family |
| $\mathcal P_{\mathcal I}(P)$ | the inner pricing map at information set $\mathcal I$, whose fixed point is card §4.3's $P(\mathcal I)$ | calligraphic $\mathcal P$ is unused in the card and has zero occurrences in the frozen manuscript |
| $\varrho(P)=\mathcal P_{\mathcal I}(P)-P$ | inner pricing residual | $\varrho$ has zero occurrences in the card and in the frozen manuscript. It is used here **because $\psi$ is not available**: card §8 rule 4 reserves $\psi$ for D7 pivotality. Appears only in Steps 7–8 and in the WHERE-IT-FAILS and check items that refer back to them |
| $\phi$ | unit normal density, paired with card §4.3's $\Phi$ | appears only inside $p'(P)$ at Step 7(iii) |
| $\bar m(\mathcal I)=m_0+\pi(\mathcal I)\Delta_m$ | expected premium at $\mathcal I$; equals $m_1$ on $\mathcal C_F$ | built from card §4.1's $m_0,\Delta_m$; the frozen manuscript writes the same object $\bar m(\pi)$ |
| $\hat v(\mathcal I)=\mathbb E[v\mid\mathcal I]$ | posterior mean of $v$ at $\mathcal I$ | the frozen manuscript's posterior-mean symbol, same meaning |
| $A=\hat v+\pi\Delta_V$ | no-takeover branch value at $\mathcal I$; proof-local to Steps 7–8 | card §4.4's $A_0,A_{1/2},A_1$ carry subscripts and belong to A($\tau$); this $A$ never appears subscripted |
| $[\underline s,\overline s]$ | the common signal bracket underlying $\Theta$ | card §4.5 posits $\Theta$ compact without naming its bracket |
| $\sigma_F$ | a generic value of the flagged tuple $\mathsf S_F=(B^F,Q^F,a{=}1)$ of card §4.6 | lowercase, always subscripted $F$; distinct from the variances $\sigma_v,\sigma_\varepsilon,\sigma_\xi$, which never appear without their own subscripts |
| $\iota_F$ | the Borel inverse of $(j,s)\mapsto\sigma_F$ on the flagged set | card §4.6 records $\iota_F$ as free |
| $\mathfrak T(k)$ | the best-response *correspondence* of Step 18 | fraktur, used only in Step 18; $\mathcal T$ remains the single-valued map |
| $s_F(k)$ | infimum of the flagged signal set at conjecture $k$ (Step 20) | subscript $F$ matches $\mathcal C_F$ |
| $\Phi_s$ | c.d.f. of the signal $s$ | $\Phi$ alone remains the unit normal c.d.f. of card §4.3 |
| $1/n$ | size of the full-support perturbation in Steps 9–10 | no Greek symbol introduced; $\varepsilon$ is reserved for card §4.1's signal noise |

---

## NOT CLAIMED

1. **Uniqueness of the equilibrium.** Not claimed, in any form: not uniqueness of $k^\star$, not
   local uniqueness, not uniqueness of the induced price system, not uniqueness within a collapse
   face. Brouwer is an existence theorem and nothing above bounds $\lVert D_k\mathcal T\rVert$. Card
   §3 and §9 both disclaim uniqueness and this proof does not weaken that.
2. That A6 is derivable at the card's level of generality. Steps 14–15 name what it assumes; they do
   not prove it. In particular the common bracket and the transversality of adjacent indifference
   are assumed, not shown.
3. That the Step 18 Kakutani route is part of P1. It is a remark. Card §3 fixes the Brouwer route
   for P1's statement, and the correspondence-valued argument still needs Step 15(i) and Step 14's
   bracket.
4. That h.7's injective form is **satisfiable** on any plan menu. The turn-2 audit records this as
   open and as Thread 2's target; Steps 6 and 10 use injectivity without exhibiting a menu on which
   it holds.
5. That h.11 holds on any particular menu, or that any menu in the calibration satisfies it.
   NUMERICAL CHECK 4 is designed to measure what it buys, not to assume it. **Nor is h.11 claimed to
   be the weakest condition delivering item (ii)** — Step 12 says why: the off-path-belief route
   permitted by card §3(vi) is untouched by Step 9's menu-only perturbation and is not analysed
   anywhere in this file. Open.
6. That an equilibrium satisfying A8 exists at any parameter. Step 20 says this plainly: h.8 is
   imposed at the fixed point, and no step produces a fixed point with $\Omega\in(0,1)$.
7. That $k^\star$ is interior, differentiable in $\vartheta$, or that any comparative static in
   $(\kappa,\tau,T)$ follows from existence. The GE certification machinery of card §4.5 is
   untouched here.
8. That the equilibrium is in pure strategies at the cutoff points themselves; at a cutoff the two
   adjacent plans are indifferent and either choice is optimal, a measure-zero indeterminacy that
   this proof does not resolve.
9. Anything about welfare, optimal $(\tau,T)$ design, endogenous filing before the deadline, or
   noisy flagged-round trading. Card §9's disclaimers stand unchanged.
10. That the frozen manuscript's four-action results transfer to the $J$-plan menu. Step 14 borrows
    an *argument shape* from it and says explicitly that the shape needs a payoff form the card does
    not impose.
11. That Step 15(i)'s joint continuity is derived. It is **stated as a condition**: continuity in $k$
    at fixed $(j,s)$ is established in Step 15, continuity in $s$ at fixed $k$ is what (i) asks of
    the card, and the conjunction of the two is strictly weaker than the joint statement the
    crossing-point argument consumes. Nor is any differentiability of $U$ in $(s,k)$ claimed — the
    crossing argument is topological, not an implicit-function-theorem argument.
12. That card §4.3's $Y$ row has been disambiguated. Step 5 records the two readings of the $P$ inside
    the takeover branch and shows the step's conclusion survives both; pinning the row is a card
    edit and a regeneration item, not a claim of this file.

---

## Repairs applied (2026-08-21, batch-1 audit)

Source: `threads/2026-08-21_batch1_proofread_audit.md` (Opus proof-read, verdict PASS, no failing
steps), together with the orchestrator's binding adjudications of the same date. Every change below
is a citation, a hypothesis restated in a satisfiable form, a hypothesis lift, a wording fix or a
notation declaration. **No claim or step conclusion was altered in substance, and no step was
renumbered**; three hypotheses were added at the end of the list (h.14, h.15) or restated in place
(h.11). The label is untouched: P1 remains CONJECTURE.

| Finding | Change made |
|---|---|
| **P1-R1** | h.11's **primary (closure) form is struck** — it is jointly unsatisfiable with h.2 by cardinality, as the hypothesis now records with the argument written out. The definitional reading is **the** hypothesis: the round-2 action set **is** the plan-generated set $\mathcal Q_j(s)$. It is no longer called a closure condition. Step 12 restated on that reading (it already ran on it), together with WHERE IT FAILS 2, the CLAIM's hypothesis summary, LABEL CLAIMED 2, NOT CLAIMED 5 and NUMERICAL CHECK 4. |
| **P1-R2** | "h.11 is the weakest condition that delivers it" **withdrawn**. Step 12 now says h.11 is *a* sufficient condition and sets out the untaken off-path-belief route (card §3(vi); Step 9 perturbs only the plan menu, so off-menu round-2 orders are reached at no $n$ and their limit beliefs are unconstrained), declaring the question open. Recorded again in NOT CLAIMED 5. |
| **P1-R3** | Step 10 now says which reading its "on path and off" stands on: it covers $(j,s)$ pairs the conjecture does not select, and tuples outside the image of $(j,s)\mapsto\sigma_F$ do not arise **because of h.11**, cited there. Step 17(vi) inherits the pinning on that reading only. |
| **P1-R4** | Step 15(i) restated as **joint continuity of $(s,k)\mapsto U_j(s;k)$, a stated condition** — with the explicit note that separate continuity in each argument is strictly weaker — and the boxed conclusion now runs on joint continuity plus the strict sign change, a **topological** argument; the implicit function theorem is named as the wrong tool (it needs differentiability nobody supplies). Step 18's Kakutani remark corrected to match. New NOT CLAIMED 11. |
| **P1-R5** | Step 20's unnumbered condition (a) lifted into **h.15 [ADDITION]** — engagement flags $1$ exactly on an upper set of the ordered menu — cited at Step 20, the one step that consumes it, with (b) card-backed and (c) = h.13 marked as such. |
| **P1-R6** | All three "card §2.10" citations removed. The blockholder payoff is now **h.14 [ADDITION — CARD GAP]**, a numbered definition of this proof faithful to `threads/thread1_turn1_answer.md` §2.10, with "the card carries no blockholder payoff row, no $\mathcal C_j^{\mathrm{trade}}$; card gap, regeneration item" flagged inline at the hypothesis, at Step 11, at Step 14 and in the NOTATION DELTA. Recommendation to absorb the row into the card recorded at h.14. |
| **P1-R7** | NOTATION DELTA completed. (a) The bare $g$ of Step 6 is renamed **$\mathcal G_F$** (zero card §4 hits; $g$ stays reserved for L3's mean-value form per the turn-2 binding ruling) and declared. (b) WHERE IT FAILS 3's $[\alpha,\beta]$ renamed **$[s_1,s_2]$**, so $\beta$ carries only card §4.1's Gaussian projection meaning; declared. (c) $\mathcal C_j^{\mathrm{trade}}$ and $C_j(s)$ declared, as consequences of P1-R6. |
| **P1-R8** | Step 5 split in two: (a) the pooled **control-node** cell, a genuine fixed point of Step 4's map under h.5; (b) intermediate dates $d<H$, a **tower-property** conditional expectation of already-solved control-node values with no self-reference. Both readings of card §4.3's $Y$ row are recorded, the step's conclusion is shown to survive either, and the ambiguity is flagged as a regeneration item (also NOT CLAIMED 12). |

Not applied here, by scope: P1-O1 … P1-O5 are OBSERVATIONs, not REPAIRs.

### FILE: proofs/T1_proof.md

# T1 — Partition attenuation theorem (fixed policies)

**Ticket 26 (T2f). Written against `research/model_v4/MODEL_CARD.md`, version stamp
2026-08-21 · commit `a175202`+** (re-stamped in the 2026-08-21 retry round; the four citations
that read A7's injective satisfiability as open are re-pointed to §5's ticket-24 note, which
records it as **resolved**, and the §4.2 A7′ row is now cited where it bites). Card §4 notation is
binding; the answer template is card §8 rule 6. Upstream results are cited by their card-ledger IDs (D1, L1, L2, L3, L4) and, where the
L3 and L4 writers amended their statements on landing, by the amended statement as quoted in
HYPOTHESES below.

---

## CLAIM

At fixed plan and cutoff policies, with $0<\Omega<1$ and $\mathcal S_P>0$:

**(A) Factorisation.** The premium's liquidity-sensitivity factors exactly into a weight and a
pooled-cell part,
$$
\mathcal S(\kappa,\tau,T) \;=\; \bigl(1-\Omega(\tau,T)\bigr)\,\mathcal S_P(\kappa,\tau,T),
$$
and the same factorisation holds for the total-variation aggregate of $\Delta^{\mathrm{act}}$
over any $\kappa$-grid, with no differentiability required.

**(B) Threshold margin — attenuation.** For $b_0<\tau'<\tau$ at a common window $T$,
$$
\frac{\mathcal S(\kappa,\tau',T)}{\mathcal S(\kappa,\tau,T)} \;=\; W_\tau\,C_\tau \;\le\; 1 ,
\qquad
W_\tau=\frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)},\quad
C_\tau=\frac{\mathcal S_P(\kappa,\tau',T)}{\mathcal S_P(\kappa,\tau,T)} ,
$$
because **both** ratios lie in $[0,1]$: $W_\tau\le 1$ by L4's first leg, $C_\tau\le 1$ by L4's
third leg **under A($\tau$) and A(br)** — A(br) as the L4 writer stated it, plus the comparability
clause (br-v) that this file adds as H17. No dominance condition is needed at this margin.

**(C) Window margin — an iff, and no sign.** For $T'<T$ at a common threshold $\tau$, with
$W_T=\bigl(1-\Omega(\tau,T')\bigr)/\bigl(1-\Omega(\tau,T)\bigr)$ and
$C_T=\mathcal S_P(\kappa,\tau,T')/\mathcal S_P(\kappa,\tau,T)$,
$$
\mathcal S(\kappa,\tau,T')\le \mathcal S(\kappa,\tau,T)
\quad\Longleftrightarrow\quad
W_T\,C_T\le 1 .
$$
Here $W_T\le 1$ is proved (window tightening weakly raises $\Omega$, from D1's clock
equivalence and the monotone Voice stake path), and $C_T$ is **unsigned** by every hypothesis
maintained here. Under a smooth window interpolation the product criterion is the integrated
form of the local criterion
$$
\frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P}\;\le\;\frac{\Omega_{r_T}}{1-\Omega},
\qquad r_T=-T ,
$$
and the two coincide exactly in the infinitesimal limit; the precise sense of "equivalently" is
proved in Steps 20–22. **No unconditional window attenuation sign is claimed, here or anywhere
in this file.**

---

## HYPOTHESES

Every hypothesis below is used; the step that consumes it is named in brackets.

**H1 — Card and stamp.** MODEL_CARD.md, stamp 2026-08-21 · `a175202`+. All symbols carry their
card §4 meanings: $\kappa$ is noise-trading intensity; $\Omega=\Pr(D=1)$ is the unconditional
flagged weight (draft_v2's $\omega_P$), distinct from $\omega_a=\Pr(D=1\mid a=1)$; upright $T$
is the filing window and $\mathcal T$ is the outer best-response map; $\Delta_m>0$.
[all steps]

**H2 — A8, interior crossing, at every policy compared.** $0<\Omega(\kappa,\tau,T)<1$ at
$(\tau,T)$, at $(\tau',T)$ and at $(\tau,T')$. [Steps 1, 6, 9, 10, 12, 13, 15, 16, 18, 20, 21]

**H3 — L1 (card ledger, verbatim).** *"Whenever $0<\Omega<1$,
$\Delta^{\mathrm{act}}=\Omega M_F+(1-\Omega)M_P$; at $\Omega=1$ it degenerates to
$\Delta^{\mathrm{act}}=M_F$ and at $\Omega=0$ to $\Delta^{\mathrm{act}}=M_P$, the null-cell
average being undefined rather than imputed."* [Steps 1, 7]

**H4 — L2 (card ledger, verbatim).** *"At fixed cutoff and execution policies, under A1, A4,
A5, **A7 in its injective form**, the no-feedback timing of §2, and $\Omega>0$:
$(B^F,Q^F,a{=}1)$ makes the pre-filing pooled history conditionally independent of $(v,s,\xi)$
on the flagged set, so the flagged posterior, price, entry probability and $M_F$ are invariant
to $\kappa$."* L2's own hypotheses travel with it and are maintained here, in particular A7 in
its injective form and the no-feedback timing (carried here as H16). The card's **ticket-24 note
(§5, 2026-08-21)** records A7-injective's satisfiability as **resolved**: A7′ (card §4.2) with a
fixed cutoff policy and $\Omega>0$ delivers the **on-path** injective form with an explicit
inverse, and a satisfying menu exists — the pro-rata single-Voice menu (adversarial verdict
SURVIVES WITH REPAIRS). What is *not* resolved, and what Step 3 therefore still rides on, is
whether the menu this model runs on satisfies A7′; the card names the failure boundary and
WHERE IT FAILS 6 carries it. [Steps 3, 7]

**H5 — Fixed policies.** The plan menu $\mathcal J$, the execution policies
$B_j(\cdot,\cdot),\,b_j^*(\cdot),\,Q_j^F(\cdot)$ and the cutoff vector $k$ are frozen: frozen in
$\kappa$, and frozen across the two rules compared at each margin. Nothing in this file permits
$k$ to solve $k=\mathcal T(k;\vartheta)$ afresh at the second rule. [Steps 3, 4, 9, 16, 18]

**H6 — PE-$\Omega$: the flagged weight does not move with liquidity.**
$\Omega(\cdot,\tau,T)$ is **constant in $\kappa$** at every policy compared — the same number at
every $\kappa$ in the maintained set, not merely a map with a vanishing derivative at the $\kappa$
of interest. The derivative form $\partial_\kappa\Omega(\kappa,\tau,T)=0$ is its corollary and is
what Steps 2 and 4 use; the **constancy** is what Step 7 uses, since a vanishing derivative at one
point would not give "$\Omega$ common to two grid nodes". Step 5 derives constancy outright, so
nothing is lost by stating the hypothesis in the stronger form. This is a **hypothesis of the
partial-equilibrium comparison**, not a property of the disclosure rule; Step 5 records why it
is available under H5 and why it fails in general equilibrium. [Steps 2, 4, 5, 7]

**H7 — $\kappa$-differentiability of the pooled cell premium.** $\kappa\mapsto M_P(\kappa,\tau,T)$
is differentiable at the $\kappa$ of interest, at every policy compared. Used only for the
derivative statements; Step 7's total-variation statement does not use it. [Steps 2, 6]

**H8 — Non-degenerate pooled sensitivity.** $\mathcal S_P>0$ at every policy that appears in a
denominator: at $(\tau,T)$ for Part B and at $(\tau,T)$ and $(\tau,T')$ for Part C, and on the
whole interpolating interval for Steps 20–22. [Steps 6, 9, 15, 18, 20, 21]

**H9 — D1 (card ledger, verbatim).** *"$D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is **measurable**
and maps every control-node history into exactly one cell; for every Voice plan
$f_j\le H \iff B_j(s,H-T)\ge\tau$; and each flagged history yields $B^F, R_d, R, J$ with
$P^F-P_{c^-}^P=R+J$."* [Steps 5, 16]

**H10 — Monotone Voice stake path, and the maintained crossing configuration.** Card §4.2: for
Voice plans $\partial_d B_j\ge 0$; A4: only Voice plans cross the threshold in the core; card
§4.1: maintained $b_0<\tau$, and for the threshold comparison $b_0<\tau'<\tau$. [Steps 16, 10]

**H11 — A($\tau$) at both compared policies** (= A(br) clause (br-i)). The pooled posterior law
has the symmetric ternary representation
$\mathbb E[h]=A_0(\kappa)h(0)+A_{1/2}(\kappa)h(\bar\pi/2)+A_1(\kappa)h(\bar\pi)$ with
$A_0'=A_1'=A'_\kappa$, $A_{1/2}'=-2A'_\kappa$; maintained orientation $C_h(\bar\pi)\le 0$ with
$\lvert C_h\rvert$ weakly increasing in $\bar\pi$. **Ruling on $\bar\pi$ (orchestrator, binding):**
$\bar\pi$ is the **upper support point** of the pooled engagement posterior in this
representation, *not* the pooled engagement share. The share is $\mathbb E[\Pi_\kappa]$, which is
$\kappa$-invariant under A($\tau$) and lies strictly below $\bar\pi$ in any non-degenerate case.
[Steps 8, 11]

**H12 — L3 (as landed by the L3 writer; amended mean-value form).** *Under A($\tau$), the pooled
cell's interior $\kappa$-motion is proportional to $C_h(\bar\pi)$ — exactly
$\partial_\kappa\mathbb E[h]=A'_\kappa\cdot C_h(\bar\pi)$ — and
$C_h(\bar\pi)=\tfrac14\bar\pi^{2}g''(\zeta)$ exactly for some $\zeta\in(0,\bar\pi)$
(mean-value form), vanishing as $\bar\pi\downarrow 0$.* The L3 writer declares **OPEN** whether
the two-round pooled cell satisfies A($\tau$); that openness is inherited by every conclusion
here that passes through H11 or H12, i.e. by the whole of Part B. [Steps 8, 11]

**H13 — A(br), the chord–sensitivity bridge (quoted verbatim from the L4 writer).**

> **A(br) — Chord–sensitivity bridge.** For the two compared thresholds $\tau'<\tau$ at fixed
> policies:
> **(br-i) Representation at both policies:** A($\tau$)'s symmetric ternary representation holds
> for the pooled class under $\tau$ and under $\tau'$, with chord endpoints
> $\bar\pi(\tau),\bar\pi(\tau')$ and weight-derivative coefficients $A'_\kappa(\tau),A'_\kappa(\tau')$.
> **(br-ii) $\kappa$-localisation:** at fixed policies all $\kappa$-dependence of $M_P$ sits in
> the A($\tau$) weights; the three support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$ as
> a function of the posterior do not move with $\kappa$; hence
> $\partial_\kappa M_P=\Delta_m\cdot A'_\kappa\cdot C_h(\bar\pi)$ exactly, with no
> composition-through-$\kappa$ remainder.
> **(br-iii) Coefficient stability across the threshold margin:**
> $\lvert A'_\kappa(\tau')\rvert\le\lvert A'_\kappa(\tau)\rvert$.
> **(br-iv) Endpoint linkage:** the chord endpoint $\bar\pi$ is a weakly increasing function of
> the pooled prior engagement share $\bar\pi_{\mathrm{pr}}=\Pr(a=1\mid D=0)$, the same function
> at $\tau$ and $\tau'$.

A(br) is quantified **over the threshold pair only**. Step 17 records that this is not a
drafting accident and that no window counterpart is assumed. The four clauses above are L4's;
Step 11 item 3 needs a fifth that L4 does not carry, and it is stated separately as H17 rather
than smuggled into this quotation. [Steps 8, 11, 15, 17]

**H14 — L4 (as landed by the L4 writer; amended).** At fixed policies, for $b_0<\tau'<\tau$:
*leg 1*, lower $\tau$ weakly raises $\Omega$, and *leg 2*, lower $\tau$ weakly lowers the pooled
prior engagement share $\bar\pi_{\mathrm{pr}}$ (the share, not the chord endpoint $\bar\pi$ —
the step from share to endpoint is A(br)'s (br-iv)), are **proved outright** (given D1's clock
equivalence and $b_0<\tau'<\tau$);
*leg 3*, lower $\tau$ weakly lowers $\mathcal S_P$, holds **only under A(br)**, and holds **with
equality whenever $C_h(\bar\pi(\tau))=0$** — the L4 writer's own qualifier, carried here because
$C_h=0$ is inside A($\tau$)'s maintained weak orientation and card §5's A($\tau$) row requires it
to be handled explicitly (WHERE IT FAILS case 4). [Steps 10, 11, 15]

**H15 — Smooth window interpolation** (Part C's local form only). There is an open interval
$I\subset\mathbb R$ of window values containing $[T',T]$ and continuously differentiable
extensions $r\mapsto\Omega(r)$ and $r\mapsto\partial_\kappa M_P(r)$ on $\{-t:t\in I\}$, agreeing
with the card's integer-valued objects at $r=-T$ and $r=-T'$, with $\Omega(r)\in(0,1)$ and
$\mathcal S_P(r)>0$ throughout, **and with $r\mapsto\Omega(r)$ weakly increasing on that set**.
Card §4.5 sanctions $r_T=-T$ as the window strictness coordinate; because the card's $T$ ranges
over $\{1,\dots,H\}$, the interpolation is an added hypothesis and is carried as one. The
monotonicity clause is part of the hypothesis and is **not** a consequence of Step 16: Step 16
compares two **integer** windows, so an extension agreeing with the card's objects at $r=-T$ and
$r=-T'$ is otherwise free to dip in between. Requiring it costs nothing — the endpoints already
satisfy it, by Step 16 — and Step 20 therefore cites H15, not Step 16, for $\Omega_{r_T}\ge0$.
[Steps 20, 21, 22]

**H16 — No-feedback timing (card §2, bullet 2), carried as a numbered hypothesis.** There is no
within-window re-optimisation, hence no feedback from realised order flow or realised prices into
the executed path: $B_j(s,d)$ and $q_{jd}(s)$ are functions of $(j,s,d)$ alone and $Q_j^F$ of
$(j,s,\tau,T)$ alone. The card states this in terms and instructs that it be cited as a numbered
hypothesis rather than as background. It also travels inside H4's quoted L2 statement, but Step 5
uses it **independently of L2** — Step 5 derives H6, it does not invoke L2 — which is why it is
numbered here. [Steps 3, 5]

**H17 — (br-v) Comparability of the chord functional across the threshold pair. T1-LOCAL: an
addition beyond L4's A(br).** For the compared thresholds $\tau'<\tau$ at fixed policies, the
chord functional $C_h(\cdot)$ — equivalently the univariate section of the kernel $h$ in its
posterior argument — is **the same function at $\tau$ and at $\tau'$**, so that
$\lvert C_h(\bar\pi(\tau'))\rvert$ and $\lvert C_h(\bar\pi(\tau))\rvert$ are two values of one
functional rather than values of two different functionals.

This clause is **not carried by A(br) as the L4 writer stated it**, and this file does not claim
that it is: (br-i) fixes the representation, the chord endpoints and the weight-derivative
coefficients at the two policies; (br-ii) freezes the support points and the kernel **along
$\kappa$**, not along $\tau$; (br-iii) compares the coefficients; and (br-iv) says "the same
function at $\tau$ and $\tau'$" of the **endpoint map** only, with no counterpart for $h$. Step 11
item 3 nonetheless evaluates one chord functional at two policies, so the premise is used and is
stated here. It is uncomfortable rather than innocuous, and Step 17 says why: at fixed policies a
change in $\tau$ moves which histories are pooled, which moves the pooled price $P$, which enters
$h$ through the entry probability $p$. It is proposed as a fifth clause of A(br) for the card
owner; until A(br) carries it, the threshold leg rests on A($\tau$), A(br) **and** (br-v).
[Steps 11, 15]

**H18 — Threshold-side smoothness** (Part B's local form only; the analogue of H15 at the other
margin). There is an open interval $I_\tau\subset(b_0,\infty)$ of threshold values containing the
compared pair $\tau'<\tau$ such that, at the common window $T$ and the frozen policies of H5:

1. the maps $t\mapsto\Omega(t,T)$ and $t\mapsto\partial_\kappa M_P(\kappa,t,T)$ are continuously
   differentiable on $I_\tau$, equivalently $r_\tau\mapsto\Omega$ and
   $r_\tau\mapsto\partial_\kappa M_P$ are continuously differentiable on $\{-t:t\in I_\tau\}$;
2. $\Omega(t,T)\in(0,1)$ and $\mathcal S_P(\kappa,t,T)>0$ at every $t\in I_\tau$ (H2 and H8
   extended from the two compared policies to the interval); and
3. H13's A(br) together with H17's (br-v) holds for **every** pair $t'<t$ in $I_\tau$, not only
   for the named pair $\tau'<\tau$.

This is an **added hypothesis and is carried as one**, for a sharper reason than H15's. Card §4.1
places no discreteness on $\tau$, so the *domain* is already continuous — what is missing is
smoothness of the maps on it, and the card positively permits its failure. Card §4.2 requires only
**weak** $\partial_sB_j\ge0$ for Voice plans, and the 2026-08-21 A7′ row constrains only the
composed **terminal** target $s\mapsto b^*_{j(s)}(s)$, not the interior date $B_j(s,H-T)$. A flat
stretch of $s\mapsto B_j(s,H-T)$ inside the Voice region therefore puts an **atom** in the law of
the date-$(H-T)$ stake, at which $t\mapsto\Omega(t,T)$ jumps and $\Omega_{r_\tau}$ does not exist.
Clause 1 assumes that away on $I_\tau$; an atomless law of $B_{j(s)}(s,H-T)$ over that range, with
a $C^1$ distribution function there, is sufficient for the $\Omega$ half. Clause 3 is what lets
H14's endpoint legs be read along the interval rather than only at its ends.

H18 is consumed by **Step 15 alone**. No boxed conclusion of this file rests on it: Part B's
conclusion is Step 13, which is finite-difference throughout, and Parts A and C never mention
$r_\tau$. If H18 fails, Step 15 is void and nothing else moves. [Step 15]

---

## PROOF

### Part A — the fixed-policy factorisation

**Step 1 (the identity).** By H2, $0<\Omega<1$ at the policy under consideration, so H3 (L1)
applies and
$$
\Delta^{\mathrm{act}}(\kappa,\tau,T)=\Omega(\kappa,\tau,T)\,M_F(\kappa,\tau,T)
+\bigl(1-\Omega(\kappa,\tau,T)\bigr)M_P(\kappa,\tau,T).
$$

**Step 2 (differentiate in $\kappa$).** Two of the three factors on the right of Step 1 do not
move with $\kappa$ at all: $M_F$ is constant in $\kappa$ by H4 (L2) at fixed policies (H5), and
$\Omega$ is constant in $\kappa$ by H6. Both constancies are established at Steps 3 and 5, neither
of which uses this step, so nothing here is circular. With those two factors constant,
$\kappa\mapsto\Delta^{\mathrm{act}}$ is an **affine image** of $\kappa\mapsto M_P$, which H7 makes
differentiable; hence $\partial_\kappa\Delta^{\mathrm{act}}$ exists and equals
$(1-\Omega)\,\partial_\kappa M_P$. Note which hypothesis does which job: boundedness (A2, card §5)
is not what licenses the differentiation and is not cited for it — boundedness is not
differentiability.

The same computation, written as one term per factor that can carry $\kappa$, reads
$$
\partial_\kappa\Delta^{\mathrm{act}}
=\Omega\,\partial_\kappa M_F+(1-\Omega)\,\partial_\kappa M_P
+(\partial_\kappa\Omega)\,(M_F-M_P),
$$
the three terms being the flagged cell's own motion, the pooled cell's own motion, and the
reallocation of mass between cells. This display is bookkeeping: Steps 3 and 4 record which
constancy kills which term, and it is worth seeing them killed one at a time. The derivative
statement in the previous paragraph is what Part A actually uses.

**Step 3 (the first term is zero).** By H4 (L2), at fixed policies (H5) $M_F$ is invariant to
$\kappa$, so $\partial_\kappa M_F=0$ and the first term of Step 2 vanishes. This is the step at
which L2's own hypothesis stack — A1, A4, A5, A7 in its injective form, the no-feedback timing
of card §2 (H16), and $\Omega>0$ (supplied by H2) — is consumed. If the plan menu violates A7′
(card §4.2), so that A7's injective form is unavailable on it, this step is void and so is
everything after it; the card's ticket-24 note settles that such menus are not the only ones —
a satisfying menu exists — but not that this model's menu is one (WHERE IT FAILS 6).

**Step 4 (the third term is zero).** By H6, $\partial_\kappa\Omega=0$ at fixed policies (H5), so
the third term of Step 2 vanishes. Note what is being discarded: $(M_F-M_P)$ is not assumed
small or signed. The term is removed because its coefficient is zero, not because the cells'
premia are close.

**Step 5 (why H6 is a hypothesis, and what it costs).** Under H5 and H9's clock equivalence,
$D=\mathbf 1\{a_{j(s)}=1,\ B_{j(s)}(s,H-T)\ge\tau\}$, where $j(s)$ is the plan the frozen cutoff
vector assigns to the signal $s$. **H16** (the no-feedback timing of card §2, numbered because
this step uses it independently of L2 — it is deriving H6, not invoking L2) makes $B_j(s,d)$ a
function of $(j,s,d)$ alone — no realised order flow and no realised price enters it — so $D$ is
a function of $s$ alone once the policies are frozen. The law of $s$ carries no $\kappa$ for two
cited reasons together: **A1** (card §5) gives $v$ and $\varepsilon$ independent with strictly
positive variances, and **card §4.1's distributional rows** give $s=v+\varepsilon\sim
N(\mu_v,\sigma_v^2+\sigma_\varepsilon^2)$ with no $\kappa$ in either row — $\kappa$ appears in
exactly one row of the card, the $z_d$ noise-mark law of §4.1 (the $\bar z$ row), which enters observed order flow
$X_d$ and nothing that $D$ depends on. Hence $\Omega=\Pr(D=1)$ is literally the same number at
every $\kappa$: **constant**, which is H6 in the form Step 7 needs, with
$\partial_\kappa\Omega=0$ as its corollary. The derivation consumes H5 in full: it is the **freezing of the
cutoff vector**, not any property of the disclosure rule, that removes $\kappa$ from $\Omega$.
In equilibrium $k$ solves $k=\mathcal T(k;\vartheta)$ and moves with $\kappa$, $\Omega$ moves
with it, and the discarded term $(\partial_\kappa\Omega)(M_F-M_P)$ reappears at full size. That
term is the object C1 bounds. Listing H6 as a hypothesis rather than as a corollary keeps the
partial-equilibrium restriction visible in the theorem's statement rather than buried in a
derivation.

**Step 6 (Part A's conclusion).** Steps 2–4 give
$\partial_\kappa\Delta^{\mathrm{act}}=(1-\Omega)\,\partial_\kappa M_P$. By H2,
$1-\Omega\in(0,1)$, so $\lvert 1-\Omega\rvert=1-\Omega$ and taking absolute values of both sides,
with $\mathcal S=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$ and
$\mathcal S_P=\lvert\partial_\kappa M_P\rvert$ (card §4.4),
$$
\boxed{\;\mathcal S(\kappa,\tau,T)=\bigl(1-\Omega(\tau,T)\bigr)\,\mathcal S_P(\kappa,\tau,T).\;}
$$
The $\Omega$ argument is written $(\tau,T)$ rather than $(\kappa,\tau,T)$ from here on, which
Step 4 licenses. Two consequences used later: $\mathcal S>0$ exactly when $\mathcal S_P>0$
(H8), and $\mathcal S_P>0$ makes $\lvert\cdot\rvert$ differentiable at $\partial_\kappa M_P$, so
$\mathcal S_P$ inherits the differentiability of $\partial_\kappa M_P$ in any policy coordinate
— which Step 20 needs.

**Step 7 (aggregation invariance — the factorisation survives the measurement convention).**
Fix any grid $\kappa_0<\kappa_1<\dots<\kappa_n$ inside the maintained parameter set, with H2
holding at each node. By Step 1 at $\kappa_i$ and $\kappa_{i+1}$, H4 ($M_F$ common to both nodes)
and H6 **in its constancy form** ($\Omega$ common to both nodes — a vanishing derivative at one
$\kappa$ would not deliver this, which is why H6 is stated as constancy and the derivative form is
its corollary; Step 5 derives the constancy outright),
$$
\Delta^{\mathrm{act}}(\kappa_{i+1})-\Delta^{\mathrm{act}}(\kappa_i)
=(1-\Omega)\bigl[M_P(\kappa_{i+1})-M_P(\kappa_i)\bigr].
$$
Summing absolute values,
$$
\mathcal S^{\mathrm{TV}}:=\sum_{i=0}^{n-1}\bigl\lvert\Delta^{\mathrm{act}}(\kappa_{i+1})-\Delta^{\mathrm{act}}(\kappa_i)\bigr\rvert
=(1-\Omega)\sum_{i=0}^{n-1}\bigl\lvert M_P(\kappa_{i+1})-M_P(\kappa_i)\bigr\rvert
=:(1-\Omega)\,\mathcal S_P^{\mathrm{TV}} .
$$
Differentiability (H7) is **not** used. The same argument runs for any aggregator of the
increment vector that is positively homogeneous of degree one — total variation, mean absolute
slope, supremum of $\lvert\cdot\rvert$ — because $(1-\Omega)$ is a single nonnegative scalar
common to every increment. Every ratio statement in Parts B and C therefore holds verbatim with
$(\mathcal S,\mathcal S_P)$ replaced by $(\mathcal S^{\mathrm{TV}},\mathcal S_P^{\mathrm{TV}})$.
This matters because the committed O-1 record measures $\kappa$-sensitivity as a total variation
over a grid, not as a pointwise derivative (see WHERE IT FAILS, case 1); without this step the
theorem and the evidence would be about different functionals.

**Step 8 (chord form of $\mathcal S_P$).** Under H11 (A($\tau$) at the policy in question) and
H13 clause (br-ii), $\partial_\kappa M_P=\Delta_m A'_\kappa C_h(\bar\pi)$ exactly, with no
composition-through-$\kappa$ remainder, which is the $M_P$-level version of H12's
$\partial_\kappa\mathbb E[h]=A'_\kappa C_h(\bar\pi)$. Taking absolute values and using
$\Delta_m>0$ (H1),
$$
\mathcal S_P=\Delta_m\,\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert
=\frac{\Delta_m}{4}\,\lvert A'_\kappa\rvert\,\bar\pi^{2}\,\lvert g''(\zeta)\rvert
\quad\text{for some }\zeta\in(0,\bar\pi),
$$
the second equality by H12's mean-value form. Two readings are used later. First, $\mathcal S_P$
is a **product** of a weight-derivative magnitude and a chord magnitude, which is why L4's third
leg needs both (br-iii) and the chord monotonicity and not either alone. Second, $\mathcal S_P$
is $O(\bar\pi^2)$ as $\bar\pi\downarrow 0$, which supplies the magnitude prediction in the
NUMERICAL CHECK REQUEST. Both readings inherit H12's open status for the two-round pooled cell.

### Part B — the threshold margin

Throughout Part B the window $T$ is common to the two rules and the comparison is
$b_0<\tau'<\tau$ (H10), so $\tau'$ is the tighter threshold (card §4.1: lower $\tau$ = tighter).

**Step 9 (the ratio identity).** Apply Step 6 at $(\tau',T)$ and at $(\tau,T)$, which H2 permits
at both. By H8, $\mathcal S_P(\kappa,\tau,T)>0$, so by Step 6 and H2, $\mathcal S(\kappa,\tau,T)>0$
and the quotient is defined:
$$
\frac{\mathcal S(\kappa,\tau',T)}{\mathcal S(\kappa,\tau,T)}
=\frac{\bigl(1-\Omega(\tau',T)\bigr)\mathcal S_P(\kappa,\tau',T)}
       {\bigl(1-\Omega(\tau,T)\bigr)\mathcal S_P(\kappa,\tau,T)}
= W_\tau\,C_\tau ,
$$
with $W_\tau$ and $C_\tau$ exactly as the card §4.4 rows define them. The identity is exact: it
is Step 6 twice and one division, and it uses H5 to guarantee that the two sides are the same
model with one primitive changed rather than two different equilibria.

**Step 10 (the weight ratio is at most one).** By H14 leg 1 (proved outright, given H9's clock
equivalence and $b_0<\tau'<\tau$ from H10), $\Omega(\tau',T)\ge\Omega(\tau,T)$. Subtracting from
one reverses the inequality: $1-\Omega(\tau',T)\le 1-\Omega(\tau,T)$. Both sides are strictly
positive by H2, so dividing preserves the direction and
$$
0\;\le\;W_\tau\;\le\;1 .
$$

**Step 11 (the composition ratio is at most one — where A($\tau$) and A(br) bind).** By H14 leg
3, $\mathcal S_P(\kappa,\tau',T)\le\mathcal S_P(\kappa,\tau,T)$, **and this leg holds only under
A(br) (H13)**. With H8 giving a strictly positive denominator,
$$
0\;\le\;C_\tau\;\le\;1 .
$$
The chain that L4 leg 3 executes, restated here so the reader can see which clause carries which
inch of the argument — it is cited, not re-derived:

1. $\tau'<\tau$ weakly lowers the pooled prior engagement share
   $\bar\pi_{\mathrm{pr}}=\Pr(a=1\mid D=0)$ — H14 leg 2, proved outright, by
   conditional-probability arithmetic on the nested flagged sets;
2. a weakly lower $\bar\pi_{\mathrm{pr}}$ gives a weakly lower chord endpoint $\bar\pi$ — H13
   clause (br-iv), and this is the clause that keeps the orchestrator's ruling honest: leg 2
   moves a **share**, the chord moves an **upper support point**, and (br-iv) is precisely the
   assumed link between the two. Without it, leg 2 says nothing about $\bar\pi$;
3. a weakly lower $\bar\pi$ gives a weakly smaller $\lvert C_h(\bar\pi)\rvert$ — H11's
   maintained monotonicity of $\lvert C_h\rvert$ in $\bar\pi$, **together with H17's clause
   (br-v)**. Both are needed and they do different jobs: H11's monotonicity is a property of
   $C_h(\cdot)$ *at a policy*, so it orders two values of **one** functional, while the comparison
   here reads that functional at $\tau$ and at $\tau'$. (br-v) is what makes them one functional.
   It is **this file's addition**, not something L4's A(br) carries — (br-i) fixes the endpoints
   and the coefficients, (br-ii) freezes the support points and the kernel along $\kappa$ only,
   and (br-iv)'s "same function at $\tau$ and $\tau'$" is about the endpoint map, not about $h$;
4. $\lvert A'_\kappa(\tau')\rvert\le\lvert A'_\kappa(\tau)\rvert$ — H13 clause (br-iii);
5. multiplying the two nonnegative factors of Step 8's product form, using items 3 and 4,
   $\mathcal S_P(\kappa,\tau',T)\le\mathcal S_P(\kappa,\tau,T)$, which is leg 3.

Items 3–5 are unavailable without H11's representation holding at **both** policies, which is
H13 clause (br-i). Item 5 is unavailable without (br-ii), because a
composition-through-$\kappa$ remainder in $\partial_\kappa M_P$ would break Step 8's product
form. The theorem's threshold leg therefore rests on all four clauses of A(br), **on (br-v)
(H17), which A(br) does not supply**, and on A($\tau$), whose applicability to the two-round
pooled cell is **open** (H12). This is why the label below stays CONJECTURE even for Part B.

**Step 12 (both ratios are nonnegative).** $W_\tau\ge 0$ because $1-\Omega>0$ at both policies
(H2). $C_\tau\ge 0$ because $\mathcal S_P$ is an absolute value (card §4.4) and its denominator
is strictly positive (H8).

**Step 13 (Part B's conclusion).** By Steps 10 and 11 both ratios lie in $[0,1]$, and by Step 12
both are nonnegative, so their product lies in $[0,1]$: $W_\tau C_\tau\le 1\cdot 1=1$.
Substituting into Step 9's identity and multiplying through by the positive number
$\mathcal S(\kappa,\tau,T)$,
$$
\boxed{\;\mathcal S(\kappa,\tau',T)\;=\;W_\tau C_\tau\,\mathcal S(\kappa,\tau,T)\;\le\;\mathcal S(\kappa,\tau,T).\;}
$$
Threshold tightening attenuates $\mathcal S$ at fixed policies. **The structural point is that no
dominance condition appears:** at this margin the weight effect and the composition effect push
the same way, so the product is bounded by one without comparing their sizes. Part C's iff is
not a weaker proof of the same thing; it is the honest statement of a margin where the second
factor is unsigned.

**Step 14 (strictness, and the null case).** The inequality of Step 13 is strict exactly when
$W_\tau<1$ or $C_\tau<1$, i.e. when the threshold move reclassifies positive mass ($\Omega$
strictly rises) or strictly lowers $\mathcal S_P$. If the move from $\tau$ to $\tau'$
reclassifies no history — no $(j,s)$ has
$\tau'\le B_j(s,H-T)<\tau$ — then $\Omega$, $\bar\pi_{\mathrm{pr}}$, $\bar\pi$ and
$\mathcal S_P$ are all unchanged, both ratios equal one, and Step 13 delivers equality. No
strict attenuation is claimed from a null reclassification.

**Step 15 (local threshold form, under H18, for symmetry with Part C).** **This step is
conditional on H18 and on nothing else new; it is consumed by no later step.** Card §4.1 places
no discreteness on $\tau$, so the domain is continuous, but a continuous domain is not a smooth
map: H18 is what supplies the derivatives, and H18 is an added hypothesis exactly as H15 is at the
window margin. Without it the display below need not exist — a flat stretch of
$s\mapsto B_j(s,H-T)$ inside the Voice region puts an atom in the law of the date-$(H-T)$ stake,
at which $t\mapsto\Omega(t,T)$ jumps, and H14 leg 1 gives only a **weak inequality between two
thresholds**, which is monotonicity and not differentiability. The same gap sits on the other
factor: Step 6's second consequence transfers differentiability of $\partial_\kappa M_P$ to
$\mathcal S_P$, it does not create it, and H7 supplies differentiability in $\kappa$ only.

Adopt H18 and write $r_\tau=-t$ for $t\in I_\tau$ (card §4.5), so higher $r_\tau$ is tighter. By
H18 clause 1 both $r_\tau\mapsto\Omega$ and $r_\tau\mapsto\partial_\kappa M_P$ are $C^1$ on
$\{-t:t\in I_\tau\}$; by H18 clause 2, $\mathcal S_P>0$ there, so $\lvert\cdot\rvert$ is
differentiable at $\partial_\kappa M_P\ne0$ and $\mathcal S_P$ is $C^1$ in $r_\tau$ (Step 6's
second consequence, whose antecedent H18 clause 1 now supplies). Differentiating Step 6:
$$
\partial_{r_\tau}\mathcal S=-\Omega_{r_\tau}\mathcal S_P+(1-\Omega)\,\partial_{r_\tau}\mathcal S_P .
$$
Now the two signs. Each comes from an endpoint leg of H14 read along the whole interval rather
than at its ends, which is what H18 clause 3 is for. H14 leg 1 holds for **every** pair $t'<t$ in
$I_\tau$ — it needs only H9's clock equivalence
and $b_0<t'<t$, both available throughout $I_\tau\subset(b_0,\infty)$ — so $t\mapsto\Omega(t,T)$
is weakly decreasing on $I_\tau$, hence $r_\tau\mapsto\Omega$ is weakly increasing, and its
derivative, which exists by H18 clause 1, satisfies $\Omega_{r_\tau}\ge0$. **H14 leg 1 alone does
not give this; H14 leg 1 plus H18's differentiability does.** Likewise H14 leg 3, which H18 clause
3 makes available at every pair in $I_\tau$ (under H13 and H17), makes $\mathcal S_P$ weakly
decreasing in $r_\tau$ there, so $\partial_{r_\tau}\mathcal S_P\le0$. The first term is then $\le0$
(using $\mathcal S_P>0$, H8 extended by H18 clause 2) and the second is $\le0$ (using
$1-\Omega>0$, H2 extended by H18 clause 2). A sum of two nonpositive terms is nonpositive:
$\partial_{r_\tau}\mathcal S\le 0$ on $I_\tau$. The local threshold criterion
$\partial_{r_\tau}\mathcal S_P/\mathcal S_P\le\Omega_{r_\tau}/(1-\Omega)$ is satisfied with the
left side nonpositive and the right side nonnegative — it holds with slack on both sides of zero,
which is the same statement as Step 13's "no dominance condition needed".

**Scope, stated so it cannot be misread.** What this step adds to Part B is a *reading*, not a
result. Part B's conclusion is the boxed weak inequality of Step 13, which is finite-difference
throughout and cites neither H18 nor any derivative in $r_\tau$; the global legs of Part B —
Steps 9–14 — are untouched by H18 and stand or fall without it. If H18 fails at some threshold in
the compared range, this step is void there and Step 13 is unaffected.

### Part C — the window margin

Throughout Part C the threshold $\tau$ is common to the two rules and the comparison is $T'<T$
(card §4.1: lower $T$ = tighter). The card's $W_T$ and $C_T$ rows fix the empirical pair
$(T',T)=(5,10)$; every statement below is written for a general pair $T'<T$ and specialises to
$(5,10)$ verbatim.

**Step 16 (the weight ratio is at most one — proved, not assumed).** Let $j$ be a Voice plan and
$s$ any signal with $D_j(s;\tau,T)=1$. By H9's clock equivalence,
$B_j(s,H-T)\ge\tau$. Since $T'<T$ gives $H-T'>H-T$, and $\partial_d B_j\ge 0$ for Voice plans
(H10), $B_j(s,H-T')\ge B_j(s,H-T)\ge\tau$; and $a_j=1$ is unchanged by the window. Applying H9's
equivalence in the other direction at $T'$, $D_j(s;\tau,T')=1$. By A4 only Voice plans cross in
the core (H10), so no non-Voice history has to be checked. Hence
$$
\mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau,T')
\quad\Longrightarrow\quad
\Omega(\tau,T')\ge\Omega(\tau,T)
\quad\Longrightarrow\quad
0\le W_T=\frac{1-\Omega(\tau,T')}{1-\Omega(\tau,T)}\le 1 ,
$$
the last implication as in Step 10, with H2 supplying a strictly positive denominator and H5
holding the plans fixed across the two windows. Two remarks. (i) The turn-1 statement of T1
carried "$\Omega(\tau,T')\ge\Omega(\tau,T)$" as its hypothesis 6; in the two-round model it is a
**consequence** of D1 and the monotone Voice path, so it is discharged here rather than assumed.
(ii) This is exactly the bridge that the static repo model could not supply — the O-1 experiment
toggles a flag and assumes the map from "shorter window" to "higher $\Omega$"; here the map is
derived from the legal clock.

**Step 17 (the composition ratio is unsigned — why L4 does not transfer).** $C_T$ carries no
sign from any hypothesis maintained in this file. Three reasons, in increasing order of
substance.

1. **A(br) is quantified over the threshold pair.** H13's clauses name $\tau$ and $\tau'$:
   (br-i) asserts the representation "under $\tau$ and under $\tau'$"; (br-iii) compares
   $\lvert A'_\kappa(\tau')\rvert$ with $\lvert A'_\kappa(\tau)\rvert$; (br-iv) asserts one and
   the same endpoint function "at $\tau$ and $\tau'$". None of the three says anything about two
   window environments. Step 11's chain therefore has no window instance to run on, and H14 has
   no window leg to cite.
2. **The window has a channel the threshold does not.** At fixed policies, changing $T$ changes
   the filing date $f_j=c_j+T$ and hence the objects the card §4.2 rows already sign:
   $T'<T\Rightarrow B^F(T')\le B^F(T)$ and $Q^F(T')\ge Q^F(T)$. Trading moves from the pooled
   round into the flagged round on histories that are flagged under **both** windows. A threshold
   change at a fixed window does not move a single unit of trade across the filing date in this
   way; it only relabels which histories file at all.
3. **The pooled cell's own information changes.** The pooled public history is
   $\mathcal H_d^P=(X_0,\dots,X_d;\text{ flag landed by }d)$ (card §4.3), so a $D=0$ history
   carries the event "no flag has landed by $d$". Under a tighter window that event rules out
   more crossing dates — "no flag by $d$" excludes $c\le d-T'$ rather than only $c\le d-T$ — so
   the pooled cell's Bayesian updating changes even holding the set of pooled histories fixed.
   A($\tau$)'s clause (br-ii) requires that the support points and the kernel do not move; here
   the conditioning event itself moves with the policy, which is a composition change of a kind
   (br-ii) was written to exclude at the $\kappa$ margin and says nothing about at the $T$ margin.

Any of the three is enough to block a window analogue of L4 leg 3. This file does not assume one,
and Step 22 records that the numerical record contains a live case where $C_T$-type composition
runs the other way.

**Step 18 (the exact finite iff).** Apply Step 6 at $(\tau,T')$ and $(\tau,T)$, permitted by H2
at both. By H8 and Step 6, $\mathcal S(\kappa,\tau,T)>0$, so
$$
\frac{\mathcal S(\kappa,\tau,T')}{\mathcal S(\kappa,\tau,T)}
=\frac{\bigl(1-\Omega(\tau,T')\bigr)\mathcal S_P(\kappa,\tau,T')}
       {\bigl(1-\Omega(\tau,T)\bigr)\mathcal S_P(\kappa,\tau,T)}
=W_T\,C_T .
$$
Multiplying an inequality by the positive number $\mathcal S(\kappa,\tau,T)$ preserves it in both
directions, so
$$
\boxed{\;\mathcal S(\kappa,\tau,T')\le\mathcal S(\kappa,\tau,T)
\iff W_T\,C_T\le 1.\;}
$$
Both directions hold, and neither side is a sign claim: the equivalence is exact and vacuous of
economics until $C_T$ is measured. The identity $\mathcal S(\kappa,\tau,T')/\mathcal S(\kappa,\tau,T)=W_TC_T$
is itself the falsifiable content at this margin, and it is the object the NUMERICAL CHECK
REQUEST asks the implementation to verify to $10^{-10}$.

**Step 19 (reading the criterion).** By Step 16, $W_T\le 1$: the weight effect always attenuates,
because tightening the window moves mass out of the $\kappa$-sensitive pooled cell into the
$\kappa$-invariant flagged cell (H4). $C_T$ is the composition effect: what happens to the
$\kappa$-sensitivity of the histories that remain pooled. Since $W_T>0$, the criterion of Step 18
rearranges to
$$
C_T\le \frac{1}{W_T}=\frac{1-\Omega(\tau,T)}{1-\Omega(\tau,T')},
$$
i.e. attenuation holds exactly when the composition effect does not exceed the reciprocal of the
weight effect. "The weight effect dominates the composition effect" in the ledger's phrasing is
this inequality and nothing more; in particular it does **not** mean $\lvert 1-W_T\rvert\ge\lvert 1-C_T\rvert$,
and it does not mean $C_T\le 1$.

**Step 20 (the local form).** Adopt H15 and write $r=r_T=-T$, $r_0=-T<r_1=-T'$, so higher $r$ is
tighter. On the interpolating interval, $\mathcal S_P(r)>0$ (H15), so $\lvert\cdot\rvert$ is
differentiable at $\partial_\kappa M_P(r)\ne 0$ and $\mathcal S_P$ is $C^1$ in $r$ (Step 6's
second consequence). Differentiating Step 6's factorisation in $r$,
$$
\partial_{r_T}\mathcal S=-\Omega_{r_T}\,\mathcal S_P+(1-\Omega)\,\partial_{r_T}\mathcal S_P .
$$
By **H15's monotonicity clause**, $\Omega_{r_T}\ge 0$, so the first term is the attenuating weight
effect and the second is the unsigned composition effect. The citation is H15 and **not** Step 16:
Step 16 compares two **integer** windows and delivers $\Omega(\tau,T')\ge\Omega(\tau,T)$ at the
endpoints, and nothing outside H15 forbids an extension that dips in between. Note what does and
does not depend on this. The boxed equivalence below is pure algebra — dividing by the strictly
positive $\mathcal S$ — and holds whether or not the interpolant is monotone; only the *reading*
of the first term as attenuating, and Block 5's predicted sign for $\Omega_{r_T}$, use the sign.
Dividing by the strictly positive number
$\mathcal S=(1-\Omega)\mathcal S_P$ (H2, H8, Step 6),
$$
\frac{\partial_{r_T}\mathcal S}{\mathcal S}
=\frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P}-\frac{\Omega_{r_T}}{1-\Omega}
\;=:\;\rho(r) ,
$$
and since $\mathcal S>0$, $\operatorname{sgn}(\partial_{r_T}\mathcal S)=\operatorname{sgn}(\rho)$.
Hence
$$
\boxed{\;\partial_{r_T}\mathcal S\le 0
\iff
\frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P}\le\frac{\Omega_{r_T}}{1-\Omega}.\;}
$$
This is the ledger's local form. It is an iff at each $r$, with no sign supplied for either side.

**Step 21 (the product form and the local form are the same criterion — proved).** The ledger
writes the two forms as "equivalently". The exact content of that word is the following four
statements, each proved here. Let $\rho$ be as in Step 20, continuous on $[r_0,r_1]$ by H15.

*(21a) The finite product criterion is the sign of the integrated local gap.* $\mathcal S(r)>0$
and $C^1$ on $[r_0,r_1]$ (H15, H8, Step 6), so $\log\mathcal S$ is $C^1$ there and the
fundamental theorem of calculus gives
$$
\log\frac{\mathcal S(r_1)}{\mathcal S(r_0)}=\int_{r_0}^{r_1}\partial_r\log\mathcal S(r)\,dr
=\int_{r_0}^{r_1}\rho(r)\,dr ,
$$
the second equality by Step 20. By Step 18, $\mathcal S(r_1)/\mathcal S(r_0)=W_TC_T$, so
$$
W_T\,C_T=\exp\!\left(\int_{r_0}^{r_1}\rho(r)\,dr\right),
\qquad\text{hence}\qquad
W_T\,C_T\le 1\iff\int_{r_0}^{r_1}\rho(r)\,dr\le 0 .
$$
The exponential is strictly increasing, so the equivalence is exact in both directions. Written
out, $\int\rho=\int\bigl[\partial_r\mathcal S_P/\mathcal S_P-\Omega_r/(1-\Omega)\bigr]dr$: the
product criterion is the local criterion integrated along the tightening path.

*(21b) Pointwise local $\Rightarrow$ finite product.* If $\rho(r)\le 0$ for every
$r\in[r_0,r_1]$, the integral of a nonpositive continuous function over $[r_0,r_1]$ is
nonpositive, so by (21a) $W_TC_T\le 1$. If in addition $\rho(r)<0$ on some subinterval of
positive length, the integral is strictly negative and $W_TC_T<1$.

*(21c) Finite product $\Rightarrow$ local at some point, and no more.* If $W_TC_T\le 1$ then by
(21a) $\int_{r_0}^{r_1}\rho\le 0$, and since $\rho$ is continuous the mean value theorem for
integrals supplies $r^\*\in(r_0,r_1)$ with
$\rho(r^\*)=(r_1-r_0)^{-1}\int_{r_0}^{r_1}\rho\le 0$: the local criterion holds **somewhere** in
the interval. It does not hold everywhere in general. A function $\rho$ that is positive on
$[r_0,\tfrac12(r_0+r_1)]$ and sufficiently negative on $[\tfrac12(r_0+r_1),r_1]$ integrates to a
nonpositive number while violating the local criterion on the first half; the finite comparison
$T\to T'$ then reports attenuation even though an intermediate window tightening amplifies. So
the implication in this direction is "at some point", never "at every point".

*(21d) The two forms coincide exactly in the infinitesimal limit.* Fix $r_0$ and let $r_1\downarrow r_0$.
By Step 18, $W_TC_T=\mathcal S(r_1)/\mathcal S(r_0)$ as a function of $r_1$, and it equals $1$ at
$r_1=r_0$, so
$$
\lim_{r_1\downarrow r_0}\frac{W_TC_T-1}{r_1-r_0}
=\frac{d}{dr_1}\left.\frac{\mathcal S(r_1)}{\mathcal S(r_0)}\right|_{r_1=r_0}
=\frac{\partial_r\mathcal S(r_0)}{\mathcal S(r_0)}=\rho(r_0).
$$
Hence: if $\rho(r_0)<0$ then $W_TC_T<1$ for every $r_1>r_0$ close enough to $r_0$; and if
$W_TC_T\le 1$ for every $r_1>r_0$ close enough to $r_0$, then the limit above is $\le 0$, i.e.
$\rho(r_0)\le 0$. The boundary case $\rho(r_0)=0$ is undetermined at first order — the finite
sign is then decided by higher-order terms — and is named as such rather than resolved.

**Summary of Step 21.** The two window criteria are the same criterion read at two scales:
(21a) shows the product form is the exponentiated integral of the local form; (21b) and (21c)
give the one-way implications at finite scale, with (21c)'s counterexample shape recorded so
nobody reads the ledger's "equivalently" as "finite $\Rightarrow$ local everywhere"; (21d) gives
exact coincidence in the limit. That is what this file means by "equivalently", and it is the
only sense in which it is asserted.

**Step 22 (no unconditional window sign — and the live case).** Nothing in H1–H18 signs $C_T$
(Step 17) or $\rho$ (Step 20), so nothing in H1–H18 signs $\partial_{r_T}\mathcal S$ or
$W_TC_T-1$. Both branches are consistent with every hypothesis maintained here:
$W_TC_T\le 1$ (attenuation) and $W_TC_T>1$ (amplification) each require only a value of $C_T$
that the hypotheses leave free. The committed O-1 record supplies a measured instance of the
amplifying branch at low $\Omega$ and of the attenuating branch at $\Omega=0.50$; it is set out
in WHERE IT FAILS case 1, which is where a claimed unconditional window theorem would die. This
is card §9's standing boundary ("a global window-margin attenuation sign" is not claimed) and
ticket 26's binding O-1 finding, and Part C is written to respect both. $\blacksquare$

---

## WHERE IT FAILS

**1. The live failure case for an unconditional window theorem — the committed O-1 numbers.**
The O-1 record (`research/model_v4/HANDOFF_sign.md` §3, reproducing
`quality_reports/reports/2026-08-19_framework_v3_referee_report.md` and re-executed by
`quality_reports/fixes/t1_o1_rerun_check.py`) reports $\kappa$-sensitivity ratios of

| $\Omega$ | 0.037252 | 0.128950 | 0.285804 | 0.500000 |
|---|---|---|---|---|
| sensitivity ratio | **1.06397** | **1.18373** | **1.13631** | **0.37798** |

i.e. **$\approx 1.064$, $1.184$ and $1.136$ — all above one — at $\Omega=0.037$, $0.129$ and
$0.286$, flipping to $0.378$ at $\Omega=0.50$**, with the sign boundary located at
**$\Omega^\*\approx 0.343$** by bisection on $k_D$ in that run ($k_D^\*=1.28618$); the earlier
committed record quoted the cut as $\lesssim 0.29$, which was the largest confirmed grid point
rather than the crossing. Anything that quotes $0.29$ should quote $0.343$ and should say it came
from that run. Three things follow for this file.

*(a) It refutes the theorem one might have wanted.* A claimed unconditional window attenuation
result predicts a ratio at most one at every $\Omega$. Three of the four committed rows exceed
one. Part C therefore states an iff and stops.

*(b) It is a rule-on/rule-off comparison, not a window comparison.* The O-1 experiment holds the
cutoffs fixed and compares two information regimes at each $k_D$ — the market sees $(X,D)$ versus
the market sees $X$ only. The static repo model has no window primitive at all (HANDOFF §4.2).
In this file's language the experiment is the extreme margin from "no rule" ($\Omega=0$) to "the
rule" ($\Omega>0$), so the O-1 ratios are **not** measurements of $W_TC_T$ in the two-round
model, and this file does not present them as such.

*(c) Read through the factorisation, they are still a weight-times-composition product, and the
composition factor is the one that misbehaves.* If the static model satisfies L1, flagged-cell
$\kappa$-invariance and PE-$\Omega$ — the first two are what the record's own mechanism sentence
asserts, the third is its fixed-cutoff design — then Step 6 and Step 7 apply to it with the
rule-on/rule-off margin in place of the window margin, giving ratio $=W_{O1}C_{O1}$ with
$W_{O1}=1-\Omega$ and $C_{O1}=\mathcal S_P^{\mathrm{TV}}(\Omega)/\mathcal S_P^{\mathrm{TV}}(0)$.
Dividing the committed ratios by $1-\Omega$:

| $\Omega$ | $W_{O1}=1-\Omega$ | committed ratio | implied $C_{O1}$ |
|---|---|---|---|
| 0.037252 | 0.962748 | 1.06397 | **1.1051** |
| 0.128950 | 0.871050 | 1.18373 | **1.3590** |
| 0.285804 | 0.714196 | 1.13631 | **1.5910** |
| 0.500000 | 0.500000 | 0.37798 | **0.7560** |

The weight effect attenuates at every row, monotonically and by construction. What decides the
sign is the composition factor, which runs at $1.11$, $1.36$, $1.59$ — amplifying, and
amplifying by more than the weight effect attenuates — before falling to $0.76$ at
$\Omega=0.50$. This is exactly HANDOFF §4.2's mechanism sentence ("the pooled cell loses its most
revealing state, and the pooled cell's remaining $\kappa$-response more than makes up for the
flagged cell's $\kappa$-invariance") expressed as a number, and it is a live instance of Step 17:
the composition effect is not merely unsigned in theory, it is measured above one in the
repo model at three of four calibrations. The four implied $C_{O1}$ values are arithmetic from
the committed ratios under the three assumptions named at the head of this paragraph, not
independent computations; the NUMERICAL CHECK REQUEST asks for them to be recomputed directly.

**2. A($\tau$) may not hold for the two-round pooled cell — the threshold leg's open premise.**
H12 records that the L3 writer declares this **OPEN**. If the two-round pooled posterior law
admits no symmetric ternary representation — a fourth support point, an asymmetric weight
derivative, or weights whose derivatives do not satisfy $A_0'=A_1'=-\tfrac12 A_{1/2}'$ — then
Step 8's product form for $\mathcal S_P$ does not exist, L4 leg 3 has nothing to act on, and Part
B's conclusion is void. Part A and Part C survive: neither uses H11 or H12.

**3. A(br) fails clause by clause.** *(br-ii) fails* if the support points $\{0,\bar\pi/2,\bar\pi\}$
or the kernel $h$ move with $\kappa$: then $\partial_\kappa M_P$ carries a
composition-through-$\kappa$ remainder, Step 8 is wrong, and $\mathcal S_P$ is no longer the
product of a weight magnitude and a chord magnitude. *(br-iii) fails* if
$\lvert A'_\kappa(\tau')\rvert>\lvert A'_\kappa(\tau)\rvert$ by more than the chord shrinks —
a tighter threshold that makes the pooled weights more $\kappa$-responsive can raise
$\mathcal S_P$ even with a shorter chord, and Step 11 item 5 then fails. *(br-iv) fails* if the
map from the pooled prior engagement share to the chord endpoint is not the same function at the
two thresholds; L4 leg 2 moves a share, the chord moves an upper support point, and only (br-iv)
connects them. In each case Part B's $C_\tau\le 1$ is lost while Step 9's identity survives, so
the threshold conclusion degrades from "attenuation" to the same kind of iff Part C states.

**4. $\mathcal S_P=0$ at a compared policy — three routes, not one.** H8 fails. Two breakages
follow in every route: the ratios $C_\tau$ and $C_T$ are $0/0$ or have a zero denominator, and
$\mathcal S_P=\lvert\partial_\kappa M_P\rvert$ is not differentiable in $r_T$ (or, with H18, in
$r_\tau$) at that point, so Steps 15 and 20's derivative forms do not exist. Step 18's iff can be
salvaged as "$\mathcal S(\tau,T')\le\mathcal S(\tau,T)$" read directly off Step 6, but the product
criterion is uninformative there. Step 8's product form
$\mathcal S_P=\Delta_m\lvert A'_\kappa\rvert\lvert C_h(\bar\pi)\rvert$ vanishes exactly when one
of its factors does, and there are three ways for that to happen — the file's earlier draft named
only the first.

*(a) $\bar\pi\downarrow 0$.* $\mathcal S_P=O(\bar\pi^2)$ by Step 8, so the small-$\bar\pi$ corner
is where the ratio form loses resolution first. This is the graceful case: everything degrades
continuously.

*(b) $A'_\kappa=0$ at $\bar\pi$ bounded away from zero.* The pooled weights are $\kappa$-insensitive
even though the chord is non-degenerate: the pooled cell has no liquidity response at all, so
$\mathcal S_P=0$ and, by Step 6, $\mathcal S=0$ at that policy. Card §4.4 asks only that
$A'_\kappa$ be bounded on $[0,1]$; nothing signs it away from zero. Every ratio statement at that
policy is undefined while Step 6's identity survives, and the theorem is true but empty there.

*(c) $C_h(\bar\pi)=0$ with $\bar\pi>0$ — the case card §5 demands be handled explicitly.* The
kernel is affine across the three support points $\{0,\bar\pi/2,\bar\pi\}$, so the chord vanishes
without its endpoint vanishing. This is **inside** A($\tau$), not outside it: A($\tau$)'s
maintained orientation is the weak $C_h\le0$, and draft_v2's (C\*) is the strict version, so a
maintained-hypothesis-satisfying model can sit here. Three consequences, and they are worth
separating. First, by H11's monotonicity of $\lvert C_h\rvert$ in $\bar\pi$ (whose comparison
across the two policies is licensed by H17 = (br-v)) and the endpoint inequality
$\bar\pi(\tau')\le\bar\pi(\tau)$ — H14 leg 2's share inequality carried to the endpoint by
A(br)'s (br-iv) — $C_h(\bar\pi(\tau))=0$ forces
$\lvert C_h(\bar\pi(\tau'))\rvert\le 0$, hence $C_h(\bar\pi(\tau'))=0$ as well: the degeneracy at
the looser threshold propagates to the tighter one, and $\mathcal S_P$ vanishes at **both**
compared policies. Second, H14 leg 3 then holds **with equality** — the qualifier H14 now carries
— and Step 13's inequality reads $0\le0$: true, weakly, and with no content. Third, the ratio form
that delivers it is unavailable ($C_\tau$ is $0/0$), so at such a policy Part B's conclusion must
be read off Step 6 directly — $\mathcal S=(1-\Omega)\cdot0=0$ at both thresholds — rather than
through $W_\tau C_\tau$. The honest statement is that the threshold theorem survives the
$C_h=0$ case only as an empty statement and says nothing there; a numerical run that reports
$C_\tau=\text{NaN}$ at some $\tau$ is showing this case, not a bug.

**5. $\Omega$ moves with $\kappa$ — the general-equilibrium failure.** H6 fails whenever the
cutoff vector is allowed to re-solve $k=\mathcal T(k;\vartheta)$ at each $\kappa$. Then Step 4's
discarded term $(\partial_\kappa\Omega)(M_F-M_P)$ returns, $\mathcal S=(1-\Omega)\mathcal S_P$ is
false, and every ratio statement in Parts B and C loses its base. Nothing in this file survives
that failure except Step 1. This is not a remote case: it is the ordinary equilibrium behaviour
of the model, and bounding the returned term is precisely C1's job.

**6. The plan menu violates A7′, so L2's injective form is unavailable on it.** The card's
**ticket-24 note (§5, 2026-08-21)** settles *satisfiability*, which the earlier draft of this file
recorded as open: A7′ (card §4.2) with a fixed cutoff policy and $\Omega>0$ delivers the on-path
injective form with an explicit inverse, and the pro-rata single-Voice menu is a satisfying menu.
The live case is therefore narrower and is a property of the **menu**, not of the hypothesis. The
card names the boundary: a binding stake cap, quantized stakes, a composed terminal target that
repeats values across a Voice-plan switch, $\Omega=0$, and a condition stated at one equilibrium's
cutoffs rather than for every $k\in\Theta$ (A7′ is quantified over the whole polytope). On any menu
at that boundary $M_F$ retains direct $\kappa$-dependence, Step 3 fails, and
$\partial_\kappa\Delta^{\mathrm{act}}$ carries an $\Omega\,\partial_\kappa M_F$ term that neither
margin's ratio form accommodates. This file verifies no clause of A7′ on the two-round menu.

**7. A cell empties.** H2 fails at $\Omega=1$ or $\Omega=0$. L1 then degenerates
($\Delta^{\mathrm{act}}=M_F$ or $=M_P$) with the null cell's conditional average undefined rather
than imputed (H3), and the ratio statements are undefined at any policy where this happens —
including the case where one of the two compared rules has an empty cell and the other does not.

**8. The finite window comparison is read as a pointwise statement.** Step 21c: a tightening from
$T$ to $T'$ can satisfy $W_TC_T\le 1$ while the local criterion is violated at intermediate
window values. Reporting "attenuation from 10 to 5 days" therefore does not license
"attenuation at every window between 10 and 5", and a numerical run that checks only the
endpoints cannot distinguish the two.

---

## LABEL CLAIMED

**CONJECTURE.** Unchanged; this file does not move the ledger. Three separate reasons, any one of
which is sufficient:

1. **Protocol.** Card §7: a label moves only on an independent re-derivation PASS *plus* a
   proof-read PASS. This file is the first proof of T1 and has neither.
2. **Upstream labels.** T1 consumes D1, L1, L2, L3 and L4, all of which are themselves
   CONJECTURE in the card ledger. A result cannot be labelled above its inputs.
3. **Open hypotheses.** Part B rests on A($\tau$), whose applicability to the two-round pooled
   cell L3 declares OPEN (H12), on A(br), which is an assumption the L4 writer introduced rather
   than a proved property, and on the further clause (br-v) that this file adds (H17) and that
   A(br) does not carry. Part A rests on L2's A7-injective form; the card's ticket-24 note now
   records its **satisfiability as resolved** (a satisfying menu exists), so that is no longer a
   reason the label stays put — what is left is whether the two-round model's own menu satisfies
   A7′, which this file does not check (WHERE IT FAILS 6). Step 15's local threshold form rests in
   addition on H18, an added smoothness hypothesis consumed by no other step. Even a passed
   re-derivation would deliver "PROVED under A($\tau$) and A(br)+(br-v) at fixed policies", with
   the hypotheses named in the statement.

What this file does claim to have settled, subject to re-derivation: Part A's factorisation and
its aggregation-invariant form (Step 7) use only L1, L2 and PE-$\Omega$; Step 16's
$W_T\le 1$ is discharged from D1 rather than assumed, removing turn-1 T1's hypothesis 6; and
Step 21's four-part equivalence pins down the sense in which the ledger's product criterion and
local criterion are the same criterion.

---

## NUMERICAL CHECK REQUEST

One script, six blocks. Measure $\kappa$-sensitivity as **total variation over the $\kappa$-grid**
(Step 7 licenses this: the factorisation is exact for the TV aggregate), and report mean
absolute slope alongside it so the numbers are comparable with the O-1 record, which uses both.
All premium objects in premium percentage points (card §7 reporting units).

**Grid.** $\kappa\in[0.15,0.85]$ on a $0.01$ step (71 nodes; the O-1 run's interval).
$\tau$ at the 10th, 30th, 50th, 70th and 90th percentiles of the equilibrium Voice stake
distribution. $T\in\{5,10\}$ for the finite blocks. For block 5 only, an interpolated window
$T\in\{4.0,4.25,\dots,12.0\}$ if the implementation admits fractional windows; if it does not,
the block must report **"local form not evaluable — integer window"** rather than being silently
skipped. Policies frozen at the baseline equilibrium cutoffs at every node (H5).

**Block 1 — the factorisation and the PE hypothesis (Steps 6, 7).** At every node compute
$\mathcal S$, $\Omega$, $\mathcal S_P$ directly and report
$\max\lvert\mathcal S-(1-\Omega)\mathcal S_P\rvert$ and
$\max\lvert\mathcal S^{\mathrm{TV}}-(1-\Omega)\mathcal S_P^{\mathrm{TV}}\rvert$.
*Predicted sign:* residual zero. *Predicted magnitude:* below $10^{-10}$ in both. Separately
report $\max_\kappa\lvert\Omega(\kappa)-\Omega(\kappa_0)\rvert$ across the $\kappa$-grid at fixed
policies. *Predicted magnitude:* below $10^{-12}$ — this checks that H6 is implemented and not
merely asserted. A nonzero value here invalidates every later block.

**Block 2 — threshold margin (Steps 9–14).** For each adjacent threshold pair $\tau'<\tau$ from
the percentile ladder, at each $T$, report
$W_\tau=(1-\Omega(\tau',T))/(1-\Omega(\tau,T))$, $C_\tau=\mathcal S_P(\tau',T)/\mathcal S_P(\tau,T)$,
their product, and the direct ratio $\mathcal S(\tau',T)/\mathcal S(\tau,T)$.
*Predicted sign:* $W_\tau\le 1$, $C_\tau\le 1$, product $\le 1$; direct ratio equals the product.
*Predicted magnitude:* identity residual below $10^{-10}$; product strictly below one at every
pair that reclassifies positive mass, and equal to one within $10^{-12}$ at any pair that
reclassifies none (Step 14). Report the reclassified mass $\Omega(\tau')-\Omega(\tau)$ next to
each row so the null case is visible rather than inferred.

**Block 3 — the chord magnitude (Step 8).** At each $\tau$ report $\bar\pi$, $\lvert A'_\kappa\rvert$,
$\lvert C_h(\bar\pi)\rvert$ and $\mathcal S_P$, and the residual
$\lvert\mathcal S_P-\Delta_m\lvert A'_\kappa\rvert\lvert C_h(\bar\pi)\rvert\rvert$.
*Predicted sign:* residual zero. *Predicted magnitude:* below $10^{-10}$; and
$\lvert C_h(\bar\pi)\rvert/\bar\pi^2$ constant to within $5\%$ between the two smallest $\bar\pi$
nodes, so that $C_\tau\approx(\bar\pi(\tau')/\bar\pi(\tau))^2\cdot\lvert A'_\kappa(\tau')/A'_\kappa(\tau)\rvert$
to within $5\%$ once $\bar\pi\le 10^{-2}$. Report $\bar\pi$ **and** the pooled engagement share
$\bar\pi_{\mathrm{pr}}=\Pr(a=1\mid D=0)$ in separate columns: they are different objects
(H11's ruling) and conflating them is the most likely implementation error in this block.

**Block 4 — window margin, the iff and no forcing (Steps 16, 18, 19).** For $(T',T)=(5,10)$ at
each $\tau$, report $W_T$, $C_T$, $W_TC_T$, the direct ratio
$\mathcal S(\tau,5)/\mathcal S(\tau,10)$, and $\Omega$ at both windows.
*Predicted sign:* $W_T\le 1$ at every node (Step 16 — a violation is a bug in the clock, not
evidence against the theorem); $C_T$ **unsigned and not to be constrained by the script**;
$W_TC_T$ reported as found. *Predicted magnitude:* identity residual
$\lvert\mathcal S(\tau,5)/\mathcal S(\tau,10)-W_TC_T\rvert$ below $10^{-10}$. **Acceptance rule
with teeth:** a run that returns $W_TC_T\le 1$ at every node, including the low-$\Omega$
calibrations, is to be treated as suspect and audited for a forced-attenuation bug before it is
believed, because the O-1 record has the analogous product above one at $\Omega=0.037$, $0.129$
and $0.286$. The script must print the count of nodes with $W_TC_T>1$ explicitly.

**Block 5 — local form and the equivalence (Steps 20–21).** On the interpolated window grid,
compute $\Omega_{r_T}$ and $\partial_{r_T}\mathcal S_P$ by central differences and report
$\rho=\partial_{r_T}\mathcal S_P/\mathcal S_P-\Omega_{r_T}/(1-\Omega)$ and
$\partial_{r_T}\mathcal S/\mathcal S$ at every node.
*Predicted sign:* the two agree in sign at every node, and $\Omega_{r_T}\ge 0$ everywhere **under
H15's monotonicity clause** — a node with $\Omega_{r_T}<0$ falsifies that clause of H15 (or the
interpolation scheme the implementation chose), not the boxed iff of Step 20, which does not use
the sign. Report such nodes rather than clipping them.
*Predicted magnitude:* $\lvert\partial_{r_T}\mathcal S/\mathcal S-\rho\rvert$ below $10^{-8}$
(central-difference tolerance); and, as the check of (21a), the trapezoidal integral of $\rho$
over $r\in[-10,-5]$ equals $\log(W_TC_T)$ from Block 4 to within $10^{-6}$. Report the count of
nodes with $\rho>0$ inside any interval whose endpoint comparison gives $W_TC_T\le 1$ — a
nonzero count is the (21c) phenomenon, and finding one instance is worth more than the whole
block passing.

**Block 6 — the O-1 regression benchmark (WHERE IT FAILS case 1).** In the static repo model at
the four committed $k_D$ values, reproduce the ratios $1.06397$, $1.18373$, $1.13631$, $0.37798$
at $\Omega=0.037252$, $0.128950$, $0.285804$, $0.500000$, and the bisected boundary
$k_D^\*=1.28618$, $\Omega^\*=0.3428$. *Predicted magnitude:* ratios within $10^{-4}$ of the
committed values, $\Omega^\*$ within $0.001$. Then compute $\mathcal S_P^{\mathrm{TV}}$ directly
in each regime and report $C_{O1}=\mathcal S_P^{\mathrm{TV}}(\Omega)/\mathcal S_P^{\mathrm{TV}}(0)$.
*Predicted sign:* $C_{O1}>1$ at the first three rows, $<1$ at the fourth. *Predicted magnitude:*
$C_{O1}=1.1051,\ 1.3590,\ 1.5910,\ 0.7560$ to within $10^{-3}$. These four numbers are this
file's arithmetic prediction from the committed ratios (WHERE IT FAILS case 1c); a mismatch
falsifies the claim that the static model's O-1 experiment satisfies L1 + flagged-cell
$\kappa$-invariance + PE-$\Omega$, and would mean the committed ratios cannot be read through
the factorisation at all. Report that outcome as a finding, not as a tolerance failure.

---

## NOTATION DELTA

Symbols used here that are not in card §4, each defined at first use above:

| Symbol | Meaning | Status |
|---|---|---|
| $\bar\pi_{\mathrm{pr}}=\Pr(a=1\mid D=0)$ | pooled **prior engagement share**, the argument of A(br)'s endpoint linkage (br-iv) | distinct from $\bar\pi$, which per the orchestrator's binding ruling is the **upper support point** of the pooled engagement posterior in the A($\tau$) representation; the share $\mathbb E[\Pi_\kappa]$ is $\kappa$-invariant under A($\tau$) and lies strictly below $\bar\pi$ in any non-degenerate case. Proposed for card §4.4 if T1 is re-derived |
| $\Pi_\kappa$ | the pooled engagement posterior as a random variable, so that A($\tau$)'s representation reads $\mathbb E[h(\Pi_\kappa)]$ | the turn-1 answer's symbol (§3, A($\tau$)); card §5 writes the same object as $\mathbb E[h]$. Used here only in the ruling on $\bar\pi$ |
| $g$, $\zeta$ | $g$ is the univariate section of the kernel $h$ in its posterior argument; $\zeta\in(0,\bar\pi)$ is the mean-value point in $C_h(\bar\pi)=\tfrac14\bar\pi^2 g''(\zeta)$ | the L3 writer's symbols in the amended (as-landed) L3 statement, quoted here unchanged. $g$ is not otherwise used in this file |
| A(br), (br-i)–(br-iv) | the chord–sensitivity bridge hypothesis and its four clauses | hypothesis label introduced by the L4 writer, quoted verbatim in H13. Proposed for card §5 alongside A($\tau$) |
| (br-v) | comparability of the chord functional across the threshold pair: $C_h(\cdot)$ and the univariate section of the kernel $h$ are the same functions of the posterior at $\tau$ and at $\tau'$ | **this file's addition (H17), not carried by L4's A(br)**. Needed by Step 11 item 3, which reads one chord functional at two policies. Proposed as a fifth clause of A(br); until the card carries it, Part B's hypothesis list is "A($\tau$) and A(br)+(br-v)" |
| $\Omega^\*$, $k_D^\*$ | the flagged weight at which the static O-1 experiment's sensitivity ratio crosses one ($\approx0.343$ in that run), and the cutoff at which the bisection located it ($1.28618$) | O-1-record notation (`HANDOFF_sign.md` §3), used in WHERE IT FAILS 1, Block 6 and NOT CLAIMED 10. $k_D$ enters card §4.5 only as a draft_v2 alias inside the $k$ row; neither starred object is a card symbol and neither is a prediction of this theorem |
| $I$, $I_\tau$ | the open **window** interval of H15 and the open **threshold** interval of H18, the sets on which the two smoothness hypotheses are posed | proof-local (H15, H18; Steps 15, 20–22). Both are sets of policy values; the strictness coordinates on them, $r_T=-T$ and $r_\tau=-\tau$, are card §4.5 |
| $\mathcal S^{\mathrm{TV}}$, $\mathcal S_P^{\mathrm{TV}}$ | total variation of $\Delta^{\mathrm{act}}$ and of $M_P$ over a stated $\kappa$-grid | proof-local (Step 7); introduced because the committed O-1 record measures sensitivity this way |
| $r_0=-T$, $r_1=-T'$, $\rho(r)$ | the two window-strictness coordinates of a finite tightening, and the log-derivative gap $\rho=\partial_r\mathcal S_P/\mathcal S_P-\Omega_r/(1-\Omega)$ | proof-local (Steps 20–21). $r_T$ itself is card §4.5 |
| $W_{O1}$, $C_{O1}$ | weight and composition ratios for the **rule-on/rule-off** margin of the static O-1 experiment: $W_{O1}=1-\Omega$, $C_{O1}=\mathcal S_P^{\mathrm{TV}}(\Omega)/\mathcal S_P^{\mathrm{TV}}(0)$ | proof-local, used only in WHERE IT FAILS case 1c and Block 6. Subscripted to respect the card §4.4 rule that the weight-effect and composition-effect letters never appear without a margin subscript. **They are not $W_T,C_T$**: the static model has no window primitive |
| $j(s)$ | the plan the frozen cutoff vector assigns to signal $s$ | proof-local (Step 5); notation for the map card §4.5's $k$ induces |

No card symbol is renumbered or re-keyed. $\kappa$ is noise-trading intensity throughout;
upright $T$ is the window and $\mathcal T$ is the outer best-response map; $\Omega$ is
$\Pr(D=1)$ and every $\Omega$-valued number quoted from the O-1 record is $\Omega$-type, not
$\omega_a$; and the reserved bare letters — D7's appropriability coefficient, D7's pivotality,
the weight-effect and composition-effect letters without a margin subscript, L2's proof-local
utility letters, and the filing-tuple letter — appear nowhere in this file.

**One statement-level flag for the card owner: the ledger's "equivalently" needs a quantifier, not
a demotion.** The ledger's T1 row writes the two window criteria as "$W_T C_T\le 1$, equivalently
$\partial_{r_T}\mathcal S_P/\mathcal S_P\le\Omega_{r_T}/(1-\Omega)$". Read **pointwise at every
$r$**, the second criterion is strictly stronger than the first: it implies the product form
(21b) but is not implied by it (21c, whose counterexample shape is a live configuration inside
H15's own freedom). Read as an **average along the tightening path**, the two are *exactly*
equivalent at finite scale, and that is (21a):
$$
W_TC_T\le1
\quad\Longleftrightarrow\quad
\int_{-T}^{-T'}\Bigl[\frac{\partial_r\mathcal S_P}{\mathcal S_P}-\frac{\Omega_r}{1-\Omega}\Bigr]dr\;\le\;0 .
$$
The row is therefore **ambiguous, not wrong**, and the repair is to supply the missing quantifier
rather than to demote the row to an infinitesimal statement — which would discard the better
reading and the exact finite-scale equivalence with it. Proposed wording, in card §5's A($\tau$)
house style: *"… $W_TC_T\le1$, equivalently $\int\rho\le0$ **on average along the tightening
path**, where $\rho=\partial_{r_T}\mathcal S_P/\mathcal S_P-\Omega_{r_T}/(1-\Omega)$; pointwise
$\rho\le0$ is the local (marginal) form and is **sufficient, not necessary**."* The infinitesimal
reading (21d) remains exact as a limit statement and is a third, weaker thing again. This is a
wording repair, not a label move, and the ledger is untouched by this file.

---

## NOT CLAIMED

1. **No unconditional window sign.** Neither $\partial_{r_T}\mathcal S\le 0$ nor $W_TC_T\le 1$ is
   claimed to hold generally, at any calibration, in any region. Part C is an iff and an
   identity; the sign is an empirical question about $C_T$.
2. **No general-equilibrium result.** Everything is at fixed plan and cutoff policies (H5). The
   term $(\partial_\kappa\Omega)(M_F-M_P)$ discarded in Step 4 is not bounded, signed or
   estimated here. That is C1's subject, and this file supplies no input to it beyond naming the
   term.
3. **No claim that A($\tau$) holds for the two-round pooled cell.** H12 carries L3's OPEN
   declaration unchanged. Part B is conditional on it.
4. **No claim that A(br) is satisfiable**, or that any of its four clauses — or the fifth, (br-v),
   that this file adds as H17 — can be verified on the two-round plan menu. They are assumed where
   used and named where they bind, and (br-v) is flagged as T1's own addition rather than
   attributed to L4.
5. **No claim about A7′ on this model's menu.** The card's ticket-24 note establishes that the
   injective form is **satisfiable** — a satisfying menu exists — and this file does not dispute
   that; what it does not claim is that the two-round model's plan menu is such a menu. No clause
   of A7′ is verified here. L2 is cited with its own hypothesis stack intact.
6. **No strict attenuation at the threshold margin.** Step 13 gives a weak inequality; Step 14
   gives equality when the threshold move reclassifies no mass.
7. **No claim that the O-1 numbers are computations of $W_TC_T$ in the two-round model.** They
   come from the static repo model with a flag toggle and no window primitive (WHERE IT FAILS
   case 1b). The implied $C_{O1}$ values in case 1c are arithmetic from the committed ratios under
   three named assumptions, not independent computations, and Block 6 exists to test them.
8. **No claim that the finite product criterion implies the local criterion at every window
   value.** Step 21c shows it implies it at one point only.
9. **No claim about $J$, $R$ or $R_d$.** The filing-day jump is not claimed $\kappa$-invariant
   (card §9) and does not appear in any step of this proof.
10. **No claim about $\omega_a$, about where $\Omega$ sits in the data, or about which branch of
    the window iff the world is on.** $\Omega^\*\approx 0.343$ is a property of the static model's
    O-1 experiment, not a prediction of this theorem, and the card records that no empirical value
    for $\omega_a$ exists in the repo.
11. **No uniqueness, no welfare, no optimal rule.** Card §9's boundaries are respected in full.
12. **No label move.** T1 stays CONJECTURE and the ledger is not edited.
13. **No unconditional local threshold form.** Step 15's $\partial_{r_\tau}\mathcal S\le0$ is
    claimed **only under H18**, the added threshold-side smoothness hypothesis. It is not claimed
    that $\tau\mapsto\Omega(\tau,T)$ is differentiable — the card's weak $\partial_sB_j\ge0$
    permits an atom in the stake law at $H-T$ at which it jumps — and no other step, and no boxed
    conclusion, uses Step 15.

---

## Retry fixes applied (2026-08-21, batch-2 audit)

Round: the one-retry rule on ticket 27's batch-2 proof-read
(`threads/2026-08-21_batch2_T1_proofread_audit.md`, verdict FAIL at Step 15). Applied by a fresh
writer who wrote neither the file nor the audit. **No boxed claim's substance changed**: the
factorisation (Step 6), the threshold attenuation inequality (Step 13), the window iff (Step 18),
the local iff (Step 20) and "no unconditional window sign" (Step 22) stand verbatim. Every change
below either adds a named hypothesis, fixes a citation, or widens a failure case.

| Finding | Change |
|---|---|
| **T1-F1** (FAIL, Step 15) | Added **H18**, threshold-side smoothness on an open interval $I_\tau$: $C^1$ maps $t\mapsto\Omega(t,T)$ and $t\mapsto\partial_\kappa M_P(\kappa,t,T)$, with $\Omega\in(0,1)$ and $\mathcal S_P>0$ there, and A(br)+(br-v) at every pair in $I_\tau$. Step 15 rewritten to cite it, to say that H14 leg 1 **plus** differentiability (not leg 1 alone) gives $\Omega_{r_\tau}\ge0$, and to state its scope: conditional on H18, consumed by no later step, Steps 9–14 and the boxed Step 13 untouched. |
| **T1-R1** (Step 2) | Differentiation now licensed by H4 and H6 (two factors constant in $\kappa$, so $\Delta^{\mathrm{act}}$ is an affine image of $M_P$) with H7 on $M_P$; boundedness (A2) explicitly demoted — it is not differentiability. Three-term display kept as bookkeeping. Non-circularity of the forward citations recorded. |
| **T1-R2** (Step 5) | Added **H16**, the no-feedback timing of card §2, as a numbered hypothesis (the card instructs this), cited at Steps 3 and 5. The $\kappa$-freedom of the law of $s$ now cites A1 **and** card §4.1's distributional rows plus the fact that $\kappa$ enters only the $z_d$ row. |
| **T1-R3** (H6, Step 7) | H6 restated as **constancy** of $\Omega$ in $\kappa$, with the derivative form as its corollary; Step 7 now cites the constancy form, which is what "common to both nodes" needs. |
| **T1-R4** (Step 11 item 3) | Added **H17**, clause **(br-v)**: $C_h(\cdot)$ and the kernel $h$ are the same functions of the posterior at $\tau$ and $\tau'$. Labelled T1-LOCAL and marked as **this file's addition beyond L4's A(br)**, not attributed to L4. Cited at Step 11 item 3; the clause tally, the CLAIM, LABEL CLAIMED, NOT CLAIMED 4 and NOTATION DELTA all updated. |
| **T1-R5** (Step 20) | Monotonicity of $r\mapsto\Omega(r)$ moved into **H15** (free at the endpoints, and the interpolant is otherwise unconstrained between integer windows); Step 20 now cites H15, not Step 16, for $\Omega_{r_T}\ge0$, and records that the boxed iff is pure algebra and unaffected either way. Block 5's predicted sign re-pointed to H15. |
| **T1-R6** (WHERE IT FAILS 4) | Case 4 split into three routes: $\bar\pi\downarrow0$, $A'_\kappa=0$, and $C_h(\bar\pi)=0$ at $\bar\pi>0$. The last is handled explicitly as card §5 demands, including that H11's monotonicity forces the degeneracy to propagate to the tighter threshold, that H14 leg 3 then holds with equality, and that Step 13 must be read off Step 6 rather than through $W_\tau C_\tau$. L4's equality qualifier carried into **H14**. |
| **T1-R7** (stale card) | Re-stamped to **2026-08-21 · `a175202`+** in the header and H1; the four citations reading A7-injective satisfiability as *open* (H4, WHERE IT FAILS 6, LABEL CLAIMED 3, NOT CLAIMED 5) re-pointed to §5's ticket-24 note (**resolved**), with the live risk narrowed to whether this model's menu satisfies **A7′** (card §4.2), whose failure boundary is now named. |
| **T1-R8** (NOTATION DELTA) | Added rows for $\Omega^\*$/$k_D^\*$ and for $I$/$I_\tau$; added a row for (br-v). |
| **T1-R9** (the ledger's "equivalently") | The card-owner flag rewritten to propose the **quantifier fix** — "equivalently, on average along the tightening path", with pointwise $\rho\le0$ named as sufficient but not necessary — instead of demoting the row to the infinitesimal reading. The exact finite-scale equivalence of Step 21a is displayed. |
| Housekeeping | Bracketed step-lists on H2, H6, H8, H13, H14 corrected (T1-O7); NOT CLAIMED 13 added for Step 15's conditionality. |

**Not applied, and why.** The audit's seven OBSERVATIONS (T1-O1 … T1-O7) are outside this round's
mandate, which was T1-F1 plus R1–R9. Three of them are card-owner-facing rather than file-facing
(**T1-O6**, the ledger's threshold row must read "under A($\tau$) and A(br)" — now also "+(br-v)";
**T1-O3b**, the $\bar\pi_{\mathrm{pr}}\le1/2$ restriction L4 inherits under the level-symmetric
reading; **T1-O2**, L4's ambiguous leg numbering in the source). **T1-O1** (Step 8 sits under the
Part A heading but is consumed only in Part B) and **T1-O4**/**T1-O5** (two clarifying sentences)
are left for the re-derivation round. **No label moves: T1 remains CONJECTURE.**

### Recheck items N1–N4 applied (2026-08-21, orchestrator)

Per `threads/2026-08-21_T1_fix_recheck.md` (verdict: T1-F1 discharged; four
one-clause citation items; close after edit, no re-proof-read): N1 — noise-mark
law repointed §4.2 → §4.1. N2 — H14 leg 2 restated as the SHARE inequality
(π̄_pr), the endpoint step attributed to (br-iv), per the binding π̄ ruling.
N3 — the cross-policy |C_h| comparison in Step 22 now cites H17 = (br-v).
N4 — Step 22's hypothesis range H1–H15 → H1–H18. Fix round CLOSED.

### FILE: proofs/C1_proof.md

# C1 — GE region certificate

**Ticket 29 (T2i). Written against `research/model_v4/MODEL_CARD.md`, version stamp
2026-08-21 · commit `a175202`+.** Card §4 notation is binding; the answer template is card §8
rule 6. Upstream results are cited by their card-ledger IDs (L1, L2, T1) and by the card's
hypothesis labels (A8, A($\tau$), AGE). The companion executed check is
`quality_reports/fixes/t2_c1_region_check.py` with output
`quality_reports/fixes/t2_c1_region_check.json`.

---

## CLAIM

Fix a window $T$, a plan menu and a strictness coordinate $r$ (card §4.5:
$r_\tau=-\tau$ or $r_T=-T$; higher $r$ = tighter). Let $\mathcal R_r$ be a named set of
parameter vectors $\vartheta=(\kappa,r)$ on which H2–H8 below hold. Then:

**(A) Inversion-free derivative bounds.** The equilibrium cutoff vector $k$ solving
$k=\mathcal T(k;\vartheta)$ is a twice continuously differentiable function of $\vartheta$ on
$\mathcal R_r$, and its derivatives obey the card §4.5 bounds
$$
\lVert\partial_\kappa k\rVert\le\bar k_\kappa=\frac{\lvert\partial_\kappa\mathcal T\rvert}{1-L_{\mathcal R}},
\qquad
\lVert\partial_r k\rVert\le\bar k_r=\frac{\lvert\partial_r\mathcal T\rvert}{1-L_{\mathcal R}},
$$
$$
\lVert\partial^2_{\kappa r}k\rVert\le\bar k_{\kappa r}
=\frac{\lvert\mathcal T_{\kappa r}\rvert+\lvert\mathcal T_{\kappa k}\rvert\bar k_r
+\lvert\mathcal T_{rk}\rvert\bar k_\kappa+\lvert\mathcal T_{kk}\rvert\bar k_\kappa\bar k_r}
{1-L_{\mathcal R}} .
$$
No inverse of $I-D_k\mathcal T$ is formed; each bound is a Neumann geometric sum.

**(B) The GE remainder bound is exactly $\mathcal B_r^{GE}$.** Writing
$\Delta^{\mathrm{act}}(k,\kappa,r)$ for the **fixed-policy** premium of card §4.4 and
$\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)$ for its **equilibrium** value, the
equilibrium cross-derivative differs from the fixed-policy one by at most the card §4.5 bound:
$$
\Bigl\lvert
\frac{d^2\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)}{d\kappa\,dr}
-\partial_{\kappa r}\Delta^{\mathrm{act}}
\Bigr\rvert
\;\le\;
\mathcal B_r^{GE}
=\lvert\Delta_{\kappa k}\rvert\bar k_r
+\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa
+\lvert\Delta_k\rvert\bar k_{\kappa r}.
$$

**(C) Dominance: the fixed-policy attenuation sign survives in equilibrium.** If in addition
$g_r^{PE}>\mathcal B_r^{GE}$ on $\mathcal R_r$, then writing $\mathcal S$ for the equilibrium
liquidity-sensitivity $\lvert d\Delta^{\mathrm{act}}/d\kappa\rvert$ evaluated along
$k(\kappa,r)$,
$$
\boxed{\;\partial_r\mathcal S\;\le\;-\eta_r\;<\;0
\qquad\text{at every }\vartheta\in\mathcal R_r,\quad \eta_r=g_r^{PE}-\mathcal B_r^{GE}.\;}
$$
Equivalently: tightening the margin strictly attenuates the premium's liquidity-sensitivity in
equilibrium, by at least $\eta_r$ per unit of strictness. Under H8 the same statement reads
"T1's fixed-policy attenuation sign survives in equilibrium on $\mathcal R_r$", which is the
ledger's wording.

**(D) Finite scale.** If $\mathcal R_r$ contains a segment $[r_0,r_1]$ at fixed $\kappa$, then
$\mathcal S(\kappa,r_1)-\mathcal S(\kappa,r_0)\le-\int_{r_0}^{r_1}\eta_r\,dr<0$.

**Nonemptiness of $\mathcal R_r$ is not claimed here and is not provable here** — it is a
property of the calibration, and the companion script is what decides it. See NOT CLAIMED 1. The
run of 2026-08-21 found 18 certifying nodes of 80 and is reported under NUMERICAL CHECK REQUEST;
a set of certified nodes is still not a certified region (Step 11).

---

## HYPOTHESES

Every hypothesis is used; the step that consumes it is named in brackets.

**H1 — Card and stamp.** MODEL_CARD.md, stamp 2026-08-21 · `a175202`+. All symbols carry their
card §4 meanings: $\kappa$ is noise-trading intensity; upright $T$ is the filing window and
$\mathcal T$ is the outer best-response map; $k=(k_1,\dots,k_{J-1})$ is the cutoff vector and
$\Theta$ the compact ordered polytope; $r_\tau=-\tau$, $r_T=-T$. No card symbol is renumbered.
[all steps]

**H2 — AGE (card §5, verbatim).** *"On a candidate region $\mathcal R$ the outer map is twice
continuously differentiable, $L_{\mathcal R}<1$, and the sign of the equilibrium liquidity
derivative is constant on $\mathcal R$."* Two readings of $L_{\mathcal R}=\sup_{\mathcal R}\lVert
D_k\mathcal T\rVert$ (card §4.5) must be kept apart, because different steps need different
ones:

- **(H2a) along-the-path reading.** $L_{\mathcal R}=\sup_{\vartheta\in\mathcal R}\lVert
  D_k\mathcal T(k(\vartheta);\vartheta)\rVert$ — the supremum over parameters of the norm **at
  the equilibrium cutoff vector**. This is what Steps 1–4 need, and it is what the companion
  script measures.
- **(H2b) over-$\Theta$ reading.** $L_{\mathcal R}=\sup_{\vartheta\in\mathcal R}\sup_{k\in\Theta}
  \lVert D_k\mathcal T(k;\vartheta)\rVert$. Strictly stronger, and **not** measured. **No step in
  the proof of (A)–(D) uses it**; Step 12 discusses what it would add, namely the upgrade of
  Step 1's *local* uniqueness to a global one on $\Theta$.

Where "$L_{\mathcal R}<1$" appears below without qualification, H2a is meant. [Steps 1–4, 7, 12]

**H3 — Interior equilibrium on a single branch.** At every $\vartheta\in\mathcal R_r$ there is a
cutoff vector $k(\vartheta)$ in the **interior** of $\Theta$ with $k(\vartheta)=\mathcal
T(k(\vartheta);\vartheta)$, and $\vartheta\mapsto k(\vartheta)$ is one branch — no switch of
selected equilibrium occurs inside $\mathcal R_r$. Interiority is a genuine restriction: card §3
permits collapsed action regions (weak inequalities $k_1\le\dots\le k_{J-1}$), and a collapsed
region puts $k$ on $\partial\Theta$, where the fixed-point equation may hold only as a
variational inequality and $k(\cdot)$ need not be differentiable. [Steps 1, 5, 12]

**H4 — Twice continuous differentiability and boundedness of the premium in
$(k,\kappa,r)$.** The fixed-policy map $(k,\kappa,r)\mapsto\Delta^{\mathrm{act}}(k,\kappa,r)$ of
card §4.4 is twice continuously differentiable on a neighbourhood of
$\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$, and the derivatives named in
$\mathcal B_r^{GE}$ — $\Delta_k$, $\Delta_{kk}$, $\Delta_{\kappa k}$, $\Delta_{kr}$,
$\Delta_{\kappa r}$ — together with those named in $\bar k_{\kappa r}$ —
$\mathcal T_{\kappa r},\mathcal T_{\kappa k},\mathcal T_{rk},\mathcal T_{kk}$ — are finite there.
This is the turn-1 C1 hypothesis 4 ("all required first and second derivatives of
$\Delta^{\mathrm{act}}$ and $\mathcal T$ are bounded on the region"), stated with the
differentiability it presupposes. Card §5's **A2′** — local boundedness of prices and payoffs
together with $\mathbb E[\max_j\lvert U_j\rvert]<\infty$, the clause that replaced A2's flat
boundedness when the latter was found false — is **not** cited for it: boundedness is not
differentiability, and A2′ is further from supplying it than A2 was. [Steps 5, 6, 9]

**H5 — Non-vanishing equilibrium liquidity derivative.**
$d\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)/d\kappa\neq0$ at every
$\vartheta\in\mathcal R_r$. H2's constancy clause fixes a common sign; H5 is what keeps the
argument of $\lvert\cdot\rvert$ away from the one point where $\lvert\cdot\rvert$ is not
differentiable. The two are separate assertions and both are needed. [Step 7]

**H6 — Strict dominance (card §4.5).** $g_r^{PE}>\mathcal B_r^{GE}$, i.e. $\eta_r>0$, at every
$\vartheta\in\mathcal R_r$, with
$g_r^{PE}=-\operatorname{sgn}\!\left(d\Delta^{\mathrm{act}}/d\kappa\right)
\partial_{\kappa r}\Delta^{\mathrm{act}}$ where the sign is the **equilibrium** liquidity
derivative's, per the card §4.5 row. [Steps 8, 10]

**H7 — A smooth strictness domain.** The coordinate $r$ ranges over an open interval on which
the objects of H2 and H4 are defined. For $r_\tau=-\tau$ card §4.1 places no discreteness on
$\tau$, so only smoothness is being assumed, not a domain. For $r_T=-T$ the card's $T$ ranges
over $\{1,\dots,H\}$, so the $r_T$ instance additionally needs a smooth window interpolation —
the same added hypothesis T1 carries as its H15, imported here unchanged and named where it
bites (WHERE IT FAILS 6). [Steps 3, 4, 5]

**H8 — Sign coherence (used only to name $g_r^{PE}$, never to reach the conclusion).**
$\operatorname{sgn}\bigl(\partial_\kappa\Delta^{\mathrm{act}}(k(\vartheta),\vartheta)\bigr)
=\operatorname{sgn}\bigl(d\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)/d\kappa\bigr)$
on $\mathcal R_r$: the fixed-policy and equilibrium liquidity derivatives point the same way.
Card §4.5 defines $g_r^{PE}$ with the **equilibrium** sign but calls it the *fixed-policy*
attenuation margin; H8 is exactly the clause that makes both halves of that name true at once.
The boxed conclusion (C) does **not** use H8 — Step 9 is where it is consumed, and Step 9 is a
statement about what (C) may be called. [Step 9]

---

## PROOF

Throughout, $\lVert\cdot\rVert$ on the cutoff space $\mathbb R^{J-1}$ is $\lVert\cdot\rVert_\infty$
and $\lVert D_k\mathcal T\rVert$ is the induced operator norm (maximum absolute row sum). For the
multilinear objects the card §4.5 bars mean the smallest constants making the displayed products
valid, namely
$$
\lvert\mathcal T_{\kappa k}\rvert=\max_i\sum_l\lvert\mathcal T^i_{\kappa k_l}\rvert,\quad
\lvert\mathcal T_{rk}\rvert=\max_i\sum_l\lvert\mathcal T^i_{r k_l}\rvert,\quad
\lvert\mathcal T_{kk}\rvert=\max_i\sum_{j,l}\lvert\mathcal T^i_{k_jk_l}\rvert,\quad
\lvert\mathcal T_{\kappa r}\rvert=\max_i\lvert\mathcal T^i_{\kappa r}\rvert,
$$
$$
\lvert\Delta_k\rvert=\sum_j\lvert\Delta_{k_j}\rvert,\quad
\lvert\Delta_{\kappa k}\rvert=\sum_j\lvert\Delta_{\kappa k_j}\rvert,\quad
\lvert\Delta_{kr}\rvert=\sum_j\lvert\Delta_{k_jr}\rvert,\quad
\lvert\Delta_{kk}\rvert=\sum_{j,l}\lvert\Delta_{k_jk_l}\rvert .
$$
These are the dual pairings that make the displayed products valid: for the bilinear objects,
$\lvert\mathcal T_{kk}[w_1,w_2]\rvert\le\lvert\mathcal T_{kk}\rvert\lVert w_1\rVert\lVert
w_2\rVert$ and likewise for $\Delta_{kk}$; for the linear ones,
$\lvert\Delta_{\kappa k}[w]\rvert\le\lvert\Delta_{\kappa k}\rvert\lVert w\rVert$ and likewise
for $\mathcal T_{\kappa k},\mathcal T_{rk},\Delta_{kr},\Delta_k$. (Card §4.6 rules $u_1,u_2$
proof-local and forbids a bare $u$, so the arguments here are written $w,w_1,w_2$; $w$ carries no
card meaning.) Card §4.5 writes the bars without fixing a norm, and NOTATION DELTA flags the
choice for the card owner. Any other consistent pairing changes the numerical value of
$\mathcal B_r^{GE}$ but not one line of the argument.

### Part A — the implicit-function step

**Step 1 (the equilibrium is a twice continuously differentiable function of the parameters).**
Define $\Psi(k;\vartheta)=k-\mathcal T(k;\vartheta)$ on a neighbourhood $\mathcal N\subseteq
\operatorname{int}\Theta\times\mathcal R_r$ of the equilibrium graph
$\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$ — **the same domain H4 chooses for
$\Delta^{\mathrm{act}}$, and the weakest one Steps 1–4 use**; every $\mathcal T$ derivative below
is evaluated at $(k(\vartheta);\vartheta)$, so smoothness away from the graph is never called on.
(Card §5's AGE says the outer map is twice continuously differentiable "on a candidate region
$\mathcal R$" without saying over which $k$ — the same ambiguity H2a/H2b flags for the norm.
NOTATION DELTA carries it as a card-owner flag; taking the weaker reading here means no step
depends on how it is resolved.) By H2 $\mathcal T$ is twice continuously differentiable on
$\mathcal N$, so $\Psi$ is, and $D_k\Psi=I-D_k\mathcal T$. Fix $\vartheta\in\mathcal R_r$ and let
$w$ satisfy $\lVert w\rVert=1$. By the reverse triangle inequality and H2a,
$$
\lVert(I-D_k\mathcal T)w\rVert\ \ge\ \lVert w\rVert-\lVert D_k\mathcal T\,w\rVert
\ \ge\ 1-L_{\mathcal R}\ >\ 0 .
$$
A linear map on a finite-dimensional space that is bounded below is injective, hence invertible.
By H3, $k(\vartheta)$ is an interior zero of $\Psi(\cdot;\vartheta)$; the implicit function
theorem then supplies a neighbourhood of $\vartheta$ on which the zero is unique and the map
$\vartheta\mapsto k(\vartheta)$ is as smooth as $\Psi$, i.e. twice continuously differentiable.
H3's single-branch clause is what lets these local objects be patched into one function on
$\mathcal R_r$.

**Step 2 (Neumann bound — no inverse is formed).** By H2a, $\lVert D_k\mathcal T\rVert\le
L_{\mathcal R}<1$, so $\sum_{n\ge0}\lVert(D_k\mathcal T)^n\rVert\le\sum_{n\ge0}L_{\mathcal
R}^{\,n}=(1-L_{\mathcal R})^{-1}<\infty$, the series $\sum_{n\ge0}(D_k\mathcal T)^n$ converges
absolutely in operator norm, and multiplying it by $(I-D_k\mathcal T)$ telescopes to $I$. Hence
$$
\bigl\lVert(I-D_k\mathcal T)^{-1}\bigr\rVert\ \le\ \frac{1}{1-L_{\mathcal R}} .
$$
This is the step the word "inversion-free" names: the bound is a geometric sum of norms, so
every derivative bound below is available from $\lVert D_k\mathcal T\rVert$ and one directional
derivative of $\mathcal T$, without solving a linear system.

**Step 3 (first-derivative bounds — the $\bar k_x$ row of card §4.5).** Let $x\in\{\kappa,r\}$;
H7 makes $x$ a coordinate on an open interval. Differentiate the identity
$k(\vartheta)=\mathcal T(k(\vartheta);\vartheta)$ in $x$, which Step 1 licenses, using the chain
rule on the first argument:
$$
\partial_xk=D_k\mathcal T\,\partial_xk+\partial_x\mathcal T
\qquad\Longleftrightarrow\qquad
(I-D_k\mathcal T)\,\partial_xk=\partial_x\mathcal T .
$$
Apply Step 2's operator bound to the right-hand side:
$$
\lVert\partial_xk\rVert\ \le\ \frac{\lVert\partial_x\mathcal T\rVert}{1-L_{\mathcal R}}
\ =\ \bar k_x ,
$$
which is card §4.5's row verbatim. Note which derivative appears on the right: $\partial_x\mathcal
T$ is the **partial** derivative of the best-response map in the parameter, holding $k$ fixed —
the belief-and-price response at frozen cutoffs — not a total derivative.

**Step 4 (the cross-derivative bound — the $\bar k_{\kappa r}$ row).** Differentiate the
$x=\kappa$ instance of Step 3 once more, in $r$. Written in components, with every $\mathcal T$
derivative evaluated at $(k(\vartheta);\vartheta)$ and the chain rule applied through
$k(\vartheta)$ in each slot,
$$
\partial^2_{\kappa r}k^i
=\sum_j\Bigl[\Bigl(\sum_l\mathcal T^i_{k_jk_l}\,\partial_rk^l+\mathcal T^i_{k_jr}\Bigr)\partial_\kappa k^j
+\mathcal T^i_{k_j}\,\partial^2_{\kappa r}k^j\Bigr]
+\sum_l\mathcal T^i_{\kappa k_l}\,\partial_rk^l+\mathcal T^i_{\kappa r},
$$
that is,
$$
(I-D_k\mathcal T)\,\partial^2_{\kappa r}k
=\mathcal T_{\kappa r}
+\mathcal T_{\kappa k}[\partial_rk]
+\mathcal T_{rk}[\partial_\kappa k]
+\mathcal T_{kk}[\partial_rk,\partial_\kappa k].
$$
Take norms on the right using the pairings fixed above and Step 3's bounds
$\lVert\partial_\kappa k\rVert\le\bar k_\kappa$, $\lVert\partial_rk\rVert\le\bar k_r$; then apply
Step 2 once more:
$$
\lVert\partial^2_{\kappa r}k\rVert
\le\frac{\lvert\mathcal T_{\kappa r}\rvert+\lvert\mathcal T_{\kappa k}\rvert\bar k_r
+\lvert\mathcal T_{rk}\rvert\bar k_\kappa+\lvert\mathcal T_{kk}\rvert\bar k_\kappa\bar k_r}
{1-L_{\mathcal R}}=\bar k_{\kappa r},
$$
which is card §4.5's row verbatim. Part (A) of the CLAIM is Steps 1, 3 and 4.

### Part B — the GE remainder

**Step 5 (the exact cross-derivative decomposition).** Write
$\Delta^*(\kappa,r):=\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)$. By H4 and Step 1
the composition is twice continuously differentiable on $\mathcal R_r$ (H7 supplies the open
domain in $r$). The chain rule in $\kappa$ gives
$$
\partial_\kappa\Delta^*=\Delta_k\!\cdot\!\partial_\kappa k+\Delta_\kappa ,
$$
and differentiating that in $r$, term by term —
$\partial_r(\Delta_k)=\Delta_{kk}[\partial_rk]+\Delta_{kr}$ and
$\partial_r(\Delta_\kappa)=\Delta_{\kappa k}[\partial_rk]+\Delta_{\kappa r}$ — gives the exact
identity
$$
\partial^2_{r\kappa}\Delta^*
=\underbrace{\Delta_{\kappa r}}_{\text{fixed policy}}
+\underbrace{\Delta_{\kappa k}[\partial_rk]
+\bigl(\Delta_{kr}+\Delta_{kk}[\partial_rk]\bigr)\!\cdot\!\partial_\kappa k
+\Delta_k\!\cdot\!\partial^2_{\kappa r}k}_{\text{GE remainder}} .
$$
Nothing is dropped and no inequality has been used: this is one identity in four groups. The
four groups are the four ways a cutoff response can enter — the pooled-cell composition moving
with the cutoffs as $\kappa$ moves, the cutoffs' own response to the rule, that response's
interaction with the liquidity response, and the premium's first-order exposure to a
second-order cutoff response. The third term of T1's Step 2 display,
$(\partial_\kappa\Omega)(M_F-M_P)$, is the piece of $\Delta_k\!\cdot\!\partial_\kappa k$ that
T1's fixed-policy hypothesis set the equilibrium free of; it reappears here inside the remainder,
which is what T1's NOT CLAIMED 2 said C1 would have to bound.

**Step 6 (the remainder is bounded by $\mathcal B_r^{GE}$).** Apply the triangle inequality to
the three remainder groups of Step 5, then the pairings fixed above, then Step 3 for
$\lVert\partial_\kappa k\rVert$ and $\lVert\partial_rk\rVert$ and Step 4 for
$\lVert\partial^2_{\kappa r}k\rVert$. H4 makes every factor finite. Group by group:
$$
\bigl\lvert\Delta_{\kappa k}[\partial_rk]\bigr\rvert\le\lvert\Delta_{\kappa k}\rvert\bar k_r,\quad
\bigl\lvert\bigl(\Delta_{kr}+\Delta_{kk}[\partial_rk]\bigr)\!\cdot\!\partial_\kappa k\bigr\rvert
\le\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa,\quad
\bigl\lvert\Delta_k\!\cdot\!\partial^2_{\kappa r}k\bigr\rvert\le\lvert\Delta_k\rvert\bar k_{\kappa r} .
$$
Summing the three,
$$
\bigl\lvert\partial^2_{r\kappa}\Delta^*-\Delta_{\kappa r}\bigr\rvert
\ \le\ \lvert\Delta_{\kappa k}\rvert\bar k_r
+\bigl(\lvert\Delta_{kr}\rvert+\lvert\Delta_{kk}\rvert\bar k_r\bigr)\bar k_\kappa
+\lvert\Delta_k\rvert\bar k_{\kappa r}
\ =\ \mathcal B_r^{GE},
$$
card §4.5's row verbatim. This is Part (B) of the CLAIM. Card §4.5 calls this *one admissible*
bound; the wording is exact, and NOT CLAIMED 5 keeps it.

### Part C — dominance

**Step 7 (the equilibrium sensitivity is differentiable, and its $r$-derivative).** By H2's
constancy clause the sign of $d\Delta^*/d\kappa$ is one and the same on $\mathcal R_r$, and by H5
that derivative never vanishes there. Hence on $\mathcal R_r$
$$
\mathcal S\ :=\ \bigl\lvert\partial_\kappa\Delta^*\bigr\rvert
\ =\ \operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\,\partial_\kappa\Delta^*
$$
is an identity **of functions on $\mathcal R_r$**, not merely of values at one point: the factor
on the right is a constant $\pm1$. Constancy is what permits differentiating it, and H5 is what
keeps $\partial_\kappa\Delta^*$ off the kink of $\lvert\cdot\rvert$. Differentiating in $r$ —
permitted by Step 5's twice continuous differentiability —
$$
\partial_r\mathcal S
=\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\,\partial^2_{r\kappa}\Delta^* .
$$

**Step 8 (dominance).** Multiply Step 5's identity by the constant
$\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)$ and read the first group through card
§4.5's definition of $g_r^{PE}$, which uses that same sign:
$$
\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\Delta_{\kappa r}
=-\left[-\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\partial_{\kappa r}\Delta^{\mathrm{act}}\right]
=-\,g_r^{PE} .
$$
For the remaining groups, multiplying by a factor of modulus one leaves the modulus alone, so
Step 6 bounds them by $\mathcal B_r^{GE}$. Combining with Step 7,
$$
\partial_r\mathcal S\ =\ -g_r^{PE}
+\operatorname{sgn}\!\left(\frac{d\Delta^{\mathrm{act}}}{d\kappa}\right)\bigl[\text{GE remainder}\bigr]
\ \le\ -g_r^{PE}+\mathcal B_r^{GE}\ =\ -\eta_r .
$$
By H6, $\eta_r>0$, so $\partial_r\mathcal S\le-\eta_r<0$: the boxed conclusion (C). Observe that
the argument never needs the remainder's sign, only its size — which is the whole point of
bounding rather than signing the GE channel.

**Step 9 (what "the fixed-policy attenuation sign survives" means, and where H8 bites).** At
fixed policies T1's object is $\mathcal S(\kappa,\tau,T)=\lvert\partial_\kappa\Delta^{\mathrm{
act}}\rvert$ at a **frozen** $k$, whose $r$-derivative is
$\operatorname{sgn}(\partial_\kappa\Delta^{\mathrm{act}})\,\partial_{\kappa r}\Delta^{\mathrm{
act}}$. Under H8 that leading sign is the same $\pm1$ as the one in $g_r^{PE}$, so the
fixed-policy $r$-derivative equals $-g_r^{PE}$ exactly, and
$$
g_r^{PE}>0\iff\text{strict fixed-policy attenuation at that node.}
$$
Step 8 then reads: fixed-policy attenuation, by a margin exceeding $\mathcal B_r^{GE}$, implies
equilibrium attenuation. Without H8 nothing in Steps 1–8 changes — none of them cites H8 — but
$g_r^{PE}$ would then be an orientation of the cross-derivative by the *equilibrium* sign while
the fixed-policy comparative static ran the other way, and the ledger's phrase "the fixed-policy
attenuation sign" would not describe it. The companion script therefore reports both signs and
the count of nodes where they disagree, rather than assuming coherence.

**Step 10 (finite scale).** Suppose $\mathcal R_r$ contains the segment
$\{(\kappa,r):r\in[r_0,r_1]\}$. By Step 5, $r\mapsto\mathcal S(\kappa,r)$ is continuously
differentiable there, so the fundamental theorem of calculus and Step 8 give
$$
\mathcal S(\kappa,r_1)-\mathcal S(\kappa,r_0)=\int_{r_0}^{r_1}\partial_r\mathcal S\,dr
\ \le\ -\int_{r_0}^{r_1}\eta_r\,dr\ <\ 0 ,
$$
the last inequality because $\eta_r>0$ (H6) and continuous on a segment of positive length.
Continuity of $\eta_r$ is not an extra assumption; it is already on the table. $g_r^{PE}$ is
continuous because $\partial_{\kappa r}\Delta^{\mathrm{act}}$ is (H4's $C^2$ clause, along the
$C^2$ path $k(\cdot)$ of Step 1) and its $\pm1$ prefactor is constant on $\mathcal R_r$ (Step 7);
$\mathcal B_r^{GE}$ is continuous because each factor in it is a continuous derivative of
$\mathcal T$ or $\Delta^{\mathrm{act}}$ (H2, H4) composed with the continuous $\bar k_x$, all
divided by the **region-constant** $1-L_{\mathcal R}$. A positive continuous function on a
segment of positive length has a positive integral. (Measurability plus positivity would suffice
just as well, and is the cheaper route if one prefers not to invoke H4 here.) This
is Part (D), and it is the form an empirical comparison of two rules can use: a bound on the
level change, not merely a sign at a point.

**Step 11 (a grid of certified nodes is not yet a certified region).** Steps 1–10 are
statements at each $\vartheta\in\mathcal R_r$; a numerical run evaluates them at finitely many
nodes. Certified nodes promote to a certified region only with a modulus of continuity: if
$\vartheta\mapsto\eta_r(\vartheta)$ is Lipschitz with constant $M$ on the convex hull of two
adjacent nodes at distance $\delta$, and $\eta_r\ge\eta_{\min}$ at both, then
$\eta_r\ge\eta_{\min}-M\delta/2$ on the hull, which is positive exactly when
$\eta_{\min}>M\delta/2$. **The companion script does not estimate $M$**, so what it reports is a
set of certified nodes, and the promotion to a region is an explicit open item rather than a
silent interpolation. The same gap applies to $L_{\mathcal R}$: a supremum over $\mathcal R$
cannot be read off finitely many nodes.

**Step 12 (what H2b would add, and why no step needs it).** Under H2b, $\mathcal
T(\cdot;\vartheta)$ is a contraction on the convex compact $\Theta$ (card §4.5), so Banach's
theorem gives a **unique** fixed point in $\Theta$ at that $\vartheta$, H3's single-branch clause
becomes automatic, and the equilibrium selection cannot jump. Under H2a alone, Step 1 gives only
local uniqueness near $k(\vartheta)$, and H3 carries the branch. The distinction is recorded
because the companion script measures the along-the-path norm and therefore certifies under H2a;
claiming uniqueness from it would be an over-read. Card §3's "Uniqueness is **not** claimed"
stands.

---

## WHERE IT FAILS

1. **$L_{\mathcal R}\ge1$ anywhere on $\mathcal R_r$.** $L_{\mathcal R}$ is a supremum, so a
   single parameter vector at which $\lVert D_k\mathcal T\rVert\ge1$ voids the certificate on the
   **whole** region, not only at that vector. Three things break at once: Step 2's Neumann series
   diverges; $1-L_{\mathcal R}\le0$ makes every $\bar k$ meaningless (negative or infinite); and
   if $1$ is an eigenvalue of $D_k\mathcal T$ then $I-D_k\mathcal T$ is singular, Step 1's
   implicit function theorem does not apply, and the equilibrium cutoff vector need not be a
   function of $\vartheta$ at all — a continuum of equilibrium cutoffs at one parameter is exactly
   the configuration $L_{\mathcal R}=1$ permits. Nothing in the certificate can be salvaged
   node-by-node in that case, because the objects $\bar k_x$ are region-level.

2. **A sign change of the equilibrium liquidity derivative inside $\mathcal R_r$** — AGE's
   constancy clause failing. At a parameter where $d\Delta^{\mathrm{act}}/d\kappa=0$ the function
   $\mathcal S=\lvert\partial_\kappa\Delta^*\rvert$ has a kink, $\partial_r\mathcal S$ does not
   exist, and Step 7's identity of functions is false on any set straddling the crossing (the
   $\pm1$ factor is not constant there). This is a live configuration, not a hypothetical: the
   committed smoke run (`numerical_v4/smoke_output.txt`) shows $M_P$ hump-shaped in $\kappa$ at
   the baseline calibration with $dM_P/d\kappa$ changing sign near $\kappa\approx0.55$, so any
   candidate region containing that peak violates the clause. A region must be carved to one side
   of the turning point, and doing so is what makes the certificate regional rather than global.

3. **The equilibrium leaves the interior of $\Theta$** — H3 failing. Card §3's weak inequalities
   permit a collapsed action region (draft_v2's baseline collapses Hold, $k_1=k_0$). On
   $\partial\Theta$ the equilibrium is characterised by a one-sided condition rather than
   $k=\mathcal T(k;\vartheta)$ as an interior equation, the implicit function theorem of Step 1
   does not apply, and $k(\cdot)$ can be non-differentiable — typically with a kink exactly where
   a region collapses, which is where comparative statics are most interesting.

4. **Multiple equilibria with a discontinuous selection.** Even where the local implicit function
   theorem applies to each branch, a switch of selected branch inside $\mathcal R_r$ makes
   $k(\cdot)$ jump, so $\partial_\kappa k$, $\partial_rk$ and $\partial^2_{\kappa r}k$ do not
   exist at the switch and Steps 3–5 are void. Under H2a this cannot be excluded; under H2b it
   can (Step 12).

5. **$\eta_r\le0$: no certificate, and no counter-claim either.** If $g_r^{PE}\le\mathcal
   B_r^{GE}$ the argument stops at Step 6 and says nothing about the sign of
   $\partial_r\mathcal S$. Because $\mathcal B_r^{GE}$ is a triangle-inequality bound, a failure
   of dominance is compatible with equilibrium attenuation, with equilibrium amplification, and
   with equality. Reading $\eta_r\le0$ as evidence against attenuation is a misuse of the
   certificate.

6. **The window instance without a smooth interpolation.** For $r_T=-T$ the card's window is an
   integer, $T\in\{1,\dots,H\}$ (card §4.1). Every derivative in Steps 3–8 taken with $x=r_T$
   then fails to exist, and $\partial_{\kappa r_T}\Delta^{\mathrm{act}}$ — hence $g_{r_T}^{PE}$
   itself — is undefined. H7 imports T1's H15 to supply an interpolation; without it the window
   instance of C1 has no content, and only the threshold instance $r_\tau=-\tau$ is available from
   the card alone. The companion script computes no $r_T$ certificate for this reason.

7. **A quantised threshold map: $\Delta^{\mathrm{act}}$ not differentiable in $\tau$, or locally
   constant in it.** H4 asks for a twice continuously differentiable
   $(k,\kappa,r)\mapsto\Delta^{\mathrm{act}}$. Two distinct failures live here and the second is
   easy to miss. (i) If the flagged set moves in jumps as $\tau$ falls — which happens whenever
   the crossing date is an integer-valued function of $\tau$, as card §4.2's
   $c_j=\inf\{d:B_j(s,d)\ge\tau\}$ makes it on a discrete calendar — then $\Omega(\cdot,T)$ is a
   step function of $\tau$, $\Delta^{\mathrm{act}}$ inherits the jumps, and
   $\partial_{\kappa r}\Delta^{\mathrm{act}}$ does not exist at them. This is T1's H18 failure
   mode, seen from the other side. (ii) **Between** the jumps the same discreteness makes
   $\Delta^{\mathrm{act}}$ locally *constant* in $\tau$, so $\partial_{\kappa r}\Delta^{\mathrm{
   act}}=0$ exactly and $g_r^{PE}=0$: H6 fails not because the GE remainder is large but because
   the direct margin is null. A node in that situation reports $\eta_r=-\mathcal B_r^{GE}\le0$ and
   is uncertifiable for a reason that has nothing to do with general equilibrium. The companion
   script separates the two attributions and reports the counts.

8. **$\mathcal T$ or $\Delta^{\mathrm{act}}$ not twice differentiable for a pricing reason** —
   H4 or H2's smoothness clause failing where card §5's A5 (unique, continuous inner price fixed
   point) holds but is not $C^2$ in beliefs, or where an off-path type's weight crosses zero and
   the belief map is only continuous. Continuity of $\mathcal T$ is what card §5's A6 supplies;
   AGE asks for more, and asks for it only on $\mathcal R$.

---

## LABEL CLAIMED

**CONJECTURE**, and two reasons carry it independently:

1. **Protocol.** Card §6: a result becomes PROVED only after an independent statements-only
   re-derivation PASS *and* an adversarial proof-read PASS, by different agents. The proof-read
   passed on 2026-08-21; the re-derivation is outstanding. This file is one half of the gate.
2. **No named region.** Card §6's intended-label row reads "C1 PROVED on a named **nonempty**
   region, NUMERICAL off-region, dropped if the region is empty." Parts (A)–(D) are implications;
   whether their antecedent is ever satisfied at the maintained calibration is decided by the
   companion script, not by this file. **The run did not come back empty** — 18 of 80 nodes
   certify, nine of them in one contiguous sign-homogeneous block — but that is a set of *nodes*.
   Naming a *region* needs Step 11's modulus of continuity, which no run in hand supplies, so the
   row's antecedent is not met either.

### The three objects, and the label each can carry

Passing both halves of the gate would not license one label but three, on three different
objects. Only the second has ever been in doubt.

1. **The certificate implication — (A), (B), (C), (D) read as conditionals** ("on a region where
   H2–H8 hold, …"). This is a pure implication. Its truth does not depend on any region being
   nonempty, and it is the object this file actually proves. **PROVED-eligible**, pending the
   re-derivation, with $\mathcal R_r$ carried as a **named hypothesis** — which is exactly what
   card §7 means by "Region-certified is not a fifth label: it is PROVED with the region named in
   the hypothesis." Card §6's C1 row must absorb the full hypothesis set before any label
   attaches: the row names only $L_{\mathcal R}<1$ and $g_r^{PE}>\mathcal B_r^{GE}$, omitting H3
   (interior equilibrium on a single branch), H4 ($C^2$ premium), H5 (non-vanishing equilibrium
   liquidity derivative) and H7 (a smooth strictness domain), and it does not separate H8's
   naming role from H6's use. Labelled against the row as written, C1 would be labelled against a
   statement this file does not prove.
2. **The 18 certified nodes — NUMERICAL, and nothing more.** Card §7's definition — "verified on
   a grid by an executed, committed check script with committed output" — fits them exactly. They
   are evidence that H2–H8 are jointly satisfiable at the maintained calibration. They are not a
   region.
3. **"C1 PROVED on a named nonempty region $\mathcal R_r$" — not available, and not obtainable
   from any run of this script.** That phrasing asserts the antecedent, and asserting it needs a
   set with interior plus a genuine supremum over that set. Step 11's Lipschitz constant $M$ is
   not estimated, and $L_{\mathcal R}$ is measured *pointwise along the equilibrium path*, node
   by node — a supremum over $\mathcal R$ cannot be read off finitely many evaluations. **No
   amount of grid refinement fixes this**: it needs a modulus of continuity for $\eta_r$ and a
   genuine supremum for $L_{\mathcal R}$, not more nodes. A live in-repo template for the
   promotion already exists — `quality_reports/fixes/d8_ge_dominance_check.py` certifies a
   *region* rather than a node set, by "(R1) pointwise dominance off an $\varepsilon$-ball around
   the channel-A peak and (R2) integral control inside it", and Part (D)'s integral form is the
   natural (R2) analogue here. A follow-on ticket should start from that construction rather than
   from a bare Lipschitz estimate.

The ledger row this file supports, once the re-derivation passes, is therefore: *C1 — the
certificate implication — **PROVED**, with $\mathcal R_r$ a hypothesis and H2–H8 named in full;
**NUMERICAL**: 18 of 80 nodes satisfy the hypothesis set at the maintained calibration, 9 of them
contiguous and sign-homogeneous; the promotion of certified nodes to a certified region
**OPEN**.* Until then the label is CONJECTURE and this file does not edit the ledger
(NOT CLAIMED 11).

### What C1 inherits from upstream, and what it does not

The economic content of the word "attenuation" is T1's, and C1 inherits T1's **conditionality**,
not its label. Card §6 now carries **T1 = PROVED at fixed policies** (proof-read, fix round
closed, re-derivation PASS, 2026-08-21). What propagates is the openness underneath it:
A($\tau$)'s applicability to the two-round pooled cell (card §9 item 1, **OPEN**); A(br) with its
clause (br-v) **assumed**; and A7′, whose *satisfiability* is resolved (card §5's ticket-24 note,
card §9) while its equilibrium selection — whether an equilibrium in which the separating plan is
actually *chosen* exists — remains card §9 item 2, **OPEN**. None of this moves C1's label in
either direction: reasons 1 and 2 above each hold it at CONJECTURE on their own.

The certificate's own hypotheses AGE, H3 and H4 are additionally not verified anywhere: the
companion script *measures* $L_{\mathcal R}$ along the equilibrium path but does not establish
AGE's differentiability clause, and no run can (WHERE IT FAILS 8). H3 is tested only as
$k_1<k_2$, which rules out the collapse faces of $\Theta$ but not its outer box faces, and H4 is
probed only by the curvature-to-slope diagnostic reported in the OUTCOME.

---

## NUMERICAL CHECK REQUEST

Executed as `quality_reports/fixes/t2_c1_region_check.py`; raw output
`quality_reports/fixes/t2_c1_region_check.json`.

**Formulas.** At each node $(\kappa,\tau,T)$: solve $k=\mathcal T(k;\vartheta)$; take a 33-point
second-order central stencil in $(k_1,k_2,\kappa,\tau)$ of both $\mathcal T$ and the
fixed-policy $\Delta^{\mathrm{act}}$; assemble
$L_{\mathcal R}=\lVert D_k\mathcal T\rVert_\infty$, then $\bar k_\kappa,\bar k_r$ (Step 3),
$\bar k_{\kappa r}$ (Step 4), $\mathcal B_r^{GE}$ (Step 6), and
$g_r^{PE}=-\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{
act}}$ with $r=r_\tau=-\tau$ and the sign taken from a re-solved equilibrium sweep in $\kappa$.
Report $\eta_r=g_r^{PE}-\mathcal B_r^{GE}$ and certify when $L_{\mathcal R}<1$ and $\eta_r>0$.

**Grid.** $\kappa\in[0.15,0.85]$, $T\in\{5,10\}$, $\tau$ at the 10th, 30th, 50th, 70th and 90th
percentiles of the baseline equilibrium's Voice $b^*(s)$, frozen once and reused (the 50th is the
committed $0.09076406$). **The $\kappa$ step is sized to the solver, not to the request.**
Measured: a 33-point stencil is about 40 s (each point is one pooled pass with run-up, one outer
map and one premium); a warm-started equilibrium re-solve at a *perturbed* parameter is about
43 s, because the solver drives $\lVert k-\mathcal T(k)\rVert$ to $10^{-10}$ and each damped
iteration costs a full pooled pass. A node without validation re-solves runs in 70–110 s; with
them, about 300 s. The requested $0.01$ grid is $71\times5\times2=710$ nodes, i.e. more than
eight hours before any validation, and **was not run**. The grid run is $\kappa$ step $0.10$,
i.e. $8\times5\times2=80$ nodes, with the six-re-solve validation on eight nodes spanning both
windows, the 10th/50th/90th thresholds and three liquidity levels. The JSON records the grid used
**and** the grid declined. A coarser certified grid honestly reported is the deliverable.

**Two readings of the equilibrium cross-derivative, and which nodes get which.** At every node
the equilibrium liquidity derivative and the equilibrium cross-derivative are read off the
implicit-function formula of Steps 3–5 — free, because the stencil already carries every
ingredient. At the eight validation nodes they are additionally read off re-solved equilibria,
which shares no arithmetic with the bound. The agreement of the two on the first derivative is
what licenses using the free reading elsewhere, and it is reported as a gating check.

**Predicted signs and magnitudes.**

*Block 1 — contraction.* $L_{\mathcal R}<1$ at every node, with the along-the-path reading (H2a)
named in the output. Any node with $L_{\mathcal R}\ge1$ is to be listed, not averaged away.

*Block 2 — the bound must contain the truth (the only verdict that can fail on substance).*
Compute $\partial^2_{r\kappa}\Delta^*$ twice by routes that do not share the bound's arithmetic:
by re-solving the equilibrium at the four corners $(\kappa\pm\varepsilon_\kappa,
\tau\pm\varepsilon_\tau)$ and cross-differencing, and by the implicit-function assembly of Steps 3–5. Then require
$$
\bigl\lvert\partial^2_{r\kappa}\Delta^*-\Delta_{\kappa r}\bigr\rvert\ \le\ \mathcal B_r^{GE}
$$
at every node with $L_{\mathcal R}<1$. *Predicted sign:* no violations. *Predicted magnitude:* the
ratio $\lvert\text{remainder}\rvert/\mathcal B_r^{GE}$ strictly below one and reported; a ratio
above one means Step 6's inequality is mis-assembled or the stencil straddles a kink, and is a
bug in one of the two, never evidence against the theorem. Separately, the two readings of
$d\Delta^*/d\kappa$ — re-solved and implicit-function — must agree to $5\times10^{-3}$ relative,
which is the executed test of Step 3's linear system.

*Block 3 — the certificate.* Report the count of certifying nodes, where they sit, and
$\min$/median/$\max$ of $\eta_r$ over them. **If no node certifies, the script must print
"EMPTY REGION" explicitly**; card §6 makes that a result, and no tolerance may be loosened to
avoid it. *No positive region size is predicted before the run.*

*Block 4 — failure attribution.* For every uncertified node say which hypothesis failed:
$L_{\mathcal R}\ge1$; $g_r^{PE}=0$ to machine precision (WHERE IT FAILS 7(ii) — the threshold map
is locally constant, so the direct margin is null and general equilibrium is not the reason);
$g_r^{PE}>0$ but dominated by $\mathcal B_r^{GE}$ (the genuine GE failure); or $g_r^{PE}<0$
(fixed-policy amplification at that node, under H8). *Predicted:* the three attributions are
mutually exclusive and their counts sum to the uncertified total.

*Block 5 — AGE's constancy clause, tested rather than assumed.* On each $(\tau,T)$ slice report
the sign of $d\Delta^{\mathrm{act}}/d\kappa$ at every $\kappa$ and the number of sign changes.
*Predicted sign:* at least one slice shows a change, because the committed smoke run has $M_P$
hump-shaped in $\kappa$ near $\kappa\approx0.55$. A slice with a change may not be taken whole as
$\mathcal R_r$ (WHERE IT FAILS 2). Also report the count of nodes where the fixed-policy and
equilibrium signs disagree, which is H8's diagnostic.

*Block 6 — A8 and A5 hygiene.* Report $\Omega$ at every node, flagging nodes with flagged-cell
mass below $0.01$ (A8 failing), the count of multiple-root pricing nodes (A5 failing), the count
of nodes with $k_1\ge k_2$ (H3's interiority failing), and the worst equilibrium solve residual.
*Predicted:* $\Omega$ collapses at $T=H$, because $T=H$ forces $c=0$ on every flagged history
(card §4.3's $P_{-1}^P$ row, turn-2 audit D1-R3), and $H=10$ in this calibration makes $T=10$
that corner. Such nodes are recorded as degenerate rather than dropped.

*Block 7 — the finite-scale secant, as a NUMERICAL side-record.* The five frozen $\tau$
percentiles are a finite tightening ladder, so across each adjacent pair report the secant
analogues of the fixed-policy and equilibrium margins, oriented by the equilibrium sign, and
whether they agree in orientation. *This is not the certificate*, which is a derivative
statement; it is the finite-difference reading of the same question, available at no extra cost,
and it is labelled NUMERICAL wherever it is quoted.

*Block 8 — the window margin, discretely.* Report $\mathcal S$ in equilibrium at $T=5$ against
$T=10$ at each $(\kappa,\tau)$, with $\Omega$ at both. *Predicted sign:* none. No $r_T$
certificate is computed (WHERE IT FAILS 6) and this block is a record.

*Block 9 — the price of the inversion-free step, as a RECORD.* Alongside $\mathcal B_r^{GE}$
report the same three groups of Step 6 with the **exactly solved** norms
$\lVert\partial_rk\rVert$, $\lVert\partial_\kappa k\rVert$, $\lVert\partial^2_{\kappa r}k\rVert$
in place of $\bar k_r$, $\bar k_\kappa$, $\bar k_{\kappa r}$, and the count of nodes that would
certify under it. **That object is not card §4.5's $\mathcal B_r^{GE}$ and certifies nothing** —
it needs $(I-D_k\mathcal T)^{-1}$, which is exactly what the card's rows avoid. Its only purpose
is to separate two very different reasons a node can fail: the GE channel is genuinely large, or
the Neumann step threw away too much. *Predicted magnitude:* the ratio
$\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$ strictly above one at every node, and the
realised remainder well below both. A large gap is a **card-owner finding** (NOT CLAIMED 5), not
a result of this file.

### OUTCOME OF THE RUN (executed 2026-08-21, 10 339 s wall, exit code 0)

Recorded here because the request and its answer belong together; the card §8 rule 6 headings are
unchanged. Every number below is in the JSON, and none of it moves the ledger (NOT CLAIMED 11).

**The region is NOT empty.** 80 nodes, 0 errors, **18 certified** ($L_{\mathcal R}<1$ and
$\eta_r>0$), all at $T=5$ and at the 50th, 70th and 90th $\tau$ percentiles. Slack on the
certified nodes: $\eta_r$ minimum $0.0595$, median $0.3467$, maximum $1.7227$.

**Live margin against null margin — every ratio in this section is reported on the live subset.**
Of the 80 nodes, **24 carry a live threshold margin** ($\lvert g_r^{PE}\rvert$ above rounding
scale) and **56 do not**: at those 56 the flagged set does not move with $\tau$, so $g_r^{PE}$
and $\mathcal B_r^{GE}$ are both at $10^{-13}$ and every ratio built from them is a ratio of
rounding noise (WHERE IT FAILS 7(ii)). Pooling the two populations moves every aggregate
magnitude below, and not in one direction, so each is given three ways:

| Statistic | Pooled (80 nodes) | **Live margin (24)** | Null margin (48 with $\mathcal B_r^{GE}>0$) |
|---|---|---|---|
| realised remainder $/\ \mathcal B_r^{GE}$, median | 0.219 | **0.094** | 0.314 |
| realised remainder $/\ \mathcal B_r^{GE}$, maximum | 1.00 | **0.306** | 1.00 |
| $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$, median | 2.09 | **2.41** | 1.92 |
| $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$, maximum | 10.3 | **8.29** | 10.3 |

On the nodes that carry content the bound is *tighter* than the pooled figure suggests ($0.094$,
not $0.22$) and the Neumann step is *costlier* ($2.41$, not $2.09$). All 18 certified nodes are
live-margin nodes.

**One contiguous, sign-homogeneous block.** AGE's constancy clause is what carves the certified
nodes into candidate regions, and it bites: **all ten** $(\tau,T)$ slices show exactly one sign
change of the equilibrium liquidity derivative, between $\kappa=0.45$ and $\kappa=0.55$ — the
smoke run's $M_P$ hump, as WHERE IT FAILS 2 predicted. Splitting there, the largest set of nodes
that is contiguous in $\kappa$, certified throughout, and carries one sign is
$$
T=5,\qquad \tau\in\{\text{50th},\text{70th},\text{90th percentile}\},\qquad
\kappa\in\{0.65,0.75,0.85\},
$$
nine nodes, every one certified, the equilibrium liquidity derivative negative throughout,
$\eta_r$ minimum $0.2282$, median $0.3739$. On the low-$\kappa$ side ($\kappa\le0.45$, sign
positive) 9 of 12 nodes certify but not contiguously. **Nine certified nodes are still nine
nodes and not a region** — Step 11 stands, and promoting them needs the modulus of continuity the
script does not estimate.

**Checks.** All four PASS/FAIL verdicts pass, no FAILs, eight RECORDs.
$\lvert\partial^2_{r\kappa}\Delta^*-\Delta_{\kappa r}\rvert\le\mathcal B_r^{GE}$ holds at every
node under both readings, and the two readings differ in how much they are worth:

- *Implicit-function reading, all 80 nodes.* No violation. Maximum ratio $1.00$ pooled and
  **$0.306$ on the live-margin subset**. The ratio reaches $1.00$ only at
  $(T{=}10,\text{q}50,\kappa{=}0.35)$ and $(T{=}10,\text{q}50,\kappa{=}0.45)$, where bound and
  remainder are both at rounding scale ($\mathcal B_r^{GE}=1.6$ and $2.6\times10^{-13}$) —
  tightness in a trivial sense only. The containment test carries an **absolute** slack of
  $10^{-6}$, which at the 56 null-margin nodes exceeds both quantities on its own, so the check's
  headline "80 nodes checked, 0 violations" has an effective coverage of **24**. (Containment
  does hold at all 80 with the slack removed — maximum ratio $1.00$ — so nothing is being
  concealed; the count is simply broader than the evidence behind it.)
- *Four-corner re-solve — the only route that shares no arithmetic with the bound.* It runs at 8
  validation nodes, **four of which are null-margin**, and it touches **2 of the 18 certified
  nodes**, $(T{=}5,\text{q}50,\kappa{=}0.25)$ and $(T{=}5,\text{q}50,\kappa{=}0.85)$. On the four
  live-margin validation nodes the realised remainder is at most **$0.310$** of the bound. The
  pooled maximum $0.511$ comes from $(T{=}10,\text{q}10,\kappa{=}0.55)$, where
  $\mathcal B_r^{GE}=7.6\times10^{-13}$ against a remainder of $3.9\times10^{-13}$ — noise over
  noise, and not a statement about tightness. The independent cross-validation of this
  certificate is therefore narrower than "eight validation nodes" sounds.
- *The two independent readings of the equilibrium derivatives, and the run's strongest evidence.*
  On the **first** derivative they agree to $1.8\times10^{-3}$ relative, inside the
  $5\times10^{-3}$ gate; this is the executed test of Step 3's linear system. On the **cross**
  derivative the check records a pooled `max_rel_diff_cross` of $0.535$, which is a null-margin
  artefact: node by node the large disagreements are $0.78$, $1.23$ and $1.00$ at three
  null-margin nodes (a fourth is $0/0$), while **on every live-margin validation node the two
  readings of the equilibrium cross-derivative agree to better than $0.4\,\%$** — $3.8\times
  10^{-3}$, $2.8\times10^{-3}$, $1.6\times10^{-3}$ and $2.2\times10^{-4}$. Two routes that share
  no arithmetic — a four-corner equilibrium re-solve and the implicit-function assembly of
  Steps 3–5 — land within four parts in a thousand of each other wherever the margin is live.
  That is what licenses reading the equilibrium cross-derivative off the free implicit-function
  formula at the 72 unvalidated nodes, and it is the single strongest thing the run establishes.

$L_{\mathcal R}\in[0.264,0.501]$ at every node, none at or above one. Fixed-policy and
equilibrium liquidity-derivative signs agree at every one of the 80 nodes, so H8 holds throughout
and $g_r^{PE}$ deserves its name here.

**Why the other 62 nodes do not certify — three attributions, mutually exclusive.**

- **56 nodes: $g_r^{PE}=0$ to machine precision.** WHERE IT FAILS 7(ii), confirmed. These are the
  10th and 30th $\tau$ percentiles at $T=5$ and **all** of $T=10$: the flagged set does not move
  with $\tau$ there, so $\Omega$, $\Delta^{\mathrm{act}}$, and $\mathcal T$ are all locally
  constant in $\tau$, and $\mathcal B_r^{GE}$ collapses with $g_r^{PE}$ (both at $10^{-13}$).
  Nothing about general equilibrium is being reported at those nodes; the threshold margin has no
  local content there.
- **4 nodes: $g_r^{PE}>0$ but dominated** — the genuine GE failure (WHERE IT FAILS 5), at
  $(T{=}5,\text{q}50,\kappa{=}0.35)$, $(T{=}5,\text{q}50,\kappa{=}0.55)$,
  $(T{=}5,\text{q}70,\kappa{=}0.35)$ and $(T{=}5,\text{q}90,\kappa{=}0.25)$.
- **2 nodes: $g_r^{PE}<0$** — fixed-policy amplification, both at $\kappa=0.55$, i.e. adjacent to
  the sign change, where the region would be void anyway.

**H4's $\tau$-smoothness was measured at every node, and it did not bite where it would matter.**
WHERE IT FAILS 7(i) is the hazard that the quantised legal clock — the implementation takes
$c=\lceil\cdot\rceil$ — puts a jump of $\Delta^{\mathrm{act}}$ *inside* a $\tau$-stencil, which
would void H4 exactly where the certificate needs it. The obvious adversarial reading of
WHERE IT FAILS 7 is that (i) and (ii) exhaust the possibilities, so that any node with
$g_r^{PE}\neq0$ must be one whose stencil straddles a jump — that is, that the certified nodes
would be precisely the nodes where H4 fails. The script carries a diagnostic that settles this,
$$
\text{(kink ratio)}\;=\;
\frac{\bigl\lvert\partial^2_{\tau\tau}\Delta^{\mathrm{act}}\bigr\rvert\,\varepsilon_\tau}
{\bigl\lvert\partial_\tau\Delta^{\mathrm{act}}\bigr\rvert},
$$
the curvature-to-slope ratio over one stencil half-width, which blows up when a jump sits inside
the stencil. **At all 18 certified nodes it is finite and below $0.68$** — minimum $0.047$,
median $0.317$, maximum $0.673$ — so the second-order term is a fraction of the first over one
stencil width and the certified nodes sit in smooth $\tau$-patches. Nineteen nodes have a ratio
above one, and **every one of them is a null-margin node** (cells $(T{=}5,\text{q}10)$,
$(T{=}5,\text{q}30)$ and all of $T=10$), where $\lvert\partial_\tau\Delta^{\mathrm{act}}\rvert$
is at rounding scale and the ratio is noise in its denominator. This does not *verify* H4, which
no run can (NOT CLAIMED 7); it converts WHERE IT FAILS 7(i) from an unmeasured hazard into a
measured one that did not fire on any node that certifies. It is the only executed evidence in
the run that bears on H4.

**Block 7 — the finite-scale secant, answered.** Across the four adjacent pairs of the five
frozen $\tau$ percentiles at each $(\kappa,T)$ — 64 pairs — the fixed-policy and equilibrium
secant margins, oriented by the equilibrium sign, agree in orientation at **45**. The 19 that
disagree are not live disagreements: in every one of them the fixed-policy secant is at rounding
scale ($\lvert\cdot\rvert\le4.9\times10^{-14}$), so what is being compared is the orientation of
noise. **All 24 pairs whose fixed-policy secant is above rounding scale agree in orientation.**
Block 7 is explicitly not the certificate — the certificate is a derivative statement and this is
the finite-difference reading of the same question — and it is labelled NUMERICAL wherever
quoted; but Part (D)'s finite-scale claim is the place a reader will want this number, so it is
recorded beside it rather than left in the JSON.

**$T=10$ is the corner, and it is degenerate.** All 40 $T=10$ nodes report flagged-cell mass
$\Omega=0.00068$, far below the $0.01$ floor, so A8 fails there: with $H=10$, $T=H$ forces
$c=0$ on every flagged history and only the very top of the Voice region can file in time. The
window certificate was not attempted (WHERE IT FAILS 6), and the $T=5$ against $T=10$ record is
a finite-difference record only — 34 of 40 pairs attenuate, the six that do not sitting at
$\kappa=0.55$.

**A5, A3 and solver hygiene.** Zero multiple-root pricing nodes over all 80 nodes and all 33
stencil points each; zero nodes with $k_1\ge k_2$ (H3's interiority held everywhere it was
looked at); worst equilibrium residual $4.2\times10^{-11}$, inside the $10^{-8}$ gate.

**The inversion-free step is what is binding, and that is a card-owner finding.** Block 9's
companion bound — the same three groups with the exactly solved
$\lVert\partial_rk\rVert,\lVert\partial_\kappa k\rVert,\lVert\partial^2_{\kappa r}k\rVert$ in
place of $\bar k_r,\bar k_\kappa,\bar k_{\kappa r}$ — is, **on the live-margin nodes**, a median
factor $2.41$ smaller than $\mathcal B_r^{GE}$ with a maximum factor $8.29$ (the pooled figures
$2.09$ and $10.3$ mix in 48 rounding-scale nodes), and it certifies **22** nodes against the card
bound's 18. The realised remainder is a median $0.094$ of $\mathcal B_r^{GE}$ on those nodes
($0.22$ pooled). The four extra nodes the sharp companion certifies are **exactly** the four
genuine-GE-failure nodes $(T{=}5,\text{q}50,0.35)$, $(T{=}5,\text{q}50,0.55)$,
$(T{=}5,\text{q}70,0.35)$, $(T{=}5,\text{q}90,0.25)$; the only other uncertified live-margin
nodes are the two with $g_r^{PE}<0$, which no bound of any size could rescue. So at this
calibration **every uncertified live-margin node that any bound could rescue is rescued by
dropping the Neumann step** — it, and not the GE channel, is what binds.
**This does not certify anything** (NOT CLAIMED 5): the sharp companion needs
$(I-D_k\mathcal T)^{-1}$, which is exactly what card §4.5's rows are written to avoid. It is
offered to the card owner as evidence that a second, inversion-using bound would be worth adding
alongside the inversion-free one, not as a result of this file.

---

## NOTATION DELTA

Symbols used here that are not in card §4, each defined at first use above:

| Symbol | Meaning | Status |
|---|---|---|
| $\Delta^*(\kappa,r)=\Delta^{\mathrm{act}}\!\left(k(\kappa,r),\kappa,r\right)$ | the **equilibrium** premium: the card §4.4 object composed with the equilibrium cutoff vector | proof-local (Step 5), introduced because the card's $\Delta^{\mathrm{act}}$ is used at *both* a frozen $k$ and the equilibrium $k$, and every step here turns on the difference. Proposed for card §4.5 if C1 is re-derived |
| $\mathcal S$ used at the equilibrium $k$ | card §4.4 defines $\mathcal S=\lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$; Parts (C)–(D) evaluate it along $k(\kappa,r)$, i.e. $\lvert d\Delta^{\mathrm{act}}/d\kappa\rvert$ | **no new symbol**: the card's letter with an argument stated in words at each use. T1's $\mathcal S$ is the frozen-$k$ reading and Step 9 keeps the two apart |
| $\Psi(k;\vartheta)=k-\mathcal T(k;\vartheta)$ | the implicit-function residual map | proof-local (Step 1) |
| $\partial_\kappa k,\ \partial_rk,\ \partial^2_{\kappa r}k$ | the equilibrium cutoff vector's derivatives | card §4.5 names only their **bounds** $\bar k_x,\bar k_{\kappa r}$; the derivatives themselves are unnamed there. Written in $\partial$ form rather than as new letters |
| $\lVert\cdot\rVert=\lVert\cdot\rVert_\infty$ and the pairings $\lvert\mathcal T_{kk}\rvert=\max_i\sum_{j,l}\lvert\cdot\rvert$, $\lvert\Delta_{kk}\rvert=\sum_{j,l}\lvert\cdot\rvert$, etc. | the norms that make card §4.5's bars into valid multilinear bounds | **card-owner flag.** Card §4.5 writes $\lvert\partial_x\mathcal T\rvert$, $\lvert\Delta_{kk}\rvert$ and the rest without fixing a norm. With $J-1>1$ the numerical value of $\mathcal B_r^{GE}$ depends on the choice; the argument does not. Proposed as a parenthesis in the §4.5 rows |
| $\eta_{\min}$, $M$, $\delta$ | the smallest slack over a node set, a Lipschitz constant for $\eta_r$, and the node spacing | proof-local (Step 11), used only to state what a grid does **not** deliver |
| $\mathcal T_{\kappa r},\ \mathcal T_{\kappa k},\ \mathcal T_{rk},\ \mathcal T_{kk}$ | subscript shorthand for the second partials of the outer map at $(k(\vartheta);\vartheta)$ | proof-local (CLAIM (A), Step 4). Card §4.5 *names* $\bar k_{\kappa r}$ but never displays its formula, so these four shorthands appear nowhere on the card |
| $\Delta_\kappa,\ \Delta_{\kappa r}$ | $\partial_\kappa\Delta^{\mathrm{act}}$ and $\partial_{\kappa r}\Delta^{\mathrm{act}}$ at frozen $k$ | proof-local (Step 5). The card's $\mathcal B_r^{GE}$ row carries $\Delta_{\kappa k},\Delta_{kr},\Delta_{kk},\Delta_k$, but its $g_r^{PE}$ row writes the cross-derivative out as $\partial_{\kappa r}\Delta^{\mathrm{act}}$ and never as $\Delta_{\kappa r}$. Same object, shorter subscript |
| $\lvert\partial_\kappa\mathcal T\rvert,\ \lvert\partial_r\mathcal T\rvert$ (bars, in the CLAIM) | $\lVert\partial_x\mathcal T\rVert_\infty$ — the one pairing the preamble list does not fix, and the CLAIM writes it with bars where Step 3 writes it with a norm | **no new object**: for a vector the two coincide under $\lVert\cdot\rVert_\infty$. Written with bars in the CLAIM to match card §4.5's $\bar k_x$ row verbatim |
| $\mathcal B_r^{GE,\text{sharp}}$ | the same three groups of Step 6 with the exactly solved $\lVert\partial_xk\rVert,\lVert\partial^2_{\kappa r}k\rVert$ in place of $\bar k_x,\bar k_{\kappa r}$ | proof-local (Block 9, NUMERICAL CHECK REQUEST). **Not a card object and it certifies nothing** — it needs $(I-D_k\mathcal T)^{-1}$, which card §4.5's rows are written to avoid |
| $\varepsilon_\kappa,\ \varepsilon_\tau$ | the stencil half-widths in $\kappa$ and $\tau$ | proof-local (Block 2 and the kink-ratio diagnostic). Written $\varepsilon$ and **not** $h$: $h$ is card §4.4's engagement-premium kernel $h=\pi p$ and is not available |
| $r_0,\ r_1$ | the endpoints of the strictness segment in Part (D) | proof-local (CLAIM (D), Step 10), with $r_1>r_0$ (higher $r$ = tighter) |
| $w,\ w_1,\ w_2$ | the unit vector of Step 1 and the arguments of the multilinear bounds | proof-local. Card §4.6 rules $u_1,u_2$ proof-local and forbids a **bare $u$**; $w$ carries no card meaning, where $\Xi$, $\Upsilon$ and $\iota_F$ are already spoken for |
| $\mathcal N$ | a neighbourhood of the equilibrium graph $\{(k(\vartheta),\vartheta):\vartheta\in\mathcal R_r\}$ inside $\operatorname{int}\Theta\times\mathcal R_r$ | proof-local (Step 1), the weakest domain on which Steps 1–4 need $\mathcal T$ smooth |
| (H2a), (H2b) | the along-the-path and over-$\Theta$ readings of $L_{\mathcal R}=\sup_{\mathcal R}\lVert D_k\mathcal T\rVert$ | **card-owner flag 1.** Card §4.5's row and card §5's AGE do not say whether the supremum runs over $k\in\Theta$ as well as over $\vartheta\in\mathcal R$. Steps 1–4 need only (H2a); only Step 12's uniqueness remark needs (H2b) |
| the $k$ at which card §4.5's $\Delta$-derivatives are read | $\partial_{\kappa r}\Delta^{\mathrm{act}}$ inside $g_r^{PE}$, and $\Delta_k,\Delta_{kk},\Delta_{\kappa k},\Delta_{kr}$ inside $\mathcal B_r^{GE}$ | **card-owner flag 2.** Card §4.5 does not say **at which cutoff vector** these are evaluated. Step 8 needs all of them at $k(\vartheta)$ — the equilibrium cutoff vector at the *same* $\vartheta$ — because that is where Step 5's identity puts them; read at any other frozen policy, Step 8's cancellation of the first group against $-g_r^{PE}$ fails and the certificate compares unlike objects. The proof and the companion script are consistent throughout on the $k(\vartheta)$ reading (the script's stencil sits at $x_0=(k_1^*,k_2^*,\kappa,\tau)$); the card should say so |
| the $k$ over which AGE's $C^2$ clause runs | card §5's "on a candidate region $\mathcal R$ the outer map is twice continuously differentiable" | **card-owner flag 3.** The clause does not say over which $k$ — the identical ambiguity flag 1 raises for the norm. Step 1 takes the *weaker* reading, smoothness on $\mathcal N$ only, so no step here depends on the resolution |

The card's $\sigma_\kappa$ is **not** used: card §4.5 rules that the sign is written inline and
that no symbol is available for it, and every occurrence above is written
$\operatorname{sgn}(d\Delta^{\mathrm{act}}/d\kappa)$ in full. No card symbol is renumbered or
re-keyed: $\kappa$ is noise-trading intensity, bare $\lambda$ and $\psi$ (D7's appropriability
coefficient and pivotality) appear nowhere, upright $T$ is the window and $\mathcal T$ is the
outer map, $h$ is left to card §4.4's engagement-premium kernel $h=\pi p$, no bare $u$ appears
(card §4.6), and $\Omega=\Pr(D=1)$ wherever it is mentioned.

---

## NOT CLAIMED

1. **Region nonemptiness.** Nothing here asserts that any parameter vector satisfies H2–H6
   simultaneously. **An empty region is a reportable outcome, not a failed run**: card §6's
   intended-label row says C1 is then dropped and the paper ships the fixed-policy theorem (T1)
   only. No tolerance is to be weakened to manufacture a nonempty region, and a run that returns
   one after a tolerance change is to be treated as void.
2. **No uniqueness of equilibrium.** Step 1 gives local uniqueness near one branch; Step 12 says
   what global uniqueness would additionally require (H2b) and that it is not measured. Card §3's
   "Uniqueness is **not** claimed" is respected.
3. **Nothing off-region.** No sign, bound or magnitude is claimed at any parameter vector outside
   $\mathcal R_r$. Off-region numbers carry at most the label NUMERICAL (card §7).
4. **A grid of certified nodes is not a certified region** (Step 11). No interpolation between
   certified nodes is claimed, and no supremum over $\mathcal R$ is inferred from finitely many
   evaluations.
5. **$\mathcal B_r^{GE}$ is not claimed tight.** It is a triangle-inequality bound and card §4.5
   calls it "one admissible" bound. $\eta_r\le0$ therefore carries no information about the sign
   of $\partial_r\mathcal S$ (WHERE IT FAILS 5), and a sharper bound — for instance solving
   $(I-D_k\mathcal T)x=\partial_x\mathcal T$ instead of bounding it — could certify strictly more
   nodes. That sharper route is not taken here because the card's rows are the inversion-free
   ones.
6. **No window-margin sign, and no window certificate.** C1 propagates whatever sign the
   fixed-policy theorem delivers; T1 delivers an iff and no unconditional sign at the window
   margin, so C1 delivers none either. The $r_T$ instance is additionally unavailable without an
   interpolation hypothesis (WHERE IT FAILS 6). Card §9's first boundary is respected.
7. **AGE is not verified.** Its differentiability clause is assumed, not tested; its contraction
   clause is *measured* along the equilibrium path only; its constancy clause is reported per
   slice and is expected to fail on some of them.
8. **No claim about $J$, $R$ or $R_d$**, and none that $J$ is $\kappa$-invariant (card §9).
   Neither appears in any step.
9. **No claim that the model's plan menu satisfies A7′** (card §4.2), on which L2 — and hence
   T1's factorisation, and hence the meaning of "attenuation" here — depends. C1 inherits that
   openness in full.
10. **No welfare, no optimal rule, no empirical value for $\omega_a$**, and no claim about where
    $\Omega$ sits in the data. Card §9's boundaries are respected.
11. **No label move.** C1 stays CONJECTURE and the card's ledger is not edited by this file.

---

## Repairs applied (2026-08-21, C1 audit)

Source: `research/model_v4/threads/2026-08-21_C1_proofread_audit.md` (adversarial proof-read,
verdict PASS, FAIL 0 · REPAIR 13). **No step, hypothesis, bound or conclusion changed** — every
repair is at the reporting or citation level, and every number below was recomputed from
`quality_reports/fixes/t2_c1_region_check.json` before it was written in.

| ID | Change |
|---|---|
| **C1-R1** | OUTCOME: added the live-margin (24) against null-margin (56) split with a three-way table, and reported every ratio on the live subset — realised remainder / $\mathcal B_r^{GE}$ median **0.094** (0.22 pooled), $\mathcal B_r^{GE}/\mathcal B_r^{GE,\text{sharp}}$ median **2.41** (2.09 pooled). Recorded that the containment test's $10^{-6}$ **absolute** slack gives its "80 nodes" headline an effective coverage of 24 |
| **C1-R2** | Corrected "at most $0.51$ of the bound": that maximum is the dead node $(T{=}10,\text{q}10,0.55)$ ($\mathcal B_r^{GE}=7.6\times10^{-13}$); the live-node figure is **0.310**. Stated that the independent four-corner route touches **2 of the 18** certified nodes. Added the omitted strongest evidence: the two independent readings of the equilibrium **cross**-derivative agree to better than **0.4 %** at every live-margin validation node (the pooled `max_rel_diff_cross` 0.535 is a null-margin artefact) |
| **C1-R3** | OUTCOME: surfaced the script's `tau_kink_ratio` diagnostic — the only executed evidence bearing on H4. Finite and $\le0.673$ at all 18 certified nodes (min 0.047, median 0.317); all 19 ratios above one are null-margin nodes. Converts WHERE IT FAILS 7(i) from an unmeasured hazard into a measured one that did not fire |
| **C1-R4** | Answered Block 7, which the request made and the OUTCOME never returned: 64 pairs, 45 same orientation; all 19 disagreements have a fixed-policy secant at rounding scale ($\le4.9\times10^{-14}$), and all 24 pairs with a live fixed-policy secant agree |
| **C1-R5** | NOTATION DELTA: added card-owner flag 2 — card §4.5 does not say **at which $k$** its $\Delta$-derivatives are evaluated, and Step 8 needs them at $k(\vartheta)$ |
| **C1-R6** | LABEL CLAIMED: replaced the stale reason 3. T1 is **PROVED at fixed policies** on the current card and A7′ satisfiability is resolved; what C1 inherits is conditionality (A($\tau$) OPEN for the two-round pooled cell, A(br)(br-v) assumed, A7′'s equilibrium selection OPEN), not a label. Stated that reasons 1–2 each carry CONJECTURE on their own |
| **C1-R7** | H4: A2 → **A2′**, with its replaced clause (local boundedness plus $\mathbb E[\max_j\lvert U_j\rvert]<\infty$) named; the point that boundedness is not differentiability strengthens |
| **C1-R8** | Card §4.6 ruling honoured: the bare $u,v,A$ of the norm preamble and Step 1 are now $w,w_1,w_2$, with the multilinear bound written on the actual objects instead of a generic form |
| **C1-R9** | NOTATION DELTA: added the ten missing symbols — $\mathcal T_{\kappa r},\mathcal T_{\kappa k},\mathcal T_{rk},\mathcal T_{kk}$; $\Delta_\kappa,\Delta_{\kappa r}$; the CLAIM's $\lvert\partial_x\mathcal T\rvert$ bars; $\mathcal B_r^{GE,\text{sharp}}$; the stencil half-widths (renamed $h_\kappa,h_\tau\to\varepsilon_\kappa,\varepsilon_\tau$, since $h$ is card §4.4's kernel $h=\pi p$); $r_0,r_1$ — plus $w,w_1,w_2$ and $\mathcal N$ |
| **C1-R10** | Step 1: $\Psi$'s domain restricted from $\operatorname{int}\Theta\times\mathcal R_r$ to a neighbourhood $\mathcal N$ of the equilibrium graph — the domain H4 already chooses — and the unflagged strengthening turned into card-owner flag 3 (AGE does not say over which $k$ its $C^2$ clause runs) |
| **C1-R11** | Step 10: continuity of $\eta_r$ argued rather than asserted, from H4's $C^2$ clause, Step 7's constant sign and the region-constant $1-L_{\mathcal R}$; the measurability route noted as the cheaper alternative |
| **C1-R12** | Block 9: "what **most** uncertified $T=5$ nodes with a live margin fail on" → **"every uncertified live-margin node that any bound could rescue"** — the sharp companion's four extra nodes are exactly the four genuine-GE-failure nodes, and the other two live failures have $g_r^{PE}<0$ |
| **C1-R13** | H2b: "not used by any step below" → "no step in the proof of (A)–(D) uses it; Step 12 discusses what it would add", which is what the H2 bracket `[Steps 1–4, 7, 12]` already implied |
| **C1-O2** | (observation, applied where the audit directed it) LABEL CLAIMED object 3 now cites `quality_reports/fixes/d8_ge_dominance_check.py`'s $\varepsilon$-ball plus integral-control construction as the live in-repo template for a future node-to-region promotion, with Part (D) as its (R2) analogue |

**Also recut, per the auditor's three-object split (orchestrator adjudication, binding):**
LABEL CLAIMED now separates (1) the certificate implication — PROVED-eligible pending the
re-derivation, with $\mathcal R_r$ a named hypothesis and card §6's C1 row required to absorb
H2–H8 first; (2) the 18 certified nodes — NUMERICAL via the executed committed check; (3) "PROVED
on a named nonempty region" — declared **not obtainable from any run of this script**, since it
needs a modulus of continuity for $\eta_r$ and a genuine supremum for $L_{\mathcal R}$, neither of
which more grid nodes can supply.

**Not applied.** C1-O1 (the stamp-hash gap: git was out of scope for the audit and is out of scope
here), C1-O3 (H3's $k_1<k_2$ test is weaker than interiority — the OUTCOME's existing hedge
"everywhere it was looked at" already carries it, and the point is now also stated in LABEL
CLAIMED), C1-O4 (three cross-file attributions to `proofs/T1_proof.md`, left for the
re-derivation to confirm against T1 directly), C1-O6 and C1-O5 (card-owner items, recorded in
LABEL CLAIMED object 1 but not actionable in this file), C1-O7 (the $M_P$-hump attribution wants
one hedging word; an observation, not a repair, and left for the writer).

---

## 5. RAW CHECK OUTPUT

Trimming rule: every top-level scalar, verdict, headline field, counts block, provenance block, and every check's name/kind/pass/detail fields are included VERBATIM. Any array of per-node or per-row records longer than 30 entries is elided to its first 3 and last 1 entries, with an explicit marker giving the elided count and the SHA-256 of the complete committed file. Nothing else is trimmed — arrays of bare grid/scalar values (e.g. kappa grids, profile series) are not "records" and are left intact regardless of length.

### FILE: quality_reports/fixes/t1_o1_rerun_check.json

```json
{
  "checks": [
    {
      "name": "baseline_cutoffs_and_masses",
      "pass": true,
      "k1": 0.8217375898536412,
      "k0": 0.8217375898536412,
      "kD": 2.2611270959836602,
      "omega_E": 0.40048145287993825,
      "omega_H": 0,
      "omega_Q": 0.5622663205825575,
      "Omega": 0.03725222653750415,
      "committed": {
        "k1": 0.8217375899,
        "k0": 0.8217375899,
        "kD": 2.261127096,
        "omega_E": 0.40048,
        "omega_H": 0.0,
        "omega_Q": 0.56227,
        "Omega": 0.03725
      },
      "note": "Omega = Pr(D=1) = draft_v2's omega_P; Hold region collapses (k1=k0)"
    },
    {
      "name": "o1_ratios_match_committed_claim",
      "pass": true,
      "grid": {
        "kappa_min": 0.15,
        "kappa_max": 0.85,
        "n": 41
      },
      "max_abs_diff": 3.096880115194267e-05,
      "tol": 0.005,
      "rows": [
        {
          "kD": 2.2611270959836602,
          "Omega": 0.03725222653750415,
          "TV_disc": 0.017594385063427954,
          "TV_nodisc": 0.016536509954342415,
          "ratio_TV": 1.0639720903628607,
          "ratio_meanslope": 1.0639720903628607,
          "attenuation_holds": false,
          "committed_ratio_TV": 1.064,
          "abs_diff_vs_committed": 2.790963713938943e-05
        },
        {
          "kD": 1.8,
          "Omega": 0.1289495176461697,
          "TV_disc": 0.015980887992609074,
          "TV_nodisc": 0.013500439216179373,
          "ratio_TV": 1.183730968801152,
          "ratio_meanslope": 1.183730968801152,
          "attenuation_holds": false,
          "committed_ratio_TV": 1.1837,
          "abs_diff_vs_committed": 3.096880115194267e-05
        },
        {
          "kD": 1.4,
          "Omega": 0.2858038224766658,
          "TV_disc": 0.012110436085768651,
          "TV_nodisc": 0.010657668098057915,
          "ratio_TV": 1.136311993800545,
          "ratio_meanslope": 1.136311993800545,
          "attenuation_holds": false,
          "committed_ratio_TV": 1.1363,
          "abs_diff_vs_committed": 1.1993800544951583e-05
        },
        {
          "kD": 1.0,
          "Omega": 0.5,
          "TV_disc": 0.003987574444282053,
          "TV_nodisc": 0.010549741489497257,
          "ratio_TV": 0.37797840338096084,
          "ratio_meanslope": 0.3779784033809608,
          "attenuation_holds": true,
          "committed_ratio_TV": 0.378,
          "abs_diff_vs_committed": 2.1596619039165876e-05
        }
      ]
    },
    {
      "name": "o1_substance_attenuation_fails_below_Omega_029",
      "pass": true,
      "ratios": [
        1.0639720903628607,
        1.183730968801152,
        1.136311993800545,
        0.37797840338096084
      ],
      "Omega": [
        0.03725222653750415,
        0.1289495176461697,
        0.2858038224766658,
        0.5
      ],
      "reading": "kappa-sensitivity is NOT lower under disclosure for Omega <~ 0.29; attenuation appears only at Omega = 0.50, far off calibration"
    },
    {
      "name": "o1_pointwise_slopes_above_kappa_07",
      "pass": true,
      "claim": "disclosure is steeper at kappa >= 0.7 for Omega <= 0.29",
      "per_kD": [
        {
          "kD": 2.2611270959836602,
          "Omega": 0.03725222653750415,
          "disc_steeper_everywhere_above_kappa_0.7": true,
          "mean_slope_disc_hi": 0.03570715249328534,
          "mean_slope_nodisc_hi": 0.030045235611829573
        },
        {
          "kD": 1.8,
          "Omega": 0.1289495176461697,
          "disc_steeper_everywhere_above_kappa_0.7": true,
          "mean_slope_disc_hi": 0.03254988707754091,
          "mean_slope_nodisc_hi": 0.018190115938894885
        },
        {
          "kD": 1.4,
          "Omega": 0.2858038224766658,
          "disc_steeper_everywhere_above_kappa_0.7": true,
          "mean_slope_disc_hi": 0.024563054293221878,
          "mean_slope_nodisc_hi": 0.0045360465063508
        },
        {
          "kD": 1.0,
          "Omega": 0.5,
          "disc_steeper_everywhere_above_kappa_0.7": false,
          "mean_slope_disc_hi": 0.007777278037312368,
          "mean_slope_nodisc_hi": 0.011424010752862142
        }
      ]
    },
    {
      "name": "o1b_figure_magnitude_at_baseline",
      "pass": true,
      "claim": "at baseline the two plotted curves' ranges over kappa in [0.15,0.85] are 0.01107 (disc) vs 0.01117 (no-disc), a <1% difference; by mean |slope| the disclosed regime is slightly MORE sensitive (0.0251 vs 0.0236)",
      "n_grid": 35,
      "range_disc": 0.011069979939183027,
      "range_nodisc": 0.011170435095143268,
      "relative_range_gap": 0.008992949254404324,
      "max_pointwise_relative_gap": 0.024763235335036004,
      "meanslope_disc": 0.025123586000346504,
      "meanslope_nodisc": 0.023624544851086556,
      "TV_ratio_35pt": 1.063452699669302
    },
    {
      "name": "o1_sign_flip_located",
      "pass": true,
      "bracket": [
        1.0,
        1.4
      ],
      "ratio_minus_1_at_bracket": [
        -0.6220215966190392,
        0.13631199380054504
      ],
      "kD_star": 1.28618407726065,
      "Omega_star": 0.342839683502031,
      "reading": "window-margin attenuation FAILS (disclosure more kappa-sensitive) for Omega < 0.3428, and HOLDS above it; the committed claim's '~0.29' is the largest grid point at which failure was confirmed, not the crossing",
      "committed_cut_is_a_grid_point_not_the_crossing": true
    }
  ],
  "n_fail": 0,
  "experiment": {
    "name": "O-1 window margin (public buy flagged vs pooled) at fixed cutoffs",
    "model": "current repo model, numerical/ package (draft_v2 static model)",
    "regimes": {
      "disclosure (tau_w = 1)": "market observes (X, D); model.compute_minority_gains",
      "no disclosure (tau_w = 0)": "market observes X only; model.compute_minority_gains_no_disclosure_given_strategy"
    },
    "object": "Delta^act = expected activism-related minority takeover gain",
    "sensitivity_measure": "total variation of Delta^act over the kappa grid; mean |slope| is the same number divided by (n-1)*step, so ratios coincide exactly on a uniform grid",
    "held_fixed": "blockholder cutoffs (k1, k0) at the baseline equilibrium",
    "varied": "kD, which moves Omega = Pr(D=1) = draft_v2's omega_P",
    "notation": "kappa = noise-trading intensity; Omega = unconditional flagged weight (MODEL_CARD sec. 4.4); omega_a (disclosed share of engagements) is NOT what this table varies",
    "date": "2026-08-21"
  },
  "grid": {
    "kappa_min": 0.15,
    "kappa_max": 0.85,
    "n_kappa": 41,
    "kD_values": [
      2.2611270959836602,
      1.8,
      1.4,
      1.0
    ],
    "Omega_values": [
      0.03725222653750415,
      0.1289495176461697,
      0.2858038224766658,
      0.5
    ]
  },
  "numbers": [
    {
      "kD": 2.2611270959836602,
      "Omega": 0.03725222653750415,
      "TV_disc": 0.017594385063427954,
      "TV_nodisc": 0.016536509954342415,
      "ratio_TV": 1.0639720903628607,
      "ratio_meanslope": 1.0639720903628607,
      "attenuation_holds": false,
      "committed_ratio_TV": 1.064,
      "abs_diff_vs_committed": 2.790963713938943e-05
    },
    {
      "kD": 1.8,
      "Omega": 0.1289495176461697,
      "TV_disc": 0.015980887992609074,
      "TV_nodisc": 0.013500439216179373,
      "ratio_TV": 1.183730968801152,
      "ratio_meanslope": 1.183730968801152,
      "attenuation_holds": false,
      "committed_ratio_TV": 1.1837,
      "abs_diff_vs_committed": 3.096880115194267e-05
    },
    {
      "kD": 1.4,
      "Omega": 0.2858038224766658,
      "TV_disc": 0.012110436085768651,
      "TV_nodisc": 0.010657668098057915,
      "ratio_TV": 1.136311993800545,
      "ratio_meanslope": 1.136311993800545,
      "attenuation_holds": false,
      "committed_ratio_TV": 1.1363,
      "abs_diff_vs_committed": 1.1993800544951583e-05
    },
    {
      "kD": 1.0,
      "Omega": 0.5,
      "TV_disc": 0.003987574444282053,
      "TV_nodisc": 0.010549741489497257,
      "ratio_TV": 0.37797840338096084,
      "ratio_meanslope": 0.3779784033809608,
      "attenuation_holds": true,
      "committed_ratio_TV": 0.378,
      "abs_diff_vs_committed": 2.1596619039165876e-05
    }
  ],
  "committed_claim": {
    "source": "quality_reports/reports/2026-08-19_framework_v3_referee_report.md:114-124 (claim); research/review_v3/verify_theory.md:32,42-53 (independent re-execution, 41-point grid)",
    "baseline_cutoffs": {
      "k1": 0.8217375899,
      "k0": 0.8217375899,
      "kD": 2.261127096
    },
    "baseline_masses": {
      "omega_E": 0.40048,
      "omega_H": 0.0,
      "omega_Q": 0.56227,
      "Omega": 0.03725
    },
    "rows": [
      {
        "kD": 2.261,
        "Omega": 0.0373,
        "TV_disc": 0.017594,
        "TV_nodisc": 0.016537,
        "ratio_TV": 1.064
      },
      {
        "kD": 1.8,
        "Omega": 0.1289,
        "TV_disc": 0.015981,
        "TV_nodisc": 0.0135,
        "ratio_TV": 1.1837
      },
      {
        "kD": 1.4,
        "Omega": 0.2858,
        "TV_disc": 0.01211,
        "TV_nodisc": 0.010658,
        "ratio_TV": 1.1363
      },
      {
        "kD": 1.0,
        "Omega": 0.5,
        "TV_disc": 0.003988,
        "TV_nodisc": 0.01055,
        "ratio_TV": 0.378
      }
    ],
    "verdict_text": "kappa-sensitivity is NOT lower under disclosure for Omega <~ 0.29; attenuation appears only at Omega = 0.50, far off calibration",
    "pointwise": "disclosure is steeper at kappa >= 0.7 for Omega <= 0.29",
    "figure_magnitude": "at baseline the two plotted curves' ranges over kappa in [0.15,0.85] are 0.01107 (disc) vs 0.01117 (no-disc), a <1% difference; by mean |slope| the disclosed regime is slightly MORE sensitive (0.0251 vs 0.0236)"
  },
  "comparison": {
    "reproduced": true,
    "tolerance": 0.005,
    "max_abs_ratio_diff": 3.096880115194267e-05,
    "explained_differences": [],
    "note": "Committed ratios are quoted to 4 dp in verify_theory.md and 2 dp in the referee report; the kD values 1.80/1.40/1.00 are the referee's own grid, and Omega is a deterministic function of kD at fixed (k1,k0), so Omega reproduces exactly."
  },
  "pointwise": {
    "claim": "disclosure is steeper at kappa >= 0.7 for Omega <= 0.29",
    "per_kD": [
      {
        "kD": 2.2611270959836602,
        "Omega": 0.03725222653750415,
        "disc_steeper_everywhere_above_kappa_0.7": true,
        "mean_slope_disc_hi": 0.03570715249328534,
        "mean_slope_nodisc_hi": 0.030045235611829573
      },
      {
        "kD": 1.8,
        "Omega": 0.1289495176461697,
        "disc_steeper_everywhere_above_kappa_0.7": true,
        "mean_slope_disc_hi": 0.03254988707754091,
        "mean_slope_nodisc_hi": 0.018190115938894885
      },
      {
        "kD": 1.4,
        "Omega": 0.2858038224766658,
        "disc_steeper_everywhere_above_kappa_0.7": true,
        "mean_slope_disc_hi": 0.024563054293221878,
        "mean_slope_nodisc_hi": 0.0045360465063508
      },
      {
        "kD": 1.0,
        "Omega": 0.5,
        "disc_steeper_everywhere_above_kappa_0.7": false,
        "mean_slope_disc_hi": 0.007777278037312368,
        "mean_slope_nodisc_hi": 0.011424010752862142
      }
    ]
  },
  "figure_magnitude": {
    "claim": "at baseline the two plotted curves' ranges over kappa in [0.15,0.85] are 0.01107 (disc) vs 0.01117 (no-disc), a <1% difference; by mean |slope| the disclosed regime is slightly MORE sensitive (0.0251 vs 0.0236)",
    "n_grid": 35,
    "range_disc": 0.011069979939183027,
    "range_nodisc": 0.011170435095143268,
    "relative_range_gap": 0.008992949254404324,
    "max_pointwise_relative_gap": 0.024763235335036004,
    "meanslope_disc": 0.025123586000346504,
    "meanslope_nodisc": 0.023624544851086556,
    "TV_ratio_35pt": 1.063452699669302
  },
  "crossing": {
    "bracket": [
      1.0,
      1.4
    ],
    "ratio_minus_1_at_bracket": [
      -0.6220215966190392,
      0.13631199380054504
    ],
    "kD_star": 1.28618407726065,
    "Omega_star": 0.342839683502031,
    "reading": "window-margin attenuation FAILS (disclosure more kappa-sensitive) for Omega < 0.3428, and HOLDS above it; the committed claim's '~0.29' is the largest grid point at which failure was confirmed, not the crossing",
    "committed_cut_is_a_grid_point_not_the_crossing": true
  },
  "sign": {
    "d_sensitivity_d_flag": "POSITIVE at baseline",
    "plain": "Flagging the public buy RAISES the liquidity-sensitivity of the expected activism premium at the paper's calibration; window-margin attenuation is FALSE at baseline in the repo model.",
    "magnitude": "TV ratio 1.06 at Omega=0.037 (baseline), 1.18 at 0.129, 1.14 at 0.286; sign flips to 0.38 only at Omega=0.50",
    "condition": "holds for Omega <~ 0.29 at fixed cutoffs (partial equilibrium)"
  },
  "all_pass": true,
  "verdict": "REPRODUCED \u2014 committed O-1 claim confirmed in the current repo model: window-margin attenuation is FALSE at baseline (TV ratio > 1 for Omega <~ 0.29), attenuation appearing only at Omega = 0.50."
}
```

### FILE: quality_reports/fixes/t2_c1_region_check.json

```json
{
  "provenance": {
    "script": "quality_reports/fixes/t2_c1_region_check.py",
    "proof": "research/model_v4/proofs/C1_proof.md",
    "card": "research/model_v4/MODEL_CARD.md, stamp 2026-08-21 / a175202+",
    "card_section": "4.5 (L_R, r_tau, g_r^PE, kbar_x, kbar_kr, B_r^GE, eta_r)",
    "model": "numerical_v4 (H=10, J=3 plans, M=2 marks)",
    "params_hash": "b4482d7fee83a8e8",
    "seed_equilibrium_k": [
      1.3124648122403926,
      1.4188874333035122
    ],
    "seed_outer_residual": 1.3427259304421568e-11,
    "tau_quantiles_pct": [
      10,
      30,
      50,
      70,
      90
    ],
    "tau_frozen": [
      0.08462696676439771,
      0.08788437014471917,
      0.09076405861553302,
      0.09337594348697996,
      0.09602833824479486
    ],
    "tau_freezing": "percentiles of the seed equilibrium's Voice b*(s); smoke.py's convention, median = 0.09076406",
    "kappa_grid": [
      0.15,
      0.25,
      0.35,
      0.45,
      0.55,
      0.65,
      0.75,
      0.85
    ],
    "kappa_grid_step": 0.1,
    "T_grid": [
      5,
      10
    ],
    "n_nodes_planned": 80,
    "requested_grid_not_run": {
      "kappa": "[0.15, 0.85] step 0.01 (71 points)",
      "nodes": 710,
      "reason": "measured 42 s per stencil-only node and 300 s per validation node; 710 nodes is >8 h of wall time even with no validation. Not run. The grid reported above is the grid certified."
    },
    "validation_nodes_T_taupct_kappa": [
      [
        5,
        10,
        0.55
      ],
      [
        5,
        50,
        0.25
      ],
      [
        5,
        50,
        0.55
      ],
      [
        5,
        50,
        0.85
      ],
      [
        5,
        90,
        0.55
      ],
      [
        10,
        10,
        0.55
      ],
      [
        10,
        50,
        0.55
      ],
      [
        10,
        90,
        0.55
      ]
    ],
    "validation_meaning": "nodes where the equilibrium is additionally re-solved at kappa +- h and at the four (kappa, tau) corners, giving a reading of d_r d_kappa Delta* that shares no arithmetic with the bound",
    "stencil": {
      "variables": [
        "k1",
        "k2",
        "kappa",
        "tau"
      ],
      "steps": [
        0.01,
        0.01,
        0.01,
        0.0005
      ],
      "points": 33,
      "scheme": "central, second order"
    },
    "strictness_coordinate": "r = r_tau = -tau. r_T = -T is NOT differentiated: T ranges over {1,...,H} in the card and is an int in the code, so d_{r_T} does not exist. T enters as a fixed environment label per node.",
    "quick_mode": false
  },
  "kind": "substantive",
  "checks": [
    {
      "name": "wiring_premium_matches_evaluate",
      "verdict": "PASS",
      "pass": true,
      "shared_pass": 0.0026885064313146695,
      "evaluate": 0.0026885064313146695,
      "abs_diff": 0.0,
      "note": "the 33-point stencil's premium is evaluate()'s, verbatim"
    },
    {
      "name": "contraction_bound_L_R",
      "verdict": "RECORD",
      "pass": null,
      "n_nodes": 80,
      "L_max": 0.5008183519068621,
      "L_min": 0.26358722304692384,
      "n_nodes_with_L_ge_1": 0,
      "nodes_with_L_ge_1": [],
      "reading": "L_R here is ||D_k T|| AT the equilibrium k*(theta), node by node -- the along-the-path reading. AGE's sup over the whole polytope is NOT computed; see C1_proof.md WHERE IT FAILS 1 and NOT CLAIMED."
    },
    {
      "name": "bound_contains_equilibrium_remainder",
      "verdict": "PASS",
      "pass": true,
      "n_checked": 8,
      "n_violations": 0,
      "violations": [],
      "max_ratio_remainder_over_bound": 0.51145897506672,
      "formula": "|d_r d_kappa Delta*(four-corner re-solve) - d_{kappa r} Delta^act(stencil)| <= B_r^GE",
      "scope": "validation nodes only (six equilibrium re-solves each)",
      "note": "this is the certificate's only substantive verdict"
    },
    {
      "name": "bound_contains_ift_remainder",
      "verdict": "PASS",
      "pass": true,
      "n_checked": 80,
      "n_violations": 0,
      "violations": [],
      "max_ratio": 1.0,
      "formula": "|d_r d_kappa Delta*(implicit function) - d_{kappa r} Delta^act| <= B_r^GE, every node",
      "note": "the Neumann bound must dominate the exactly-solved cutoff responses; a violation is a mis-assembly of C1_proof.md Step 6"
    },
    {
      "name": "ift_matches_resolved_equilibrium",
      "verdict": "PASS",
      "pass": true,
      "n_checked": 8,
      "max_rel_diff_first": 0.0017908506838800768,
      "n_checked_cross": 8,
      "max_rel_diff_cross": 0.5351851693758926,
      "tol": 0.005,
      "scope": "validation nodes only",
      "formula": "d Delta*/d kappa = Delta_kappa + Delta_k . (I-D_kT)^-1 d_kappa T",
      "note": "this is what licenses taking the equilibrium sign from the implicit-function reading at the non-validation nodes; the cross-derivative agreement is reported but does not gate, since a four-corner re-solve of a second derivative is the noisier of the two"
    },
    {
      "name": "certified_region",
      "verdict": "RECORD",
      "pass": null,
      "empty_region": false,
      "n_certified": 18,
      "n_nodes": 80,
      "eta_min": 0.05953542544265861,
      "eta_median": 0.34671597204015125,
      "eta_max": 1.7227279502670638,
      "certified_cells_T_taupct": [
        [
          5,
          50
        ],
        [
          5,
          70
        ],
        [
          5,
          90
        ]
      ],
      "certified_kappa_by_cell": {
        "T5_q50": [
          0.15,
          0.25,
          0.45,
          0.65,
          0.75,
          0.85
        ],
        "T5_q70": [
          0.15,
          0.25,
          0.45,
          0.65,
          0.75,
          0.85
        ],
        "T5_q90": [
          0.15,
          0.35,
          0.45,
          0.65,
          0.75,
          0.85
        ]
      },
      "criterion": "L_R < 1 AND eta_r = g_r^PE - B_r^GE > 0",
      "note": "card section 6: an empty region is a reportable outcome; C1 is then dropped and the paper ships T1 only. No tolerance was weakened to make it nonempty."
    },
    {
      "name": "inversion_free_slack",
      "verdict": "RECORD",
      "pass": null,
      "n_certified_card_bound": 18,
      "n_certified_sharp_bound": 22,
      "sharp_cells_T_taupct": [
        [
          5,
          50
        ],
        [
          5,
          70
        ],
        [
          5,
          90
        ]
      ],
      "median_B_over_B_sharp": 2.0855593178477276,
      "max_B_over_B_sharp": 10.298150760660382,
      "median_realised_remainder_over_B": 0.21920640457370627,
      "reading": "B_r_GE_sharp replaces the inversion-free kbar's with the exactly-solved ||d_x k|| and ||d^2_{kappa r} k||. It is NOT card 4.5's object and certifies nothing; it measures the price of the Neumann step. A large gap between the two counts is a card-owner finding (C1_proof.md NOT CLAIMED 5), not a result."
    },
    {
      "name": "failure_attribution",
      "verdict": "RECORD",
      "pass": null,
      "n_L_ge_1": 0,
      "n_g_r_PE_zero_to_1e-10": 56,
      "n_g_positive_but_dominated": 4,
      "n_g_negative": 2,
      "zero_g_cells_T_taupct": [
        [
          5,
          10
        ],
        [
          5,
          30
        ],
        [
          10,
          10
        ],
        [
          10,
          30
        ],
        [
          10,
          50
        ],
        [
          10,
          70
        ],
        [
          10,
          90
        ]
      ],
      "reading": "g_r^PE = 0 exactly means the flagged set does not move with tau at that node: the implemented legal clock quantises the crossing date (c = ceil(.)), so Omega(tau) is locally constant and d_{kappa r} Delta^act vanishes identically there."
    },
    {
      "name": "degenerate_and_multiple_root_nodes",
      "verdict": "RECORD",
      "pass": null,
      "n_degenerate_nodes": 40,
      "degenerate_cells_T_taupct": [
        [
          10,
          10
        ],
        [
          10,
          30
        ],
        [
          10,
          50
        ],
        [
          10,
          70
        ],
        [
          10,
          90
        ]
      ],
      "degenerate_sample": [
        {
          "T": 10,
          "tau_pct": 10,
          "kappa": 0.15,
          "Omega": 0.0006812715261460648,
          "degenerate": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "T": 10,
          "tau_pct": 10,
          "kappa": 0.25,
          "Omega": 0.0006812715261460647,
          "degenerate": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "T": 10,
          "tau_pct": 10,
          "kappa": 0.35,
          "Omega": 0.0006812715261460647,
          "degenerate": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "T": 10,
          "tau_pct": 10,
          "kappa": 0.45,
          "Omega": 0.0006812715261460647,
          "degenerate": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "T": 10,
          "tau_pct": 10,
          "kappa": 0.55,
          "Omega": 0.0006812715261460647,
          "degenerate": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "T": 10,
          "tau_pct": 10,
          "kappa": 0.65,
          "Omega": 0.0006812715261460647,
          "degenerate": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        }
      ],
      "n_nodes_with_multiple_roots": 0,
      "multiple_roots": [],
      "n_k_order_violations": 0,
      "max_solve_residual": 4.162448163924637e-11,
      "n_solve_residual_above_tol": 0,
      "tol_solve": 1e-08
    },
    {
      "name": "age_sign_constancy_on_kappa_slices",
      "verdict": "RECORD",
      "pass": null,
      "n_slices": 10,
      "n_slices_with_a_sign_change": 10,
      "slices": [
        {
          "T": 5,
          "tau_pct": 10,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 5,
          "tau_pct": 30,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 5,
          "tau_pct": 50,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 5,
          "tau_pct": 70,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 5,
          "tau_pct": 90,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 10,
          "tau_pct": 10,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 10,
          "tau_pct": 30,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 10,
          "tau_pct": 50,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 10,
          "tau_pct": 70,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        },
        {
          "T": 10,
          "tau_pct": 90,
          "n_sign_changes": 1,
          "kappas": [
            0.15,
            0.25,
            0.35,
            0.45,
            0.55,
            0.65,
            0.75,
            0.85
          ],
          "signs": [
            1.0,
            1.0,
            1.0,
            1.0,
            -1.0,
            -1.0,
            -1.0,
            -1.0
          ]
        }
      ],
      "n_sign_incoherent_nodes": 0,
      "reading": "AGE requires the sign of the equilibrium liquidity derivative to be constant on R. A slice with a sign change cannot be taken whole as a region; see C1_proof.md WHERE IT FAILS 2."
    },
    {
      "name": "finite_scale_secant_orientation",
      "verdict": "RECORD",
      "pass": null,
      "n_pairs": 64,
      "n_same_orientation": 45,
      "n_fixed_policy_secant_positive": 19,
      "n_equilibrium_secant_positive": 22,
      "pairs": [
        {
          "T": 5,
          "kappa": 0.15,
          "tau_pct_lo": 10,
          "tau_pct_hi": 30,
          "secant_g_fixed_policy": 4.9926369836570964e-15,
          "secant_g_equilibrium": -6.292053969270249e-13,
          "same_orientation": false
        },
        "...ELIDED: 62 of 64 array entries omitted here (kept: first 1, last 1 -- tightened past the base first-3/last-1 rule because the bundle exceeded the ~500KB target after every proof and the card were kept verbatim). Full array is in the committed file quality_reports/fixes/t2_c1_region_check.json, sha256=e016012bc8ae2be3419b4a19f9ea6bf468ca0baf8d98cb8d09a0da4dfacc9845...",
        {
          "T": 10,
          "kappa": 0.85,
          "tau_pct_lo": 70,
          "tau_pct_hi": 90,
          "secant_g_fixed_policy": -2.4198799376311067e-14,
          "secant_g_equilibrium": -6.867226850034222e-13,
          "same_orientation": true
        }
      ],
      "reading": "secant analogue of g_r^PE across adjacent frozen tau percentiles, oriented by the equilibrium sign. This is NUMERICAL evidence at finite scale and is NOT the certificate, which is a derivative statement."
    },
    {
      "name": "window_margin_discrete_record",
      "verdict": "RECORD",
      "pass": null,
      "n_pairs": 40,
      "n_attenuating": 34,
      "pairs": [
        {
          "tau_pct": 10,
          "kappa": 0.15,
          "S_star_T10": 0.010978508474491005,
          "S_star_T5": 0.004072675184308375,
          "ratio_5_over_10": 0.3709679865686123,
          "Omega_T10": 0.0006812715261460648,
          "Omega_T5": 0.14465741548984062
        },
        "...ELIDED: 38 of 40 array entries omitted here (kept: first 1, last 1 -- tightened past the base first-3/last-1 rule because the bundle exceeded the ~500KB target after every proof and the card were kept verbatim). Full array is in the committed file quality_reports/fixes/t2_c1_region_check.json, sha256=e016012bc8ae2be3419b4a19f9ea6bf468ca0baf8d98cb8d09a0da4dfacc9845...",
        {
          "tau_pct": 90,
          "kappa": 0.85,
          "S_star_T10": 0.014711935945512209,
          "S_star_T5": 0.011611681828384766,
          "ratio_5_over_10": 0.7892694660573779,
          "Omega_T10": 0.0006812715261460648,
          "Omega_T5": 0.027679261597019344
        }
      ],
      "reading": "T is an integer primitive; r_T = -T carries no derivative, so no r_T certificate is computed. This row is an EQUILIBRIUM finite-difference record of S* at T=5 against T=10, nothing more."
    }
  ],
  "nodes": [
    {
      "kappa": 0.15,
      "tau": 0.08462696676439771,
      "T": 5,
      "k1": 1.027275215816451,
      "k2": 1.722814202265274,
      "outer_residual": 4.154254718002903e-11,
      "payoff_residual": 0.0,
      "Omega": 0.14465741548984062,
      "omega_a": 0.9433775527625275,
      "pi_bar": 0.010150880252565334,
      "M_F": 0.0057812407924740464,
      "Delta_act": 0.0009492038311797583,
      "degenerate": [],
      "multiple_root_nodes": 0,
      "k_order_ok": true,
      "L_R": 0.4307364316472606,
      "abs_dT_dkappa": 0.9786620766553455,
      "abs_dT_dr": 1.5543122344752192e-12,
      "kbar_kappa": 1.7191721569101464,
      "kbar_r": 2.7303911946673224e-12,
      "kbar_kappa_r": 6.625990658849147e-10,
      "dDelta_dkappa_fixed": 0.00017362142779985142,
      "dDelta_dtau_fixed": 0.0,
      "d2Delta_dkappa_dtau_fixed": 5.421010862427521e-15,
      "abs_Delta_k": 0.004375458046712046,
      "abs_Delta_kappa_k": 0.004410550356140646,
      "abs_Delta_k_r": 1.6263032587282563e-14,
      "abs_Delta_kk": 0.013197299786060507,
      "B_r_GE": 3.00112418565437e-12,
      "tau_kink_ratio": NaN,
      "validation_node": false,
      "dDelta_star_dkappa": NaN,
      "dDelta_star_dkappa_ift": 0.004072675184308375,
      "dDelta_star_dkappa_used": 0.004072675184308375,
      "sign_source": "implicit_function",
      "sign_equilibrium": 1.0,
      "sign_fixed_policy": 1.0,
      "sign_coherent": true,
      "cross_r_equilibrium_numeric": NaN,
      "cross_r_equilibrium_ift": 5.974710193330114e-13,
      "remainder_numeric": NaN,
      "remainder_ift": 6.02892030195439e-13,
      "g_r_PE": 5.421010862427521e-15,
      "eta_r": -2.9957031747919423e-12,
      "certified": false,
      "B_r_GE_sharp": 7.008270403536936e-13,
      "eta_r_sharp": -6.954060294912661e-13,
      "certified_sharp": false,
      "norm_k_kappa": 0.8911189902594315,
      "norm_k_r": 2.730391194667264e-12,
      "norm_k_kappa_r": 1.4676904975381356e-10,
      "worst_solve_residual": 4.154254718002903e-11,
      "dr_S_star_ift": 5.974710193330114e-13,
      "dr_S_star_numeric": NaN,
      "seconds": 106.89094437495805,
      "tau_pct": 10
    },
    "...ELIDED: 78 of 80 array entries omitted here (kept: first 1, last 1 -- tightened past the base first-3/last-1 rule because the bundle exceeded the ~500KB target after every proof and the card were kept verbatim). Full array is in the committed file quality_reports/fixes/t2_c1_region_check.json, sha256=e016012bc8ae2be3419b4a19f9ea6bf468ca0baf8d98cb8d09a0da4dfacc9845...",
    {
      "kappa": 0.85,
      "tau": 0.09602833824479486,
      "T": 10,
      "k1": 1.050545549573866,
      "k2": 1.696911726587691,
      "outer_residual": 3.872635545576486e-11,
      "payoff_residual": 0.0,
      "Omega": 0.0006812715261460648,
      "omega_a": 0.004200993829744704,
      "pi_bar": 0.1615979533291511,
      "M_F": 3.265374196109075e-05,
      "Delta_act": 0.0021448992560277064,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "multiple_root_nodes": 0,
      "k_order_ok": true,
      "L_R": 0.4204125294419714,
      "abs_dT_dkappa": 0.6506165911244199,
      "abs_dT_dr": 0.0,
      "kbar_kappa": 1.1225511664322285,
      "kbar_r": 0.0,
      "kbar_kappa_r": 0.0,
      "dDelta_dkappa_fixed": -0.01050392540083132,
      "dDelta_dtau_fixed": 0.0,
      "d2Delta_dkappa_dtau_fixed": 0.0,
      "abs_Delta_k": 0.004671569446579164,
      "abs_Delta_kappa_k": 0.0033640439375847483,
      "abs_Delta_k_r": 0.0,
      "abs_Delta_kk": 0.015559859184327042,
      "B_r_GE": 0.0,
      "tau_kink_ratio": NaN,
      "validation_node": false,
      "dDelta_star_dkappa": NaN,
      "dDelta_star_dkappa_ift": -0.014711935945512209,
      "dDelta_star_dkappa_used": -0.014711935945512209,
      "sign_source": "implicit_function",
      "sign_equilibrium": -1.0,
      "sign_fixed_policy": -1.0,
      "sign_coherent": true,
      "cross_r_equilibrium_numeric": NaN,
      "cross_r_equilibrium_ift": -0.0,
      "remainder_numeric": NaN,
      "remainder_ift": 0.0,
      "g_r_PE": -0.0,
      "eta_r": -0.0,
      "certified": false,
      "B_r_GE_sharp": 0.0,
      "eta_r_sharp": -0.0,
      "certified_sharp": false,
      "norm_k_kappa": 0.9007701999939819,
      "norm_k_r": 0.0,
      "norm_k_kappa_r": 0.0,
      "worst_solve_residual": 3.872635545576486e-11,
      "dr_S_star_ift": 0.0,
      "dr_S_star_numeric": NaN,
      "seconds": 98.84337800007779,
      "tau_pct": 90
    }
  ],
  "n_fail": 0,
  "n_error_nodes": 0,
  "wall_seconds": 10339.306285416009,
  "all_pass": true,
  "empty_region": false
}
```

### FILE: quality_reports/fixes/t2_d1_check.json

```json
{
  "checks": [
    {
      "name": "d1_clock_equivalence_three_routes",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "err_1 = |1{f_j <= H} - 1{B_j(s,H-T) >= tau}| over Voice types; predicted exactly 0",
      "routes": "A = date-by-date crossing scan (disclosure_by_scan); B = one evaluation at H-T (disclosure_by_h_minus_T); C = legal_clock's closed-form crossing date plus f <= H",
      "max_err1": {
        "AB": 0,
        "AC": 0,
        "BC": 0
      },
      "kappa_free": "err_1 does not involve the noise law; the kappa grid is carried by the enumeration checks below",
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "n_scan_points": 20092,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 8286
        },
        {
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "n_scan_points": 20084,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 8282
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "n_scan_points": 20076,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 8228
        },
        {
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "n_scan_points": 20060,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 7712
        },
        {
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "n_scan_points": 20060,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 6819
        },
        {
          "T": 10,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "n_scan_points": 20092,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 4667
        },
        {
          "T": 10,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "n_scan_points": 20084,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 4671
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "n_scan_points": 20076,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 4671
        },
        {
          "T": 10,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "n_scan_points": 20060,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 4667
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "n_scan_points": 20060,
          "err1_scan_vs_HminusT": 0,
          "err1_scan_vs_legal_clock": 0,
          "err1_HminusT_vs_legal_clock": 0,
          "max_abs_c_scan_minus_c_closed_form": 0.0,
          "n_flagged_scan_points": 4667
        }
      ]
    },
    {
      "name": "d1_crossing_date_two_routes",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "the crossing date c itself, by the same two routes",
      "max_abs_difference": 0.0,
      "predicted": 0.0
    },
    {
      "name": "d1_partition_exclusivity",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "err_3 = |1_{C_F} + 1_{C_P} - 1| and Pr(C_F cap C_P); plus the count of histories with D not in {0,1}",
      "max_err3": 0.0,
      "max_overlap_mass": 0.0,
      "n_histories_with_D_not_binary": 0,
      "membership_routes": "C_F decided by the one-shot H-T rule, C_P by the date-by-date crossing scan, so overlap and gap are cross-route quantities rather than a tautology",
      "why_wiring": "D is a Python if on one atom; the partition holds by construction and this cannot be evidence for D1"
    },
    {
      "name": "d1_partition_exhaustion",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "|Pr(C_F) + Pr(C_P) - 1| below 1e-12",
      "tol": 1e-12,
      "max_atom_level_residual": 0.0,
      "max_history_level_residual": 3.3306690738754696e-16,
      "history_level_meaning": "|sum_h mass_H(h) - (1 - Omega)|: the enumerated pooled cell must carry exactly the unflagged mass"
    },
    {
      "name": "d1_timing_split_residual",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "err_2 = max_{D=1} |P^F - P^P_{c-} - R - J| below 1e-12",
      "tol": 1e-12,
      "max_err2": 0.0,
      "expected_magnitude": "~10 eps |mu_v| ~ 2e-15; a value above 1e-8 would mean P_ND is not P^P_{f-} (RD-3)",
      "why_wiring": "telescoping subtraction of three prices computed on the same order flow"
    },
    {
      "name": "d1_cell_mass_floor",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "predicted minimum mass of each cell at least 0.01 under the interiority calibration; outside it only the zero partition and timing-split residuals are predicted",
      "floor": 0.01,
      "n_degenerate_nodes": 25,
      "degenerate_nodes": [
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.08462696676439771,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.08788437014471917,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.09076405861553302,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.09337594348697996,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.09602833824479486,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.08462696676439771,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.08788437014471917,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.09076405861553302,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.09337594348697996,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.09602833824479486,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.08462696676439771,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.08788437014471917,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.09076405861553302,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.09337594348697996,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.09602833824479486,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.75,
          "T": 10,
          "tau": 0.08462696676439771,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.75,
          "T": 10,
          "tau": 0.08788437014471917,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.75,
          "T": 10,
          "tau": 0.09076405861553302,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.75,
          "T": 10,
          "tau": 0.09337594348697996,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.75,
          "T": 10,
          "tau": 0.09602833824479486,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.85,
          "T": 10,
          "tau": 0.08462696676439771,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.85,
          "T": 10,
          "tau": 0.08788437014471917,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.85,
          "T": 10,
          "tau": 0.09076405861553302,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.85,
          "T": 10,
          "tau": 0.09337594348697996,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        },
        {
          "kappa": 0.85,
          "T": 10,
          "tau": 0.09602833824479486,
          "reasons": [
            "flagged cell mass 0.0006813 < 0.01"
          ]
        }
      ],
      "reading": "the T = H = 10 corner drives Omega to 6.8e-4, below the 0.01 floor, at every tau on the ladder. Those nodes are reported as degenerate, not silently kept: only the partition and timing-split residuals are claimed there."
    },
    {
      "name": "d1_rho0_at_T_equals_H",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "varrho_0 = share of flagged mass with c = 0 at the T = H node; predicted 1.000. This is the node that exercises the P^P_{-1} = E[Y] convention",
      "T": 10,
      "n_corner_nodes": 25,
      "varrho_0_min": 1.0,
      "varrho_0_max": 1.0
    },
    {
      "name": "d1_QF_T_monotonicity",
      "kind": "substantive",
      "pass": true,
      "vacuous": true,
      "finding": "Q^F is identically 0 at EVERY T on this menu, not only at T >= 5. On the accumulation-length family the crossing date satisfies c ~ n-1 for every type that crosses at all, so the filing date f = c + T always lands at or after accumulation completes and B^F = b*(s). Any Q^F T-monotonicity assertion is therefore VACUOUS at this calibration and must not be reported as a pass of substance. The small-T column (T = 1, 2, 3) is included and does not rescue it.",
      "all_Q_F_zero": true,
      "rows": [
        {
          "T": 1,
          "n_flagged_atoms": 10,
          "max_Q_F_pp": 0.0,
          "min_Q_F_pp": 0.0,
          "min_B_F_pp": 9.143561264653497,
          "max_B_F_pp": 9.94864755873579
        },
        {
          "T": 2,
          "n_flagged_atoms": 10,
          "max_Q_F_pp": 0.0,
          "min_Q_F_pp": 0.0,
          "min_B_F_pp": 9.143561264653497,
          "max_B_F_pp": 9.94864755873579
        },
        {
          "T": 3,
          "n_flagged_atoms": 10,
          "max_Q_F_pp": 0.0,
          "min_Q_F_pp": 0.0,
          "min_B_F_pp": 9.143561264653497,
          "max_B_F_pp": 9.94864755873579
        },
        {
          "T": 5,
          "n_flagged_atoms": 10,
          "max_Q_F_pp": 0.0,
          "min_Q_F_pp": 0.0,
          "min_B_F_pp": 9.143561264653497,
          "max_B_F_pp": 9.94864755873579
        },
        {
          "T": 10,
          "n_flagged_atoms": 2,
          "max_Q_F_pp": 0.0,
          "min_Q_F_pp": 0.0,
          "min_B_F_pp": 9.911983673570605,
          "max_B_F_pp": 9.94864755873579
        }
      ],
      "consequence_for_A7": "A7' injectivity of (B^F, Q^F) reduces here to strict monotonicity of B^F = b*(s), which is what a7_certificate's min-slope gate measures"
    },
    {
      "name": "d1_clock_equivalence_H12",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "design section 13, ruling 2: H = 12 robustness re-run, cheap for D1",
      "scope": "menu/clock half only",
      "max_err1_at_H12": 0,
      "policy": "the cutoffs are the frozen H = 10 baseline equilibrium; H = 12 cannot be re-solved because the solver runs through the enumeration",
      "enumeration_at_H12": "NOT EVALUABLE -- feasible histories 8,503,056 x N_theta 14 = 1.190e+08 exceeds the design build-step-4 gate of 1e8 (working set ~2.5 GB). The gate is respected, not overridden. err_2, the history-level exhaustion residual and every price object are therefore reported at H = 10 only.",
      "feasible_history_count_H10": 826686,
      "feasible_history_count_H12": 8503056,
      "counter_validation": "the H = 10 value reproduces pooled.py's enumerated 826,686 exactly",
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "err1": 0,
          "Omega": 0.16867782523442393,
          "pi_bar_pr": 0.06935319074143932,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "err1": 0,
          "Omega": 0.16867782523442398,
          "pi_bar_pr": 0.06935319074143934,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "err1": 0,
          "Omega": 0.13839631193144664,
          "pi_bar_pr": 0.10206126073370039,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "err1": 0,
          "Omega": 0.08303778676423275,
          "pi_bar_pr": 0.15627130731880298,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "err1": 0,
          "Omega": 0.027679261597019337,
          "pi_bar_pr": 0.20430851790510443,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "err1": 0,
          "Omega": 0.028913438392177894,
          "pi_bar_pr": 0.20329725484974828,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "err1": 0,
          "Omega": 0.028913438392177897,
          "pi_bar_pr": 0.2032972548497483,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "err1": 0,
          "Omega": 0.028913438392177904,
          "pi_bar_pr": 0.2032972548497483,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "err1": 0,
          "Omega": 0.02891343839217789,
          "pi_bar_pr": 0.20329725484974825,
          "corner": false,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "err1": 0,
          "Omega": 0.027679261597019337,
          "pi_bar_pr": 0.20430851790510443,
          "corner": false,
          "degenerate": []
        }
      ]
    }
  ],
  "n_fail": 0,
  "n_vacuous": 1,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "8ef7c5c2d3896bf8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/threads/thread1_turn2_answer.md, D1 NUMERICAL CHECK REQUEST (turn-2 supersedes turn-1); core_D1_L1_L2_rederivation.md section A"
  },
  "grid": {
    "kappa": [
      0.15,
      0.35,
      0.55,
      0.75,
      0.85
    ],
    "tau": [
      0.08462696676439771,
      0.08788437014471917,
      0.09076405861553302,
      0.09337594348697996,
      0.09602833824479486
    ],
    "tau_quantiles": [
      0.1,
      0.3,
      0.5,
      0.7,
      0.9
    ],
    "T": [
      5,
      10
    ],
    "T_for_QF_column": [
      1,
      2,
      3,
      5,
      10
    ],
    "H": 10,
    "H_robustness": 12,
    "M": 2,
    "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice b*(s) distribution, design section 6.2",
    "policy": "frozen at the baseline equilibrium k, per the requests' fixed-policy hypothesis",
    "n_nodes": 50,
    "n_scan_points_per_node": "20,001 uniform + every breakpoint (nudged both ways) + every atom midpoint"
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "n_atoms_baseline": 19,
    "discarded_mass": 0.0
  },
  "baseline": {
    "k": [
      1.2405757282617416,
      1.5310222869296415
    ],
    "tau": 0.09076405861553302,
    "T": 5,
    "H": 10,
    "Omega": 0.1383963119314466,
    "R_bp": 389.1770949414176,
    "J_bp": 2590.5234497488327,
    "identity_residual": 0.0
  },
  "degenerate_nodes": [
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    }
  ],
  "multiple_root_nodes": 0,
  "node_table": [
    {
      "kappa": 0.15,
      "T": 5,
      "tau_quantile": 0.1,
      "tau": 0.08462696676439771,
      "corner": false,
      "Omega": 0.14465741548984065,
      "pi_bar_pr": 0.09548835352967079,
      "err3_exclusivity": 0.0,
      "overlap_mass": 0.0,
      "gap_mass": 0.0,
      "exhaustion_residual": 0.0,
      "history_level_mass_error": 1.1102230246251565e-16,
      "err2_timing_split": 0.0,
      "R_bp": 695.6512136458542,
      "J_bp": 1062.2605021710456,
      "n_atoms": 23,
      "n_flagged_atoms": 13,
      "degenerate": [],
      "multiple_root_nodes": 0
    },
    "...ELIDED: 48 of 50 array entries omitted here (kept: first 1, last 1 -- tightened past the base first-3/last-1 rule because the bundle exceeded the ~500KB target after every proof and the card were kept verbatim). Full array is in the committed file quality_reports/fixes/t2_d1_check.json, sha256=21d37d727dc5d4736331ff75ef9e68b0e3630964ab56b3c62044f109c02d063d...",
    {
      "kappa": 0.85,
      "T": 10,
      "tau_quantile": 0.9,
      "tau": 0.09602833824479486,
      "corner": true,
      "Omega": 0.0006812715261460648,
      "pi_bar_pr": 0.2258052337385839,
      "err3_exclusivity": 0.0,
      "overlap_mass": 0.0,
      "gap_mass": 0.0,
      "exhaustion_residual": 0.0,
      "history_level_mass_error": 3.3306690738754696e-16,
      "err2_timing_split": 0.0,
      "R_bp": 3842.2694896012977,
      "J_bp": 12894.708539956779,
      "n_atoms": 15,
      "n_flagged_atoms": 1,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "multiple_root_nodes": 0
    }
  ],
  "seconds": 191.77261583297513,
  "all_pass": true
}
```

### FILE: quality_reports/fixes/t2_l1_check.json

```json
{
  "checks": [
    {
      "name": "l1_decomposition_residual",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "err_4 = |Delta^act - (Omega M_F + (1-Omega) M_P)|, both sides from the same solved equilibrium object; predicted 0, required below 1e-12",
      "tol": 1e-12,
      "max_err4": 8.673617379884035e-19,
      "n_nodes": 25,
      "n_skipped_non_interior": 25,
      "skipped": [
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.08462696676439771,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.08788437014471917,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.09076405861553302,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.09337594348697996,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.15,
          "T": 10,
          "tau": 0.09602833824479486,
          "Omega": 0.0006812715261460648,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.08462696676439771,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.08788437014471917,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.09076405861553302,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.09337594348697996,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.35,
          "T": 10,
          "tau": 0.09602833824479486,
          "Omega": 0.0006812715261460648,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.08462696676439771,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        },
        {
          "kappa": 0.55,
          "T": 10,
          "tau": 0.08788437014471917,
          "Omega": 0.0006812715261460647,
          "why": "outside the request's interior filter 0.01 <= Omega <= 0.99"
        }
      ],
      "integration": "deterministic: exact Phi-difference atom masses plus 20-node Gauss-Legendre per atom; no Monte Carlo",
      "why_wiring": "total_premium sums Delta^act over the same enumeration the two-term form reads; the residual cannot falsify L1",
      "rows": [
        {
          "kappa": 0.15,
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "corner": false,
          "Omega": 0.14465741548984065,
          "Delta_act_pp": 0.20871798099650177,
          "M_F_pp": 0.5781240792474046,
          "M_P_pp": 0.14624321076187763,
          "two_term_pp": 0.20871798099650177,
          "err4": 0.0
        },
        {
          "kappa": 0.15,
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "corner": false,
          "Omega": 0.1446574154898407,
          "Delta_act_pp": 0.2087179809965017,
          "M_F_pp": 0.5781240792474042,
          "M_P_pp": 0.14624321076187768,
          "two_term_pp": 0.2087179809965017,
          "err4": 0.0
        },
        {
          "kappa": 0.15,
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "corner": false,
          "Omega": 0.1383963119314466,
          "Delta_act_pp": 0.20949439126721728,
          "M_F_pp": 0.552817848535105,
          "M_P_pp": 0.15434757499494428,
          "two_term_pp": 0.20949439126721725,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.15,
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "corner": false,
          "Omega": 0.08303778676423275,
          "Delta_act_pp": 0.21735072650384615,
          "M_F_pp": 0.33067147617283865,
          "M_P_pp": 0.20708868504657468,
          "two_term_pp": 0.2173507265038461,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.15,
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "corner": false,
          "Omega": 0.02767926159701934,
          "Delta_act_pp": 0.24718672732299737,
          "M_F_pp": 0.111337098812026,
          "M_P_pp": 0.2510539876383427,
          "two_term_pp": 0.24718672732299737,
          "err4": 0.0
        },
        {
          "kappa": 0.35,
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "corner": false,
          "Omega": 0.14465741548984065,
          "Delta_act_pp": 0.2365133422663554,
          "M_F_pp": 0.5781240792474046,
          "M_P_pp": 0.178739384544423,
          "two_term_pp": 0.23651334226635537,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.35,
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "corner": false,
          "Omega": 0.1446574154898407,
          "Delta_act_pp": 0.23651334226635531,
          "M_F_pp": 0.5781240792474042,
          "M_P_pp": 0.178739384544423,
          "two_term_pp": 0.23651334226635537,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.35,
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "corner": false,
          "Omega": 0.1383963119314466,
          "Delta_act_pp": 0.24213053594805142,
          "M_F_pp": 0.552817848535105,
          "M_P_pp": 0.19222594660915387,
          "two_term_pp": 0.24213053594805142,
          "err4": 0.0
        },
        {
          "kappa": 0.35,
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "corner": false,
          "Omega": 0.08303778676423275,
          "Delta_act_pp": 0.28625142390543895,
          "M_F_pp": 0.33067147617283865,
          "M_P_pp": 0.28222885593590363,
          "two_term_pp": 0.2862514239054389,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.35,
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "corner": false,
          "Omega": 0.02767926159701934,
          "Delta_act_pp": 0.3798704769606992,
          "M_F_pp": 0.111337098812026,
          "M_P_pp": 0.38751487384306615,
          "two_term_pp": 0.3798704769606992,
          "err4": 0.0
        },
        {
          "kappa": 0.55,
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "corner": false,
          "Omega": 0.14465741548984065,
          "Delta_act_pp": 0.2608348420018674,
          "M_F_pp": 0.5781240792474046,
          "M_P_pp": 0.20717418970432333,
          "two_term_pp": 0.26083484200186735,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.55,
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "corner": false,
          "Omega": 0.1446574154898407,
          "Delta_act_pp": 0.2608348420018674,
          "M_F_pp": 0.5781240792474042,
          "M_P_pp": 0.2071741897043234,
          "two_term_pp": 0.2608348420018674,
          "err4": 0.0
        },
        {
          "kappa": 0.55,
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "corner": false,
          "Omega": 0.1383963119314466,
          "Delta_act_pp": 0.26850958710758577,
          "M_F_pp": 0.552817848535105,
          "M_P_pp": 0.222842170198758,
          "two_term_pp": 0.26850958710758577,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.55,
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "corner": false,
          "Omega": 0.08303778676423275,
          "Delta_act_pp": 0.3429545211797668,
          "M_F_pp": 0.33067147617283865,
          "M_P_pp": 0.3440668427753335,
          "two_term_pp": 0.34295452117976677,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.55,
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "corner": false,
          "Omega": 0.02767926159701934,
          "Delta_act_pp": 0.4773597195791536,
          "M_F_pp": 0.111337098812026,
          "M_P_pp": 0.4877793634996158,
          "two_term_pp": 0.4773597195791537,
          "err4": 8.673617379884035e-19
        },
        {
          "kappa": 0.75,
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "corner": false,
          "Omega": 0.14465741548984065,
          "Delta_act_pp": 0.22537557077113587,
          "M_F_pp": 0.5781240792474046,
          "M_P_pp": 0.16571796868495436,
          "two_term_pp": 0.22537557077113587,
          "err4": 0.0
        },
        {
          "kappa": 0.75,
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "corner": false,
          "Omega": 0.1446574154898407,
          "Delta_act_pp": 0.22537557077113574,
          "M_F_pp": 0.5781240792474042,
          "M_P_pp": 0.16571796868495428,
          "two_term_pp": 0.2253755707711358,
          "err4": 4.336808689942018e-19
        },
        {
          "kappa": 0.75,
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "corner": false,
          "Omega": 0.1383963119314466,
          "Delta_act_pp": 0.22885211308167216,
          "M_F_pp": 0.552817848535105,
          "M_P_pp": 0.17681465827525022,
          "two_term_pp": 0.22885211308167216,
          "err4": 0.0
        },
        {
          "kappa": 0.75,
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "corner": false,
          "Omega": 0.08303778676423275,
          "Delta_act_pp": 0.26628388690266674,
          "M_F_pp": 0.33067147617283865,
          "M_P_pp": 0.2604531091117123,
          "two_term_pp": 0.26628388690266674,
          "err4": 0.0
        },
        {
          "kappa": 0.75,
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "corner": false,
          "Omega": 0.02767926159701934,
          "Delta_act_pp": 0.3533571200905467,
          "M_F_pp": 0.111337098812026,
          "M_P_pp": 0.36024675559465746,
          "two_term_pp": 0.3533571200905467,
          "err4": 0.0
        },
        {
          "kappa": 0.85,
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "corner": false,
          "Omega": 0.14465741548984065,
          "Delta_act_pp": 0.21003670704069968,
          "M_F_pp": 0.5781240792474046,
          "M_P_pp": 0.14778496264945978,
          "two_term_pp": 0.21003670704069968,
          "err4": 0.0
        },
        {
          "kappa": 0.85,
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "corner": false,
          "Omega": 0.1446574154898407,
          "Delta_act_pp": 0.21003670704069963,
          "M_F_pp": 0.5781240792474042,
          "M_P_pp": 0.14778496264945978,
          "two_term_pp": 0.21003670704069963,
          "err4": 0.0
        },
        {
          "kappa": 0.85,
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "corner": false,
          "Omega": 0.1383963119314466,
          "Delta_act_pp": 0.21126249149795517,
          "M_F_pp": 0.552817848535105,
          "M_P_pp": 0.15639967882785788,
          "two_term_pp": 0.21126249149795517,
          "err4": 0.0
        },
        {
          "kappa": 0.85,
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "corner": false,
          "Omega": 0.08303778676423275,
          "Delta_act_pp": 0.22287560602615933,
          "M_F_pp": 0.33067147617283865,
          "M_P_pp": 0.2131138837325893,
          "two_term_pp": 0.22287560602615933,
          "err4": 0.0
        },
        {
          "kappa": 0.85,
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "corner": false,
          "Omega": 0.02767926159701934,
          "Delta_act_pp": 0.264964469219798,
          "M_F_pp": 0.111337098812026,
          "M_P_pp": 0.2693378123009743,
          "two_term_pp": 0.264964469219798,
          "err4": 0.0
        }
      ]
    },
    {
      "name": "l1_degenerate_Omega_1",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "one all-flagged policy with Omega = 1: verify Delta^act = M_F and record the zero-mass cell average as UNDEFINED rather than imputing it",
      "construction": "all-Voice menu (k = (s_lo, s_lo)) with tau = 0.0302337771 <= inf_s B(s, H-T) = 0.0302597524",
      "tol_err5": 1e-10,
      "Omega": 1.0,
      "err5": 6.938893903907228e-18,
      "Delta_act_pp": 4.694626206538875,
      "M_F_pp": 4.694626206538876,
      "M_P": null,
      "M_P_is_nan": true,
      "clause_with_content": "isnan(M_P) is asserted, not a tolerance: an implementation returning M_P = 0 would pass err_4 while violating the clause the lemma actually adds",
      "degenerate": [
        "pooled cell mass 0 < 0.01"
      ]
    },
    {
      "name": "l1_degenerate_Omega_0",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "one all-pooled policy with Omega = 0: verify Delta^act = M_P and record M_F as UNDEFINED",
      "construction": "tau = 0.1200 > b_bar = 0.1, so no type ever crosses",
      "tol_err5": 1e-10,
      "Omega": 0.0,
      "residual_Delta_act_minus_M_P": 0.0,
      "Delta_act_pp": 0.5761873596989027,
      "M_P_pp": 0.5761873596989027,
      "M_F": null,
      "M_F_is_nan": true,
      "degenerate": [
        "flagged cell mass 0 < 0.01"
      ]
    },
    {
      "name": "l1_H12_not_evaluable",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "design section 13, ruling 2: H = 12 robustness is cheap for L1",
      "outcome": "NOT EVALUABLE. Every object in L1's identity -- Delta^act and M_P -- runs through the pooled enumeration, and at H = 12 the feasible history count is 8,503,056, so 8,503,056 x N_theta 14 = 1.19e8 exceeds the design's own build-step-4 gate of 1e8 (working set ~2.5 GB). The gate is respected rather than overridden; L1 is reported at H = 10 only.",
      "feasible_history_count_H12": 8503056,
      "gate_limit": 100000000.0
    }
  ],
  "n_fail": 0,
  "n_vacuous": 0,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "8ef7c5c2d3896bf8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/threads/thread1_turn2_answer.md, L1 NUMERICAL CHECK REQUEST; core_D1_L1_L2_rederivation.md section B",
    "classification": "design section 0 rules L1 a WIRING check: both sides run through the same enumeration, so the residual is machine noise by construction and is not evidence for the lemma"
  },
  "grid": {
    "kappa": [
      0.15,
      0.35,
      0.55,
      0.75,
      0.85
    ],
    "tau": [
      0.08462696676439771,
      0.08788437014471917,
      0.09076405861553302,
      0.09337594348697996,
      0.09602833824479486
    ],
    "tau_quantiles": [
      0.1,
      0.3,
      0.5,
      0.7,
      0.9
    ],
    "T": [
      5,
      10
    ],
    "H": 10,
    "M": 2,
    "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice b*(s) distribution, design section 6.2",
    "policy": "frozen at the baseline equilibrium k",
    "interior_filter": "0.01 <= Omega <= 0.99",
    "units": "Delta^act, M_F, M_P in premium percentage points, never normalised indices"
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "n_atoms_baseline": 19,
    "discarded_mass": 0.0
  },
  "degenerate_nodes": [
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.15,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.35,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.55,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.75,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "kappa": 0.85,
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    }
  ],
  "multiple_root_nodes": 0,
  "baseline": {
    "k": [
      1.2405757282617416,
      1.5310222869296415
    ],
    "tau": 0.09076405861553302,
    "T": 5,
    "H": 10,
    "Omega": 0.1383963119314466,
    "Delta_act_pp": 0.268471939827342,
    "M_F_pp": 0.552817848535105,
    "M_P_pp": 0.2227984757708382,
    "cutoff_scale": 2.595657022652631e-11,
    "payoff_scale": 0.0
  },
  "seconds": 84.9344951249659,
  "all_pass": true
}
```

### FILE: quality_reports/fixes/t2_l2_check.json

```json
{
  "checks": [
    {
      "name": "l2_flagged_invariance_ranges",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "range_kappa of each flagged engagement posterior, each conditional-value posterior used by pricing, P^F, the bidder-entry probability p, and M_F; predicted exactly zero, required below 1e-10",
      "tol": 1e-10,
      "max_range": {
        "v_hat": 0.0,
        "pi_flagged": 0.0,
        "P_F": 0.0,
        "p_bid": 0.0,
        "M_F": 0.0,
        "Omega": 0.0
      },
      "note": "P^F and p are compared POINTWISE over the flagged quadrature nodes, not only in the M_F average, so a sign-cancelling error cannot hide inside M_F",
      "Omega_note": "range_kappa Omega is the Step 2 by-product: D is deterministic in (j,s) and never touches the noise law",
      "rows": [
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "n_flagged_nodes": 260,
          "M_F_pp_at_kappa_ref": 0.5781240792474046,
          "Omega_at_kappa_ref": 0.14465741548984065
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 5,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "n_flagged_nodes": 240,
          "M_F_pp_at_kappa_ref": 0.5781240792474042,
          "Omega_at_kappa_ref": 0.1446574154898407
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "n_flagged_nodes": 200,
          "M_F_pp_at_kappa_ref": 0.552817848535105,
          "Omega_at_kappa_ref": 0.1383963119314466
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 5,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "n_flagged_nodes": 100,
          "M_F_pp_at_kappa_ref": 0.33067147617283865,
          "Omega_at_kappa_ref": 0.08303778676423275
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "n_flagged_nodes": 60,
          "M_F_pp_at_kappa_ref": 0.111337098812026,
          "Omega_at_kappa_ref": 0.02767926159701934
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 10,
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "n_flagged_nodes": 20,
          "M_F_pp_at_kappa_ref": 0.0032653741961090753,
          "Omega_at_kappa_ref": 0.0006812715261460647
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 10,
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "n_flagged_nodes": 40,
          "M_F_pp_at_kappa_ref": 0.003265374196109537,
          "Omega_at_kappa_ref": 0.0006812715261460647
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 10,
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "n_flagged_nodes": 40,
          "M_F_pp_at_kappa_ref": 0.003265374196109093,
          "Omega_at_kappa_ref": 0.0006812715261460647
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 10,
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "n_flagged_nodes": 20,
          "M_F_pp_at_kappa_ref": 0.0032653741961090753,
          "Omega_at_kappa_ref": 0.0006812715261460647
        },
        {
          "range_v_hat_max_over_nodes": 0.0,
          "range_P_F_max_over_nodes": 0.0,
          "range_p_bid_max_over_nodes": 0.0,
          "range_pi_flagged": 0.0,
          "range_M_F": 0.0,
          "range_Omega": 0.0,
          "T": 10,
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "n_flagged_nodes": 20,
          "M_F_pp_at_kappa_ref": 0.0032653741961090753,
          "Omega_at_kappa_ref": 0.0006812715261460648
        }
      ]
    },
    {
      "name": "l2_flagged_invariance_derivs",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "central finite-difference derivatives in kappa below 1e-8 in absolute value",
      "tol": 1e-08,
      "kappa": 0.5,
      "method": "premium.d_dkappa, 4th-order central difference, h = 1e-3",
      "derivatives": {
        "dM_F_dkappa": 0.0,
        "dOmega_dkappa": 0.0,
        "dP_F_dkappa": 0.0,
        "dp_bid_dkappa": 0.0
      }
    },
    {
      "name": "l2_placebo_M_P_moves",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "PLACEBO 1: D_P = max_kappa |M_P(kappa) - M_P(0.5)| must be STRICTLY POSITIVE. If it returns at solver tolerance the invariance check is uninformative rather than confirmatory, and the grid must be rebuilt with pi_bar bounded away from zero",
      "D_P": 0.0007223678779180148,
      "D_P_pp": 0.07223678779180148,
      "M_P_min_pp": 0.1505616879790367,
      "M_P_max_pp": 0.222842170198758,
      "range_M_P_pp": 0.07228048221972129,
      "pi_bar_pr_at_reference": 0.10206126073370039,
      "verdict": "the invariance target is NOT vacuous at this calibration: M_P moves by 0.072280 premium pp over the kappa grid while M_F moves by exactly 0",
      "M_P_pp_by_kappa": [
        0.1505616879790367,
        0.15143696821182068,
        0.15434757499494428,
        0.16000431833787593,
        0.16849001460233046,
        0.17947885602943942,
        0.19222594660915387,
        0.2052357869349295,
        0.21623100522062338,
        0.2227984757708382,
        0.222842170198758,
        0.2155322480848083,
        0.2032398320886169,
        0.18990130006898892,
        0.17681465827525022,
        0.164914461162899,
        0.15639967882785788,
        0.1519726357256568,
        0.15060053491851783
      ]
    },
    {
      "name": "l2_placebo_J_moves",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "PLACEBO 2: D_J = max_kappa |J(s_0;kappa) - J(s_0;0.5)| must be STRICTLY POSITIVE, with d_kappa J = -d_kappa P^P_{f-}. D_J = 0 would indicate the pooled price is being cached rather than recomputed",
      "s_0": 2.662283757197735,
      "atom": [
        2.549291170307685,
        2.7752763440877857
      ],
      "D_J": 0.5089777332231028,
      "D_J_bp": 5089.777332231028,
      "J_min_bp": 593.5941104243373,
      "J_max_bp": 5804.298321506394,
      "J_bp_by_kappa": [
        593.5941104243373,
        2061.876946057806,
        3456.665510217509,
        4504.935350954081,
        5173.931374365166,
        5552.995181702133,
        5740.861681065689,
        5804.298321506394,
        5779.306765326507,
        5683.371442655365,
        5524.447377101687,
        5305.438050467293,
        5026.875409522197,
        4689.177781892557,
        4291.864308201056,
        3827.172357400965,
        3267.765275950655,
        2527.145256162311,
        1261.930711645676
      ]
    },
    {
      "name": "l2_placebo_M_P_sign_A_tau",
      "kind": "substantive",
      "pass": false,
      "vacuous": false,
      "request": "the placebo's SIGN clause: d_kappa M_P <= 0 under A(tau)'s maintained C_h(pi_bar) <= 0",
      "n_positive_increments": 10,
      "n_total_increments": 18,
      "n_sign_changes": 1,
      "kappa_at_M_P_peak": 0.55,
      "finding": "FAILED HYPOTHESIS, reported and not smoothed: the enumerated pooled M_P is HUMP-SHAPED in kappa on this calibration -- it rises to a peak near kappa = 0.55 and falls after -- so d_kappa M_P changes sign and the A(tau)-conditional prediction d_kappa M_P <= 0 does not hold globally. This is a statement about A(tau)'s orientation on the enumerated two-round pooled law, NOT about L2: L2's own claims are the flagged-side ranges and derivatives above, which are exactly zero. Design section 0 rules that the enumeration never imposes A(tau), so this gap is the object the design intended to measure.",
      "scope": "ancillary to L2; L2's verdict is carried by l2_flagged_invariance_ranges and _derivs"
    }
  ],
  "n_fail": 1,
  "n_vacuous": 0,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "8ef7c5c2d3896bf8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/threads/thread1_turn2_answer.md, L2 NUMERICAL CHECK REQUEST; placebos from core_D1_L1_L2_rederivation.md section C",
    "classification": "design section 0 rules L2 SUBSTANTIVE: the flagged path must never touch the kappa-dependent array"
  },
  "grid": {
    "kappa": [
      0.05,
      0.1,
      0.15,
      0.2,
      0.25,
      0.3,
      0.35,
      0.4,
      0.45,
      0.5,
      0.55,
      0.6,
      0.65,
      0.7,
      0.75,
      0.8,
      0.85,
      0.9,
      0.95
    ],
    "kappa_reference": 0.5,
    "tau": [
      0.08462696676439771,
      0.08788437014471917,
      0.09076405861553302,
      0.09337594348697996,
      0.09602833824479486
    ],
    "tau_quantiles": [
      0.1,
      0.3,
      0.5,
      0.7,
      0.9
    ],
    "T": [
      5,
      10
    ],
    "H": 10,
    "M": 2,
    "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice b*(s) distribution, design section 6.2",
    "policy": "frozen at the baseline equilibrium k; L2 is a fixed-policy statement and a re-solve at each kappa would test a GE channel the lemma explicitly does not claim",
    "n_nodes": 190
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "n_atoms_baseline": 19,
    "discarded_mass": 0.0
  },
  "degenerate_nodes": [
    {
      "T": 10,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    }
  ],
  "multiple_root_nodes": 0,
  "baseline": {
    "k": [
      1.2405757282617416,
      1.5310222869296415
    ],
    "tau": 0.09076405861553302,
    "T": 5,
    "H": 10,
    "Omega": 0.1383963119314466,
    "M_F_pp": 0.552817848535105,
    "M_P_pp": 0.2227984757708382,
    "pi_bar_pr": 0.10206126073370039,
    "cutoff_scale": 2.595657022652631e-11,
    "payoff_scale": 0.0
  },
  "seconds": 135.63737950008363,
  "all_pass": false
}
```

### FILE: quality_reports/fixes/t2_l3_check.json

```json
{
  "checks": [
    {
      "name": "l3_block1_derivative_identity",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 1, Example A: central finite difference of E_kappa[h] (step 1e-5) vs A'_kappa C_h(1) with A'_kappa = -1/4. Acceptance: pointwise residual below 1e-10; range of d_kappa E across the kappa grid below 1e-12",
      "routes": "route 1 enumerates the three atoms and differentiates numerically; route 2 is the closed-form three-atom law",
      "tol_pointwise": 1e-10,
      "tol_range": 1e-12,
      "C_h_1": -0.022547549753707208,
      "predicted_C_h_1": -0.0225,
      "dE_dkappa": 0.005636887439129875,
      "predicted_dE_dkappa": 0.00563,
      "sign": "positive",
      "max_residual_at_requested_step": 4.50120409695165e-12,
      "range_dE_over_kappa_at_requested_step": 8.326672684688674e-12,
      "range_by_step": {
        "step_1e-05": {
          "range": 8.326672684688674e-12,
          "max_residual_vs_closed_form": 4.50120409695165e-12
        },
        "step_0.0001": {
          "range": 5.551115123125783e-13,
          "max_residual_vs_closed_form": 3.3786862196905076e-13
        },
        "step_0.001": {
          "range": 8.326672684688674e-14,
          "max_residual_vs_closed_form": 5.0709436649754025e-14
        }
      },
      "roundoff_confirmed_by_step_scaling": true,
      "resolution_note": "The pointwise residual criterion (1e-10) passes at the requested step. The range criterion (1e-12) does NOT pass at the requested step 1e-5: the range is 8.327e-12. That number is floating-point roundoff of the difference quotient, not scatter in the derivative: eps |E| / (2 h) at |E| ~ 0.5 and h = 1e-5 is ~5e-12, which is what is observed, and the range falls by the factor 100 that pure roundoff predicts when the step is raised to 1e-3 (8.327e-12 -> 8.327e-14), where it clears 1e-12. E_kappa[h] is exactly affine in kappa on Example A, so the central difference has zero truncation error and roundoff is the only term. The requested tolerance is below the requested step's resolution -- the same species of issue as design open question 5, resolved here by reporting the scaling rather than by moving the tolerance.",
      "h_values": {
        "h(0)": 0.0,
        "h(0.5)": 0.4942735175419424,
        "h(1)": 0.9659994853301775
      },
      "rows": [
        {
          "kappa": 0.05,
          "dE_dkappa": 0.005636887437376891,
          "A_prime_C_h": 0.005636887438426802,
          "residual": 1.049911026174133e-12
        },
        {
          "kappa": 0.1,
          "dE_dkappa": 0.0056368874401524485,
          "A_prime_C_h": 0.005636887438426802,
          "residual": 1.7256465353887585e-12
        },
        {
          "kappa": 0.15,
          "dE_dkappa": 0.0056368874401524485,
          "A_prime_C_h": 0.005636887438426802,
          "residual": 1.7256465353887585e-12
        },
        {
          "kappa": 0.2,
          "dE_dkappa": 0.005636887437376891,
          "A_prime_C_h": 0.005636887438426802,
          "residual": 1.049911026174133e-12
        },
        {
          "kappa": 0.25,
          "dE_dkappa": 0.0056368874401524485,
          "A_prime_C_h": 0.005636887438426802,
          "residual": 1.7256465353887585e-12
        }
      ]
    },
    {
      "name": "l3_block1b_split_routes",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "design section 8 split of L3's comparison, with the section 13 ruling-5 tolerances",
      "tolerance_note": "tolerance amended per design review 2026-08-21",
      "kernel": "check convention: P(pi) = m0 + Delta_m pi at m0=0.10, Delta_m=0.18, K=0.15, S_bar=1.44, sigma_xi=0.40",
      "weights": "Example A' (Step 16): alpha = 0.4, c = 0.3, A'_kappa = -0.3, pi_bar free",
      "split_at_pi_bar": 0.01,
      "tol_absolute_full_model": 1e-10,
      "tol_relative_chord": 1e-06,
      "which_criterion_decides": [
        "design section 8 routes pi_bar >= 1e-2 to the enumerated d_kappa E vs A'_kappa C_h comparison at absolute 1e-10, and pi_bar < 1e-2 to the standalone chord module, where the amended relative criterion applies to the chord's own cancellation error against |C_h|. The finite-difference residual is still REPORTED below the split (column fd_vs_closed_form_relative) as a diagnostic: it runs 1e-6 to 1e-5 relative there, which is the difference quotient's roundoff floor eps|E|/(2h) measured against a chord of size 1e-11, and is exactly the two-significant-digit problem ruling 5 was written to remove."
      ],
      "rows": [
        {
          "pi_bar": 0.0001,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -4.3827679861523604e-11,
          "A_prime_C_h": 1.3148303958457081e-11,
          "deciding_quantity": 5.050016817857365e-10,
          "chord_cancellation_headroom": 2.2133052038836275e-20,
          "relative_cancellation_residual": 5.050016817857365e-10,
          "fd_vs_closed_form_abs_residual": 3.578883608722714e-16,
          "fd_vs_closed_form_relative": 8.165806677493376e-06,
          "pass": true
        },
        {
          "pi_bar": 0.0002,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -1.7534296776577744e-10,
          "A_prime_C_h": 5.260289032973323e-11,
          "deciding_quantity": 2.5245417998652223e-10,
          "chord_cancellation_headroom": 4.4266065143712546e-20,
          "relative_cancellation_residual": 2.5245417998652223e-10,
          "fd_vs_closed_form_abs_residual": 5.662001900290888e-16,
          "fd_vs_closed_form_relative": 3.229101213716293e-06,
          "pass": true
        },
        {
          "pi_bar": 0.0005,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -1.0964984031424513e-09,
          "A_prime_C_h": 3.289495209427354e-10,
          "deciding_quantity": 1.0092570166465412e-10,
          "chord_cancellation_headroom": 1.1066487071132468e-19,
          "relative_cancellation_residual": 1.0092570166465412e-10,
          "fd_vs_closed_form_abs_residual": 2.8392002290360917e-15,
          "fd_vs_closed_form_relative": 2.5893336651464668e-06,
          "pass": true
        },
        {
          "pi_bar": 0.001,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -4.390028639873408e-09,
          "A_prime_C_h": 1.3170085919620225e-09,
          "deciding_quantity": 5.041624663452234e-11,
          "chord_cancellation_headroom": 2.213287666404744e-19,
          "relative_cancellation_residual": 5.041624663452234e-11,
          "fd_vs_closed_form_abs_residual": 4.31302129411225e-15,
          "fd_vs_closed_form_relative": 9.8245857781844e-07,
          "pass": true
        },
        {
          "pi_bar": 0.002,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -1.759243475289024e-08,
          "A_prime_C_h": 5.277730425867072e-09,
          "deciding_quantity": 2.5161589807971372e-11,
          "chord_cancellation_headroom": 4.4265362697572445e-19,
          "relative_cancellation_residual": 2.5161589807971372e-11,
          "fd_vs_closed_form_abs_residual": 7.722555235006932e-15,
          "fd_vs_closed_form_relative": 4.3897023598386246e-07,
          "pass": true
        },
        {
          "pi_bar": 0.005,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -1.1056072368557934e-07,
          "A_prime_C_h": 3.31682171056738e-08,
          "deciding_quantity": 1.0009021190104222e-11,
          "chord_cancellation_headroom": 1.1066046261622213e-18,
          "relative_cancellation_residual": 1.0009021190104222e-11,
          "fd_vs_closed_form_abs_residual": 2.2352432403680463e-14,
          "fd_vs_closed_form_relative": 2.0217335468287945e-07,
          "pass": true
        },
        {
          "pi_bar": 0.01,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -4.4632308469384763e-07,
          "A_prime_C_h": 1.3389692540815428e-07,
          "deciding_quantity": 3.877436565209808e-14,
          "chord_cancellation_headroom": 2.213110148691433e-18,
          "relative_cancellation_residual": 4.958538387521455e-12,
          "fd_vs_closed_form_abs_residual": 3.877436565209808e-14,
          "fd_vs_closed_form_relative": 8.687510680451383e-08,
          "pass": true
        },
        {
          "pi_bar": 0.02,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -1.8183393350537647e-06,
          "A_prime_C_h": 5.455018005161293e-07,
          "deciding_quantity": 4.9107245983814375e-14,
          "chord_cancellation_headroom": 4.425816544943594e-18,
          "relative_cancellation_residual": 2.433988232901936e-12,
          "fd_vs_closed_form_abs_residual": 4.9107245983814375e-14,
          "fd_vs_closed_form_relative": 2.7006645589813616e-08,
          "pass": true
        },
        {
          "pi_bar": 0.05,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -1.200493935168273e-05,
          "A_prime_C_h": 3.601481805504819e-06,
          "deciding_quantity": 1.9256887776473368e-13,
          "chord_cancellation_headroom": 1.1061361737572384e-17,
          "relative_cancellation_residual": 9.214008845469024e-13,
          "fd_vs_closed_form_abs_residual": 1.9256887776473368e-13,
          "fd_vs_closed_form_relative": 1.604080388275692e-08,
          "pass": true
        },
        {
          "pi_bar": 0.1,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -5.257561485223772e-05,
          "A_prime_C_h": 1.5772684455671313e-05,
          "deciding_quantity": 2.5528329247064864e-13,
          "chord_cancellation_headroom": 2.2111049343516212e-17,
          "relative_cancellation_residual": 4.2055712340518874e-13,
          "fd_vs_closed_form_abs_residual": 2.5528329247064864e-13,
          "fd_vs_closed_form_relative": 4.855545544985354e-09,
          "pass": true
        },
        {
          "pi_bar": 0.2,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.0002514045509238727,
          "A_prime_C_h": 7.542136527716181e-05,
          "deciding_quantity": 9.843237336326638e-13,
          "chord_cancellation_headroom": 4.416627566284618e-17,
          "relative_cancellation_residual": 1.7567810725995997e-13,
          "fd_vs_closed_form_abs_residual": 9.843237336326638e-13,
          "fd_vs_closed_form_relative": 3.915297992878119e-09,
          "pass": true
        },
        {
          "pi_bar": 0.5,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.002621649795169545,
          "A_prime_C_h": 0.0007864949385508634,
          "deciding_quantity": 1.318156738275289e-12,
          "chord_cancellation_headroom": 1.0975076792750613e-16,
          "relative_cancellation_residual": 4.1863245094644086e-14,
          "fd_vs_closed_form_abs_residual": 1.318156738275289e-12,
          "fd_vs_closed_form_relative": 5.027966514459809e-10,
          "pass": true
        },
        {
          "pi_bar": 0.9,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.015818231822929407,
          "A_prime_C_h": 0.004745469546878822,
          "deciding_quantity": 3.769984324719644e-12,
          "chord_cancellation_headroom": 1.9429532946429415e-16,
          "relative_cancellation_residual": 1.2282999240322946e-14,
          "fd_vs_closed_form_abs_residual": 3.769984324719644e-12,
          "fd_vs_closed_form_relative": 2.3833158894882564e-10,
          "pass": true
        },
        {
          "pi_bar": 1.0,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.022547549753707208,
          "A_prime_C_h": 0.0067642649261121625,
          "deciding_quantity": 5.40144491634198e-12,
          "chord_cancellation_headroom": 2.1449497407792285e-16,
          "relative_cancellation_residual": 9.513005910660255e-15,
          "fd_vs_closed_form_abs_residual": 5.40144491634198e-12,
          "fd_vs_closed_form_relative": 2.395579553141418e-10,
          "pass": true
        }
      ]
    },
    {
      "name": "l3_block1b_model_kernel",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "design section 8 split of L3's comparison, with the section 13 ruling-5 tolerances",
      "tolerance_note": "tolerance amended per design review 2026-08-21",
      "kernel": "MODEL kernel: h = pi p with P at the inner pricing fixed point (numerical_v4.premium.h_kernel), v_hat = mu_v, package baseline",
      "weights": "Example A' (Step 16): alpha = 0.4, c = 0.3, A'_kappa = -0.3, pi_bar free",
      "split_at_pi_bar": 0.01,
      "tol_absolute_full_model": 1e-10,
      "tol_relative_chord": 1e-06,
      "which_criterion_decides": [
        "design section 8 routes pi_bar >= 1e-2 to the enumerated d_kappa E vs A'_kappa C_h comparison at absolute 1e-10, and pi_bar < 1e-2 to the standalone chord module, where the amended relative criterion applies to the chord's own cancellation error against |C_h|. The finite-difference residual is still REPORTED below the split (column fd_vs_closed_form_relative) as a diagnostic: it runs 1e-6 to 1e-5 relative there, which is the difference quotient's roundoff floor eps|E|/(2h) measured against a chord of size 1e-11, and is exactly the two-significant-digit problem ruling 5 was written to remove."
      ],
      "why": "the same identity on the kernel the other six scripts run, so the split is tested against the model and not only against the request's convention",
      "rows": [
        {
          "pi_bar": 0.0001,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -2.2187463469207466e-09,
          "A_prime_C_h": 6.65623904076224e-10,
          "deciding_quantity": 5.619121351870362e-12,
          "chord_cancellation_headroom": 1.2467404972366732e-20,
          "relative_cancellation_residual": 5.619121351870362e-12,
          "fd_vs_closed_form_abs_residual": 3.419485561419947e-16,
          "fd_vs_closed_form_relative": 1.5411791285496102e-07,
          "pass": true
        },
        {
          "pi_bar": 0.0002,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -8.874616474937582e-09,
          "A_prime_C_h": 2.662384942481275e-09,
          "deciding_quantity": 2.809455423165178e-12,
          "chord_cancellation_headroom": 2.4932839384024426e-20,
          "relative_cancellation_residual": 2.809455423165178e-12,
          "fd_vs_closed_form_abs_residual": 2.0818579015892698e-16,
          "fd_vs_closed_form_relative": 2.3458567561410165e-08,
          "pass": true
        },
        {
          "pi_bar": 0.0005,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -5.545943769649049e-08,
          "A_prime_C_h": 1.6637831308947147e-08,
          "deciding_quantity": 1.1236558371483046e-12,
          "chord_cancellation_headroom": 6.231732089262425e-20,
          "relative_cancellation_residual": 1.1236558371483046e-12,
          "fd_vs_closed_form_abs_residual": 4.825946493441408e-16,
          "fd_vs_closed_form_relative": 8.701758787840716e-09,
          "pass": true
        },
        {
          "pi_bar": 0.001,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -2.2179167349337288e-07,
          "A_prime_C_h": 6.653750204801186e-08,
          "deciding_quantity": 5.617225939027626e-13,
          "chord_cancellation_headroom": 1.24585394140732e-19,
          "relative_cancellation_residual": 5.617225939027626e-13,
          "fd_vs_closed_form_abs_residual": 1.5404561386517883e-15,
          "fd_vs_closed_form_relative": 6.945509334902137e-09,
          "pass": true
        },
        {
          "pi_bar": 0.002,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -8.867984424660788e-07,
          "A_prime_C_h": 2.6603953273982363e-07,
          "deciding_quantity": 2.807558826775703e-13,
          "chord_cancellation_headroom": 2.489738794716585e-19,
          "relative_cancellation_residual": 2.807558826775703e-13,
          "fd_vs_closed_form_abs_residual": 6.833682935677147e-15,
          "fd_vs_closed_form_relative": 7.706015942781207e-09,
          "pass": true
        },
        {
          "pi_bar": 0.005,
          "route": "standalone chord: C_h evaluated directly, relative cancellation criterion 1e-6 (ruling 5)",
          "C_h": -5.535603769533156e-06,
          "A_prime_C_h": 1.6606811308599468e-06,
          "deciding_quantity": 1.121755710238553e-13,
          "chord_cancellation_headroom": 6.209595138091877e-19,
          "relative_cancellation_residual": 1.121755710238553e-13,
          "fd_vs_closed_form_abs_residual": 1.133056343553525e-14,
          "fd_vs_closed_form_relative": 2.046852323119003e-09,
          "pass": true
        },
        {
          "pi_bar": 0.01,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -2.2096744831689476e-05,
          "A_prime_C_h": 6.629023449506843e-06,
          "deciding_quantity": 3.4243008581946125e-14,
          "chord_cancellation_headroom": 1.2370125646420936e-18,
          "relative_cancellation_residual": 5.598166490423802e-14,
          "fd_vs_closed_form_abs_residual": 3.4243008581946125e-14,
          "fd_vs_closed_form_relative": 1.549685659257711e-09,
          "pass": true
        },
        {
          "pi_bar": 0.02,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -8.802511937315918e-05,
          "A_prime_C_h": 2.6407535811947755e-05,
          "deciding_quantity": 6.828738624369522e-14,
          "chord_cancellation_headroom": 2.4544796264294954e-18,
          "relative_cancellation_residual": 2.7883854562291237e-14,
          "fd_vs_closed_form_abs_residual": 6.828738624369522e-14,
          "fd_vs_closed_form_relative": 7.75771583497762e-10,
          "pass": true
        },
        {
          "pi_bar": 0.05,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.0005435361705674498,
          "A_prime_C_h": 0.00016306085117023494,
          "deciding_quantity": 6.389021798593186e-14,
          "chord_cancellation_headroom": 5.991177272419836e-18,
          "relative_cancellation_residual": 1.1022591681736782e-14,
          "fd_vs_closed_form_abs_residual": 6.389021798593186e-14,
          "fd_vs_closed_form_relative": 1.1754547617177108e-10,
          "pass": true
        },
        {
          "pi_bar": 0.1,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.0021319302660065542,
          "A_prime_C_h": 0.0006395790798019663,
          "deciding_quantity": 2.99781900692242e-16,
          "chord_cancellation_headroom": 1.150897093119653e-17,
          "relative_cancellation_residual": 5.398380573091947e-15,
          "fd_vs_closed_form_abs_residual": 2.99781900692242e-16,
          "fd_vs_closed_form_relative": 1.4061524688318317e-13,
          "pass": true
        },
        {
          "pi_bar": 0.2,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.008212506241301695,
          "A_prime_C_h": 0.0024637518723905085,
          "deciding_quantity": 4.288249443040737e-13,
          "chord_cancellation_headroom": 2.119439915859887e-17,
          "relative_cancellation_residual": 2.5807467946885267e-15,
          "fd_vs_closed_form_abs_residual": 4.288249443040737e-13,
          "fd_vs_closed_form_relative": 5.221608747734775e-11,
          "pass": true
        },
        {
          "pi_bar": 0.5,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.04604324999604903,
          "A_prime_C_h": 0.013812974998814708,
          "deciding_quantity": 1.101362057109867e-12,
          "chord_cancellation_headroom": 4.0565092078116826e-17,
          "relative_cancellation_residual": 8.8102147614683405e-16,
          "fd_vs_closed_form_abs_residual": 1.101362057109867e-12,
          "fd_vs_closed_form_relative": 2.3920163263982773e-11,
          "pass": true
        },
        {
          "pi_bar": 0.9,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.12780114893014813,
          "A_prime_C_h": 0.03834034467904444,
          "deciding_quantity": 7.884595754070745e-13,
          "chord_cancellation_headroom": 4.814220428889615e-17,
          "relative_cancellation_residual": 3.7669617755321654e-16,
          "fd_vs_closed_form_abs_residual": 7.884595754070745e-13,
          "fd_vs_closed_form_relative": 6.1694247822296205e-12,
          "pass": true
        },
        {
          "pi_bar": 1.0,
          "route": "full-model: enumerated d_kappa E vs A'_kappa C_h, absolute 1e-10",
          "C_h": -0.15117975601025813,
          "A_prime_C_h": 0.045353926803077434,
          "deciding_quantity": 1.4162698791508888e-12,
          "chord_cancellation_headroom": 4.756153496027326e-17,
          "relative_cancellation_residual": 3.1460253816685633e-16,
          "fd_vs_closed_form_abs_residual": 1.4162698791508888e-12,
          "fd_vs_closed_form_relative": 9.368118566448734e-12,
          "pass": true
        }
      ]
    },
    {
      "name": "l3_block2_mean_value_form",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 2: solve C_h(pi_bar) = 1/4 pi_bar^2 h''(zeta) for zeta by bisection on (0, pi_bar) using the closed-form h'' = 2p' + pi p''; C_h < 0 and h''(zeta) < 0 at every grid point; zeta/pi_bar -> 1/2 as pi_bar falls",
      "tol": 1e-14,
      "max_residual": 3.469446951953614e-18,
      "zeta_over_pi_bar_at_smallest": 0.5000052712172776,
      "rows": [
        {
          "pi_bar": 0.0001,
          "C_h": -4.3827679861523604e-11,
          "C_h_negative": true,
          "zeta": 5.000052712172776e-05,
          "zeta_over_pi_bar": 0.5000052712172776,
          "h2_at_zeta": -0.01753107194460944,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 0.0002,
          "C_h": -1.7534296776577744e-10,
          "C_h_negative": true,
          "zeta": 0.00010000237549840704,
          "zeta_over_pi_bar": 0.5000118774920351,
          "h2_at_zeta": -0.01753429677657775,
          "residual": 7.754818242684634e-26,
          "root_found": true
        },
        {
          "pi_bar": 0.0005,
          "C_h": -1.0964984031424513e-09,
          "C_h_negative": true,
          "zeta": 0.00025001473922943185,
          "zeta_over_pi_bar": 0.5000294784588637,
          "h2_at_zeta": -0.017543974450279224,
          "residual": 2.0679515313825692e-25,
          "root_found": true
        },
        {
          "pi_bar": 0.001,
          "C_h": -4.390028639873408e-09,
          "C_h_negative": true,
          "zeta": 0.0005000589356637158,
          "zeta_over_pi_bar": 0.5000589356637158,
          "h2_at_zeta": -0.017560114559493634,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 0.002,
          "C_h": -1.759243475289024e-08,
          "C_h_negative": true,
          "zeta": 0.0010002356342172557,
          "zeta_over_pi_bar": 0.5001178171086278,
          "h2_at_zeta": -0.017592434752890237,
          "residual": 3.308722450212111e-24,
          "root_found": true
        },
        {
          "pi_bar": 0.005,
          "C_h": -1.1056072368557934e-07,
          "C_h_negative": true,
          "zeta": 0.0025014711196699553,
          "zeta_over_pi_bar": 0.500294223933991,
          "h2_at_zeta": -0.017689715789692695,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 0.01,
          "C_h": -4.4632308469384763e-07,
          "C_h_negative": true,
          "zeta": 0.005005873912400767,
          "zeta_over_pi_bar": 0.5005873912400767,
          "h2_at_zeta": -0.017852923387753905,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 0.02,
          "C_h": -1.8183393350537647e-06,
          "C_h_negative": true,
          "zeta": 0.010023411115236478,
          "zeta_over_pi_bar": 0.5011705557618239,
          "h2_at_zeta": -0.01818339335053765,
          "residual": 4.235164736271502e-22,
          "root_found": true
        },
        {
          "pi_bar": 0.05,
          "C_h": -1.200493935168273e-05,
          "C_h_negative": true,
          "zeta": 0.025144738159449502,
          "zeta_over_pi_bar": 0.50289476318899,
          "h2_at_zeta": -0.01920790296269238,
          "residual": 8.470329472543003e-21,
          "root_found": true
        },
        {
          "pi_bar": 0.1,
          "C_h": -5.257561485223772e-05,
          "C_h_negative": true,
          "zeta": 0.05056845994397926,
          "zeta_over_pi_bar": 0.5056845994397926,
          "h2_at_zeta": -0.021030245940895087,
          "residual": 1.3552527156068805e-20,
          "root_found": true
        },
        {
          "pi_bar": 0.2,
          "C_h": -0.0002514045509238727,
          "C_h_negative": true,
          "zeta": 0.102190653549664,
          "zeta_over_pi_bar": 0.51095326774832,
          "h2_at_zeta": -0.025140455092387267,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 0.5,
          "C_h": -0.002621649795169545,
          "C_h_negative": true,
          "zeta": 0.2621698873803735,
          "zeta_over_pi_bar": 0.524339774760747,
          "h2_at_zeta": -0.04194639672271272,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 0.9,
          "C_h": -0.015818231822929407,
          "C_h_negative": true,
          "zeta": 0.48312107277909,
          "zeta_over_pi_bar": 0.5368011919767667,
          "h2_at_zeta": -0.07811472505150324,
          "residual": 0.0,
          "root_found": true
        },
        {
          "pi_bar": 1.0,
          "C_h": -0.022547549753707208,
          "C_h_negative": true,
          "zeta": 0.5389914214735335,
          "zeta_over_pi_bar": 0.5389914214735335,
          "h2_at_zeta": -0.09019019901482885,
          "residual": 3.469446951953614e-18,
          "root_found": true
        }
      ]
    },
    {
      "name": "l3_block3_quadratic_rate",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 3: C_h/pi_bar^2 vs 1/4 h''(0); negative throughout; the two smallest pi_bar within 5%; the ratio within 2% at pi_bar <= 1e-3",
      "quarter_h2_0": -0.004381961913514803,
      "predicted_quarter_h2_0": -0.00438,
      "spread_two_smallest": 0.0001839495028308555,
      "tol_spread": 0.05,
      "max_abs_ratio_minus_1_at_pi_bar_le_1e-3": 0.0018408937635276956,
      "tol_ratio": 0.02,
      "C_h_at_1e-2": -4.4632308469384763e-07,
      "predicted_C_h_at_1e-2": -4.4e-07,
      "rows": [
        {
          "pi_bar": 0.0001,
          "C_h": -4.3827679861523604e-11,
          "C_h_over_pi_bar2": -0.00438276798615236,
          "ratio_to_quarter_h2_0": 1.0001839524517708
        },
        {
          "pi_bar": 0.0002,
          "C_h": -1.7534296776577744e-10,
          "C_h_over_pi_bar2": -0.004383574194144436,
          "ratio_to_quarter_h2_0": 1.0003679357925637
        },
        {
          "pi_bar": 0.0005,
          "C_h": -1.0964984031424513e-09,
          "C_h_over_pi_bar2": -0.004385993612569805,
          "ratio_to_quarter_h2_0": 1.0009200671148162
        },
        {
          "pi_bar": 0.001,
          "C_h": -4.390028639873408e-09,
          "C_h_over_pi_bar2": -0.004390028639873408,
          "ratio_to_quarter_h2_0": 1.0018408937635277
        },
        {
          "pi_bar": 0.002,
          "C_h": -1.759243475289024e-08,
          "C_h_over_pi_bar2": -0.00439810868822256,
          "ratio_to_quarter_h2_0": 1.0036848277156305
        },
        {
          "pi_bar": 0.005,
          "C_h": -1.1056072368557934e-07,
          "C_h_over_pi_bar2": -0.004422428947423174,
          "ratio_to_quarter_h2_0": 1.0092349122851942
        },
        {
          "pi_bar": 0.01,
          "C_h": -4.4632308469384763e-07,
          "C_h_over_pi_bar2": -0.004463230846938476,
          "ratio_to_quarter_h2_0": 1.0185462436752415
        },
        {
          "pi_bar": 0.02,
          "C_h": -1.8183393350537647e-06,
          "C_h_over_pi_bar2": -0.004545848337634412,
          "ratio_to_quarter_h2_0": 1.0374002392887423
        },
        {
          "pi_bar": 0.05,
          "C_h": -1.200493935168273e-05,
          "C_h_over_pi_bar2": -0.004801975740673091,
          "ratio_to_quarter_h2_0": 1.0958506339050749
        },
        {
          "pi_bar": 0.1,
          "C_h": -5.257561485223772e-05,
          "C_h_over_pi_bar2": -0.005257561485223771,
          "ratio_to_quarter_h2_0": 1.1998190739651233
        },
        {
          "pi_bar": 0.2,
          "C_h": -0.0002514045509238727,
          "C_h_over_pi_bar2": -0.006285113773096817,
          "ratio_to_quarter_h2_0": 1.4343150162287654
        },
        {
          "pi_bar": 0.5,
          "C_h": -0.002621649795169545,
          "C_h_over_pi_bar2": -0.01048659918067818,
          "ratio_to_quarter_h2_0": 2.393128782871324
        },
        {
          "pi_bar": 0.9,
          "C_h": -0.015818231822929407,
          "C_h_over_pi_bar2": -0.01952868126287581,
          "ratio_to_quarter_h2_0": 4.456606800402725
        },
        {
          "pi_bar": 1.0,
          "C_h": -0.022547549753707208,
          "C_h_over_pi_bar2": -0.022547549753707208,
          "ratio_to_quarter_h2_0": 5.1455375922292435
        }
      ]
    },
    {
      "name": "l3_block3b_model_kernel_rate",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "the ticket-28 line: |C_h|/pi_bar^2 stabilising on the MODEL kernel (h = pi p with P at the inner fixed point); the smoke run reports 0.2219",
      "smoke_reference": 0.2219,
      "spread_two_smallest": 0.00037391024357924556,
      "tol_spread": 0.05,
      "headroom_note": "cancellation headroom eps*max|h| is ~7 orders below |C_h| at every node, so the chord is resolved, not noise",
      "rows": [
        {
          "pi_bar": 0.1,
          "C_h": -0.0021319302660065542,
          "abs_C_h_over_pi_bar2": 0.2131930266006554,
          "cancellation_headroom": 1.150897093119653e-17,
          "C_h_le_0": true
        },
        {
          "pi_bar": 0.01,
          "C_h": -2.2096744831689476e-05,
          "abs_C_h_over_pi_bar2": 0.22096744831689474,
          "cancellation_headroom": 1.2370125646420936e-18,
          "C_h_le_0": true
        },
        {
          "pi_bar": 0.001,
          "C_h": -2.2179167349337288e-07,
          "abs_C_h_over_pi_bar2": 0.2217916734933729,
          "cancellation_headroom": 1.24585394140732e-19,
          "C_h_le_0": true
        },
        {
          "pi_bar": 0.0001,
          "C_h": -2.2187463469207466e-09,
          "abs_C_h_over_pi_bar2": 0.22187463469207466,
          "cancellation_headroom": 1.2467404972366732e-20,
          "C_h_le_0": true
        }
      ]
    },
    {
      "name": "l3_block4_affine_kernel_zero_chord",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 4: the C_h = 0 case CONSTRUCTED (affine kernel h = 0.5 pi), not searched for; range of E_kappa[h] across the kappa grid below 1e-14",
      "tol": 1e-14,
      "max_abs_C_h": 0.0,
      "range_E_over_kappa": 0.0,
      "max_abs_dE_dkappa": 0.0,
      "reading": "a nonzero range would refute Step 8 or the Step 16 weight algebra, not the kernel",
      "rows": [
        {
          "pi_bar": 0.0001,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.0002,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.0005,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.001,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.002,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.005,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.01,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.02,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.05,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.1,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.2,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.5,
          "C_h": 0.0
        },
        {
          "pi_bar": 0.9,
          "C_h": 0.0
        },
        {
          "pi_bar": 1.0,
          "C_h": 0.0
        }
      ]
    },
    {
      "name": "l3_block5a_tent_kernel_no_root",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 5(a), REFUTATION TEST: tent kernel at pi_bar = 1 must give C_h(1) = -1 and NO root zeta of C_h = 1/4 h''(zeta) on (0,1) \\ {1/2}",
      "C_h_1": -1.0,
      "predicted": -1.0,
      "n_candidate_zeta": 0,
      "n_points_searched": 200000,
      "reading": "Hypothesis 4's twice-differentiability on the open interval is not decoration; a script reporting a root here has a bug"
    },
    {
      "name": "l3_block5b_exampleB_gap",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 5(b), REFUTATION TEST: Example B at rho = 0.5 -- four distinct posteriors, pi_- strictly increasing and pi_+ strictly decreasing in kappa, and a NONZERO gap between the direct d_kappa E_kappa[h] and A'_kappa C_h(pi_bar) for any scalar A'_kappa fitted to the two end weights",
      "n_atoms": 4,
      "pi_minus_strictly_increasing": true,
      "pi_plus_strictly_decreasing": true,
      "pi_minus_range": [
        0.025641025641025644,
        0.9047619047619047
      ],
      "pi_plus_range": [
        0.09523809523809532,
        0.9743589743589743
      ],
      "A_prime_fitted_from_end_weights": 0.25,
      "C_h_1": -0.022547549753707208,
      "min_abs_gap": 0.0011270146854044094,
      "max_abs_gap": 0.03221992163799295,
      "reading": "confirms A(tau) is a restriction with content and that the frozen manuscript's own no-disclosure structure lies outside it. A zero gap here would be the bug."
    },
    {
      "name": "l3_block5c_unbounded_h2_witness",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "WHERE IT FAILS 3 / rederivation N5, REFUTATION TEST: h(pi) = 0.19766 pi + pi^{3/2}. C_h must be POSITIVE (A(tau)'s maintained orientation fails) and C_h/pi_bar^2 must diverge",
      "C_h_positive_everywhere": true,
      "C_h_over_pi_bar2_diverging": true,
      "closed_form": "C_h = (1 - 2^{-1/2}) pi_bar^{3/2} = 0.29289 pi_bar^{3/2}",
      "rows": [
        {
          "pi_bar": 0.4,
          "C_h": 0.07409677461348718,
          "C_h_over_pi_bar2": 0.4631048413342948,
          "C_h_over_pi_bar1p5": 0.2928932188134525
        },
        {
          "pi_bar": 0.2,
          "C_h": 0.02619716589662402,
          "C_h_over_pi_bar2": 0.6549291474156004,
          "C_h_over_pi_bar1p5": 0.29289321881345265
        },
        {
          "pi_bar": 0.1,
          "C_h": 0.009262096826685898,
          "C_h_over_pi_bar2": 0.9262096826685896,
          "C_h_over_pi_bar1p5": 0.2928932188134525
        },
        {
          "pi_bar": 0.01,
          "C_h": 0.0002928932188134524,
          "C_h_over_pi_bar2": 2.928932188134524,
          "C_h_over_pi_bar1p5": 0.29289321881345237
        },
        {
          "pi_bar": 0.001,
          "C_h": 9.26209682668589e-06,
          "C_h_over_pi_bar2": 9.262096826685891,
          "C_h_over_pi_bar1p5": 0.29289321881345226
        }
      ]
    }
  ],
  "n_fail": 0,
  "n_vacuous": 0,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "b4482d7fee83a8e8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/proofs/L3_proof.md, NUMERICAL CHECK REQUEST (five blocks); design section 8 split",
    "tolerance_amendment": "tolerance amended per design review 2026-08-21: relative criterion residual/|C_h| < 1e-6 for the standalone chord route (pi_bar < 1e-2); absolute 1e-10 retained on the full-model route (pi_bar >= 1e-2); smallest pi_bar stays 1e-4"
  },
  "grid": {
    "kappa": [
      0.05,
      0.1,
      0.15,
      0.2,
      0.25,
      0.3,
      0.35,
      0.4,
      0.45,
      0.5,
      0.55,
      0.6,
      0.65,
      0.7,
      0.75,
      0.8,
      0.85,
      0.9,
      0.95
    ],
    "pi_bar": [
      0.0001,
      0.0002,
      0.0005,
      0.001,
      0.002,
      0.005,
      0.01,
      0.02,
      0.05,
      0.1,
      0.2,
      0.5,
      0.9,
      1.0
    ],
    "tau": "not applicable -- L3 is a within-pooled-cell statement at fixed (tau, T); the pooled law is supplied by Examples A / A' / B",
    "T": "not applicable",
    "H": 10,
    "M": 2,
    "tau_frozen_from": "not applicable",
    "central_difference_step": 1e-05,
    "split_at_pi_bar": 0.01
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "discarded_mass": 0.0,
    "note": "L3 runs on the three- and four-atom analytic laws and on the standalone chord module; it does not enumerate histories, so these counts are the package's, quoted for provenance only"
  },
  "degenerate_nodes": [],
  "multiple_root_nodes": 0,
  "seconds": 0.06474208401050419,
  "all_pass": true
}
```

### FILE: quality_reports/fixes/t2_l4_check.json

```json
{
  "checks": [
    {
      "name": "l4_sign_Omega_up",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Omega(tau') - Omega(tau) >= 0 at every tightening step, every kappa and both T",
      "n_steps": 16,
      "n_violations": 0,
      "violations": [],
      "min_d_Omega": 0.022633267058852102
    },
    {
      "name": "l4_sign_pi_bar_down",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "pi_bar_pr(tau') - pi_bar_pr(tau) <= 0 at every tightening step",
      "n_steps": 16,
      "n_violations": 0,
      "violations": [],
      "max_d_pi_bar_pr": -0.018765572006326142
    },
    {
      "name": "l4_sign_S_P_down",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "S_P(tau') - S_P(tau) <= 0 at every tightening step, with S_P = Delta_m |A'_kappa| |C_h(pi_bar)| -- the request's own formula, which is the chord route",
      "n_steps": 16,
      "n_violations": 0,
      "violations": [],
      "max_d_S_P_chord": -9.471395101699196e-05,
      "note": "a single violation would be a failed hypothesis, not sampling error: there is no sampling in this computation"
    },
    {
      "name": "l4_pred1_step11_identity",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "prediction 1: |pi_bar_pr(tau) - [(1-nu/rho_P) pi_bar_pr(tau') + nu/rho_P]| < 1e-12; machine precision is the right tolerance because nothing here is approximated",
      "tol": 1e-12,
      "max_residual": 1.249000902703301e-16,
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.9,
          "nu": 0.022633267058852626,
          "rho_P": 0.9773667329411471,
          "residual": 5.551115123125783e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.8,
          "nu": 0.02263326705885306,
          "rho_P": 0.9547334658822945,
          "residual": 2.7755575615628914e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.7000000000000001,
          "nu": 0.022633267058852963,
          "rho_P": 0.9321001988234414,
          "residual": 8.326672684688674e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.6000000000000001,
          "nu": 0.022633267058853143,
          "rho_P": 0.9094669317645884,
          "residual": 8.326672684688674e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "nu": 0.02263326705885267,
          "rho_P": 0.8868336647057352,
          "residual": 8.326672684688674e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.4,
          "nu": 0.02263326705885324,
          "rho_P": 0.8642003976468826,
          "residual": 5.551115123125783e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.30000000000000004,
          "nu": 0.022633267058852602,
          "rho_P": 0.8415671305880293,
          "residual": 1.249000902703301e-16
        },
        {
          "T": 5,
          "tau_quantile": 0.2,
          "nu": 0.02263326705885288,
          "rho_P": 0.8189338635291767,
          "residual": 1.0408340855860843e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "nu": 0.02263326705885229,
          "rho_P": 0.9773667329411471,
          "residual": 2.7755575615628914e-17
        },
        {
          "T": 10,
          "tau_quantile": 0.8,
          "nu": 0.022633267058853386,
          "rho_P": 0.9547334658822948,
          "residual": 0.0
        },
        {
          "T": 10,
          "tau_quantile": 0.7000000000000001,
          "nu": 0.022633267058852963,
          "rho_P": 0.9321001988234414,
          "residual": 2.7755575615628914e-17
        },
        {
          "T": 10,
          "tau_quantile": 0.6000000000000001,
          "nu": 0.02263326705885313,
          "rho_P": 0.9094669317645884,
          "residual": 5.551115123125783e-17
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "nu": 0.022633267058852644,
          "rho_P": 0.8868336647057353,
          "residual": 2.7755575615628914e-17
        },
        {
          "T": 10,
          "tau_quantile": 0.4,
          "nu": 0.022633267058853268,
          "rho_P": 0.8642003976468826,
          "residual": 1.3877787807814457e-17
        },
        {
          "T": 10,
          "tau_quantile": 0.30000000000000004,
          "nu": 0.022633267058852102,
          "rho_P": 0.8415671305880293,
          "residual": 2.7755575615628914e-17
        },
        {
          "T": 10,
          "tau_quantile": 0.2,
          "nu": 0.022633267058853324,
          "rho_P": 0.8189338635291773,
          "residual": 9.71445146547012e-17
        }
      ]
    },
    {
      "name": "l4_pred2_flat_in_kappa",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "prediction 2: max_kappa |Omega(tau,T,kappa) - Omega(tau,T,0.5)| < 1e-12, and the same for pi_bar_pr. A residual above 1e-8 would mean the execution path is reading realised order flow, i.e. the no-feedback timing has been violated in the code",
      "tol": 1e-12,
      "max_flat_residual": {
        "Omega": 0.0,
        "pi_bar_pr": 0.0
      },
      "n_kappa_nodes": 71
    },
    {
      "name": "l4_pred3_tau_grid_bites",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "prediction 3: omega_a(tau_p) = Pr(B >= tau_p | a=1) should run from ~0.9 at the 10th percentile to ~0.1 at the 90th; deviation above 0.02 at any decile means the grid is not the percentile grid it claims to be",
      "tol": 0.02,
      "max_deviation": 2.4980018054066022e-15,
      "Omega_span_ratio": {
        "T=5": 8.99999999999998,
        "T=10": 8.999999999999979
      },
      "predicted_span": "roughly ninefold",
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.1,
          "omega_a": 0.8999999999999997,
          "predicted": 0.9,
          "deviation": 3.3306690738754696e-16
        },
        {
          "T": 5,
          "tau_quantile": 0.2,
          "omega_a": 0.7999999999999997,
          "predicted": 0.8,
          "deviation": 3.3306690738754696e-16
        },
        {
          "T": 5,
          "tau_quantile": 0.30000000000000004,
          "omega_a": 0.7000000000000014,
          "predicted": 0.7,
          "deviation": 1.4432899320127035e-15
        },
        {
          "T": 5,
          "tau_quantile": 0.4,
          "omega_a": 0.5999999999999998,
          "predicted": 0.6,
          "deviation": 2.220446049250313e-16
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "omega_a": 0.5000000000000009,
          "predicted": 0.5,
          "deviation": 8.881784197001252e-16
        },
        {
          "T": 5,
          "tau_quantile": 0.6000000000000001,
          "omega_a": 0.39999999999999986,
          "predicted": 0.3999999999999999,
          "deviation": 5.551115123125783e-17
        },
        {
          "T": 5,
          "tau_quantile": 0.7000000000000001,
          "omega_a": 0.29999999999999966,
          "predicted": 0.29999999999999993,
          "deviation": 2.7755575615628914e-16
        },
        {
          "T": 5,
          "tau_quantile": 0.8,
          "omega_a": 0.19999999999999893,
          "predicted": 0.19999999999999996,
          "deviation": 1.0269562977782698e-15
        },
        {
          "T": 5,
          "tau_quantile": 0.9,
          "omega_a": 0.10000000000000021,
          "predicted": 0.09999999999999998,
          "deviation": 2.3592239273284576e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.1,
          "omega_a": 0.8999999999999997,
          "predicted": 0.9,
          "deviation": 3.3306690738754696e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.2,
          "omega_a": 0.7999999999999977,
          "predicted": 0.8,
          "deviation": 2.3314683517128287e-15
        },
        {
          "T": 10,
          "tau_quantile": 0.30000000000000004,
          "omega_a": 0.7000000000000015,
          "predicted": 0.7,
          "deviation": 1.5543122344752192e-15
        },
        {
          "T": 10,
          "tau_quantile": 0.4,
          "omega_a": 0.5999999999999998,
          "predicted": 0.6,
          "deviation": 2.220446049250313e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "omega_a": 0.500000000000001,
          "predicted": 0.5,
          "deviation": 9.992007221626409e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.6000000000000001,
          "omega_a": 0.3999999999999998,
          "predicted": 0.3999999999999999,
          "deviation": 1.1102230246251565e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.7000000000000001,
          "omega_a": 0.29999999999999966,
          "predicted": 0.29999999999999993,
          "deviation": 2.7755575615628914e-16
        },
        {
          "T": 10,
          "tau_quantile": 0.8,
          "omega_a": 0.19999999999999746,
          "predicted": 0.19999999999999996,
          "deviation": 2.4980018054066022e-15
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "omega_a": 0.10000000000000021,
          "predicted": 0.09999999999999998,
          "deviation": 2.3592239273284576e-16
        }
      ]
    },
    {
      "name": "l4_pred4_quadratic_corollary",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "prediction 4 (L3's quadratic corollary): at the two smallest pi_bar points, S_P/pi_bar^2 should agree within 5%. If this fails while 1-3 pass, the failure is in h's regularity, not in L4",
      "tol": 0.05,
      "by_T": {
        "T=5": {
          "pi_bar_two_smallest": [
            0.05684603819004282,
            0.11054991406175543
          ],
          "S_P_over_pi_bar2": [
            0.010841150112949574,
            0.010616464685766649
          ],
          "relative_gap": 0.020725239005273247
        },
        "T=10": {
          "pi_bar_two_smallest": [
            0.05684603819004281,
            0.11054991406175642
          ],
          "S_P_over_pi_bar2": [
            0.010841150112949635,
            0.010616464685766661
          ],
          "relative_gap": 0.020725239005277608
        }
      }
    },
    {
      "name": "l4_pred5_A_prime_kappa_channel",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "prediction 5: under the equality version of (br-iii), C_tau = S_P(tau')/S_P(tau) should equal |C_h(pi_bar(tau'))|/|C_h(pi_bar(tau))|. REPORT THE RESIDUAL AS A NUMBER, NOT PASS/FAIL: it IS the size of the A'_kappa channel -- how much of the composition effect comes from the pooled weights reshaping rather than from the chord shortening, and it is what T1's C_tau inherits",
      "verdict": "REPORTED, not gated -- the request forbids a pass/fail here",
      "C_tau_uses": "the MODEL route S_P = |d_kappa M_P| at kappa = 0.5; the chord ratio is the request's closed form. On the chord route the two coincide by construction, so the model route is the only one that can measure the channel",
      "median_abs_residual": 0.035197279978000706,
      "max_abs_residual": 0.121292279856974,
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.9,
          "tau_prime_quantile": 0.8,
          "C_tau_model": 0.8553419852440902,
          "chord_ratio": 0.8392979663206694,
          "residual": 0.016044018923420778,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.8,
          "tau_prime_quantile": 0.7000000000000001,
          "C_tau_model": 0.7354278799179113,
          "chord_ratio": 0.8147172733269992,
          "residual": 0.07928939340908792,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.7000000000000001,
          "tau_prime_quantile": 0.6000000000000001,
          "C_tau_model": 0.7811335712876109,
          "chord_ratio": 0.7832996695002818,
          "residual": 0.002166098212670997,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.6000000000000001,
          "tau_prime_quantile": 0.5,
          "C_tau_model": 0.774420523738143,
          "chord_ratio": 0.7419282938872818,
          "residual": 0.0324922298508612,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "tau_prime_quantile": 0.4,
          "C_tau_model": 0.6091562322853169,
          "chord_ratio": 0.6853210135486675,
          "residual": 0.07616478126335058,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.4,
          "tau_prime_quantile": 0.30000000000000004,
          "C_tau_model": 0.6007852102287234,
          "chord_ratio": 0.6038547692068341,
          "residual": 0.003069558978110676,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.30000000000000004,
          "tau_prime_quantile": 0.2,
          "C_tau_model": 0.44056956578555345,
          "chord_ratio": 0.4784718958906557,
          "residual": 0.037902330105102244,
          "S_P_model_undefined": false
        },
        {
          "T": 5,
          "tau_quantile": 0.2,
          "tau_prime_quantile": 0.1,
          "C_tau_model": 0.14871720786079773,
          "chord_ratio": 0.2700094877177717,
          "residual": 0.121292279856974,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "tau_prime_quantile": 0.8,
          "C_tau_model": 0.8553419852440679,
          "chord_ratio": 0.8392979663206693,
          "residual": 0.016044018923398573,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.8,
          "tau_prime_quantile": 0.7000000000000001,
          "C_tau_model": 0.7354278799179435,
          "chord_ratio": 0.814717273327,
          "residual": 0.0792893934090565,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.7000000000000001,
          "tau_prime_quantile": 0.6000000000000001,
          "C_tau_model": 0.7811335712877209,
          "chord_ratio": 0.7832996695002843,
          "residual": 0.0021660982125634165,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.6000000000000001,
          "tau_prime_quantile": 0.5,
          "C_tau_model": 0.7744205237381786,
          "chord_ratio": 0.7419282938872794,
          "residual": 0.03249222985089917,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "tau_prime_quantile": 0.4,
          "C_tau_model": 0.6091562322847248,
          "chord_ratio": 0.6853210135486675,
          "residual": 0.07616478126394266,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.4,
          "tau_prime_quantile": 0.30000000000000004,
          "C_tau_model": 0.6007852102288728,
          "chord_ratio": 0.6038547692068341,
          "residual": 0.003069558977961351,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.30000000000000004,
          "tau_prime_quantile": 0.2,
          "C_tau_model": 0.4405695657832671,
          "chord_ratio": 0.47847189589066463,
          "residual": 0.03790233010739752,
          "S_P_model_undefined": false
        },
        {
          "T": 10,
          "tau_quantile": 0.2,
          "tau_prime_quantile": 0.1,
          "C_tau_model": 0.14871720786155607,
          "chord_ratio": 0.270009487717768,
          "residual": 0.12129227985621194,
          "S_P_model_undefined": false
        }
      ]
    },
    {
      "name": "l4_model_route_S_P",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "the model route reported beside the request's chord formula, so the two are never conflated",
      "verdict": "REPORTED, not gated",
      "n_sign_violations_model_route": 0,
      "violations_model_route": [],
      "reading": "S_P = |d_kappa M_P| is measured at kappa = 0.5, which on this calibration sits within 0.05 of the peak of the hump-shaped M_P(kappa) profile, so the model-route level is small and its tau-ordering is not the chord route's. The request's verdict binds on the chord formula it writes down; this column is the diagnostic that shows the two are different objects."
    },
    {
      "name": "l4_H12_robustness",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "design section 13, ruling 2: H = 12 robustness, cheap for L4",
      "scope": "Omega, omega_a, pi_bar_pr and the chord-route S_P -- none of which touch the pooled enumeration",
      "not_evaluable_at_H12": "the model route S_P = |d_kappa M_P| runs through the enumeration; at H = 12 the feasible history count is 8,503,056 and 8,503,056 x N_theta 14 = 1.19e8 exceeds the design build-step-4 gate of 1e8 (~2.5 GB working set). The gate is respected.",
      "policy": "cutoffs frozen at the H = 10 baseline equilibrium; H = 12 cannot be re-solved for the same reason",
      "n_sign_violations": 0,
      "violations": [],
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.1,
          "tau": 0.07586332924848985,
          "Omega": 0.20369940352967594,
          "omega_a": 0.8999999999999988,
          "pi_bar_pr": 0.028423019095021682,
          "S_P_chord": 3.50328736655376e-05,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.2,
          "tau": 0.08206662693528996,
          "Omega": 0.18106613647082348,
          "omega_a": 0.8000000000000008,
          "pi_bar_pr": 0.055274957030877425,
          "S_P_chord": 0.00012974682468252992,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.30000000000000004,
          "tau": 0.0897601074265302,
          "Omega": 0.15843286941197068,
          "omega_a": 0.7000000000000014,
          "pi_bar_pr": 0.08068257267737478,
          "S_P_chord": 0.0002711691654135942,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.4,
          "tau": 0.09089137143817187,
          "Omega": 0.1357996023531174,
          "omega_a": 0.5999999999999998,
          "pi_bar_pr": 0.10475934572805422,
          "S_P_chord": 0.0004490635484584747,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "tau": 0.09197763253912061,
          "Omega": 0.11316633529426473,
          "omega_a": 0.5000000000000009,
          "pi_bar_pr": 0.127607171218308,
          "S_P_chord": 0.0006552601475521293,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.6000000000000001,
          "tau": 0.09303125238357923,
          "Omega": 0.09053306823541162,
          "omega_a": 0.3999999999999999,
          "pi_bar_pr": 0.1493178010217843,
          "S_P_chord": 0.0008831852794276673,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.7000000000000001,
          "tau": 0.09407139027595574,
          "Omega": 0.06789980117655864,
          "omega_a": 0.2999999999999996,
          "pi_bar_pr": 0.16997407533219594,
          "S_P_chord": 0.001127519024731756,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.8,
          "tau": 0.09513374043270158,
          "Omega": 0.04526653411770558,
          "omega_a": 0.19999999999999896,
          "pi_bar_pr": 0.18965097898133854,
          "S_P_chord": 0.0013839390198852565,
          "degenerate": []
        },
        {
          "T": 5,
          "tau_quantile": 0.9,
          "tau": 0.09631173355658933,
          "Omega": 0.022633267058852952,
          "omega_a": 0.1000000000000002,
          "pi_bar_pr": 0.208416550987665,
          "S_P_chord": 0.0016489245481580218,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.1,
          "tau": 0.047198748468183685,
          "Omega": 0.20369940352967617,
          "omega_a": 0.8999999999999999,
          "pi_bar_pr": 0.028423019095021415,
          "S_P_chord": 3.5032873665537254e-05,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.2,
          "tau": 0.049524985100733734,
          "Omega": 0.1810661364708234,
          "omega_a": 0.8000000000000006,
          "pi_bar_pr": 0.055274957030877425,
          "S_P_chord": 0.00012974682468252992,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.30000000000000004,
          "tau": 0.052410040284948826,
          "Omega": 0.15843286941197068,
          "omega_a": 0.7000000000000014,
          "pi_bar_pr": 0.08068257267737475,
          "S_P_chord": 0.0002711691654135942,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.4,
          "tau": 0.056096302044930796,
          "Omega": 0.1357996023531177,
          "omega_a": 0.6000000000000011,
          "pi_bar_pr": 0.10475934572805386,
          "S_P_chord": 0.0004490635484584712,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "tau": 0.060988816269560306,
          "Omega": 0.11316633529426477,
          "omega_a": 0.500000000000001,
          "pi_bar_pr": 0.127607171218308,
          "S_P_chord": 0.0006552601475521293,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.6000000000000001,
          "tau": 0.061515626191789616,
          "Omega": 0.09053306823541159,
          "omega_a": 0.39999999999999974,
          "pi_bar_pr": 0.1493178010217843,
          "S_P_chord": 0.0008831852794276673,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.7000000000000001,
          "tau": 0.06844283416557344,
          "Omega": 0.06789980117655899,
          "omega_a": 0.30000000000000115,
          "pi_bar_pr": 0.16997407533219566,
          "S_P_chord": 0.001127519024731756,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.8,
          "tau": 0.07885030532452618,
          "Omega": 0.04526653411770558,
          "omega_a": 0.19999999999999896,
          "pi_bar_pr": 0.18965097898133856,
          "S_P_chord": 0.0013839390198852565,
          "degenerate": []
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "tau": 0.09631173355658933,
          "Omega": 0.022633267058852952,
          "omega_a": 0.1000000000000002,
          "pi_bar_pr": 0.208416550987665,
          "S_P_chord": 0.0016489245481580218,
          "degenerate": []
        }
      ]
    }
  ],
  "n_fail": 0,
  "n_vacuous": 0,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "8ef7c5c2d3896bf8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/proofs/L4_proof.md, NUMERICAL CHECK REQUEST; L4_rederivation.md",
    "frozen_inputs": "k and B_j(s,.) solved once at the reference threshold tau_50 and held fixed across the entire tau grid, per the request's Frozen inputs clause"
  },
  "grid": {
    "kappa": [
      0.15,
      0.16,
      0.17,
      0.18,
      0.19,
      0.2,
      0.21,
      0.22,
      0.23,
      0.24,
      0.25,
      0.26,
      0.27,
      0.28,
      0.29,
      0.3,
      0.31,
      0.32,
      0.33,
      0.34,
      0.35,
      0.36,
      0.37,
      0.38,
      0.39,
      0.4,
      0.41,
      0.42,
      0.43,
      0.44,
      0.45,
      0.46,
      0.47,
      0.48,
      0.49,
      0.5,
      0.51,
      0.52,
      0.53,
      0.54,
      0.55,
      0.56,
      0.57,
      0.58,
      0.59,
      0.6,
      0.61,
      0.62,
      0.63,
      0.64,
      0.65,
      0.66,
      0.67,
      0.68,
      0.69,
      0.7,
      0.71,
      0.72,
      0.73,
      0.74,
      0.75,
      0.76,
      0.77,
      0.78,
      0.79,
      0.8,
      0.81,
      0.82,
      0.83,
      0.84,
      0.85
    ],
    "kappa_for_model_route": [
      0.25,
      0.5,
      0.75
    ],
    "tau": {
      "T=5": [
        0.07299687117045922,
        0.07393121647665091,
        0.08122294922274018,
        0.09089137143817187,
        0.09197763253912061,
        0.09303125238357923,
        0.09407139027595574,
        0.09513374043270158,
        0.09631173355658933
      ],
      "T=10": [
        0.037166145195076536,
        0.037321869412775155,
        0.03853715820379003,
        0.04014856190636198,
        0.04032960542318677,
        0.042606250476715846,
        0.04601784756898893,
        0.0462834351081754,
        0.052103911185529775
      ]
    },
    "tau_quantiles": [
      0.1,
      0.2,
      0.30000000000000004,
      0.4,
      0.5,
      0.6000000000000001,
      0.7000000000000001,
      0.8,
      0.9
    ],
    "tau_definition": "deciles of B_{j(s)}(s, H-T) over Voice signals -- L4's own object, T-dependent",
    "T": [
      5,
      10
    ],
    "H": 10,
    "H_robustness": 12,
    "M": 2,
    "tau_frozen_from": "the baseline equilibrium at tau_50 = 0.09076406; policy frozen there",
    "A_prime_kappa": 0.25,
    "A_prime_kappa_source": "Example A of card section 4.4 / L3 Step 16: A_1 = A_0 = (2-kappa)/4, A_{1/2} = kappa/2, so A'_kappa = -1/4",
    "n_nodes": 1278
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "discarded_mass": 0.0
  },
  "degenerate_nodes": [],
  "multiple_root_nodes": 0,
  "node_table": [
    {
      "T": 5,
      "tau_quantile": 0.1,
      "tau": 0.07299687117045922,
      "corner": false,
      "Omega": 0.20369940352967614,
      "Pr_a": 0.22633267058852913,
      "omega_a": 0.8999999999999997,
      "pi_bar_pr": 0.02842301909502141,
      "pi_bar_level_symmetric": 0.05684603819004282,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.0007006574733107451,
      "abs_C_h": 0.0007006574733107451,
      "S_P_chord": 3.5032873665537254e-05,
      "S_P_chord_pp": 0.003503287366553725,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.000455251240516265,
        "kappa=0.5": 2.96580129724567e-05,
        "kappa=0.75": 0.00042249382830430684
      },
      "S_P_model_pp_at_kappa_0.5": 0.00296580129724567
    },
    {
      "T": 5,
      "tau_quantile": 0.2,
      "tau": 0.07393121647665091,
      "corner": false,
      "Omega": 0.18106613647082326,
      "Pr_a": 0.22633267058852916,
      "omega_a": 0.7999999999999997,
      "pi_bar_pr": 0.05527495703087772,
      "pi_bar_level_symmetric": 0.11054991406175543,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.0025949364936505848,
      "abs_C_h": 0.0025949364936505848,
      "S_P_chord": 0.00012974682468252922,
      "S_P_chord_pp": 0.012974682468252922,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0009274648425652958,
        "kappa=0.5": 0.00019942556345071508,
        "kappa=0.75": 0.0010313629800905984
      },
      "S_P_model_pp_at_kappa_0.5": 0.019942556345071506
    },
    {
      "T": 5,
      "tau_quantile": 0.30000000000000004,
      "tau": 0.08122294922274018,
      "corner": false,
      "Omega": 0.15843286941197066,
      "Pr_a": 0.22633267058852907,
      "omega_a": 0.7000000000000014,
      "pi_bar_pr": 0.08068257267737476,
      "pi_bar_level_symmetric": 0.16136514535474952,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.005423383308271884,
      "abs_C_h": 0.005423383308271884,
      "S_P_chord": 0.0002711691654135942,
      "S_P_chord_pp": 0.02711691654135942,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0014340629976518815,
        "kappa=0.5": 0.00045265397099123535,
        "kappa=0.75": 0.0017882768274080916
      },
      "S_P_model_pp_at_kappa_0.5": 0.045265397099123535
    },
    {
      "T": 5,
      "tau_quantile": 0.4,
      "tau": 0.09089137143817187,
      "corner": false,
      "Omega": 0.13579960235311742,
      "Pr_a": 0.2263326705885291,
      "omega_a": 0.5999999999999998,
      "pi_bar_pr": 0.10475934572805422,
      "pi_bar_level_symmetric": 0.20951869145610844,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.008981270969169494,
      "abs_C_h": 0.008981270969169494,
      "S_P_chord": 0.0004490635484584747,
      "S_P_chord_pp": 0.04490635484584747,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0020757970432046216,
        "kappa=0.5": 0.000753437273895119,
        "kappa=0.75": 0.002688389257085986
      },
      "S_P_model_pp_at_kappa_0.5": 0.0753437273895119
    },
    {
      "T": 5,
      "tau_quantile": 0.5,
      "tau": 0.09197763253912061,
      "corner": false,
      "Omega": 0.11316633529426474,
      "Pr_a": 0.2263326705885291,
      "omega_a": 0.5000000000000009,
      "pi_bar_pr": 0.127607171218308,
      "pi_bar_level_symmetric": 0.255214342436616,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.013105202951042588,
      "abs_C_h": 0.013105202951042588,
      "S_P_chord": 0.0006552601475521293,
      "S_P_chord_pp": 0.06552601475521293,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0027752827822195153,
        "kappa=0.5": 0.001236853920165137,
        "kappa=0.75": 0.0037652658069869645
      },
      "S_P_model_pp_at_kappa_0.5": 0.1236853920165137
    },
    {
      "T": 5,
      "tau_quantile": 0.6000000000000001,
      "tau": 0.09303125238357923,
      "corner": false,
      "Omega": 0.0905330682354116,
      "Pr_a": 0.2263326705885291,
      "omega_a": 0.39999999999999986,
      "pi_bar_pr": 0.14931780102178435,
      "pi_bar_level_symmetric": 0.2986356020435687,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.01766370558855329,
      "abs_C_h": 0.01766370558855329,
      "S_P_chord": 0.0008831852794276645,
      "S_P_chord_pp": 0.08831852794276644,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.003649920024506657,
        "kappa=0.5": 0.0015971347378486548,
        "kappa=0.75": 0.005079685628406147
      },
      "S_P_model_pp_at_kappa_0.5": 0.15971347378486547
    },
    {
      "T": 5,
      "tau_quantile": 0.7000000000000001,
      "tau": 0.09407139027595574,
      "corner": false,
      "Omega": 0.06789980117655864,
      "Pr_a": 0.22633267058852904,
      "omega_a": 0.29999999999999966,
      "pi_bar_pr": 0.16997407533219594,
      "pi_bar_level_symmetric": 0.3399481506643919,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.02255038049463512,
      "abs_C_h": 0.02255038049463512,
      "S_P_chord": 0.001127519024731756,
      "S_P_chord_pp": 0.1127519024731756,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.004862626747702971,
        "kappa=0.5": 0.0020446371741723477,
        "kappa=0.75": 0.006550721100592601
      },
      "S_P_model_pp_at_kappa_0.5": 0.20446371741723476
    },
    {
      "T": 5,
      "tau_quantile": 0.8,
      "tau": 0.09513374043270158,
      "corner": false,
      "Omega": 0.04526653411770558,
      "Pr_a": 0.2263326705885291,
      "omega_a": 0.19999999999999893,
      "pi_bar_pr": 0.18965097898133856,
      "pi_bar_level_symmetric": 0.3793019579626771,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.027678780397705133,
      "abs_C_h": 0.027678780397705133,
      "S_P_chord": 0.0013839390198852565,
      "S_P_chord_pp": 0.13839390198852564,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.006175482165796232,
        "kappa=0.5": 0.0027802007919533467,
        "kappa=0.75": 0.008255659079688737
      },
      "S_P_model_pp_at_kappa_0.5": 0.27802007919533467
    },
    {
      "T": 5,
      "tau_quantile": 0.9,
      "tau": 0.09631173355658933,
      "corner": false,
      "Omega": 0.022633267058852952,
      "Pr_a": 0.22633267058852904,
      "omega_a": 0.10000000000000021,
      "pi_bar_pr": 0.20841655098766498,
      "pi_bar_level_symmetric": 0.41683310197532997,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.03297849096316044,
      "abs_C_h": 0.03297849096316044,
      "S_P_chord": 0.0016489245481580218,
      "S_P_chord_pp": 0.16489245481580217,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.007271354342393273,
        "kappa=0.5": 0.003250396730098496,
        "kappa=0.75": 0.010085351285624496
      },
      "S_P_model_pp_at_kappa_0.5": 0.3250396730098496
    },
    {
      "T": 10,
      "tau_quantile": 0.1,
      "tau": 0.037166145195076536,
      "corner": true,
      "Omega": 0.20369940352967605,
      "Pr_a": 0.22633267058852902,
      "omega_a": 0.8999999999999997,
      "pi_bar_pr": 0.028423019095021405,
      "pi_bar_level_symmetric": 0.05684603819004281,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.0007006574733107486,
      "abs_C_h": 0.0007006574733107486,
      "S_P_chord": 3.503287366553743e-05,
      "S_P_chord_pp": 0.003503287366553743,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.000455251240516265,
        "kappa=0.5": 2.965801297243863e-05,
        "kappa=0.75": 0.0004224938283042346
      },
      "S_P_model_pp_at_kappa_0.5": 0.002965801297243863
    },
    {
      "T": 10,
      "tau_quantile": 0.2,
      "tau": 0.037321869412775155,
      "corner": true,
      "Omega": 0.18106613647082273,
      "Pr_a": 0.22633267058852904,
      "omega_a": 0.7999999999999977,
      "pi_bar_pr": 0.05527495703087821,
      "pi_bar_level_symmetric": 0.11054991406175642,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.0025949364936506333,
      "abs_C_h": 0.0025949364936506333,
      "S_P_chord": 0.00012974682468253166,
      "S_P_chord_pp": 0.012974682468253165,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0009274648425654042,
        "kappa=0.5": 0.00019942556344957666,
        "kappa=0.75": 0.0010313629800918632
      },
      "S_P_model_pp_at_kappa_0.5": 0.019942556344957667
    },
    {
      "T": 10,
      "tau_quantile": 0.30000000000000004,
      "tau": 0.03853715820379003,
      "corner": true,
      "Omega": 0.15843286941197063,
      "Pr_a": 0.226332670588529,
      "omega_a": 0.7000000000000015,
      "pi_bar_pr": 0.08068257267737478,
      "pi_bar_level_symmetric": 0.16136514535474955,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.005423383308271884,
      "abs_C_h": 0.005423383308271884,
      "S_P_chord": 0.0002711691654135942,
      "S_P_chord_pp": 0.02711691654135942,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0014340629976519177,
        "kappa=0.5": 0.00045265397099100046,
        "kappa=0.75": 0.0017882768274082542
      },
      "S_P_model_pp_at_kappa_0.5": 0.045265397099100046
    },
    {
      "T": 10,
      "tau_quantile": 0.4,
      "tau": 0.04014856190636198,
      "corner": true,
      "Omega": 0.13579960235311736,
      "Pr_a": 0.22633267058852904,
      "omega_a": 0.5999999999999998,
      "pi_bar_pr": 0.1047593457280542,
      "pi_bar_level_symmetric": 0.2095186914561084,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.008981270969169494,
      "abs_C_h": 0.008981270969169494,
      "S_P_chord": 0.0004490635484584747,
      "S_P_chord_pp": 0.04490635484584747,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0020757970432047843,
        "kappa=0.5": 0.0007534372738945408,
        "kappa=0.75": 0.0026883892570859678
      },
      "S_P_model_pp_at_kappa_0.5": 0.07534372738945408
    },
    {
      "T": 10,
      "tau_quantile": 0.5,
      "tau": 0.04032960542318677,
      "corner": true,
      "Omega": 0.11316633529426472,
      "Pr_a": 0.226332670588529,
      "omega_a": 0.500000000000001,
      "pi_bar_pr": 0.127607171218308,
      "pi_bar_level_symmetric": 0.255214342436616,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.013105202951042588,
      "abs_C_h": 0.013105202951042588,
      "S_P_chord": 0.0006552601475521293,
      "S_P_chord_pp": 0.06552601475521293,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0027752827822194793,
        "kappa=0.5": 0.0012368539201653898,
        "kappa=0.75": 0.003765265806986314
      },
      "S_P_model_pp_at_kappa_0.5": 0.12368539201653898
    },
    {
      "T": 10,
      "tau_quantile": 0.6000000000000001,
      "tau": 0.042606250476715846,
      "corner": true,
      "Omega": 0.09053306823541159,
      "Pr_a": 0.22633267058852907,
      "omega_a": 0.3999999999999998,
      "pi_bar_pr": 0.1493178010217843,
      "pi_bar_level_symmetric": 0.2986356020435686,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.017663705588553347,
      "abs_C_h": 0.017663705588553347,
      "S_P_chord": 0.0008831852794276673,
      "S_P_chord_pp": 0.08831852794276673,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0036499200245066208,
        "kappa=0.5": 0.001597134737848908,
        "kappa=0.75": 0.005079685628406074
      },
      "S_P_model_pp_at_kappa_0.5": 0.15971347378489079
    },
    {
      "T": 10,
      "tau_quantile": 0.7000000000000001,
      "tau": 0.04601784756898893,
      "corner": true,
      "Omega": 0.06789980117655862,
      "Pr_a": 0.226332670588529,
      "omega_a": 0.29999999999999966,
      "pi_bar_pr": 0.16997407533219594,
      "pi_bar_level_symmetric": 0.3399481506643919,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.02255038049463512,
      "abs_C_h": 0.02255038049463512,
      "S_P_chord": 0.001127519024731756,
      "S_P_chord_pp": 0.1127519024731756,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.004862626747703044,
        "kappa=0.5": 0.0020446371741723837,
        "kappa=0.75": 0.0065507211005926365
      },
      "S_P_model_pp_at_kappa_0.5": 0.20446371741723837
    },
    {
      "T": 10,
      "tau_quantile": 0.8,
      "tau": 0.0462834351081754,
      "corner": true,
      "Omega": 0.04526653411770524,
      "Pr_a": 0.22633267058852907,
      "omega_a": 0.19999999999999746,
      "pi_bar_pr": 0.1896509789813388,
      "pi_bar_level_symmetric": 0.3793019579626776,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.027678780397705105,
      "abs_C_h": 0.027678780397705105,
      "S_P_chord": 0.0013839390198852552,
      "S_P_chord_pp": 0.13839390198852553,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.006175482165796196,
        "kappa=0.5": 0.0027802007919532743,
        "kappa=0.75": 0.00825565907968787
      },
      "S_P_model_pp_at_kappa_0.5": 0.27802007919532745
    },
    {
      "T": 10,
      "tau_quantile": 0.9,
      "tau": 0.052103911185529775,
      "corner": true,
      "Omega": 0.02263326705885295,
      "Pr_a": 0.22633267058852902,
      "omega_a": 0.10000000000000021,
      "pi_bar_pr": 0.20841655098766496,
      "pi_bar_level_symmetric": 0.4168331019753299,
      "pi_bar_enumerated_support_max": {
        "kappa=0.25": 1.0,
        "kappa=0.5": 1.0,
        "kappa=0.75": 1.0
      },
      "C_h": -0.03297849096316041,
      "abs_C_h": 0.03297849096316041,
      "S_P_chord": 0.0016489245481580205,
      "S_P_chord_pp": 0.16489245481580206,
      "flat_in_kappa_Omega": 0.0,
      "flat_in_kappa_pi_bar_pr": 0.0,
      "degenerate": [],
      "S_P_model_abs_dM_P_dkappa": {
        "kappa=0.25": 0.0072713543423929845,
        "kappa=0.5": 0.003250396730098496,
        "kappa=0.75": 0.010085351285623916
      },
      "S_P_model_pp_at_kappa_0.5": 0.3250396730098496
    }
  ],
  "tightening_steps": [
    {
      "T": 5,
      "tau": 0.09631173355658933,
      "tau_prime": 0.09513374043270158,
      "tau_quantile": 0.9,
      "tau_prime_quantile": 0.8,
      "d_Omega": 0.022633267058852626,
      "d_pi_bar_pr": -0.01876557200632642,
      "d_S_P_chord": -0.0002649855282727653,
      "d_S_P_model": -0.0004701959381451493,
      "reclassified_mass": 0.022633267058852626
    },
    {
      "T": 5,
      "tau": 0.09513374043270158,
      "tau_prime": 0.09407139027595574,
      "tau_quantile": 0.8,
      "tau_prime_quantile": 0.7000000000000001,
      "d_Omega": 0.02263326705885306,
      "d_pi_bar_pr": -0.019676903649142624,
      "d_S_P_chord": -0.00025641999515350054,
      "d_S_P_model": -0.0007355636177809989,
      "reclassified_mass": 0.02263326705885306
    },
    {
      "T": 5,
      "tau": 0.09407139027595574,
      "tau_prime": 0.09303125238357923,
      "tau_quantile": 0.7000000000000001,
      "tau_prime_quantile": 0.6000000000000001,
      "d_Omega": 0.022633267058852963,
      "d_pi_bar_pr": -0.020656274310411588,
      "d_S_P_chord": -0.00024433374530409145,
      "d_S_P_model": -0.0004475024363236929,
      "reclassified_mass": 0.022633267058852963
    },
    {
      "T": 5,
      "tau": 0.09303125238357923,
      "tau_prime": 0.09197763253912061,
      "tau_quantile": 0.6000000000000001,
      "tau_prime_quantile": 0.5,
      "d_Omega": 0.022633267058853143,
      "d_pi_bar_pr": -0.02171062980347635,
      "d_S_P_chord": -0.00022792513187553515,
      "d_S_P_model": -0.00036028081768351783,
      "reclassified_mass": 0.022633267058853143
    },
    {
      "T": 5,
      "tau": 0.09197763253912061,
      "tau_prime": 0.09089137143817187,
      "tau_quantile": 0.5,
      "tau_prime_quantile": 0.4,
      "d_Omega": 0.02263326705885267,
      "d_pi_bar_pr": -0.022847825490253784,
      "d_S_P_chord": -0.00020619659909365464,
      "d_S_P_model": -0.00048341664627001805,
      "reclassified_mass": 0.02263326705885267
    },
    {
      "T": 5,
      "tau": 0.09089137143817187,
      "tau_prime": 0.08122294922274018,
      "tau_quantile": 0.4,
      "tau_prime_quantile": 0.30000000000000004,
      "d_Omega": 0.02263326705885324,
      "d_pi_bar_pr": -0.024076773050679456,
      "d_S_P_chord": -0.00017789438304488048,
      "d_S_P_model": -0.0003007833029038836,
      "reclassified_mass": 0.02263326705885324
    },
    {
      "T": 5,
      "tau": 0.08122294922274018,
      "tau_prime": 0.07393121647665091,
      "tau_quantile": 0.30000000000000004,
      "tau_prime_quantile": 0.2,
      "d_Omega": 0.022633267058852602,
      "d_pi_bar_pr": -0.025407615646497045,
      "d_S_P_chord": -0.000141422340731065,
      "d_S_P_model": -0.0002532284075405203,
      "reclassified_mass": 0.022633267058852602
    },
    {
      "T": 5,
      "tau": 0.07393121647665091,
      "tau_prime": 0.07299687117045922,
      "tau_quantile": 0.2,
      "tau_prime_quantile": 0.1,
      "d_Omega": 0.02263326705885288,
      "d_pi_bar_pr": -0.026851937935856305,
      "d_S_P_chord": -9.471395101699196e-05,
      "d_S_P_model": -0.00016976755047825838,
      "reclassified_mass": 0.02263326705885288
    },
    {
      "T": 10,
      "tau": 0.052103911185529775,
      "tau_prime": 0.0462834351081754,
      "tau_quantile": 0.9,
      "tau_prime_quantile": 0.8,
      "d_Omega": 0.02263326705885229,
      "d_pi_bar_pr": -0.018765572006326142,
      "d_S_P_chord": -0.0002649855282727653,
      "d_S_P_model": -0.00047019593814522174,
      "reclassified_mass": 0.02263326705885229
    },
    {
      "T": 10,
      "tau": 0.0462834351081754,
      "tau_prime": 0.04601784756898893,
      "tau_quantile": 0.8,
      "tau_prime_quantile": 0.7000000000000001,
      "d_Omega": 0.022633267058853386,
      "d_pi_bar_pr": -0.019676903649142874,
      "d_S_P_chord": -0.00025641999515349924,
      "d_S_P_model": -0.0007355636177808905,
      "reclassified_mass": 0.022633267058853386
    },
    {
      "T": 10,
      "tau": 0.04601784756898893,
      "tau_prime": 0.042606250476715846,
      "tau_quantile": 0.7000000000000001,
      "tau_prime_quantile": 0.6000000000000001,
      "d_Omega": 0.022633267058852963,
      "d_pi_bar_pr": -0.020656274310411643,
      "d_S_P_chord": -0.00024433374530408863,
      "d_S_P_model": -0.00044750243632347584,
      "reclassified_mass": 0.022633267058852963
    },
    {
      "T": 10,
      "tau": 0.042606250476715846,
      "tau_prime": 0.04032960542318677,
      "tau_quantile": 0.6000000000000001,
      "tau_prime_quantile": 0.5,
      "d_Omega": 0.02263326705885313,
      "d_pi_bar_pr": -0.021710629803476295,
      "d_S_P_chord": -0.00022792513187553797,
      "d_S_P_model": -0.00036028081768351805,
      "reclassified_mass": 0.02263326705885313
    },
    {
      "T": 10,
      "tau": 0.04032960542318677,
      "tau_prime": 0.04014856190636198,
      "tau_quantile": 0.5,
      "tau_prime_quantile": 0.4,
      "d_Omega": 0.022633267058852644,
      "d_pi_bar_pr": -0.022847825490253798,
      "d_S_P_chord": -0.00020619659909365464,
      "d_S_P_model": -0.0004834166462708491,
      "reclassified_mass": 0.022633267058852644
    },
    {
      "T": 10,
      "tau": 0.04014856190636198,
      "tau_prime": 0.03853715820379003,
      "tau_quantile": 0.4,
      "tau_prime_quantile": 0.30000000000000004,
      "d_Omega": 0.022633267058853268,
      "d_pi_bar_pr": -0.02407677305067943,
      "d_S_P_chord": -0.00017789438304488048,
      "d_S_P_model": -0.0003007833029035403,
      "reclassified_mass": 0.022633267058853268
    },
    {
      "T": 10,
      "tau": 0.03853715820379003,
      "tau_prime": 0.037321869412775155,
      "tau_quantile": 0.30000000000000004,
      "tau_prime_quantile": 0.2,
      "d_Omega": 0.022633267058852102,
      "d_pi_bar_pr": -0.025407615646496566,
      "d_S_P_chord": -0.00014142234073106255,
      "d_S_P_model": -0.00025322840754142377,
      "reclassified_mass": 0.022633267058852102
    },
    {
      "T": 10,
      "tau": 0.037321869412775155,
      "tau_prime": 0.037166145195076536,
      "tau_quantile": 0.2,
      "tau_prime_quantile": 0.1,
      "d_Omega": 0.022633267058853324,
      "d_pi_bar_pr": -0.026851937935856805,
      "d_S_P_chord": -9.471395101699423e-05,
      "d_S_P_model": -0.00016976755047713802,
      "reclassified_mass": 0.022633267058853324
    }
  ],
  "baseline": {
    "k": [
      1.2405757282617416,
      1.5310222869296415
    ],
    "tau_reference": 0.09076405861553302,
    "T": 5,
    "H": 10,
    "Omega": 0.1383963119314466,
    "pi_bar_pr": 0.10206126073370039,
    "M_P_pp": 0.2227984757708382,
    "M_F_pp": 0.552817848535105,
    "cutoff_scale": 2.595657022652631e-11,
    "payoff_scale": 0.0
  },
  "seconds": 414.66308566601947,
  "all_pass": true
}
```

### FILE: quality_reports/fixes/t2_p1_check.json

```json
{
  "checks": [
    {
      "name": "p1_inner_root_single_crossing",
      "kind": "substantive",
      "pass": true,
      "request": "item 2: exactly one sign change of rho(P) on a 2001-point grid over [v_hat-5 sigma_v, v_hat+5 sigma_v+m1]",
      "predicted_frac_multiroot": 0.0,
      "tol_frac": 0.0001,
      "by_cell": {
        "pooled": {
          "n_information_sets": 4000,
          "n_scanned": 2000,
          "frac_sign_changes_ne_1": 0.0,
          "min_sign_changes": 1,
          "max_sign_changes": 1,
          "pctl5_abs_g_slope": 0.6179980268160226,
          "min_abs_g_slope": 0.6179980268160226,
          "max_abs_rho_slope": 1.7331930440948806,
          "min_abs_rho_slope": 1.0963053330930996,
          "mean_p_bid_at_root": 0.25906290062863024,
          "all_rho_slopes_negative": true
        },
        "flagged": {
          "n_information_sets": 5000,
          "n_scanned": 1667,
          "frac_sign_changes_ne_1": 0.0,
          "min_sign_changes": 1,
          "max_sign_changes": 1,
          "pctl5_abs_g_slope": 1.000000021640895,
          "min_abs_g_slope": 1.0000000068645196,
          "max_abs_rho_slope": 1.0942970064326445,
          "min_abs_rho_slope": 1.000000008804862,
          "mean_p_bid_at_root": 0.013289500180212304,
          "all_rho_slopes_negative": true
        }
      }
    },
    {
      "name": "p1_inner_root_transversality",
      "kind": "substantive",
      "pass": true,
      "request": "item 2: rho' < 0 strictly at the root; 5th percentile of |g'| (the >= 1-p bound's own residual form) > 0.05",
      "tol_pctl5": 0.05,
      "by_cell": {
        "pooled": {
          "pctl5_abs_g_slope": 0.6179980268160226,
          "min_abs_g_slope": 0.6179980268160226,
          "max_abs_rho_slope": 1.7331930440948806,
          "min_abs_rho_slope": 1.0963053330930996,
          "mean_p_bid_at_root": 0.25906290062863024,
          "all_rho_slopes_negative": true
        },
        "flagged": {
          "pctl5_abs_g_slope": 1.000000021640895,
          "min_abs_g_slope": 1.0000000068645196,
          "max_abs_rho_slope": 1.0942970064326445,
          "min_abs_rho_slope": 1.000000008804862,
          "mean_p_bid_at_root": 0.013289500180212304,
          "all_rho_slopes_negative": true
        }
      }
    },
    {
      "name": "p1_flagged_family_single_valued",
      "kind": "substantive",
      "pass": true,
      "request": "item 3: single-valued and strictly increasing in v_hat; two independent solvers must agree",
      "n_tuples": 5000,
      "max_abs_disagreement_bisection_vs_brentq": 8.881784197001252e-16,
      "strictly_increasing_in_s": true,
      "min_dP": 6.167306076720891e-06
    },
    {
      "name": "p1_flagged_family_slope",
      "kind": "substantive",
      "pass": true,
      "request": "item 3: slope in (0,1]; numerical vs analytic below 1e-6; predicted 0.60 +- 0.10 at p ~ 0.85",
      "tol": 1e-06,
      "max_abs_gap_numeric_vs_analytic": 3.6105862744051365e-10,
      "slope_min": 0.9138286900522985,
      "slope_max": 0.9999999914800384,
      "slope_mean": 0.9771539654272577,
      "p_bid_mean": 0.013281039826058163,
      "slope_in_0_1": true,
      "note": "p_bid here is far from the request's illustrative 0.85, so the 0.60 +- 0.10 point prediction is reported, not enforced"
    },
    {
      "name": "p1_flagged_sequential_h11",
      "kind": "substantive",
      "pass": true,
      "request": "item 4: under h.11 (round 2 restricted to the plan-generated set) max gain = 0 to 1e-9 premium pp",
      "tol_pp": 1e-09,
      "max_gain_restricted_pp": 0.0,
      "max_gain_full_interval_pp": 5.551115123125783e-15,
      "n_tuples": 30,
      "finding": "The request predicts a strictly positive gain of order 1e-2 premium pp once round 2 is opened to the full interval. On this menu the gain is 0 to machine precision, because at the equilibrium flagged price family E[Y] - P^F = 0 identically (P^F = v_hat + Delta_V + p m1/(1-p) makes the blockholder exactly indifferent over Q'). h.11 therefore buys nothing here; that is a finding about the menu, not a refutation of P1, and it is reported rather than tuned away.",
      "max_abs_EY_minus_P_F": 2.9753977059954195e-14,
      "rows": [
        {
          "s": 1.7919690277957754,
          "B_F": 0.0911079560923789,
          "Q_F": 0.0,
          "P_F": 1.6376751930581825,
          "p_bid": 0.052703411431464176,
          "EY_minus_P_F": 0.0,
          "gain_full_interval_pp": 2.7755575615628914e-15
        },
        {
          "s": 1.8149221725375557,
          "B_F": 0.09143561264653498,
          "Q_F": 0.0,
          "P_F": 1.648226173059458,
          "p_bid": 0.04992663042931844,
          "EY_minus_P_F": 0.0,
          "gain_full_interval_pp": 2.7755575615628914e-15
        },
        {
          "s": 1.837875317279336,
          "B_F": 0.09174784981240325,
          "Q_F": 0.0,
          "P_F": 1.658818181524341,
          "p_bid": 0.047257679669576946,
          "EY_minus_P_F": 0.0,
          "gain_full_interval_pp": 2.7755575615628914e-15
        },
        {
          "s": 1.8971789939845638,
          "B_F": 0.09248865614793234,
          "Q_F": 0.0,
          "P_F": 1.686366174443057,
          "p_bid": 0.04084920127328073,
          "EY_minus_P_F": -2.220446049250313e-16,
          "gain_full_interval_pp": 0.0
        },
        {
          "s": 1.9335295259480108,
          "B_F": 0.09289984425701535,
          "Q_F": 0.0,
          "P_F": 1.7033746092519668,
          "p_bid": 0.03725763616469713,
          "EY_minus_P_F": 0.0,
          "gain_full_interval_pp": 2.7755575615628914e-15
        },
        {
          "s": 1.9698800579114577,
          "B_F": 0.09328161596256279,
          "Q_F": 0.0,
          "P_F": 1.7204706897845838,
          "p_bid": 0.03391182307327445,
          "EY_minus_P_F": 2.220446049250313e-16,
          "gain_full_interval_pp": 2.7755575615628914e-15
        }
      ]
    },
    {
      "name": "p1_both_cells_on_path",
      "kind": "substantive",
      "pass": true,
      "request": "item 5: 0 < Omega < 1 at every interior (tau,T) node; Omega in 0.03..0.30 at the card calibration",
      "Omega": 0.1383963119314466,
      "Pr_a": 0.2263326705885291,
      "omega_a": 0.6114729772399935,
      "pi_bar_pr": 0.10206126073370039,
      "in_predicted_band_0.03_0.30": true,
      "degenerate": []
    },
    {
      "name": "p1_threshold_reformulation",
      "kind": "substantive",
      "pass": true,
      "request": "item 5: Omega = 1 - Phi_s(s_F) wherever h.13 holds, agreement to 1e-10; disagreement tests h.13",
      "tol": 1e-10,
      "s_F": 1.7690158830539948,
      "flagged_set_is_upper_interval": true,
      "Omega_direct": 0.1383963119314466,
      "Omega_from_s_F": 0.1383963119314466,
      "abs_gap": 0.0,
      "note": "Phi_s is renormalised on the +-6 sigma_s truncated support, matching the atom masses evaluate() integrates."
    },
    {
      "name": "p1_Omega_monotone_tau_T",
      "kind": "substantive",
      "pass": true,
      "request": "item 5: Omega weakly increasing as tau falls and as T falls; Omega = 0 exactly at tau > b_bar",
      "grid_tau": [
        0.05,
        0.075,
        0.09076405861553302,
        0.098
      ],
      "grid_T": [
        1,
        2,
        5,
        10
      ],
      "Omega": {
        "T=1": [
          0.2263326705885291,
          0.22633267058852904,
          0.1383963119314466,
          0.002329388426713565
        ],
        "T=2": [
          0.2263326705885291,
          0.22633267058852904,
          0.1383963119314466,
          0.002329388426713565
        ],
        "T=5": [
          0.2263326705885291,
          0.17565414119031927,
          0.1383963119314466,
          0.002329388426713565
        ],
        "T=10": [
          0.043340421572277237,
          0.0006812715261460645,
          0.0006812715261460647,
          0.0006812715261460645
        ]
      },
      "violations_tau": [],
      "violations_T": [],
      "Omega_at_tau_above_b_bar": 0.0
    },
    {
      "name": "p1_multistart_existence_core",
      "kind": "substantive",
      "pass": true,
      "request": "item 1: 30-seed multistart at every node; at least one seed converges. BINDING = payoff scale < 1e-9 (design 13.4); cutoff scale 1e-10 diagnostic only",
      "node": {
        "kappa": 0.5,
        "tau": 0.09076405861553302,
        "T": 5,
        "H": 10
      },
      "n_seeds": 30,
      "early_stop": false,
      "tol_payoff_binding": 1e-09,
      "tol_cutoff_diagnostic": 1e-10,
      "median_best_cutoff_scale": 1.78974612907723e-11,
      "rows": [
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.7891910175649173e-11,
          "k": [
            1.2405757282617416,
            1.5310222869296415
          ],
          "seconds": 1170.7947851659264,
          "variant": "baseline",
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.793942772110313e-11,
          "k": [
            1.1914476463226624,
            1.5618677486891202
          ],
          "seconds": 1311.4214346249355,
          "variant": "sigma_xi -20%",
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.9182877508683305e-11,
          "k": [
            1.2813763702926402,
            1.4993846885500108
          ],
          "seconds": 1507.7841297499835,
          "variant": "sigma_xi +20%",
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.78974612907723e-11,
          "k": [
            1.2332683694860702,
            1.5292054120873009
          ],
          "seconds": 1617.3796074589482,
          "variant": "Delta_m -20%",
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.749156375296934e-11,
          "k": [
            1.2465041564227206,
            1.5334466239604543
          ],
          "seconds": 1234.026818000013,
          "variant": "Delta_m +20%",
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.2691404311103724e-11,
          "k": [
            1.2833763295489828,
            1.4465322079021048
          ],
          "seconds": 781.319002791075,
          "variant": "C0 -20%",
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 30,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.7322809853226318e-11,
          "k": [
            1.2102901035268387,
            1.5987153792882898
          ],
          "seconds": 701.4820968329441,
          "variant": "C0 +20%",
          "converged_payoff": true,
          "converged_cutoff": true
        }
      ]
    },
    {
      "name": "p1_multistart_existence_sweep",
      "kind": "substantive",
      "pass": false,
      "request": "item 1 across the policy grid, early-stopping multistart (seeds 0..4, stop at the first seed meeting the binding criterion). The request's 30-seed ask is carried by node set A; this sweep is grid coverage, capped at 5 seeds so a non-converging node costs 2 min rather than 14",
      "n_seeds_cap": 5,
      "grid": {
        "kappa": [
          0.15,
          0.5,
          0.85
        ],
        "tau": [
          0.05,
          0.075,
          0.09076405861553302
        ],
        "T": [
          1,
          5,
          10
        ]
      },
      "n_nodes": 27,
      "n_converged": 23,
      "median_best_cutoff_scale": 2.7496227517076477e-11,
      "rows": [
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.1351586337582376e-11,
          "k": [
            0.9848656471040279,
            1.405443837554305
          ],
          "seconds": 13.32870533305686,
          "kappa": 0.15,
          "tau": 0.05,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 5,
          "best_payoff_scale": 0.001488170939392311,
          "best_cutoff_scale": 1.8952395208771122e-11,
          "k": [
            1.0074676693103841,
            1.5613050961812023
          ],
          "seconds": 85.2498247079784,
          "kappa": 0.15,
          "tau": 0.05,
          "T": 5,
          "corner": false,
          "converged_payoff": false,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.934363863005274e-11,
          "k": [
            1.0261792633655062,
            1.7247476202912642
          ],
          "seconds": 34.48688045900781,
          "kappa": 0.15,
          "tau": 0.05,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 5,
          "best_payoff_scale": 0.0010592282017965887,
          "best_cutoff_scale": 1.2545520178264269e-14,
          "k": [
            1.0039258750690332,
            1.5361669836666294
          ],
          "seconds": 83.91239004197996,
          "kappa": 0.15,
          "tau": 0.075,
          "T": 1,
          "corner": false,
          "converged_payoff": false,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.9973357129620126e-11,
          "k": [
            1.0269292934852638,
            1.7188164187922315
          ],
          "seconds": 24.662359042093158,
          "kappa": 0.15,
          "tau": 0.075,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.4831471040774886e-11,
          "k": [
            1.0232161239375368,
            1.7288567020075272
          ],
          "seconds": 37.3102034580661,
          "kappa": 0.15,
          "tau": 0.075,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.0443202686237782e-11,
          "k": [
            1.0235134306069529,
            1.6886239853940521
          ],
          "seconds": 26.589181166957133,
          "kappa": 0.15,
          "tau": 0.09076405861553302,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.45770079235308e-11,
          "k": [
            1.0271277351914962,
            1.7218534313570004
          ],
          "seconds": 28.960273541975766,
          "kappa": 0.15,
          "tau": 0.09076405861553302,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.4831471040774886e-11,
          "k": [
            1.0232161239375388,
            1.7288567020075274
          ],
          "seconds": 37.957647374947555,
          "kappa": 0.15,
          "tau": 0.09076405861553302,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 4.3553827211439966e-11,
          "k": [
            1.35358624390523,
            1.35358624390523
          ],
          "seconds": 9.421609582961537,
          "kappa": 0.5,
          "tau": 0.05,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.3427259304421568e-11,
          "k": [
            1.3124648122403926,
            1.4188874333035122
          ],
          "seconds": 14.469053499982692,
          "kappa": 0.5,
          "tau": 0.05,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.0220047858288126e-11,
          "k": [
            1.209953101041571,
            1.5427418820422603
          ],
          "seconds": 27.900847374927253,
          "kappa": 0.5,
          "tau": 0.05,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.486832879038502e-11,
          "k": [
            1.3329053753496902,
            1.3856452728203859
          ],
          "seconds": 15.497320082969964,
          "kappa": 0.5,
          "tau": 0.075,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.818700745559454e-11,
          "k": [
            1.2474379654606653,
            1.5275078110677354
          ],
          "seconds": 21.655889875022694,
          "kappa": 0.5,
          "tau": 0.075,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.082845090318642e-11,
          "k": [
            1.1751647692528333,
            1.5524833105541282
          ],
          "seconds": 28.79393050004728,
          "kappa": 0.5,
          "tau": 0.075,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.7496227517076477e-11,
          "k": [
            1.2629896052256364,
            1.4853933354309685
          ],
          "seconds": 23.003384666983038,
          "kappa": 0.5,
          "tau": 0.09076405861553302,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.595657022652631e-11,
          "k": [
            1.2405757282617416,
            1.5310222869296415
          ],
          "seconds": 24.27560908300802,
          "kappa": 0.5,
          "tau": 0.09076405861553302,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.082845090318642e-11,
          "k": [
            1.1751647692528333,
            1.5524833105541285
          ],
          "seconds": 28.617705083917826,
          "kappa": 0.5,
          "tau": 0.09076405861553302,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 1.2283285499847807e-11,
          "k": [
            1.1157977627393094,
            1.4012599049980128
          ],
          "seconds": 13.083739583962597,
          "kappa": 0.85,
          "tau": 0.05,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 5,
          "best_payoff_scale": 0.00039841768806352096,
          "best_cutoff_scale": 2.2122526033285794e-11,
          "k": [
            1.0871354370969635,
            1.548848450728854
          ],
          "seconds": 86.30552520800848,
          "kappa": 0.85,
          "tau": 0.05,
          "T": 5,
          "corner": false,
          "converged_payoff": false,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.68594044175552e-11,
          "k": [
            1.061826796222292,
            1.6910736046667811
          ],
          "seconds": 32.80734025000129,
          "kappa": 0.85,
          "tau": 0.05,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 5,
          "best_payoff_scale": 0.0003061479141195228,
          "best_cutoff_scale": 2.173439206387684e-11,
          "k": [
            1.088861883430131,
            1.5387849788427397
          ],
          "seconds": 82.52846516598947,
          "kappa": 0.85,
          "tau": 0.075,
          "T": 1,
          "corner": false,
          "converged_payoff": false,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.4767743411757692e-11,
          "k": [
            1.066803889468342,
            1.6819731495707522
          ],
          "seconds": 26.277260291972198,
          "kappa": 0.85,
          "tau": 0.075,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.622768751654348e-11,
          "k": [
            1.050545549572742,
            1.696911726592003
          ],
          "seconds": 35.871342208003625,
          "kappa": 0.85,
          "tau": 0.075,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.2281954887025677e-11,
          "k": [
            1.0722997080636352,
            1.6400179955678202
          ],
          "seconds": 28.385986541979946,
          "kappa": 0.85,
          "tau": 0.09076405861553302,
          "T": 1,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 2.887023953235257e-11,
          "k": [
            1.0657183897027622,
            1.6873782038086496
          ],
          "seconds": 29.420030874898657,
          "kappa": 0.85,
          "tau": 0.09076405861553302,
          "T": 5,
          "corner": false,
          "converged_payoff": true,
          "converged_cutoff": true
        },
        {
          "seeds_run": 1,
          "best_payoff_scale": 0.0,
          "best_cutoff_scale": 3.622702138272871e-11,
          "k": [
            1.050545549572741,
            1.6969117265920035
          ],
          "seconds": 36.78525491594337,
          "kappa": 0.85,
          "tau": 0.09076405861553302,
          "T": 10,
          "corner": true,
          "converged_payoff": true,
          "converged_cutoff": true
        }
      ]
    }
  ],
  "n_fail": 1,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "8ef7c5c2d3896bf8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/proofs/P1_proof.md, NUMERICAL CHECK REQUEST",
    "binding_criterion": "payoff scale, no adjacent-plan deviation above 1e-9 (design section 13, ruling 4); cutoff-scale 1e-10 diagnostic only",
    "H12_robustness": "excluded for P1 by design section 13, ruling 2"
  },
  "grid": {
    "kappa": [
      0.15,
      0.5,
      0.85
    ],
    "tau": [
      0.05,
      0.075,
      0.09076405861553302
    ],
    "tau_excluded": {
      "0.03": "equals b0; violates the maintained b0 < tau",
      "0.10": "equals b_bar; no type crosses, Omega = 0 (checked directly in p1_Omega_monotone_tau_T instead)"
    },
    "T": [
      1,
      5,
      10
    ],
    "T_excluded": {
      "2": "dropped for runtime; T=1 already exercises the short-window end"
    },
    "H": 10,
    "M": 2,
    "tau_frozen_from": "median of the seed-equilibrium (tau=0.05) Voice b*(s) distribution, design section 6.2",
    "n_seeds": 30,
    "sizing": "One cold solve_policy ~= 27 s. The request's full grid (19 kappa x 4 tau x 5 T x 7 parameter variants x 30 seeds) is ~600 h and is not runnable. Cut to NODE SET A = 7 parameter variants x 30 seeds (no early stop, ~95 min) at kappa=0.5, tau=tau_50, T=5, plus NODE SET B = 3 kappa x 3 tau x 3 T early-stopping multistart capped at 5 seeds (~12 min typical, ~60 min worst case). Both sets are stated in the check details."
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "n_atoms": 19,
    "n_flagged_atoms": 10,
    "discarded_mass": 0.0,
    "n_pooled_information_sets_sampled": 4000,
    "n_flagged_tuples": 5000
  },
  "degenerate_nodes": [],
  "multiple_root_nodes": 0,
  "baseline": {
    "k": [
      1.2405757282617416,
      1.5310222869296415
    ],
    "kappa": 0.5,
    "tau": 0.09076405861553302,
    "T": 5,
    "H": 10,
    "Omega": 0.1383963119314466,
    "M_F_pp": 0.552817848535105,
    "M_P_pp": 0.2227984757708382,
    "cutoff_scale": 2.595657022652631e-11,
    "payoff_scale": 0.0,
    "slopes": [
      -0.005427536789101572,
      -0.03996569598908872
    ],
    "a7_passes": true,
    "a7_min_slope": 0.00021992796519100947,
    "max_Q_F": 0.0
  },
  "seconds": 9349.987605500035,
  "all_pass": false
}
```

### FILE: quality_reports/fixes/t2_t1_check.json

```json
{
  "checks": [
    {
      "name": "t1_block1_factorisation",
      "kind": "wiring",
      "pass": true,
      "vacuous": false,
      "request": "Block 1: max |S - (1-Omega) S_P| and max |S^TV - (1-Omega) S_P^TV|, both predicted below 1e-10",
      "tol": 1e-10,
      "max_pointwise_residual": 2.0643209364124004e-16,
      "max_TV_residual": 3.469446951953614e-18,
      "why_wiring": "at frozen policy Omega and M_F are kappa-free, so Delta^act = Omega M_F + (1-Omega) M_P differentiates to (1-Omega) d_kappa M_P identically; the residual is machine noise by construction (design section 0 rules the product identity wiring and the <= 1 substantive)",
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.1,
          "Omega": 0.14465741548984065,
          "S_TV_pp": 0.10416626247291266,
          "S_P_TV_pp": 0.12178308944195376,
          "S_meanslope": 0.0014880894638987507,
          "S_P_meanslope": 0.001739758420599338,
          "max_pointwise_factorisation_residual": 1.1937065919065404e-16,
          "TV_factorisation_residual": 2.168404344971009e-19
        },
        {
          "T": 5,
          "tau_quantile": 0.3,
          "Omega": 0.1446574154898407,
          "S_TV_pp": 0.10416626247291266,
          "S_P_TV_pp": 0.1217830894419538,
          "S_meanslope": 0.001488089463898751,
          "S_P_meanslope": 0.0017397584205993384,
          "max_pointwise_factorisation_residual": 1.1535911115245767e-16,
          "TV_factorisation_residual": 0.0
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "Omega": 0.1383963119314466,
          "S_TV_pp": 0.11775884396770524,
          "S_P_TV_pp": 0.13667402495883435,
          "S_meanslope": 0.0016822691995386448,
          "S_P_meanslope": 0.001952486070840489,
          "max_pointwise_factorisation_residual": 8.196568423990414e-17,
          "TV_factorisation_residual": 6.505213034913027e-19
        },
        {
          "T": 5,
          "tau_quantile": 0.7,
          "Omega": 0.08303778676423275,
          "S_TV_pp": 0.24634328441359002,
          "S_P_TV_pp": 0.26865151132487386,
          "S_meanslope": 0.003519189777336997,
          "S_P_meanslope": 0.0038378787332124806,
          "max_pointwise_factorisation_residual": 1.3704315460216776e-16,
          "TV_factorisation_residual": 8.673617379884035e-19
        },
        {
          "T": 5,
          "tau_quantile": 0.9,
          "Omega": 0.02767926159701934,
          "S_TV_pp": 0.44256824261551186,
          "S_P_TV_pp": 0.4551669270599147,
          "S_meanslope": 0.006322403465935877,
          "S_P_meanslope": 0.006502384672284489,
          "max_pointwise_factorisation_residual": 1.4051260155412137e-16,
          "TV_factorisation_residual": 0.0
        },
        {
          "T": 10,
          "tau_quantile": 0.1,
          "Omega": 0.0006812715261460647,
          "S_TV_pp": 0.5729694455260462,
          "S_P_TV_pp": 0.5733600594087505,
          "S_meanslope": 0.008185277793229223,
          "S_P_meanslope": 0.008190857991553575,
          "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
          "TV_factorisation_residual": 3.469446951953614e-18
        },
        {
          "T": 10,
          "tau_quantile": 0.3,
          "Omega": 0.0006812715261460647,
          "S_TV_pp": 0.5729694455260461,
          "S_P_TV_pp": 0.5733600594087503,
          "S_meanslope": 0.008185277793229223,
          "S_P_meanslope": 0.008190857991553571,
          "max_pointwise_factorisation_residual": 1.717376241217039e-16,
          "TV_factorisation_residual": 3.469446951953614e-18
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "Omega": 0.0006812715261460647,
          "S_TV_pp": 0.5729694455260461,
          "S_P_TV_pp": 0.5733600594087507,
          "S_meanslope": 0.008185277793229223,
          "S_P_meanslope": 0.008190857991553573,
          "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
          "TV_factorisation_residual": 0.0
        },
        {
          "T": 10,
          "tau_quantile": 0.7,
          "Omega": 0.0006812715261460647,
          "S_TV_pp": 0.5729694455260458,
          "S_P_TV_pp": 0.5733600594087505,
          "S_meanslope": 0.008185277793229218,
          "S_P_meanslope": 0.008190857991553571,
          "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
          "TV_factorisation_residual": 8.673617379884035e-19
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "Omega": 0.0006812715261460648,
          "S_TV_pp": 0.5729694455260461,
          "S_P_TV_pp": 0.5733600594087507,
          "S_meanslope": 0.008185277793229221,
          "S_P_meanslope": 0.008190857991553575,
          "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
          "TV_factorisation_residual": 0.0
        }
      ]
    },
    {
      "name": "t1_block1_Omega_flat_in_kappa",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 1: max_kappa |Omega(kappa) - Omega(kappa_0)| at fixed policies, predicted below 1e-12 -- this checks that H6 is implemented and not merely asserted. A nonzero value here invalidates every later block",
      "tol": 1e-12,
      "max_residual": 0.0,
      "n_kappa_nodes": 71
    },
    {
      "name": "t1_block2_threshold_margin",
      "kind": "mixed",
      "pass": true,
      "vacuous": false,
      "request": "Block 2: W_tau = (1-Omega(tau'))/(1-Omega(tau)), C_tau = S_P(tau')/S_P(tau), their product, and the direct ratio S(tau')/S(tau). Predicted W_tau <= 1, C_tau <= 1, product <= 1; identity residual below 1e-10; product equal to one within 1e-12 at any pair that reclassifies no mass",
      "tol_identity": 1e-10,
      "tol_null": 1e-12,
      "max_identity_residual": 5.551115123125783e-16,
      "n_pairs": 8,
      "n_product_above_one": 0,
      "violations": [],
      "n_null_reclassification_pairs": 5,
      "null_pairs_product_equals_one": true,
      "note": "the terminal-stake tau ladder does not bite below the median at T = 5, and does not bite at all at T = 10, so several pairs reclassify zero mass. Those are Step 14's null case and are reported explicitly rather than inferred; L4's own ladder (deciles of B(s,H-T)) bites at every step and is checked in t2_l4_check.py",
      "rows": [
        {
          "T": 5,
          "tau": 0.09602833824479486,
          "tau_prime": 0.09337594348697996,
          "tau_quantile": 0.9,
          "tau_prime_quantile": 0.7,
          "W_tau": 0.9430655719036305,
          "C_tau": 0.5902263441243186,
          "W_tau_C_tau": 0.5566221447741896,
          "direct_ratio": 0.5566221447741895,
          "identity_residual": 1.1102230246251565e-16,
          "reclassified_mass": 0.05535852516721341,
          "S_P_TV_pp_tau": 0.4551669270599147,
          "S_P_TV_pp_tau_prime": 0.26865151132487386,
          "null_reclassification": false
        },
        {
          "T": 5,
          "tau": 0.09337594348697996,
          "tau_prime": 0.09076405861553302,
          "tau_quantile": 0.7,
          "tau_prime_quantile": 0.5,
          "W_tau": 0.9396283463286178,
          "C_tau": 0.5087409495104522,
          "W_tau_C_tau": 0.47802741709815705,
          "direct_ratio": 0.4780274170981575,
          "identity_residual": 4.440892098500626e-16,
          "reclassified_mass": 0.05535852516721386,
          "S_P_TV_pp_tau": 0.26865151132487386,
          "S_P_TV_pp_tau_prime": 0.13667402495883435,
          "null_reclassification": false
        },
        {
          "T": 5,
          "tau": 0.09076405861553302,
          "tau_prime": 0.08788437014471917,
          "tau_quantile": 0.5,
          "tau_prime_quantile": 0.3,
          "W_tau": 0.9927331978204161,
          "C_tau": 0.891047801355337,
          "W_tau_C_tau": 0.8845727332503346,
          "direct_ratio": 0.8845727332503343,
          "identity_residual": 3.3306690738754696e-16,
          "reclassified_mass": 0.006261103558394099,
          "S_P_TV_pp_tau": 0.13667402495883435,
          "S_P_TV_pp_tau_prime": 0.1217830894419538,
          "null_reclassification": false
        },
        {
          "T": 5,
          "tau": 0.08788437014471917,
          "tau_prime": 0.08462696676439771,
          "tau_quantile": 0.3,
          "tau_prime_quantile": 0.1,
          "W_tau": 1.0,
          "C_tau": 0.9999999999999997,
          "W_tau_C_tau": 0.9999999999999997,
          "direct_ratio": 1.0,
          "identity_residual": 3.3306690738754696e-16,
          "reclassified_mass": -5.551115123125783e-17,
          "S_P_TV_pp_tau": 0.1217830894419538,
          "S_P_TV_pp_tau_prime": 0.12178308944195376,
          "null_reclassification": true
        },
        {
          "T": 10,
          "tau": 0.09602833824479486,
          "tau_prime": 0.09337594348697996,
          "tau_quantile": 0.9,
          "tau_prime_quantile": 0.7,
          "W_tau": 1.0,
          "C_tau": 0.9999999999999997,
          "W_tau_C_tau": 0.9999999999999997,
          "direct_ratio": 0.9999999999999996,
          "identity_residual": 1.1102230246251565e-16,
          "reclassified_mass": -1.0842021724855044e-19,
          "S_P_TV_pp_tau": 0.5733600594087507,
          "S_P_TV_pp_tau_prime": 0.5733600594087505,
          "null_reclassification": true
        },
        {
          "T": 10,
          "tau": 0.09337594348697996,
          "tau_prime": 0.09076405861553302,
          "tau_quantile": 0.7,
          "tau_prime_quantile": 0.5,
          "W_tau": 1.0,
          "C_tau": 1.0000000000000002,
          "W_tau_C_tau": 1.0000000000000002,
          "direct_ratio": 1.0000000000000004,
          "identity_residual": 2.220446049250313e-16,
          "reclassified_mass": 0.0,
          "S_P_TV_pp_tau": 0.5733600594087505,
          "S_P_TV_pp_tau_prime": 0.5733600594087507,
          "null_reclassification": true
        },
        {
          "T": 10,
          "tau": 0.09076405861553302,
          "tau_prime": 0.08788437014471917,
          "tau_quantile": 0.5,
          "tau_prime_quantile": 0.3,
          "W_tau": 1.0,
          "C_tau": 0.9999999999999994,
          "W_tau_C_tau": 0.9999999999999994,
          "direct_ratio": 1.0,
          "identity_residual": 5.551115123125783e-16,
          "reclassified_mass": 0.0,
          "S_P_TV_pp_tau": 0.5733600594087507,
          "S_P_TV_pp_tau_prime": 0.5733600594087503,
          "null_reclassification": true
        },
        {
          "T": 10,
          "tau": 0.08788437014471917,
          "tau_prime": 0.08462696676439771,
          "tau_quantile": 0.3,
          "tau_prime_quantile": 0.1,
          "W_tau": 1.0,
          "C_tau": 1.0000000000000002,
          "W_tau_C_tau": 1.0000000000000002,
          "direct_ratio": 1.0000000000000002,
          "identity_residual": 0.0,
          "reclassified_mass": 0.0,
          "S_P_TV_pp_tau": 0.5733600594087503,
          "S_P_TV_pp_tau_prime": 0.5733600594087505,
          "null_reclassification": true
        }
      ]
    },
    {
      "name": "t1_block3_chord_magnitude",
      "kind": "substantive",
      "pass": false,
      "vacuous": false,
      "request": "Block 3: residual |S_P - Delta_m |A'_kappa| |C_h(pi_bar)||, predicted below 1e-10; and |C_h(pi_bar)|/pi_bar^2 constant to within 5% between the two smallest pi_bar nodes",
      "tol": 1e-10,
      "max_residual": 0.006279460912900145,
      "max_residual_pp": 0.6279460912900146,
      "chord_ratio_spread_two_smallest": 0.004844043274959965,
      "chord_ratio_within_5pct": true,
      "pi_bar_two_smallest_distinct": [
        0.19097670705934158,
        0.20412252146740079
      ],
      "n_distinct_pi_bar": 5,
      "implied_abs_A_prime_kappa_range": [
        0.9968382246618326,
        1.1578010526026856
      ],
      "implied_A_prime_note": "S_P/(Delta_m |C_h(pi_bar)|) is the value |A'_kappa| would have to take for the chord formula to reproduce the enumerated sensitivity. Example A gives 1/4; the gap between the two IS the A'_kappa channel that L4 prediction 5 and T1's C_tau inherit",
      "pi_bar_vs_pi_bar_pr": "reported in separate columns per H11's ruling: pi_bar is the upper support point of the pooled engagement posterior (here the level-symmetric 2 pi_bar_pr), pi_bar_pr is the share Pr(a=1|D=0); conflating them is the most likely implementation error in this block",
      "max_relative_residual": 3.631204210410743,
      "finding": "FAILED HYPOTHESIS, reported and not smoothed. The residual is 0.627946 premium pp, far above 1e-10. It is the gap between the ENUMERATED two-round pooled sensitivity and A(tau)'s three-atom closed form -- exactly the object design section 0 says the build must measure ('the enumeration never imposes A(tau)'). It is a failed hypothesis about A(tau)'s applicability to this pooled law, not a wiring error: L3's Example B shows the manuscript's four-atom structure lies outside A(tau), and t2_l3_check.py's block 5b measures the same gap analytically.",
      "rows": [
        {
          "T": 5,
          "tau_quantile": 0.1,
          "pi_bar_level_symmetric": 0.19097670705934158,
          "pi_bar_pr": 0.09548835352967079,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.007513201066316352,
          "abs_C_h_over_pi_bar2": 0.20599857213154243,
          "S_P_meanslope_pp": 0.1739758420599338,
          "S_P_TV_pp": 0.12178308944195376,
          "chord_formula_pp": 0.037566005331581755,
          "residual": 0.0013640983672835204,
          "residual_pp": 0.13640983672835205,
          "relative_residual": 3.6312042104107416,
          "implied_abs_A_prime_kappa": 1.1578010526026854
        },
        {
          "T": 5,
          "tau_quantile": 0.3,
          "pi_bar_level_symmetric": 0.19097670705934158,
          "pi_bar_pr": 0.09548835352967079,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.007513201066316352,
          "abs_C_h_over_pi_bar2": 0.20599857213154243,
          "S_P_meanslope_pp": 0.17397584205993386,
          "S_P_TV_pp": 0.1217830894419538,
          "chord_formula_pp": 0.037566005331581755,
          "residual": 0.0013640983672835209,
          "residual_pp": 0.13640983672835208,
          "relative_residual": 3.631204210410743,
          "implied_abs_A_prime_kappa": 1.1578010526026856
        },
        {
          "T": 5,
          "tau_quantile": 0.5,
          "pi_bar_level_symmetric": 0.20412252146740079,
          "pi_bar_pr": 0.10206126073370039,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.008541560194656406,
          "abs_C_h_over_pi_bar2": 0.20500070613355728,
          "S_P_meanslope_pp": 0.1952486070840489,
          "S_P_TV_pp": 0.13667402495883435,
          "chord_formula_pp": 0.04270780097328202,
          "residual": 0.0015254080611076689,
          "residual_pp": 0.1525408061107669,
          "relative_residual": 3.5717316891636806,
          "implied_abs_A_prime_kappa": 1.1429329222909201
        },
        {
          "T": 5,
          "tau_quantile": 0.7,
          "pi_bar_level_symmetric": 0.31254261463760596,
          "pi_bar_pr": 0.15627130731880298,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.01925025865914423,
          "abs_C_h_over_pi_bar2": 0.1970688976791492,
          "S_P_meanslope_pp": 0.3837878733212481,
          "S_P_TV_pp": 0.26865151132487386,
          "chord_formula_pp": 0.09625129329572114,
          "residual": 0.002875365800255269,
          "residual_pp": 0.2875365800255269,
          "relative_residual": 2.9873528986473303,
          "implied_abs_A_prime_kappa": 0.9968382246618326
        },
        {
          "T": 5,
          "tau_quantile": 0.9,
          "pi_bar_level_symmetric": 0.4086170358102089,
          "pi_bar_pr": 0.20430851790510446,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.0317852307632788,
          "abs_C_h_over_pi_bar2": 0.19036733526975255,
          "S_P_meanslope_pp": 0.6502384672284489,
          "S_P_TV_pp": 0.4551669270599147,
          "chord_formula_pp": 0.158926153816394,
          "residual": 0.00491312313412055,
          "residual_pp": 0.491312313412055,
          "relative_residual": 3.0914503473082466,
          "implied_abs_A_prime_kappa": 1.0228625868270615
        },
        {
          "T": 10,
          "tau_quantile": 0.1,
          "pi_bar_level_symmetric": 0.4516104674771677,
          "pi_bar_pr": 0.22580523373858385,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.03822794157306861,
          "abs_C_h_over_pi_bar2": 0.18743595986400846,
          "S_P_meanslope_pp": 0.8190857991553575,
          "S_P_TV_pp": 0.5733600594087505,
          "chord_formula_pp": 0.191139707865343,
          "residual": 0.006279460912900145,
          "residual_pp": 0.6279460912900146,
          "relative_residual": 3.2852728420637716,
          "implied_abs_A_prime_kappa": 1.071318210515943
        },
        {
          "T": 10,
          "tau_quantile": 0.3,
          "pi_bar_level_symmetric": 0.45161046747716777,
          "pi_bar_pr": 0.22580523373858388,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.03822794157306861,
          "abs_C_h_over_pi_bar2": 0.1874359598640084,
          "S_P_meanslope_pp": 0.8190857991553571,
          "S_P_TV_pp": 0.5733600594087503,
          "chord_formula_pp": 0.191139707865343,
          "residual": 0.0062794609129001415,
          "residual_pp": 0.6279460912900141,
          "relative_residual": 3.28527284206377,
          "implied_abs_A_prime_kappa": 1.0713182105159424
        },
        {
          "T": 10,
          "tau_quantile": 0.5,
          "pi_bar_level_symmetric": 0.4516104674771678,
          "pi_bar_pr": 0.2258052337385839,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.03822794157306861,
          "abs_C_h_over_pi_bar2": 0.18743595986400838,
          "S_P_meanslope_pp": 0.8190857991553573,
          "S_P_TV_pp": 0.5733600594087507,
          "chord_formula_pp": 0.191139707865343,
          "residual": 0.006279460912900143,
          "residual_pp": 0.6279460912900143,
          "relative_residual": 3.2852728420637707,
          "implied_abs_A_prime_kappa": 1.0713182105159427
        },
        {
          "T": 10,
          "tau_quantile": 0.7,
          "pi_bar_level_symmetric": 0.4516104674771677,
          "pi_bar_pr": 0.22580523373858385,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.03822794157306861,
          "abs_C_h_over_pi_bar2": 0.18743595986400846,
          "S_P_meanslope_pp": 0.8190857991553571,
          "S_P_TV_pp": 0.5733600594087505,
          "chord_formula_pp": 0.191139707865343,
          "residual": 0.0062794609129001415,
          "residual_pp": 0.6279460912900141,
          "relative_residual": 3.28527284206377,
          "implied_abs_A_prime_kappa": 1.0713182105159424
        },
        {
          "T": 10,
          "tau_quantile": 0.9,
          "pi_bar_level_symmetric": 0.4516104674771678,
          "pi_bar_pr": 0.2258052337385839,
          "abs_A_prime_kappa": 0.25,
          "abs_C_h": 0.03822794157306861,
          "abs_C_h_over_pi_bar2": 0.18743595986400838,
          "S_P_meanslope_pp": 0.8190857991553575,
          "S_P_TV_pp": 0.5733600594087507,
          "chord_formula_pp": 0.191139707865343,
          "residual": 0.006279460912900145,
          "residual_pp": 0.6279460912900146,
          "relative_residual": 3.2852728420637716,
          "implied_abs_A_prime_kappa": 1.071318210515943
        }
      ]
    },
    {
      "name": "t1_block4_window_margin",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 4: for (T',T) = (5,10) at each tau report W_T, C_T, W_T C_T, the direct ratio and Omega at both windows. W_T <= 1 at every node (a violation is a bug in the clock, not evidence against the theorem); C_T UNSIGNED and not to be constrained; W_T C_T reported as found; identity residual below 1e-10",
      "tol": 1e-10,
      "max_identity_residual": 1.1102230246251565e-16,
      "n_W_T_above_one": 0,
      "W_T_violations": [],
      "n_nodes_with_W_T_C_T_above_one": 0,
      "suspected_forced_attenuation_bug": true,
      "acceptance_rule_with_teeth": "a run returning W_T C_T <= 1 at EVERY node, including the low-Omega calibrations, is to be treated as suspect and audited for a forced-attenuation bug before it is believed, because the O-1 record has the analogous product above one at Omega = 0.037, 0.129 and 0.286 (reproduced in t1_block6_O1_benchmark)",
      "audit_note": "FLAGGED: this run returns W_T C_T <= 1 at every node. The audit trail is: (i) W_T = (1-Omega(5))/(1-Omega(10)) is 0.8559-0.9730 across the ladder because the T = H = 10 corner drives Omega(10) to 6.81e-04, so the window comparison here is a corner-vs-interior comparison, not the two-interior-window comparison the theorem contemplates; (ii) C_T is computed from independently enumerated S_P levels, both reported above, and is NOT clipped or signed anywhere in this script; (iii) the H = 12 column below re-runs the same comparison with T = 10 strictly interior. The product staying below one is therefore a property of this calibration's corner, and is reported as suspect rather than as confirmation.",
      "rows": [
        {
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "W_T": 0.8559257023196463,
          "C_T": 0.212402464112231,
          "W_T_C_T": 0.18180072826968477,
          "direct_ratio_S5_over_S10": 0.1818007282696847,
          "identity_residual": 5.551115123125783e-17,
          "Omega_T5": 0.14465741548984065,
          "Omega_T10": 0.0006812715261460647,
          "S_P_TV_pp_T5": 0.12178308944195376,
          "S_P_TV_pp_T10": 0.5733600594087505,
          "corner_T10_equals_H": true
        },
        {
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "W_T": 0.8559257023196463,
          "C_T": 0.21240246411223113,
          "W_T_C_T": 0.18180072826968488,
          "direct_ratio_S5_over_S10": 0.18180072826968477,
          "identity_residual": 1.1102230246251565e-16,
          "Omega_T5": 0.1446574154898407,
          "Omega_T10": 0.0006812715261460647,
          "S_P_TV_pp_T5": 0.1217830894419538,
          "S_P_TV_pp_T10": 0.5733600594087503,
          "corner_T10_equals_H": true
        },
        {
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "W_T": 0.8621910742975696,
          "C_T": 0.23837381539930197,
          "W_T_C_T": 0.2055237759835347,
          "direct_ratio_S5_over_S10": 0.2055237759835348,
          "identity_residual": 1.1102230246251565e-16,
          "Omega_T5": 0.1383963119314466,
          "Omega_T10": 0.0006812715261460647,
          "S_P_TV_pp_T5": 0.13667402495883435,
          "S_P_TV_pp_T10": 0.5733600594087507,
          "corner_T10_equals_H": true
        },
        {
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "W_T": 0.9175873393628272,
          "C_T": 0.4685563755555411,
          "W_T_C_T": 0.4299413979874986,
          "direct_ratio_S5_over_S10": 0.42994139798749853,
          "identity_residual": 5.551115123125783e-17,
          "Omega_T5": 0.08303778676423275,
          "Omega_T10": 0.0006812715261460647,
          "S_P_TV_pp_T5": 0.26865151132487386,
          "S_P_TV_pp_T10": 0.5733600594087505,
          "corner_T10_equals_H": true
        },
        {
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "W_T": 0.9729836044280844,
          "C_T": 0.7938587970869181,
          "W_T_C_T": 0.7724115937965729,
          "direct_ratio_S5_over_S10": 0.7724115937965728,
          "identity_residual": 1.1102230246251565e-16,
          "Omega_T5": 0.02767926159701934,
          "Omega_T10": 0.0006812715261460648,
          "S_P_TV_pp_T5": 0.4551669270599147,
          "S_P_TV_pp_T10": 0.5733600594087507,
          "corner_T10_equals_H": true
        }
      ]
    },
    {
      "name": "t1_block5_local_form",
      "kind": "substantive",
      "pass": true,
      "vacuous": true,
      "request": "Block 5: on an interpolated window grid T in {4.0, 4.25, ..., 12.0}, compute Omega_{r_T} and d_{r_T} S_P by central differences",
      "outcome": "LOCAL FORM NOT EVALUABLE -- INTEGER WINDOW",
      "why": "numerical_v4's legal clock computes the filing date as f = c + T with c an integer trading date and indexes the stake path at int(f)+1, so a fractional T is truncated rather than interpolated. The implementation does not admit fractional windows, and the request's own instruction for that case is to report this line rather than skip the block silently.",
      "consequences": "the (21a) integral check of rho over r in [-10,-5] against log(W_T C_T), and the count of nodes with rho > 0 inside an interval whose endpoint comparison gives W_T C_T <= 1, are both unavailable. The finite form of Step 20 is still exercised by block 4.",
      "n_evaluated": 0
    },
    {
      "name": "t1_block6_O1_benchmark",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 6 / WHERE IT FAILS case 1: in the STATIC repo model at the four committed k_D values, reproduce the ratios 1.06397 / 1.18373 / 1.13631 / 0.37798 at Omega = 0.037252 / 0.128950 / 0.285804 / 0.500000, and the bisected boundary k_D* = 1.28618, Omega* = 0.3428",
      "model": "numerical/ (draft_v2 static model), NOT the two-round model; everything recomputed, no CSV read",
      "grid": {
        "kappa_min": 0.15,
        "kappa_max": 0.85,
        "n": 41
      },
      "baseline_cutoffs": {
        "k1": 0.8217375898536412,
        "k0": 0.8217375898536412,
        "kD": 2.2611270959836602
      },
      "tol_ratio": 0.0001,
      "tol_Omega_star": 0.001,
      "max_abs_diff_vs_committed": 2.09036286058506e-06,
      "kD_star": 1.2861843109130855,
      "Omega_star": 0.3428395620440514,
      "committed_kD_star": 1.28618,
      "committed_Omega_star": 0.3428,
      "directions": "a ratio above 1 means the flag makes premia MORE liquidity-sensitive, i.e. attenuation FAILS",
      "rows": [
        {
          "kD": 2.2611270959836602,
          "Omega": 0.03725222653750415,
          "committed_Omega": 0.037252,
          "TV_flagged": 0.017594385063427954,
          "TV_pooled": 0.016536509954342415,
          "ratio_TV": 1.0639720903628607,
          "committed_ratio": 1.06397,
          "abs_diff_vs_committed": 2.09036286058506e-06,
          "attenuation_holds": false,
          "W_O1": 0.9627477734624958,
          "C_O1": 1.1051410553112102,
          "committed_C_O1": 1.1051,
          "abs_diff_C_O1": 4.105531121023631e-05,
          "S_P_TV_flagged_regime": 0.01827517606210631,
          "S_P_TV_pooled_regime": 0.016536509954342415
        },
        {
          "kD": 1.8,
          "Omega": 0.1289495176461697,
          "committed_Omega": 0.12895,
          "TV_flagged": 0.015980887992609074,
          "TV_pooled": 0.013500439216179373,
          "ratio_TV": 1.183730968801152,
          "committed_ratio": 1.18373,
          "abs_diff_vs_committed": 9.688011519681794e-07,
          "attenuation_holds": false,
          "W_O1": 0.8710504823538303,
          "C_O1": 1.358969420006942,
          "committed_C_O1": 1.359,
          "abs_diff_C_O1": 3.0579993057999744e-05,
          "S_P_TV_flagged_regime": 0.01834668405145026,
          "S_P_TV_pooled_regime": 0.013500439216179373
        },
        {
          "kD": 1.4,
          "Omega": 0.2858038224766658,
          "committed_Omega": 0.285804,
          "TV_flagged": 0.012110436085768651,
          "TV_pooled": 0.010657668098057915,
          "ratio_TV": 1.136311993800545,
          "committed_ratio": 1.13631,
          "abs_diff_vs_committed": 1.9938005451081153e-06,
          "attenuation_holds": false,
          "W_O1": 0.7141961775233342,
          "C_O1": 1.591036230046778,
          "committed_C_O1": 1.591,
          "abs_diff_C_O1": 3.623004677799635e-05,
          "S_P_TV_flagged_regime": 0.01695673607182388,
          "S_P_TV_pooled_regime": 0.010657668098057915
        },
        {
          "kD": 1.0,
          "Omega": 0.5,
          "committed_Omega": 0.5,
          "TV_flagged": 0.003987574444282053,
          "TV_pooled": 0.010549741489497257,
          "ratio_TV": 0.37797840338096084,
          "committed_ratio": 0.37798,
          "abs_diff_vs_committed": 1.5966190391458746e-06,
          "attenuation_holds": true,
          "W_O1": 0.5,
          "C_O1": 0.7559568067619217,
          "committed_C_O1": 0.756,
          "abs_diff_C_O1": 4.319323807833175e-05,
          "S_P_TV_flagged_regime": 0.007975148888564106,
          "S_P_TV_pooled_regime": 0.010549741489497257
        }
      ]
    },
    {
      "name": "t1_block6_composition_factors",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "Block 6: compute S_P^TV directly in each regime and report C_O1 = S_P^TV(Omega)/S_P^TV(0); predicted C_O1 = 1.1051, 1.3590, 1.5910, 0.7560 to within 1e-3, with C_O1 > 1 at the first three rows and < 1 at the fourth",
      "tol": 0.001,
      "computed_C_O1": [
        1.1051410553112102,
        1.358969420006942,
        1.591036230046778,
        0.7559568067619217
      ],
      "predicted_C_O1": [
        1.1051,
        1.359,
        1.591,
        0.756
      ],
      "max_abs_diff": 4.319323807833175e-05,
      "signs_as_predicted": true,
      "derivation": "W_O1 = 1 - Omega and S = W C, so C_O1 = ratio_TV / (1 - Omega); S_P^TV is reported in levels in the block-6 rows, so the ratio is not taken on an unreported denominator",
      "reading": "a mismatch here would falsify the claim that the static model's O-1 experiment satisfies L1 + flagged-cell kappa-invariance + PE-Omega, and would mean the committed ratios cannot be read through the factorisation at all -- reported as a finding, not as a tolerance failure",
      "rows": [
        {
          "kD": 2.2611270959836602,
          "Omega": 0.03725222653750415,
          "ratio_TV": 1.0639720903628607,
          "W_O1": 0.9627477734624958,
          "C_O1": 1.1051410553112102,
          "S_P_TV_flagged_regime": 0.01827517606210631,
          "S_P_TV_pooled_regime": 0.016536509954342415
        },
        {
          "kD": 1.8,
          "Omega": 0.1289495176461697,
          "ratio_TV": 1.183730968801152,
          "W_O1": 0.8710504823538303,
          "C_O1": 1.358969420006942,
          "S_P_TV_flagged_regime": 0.01834668405145026,
          "S_P_TV_pooled_regime": 0.013500439216179373
        },
        {
          "kD": 1.4,
          "Omega": 0.2858038224766658,
          "ratio_TV": 1.136311993800545,
          "W_O1": 0.7141961775233342,
          "C_O1": 1.591036230046778,
          "S_P_TV_flagged_regime": 0.01695673607182388,
          "S_P_TV_pooled_regime": 0.010657668098057915
        },
        {
          "kD": 1.0,
          "Omega": 0.5,
          "ratio_TV": 0.37797840338096084,
          "W_O1": 0.5,
          "C_O1": 0.7559568067619217,
          "S_P_TV_flagged_regime": 0.007975148888564106,
          "S_P_TV_pooled_regime": 0.010549741489497257
        }
      ]
    },
    {
      "name": "t1_H12_window_robustness",
      "kind": "substantive",
      "pass": true,
      "vacuous": false,
      "request": "design section 13, ruling 2: the H = 12 re-run is MANDATORY for T1's window comparison",
      "scope": "Omega, W_T and the chord-route C_T -- none of which touch the pooled enumeration. At H = 12, T = 10 is strictly interior (T < H), so this column is exactly the corner audit block 4 asks for.",
      "not_evaluable_at_H12": "the enumerated S_P (and hence the enumerated C_T and the direct ratio) run through the pooled enumeration; at H = 12 the feasible history count is 8,503,056 and 8,503,056 x N_theta 14 = 1.19e8 exceeds the design build-step-4 gate of 1e8 (~2.5 GB working set). The gate is respected, not overridden.",
      "policy": "cutoffs frozen at the H = 10 baseline equilibrium; H = 12 cannot be re-solved for the same reason",
      "n_W_T_above_one": 0,
      "n_nodes_with_W_T_C_T_above_one": 0,
      "rows": [
        {
          "tau_quantile": 0.1,
          "tau": 0.08462696676439771,
          "H": 12,
          "Omega_T5": 0.16867782523442393,
          "Omega_T10": 0.028913438392177894,
          "pi_bar_pr_T5": 0.06935319074143932,
          "pi_bar_pr_T10": 0.20329725484974828,
          "W_T": 0.8560742241033189,
          "C_T_chord_route": 0.12832579520148654,
          "W_T_C_T_chord_route": 0.10985640555955399,
          "S_P_chord_pp_T5": 0.020207654173085773,
          "S_P_chord_pp_T10": 0.1574714899787481,
          "T10_is_corner": false,
          "degenerate_T5": [],
          "degenerate_T10": []
        },
        {
          "tau_quantile": 0.3,
          "tau": 0.08788437014471917,
          "H": 12,
          "Omega_T5": 0.16867782523442398,
          "Omega_T10": 0.028913438392177897,
          "pi_bar_pr_T5": 0.06935319074143934,
          "pi_bar_pr_T10": 0.2032972548497483,
          "W_T": 0.8560742241033188,
          "C_T_chord_route": 0.1283257952014873,
          "W_T_C_T_chord_route": 0.10985640555955463,
          "S_P_chord_pp_T5": 0.02020765417308591,
          "S_P_chord_pp_T10": 0.15747148997874827,
          "T10_is_corner": false,
          "degenerate_T5": [],
          "degenerate_T10": []
        },
        {
          "tau_quantile": 0.5,
          "tau": 0.09076405861553302,
          "H": 12,
          "Omega_T5": 0.13839631193144664,
          "Omega_T10": 0.028913438392177904,
          "pi_bar_pr_T5": 0.10206126073370039,
          "pi_bar_pr_T10": 0.2032972548497483,
          "W_T": 0.8872573487599307,
          "C_T_chord_route": 0.2712097344036416,
          "W_T_C_T_chord_route": 0.24063282990486,
          "S_P_chord_pp_T5": 0.04270780097328202,
          "S_P_chord_pp_T10": 0.15747148997874827,
          "T10_is_corner": false,
          "degenerate_T5": [],
          "degenerate_T10": []
        },
        {
          "tau_quantile": 0.7,
          "tau": 0.09337594348697996,
          "H": 12,
          "Omega_T5": 0.08303778676423275,
          "Omega_T10": 0.02891343839217789,
          "pi_bar_pr_T5": 0.15627130731880298,
          "pi_bar_pr_T10": 0.20329725484974825,
          "W_T": 0.944264136162649,
          "C_T_chord_route": 0.6112299649207037,
          "W_T_C_T_chord_route": 0.5771625348225745,
          "S_P_chord_pp_T5": 0.09625129329572114,
          "S_P_chord_pp_T10": 0.1574714899787481,
          "T10_is_corner": false,
          "degenerate_T5": [],
          "degenerate_T10": []
        },
        {
          "tau_quantile": 0.9,
          "tau": 0.09602833824479486,
          "H": 12,
          "Omega_T5": 0.027679261597019337,
          "Omega_T10": 0.027679261597019337,
          "pi_bar_pr_T5": 0.20430851790510443,
          "pi_bar_pr_T10": 0.20430851790510443,
          "W_T": 1.0,
          "C_T_chord_route": 1.0,
          "W_T_C_T_chord_route": 1.0,
          "S_P_chord_pp_T5": 0.1589261538163944,
          "S_P_chord_pp_T10": 0.1589261538163944,
          "T10_is_corner": false,
          "degenerate_T5": [],
          "degenerate_T10": []
        }
      ]
    }
  ],
  "n_fail": 1,
  "n_vacuous": 1,
  "provenance": {
    "model_card_stamp": "2026-08-20 (commit 0c9185b)",
    "commit": "0c9185b -- MODEL_CARD stamp as recorded in numerical_v4/smoke.py; this script does not shell out to git",
    "params_hash": "8ef7c5c2d3896bf8",
    "design": "research/model_v4/impl_design.md section 13 APPROVED",
    "request": "research/model_v4/proofs/T1_proof.md, NUMERICAL CHECK REQUEST (six blocks); O-1 record in HANDOFF_sign.md",
    "measurement": "total variation over the kappa grid (Step 7), with mean absolute slope reported alongside",
    "H12_robustness": "MANDATORY for T1's window comparison (design section 13, ruling 2); delivered for the Omega/W_T/chord half"
  },
  "grid": {
    "kappa": [
      0.15,
      0.16,
      0.17,
      0.18,
      0.19,
      0.2,
      0.21,
      0.22,
      0.23,
      0.24,
      0.25,
      0.26,
      0.27,
      0.28,
      0.29,
      0.3,
      0.31,
      0.32,
      0.33,
      0.34,
      0.35,
      0.36,
      0.37,
      0.38,
      0.39,
      0.4,
      0.41,
      0.42,
      0.43,
      0.44,
      0.45,
      0.46,
      0.47,
      0.48,
      0.49,
      0.5,
      0.51,
      0.52,
      0.53,
      0.54,
      0.55,
      0.56,
      0.57,
      0.58,
      0.59,
      0.6,
      0.61,
      0.62,
      0.63,
      0.64,
      0.65,
      0.66,
      0.67,
      0.68,
      0.69,
      0.7,
      0.71,
      0.72,
      0.73,
      0.74,
      0.75,
      0.76,
      0.77,
      0.78,
      0.79,
      0.8,
      0.81,
      0.82,
      0.83,
      0.84,
      0.85
    ],
    "tau": [
      0.08462696676439771,
      0.08788437014471917,
      0.09076405861553302,
      0.09337594348697996,
      0.09602833824479486
    ],
    "tau_quantiles": [
      0.1,
      0.3,
      0.5,
      0.7,
      0.9
    ],
    "T": [
      5,
      10
    ],
    "H": 10,
    "H_robustness": 12,
    "M": 2,
    "tau_frozen_from": "percentiles of the seed-equilibrium (tau=0.05) Voice b*(s) terminal-stake distribution, design 6.2",
    "policy": "frozen at the baseline equilibrium cutoffs at every node (H5)",
    "A_prime_kappa": 0.25,
    "n_v4_evaluations": 710
  },
  "counts": {
    "n_hist": 4194304,
    "n_hist_feasible": 826686,
    "n_theta": 12,
    "discarded_mass": 0.0
  },
  "degenerate_nodes": [
    {
      "T": 10,
      "tau_quantile": 0.1,
      "tau": 0.08462696676439771,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau_quantile": 0.3,
      "tau": 0.08788437014471917,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau_quantile": 0.5,
      "tau": 0.09076405861553302,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau_quantile": 0.7,
      "tau": 0.09337594348697996,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    },
    {
      "T": 10,
      "tau_quantile": 0.9,
      "tau": 0.09602833824479486,
      "reasons": [
        "flagged cell mass 0.0006813 < 0.01"
      ]
    }
  ],
  "multiple_root_nodes": 0,
  "node_table": [
    {
      "tau": 0.08462696676439771,
      "T": 5,
      "corner": false,
      "Omega": 0.14465741548984065,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.0010416626247291266,
      "S_P_TV": 0.0012178308944195376,
      "S_TV_pp": 0.10416626247291266,
      "S_P_TV_pp": 0.12178308944195376,
      "S_meanslope": 0.0014880894638987507,
      "S_P_meanslope": 0.001739758420599338,
      "max_pointwise_factorisation_residual": 1.1937065919065404e-16,
      "TV_factorisation_residual": 2.168404344971009e-19,
      "multiple_root_nodes": 0,
      "degenerate": [],
      "tau_quantile": 0.1,
      "pi_bar_pr": 0.09548835352967079,
      "pi_bar_level_symmetric": 0.19097670705934158
    },
    {
      "tau": 0.08788437014471917,
      "T": 5,
      "corner": false,
      "Omega": 0.1446574154898407,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.0010416626247291266,
      "S_P_TV": 0.001217830894419538,
      "S_TV_pp": 0.10416626247291266,
      "S_P_TV_pp": 0.1217830894419538,
      "S_meanslope": 0.001488089463898751,
      "S_P_meanslope": 0.0017397584205993384,
      "max_pointwise_factorisation_residual": 1.1535911115245767e-16,
      "TV_factorisation_residual": 0.0,
      "multiple_root_nodes": 0,
      "degenerate": [],
      "tau_quantile": 0.3,
      "pi_bar_pr": 0.09548835352967079,
      "pi_bar_level_symmetric": 0.19097670705934158
    },
    {
      "tau": 0.09076405861553302,
      "T": 5,
      "corner": false,
      "Omega": 0.1383963119314466,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.0011775884396770524,
      "S_P_TV": 0.0013667402495883435,
      "S_TV_pp": 0.11775884396770524,
      "S_P_TV_pp": 0.13667402495883435,
      "S_meanslope": 0.0016822691995386448,
      "S_P_meanslope": 0.001952486070840489,
      "max_pointwise_factorisation_residual": 8.196568423990414e-17,
      "TV_factorisation_residual": 6.505213034913027e-19,
      "multiple_root_nodes": 0,
      "degenerate": [],
      "tau_quantile": 0.5,
      "pi_bar_pr": 0.10206126073370039,
      "pi_bar_level_symmetric": 0.20412252146740079
    },
    {
      "tau": 0.09337594348697996,
      "T": 5,
      "corner": false,
      "Omega": 0.08303778676423275,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.0024634328441359003,
      "S_P_TV": 0.0026865151132487385,
      "S_TV_pp": 0.24634328441359002,
      "S_P_TV_pp": 0.26865151132487386,
      "S_meanslope": 0.003519189777336997,
      "S_P_meanslope": 0.0038378787332124806,
      "max_pointwise_factorisation_residual": 1.3704315460216776e-16,
      "TV_factorisation_residual": 8.673617379884035e-19,
      "multiple_root_nodes": 0,
      "degenerate": [],
      "tau_quantile": 0.7,
      "pi_bar_pr": 0.15627130731880298,
      "pi_bar_level_symmetric": 0.31254261463760596
    },
    {
      "tau": 0.09602833824479486,
      "T": 5,
      "corner": false,
      "Omega": 0.02767926159701934,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.004425682426155118,
      "S_P_TV": 0.004551669270599147,
      "S_TV_pp": 0.44256824261551186,
      "S_P_TV_pp": 0.4551669270599147,
      "S_meanslope": 0.006322403465935877,
      "S_P_meanslope": 0.006502384672284489,
      "max_pointwise_factorisation_residual": 1.4051260155412137e-16,
      "TV_factorisation_residual": 0.0,
      "multiple_root_nodes": 0,
      "degenerate": [],
      "tau_quantile": 0.9,
      "pi_bar_pr": 0.20430851790510446,
      "pi_bar_level_symmetric": 0.4086170358102089
    },
    {
      "tau": 0.08462696676439771,
      "T": 10,
      "corner": true,
      "Omega": 0.0006812715261460647,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.005729694455260463,
      "S_P_TV": 0.005733600594087505,
      "S_TV_pp": 0.5729694455260462,
      "S_P_TV_pp": 0.5733600594087505,
      "S_meanslope": 0.008185277793229223,
      "S_P_meanslope": 0.008190857991553575,
      "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
      "TV_factorisation_residual": 3.469446951953614e-18,
      "multiple_root_nodes": 0,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "tau_quantile": 0.1,
      "pi_bar_pr": 0.22580523373858385,
      "pi_bar_level_symmetric": 0.4516104674771677
    },
    {
      "tau": 0.08788437014471917,
      "T": 10,
      "corner": true,
      "Omega": 0.0006812715261460647,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.005729694455260461,
      "S_P_TV": 0.005733600594087503,
      "S_TV_pp": 0.5729694455260461,
      "S_P_TV_pp": 0.5733600594087503,
      "S_meanslope": 0.008185277793229223,
      "S_P_meanslope": 0.008190857991553571,
      "max_pointwise_factorisation_residual": 1.717376241217039e-16,
      "TV_factorisation_residual": 3.469446951953614e-18,
      "multiple_root_nodes": 0,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "tau_quantile": 0.3,
      "pi_bar_pr": 0.22580523373858388,
      "pi_bar_level_symmetric": 0.45161046747716777
    },
    {
      "tau": 0.09076405861553302,
      "T": 10,
      "corner": true,
      "Omega": 0.0006812715261460647,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.005729694455260461,
      "S_P_TV": 0.005733600594087507,
      "S_TV_pp": 0.5729694455260461,
      "S_P_TV_pp": 0.5733600594087507,
      "S_meanslope": 0.008185277793229223,
      "S_P_meanslope": 0.008190857991553573,
      "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
      "TV_factorisation_residual": 0.0,
      "multiple_root_nodes": 0,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "tau_quantile": 0.5,
      "pi_bar_pr": 0.2258052337385839,
      "pi_bar_level_symmetric": 0.4516104674771678
    },
    {
      "tau": 0.09337594348697996,
      "T": 10,
      "corner": true,
      "Omega": 0.0006812715261460647,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.005729694455260458,
      "S_P_TV": 0.005733600594087505,
      "S_TV_pp": 0.5729694455260458,
      "S_P_TV_pp": 0.5733600594087505,
      "S_meanslope": 0.008185277793229218,
      "S_P_meanslope": 0.008190857991553571,
      "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
      "TV_factorisation_residual": 8.673617379884035e-19,
      "multiple_root_nodes": 0,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "tau_quantile": 0.7,
      "pi_bar_pr": 0.22580523373858385,
      "pi_bar_level_symmetric": 0.4516104674771677
    },
    {
      "tau": 0.09602833824479486,
      "T": 10,
      "corner": true,
      "Omega": 0.0006812715261460648,
      "Omega_flat_residual": 0.0,
      "S_TV": 0.005729694455260461,
      "S_P_TV": 0.005733600594087507,
      "S_TV_pp": 0.5729694455260461,
      "S_P_TV_pp": 0.5733600594087507,
      "S_meanslope": 0.008185277793229221,
      "S_P_meanslope": 0.008190857991553575,
      "max_pointwise_factorisation_residual": 2.0643209364124004e-16,
      "TV_factorisation_residual": 0.0,
      "multiple_root_nodes": 0,
      "degenerate": [
        "flagged cell mass 0.0006813 < 0.01"
      ],
      "tau_quantile": 0.9,
      "pi_bar_pr": 0.2258052337385839,
      "pi_bar_level_symmetric": 0.4516104674771678
    }
  ],
  "kappa_profiles": {
    "T=5,q=0.1": {
      "Delta_act_pp": [
        0.20871798099650177,
        0.20931555246520958,
        0.2099940462028189,
        0.2107564740295878,
        0.21160533725863856,
        0.21254259413849758,
        0.21356962874158292,
        0.21468722196753767,
        0.2158955245107584,
        0.21719403067723847,
        0.21858155098936077,
        0.22005618078603847,
        0.22161526172488358,
        0.2232553334305761,
        0.2249720736739629,
        0.22676022748415303,
        0.2286135284209521,
        0.23052461859841625,
        0.2324849774519417,
        0.23448487196438828,
        0.2365133422663554,
        0.23855823540307972,
        0.24060629609972162,
        0.24264331656781743,
        0.2446543384711121,
        0.2466238904803867,
        0.24853623625151577,
        0.25037560218305993,
        0.25212635382643744,
        0.25377309586495156,
        0.25530068419987717,
        0.2566941600429837,
        0.2579386431052941,
        0.2590192480537697,
        0.25992110421044917,
        0.26062954945809996,
        0.26113052908931367,
        0.2614111720143343,
        0.26146047525505706,
        0.26127003787495995,
        0.2608348420018674,
        0.260154117593308,
        0.25923227723117764,
        0.2580797757742032,
        0.2567136302834345,
        0.2551572992706969,
        0.25343967259486117,
        0.25159309702095495,
        0.24965069780688312,
        0.2476436008001348,
        0.24559871358930452,
        0.24353742288852429,
        0.24147517545179153,
        0.23942169958151832,
        0.2373816400864009,
        0.23535552507300742,
        0.2333411412692401,
        0.2313354397722529,
        0.22933688984770992,
        0.2273477649109715,
        0.22537557077113587,
        0.22343311789632514,
        0.22153734307564008,
        0.21970737652846264,
        0.21796248712471497,
        0.21632040554771975,
        0.21479607545056004,
        0.2134006741329635,
        0.21214105797658744,
        0.21101994072363633,
        0.21003670704069968
      ],
      "M_P_pp": [
        0.14624321076187763,
        0.14694184482912687,
        0.14773508691703,
        0.14862645821149872,
        0.14961888305322082,
        0.15071465087401248,
        0.15191537982365727,
        0.15322198286926006,
        0.15463463619098466,
        0.15615274857074382,
        0.15777492936385476,
        0.15949895178876677,
        0.1613217079183917,
        0.1632391521511394,
        0.16524623127297447,
        0.16733680158079348,
        0.16950353684028066,
        0.17173783478366977,
        0.1740297338297673,
        0.17636785489220905,
        0.178739384544423,
        0.18113011449725866,
        0.18352454771469842,
        0.18590607355590552,
        0.1882572038979618,
        0.19055985086648916,
        0.19279561675229995,
        0.1949460602878542,
        0.1969929028923063,
        0.19891814555920467,
        0.2007040829866045,
        0.20233322652317298,
        0.2037881792927969,
        0.2050515385222389,
        0.20610591857183727,
        0.20693417763490793,
        0.20751988404107335,
        0.20784798991362424,
        0.2079056314266456,
        0.20768298685878958,
        0.20717418970432333,
        0.20637833968950242,
        0.20530059566175907,
        0.20395318062847806,
        0.20235598961342885,
        0.2005364484834512,
        0.19852833301376543,
        0.1963694605253067,
        0.1940985584923111,
        0.19175201683392082,
        0.18936129380917938,
        0.18695139310025974,
        0.18454037385010302,
        0.18213960963298037,
        0.17975453079783066,
        0.17738575476576418,
        0.17503069395124743,
        0.17268578381429242,
        0.17034923473941208,
        0.16802370462696298,
        0.16571796868495436,
        0.16344700391599784,
        0.16123061149614565,
        0.15909115698947524,
        0.15705116805948768,
        0.15513137404159064,
        0.1533492458922799,
        0.15171785124074905,
        0.15024520603497163,
        0.14893448297119113,
        0.14778496264945978
      ]
    },
    "T=5,q=0.3": {
      "Delta_act_pp": [
        0.2087179809965017,
        0.2093155524652095,
        0.20999404620281886,
        0.21075647402958778,
        0.21160533725863842,
        0.2125425941384974,
        0.21356962874158275,
        0.21468722196753756,
        0.21589552451075833,
        0.21719403067723833,
        0.21858155098936072,
        0.22005618078603847,
        0.22161526172488352,
        0.22325533343057605,
        0.22497207367396288,
        0.22676022748415298,
        0.228613528420952,
        0.2305246185984161,
        0.23248497745194163,
        0.23448487196438814,
        0.23651334226635531,
        0.23855823540307966,
        0.24060629609972153,
        0.24264331656781743,
        0.24465433847111204,
        0.24662389048038677,
        0.24853623625151564,
        0.2503756021830598,
        0.2521263538264373,
        0.25377309586495156,
        0.2553006841998771,
        0.25669416004298357,
        0.25793864310529396,
        0.2590192480537697,
        0.25992110421044917,
        0.26062954945809985,
        0.2611305290893136,
        0.2614111720143342,
        0.261460475255057,
        0.2612700378749598,
        0.2608348420018674,
        0.260154117593308,
        0.2592322772311776,
        0.25807977577420316,
        0.25671363028343447,
        0.25515729927069686,
        0.253439672594861,
        0.25159309702095484,
        0.24965069780688307,
        0.24764360080013476,
        0.24559871358930443,
        0.24353742288852406,
        0.24147517545179145,
        0.23942169958151827,
        0.2373816400864009,
        0.23535552507300733,
        0.23334114126924002,
        0.23133543977225285,
        0.22933688984771006,
        0.22734776491097142,
        0.22537557077113574,
        0.22343311789632508,
        0.22153734307563988,
        0.21970737652846256,
        0.21796248712471494,
        0.21632040554771967,
        0.21479607545055995,
        0.21340067413296349,
        0.21214105797658736,
        0.2110199407236361,
        0.21003670704069963
      ],
      "M_P_pp": [
        0.14624321076187768,
        0.14694184482912687,
        0.14773508691703008,
        0.14862645821149875,
        0.14961888305322082,
        0.15071465087401248,
        0.15191537982365724,
        0.1532219828692601,
        0.15463463619098466,
        0.15615274857074377,
        0.15777492936385482,
        0.15949895178876683,
        0.16132170791839176,
        0.16323915215113943,
        0.16524623127297453,
        0.1673368015807935,
        0.16950353684028066,
        0.1717378347836697,
        0.17402973382976736,
        0.17636785489220905,
        0.178739384544423,
        0.18113011449725872,
        0.18352454771469845,
        0.1859060735559056,
        0.1882572038979618,
        0.1905598508664893,
        0.19279561675229992,
        0.1949460602878542,
        0.19699290289230628,
        0.19891814555920476,
        0.2007040829866045,
        0.20233322652317298,
        0.20378817929279694,
        0.20505153852223898,
        0.20610591857183735,
        0.20693417763490793,
        0.20751988404107338,
        0.20784798991362424,
        0.20790563142664564,
        0.20768298685878958,
        0.2071741897043234,
        0.20637833968950242,
        0.20530059566175907,
        0.20395318062847806,
        0.20235598961342885,
        0.20053644848345123,
        0.19852833301376538,
        0.19636946052530665,
        0.1940985584923111,
        0.19175201683392082,
        0.18936129380917938,
        0.18695139310025954,
        0.18454037385010302,
        0.18213960963298037,
        0.1797545307978307,
        0.17738575476576418,
        0.17503069395124746,
        0.17268578381429245,
        0.17034923473941233,
        0.16802370462696298,
        0.16571796868495428,
        0.16344700391599784,
        0.1612306114961456,
        0.15909115698947524,
        0.15705116805948774,
        0.15513137404159064,
        0.1533492458922799,
        0.15171785124074905,
        0.15024520603497166,
        0.14893448297119105,
        0.14778496264945978
      ]
    },
    "T=5,q=0.5": {
      "Delta_act_pp": [
        0.20949439126721728,
        0.21027109622474346,
        0.21114615646873228,
        0.21212060211001352,
        0.21319474293862326,
        0.21436826219394436,
        0.21564029245887412,
        0.21700947241255286,
        0.21847398506759058,
        0.22003157850610977,
        0.22167956939122793,
        0.22341482812644273,
        0.2252337429738354,
        0.22713215930215505,
        0.22910529009803451,
        0.23114759569242554,
        0.23325263498495422,
        0.23541289745902977,
        0.2376196341114027,
        0.2398627137946356,
        0.24213053594805142,
        0.24441002791285993,
        0.24668674361372975,
        0.24894506233378408,
        0.25116846658155906,
        0.25333986235392275,
        0.2554418973533817,
        0.25745723417379734,
        0.2593687458631262,
        0.26115962005409954,
        0.2628133829799953,
        0.2643138794209931,
        0.26564525765770763,
        0.26679200254222524,
        0.2677390419970682,
        0.268471939827342,
        0.26897718745322585,
        0.2692426065796006,
        0.26925786336643887,
        0.26901508562097015,
        0.26850958710758577,
        0.2677407194538837,
        0.26671283652804767,
        0.26543624332200677,
        0.2639278685574456,
        0.26221133125471285,
        0.2603161047908826,
        0.2582756515699941,
        0.25612474051935763,
        0.2538965337664321,
        0.25162014029712143,
        0.24931907306526552,
        0.2470106473453504,
        0.24470611103413115,
        0.2424112834393036,
        0.24012761191558948,
        0.23785370542104856,
        0.23558742710457986,
        0.23332839109154418,
        0.23108027164617057,
        0.22885211308167216,
        0.22665818236860313,
        0.22451653712688133,
        0.22244690197802974,
        0.2204685727474611,
        0.2185988593609276,
        0.2168521443709348,
        0.2152394118839522,
        0.21376810346020544,
        0.21244218350856353,
        0.21126249149795517
      ],
      "M_P_pp": [
        0.15434757499494428,
        0.1552490392856408,
        0.15626465731990252,
        0.15739562467156934,
        0.15864230089114034,
        0.16000431833787593,
        0.16148067026457352,
        0.16306977668628353,
        0.16476952875944456,
        0.16657731284868263,
        0.16849001460233046,
        0.17050400172801777,
        0.1726150823473105,
        0.17481843448543255,
        0.17710850220821883,
        0.17947885602943942,
        0.18192202023785586,
        0.18442927792951938,
        0.18699047478015005,
        0.18959385231241338,
        0.19222594660915387,
        0.19487158519725978,
        0.1975140015801022,
        0.20013506594104613,
        0.202715607643182,
        0.2052357869349295,
        0.20767546428144967,
        0.21001451743120278,
        0.21223306839123152,
        0.21431160428397814,
        0.21623100522062338,
        0.21797252102629672,
        0.21951775377674954,
        0.2208486961814742,
        0.22194785518921475,
        0.2227984757708382,
        0.2233848795117698,
        0.2236929319609993,
        0.22371063939081826,
        0.22342886512635002,
        0.222842170198758,
        0.22194980208990558,
        0.22075681401421582,
        0.21927516621753265,
        0.21752450662142242,
        0.2155322480848083,
        0.21333259818767433,
        0.21096439428007202,
        0.2084679900974737,
        0.20588187448099987,
        0.2032398320886169,
        0.20056915267565598,
        0.19788993280707587,
        0.19521522708896863,
        0.19255178956356547,
        0.18990130006898892,
        0.18726214412521813,
        0.18463184164641958,
        0.18200994477629395,
        0.17940071796296264,
        0.17681465827525022,
        0.17426832433605005,
        0.17178267429603836,
        0.16938060107198905,
        0.16708449990858362,
        0.164914461162899,
        0.16288717760529448,
        0.16101539767988837,
        0.1593077582580505,
        0.1577688605374358,
        0.15639967882785788
      ]
    },
    "T=5,q=0.7": {
      "Delta_act_pp": [
        0.21735072650384615,
        0.21933841061770967,
        0.22149818968977783,
        0.2238303558897988,
        0.22633460826363178,
        0.22900997616312965,
        0.23185474678917997,
        0.2348664007853178,
        0.23804155738858726,
        0.24137592797559151,
        0.24486427417825196,
        0.24850036443788825,
        0.25227692135105384,
        0.2561855519081578,
        0.2602166541801405,
        0.26435929748180265,
        0.26860107857141247,
        0.2729279636354488,
        0.2773241336796942,
        0.28177185792708953,
        0.28625142390543895,
        0.290741152090694,
        0.29521751587643946,
        0.2996553741636185,
        0.3040283055797004,
        0.30830901341995376,
        0.3124697530300029,
        0.31648272275007744,
        0.32032035912271833,
        0.3239554889396905,
        0.3273613156628959,
        0.33051125509268264,
        0.3333786813127772,
        0.33593668958014244,
        0.33815801065706036,
        0.3400151999263163,
        0.34148116380794985,
        0.342529993147993,
        0.3431379959371172,
        0.34328480847179776,
        0.3429545211797668,
        0.34213683180492704,
        0.34082826322874693,
        0.33903342194393454,
        0.3367661492730378,
        0.33405028063366643,
        0.3309196268990243,
        0.32741679226948567,
        0.3235906426047025,
        0.3194926635956549,
        0.31517290684912264,
        0.31067639903089456,
        0.30604067916742594,
        0.30129474491025116,
        0.296459402049549,
        0.2915488987046819,
        0.28657365607589763,
        0.28154370175937476,
        0.2764720644348237,
        0.27137720576928476,
        0.26628388690266674,
        0.26122254452813676,
        0.25622776177691503,
        0.2513365149523056,
        0.24658663424727556,
        0.24201540872838054,
        0.23765782684100414,
        0.23354428864293086,
        0.2296987132268462,
        0.22613837109896456,
        0.22287560602615933
      ],
      "M_P_pp": [
        0.20708868504657468,
        0.20925636882369508,
        0.2116117320446578,
        0.21415509333736726,
        0.21688612449403394,
        0.2198037669670614,
        0.2229061528505665,
        0.22619053464151337,
        0.2296532254235741,
        0.23328954820642667,
        0.23709379024858326,
        0.24105915567711636,
        0.2451777080652665,
        0.24944029435364926,
        0.253836443086712,
        0.25835423372395494,
        0.26298013981733853,
        0.26769885668656224,
        0.2724931328091652,
        0.27734363175360943,
        0.28222885593590363,
        0.2871251625889464,
        0.2920068945961458,
        0.29684663414388435,
        0.30161556720673194,
        0.30628392515917974,
        0.31082145086088425,
        0.3151978250038422,
        0.31938298805336285,
        0.3233473060639649,
        0.327061555870603,
        0.3304967458755119,
        0.33362383898655307,
        0.3364134940349749,
        0.33883597234962587,
        0.3408613439979321,
        0.34246006187362354,
        0.34360387055505437,
        0.3442669325442488,
        0.3444270400520189,
        0.3440668427753335,
        0.3431751055117506,
        0.34174803626364886,
        0.3397906586761049,
        0.3373180675069486,
        0.33435625664912977,
        0.3309420988033067,
        0.32712205629885294,
        0.32294942016450057,
        0.31848033850563207,
        0.31376939547637817,
        0.30886569524388885,
        0.3038101762742356,
        0.2986344621731853,
        0.29336124285083254,
        0.288006056700316,
        0.2825802686395107,
        0.2770948143384297,
        0.2715639023211784,
        0.2660076660968303,
        0.2604531091117123,
        0.25493342432920674,
        0.2494863266417284,
        0.24415214083340664,
        0.2389721229041305,
        0.233986938724333,
        0.22923474520482107,
        0.22474869535598646,
        0.2205548743232589,
        0.21667211658636382,
        0.2131138837325893
      ]
    },
    "T=5,q=0.9": {
      "Delta_act_pp": [
        0.24718672732299737,
        0.2519089795817564,
        0.2568537445857793,
        0.2620241402647271,
        0.2674224542892067,
        0.2730498285960145,
        0.27890598844602055,
        0.2849890169387786,
        0.29129517168319863,
        0.2978187343175814,
        0.3045518776379627,
        0.31148453153571176,
        0.31860423017196843,
        0.3258959306487487,
        0.33334180814669323,
        0.34092105190433447,
        0.34860970559632587,
        0.356380607899351,
        0.3642034880119495,
        0.3720452535687326,
        0.3798704769606992,
        0.38764204785879686,
        0.39532192467146515,
        0.40287189462315476,
        0.41025424598174504,
        0.4174322667329403,
        0.4243705083151008,
        0.43103478644684334,
        0.43739192977508884,
        0.4434093277303162,
        0.449054367111038,
        0.4542938751812385,
        0.45909369579952486,
        0.46341850653048733,
        0.46723193931703283,
        0.47049700802508254,
        0.47317679517020295,
        0.47523532769245136,
        0.4766385835499212,
        0.4773556042061431,
        0.4773597195791536,
        0.47662990227654967,
        0.4751522487087526,
        0.4729215357294021,
        0.46994272493786304,
        0.46623218753497914,
        0.46181831734519685,
        0.4567411366227943,
        0.4510505709696258,
        0.4448033583868212,
        0.4380590072113664,
        0.4308755966766463,
        0.42330629868793646,
        0.4153972828094231,
        0.40718731816339243,
        0.39870904660106843,
        0.3899915799616932,
        0.3810637452924044,
        0.3719570745269795,
        0.3627077394416932,
        0.3533571200905467,
        0.34395124726764187,
        0.3345396159511387,
        0.3251738002285484,
        0.3159060902674316,
        0.3067881257772198,
        0.29786925246614776,
        0.2891942627189715,
        0.28080070794383044,
        0.2727171406732664,
        0.264964469219798
      ],
      "M_P_pp": [
        0.2510539876383427,
        0.2559106692581498,
        0.26099619794094286,
        0.26631378037515074,
        0.2718657693549871,
        0.277653339325006,
        0.28367620772502056,
        0.2899324030857708,
        0.29641807648072255,
        0.3031273467623558,
        0.3100521639080235,
        0.31718217114116737,
        0.3245045477552368,
        0.3320038226228662,
        0.33966166350176613,
        0.3474566672060891,
        0.3553641954406713,
        0.36335631367501925,
        0.3714018893823187,
        0.37946688814976565,
        0.38751487384306615,
        0.39550767970552503,
        0.4034061812074906,
        0.4111710777621916,
        0.418763584089595,
        0.42614594308667353,
        0.43328169707003134,
        0.44013568862706476,
        0.4466738021087201,
        0.45286249861344635,
        0.45866823653280175,
        0.46405689879542744,
        0.46899335692977717,
        0.47344128296914745,
        0.4773632735592166,
        0.4807212896737474,
        0.4834773628904124,
        0.4855944960965081,
        0.48703769873741315,
        0.4877751309734051,
        0.4877793634996158,
        0.48702877033238307,
        0.4855090520856818,
        0.48321483692473144,
        0.4801512276918033,
        0.47633506163020256,
        0.47179554085742553,
        0.46657382694978866,
        0.46072126675189035,
        0.4542962134376253,
        0.44735986938048605,
        0.43997196716776693,
        0.4321871923606983,
        0.42405302884228585,
        0.41560934938367894,
        0.40688972505863436,
        0.3979240964393236,
        0.3887421111985761,
        0.3793761988964458,
        0.36986356101886836,
        0.36024675559465746,
        0.35057312378633687,
        0.34089356955615396,
        0.3312611351621561,
        0.32172959932724327,
        0.31235207179945673,
        0.30317930302181945,
        0.29425736049344675,
        0.28562486460641334,
        0.27731118070428745,
        0.2693378123009743
      ]
    },
    "T=10,q=0.1": {
      "Delta_act_pp": [
        0.2718786254840475,
        0.2793630488978054,
        0.2872455107960393,
        0.2955120804635874,
        0.30413958093041293,
        0.3130965275311046,
        0.32234485569075544,
        0.33184211826044246,
        0.3415438107247364,
        0.3514055289222537,
        0.3613847515308453,
        0.37144213813273064,
        0.38154231956200985,
        0.39165421781541837,
        0.401750965816533,
        0.41180950763221225,
        0.421809955606394,
        0.43173477091886026,
        0.44156782528225236,
        0.4512933980925069,
        0.4608951663169168,
        0.4703552514652724,
        0.479653394263867,
        0.48876632707233225,
        0.49766740148526317,
        0.5063265019542238,
        0.5147102384253855,
        0.5227823695378417,
        0.5305043735463377,
        0.5378360672542916,
        0.5447361802734771,
        0.5511628223261901,
        0.5570738267950008,
        0.5624270004475669,
        0.5671803427274428,
        0.5712923091849165,
        0.5747221831972851,
        0.5774305978201899,
        0.5793802282703484,
        0.5805366633663582,
        0.5808694604112531,
        0.5803533840710711,
        0.5789698147123223,
        0.5767082760430468,
        0.5735679705045839,
        0.5695591244615777,
        0.5647038462563336,
        0.559036127948759,
        0.5526006554869884,
        0.5454503144077989,
        0.5376426690332581,
        0.5292360753841677,
        0.520286248966922,
        0.5108439838529046,
        0.5009544113507776,
        0.4906578225035021,
        0.47999171384118194,
        0.46899338775894145,
        0.45770227343657255,
        0.44616129816176103,
        0.4344171040768686,
        0.42251936790578215,
        0.4105196674175229,
        0.3984702659886364,
        0.38642302720100574,
        0.37442854479761245,
        0.36253553858943527,
        0.35079065043792074,
        0.3392388536786794,
        0.32792436013383963,
        0.3168908498124124
      ],
      "M_P_pp": [
        0.2720617488003967,
        0.27955127461483625,
        0.28743911027090563,
        0.29571131555637314,
        0.30434469770062794,
        0.31330775057402954,
        0.3225623836516811,
        0.33206612084691123,
        0.3417744273039614,
        0.3516428685895341,
        0.3616288943931651,
        0.3716931374772958,
        0.38180020456359376,
        0.3919189964618015,
        0.4020226277792433,
        0.4120880268647188,
        0.4220952925040353,
        0.43202687392012984,
        0.44186663183041036,
        0.4515988349135121,
        0.46120714900872944,
        0.4706736834374426,
        0.4799781651144692,
        0.48909731053705385,
        0.4980044531326142,
        0.5066694568218624,
        0.5150589087877686,
        0.5231365429623865,
        0.5308638113388022,
        0.5382005033261031,
        0.5451053204005548,
        0.5515363437263435,
        0.5574513779395398,
        0.5628082010431571,
        0.5675647838474592,
        0.5716795535803887,
        0.5751117658612559,
        0.5778220269078401,
        0.5797729864912115,
        0.5809302099706273,
        0.5812632338952394,
        0.5807468057272513,
        0.5793622931394989,
        0.5770992126979572,
        0.5739567663002412,
        0.5699451872826755,
        0.5650865990596176,
        0.5594150168645853,
        0.5529751571097313,
        0.5458199413858058,
        0.5380069732585451,
        0.5295946485321501,
        0.5206387206962795,
        0.511190018450463,
        0.501293703870999,
        0.49099009546870265,
        0.48031671533641057,
        0.4693108912996322,
        0.45801207941844924,
        0.4464632362456242,
        0.43471103572114483,
        0.42280518843530784,
        0.4107973073195551,
        0.3987396913802561,
        0.38668423955656306,
        0.37468158008303243,
        0.3627804659846906,
        0.351027570920419,
        0.3394678988857689,
        0.3281456918436582,
        0.3171046595813313
      ]
    },
    "T=10,q=0.3": {
      "Delta_act_pp": [
        0.2718786254840476,
        0.27936304889780555,
        0.28724551079603944,
        0.29551208046358757,
        0.30413958093041304,
        0.3130965275311046,
        0.32234485569075555,
        0.33184211826044246,
        0.3415438107247365,
        0.3514055289222538,
        0.3613847515308453,
        0.3714421381327309,
        0.38154231956201,
        0.39165421781541837,
        0.40175096581653313,
        0.41180950763221247,
        0.4218099556063941,
        0.43173477091886037,
        0.4415678252822524,
        0.45129339809250696,
        0.4608951663169169,
        0.4703552514652724,
        0.47965339426386705,
        0.4887663270723324,
        0.49766740148526345,
        0.5063265019542239,
        0.5147102384253857,
        0.522782369537842,
        0.5305043735463377,
        0.5378360672542917,
        0.5447361802734774,
        0.5511628223261901,
        0.557073826795001,
        0.562427000447567,
        0.5671803427274428,
        0.5712923091849164,
        0.5747221831972852,
        0.57743059782019,
        0.5793802282703484,
        0.5805366633663582,
        0.5808694604112531,
        0.5803533840710711,
        0.5789698147123225,
        0.576708276043047,
        0.5735679705045841,
        0.5695591244615779,
        0.5647038462563336,
        0.5590361279487591,
        0.5526006554869886,
        0.5454503144077989,
        0.5376426690332581,
        0.5292360753841677,
        0.520286248966922,
        0.5108439838529046,
        0.5009544113507777,
        0.49065782250350226,
        0.47999171384118194,
        0.46899338775894145,
        0.457702273436573,
        0.44616129816176114,
        0.4344171040768687,
        0.42251936790578215,
        0.4105196674175229,
        0.3984702659886364,
        0.38642302720100585,
        0.37442854479761256,
        0.36253553858943527,
        0.35079065043792074,
        0.33923885367867956,
        0.32792436013383974,
        0.31689084981241256
      ],
      "M_P_pp": [
        0.2720617488003968,
        0.2795512746148364,
        0.28743911027090574,
        0.2957113155563733,
        0.304344697700628,
        0.31330775057402954,
        0.3225623836516813,
        0.33206612084691123,
        0.3417744273039615,
        0.35164286858953414,
        0.3616288943931651,
        0.3716931374772961,
        0.38180020456359387,
        0.39191899646180156,
        0.4020226277792434,
        0.412088026864719,
        0.4220952925040353,
        0.43202687392013006,
        0.44186663183041053,
        0.4515988349135123,
        0.4612071490087296,
        0.4706736834374426,
        0.4799781651144694,
        0.48909731053705396,
        0.4980044531326145,
        0.5066694568218626,
        0.5150589087877686,
        0.5231365429623869,
        0.5308638113388022,
        0.5382005033261034,
        0.5451053204005549,
        0.5515363437263435,
        0.55745137793954,
        0.5628082010431572,
        0.5675647838474592,
        0.5716795535803886,
        0.575111765861256,
        0.5778220269078402,
        0.5797729864912115,
        0.5809302099706273,
        0.5812632338952395,
        0.5807468057272513,
        0.5793622931394992,
        0.5770992126979573,
        0.5739567663002413,
        0.5699451872826756,
        0.5650865990596177,
        0.5594150168645854,
        0.5529751571097316,
        0.5458199413858059,
        0.5380069732585451,
        0.5295946485321501,
        0.5206387206962795,
        0.5111900184504631,
        0.5012937038709993,
        0.4909900954687028,
        0.48031671533641057,
        0.4693108912996322,
        0.4580120794184497,
        0.4464632362456242,
        0.434711035721145,
        0.42280518843530784,
        0.4107973073195551,
        0.3987396913802561,
        0.3866842395565631,
        0.37468158008303254,
        0.3627804659846906,
        0.351027570920419,
        0.339467898885769,
        0.32814569184365827,
        0.31710465958133155
      ]
    },
    "T=10,q=0.5": {
      "Delta_act_pp": [
        0.2718786254840476,
        0.2793630488978055,
        0.2872455107960394,
        0.29551208046358746,
        0.30413958093041293,
        0.3130965275311046,
        0.32234485569075544,
        0.33184211826044246,
        0.3415438107247365,
        0.3514055289222538,
        0.3613847515308453,
        0.37144213813273075,
        0.3815423195620099,
        0.39165421781541837,
        0.40175096581653313,
        0.41180950763221225,
        0.4218099556063941,
        0.43173477091886026,
        0.4415678252822524,
        0.45129339809250696,
        0.4608951663169168,
        0.4703552514652724,
        0.47965339426386705,
        0.48876632707233225,
        0.4976674014852632,
        0.5063265019542238,
        0.5147102384253855,
        0.522782369537842,
        0.5305043735463377,
        0.5378360672542917,
        0.5447361802734773,
        0.5511628223261901,
        0.557073826795001,
        0.562427000447567,
        0.5671803427274428,
        0.5712923091849165,
        0.5747221831972852,
        0.5774305978201899,
        0.5793802282703484,
        0.5805366633663581,
        0.5808694604112531,
        0.5803533840710712,
        0.5789698147123225,
        0.576708276043047,
        0.5735679705045841,
        0.5695591244615777,
        0.5647038462563336,
        0.559036127948759,
        0.5526006554869886,
        0.5454503144077989,
        0.5376426690332581,
        0.5292360753841677,
        0.520286248966922,
        0.5108439838529046,
        0.5009544113507777,
        0.4906578225035022,
        0.47999171384118194,
        0.46899338775894145,
        0.45770227343657255,
        0.44616129816176114,
        0.4344171040768687,
        0.42251936790578215,
        0.4105196674175229,
        0.39847026598863655,
        0.38642302720100574,
        0.37442854479761245,
        0.36253553858943527,
        0.3507906504379205,
        0.3392388536786794,
        0.32792436013383974,
        0.3168908498124124
      ],
      "M_P_pp": [
        0.2720617488003968,
        0.27955127461483636,
        0.2874391102709057,
        0.2957113155563732,
        0.30434469770062794,
        0.31330775057402954,
        0.3225623836516812,
        0.33206612084691123,
        0.3417744273039615,
        0.35164286858953414,
        0.3616288943931651,
        0.371693137477296,
        0.3818002045635938,
        0.3919189964618015,
        0.4020226277792434,
        0.4120880268647189,
        0.4220952925040353,
        0.43202687392012984,
        0.4418666318304104,
        0.4515988349135123,
        0.4612071490087295,
        0.4706736834374426,
        0.47997816511446934,
        0.48909731053705385,
        0.4980044531326143,
        0.5066694568218624,
        0.5150589087877686,
        0.5231365429623867,
        0.5308638113388022,
        0.5382005033261033,
        0.5451053204005548,
        0.5515363437263435,
        0.5574513779395399,
        0.5628082010431572,
        0.5675647838474592,
        0.5716795535803887,
        0.575111765861256,
        0.5778220269078401,
        0.5797729864912115,
        0.5809302099706272,
        0.5812632338952394,
        0.5807468057272515,
        0.579362293139499,
        0.5770992126979573,
        0.5739567663002413,
        0.5699451872826755,
        0.5650865990596176,
        0.5594150168645853,
        0.5529751571097316,
        0.5458199413858058,
        0.5380069732585451,
        0.5295946485321501,
        0.5206387206962795,
        0.5111900184504631,
        0.5012937038709991,
        0.4909900954687028,
        0.48031671533641057,
        0.4693108912996322,
        0.45801207941844924,
        0.4464632362456242,
        0.4347110357211449,
        0.42280518843530784,
        0.4107973073195551,
        0.3987396913802562,
        0.38668423955656306,
        0.37468158008303243,
        0.3627804659846906,
        0.3510275709204188,
        0.3394678988857689,
        0.32814569184365827,
        0.3171046595813313
      ]
    },
    "T=10,q=0.7": {
      "Delta_act_pp": [
        0.2718786254840476,
        0.2793630488978054,
        0.2872455107960393,
        0.29551208046358746,
        0.30413958093041293,
        0.3130965275311046,
        0.32234485569075544,
        0.3318421182604423,
        0.3415438107247364,
        0.3514055289222537,
        0.36138475153084526,
        0.37144213813273064,
        0.38154231956200985,
        0.39165421781541826,
        0.401750965816533,
        0.41180950763221225,
        0.421809955606394,
        0.43173477091886037,
        0.44156782528225225,
        0.4512933980925069,
        0.4608951663169168,
        0.4703552514652724,
        0.479653394263867,
        0.48876632707233225,
        0.49766740148526317,
        0.5063265019542238,
        0.5147102384253855,
        0.5227823695378419,
        0.5305043735463376,
        0.5378360672542916,
        0.5447361802734773,
        0.5511628223261901,
        0.5570738267950008,
        0.5624270004475669,
        0.5671803427274428,
        0.5712923091849165,
        0.5747221831972851,
        0.5774305978201898,
        0.5793802282703483,
        0.5805366633663581,
        0.5808694604112529,
        0.5803533840710711,
        0.5789698147123225,
        0.576708276043047,
        0.5735679705045839,
        0.5695591244615777,
        0.5647038462563336,
        0.559036127948759,
        0.5526006554869884,
        0.5454503144077989,
        0.5376426690332581,
        0.5292360753841677,
        0.5202862489669219,
        0.5108439838529046,
        0.5009544113507776,
        0.4906578225035021,
        0.47999171384118183,
        0.46899338775894145,
        0.45770227343657255,
        0.44616129816176103,
        0.4344171040768686,
        0.42251936790578215,
        0.4105196674175229,
        0.39847026598863655,
        0.38642302720100574,
        0.37442854479761245,
        0.36253553858943527,
        0.3507906504379205,
        0.3392388536786794,
        0.32792436013383974,
        0.3168908498124123
      ],
      "M_P_pp": [
        0.2720617488003968,
        0.27955127461483625,
        0.28743911027090563,
        0.29571131555637314,
        0.30434469770062794,
        0.31330775057402954,
        0.3225623836516811,
        0.33206612084691106,
        0.3417744273039614,
        0.3516428685895341,
        0.361628894393165,
        0.3716931374772958,
        0.38180020456359376,
        0.3919189964618014,
        0.4020226277792433,
        0.4120880268647188,
        0.4220952925040353,
        0.43202687392012995,
        0.44186663183041025,
        0.4515988349135122,
        0.46120714900872944,
        0.4706736834374426,
        0.4799781651144692,
        0.48909731053705385,
        0.4980044531326142,
        0.5066694568218624,
        0.5150589087877686,
        0.5231365429623867,
        0.5308638113388021,
        0.5382005033261031,
        0.5451053204005548,
        0.5515363437263435,
        0.5574513779395398,
        0.5628082010431571,
        0.5675647838474592,
        0.5716795535803887,
        0.5751117658612559,
        0.5778220269078401,
        0.5797729864912113,
        0.5809302099706272,
        0.5812632338952393,
        0.5807468057272513,
        0.579362293139499,
        0.5770992126979573,
        0.5739567663002412,
        0.5699451872826755,
        0.5650865990596176,
        0.5594150168645853,
        0.5529751571097314,
        0.5458199413858058,
        0.5380069732585451,
        0.5295946485321501,
        0.5206387206962793,
        0.5111900184504631,
        0.501293703870999,
        0.49099009546870276,
        0.4803167153364105,
        0.4693108912996322,
        0.45801207941844924,
        0.4464632362456242,
        0.43471103572114483,
        0.42280518843530784,
        0.4107973073195551,
        0.3987396913802562,
        0.38668423955656306,
        0.37468158008303243,
        0.3627804659846906,
        0.3510275709204188,
        0.3394678988857689,
        0.32814569184365827,
        0.3171046595813313
      ]
    },
    "T=10,q=0.9": {
      "Delta_act_pp": [
        0.2718786254840476,
        0.2793630488978055,
        0.2872455107960394,
        0.29551208046358746,
        0.30413958093041293,
        0.3130965275311046,
        0.32234485569075544,
        0.3318421182604423,
        0.3415438107247364,
        0.3514055289222538,
        0.3613847515308453,
        0.37144213813273075,
        0.3815423195620099,
        0.39165421781541837,
        0.401750965816533,
        0.41180950763221225,
        0.421809955606394,
        0.43173477091886037,
        0.44156782528225225,
        0.4512933980925069,
        0.4608951663169168,
        0.4703552514652724,
        0.47965339426386705,
        0.48876632707233225,
        0.4976674014852632,
        0.5063265019542238,
        0.5147102384253855,
        0.5227823695378419,
        0.5305043735463377,
        0.5378360672542917,
        0.5447361802734773,
        0.5511628223261901,
        0.557073826795001,
        0.562427000447567,
        0.5671803427274428,
        0.5712923091849165,
        0.5747221831972852,
        0.5774305978201899,
        0.5793802282703484,
        0.5805366633663581,
        0.5808694604112531,
        0.5803533840710712,
        0.5789698147123225,
        0.576708276043047,
        0.5735679705045839,
        0.5695591244615777,
        0.5647038462563336,
        0.559036127948759,
        0.5526006554869886,
        0.5454503144077989,
        0.5376426690332581,
        0.5292360753841677,
        0.520286248966922,
        0.5108439838529046,
        0.5009544113507776,
        0.4906578225035021,
        0.47999171384118183,
        0.46899338775894145,
        0.45770227343657255,
        0.44616129816176114,
        0.4344171040768687,
        0.42251936790578215,
        0.4105196674175229,
        0.39847026598863655,
        0.38642302720100574,
        0.37442854479761245,
        0.36253553858943527,
        0.3507906504379205,
        0.3392388536786794,
        0.32792436013383974,
        0.3168908498124124
      ],
      "M_P_pp": [
        0.2720617488003968,
        0.27955127461483636,
        0.2874391102709057,
        0.29571131555637314,
        0.30434469770062794,
        0.31330775057402954,
        0.3225623836516811,
        0.33206612084691106,
        0.3417744273039614,
        0.35164286858953414,
        0.3616288943931651,
        0.371693137477296,
        0.3818002045635938,
        0.3919189964618015,
        0.4020226277792433,
        0.4120880268647189,
        0.4220952925040353,
        0.43202687392012995,
        0.44186663183041025,
        0.4515988349135122,
        0.4612071490087295,
        0.4706736834374426,
        0.47997816511446934,
        0.48909731053705385,
        0.4980044531326143,
        0.5066694568218624,
        0.5150589087877686,
        0.5231365429623867,
        0.5308638113388022,
        0.5382005033261033,
        0.5451053204005548,
        0.5515363437263435,
        0.5574513779395399,
        0.5628082010431572,
        0.5675647838474592,
        0.5716795535803887,
        0.575111765861256,
        0.5778220269078401,
        0.5797729864912115,
        0.5809302099706272,
        0.5812632338952394,
        0.5807468057272515,
        0.579362293139499,
        0.5770992126979573,
        0.5739567663002412,
        0.5699451872826755,
        0.5650865990596176,
        0.5594150168645853,
        0.5529751571097316,
        0.5458199413858058,
        0.5380069732585451,
        0.5295946485321501,
        0.5206387206962795,
        0.5111900184504631,
        0.501293703870999,
        0.49099009546870276,
        0.4803167153364105,
        0.4693108912996322,
        0.45801207941844924,
        0.4464632362456242,
        0.4347110357211449,
        0.42280518843530784,
        0.4107973073195551,
        0.3987396913802562,
        0.38668423955656306,
        0.37468158008303243,
        0.3627804659846906,
        0.3510275709204188,
        0.3394678988857689,
        0.32814569184365827,
        0.3171046595813313
      ]
    }
  },
  "baseline": {
    "k": [
      1.2405757282617416,
      1.5310222869296415
    ],
    "tau_reference": 0.09076405861553302,
    "T": 5,
    "H": 10,
    "Omega": 0.1383963119314466,
    "Delta_act_pp": 0.268471939827342,
    "M_F_pp": 0.552817848535105,
    "M_P_pp": 0.2227984757708382,
    "cutoff_scale": 2.595657022652631e-11,
    "payoff_scale": 0.0
  },
  "seconds": 918.1377665419132,
  "all_pass": false
}
```

---

## 6. RE-RUN VERDICT

FILE: quality_reports/fixes/t2_rerun_verify_note.md (verbatim)

# T2 check-script re-run verification (ticket 28 D-series discipline)

**Re-runner:** fresh Opus agent, wrote none of the eight scripts. Adversarial
stance: the goal was to break the claims, not to confirm them.

**Worktree:** `/Users/austinli/Projects/blockholder_v4_theory` (branch `v4-theory`).
**Interpreter:** `.venv/bin/python` (CPython 3.12.13), invoked from the worktree root.
**Run window:** 2026-08-21 23:16 CST -> 2026-08-22 02:07 CST.
**No git commands were run. No script and no committed JSON was edited.**

---

## Overall

**ALL REPRODUCE.**

All eight scripts ran to completion. Every one of the eight freshly written JSONs
is identical to its committed counterpart **in every field except wall-clock
timing fields** (`seconds`, `wall_seconds`, and per-row/per-node `seconds`).
**Zero numeric result differences of any size** — not merely below the 1e-12
relative bar, but bit-identical: every non-timing float compared equal under
Python `==`.

One MISCITED item, on a characterisation in the handoff text rather than in any
committed artefact — see "Discrepancies" below. It does not affect any verdict.

---

## Per-script table

| script | exit code | byte-match | field diffs | headline claims confirmed |
|---|---|---|---|---|
| `t2_l3_check.py` | 0 | no | 1, timing only (`/seconds` 0.0647 -> 0.0323) | YES |
| `t2_l1_check.py` | 0 | no | 1, timing only (`/seconds` 84.93 -> 79.60) | YES |
| `t2_l2_check.py` | 1 | no | 1, timing only (`/seconds` 135.64 -> 119.46) | YES |
| `t2_d1_check.py` | 0 | no | 1, timing only (`/seconds` 191.77 -> 179.79) | YES |
| `t2_l4_check.py` | 0 | no | 1, timing only (`/seconds` 414.66 -> 400.93) | YES |
| `t2_t1_check.py` | 1 (see note) | no | 1, timing only (`/seconds` 918.14 -> 989.65) | YES |
| `t2_p1_check.py` | 1 (see note) | no | 35, timing only (7 node-set-A row `seconds`, 27 sweep row `seconds`, top-level `seconds` 9349.99 -> 9492.92) | YES on the FAIL identity and 23/27; the "pi_bar_pr = 0 corners" gloss is MISCITED |
| `t2_c1_region_check.py` | 0 (see note) | no | 81, timing only (80 per-node `seconds` + `wall_seconds` 10339.31 -> 8905.50) | YES |

**Exit-code note.** `t2_t1`, `t2_p1` and `t2_c1_region_check` were run detached
(`nohup`) because they exceed the 10-minute foreground tool ceiling, so their
raw exit status was not captured by the shell. All three ran to completion,
printed their normal summary line, and wrote a complete JSON. Every script ends
with `sys.exit(main())` and `main()` returns `0 if all_pass else 1` (c1:
`0 if n_fail == 0 else 1`), so the codes above follow deterministically from the
JSONs those runs wrote: t1 `all_pass=false` -> 1, p1 `all_pass=false` -> 1, c1
`n_fail=0` -> 0. The five foreground runs' codes were captured directly.

**A first `t2_t1` attempt was killed at 10 minutes by the tool timeout, not by a
crash.** It had not yet reached its JSON write; `t2_t1_check.json` was verified
byte-unchanged afterwards. The script was then relaunched detached and completed
normally in 990 s. **No `--quick` mode was used anywhere. Every script was run
full.**

---

## Headline claims, verified against the fresh JSONs

- **D1** — `all_pass = true`, `n_fail = 0`, 9 checks (1 vacuous:
  `d1_QF_T_monotonicity`). CONFIRMED.
- **L1** — `all_pass = true`, `n_fail = 0`, and all 4 checks carry
  `kind = "wiring"`. Wiring-labelled as reported. CONFIRMED.
- **L2** — `all_pass = false`, `n_fail = 1`, and the single FAIL is
  `l2_placebo_M_P_sign_A_tau`. Core invariance is **exactly** zero:
  `l2_flagged_invariance_ranges.max_range` = `{v_hat: 0.0, pi_flagged: 0.0,
  P_F: 0.0, p_bid: 0.0, M_F: 0.0, Omega: 0.0}` and
  `l2_flagged_invariance_derivs.derivatives` = `{dM_F_dkappa: 0.0,
  dOmega_dkappa: 0.0, dP_F_dkappa: 0.0, dp_bid_dkappa: 0.0}` — literal `0.0`,
  not "below tolerance". CONFIRMED.
- **L3** — `all_pass = true`, `n_fail = 0`, 10 checks, 0 vacuous. The
  amended-tolerance provenance is present as a `tolerance_amendment` field
  reading "tolerance amended per design review 2026-08-21: relative criterion
  residual/|C_h| < 1e-6 for the standalone chord route (pi_bar < 1e-2);
  absolute 1e-10 retained on the full-model route (pi_bar >= 1e-2)". CONFIRMED.
- **L4** — `all_pass = true`, `n_fail = 0`, 10 checks. `n_sign_violations = 0`,
  `n_sign_violations_model_route = 0`, `n_violations = 0`, and both `violations`
  and `violations_model_route` are empty lists. CONFIRMED.
- **T1** — `all_pass = false`, `n_fail = 1`, single FAIL
  `t1_block3_chord_magnitude` with `max_residual_pp = 0.6279460912900146`
  (~0.628 pp). O-1 benchmark ratios recomputed as
  `1.0639720903628607 / 1.183730968801152 / 1.136311993800545 /
  0.37797840338096084` against committed `1.06397 / 1.18373 / 1.13631 /
  0.37798`, `max_abs_diff_vs_committed = 2.09e-06` under `tol_ratio = 1e-4`;
  `kD_star = 1.28618431`, `Omega_star = 0.34283956`. Composition factors
  `1.1051410553 / 1.3589694200 / 1.5910362300 / 0.7559568068` against predicted
  `1.1051 / 1.3590 / 1.5910 / 0.7560`, `max_abs_diff = 4.32e-05` under
  `tol = 1e-3`. CONFIRMED. ("Exact" here means agreement with the committed
  digits to within the script's own stated tolerance, which is what the JSON
  asserts — not bit-identity.)
- **P1** — `all_pass = false`, `n_fail = 1`, single FAIL
  `p1_multistart_existence_sweep`, `n_converged = 23` of `n_nodes = 27`.
  CONFIRMED. The four failing nodes: see the discrepancy below.
- **C1** — `all_pass = true`, `n_fail = 0`, 12 checks split **4 PASS / 8 RECORD /
  0 FAIL**; `n_error_nodes = 0`, 80 nodes, `empty_region = false`,
  `n_certified = 18` of 80, `L_min = 0.26358722`, `L_max = 0.50081835`
  (L_R in [0.264, 0.501]), `n_nodes_with_L_ge_1 = 0`,
  `eta_min = 0.05953542544265861` (~0.0595), `eta_median = 0.34671597`,
  `eta_max = 1.72272795`. CONFIRMED.

---

## Discrepancies

**One. MISCITED — P1's four failing nodes are not "pi_bar_pr = 0 corners".**

The re-run reproduces the FAIL exactly (23/27), but the handoff's gloss on *which*
four nodes fail is not supported by the artefact. The four rows with
`converged_payoff = false` are:

| kappa | tau | T | `corner` | `converged_cutoff` | `best_payoff_scale` |
|---|---|---|---|---|---|
| 0.15 | 0.05  | 5 | **false** | true | 1.488e-3 |
| 0.15 | 0.075 | 1 | **false** | true | 1.059e-3 |
| 0.85 | 0.05  | 5 | **false** | true | 3.984e-4 |
| 0.85 | 0.075 | 1 | **false** | true | 3.061e-4 |

`corner` is set at `t2_p1_check.py:557` as `bool(T == p.H)`, i.e. T at the
horizon H = 10. None of the four failing nodes is a corner in that sense; all
nine corner rows in the sweep converged. Nor is `pi_bar_pr` zero anywhere in the
file: the string `pi_bar_pr` occurs exactly once in `t2_p1_check.json`, with
value `0.10206126073370039`, and the word "corner" appears only as the field
name — there is no note anywhere in the JSON characterising the failures that
way.

What the artefact actually shows is different and more specific: all four
failures are at the **kappa extremes** (0.15 and 0.85), at the two **lower tau**
values, at T in {1, 5}; in every case the **cutoff** criterion converged and only
the **payoff** criterion did not, at a payoff scale of 3e-4 to 1.5e-3. The claim
stands; the citation does not. Swap the gloss for the table above.

Nothing blocks. No WRONG verdict on any script. No UNCHECKED claims — every
headline item was checked against a completed executed run.

---

## Determinism

No concerns.

- **RNG.** The only randomness anywhere in the dependency closure is
  `np.random.default_rng(seed)` at `numerical_v4/solver.py:148`, with an explicit
  integer seed (0 on the default path, `sd = 0..29` in P1's multistart), and
  `jitter = ... if seed else np.zeros(2)` — the seed-0 path takes no draw at all.
  The v2 `numerical/` package used by T1 contains no RNG at all. No unseeded RNG,
  no Monte Carlo.
- **Clock.** `time.perf_counter()` is used only for the reported `seconds` /
  `wall_seconds` / per-row `seconds` fields. No date, no `datetime`, no
  clock-dependent branching. These fields are the *entire* content of every
  byte-level difference observed across all eight scripts.
- **Inputs.** Zero. Grep across all eight scripts and all of `numerical_v4/`
  found no `open(..., "r")`, `json.load`, `read_csv`, `loadtxt`, `np.load`,
  `pickle`, `os.environ`, `getenv`, `subprocess`, `urllib`, `requests` or
  `socket`. Every script's only file operation is `open(OUT, "w")` on its own
  JSON. Everything is computed from `numerical_v4/` (and, for T1's block 6, the
  static `numerical/` package) at run time — nothing is read back from a result
  file. `sys.path` is set from `os.path.abspath(__file__)`, so the runs are
  cwd-independent.
- **Self-overwrite.** Each script writes to its own committed JSON path, so
  running it necessarily rewrote the committed file. All eight were copied to a
  scratch directory before the first run and **restored byte-for-byte
  afterwards**; the eight SHA-256 sums in the worktree now equal the as-found
  sums. C1 additionally writes incrementally per node
  (`t2_c1_region_check.py:594`), so a crash would leave a partial file — the
  fresh C1 output was checked complete (80 nodes, `wall_seconds` present).
- **Scheduling.** Wall time was compressed by overlapping the three long runs:
  `t2_l3` ran first to validate the environment, then `t2_c1_region_check` and
  `t2_p1_check` were launched detached while `l1 -> l2 -> d1 -> l4 -> t1` ran in
  the requested cheap-first order in the foreground. At most three Python
  processes ran at once on a 10-core machine. Since the scripts share no state
  and read no files, this affects only the timing fields — and indeed the only
  fields that moved were timing fields.

**Total runtime:** 20,168 s of script time (5 h 36 m summed: l3 0.03 s, l1 79.6 s,
l2 119.5 s, d1 179.8 s, l4 400.9 s, t1 989.7 s, p1 9,492.9 s, c1 8,905.5 s),
compressed into **2 h 51 m of wall time** by the overlap above.
