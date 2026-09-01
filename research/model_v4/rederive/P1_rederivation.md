# P1 — independent re-derivation (ticket 27)

**Re-deriver:** Opus, statements-only lane. Inputs seen: `MODEL_CARD.md` (version stamp
2026-08-21 · commit `a175202`+), and the amended P1 statement plus h.11 and h.12 as handed over.
`proofs/` and `threads/` were **not** opened. `draft_v2.tex` was not used and nothing is cited
from it.

**VERDICT: PROVED-WITH-CHANGES.**

Changes, in one place (each is argued at the step where it bites):

| # | Change | Kind | Where |
|---|---|---|---|
| C1 | **A2's boundedness clause is inconsistent with A7′ + Gaussian $v$** and is replaced by A2′ (local boundedness + one integrability condition). | amended hypothesis | Steps 3, 12 |
| C2 | **The blockholder's objective is nowhere written in the card.** It is added as h.13, and the proof is run off two structural properties of it, not off its algebra. | added hypothesis | Steps 4, 22 |
| C3 | **A5 can be dropped**: its existence, uniqueness and continuity clauses are *proved* at every control node from A1, h.12 and §4.3's entry rule. This is the only place h.12 does work. | dropped hypothesis (h.12 buys it) | Lemma 2, Steps 9–13 |
| C4 | **A6's continuity clause is doing load-bearing, non-obvious work.** It is not implied by A3 plus continuity of payoffs in $k$. It is retained as a hypothesis; a sufficient primitive condition and a repair route are given. | retained, flagged | Steps 24, 27, Remark R1 |
| C5 | §2's sequence is read as **"the flag terminates the pooled round"**. Without this reading $Q^F_j = b^*_j - B^F_j$ is not the whole residual and Step 18 fails. | added reading | Step 2 |
| C6 | **A8 is a condition on the fixed point found, not a primitive.** P1's second sentence is therefore conditional on the fixed point exhibited satisfying it; existence of a fixed point *at which* A8 holds is not claimed. | amended reading | Steps 34–36 |
| C7 | **h.12 is idle under A5 as written.** If A5 is kept as a hypothesis, h.12 is used at no step of the existence proof. It earns its keep only in the C3 trade. | finding on a given hypothesis | Lemma 2 |
| C8 | h.11 is **load-bearing twice** and is not cosmetic: it makes the flagged round a finite choice among tremble-reachable actions (Step 20) and it makes date-0 optimality *imply* flagged-round sequential optimality (Step 19). | finding on a given hypothesis | Steps 15–20 |

---

## CLAIM

Fix the parameter vector $\vartheta$. Under A1, A2′, A3, A4, A6, A7 in its on-path injective form
via the §4.2 A7′ row, the card's §2 no-feedback timing read with C5, D1's ledger statement, and
h.11, h.12, h.13, the two-round model has **at least one** cutoff perfect Bayesian equilibrium over
complete contingent plans, in the sense of the card's §3 components (i)–(vi). A5 is not needed: its
content is derived (Lemma 2). At any such equilibrium at which A8 holds, both the flagged cell
$\mathcal C_F$ and the pooled cell $\mathcal C_P$ carry strictly positive probability, so both are on
path. Uniqueness is not claimed.

---

## HYPOTHESES

Numbered H1–H13; every one is used, and the step that uses it is named.

- **H1 = A1 (independent primitives).** $v,\varepsilon,\xi$ and all $z_d$ mutually independent, all
  variances strictly positive. Used: Steps 9, 11, 17, 30.
- **H2 = A2′ (finite model, amended boundedness).** The plan menu $\mathcal J$, the image of
  $\Gamma$, the noise support and the calendar $\{0,\dots,H\}$ are finite. **Amended clause
  (C1):** prices and payoffs are *locally* bounded in $(s,\vartheta)$ and
  $\mathbb E\big[\max_{j\in\mathcal J}\lvert U(j,s;k)\rvert\big] < \infty$ for every $k \in \Theta$,
  in place of the card's flat "bounded". Used: Steps 6, 12, 21, 22.
- **H3 = A3 (ordered plans, single crossing).** At **every** belief/price system, adjacent-plan
  payoff differences cross zero at most once in $s$, and the preferred plan is weakly increasing in
  $s$. The universal quantifier over belief/price systems is essential and is used as written. Used:
  Steps 23, 25.
- **H4 = A4 (legal-clock discipline).** $c$ is the first date the path reaches $\tau$; the filing
  lands exactly at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in the
  core. Used: Steps 15, 16, 34.
- **H5 = A6 (compact outer self-map).** All best-response cutoffs lie in a common compact ordered
  polytope $\Theta$; $\mathcal T$ is continuous and maps $\Theta$ into itself. Used: Steps 24, 26,
  27; flagged at Remark R1.
- **H6 = A7 on-path injective form via A7′.** On the flagged set the composed terminal target
  $s \mapsto b^*_{j_k(s)}(s)$ is strictly increasing, **for every cutoff vector $k \in \Theta$**.
  Used: Steps 10, 11, 17, 20, 30.
- **H7 = A8 (interior crossing).** $0 < \Omega < 1$, imposed on the equilibrium exhibited (C6).
  Used: Steps 34–36 only.
- **H8 = §2 no-feedback timing, read with C5.** $B_j(s,d)$, $q_{jd}(s)$, $Q^F_j$ are functions of
  $(j,s,d)$ and $(j,s,\tau,T)$ alone; realised order flow and prices feed back into nothing; and the
  landing of the flag terminates the pooled round, the flagged round and then the bidder following
  it. Used: Steps 2, 6, 17, 18.
- **H9 = D1's ledger statement.** $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is measurable and maps every
  control-node history into exactly one of $\mathcal C_F,\mathcal C_P$; for every Voice plan
  $f_j \le H \iff B_j(s,H-T)\ge\tau$. Used: Steps 5, 10, 34, 35.
- **H10 = h.11 (flagged closure, definitional reading).** The round-2 action set at a flagged node
  reached by $(j,s)$ is $\{Q^F_{j'}(s) : j' \in \mathcal J$ shares $j$'s pooled path up to $f_j$ and
  $a_{j'} = a_j\}$ — the plan-generated set, not $[0,\bar b - B^F]$. Used: Steps 15, 16, 18, 19, 20.
- **H11 = h.12 (nonnegative premia).** $m_0 \ge 0$, hence
  $\bar m(\mathcal I) := m_0 + \pi(\mathcal I)\Delta_m \ge 0$. Used: Lemma 2 (Steps 9, 13) **only**.
- **H12 = h.13 (blockholder objective; added, C2).** The blockholder's date-0 payoff at signal $s$
  from plan $j$, in the belief/price system indexed by $k$, is
  $$U(j,s;k) \;=\; \mathbb E\Big[\, b^*_j(s)\,Y \;-\; \textstyle\sum_{d\le \iota_j(s)} \big(B_j(s,d)-B_j(s,d-1)\big)P^P_d \;-\; \mathbf 1\{D_j(s)=1\}\,Q^F_j(s)\,P^F \;-\; a_j\,C_j(s) \,\Big|\, s\Big],$$
  where $\iota_j(s) = f_j(s)$ when $D_j(s)=1$ and $H$ otherwise, and $C_j(s)\ge0$ is §4.4's
  engagement cost. The proof uses only two properties of this object:
  **(P-i) plan-locality** — $U(j,s;k)$ depends on $j$ only through the executed stake path, the
  prices paid on it, the terminal stake, the engagement flag and the cost; and
  **(P-ii) integrability** — H2's amended clause. Any objective with (P-i) and (P-ii) carries the
  proof. Used: Steps 4, 18, 19, 21, 22.
- **H13 = §4.3's entry rule and payoff.** $\mathsf B = \mathbf 1\{\xi \ge P + K + m_0 + \pi\Delta_m
  - \bar S\}$, so $p(\mathcal I) = 1-\Phi\big((P+K+\bar m-\bar S)/\sigma_\xi\big)$, and
  $Y = (1-\mathsf B)(v+a\Delta_V) + \mathsf B(P+m_0+a\Delta_m)$. Used: Lemma 2, Steps 9, 11, 17.

---

## PROOF

### Part I — objects, and the two readings the card leaves open

**Step 1 (the unknown).** By §3 an equilibrium is a six-tuple: a weakly ordered cutoff vector
$k=(k_1\le\dots\le k_{J-1})\in\Theta$ with its induced plan rule; sequentially optimal pooled and
flagged components; on-path Bayes beliefs; pooled and flagged prices at their fixed points; the
bidder-entry rule; and off-path beliefs that are limits of full-support perturbations. The proof
constructs all six and verifies each.

Write $j_k(s) := 1 + \#\{i \in \{1,\dots,J-1\} : k_i \le s\}$ for the plan rule generated by $k$.
Because $k$ is weakly ordered, $j_k$ is a nondecreasing step function from $\mathbb R$ onto a subset
of $\mathcal J$, and a plan whose cutoff interval is empty is simply unplayed — §3's weak
inequalities permit exactly this.

**Step 2 (reading C5: the flag terminates the pooled round).** §2's sequence is written "pooled round
$\to$ flag or no flag $\to$ flagged round if applicable $\to$ bidder decision", and §4.2 sets
$Q^F_j = b^*_j(s) - B^F_j$, the entire residual between the stake at filing and the terminal target.
These two are consistent only if no pooled trading occurs after $f_j$ on a flagged history: otherwise
the residual would be split between a post-filing pooled leg and $Q^F$, and $Q^F_j = b^*_j - B^F_j$
would overstate the flagged order. I therefore read §2 as: on a history with $D_j(s)=1$, the pooled
round runs over $d = 0,\dots,f_j$ and stops, the flagged round executes $Q^F_j$, and the control node
follows. On a history with $D_j(s)=0$ the pooled round runs over $d=0,\dots,H$ and the control node
follows it. This is H8's second clause. Everything below uses it at Steps 6, 17 and 18.

**Step 3 (reading C1: A2's boundedness cannot be taken literally).** H6 (A7′) requires
$s\mapsto b^*_{j_k(s)}(s)$ to be **strictly** increasing on the flagged set, and $s$ ranges over an
unbounded set because $v$ and $\varepsilon$ are Gaussian (H1, §4.1). Lemma 2 below shows the
control-node price at a flagged tuple equals $\bar y + \frac{p}{1-p}\bar m$ with
$\bar y = \mu_v + \beta(s-\mu_v) + \Delta_V$, which is unbounded in $s$. So "prices and payoffs
bounded" in A2, read as a uniform bound over the flagged continuum, contradicts A7′ together with
Gaussian signals. The clause is used in this proof only to make expectations finite and to make the
outer payoff differences finite, and for that the amended H2 suffices. $\mathbb E[\max_j|U(j,s;k)|]
<\infty$ holds under H12 because $Y$ is affine in $v$ with coefficients bounded by
$\max(1,|\Delta_V|,|\Delta_m|,|m_0|)$, $b^*_j \in [0,\bar b]$, prices are affine-in-$s$ plus a term
bounded by $\bar m \cdot \sup_P \frac{p}{1-p}$ on any compact price range, and $v$ has all moments.
This is C1.

**Step 4 (reading C2: the objective).** The card names $Y$ (terminal shareholder payoff) and
$C_j(s)$ (engagement cost, §4.4's overloading note) but never writes what the blockholder maximises.
An existence theorem cannot be stated without it, so H12 supplies it. The proof never differentiates
$U$ and never uses its algebra; it uses (P-i) at Steps 18–19 and (P-ii) at Steps 21–22. This is C2.

**Step 5 (the flagged set is Borel).** By H9, $D$ is measurable, and by H8 $D_j(s)$ is a function of
$(j,s,\tau,T)$ alone. Hence for each $k \in \Theta$ the set
$\mathcal E_k := \{s \in \mathbb R : D_{j_k(s)}(s) = 1\}$ is Borel: it is the finite union over
$j\in\mathcal J$ of $j_k^{-1}(j) \cap \{s : D_j(s)=1\}$, each factor Borel — the first because $j_k$
is a step function with finitely many pieces (Step 1, H2), the second by H9. Every construction below
that ranges over "the flagged set" ranges over $\mathcal E_k$.

### Part II — inner pricing at fixed cutoffs

Fix $k \in \Theta$ for the whole of Part II.

**Step 6 (the pooled histories are a finite set).** By H2 the image of $\Gamma$ is finite and the
noise support $\{-\bar z,0,+\bar z\}$ is finite, so $X_d = q_{jd}+z_d$ takes finitely many values; by
H2 the calendar $\{0,\dots,H\}$ is finite; by §4.3 the pooled public history $\mathcal H^P_d$ is
$(X_0,\dots,X_d;$ flag landed by $d)$, so the number of pooled histories is at most
$(3\lvert\mathrm{im}\,\Gamma\rvert)^{H+1}\cdot 2^{H+1}$, a finite number. By H8 the marks
$q_{jd}(s)$ do not depend on realised flow or prices, so this enumeration does not depend on the
price system being constructed. This answers the first half of task (a): the pooled side is finite
and no measurability question arises there.

**Step 7 (which pooled histories carry mass).** Under the cutoff rule $j_k$, a pooled history
$\eta$ has $\mathbb P_k(\eta) > 0$ exactly when there is a plan $j$ in the range of $j_k$ and a set
of signals of positive Lebesgue-times-Gaussian mass in $j_k^{-1}(j)$ whose marks
$(q_{j0},\dots,q_{jd})$ are compatible with $(X_0,\dots,X_d)$ under some noise string of positive
probability. Because the noise marks $\pm\bar z$ carry probability $\kappa/2$ each and $0$ carries
$1-\kappa$, at $\kappa \in (0,1)$ every noise string has positive probability; at $\kappa \in \{0,1\}$
some do not. Histories with $\mathbb P_k(\eta)=0$ are handled at Step 31, not here.

**Step 8 (only control nodes carry a genuine pricing fixed point).** By §4.3 a price is
$P(\mathcal I) = \mathbb E[Y \mid \mathcal I]$, and $Y$ contains the control-node price $P$ inside
$\mathsf B(P + m_0 + a\Delta_m)$ (H13). At a **control node** — a flagged tuple, or a pooled history
at $d=H$ with no flag — the price therefore appears on both sides and the equation is a genuine
fixed point in a scalar. At a pooled history with $d < H$ and no flag landed, the control node is a
strictly later event, and by the tower property
$$P^P_d \;=\; \mathbb E[Y \mid \mathcal H^P_d] \;=\; \mathbb E\big[\,\mathbb E[Y \mid \mathcal I_H]\,\big\vert\,\mathcal H^P_d\big] \;=\; \mathbb E\big[P(\mathcal I_H)\,\big\vert\,\mathcal H^P_d\big],$$
which is an average of already-determined numbers and contains no self-reference. So the inner system
is: solve the control nodes, then run one backward average. §4.3's convention $P^P_{-1}:=\mathbb E[Y]$
is the $d=-1$ instance of the same average and is used whenever $c=0$.

**Lemma 2 (control-node price: existence, uniqueness, continuity).** *Let $\mathcal I$ be a control
node with belief $\mu$ over $(v,a)$, and write $\bar y := \mathbb E_\mu[v] + \pi(\mathcal I)\Delta_V$
and $\bar m := m_0 + \pi(\mathcal I)\Delta_m$. Under H1, H11 and H13, the equation
$P = \mathbb E[Y\mid\mathcal I]$ has exactly one solution $P^\ast(\bar y,\bar m)$, and
$(\bar y,\bar m)\mapsto P^\ast$ is continuous on $\mathbb R\times[0,\infty)$.*

**Step 9 (reduction to one scalar equation).** By H13 the entry indicator $\mathsf B$ is a function
of $\xi$, $P$ and $\pi(\mathcal I)$ only, and by H1 $\xi$ is independent of $(v,\varepsilon)$ and
hence of $(v,a)$ given $\mathcal I$ — $a$ is a function of the selected plan, hence of $s$, hence of
$(v,\varepsilon)$. Therefore
$$\mathbb E[Y\mid\mathcal I] = (1-p)\big(\mathbb E_\mu[v]+\pi\Delta_V\big) + p\big(P+m_0\big) + p\,\pi\Delta_m = (1-p)\bar y + p\,(P+\bar m),$$
with $p = p(P) = 1-\Phi\big((P+K+\bar m-\bar S)/\sigma_\xi\big) \in (0,1)$ for every finite $P$,
strictly because $\sigma_\xi > 0$ (H1) and $\Phi$ has full support. Setting $P = \mathbb E[Y\mid
\mathcal I]$ and subtracting $pP$ from both sides gives $P(1-p(P)) = (1-p(P))\bar y + p(P)\bar m$, and
dividing by $1-p(P) > 0$,
$$P \;=\; \Psi_{\mathcal I}(P) \;:=\; \bar y + \frac{p(P)}{1-p(P)}\,\bar m. \tag{$\ast$}$$

**Step 10 (the two belief summaries are finite at every control node).** At a pooled control node,
$\mu$ is a finite mixture over the plans in the range of $j_k$ of the conditional law of $v$ given
$s$ lies in a cutoff interval and the marks match; each component is a Gaussian conditional law with
finite mean, and the mixture is over at most $J$ components (H2), so $\mathbb E_\mu[v]$ is finite. At
a flagged tuple, Step 11 shows $\mu$ is a point mass at a single $s$, so
$\mathbb E_\mu[v] = \mu_v + \beta(s-\mu_v)$, finite. $\pi(\mathcal I)\in[0,1]$ by §4.3, so $\bar m$ is
finite, and $\bar m \ge m_0 \ge 0$ by H11. That $\pi = 1$ on $\mathcal C_F$ is §4.3's row; combined
with H9 it gives $\bar m = m_1$ there.

**Step 11 (flagged beliefs are point masses, and the inverse is elementary).** Fix $k$ and define on
$\mathcal E_k$ (Step 5) the flagged-tuple map
$$\Lambda_k(s) \;:=\; \big(B^F_{j_k(s)}(s),\; Q^F_{j_k(s)}(s),\; 1\big), \qquad
\Sigma_k(s) \;:=\; B^F_{j_k(s)}(s) + Q^F_{j_k(s)}(s) \;=\; b^*_{j_k(s)}(s),$$
the last equality by §4.2's definition $Q^F_j = b^*_j - B^F_j$. By H6 (A7′), $\Sigma_k$ is strictly
increasing on $\mathcal E_k$, **for this $k$ and for every other $k\in\Theta$**. A strictly
increasing real function is injective and its inverse on its image is increasing, hence Borel; so
$\sigma_k := \Sigma_k^{-1}$ is a Borel map from $\Sigma_k(\mathcal E_k)$ onto $\mathcal E_k$, and
$$s \;=\; \sigma_k\big(B^F + Q^F\big) \qquad\text{for every } \Lambda_k(s) = (B^F,Q^F,1). \tag{$\dagger$}$$
No appeal to a descriptive-set-theoretic inverse theorem is needed: monotonicity supplies the
inverse. Consequently the conditional law of $s$ given the flagged tuple is the point mass
$\delta_{\sigma_k(B^F+Q^F)}$. That this is a legitimate version of the disintegration is the content
of Step 12. By H1, conditioning further on $(v,\varepsilon)$-independent objects changes nothing, and
by H9 $a = 1$ on $\mathcal C_F$, so $\pi = 1$ there.

**Step 12 (why the point mass is a version, not a choice).** The flagged tuple lives in a continuum,
so each tuple is a null event and $\mathbb E[\cdot\mid\Lambda_k]$ is defined only up to a null set;
task (a) asks how prices are then defined across that continuum. The answer: for every bounded Borel
$\phi$ and every Borel $C$ in tuple space,
$$\mathbb E\big[\phi(s)\mathbf 1_C(\Lambda_k(s))\mathbf 1_{\mathcal E_k}(s)\big]
= \mathbb E\big[\phi(\sigma_k(\Sigma_k(s)))\mathbf 1_C(\Lambda_k(s))\mathbf 1_{\mathcal E_k}(s)\big],$$
because $\sigma_k(\Sigma_k(s)) = s$ pointwise on $\mathcal E_k$ by ($\dagger$). The right-hand side is
$\int_C \big(\int \phi\, d\delta_{\sigma_k(\cdot)}\big)\,d(\mathbb P\circ\Lambda_k^{-1})$. So
$\phi \mapsto \phi(\sigma_k(B^F+Q^F))$ satisfies the defining identity of a regular conditional
expectation **at every tuple in the image**, not merely almost everywhere. This gives an
everywhere-defined version with no arbitrary selection, and it agrees with any other version off a
null set. Integrability of $\phi(s) = v$ is H2's amended clause (Step 3).

**Step 13 (proof of Lemma 2).** $\Psi_{\mathcal I}$ in ($\ast$) is continuous in $P$ because $\Phi$
is continuous and $p<1$ strictly (Step 9). $P \mapsto p(P)$ is strictly decreasing, so
$P\mapsto p/(1-p)$ is strictly decreasing, so — using $\bar m \ge 0$ from **H11** — the map
$\Psi_{\mathcal I}$ is weakly decreasing in $P$. Hence $\zeta(P) := P - \Psi_{\mathcal I}(P)$ is
strictly increasing and continuous. Limits: as $P\to+\infty$, $p(P)\to0$ so
$\Psi_{\mathcal I}(P)\to\bar y$ and $\zeta(P)\to+\infty$; as $P\to-\infty$, $p(P)\to1$ so
$p/(1-p)\to+\infty$, giving $\Psi_{\mathcal I}(P)\to+\infty$ when $\bar m>0$ and
$\Psi_{\mathcal I}(P)=\bar y$ when $\bar m=0$, and in both cases $\zeta(P)\to-\infty$. A continuous
strictly increasing function with these limits has exactly one zero, which is the unique solution of
($\ast$). For continuity in $(\bar y,\bar m)$: $\zeta$ is jointly continuous in $(P,\bar y,\bar m)$
and strictly increasing in $P$, so for any $\varepsilon_0>0$ we have
$\zeta(P^\ast-\varepsilon_0;\bar y,\bar m)<0<\zeta(P^\ast+\varepsilon_0;\bar y,\bar m)$, and both
strict inequalities persist under a small perturbation of $(\bar y,\bar m)$, placing the perturbed
root inside $(P^\ast-\varepsilon_0,P^\ast+\varepsilon_0)$. $\square$

**Step 14 (the inner system is solved, and is Borel across the flagged continuum).** Combining:
control-node prices exist and are unique (Lemma 2); at flagged tuples the belief summary is
$\bar y(\phi) = \mu_v + \beta(\sigma_k(B^F+Q^F)-\mu_v) + \Delta_V$ and $\bar m = m_1$, a Borel
function of the tuple $\phi$ by Step 11; the root map $(\bar y,\bar m)\mapsto P^\ast$ is continuous
by Lemma 2. A continuous map composed with a Borel map is Borel, so
$$P^F(\phi) \;=\; P^\ast\big(\bar y(\phi),\, m_1\big)$$
is an everywhere-defined Borel function on the flagged continuum. Pooled control-node prices are
finitely many numbers (Step 6), and pooled prices at $d<H$ follow by the single backward average of
Step 8, whose integrand is Borel and integrable by H2's amended clause. **This discharges task (a)
in full, and it discharges A5 (change C3): existence, uniqueness and continuity in beliefs at every
node were proved, not assumed.** The one hypothesis that made this possible is **H11 = h.12**: it is
what makes $\Psi_{\mathcal I}$ weakly decreasing at Step 13. Under A5 as written, h.12 is used
nowhere (change C7).

### Part III — sequential optimality of the flagged-round component

This is task (b), and it is where h.11 is tested. Fix $k \in \Theta$ and the inner system of Part II.

**Step 15 (h.11's set is an equivalence class, so the flagged node has a well-posed finite menu).**
Fix a flagged $(j,s)$, so $a_j=1$, $c_j(s)<\infty$ and $f_j(s)=c_j(s)+T\le H$ (H4, H9). Define
$$\mathcal K_s(j) \;:=\; \{\,j'\in\mathcal J \;:\; B_{j'}(s,d)=B_j(s,d)\ \ \forall d\le f_j(s),\ \ a_{j'}=a_j\,\},$$
which is exactly the index set in h.11 (H10). I check that $\sim$ defined by "$j'\in\mathcal K_s(j)$"
is an equivalence relation on the plans flagged at $s$. Reflexive: immediate from the definition.
Suppose $j'\in\mathcal K_s(j)$. Because $T\ge 1$ (§4.2), $c_j(s) = f_j(s)-T \le f_j(s)$, so the
common initial segment $d\le f_j(s)$ contains the crossing date of $j$; and since
$c_{j'}(s)=\inf\{d:B_{j'}(s,d)\ge\tau\}$ is determined by the path on $\{d \le f_j(s)\}$ whenever that
infimum is attained there, $c_{j'}(s)=c_j(s)$ and therefore $f_{j'}(s)=f_j(s)$ (H4 fixes the filing
lag at exactly $T$). So "agree up to $f_j$" and "agree up to $f_{j'}$" are the same requirement:
symmetry and transitivity hold. Hence the flagged node's menu is the class $\mathcal K_s(j)$, and by
H2 ($J<\infty$) it is a **finite, nonempty** set containing $j$ itself. The corresponding action set
$\{Q^F_{j'}(s):j'\in\mathcal K_s(j)\}$ is therefore a finite subset of $[0,\bar b - B^F]$, and each
of its elements is nonnegative because $a_{j'}=a_j=1$ makes $j'$ a Voice plan, for which
$Q^F\ge0$ (§4.2).

**Step 16 (all members of a class share the entire pre-filing public record).** For
$j'\in\mathcal K_s(j)$: $B_{j'}(s,\cdot)=B_j(s,\cdot)$ on $\{d\le f_j\}$, so the increments and hence
the marks $q_{j'd}(s)=\Gamma(B_{j'}(s,d)-B_{j'}(s,d-1))$ coincide with $q_{jd}(s)$ for all
$d\le f_j$ (§4.2); by H8 the marks do not depend on realised flow, so for each realisation
$z_{0:f_j}$ the order flow $X_d=q_{\cdot d}+z_d$ coincides too, hence the pooled histories coincide
**pathwise**, hence by Step 8 the pooled prices $P^P_d$, $d\le f_j$, coincide pathwise. Also
$B^F_{j'}(s)=B_{j'}(s,f_{j'})=B_j(s,f_j)=B^F_j(s)$ and $D_{j'}(s)=D_j(s)=1$. By Step 2 (H8) there is
no pooled trading after $f_j$ on a flagged history. Therefore **the only object on which two members
of a class differ is the flagged order $Q^F$, equivalently the terminal stake $b^*$**.

**Step 17 (the flagged continuation payoff does not depend on the noise realisation).** Consider the
flagged node reached by $(j,s)$ after noise $z_{0:f_j}$. By §4.3 the flagged price is $P(F,Q^F)$, a
function of the tuple; I check that enlarging the control-node information set on a flagged history
by $z_{0:f_j}$ would change nothing, so this convention is without loss here. First, $\pi = 1$ on
$\mathcal C_F$ (§4.3, H9), independent of $z$. Second, by Step 11 the tuple already pins $s$, and by
H1 $z$ is independent of $(v,\varepsilon,\xi)$, so
$\mathbb E[v\mid \text{tuple},z_{0:f_j}] = \mathbb E[v\mid s] = \mu_v+\beta(s-\mu_v)$ and the belief
summary $(\bar y,\bar m)$ is unchanged; by Lemma 2's uniqueness the price is therefore the same
number. Third, by H13 the bidder's entry threshold is a function of $(P,\pi,\xi)$ only, so entry is
unchanged. Hence the flagged-round and control-node objects at a flagged node are functions of
$(j',s)$ alone, and I write the flagged continuation payoff as $U^F(j',s)$.

**Step 18 (the flagged comparison equals the date-0 comparison, pathwise).** Let $j'\in\mathcal
K_s(j)$ and let $s$ be flagged. Write $\mathfrak d(s;j,j') := U(j,s;k)-U(j',s;k)$ for the date-0
difference under H12. By (P-i) of H12, $U$ depends on the plan only through the executed path, the
prices paid on it, the terminal stake, the engagement flag and the cost. By Step 16 the executed
pooled path, the pooled prices paid on it, the flag and (since $a_{j'}=a_j$) the engagement
indicator coincide for $j$ and $j'$ at this $s$, realisation by realisation of $z_{0:f_j}$; and by
H8 the flag $D_j(s)$ is deterministic in $(j,s)$, so no expectation over $z$ mixes a flagged with a
pooled branch. The pooled leg of $U$ therefore cancels term by term inside the expectation, leaving
$$\mathfrak d(s;j,j') \;=\; U^F(j,s) - U^F(j',s) \;+\; \big(a_jC_j(s)-a_{j'}C_{j'}(s)\big)\cdot(-1),$$
where the cost term is the one place a class-mate can still differ. Two readings are available: if
the cost is attached to engagement rather than to the plan, $C_j=C_{j'}$ whenever $a_j=a_{j'}$ and
the term vanishes; if it is plan-specific, fold it into $U^F$, which is legitimate because by Step 16
the cost is the only remaining plan-dependent object besides $Q^F$ and it is incurred at the same
node. Either way
$$\boxed{\ \mathfrak d(s;j,j') \;=\; U^F(j,s)-U^F(j',s)\ }\tag{$\ddagger$}$$
and by Step 17 both sides are free of $z$, so the identity holds at **every** flagged node, not only
in expectation.

**Step 19 (sequential optimality of the flagged component, given date-0 optimality).** Suppose $k$ is
such that the plan rule $j_k$ is a date-0 best response, that is $U(j_k(s),s;k)\ge U(j',s;k)$ for
every $j'\in\mathcal J$ and every $s$ (this is what Step 25 delivers at a fixed point). Take any
flagged $s$ and any available round-2 action, which by H10 and Step 15 is $Q^F_{j'}(s)$ for some
$j'\in\mathcal K_s(j_k(s))$. Then $\mathfrak d(s;j_k(s),j')\ge 0$ by date-0 optimality, so by
($\ddagger$) $U^F(j_k(s),s)\ge U^F(j',s)$: the prescribed flagged order is optimal in the available
set. **This is h.11 earning its keep.** The closure condition in h.11 — same pooled path up to $f_j$,
same $a$ — is exactly the condition under which every available round-2 action is the round-2
component of a plan that was available at date 0 *and* differs from the incumbent in nothing else.
Drop it and ($\ddagger$) has no left-hand side: a deviation $Q'$ outside the plan-generated set
corresponds to no element of $\mathcal J$, so date-0 optimality says nothing about it, and the
flagged round becomes a signalling problem with a continuum of messages whose existence question is
separate from, and not implied by, the outer fixed point. See WHERE IT FAILS, case 1.

**Step 20 (h.11's set is exactly the perturbation-reachable set — the second place it earns its
keep).** Consider the full-support perturbations of §3(vi), built as follows: index them by a
tremble size $t\in(0,1)$ and a full-support kernel $\rho$ on $\mathcal J$, and let type $s$ play plan
$j$ with probability $(1-t)\mathbf 1\{j=j_k(s)\}+t\rho(j)$. Under such a perturbation type $s$ plays
$j'$ with positive probability for **every** $j'\in\mathcal J$, and if $j'\in\mathcal K_s(j_k(s))$
then by Step 16 that play produces exactly the tuple
$\big(B^F_{j_k(s)}(s),\,Q^F_{j'}(s),\,1\big)$ — the same $B^F$, the deviant $Q^F$. So every action in
h.11's set is reached with positive probability under every full-support perturbation, and its belief
is a Bayes belief in the perturbed system, whose limit as $t\downarrow0$ exists (Step 32). No belief
at a flagged node is ever an arbitrary selection. With the full interval $[0,\bar b-B^F]$ as the
action set this property is lost at once: a $Q'$ that no plan generates is unreached under **every**
plan-perturbation, so §3(vi) has to be re-run over trembles in $Q'$ itself, which is a different
perturbation class from the one the card names.

### Part IV — the outer best-response cutoff map

**Step 21 ($U$ is well defined for every plan, on and off the path).** By Part II the belief/price
system indexed by $k$ assigns a price to every pooled history (Steps 6–8, 31) and to every flagged
tuple (Step 14), including tuples generated by plans that no type plays under $j_k$. By H12's
(P-ii)/H2 the expectation defining $U(j,s;k)$ is finite for every $j\in\mathcal J$ and a.e. $s$.
Hence the full payoff array $\{U(j,\cdot;k)\}_{j\in\mathcal J}$ is defined, which is what a
best-response map needs.

**Step 22 (the best plan is well defined).** $\mathcal J$ is finite (H2), so
$\arg\max_{j\in\mathcal J}U(j,s;k)$ is nonempty for a.e. $s$, and
$$\mathfrak b(s;k) \;:=\; \min\arg\max_{j\in\mathcal J}U(j,s;k)$$
is a single-valued selection. Ties are therefore broken by a fixed rule rather than left open; §3's
weak inequalities permit exactly this, and the tie set is where a collapsed region can appear.

**Step 23 (A3 makes $\mathfrak b$ a nondecreasing step function).** H3's second clause states that at
every belief/price system the preferred plan is weakly increasing in $s$. Applied to the system
indexed by $k$ — H3 is quantified over *all* belief/price systems, which is what lets me apply it at
a candidate $k$ that is not yet an equilibrium — this says the argmax correspondence is
nondecreasing in the strong set order in $s$, and the minimum selection of a nondecreasing
correspondence is a nondecreasing function. So $\mathfrak b(\cdot;k):\mathbb R\to\mathcal J$ is
nondecreasing, with finitely many values (H2), hence a nondecreasing step function. H3's first clause
(adjacent differences cross at most once) is the primitive that delivers the second clause; I use the
second clause directly.

**Step 24 (definition of $\mathcal T$, and that it is weakly ordered).** Write $\Theta$'s bounds as
$\underline\theta\le\bar\theta$, so $\Theta=\{k\in\mathbb R^{J-1}:\underline\theta\le k_1\le\dots\le
k_{J-1}\le\bar\theta\}$ — nonempty, compact and convex (§4.5). For $j=1,\dots,J-1$ set
$$\mathcal T_j(k) \;:=\; \min\Big\{\bar\theta,\ \max\big\{\underline\theta,\ \inf\{s\in\mathbb R:\mathfrak b(s;k)\ge j+1\}\big\}\Big\},$$
with $\inf\emptyset := +\infty$. Since $\mathfrak b(\cdot;k)$ is nondecreasing (Step 23), the sets
$\{s:\mathfrak b(s;k)\ge j+1\}$ are nested and decreasing in $j$, so their infima are nondecreasing
in $j$, and clipping to $[\underline\theta,\bar\theta]$ preserves the order. Hence
$\mathcal T_1(k)\le\dots\le\mathcal T_{J-1}(k)$ and $\mathcal T(k)\in\Theta$: the map is a self-map
of $\Theta$ by construction, and H5's self-map clause additionally records that the clipping is not
binding, that is that the unclipped best-response cutoffs already lie in $\Theta$. This is task (c).
Continuity of $\mathcal T$ is **H5's remaining clause**; it is not derived here and Remark R1 says
what it hides.

**Step 25 (a fixed point of $\mathcal T$ is a date-0 best response).** Let $k=\mathcal T(k)$. Fix $s$
with $k_{i-1}<s<k_i$ for the relevant neighbouring cutoffs, so that $j_k(s)=i$ (Step 1). By the
definition in Step 24 and $k_i=\mathcal T_i(k)$: $s<k_i$ places $s$ outside
$\{s':\mathfrak b(s';k)\ge i+1\}$, because that set is an up-set with infimum $k_i$; hence
$\mathfrak b(s;k)\le i$. And $s>k_{i-1}=\mathcal T_{i-1}(k)$ places $s$ inside
$\{s':\mathfrak b(s';k)\ge i\}$; hence $\mathfrak b(s;k)\ge i$. So $\mathfrak b(s;k)=i=j_k(s)$: the
cutoff rule generated by $k$ selects a payoff-maximising plan at every $s$ outside the finite set
$\{k_1,\dots,k_{J-1}\}$, which is Lebesgue-null and hence null under the Gaussian law of $s$ (H1).
At the cutoffs themselves the types are indifferent between the adjacent plans by continuity of the
crossing, and §3's weak inequalities permit either assignment. Date-0 optimality holds.

### Part V — the fixed point

**Step 26 (Brouwer).** $\Theta$ is nonempty, compact and convex (§4.5, Step 24). $\mathcal T$ maps
$\Theta$ into $\Theta$ (Step 24) and is continuous (H5). Brouwer's fixed-point theorem therefore
yields $k^\ast\in\Theta$ with $k^\ast=\mathcal T(k^\ast)$. This is task (d), and it is §3's own
prescription ("Existence is Brouwer on the compact ordered polytope $\Theta$").

**Step 27 (what H5 is carrying).** Two clauses of H5 are used and neither is innocuous. The self-map
clause rules out best responses escaping to $\pm\infty$; with Gaussian signals on $\mathbb R$ the
indifference point can in principle sit outside any fixed compact set, so this is a restriction on
$\vartheta$ and on the menu, not a normalisation. The continuity clause is stronger still: see
Remark R1.

### Part VI — assembly of the six components, including off-path beliefs

This is task (e). Take $k^\ast$ from Step 26 and the inner system of Part II evaluated at $k^\ast$.

**Step 28 (components (i), (ii), (iv), (v)).** (i) The cutoff vector is $k^\ast\in\Theta$, weakly
ordered by Step 24, with plan rule $j_{k^\ast}$ (Step 1). (ii) The pooled component is sequentially
optimal because H8 removes within-window re-optimisation: on a pooled history the blockholder has no
decision node between date $0$ and the flag, so the only optimality requirement on the pooled
component is date-0 optimality of the plan, which is Step 25. The flagged component is sequentially
optimal by Step 19 applied at $k^\ast$, whose premise is exactly Step 25. (iv) Pooled and flagged
prices are at their fixed points by Lemma 2 and Steps 8 and 14, at every pooled history and at every
flagged tuple. (v) The bidder-entry rule is H13's threshold rule evaluated at those prices and at
$\pi(\mathcal I)$; it is a best response to the bidder's own posterior by construction of the
threshold.

**Step 29 (component (iii): on-path Bayes beliefs, pooled side).** For a pooled history $\eta$ with
$\mathbb P_{k^\ast}(\eta)>0$ (Step 7) the belief over $(v,a)$ is the Bayes posterior: a finite
mixture, over the plans in the range of $j_{k^\ast}$ whose marks are compatible with $\eta$, of the
laws of $v$ conditional on $s$ lying in the corresponding cutoff interval, with weights proportional
to (prior mass of that interval) $\times$ (probability of the noise string reconciling the marks with
$\eta$). Finiteness of the mixture is H2; positivity of the denominator is the definition of
$\mathbb P_{k^\ast}(\eta)>0$. $\pi(\eta)$ is the total weight on plans with $a_j=1$.

**Step 30 (component (iii): on-path beliefs, flagged side).** For a flagged tuple in
$\Lambda_{k^\ast}(\mathcal E_{k^\ast})$ the belief is the point mass
$\delta_{\sigma_{k^\ast}(B^F+Q^F)}$ on $s$, together with $a=1$ and $\pi=1$. Step 12 shows this is a
version of the disintegration at every such tuple. Note the sense in which a flagged node is "on
path": the flagged **cell** carries mass $\Omega$, while each individual tuple is null, so
Bayes-consistency at flagged nodes is cell-level plus disintegration, and §3(vi) is needed only for
tuples outside $\Lambda_{k^\ast}(\mathcal E_{k^\ast})$.

**Step 31 (component (vi): off-path pooled histories).** Let $\eta$ be a pooled history with
$\mathbb P_{k^\ast}(\eta)=0$. Take the perturbation family of Step 20, indexed by $t\in(0,1)$ with
kernel $\rho$ of full support on $\mathcal J$, and — when $\kappa\in\{0,1\}$ makes some noise strings
null — perturb the noise to $\kappa_t := (1-t)\kappa + t/2 \in(0,1)$, which gives every ternary
string positive probability. Under $(t,\rho,\kappa_t)$ every pooled history has strictly positive
probability, so the Bayes posterior $\mu^t(\eta)$ is defined.

**Step 32 (the perturbed posteriors converge, and the limit is a probability measure).** Write
$\mu^t(\eta)$ in the mixture form of Step 29. Its components are the laws
$\mathcal L\big(v \mid s\in I\big)$ for $I$ ranging over the at most $J$ cutoff intervals of
$k^\ast$ together with the unconditional prior law of $v$ — the latter being the relevant component
for a type that trembled, since under the tremble the event "plan $j$ was played by a trembler" is
independent of $s$ and therefore leaves $s$ at its prior. These components are **finitely many and do
not depend on $t$**. Only the mixture weights depend on $t$, and they live in a simplex of dimension
at most $2J$, which is compact. Take a sequence $t_n\downarrow0$ along which the weights converge;
the limit weights are nonnegative and sum to one, so the limit is a finite mixture of probability
measures, hence a probability measure. No mass escapes to infinity, because the components are fixed
probability measures rather than a $t$-dependent family. Define the off-path belief at $\eta$ to be
this limit. It is by construction a limit of full-support-perturbation Bayes beliefs, which is
§3(vi). The same construction, applied at flagged tuples that lie outside
$\Lambda_{k^\ast}(\mathcal E_{k^\ast})$ but inside h.11's action sets, supplies their beliefs; Step
20 showed those tuples are reached with positive probability under the same perturbations, so the
same subsequence works, and there is no separate perturbation class to invent.

**Step 33 (the off-path prices, and closure of the construction).** Given the beliefs of Steps 31–32,
the price at an off-path node is the unique root of ($\ast$) at that node's $(\bar y,\bar m)$, which
exists by Lemma 2 because the limit belief is a probability measure with finite mean (Step 32,
components have finite means by H1 and H2's amended clause) and $\bar m\ge m_0\ge0$ (H11). No
deviation payoff was left undefined at Step 21, and none was left undefined at Step 19. All six
components of §3 are now specified, and each has been verified. **This completes the existence
claim.**

### Part VII — A8 and the two cells

This is task (f).

**Step 34 (the cells partition the control-node histories).** By H9, $D=\mathbf 1\{a=1,\ c(\tau)+T\le
H\}$ is measurable and maps every control-node history into exactly one of $\mathcal C_F$ (where
$D=1$) and $\mathcal C_P$ (where $D=0$); §4.3 records the same exclusivity and exhaustiveness. By H4
the crossing date $c$ is the first date the path reaches $\tau$ and the filing lands exactly at
$c+T$, so no history is both flagged and pooled and none is neither.

**Step 35 (A8 gives both cells strictly positive mass).** At the equilibrium of Step 33, $\Omega =
\Pr(D=1)$ is a well-defined number in $[0,1]$ because $D$ is measurable (H9) and, by Step 5,
$\{D=1\}=\{s\in\mathcal E_{k^\ast}\}$ up to the noise coordinates, a Borel set. If H7 (A8) holds at
this equilibrium, then $\Pr(\mathcal C_F)=\Omega>0$ and, by Step 34's exhaustiveness,
$\Pr(\mathcal C_P)=1-\Omega>0$. An information set with strictly positive probability is reached with
strictly positive probability under the equilibrium strategy profile, which is what "on path" means
in §3(iii). So both cells are on path, the Bayes constructions of Steps 29–30 apply on both, and no
cell's conditional objects are imputed.

**Step 36 (reading C6: A8 is a condition on the fixed point, not a primitive).** $\Omega$ is
endogenous: it depends on $k^\ast$ through $\mathcal E_{k^\ast}$, and $k^\ast$ was produced by
Brouwer, which selects no particular fixed point. So the honest form of P1's second sentence is
conditional: *at any equilibrium exhibited by Step 33 at which $0<\Omega<1$, both cells are on path.*
The existence of an equilibrium at which A8 holds is a separate claim and is **not** established
here; A8 as written restricts an object that only exists after the fixed point is chosen. Two
degenerate corners are consistent with everything proved above: $\Omega=0$ (no type's plan crosses
$\tau$ by $H-T$, so the flagged cell is empty and $\Lambda_{k^\ast}$ has empty domain, which also
voids A7′ vacuously) and $\Omega=1$ (every type files, so the pooled cell is empty at the control
node). Both are equilibria under the construction; A8 excludes them by assumption, it does not
refute them.

### Remark R1 — what A6's continuity clause hides, and how to repay it

**R1.1 (it is not implied by A3 plus continuity of payoffs).** Suppose $U(j,s;k)$ is jointly
continuous in $(s,k)$ and A3 holds. $\mathcal T_j(k)$ is an infimum of an up-set determined by a
weak inequality among payoffs. If at some $k^0$ the adjacent difference $U(j+1,\cdot;k^0)-U(j,\cdot;
k^0)$ touches zero from below on an interval and then perturbs to strictly negative, the infimum
jumps by the length of that interval. Single crossing "at most once" does not exclude a flat contact,
and the card's §3 explicitly permits collapsed regions, which is where flat contacts live. So A3 plus
continuity of $U$ gives an upper- or lower-hemicontinuous correspondence, not a continuous function.
The clean primitive sufficient condition is **strict** single crossing: at every belief/price system
and every $j$, the adjacent difference is strictly increasing in $s$ on a neighbourhood of its zero.
Adding that to A3 makes $\mathcal T_j$ continuous in $k$ wherever $U$ is continuous in $k$, by the
same crossing argument used at Step 13.

**R1.2 (a second, independent source of discontinuity: off-path beliefs move with $k$).** $U(j,s;k)$
for a plan $j$ outside the range of $j_k$ is computed under the off-path beliefs of Steps 31–32,
which depend on which plans are on path, which changes discontinuously in $k$ exactly when a cutoff
interval collapses. So even with strict single crossing, $k\mapsto U(j,\cdot;k)$ can jump. The repair
is to run the whole of Parts IV–V inside the perturbed game at a fixed tremble size $t>0$: there every
plan is played with probability at least $t\min_j\rho(j)>0$ by every type, so every node is on path,
every belief is Bayes, and the mixture weights of Step 29 are continuous in $k$; then take
$t_n\downarrow0$, extract a convergent subsequence of the fixed points $k^{t_n}\in\Theta$ (compact,
§4.5), and pass to the limit using Lemma 2's continuity for prices and Step 32's compactness for
beliefs. The limit object satisfies §3(i)–(v) and, by construction, §3(vi). I did not run this route
as the main proof, because the card's §3 prescribes Brouwer under A6 and A6 is available as a
hypothesis; I record it because it is the route that discharges A6's continuity clause rather than
assuming it, and it costs only the strict-crossing strengthening of A3 in R1.1.

**R1.3 (what would be needed to make A6 a theorem).** A3 strengthened as in R1.1, the perturbed-game
route of R1.2, and a uniform bound placing all indifference points in a fixed compact interval —
which for Gaussian signals needs a condition such as: the adjacent payoff difference is strictly
negative below some $\underline\theta$ and strictly positive above some $\bar\theta$, uniformly over
belief/price systems reachable from $\Theta$. That last condition is A6's self-map clause in
primitive form, and I do not verify it for any concrete menu.

---

## WHERE IT FAILS

**Case 1 — h.11 replaced by the full interval $[0,\bar b-B^F]$ (the non-definitional reading).**
Then the flagged node has a continuum of actions, and all but countably many are generated by no
plan. Identity ($\ddagger$) of Step 18 has no counterpart for such a $Q'$, so date-0 optimality
places no restriction on it and Step 19 collapses. Sequential optimality then requires the prescribed
$Q^F_j(s)$ to solve a genuine maximisation over an interval. But $Q^F_j(s)=b^*_j(s)-B^F_j(s)$ is
fixed by the exogenous menu (§4.2) and by H8's no-re-optimisation clause; it was never derived from a
first-order condition in $Q'$. Concretely: the flagged payoff at a deviation $Q'$ is
$b^*{}'\,\mathbb E[Y\mid\text{tuple}] - Q'P^F(B^F,Q')$ with $b^*{}'=B^F+Q'$, whose derivative in $Q'$
at $Q'=Q^F_j(s)$ is $\mathbb E[Y\mid\cdot] - P^F - Q'\,\partial_{Q'}P^F$ plus the belief-response
term. There is no mechanism in the card forcing this to vanish, so for a generic menu the prescribed
order is not a local maximum and **no** cutoff PBE with the menu's own flagged component exists. The
flagged round becomes a continuum-message signalling game whose existence question is separate; §9
already records that the card does not claim noisy or partially revealing flagged trading, and this
is the cost of that.

**Case 2 — A7′ dropped, so the composed target is not strictly increasing.** Suppose two flagged
signals $s\ne s'$ (possibly under different plans) satisfy $\Sigma_k(s)=\Sigma_k(s')$ and
$B^F(s)=B^F(s')$. Then $\Lambda_k$ is not injective, ($\dagger$) fails, and the flagged belief is a
nondegenerate two-point mixture rather than a point mass. Two consequences, both fatal to the
architecture above. (a) Step 12's everywhere-defined version is lost: the conditional law can then be
pinned only almost everywhere, so $P^F$ becomes a choice on a null set and the flagged-node objects
are no longer functions of the tuple. (b) Step 17's $z$-freeness argument breaks, because the belief
at the tuple must then be formed from the whole flagged information set; the deviation $Q^F_{j'}(s)$
is priced at a mixture that includes type $s'$, so ($\ddagger$) is replaced by an inequality with an
uncontrolled cross-type term and Step 19 no longer delivers sequential optimality. The card's own
failure boundary for A7′ — a binding stake cap, quantised stakes, a composed target repeating values
across Voice-plan switches — is exactly the set of menus on which this case is live.

**Case 3 — A6's continuity clause dropped.** By Remark R1.1 the map $\mathcal T$ can jump at a $k$
where an adjacent payoff difference has flat contact with zero, and by R1.2 it can jump where a
cutoff interval collapses and a plan leaves the path. A discontinuous self-map of a compact convex
set need have no fixed point — the one-dimensional witness is $\Theta=[0,1]$ with
$\mathcal T(k)=1$ for $k<\tfrac12$ and $\mathcal T(k)=0$ for $k\ge\tfrac12$ — so Step 26 fails and
existence is not merely unproved but can be false. Since §3 explicitly permits collapsed regions,
this is not a corner case of the model but a region the card invites.

**Case 4 — h.12 dropped in the strengthened architecture (A5 derived rather than assumed).** Take a
pooled control node with $m_0<0$ and a low engagement posterior, so $\bar m<0$, and put
$\bar y=0$, $\bar m=-1$, $K=0.2$, $\bar S=0.5$, $\sigma_\xi=0.1$. Then
$\zeta(P)=P-\Psi(P)=P+\frac{p(P)}{1-p(P)}$ with $p(P)=\Phi\big((1.3-P)/0.1\big)$. Every term is
strictly positive for $P\ge0$, and for $P\to-\infty$ the ratio $p/(1-p)$ grows at the Gaussian
inverse-Mills rate, which dominates $|P|$; the minimum of $\zeta$ over $\mathbb R$ is near $P\approx
1.5$ and is close to $1.52$, strictly above zero. So ($\ast$) has **no** solution: the competitive
price does not exist at that node, A5's existence clause is false there, and both the pooled price
and everything built on it are undefined. With $\bar m<0$ but smaller in magnitude one instead gets
$\Psi$ increasing, hence possible multiplicity, hence failure of A5's uniqueness clause and of the
measurable selection at Step 14. This is the precise sense in which h.12 buys A5.

---

## LABEL CLAIMED

**For this document: PROVED-WITH-CHANGES**, with the eight changes C1–C8 tabulated at the top and
argued at the steps named there.

**For the card's ledger: P1 stays CONJECTURE until a proof-read passes.** §7's protocol requires an
independent re-derivation PASS *plus* a proof-read PASS before PROVED, and §8's rule 1 keeps that
gate outside this document. What I can say is what this re-derivation supports: P1 in its amended
form is provable, and the proof I can supply is the one above, under A1, **A2′**, A3, A4, A6, A7′,
h.11, h.12, h.13, §2 read with C5, and D1's ledger statement — with A5 **dropped** because it is
derived, and with A8 read as a condition on the exhibited fixed point rather than a primitive. If the
proof-read accepts C1–C8, the label move is `P1 | CONJECTURE→PROVED | rederive/P1_rederivation.md +
proof-read path | Opus re-deriver | 2026-08-21 | <commit>`. If the proof-read rejects C1 (the A2
amendment) or C2 (the added objective), the honest label is CONJECTURE, because P1 as literally
stated then rests on a hypothesis set that is either self-contradictory (C1) or incomplete (C2).

---

## NUMERICAL CHECK REQUEST

Four checks. All are scalar or low-dimensional; none needs the full solver.

**Check A — Lemma 2, existence and uniqueness under h.12.**
Formula: $\zeta(P)=P-\bar y-\dfrac{p(P)}{1-p(P)}\bar m$, $p(P)=1-\Phi\!\big((P+K+\bar m-\bar
S)/\sigma_\xi\big)$.
Grid: $\bar y\in\{-2,-1,0,1,2\}$, $\bar m\in\{0,0.1,0.3,0.6,1.0\}$, $K\in\{0.1,0.2,0.5\}$,
$\bar S\in\{0,0.5,1\}$, $\sigma_\xi\in\{0.25,0.5,1\}$, $P$ on $[-20,20]$ at step $10^{-3}$.
Predicted sign: exactly one sign change of $\zeta$ per cell, and $\zeta$ nondecreasing along the $P$
grid in every cell (weakly, to $10^{-12}$).
Predicted magnitude: at $\bar y=0$, $\bar m=0.3$, $K=0.2$, $\bar S=0.5$, $\sigma_\xi=0.5$ the root is
$P^\ast\approx 0.1727$ with $p(P^\ast)\approx 0.365$; the root should lie in $[0.170,0.176]$ and
$p(P^\ast)$ in $[0.36,0.37]$.

**Check B — Case 4, nonexistence when h.12 is dropped.**
Same formula, $\bar y=0$, $\bar m=-1$, $K=0.2$, $\bar S=0.5$, $\sigma_\xi=0.1$, $P$ on $[-50,50]$ at
step $10^{-3}$.
Predicted sign: $\zeta>0$ at every grid point — zero roots.
Predicted magnitude: $\min_P\zeta(P)\approx 1.52$, attained near $P\approx 1.5$; report the minimum
and its argmin, expected in $[1.45,1.60]$ and $[1.4,1.7]$ respectively. A second cell with
$\bar m=-0.05$, $\sigma_\xi=0.05$ should exhibit **three** roots, breaking uniqueness rather than
existence.

**Check C — Step 11, the monotone inverse.**
Formula: on a pro-rata single-Voice menu, tabulate $\Sigma_k(s)=b^*_{j_k(s)}(s)$ and
$\sigma_k(\Sigma_k(s))$ over the flagged set.
Grid: $s$ on $[-4,4]$ at step $10^{-4}$, for at least 20 draws of $k$ from $\Theta$ including two
with a collapsed interval ($k_i=k_{i+1}$).
Predicted sign: $\Sigma_k$ strictly increasing at every consecutive grid pair, for **every** drawn
$k$ (this is A7′'s uniformity clause and is the one the fixed point needs).
Predicted magnitude: $\max_s|\sigma_k(\Sigma_k(s))-s| \le 10^{-12}$; and
$\min_s\big(\Sigma_k(s+10^{-4})-\Sigma_k(s)\big) > 0$ with the reported minimum increment of order
$10^{-4}\cdot\partial_s b^*$, not of order $10^{-16}$.

**Check D — Steps 24–26, the outer map.**
Formula: a $J=3$ menu (Exit, Hold, one Voice plan), $U(j,s;k)$ from H12 with the prices of Check A;
$\mathcal T$ as in Step 24; iterate $k\mapsto\mathcal T(k)$ from 50 starts in $\Theta$.
Grid: $\kappa\in\{0.1,0.3,0.5,0.7,0.9\}$, $\tau\in\{0.03,0.05,0.10\}$, $T\in\{1,5,10\}$, $H=20$.
Predicted sign: $\mathfrak b(\cdot;k)$ nondecreasing in $s$ at every $k$ visited (A3's testable
content), and $\mathcal T_1(k)\le\mathcal T_2(k)$ at every $k$ visited (Step 24).
Predicted magnitude: at least one fixed point per cell with $\lVert k-\mathcal T(k)\rVert_\infty\le
10^{-8}$; and the count of distinct fixed points across the 50 starts reported per cell, expected
$\ge1$ and **not** expected to be $1$ everywhere — a cell with more than one fixed point is
consistent with the claim, since uniqueness is not claimed.

---

## NOTATION DELTA

Every symbol used above that is not in §4 of the card. Bare $g$ is not used anywhere (reserved for
$g_r^{PE}$); $\beta$ is used only in §4.1's sense; bare $\lambda$, $\psi$, $\chi$, $W$, $G$ and
$\mathsf Z$ do not appear.

| Symbol | Meaning | Introduced |
|---|---|---|
| $j_k(s)$ | the plan rule generated by cutoff vector $k$: $1+\#\{i:k_i\le s\}$ | Step 1 |
| $\mathcal E_k$ | the flagged signal set $\{s: D_{j_k(s)}(s)=1\}$ at cutoff vector $k$ | Step 5 |
| $U(j,s;k)$ | blockholder date-0 expected payoff from plan $j$ at signal $s$ in the system indexed by $k$ | H12, Step 4 |
| $U^F(j,s)$ | flagged-round continuation payoff, shown to be free of the noise realisation | Step 17 |
| $\mathfrak d(s;j,j')$ | date-0 payoff difference $U(j,s;k)-U(j',s;k)$ (fraktur d; $D$ is disclosure, $\Delta$'s are premia) | Step 18 |
| $\iota_j(s)$ | last pooled trading date under plan $j$: $f_j(s)$ if flagged, else $H$ ($\iota_F$ is free per §4.6) | H12 |
| $\mathcal K_s(j)$ | h.11's closure class: plans sharing $j$'s pooled path up to $f_j$ with the same $a$ | Step 15 |
| $\Lambda_k$ | flagged-tuple map $s\mapsto(B^F,Q^F,1)$ at cutoff vector $k$ | Step 11 |
| $\Sigma_k$ | composed terminal target $s\mapsto b^*_{j_k(s)}(s)$, A7′'s object, $=B^F+Q^F$ | Step 11 |
| $\sigma_k$ | the increasing inverse $\Sigma_k^{-1}$ on the image (lower-case sigma; $\sigma_v,\sigma_\varepsilon,\sigma_\xi$ always carry subscripts) | Step 11 |
| $\delta_x$ | point mass at $x$ | Step 11 |
| $\bar y(\mathcal I)$ | belief summary $\mathbb E_\mu[v]+\pi(\mathcal I)\Delta_V$ | Lemma 2 |
| $\bar m(\mathcal I)$ | belief summary $m_0+\pi(\mathcal I)\Delta_m$ — h.12's object | Lemma 2 |
| $\Psi_{\mathcal I}$ | the scalar pricing map $P\mapsto\bar y+\frac{p}{1-p}\bar m$. **Capital psi; distinct from D7's lower-case $\psi$ (pivotality), which is not used here** | Step 9 |
| $\zeta$ | the excess-price function $P-\Psi_{\mathcal I}(P)$ | Step 13 |
| $P^\ast(\bar y,\bar m)$ | the unique root of $\zeta$ | Lemma 2 |
| $\eta$ | a pooled public history (a realised value of $\mathcal H^P_d$) | Step 7 |
| $t$, $t_n$, $\rho$, $\kappa_t$ | tremble size, tremble sequence, full-support kernel on $\mathcal J$, perturbed noise intensity. **Roman $t$, not $\varepsilon$ — $\varepsilon$ is the signal noise** | Steps 20, 31 |
| $\mu$, $\mu^t(\eta)$ | a belief over $(v,a)$ at a node; the perturbed Bayes belief at $\eta$ | Lemma 2, Step 31 |
| $\mathfrak b(s;k)$ | the min-selection best plan $\min\arg\max_j U(j,s;k)$ (fraktur b; $b_0,\bar b,b^*_j$ are stakes) | Step 22 |
| $\underline\theta,\bar\theta$ | the lower and upper bounds of the polytope $\Theta$ | Step 24 |
| $\varepsilon_0$ | a proof-local positive number in the crossing argument, distinct from the signal noise $\varepsilon$ | Step 13 |
| A2′ | the amended finiteness hypothesis of change C1 | H2 |
| h.13 | the added blockholder-objective hypothesis of change C2 | H12 |
| $u_1,u_2$ | not used | — |

---

## NOT CLAIMED

1. **Uniqueness.** Nothing above rules out multiple fixed points of $\mathcal T$, and Check D is
   written so that finding several is not a refutation.
2. **That an equilibrium satisfying A8 exists.** Step 36: A8 restricts an endogenous object at a
   fixed point Brouwer does not select. $\Omega=0$ and $\Omega=1$ equilibria are not excluded by
   anything proved here.
3. **That A3, A6 or A7′ hold for any concrete menu.** They are used as hypotheses at Steps 23–24 and
   11. I did not open the A7′ construction file and I verify nothing about it; Check C is the
   executed test I would want run against whatever menu the card ends up carrying.
4. **That A6's continuity clause is true.** Remark R1 states what it hides and gives a route to
   repay it; I did not run that route.
5. **Refinement.** The equilibrium constructed is a perfect Bayesian equilibrium in the card's §3
   sense. It is not claimed sequential, trembling-hand perfect, or robust to trembles in the flagged
   order $Q^F$ itself — Step 20's perturbation class is trembles over **plans** only, which is what
   h.11 makes sufficient.
6. **Uniqueness of off-path beliefs.** Step 32 extracts a convergent subsequence; a different
   subsequence or a different kernel $\rho$ can give a different limit, and every such limit yields
   an equilibrium by the same argument.
7. **That h.11 is economically innocuous.** It is a modelling restriction with content: it removes
   the flagged round's continuum of deviations by definition rather than by an argument, and Case 1
   shows what it is removing. Whether that restriction is defensible is a modelling judgement, not a
   theorem, and this document does not make it.
8. **Anything about comparative statics.** No claim about $\kappa$, $\tau$, $T$, $\Delta^{\mathrm
   {act}}$, $\mathcal S$, $M_F$, $M_P$, the chord, or the sign of any derivative. P1 is an existence
   statement and this is an existence proof.
9. **That the pooled component is optimal against within-window re-optimisation.** Step 28 uses H8 to
   assert there is no decision node inside the window. If §2's no-feedback clause were relaxed, the
   pooled component's sequential optimality would need its own argument and Step 28(ii) would fail.
10. **That the card's A2, as literally written, is consistent with A7′.** Step 3 argues it is not,
    and I proceed under A2′ instead.

