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
*leg 1*, lower $\tau$ weakly raises $\Omega$, and *leg 2*, lower $\tau$ weakly lowers $\bar\pi$
in the pooled class, are **proved outright** (given D1's clock equivalence and $b_0<\tau'<\tau$);
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

