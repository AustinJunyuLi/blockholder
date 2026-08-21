# P1 — Cutoff PBE existence (full proof)

**Written against MODEL CARD v4, version stamp 2026-08-20 · commit `0c9185b`.**
Sources consumed: card §§2–5 and §8; `threads/thread1_turn1_answer.md` §P1 (the statement);
`threads/thread1_turn2_audit.md` (the D1 repairs, in particular D1-R2 on the flagged continuum,
and L2-R1/L2-R2 on the injective form of A7 and the no-feedback timing).

---

## CLAIM

Fix the parameter vector $\vartheta$. Under hypotheses h.1–h.12 below — A1–A7 of card §5, together
with the card's §2 no-feedback timing, D1, the flagged-closure condition h.11 and the sign
convention h.12 — the two-round model has at least one **cutoff perfect Bayesian equilibrium over
complete contingent plans** in the sense of card §3: a weakly ordered cutoff vector
$k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, together with pooled and flagged
price families at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs
obtained as limits of full-support perturbations, the card §4.3 bidder-entry rule, and a
sequentially optimal flagged component. Under A8 evaluated at $k^\star$, both cells $\mathcal C_F$
and $\mathcal C_P$ carry strictly positive probability, hence both are on path.

h.13 is not needed for either half of the claim; it is used only in Step 20, to turn A8 from an
assumption about $\Omega$ into a statement about a single signal threshold.

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
11. **h.11 [ADDITION] — flagged closure.** For every $j\in\mathcal J$, every $s$ on the flagged set,
    and every feasible round-2 order $Q'\in[0,\bar b-B_j^F(s)]$, there exists $j'\in\mathcal J$ with
    $B_{j'}(s,d)=B_j(s,d)$ for all $d\le f_j(s)$, $a_{j'}=a_j$, and $Q_{j'}^F(s)=Q'$. Equivalently
    (and this is the weakest reading), the round-2 action set is *defined* to be
    $\{Q_{j'}^F(s):j'\in\mathcal J\text{ shares }j\text{'s pooled path up to }f_j\}$ rather than the
    full interval. *Used: Step 12.*
12. **h.12 [ADDITION] — nonnegative premia.** $m_0\ge 0$. Card §4.1 restricts only $m_1>m_0$ and
    $\Delta_m>0$; it does not sign $m_0$. With $\Delta_m>0$ and $\pi\in[0,1]$ this gives
    $\bar m(\mathcal I):=m_0+\pi(\mathcal I)\Delta_m\ge 0$. *Used: Steps 7, 8.*
13. **h.13 [ADDITION] — Voice stake monotonicity across plans.** For Voice plans $j'>j$,
    $B_{j'}(s,d)\ge B_j(s,d)$ for every $(s,d)$. Not in the card; the card orders the menu by
    "aggressiveness" without tying that order to the stake path. *Used: Step 20 only, for the
    threshold reformulation of A8 — not for existence.*

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

**Step 5 (pooled layer: A5 on a finite index set).**
By Step 3 there are finitely many pooled public histories. For each of them, h.5 supplies a unique
fixed point of $\mathcal P_{\mathcal I}$, and h.5's continuity clause makes it continuous in beliefs
and cutoffs. A finite family of numbers requires no selection argument: the pooled price family
$k\mapsto (P_d^P(\mathcal H_d^P;k))_{\mathcal H_d^P}$ is a finite vector of continuous functions of
$k$, on those histories that carry positive probability under the conjecture $k$. Histories of zero
probability under $k$ are handled in Step 9.

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
scalar $\hat v(\sigma_F;k)=\mathbb E[v\mid\sigma_F,D=1]$. Write $g(\cdot)$ for the map sending a
belief $\hat v$ to the unique root of $\mathcal P(\cdot)-\mathrm{id}$ at $(\hat v,\pi=1)$. h.5's
uniqueness clause makes $g$ single-valued and h.5's continuity-in-beliefs clause makes $g$
continuous.

(c) $\sigma_F\mapsto\hat v(\sigma_F;k)$ is Borel measurable. Two routes, both available: it is a
conditional expectation with respect to $\sigma(\sigma_F)$ and hence $\sigma(\sigma_F)$-measurable
by construction; and under h.7 the map $(j,s)\mapsto\sigma_F$ is injective on the flagged set and
Borel by Step 2, so — both $\mathcal J\times\mathbb R$ and $[0,\bar b]^2\times\{1\}$ being Borel
subsets of Polish spaces — Lusin–Souslin gives a Borel inverse $\iota_F$ on the image, and
$\hat v(\sigma_F;k)=\mu_v+\beta\bigl(\iota_F(\sigma_F)_s-\mu_v\bigr)$ with $\beta$ the card §4.1
projection coefficient. Injectivity plus measurability already delivers the measurable inverse; no
separate assumption is introduced.

(d) Therefore $P^F(\sigma_F;k)=g\bigl(\hat v(\sigma_F;k)\bigr)$ is the composition of a Borel map
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
limit family. Off-path beliefs at flagged nodes carry no free parameter — a consequence of h.7
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
in $(j,s)$; and by card §4.3 the control-node price on that branch is $P^F$. Card §2.10's payoff
$U_j(s)=\mathbb E[b_j^*(s)Y-\mathcal C_j^{\mathrm{trade}}-C_j(s)\mid s,j]$ therefore splits as
$$
U_j(s;k)\;=\;\underbrace{b_j^*(s)\,\mathbb E\bigl[Y\mid s,j,D=1\bigr]-P^F(\sigma_F)\,Q_j^F(s)-C_j(s)}_{\text{flagged continuation: deterministic in }(j,s)}
\;-\;\underbrace{\mathbb E_{z}\Bigl[\textstyle\sum_{d\le f_j}P_d^P\bigl(\mathcal H_d^P\bigr)\bigl(B_j(s,d)-B_j(s,d-1)\bigr)\Bigr]}_{\text{pooled execution: determined by the pooled path alone}} ,
$$
where the pooled expectation is over the noise $z_{0:H}$ only. The noise enters the first bracket
nowhere: $\mathbb E[Y\mid s,j,D=1]$ depends on $(v,\xi)$ and on $P^F$, and $\xi$ is independent of
$z$ by h.1 while $P^F$ is $z$-free by Step 6.

**Step 12 (h.11 makes the flagged component sequentially optimal, and without h.11 nothing does).**
Let $k$ be a conjecture and let $j=j_k(s)$ maximise $U_{\cdot}(s;k)$ over $\mathcal J$. Suppose some
feasible round-2 order $Q'$ strictly improves the flagged continuation at $(j,s)$, holding the
market's flagged pricing schedule at the family of Step 6. By h.11 there is $j'\in\mathcal J$ with
the same pooled path up to $f_j(s)$, the same engagement flag, and $Q_{j'}^F(s)=Q'$. Identical
pooled paths give identical order marks $q_{j'd}=q_{jd}$ for $d\le f_j$ (h.10, Step 2), hence
identical realised pooled histories for every noise draw and therefore an identical second bracket
in Step 11's decomposition. The first bracket is strictly larger at $j'$ by assumption. So
$U_{j'}(s;k)>U_j(s;k)$, contradicting the optimality of $j$ at $s$. Hence no feasible flagged
deviation improves, which is sequential optimality of the flagged component.

The converse direction is the honest part. Without h.11, date-0 optimality over $\mathcal J$
constrains only those round-2 orders that appear as the flagged component of some menu element
paired with the same pooled path; an order outside that set is never compared, so a fixed point of
$\mathcal T$ can fail item (ii) of card §3 at the flagged node while satisfying every other item.
**Sequential optimality of the flagged component does not follow from A1–A7 and is not a free
consequence of complete contingent plans; h.11 is the weakest condition that delivers it, and its
weakest reading is a restriction on the round-2 action set rather than on the menu.** The turn-1
statement of P1 listed "sequential optimality of the flagged component" as its Hypothesis 6 without
content; h.11 is that content.

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
v$ payoff form with ordered slopes. Card §2.10 does not impose that form on a general finite menu:
it imposes increasing differences only. At the card's level of generality the common bracket is
therefore **assumed**, and it is the first of the two things h.6 is doing.

**Step 15 (continuity: this is where h.6 assumes rather than derives, and here is exactly what it is
assuming).**
$U_j(s;k)$ is continuous in $k$ for each fixed $(j,s)$: by h.5 the pooled and flagged inner prices
are continuous in the cutoffs, and by Step 4 they enter $U_j$ only through $(\hat v,\pi)$, which are
ratios of integrals over signal intervals with endpoints $k$ and are continuous in $k$ wherever the
conditioning event has probability bounded away from zero; at histories of vanishing probability
the Step 9 perturbation limit supplies the value. Continuity of $\mathcal T$ in $k$ needs two more
things that the card does not supply:

 (i) *continuity in the signal*: $s\mapsto\bigl(B_j(s,\cdot),b_j^*(s),C_j(s)\bigr)$ continuous, so
 that $s\mapsto U_j(s;k)$ is continuous. Card §4.2 imposes monotonicity on the stake path and
 nothing else; a plan that acquires a block discontinuously at a signal trigger is permitted by the
 card and makes $U_j(\cdot;k)$ jump, at which point the best-response cutoff is a jump point rather
 than a crossing point and moves discontinuously with $k$.

 (ii) *transversality*: for every adjacent pair $(i,i+1)$ and every $k\in\Theta$, the indifference
 set $\{s:U_{i+1}(s;k)=U_i(s;k)\}$ has empty interior. h.3 says the difference crosses zero "at
 most once", which does not exclude an interval on which it is identically zero; on such an
 interval the cutoff is indeterminate, and as the interval opens and closes with $k$ the selection
 $\mathcal T_i$ jumps.

**Under (i) and (ii), continuity of $\mathcal T$ is implied by continuity of $U$ in $(s,k)$ together
with the strict sign change of $U_{i+1}-U_i$ at each crossing, which locates the crossing by the
implicit function theorem and moves it continuously with $k$. h.6 assumes the conclusion instead: it asserts continuity of
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
continuous in $(s,k)$ under Step 15(i) alone. Kakutani's theorem then gives a fixed point without
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

The reformulation that gives h.8 something to bite on: suppose in addition (a) the engagement flags
$a_j$ are $1$ exactly on an upper set of the ordered menu, (b) $\partial_s B_j\ge0$ on Voice plans
(card §4.2), and (c) h.13. Then the flagged set
$\{s:a_{j_{k^\star}(s)}=1\text{ and }B_{j_{k^\star}(s)}(s,H-T)\ge\tau\}$ — the equivalence
$f_j\le H\iff B_j(s,H-T)\ge\tau$ is h.9 — is an upper interval of signals: the first condition is
an upper set because $j_{k^\star}$ is weakly increasing and (a); within it, $s\mapsto
B_{j_{k^\star}(s)}(s,H-T)$ is weakly increasing because it increases in $s$ at fixed plan by (b) and
increases across plans by (c). Writing $s_F(k^\star)$ for the infimum of that upper interval,
$\Omega=1-\Phi_s\bigl(s_F(k^\star)\bigr)$ with $\Phi_s$ the signal c.d.f., and h.8 is equivalent to
$s_F(k^\star)$ being finite and strictly above $-\infty$. **Condition (c) is h.13, which is not in
the card**: the card orders the menu by aggressiveness without tying that order to the stake path,
so without h.13 the flagged set need not be an interval and $\Omega$ need not be a single-threshold
object.

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
2. **h.11 fails: the menu is not closed under flagged deviations.** Take
   $\mathcal J=\{\text{Exit},\text{Hold},\text{one Voice plan}\}$ with the Voice plan's terminal
   target $b^*(s)$ chosen for its pooled-execution properties. The round-2 problem
   $\max_{Q}\ b^*Y-P(F,Q)Q$ has a first-order condition that the single available $Q^F=b^*-B^F$
   generically does not satisfy. The fixed point of $\mathcal T$ then exists and satisfies items
   (i), (iii)–(vi) of card §3 but fails item (ii) at the flagged node: it is a date-0 equilibrium,
   not a PBE. This is the concrete case in which P1's claim is false as stated under A1–A7 alone.
3. **h.6's continuity fails through an indifference plateau (Step 15(ii)).** Let the engagement cost
   $C_j(s)$ be constant on an interval $[\alpha,\beta]$ and let the conjecture be such that
   $U_{i+1}(\cdot;k)-U_i(\cdot;k)\equiv 0$ there. Every $k_i\in[\alpha,\beta]$ represents a best
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
2. The proof consumes two hypotheses that are not in card §5 — h.11 (flagged closure) and h.12
   ($m_0\ge0$) — plus h.13 for the Step 20 reformulation. Card §5 would have to absorb h.11 and h.12
   before "under A1–A7" in the card's P1 row is an accurate antecedent. As written, the card's P1
   row overstates what A1–A7 deliver, because sequential optimality of the flagged component
   (item (ii) of card §3) is not among their consequences (Step 12, WHERE IT FAILS 2).
3. The proof cites h.9 = D1, which itself carries the label CONJECTURE. P1 inherits that
   conditionality regardless of how this document is audited.

The intended final label remains PROVED, conditional on the card absorbing h.11 and h.12 and on D1
clearing its own re-derivation.

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
   resolution). The sharp prediction is conditional: **on a menu satisfying h.11 the maximum gain is
   $0$ to within $10^{-9}$ premium percentage points at every tuple; on a menu that does not close,
   a strictly positive gain of order $10^{-2}$ premium percentage points appears at a positive
   fraction of tuples.** Reporting a positive gain therefore refutes h.11 for that menu, not P1.
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
| $U_j(s;k)$ | blockholder's conditional expected payoff to plan $j$ at signal $s$ under conjecture $k$; the object of card §2.10 with the conjecture displayed | matches the frozen manuscript's blockholder utility; **never a bare $U$** |
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
   NUMERICAL CHECK 4 is designed to test it, not to assume it.
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
