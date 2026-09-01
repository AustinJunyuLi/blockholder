# L4 — independent re-derivation (ticket 27)

**Inputs seen:** `research/model_v4/MODEL_CARD.md` (version stamp 2026-08-21, commit `a175202`+)
**and the amended L4 statement + A(br) as handed to me in the task message.**
`proofs/` and `threads/` were **not** opened. Card stamp checked before writing.

**VERDICT: PROVED-WITH-CHANGES.** Legs 1 and 2 go through as stated with no addition beyond one
edge hypothesis made explicit. Leg 3 goes through with one **added** A(br) clause (`br-ii′`,
τ-invariance of the kernel), one A(br) clause found **partly redundant** (the trailing "hence"
of `br-ii`, which is a consequence of its own antecedent), and one clause found **load-bearing
and sharpenable** (`br-iv`, for which I give an exact equivalent form). All changes are listed
under CHANGES and again inside the numbered steps that use them.

---

## CLAIM

Fix the policies (the cutoff vector $k$ and the execution policies) and fix the window
$T \in \{1,\dots,H\}$. Let $b_0 < \tau' < \tau$ be two admissible stake thresholds, compared at a
common noise-trading intensity $\kappa$. Then

- **(Leg 1)** $\mathcal C_F(\tau,T) \subseteq \mathcal C_F(\tau',T)$ and hence
  $\Omega(\tau',T) \ge \Omega(\tau,T)$;
- **(Leg 2)** $\bar\pi_{\mathrm{pr}}(\tau') \le \bar\pi_{\mathrm{pr}}(\tau)$, where
  $\bar\pi_{\mathrm{pr}}(x) := \Pr(a=1 \mid D=0 \text{ at threshold } x)$;
- **(Leg 3)** $\mathcal S_P(\tau') \le \mathcal S_P(\tau)$, where
  $\mathcal S_P(x) = \lvert\partial_\kappa M_P(x)\rvert$.

All three inequalities are **weak**; the equality cases are characterised in Steps 7, 13 and 21.

---

## HYPOTHESES

Each is used; the steps that use it are named.

| # | Hypothesis | Source | Used in |
|---|---|---|---|
| **H1** | **Fixed policies + no within-window re-optimisation.** The cutoff vector $k$ and the execution policies are held at one common setting for both thresholds; by §2, $B_j(s,d)$, $q_{jd}(s)$ and $Q_j^F$ are functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone, with no feedback from order flow or prices. | card §2, §4.2; amended statement ("at fixed policies") | 1, 2, 22 |
| **H2** | **Admissible threshold pair.** $b_0 < \tau' < \tau$, both thresholds paired with the same $T \in \{1,\dots,H\}$, so $H-T \ge 0$. | amended statement; card §4.1, §4.2 (maintained $b_0 < \tau$) | 2, 3, 4 |
| **H3** | **A4 legal-clock discipline.** $c$ is the first date the path reaches the threshold; the filing lands exactly at $c+T$; only Voice plans cross in the core. | card §5 A4 | 3, 4, 5 |
| **H4** | **D1's clock equivalence (ledger statement).** For every Voice plan, $f_j \le H \iff B_j(s,H-T) \ge \tau$. | card §6, D1 row; card §4.2 $f_j$ row | 4, 5 |
| **H5** | **[ADDED — see CHANGE 1] Pooled mass at the tighter threshold.** $\Omega(\tau',T) < 1$, i.e. A8's upper half read at $\tau'$. | card §5 A8, read at $\tau'$ | 11, 12, 13, 17 |
| **H6** | **Flagged $\Rightarrow$ engaged.** $D=1 \Rightarrow a=1$; equivalently $\pi(\mathcal I)=1$ on $\mathcal C_F$. | card §4.2 $D_j$ row, §4.3 $\pi$ row | 9 |
| **H7** | **A($\tau$)'s coefficient structure and maintained magnitude monotonicity.** $A_0' = A_1' = A'_\kappa$, $A_{1/2}' = -2A'_\kappa$; $\lvert C_h\rvert$ weakly increasing in $\bar\pi$. Also $\Delta_m = m_1 - m_0 > 0$ and $\kappa$-free (card §4.1 primitives). | card §5 A($\tau$), §4.4 | 16, 17, 19, 23 |
| **H8** | **L3's statement, first half.** Under A($\tau$) the pooled cell's interior $\kappa$-motion is proportional to $C_h(\bar\pi)$. | card §6, L3 row | 16 (corroborative only — see CHANGE 4) |
| **H9** | **A(br)(i)–(iv)** exactly as supplied with the amended statement. | task message | 14, 15, 18, 20 |
| **H10** | **[ADDED — see CHANGE 3] (br-ii′) $\tau$-invariance of the kernel.** At fixed policies and common $\kappa$, the map $\pi \mapsto h(\pi)$ used in the pooled ternary representation — and therefore the function $\bar\pi \mapsto C_h(\bar\pi)$ — is the same at $\tau$ and at $\tau'$. | added by this re-derivation | 19 |
| **H11** | **Common $\kappa$.** All cross-threshold comparisons of $A'_\kappa$, $C_h$ and $\mathcal S_P$ are made at one and the same value of $\kappa$. | added as an explicitness repair (CHANGE 2) | 17, 20, 21 |

---

## PROOF

### Part 0 — setup

**Step 1.** By H1 the cutoff vector $k$ is held fixed across the two thresholds, so it induces one
selection map $j(\cdot)$ sending a signal $s$ to the plan it plays. Write $A := a_{j(s)}$ for the
engagement attached to the selected plan (card §4.2, $a_j$ row). $A$ is a function of $s$ alone and
carries no dependence on the threshold, since $a_j$ is attached to the plan, not to the threshold.

**Step 2.** By H2, $H - T \ge 0$, so the day $H-T$ is on the calendar and the random variable
$$\Lambda := B_{j(s)}(s,\,H-T)$$
is well defined. By H1 (no feedback), $B_j(s,d)$ is a function of $(j,s,d)$ alone, so by Step 1 the
joint law of $(A,\Lambda)$ is a function of the primitives and the fixed policies only: **it does not
depend on the threshold.** The threshold enters below only as the level against which $\Lambda$ is
compared. This is the single fact that makes a cross-threshold comparison a comparison of one random
variable against two levels rather than a comparison of two different random variables.

**Step 3.** By H2, $b_0 < \tau' < \tau$. By card §4.2 a Hold path is constant at $b_0$ and an Exit
path is weakly decreasing from $b_0$; neither reaches $\tau'$, and *a fortiori* neither reaches
$\tau$. Hence at **both** thresholds only Voice plans cross, which is what H3 (A4) maintains for the
core, and at both thresholds $c_j$ is the first date a path strictly below the level reaches it.
The clause "both strictly above the initial stake" in the amended statement is therefore
**load-bearing**: it is what carries A4's core discipline and D1's applicability down from $\tau$
to $\tau'$. Step 3 is used again in Step 4.

### Part A — Leg 1: the nested-cell inclusion and $\Omega$

**Step 4.** By Step 3 the threshold $\tau'$ is admissible in the same sense $\tau$ is, so H4 (D1's
clock equivalence) may be read at either level $x \in \{\tau',\tau\}$: for every Voice plan,
$$f_j \le H \iff B_j(s,\,H-T) \ge x .$$

**Step 5.** Fix a level $x \in \{\tau',\tau\}$ and let $D^{(x)}$ denote the disclosure indicator at
that level. By card §4.2, $D^{(x)} = \mathbf 1\{a_j = 1,\ c_j(s;x)<\infty,\ f_j \le H\}$. Take the
two inclusions in turn.

- *If $D^{(x)}=1$:* then $a_j=1$ and $f_j \le H$, so by Step 4, $\Lambda \ge x$.
- *If $A=1$ and $\Lambda \ge x$:* the plan is Voice, and $B_j(s,H-T) \ge x$ with $B_j(s,-1)=b_0 < x$
  (Step 3) gives $c_j(s;x) \le H-T < \infty$, so the second conjunct holds; Step 4 then gives
  $f_j \le H$, the third conjunct. Hence $D^{(x)}=1$.

Therefore
$$\mathcal C_F(x,T) \;=\; \{A=1\} \cap \{\Lambda \ge x\}. \tag{5.1}$$

**Step 6.** By H2, $\tau' < \tau$, so $\{\Lambda \ge \tau\} \subseteq \{\Lambda \ge \tau'\}$.
Intersecting both sides with $\{A=1\}$ and applying (5.1) at each level:
$$\mathcal C_F(\tau,T) \;\subseteq\; \mathcal C_F(\tau',T). \tag{6.1}$$
By Step 2 the two sides are events for **one** pair $(A,\Lambda)$ under **one** probability measure,
so (6.1) is a genuine set inclusion and not a comparison across two models.

**Step 7.** Monotonicity of a probability measure applied to (6.1):
$$\Omega(\tau',T) \;=\; \Pr\big(\mathcal C_F(\tau',T)\big) \;\ge\; \Pr\big(\mathcal C_F(\tau,T)\big) \;=\; \Omega(\tau,T).$$
Equality holds exactly when $\Pr(A=1,\ \tau' \le \Lambda < \tau) = 0$, i.e. when no engaging type has
its day-$(H-T)$ stake in the opened band. **Leg 1 is proved.**

### Part B — Leg 2: the newly flagged block, spelled out

**Step 8.** Define the **newly flagged set**
$$N \;:=\; \mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T) \;\stackrel{(5.1)}{=}\; \{A=1,\ \tau' \le \Lambda < \tau\}.$$
By card §4.3 the flagged and pooled cells are exclusive and exhaustive, so
$\mathcal C_P(x,T)$ is the complement of $\mathcal C_F(x,T)$. Since $N \cap \mathcal C_F(\tau,T)=\varnothing$
(Step 8's definition), $N \subseteq \mathcal C_P(\tau,T)$; and since $N \subseteq \mathcal C_F(\tau',T)$,
$$\mathcal C_P(\tau',T) \;=\; \mathcal C_P(\tau,T)\setminus N. \tag{8.1}$$
In words: lowering the threshold moves the block $N$, and only that block, out of the pooled class.

**Step 9 (the newly-flagged-is-Voice arithmetic — the load-bearing fact).** Every element of $N$ lies
in $\mathcal C_F(\tau',T)$, so it carries $D^{(\tau')}=1$, so by H6 it carries $a=1$. Hence
$$\Pr(a=1 \mid N) = 1 \quad\text{whenever } \Pr(N)>0, \qquad\text{equivalently}\qquad \Pr(a=1,\ N) = \Pr(N). \tag{9.1}$$
The engagement share of the removed block is **1, the maximum a share can take**. This is what makes
Leg 2 unconditional: no assumption is needed about where the removed types sit relative to the rest
of the pooled class, because there is nothing above 1 for the remainder to be compared against.

**Step 10 (bookkeeping).** Write
$$w := \Pr\big(\mathcal C_P(\tau,T)\big), \quad g := \Pr\big(a=1,\ \mathcal C_P(\tau,T)\big), \quad n := \Pr(N) \ge 0,$$
$$w' := \Pr\big(\mathcal C_P(\tau',T)\big), \quad g' := \Pr\big(a=1,\ \mathcal C_P(\tau',T)\big).$$
By (8.1), $w' = w - n$. By (8.1) and (9.1), $g' = g - \Pr(a=1,N) = g - n$. Also $0 \le g \le w$ and
$0 \le g' \le w'$, since an intersection has no more mass than the set. By definition
$\bar\pi_{\mathrm{pr}}(\tau) = g/w$ and $\bar\pi_{\mathrm{pr}}(\tau') = g'/w'$.

**Step 11.** By H5, $w' = 1 - \Omega(\tau',T) > 0$, so $\bar\pi_{\mathrm{pr}}(\tau')$ is defined; and
$w = w' + n \ge w' > 0$, so $\bar\pi_{\mathrm{pr}}(\tau)$ is defined as well. **H5 at $\tau'$ alone
suffices** — the pooled cell at the looser threshold is at least as large (Step 7), so its positivity
is derived, not assumed.

**Step 12 (mixture form).** Using $w = w'+n$ and $g = g'+n$ from Step 10, and setting
$\theta := w'/(w'+n) \in (0,1]$:
$$\bar\pi_{\mathrm{pr}}(\tau) \;=\; \frac{g'+n}{w'+n} \;=\; \frac{w'}{w'+n}\cdot\frac{g'}{w'} \;+\; \frac{n}{w'+n}\cdot 1 \;=\; \theta\,\bar\pi_{\mathrm{pr}}(\tau') + (1-\theta)\cdot 1 . \tag{12.1}$$
The pooled share at the **looser** threshold is a convex combination of the pooled share at the
tighter threshold and the removed block's share, which Step 9 pinned at 1.

**Step 13.** Subtract $\bar\pi_{\mathrm{pr}}(\tau')$ from both sides of (12.1):
$$\bar\pi_{\mathrm{pr}}(\tau) - \bar\pi_{\mathrm{pr}}(\tau') \;=\; (1-\theta)\big(1 - \bar\pi_{\mathrm{pr}}(\tau')\big) \;=\; \frac{n}{w'+n}\Big(1 - \frac{g'}{w'}\Big) \;\ge\; 0,$$
because $n \ge 0$, $w'>0$ (Step 11) and $g' \le w'$ (Step 10). Hence
$$\bar\pi_{\mathrm{pr}}(\tau') \;\le\; \bar\pi_{\mathrm{pr}}(\tau).$$
Equality holds exactly when $n=0$ (no type is newly flagged) or $g'=w'$ (the pooled class at $\tau'$
is entirely engaging, so its share is already 1 and removing more mass at share 1 changes nothing).

*Cross-check by direct cross-multiplication.* $(g-n)/(w-n) \le g/w$ with $w-n=w'>0$ and $w>0$ is
equivalent to $w(g-n) \le g(w-n)$, i.e. $wg - wn \le gw - gn$, i.e. $gn \le wn$, i.e.
$n(g-w) \le 0$, which holds because $n \ge 0$ and $g \le w$. Same inequality, same equality cases.
**Leg 2 is proved.** Note what was *not* used: no monotone structure on $\Lambda$, no ordering of
signals inside the pooled class, no property of $\kappa$, no property of the kernel $h$.

### Part C — Leg 3: the sensitivity $\mathcal S_P$

**Step 14.** By H9 (br-i), read at $x \in \{\tau',\tau\}$ for the pooled class:
$$M_P(x) \;=\; \Delta_m\,\mathbb E[h \mid D^{(x)}=0] \;=\; \Delta_m\Big[A_0(\kappa;x)h(0) + A_{1/2}(\kappa;x)h\big(\tfrac{\bar\pi(x)}{2}\big) + A_1(\kappa;x)h\big(\bar\pi(x)\big)\Big],$$
with chord endpoint $\bar\pi(x)$ and weight-derivative coefficient $A'_\kappa(x)$. This is defined at
both thresholds by Step 11 (card §4.4: $M_P$ is defined when the cell has mass).

**Step 15.** By H9 (br-ii) the whole $\kappa$-dependence of $M_P$ at fixed policies sits in the
weights: the support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$ as a function of the
posterior do not move with $\kappa$; and $\Delta_m$ is a primitive (card §4.1), hence $\kappa$-free.
Differentiating Step 14 in $\kappa$ with those three objects held fixed:
$$\partial_\kappa M_P(x) \;=\; \Delta_m\Big[A_0'(\kappa;x)h(0) + A_{1/2}'(\kappa;x)h\big(\tfrac{\bar\pi(x)}{2}\big) + A_1'(\kappa;x)h\big(\bar\pi(x)\big)\Big].$$
The $A_i'$ exist by H7 (A($\tau$) names them) and are bounded on $[0,1]$ (card §4.4).

**Step 16.** Substitute H7's coefficient structure $A_0'=A_1'=A'_\kappa$, $A_{1/2}'=-2A'_\kappa$ into
Step 15 and factor:
$$\partial_\kappa M_P(x) \;=\; \Delta_m A'_\kappa(x)\Big[h(0) - 2h\big(\tfrac{\bar\pi(x)}{2}\big) + h\big(\bar\pi(x)\big)\Big] \;=\; \Delta_m\,A'_\kappa(x)\,C_h\big(\bar\pi(x)\big), \tag{16.1}$$
using the card §4.4 definition $C_h(\bar\pi) = h(0)-2h(\bar\pi/2)+h(\bar\pi)$. This reproduces H8
(L3's proportionality) **with the constant of proportionality named** as $\Delta_m A'_\kappa(x)$.
Two consequences worth recording: (a) the trailing "hence $\partial_\kappa M_P = \Delta_m A'_\kappa
C_h(\bar\pi)$ exactly" inside (br-ii) is a **derived** statement, not an independent assumption
(CHANGE 4); (b) naming the constant is exactly what a cross-threshold comparison needs — L3's bare
"proportional to" would leave an unnamed threshold-dependent factor and would not license Step 21.

**Step 17.** Take absolute values in (16.1). $\Delta_m > 0$ by H7, so
$$\mathcal S_P(x) \;=\; \lvert\partial_\kappa M_P(x)\rvert \;=\; \Delta_m\,\big\lvert A'_\kappa(x)\big\rvert \cdot \big\lvert C_h(\bar\pi(x))\big\rvert, \tag{17.1}$$
a product of two non-negative factors, evaluated at the common $\kappa$ of H11.

**Step 18.** By H9 (br-iv), $\bar\pi(x) = \varphi(\bar\pi_{\mathrm{pr}}(x))$ for one weakly increasing
$\varphi$ used at both thresholds. Step 13 gives $\bar\pi_{\mathrm{pr}}(\tau') \le
\bar\pi_{\mathrm{pr}}(\tau)$, so applying $\varphi$ to both sides:
$$\bar\pi(\tau') \;\le\; \bar\pi(\tau). \tag{18.1}$$
This is the only place Leg 2 enters Leg 3, and (br-iv) is the only bridge available: by the binding
orchestrator ruling, $\bar\pi$ is the **upper support point** of the pooled posterior while
$\bar\pi_{\mathrm{pr}}$ is the pooled share $\mathbb E[\Pi_\kappa]$, which sits strictly below it, so
Leg 2's inequality does not by itself move $\bar\pi$. Steps 22–24 sharpen this.

**Step 19.** By H7 the map $\bar\pi \mapsto \lvert C_h(\bar\pi)\rvert$ is weakly increasing, and by
H10 (br-ii′) it is the **same** map at both thresholds. Combining with (18.1):
$$\big\lvert C_h(\bar\pi(\tau'))\big\rvert \;\le\; \big\lvert C_h(\bar\pi(\tau))\big\rvert. \tag{19.1}$$
Without H10 this step does not close: the kernel $h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$ carries
the entry probability $p$, which by card §4.3 depends on the pooled price $P$, and the pooled price is
priced off a cell whose composition the threshold moves. A($\tau$) and (br-ii) quarantine only
$\kappa$-movement of $h$, not $\tau$-movement. See CHANGE 3.

**Step 20.** By H9 (br-iii), at the common $\kappa$ of H11,
$$\big\lvert A'_\kappa(\tau')\big\rvert \;\le\; \big\lvert A'_\kappa(\tau)\big\rvert. \tag{20.1}$$
Nothing in Legs 1–2 or in the card pins this magnitude — card §4.4 records only that $A'_\kappa$ is
bounded on $[0,1]$ — so (br-iii) is a substantive, unearned assumption rather than a bookkeeping one.

**Step 21.** For non-negative reals, $0 \le \alpha' \le \alpha$ and $0 \le \gamma' \le \gamma$ give
$\alpha'\gamma' \le \alpha\gamma$. Apply this to (17.1) with $\alpha = \lvert A'_\kappa(\tau)\rvert$,
$\gamma = \lvert C_h(\bar\pi(\tau))\rvert$ and the primed counterparts, using (19.1) and (20.1) and
$\Delta_m>0$:
$$\mathcal S_P(\tau') \;\le\; \mathcal S_P(\tau).$$
Equality holds when both factors tie, in particular whenever $n=0$ and $\lvert A'_\kappa\rvert$ is
threshold-flat. **Leg 3 is proved under H1–H11.**

### Part D — two derived remarks that sharpen A(br) (not needed for the three legs)

**Step 22.** Let $\Pi_\kappa := \pi(\mathcal I_H)$ on the pooled cell. By card §4.3 the pooled public
history $\mathcal H_d^P$ records whether the flag has landed by $d$, so the event $\{D=0\}$ is
measurable with respect to the control-node information set. The tower property then gives
$$\mathbb E\big[\Pi_\kappa \mid D=0\big] \;=\; \Pr(a=1\mid D=0) \;=\; \bar\pi_{\mathrm{pr}} .$$
By Step 1 and H1, $a$ and $D$ are functions of $s$ alone at fixed policies, so
$\bar\pi_{\mathrm{pr}}$ carries no $\kappa$-dependence.

**Step 23 (the A($\tau$) perturbation is mean-preserving).** Under the ternary representation of
Step 14, $\mathbb E[\Pi_\kappa] = A_{1/2}\bar\pi/2 + A_1\bar\pi = \rho\,\bar\pi$ with
$$\rho(x) := \tfrac12 A_{1/2}(\kappa;x) + A_1(\kappa;x).$$
By H7, $\partial_\kappa\rho = \tfrac12 A_{1/2}' + A_1' = -A'_\kappa + A'_\kappa = 0$: the weight
perturbation shifts mass symmetrically from the midpoint $\bar\pi/2$ to the two endpoints $0$ and
$\bar\pi$ and leaves the mean fixed. This is internally consistent with Step 22 ($\bar\pi_{\rm pr}$
is $\kappa$-free), and it is the structural reason the chord $C_h$ — a second difference — is the
object that survives differentiation in Step 16.

**Step 24 (exact form of (br-iv)).** By Steps 22–23, whenever $\bar\pi(x)>0$,
$$\bar\pi(x) \;=\; \bar\pi_{\mathrm{pr}}(x)\,/\,\rho(x), \qquad \rho(x)\in(0,1),$$
where $\rho<1$ is the orchestrator ruling that the pooled share sits strictly below the upper support
point. Hence (br-iv) is **exactly equivalent** to
$$\frac{\rho(\tau')}{\rho(\tau)} \;\ge\; \frac{\bar\pi_{\mathrm{pr}}(\tau')}{\bar\pi_{\mathrm{pr}}(\tau)} ,$$
i.e. (br-iv) forbids the pooled posterior from becoming dispersed fast enough, as the threshold
tightens, to lift the upper support point even while the mean falls. (br-iv) is therefore neither
redundant nor cosmetic: it is a restriction on how the pooled posterior's spread co-moves with its
mean across thresholds, and this form is directly checkable on a grid (see NUMERICAL CHECK REQUEST).

---

## CHANGES (every one, named)

1. **ADDED H5 — pooled mass at $\tau'$ ($\Omega(\tau',T)<1$, A8's upper half read at $\tau'$).**
   Without it $\bar\pi_{\mathrm{pr}}(\tau')$ and $M_P(\tau')$ are undefined (card §4.4: $M_P$ is
   defined when the cell has mass), and Legs 2 and 3 have no content. It is arguably implicit in
   (br-i), which asserts a representation of the pooled-conditional law at $\tau'$, but the amended
   statement does not say it out loud. The looser-threshold counterpart is **not** needed: Leg 1
   derives $\Omega(\tau,T) \le \Omega(\tau',T) < 1$.
2. **ADDED H11 — a common $\kappa$.** (br-iii) and the conclusion compare $\kappa$-derivatives; the
   statement does not say the two thresholds are compared at one $\kappa$. Used in Steps 17, 20, 21.
3. **ADDED H10 = (br-ii′) — $\tau$-invariance of the kernel. This is an INSUFFICIENCY of A(br) as
   literally written.** (br-ii) quarantines only $\kappa$-movement of $h$ and of the support points.
   Step 19 compares $\lvert C_h\rvert$ **across thresholds**, which needs one function $C_h$, hence
   one kernel $h$ at both thresholds. The kernel is $h=\pi p$ with $p$ depending on the pooled price
   $P$ (card §4.3), and the pooled price is priced off a cell whose composition the threshold moves —
   so $\tau$-invariance of $h$ is a real restriction, not bookkeeping. The card's own notation
   ($C_h(\bar\pi)$ written as a function of $\bar\pi$ alone) already presumes it, so the repair is one
   clause, not a new idea: extend (br-ii)'s "do not move with $\kappa$" to "do not move with $\kappa$
   or with $\tau$". **Recommended wording:** *(br-ii′) at fixed policies and common $\kappa$, the
   kernel $h$ as a function of the posterior is the same at $\tau$ and $\tau'$.*
4. **REDUNDANCY inside (br-ii).** Its trailing clause "hence $\partial_\kappa M_P = \Delta_m\cdot
   A'_\kappa\cdot C_h(\bar\pi)$ exactly" is a **consequence** of (br-ii)'s own antecedent plus (br-i)
   plus A($\tau$)'s coefficient structure plus $\Delta_m$ being a $\kappa$-free primitive. Step 16
   derives it. Keeping it as a hypothesis is harmless but overstates what is assumed.
5. **REDUNDANCY of the L3 citation for Leg 3.** Given (br-i) + (br-ii)'s antecedent + A($\tau$),
   Step 16 produces the identity outright, so L3's statement adds nothing beyond it. L3's *second*
   half ($C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$) is unused; it does corroborate H7's
   maintained monotonicity of $\lvert C_h\rvert$ near $\bar\pi=0$, where the quadratic is increasing.
6. **NARROWING of what A($\tau$) is used for.** Leg 3 uses only the **magnitude** half of A($\tau$)'s
   maintained orientation ($\lvert C_h\rvert$ weakly increasing in $\bar\pi$). The **sign** half
   ($C_h \le 0$) is never used, and the awkward $C_h = 0$ case needs no separate treatment here,
   because the conclusion is an inequality between magnitudes.
7. **CONFIRMED LOAD-BEARING, not changed.** The clause "both strictly above the initial stake"
   ($b_0 < \tau'$): Step 3 shows it is what carries A4's "only Voice plans cross" and D1's
   applicability from $\tau$ down to $\tau'$. It is not decoration.
8. **SHARPENING of (br-iv), not a change to the claim.** Steps 22–24 derive
   $\bar\pi = \bar\pi_{\mathrm{pr}}/\rho$ with $\rho := \tfrac12 A_{1/2}+A_1$ $\kappa$-free, so
   (br-iv) $\iff$ $\rho(\tau')/\rho(\tau) \ge \bar\pi_{\mathrm{pr}}(\tau')/\bar\pi_{\mathrm{pr}}(\tau)$.

---

## WHERE IT FAILS

1. **Pre-existing crossing, $b_0 \ge \tau'$.** Then $c_j(s;\tau')=0$ for *every* plan, Hold and Exit
   included, so A4's "only Voice plans cross in the core" fails at $\tau'$ and Step 3 breaks. The set
   $\mathcal C_F(\tau',T)$ can then contain non-engaging histories, (9.1) becomes
   $\Pr(a=1\mid N)<1$, and Step 13's sign reverses whenever
   $\Pr(a=1\mid N) < \bar\pi_{\mathrm{pr}}(\tau)$: the pooled share **rises**. Leg 1 survives (the
   inclusion is level-monotone regardless), Legs 2 and 3 do not. This is the boundary card §4.2
   already flags as outside the core (turn-2 audit D1-O1).
2. **Policies re-optimise.** If lowering the threshold shifts the cutoff vector $k$, Step 2 fails —
   $\Lambda$ has two different laws at the two thresholds — and (6.1) is no longer a set inclusion.
   Concretely, a lower threshold that pushes marginal types out of Voice into Hold shrinks
   $\{A=1\}$ and can lower $\Omega$ outright. This is C1's region-certified business
   ($g_r^{PE} > \mathcal B_r^{GE}$), and L4 claims nothing there.
3. **(br-iii) fails.** Suppose the newly flagged block is tiny ($n \approx 0$), so
   $\bar\pi_{\mathrm{pr}}$ and hence $\lvert C_h\rvert$ barely move, while the tighter threshold makes
   the pooled weights more $\kappa$-responsive: $\lvert A'_\kappa(\tau')\rvert = 1.4\lvert
   A'_\kappa(\tau)\rvert$ against $\lvert C_h\rvert$ ratio $0.98$ gives
   $\mathcal S_P(\tau')/\mathcal S_P(\tau) = 1.37 > 1$. Leg 3 fails while Legs 1 and 2 hold.
4. **(br-iv) fails through dispersion.** Removing the highest-posterior types can leave a pooled cell
   whose posterior is *more* spread. With $\bar\pi_{\mathrm{pr}}: 0.30 \to 0.28$ and
   $\rho: 0.60 \to 0.50$, Step 24 gives $\bar\pi: 0.500 \to 0.560$ — the chord endpoint **rises**
   while the mean falls, so (19.1) reverses and $\mathcal S_P$ rises. Leg 2 holds, Leg 3 fails.
5. **The kernel moves with the threshold (the CHANGE 3 gap).** If the tighter threshold raises the
   pooled price $P$, the entry probability $p$ shifts and with it $h$; then
   $\lvert C_{h_{\tau'}}(\bar\pi)\rvert$ can exceed $\lvert C_{h_{\tau}}(\bar\pi)\rvert$ at the *same*
   $\bar\pi$, and Step 19 fails even though (18.1) holds. Repaired only by H10.
6. **$\Omega(\tau',T)=1$.** The pooled cell is emptied at the tighter threshold;
   $\bar\pi_{\mathrm{pr}}(\tau')$ and $M_P(\tau')$ are undefined, and by the card's own L1 convention
   the null-cell average is undefined rather than imputed. Legs 2 and 3 are vacuous. Excluded by H5.
7. **The all-engaging pooled class, $g=w$.** Then $\bar\pi_{\mathrm{pr}}=1$ at both thresholds and
   Leg 2 holds with equality; Leg 3 then delivers a strict decrease only through (br-iii). Not a
   failure of the claim, but a case where Leg 2 has no bite and the conclusion rests entirely on an
   unearned assumption.

---

## LABEL CLAIMED

**CONJECTURE** — unchanged, and this document does not move it.

Why: card §7 permits a label move only by an executed check or an independent re-derivation, and
the protocol recorded in card §6 requires **independent re-derivation PASS *plus* proof-read PASS**.
This is the re-derivation half only. Under H1–H11 the three legs are complete deductions with no gap
I can find, but two of the hypotheses they rest on — (br-iii) and (br-iv) — are unearned restrictions
supplied with the statement rather than card-maintained facts, and one further clause (H10) had to be
added. The honest reading is: **L4 is proved conditional on A(br) as amended by CHANGE 3**, and A(br)
itself is a conjecture whose satisfiability nobody has demonstrated. If A(br) is later derived inside
the model, L4's label should move with it; if A(br) is only ever asserted, L4's eventual PROVED must
carry A(br) visibly in its hypothesis list, in the same way C1 carries its named region.

---

## NUMERICAL CHECK REQUEST

**Formulas to compute** (fixed policies, one menu, one $T$ per run):

- $\Omega(x) = \Pr\big(a_{j(s)}=1,\ B_{j(s)}(s,H-T)\ge x\big)$ — the Step-5 form, computed directly
  from $\Lambda$, not by simulating filings.
- $g(x) = \Pr(a=1,\ D^{(x)}=0)$, $w(x) = 1-\Omega(x)$, $\bar\pi_{\mathrm{pr}}(x)=g(x)/w(x)$.
- $\rho(x) = \tfrac12 A_{1/2}(\kappa;x) + A_1(\kappa;x)$, $\bar\pi(x) = \bar\pi_{\mathrm{pr}}(x)/\rho(x)$.
- $\mathcal S_P(x) = \Delta_m\lvert A'_\kappa(x)\rvert\,\lvert C_h(\bar\pi(x))\rvert$, and separately
  the finite-difference $\lvert M_P(x;\kappa+\delta)-M_P(x;\kappa-\delta)\rvert/(2\delta)$ as a
  cross-check on (16.1).

**Grid.** $b_0 = 0.005$; $\tau \in \{0.02, 0.03, 0.04, 0.05, 0.10\}$ (every pair with
$b_0<\tau'<\tau$); $T \in \{5,10\}$ business days, $H = 60$; $\kappa \in \{0.05,0.10,\dots,0.95\}$;
menu = the pro-rata single-Voice menu; $\Delta_m$ at baseline calibration.

**Predicted signs — every grid node, no exceptions.**
$\Omega(\tau')-\Omega(\tau) \ge 0$; $\bar\pi_{\mathrm{pr}}(\tau')-\bar\pi_{\mathrm{pr}}(\tau) \le 0$;
$\mathcal S_P(\tau')-\mathcal S_P(\tau) \le 0$. Any node violating the third while satisfying the
first two isolates a failure of (br-iii), (br-iv) or H10 — print
$\big(\Delta\Omega,\ \Delta\bar\pi_{\mathrm{pr}},\ \lvert A'_\kappa\rvert\text{-ratio},\
\lvert C_h\rvert\text{-ratio},\ \rho\text{-ratio}\big)$ at every node so the offending factor is named.

**Predicted magnitudes.** Anchor on the card's $\Omega$ ladder ($0.037 / 0.129 / 0.286 / 0.50$) and a
starting pooled share $\bar\pi_{\mathrm{pr}}(\tau)=0.30$. Take one rung, $\Omega: 0.129 \to 0.286$,
so $n = 0.157$, $w = 0.871$, $g = 0.261$. Step 10 gives $w' = 0.714$, $g' = 0.104$, hence
$$\bar\pi_{\mathrm{pr}}: 0.300 \longrightarrow 0.146 \quad (\text{a } 51\% \text{ relative fall}).$$
Using L3's quadratic as a local calibration of $\lvert C_h\rvert$, the chord ratio is
$\approx (0.146/0.300)^2 = 0.237$, so with $\lvert A'_\kappa\rvert$ threshold-flat, predict
$$\mathcal S_P(\tau')/\mathcal S_P(\tau) \approx 0.24 \quad (\text{a } \approx 76\% \text{ fall}).$$

**Three invariants that must hold to machine precision** (each a direct executed test of a step):

- $\Omega(x) + g(x) = \Pr(a=1)$, the same constant at every $x$ — tests Step 2 and H6 jointly. With
  the numbers above: $0.129+0.261 = 0.286+0.104 = 0.390$, so also $\omega_a = 0.129/0.390 = 0.331$
  at the looser threshold and $0.286/0.390 = 0.733$ at the tighter one.
- $\max_{\text{grid}} \lvert\partial_\kappa\rho(x)\rvert \le 10^{-12}$ — tests Step 23's
  mean-preserving property, hence the internal consistency of (br-ii) with A($\tau$).
- $\lvert \Delta_m A'_\kappa(x)C_h(\bar\pi(x)) - \partial_\kappa M_P(x)\rvert \le 10^{-8}$ at every
  node — tests (16.1) and, through it, whether (br-ii)'s antecedent actually holds in the numerical
  model rather than only on paper.

---

## NOTATION DELTA

Symbols used above that are **not** in card §4:

| Symbol | Meaning | Status |
|---|---|---|
| $\bar\pi_{\mathrm{pr}}(x)$ | pooled **prior** engagement share $\Pr(a=1\mid D=0)$ at threshold $x$ | new; distinct from card §4.4's $\bar\pi$, which by the binding orchestrator ruling is the pooled posterior's **upper support point**. Step 22 shows $\bar\pi_{\mathrm{pr}} = \mathbb E[\Pi_\kappa]$, which sits strictly below $\bar\pi$ |
| $\tau'$ | the tighter of the two thresholds, $b_0<\tau'<\tau$ | new; from the amended statement |
| $\mathrm{A(br)}$, (br-i)–(br-iv), (br-ii′) | the bridging hypothesis handed to me with the amended statement; (br-ii′) added by CHANGE 3 | **not a card ID** — cited as a supplied hypothesis, never as card evidence |
| $\Lambda := B_{j(s)}(s,H-T)$ | the day-$(H-T)$ stake of the selected plan | proof-local |
| $A := a_{j(s)}$ | engagement of the selected plan | proof-local; card has $a_j$ but no name for its composition with the selection |
| $j(\cdot)$ | selection map from signal to plan induced by the fixed cutoff vector $k$ | proof-local; card has $k$ and $\mathcal J$ but no name for the map |
| $D^{(x)}$ | disclosure indicator read at threshold level $x$ | proof-local index on card's $D_j$ |
| $N$ | newly flagged set $\mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T)$ | proof-local |
| $w, w', g, g', n, \theta$ | pooled masses, engaging pooled masses, mass of $N$, mixture weight | proof-local scalars; chosen to avoid $W_\tau/W_T$, $P$, $\Gamma$ and $\Theta$ |
| $\Pi_\kappa$ | the pooled-cell engagement posterior $\pi(\mathcal I_H)$ viewed as a random variable | proof-local; the orchestrator ruling names $\mathbb E[\Pi_\kappa]$ |
| $\rho(x) := \tfrac12 A_{1/2}(\kappa;x)+A_1(\kappa;x)$ | pooled mean-to-endpoint ratio; $\kappa$-free by Step 23 | new, derived in Steps 23–24 |
| $\varphi$ | the weakly increasing map $\bar\pi_{\mathrm{pr}}\mapsto\bar\pi$ posited by (br-iv) | new; from the supplied hypothesis |
| $\alpha,\alpha',\gamma,\gamma'$ | placeholders in Step 21's product inequality | proof-local |

No card symbol was renumbered or re-keyed. $\kappa$ is noise-trading intensity throughout; upright
$T$ is the window; no bare $\lambda$, no $\psi$, no $\omega$ without its subscript.

---

## NOT CLAIMED

1. **No strictness.** All three legs are weak. Nothing here shows $\Omega$ strictly rises,
   $\bar\pi_{\mathrm{pr}}$ strictly falls, or $\mathcal S_P$ strictly falls; the equality cases in
   Steps 7, 13 and 21 are live.
2. **Nothing about the window margin $T$.** $T$ is held fixed. The card's §9 already disowns a global
   window-margin attenuation sign, and this document adds no window result.
3. **Nothing about $\mathcal S$.** The relation $\mathcal S=(1-\Omega)\mathcal S_P$ and T1's
   $W_T C_T \le 1$ condition are never invoked. Legs 1 and 3 move $\Omega$ and $\mathcal S_P$ in
   opposite directions; their product is T1's problem, not L4's.
4. **Nothing about the flagged cell.** L2, $M_F$, $\kappa$-invariance of the flagged objects, A7 and
   A7′ are not used anywhere above. Leg 1's inclusion is a statement about which histories are
   flagged, not about what happens inside the flagged cell.
5. **Nothing about equilibrium.** Everything is at fixed policies. No claim that a lower threshold
   raises or lowers $\Delta^{\mathrm{act}}$, entry, prices, surplus or welfare; no claim the sign
   survives cutoff re-optimisation; no claim about the GE-certified region's emptiness.
6. **No satisfiability claim for A(br).** I supply no menu, no distribution and no construction under
   which (br-i)–(br-iv) hold, and I have not shown they are mutually consistent with A($\tau$) beyond
   the one consistency check in Step 23. (br-iii) and (br-iv) are unearned.
7. **No sign for $\partial_\kappa M_P$.** Only its magnitude is compared. The maintained orientation
   $C_h \le 0$ is never used, so nothing here says whether the pooled cell's premium rises or falls
   with liquidity.
8. **No identification of $\bar\pi$ with $\bar\pi_{\mathrm{pr}}$.** They are different objects; Step
   24 gives the exact relation under the ternary representation and nothing stronger.
9. **No proof-read.** This is one half of the two-part protocol. The label stays CONJECTURE.
