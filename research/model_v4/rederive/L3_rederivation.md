# L3 — independent re-derivation (ticket 27)

**Mode: statements-only.** Inputs were `research/model_v4/MODEL_CARD.md` (version stamp
2026-08-21 · commit `a175202`+) and nothing else. `research/model_v4/proofs/` and
`research/model_v4/threads/` were not opened; `draft_v2.tex` was not opened. No result below is
copied from, checked against, or cited to an existing L3 proof.

**Statement under re-derivation** (card §6, L3 row): *Under A($\tau$) the pooled cell's interior
$\kappa$-motion is proportional to $C_h(\bar\pi)$, and $C_h = \tfrac14 h''(0)\bar\pi^2 +
o(\bar\pi^2)$, so it vanishes as $\bar\pi\downarrow 0$.*

**Verdict (detail in the final section): PROVED-WITH-CHANGES.** Five hypotheses the card does not
carry are load-bearing, and one card row (§4.4's gloss on $\bar\pi$) has to be amended. The
mathematics goes through cleanly once they are written down.

Headings below are the card §8 rule 6 template, in order, with a `VERDICT` section appended because
ticket 27 asks for one.

---

## CLAIM

Let the pooled cell carry positive mass and let the disclosure margin $(\tau,T)$, the cutoff policy
and the execution policy be held fixed. Write $M_P = \Delta_m\,\mathbb E[h \mid D=0]$ (card §4.4)
and $\mathcal S_P = \lvert \partial_\kappa M_P\rvert$ (card §4.4).

**C1 (exact motion identity).** Under H1–H5,
$$\partial_\kappa \mathbb E[h\mid D=0] \;=\; A'_\kappa\, C_h(\bar\pi),
\qquad\text{hence}\qquad
\partial_\kappa M_P = \Delta_m A'_\kappa C_h(\bar\pi),
\qquad
\mathcal S_P = \Delta_m\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert .$$
The interior $\kappa$-motion of the pooled cell is proportional to the chord, with proportionality
constant $\Delta_m A'_\kappa$. If $C_h(\bar\pi) = 0$ the motion is zero whatever $A'_\kappa$ is; the
reverse reading is not available (see Step 8).

**C2 (exact mean-value form of the chord).** Under H6, for every $\bar\pi \in (0,1]$ there exists
$\zeta \in (0,\bar\pi)$ with
$$C_h(\bar\pi) \;=\; \tfrac14\, h''(\zeta)\,\bar\pi^{2}.$$
No continuity of $h''$ is used.

**C3 (quadratic corollary and vanishing).** Under H7,
$$C_h(\bar\pi) \;=\; \tfrac14 h''(0)\,\bar\pi^{2} + o(\bar\pi^{2}) \qquad (\bar\pi\downarrow 0),$$
and under H7 + H8 the interior motion vanishes at that rate:
$\mathcal S_P = O(\bar\pi^{2}) \to 0$ as $\bar\pi \downarrow 0$.

**C4 (by-product, used to justify the $\bar\pi$ amendment).** Under H1–H3 the pooled engagement
share is $\kappa$-invariant:
$\Pr(a=1\mid D=0) = \mathbb E[\Pi_\kappa] = \bar\pi\,(1 - A_0 - \tfrac12 A_{1/2})$, with
$\partial_\kappa \mathbb E[\Pi_\kappa] = 0$, and $\mathbb E[\Pi_\kappa] < \bar\pi$ unless
$A_0 = A_{1/2} = 0$. The A($\tau$) weight-derivative structure is exactly a mean-preserving
perturbation of the pooled posterior.

---

## HYPOTHESES

Each is used at the step named. H3, H4, H6, H7 and the uniformity half of H8 are **not** in the card
as printed; they are the "changes" in the verdict.

**H1 — A($\tau$) ternary representation** *(card §5, A($\tau$))*. The pooled posterior law admits
$\mathbb E[h] = A_0(\kappa)h(0) + A_{1/2}(\kappa)h(\bar\pi/2) + A_1(\kappa)h(\bar\pi)$ with
$A_0' = A_1' = A'_\kappa$ and $A_{1/2}' = -2A'_\kappa$. Used: Steps 2, 3, 5.

**H2 — the weights are a differentiable probability vector** *(unpacking of "the pooled posterior
law has the representation"; the derivative notation in A($\tau$) presumes the differentiability)*.
$A_0,A_{1/2},A_1 \ge 0$, $A_0 + A_{1/2} + A_1 = 1$ on an open $\kappa$-interval, each differentiable
there. Used: Steps 2, 4, 5, 9.

**H3 — $\bar\pi$ is the upper support point and is $\kappa$-free.** In the A($\tau$) representation
$\bar\pi$ is the largest point of the three-point support $\{0,\bar\pi/2,\bar\pi\}$ of the pooled
engagement posterior; at fixed $(\tau,T)$ and fixed policies it does not move with $\kappa$. Used:
Step 3 (the whole identity fails without it — see F1) and Step 9.
*This contradicts the §4.4 gloss "pre-order pooled engagement share in the chord"; C4 shows the
share is $\mathbb E[\Pi_\kappa]$, a different and strictly smaller number.*

**H4 — kernel reduction to the engagement posterior.** $h$ depends on the control-node information
set only through $\pi$: there is a function $h:[0,1]\to[0,\infty)$ with
$h(\mathcal I) = h(\pi(\mathcal I))$. Given card §4.4's $h = \pi p$ and card §4.3's
$p = 1 - \Phi\big((P + K + m_0 + \pi\Delta_m - \bar S)/\sigma_\xi\big)$, this requires a map
$\mathcal P$ with $P(\mathcal I) = \mathcal P(\pi(\mathcal I))$ — the pooled price must be a
function of the engagement posterior alone. Used: Steps 1, 2, 12; it is what makes
$h(0), h(\bar\pi/2), h(\bar\pi)$ well-formed at all.

**H5 — interior crossing** *(card §5, A8)*. $0 < \Omega < 1$, so the pooled cell has mass and
$\mathbb E[\cdot\mid D=0]$ is defined. Used: Step 1.

**H6 — regularity for the mean-value form (minimal).** $h$ is continuous on $[0,\bar\pi]$ and twice
differentiable on the open interval $(0,\bar\pi)$. Used: Steps 6, 7, 8. $h''$ is **not** assumed
continuous, bounded, or defined at the endpoints.

**H7 — regularity for the corollary (minimal).** $h$ admits a second-order Peano expansion at the
right of $0$: $h(t) = h(0) + h'(0)t + \tfrac12 h''(0)t^2 + \rho(t)$ with $\rho(t)/t^2 \to 0$ as
$t\downarrow 0$. This is implied by, and weaker than, $h \in C^2$ on some $[0,\delta)$. It is what
gives the symbol $h''(0)$ in the card's L3 statement a meaning. Used: Step 9.

**H8 — uniform bound on $A'_\kappa$, and a fixed kernel along the limit** *(card §4.4's "$A'_\kappa$
bounded on $[0,1]$", strengthened)*. $\sup\lvert A'_\kappa\rvert =: \bar A < \infty$, the supremum
taken over the maintained $\kappa$-range **and** over $\bar\pi$ in a right-neighbourhood of $0$; and
$h$ itself does not vary as $\bar\pi\downarrow 0$. Used: Step 10.

**H9 — fixed policies and fixed margin.** Cutoff and execution policies and $(\tau,T)$ are held
fixed while $\kappa$ moves; "interior motion" means the within-cell derivative, with no
reclassification of histories across cells. Used: Step 1.

---

## PROOF

**Step 1 (the object).** By H9 and H5 the pooled-cell conditional expectation is defined; write
$m(\kappa) := \mathbb E[h(\mathcal I_H)\mid D=0]$, so $M_P = \Delta_m m(\kappa)$ by card §4.4's
$M_P$ row. "Interior $\kappa$-motion" is $\partial_\kappa M_P$ at fixed $(\tau,T)$ and fixed
policies (H9). By H4, $h(\mathcal I_H) = h(\pi(\mathcal I_H))$; write $\Pi_\kappa := \pi(\mathcal
I_H)$ for the engagement posterior viewed as a random variable under the pooled law. Then
$m(\kappa) = \mathbb E[h(\Pi_\kappa)]$.

**Step 2 (the law).** By H1 and H2, $\Pi_\kappa$ takes the three values $0$, $\bar\pi/2$, $\bar\pi$
with probabilities $A_0(\kappa)$, $A_{1/2}(\kappa)$, $A_1(\kappa)$, and by Step 1
$$m(\kappa) = A_0(\kappa)h(0) + A_{1/2}(\kappa)h(\bar\pi/2) + A_1(\kappa)h(\bar\pi).$$

**Step 3 (differentiate the weights only).** By H3 the three support points $0$, $\bar\pi/2$,
$\bar\pi$ carry no $\kappa$-dependence, so in Step 2's right side the only $\kappa$-dependence sits
in the weights; the three numbers $h(0), h(\bar\pi/2), h(\bar\pi)$ are constants of the
differentiation. By H2 each weight is differentiable on an open $\kappa$-interval, so $m$ is
differentiable there and
$$\partial_\kappa m = A_0'\,h(0) + A_{1/2}'\,h(\bar\pi/2) + A_1'\,h(\bar\pi).$$

**Step 4 (coherence of the weight-derivative structure).** By H2, $A_0 + A_{1/2} + A_1 = 1$ on an
open interval, so $A_0' + A_{1/2}' + A_1' = 0$ there. Substituting H1's structure gives
$A'_\kappa - 2A'_\kappa + A'_\kappa = 0$. H1 and H2 are therefore mutually consistent; the
$(1,-2,1)$ pattern is the unique-up-to-scale direction that a symmetric three-point probability
vector can move in, which is why A($\tau$) can impose it without further restriction on $A'_\kappa$.

**Step 5 (claim C1).** Substituting H1's $A_0' = A_1' = A'_\kappa$, $A_{1/2}' = -2A'_\kappa$ into
Step 3:
$$\partial_\kappa m = A'_\kappa\big[h(0) - 2h(\bar\pi/2) + h(\bar\pi)\big] = A'_\kappa\,C_h(\bar\pi),$$
the bracket being the chord of card §4.4. Multiplying by $\Delta_m$ (Step 1) gives
$\partial_\kappa M_P = \Delta_m A'_\kappa C_h(\bar\pi)$ and, taking absolute values with the card
§4.4 definition, $\mathcal S_P = \Delta_m\lvert A'_\kappa\rvert\lvert C_h(\bar\pi)\rvert$. This is
C1.

**Step 6 (Rolle).** Fix $\bar\pi \in (0,1]$ and set $x := \bar\pi/2$, so that
$C_h(\bar\pi) = h(x + \bar\pi/2) - 2h(x) + h(x - \bar\pi/2)$: the chord is the second central
difference at the midpoint with half-step $\bar\pi/2$. Under H6 define, for $t \in [0,\bar\pi/2]$,
$$u_1(t) := h(x+t) + h(x-t) - 2h(x) - \frac{4t^2}{\bar\pi^2}\,C_h(\bar\pi).$$
Then $u_1(0) = 0$ and $u_1(\bar\pi/2) = C_h(\bar\pi) - C_h(\bar\pi) = 0$. H6's continuity of $h$ on
$[0,\bar\pi]$ makes $u_1$ continuous on $[0,\bar\pi/2]$, and H6's twice-differentiability on
$(0,\bar\pi)$ makes $h$ differentiable at $x\pm t$ for every $t \in (0,\bar\pi/2)$, so $u_1$ is
differentiable on $(0,\bar\pi/2)$. Rolle's theorem gives $t_1 \in (0,\bar\pi/2)$ with $u_1'(t_1)=0$,
that is
$$h'(x+t_1) - h'(x-t_1) = \frac{8 t_1}{\bar\pi^2}\,C_h(\bar\pi). \tag{6.1}$$

**Step 7 (mean value theorem, second application).** Define $u_2(t) := h'(x+t) - h'(x-t)$ on
$[0,t_1]$. By H6, $h''$ exists on $(0,\bar\pi)$, hence $h'$ is differentiable — therefore continuous
— on $(0,\bar\pi)$; since $t_1 < \bar\pi/2$, the points $x \pm t$ lie in $(0,\bar\pi)$ for every
$t \in [0,t_1]$, so $u_2$ is continuous on $[0,t_1]$ and differentiable on $(0,t_1)$ with
$u_2'(t) = h''(x+t) + h''(x-t)$. Also $u_2(0) = 0$. The mean value theorem on $[0,t_1]$ gives
$t_2 \in (0,t_1)$ with $u_2(t_1) - u_2(0) = t_1\,u_2'(t_2)$, which with (6.1) reads
$$\frac{8t_1}{\bar\pi^2}C_h(\bar\pi) = t_1\big[h''(x+t_2) + h''(x-t_2)\big],
\qquad\text{so}\qquad
C_h(\bar\pi) = \frac{\bar\pi^2}{8}\big[h''(x+t_2) + h''(x-t_2)\big]. \tag{7.1}$$

**Step 8 (Darboux collapses the two points to one; claim C2).** By H6, $h''$ is the derivative of
$h'$ on $(0,\bar\pi)$. Darboux's theorem — a derivative on an interval takes every value between any
two of its values, at some point between them — applies to $h''$ on
$[x-t_2, x+t_2] \subset (0,\bar\pi)$. The arithmetic mean
$\tfrac12[h''(x+t_2) + h''(x-t_2)]$ lies between $h''(x-t_2)$ and $h''(x+t_2)$, so there is
$\zeta \in [x-t_2, x+t_2] \subset (0,\bar\pi)$ with
$h''(\zeta) = \tfrac12[h''(x+t_2)+h''(x-t_2)]$. Substituting into (7.1),
$$C_h(\bar\pi) = \tfrac14\,h''(\zeta)\,\bar\pi^{2}, \qquad \zeta \in (0,\bar\pi),$$
which is C2. Darboux is what removes any continuity requirement on $h''$; H6 is therefore the
minimal regularity for C2, and it is strictly weaker than $h \in C^2$.

*Corollary of Steps 5 and 8 (the $C_h = 0$ case, ruling (c)).* C1 is an identity, so it holds with
either side zero. If $C_h(\bar\pi) = 0$ then $\partial_\kappa M_P = 0$ for every value of
$A'_\kappa$ — a vanishing chord kills the interior motion. The converse is unavailable:
$\partial_\kappa M_P = 0$ also occurs at $A'_\kappa = 0$ with $C_h(\bar\pi) < 0$, i.e. when the
A($\tau$) weights happen to be flat in $\kappa$ at that point. By C2, $C_h(\bar\pi) = 0$ with
$\bar\pi > 0$ forces $h''(\zeta) = 0$ at some interior $\zeta$; it does not force $h$ affine. L3 is
an implication in one direction only, never an equivalence.

**Step 9 (claim C3, the expansion).** Let $\bar\pi \downarrow 0$ and use H7:
$h(t) = h(0) + h'(0)t + \tfrac12 h''(0)t^2 + \rho(t)$ with $\rho(0) = 0$ and $\rho(t) = o(t^2)$.
Evaluate the chord term by term.
- Constant term: $h(0) - 2h(0) + h(0) = 0$.
- Linear term: $h'(0)\big[0 - 2\cdot\tfrac{\bar\pi}{2} + \bar\pi\big] = 0$.
- Quadratic term:
  $\tfrac12 h''(0)\big[0 - 2\cdot\tfrac{\bar\pi^2}{4} + \bar\pi^2\big]
  = \tfrac12 h''(0)\cdot\tfrac{\bar\pi^2}{2} = \tfrac14 h''(0)\bar\pi^2$.
- Remainder: $\rho(0) - 2\rho(\bar\pi/2) + \rho(\bar\pi) = -2\rho(\bar\pi/2) + \rho(\bar\pi)$, and
  $\lvert\rho(\bar\pi/2)\rvert = \tfrac{\bar\pi^2}{4}\cdot\frac{\lvert\rho(\bar\pi/2)\rvert}{(\bar\pi/2)^2} = o(\bar\pi^2)$
  and $\lvert\rho(\bar\pi)\rvert = o(\bar\pi^2)$, so the remainder is $o(\bar\pi^2)$.

Summing: $C_h(\bar\pi) = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, which is C3's first half and
matches the card's L3 constant $\tfrac14$ exactly. The chord annihilates constants and linear terms
(the first two bullets); that annihilation is why the leading behaviour is quadratic rather than
linear, and it is also why the maintained sign $C_h \le 0$ near $0$ is a statement about $h''(0)$
and about nothing else.

**Step 10 (claim C3, the vanishing).** By H8 there is $\bar A < \infty$ bounding
$\lvert A'_\kappa\rvert$ uniformly over the maintained $\kappa$-range and over $\bar\pi$ near $0$,
and $h$ is the same function throughout the limit. Combining Step 5 and Step 9,
$$\mathcal S_P = \Delta_m\lvert A'_\kappa\rvert\,\lvert C_h(\bar\pi)\rvert
\;\le\; \Delta_m\,\bar A\Big(\tfrac14\lvert h''(0)\rvert\,\bar\pi^2 + o(\bar\pi^2)\Big)
\;\longrightarrow\; 0 \quad (\bar\pi\downarrow 0),$$
at rate $\bar\pi^2$. This completes C3. Both halves of H8 are load-bearing: an $A'_\kappa$ that blew
up as $\bar\pi^2{}^{-1}$, or a kernel that changed shape as the margin tightened, would leave the
product bounded away from zero with C3's first half still true.

**Step 11 (claim C4).** By H1–H3, $\mathbb E[\Pi_\kappa] = 0\cdot A_0 + \tfrac{\bar\pi}{2}A_{1/2} +
\bar\pi A_1$, so
$$\partial_\kappa \mathbb E[\Pi_\kappa] = \tfrac{\bar\pi}{2}(-2A'_\kappa) + \bar\pi A'_\kappa
= -\bar\pi A'_\kappa + \bar\pi A'_\kappa = 0 .$$
The perturbation direction $A'_\kappa(1,-2,1)$ moves mass $2A'_\kappa\,d\kappa$ off the midpoint and
places half of it at each endpoint, the two endpoints being symmetric about that midpoint: a
mean-preserving spread when $A'_\kappa > 0$ and a mean-preserving contraction when $A'_\kappa < 0$.
Step 5 is then the second-order response of $\mathbb E[h]$ to that spread, the chord being the
finite-difference concavity of $h$ on the triple. By H2,
$\mathbb E[\Pi_\kappa] = \bar\pi(1 - A_0 - \tfrac12 A_{1/2}) < \bar\pi$ unless $A_0 = A_{1/2} = 0$.
This is C4, and it is the argument for H3's amendment of the §4.4 gloss: the pooled engagement share
is $\mathbb E[\Pi_\kappa]$, which is strictly below $\bar\pi$ in any non-degenerate case, and — a
separate and sharper point — under A($\tau$) the share does not move with $\kappa$ at all, so the
share could not be the object whose $\kappa$-motion L3 is about.

**Step 12 (consistency remark, outside the claim).** With card §4.4's $h = \pi p$ read through H4:
$h(0) = 0$ (card §4.4), $h'(0) = p(0) > 0$ (card §4.3, $p \in (0,1)$), and $h''(0) = 2p'(0)$. From
card §4.3's entry row with H4's $\mathcal P$,
$p'(\pi) = -\varphi\big((\mathcal P(\pi)+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)\,
(\Delta_m + \mathcal P'(\pi))/\sigma_\xi$. With $\Delta_m > 0$ (card §4.1) and $\mathcal P' \ge 0$,
$p'(0) < 0$, so $h''(0) < 0$ and Step 9 delivers $C_h(\bar\pi) < 0$ for small $\bar\pi$ — the
maintained orientation $C_h \le 0$ of A($\tau$) is consistent with the card's own kernel near the
tight-margin limit. This is a consistency observation, not part of C1–C4: it needs the extra input
$\mathcal P' \ge 0$, which the card does not carry, and it says nothing about $\bar\pi$ away from
$0$.

*Executed arithmetic check run during this re-derivation* (a scratch script, not committed; the
committed version is requested below). With $\mathcal P(\pi) = 1.0 + 0.05\pi$, $K = 0.05$,
$m_0 = 0.10$, $\Delta_m = 0.15$, $\bar S = 0.30$, $\sigma_\xi = 1$, and weights
$A_0 = 0.20+0.30\kappa$, $A_{1/2} = 0.50-0.60\kappa$, $A_1 = 0.30+0.30\kappa$: the central
finite-difference $\partial_\kappa\mathbb E[h]$ matched $A'_\kappa C_h(\bar\pi)$ to relative
$10^{-10}$ at every $\kappa \in \{0,0.2,0.4,0.6,0.8\}$; $C_h/(\tfrac14 h''(0)\bar\pi^2)$ ran
$0.9486, 0.9744, 0.9872, 0.9936, 0.9968$ across $\bar\pi = 0.4, 0.2, 0.1, 0.05, 0.025$ (the gap
halving with $\bar\pi$, as Step 13 predicts); the $\zeta$ solving C2 came out at
$\zeta/\bar\pi = 0.5005, 0.5003, 0.5002$; and $\mathbb E[\Pi_\kappa] = 0.055$ at every $\kappa$
with $\bar\pi = 0.1$, confirming Step 11.

**Step 13 (third-order refinement, for the check).** If $h$ additionally admits a third-order Peano
expansion at $0$, the same term-by-term evaluation as Step 9 gives for the cubic term
$\tfrac16 h'''(0)\big[0 - 2(\bar\pi/2)^3 + \bar\pi^3\big] = \tfrac16 h'''(0)\cdot\tfrac34\bar\pi^3
= \tfrac18 h'''(0)\bar\pi^3$, so
$$C_h(\bar\pi) = \tfrac14 h''(0)\bar\pi^2 + \tfrac18 h'''(0)\bar\pi^3 + o(\bar\pi^3),$$
i.e. the relative error of C3 is $\approx \dfrac{h'''(0)}{2h''(0)}\bar\pi$ — first order in
$\bar\pi$, halving when $\bar\pi$ halves. Feeding this into C2 gives
$\zeta = \bar\pi/2 + O(\bar\pi^2)$: the mean-value point sits at the midpoint to leading order.

---

## WHERE IT FAILS

**F1 — $\bar\pi$ moves with $\kappa$ (H3 dropped).** Suppose deeper noise trading lets more
aggressive engagement plans hide, so the pooled posterior's upper support point rises with liquidity:
$\partial_\kappa\bar\pi > 0$. Step 3 then carries two extra terms and
$$\partial_\kappa \mathbb E[h] = A'_\kappa C_h(\bar\pi)
+ \Big[\tfrac12 A_{1/2}h'(\bar\pi/2) + A_1 h'(\bar\pi)\Big]\partial_\kappa\bar\pi .$$
The bracket tends to $(\tfrac12 A_{1/2} + A_1)h'(0) = (\tfrac12 A_{1/2}+A_1)p(0) > 0$ as
$\bar\pi\downarrow 0$ (Step 12), so the second term is **first order**, not second order, in the
neighbourhood of the tight-margin limit. C3's conclusion — that the motion vanishes as
$\bar\pi\downarrow 0$ — is then false whenever $\partial_\kappa\bar\pi$ does not itself vanish. This
is the single most damaging omission in the card's L3 as printed.

**F2 — $h$ is not a function of $\pi$ alone (H4 dropped).** Take two pooled control-node histories
with the same engagement posterior $\pi$ but different realised pooled prices $P$ — one arriving
after a run-up, one after flat order flow. Card §4.3's entry row makes $p$ a decreasing function of
$P$, so the two histories carry different $h$. Then $h(\bar\pi/2)$ and $h(\bar\pi)$ are not
well-defined numbers, the right side of A($\tau$) is not well-formed, and the correct object is an
expectation over the joint law of $(\pi, P)$, which a three-point chord in $\pi$ does not summarise.
The repair is either H4's price reduction $P = \mathcal P(\pi)$ or a restatement of A($\tau$) as a
representation of the joint law.

**F3 — $h''(0)$ does not exist (H7 dropped) — and the maintained sign goes with it.** Take
$h(\pi) = p(0)\pi + \pi^{3/2}$, which is continuous on $[0,\bar\pi]$ and twice differentiable on
$(0,\bar\pi)$, so C2 survives. But
$C_h(\bar\pi) = \bar\pi^{3/2}(1 - 2\cdot 2^{-3/2}) = (1 - 2^{-1/2})\bar\pi^{3/2} \approx
0.293\,\bar\pi^{3/2}$, which is (i) of order $\bar\pi^{3/2}$, an order **larger** than $\bar\pi^2$,
and (ii) strictly **positive**, violating A($\tau$)'s maintained $C_h \le 0$ at every small
$\bar\pi$. So a kernel with a one-sided $3/2$-power at the origin breaks C3's rate and A($\tau$)'s
orientation together; $h''(0)$ existing is not a formality.

**F4 — the weight vector hits its boundary.** A($\tau$)'s structure forces
$A_{1/2}' = -2A'_\kappa$. At a $\kappa_0$ where $A_{1/2}(\kappa_0) = 0$ and $A'_\kappa > 0$, the
requirement pushes $A_{1/2}$ negative just above $\kappa_0$, which H2 forbids. A($\tau$) therefore
cannot hold on an open neighbourhood of such a $\kappa_0$: only the one-sided derivative exists, and
C1 holds as a left-derivative statement at $\kappa_0$, not as the two-sided identity. The same
applies at $A_0 = 0$ or $A_1 = 0$ with $A'_\kappa < 0$. Any claim quantified over all
$\kappa \in [0,1]$ has to exclude these boundary points or verify they are unreached.

**F5 — $A'_\kappa$ unbounded along the tightening path (H8's uniformity dropped).** The card's §4.4
row reads "$A'_\kappa$ bounded on $[0,1]$", which is a statement about $\kappa$ at a fixed margin.
If the weights become more $\kappa$-sensitive as $\tau$ tightens — $\lvert A'_\kappa\rvert$ of order
$\bar\pi^{-2}$ along the path — then $\mathcal S_P = \Delta_m\lvert A'_\kappa\rvert\lvert C_h\rvert$
stays bounded away from zero even though $C_h \to 0$. C3's first half survives, C3's conclusion does
not. Since L4 consumes L3 exactly along the $\tau$-tightening path, this uniformity is where the two
results meet and has to be stated at L3, not assumed at L4.

---

## LABEL CLAIMED

**L3 stays CONJECTURE.** Reasons, in the card's own terms:

1. Card §6 requires *independent re-derivation PASS **plus** proof-read PASS* before PROVED. This
   document supplies one of the two legs and cannot supply the other (it has not seen, and by ticket
   27's scope may not see, the L3 proof of record). One leg does not move a label (card §7: only an
   executed check or an independent re-derivation may move a label, and §6 names both requirements).
2. Independently of the protocol, **L3 as printed on the card is not provable as printed**: H3, H4,
   H6, H7 and H8's uniformity are load-bearing and absent, and §4.4's gloss on $\bar\pi$
   contradicts H3. C1–C4 above are proved; the card's sentence is not, until §4.4 and §5 carry the
   amendments listed in the verdict.
3. The intended final label in card §6 ("L3 PROVED under A($\tau$)") remains reachable: nothing in
   this re-derivation is an obstruction, and the additions are hypotheses a theorist can grant, not
   gaps in the argument.

Claims C1 and C4 are exact identities and need no numerical support beyond arithmetic; C2 and C3
are analysis results whose content is a rate, and the check below is what would earn them a
**NUMERICAL** corroboration alongside the proof.

---

## NUMERICAL CHECK REQUEST

**Test kernel** (satisfies H4, H6, H7 by construction; $\varphi,\Phi$ the $N(0,1)$ density and c.d.f.):
$$h(\pi) = \pi\Big(1 - \Phi\big((\mathcal P_0 + \mathcal P_1\pi + K + m_0 + \pi\Delta_m - \bar S)/\sigma_\xi\big)\Big),$$
baseline $\mathcal P_0 = 1.0$, $\mathcal P_1 = 0.05$, $K = 0.05$, $m_0 = 0.10$, $\Delta_m = 0.15$,
$\bar S = 0.30$, $\sigma_\xi = 1$. These give $p(0) = 0.19766$,
$h''(0) = 2p'(0) = -2\varphi(0.85)(\mathcal P_1+\Delta_m)/\sigma_\xi = -0.111194$, and
$\tfrac14 h''(0) = -0.0277985$.

**Test weights** (satisfy H1, H2 on $\kappa \in [0, 0.8]$):
$A_0(\kappa) = 0.20 + 0.30\kappa$, $A_{1/2}(\kappa) = 0.50 - 0.60\kappa$,
$A_1(\kappa) = 0.30 + 0.30\kappa$; sum $\equiv 1$, all non-negative on the range, $A'_\kappa = 0.30$.

**Grid.** $\kappa \in \{0, 0.2, 0.4, 0.6, 0.8\}$; $\bar\pi \in \{0.4, 0.2, 0.1, 0.05, 0.025\}$;
central difference step $\Delta\kappa = 10^{-4}$.

| # | Formula checked | Predicted sign | Predicted magnitude |
|---|---|---|---|
| N1 | $\big[\mathbb E[h](\kappa+\Delta\kappa) - \mathbb E[h](\kappa-\Delta\kappa)\big]/2\Delta\kappa$ vs. $A'_\kappa C_h(\bar\pi)$ | both **negative** ($A'_\kappa>0$, $C_h<0$) | equal to relative $10^{-8}$ or better; at $\bar\pi = 0.1$ both equal $-8.233\times 10^{-5}$, flat in $\kappa$ |
| N2 | $\mathbb E[\Pi_\kappa] = \tfrac{\bar\pi}{2}A_{1/2} + \bar\pi A_1$ across the $\kappa$ grid (Step 11) | zero variation | constant $0.055$ at $\bar\pi = 0.1$, i.e. $0.55\bar\pi$, strictly below $\bar\pi$; spread across the $\kappa$ grid $< 10^{-15}$ |
| N3 | $C_h(\bar\pi)$ vs. $\tfrac14 h''(0)\bar\pi^2$ (C3) | both **negative** | ratio $r(\bar\pi) = 0.9486, 0.9744, 0.9872, 0.9936, 0.9968$ on the $\bar\pi$ grid; $\lvert r-1\rvert$ halves per halving of $\bar\pi$ (Step 13), so $\lvert r - 1\rvert/\bar\pi \to \lvert h'''(0)/2h''(0)\rvert \approx 0.128$ |
| N4 | $\zeta$ solving $h''(\zeta) = 4C_h(\bar\pi)/\bar\pi^2$ (C2) | $\zeta \in (0,\bar\pi)$ | $\zeta/\bar\pi = 0.5005, 0.5003, 0.5002$ at $\bar\pi = 0.4, 0.2, 0.1$; $\to 0.5$ (Step 13) |
| N5 | Counterexample F3: $h(\pi) = 0.19766\pi + \pi^{3/2}$ | $C_h$ **positive** — A($\tau$)'s orientation fails | $C_h(\bar\pi) = 0.29289\,\bar\pi^{3/2}$: $+7.41\times10^{-2}, +2.62\times10^{-2}, +9.26\times10^{-3}$ at $\bar\pi = 0.4,0.2,0.1$, i.e. of order $\bar\pi^{3/2}$, and $C_h/\bar\pi^2 \to +\infty$ |

N1 and N2 test C1 and C4 (exact, so they should hold to machine precision). N3 and N4 test C3 and
C2 (rates, so the diagnostic is the *ratio's* convergence, not any single value). N5 is the
regularity boundary: it must **fail** the maintained orientation, and a check script that reports it
as passing has a bug.

---

## NOTATION DELTA

Symbols used above that are not in card §4. Card §8 rule 4 is respected: no card symbol is renumbered
or re-keyed; $\psi$, bare $\lambda$, bare $W$, $G$, bare $u$ and upright $T$-as-map are all avoided.

| Symbol | Meaning | Status |
|---|---|---|
| $\Pi_\kappa$ | the engagement posterior $\pi(\mathcal I_H)$ read as a random variable under the pooled ($D=0$) law, with support $\{0,\bar\pi/2,\bar\pi\}$ and weights $(A_0,A_{1/2},A_1)$ | new; needed to state C4 and to separate the *share* $\mathbb E[\Pi_\kappa]$ from the *support point* $\bar\pi$ |
| $\mathcal P$ | pooled price as a function of the engagement posterior, $P(\mathcal I) = \mathcal P(\pi(\mathcal I))$ | new (H4). Calligraphic $\mathcal P$ is free on the card; upright $P$ stays the price |
| $m(\kappa)$ | $\mathbb E[h\mid D=0]$, so $M_P = \Delta_m m(\kappa)$ | proof-local shorthand |
| $\varphi$ | the $N(0,1)$ density (card §4.3 already uses $\Phi$ for its c.d.f.) | new, used only in Step 12 and the check |
| $\zeta$ | the mean-value point of C2, $\zeta \in (0,\bar\pi)$ | proof-local |
| $x$, $t$, $t_1$, $t_2$ | $x := \bar\pi/2$ (chord midpoint); $t$ a half-step variable; $t_1$ from Rolle, $t_2$ from the mean value theorem | proof-local |
| $u_1$, $u_2$ | the two auxiliary functions of Steps 6 and 7 | proof-local; card §4.6 permits $u_1,u_2$ proof-local and forbids a bare $u$, which is respected |
| $\rho$ | the Peano remainder of H7, $\rho(t) = o(t^2)$ | proof-local |
| $\bar A$ | $\sup\lvert A'_\kappa\rvert$ of H8 | proof-local |
| $\delta$ | radius of the right-neighbourhood in H7 | proof-local |
| $h''(0)$, $h'''(0)$, $h'(0)$ | derivatives of $h$ **read as a function on $[0,1]$** under H4 | not a new symbol, but a changed reading of a card symbol: card §4.4 defines $h(\mathcal I)$ on information sets, where $h''$ has no meaning |
| $r(\bar\pi)$ | check-only ratio $C_h(\bar\pi)/(\tfrac14 h''(0)\bar\pi^2)$ | check-only |
| $\mathcal P_0$, $\mathcal P_1$ | check-only affine coefficients of $\mathcal P$ | check-only |

---

## NOT CLAIMED

1. **No "iff".** C1 is an identity, and the vanishing direction runs one way only: $C_h(\bar\pi)=0
   \Rightarrow$ no interior motion, and $\bar\pi\downarrow 0 \Rightarrow$ motion $\to 0$. Zero
   interior motion does **not** imply a zero chord ($A'_\kappa = 0$ does it too), and a zero chord
   does not imply $h$ affine.
2. **The maintained orientation is not derived.** $C_h \le 0$ and $\lvert C_h\rvert$ weakly
   increasing in $\bar\pi$ are A($\tau$) hypotheses, used nowhere in the proofs of C1–C3 and proved
   nowhere here. Step 12 shows only local consistency at $\bar\pi$ near $0$, and only after granting
   $\mathcal P' \ge 0$.
3. **No sign for $A'_\kappa$.** Whether liquidity spreads or contracts the pooled posterior is not
   determined here, so no sign is claimed for $\partial_\kappa M_P$ itself — only its magnitude
   $\Delta_m\lvert A'_\kappa\rvert\lvert C_h\rvert$ and the fact that the sign is
   $-\mathrm{sgn}(A'_\kappa)$ when $C_h < 0$.
4. **Nothing about the flagged cell**, about $M_F$, about $\Omega$, or about $\mathcal S =
   (1-\Omega)\mathcal S_P$. L3 is a within-pooled-cell statement at fixed $(\tau,T)$.
5. **No claim that $\bar\pi \downarrow 0$ is reachable** by tightening $\tau$. That the tightening
   path drives the upper support point down is L4's business, not L3's; C3 is a statement about a
   limit, agnostic about what produces it.
6. **No claim that A($\tau$) itself holds** — that the pooled posterior really is three-point,
   symmetric, and moves in the $(1,-2,1)$ direction. That is a hypothesis about a primitive object,
   and C4 shows it has a strong side effect (a $\kappa$-invariant pooled engagement share) that
   should be checked against the model before A($\tau$) is treated as innocuous.
7. **No uniformity over a family of kernels.** The $o(\bar\pi^2)$ of C3 is for one fixed $h$ (H8);
   if $h$ shifted with the margin, the remainder would need its own uniform control.
8. **No general-equilibrium content.** Fixed policies throughout (H9); nothing about $\mathcal T$,
   $L_{\mathcal R}$, or C1-the-result (the card's certification result, distinct from this
   document's claim C1).

---

## VERDICT

**PROVED-WITH-CHANGES.**

The three things ticket 27 asked for are established: the weight-derivative identity
$\partial_\kappa\mathbb E[h] = A'_\kappa C_h(\bar\pi)$ (Step 5), an exact mean-value form
$C_h(\bar\pi) = \tfrac14 h''(\zeta)\bar\pi^2$ with $\zeta \in (0,\bar\pi)$ (Step 8), and the
quadratic corollary $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$ with the resulting
$O(\bar\pi^2)$ vanishing (Steps 9–10). The card's constant $\tfrac14$ is correct.

Every change, named:

**CH1 — §4.4's $\bar\pi$ row is wrong and must be amended.** The card glosses $\bar\pi$ as the
"pre-order pooled engagement share in the chord". Under A($\tau$), $\bar\pi$ is the **upper support
point** of the pooled engagement posterior; the share is $\mathbb E[\Pi_\kappa] = \bar\pi(1 - A_0 -
\tfrac12 A_{1/2})$, strictly smaller unless the law is degenerate at $\bar\pi$ (Step 11). Sharper:
under A($\tau$) the share is $\kappa$-**invariant**, so it could not be the quantity whose
$\kappa$-motion L3 describes. Adopting the orchestrator's ruling (a).

**CH2 — new hypothesis H3: $\bar\pi$ is $\kappa$-free at fixed $(\tau,T)$.** Without it Step 3 gains
a term that is first order in $\bar\pi$, and C3's vanishing conclusion is false (F1). This is the
one omission that could sink the result rather than merely qualify it.

**CH3 — new hypothesis H4: $h$ depends on the information set only through $\pi$.** Card §4.4
defines $h(\mathcal I) = \pi(\mathcal I)p(\mathcal I)$ on information sets, and A($\tau$)'s right
side applies $h$ to the three numbers $0, \bar\pi/2, \bar\pi$. The two are reconciled only if $h$
descends to a function on $[0,1]$, which needs the pooled price to satisfy $P = \mathcal P(\pi)$
(F2). Adopting the orchestrator's ruling (b) and recording it as an explicit hypothesis: it is a
real restriction on the pricing map, not a notational convenience.

**CH4 — regularity for the mean-value form, stated minimally (H6): $h$ continuous on $[0,\bar\pi]$
and twice differentiable on the open $(0,\bar\pi)$.** Continuity of $h''$ is **not** needed —
Darboux's theorem on $h''$ (a derivative, hence with the intermediate value property) collapses the
two-point average of (7.1) into a single $h''(\zeta)$ (Step 8). The card names no regularity for $h$
anywhere.

**CH5 — extra regularity for the corollary, stated minimally (H7): a second-order Peano expansion of
$h$ at $0+$**, i.e. $h(t) = h(0)+h'(0)t+\tfrac12 h''(0)t^2+o(t^2)$. Weaker than $h\in C^2[0,\delta)$,
and it is what gives the card's symbol $h''(0)$ a meaning. F3 exhibits a kernel satisfying H6 but not
H7 for which the rate is $\bar\pi^{3/2}$ and the maintained sign $C_h \le 0$ reverses.

**CH6 — H8's uniformity: $\lvert A'_\kappa\rvert$ bounded uniformly in $\bar\pi$ along the limit,
and $h$ fixed along it.** §4.4's "bounded on $[0,1]$" is boundedness in $\kappa$ at a fixed margin,
which is not enough for Step 10 (F5). This is exactly the seam where L4 consumes L3, so it belongs
in L3's hypotheses.

**CH7 — "if", never "iff", with the $C_h = 0$ case explicit.** Recorded in the corollary to Step 8
and in NOT CLAIMED item 1. Adopting the orchestrator's ruling (c).

No obstruction was found. With CH1–CH7 written into card §4.4 and §5, L3 is a theorem; without them
the card's sentence as printed is not one.
