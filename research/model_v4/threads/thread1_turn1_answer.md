# Thread 1 — BUILD · Model Card v4.0 and Theorem Stack

The bundle fixes the architecture: one pooled trading round, the disclosure flag lands or does not land, then one flagged round followed by the bidder’s decision. The disclosure rule must contain the threshold margin (\tau) and the window margin (T) as primitives, while the stake at filing, run-up path, and filing-day jump must be endogenous model objects.  

The model below also treats the O-1 finding as a binding fact: window tightening did **not** attenuate liquidity-sensitivity in the previous framework when disclosed mass was below approximately (0.29); the reported ratios were (1.06), (1.19), and (1.14), with attenuation appearing only at disclosed mass (0.50). The new theorem therefore gives a condition for the window margin, not a global sign. 

## 1. Source-mandated elements and new design choices

### 1.1 Elements fixed by the bundle

1. The disclosure rule is the market’s **partition**, not an auxiliary disclosure indicator appended to an otherwise static trading game.
2. The threshold margin and window margin enter separately.
3. The run-up path and filing-day jump (J) are distinct objects.
4. The flagged cell’s control-node price and bidder entry must be directly (\kappa)-invariant.
5. The distinction between a structural partition and positive probability in both cells must remain explicit.
6. Existence should reuse the Gaussian signal, ordered cutoff, competitive-pricing fixed point, and outer Brouwer machinery from draft_v2. 
7. No global window-margin attenuation result may be claimed.

### 1.2 New design choices made here

These choices are not specified by the source bundle; they are introduced explicitly to close the model.

**Design choice 1: fixed control horizon.**
The bidder makes its decision at a fixed business-day horizon (H). A threshold crossing at day (c) produces a filing at (c+T). The control node is flagged exactly when (c+T\le H). This makes (T) a genuine legal-time primitive rather than a disclosure probability.

**Design choice 2: one strategic pooled round with a finite calendar clock.**
The blockholder chooses a complete pooled execution plan once. That plan unfolds over business-day observation dates (d=0,\ldots,H), allowing the model to define a daily run-up path. There is no within-window reoptimization. Thus the business-day observations do not create additional strategic rounds.

**Design choice 3: complete contingent plans.**
A plan specifies the pooled stake path, engagement choice, and the order to be submitted if the flag lands. A finite ordered plan menu preserves the draft_v2 cutoff/Brouwer machinery.

**Design choice 4: filing sufficiency at the control node.**
The filing reveals stake and purpose, and the flagged-round order is separately observed. The pair consisting of stake at filing and the flagged-round order identifies the informed component of the blockholder’s plan. This is the assumption that delivers direct flagged-cell (\kappa)-invariance.

These choices can later be relaxed in named extensions. In particular, strategic filing before the deadline, noisy flagged-round trading, and continuous-time execution remain outside the core model.

---

# 2. The model card

## 2.1 Position and object

The model studies how liquidity changes bidder entry and the expected takeover premium when the disclosure rule partitions control-node histories into a flagged cell and a pooled cell.

The primary control-outcome object is the expected engagement-related premium

[
\Delta^{\mathrm{act}}(\kappa,\tau,T),
]

and the primary price-path objects are:

[
\text{run-up path},\qquad
\text{cumulative run-up }R,\qquad
\text{filing-day jump }J.
]

A lower (\tau) is a tighter threshold margin. A lower (T) is a tighter window margin.

---

## 2.2 Players and uncertainty

There are four risk-neutral players:

1. one blockholder with an initial stake (b_0);
2. competitive market makers;
3. noise traders;
4. one potential bidder.

The target’s standalone value is

[
v\sim N(\mu_v,\sigma_v^2).
]

The blockholder observes

[
s=v+\varepsilon,
\qquad
\varepsilon\sim N(0,\sigma_\varepsilon^2),
]

with (v) and (\varepsilon) independent. Hence

[
\mathbb E[v\mid s]
==================

\mu_v+\lambda_s(s-\mu_v),
\qquad
\lambda_s
=========

\frac{\sigma_v^2}
{\sigma_v^2+\sigma_\varepsilon^2}.
]

The bidder privately observes

[
\xi\sim N(0,\sigma_\xi^2),
]

independently of (v,s), and all noise trades.

---

## 2.3 Complete contingent plans

The blockholder chooses a plan

[
j\in\mathcal J={1,\ldots,J}.
]

The plan menu is finite and ordered from least to most aggressive. It may contain Exit and Hold plans and one or more Voice plans. Quiet voice and Public voice are not separate primitive actions: they are realized legal statuses of a Voice plan under the rule.

Each plan (j) specifies:

[
a_j\in{0,1},
]

where (a_j=1) means engagement;

[
B_j(s,d)\in[0,\bar b],
]

the cumulative stake that would be held at business day (d) if the plan remained pooled;

[
b_j^*(s)=B_j(s,H),
]

the plan’s terminal target stake;

and

[
Q_j^F(s;\tau,T),
]

the order prescribed in the flagged round.

For a Voice plan:

[
a_j=1,
\qquad
B_j(s,d+1)\ge B_j(s,d),
\qquad
\frac{\partial B_j(s,d)}{\partial s}\ge 0.
]

For Exit and Hold, (a_j=0). Hold has a constant stake path; Exit has a weakly decreasing path.

The pooled execution path is chosen once at the beginning of the model. The flagged-round component is a contingent action of the same complete plan and must be sequentially optimal if the flag lands.

---

## 2.4 The business-day execution clock

The calendar contains dates

[
d=0,1,\ldots,H.
]

The legal filing window is

[
T\in{1,\ldots,H}.
]

The empirical comparison (10\to5) is therefore represented directly as a change in this primitive rather than as a change in a disclosure probability.

For a Voice plan, define the threshold-crossing date

[
c_j(s;\tau)
===========

\inf{d\in{0,\ldots,H}:B_j(s,d)\ge\tau}.
]

If the plan never crosses by (H), set

[
c_j(s;\tau)=+\infty.
]

The legal filing date is

[
f_j(s;\tau,T)
=============

c_j(s;\tau)+T.
]

The filing lands before the control decision exactly when

[
f_j(s;\tau,T)\le H.
]

An equivalent condition is that the stake path has reached the threshold by (H-T):

[
f_j(s;\tau,T)\le H
\quad\Longleftrightarrow\quad
B_j(s,H-T)\ge\tau.
]

This equivalence is useful because it makes both margins transparent:

[
\tau\downarrow
\quad\Rightarrow\quad
\text{more plans satisfy }B_j(s,H-T)\ge\tau,
]

and

[
T\downarrow
\quad\Rightarrow\quad
H-T\uparrow
\quad\Rightarrow\quad
\text{more plans have crossed in time to file}.
]

---

## 2.5 The disclosure flag and the partition

The disclosure indicator is

[
D_j(s;\tau,T)
=============

\mathbf 1
\left{
a_j=1,;
c_j(s;\tau)<\infty,;
f_j(s;\tau,T)\le H
\right}.
]

Thus the control-node partition is

[
\mathcal C_F(\tau,T)
====================

{(j,s,\mathbf z):D_j(s;\tau,T)=1},
]

and

[
\mathcal C_P(\tau,T)
====================

{(j,s,\mathbf z):D_j(s;\tau,T)=0}.
]

The partition exists for every parameter configuration because (D) is defined for every realized history.

Both cells have positive equilibrium probability only under the separate interiority condition

[
0<\Omega(\kappa,\tau,T)<1,
\qquad
\Omega(\kappa,\tau,T)
=====================

\Pr(D=1).
]

Thus:

* existence of the partition is structural;
* positive cell mass is an equilibrium property.

This preserves the distinction required by the source: the rule can define a partition even when one cell is off path. 

---

## 2.6 Stake at filing and the flagged-round order

For a flagged history, the stake at filing is

[
B_j^F(s;\tau,T)
===============

B_j!\left(s,f_j(s;\tau,T)\right).
]

This is an equilibrium object because it is generated jointly by:

[
\text{the chosen execution plan},
\quad
s,
\quad
\tau,
\quad
T.
]

The flagged-round order is

[
Q_j^F(s;\tau,T)
===============

b_j^*(s)-B_j^F(s;\tau,T).
]

The core assumes

[
Q_j^F\ge0
]

for Voice plans. A shorter window generally gives

[
B_j^F(s;\tau,T')
\le
B_j^F(s;\tau,T)
\qquad
\text{when }T'<T,
]

and therefore shifts more of the target accumulation into the flagged round:

[
Q_j^F(s;\tau,T')
\ge
Q_j^F(s;\tau,T).
]

This is the model counterpart of “moving trading from before the flag to after the flag.”

---

## 2.7 Pooled order flow and liquidity

The informed component of day-(d) pooled trading is

[
q_{jd}(s)
=========

\psi!\left(
B_j(s,d)-B_j(s,d-1)
\right),
]

where (\psi) is a finite ordered coarsening map. The convention is

[
B_j(s,-1)=b_0.
]

The noise order is

[
z_d\in{-\bar z,0,+\bar z},
]

with

[
\Pr(z_d=0)=1-\kappa,
\qquad
\Pr(z_d=+\bar z)
================

# \Pr(z_d=-\bar z)

\frac{\kappa}{2}.
]

The model’s liquidity variable is therefore exactly the source-defined noise-trading intensity (\kappa).

Observed pooled order flow is

[
X_d=q_{jd}(s)+z_d.
]

The pooled public history at date (d) is

[
\mathcal H_d^P
==============

\left(
X_0,\ldots,X_d;
\text{ whether a flag has landed by }d
\right).
]

The finite coarsening (\psi), finite calendar, and ternary noise preserve finite public histories and keep the pricing layer tractable.

---

## 2.8 The two strategic rounds

### Round 1: pooled trading

Nature draws (v,s). The blockholder chooses a complete plan (j). Its pooled execution path unfolds until either:

[
f_j(s;\tau,T),
]

when the flag lands, or

[
H,
]

when the bidder makes its decision while the history remains pooled.

Market makers observe (\mathcal H_d^P) and set competitive pooled prices

[
P_d^P
=====

\mathbb E[Y\mid\mathcal H_d^P].
]

There is no within-window strategic revision of the pooled execution plan.

### Disclosure node

If

[
D=1,
]

the disclosure flag reveals:

[
F=(B^F,a=1).
]

If

[
D=0,
]

no stake or purpose is publicly revealed before the control decision.

### Round 2: flagged trading and bidder decision

If (D=1), the blockholder submits the flagged-round order

[
Q^F.
]

The market observes (F) and (Q^F), sets the flagged price (P^F), and the bidder then decides whether to enter.

If (D=0), there is no flagged round before the decision; the bidder acts on the pooled history.

This is the required sequence:

[
\boxed{
\text{pooled round}
;\longrightarrow;
\text{flag or no flag}
;\longrightarrow;
\text{flagged round if applicable}
;\longrightarrow;
\text{bidder decision}.
}
]

---

## 2.9 Bidder entry and terminal value

For any control-node information set (\mathcal I), define

[
\pi(\mathcal I)
===============

\Pr(a=1\mid\mathcal I).
]

The bidder enters when

[
\bar S+\xi-K-P(\mathcal I)
-\left[m_0+\pi(\mathcal I)\Delta_m\right]
\ge0,
]

where

[
\Delta_m=m_1-m_0>0
]

is the premium wedge.

The entry probability is

[
p(\mathcal I)
=============

1-\Phi
\left(
\frac{
P(\mathcal I)+K+m_0+\pi(\mathcal I)\Delta_m-\bar S
}{
\sigma_\xi
}
\right).
]

Let (\mathsf B\in{0,1}) denote bidder entry. The shareholder payoff is

[
Y
=

(1-\mathsf B)(v+a\Delta_V)
+
\mathsf B\left(P(\mathcal I)+m_0+a\Delta_m\right),
]

where (\Delta_V\ge0) is the expected non-takeover value created by successful engagement.

The competitive control-node price solves

[
P(\mathcal I)
=============

\mathbb E[Y\mid\mathcal I].
]

This is the inner pricing fixed point. Its uniqueness is maintained under the pricing contraction hypothesis stated below.

---

## 2.10 Blockholder payoff

For plan (j), let

[
\mathcal C_j^{\mathrm{trade}}
]

denote the sum of pooled and, when applicable, flagged-round acquisition expenditures.

Let

[
C_j(s)\ge0
]

be the engagement and execution cost, with (C_j(s)=0) for non-Voice plans.

The blockholder’s conditional expected payoff is

[
U_j(s)
======

\mathbb E
\left[
b_j^*(s)Y
---------

## \mathcal C_j^{\mathrm{trade}}

C_j(s)
\mid s,j
\right].
]

The core imposes increasing differences between (s) and plan aggressiveness. The finite plan menu can therefore be represented by weakly ordered signal cutoffs.

---

## 2.11 Run-up path, cumulative run-up, and filing-day jump

Consider a flagged history with crossing date

[
c=c_j(s;\tau)
]

and filing date

[
f=c+T.
]

Let

[
P_{c^-}^P
]

be the pooled price immediately before the trigger-date order.

The run-up path is

[
R_d
===

P_d^P-P_{c^-}^P,
\qquad
d=c,\ldots,f^-.
]

The cumulative run-up is

[
R
=

P_{f^-}^P-P_{c^-}^P.
]

Let

[
P_{\mathrm{ND}}(\mathcal H_{f^-}^P)
]

be the counterfactual pooled price at the same realized pooled order-flow history if the disclosure flag did not land. By construction,

[
P_{\mathrm{ND}}(\mathcal H_{f^-}^P)
===================================

P_{f^-}^P.
]

After the filing and flagged-round order, the flagged price is

[
P^F
===

P(F,Q^F).
]

The filing-day jump is

[
J
=

## P^F

P_{\mathrm{ND}}(\mathcal H_{f^-}^P).
]

Therefore the timing split is the accounting identity

[
P^F-P_{c^-}^P
=============

R+J.
]

This adopts the required same-order-flow counterfactual definition of (J). 

The model does **not** impose that (J) is (\kappa)-invariant. Even when (P^F) is directly (\kappa)-invariant, the counterfactual pooled price can depend on (\kappa), so (J) can move with liquidity.

---

## 2.12 Premium objects and cell decomposition

Define the reduced engagement-premium kernel

[
h(\mathcal I)
=============

\pi(\mathcal I)p(\mathcal I).
]

The expected engagement-related premium is

[
\Delta^{\mathrm{act}}
=====================

\Delta_m,
\mathbb E[h(\mathcal I_H)].
]

Let

[
M_F
===

\Delta_m,
\mathbb E[h(\mathcal I_H)\mid D=1],
]

and

[
M_P
===

\Delta_m,
\mathbb E[h(\mathcal I_H)\mid D=0].
]

Let

[
\Omega=\Pr(D=1)
]

denote the unconditional flagged-cell weight. Then

[
\Delta^{\mathrm{act}}
=====================

\Omega M_F
+
(1-\Omega)M_P.
]

The empirically calibrated disclosed-engagement share is a different object:

[
\omega
======

\Pr(D=1\mid a=1).
]

The distinction matters:

[
\Omega
======

\Pr(a=1),\omega
]

when (D=1) implies engagement.

The fixed-policy liquidity-sensitivity is

[
\mathcal S(\kappa,\tau,T)
=========================

\left|
\partial_\kappa
\Delta^{\mathrm{act}}
\right|.
]

The pooled-cell liquidity-sensitivity is

[
\mathcal S_P(\kappa,\tau,T)
===========================

\left|
\partial_\kappa M_P
\right|.
]

Under flagged-cell invariance and fixed plan cutoffs,

[
\mathcal S
==========

(1-\Omega)\mathcal S_P.
]

---

## 2.13 Equilibrium notion

A **cutoff perfect Bayesian equilibrium** consists of:

1. a weakly ordered cutoff vector

   [
   k=(k_1,\ldots,k_{J-1}),
   \qquad
   k_1\le\cdots\le k_{J-1},
   ]

   mapping the blockholder’s signal into a complete contingent plan;

2. sequentially optimal pooled and flagged components of each selected plan;

3. Bayes-consistent beliefs after every on-path pooled and flagged history;

4. competitive pooled and flagged prices satisfying the corresponding pricing fixed points;

5. the bidder-entry rule above;

6. consistent beliefs at zero-probability histories obtained by limits of full-support perturbations.

Weak inequalities permit action regions to collapse, including a collapsed Hold region.

For a proposed cutoff vector (k), solve the finite collection of inner price fixed points and compute the blockholder’s adjacent-plan indifference cutoffs. This defines the outer best-response map

[
\mathcal T(k;\vartheta),
]

where (\vartheta) collects model parameters. An equilibrium cutoff vector satisfies

[
k=\mathcal T(k;\vartheta).
]

Existence is intended to follow from Brouwer on a compact ordered cutoff polytope. Uniqueness is not part of the core existence claim.

---

# 3. Standing hypotheses

## A1. Independent primitives

The variables (v,\varepsilon,\xi), and all (z_d) are mutually independent. The Gaussian distributions have strictly positive variances.

## A2. Finite model

The plan menu, pooled order-mark support, noise support, and calendar horizon are finite. Prices and payoffs are bounded on the maintained parameter set.

## A3. Ordered plans and single crossing

For every fixed belief and price system, adjacent-plan payoff differences cross zero at most once in (s), and the preferred plan is weakly increasing in (s).

## A4. Legal-clock discipline

The crossing date is the first date on which the stake path reaches (\tau). The filing lands at the deadline (c+T). Filings truthfully reveal stake and purpose. Only Voice plans cross the threshold in the core.

## A5. Inner pricing regularity

Each public-history pricing map has a unique fixed point and is continuous in beliefs, cutoffs, and parameters.

## A6. Compact outer self-map

All best-response cutoffs lie in a common compact ordered polytope, and (\mathcal T) is continuous and maps that polytope into itself.

## A7. Filing sufficiency

For flagged histories, the tuple

[
(B^F,Q^F,a=1)
]

identifies the informed component of the selected plan. Conditional on that tuple, the pooled order-flow residual is pure noise and is independent of (v,s,\xi).

A stronger convenient version is that

[
(j,s)
\longmapsto
(B_j^F(s),Q_j^F(s),a_j)
]

is injective on the flagged set.

## A8. Interior crossing

When positive cell mass is invoked,

[
0<\Omega(\kappa,\tau,T)<1.
]

This is not required for the structural partition.

## A(\tau). Threshold chord restriction

For the closed-form threshold result, the relevant pooled posterior law has the symmetric ternary-kernel representation

[
\mathbb E[h(\Pi_\kappa)]
========================

A_0(\kappa)h(0)
+
A_{1/2}(\kappa)h(\bar\pi/2)
+
A_1(\kappa)h(\bar\pi),
]

with

[
A_0'(\kappa)
============

# A_1'(\kappa)

a_\kappa,
\qquad
A_{1/2}'(\kappa)
================

-2a_\kappa.
]

The associated chord is

[
C_h(\bar\pi)
============

h(0)-2h(\bar\pi/2)+h(\bar\pi).
]

The maintained orientation is

[
C_h(\bar\pi)\le0,
]

and

[
|C_h(\bar\pi)|
]

is weakly increasing in (\bar\pi).

## AGE. GE differentiability and contraction

On a candidate region (\mathcal R), the outer map is twice continuously differentiable and

[
L_{\mathcal R}
==============

\sup_{\vartheta\in\mathcal R}
|D_k\mathcal T(k;\vartheta)|
<1.
]

The sign of the equilibrium liquidity derivative is constant on the region.

---

# 4. Complete symbol table

## 4.1 Primitives and parameters

| Symbol               | Meaning                                                 |
| -------------------- | ------------------------------------------------------- |
| (v)                  | Target standalone value                                 |
| (\mu_v,\sigma_v)     | Mean and standard deviation of (v)                      |
| (s)                  | Blockholder’s private signal                            |
| (\varepsilon)        | Signal noise                                            |
| (\sigma_\varepsilon) | Standard deviation of signal noise                      |
| (\lambda_s)          | Gaussian projection coefficient in (\mathbb E[v\mid s]) |
| (\xi)                | Bidder’s private synergy shock                          |
| (\sigma_\xi)         | Standard deviation of (\xi)                             |
| (\bar S)             | Mean bidder synergy component                           |
| (K)                  | Bidder’s fixed entry/control cost                       |
| (m_0,m_1)            | Takeover premia without and with engagement             |
| (\Delta_m=m_1-m_0)   | Premium wedge                                           |
| (\Delta_V)           | Expected non-takeover value created by engagement       |
| (\kappa)             | Noise-trading intensity; liquidity                      |
| (\bar z)             | Absolute size of a ternary noise-order mark             |
| (\tau)               | Stake threshold; lower (\tau) is tighter                |
| (T)                  | Filing window in business days; lower (T) is tighter    |
| (H)                  | Business-day control-decision horizon                   |
| (b_0)                | Initial blockholder stake                               |
| (\bar b)             | Maximum feasible stake                                  |

## 4.2 Plans and legal timing

| Symbol            | Meaning                                                         |
| ----------------- | --------------------------------------------------------------- |
| (\mathcal J)      | Finite ordered set of complete contingent plans                 |
| (j)               | Plan index                                                      |
| (a_j)             | Engagement choice attached to plan (j)                          |
| (B_j(s,d))        | Cumulative pooled stake path under plan (j)                     |
| (b_j^*(s))        | Target stake (B_j(s,H))                                         |
| (c_j(s;\tau))     | First threshold-crossing date                                   |
| (f_j(s;\tau,T))   | Filing date (c_j+T)                                             |
| (D_j(s;\tau,T))   | Indicator that the flag lands by (H)                            |
| (B_j^F(s;\tau,T)) | Stake at filing                                                 |
| (Q_j^F(s;\tau,T)) | Flagged-round order                                             |
| (\psi)            | Coarsening map from actual stake increment to pooled order mark |
| (q_{jd}(s))       | Informed pooled order mark                                      |
| (z_d)             | Noise order at day (d)                                          |
| (X_d)             | Observed pooled order flow                                      |

## 4.3 Information, prices, and control outcome

| Symbol                      | Meaning                                                             |
| --------------------------- | ------------------------------------------------------------------- |
| (\mathcal H_d^P)            | Pooled public history at day (d)                                    |
| (F)                         | Filing message ((B^F,a=1))                                          |
| (\mathcal I_H)              | Information available at the control node                           |
| (\mathcal C_F,\mathcal C_P) | Flagged and pooled cells                                            |
| (\pi(\mathcal I))           | Posterior probability of engagement                                 |
| (p(\mathcal I))             | Bidder-entry probability                                            |
| (\mathsf B)                 | Bidder-entry indicator                                              |
| (Y)                         | Terminal shareholder payoff                                         |
| (P_d^P)                     | Competitive pooled price at day (d)                                 |
| (P_{\mathrm{ND}})           | Counterfactual pooled price at the same order flow without the flag |
| (P^F)                       | Price after the flag and flagged-round order                        |
| (R_d)                       | Run-up path relative to the pre-trigger price                       |
| (R)                         | Cumulative pre-filing run-up                                        |
| (J)                         | Filing-day jump (P^F-P_{\mathrm{ND}})                               |

## 4.4 Premium and comparative-static objects

| Symbol                                       | Meaning                                                        |
| -------------------------------------------- | -------------------------------------------------------------- |
| (h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)) | Engagement-premium kernel                                      |
| (\Delta^{\mathrm{act}})                      | Expected engagement-related premium                            |
| (M_F)                                        | Conditional expected engagement premium in flagged cell        |
| (M_P)                                        | Conditional expected engagement premium in pooled cell         |
| (\Omega=\Pr(D=1))                            | Unconditional flagged-cell weight                              |
| (\omega=\Pr(D=1\mid a=1))                    | Disclosed share of engagements; calibration object             |
| (\bar\pi)                                    | Pre-order pooled engagement share used in the chord lemma      |
| (\mathcal S)                                 | Absolute liquidity-sensitivity of (\Delta^{\mathrm{act}})      |
| (\mathcal S_P)                               | Absolute liquidity-sensitivity of the pooled-cell premium      |
| (C_h(\bar\pi))                               | Chord (h(0)-2h(\bar\pi/2)+h(\bar\pi))                          |
| (W_\tau,W_T)                                 | Weight-effect ratios for threshold and window tightenings      |
| (C_\tau,C_T)                                 | Composition-effect ratios for threshold and window tightenings |

## 4.5 Equilibrium and GE-certification objects

| Symbol                    | Meaning                                                            |
| ------------------------- | ------------------------------------------------------------------ |
| (k)                       | Weakly ordered cutoff vector                                       |
| (\Theta)                  | Compact ordered cutoff polytope                                    |
| (\vartheta)               | Parameter vector                                                   |
| (\mathcal T(k;\vartheta)) | Outer cutoff best-response map                                     |
| (L_{\mathcal R})          | Contraction bound for (D_k\mathcal T) on region (\mathcal R)       |
| (r_\tau=-\tau)            | Threshold strictness coordinate                                    |
| (r_T=-T)                  | Window strictness coordinate or smooth interpolation               |
| (\sigma_\kappa)           | Constant sign of the liquidity derivative on a candidate GE region |
| (g_r^{PE})                | Direct fixed-policy attenuation margin                             |
| (\mathcal B_r^{GE})       | Bound on all equilibrium cutoff-response terms                     |
| (\mathcal R_r)            | Region satisfying contraction and dominance conditions             |

---

# 5. Result ledger

Because this turn contains statements but deliberately no proofs, the active label on every nondefinitional result is **CONJECTURE**. The intended final labels are shown separately and may be upgraded only after the dedicated proof and numerical-check turn.

| ID | Result                                               | Current label |                                    Intended final label |
| -- | ---------------------------------------------------- | ------------: | ------------------------------------------------------: |
| D1 | Rule-keyed partition and timing-split representation |    CONJECTURE |                                                  PROVED |
| P1 | Cutoff PBE existence                                 |    CONJECTURE |                                                  PROVED |
| L1 | Premium cell decomposition                           |    CONJECTURE |                                                  PROVED |
| L2 | Flagged-cell direct liquidity-invariance             |    CONJECTURE |                                                  PROVED |
| L3 | Chord-vanishing lemma                                |    CONJECTURE |                                    PROVED under (A\tau) |
| L4 | Threshold composition lemma                          |    CONJECTURE |                    PROVED under nested reclassification |
| T1 | Partition attenuation theorem                        |    CONJECTURE |                                PROVED at fixed policies |
| C1 | GE region certificate                                |    CONJECTURE | PROVED on a named nonempty region; NUMERICAL off-region |

---

# 6. Theorem stack

## D1 — Rule-keyed partition and timing-split representation

**CLAIM** — For every ((\tau,T)) and every strategy profile, (D=\mathbf 1{a=1,\ c(\tau)+T\le H}) maps each control-node history into exactly one flagged or pooled cell, and each flagged history produces endogenous objects (B^F), (R_d), (R), and (J) satisfying (P^F-P_{c^-}^P=R+J).

**HYPOTHESES**

1. A2: the calendar horizon and public histories are finite.
2. A4: crossing and filing dates obey the legal-clock definitions.
3. The same-history counterfactual (P_{\mathrm{ND}}) is well-defined.
4. The flagged price (P^F) is observed before the control decision.

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will first establish measurability and exclusivity of (D), then establish the timing-split equality by adding and subtracting (P_{\mathrm{ND}}).

**WHERE IT FAILS**

1. Filing occurs at a discretionary date unrelated to (c+T).
2. The bidder decides before the flagged-round price is formed.
3. The filing does not identify a stake or purpose, so (B^F) is not an observable model object.

**LABEL CLAIMED** — CONJECTURE in this turn because the representation proof is deferred; intended final label PROVED.

**NUMERICAL CHECK REQUEST** — Run one history-enumeration script over (\kappa\in{0.15,0.35,0.55,0.75,0.85}), (T\in{5,10}), and thresholds at the (10)th, (30)th, (50)th, (70)th, and (90)th percentiles of equilibrium stake paths; verify zero histories with (D\notin{0,1}), zero overlap between cells, exhaustive cell probability summing to one, and (\max|P^F-P_{c^-}^P-R-J|<10^{-12}). Under the interiority calibration, the predicted minimum cell mass is at least the chosen grid floor (0.01); outside that calibration only the zero identity residual is predicted.

**NOTATION DELTA** — None beyond the model card.

**NOT CLAIMED** — Positive probability in both cells without A8; any sign for (R) or (J); any causal interpretation of the timing split.

---

## P1 — Cutoff PBE existence

**CLAIM** — Under A1–A7, the two-round model has at least one perfect Bayesian equilibrium in weakly ordered cutoff strategies over complete contingent plans; under A8, both partition cells are on path.

**HYPOTHESES**

1. A1: independent Gaussian value, signal, and bidder primitives.
2. A2: finite histories, plan menu, and noise support.
3. A3: adjacent-plan single crossing and ordered plan preferences.
4. A5: continuous unique inner price fixed points.
5. A6: a compact cutoff polytope and continuous self-map.
6. Sequential optimality of the flagged component of each complete contingent plan.
7. A8 only for the positive-cell-mass conclusion.

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will construct the inner prices, show that adjacent indifference values define a continuous self-map of the ordered cutoff polytope, and invoke Brouwer.

**WHERE IT FAILS**

1. The pricing layer has no fixed point or jumps discontinuously with cutoffs.
2. Adjacent-plan payoff differences cross more than once, so cutoff strategies do not represent best responses.
3. The plan set or cutoff domain is unbounded.
4. Positive cell mass can fail even when equilibrium exists.

**LABEL CLAIMED** — CONJECTURE in this turn; intended final label PROVED. Uniqueness is not included.

**NUMERICAL CHECK REQUEST** — Run one 30-seed multistart equilibrium script on the full ((\kappa,\tau,T)) grid from D1 plus (\pm20%) perturbations of (\sigma_\xi,\Delta_m), and engagement costs; at every node require at least one weakly ordered solution with (|k-\mathcal T(k)|_\infty<10^{-10}), inner pricing residuals below (10^{-10}), and no profitable adjacent-plan deviation above (10^{-9}). Predicted magnitude: at least one equilibrium per node; no prediction of uniqueness or identical convergence across seeds.

**NOTATION DELTA** — None beyond the model card.

**NOT CLAIMED** — Equilibrium uniqueness, strict interiority, global differentiability of equilibrium cutoffs, or monotone comparative statics in (\kappa,\tau,T).

---

## L1 — Premium cell decomposition

**CLAIM** — Whenever (0<\Omega<1), the expected engagement-related premium satisfies the accounting identity (\Delta^{\mathrm{act}}=\Omega M_F+(1-\Omega)M_P).

**HYPOTHESES**

1. The flagged and pooled cells are mutually exclusive and exhaustive.
2. (\Delta_m h(\mathcal I_H)) is integrable.
3. (0<\Omega<1) so both conditional cell averages are defined.

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will apply the law of iterated expectations to the indicator (D).

**WHERE IT FAILS**

1. The reported “cell premia” are computed using different populations or different control horizons.
2. The cells overlap or omit histories.
3. At a zero-mass cell, its conditional average is undefined unless a limiting convention is specified.

**LABEL CLAIMED** — CONJECTURE in this turn; intended final label PROVED as an accounting identity.

**NUMERICAL CHECK REQUEST** — Run one direct-summation check at every equilibrium grid node, comparing (\Delta^{\mathrm{act}}) computed from all histories with (\Omega M_F+(1-\Omega)M_P); predicted signed residual is zero and absolute residual is below (10^{-12}). Report all objects in premium percentage points, not normalized indices.

**NOTATION DELTA** — None beyond the model card.

**NOT CLAIMED** — A sign for either cell premium, a causal decomposition, or attenuation from the identity alone.

---

## L2 — Flagged-cell direct liquidity-invariance

**CLAIM** — Holding the cutoff and execution policies fixed, A7 implies that the flagged control-node posterior, price, bidder-entry probability, and conditional expected premium are invariant to (\kappa).

**HYPOTHESES**

1. A7: ((B^F,Q^F,a=1)) identifies the informed component of the selected plan.
2. Conditional on that tuple, pooled order-flow residuals consist only of independent noise.
3. Noise-trading intensity (\kappa) enters neither target value nor bidder primitives.
4. The plan and cutoff policies are held fixed.
5. The flagged-round order is observed without an additional (\kappa)-dependent noise layer.

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will show the conditional-independence statement
   [
   (v,s,\xi)\perp!!!\perp \mathcal H^P
   \mid(B^F,Q^F,a=1),
   ]
   and then apply it to the pricing and entry equations.

**WHERE IT FAILS**

1. The filing and flagged-round order do not identify the informed execution plan, leaving residual inference in pooled order flow.
2. Flagged-round trading is itself mixed with noise whose intensity is (\kappa).
3. The equilibrium cutoff or execution policy is allowed to change with (\kappa); that is a GE channel, not direct invariance.
4. Passive threshold crossers are admitted without their purpose being distinguished.

**LABEL CLAIMED** — CONJECTURE in this turn; intended final label PROVED at fixed policies.

**NUMERICAL CHECK REQUEST** — Freeze one equilibrium cutoff and plan policy at each ((\tau,T)), vary (\kappa) over ({0.05,0.10,\ldots,0.95}), and recompute every on-path flagged posterior, price, entry probability, and (M_F). The predicted maximum range of each object is zero; numerical acceptance requires ranges below (10^{-10}) and central finite-difference derivatives below (10^{-8}).

**NOTATION DELTA** — None beyond the model card.

**NOT CLAIMED** — Filing-day jump invariance; pooled-price invariance; total-equilibrium invariance after cutoff responses.

---

## L3 — Chord-vanishing lemma

**CLAIM** — Under A(\tau), the pooled cell’s interior liquidity motion is proportional to (C_h(\bar\pi)=h(0)-2h(\bar\pi/2)+h(\bar\pi)), and if (h) is twice continuously differentiable at zero then (C_h(\bar\pi)=\tfrac14h''(0)\bar\pi^2+o(\bar\pi^2)), so the interior (\kappa)-motion vanishes as (\bar\pi\downarrow0).

**HYPOTHESES**

1. A(\tau): the symmetric ternary posterior-law representation.
2. (h) is twice continuously differentiable in a neighborhood of zero.
3. (h(0)=0).
4. The cell’s standalone-value component is held fixed in the chord comparison.
5. The coefficient (a_\kappa) is bounded on the liquidity interval.

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will differentiate the three-point posterior-law representation and then apply a second-order Taylor expansion of (h) at zero.

**WHERE IT FAILS**

1. The pooled posterior law cannot be reduced to the three-point symmetric chord representation.
2. (h) has a kink or unbounded second derivative at zero.
3. Changes in (\bar\pi) simultaneously alter an uncontrolled standalone-value component.
4. An additional pooled type creates posterior support outside the chord representation.

**LABEL CLAIMED** — CONJECTURE in this turn; intended final label PROVED under A(\tau).

**NUMERICAL CHECK REQUEST** — Run one chord script on (\bar\pi\in{10^{-4},2\cdot10^{-4},5\cdot10^{-4},10^{-3},\ldots,0.9}) and (\kappa\in{0.15,0.25,\ldots,0.85}); compare the directly enumerated (\partial_\kappa\mathbb E[h]) with (a_\kappa C_h(\bar\pi)), requiring residual below (10^{-10}). Predicted sign is the sign of (a_\kappa C_h); predicted small-(\bar\pi) magnitude is quadratic, with (|C_h|/\bar\pi^2) differing by less than (5%) between the two smallest (\bar\pi) points.

**NOTATION DELTA** — (a_\kappa) is the derivative coefficient in A(\tau); it is now added to the card’s theorem-specific notation.

**NOT CLAIMED** — That (C_h<0) for every parameter configuration; that the whole premium is hump-shaped; any GE cutoff-shift result.

---

## L4 — Threshold composition lemma

**CLAIM** — At fixed plan and cutoff policies, a lower threshold (\tau) weakly raises (\Omega), weakly lowers the engagement share (\bar\pi) remaining in the relevant pooled class, and—under L3 and monotonicity of (|C_h|)—weakly lowers (\mathcal S_P).

**HYPOTHESES**

1. Threshold reclassification is nested:
   [
   \tau'<\tau
   \quad\Rightarrow\quad
   \mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T).
   ]
2. Every history newly moved to the flagged cell is generated by a Voice plan.
3. Passive histories are not moved into the flagged cell.
4. The preselected execution policies and signal cutoffs are held fixed.
5. L3 applies to the relevant pooled posterior class.
6. (|C_h(\bar\pi)|) is weakly increasing in (\bar\pi).

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will first establish the flagged-set inclusion, then use conditional-probability arithmetic to show that removing engagement histories lowers (\bar\pi), and finally invoke L3.

**WHERE IT FAILS**

1. Lowering the threshold changes execution plans or engagement choices rather than only legal classification.
2. Passive blockholders cross the threshold and are newly flagged.
3. The marginal Voice histories removed from the pool have an order kernel that raises rather than lowers pooled posterior motion.
4. Early or strategically delayed filings violate nestedness.

**LABEL CLAIMED** — CONJECTURE in this turn; intended final label PROVED under the listed nestedness and chord hypotheses.

**NUMERICAL CHECK REQUEST** — Freeze plan cutoffs and evaluate thresholds at the (90)th through (10)th percentiles of the Voice stake distribution, with (\kappa\in[0.15,0.85]) on a (0.01) grid and (T\in{5,10}). In one script, report (\Omega(\tau)), (\bar\pi(\tau)), and (\mathcal S_P(\tau)). Predicted signs for a tightening are (\Delta\Omega\ge0), (\Delta\bar\pi\le0), and (\Delta\mathcal S_P\le0); the predicted limiting magnitude is (\mathcal S_P=O(\bar\pi^2)) near zero. Any sign violation is a failed hypothesis, not sampling error.

**NOTATION DELTA** — None beyond the model card and (a_\kappa) introduced in L3.

**NOT CLAIMED** — A threshold result after equilibrium cutoff responses; strict attenuation when no mass crosses; attenuation caused solely by the legal flag rather than by changes in order informativeness.

---

## T1 — Partition attenuation theorem

**CLAIM** — At fixed plan and cutoff policies, threshold tightening attenuates the premium’s liquidity-sensitivity under L3–L4, whereas window tightening attenuates it if and only if its weight effect dominates its composition effect.

**HYPOTHESES**

1. L1: the premium cell decomposition.
2. L2: direct flagged-cell (\kappa)-invariance.
3. (\Omega) is fixed with respect to (\kappa) in the partial-equilibrium comparison.
4. (0<\Omega<1) and (\mathcal S_P>0).
5. L3 and L4 for the threshold-margin conclusion.
6. For a tighter window (T'<T),
   [
   \Omega(\tau,T')\ge\Omega(\tau,T).
   ]
7. The same plan and cutoff policies are used in the two window environments.

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will derive
   [
   \mathcal S=(1-\Omega)\mathcal S_P,
   ]
   apply L4 to the threshold margin, and state the exact product criterion for the window margin.

**WHERE IT FAILS**

1. Window tightening raises the pooled-cell sensitivity enough to dominate the reduction in pooled weight.
2. The flagged component retains direct (\kappa)-dependence.
3. The plan or cutoff policy changes between the compared rules.
4. (\mathcal S_P=0), making the ratio form uninformative.
5. The old low-disclosed-mass calibration is precisely a failure case for an unconditional window theorem.

**LABEL CLAIMED** — CONJECTURE in this turn; intended final label PROVED at fixed policies. The window conclusion is an if-and-only-if condition, not unconditional attenuation.

**NUMERICAL CHECK REQUEST** — Run one fixed-policy rule-comparison script. For threshold pairs (\tau'<\tau), calculate
[
W_\tau=
\frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)},
\qquad
C_\tau=
\frac{\mathcal S_P(\tau',T)}{\mathcal S_P(\tau,T)},
]
and verify
[
\frac{\mathcal S(\tau',T)}{\mathcal S(\tau,T)}
==============================================

W_\tau C_\tau
\le1.
]
For the window comparison (T'=5<T=10), calculate
[
W_T=
\frac{1-\Omega(\tau,5)}{1-\Omega(\tau,10)},
\qquad
C_T=
\frac{\mathcal S_P(\tau,5)}{\mathcal S_P(\tau,10)},
]
and verify
[
\frac{\mathcal S(\tau,5)}{\mathcal S(\tau,10)}
==============================================

W_T C_T
]
to within (10^{-10}). Predicted threshold sign: ratio at most one. Predicted window sign: attenuation exactly when (W_TC_T\le1), amplification when (W_TC_T>1); no unconditional economic magnitude is predicted before calibration. As a regression benchmark, applying the analogous decomposition to the old framework must reproduce the documented directions around (1.06,1.19,1.14,) and (0.38), rather than silently forcing attenuation. 

**NOTATION DELTA** — The finite-change ratios (W_\tau,C_\tau,W_T,C_T) are now fully defined in this claim and added to the card.

**NOT CLAIMED** — Global window attenuation; general-equilibrium attenuation; a positive or negative filing-day-jump slope; agreement with the parallel rebuilt-model O-1 run before its raw output is supplied.

### Equivalent local window condition

For a smooth interpolation with window strictness

[
r_T=-T,
]

the product criterion is equivalent to

[
\partial_{r_T}\mathcal S
========================

-\Omega_{r_T}\mathcal S_P
+
(1-\Omega)\partial_{r_T}\mathcal S_P
\le0.
]

Because

[
\Omega_{r_T}\ge0,
]

the first term is the attenuating weight effect. The composition effect is the second term and is unsigned. Attenuation holds exactly when

[
\frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P}
\le
\frac{\Omega_{r_T}}{1-\Omega}.
]

This is the condition the rebuilt-model O-1 run must evaluate.

---

## C1 — GE region certificate

**CLAIM** — On any named parameter region where the outer cutoff map is a contraction and the direct fixed-policy attenuation margin exceeds a computable inversion-free bound on all cutoff-response terms, the corresponding threshold or window attenuation sign survives in equilibrium.

**HYPOTHESES**

1. AGE: twice differentiable outer map and
   [
   L_{\mathcal R}<1.
   ]
2. The equilibrium is locally represented by
   [
   k=\mathcal T(k;\vartheta).
   ]
3. The sign
   [
   \sigma_\kappa
   =============

   \operatorname{sgn}
   \left(
   \frac{d\Delta^{\mathrm{act}}}{d\kappa}
   \right)
   ]
   is constant on the candidate region.
4. All required first and second derivatives of (\Delta^{\mathrm{act}}) and (\mathcal T) are bounded on the region.
5. The direct fixed-policy attenuation margin
   [
   g_r^{PE}
   ========

   -\sigma_\kappa
   \partial_{\kappa r}
   \Delta^{\mathrm{act}}
   ]
   is strictly positive.
6. The calculated GE remainder bound satisfies
   [
   g_r^{PE}>\mathcal B_r^{GE}.
   ]

**PROOF**

1. Deferred under the statement-only pacing instruction.
2. The proof turn will derive inversion-free bounds for (k_\kappa), (k_r), and (k_{\kappa r}), bound each cutoff-response term in the total cross-derivative, and apply the strict dominance inequality.

**WHERE IT FAILS**

1. The contraction bound reaches or exceeds one.
2. The direct fixed-policy attenuation margin is zero or smaller than the GE remainder.
3. The liquidity derivative changes sign inside the region.
4. Multiple equilibria produce discontinuous equilibrium selection.
5. The certified set is empty.

**LABEL CLAIMED** — CONJECTURE in this turn. Intended final label PROVED only on an explicitly named nonempty region satisfying the inequalities. If the numerical certificate returns an empty region, this claim is dropped and the paper ships the fixed-policy theorem only. Off-region results receive at most the label NUMERICAL.

**NUMERICAL CHECK REQUEST** — Run one region-certification script over (\kappa\in[0.15,0.85]) on a (0.01) grid, (T\in{5,10}), threshold percentiles (10) through (90), and the maintained robustness perturbations. At each node calculate (L_{\mathcal R}), (g_r^{PE}), the inversion-free derivative bounds, (\mathcal B_r^{GE}), and the slack
[
\eta_r=g_r^{PE}-\mathcal B_r^{GE}.
]
Predicted sign on certified nodes is attenuation, with certified magnitude at least (\eta_r>0); numerical acceptance requires derivative-bound residuals below (10^{-8}). No positive region size is predicted before the run. The raw output must explicitly report “empty region” if no node has (L<1) and (\eta_r>0).

**NOTATION DELTA** — For (x\in{\kappa,r}), define the inversion-free first-derivative bound
[
\bar k_x
========

\frac{|\partial_x\mathcal T|}{1-L_{\mathcal R}}.
]
Define
[
\bar k_{\kappa r}
=================

\frac{
|\mathcal T_{\kappa r}|
+|\mathcal T_{\kappa k}|\bar k_r
+|\mathcal T_{rk}|\bar k_\kappa
+|\mathcal T_{kk}|\bar k_\kappa\bar k_r
}{
1-L_{\mathcal R}
}.
]
One admissible GE remainder bound is
[
\mathcal B_r^{GE}
=================

|\Delta_{\kappa k}|\bar k_r
+
\left(
|\Delta_{kr}|
+
|\Delta_{kk}|\bar k_r
\right)\bar k_\kappa
+
|\Delta_k|\bar k_{\kappa r}.
]

**NOT CLAIMED** — A global GE sign, uniqueness of equilibrium, a nonempty certified region, or attenuation outside the certified region.

---

# 7. Calibration card

The model distinguishes the accounting weight

[
\Omega=\Pr(D=1)
]

from the empirically meaningful disclosed-engagement share

[
\omega=\Pr(D=1\mid a=1).
]

The calibration should target:

[
\omega,
\qquad
\mathcal L(B^F\mid D=1),
\qquad
\mathcal L(c),
\qquad
\mathcal L(f-c),
]

rather than selecting an arbitrary cutoff that happens to generate a small public-action mass.

The previous calibration’s disclosed mass of approximately (0.037) produced a difference below one percent and even slightly greater mean liquidity-sensitivity in the disclosed comparison. That number must not be carried over as the v4 anchor. 

All numerical results should be reported in economically interpretable units:

| Object                          | Required reporting unit                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| (\omega,\Omega)                 | Percentage of engagements / percentage of all histories                              |
| (B^F)                           | Percentage points of outstanding shares                                              |
| Bidder entry                    | Percentage-point change in entry probability                                         |
| (M_F,M_P,\Delta^{\mathrm{act}}) | Premium percentage points                                                            |
| (R,J)                           | Basis points or percentage returns                                                   |
| Liquidity-sensitivity           | Premium percentage points per one-standard-deviation increase in empirical liquidity |
| Window comparison               | Level change from 10 to 5 business days                                              |
| Threshold comparison            | Level change for a stated threshold move, such as 5% to 3%                           |

The model does not presently assign an empirical value to (\omega); the source bundle supplies the required calibration object but not the estimate.

---

# 8. Global boundaries of the model card

The card deliberately does not claim:

1. a global attenuation sign for the window margin;
2. that the filing-day jump is (\kappa)-invariant;
3. equilibrium uniqueness;
4. a nonempty GE-certified region;
5. endogenous filing before the deadline;
6. noisy or partially revealing flagged-round trading;
7. continuous-time execution;
8. welfare or an optimal disclosure rule;
9. that the old hump result survives;
10. that the prior calibration is economically meaningful.

The first dedicated proof turn should take **D1 — Rule-keyed partition and timing-split representation**, because all later claims use its partition and price-path objects.
