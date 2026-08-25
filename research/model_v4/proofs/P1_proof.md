# P1 — Cutoff PBE existence (full proof)

**Written against MODEL CARD v4, version stamp 2026-08-20 · commit `0c9185b`.**
Sources consumed: card §§2–5 and §8; `threads/thread1_turn1_answer.md` §P1 (the statement);
`threads/thread1_turn2_audit.md` (the D1 repairs, in particular D1-R2 on the flagged continuum,
and L2-R1/L2-R2 on the injective form of A7 and the no-feedback timing).

**Patched 2026-08-25 (ticket 35 / R5) against MODEL CARD stamp 2026-08-23 · commit `d2ccf62`**, to
match the amended P1 row: A7-J in place of A7′ at h.7, the new h.16, the $\kappa$ boundary in Step 9,
and the objective display at h.14. Every change is listed in *Repairs applied (2026-08-25)* at the
foot of this file and traces to a numbered finding of
`threads/2026-08-23_gpt_end_review_audit.md`. **No step conclusion is weakened and no label moves:
P1 remains CONJECTURE** pending ticket 35's two fresh passes.

---

## CLAIM

Fix the parameter vector $\vartheta$. Under hypotheses h.1–h.12, h.14 and h.16 below — A1–A6 of card
§5 together with A7 in its **A7-J (joint tuple injectivity)** form, the card's §2 no-feedback timing,
D1, the round-2 action-set stipulation h.11, the continuation-cost equivalence h.16, the sign
convention h.12, and the blockholder payoff definition h.14 (card §4.3's $U_j$ row, absorbed there at
the 2026-08-23 regeneration) — the two-round model has, **at every $\kappa\in[0,1]$**, at least one
**cutoff perfect Bayesian equilibrium over
complete contingent plans** in the sense of card §3: a weakly ordered cutoff vector
$k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, together with pooled and flagged
price families at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs
obtained as limits of full-support perturbations over **plans** at every pooled history reachable
under some plan profile, flagged-tuple beliefs **pinned by h.7** at every tuple in the image of the
flagged-pair map $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$ — on path and off — with no tuple outside that image
arising under h.11 (Step 10), the card §4.3 bidder-entry rule, and a
sequentially optimal flagged component. Under A8 evaluated at $k^\star$, both cells $\mathcal C_F$
and $\mathcal C_P$ carry strictly positive probability, hence both are on path.

*On the belief clause.* The qualifier "reachable" is Step 9's, and it is a precision about which
information sets carry a card §3(vi) requirement, not a weakening of the requirement at any of them.
At $\kappa\in\{0,1\}$ the noise support degenerates — $\mathrm{supp}(z_d)=\{0\}$ at $\kappa=0$ and
$\{-\bar z,+\bar z\}$ at $\kappa=1$ — and a pooled history that needs a mark outside it has
probability zero under **every** plan profile and every perturbation stage, so it is null under
nature rather than off path under the players and §3(vi) asks nothing of it. At every reachable
history, on path and off, the limit exists and pins the belief.

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
7. **h.7 = A7-J (joint tuple injectivity)** — card §5's **joint** form of A7, not its on-path form
   A7′. $(j,s)\mapsto (B_j^F(s),Q_j^F(s),a_j)$ is injective on the flagged-**pair** set
   $\{(j,s):D_j(s;\tau,T)=1\}$, **including flagged pairs that no cutoff vector $k\in\Theta$
   selects**. Per card §5's turn-2 note the weak wording of A7 ("identifies the informed component")
   is not sufficient, and injectivity forces the **tuple** $(B^F,Q^F)$ to be continuum-valued — *not*
   the coordinate $B^F$ on its own, which may be non-monotone and may jump downward while the tuple
   still separates through the sum coordinate $B^F+Q^F=b_j^*(s)$; the coordinates trade the burden
   (card §5's A7 note; `proofs/A7_construction.md` Steps 8–9 with its numeric witness;
   `proofs/A7_attack_verdict.md` S-10; audit Finding 7(ii)).
   **This is strictly stronger than A7′** — on-path injectivity can hold while the joint map collides
   at pairs off the selected policy (the 40-collision executed witness in the attack verdict) — and
   it is the form Steps 6 and 10 consume: Step 10 pins the *off-path* flagged belief, which is a
   statement about pairs the conjecture does not select. It is **satisfiable**: the pinned pro-rata
   single-Voice menu with terminal target strictly increasing on all of $\mathbb R$ satisfies A7-J
   (`proofs/A7_construction.md` Step 7; card §5's A7 note, ticket 24). *Used: Steps 6, 10.*
8. **h.8 = A8 (interior crossing), evaluated at the fixed point.** $0<\Omega(\kappa,\tau,T)<1$ at
   $k^\star$. *Used: Step 19 only.*
9. **h.9 = D1 (rule-keyed partition and timing split).** $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is
   measurable and maps every control-node public history into exactly one cell; for every Voice
   plan $f_j\le H\iff B_j(s,H-T)\ge\tau$. D1 carried the card's label CONJECTURE when this proof was
   written, so P1 inherited that conditionality; **at stamp `d2ccf62` D1 is PROVED** (moved
   2026-08-21 with both passes on file), and what P1 inherits is D1's own hypothesis set as listed in
   the card's D1 row, not a provisional label. *Used: Steps 2, 6, 19, 20.*
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
14. **h.14 [ADDITION, card gap closed 2026-08-23] — the blockholder's payoff.** For plan $j$ at
    signal $s$,
    $$U_j(s)=\mathbb E\bigl[b_j^*(s)\,Y-\mathcal C_j^{\mathrm{trade}}-a_j\,C_j(s)\ \big\vert\ s,j\bigr],$$
    with $\mathcal C_j^{\mathrm{trade}}$ the plan's execution outlay — the stake increments valued at
    the pooled prices $P_d^P$ up to the plan's last pooled date, plus $Q_j^F(s)P^F$ when $D_j=1$ —
    and $C_j(s)\ge0$ the engagement cost, which enters **weighted by the engagement flag $a_j$**, so
    that plans with $a_j=0$ pay no engagement cost whatever $C_j$ is written as. *Display aligned
    2026-08-25 with card §4.3's $U_j$ row, which carries $-a_jC_j(s)$ and cites this hypothesis as
    "displayed there in full"; the pre-repair display wrote $-C_j(s)$ (audit Finding 1, citation
    nit). The $a_j$ factor is immaterial to every step that consumes h.14: Steps 11–12 run on the
    flagged set, where $a_j=1$ by h.4.* No step consumes the sign $C_j\ge0$; it is transcribed
    because the card row carries it.
    **History:** when this proof was written the card carried no blockholder payoff row — no §2.10,
    no $U_j$, no $\mathcal C_j^{\mathrm{trade}}$ — and the object was stated here as this proof's own
    numbered definition, faithful to `threads/thread1_turn1_answer.md` §2.10. The 2026-08-23
    regeneration absorbed it as card §4.3's $U_j$ row (batch-1 audit P1-R6, P1 re-derivation change
    C2), so h.14 is now a transcription of a card row rather than a card gap. *Used: Steps 11, 13,
    14, 15 — it is the optimand of Steps 11–13 and the object Step 15 asks to be continuous.*
15. **h.15 [ADDITION] — engagement flags on an upper set of the menu.** $a_j=1$ exactly on an upper
    set of the ordered menu: there is $j_a$ with $a_j=1$ for $j\ge j_a$ and $a_j=0$ for $j<j_a$.
    Card §4.2 says $a_j=1$ for Voice and $0$ for Exit/Hold and orders the menu "least to most
    aggressive", but never ties the two; card §4.5's four-action gloss happens to satisfy this and a
    general finite menu need not. *Used: Step 20 only, alongside h.13 — not for existence.*
16. **h.16 [ADDITION] — continuation-cost equivalence on the round-2 deviation set.** For every
    $(j,s)$ on the flagged set and every $j'$ in the generating set of h.11's action set
    $\mathcal Q_j(s)$ — every $j'\in\mathcal J$ that shares $j$'s pooled path up to $f_j(s)$ and has
    $a_{j'}=a_j$ — the engagement costs agree:
    $$C_{j'}(s)=C_j(s)\qquad\text{on each h.11 deviation set.}$$
    Equivalently: within a deviation set the engagement cost is a function of $(a_j,s)$ alone and not
    of which round-2 order the plan carries. *Used: Step 12.*

    **Why this clause is needed (audit Finding 1(b)).** Step 12 defeats a round-2 deviation by moving
    it back to date 0, so the two comparisons have to be the same comparison. Write Step 11's
    decomposition as $U_j=G_j-a_jC_j-E_j$, with
    $G_j(s;k)=b_j^*(s)\mathbb E[Y\mid s,j,D=1]-P^F(\sigma_F)Q_j^F(s)$ the **trading terms** of the
    first bracket and $E_j$ the pooled-execution second bracket. On a deviation set $E_{j'}=E_j$
    (identical pooled paths) and $a_{j'}=a_j=1$ (h.4), so the *only* wedge between "the deviation
    improves the flagged continuation" and "$U_{j'}>U_j$" is $C_{j'}(s)-C_j(s)$. A round-2 deviator
    has already sunk the engagement — the filing has landed and $D=1\Rightarrow a=1$ is public (h.4),
    so the engagement cannot be unmade — and therefore compares continuations holding that cost
    fixed. Without h.16 the wedge is live and the contradiction fails; the pre-repair Step 12 closed
    it silently.

    **Why the sunk-cost restatement does not replace it (spec MAY-11, both routes worked out).**
    Two readings of the deviation's continuation are available and the card fixes neither (card
    §4.3's $U_j$ row does not date $C_j$): **(α) plan completion** — submitting $Q_{j'}^F(s)$ *is*
    completing plan $j'$, so the deviator bears $C_{j'}(s)$ and the continuation is $G_{j'}-C_{j'}$;
    **(β) sunk cost** — the engagement cost is already booked, so the continuation is $G_{j'}-C_j$.
    Under (α) Step 12 needs no extra clause, but (α) is the reading that begs the question, since the
    deviation is precisely a *departure* from plan $j'$'s date-0 commitment. Under (β), date-0
    optimality of $j$ delivers only $G_j-G_{j'}\ge C_j-C_{j'}$, while (β)-optimality needs
    $G_j-G_{j'}\ge 0$; the implication therefore requires $C_{j'}(s)\le C_j(s)$ at the selected $j$
    — a one-sided clause, not no clause. And once it is a hypothesis of P1 the one-sided form
    collapses onto h.16's equality. Two reasons, both needed:
    *(1) the sharing relation is symmetric.* If $j'$ agrees with $j$ on the pooled path up to
    $f_j(s)$ then $c_{j'}(s)=c_j(s)$ — the crossing date is a first-hitting index of a path they
    share, and $c_j\le f_j-T\le f_j$ — hence $f_{j'}(s)=f_j(s)$, so $j$ agrees with $j'$ up to
    $f_{j'}(s)$ as well; with $a_{j'}=a_j$, "shares the pooled path and the engagement flag" is an
    equivalence relation on the flagged set at each $s$, and each h.11 deviation set is one of its
    classes.
    *(2) the hypothesis must be uniform on $\Theta$.* Brouwer does not say which $k^\star$ it
    returns, and at every $s<\overline s$ each $j\in\mathcal J$ is the selected plan at some
    $k\in\Theta$ (choose cutoffs with $j_k(s)=j$; only the right endpoint $s=\overline s$ is
    exceptional, where $k_i\le\overline s$ forces $j_k(\overline s)=J$ — a single signal point, and
    h.16 is imposed as an equality at every $s$ regardless, so nothing turns on it). A hypothesis of
    P1 therefore cannot be indexed by the equilibrium's selection. Imposing
    $C_{j'}\le C_j$ for every selectable $j$ and every $j'$ in its class imposes it in both
    directions across the class: $C_{j'}=C_j$. **MAY-11's route therefore lands on this same clause**,
    which is why it is stated once, as h.16, rather than twice.
    **A bonus of h.16, and the reason it is the cleaner discharge:** under it (α) and (β) are the
    *same number* on every deviation set, so Step 12 is valid whichever date the engagement cost is
    booked at, and the proof does not have to adjudicate a card ambiguity it has no standing to
    settle. **Card ambiguity, regeneration item: card §4.3's $U_j$ row should say when $C_j(s)$ is
    incurred.**

    **Satisfiability.** h.16 is **trivially true on any single-Voice menu**, the pinned pro-rata menu
    included: on the flagged set $a_j=1$ (h.4), so a deviation set contains only Voice plans, and
    with one Voice plan it is the singleton $\{j\}$ and $\mathcal Q_j(s)=\{Q_j^F(s)\}$
    (`proofs/A7_construction.md` Steps 5–7: Exit and Hold never cross $\tau$ when $b_0<\tau$). It is
    a genuine restriction only on menus carrying two or more Voice plans that share a pooled path
    (WHERE IT FAILS 7).

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

**Step 9 (pooled off-path beliefs as limits of full-support perturbations, on the reachable history
set — stated for every $\kappa\in[0,1]$, endpoints included).**
Card §3(vi) requires off-path beliefs to be limits of full-support perturbations. Index the
perturbation by $n$: at stage $n$ every signal type plays every plan $j\in\mathcal J$ with weight at
least $1/n$, the remaining mass following $j_k$.

*(a) The alphabet, said honestly.* Card §4.1's noise law is $\Pr(z_d=0)=1-\kappa$ and
$\Pr(z_d=\pm\bar z)=\kappa/2$ on the in-domain range $\kappa\in[0,1]$, so the **realised** support is
$$\mathrm{supp}(z_d)=\{0\}\ \text{at }\kappa=0,\qquad \{-\bar z,+\bar z\}\ \text{at }\kappa=1,\qquad
\{-\bar z,0,+\bar z\}\ \text{at every }\kappa\in(0,1).$$
No conflict with h.2: h.2's $\{-\bar z,0,+\bar z\}$ is the noise **alphabet**, finite at every
$\kappa$ and the only thing Step 3's finiteness argument needs; $\mathrm{supp}(z_d)$ is the subset of
that alphabet carrying positive probability at the maintained $\kappa$, and it is the object a
zero-probability argument has to be quantified over.
Call a pooled history $\mathcal H_d^P=(X_0,\dots,X_d;\text{flag landed by }d)$ **reachable** if it
carries strictly positive probability under some plan and a positive-probability set of signals:
some $j\in\mathcal J$ and some Borel $S$ with $\Pr(s\in S)>0$ such that
$X_{d'}-q_{jd'}(s)\in\mathrm{supp}(z_{d'})$ for every $d'\le d$ and every $s\in S$, with the flag
coordinate agreeing with $\mathbf 1\{f_j(s)\le d\}$. Reachability is a property of the menu and the
noise law alone: it does not depend on the conjecture $k$ and it does not depend on $n$, because the
perturbation gives every plan weight at least $1/n>0$ at every type and the noise law is common
across plans. This is the whole-history form, and it is what the argument needs — a history each of
whose marks is individually attainable under *some* plan need not be attainable under any *one*
plan.

*(b) The limit exists at every reachable history.* By h.2 the plan menu is finite and by Step 3 the
pooled history alphabet is finite, so for each pooled history the perturbed
posterior over plans is a ratio whose numerator and denominator are finite sums of terms
polynomial in $1/n$ with coefficients that do not depend on $n$. At a reachable history the
denominator is strictly positive for every $n$: the witnessing pair $(j,S)$ contributes at least
$(1/n)\int_S\prod_{d'\le d}\Pr\bigl(z_{d'}=X_{d'}-q_{jd'}(s)\bigr)\,\mathrm d\Phi_s(s)$, with $\Phi_s$
the signal c.d.f. of the NOTATION DELTA, and it is strictly
positive because each factor is positive on $S$ by the definition of reachability and, by h.2, the
mark $q_{jd'}(\cdot)$ takes finitely many values, so the product takes finitely many positive values
on $S$ and is bounded below by their minimum; every other term in the denominator is nonnegative.
A ratio of polynomials in $1/n$ with a denominator that is nonzero
for all large $n$ converges as $n\to\infty$. Hence the limiting belief exists at every **reachable**
pooled history, on path and off, and on path it agrees with the Bayes posterior. This is where h.2's
finiteness pays: with a continuum of pooled histories the limit would need a separate argument.

*(c) Unreachable histories carry no requirement, and no step consumes one.* An unreachable history
has probability zero under **every** plan profile, perturbed or not — it is null under nature, not
off path under the players — so card §3(vi) asks nothing of it and card §3(iv) prices nothing there.
Nothing downstream evaluates one: Step 11's pooled-execution bracket integrates
$P_d^P(\mathcal H_d^P)$ against the law of $z_{0:H}$ under the plan actually played, which puts mass
only on reachable histories, and the same holds for every deviation in h.11's action set, since those
share $j$'s pooled path and hence its reachable set. So no payoff comparison anywhere in Parts D–E
reads a price at an unreachable history.

*(d) The $\kappa$ boundary (audit Finding 1(c)).* The pre-repair text asserted that "every noise mark
carries positive probability whenever $\kappa>0$", with $\kappa=0$ special-cased. That is **false at
$\kappa=1$**, which is in-domain: there $\Pr(z_d=0)=0$, and a pooled history requiring a zero mark is
null under every plan profile, so the plan-only perturbation leaves its limit belief undefined —
exactly the mirror of the $\kappa=0$ case, where only the zero mark survives. Parts (a)–(c) replace
both special cases with one sentence quantified over $\mathrm{supp}(z_d)$, and the claim therefore
holds on the card's **full domain $\kappa\in[0,1]$, both endpoints included**, with no restriction to
$\kappa\in[0,1)$. What the endpoints change is *which* histories are reachable, never whether the
reachable ones carry a limit. Note the correction runs the other way too: the pre-repair claim
"the limiting belief exists at every pooled history" was false as stated at $\kappa\in\{0,1\}$, so
naming the reachable set is a repair of a false assertion, not a retreat from a true one.

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
of **h.14** — $U_j(s)=\mathbb E[b_j^*(s)Y-\mathcal C_j^{\mathrm{trade}}-a_jC_j(s)\mid s,j]$, now
card §4.3's $U_j$ row and transcribed at h.14 — therefore splits as
$$
U_j(s;k)\;=\;\underbrace{b_j^*(s)\,\mathbb E\bigl[Y\mid s,j,D=1\bigr]-P^F(\sigma_F)\,Q_j^F(s)-a_jC_j(s)}_{\text{flagged continuation: deterministic in }(j,s)}
\;-\;\underbrace{\mathbb E_{z}\Bigl[\textstyle\sum_{d\le f_j}P_d^P\bigl(\mathcal H_d^P\bigr)\bigl(B_j(s,d)-B_j(s,d-1)\bigr)\Bigr]}_{\text{pooled execution: determined by the pooled path alone}} ,
$$
where the pooled expectation is over the noise $z_{0:H}$ only. **On the flagged branch $a_j=1$ by
h.4**, so the engagement term of the first bracket is $C_j(s)$ and the $a_j$ factor — carried here to
match card §4.3's display (audit Finding 1, citation nit) — changes nothing in Steps 12–13. By Step
9(c) every pooled history the second bracket weighs is reachable, so the prices it reads are the ones
Steps 5 and 9 supply. The noise enters the first bracket
nowhere: $\mathbb E[Y\mid s,j,D=1]$ depends on $(v,\xi)$ and on $P^F$, and $\xi$ is independent of
$z$ by h.1 while $P^F$ is $z$-free by Step 6.

**Step 12 (h.11 and h.16 make the flagged component sequentially optimal, and nothing in A1–A7
does).**
Let $k$ be a conjecture and let $j=j_k(s)$ maximise $U_{\cdot}(s;k)$ over $\mathcal J$ at a flagged
$(j,s)$. Write Step 11's decomposition as
$$U_j(s;k)=G_j(s;k)-a_jC_j(s)-E_j(s;k),\qquad
G_j(s;k):=b_j^*(s)\,\mathbb E\bigl[Y\mid s,j,D=1\bigr]-P^F(\sigma_F)\,Q_j^F(s),$$
with $G_j$ the **trading terms** of the first bracket and $E_j$ the pooled-execution second bracket.
Suppose some
round-2 order $Q'$ available at $(j,s)$ strictly improves the flagged continuation, holding the
market's flagged pricing schedule at the family of Step 6. By **h.11** the available orders are
exactly $\mathcal Q_j(s)$, the plan-generated set, so $Q'=Q_{j'}^F(s)$ for some $j'\in\mathcal J$ with
the same pooled path up to $f_j(s)$ and the same engagement flag. Identical
pooled paths give identical order marks $q_{j'd}=q_{jd}$ for $d\le f_j$ (h.10, Step 2), hence
identical realised pooled histories for every noise draw and therefore $E_{j'}=E_j$; and
$a_{j'}=a_j=1$ on the flagged set by h.4. Note also $B_{j'}^F(s)=B_j^F(s)$ — the shared path pins the
stake at the shared filing date — so the deviation's flagged tuple is
$\sigma_F'=(B_j^F(s),Q_{j'}^F(s),1)$ and its terminal stake is $b_{j'}^*(s)$: the deviation's trading
terms are exactly $G_{j'}(s;k)$.

**The comparison must be cost-honest (audit Finding 1(b)).** The deviation's continuation is
$G_{j'}-C_{j'}(s)$ if submitting $Q^F_{j'}(s)$ counts as completing plan $j'$ and paying its
engagement cost, and $G_{j'}-C_j(s)$ if the engagement cost is already sunk at round 2 — which it is,
the filing having landed with $D=1\Rightarrow a=1$ public (h.4). The card dates $C_j$ under neither
reading. **Under h.16 the two are the same number**, $C_{j'}(s)=C_j(s)$ on the deviation set, so the
supposition "$Q'$ strictly improves the flagged continuation" says $G_{j'}(s;k)>G_j(s;k)$ on either
reading. Then
$$U_{j'}(s;k)-U_j(s;k)=\bigl[G_{j'}-G_j\bigr]-\bigl[C_{j'}-C_j\bigr]-\bigl[E_{j'}-E_j\bigr]
=G_{j'}-G_j\;>\;0,$$
contradicting the optimality of $j$ at $s$. Hence no available flagged
deviation improves, which is sequential optimality of the flagged component.

**What h.16 is doing, and why the sunk-cost route does not do it instead (spec MAY-11).** Drop h.16
and the middle bracket survives: date-0 optimality of $j$ gives only $G_j-G_{j'}\ge C_j-C_{j'}$,
while sunk-cost round-2 optimality needs $G_j-G_{j'}\ge0$, so the step would need
$C_{j'}(s)\le C_j(s)$ at the selected $j$. It can fail. With $C_j(s)=0.01$, $C_{j'}(s)=0.99$ and
$G_{j'}-G_j=0.5$, plan $j$ is date-0 optimal ($U_{j'}-U_j=0.5-0.98=-0.48<0$) while the round-2
deviation raises the sunk-cost continuation by $0.5$: a fixed point of $\mathcal T$ then satisfies
items (i), (iii)–(vi) of card §3 and fails item (ii) at the flagged node (the GPT end review's
arithmetic; WHERE IT FAILS 7). Nor is the one-sided clause a weaker hypothesis than h.16: h.16's
"why" note shows the deviation set is an equivalence class and that P1's hypotheses must hold
uniformly on $\Theta$, so $C_{j'}\le C_j$ imposed at every selectable $j$ *is* $C_{j'}=C_j$.
**Restating round-2 optimality against the sunk-cost continuation therefore lands on h.16, and h.16
additionally makes the two readings agree, so this step never has to adjudicate the card's
ambiguity.** The clause is vacuous on any single-Voice menu, where $\mathcal Q_j(s)$ is a singleton,
and live on any admissible menu with two Voice plans sharing a pooled path.

The converse direction is the honest part. Without h.11 — i.e. if round 2 offers the full interval
$[0,\bar b-B_j^F(s)]$ — date-0 optimality over $\mathcal J$ constrains only those round-2 orders that
appear as the flagged component of some menu element paired with the same pooled path; an order
outside that set is never compared, so a fixed point of $\mathcal T$ can fail item (ii) of card §3 at
the flagged node while satisfying every other item. **Sequential optimality of the flagged component
does not follow from A1–A7 and is not a free consequence of complete contingent plans; h.11 is *a*
sufficient condition that delivers it, and it is a restriction on the round-2 action set rather than
on the menu.** Strengthening A7 to **A7-J** does not change this: WHERE IT FAILS 2's menu may be
taken with $b^*$ strictly increasing on all of $\mathbb R$, so it satisfies A7-J and still fails
item (ii). The turn-1 statement of P1 listed "sequential optimality of the flagged component" as
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
h.14 fixes the accounting of the payoff without restricting its shape in $\hat v$. (Card §4.3's $U_j$
row, which absorbed h.14 on 2026-08-23, imposes nothing here either: it names only plan-locality and
integrability as the properties ever used, and neither is a shape restriction in $\hat v$.) At the
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
(Step 11). Flagged: Step 12 under h.11 **and h.16**. Date-0 plan optimality: $k^\star$ is a fixed point of
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
   not a PBE. This is one of the two concrete cases in which P1's claim is false as stated under
   A1–A7 alone — case 7 is the other — and it survives the strengthening of A7 to A7-J: take the
   Voice plan's $b^*$ strictly increasing on all of $\mathbb R$ and A7-J holds on the menu while
   item (ii) still fails.
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
7. **h.16 fails: two Voice plans share a pooled path at different engagement costs.** Take an
   admissible menu with Voice plans $j\ne j'$ agreeing on the pooled path up to $f_j(s)$ and
   differing only in the flagged order — then h.11's deviation set at $(j,s)$ is a genuine pair, not
   a singleton — with $C_j(s)=0.01$, $C_{j'}(s)=0.99$ and trading terms $G_{j'}-G_j=0.5$ (Step 12's
   notation). Plan $j$ is date-0 optimal, $U_{j'}-U_j=0.5-0.98=-0.48<0$, so Step 13's construction
   and Brouwer run unchanged and the fixed point satisfies items (i), (iii)–(vi) of card §3. But the
   round-2 deviator has sunk $C_j(s)=0.01$, and the deviation to $Q^F_{j'}(s)$ raises the sunk-cost
   continuation by $0.5$: item (ii) fails at the flagged node, and the object is a date-0
   equilibrium, not a PBE. This is the GPT end review's arithmetic (audit Finding 1(b)), and it is
   the second case — with case 2 — in which P1's claim is false as stated without its [ADDITION]
   hypotheses. It is **vacuous on any single-Voice menu**, the pinned pro-rata menu included, where
   $a_{j'}=a_j=1$ forces $j'=j$; that is why the paper's instance is untouched by it.

---

## LABEL CLAIMED

**CONJECTURE.** Three reasons as written on 2026-08-21; **reason 1 is sufficient on its own**, and
reasons 2 and 3 are updated below to their status at card stamp `d2ccf62` — part of each has since
been absorbed by the card, and saying so is not a label move (2026-08-25, ticket 35).

1. Card §7: a label moves only on an executed check or an independent re-derivation, never on
   prose. This document is prose. The card's ledger carries P1 at CONJECTURE and this proof does not
   touch the ledger.
2. The proof consumes hypotheses that are not card §5 assumptions — **h.11** (the round-2 action set
   is the plan-generated set) and **h.16** (continuation-cost equivalence on that set) — plus h.13
   and h.15 for the Step 20 reformulation. "Under A1–A7" was never an accurate antecedent for this
   proof, because sequential optimality of the flagged component (item (ii) of card §3) is not among
   A1–A7's consequences (Step 12, WHERE IT FAILS 2 and 7). *Status at stamp `d2ccf62`:* h.12
   ($m_0\ge0$) is now card §4.1's sign restriction and h.14 is now card §4.3's $U_j$ row, so those
   two are discharged; h.11 and h.16 are carried **descriptively in the card's P1 row itself**
   (ticket 35's amended statement), not as §5 assumptions, and A7 is cited there in its **A7-J**
   form, which is what h.7 consumes.
3. The proof cites h.9 = D1 by statement. *Status at stamp `d2ccf62`:* D1 moved to PROVED on
   2026-08-21 with both passes on file, so the inherited-label conditionality of the original reason
   3 is discharged; what P1 still inherits is D1's own hypothesis set, listed in the card's D1 row.

**The label claimed by this document is unchanged at CONJECTURE**, and reason 1 alone carries it: no
document of prose moves a label, and the two fresh passes ticket 35 requires — an adversarial
proof-read of this file and a statements-only re-derivation of the amended card row — are not this
file's to claim. The intended final label remains PROVED, conditional on those two passes.

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
| $U_j(s;k)$ | blockholder's conditional expected payoff to plan $j$ at signal $s$ under conjecture $k$; the object **defined at h.14** with the conjecture displayed | matches the frozen manuscript's blockholder utility; **never a bare $U$**. **Card gap closed 2026-08-23:** the object is now card §4.3's $U_j$ row, and h.14 transcribes it (the row cites h.14 as "displayed there in full", which the 2026-08-25 display alignment makes literally true) |
| $\mathcal C_j^{\mathrm{trade}}$ | plan $j$'s execution outlay: increments valued at the pooled prices $P_d^P$ up to the plan's last pooled date, plus $Q_j^F(s)P^F$ when $D_j=1$ (h.14) | calligraphic and always subscripted $j$ with the superscript written, so it is clear of card §4.4's $C_h$ (chord), $C_\tau/C_T$ (composition ratios) and $\mathcal C_F/\mathcal C_P$ (cells); **never a bare $C$**. Now carried by card §4.3's $U_j$ row in the same words |
| $C_j(s)$ | plan $j$'s engagement cost at signal $s$; enters $U_j$ as $a_jC_j(s)$, so plans with $a_j=0$ pay nothing (h.14) | named in card §4.4's $C$-overload note and carried by card §4.3's $U_j$ row; subscripted, never bare. **h.16** constrains it across each h.11 deviation set; card §4.3 does not say at which date it is incurred (regeneration item, Step 12) |
| $G_j(s;k)$ | the **trading terms** of Step 11's first bracket: $b_j^*(s)\mathbb E[Y\mid s,j,D=1]-P^F(\sigma_F)Q_j^F(s)$, i.e. the flagged continuation net of the engagement cost | proof-local to Steps 12 and WHERE IT FAILS 7, introduced 2026-08-25 so the cost-honest comparison has a name. Card §4.4 carries no $G$; $\mathcal G_F$ (this table) is calligraphic and is the inner-root map, a different object |
| $E_j(s;k)$ | Step 11's second bracket, the pooled-execution expectation | proof-local, same steps as $G_j$. Distinct from any card symbol; $\mathbb E$ is the expectation operator and is never subscripted by a plan |
| $\mathrm{supp}(z_d)$ | the realised support of the noise mark at the maintained $\kappa$: $\{0\}$ at $\kappa=0$, $\{-\bar z,+\bar z\}$ at $\kappa=1$, all three marks in between | roman operator on card §4.1's $z_d$ row, not a new model symbol; used only in Step 9, where the $\kappa$-boundary argument is quantified over it |
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
4. That **A7-J** (h.7) holds on a general finite menu. *Updated 2026-08-25:* satisfiability is no
   longer open — ticket 24 exhibits a menu on which A7-J holds, the pro-rata single-Voice menu with
   $b^*$ strictly increasing on all of $\mathbb R$ (`proofs/A7_construction.md` Step 7, attack
   verdict SURVIVES WITH REPAIRS), and that menu is the paper's pinned instance. What is **not**
   claimed is A7-J beyond it: this file exhibits no other menu, and card §5 records the failure
   boundary (a binding stake cap, quantized stakes, a composed target repeating values across
   Voice-plan switches, $\Omega=0$, and a target flat off the Voice region — the last leaves the
   on-path A7′ intact while breaking A7-J, on a 40-collision executed witness). Steps 6 and 10
   consume A7-J as a hypothesis and do not verify it menu by menu.
5. That h.11 holds on any particular menu, or that any menu in the calibration satisfies it.
   NUMERICAL CHECK 4 is designed to measure what it buys, not to assume it. **Nor is h.11 claimed to
   be the weakest condition delivering item (ii)** — Step 12 says why: the off-path-belief route
   permitted by card §3(vi) is untouched by Step 9's menu-only perturbation and is not analysed
   anywhere in this file. Open. *Added 2026-08-25:* the same three disclaimers attach to **h.16**.
   It is trivially true on any single-Voice menu, the pinned pro-rata menu included (the deviation
   set is a singleton), and a genuine restriction on multi-Voice menus whose Voice plans share pooled
   paths; no step verifies it there, and no menu outside the single-Voice family is exhibited
   satisfying it. h.16 is claimed to be the weakest *uniform* form of the sunk-cost route's one-sided
   condition (h.16's "why" note) — a narrower claim than weakest-overall, which is not made for
   either hypothesis.
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
13. That a belief or a price is supplied at a pooled history that is null under **every** plan
    profile. Step 9(a)–(c) names the reachable set and confines the §3(vi) limit and the §3(iv) price
    to it; at $\kappa\in\{0,1\}$ the noise support degenerates and the unreachable set is nonempty.
    No step consumes such a history (Step 9(c)) and card §3 requires nothing at one, so the assembled
    equilibrium of Step 17 is complete — but the pre-repair sentence "the limiting belief exists at
    every pooled history" is **withdrawn**, being false at the endpoints (audit Finding 1(c)).
14. That the date at which the engagement cost $C_j(s)$ is incurred has been settled. Step 12 records
    both readings — plan completion and sunk cost — and shows its conclusion survives either **under
    h.16**, which makes them numerically identical on each deviation set; dating the cost is a card
    edit and a regeneration item, not a claim of this file. Without h.16 the conclusion does *not*
    survive both (WHERE IT FAILS 7).

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

---

## Repairs applied (2026-08-25, ticket 35 / R5 — post-review P1 repair, route A)

Source: `threads/2026-08-23_gpt_end_review_audit.md` **Finding 1** (three gaps — (a) hypothesis-form
mismatch, (b) Step 12's cost gap, (c) the $\kappa=1$ tremble gap — plus the objective-display
citation nit) and **Finding 7(ii)** (the continuum sentence names the coordinate where it should name
the tuple), against `MODEL_CARD.md` stamp 2026-08-23 · `d2ccf62`. Route **A** per spec
`quality_reports/specs/2026-08-23_post-review-repairs.md` (Austin's Q4 decision): keep the general
finite-menu theorem and state the hypotheses the proof actually needs.

**What moved and what did not.** The **conclusion is unchanged** — same equilibrium object, same six
card §3 items, same $\Theta$, same Brouwer route, and now stated explicitly for the card's full
domain $\kappa\in[0,1]$ rather than restricted to $[0,1)$. Two **hypotheses are strengthened**: h.7
becomes A7-J (strictly stronger than the on-path A7′ the pre-review card row carried) and h.16 is
added. One clause of the conclusion is **made precise**: card §3(vi)'s off-path beliefs are supplied
at every *reachable* pooled history, which repairs a sentence that was false at $\kappa\in\{0,1\}$
rather than retreating from a true one. No step was renumbered; WHERE IT FAILS gains item 7 at the
end and NOT CLAIMED gains items 13–14 at the end, so every pre-existing cross-reference still
resolves. **The label is untouched: P1 remains CONJECTURE**, and ticket 35's two fresh passes — an
adversarial proof-read of this file and a statements-only re-derivation of the amended card row —
are the only things that may move it.

| Finding | Change made |
|---|---|
| **P1-R9** (Finding 1(a)) | **h.7 renamed A7-J (joint tuple injectivity)** and restated on the flagged-**pair** set $\{(j,s):D_j=1\}$, including pairs no $k\in\Theta$ selects, with the note that this is strictly stronger than A7′ and is what Step 10's *off-path* pinning consumes. The pre-review card row recorded the weaker on-path A7′ while this proof consumed the joint form — the mismatch that meant the 2026-08-21 passes covered two different statements. CLAIM's antecedent updated from "A1–A7 of card §5" to "A1–A6 together with A7 in its A7-J form". Steps 6 and 10 already read "injective on the flagged set" and are unchanged in substance. Two neighbours checked and annotated rather than changed: **WHERE IT FAILS 2** and Step 12's converse paragraph each gain one sentence recording that the counterexample menu there can be taken A7-J-satisfying ($b^*$ strictly increasing on all of $\mathbb R$), so strengthening A7 does not silently repair a failure case or make item (ii) follow from the card's assumptions after all. |
| **P1-R10** (Finding 7(ii)) | h.7's continuum sentence corrected: injectivity forces the **tuple** $(B^F,Q^F)$ to be continuum-valued, **not the coordinate $B^F$** — which on the pinned pro-rata menu is not even monotone, jumping down at every crossing-date boundary while the sum $B^F+Q^F=b^*_j(s)$ carries the separation (`proofs/A7_construction.md` Steps 8–9; `proofs/A7_attack_verdict.md` S-10, where our own attack flagged this and the card note was never amended). Card §5's A7 note already carries the corrected form. |
| **P1-R11** (Finding 1(b); spec MAY-11) | **h.16 [ADDITION] added** — continuation-cost equivalence, $C_{j'}(s)=C_j(s)$ on each h.11 deviation set — with a "Why" note deriving it, and **Step 12 rewritten cost-honestly**: the trading terms $G_j$ are named and separated from the engagement cost, the deviation's two possible continuations (plan completion, sunk cost) are displayed, and the contradiction now runs on $G_{j'}>G_j$ with the middle bracket $C_{j'}-C_j$ shown to vanish under h.16. **MAY-11 route considered and declined with a reason:** restating optimality against the sunk-cost continuation does not discharge the gap on its own — date-0 optimality gives $G_j-G_{j'}\ge C_j-C_{j'}$ where sunk-cost optimality needs $G_j-G_{j'}\ge0$, so it needs $C_{j'}\le C_j$ at the selected $j$; and since the deviation set is an equivalence class (shared path $\Rightarrow c_{j'}=c_j\Rightarrow f_{j'}=f_j$, so the relation is symmetric) and P1's hypotheses must hold uniformly on $\Theta$ (Brouwer does not say which $k^\star$ it returns), that one-sided clause collapses to h.16's equality. h.16 additionally makes the two readings *coincide*, so the step never adjudicates the card's silence on when $C_j$ is incurred. The Θ-uniformity leg is stated with its one exceptional signal named ($s=\overline s$, where $j_k(\overline s)=J$ for every $k$; immaterial, since h.16 is imposed at every $s$ regardless). Propagated to the CLAIM, Step 17(ii), **WHERE IT FAILS 7** (new, carrying the review's $0.01$-vs-$0.99$ arithmetic), NOT CLAIMED 5 and 14, and LABEL CLAIMED 2. |
| **P1-R12** (Finding 1(c)) | **Step 9 rewritten** in four parts: (a) $\mathrm{supp}(z_d)$ is displayed at $\kappa=0$, $\kappa=1$ and in between, and a pooled history is defined **reachable** when some plan and a positive-probability signal set make the *whole* history positive-probability; (b) the perturbed-posterior limit is established at every reachable history, with the denominator bound written out; (c) unreachable histories are shown to carry no card §3(vi) or §3(iv) requirement **and to be consumed by no step** (Step 11's pooled bracket and every h.11 deviation integrate over the played plan's own reachable set); (d) the false sentence is named and withdrawn. **The $\kappa=1$ route is the extension, not the restriction** — the theorem now holds on $\kappa\in[0,1]$ with both endpoints, and the $\kappa=0$ special case becomes the same sentence. Propagated to the CLAIM's belief clause (with its own "on the belief clause" note), Step 11, and NOT CLAIMED 13. The integrating measure in (b) is written $\mathrm d\Phi_s$, the NOTATION DELTA's declared signal c.d.f., so the step introduces no undeclared symbol. |
| **P1-R16** (two-pass protocol; no change of substance) | The amended card row's belief clause covered only the **pooled** layer once the reachability qualifier was added, and the row is the statements-only re-deriver's sole input. Both the row and this file's CLAIM now name the **flagged** layer explicitly: flagged-tuple beliefs are pinned by A7-J at every tuple in the image of $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$, on path and off, with no tuple outside the image arising under the round-2 action-set hypothesis. This states what Step 10 has always proved (and what Step 17(iii)/(vi) has always assembled); nothing in the proof changes. |
| **P1-R13** (Finding 1, citation nit) | **h.14's display aligned with card §4.3's $U_j$ row**: $-a_jC_j(s)$ in place of $-C_j(s)$, the $\mathcal C_j^{\mathrm{trade}}$ gloss expanded to the card's own words (increments at the pooled prices up to the last pooled date, plus $Q^F_jP^F$ when $D_j=1$), and $C_j(s)\ge0$ transcribed, so the card's "displayed there in full" is literally true. The card row was **not** edited (it is outside this ticket's edit surface; the fix is on the proof side, which the ticket permits). Step 11's display carries $-a_jC_j(s)$ with the note that $a_j=1$ on the flagged branch (h.4), so Steps 12–13 are unchanged. NOTATION DELTA rows for $U_j$, $\mathcal C_j^{\mathrm{trade}}$ and $C_j(s)$ updated; new rows for $G_j$, $E_j$ and $\mathrm{supp}(z_d)$. |
| **P1-R14** (staleness against `d2ccf62`; audit Finding 1's "not disturbed" paragraph) | **NOT CLAIMED 4 refreshed.** It said A7 satisfiability was open and a Thread 2 target; ticket 24 closed it — the pinned pro-rata single-Voice menu with globally strict $b^*$ satisfies A7-J (`proofs/A7_construction.md` Step 7). The item now disclaims what is genuinely undisclaimed: A7-J on menus beyond that one, with card §5's failure boundary quoted. |
| **P1-R15** (Finding 8, card-snapshot staleness) | **LABEL CLAIMED reasons 2 and 3 brought to stamp `d2ccf62`**, and Step 14's parenthetical with them. Reason 2 previously listed h.12 and h.14 as absent from the card; $m_0\ge0$ is now card §4.1's sign restriction and $U_j$ is now card §4.3's row, while h.11 and h.16 are carried descriptively in the card's amended P1 row rather than as §5 assumptions. Reason 3 previously called D1 a CONJECTURE; D1 moved to PROVED on 2026-08-21. **No label is moved by this row** — the section header still claims CONJECTURE, now resting on reason 1 alone (prose never moves a label; ticket 35's two fresh passes are not this file's to claim). |

**The pinned instance, clause by clause.** The paper's pro-rata single-Voice menu satisfies every
strengthened clause, so route A's repairs cost the paper's instance nothing: **A7-J** holds on it
(`proofs/A7_construction.md` Step 7 — only the Voice plan ever flags, so the flagged-pair set is
$\{(V,s)\}$, and globally strict $b^*$ separates it through the sum coordinate); **h.16** holds
trivially (on the flagged set $a_j=1$, Exit and Hold never cross $\tau$ under $b_0<\tau$, so the
deviation set is the singleton $\{V\}$ — the same fact that makes h.11's action set a singleton
there); and the **$\kappa$** repair is an extension, so no boundary clause has to be satisfied at
all, with every numerical node of `t2_p1_check` sitting at interior $\kappa$ regardless.
