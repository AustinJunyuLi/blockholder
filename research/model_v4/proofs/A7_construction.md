# A7 satisfiability — the on-path construction (ticket 24, T2d)

Author: Fable (session model), 2026-08-21, per the ADR-0008 grant (the hardest theory
bits go to Fable). Written against `MODEL_CARD.md` stamp 2026-08-20 · `0c9185b`
(ledger unchanged at HEAD `42ef47a`). Spec: `threads/thread1_msg3.md` §1 (the
L2-R1 block) and ticket 24. Status: **awaiting the ticket-24 Opus adversarial
attack**; survives → the card's A7 note and §4.2 patch row are updated as
proposed in §CLAIM (iv) below. Not a ledger row; no label moves here.

## CLAIM

Four parts.

**(i) Tuple equivalence.** On the flagged set, the flagged tuple
$\mathsf S_F = (B^F, Q^F, a{=}1)$ (the filing message $F$ augmented by the flagged
order $Q^F$) is informationally equivalent to $(B^F,\, b_j^*(s),\, a{=}1)$: the map
between them is a linear bijection, and in particular the sum $B^F + Q^F$ reveals
the terminal target $b_j^*(s)$ exactly.

**(ii) On-path sufficiency of composed-target strictness (A7′).** Fix a cutoff
policy $s \mapsto j(s)$ (L2's fixed-policy setting) and let
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
one Voice family with strictly increasing continuous terminal target) satisfies
A7′ for every $(\tau, T)$ with $b_0 < \tau$, and is conformant with every card
§4.2 row. Hence A7, in its on-path injective form, is **satisfiable** — the
stack's largest open risk (turn-2 audit L2-R1, msg3 §1) is closed at the level
of existence of a qualifying menu.

**(iv) The card's §4.2 patch must be replaced, not merely weakened.** The patch
("on the flagged set $s \mapsto (B_j^F, b_j^*)$ strictly increasing for Voice")
implies A7′ but is strictly stronger — and the pro-rata menu **violates** it:
$B^F$ is generically non-monotone in $s$, with a downward jump at every
crossing-date boundary (numeric witness in Step 9). Proposed card edits:

- §4.2 `B_j(s,d)` row, replace the strict-monotonicity sentence with: "On the
  flagged set the **composed terminal target** $s \mapsto b^*_{j(s)}(s)$ must be
  strictly increasing (hypothesis A7′, `proofs/A7_construction.md`); strictness
  of $B^F$ is not required and fails generically at crossing-date jumps."
- §5 A7 note, append: "A7′ + a fixed cutoff policy deliver the injective form
  on path with an explicit continuous inverse; a satisfying menu exists
  (pro-rata; `proofs/A7_construction.md`), so injective A7 is satisfiable. The
  failure boundary: a binding stake cap, quantized stakes, or a composed target
  that repeats values across Voice-plan switches."

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
   $f_j \le H \iff B_j(s, H-T) \ge \tau$.

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
inverse is continuous on it. No appeal to Lusin–Souslin is needed (compare
turn-2 audit L2-O1 — here the inverse is exhibited, not merely granted).

**Step 4 (A7′ ⟹ the identification clause — CLAIM ii, second clause).** By
hypotheses 2 and 5, on $\{D = 1\}$ the tuple $\mathsf S_F$ is a Borel function
of $s$ alone, and $\{D = 1\} = \{s \in S_{\mathrm{fl}}\}$ is an $s$-event. Hence
$\sigma(\mathsf S_F, \mathbf 1\{D=1\}) \subseteq \sigma(s) \subseteq
\sigma(v, s, \xi)$. By hypothesis 3, $z_{0:H}$ is independent of $(v,s,\xi)$,
hence of $\sigma(\mathsf S_F, \mathbf 1\{D=1\})$. So conditional on
$(\mathsf S_F, D=1)$, $z_{0:H}$ has its unconditional law. Moreover, writing
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
[b_0, \bar b)$, continuous, weakly increasing everywhere and strictly increasing
on the Voice region $[k_{J-1}, \infty)$, with $b^*(s) > b_0$ there. The menu:

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
stake.

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

**Step 7 (A7′ holds on the pro-rata menu).** On $S_{\mathrm{fl}}$ the policy
selects the single Voice plan (Step 2 plus Step 5's menu: Exit and Hold never
cross, so never flag), so $b^{\circ}(s) = b^*(s)$, which is strictly increasing
on the Voice region $\supseteq S_{\mathrm{fl}}$ by Step 5's choice of $b^*$.
A7′ holds. By Steps 3–4, the on-path injective form of A7 holds on this menu.
This proves CLAIM (iii).

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
A7′, per CLAIM (iv). A7′ is also implied by the patch (strictness of the
$b_j^*$ coordinate is strictness of the composed target on the single Voice
plan), so the replacement is a strict weakening that all previously conformant
menus survive.

**Step 10 (consistency with D1-R2 — continuum-valued $B^F$).** On the pro-rata
menu, $b^*$ is continuous and strictly increasing on $S_{\mathrm{fl}}$, so on
each $c$-constant interval $B^F$ ranges over a nondegenerate interval:
$B^F$ is continuum-valued, exactly as D1 repair 2 requires (an injective map
out of a continuum of signals cannot land in a finite set — turn-2 audit,
locked findings D1-R2/L2-R1). The pooled alphabet stays finite (hypothesis 2's
$q_{jd}(s) = \Gamma(\cdot)$ coarsens increments to finitely many marks; A2)
while the filing reveals the exact stake — the two resolutions coexist by
design. And A5's measurable-selection reading over the flagged continuum is
strictly easier here: the flagged tuples are parametrized continuously by
$s \in S_{\mathrm{fl}}$ with a continuous inverse (Step 3), so the selected
pricing fixed points can be chosen continuous in $s$.

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
   the grid's $b^*$ values are pairwise distinct — trivially arrangeable, but
   it must be checked, not assumed.
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

Menu-level joint injectivity of $(j,s) \mapsto (B_j^F, Q_j^F, a_j)$ over all
plan–signal pairs (only the on-path composed form, which is what L2's
fixed-policy setting consumes); anything about off-path tuples (the conditional
law is pinned only up to null sets, as L2 already hedges); that A7′ is
necessary outside the pro-rata family (Step 8's necessity is family-specific;
in general the minimal condition is bare injectivity of
$s \mapsto (B^F, Q^F)$ on $S_{\mathrm{fl}}$, which lacks a primitive menu
reading); equilibrium existence or optimality of the cutoff policy on this
menu (P1's burden); that the flagged region is nonempty (A8's burden);
κ-invariance itself (L2's conclusion, not re-proved here); any uniqueness.
