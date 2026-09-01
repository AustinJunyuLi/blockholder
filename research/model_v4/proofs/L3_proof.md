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
