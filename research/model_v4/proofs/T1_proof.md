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
