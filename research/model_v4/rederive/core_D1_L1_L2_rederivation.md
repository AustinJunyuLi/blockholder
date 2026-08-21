# Independent re-derivation of D1, L1, L2 (ticket 27, Thread 2)

**Re-deriver:** Opus, ticket 27 lane.
**Card version worked against:** MODEL CARD 2026-08-21, commit `a175202`+ (the surgical-edit stamp
with the A7 note and the §4.2 A7′ row).
**Inputs used:** `research/model_v4/MODEL_CARD.md` only.
**Independence attestation:** `research/model_v4/proofs/` and `research/model_v4/threads/` were not
opened, listed for content, searched or read at any point. `draft_v2.tex` was deliberately not opened
either, to keep the notation of this file bound to card §4 alone. No `git` command was run.

## Verdict summary

| ID | Verdict | One-line reason |
|---|---|---|
| D1 | **PROVED-WITH-CHANGES** | Closes, but needs an explicit content for $\mathcal I_H$ (card §4.3 leaves it "—") and a Borel-regularity rider on $s\mapsto B_j(s,d)$ for non-Voice plans, without which the *pooled prices* in part (c) are not defined. |
| L1 | **PROVED-AS-STATED** | Closes under D1 plus the standing hypotheses; the boundary clauses are proved directly, not as limits, and the non-imputation clause is proved as a non-identification statement. |
| L2 | **PROVED-WITH-CHANGES** | Closes, but the ledger's enumerated hypothesis list (A1, A4, A5, A7-injective, §2 timing, $\Omega>0$) is **incomplete**: the derivation also uses A2 with the §4.1/§4.2 table restrictions, D1's measurability, and an explicit bidder-entry rule. A7′ is used only *almost surely* on the flagged set (a weakening, i.e. permissive). |

### By-products worth carrying to the ledger

1. **$\partial_\kappa\Omega = 0$ at fixed policies** falls out of L2 Step 2 and is not stated anywhere in
   the card. It is needed for §4.4's row $\mathcal S=(1-\Omega)\mathcal S_P$.
2. §4.4's $\mathcal S=(1-\Omega)\mathcal S_P$ **additionally needs differentiability of $M_P$ in
   $\kappa$**, which no card hypothesis supplies (AGE gives smoothness of the *outer* map only). See
   L1 Remark R1.
3. **A7′ $\Rightarrow$ on-path injectivity is a two-line argument** (L2 Step 3), because
   $B^F+Q^F=b^*_{j(s)}(s)$ by the §4.2 definition of $Q^F$. This also gives a *monotone* inverse, so
   L2 does not need the Lusin–Souslin route the A7 note mentions.
4. §4.3's $P_{\mathrm{ND}}$ row reads ambiguously ("counterfactual pooled price … no flag") but its
   own clause "$=P_{f^-}^P$ by construction" fixes it as the **not-yet-disclosed** price, not a
   never-disclosed one. D1's identity is exact under the fixing clause and would acquire an extra
   term under the other reading. See D1 Reading RD-3.

## Reading decisions (gaps in the card I had to fill to evaluate the statements)

These are declared once and used throughout; each is the minimal fill consistent with §2–§4.

- **RD-1 ($\mathcal I_H$ content).** §4.3 lists $\mathcal I_H$ "control-node information set" with
  meaning "—". Both D1 ("maps every control-node history into exactly one cell") and L2 ("the
  flagged posterior") are claims *about* $\mathcal I_H$ and cannot be evaluated without it. I take
  $\mathcal I_H$ to be the **public** information set at the control node (the bidder's own $\xi$ is
  private — otherwise §4.3's $p(\mathcal I)$ would be an indicator, not a probability), given by
  $\mathcal I_H = (\mathcal H_{f^-}^P, F, Q^F)$ on $\mathcal C_F$ and $\mathcal I_H=\mathcal H_H^P$ on
  $\mathcal C_P$, per the §2 sequence. **L2 is proved in a form that is robust to this fill** (Step 6
  sandwich), so RD-1 is load-bearing for D1's cell-map clause only.
- **RD-2 ($f^-$, $c^-$).** Trading is daily on $\{0,\dots,H\}$, so $f^- := f-1$ and $c^- := c-1$, with
  the §4.3 convention $P_{-1}^P:=\mathbb E[Y]$ covering $c=0$. D1's identity is unaffected by the
  alternative reading ("date $f$, before the filing is processed"); the $\kappa$-dependence discussion
  in L2 Step 14 is not.
- **RD-3 ($P_{\mathrm{ND}}$).** Taken as the §4.3 clause states: $P_{\mathrm{ND}}(\mathcal H^P_{f^-})
  := P^P_{f^-}$, the price at the last pre-filing history (which already contains "flag not landed
  by $f-1$"). Not a never-disclosed counterfactual.
- **RD-4 ($R_d$ index range).** $d\in\{c-1,\dots,f-1\}$, so $R_{c-1}=0$ and $R_{f-1}=R$, matching
  §4.3's $R=P^P_{f^-}-P^P_{c^-}$.
- **RD-5 (entry rule).** §4.3 gives $p(\mathcal I)$ and names $\mathsf B$ but not the rule generating
  it. I take $\mathsf B=\mathbf 1\{\xi\ge\mathsf t\}$, $\mathsf t=P+K+m_0+\pi\Delta_m-\bar S$, which is
  the rule reproducing §4.3's $p$ when $\xi\mid\mathcal I\sim N(0,\sigma_\xi^2)$. L2 Step 11 also gives
  the weaker condition under which the conclusion survives any other rule.
- **RD-6 (noise law).** §4.1 gives one law per date indexed by $\kappa$; with A1's mutual
  independence I read $z_0,\dots,z_H$ as independent with that common law, written $Q_\kappa$ for the
  law of the vector $z_{0:H}$. Nothing below uses identical distribution across dates — only that
  every $z_d$ depends on $\kappa$ and on no other primitive.
- **RD-7 (cutoff selection map).** §3(i) gives a weakly ordered cutoff vector "mapping $s$ into a
  plan"; I write that map $j(\cdot)$ and take it to be the right-continuous step function with
  breakpoints $k_1\le\dots\le k_{J-1}$. Ties and collapsed regions are permitted by §3 and change
  nothing below.

---
---

# A. D1

## CLAIM

$D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is measurable and maps every control-node history into exactly
one cell; for every Voice plan $f_j\le H\iff B_j(s,H-T)\ge\tau$; and each flagged history yields
$B^F,R_d,R,J$ with $P^F-P^P_{c^-}=R+J$.

## HYPOTHESES

1. **H1 = A1.** $v,\varepsilon,\xi$ and all $z_d$ mutually independent, variances strictly positive.
   *(Used: Step 1 for the existence of the joint law; Step 11 for prices.)*
2. **H2 = A2.** Plan menu, order-mark support, noise support and calendar horizon finite; prices and
   payoffs bounded. *(Used: Steps 1, 3, 4, 11.)*
3. **H3 = A4.** $c$ is the first date the path reaches $\tau$; the filing lands exactly at $c+T$;
   filings truthfully reveal stake and purpose; only Voice plans cross in the core. *(Used: Steps 3,
   6, 9, 10.)*
4. **H4 = A5.** Each public-history pricing map has a unique fixed point. *(Used: Step 11.)*
5. **H5 = §4.1 restrictions.** $H$ finite; $T\in\{1,\dots,H\}$; maintained $b_0<\tau$; $b_0\in[0,\bar
   b]$. *(Used: Steps 4, 8, 9, 11.)*
6. **H6 = §4.2 definitions and restrictions.** $B_j(s,-1)=b_0$; for Voice $\partial_dB_j\ge0$ and
   $\partial_sB_j\ge0$; Hold constant, Exit weakly decreasing in $d$; $c_j=\inf\{d:B_j(s,d)\ge\tau\}$
   with $+\infty$ if never; $f_j=c_j+T$; $D_j=\mathbf 1\{a_j=1,c_j<\infty,f_j\le H\}$;
   $B_j^F=B_j(s,f_j)$; $Q_j^F=b_j^*(s)-B_j^F$. *(Used: Steps 2, 3, 7, 8, 10.)*
7. **H7 = §4.3 definitions and conventions.** $\mathcal H^P_d=(X_0,\dots,X_d;\text{flag landed by
   }d)$; $P^P_{-1}:=\mathbb E[Y]$; $P_{\mathrm{ND}}:=P^P_{f^-}$ (RD-3); $R_d=P^P_d-P^P_{c^-}$,
   $R=P^P_{f^-}-P^P_{c^-}$, $J=P^F-P_{\mathrm{ND}}$. *(Used: Steps 6, 10, 11, 12, 13.)*
8. **H8 = §3(i).** A weakly ordered cutoff vector maps $s$ into a plan (RD-7). *(Used: Step 1.)*
9. **H9 (ADDED — regularity rider).** For every $j\in\mathcal J$ and $d\in\{-1,\dots,H\}$, the map
   $s\mapsto B_j(s,d)$ is Borel. For Voice this is already delivered by H6's $\partial_sB_j\ge0$ and
   for Hold by constancy; **for Exit plans the card supplies monotonicity in $d$ only**, so this is
   a genuine addition. *(Used: Step 11 only — the pooled pricing map at a history integrates over
   every type, including Exit types, so without H9 the object $P^P_d$ in part (c) is not defined.
   Part (a) and part (b) do not need H9.)*
10. **H10 (ADDED — definitional fill).** RD-1's content for $\mathcal I_H$. *(Used: Step 6.)*

## PROOF

**Step 1 (a probability space and a measurable type map).** By H1 the vector
$(v,\varepsilon,\xi,z_{0:H})$ has a joint law on a finite product of Polish spaces (the noise
coordinates take values in the finite set $\{-\bar z,0,+\bar z\}$ by §4.1, the rest in $\mathbb R$),
so all objects below are defined on one probability space. $s=v+\varepsilon$ is a sum of two
coordinates, hence Borel. By H8 and RD-7, $j(\cdot)$ is a step function with the finitely many
breakpoints $k_1\le\dots\le k_{J-1}$ (finitely many because $J<\infty$ by H2), taking values in
$\mathcal J$. A step function with finitely many breakpoints is a finite sum of indicators of
half-lines, so $j(\cdot)$ is Borel and $\{s:j(s)=j\}$ is Borel for each $j\in\mathcal J$.

**Step 2 (engagement is measurable).** $a=a_{j(s)}$ is the composition of the Borel map $j(\cdot)$
(Step 1) with the map $j\mapsto a_j$ defined on the finite set $\mathcal J$ (H6). Every map on a
finite set carrying the discrete $\sigma$-algebra is measurable, and $\mathcal J$ carries the discrete
$\sigma$-algebra by H2's finiteness. Hence $\{a=1\}$ is Borel, and it lies in $\sigma(s)$.

**Step 3 (the crossing date is well defined, unique, and measurable on the Voice region).** Fix
$j$ with $a_j=1$. By H6, $B_j(\cdot,d)$ is weakly increasing in $s$, and a weakly monotone real
function is Borel (the preimage of $[\tau,\infty)$ is an interval), so $\{s:B_j(s,d)\ge\tau\}$ is
Borel for each $d$. The calendar $\{0,\dots,H\}$ is finite (H2, H5), so
$\{c_j\le d\}=\bigcup_{d'\le d}\{s:B_j(s,d')\ge\tau\}$ is a finite union of Borel sets, hence Borel;
therefore $c_j$ is a Borel map into $\{0,\dots,H\}\cup\{+\infty\}$. Uniqueness of the value: a
nonempty subset of the finite well-ordered set $\{0,\dots,H\}$ has exactly one minimum, and by H3 $c$
*is* that first date; if the subset is empty, $c_j=+\infty$ by H6's convention. Non-Voice plans are
not treated here and are not needed: see Step 4.

**Step 4 ($D$ is measurable).** By H6, $D=1$ requires $a=1$; therefore
$$\{D=1\}=\bigcup_{j\in\mathcal J:\,a_j=1}\Big(\{s:j(s)=j\}\cap\{s:c_j(s)\le H-T\}\Big),$$
using $f_j=c_j+T\le H\iff c_j\le H-T$ together with the convention $(+\infty)+T=+\infty>H$, which is
available because $H$ is finite (H5). Each set in the union is Borel by Steps 1 and 3, and the union
is finite by H2. Hence $\{D=1\}$ is Borel, so $D$ is a measurable $\{0,1\}$-valued map. Two facts
recorded for later use: (i) every ingredient is a function of $s$ alone at a fixed cutoff policy, so
$\{D=1\}\in\sigma(s)$; (ii) measurability of $B_j(\cdot,d)$ for **non**-Voice $j$ was never invoked,
because the conjunct $a=1$ removes those plans from the union.

**Step 5 (exactly one cell).** Put $\mathcal C_F:=\{D=1\}$ and $\mathcal C_P:=\{D=0\}$. $D$ is an
indicator of a Borel event (Step 4), so it takes exactly one of the values $0,1$ at every sample
point; therefore $\mathcal C_F\cap\mathcal C_P=\emptyset$ and $\mathcal C_F\cup\mathcal C_P$ is the
whole space. This is §4.3's "exclusive and exhaustive by construction", now derived rather than
asserted.

**Step 6 (the cell assignment is a function of the *history*, not of the hidden state).** Step 5
partitions the *state* space; the claim is about control-node **histories**. By H7 each pooled
history $\mathcal H^P_d$ carries the component "flag landed by $d$", and by H10 the control-node
information set contains $\mathcal H^P$ up to the control node. By H3 the flag lands exactly at
$f=c+T$ and only through the disclosure node of §2.3, so the component "flag landed by $H$" equals
$\mathbf 1\{f\le H\}$; combining with H6's $D=\mathbf 1\{a=1,c<\infty,f\le H\}$ and with the fact
that a landed flag entails $a=1$ (H3: only Voice plans cross), that component equals $D$. Hence $D$
is measurable with respect to the control-node history, and the map (history) $\mapsto$ (cell) is a
well-defined single-valued map onto $\{\mathcal C_F,\mathcal C_P\}$. *This step is the bridge that
turns Step 5's partition of states into the claimed partition of histories; it consumes H7 and H10
and nothing else.*

**Step 7 (part (b), the direction $f_j\le H\Rightarrow B_j(s,H-T)\ge\tau$).** Let $j$ be a Voice plan
and suppose $f_j\le H$. Then $c_j=f_j-T\le H-T$ and $c_j<\infty$. By H6's definition of $c_j$ as the
first date at which the path reaches $\tau$, $B_j(s,c_j)\ge\tau$. By H6's $\partial_dB_j\ge0$ for
Voice and $c_j\le H-T$, $B_j(s,H-T)\ge B_j(s,c_j)$. Chaining the two inequalities gives
$B_j(s,H-T)\ge\tau$.

**Step 8 (part (b), the converse).** Suppose $B_j(s,H-T)\ge\tau$. By H5, $T\in\{1,\dots,H\}$, so
$H-T\in\{0,\dots,H-1\}$ is a calendar date of the model. Hence $H-T$ belongs to
$\{d\in\{0,\dots,H\}:B_j(s,d)\ge\tau\}$, which is therefore nonempty, so its minimum $c_j$ satisfies
$c_j\le H-T<\infty$ (Step 3), and $f_j=c_j+T\le H$. Steps 7 and 8 together give the equivalence
$f_j\le H\iff B_j(s,H-T)\ge\tau$ for every Voice plan. Note that the converse direction used no
monotonicity in $d$; only the forward direction did.

**Step 9 (the role of the maintained $b_0<\tau$).** By H6, $B_j(s,-1)=b_0$ for every plan, and Hold
is constant while Exit is weakly decreasing in $d$. If $b_0\ge\tau$ then for a Hold plan
$B_j(s,0)=b_0\ge\tau$, so $c_j=0<\infty$ for a plan with $a_j=0$; that contradicts H3's "only Voice
plans cross in the core". So H3 and the H6 path table are jointly satisfiable only under H5's
maintained $b_0<\tau$, which is why the card excludes a pre-existing crossing from the core rather
than treating it as a special case.

**Step 10 (the flagged history determines the objects in part (c)).** On a flagged history: the
filing date $f$ is observed, being the first date at which the "flag landed by $d$" component of H7's
history equals one (Step 6). By H3 the filing lands exactly at $c+T$ and $T$ is a known policy
parameter, so $c=f-T$ is identified from the history; hence the baseline date $c^-=c-1$ of $R_d$ and
$R$ is identified. By H3 the filing truthfully reveals the stake, so the reported $B^F$ is
$B_j(s,f_j)$ (H6). By §2.4 the flagged order $Q^F$ is submitted and priced, so it is in the
control-node history (H10).

**Step 11 (every price in part (c) is a well-defined finite real number).** For
$d\in\{0,\dots,H\}$, $P^P_d$ is the unique fixed point of the pricing map at $\mathcal H^P_d$ (H4);
that map is well defined because the joint law of $(X_{0:d},Y)$ exists — this is where **H9** is
consumed, since $X_d=q_{jd}+z_d$ with $q_{jd}=\Gamma(B_j(s,d)-B_j(s,d-1))$ must be a random variable
for *every* plan in the support, Exit plans included, and $\Gamma$ is Borel because it is ordered in
the increment (H6/§4.2). Finiteness is H2's boundedness of prices. For $d=-1$, $P^P_{-1}=\mathbb E[Y]$
by H7's convention, finite by H2. $P^F$ is the unique fixed point at the flagged information set
(H4), finite by H2. Dates: on a flagged history $c\ge0$, so $c^-=c-1\ge-1$; and $f^-=f-1=c+T-1\ge0$
because $T\ge1$ (H5). When $T=H$, Step 8 forces $c=0$ on every flagged history, so $c^-=-1$ and the
H7 convention is exactly what makes $P^P_{c^-}$ exist; the convention is therefore not decorative.

**Step 12 (the identity).** Using H7's three definitions and RD-3,
$$R+J=\big(P^P_{f^-}-P^P_{c^-}\big)+\big(P^F-P_{\mathrm{ND}}\big)
=\big(P^P_{f^-}-P^P_{c^-}\big)+\big(P^F-P^P_{f^-}\big)=P^F-P^P_{c^-}.$$
The cancellation of $P^P_{f^-}$ is legitimate because all three prices are finite real numbers
(Step 11). The identity is exact and pathwise: it uses no distributional assumption, no optimality,
and no property of $\kappa$. It is a telescoping of the same price at the same history, which is
precisely why RD-3 is load-bearing — under a "never-disclosed" reading of $P_{\mathrm{ND}}$ the
middle terms would not cancel and the identity would carry a residual
$P^P_{f^-}-P_{\mathrm{ND}}\ne0$.

**Step 13 (the run-up path).** For $d\in\{c-1,\dots,f-1\}$ (RD-4), $R_d=P^P_d-P^P_{c^-}$ is
well-defined by Step 11 and computable at the control node by Step 10, with $R_{c-1}=0$ and
$R_{f-1}=R$. Together with Steps 5, 6, 8, 10 and 12 this establishes every conjunct of the claim.
$\blacksquare$

## WHERE IT FAILS

1. **Pre-existing crossing, $b_0\ge\tau$.** Step 9: a Hold plan then has $c=0<\infty$, so H3's "only
   Voice plans cross" is false and the disclosure event stops being the model's engagement event.
   Excluded by H5's maintained $b_0<\tau$ (the card's turn-2 audit D1-O1 exclusion, which I reach
   independently).
2. **A Voice path that is not weakly increasing in $d$.** Take a plan that reaches $\tau$ at $d=2$,
   sells back below $\tau$ at $d=4$, and has $B_j(s,H-T)<\tau$ with $T=3$, $H=10$. Then $f=5\le H$ but
   $B_j(s,7)<\tau$, so Step 7's direction fails and part (b) is false. Excluded by H6's
   $\partial_dB_j\ge0$ for Voice.
3. **A flag that is not public.** If the "flag landed by $d$" component were dropped from H7's
   history, Step 6 breaks: $D$ would remain a measurable function of the *state* (Step 4) while the
   cell assignment would no longer be a function of the control-node **history**, which is what the
   claim asserts. Nothing else in the card would notice, which is why this bridge deserves an
   explicit citation.
4. **Non-Voice paths that are not Borel in $s$.** Step 11 needs H9. A pathological Exit schedule
   $B_j(\cdot,d)$ that is non-measurable in $s$ leaves $X_d$ without a law, so $P^P_d$, hence $R_d$,
   $R$ and $J$, are undefined — while parts (a) and (b) survive untouched.
5. **Continuous-time execution or intraday crossing.** If the path may reach $\tau$ strictly between
   business days, Step 3's "minimum of a nonempty subset of a finite well-ordered set" argument is
   unavailable and $c$ need not be attained. §9 already disclaims continuous time.

## LABEL CLAIMED

**Re-derivation verdict: PROVED-WITH-CHANGES.** Changes, exhaustively:

- **Added H9** (Borel regularity of $s\mapsto B_j(s,d)$ for non-Voice plans). Why: part (c)'s pooled
  prices integrate over all types. Scope: part (c) only. Cost to fix: one clause in A2 or one column
  in §4.2 — the card already supplies the property for Voice and Hold.
- **Added H10 / RD-1** (a content for $\mathcal I_H$, which §4.3 leaves as "—"). Why: the clause "maps
  every control-node history into exactly one cell" is unevaluable otherwise. Scope: Step 6 only.
- **Readings RD-2, RD-3, RD-4** fixed as declared. RD-3 is not a change (the card's own clause fixes
  it) but the row's prose invites the other reading, under which the identity is false.
- **Nothing dropped, nothing weakened.**

Card label supported: **PROVED**, once H9 and H10 are written into the card. Until then D1's part (c)
is proved under a hypothesis the card does not carry, so it should not move off CONJECTURE on the
strength of this re-derivation alone.

## NUMERICAL CHECK REQUEST

**Formulas** (per simulated or quadrature node):
- $\mathrm{err}_1=\big|\mathbf 1\{f_j\le H\}-\mathbf 1\{B_j(s,H-T)\ge\tau\}\big|$ over Voice types.
- $\mathrm{err}_2=\big|(P^F-P^P_{c^-})-(R+J)\big|$ over flagged histories.
- $\mathrm{err}_3=\big|\mathbf 1_{\mathcal C_F}+\mathbf 1_{\mathcal C_P}-1\big|$ over all histories.
- $\varrho_0=$ share of flagged histories with $c=0$, at the node $T=H$.

**Grid:** $\kappa\in\{0.1,0.3,0.5,0.7,0.9\}$, $\tau\in\{0.03,0.05,0.10\}$, $T\in\{1,5,10\}$, $H=10$,
$b_0=0$, $N=10^4$ signal draws per node (45 nodes).

**Predicted sign and magnitude:** $\max\mathrm{err}_1=0$ **exactly** (an integer comparison — any
single nonzero entry falsifies part (b), and the first place to look is a menu whose Voice paths are
not weakly increasing in $d$). $\max\mathrm{err}_3=0$ exactly. $\max\mathrm{err}_2\le10^{-10}$; the
expected magnitude is floating-point cancellation of three prices of order $|\mu_v|$, i.e.
$\approx10\,\epsilon_{\text{mach}}|\mu_v|\approx2\times10^{-15}$ at $|\mu_v|=1$ — a value above
$10^{-8}$ is diagnostic of an implementation that uses a $P_{\mathrm{ND}}$ other than $P^P_{f^-}$
(RD-3), not of numerical error. $\varrho_0=1.000$ at the $T=H=10$ node, which is the node that
exercises the $P^P_{-1}=\mathbb E[Y]$ convention; a check suite that never sets $T=H$ never tests it.

## NOTATION DELTA

Symbols used above that are not in card §4:

| Symbol | Meaning |
|---|---|
| $j(\cdot)$ | the cutoff plan-selection map of §3(i) (RD-7); the card describes it but gives it no symbol |
| $\sigma(\cdot)$ with a random-variable argument | the generated $\sigma$-algebra. The subscripted $\sigma_v,\sigma_\varepsilon,\sigma_\xi$ remain standard deviations; the two never appear in the same expression |
| $\mathrm{err}_1,\mathrm{err}_2,\mathrm{err}_3,\varrho_0,N$ | numerical-check quantities defined at their point of use |
| $\epsilon_{\text{mach}}$ | machine epsilon (numerical check only); distinct from the card's $\varepsilon$, the signal noise |

## NOT CLAIMED

- No claim that $R$, $R_d$ or $J$ is invariant to $\kappa$ (§4.3 explicitly declines this for $J$; the
  derivation above is pathwise and is silent on it).
- No claim that the crossing date or the filing date is chosen optimally, or that filing before the
  deadline can occur (§9).
- No claim for $b_0\ge\tau$, for intraday or continuous-time crossing, or for a randomised filing date.
- No claim that both cells have positive mass — that is A8, not D1. D1 holds when one cell is null.
- No claim about the blockholder's own information set, only about the public control-node history.
- No claim that $\mathcal I_H$ as filled in by RD-1 is the card's intended object; only that some fill
  is needed and that this one is the minimal fill consistent with §2 and §4.3.

---
---

# B. L1

## CLAIM

Whenever $0<\Omega<1$, $\Delta^{\mathrm{act}}=\Omega M_F+(1-\Omega)M_P$; at $\Omega=1$ it degenerates
to $\Delta^{\mathrm{act}}=M_F$ and at $\Omega=0$ to $\Delta^{\mathrm{act}}=M_P$, the null-cell average
being undefined rather than imputed.

## HYPOTHESES

1. **G1 = D1.** $D$ measurable, $\{\mathcal C_F,\mathcal C_P\}$ an exclusive and exhaustive partition.
   *(Used: Steps 3, 4.)*
2. **G2 = §4.3 definitions.** $\pi(\mathcal I)=\Pr(a=1\mid\mathcal I)\in[0,1]$;
   $p(\mathcal I)\in(0,1)$; $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$. *(Used: Steps 1, 2.)*
3. **G3 = §4.4 definitions.** $h=\pi p$; $\Delta^{\mathrm{act}}=\Delta_m\mathbb E[h(\mathcal I_H)]$;
   $M_F=\Delta_m\mathbb E[h\mid D=1]$, $M_P=\Delta_m\mathbb E[h\mid D=0]$, each defined when its cell
   has mass; $\Omega=\Pr(D=1)$. *(Used: Steps 1, 3, 6, 7.)*
4. **G4 = A5.** Each public-history pricing map has a unique fixed point, so $P(\mathcal I_H)$ is a
   pinned-down version of $\mathbb E[Y\mid\mathcal I_H]$. *(Used: Step 2.)*
5. **G5 = A2 and §4.1.** Payoffs bounded; $\Delta_m>0$ and finite. *(Used: Steps 1, 7.)*
6. **G6 = A1.** The primitives live on one probability space, so $\Pr$ and $\mathbb E$ below are
   taken under a single probability measure. *(Used: Steps 4, 5.)*

## PROOF

**Step 1 ($h$ is bounded).** By G2, $\pi\in[0,1]$ and $p\in(0,1)$, so their product satisfies
$0\le h\le1$ pointwise. Hence $h$ is bounded by 1 irrespective of G5's payoff bound.

**Step 2 ($h(\mathcal I_H)$ is a random variable).** $\pi(\mathcal I_H)=\Pr(a=1\mid\mathcal I_H)$ is a
version of a conditional probability given the $\sigma$-algebra $\mathcal I_H$, hence
$\mathcal I_H$-measurable by the definition of conditional expectation (G2). $P(\mathcal I_H)=\mathbb
E[Y\mid\mathcal I_H]$ is $\mathcal I_H$-measurable for the same reason, and G4 pins the version up to
a null set. $p$ is a composition of these with the continuous map
$x\mapsto1-\Phi\big((x+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)$ (G2), hence
$\mathcal I_H$-measurable. A product of two measurable functions is measurable, so $h(\mathcal I_H)$
is measurable. With Step 1 it is integrable.

**Step 3 (the partition and $\Omega$).** By G1, $\{D=1\}$ and $\{D=0\}$ are measurable, disjoint and
cover the space, so $\Omega=\Pr(D=1)$ is defined and $\Pr(D=0)=1-\Omega$ (G3).

**Step 4 (pointwise split).** By Step 3, at every sample point exactly one of
$\mathbf 1\{D=1\},\mathbf 1\{D=0\}$ equals 1 and the other 0, so
$h=h\,\mathbf 1\{D=1\}+h\,\mathbf 1\{D=0\}$ pointwise.

**Step 5 (integrate).** Each summand in Step 4 is bounded in absolute value by 1 (Step 1), hence
integrable on the probability space (G6). Linearity of the integral gives
$\mathbb E[h]=\mathbb E[h\mathbf 1\{D=1\}]+\mathbb E[h\mathbf 1\{D=0\}]$.

**Step 6 (interior case $0<\Omega<1$).** Both conditioning events have strictly positive probability,
so the elementary conditional expectations
$\mathbb E[h\mid D=1]:=\mathbb E[h\mathbf 1\{D=1\}]/\Omega$ and
$\mathbb E[h\mid D=0]:=\mathbb E[h\mathbf 1\{D=0\}]/(1-\Omega)$
are defined and finite (Step 1 bounds both by 1). Substituting
$\mathbb E[h\mathbf 1\{D=1\}]=\Omega\,\mathbb E[h\mid D=1]$ and
$\mathbb E[h\mathbf 1\{D=0\}]=(1-\Omega)\mathbb E[h\mid D=0]$ into Step 5:
$\mathbb E[h]=\Omega\,\mathbb E[h\mid D=1]+(1-\Omega)\mathbb E[h\mid D=0]$.

**Step 7 (scale to premia).** Multiply Step 6 by $\Delta_m$, which is a strictly positive finite
constant (G5), and read off G3's definitions:
$$\Delta^{\mathrm{act}}=\Delta_m\mathbb E[h]=\Omega\,\Delta_m\mathbb E[h\mid D=1]+(1-\Omega)\Delta_m
\mathbb E[h\mid D=0]=\Omega M_F+(1-\Omega)M_P.$$

**Step 8 (degenerate case $\Omega=1$).** Then $\Pr(D=0)=0$, and by Step 1
$\big|\mathbb E[h\mathbf 1\{D=0\}]\big|\le\mathbb E[\mathbf 1\{D=0\}]=\Pr(D=0)=0$, so that term of
Step 5 vanishes: $\mathbb E[h]=\mathbb E[h\mathbf 1\{D=1\}]=\Omega\,\mathbb E[h\mid D=1]=\mathbb
E[h\mid D=1]$, the middle equality being Step 6's definition, which is available because
$\Omega=1>0$. Multiplying by $\Delta_m$ (G5): $\Delta^{\mathrm{act}}=M_F$.

**Step 9 (at $\Omega=1$ the pooled average is not merely unavailable, it is unidentified).** $M_P$
would require dividing by $\Pr(D=0)=0$, so the elementary definition of Step 6 does not apply. The
$\sigma$-algebra route does not rescue it either: let $\mathcal D:=\sigma(D)$, whose atoms are
$\{D=1\}$ and $\{D=0\}$. For any real $x$, the function
$\Delta_m\mathbb E[h\mid D=1]\,\mathbf 1\{D=1\}+x\,\mathbf 1\{D=0\}$ is $\mathcal D$-measurable and
integrates to $\Delta_m\mathbb E[h\mathbf 1_A]$ over every $A\in\mathcal D$ (the two candidate
functions differ only on the null set $\{D=0\}$), so it is a version of
$\Delta_m\mathbb E[h\mid\mathcal D]$. Every $x$ is therefore consistent with the law: no value of
$M_P$ is determined by the model. The card's phrase "undefined rather than imputed" is exactly this
non-identification, and the correct statement at $\Omega=1$ is Step 8's one-term equation, not the
two-term equation of Step 7 with a term stipulated to be zero.

**Step 10 (degenerate case $\Omega=0$).** Mirror of Steps 8–9 with the roles of the cells exchanged:
$\big|\mathbb E[h\mathbf 1\{D=1\}]\big|\le\Pr(D=1)=0$, so $\mathbb E[h]=\mathbb E[h\mid D=0]$ and
$\Delta^{\mathrm{act}}=M_P$, while $M_F$ is unidentified by the argument of Step 9. $\blacksquare$

**Remark R1 (what the decomposition does *not* yet deliver).** §4.4's row
$\mathcal S=(1-\Omega)\mathcal S_P$ does not follow from Step 7 alone. Differentiating Step 7 in
$\kappa$ at fixed policies needs three ingredients: (i) $\partial_\kappa M_F=0$ — supplied by L2;
(ii) $\partial_\kappa\Omega=0$ — **not stated in the card**, but derived here as L2 Step 2; and
(iii) differentiability of $M_P$ in $\kappa$ — **supplied by no card hypothesis** (AGE assumes
smoothness of the outer map $\mathcal T$, not of the pooled cell average). Item (iii) is a real gap
in the chain from L1+L2 to §4.4's sensitivity row and should be added as a hypothesis or discharged
from A5's continuity plus a dominated-convergence argument over the finite pooled-history space.

## WHERE IT FAILS

1. **Imputing $M_P:=0$ at $\Omega=1$.** Step 9 shows any value is consistent with the law. The damage
   is not to the level (the term is multiplied by $1-\Omega=0$) but to any statement carrying
   $M_P$ *outside* the product — for instance a decomposition of $\Delta^{\mathrm{act}}$ into "weight
   effect $\times$ composition effect" (§4.4's $W_\tau,W_T,C_\tau,C_T$) evaluated at or near a
   corner, where the imputed number is a free parameter driving the reported ratio.
2. **Applying the identity to the wrong partition.** $\Omega=\Pr(a=1)\,\omega_a$ (§4.4), so
   $\Omega\ne\Pr(a=1)$ whenever $\omega_a<1$. Averaging $h$ over $\{a=1\}$ and $\{a=0\}$ and weighting
   by $\Pr(a=1)$ gives a different, generally unequal, decomposition: the engaged-but-undisclosed
   types sit in $\mathcal C_P$, not $\mathcal C_F$. Step 4's split is only valid for the $D$-partition
   that D1 constructs.
3. **A non-measurable disclosure event.** If D1's Step 4 failed — for example under a filing date
   randomised by a device that is not in the public history — then $\Omega$ is not defined and Step 5
   has no content. L1 is a corollary of D1 in the strict sense that it inherits every one of D1's
   failure modes.
4. **Unbounded $h$.** Not possible here (Step 1), but recorded because Steps 5, 8 and 10 all use
   boundedness rather than integrability; a version of the model in which $h$ is a premium *level*
   rather than a probability product would need an integrability hypothesis.

## LABEL CLAIMED

**Re-derivation verdict: PROVED-AS-STATED.** No hypothesis added, dropped or weakened. The derivation
uses D1 (a card result), the standing A1/A2/A5, and the §4.3–§4.4 definitions — all card-supplied.
Two points of interpretation, neither a change: (i) at the corners the card's word "degenerates"
is read as asserting the one-term equation directly, which is what Steps 8 and 10 prove, rather than
the two-term equation evaluated with a convention; (ii) "undefined rather than imputed" is read as
non-identification, which is what Step 9 proves. Card label supported: **PROVED**, subject to the
protocol's separate proof-read leg.

## NUMERICAL CHECK REQUEST

**Formula:** $\mathrm{err}_4=\big|\Delta^{\mathrm{act}}-\big(\Omega M_F+(1-\Omega)M_P\big)\big|$,
with all four quantities recomputed from the same solved equilibrium object (not re-simulated
separately), plus the corner diagnostic $\mathrm{err}_5=\big|\Delta^{\mathrm{act}}-M_F\big|$ at a node
forced to $\Omega=1$.

**Grid:** the D1 grid restricted to nodes with $0.01\le\Omega\le0.99$; plus one corner node built by
taking an all-Voice menu with $\tau$ low enough that every type in the support crosses by $H-T$
(which by D1 Step 8 is $\tau\le\inf_sB_j(s,H-T)$), giving $\Omega=1$ exactly. Integrate over $s$ by
deterministic quadrature (201-node Gauss–Hermite), not Monte Carlo, so that sampling noise cannot
mask a real violation.

**Predicted sign and magnitude:** $\mathrm{err}_4$ identically zero and **two-sided** — it is an
algebraic identity, so the predicted value is $0$ up to quadrature and solver tolerance
($\le10^{-10}$ with quadrature; $O(N^{-1/2})\Delta_m\approx10^{-2}\Delta_m$ at $N=10^4$ under Monte
Carlo, which is why quadrature is requested). At the corner node: $\mathrm{err}_5\le10^{-10}$ **and**
the implementation must return a missing value for $M_P$; an implementation returning $M_P=0$ passes
$\mathrm{err}_4$ while violating the clause the lemma actually adds, so the check must assert
`isnan(M_P)` and not merely a numerical tolerance.

## NOTATION DELTA

| Symbol | Meaning |
|---|---|
| $\mathcal D$ | the $\sigma$-algebra $\sigma(D)$ generated by the disclosure indicator, used only in Step 9 |
| $\mathrm{err}_4,\mathrm{err}_5$ | numerical-check quantities defined at their point of use |
| $A$ | a generic element of $\mathcal D$ in Step 9 (proof-local; not the card's $A_0,A_{1/2},A_1$ chord weights, which never appear in this section) |

## NOT CLAIMED

- No comparative statics of any kind: L1 is an identity at a fixed parameter point.
- No claim that $\Omega$, $M_F$ or $M_P$ is continuous or differentiable in $\kappa$, $\tau$ or $T$.
- No claim of §4.4's $\mathcal S=(1-\Omega)\mathcal S_P$ — see Remark R1 for the two further
  ingredients that claim needs, one of which the card does not supply.
- No claim about the sign of $M_F-M_P$, and in particular no claim that flagged histories carry the
  higher engagement-related premium.
- No claim that the corners $\Omega\in\{0,1\}$ are reachable in equilibrium; A8 excludes them, and
  Steps 8–10 are stated for completeness of the ledger's wording.

---
---

# C. L2

## CLAIM

At fixed cutoff and execution policies, under A1, A4, A5, A7 in its injective (on-path) form, the
no-feedback timing of §2, and $\Omega>0$: $(B^F,Q^F,a=1)$ makes the pre-filing pooled history
conditionally independent of $(v,s,\xi)$ on the flagged set, so the flagged posterior, price, entry
probability and $M_F$ are invariant to $\kappa$.

## HYPOTHESES

1. **K1 = A1.** $v,\varepsilon,\xi$ and all $z_d$ mutually independent. *(Used: Steps 2, 7, 10, 11.)*
2. **K2 = A2 with the §4.1/§4.2 table restrictions** — finite plan menu, finite calendar, finite noise
   support, bounded payoffs; for Voice $\partial_sB_j\ge0$; $\Gamma$ ordered in the increment.
   *(Used: Steps 3, 4, 13. **This hypothesis is not in the ledger's enumerated list for L2.**)*
3. **K3 = A4.** Only Voice plans cross; the filing lands exactly at $c+T$; filings truthfully reveal
   stake and purpose. *(Used: Steps 3, 6, 9.)*
4. **K4 = A5.** Unique pricing fixed point at each public history. *(Used: Steps 5, 11.)*
5. **K5 = A7′ / A7 injective on-path.** On the flagged set, at the cutoff vector in force, the
   composed terminal target $s\mapsto b^*_{j(s)}(s)$ is strictly increasing, which is the §4.2 row
   version of A7's injective form. **Used only $\Pr$-almost surely on $\mathcal C_F$** — see the
   verdict. *(Used: Step 3.)*
6. **K6 = §2 no-feedback timing.** No within-window re-optimisation: $B_j(s,d)$, $q_{jd}(s)$ and
   $Q_j^F$ are functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone. *(Used: Steps 1, 4.)*
7. **K7 = $\Omega>0$.** *(Used: Steps 3, 13.)*
8. **K8 = fixed cutoff and execution policies.** The cutoff vector $k$, the menu $\{B_j\}$ and
   $\Gamma$ are held fixed as $\kappa$ varies. *(Used: Steps 1, 2, 3.)*
9. **K9 = D1.** $\mathcal C_F$ measurable, $\mathcal C_F\in\sigma(s)$, $D=1\Rightarrow a=1$, the flag
   status public. *(Used: Steps 2, 6, 9. **Not in the ledger's enumerated list for L2.**)*
10. **K10 = RD-1, RD-5, RD-6.** A content for $\mathcal I_H$, an entry rule generating $\mathsf B$,
    and the noise law $Q_\kappa$. *(Used: Steps 6, 11. The conclusion is made robust to RD-1 in
    Step 6.)*

## PROOF

**Step 1 (where $\kappa$ lives).** By K8 and K6, every policy object — $j=j(s)$, the path
$B_{j}(s,\cdot)$, the marks $q_{jd}(s)$, the terminal target $b^*_j(s)$, the crossing date $c_j(s)$,
the filing date $f_j(s)$, the indicator $D_j(s)$, the filing stake $B^F_j(s)$ and the flagged order
$Q^F_j(s)$ — is a function of $(s;\tau,T)$ alone: K6 removes any dependence on realised order flow or
prices, and K8 removes any dependence on $\kappa$ through re-optimised cutoffs. Inspecting §4.1's
primitive list, $\kappa$ appears in exactly one place, the law of the ternary noise mark
($\Pr(z_d=0)=1-\kappa$, $\Pr(z_d=\pm\bar z)=\kappa/2$); the laws of $v,\varepsilon,\xi$ and the
constants $(\bar S,K,m_0,m_1,\Delta_V,\bar z,\tau,T,H,b_0,\bar b,\sigma_\xi)$ carry no $\kappa$.
Write $Q_\kappa$ for the law of $z_{0:H}$ (RD-6). **Conclusion: at fixed policies, $\kappa$ enters the
model only through $Q_\kappa$.**

**Step 2 (the flagged set and its mass are $\kappa$-free).** By K9, $\mathcal C_F=\{D=1\}$ is
measurable and lies in $\sigma(s)$; by Step 1 it is one fixed Borel subset of the $s$-axis, the same
subset for every $\kappa$. By K1 and §4.1, $s=v+\varepsilon\sim N(\mu_v,\sigma_v^2+\sigma_\varepsilon^2)$,
a law free of $\kappa$ because $z$ enters neither $v$ nor $\varepsilon$. Hence
$\Omega=\Pr(s\in\mathcal C_F)$ is the same number for every $\kappa$. **By-product:
$\partial_\kappa\Omega=0$ at fixed policies** — used in L1 Remark R1 and in §4.4's sensitivity row,
and stated nowhere in the card.

**Step 3 ($\mathsf S_F$ pins down $s$, with a measurable inverse).** Write
$\mathsf S_F=(B^F,Q^F,a{=}1)$, that is $F$ augmented by $Q^F$. On $\mathcal C_F$ we have $a=1$ (K9's
$D=1\Rightarrow a=1$, and K3's "only Voice plans cross"), so the third coordinate is uninformative,
and by the §4.2 definition $Q^F_j=b^*_j(s)-B^F_j$,
$$B^F_{j(s)}(s)+Q^F_{j(s)}(s)=b^*_{j(s)}(s).$$
By K5 the right-hand side is strictly increasing in $s$ on $\mathcal C_F$, hence injective there.
Therefore the first two coordinates of $\mathsf S_F$ determine $b^*_{j(s)}(s)$, which determines $s$,
which determines $j=j(s)$ (K8). Write $\iota_F$ for the inverse map, $s=\iota_F(B^F+Q^F)$ on
$\mathcal C_F$. $\iota_F$ is itself strictly increasing on the image $b^*_{j(\cdot)}(\mathcal C_F)$,
and a monotone real function on a Borel set is Borel (the preimage of an interval is the intersection
of an interval with the domain), so $\iota_F$ is measurable. By K7 the set on which this holds has
strictly positive probability, so the statement is not vacuous. **Conclusion: restricted to
$\mathcal C_F$, $\sigma(\mathsf S_F)=\sigma(s)$ up to $\Pr$-null sets.**
*Sub-remark:* this is a two-line derivation of A7's injective form from the §4.2 A7′ row, and it
delivers a monotone inverse directly, so L2 does not need the Lusin–Souslin route named in the card's
A7 note. That route remains the fallback if A7 is assumed in the abstract injective form without
monotonicity: an injective Borel map between Polish spaces has Borel image and Borel inverse on it.

**Step 4 (the pre-filing pooled history is a noise transform indexed by $(j,s)$).** Define
$$\Upsilon_{j,s}(z_{0:H}):=\Big(\big(q_{j0}(s)+z_0,\dots,q_{j,f_j(s)-1}(s)+z_{f_j(s)-1}\big);\ \text{flag
not landed by }f_j(s)-1\Big),$$
so that $\mathcal H^P:=\mathcal H^P_{f^-}=\Upsilon_{j(s),s}(z_{0:H})$ pointwise on $\mathcal C_F$
(§4.3's history definition, RD-2). The indexing by $(j,s)$ alone is exactly K6: with within-window
re-optimisation the marks would depend on realised $X_{0:d-1}$, hence on past noise, and no such
indexing would exist. Joint measurability in $(s,z_{0:H})$: $f_{j(s)}(s)$ takes finitely many values
(K2's finite calendar), and on each of the finitely many level sets $\{f_{j(s)}(s)=t\}$ — measurable
by K9 — the map is $(s,z)\mapsto(q_{j(s)d}(s)+z_d)_{d<t}$, which is measurable because
$q_{jd}=\Gamma\big(B_j(\cdot,d)-B_j(\cdot,d-1)\big)$ composes a Borel function (K2: $B_j(\cdot,d)$
weakly increasing in $s$ on the Voice region, and only Voice plans reach $\mathcal C_F$ by K3) with
$\Gamma$, which is Borel because it is ordered in the increment (K2). Patching finitely many
measurable restrictions gives a measurable map. The second component, "flag not landed by
$f_j(s)-1$", is a deterministic function of $s$ (Step 1) and so carries no information beyond $s$.

**Step 5 (observed prices enlarge nothing).** By K4 each pooled price $P^P_d$ is the unique fixed
point of the pricing map at $\mathcal H^P_d$, hence a function of $\mathcal H^P_d$; likewise $P^F$ is
a function of the flagged information set. Adjoining the value of a function of a $\sigma$-algebra's
generator to that $\sigma$-algebra does not enlarge it. Therefore prices may be ignored when
computing the information content of $\mathcal I_H$.

**Step 6 (information sandwich — the step that makes the result robust to RD-1).** On $\mathcal C_F$,
$$\sigma(s)\cap\mathcal C_F\ \subseteq\ \mathcal I_H\ \subseteq\ \sigma(s,z_{0:H})\cap\mathcal C_F.$$
*Left inclusion:* by §2.3–2.4 the filing reveals $F=(B^F,a{=}1)$ and the flagged order $Q^F$ is
submitted and priced, so $\mathsf S_F$ is in $\mathcal I_H$ (K10/RD-1); by Step 3, $\mathsf S_F$
recovers $s$; and $\mathcal C_F\in\sigma(s)$ (Step 2), so restricting to $\mathcal C_F$ is itself a
$\sigma(s)$-operation. *Right inclusion:* every component of $\mathcal I_H$ — pooled order flow, flag
status, filing content, $Q^F$, and prices — is a measurable function of $(s,z_{0:H})$ by Steps 1, 4
and 5. Everything below uses only this sandwich, so the conclusion holds for **any** fill of RD-1
satisfying it, including the wider fill in which post-filing pooled flow is also observed at the
control node.

**Step 7 (a freezing lemma).** Let $\mathcal G$ be a $\sigma$-algebra with $z_{0:H}$ independent of
$\mathcal G$, let $S$ be $\mathcal G$-measurable, and let $u_4(x,\zeta)$ be bounded and jointly
measurable. Put $\bar u_4(x):=\int u_4(x,\zeta)\,Q_\kappa(\mathrm d\zeta)$. Then
$\mathbb E[u_4(S,z_{0:H})\mid\mathcal G]=\bar u_4(S)$.
*Proof:* for a product form $u_4(x,\zeta)=u_1(x)u_2(\zeta)$,
$\mathbb E[u_1(S)u_2(z)\mid\mathcal G]=u_1(S)\mathbb E[u_2(z)\mid\mathcal G]=u_1(S)\mathbb E[u_2(z)]
=\bar u_4(S)$, pulling out the $\mathcal G$-measurable factor and using independence. The product
forms generate the product $\sigma$-algebra and are closed under multiplication; both sides of the
asserted equality are linear in $u_4$ and stable under bounded monotone limits, so the monotone class
theorem extends the equality to every bounded jointly measurable $u_4$. $\square$

**Step 8 (the conditional independence).** By Step 3, on $\mathcal C_F$ conditioning on
$\sigma(\mathsf S_F)$ is conditioning on $\sigma(s)$, so the claim to prove is
$$\mathcal H^P\ \perp\ \Xi\ \big|\ s\qquad\text{on }\mathcal C_F,\qquad \Xi:=(v,s,\xi).$$
Given $s$, the coordinate $s$ of $\Xi$ is degenerate, so it suffices to show, for bounded measurable
$u_1$ on the pre-filing-history space and bounded measurable $u_2$ on $\mathbb R^2$,
$$\mathbb E\big[u_1(\mathcal H^P)\,u_2(v,\xi)\mid s\big]=\mathbb E\big[u_1(\mathcal H^P)\mid
s\big]\cdot\mathbb E\big[u_2(v,\xi)\mid s\big]\quad\text{a.s. on }\mathcal C_F.$$
Write $u_4(x,\zeta):=u_1(\Upsilon_{j(x),x}(\zeta))$, bounded and jointly measurable by Step 4, so that
$u_1(\mathcal H^P)=u_4(s,z_{0:H})$. By K1, $z_{0:H}\perp(v,\varepsilon,\xi)$, and $(v,s,\xi)$ is a
measurable function of $(v,\varepsilon,\xi)$, hence $z_{0:H}\perp\Xi$. Apply Step 7 with
$\mathcal G=\sigma(v,s,\xi)$ and $S=s$:
$$\mathbb E\big[u_4(s,z)u_2(v,\xi)\mid v,s,\xi\big]=u_2(v,\xi)\,\bar u_4(s).$$
Take $\mathbb E[\,\cdot\mid s]$ of both sides (tower property) and pull out the $\sigma(s)$-measurable
factor $\bar u_4(s)$:
$\mathbb E[u_1u_2\mid s]=\bar u_4(s)\,\mathbb E[u_2\mid s]$. Setting $u_2\equiv1$ in the same display
gives $\mathbb E[u_1\mid s]=\bar u_4(s)$, and substituting yields the product form. This is the first
conjunct of the claim: **conditional on $(B^F,Q^F,a{=}1)$, the pre-filing pooled history is
independent of $(v,s,\xi)$ on the flagged set.** Note where the apparent paradox dissolves —
unconditionally $\mathcal H^P$ is strongly dependent on $s$ through the marks $q_{jd}(s)$; the
conditioning event removes exactly that dependence by pinning $s$ (Step 3), leaving $\Upsilon$'s only
remaining randomness, the noise.

**Step 9 (the flagged posterior).** Let $u_3$ be bounded, $\mathcal I_H$-measurable and supported on
$\mathcal C_F$. By Step 6's right inclusion and the Doob–Dynkin lemma, $u_3=u_5(s,z_{0:H})$ for some
bounded jointly measurable $u_5$. For bounded measurable $u_2$ on $\mathbb R^2$, the computation of
Step 8 with $u_5$ in place of $u_4$ gives
$\mathbb E[u_2u_3]=\mathbb E\big[\bar u_5(s)\,\mathbb E[u_2\mid s]\big]$, while the tower property
gives $\mathbb E\big[u_3\,\mathbb E[u_2\mid s]\big]=\mathbb E\big[\mathbb E[u_3\mid s]\,\mathbb
E[u_2\mid s]\big]=\mathbb E\big[\bar u_5(s)\mathbb E[u_2\mid s]\big]$ (Step 7 gives
$\mathbb E[u_3\mid s]=\bar u_5(s)$). Hence $\mathbb E[u_2u_3]=\mathbb E\big[\mathbb E[u_2\mid
s]\,u_3\big]$ for every such $u_3$. Since $\mathbb E[u_2\mid s]$ is $\sigma(s)$-measurable and
$\sigma(s)\cap\mathcal C_F\subseteq\mathcal I_H$ (Step 6, left inclusion), $\mathbb E[u_2\mid s]$ is a
version of $\mathbb E[u_2\mid\mathcal I_H]$ on $\mathcal C_F$:
$$\mathbb E[u_2(v,\xi)\mid\mathcal I_H]=\mathbb E[u_2(v,\xi)\mid s]\quad\text{a.s. on }\mathcal C_F.$$
The extension from bounded $u_2$ to integrable $u_2$ (needed for $u_2(v,\xi)=v$ in Step 11) follows by
applying the display to $u_2^{(n)}:=\max(-n,\min(n,u_2))$ and passing to the limit under conditional
dominated convergence, the dominating variable being $|u_2|$, integrable because $v$ is Gaussian
(K1). Separately, $\pi(\mathcal I_H)=\Pr(a=1\mid\mathcal I_H)=1$ on $\mathcal C_F$, because
$\mathcal C_F\subseteq\{a=1\}$ (K9, K3) and $\mathcal C_F\in\mathcal I_H$ (D1 Step 6).

**Step 10 (the posterior is $\kappa$-free).** By Step 9 the conditional law of $(v,\xi)$ given
$\mathcal I_H$ on $\mathcal C_F$ equals its conditional law given $s$. By K1 and §4.1 that law is
$v\mid s\sim N\big(\mu_v+\beta(s-\mu_v),(1-\beta)\sigma_v^2\big)$ with
$\beta=\sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)$, and $\xi\mid s\sim N(0,\sigma_\xi^2)$
independent of $v$ (K1 gives $\xi\perp(v,\varepsilon)$, hence $\xi\perp(v,s)$). None of these depend
on $\kappa$ (Step 1: $\kappa$ lives only in $Q_\kappa$, and no $z_d$ appears in $(v,s,\xi)$). With
$\pi=1$ (Step 9), the **flagged posterior over $(v,a,\xi)$ is a $\kappa$-free function of $s$**, hence
by Step 3 a $\kappa$-free function of $\mathsf S_F$. *(First conclusion of the claim.)*

**Step 11 (the flagged price).** By §4.3, $P^F$ solves the inner fixed point $P=\mathbb E[Y\mid
\mathcal I_H]$ with $Y=(1-\mathsf B)(v+a\Delta_V)+\mathsf B(P+m_0+a\Delta_m)$. On $\mathcal C_F$,
$a=1$ and $\pi=1$ (Step 9). Under RD-5, $\mathsf B=\mathbf 1\{\xi\ge\mathsf t\}$ with
$\mathsf t=P+K+m_0+\Delta_m-\bar S$, and by Step 10 $\xi\mid\mathcal I_H\sim N(0,\sigma_\xi^2)$
independent of $v$, so $\Pr(\mathsf B=1\mid\mathcal I_H)=1-\Phi(\mathsf t/\sigma_\xi)=p$, reproducing
§4.3's entry-probability formula, and
$$\mathbb E[Y\mid\mathcal I_H]=\big(1-p\big)\Big(\mathbb E[v\mid\mathcal I_H]+\Delta_V\Big)+p\,\big(P+m_0+\Delta_m\big),$$
where the factorisation of the first term uses $\mathsf B\perp v\mid\mathcal I_H$, itself a
consequence of $\xi\perp v\mid\mathcal I_H$ (Step 10) and of $\mathsf B$ being a function of $\xi$ and
of $\mathcal I_H$-measurable quantities. By Step 9, $\mathbb E[v\mid\mathcal I_H]=\mathbb E[v\mid
s]=\mu_v+\beta(s-\mu_v)$. Therefore the fixed-point equation reads
$$P=\big(1-p(P)\big)\Big(\mu_v+\beta(s-\mu_v)+\Delta_V\Big)+p(P)\big(P+m_0+\Delta_m\big),\qquad
p(P)=1-\Phi\big((P+K+m_0+\Delta_m-\bar S)/\sigma_\xi\big),$$
whose data are the single number $\mathbb E[v\mid s]$ and the parameters
$(\Delta_V,m_0,\Delta_m,K,\bar S,\sigma_\xi)$. By Step 10 and §4.1 none of these depends on $\kappa$.
By K4 the fixed point is unique, so the solution is a function of the data alone; equal data give
equal solutions. Hence **$P^F$ on $\mathcal C_F$ is a $\kappa$-free function of $s$**, which by Step 3
is a $\kappa$-free function of $\mathsf S_F$. *(Second conclusion.)*
*Robustness to RD-5:* the argument never used the threshold form as such. It used only (i)
$\Pr(\mathsf B=1\mid\mathcal I_H)=p(\mathcal I_H)$ and (ii) $\mathsf B\perp v\mid\mathcal I_H$. Any
entry rule with those two properties leaves $\mathbb E[Y\mid\mathcal I_H]$ a function of
$\big(\mathbb E[v\mid\mathcal I_H],\pi,P\big)$ and the parameters, and the conclusion stands.

**Step 12 (the entry probability).** By §4.3 with $\pi=1$ (Step 9),
$p(\mathcal I_H)=1-\Phi\big((P^F+K+m_0+\Delta_m-\bar S)/\sigma_\xi\big)$ on $\mathcal C_F$. Every
argument is $\kappa$-free (Step 11 for $P^F$, §4.1 for the constants) and $\Phi$ does not depend on
$\kappa$. Hence the flagged entry probability is a $\kappa$-free function of $s$; write $p_F(s)$ for
it, a measurable function by Step 11 (composition of the monotone $s\mapsto\mathbb E[v\mid s]$, the
fixed-point solution, and $\Phi$) and bounded in $(0,1)$ by §4.3. *(Third conclusion.)*

**Step 13 ($M_F$).** By §4.4, $h=\pi p$, so $h=p_F(s)$ on $\mathcal C_F$ (Steps 9, 12). By K7 and
L1 Step 6's elementary conditional expectation,
$$M_F=\Delta_m\,\mathbb E[h\mid D=1]=\frac{\Delta_m\,\mathbb E\big[p_F(s)\,\mathbf
1\{s\in\mathcal C_F\}\big]}{\Omega}.$$
The numerator integrates a $\kappa$-free bounded measurable function (Step 12) over a $\kappa$-free
Borel set (Step 2) against the $\kappa$-free law of $s$ (Step 2); it is finite because $p_F\le1$ (K2's
boundedness is not even needed). The denominator is $\kappa$-free and strictly positive (Step 2, K7).
Hence **$M_F$ is invariant to $\kappa$**. *(Fourth conclusion.)* $\blacksquare$

**Step 14 (consistency check, not part of the claim).** Nothing above asserts $\kappa$-invariance of
$P^P_{f^-}$. Indeed $P^P_{f^-}=\mathbb E[Y\mid\mathcal H^P_{f^-}]$ conditions on order flow whose law
is $Q_\kappa$-dependent, so it moves with $\kappa$ in general; since $J=P^F-P^P_{f^-}$ (§4.3, RD-3)
and $\partial_\kappa P^F=0$ on the flagged set (Step 11), wherever the derivative exists
$\partial_\kappa J=-\partial_\kappa P^P_{f^-}$. This reproduces §4.3's refusal to claim
$\kappa$-invariance of $J$ and is a good falsification target for the numerical check below: a run in
which $J$ comes out $\kappa$-invariant indicates the pooled price is not being recomputed.

## WHERE IT FAILS

1. **A7 in the weak wording only.** Suppose two flagged types $(j,s)$ and $(j',s')$, $s\ne s'$, share
   the same $(B^F,Q^F,1)$ — for instance two Voice plans with the same terminal target and the same
   filing-date stake but different intra-window front-loading, so
   $\big(q_{jd}(s)\big)_d\ne\big(q_{j'd}(s')\big)_d$. Then Step 3 fails, $\sigma(\mathsf S_F)\subsetneq
   \sigma(s)$ on $\mathcal C_F$, and the pre-filing flow remains informative about which type filed,
   hence about $v$. The flagged posterior then weights the two types by likelihoods computed under
   $Q_\kappa$, so it moves with $\kappa$: raising $\kappa$ blurs the flow and pushes the posterior
   towards the prior mix. Every later step falls with it. This is precisely why the injective form and
   not the weak wording is the hypothesis.
2. **Within-window re-optimisation (feedback).** If the blockholder revises the remaining path after
   observing $X_{0:d}$, then $B^F$ and $Q^F$ become functions of $(s,z_{0:f})$. Step 4's indexing by
   $(j,s)$ is unavailable, and Step 3's inversion recovers not $s$ but a mixture of $s$ and realised
   noise, so conditioning on $\mathsf S_F$ leaves residual $\kappa$-dependent uncertainty about $s$.
   Concretely, a "buy more if the price has not moved" rule makes a large $B^F$ evidence of low
   $\kappa$-driven price impact rather than of a high signal.
3. **A noisy flagged round.** If $Q^F$ were pooled with noise rather than observed
   (§9 explicitly disclaims this case), $\mathsf S_F$ is not in $\mathcal I_H$, Step 6's left
   inclusion fails, and the flagged price conditions on a $Q_\kappa$-blurred order — $\kappa$ then
   enters $P^F$ directly.
4. **$\Omega=0$.** Step 3's conclusion is vacuous, Step 13's denominator vanishes, and $M_F$ is
   unidentified by L1 Step 9. K7 is not a technicality: it is what makes "on-path" meaningful.
5. **Endogenous cutoffs, i.e. dropping K8.** In equilibrium $k=k(\kappa)$, so $j(\cdot)$, the flagged
   set $\mathcal C_F$ and hence $\Omega$ and $M_F$ all move with $\kappa$ through the outer map. L2 is
   a fixed-policy statement and gives no equilibrium invariance; that is C1's territory.
6. **Off-path flagged tuples.** For a tuple $(B^F,Q^F,1)$ of zero probability, beliefs come from
   §3(vi)'s limits of full-support perturbations, and nothing above forces those limits to be
   $\kappa$-free. The claim is on-path only.

## LABEL CLAIMED

**Re-derivation verdict: PROVED-WITH-CHANGES.** Changes, exhaustively:

- **Weakened (permissive): K5 / A7′ is used only $\Pr$-almost surely on $\mathcal C_F$.** Step 3 needs
  injectivity off a null set, because every later step is an almost-sure statement about conditional
  expectations. This is weaker than §5's literal "injective on the flagged set", so it cannot break
  the result; it is recorded because it is the exact form the proof consumes, and because it is the
  form that makes the card's "on-path (positive-probability flagged tuples)" wording coherent when
  $B^F$ is continuum-valued — with a continuum-valued $B^F$ no individual flagged tuple has positive
  probability, so "positive-probability tuples" must be read as "almost surely on a
  positive-probability set", not as "on a set of atoms".
- **Added: K2 (A2 together with the §4.1/§4.2 table restrictions).** The ledger's enumerated list for
  L2 omits it, but Steps 3, 4 and 13 use the finite calendar, the finite menu, Voice monotonicity in
  $s$, and $\Gamma$'s orderedness to get measurability of $q_{jd}(\cdot)$, of $\Upsilon$, and of
  $\iota_F$. Without some such regularity the conditional expectations in Steps 8–9 are not defined.
- **Added: K9 (D1).** The ledger's list omits it; Steps 2, 6 and 9 use $\mathcal C_F$'s measurability,
  $\mathcal C_F\in\sigma(s)$, the implication $D=1\Rightarrow a=1$, and the public flag.
- **Added: K10 (RD-1 and RD-5).** A content for $\mathcal I_H$ and an entry rule. The RD-1 dependence
  is neutralised by Step 6's sandwich, so the conclusion holds for any admissible fill; the RD-5
  dependence is neutralised by Step 11's robustness remark, so the conclusion holds for any entry rule
  with the two named properties.
- **Nothing dropped.**

The substance closes: given A7′ at a fixed cutoff policy with $\Omega>0$, the four invariance
conclusions follow with no gap I could not justify. The changes are bookkeeping about which
hypotheses the ledger row should enumerate, not repairs to the argument. Card label supported:
**PROVED**, once the ledger row for L2 is amended to read "under A1, A2, A4, A5, A7′ (on-path,
a.s.), D1, the no-feedback timing of §2, fixed cutoff and execution policies, and $\Omega>0$".

## NUMERICAL CHECK REQUEST

**Formulas** (all at fixed $(k,\text{menu},\Gamma)$, recomputing every object from scratch at each
$\kappa$):
- $\mathcal D_F:=\max_\kappa\big|M_F(\kappa)-M_F(0.5)\big|$ — the target.
- $\mathcal D_\Omega:=\max_\kappa\big|\Omega(\kappa)-\Omega(0.5)\big|$ — the Step 2 by-product.
- $\mathcal D_{P}^{F}:=\max_\kappa\max_{s\in\mathcal C_F}\big|P^F(s;\kappa)-P^F(s;0.5)\big|$ — the
  Step 11 conclusion, checked pointwise rather than in the average, so that a sign-cancelling error
  cannot hide inside $M_F$.
- **Placebo 1** $\mathcal D_P:=\max_\kappa\big|M_P(\kappa)-M_P(0.5)\big|$.
- **Placebo 2** $\mathcal D_J:=\max_\kappa\big|J(s_0;\kappa)-J(s_0;0.5)\big|$ at one fixed flagged
  signal $s_0$.

**Grid:** $\kappa\in\{0.05,0.10,\dots,0.95\}$ (19 nodes) $\times$ $\tau\in\{0.03,0.05,0.10\}$
$\times$ $T\in\{1,5,10\}$, $H=10$; integrate over $s$ by 201-node Gauss–Hermite quadrature, not Monte
Carlo — with $N=10^4$ draws the sampling error $O(N^{-1/2})\Delta_m\approx10^{-2}\Delta_m$ is three
orders of magnitude larger than the effect being tested, so a Monte-Carlo version of this check cannot
distinguish invariance from a small violation.

**Predicted sign and magnitude:**
- $\mathcal D_F=0$, $\mathcal D_\Omega=0$, $\mathcal D_P^F=0$, each up to the pricing solver's own
  convergence tolerance (the card names no tolerance; use the solver's, and assert
  $\le10^{-6}$). The prediction is exact zero, not a small number: these are *identical* computations
  at different $\kappa$, so any monotone drift in $\kappa$ — of any magnitude — falsifies the lemma
  rather than indicating numerical noise.
- **Placebo 1: $\mathcal D_P>0$ strictly**, with magnitude of order
  $\Delta_m\max_\kappa|A'_\kappa|\cdot|C_h(\bar\pi)|\times0.9$ (the $\kappa$-span of the grid), and
  with $\partial_\kappa M_P\le0$ under A($\tau$)'s maintained $C_h(\bar\pi)\le0$. If $\mathcal D_P$
  also returns at solver tolerance, the check is **uninformative rather than confirmatory** — it means
  the calibration has $\bar\pi\approx0$ so that nothing moves with $\kappa$ anywhere, and the grid must
  be rebuilt with $\bar\pi$ bounded away from zero before $\mathcal D_F=0$ carries any evidential
  weight.
- **Placebo 2: $\mathcal D_J>0$ strictly**, with $\partial_\kappa J=-\partial_\kappa P^P_{f^-}$
  (Step 14). $\mathcal D_J=0$ indicates the pooled price is being cached rather than recomputed.

## NOTATION DELTA

| Symbol | Meaning |
|---|---|
| $j(\cdot)$ | the §3(i) cutoff plan-selection map (RD-7) |
| $Q_\kappa$ | the law of the noise vector $z_{0:H}$ (RD-6); the only place $\kappa$ enters the model at fixed policies |
| $\iota_F$ | the inverse of $s\mapsto b^*_{j(s)}(s)$ on the flagged set, sanctioned as free by §4.6 |
| $u_1,u_2$ | proof-local bounded test functions, sanctioned by §4.6 (never a bare $u$): $u_1$ on the pre-filing-history space, $u_2$ on $\mathbb R^2$ with arguments $(v,\xi)$ |
| $u_3,u_4,u_5,\bar u_4,\bar u_5$ | further proof-local test functions in the same family; $\bar u_4(x):=\int u_4(x,\zeta)Q_\kappa(\mathrm d\zeta)$ |
| $\mathcal G$, $S$ | the generic $\sigma$-algebra and the generic measurable argument of the Step 7 freezing lemma (proof-local; $S$ is instantiated at $s$ and is not §4.1's $\bar S$) |
| $\mathsf t$ | the bidder's entry threshold in $\xi$ (RD-5), $\mathsf t=P+K+m_0+\pi\Delta_m-\bar S$ |
| $p_F(\cdot)$ | the flagged entry probability as a function of $s$ (Step 12) |
| $\sigma(\cdot)$ with a random-variable argument | the generated $\sigma$-algebra; the subscripted $\sigma_v,\sigma_\varepsilon,\sigma_\xi$ remain standard deviations |
| $\Phi$ | the $N(0,1)$ cumulative distribution function, as used implicitly in §4.3's $p(\mathcal I)$ |
| $\mathcal D_F,\mathcal D_\Omega,\mathcal D_P^F,\mathcal D_P,\mathcal D_J,s_0$ | numerical-check quantities defined at their point of use |

Card symbols reused exactly as §4.6 rules them: $\Xi=(v,s,\xi)$, $\Upsilon_{j,s}$,
$\mathsf S_F=(B^F,Q^F,a{=}1)$ introduced once as "$F$ augmented by $Q^F$", $\mathcal H^P$ as shorthand
for $\mathcal H^P_{f^-}$ with the subscript written at first use (Step 4), $z_{0:H}$. Not used:
$\mathsf Z$ (dropped by §4.6), bare $W$, bare $G$, bare $\psi$, bare $\lambda$, bare $u$.

## NOT CLAIMED

- **Nothing about equilibrium.** The result is at fixed cutoff and execution policies. With
  $k=k(\kappa)$ every conclusion can fail, including $\partial_\kappa\Omega=0$.
- **Nothing about $J$, $R$, $R_d$ or $P^P$.** Step 14 points the other way for $J$.
- **Nothing off path.** §3(vi)'s limit beliefs at zero-probability flagged tuples are untouched.
- **Nothing about the satisfiability of A7′** beyond Step 3's observation that A7′ implies the on-path
  injective form in two lines. Whether a menu satisfying A7′ exists, and whether such a menu is
  incentive-compatible, is not addressed here — I did not open the construction on file.
- **No invariance in $\tau$ or $T$.** $M_F$ is invariant to $\kappa$ only; changing $\tau$ or $T$ moves
  the flagged set $\mathcal C_F$ itself (Step 2), so $M_F$ moves with them.
- **No claim that $M_F$ is differentiable in anything**, and therefore no claim of §4.4's
  $\mathcal S=(1-\Omega)\mathcal S_P$; see L1 Remark R1 for the missing ingredient.
- **No uniqueness of equilibrium**, and no claim that the fixed policies used here are the ones an
  equilibrium selects.

---
---

# D. Consolidated findings for the ledger

1. **D1's hypothesis list should carry a Borel-regularity rider** on $s\mapsto B_j(s,d)$ for every
   plan (not only Voice and Hold, which §4.2 already covers). Without it, part (c)'s pooled prices are
   undefined. Parts (a) and (b) are unaffected.
2. **§4.3's $\mathcal I_H$ row is empty ("—") and two ledger statements are claims about it.** D1's
   cell-map clause and L2's posterior clause both need a content. L2 has been proved here in a form
   robust to the fill (Step 6); D1's cell-map clause has not, and cannot be, because it *is* a claim
   about histories.
3. **L2's ledger row under-enumerates its hypotheses.** It should read: A1, **A2 with the §4.1/§4.2
   table restrictions**, A4, A5, A7′ (on-path, almost surely), **D1**, the no-feedback timing of §2,
   fixed cutoff and execution policies, and $\Omega>0$.
4. **$\partial_\kappa\Omega=0$ at fixed policies is a free by-product** (L2 Step 2) and is currently
   asserted nowhere; §4.4's $\mathcal S=(1-\Omega)\mathcal S_P$ row needs it.
5. **§4.4's $\mathcal S=(1-\Omega)\mathcal S_P$ row also needs differentiability of $M_P$ in
   $\kappa$**, which no card hypothesis supplies (L1 Remark R1). This is the one genuinely open item
   this re-derivation turned up outside the three target statements.
6. **A7′ $\Rightarrow$ on-path injectivity in two lines** (L2 Step 3), via $B^F+Q^F=b^*_{j(s)}(s)$,
   with a monotone — therefore Borel — inverse. The Lusin–Souslin appeal in the A7 note is a fallback,
   not a requirement, under A7′.
7. **§4.3's $P_{\mathrm{ND}}$ row should say "the not-yet-disclosed price at $f^-$", not
   "counterfactual … no flag".** Under the never-disclosed reading D1's identity acquires a residual
   term. The row's own "$=P^P_{f^-}$ by construction" clause already settles it, but the prose invites
   the wrong reading and the identity is the paper's price-path anchor.
