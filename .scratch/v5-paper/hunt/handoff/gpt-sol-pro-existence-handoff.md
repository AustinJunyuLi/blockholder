# Handoff: equilibrium existence at the calibration of "Who Gets Caught"

Prepared 2026-09-02 by the orchestrating session of the paper *Who Gets Caught: Blockholder
Disclosure Rules and Market Inference* (worktree `blockholder_v5`, branch `v5`). The reader of
this document has no access to the worktree, so everything needed is inline. Each section names
the file it was taken from, for the session that receives the answer.

## 1. Objective

A theorem, with a complete proof, that an equilibrium of the two-round game of section 5 exists
at the paper's calibration (section 7): at each of the ten calibration nodes (two clocks, five
thresholds), or at the calibration as a whole. Each hypothesis of the theorem is either proved from the primitives or is
a finite computation a script can perform at a node from the objects section 9 lists.

The paper's equilibrium notion is the cutoff perfect Bayesian equilibrium of section 5.4. A
theorem under a different notion is admissible if it states the notion as a definition, names
what differs from the paper's, and says what the calibration's cutoff policy (section 7) is under
it. Whether the paper adopts a different notion is the author's decision; this document asks for
the theorem and the cost, not the decision.

If no theorem of this kind exists, a precise negative finding with its reason is the answer.

## 2. Constraints

- The primitives are fixed as section 5 and section 7 state them: the menu, the stake paths, the
  building count n(s), the noise law, the pricing rule, the bidder, the order size of two noise
  lumps, and the parameter values. A theorem that changes a primitive answers a different
  question.
- Every hypothesis is stated in the theorem. Two assumptions the paper dropped stay out of the
  proof: the ternary pooled law of order size one, and any support assumption on the pooled
  posterior.
- The paper's headline results (section 4) hold at fixed policies and use no existence result.
  The theorem leaves them as they are.
- A hypothesis quantified over a continuum (of signals, of policies, of prices) is proved from the
  primitives, or is reduced to finitely many computations at a node with the reduction proved.
- The proof is complete at the level of a journal appendix: every step follows from something in
  this document or in a named textbook result with its hypotheses checked.
- Anything not proved is labelled as such. The paper carries three labels, PROVED, NUMERICAL
  (verified on a stated grid) and ESTIMATED; a working conjecture is labelled CONJECTURE.
- The proof is in the notation of sections 5 to 7. LaTeX is welcome.

## 3. What to return

Two deliverables, in this order.

**Deliverable A: the theorem.**
1. Statement, with the full hypothesis list.
2. The equilibrium notion used, and, if it differs from section 5.4, the definition, the
   difference, and the status of the calibration's cutoff policy under it.
3. The proof.
4. "What a script computes at a node": the finite checks, each as a formula in the objects of
   section 9, with the tolerance the proof needs.
5. Anything left open, labelled.

**Deliverable B: holistic comments.** An evaluation of the endeavour as a whole, as a referee at
a top journal and as a co-author would give it: whether the existence question deserves the
paper's effort; whether the model, the calibration, or the results have a better framing or a
better angle than section 4 states; what a referee would say first; anything in sections 5 to 8
that looks wrong. Independent of Deliverable A: comments are welcome whether or not a theorem
was found.

## 4. The paper in brief

From `.scratch/v5-paper/spec.md`, sections 2 and 3, with the labels each result holds after the
review of 2026-09-02 (`grok/checkpoint-1.md`).

#### Headline (spec section 2)

A disclosure rule has two dials. The stake threshold τ and the filing clock T split every
blockholder history into a flagged cell (the filing landed; the market knows) and a pooled cell
(no filing; the market reads order flow). Noise sensitivity of the price factorises as the
pooled share times the pooled sensitivity. Tightening the threshold lowers it at fixed policies:
the weight effect by proof, the composition effect on the calibration grid. Shortening the clock
lowers it if and only if its composition ratio is at most one, and the who-gets-caught corollary
characterises that ratio by the noise sensitivity of what the shorter clock removes from the pool.

#### The model, as the paper states it (spec section 3)

Two rounds of the inherited two-round structure, one change. The engaged blockholder's order
while building the stake is two noise lumps (ADR 0003). The noise trader trades one lump up or
down with probability κ/2 each and sits out with probability 1 minus κ. Order flow takes five
values; only the value plus one is ambiguous between "blockholder bought, noise sold" and
"blockholder idle, noise bought". Everything else in the model (plans, the Voice and Exit menu,
the bidder, the pricing rule, the calibration) is inherited unchanged and restated in the
paper's own words.

Results the paper carries, each with a label at delivery:

| Tag | Statement | Route | Ticket |
|---|---|---|---|
| Partition and factorisation | The rule partitions histories; S = (1 minus Ω) times S_P | Inherited proof, transcribed and attacked on v5 | 04 |
| Flagged cell is κ-free | The flagged endpoint does not depend on κ | Inherited proof, transcribed and attacked on v5 | 04 |
| Garbling lemma (new) | At order size two, the pooled experiment at higher κ is a garbling of that at lower κ; the pooled expectation of any convex (concave) kernel is monotone in κ | New proof | 02 |
| Threshold dial | At fixed policies a tighter threshold weakly lowers noise sensitivity | Factorisation and weight leg proved; the closed form of S_P in κ proved; the composition leg is Condition D, equivalent to the composition ratio being at most one, verified on the grid (NUMERICAL, κ in [0.15, 0.85]) | 02 |
| Clock dial | At fixed policies a shorter clock lowers noise sensitivity iff W_T times C_T is at most one | Inherited proof, transcribed and attacked on v5 | 04 |
| Who gets caught (new) | C_T is at most one iff the sensitivity of what the shorter clock removes lies weakly between the pool's and (2 minus φ)/φ times it; the paper gives the identity behind it | New proof plus a grid check | 03 |
| Existence (conditional on cleanliness) | An equilibrium exists at the paper's calibration | Only if the proof is clean at the numbers used; otherwise absent | 05 |

The general-equilibrium dominance result is not in the paper. Nothing in the paper says so.

Labels now. PROVED: the partition and factorisation, the flagged cell's κ-invariance, the garbling
lemma, the threshold weight leg and the closed form of S_P in κ, the clock dial, the
who-gets-caught identity and characterisation. NUMERICAL: the threshold composition leg on the
grid κ in [0.15, 0.85] at order size two, H = 10 (the condition fails just below the grid, so no
"for every κ" claim is made), and any directional who-gets-caught sentence off the five-node grid
record. ESTIMATED: E1 (stake at filing). ABSENT: existence (this document), and E2 (its link
coverage gate failed). The inherited draft carried an existence proposition whose hypotheses
failed at the calibration; it was dropped. A referee of that draft asked why the paper computes
at a calibration where its own existence result asserts nothing.

## 5. The model

### 5.1 The one change from the inherited draft

From `docs/adr/0003-doubled-order-size-and-existence.md`:

**The blockholder's order is twice the noise lump; existence appears only if proved clean.**

In the inherited model the blockholder's per-round order equalled the noise trader's lump, so
order flow took four values and the blockholder could hide inside the noise. The threshold
result then needed a support assumption on the pooled posterior that the calibration violated.
With the order set to two noise lumps, order flow takes five values, only one of which is
ambiguous, and the market's experiment at higher noise is a garbling of the experiment at lower
noise. That ordering signs the pooled cell's noise sensitivity without a support assumption.
The cost is a louder blockholder, defended in one paragraph of the paper, and an enumeration
about twelve times larger at the same horizon. The horizon is a calibration parameter and is not
lowered to compensate.

Every headline result is a fixed-policy comparison and does not need equilibrium existence.
An existence statement therefore enters the paper only if its proof is clean at the numbers the
paper uses. The general-equilibrium dominance result is dropped: it held on a minority of grid
nodes and answered a question the paper does not ask.

Read section 5.2 with that change: the engaged blockholder's order on a building date is two
noise lumps, order flow takes the five values in {-1, 0, 1, 2, 3} in lump units, and only the
value +1 is ambiguous between "blockholder bought, noise sold" and "blockholder idle, noise
bought".

### 5.2 The model section of the inherited draft (verbatim, LaTeX)

From `inherited/draft_v3/draft_v3.tex`, the section "The model" (subsections 5.4 "Equilibrium
notion" and 5.5 "The cutoff polytope and the premium objects" are inside it). Citation macros
and `\compatlabel` are the draft's own and carry nothing.

```latex
\section{The model}
\label{sec:model}
\label{sec:hypotheses}
%==============================================================================

\subsection{Object and partition}
\label{sec:object}

The disclosure rule divides the market's information into two cases. A stake threshold $\tau$ and a
filing window $T$ determine whether the filing has arrived by the control decision. In the \emph{flagged}
cell, the market sees the stake and the intention to engage. In the \emph{pooled} cell, it sees only
order flow and must infer whether an informed blockholder is trading. The cells are exhaustive. The
outcome of interest is the expected engagement-related premium $\Dact(\kappa,\tau,T)$. I also track
the run-up before the filing and the jump when the filing arrives. A lower threshold is a tighter
threshold margin; a shorter window is a tighter window margin.

The model uses the discrete order-flow structure of \citet{Kyle1985} and
\citet{EdmansGoldsteinJiang2015}, competitive prices as in \citet{GlostenMilgrom1985}, and the
takeover premium as the dispersed shareholder's control-outcome measure in the spirit of
\citet{GrossmanHart1980}. The contribution is the legal partition between those familiar pieces.
\subsection{Timing: the two rounds}
\label{sec:timing}

Trading runs over business days $d=0,\ldots,H$. Nature draws the firm's standalone value and the
blockholder's private signal. The blockholder then chooses a complete contingent plan from a finite
ordered menu. The plan fixes the stake path and whether it is meant to engage the firm.

In the first round, market makers see the plan's order flow mixed with ternary noise. The blockholder
does not revise the path in response to realised prices or order flow. The filing arrives exactly $T$
business days after the first crossing of $\tau$, provided that date is before the horizon. That filing
ends the pooled round. In the second round the blockholder trades the residual position, the market
updates its price, and the bidder decides whether to enter. If no filing arrives, the bidder acts on the
pooled history. The technical appendix spells out the off-path beliefs and the regularity conditions
needed for this timing.
\compatlabel{1}{asm:timing}
\compatlabel{1(a)}{asm:nofeedback}
\compatlabel{1(b)}{asm:flagterm}
\compatlabel{1(c)}{asm:A4}
\compatlabel{1(d)}{asm:A8}

\subsection{Primitives}
\label{sec:primitives}

% The model's ingredients are described in prose; the appendix retains the technical labels.
\compatlabel{1}{def:primitives}
The firm's standalone value is $v \sim N(\mu_v,\sigma_v^2)$. The blockholder observes
$s=v+\varepsilon$, where $\varepsilon \sim N(0,\sigma_\varepsilon^2)$ is independent of $v$. Her
posterior mean is $\Eop[v\mid s]=\mu_v+\beta(s-\mu_v)$, with
$\beta=\sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)\in(0,1)$. A potential bidder has an independent
synergy shock $\xi\sim N(0,\sigma_\xi^2)$, mean synergy $\bar S$, and entry cost $K>0$. Engagement
changes the takeover premium from $m_0$ to $m_1$, where $\Delta_m=m_1-m_0>0$, and creates non-takeover
value $\Delta_V\geq0$.

Noise trading takes the values $-\bar z$, $0$, and $+\bar z$. The zero-noise probability is
$1-\kappa$ and each nonzero value has probability $\kappa/2$, so $\kappa\in[0,1]$ measures
noise-trading intensity. The disclosure policy is $(\tau,T)$, with $T\in\{1,\ldots,H\}$; $b_0$ and
$\bar b$ are the initial and maximum stakes.

The blockholder chooses a plan from a finite menu $\mathcal J$, ordered from least to most aggressive.
Plan $j$ has an engagement flag $a_j$, equal to one for Voice and zero for Exit or Hold. Its pooled
stake at date $d$ is $B_j(s,d)$, with $B_j(s,-1)=b_0$, and its terminal target is
$b_j^*(s)=B_j(s,H)$. The first crossing of the threshold is
$c_j(s;\tau)=\inf\{d:B_j(s,d)\geq\tau\}$, with value $+\infty$ when no crossing occurs. The filing
date is $f_j=c_j+T$, and disclosure occurs when $a_j=1$ and $f_j\leq H$. At a filing, the reported
stake is $B_j^F=B_j(s,f_j)$ and the remaining order is $Q_j^F=b_j^*(s)-B_j^F$. A finite coarsening
$\Gamma$ maps the stake increment into the pooled order mark
$q_{jd}(s)=\Gamma(B_j(s,d)-B_j(s,d-1))$, so observed pooled flow is $X_d=q_{jd}+z_d$.
\compatlabel{2}{def:plans}

Market makers observe the pooled history
$\mathcal H_d^P=(X_0,\ldots,X_d;\ \text{flag landed by }d)$. A filing reports
$F=(B^F,a=1)$, and the flagged tuple adds the residual order, $\Sfl=(B^F,Q^F,a=1)$. At the control
node, public information is $\mathcal H_H^P$ in the pooled cell and $\Sfl$ in the flagged cell; the
bidder's $\xi$ remains private. I write these cells as $\mathcal C_P$ and $\mathcal C_F$. They are
exclusive and exhaustive. The engagement posterior is $\pi(\mathcal I)=\Prb(a=1\mid\mathcal I)$, and
equals one after a filing. The bidder enters with probability
\begin{equation}
\label{eq:entry}
p(\mathcal I) \;=\; 1 - \Phi\!\left(\frac{P + K + m_0 + \pi\Delta_m - \bar S}{\sigma_\xi}\right)
\;\in\;(0,1).
\end{equation}
With $\mathsf B$ the entry indicator, the terminal shareholder payoff is
\begin{equation}
\label{eq:Y}
Y \;=\; (1-\mathsf B)\,(v + a\Delta_V) \;+\; \mathsf B\,(P + m_0 + a\Delta_m),
\end{equation}
and prices satisfy the inner fixed point $P(\mathcal I) = \Eop[Y\mid\mathcal I]$. Two conventions are
part of the model rather than notation. First, $P_{-1}^P := \Eop[Y]$ is the pre-trading pooled
price, which is needed whenever $c = 0$, as $T = H$ forces on every flagged history. Second,
$P_{\ND}(\mathcal H_{f^-}^P) := P_{f^-}^P$: the not-yet-disclosed price is the last pre-filing pooled
price at the \emph{same} realised order flow, whose history already carries ``flag not landed by
$f-1$'', and not a never-disclosed counterfactual. Throughout, $c^-$ and $f^-$ denote the business days
immediately before the crossing date and the filing date. The price-path objects are the run-up path
$R_d = P_d^P - P_{c^-}^P$, the cumulative run-up $R = P_{f^-}^P - P_{c^-}^P$, and the filing-day
jump $J = P^F - P_{\ND}$; $R_d$, $R$ and $J$ are unsigned, and $J$ is not claimed to be
$\kappa$-invariant.\compatlabel{3}{def:prices}

The genuine fixed point sits at the control nodes. At an earlier pooled date $d < H$ the price is a
tower expectation of already-solved control-node values, with no self-reference; only the
control-node map is a fixed point to be solved.

The blockholder evaluates a plan by the expected terminal value of the position it builds, less the
trading outlay and the cost of engagement:
\begin{equation}
\label{eq:Uj}
U_j(s) \;=\; \Eop\Bigl[\, b_j^*(s)\,Y \;-\; \mathcal C_j^{\mathrm{trade}} \;-\; a_j\,C_j(s)
\;\Bigm\vert\; s,\, j \,\Bigr],
\end{equation}
where $\mathcal C_j^{\mathrm{trade}}$ is the execution outlay, with increments valued at the pooled
prices $P_d^P$ up to the plan's last pooled date and $Q_j^F(s)\,P^F$ when $D_j = 1$, and
$C_j(s) \ge 0$ is the engagement cost. Only two properties of \eqref{eq:Uj} are ever used:
\emph{plan-locality}, that $U_j$ depends on $j$ only through the executed stake path, the prices paid
on it, the terminal stake, the engagement flag and the cost; and \emph{integrability},
$\Eop[\max_{j}|U_j|] < \infty$ under the finiteness conditions of Section~\ref{sec:primitives}.
\compatlabel{4}{def:U}

The cost in \eqref{eq:Uj} is not tied to a particular date. It can be booked when the plan is completed
or treated as sunk once the filing arrives. These readings give the same comparison among flagged
round-two deviations, so the existence argument does not depend on the convention.
\compatlabel{1}{rem:Ctiming}


The primitive draws are mutually independent, with strictly positive variances. The menu, order-mark
support, noise support, and calendar are finite; prices and payoffs are locally bounded on the
maintained parameter set; and $\Eop[\max_{j\in\mathcal J}|U_j|]<\infty$ throughout the cutoff set.

Four restrictions on the primitive table travel together, and several results below consume them as
a block. Clause (TR-i), \emph{distributional forms and signs}: the distributions above hold as
stated, with $\sigma_v^2,\sigma_\varepsilon^2,\sigma_\xi^2>0$, $K>0$, $\bar z>0$, $\Delta_m>0$,
$\Delta_V\geq0$, and
\begin{equation}
\label{eq:m0}
m_0\geq0,
\end{equation}
so that $\bar m(\mathcal I)=m_0+\pi(\mathcal I)\Delta_m\geq0$. Restriction \eqref{eq:m0} is what
makes the inner pricing root exist, be unique and be continuous; when it is dropped, executed
counterexamples produce both no root and three roots. The initial stake satisfies $b_0<\tau$, so a
crossing that predates the model is outside the core analysis. Clause (TR-ii), \emph{stake-path
regularity}: Voice stakes are weakly increasing in the calendar date and in the signal, Hold stakes
are constant, Exit stakes are weakly decreasing in the date, and every map $s\mapsto B_j(s,d)$ is
Borel. Borel regularity is automatic for Voice and for Hold and is a genuine addition for Exit,
where the primitives supply monotonicity in the date alone; without it the pooled prices are not
defined, because pooled pricing integrates over every type. Stake levels themselves remain
continuum-valued: the finiteness above covers the menu, the image of $\Gamma$, the noise support and
the calendar, not the stake level. Clause (TR-iii), \emph{legal-clock objects}: the crossing,
filing, stake-at-filing, residual-order and terminal-target definitions hold as stated, together
with $D=1\Rightarrow a=1$, $Q^F\geq0$ for Voice plans, and, at fixed policies, $T'<T$ implying
$B^F(T')\leq B^F(T)$ and $Q^F(T')\geq Q^F(T)$. Clause (TR-iv), \emph{pricing and entry}: the
terminal payoff is \eqref{eq:Y}, prices obey $P(\mathcal I)=\Eop[Y\mid\mathcal I]$, entry obeys
\eqref{eq:entry}, the control-node information set is the fill given above, and the two price
conventions $P_{-1}^P=\Eop[Y]$ and $P_{\ND}=P_{f^-}^P$ hold.\compatlabel{2}{asm:primitives}
\compatlabel{2(a)}{asm:A1}
\compatlabel{2(b)}{asm:A2p}
\compatlabel{2(c)}{asm:TR}

\subsection{Equilibrium notion}
\label{sec:equilibrium-notion}


I use a cutoff perfect Bayesian equilibrium, and it carries six requirements: (i) a weakly ordered
cutoff vector $k=(k_1,\ldots,k_{J-1})$ selects the plan as a function of the signal; (ii) the pooled
and flagged actions are sequentially optimal at every history; (iii) beliefs obey Bayes' rule at
every history reached with positive probability; (iv) prices solve their competitive fixed points;
(v) the bidder follows \eqref{eq:entry}; and (vi) off-path beliefs are limits along one fixed
full-support perturbation family over plans. Weak inequalities allow an action region, including
Hold, to collapse. The outer cutoff map is solved on a compact ordered polytope, and uniqueness is
not claimed.\compatlabel{5}{def:cpbe}

The timing and primitive restrictions accompany every result. The cutoff construction requires adjacent
plan payoff differences to cross at most once in the signal, with the preferred plan weakly increasing
in the signal. It also requires a common compact bracket containing an indifference signal for every
adjacent plan pair at every point of $\Theta$, and a continuous, self-mapping outer best-response map
$\Tmap(k;\vartheta)$. The inner pricing root is unique and continuous in its belief summaries under
\eqref{eq:m0}; continuity of the composed price family in the cutoff vector is the part retained as a
condition.\compatlabel{3}{asm:eqobject}
\compatlabel{3(a)}{asm:A3}
\compatlabel{3(b)}{asm:A6}
\compatlabel{3(c)}{asm:A5}

On a flagged history, $(B^F,Q^F,a=1)$ identifies the informed plan component, so the remaining pooled
order is independent noise conditional on that tuple. For the fixed-policy comparisons, the composed
terminal target $s\mapsto b^*_{j(s)}(s)$ must be strictly increasing on the flagged signal region for
every $k\in\Theta$. The existence construction uses the stronger statement that
$(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ is injective over all flagged pairs, including pairs not selected by
the cutoff policy.\compatlabel{4}{asm:ident}
\compatlabel{4(a)}{asm:A7}
\compatlabel{4(b)}{asm:A7p}
\compatlabel{4(c)}{asm:A7J}

The pooled-cell comparison uses a strong support restriction. Its posterior law must have the
three-point form
\begin{equation}
\label{eq:atau}
\Eop[h] \;=\; A_0(\kappa)\,h(0) \;+\; A_{1/2}(\kappa)\,h(\bar\pi/2) \;+\; A_1(\kappa)\,h(\bar\pi),
\end{equation}
with $A_0'=A_1'=\Akap$, $A_{1/2}'=-2\Akap$, and a non-positive chord whose absolute value is weakly
increasing in $\bar\pi$. Two clauses carry the restriction's remaining bite: ($\tau$-i),
\emph{kernel through posterior}, that $h$ depends on the information set through the posterior
alone; and ($\tau$-ii), \emph{$\kappa$-free support}, that the three support points, the upper point
$\bar\pi$ included, do not move with $\kappa$. I write the restriction $\Atau$. Whether the
two-round pooled cell satisfies the support condition is open; the implemented calibration does
not.\compatlabel{5}{asm:Atau}

A threshold comparison $\tau'<\tau$ at fixed policies and a common $\kappa$ needs a bridge between
the two pooled classes, written $\Abr$, in five clauses. (br-i), \emph{representation at both
policies}: \eqref{eq:atau} holds under $\tau$ and under $\tau'$, with endpoints $\bar\pi(\tau)$ and
$\bar\pi(\tau')$ and coefficients $\Akap(\tau)$ and $\Akap(\tau')$. (br-ii),
\emph{$\kappa$-localisation}: all $\kappa$-dependence of $M_P$ sits in the weights, so that
$\partial_\kappa M_P=\Delta_m\Akap C_h(\bar\pi)$ exactly, with no composition remainder; that last
step is derived rather than assumed, and the clause names the same object as ($\tau$-i) against the
reading $h=\pi\,p(\hat v,\pi)$ rather than adding an independent restriction. (br-iii),
\emph{coefficient stability}: $|\Akap(\tau')|\leq|\Akap(\tau)|$, whose weakest sufficient form is
equality, reclassification changing which histories are pooled rather than the $\kappa$-responsiveness
of the pooled weights. (br-iv), \emph{endpoint linkage}: $\bar\pi$ is the chord endpoint of
\eqref{eq:atau} and is the same weakly increasing function of the pooled prior engagement share
$\bar\pi_{\mathrm{pr}}=\Prb(a=1\mid D=0)$ at $\tau$ and at $\tau'$, the identity branch
$\bar\pi=\bar\pi_{\mathrm{pr}}$ being excluded as degenerate. (br-v), \emph{comparability of the
chord functional}: $C_h(\cdot)$ and the kernel behind it are the same functions of the posterior at
both thresholds; without it the threshold comparison sets $|C_h|$ against a different functional and
means nothing. These clauses are used only for the threshold sensitivity result. For the
general-equilibrium result I require a twice continuously differentiable outer map on a candidate
region $\mathcal R$, a contraction bound $L_{\mathcal R}<1$, and a constant sign for the equilibrium
liquidity derivative.\compatlabel{6}{asm:bridge}
\compatlabel{6(a)}{asm:Abr}
\compatlabel{6(b)}{asm:AGE}

\subsection{The cutoff polytope and the premium objects}
\label{sec:polytope}


The cutoff vector is $k=(k_1,\ldots,k_{J-1})$ with weak ordering. The compact, convex set of such
vectors is $\Theta$, and $\vartheta$ collects the remaining parameters. The outer map
$\Tmap(k;\vartheta)$ gives the cutoff vector implied by a conjectured vector $k$. On a candidate
region $\mathcal R$, write $L_{\mathcal R}=\sup_{\mathcal R}\lVert D_k\Tmap\rVert$ and use
$r_\tau=-\tau$ and $r_T=-T$ so that a larger $r$ means a tighter rule. The fixed-policy attenuation
margin is
\begin{equation}
\label{eq:gPE}
g_r^{PE} \;=\; -\operatorname{sgn}\!\bigl(d\Dact/d\kappa\bigr)\;\partial_{\kappa r}\Dact,
\end{equation}
and the inversion-free cutoff bounds are $\bar k_x=|\partial_x\Tmap|/(1-L_{\mathcal R})$ and
$\bar k_{\kappa r}$. The general-equilibrium remainder is
\begin{equation}
\label{eq:BGE}
\mathcal B_r^{GE} \;=\; |\Delta_{\kappa k}|\,\bar k_r
\;+
\bigl(|\Delta_{kr}|+|\Delta_{kk}|\,\bar k_r\bigr)\bar k_\kappa
\;+
|\Delta_k|\,\bar k_{\kappa r}.
\end{equation}
Here the $\Delta$ terms are the gradient and cross-partials of $\Dact$ in $(k,\kappa,r)$ along the
equilibrium branch. The dominance-and-contraction region $\mathcal R_r$ has slack
$\eta_r=g_r^{PE}-\mathcal B_r^{GE}$ and may be empty.\compatlabel{6}{def:theta}

The engagement component of the premium is built from
$h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$. The kernel satisfies $h\geq0$ and $h(0)=0$, and the
expected engagement-related premium is
\begin{equation}
\label{eq:Dact}
\Dact \;=\; \Delta_m\,\Eop\bigl[h(\mathcal I_H)\bigr] \;\ge\; 0.
\end{equation}
The cell averages are $M_F=\Delta_m\Eop[h\mid D=1]$ and $M_P=\Delta_m\Eop[h\mid D=0]$ when the
corresponding cell has positive mass. The flagged weight is $\Omega=\Prb(D=1)=\Prb(a=1)\omega_a$,
where $\omega_a=\Prb(D=1\mid a=1)$. In the three-point representation, $\bar\pi$ is the upper
support point, not the mean pooled engagement share. The latter is $\kappa$-invariant under the support
restriction and is strictly below $\bar\pi$ away from the degenerate case; it equals $\bar\pi/2$ only
when $A_0=A_1$. Define $\mathcal S=|\partial_\kappa\Dact|$ and
$\mathcal S_P=|\partial_\kappa M_P|$. The chord is
\begin{equation}
\label{eq:chord}
C_h(\bar\pi) \;=\; h(0) \;-\; 2h(\bar\pi/2) \;+\; h(\bar\pi),
\end{equation}
maintained non-positive with $|C_h|$ weakly increasing in $\bar\pi$, and $\Akap$ is the common
derivative of the weights in \eqref{eq:atau}, bounded on $[0,1]$. The weight-effect ratios are
$W_\tau$ and $W_T$, for instance $W_T = (1-\Omega(\tau,5))/(1-\Omega(\tau,10))$, which is at most
$1$ when $\Omega$ rises. The composition-effect ratios are $C_\tau$ and $C_T$, for instance
$C_T = \mathcal S_P(\tau,5)/\mathcal S_P(\tau,10)$, which are unsigned. The margin subscript on a
composition ratio is always written, because $C$ is otherwise overloaded by the chord $C_h$, the
engagement cost $C_j(s)$ and the cells $\mathcal C_F,\mathcal C_P$.\compatlabel{7}{def:premium}

Reading $\bar\pi$ as the mean of the pooled posterior law rather than as its upper support point
forces a point mass at $\bar\pi$ with $\Akap = 0$ and zero interior motion for every kernel. That is
degenerate, and it is excluded throughout.

%==============================================================================
```

## 6. Standing conditions of the proved results

From `proofs/04_inherited.tex`. These are in force in every proved fixed-policy result and
define the objects those results use.

```latex
\subsubsection*{Standing conditions}

The following are in force throughout the subsection.

\begin{enumerate}[label=(S\arabic*),leftmargin=3.0em,itemsep=2pt]
\item \label{p:space} \emph{One probability space.} The primitive vector, the value $v$, the signal
  noise $\varepsilon$, the bidder draw $\xi$ and the noise-trader marks $z_{0:H}$, has a joint law
  on a finite product of Polish spaces, with the noise marks valued in the finite set
  $\{-\bar z,0,+\bar z\}$. The signal is $s = v + \varepsilon$.
\item \label{p:menu} \emph{A finite menu and a finite calendar.} The plan menu $\mathcal J$ is
  finite, the horizon $H$ is finite, and the window margin satisfies $T \in \{1,\dots,H\}$.
\item \label{p:cutoff} \emph{A cutoff selection map.} The signal is carried into a plan by a step
  function $j(\cdot)$ with breakpoints $k_1 \le \dots \le k_{J-1}$.
\item \label{p:paths} \emph{Monotone Voice paths and a clean start.} Each plan $j$ carries a stake
  path $B_j(s,\cdot)$ with $B_j(s,-1) = b_0 < \tau$; for a Voice plan the path is weakly increasing
  in the signal and weakly increasing in the calendar date.
\item \label{p:clock} \emph{Legal-clock discipline.} Only Voice plans cross the threshold; the
  crossing date $c_j(s)$ is the first date at which the path reaches $\tau$, or $+\infty$ if the
  path never reaches it; the filing lands exactly at $f_j = c_j + T$ and only through the disclosure
  node; the filing reports the stake truthfully.
\item \label{p:public} \emph{The flag is public.} Each pooled history carries the coordinate ``the
  filing has landed by date $d$'', and the control-node information set $\mathcal I_H$ contains the
  pooled history up to the control node.
\item \label{p:nofeedback} \emph{No-feedback timing.} The executed path, the order marks, the
  terminal target, the crossing date, the filing date, the filing stake and the flagged order are
  functions of the plan and the signal alone. Neither realised order flow nor a realised price
  enters any of them.
\item \label{p:kernel} \emph{A bounded, pinned kernel.} The engagement-premium kernel is
  $h(\mathcal I) = \pi(\mathcal I)\,p(\mathcal I)$, where the engagement posterior
  $\pi(\mathcal I) = \Prb(a = 1 \mid \mathcal I)$ takes values in $[0,1]$ and the bidder-entry
  probability $p(\mathcal I)$ takes values in $(0,1)$ and is a continuous function of the posterior
  and the price. The pricing rule pins one version of $\Eop[Y \mid \mathcal I]$ rather than an
  equivalence class.
\item \label{p:wedge} \emph{A finite wedge.} The premium wedge $\Delta_m$ is a finite, strictly
  positive constant, and $\Dact = \Delta_m\,\Eop[h(\mathcal I_H)]$.
\item \label{p:kappa} \emph{Liquidity enters in one place.} The intensity $\kappa$ appears in the
  primitives only in the law of the ternary noise mark. The laws of $v$, $\varepsilon$ and $\xi$
  and the remaining constants carry no $\kappa$.
\item \label{p:fixed} \emph{Fixed policies.} The plan menu, the execution policies and the cutoff
  vector $k$ are held fixed in $\kappa$ and held fixed across any two rules compared.
\end{enumerate}
```

## 7. The calibration

From `numerical_v4/params.py`, `numerical_v4/menu.py`, `numerical_v4/policy.py` and the grid
records. A calibration node is a pair (T, τ) with T in {5, 10} and τ one of five values; the
liquidity is κ = 0.5 throughout, H = 10, order size 2.

Parameters: μ_v = 1.0, σ_v = 0.5, σ_ε = 0.5, so σ_s = sqrt(σ_v² + σ_ε²) = 0.7071 and
β = σ_v²/(σ_v² + σ_ε²) = 0.5; bidder σ_ξ = 0.40, S̄ = 1.44, K = 0.15; premia m_0 = 0.10,
m_1 = 0.30, Δ_m = m_1 − m_0 = 0.20, Δ_V = 0.225; κ = 0.5, z̄ = 1 (one noise lump), mark = 2;
stakes b_0 = 0.03, b̄ = 0.10; T = 5 (and 10 for the longer clock), H = 10; menu shape
n_scale = 4.0, γ̄ = 1e-6; engagement cost C_0 = 0.014, χ = 0.5. The signal support used in
computation is μ_v ± 6 σ_s, that is [−3.2426, 5.2426].

Functional forms (pinned in code):
- Terminal Voice target: b*(s) = b_0 + (b̄ − b_0) · g(x), with x = (s − μ_v)/σ_s and
  g(x) = (1 + x/sqrt(1 + x²))/2, the algebraic sigmoid; strictly increasing in s.
- Building count: n(s) = clip(ceil(n_scale · (H + 1) · (1 − g(x))), 1, H + 1), weakly decreasing
  in s; a step function with breakpoints where n_scale · (H + 1) · (1 − g(x)) crosses an integer.
- Voice stake path: B_Voice(s, d) = b_0 + (b*(s) − b_0) · min(1, (d + 1)/n(s)) for d = 0, …, H;
  the order marks are "n(s) ones then zeros" (Γ(x) = 1{x ≥ γ̄}). Exit sells b_0 at date 0 and
  is flat at 0; Hold is flat at b_0. Exit and Hold have identical (all-zero) mark paths.
- Engagement cost, Voice only: C(s) = C_0 · exp(−χ · x).
- Plan payoff at signal s given the market's pricing (a pooled pass at a fixed policy):
  U_j(s) = b_j^term(s) · E[Y | s, j] − trade cost − C_j(s), where trade cost is the sum over
  execution dates of the order times the expected price at that date's public history, and
  E[Y | s, j] combines the bidder-entry probability and the price at the control node
  (the flagged price if the filing lands by H, the pooled expectations otherwise). The Exit
  payoff carries no s.
- Cutoff policy: k = (k_1, k_2) in Θ = {s_lo ≤ k_1 ≤ k_2 ≤ s_hi}: Exit below k_1, Hold on
  [k_1, k_2), Voice at and above k_2. The legal clock: the crossing date c(s) is the first d with
  B_Voice(s, d) ≥ τ; the filing lands at c(s) + T; the flagged cell is the event that it lands by
  H.

The threshold ladder (the five τ values, quantiles 0.1, 0.3, 0.5, 0.7, 0.9 of the baseline
equilibrium's stake-at-filing distribution): τ = 0.09239820, 0.09346756, 0.09453535, 0.09565658, 0.09703177.
The baseline cutoffs the fixed-policy grids freeze: k = (0.9425017267, 1.8484512098),
solved at τ = 0.09453535 (the median), T = 5, κ = 0.5. The solver returns the cutoff pair at
which each adjacent-plan payoff gap crosses zero, iterating the outer map k ↦ (z_EH(k), z_HV(k))
to a cutoff tolerance of 1e-11 and a payoff tolerance of 1e-9 (the P1 gate).

A node's solved candidate at (T = 5, τ = 0.09239820, the first node) is
k̂ = (0.9425042193, 1.8472640726), reached in 264 s with cutoff residual 3.4e-11.

## 8. The record of the attempt

### 8.1 The conditional theorem that was written (verbatim, LaTeX)

From `proofs/05_existence.tex` (written 2026-09-02). An independent attack on the implication
(B1) to (B4) ⇒ equilibrium returned PASS with seven nits and no hole; the nits are in 8.2.

```latex
% =============================================================================
% proofs/05_existence.tex
% Cutoff equilibrium at order size two, conditional on a certified box.
% Statements first, then the proofs.  Assembled into appendix.tex.
% Needs amsmath, amssymb, amsthm and enumitem in the assembling preamble.
% =============================================================================

\providecommand{\Eop}{\mathbb{E}}
\providecommand{\Prb}{\mathbb{P}}
\providecommand{\ind}{\mathbf{1}}
\providecommand{\Tmap}{\mathsf{T}}

\makeatletter
\@ifundefined{c@theorem}{\newtheorem{theorem}{Theorem}}{}
\@ifundefined{c@lemma}{\newtheorem{lemma}{Lemma}}{}
\@ifundefined{c@remark}{\newtheorem{remark}{Remark}}{}
\makeatother

\section{Cutoff equilibrium at order size two}
\label{sec:pf-existence}

\subsection*{Setting and notation}
\label{sec:pf-existence-setup}

Trading occupies dates $d=0,\ldots,H$. After date $H$ a bidder observes the public information set
and enters with probability $p(\mathcal I_H)$. That is the two-round game: a trading round, then a
control round. Noise takes the values $-\bar z$, $0$ and $+\bar z$ with probabilities $\kappa/2$,
$1-\kappa$ and $\kappa/2$. On a building date the engaged blockholder's order is two noise lumps, so
pooled order flow takes five values. The plan menu is Exit, Hold and one Voice family. Exit sells
the initial stake $b_0$ at date $0$ and is idle thereafter; Hold is idle at $b_0$ throughout; Voice
accumulates from $b_0$ to a strictly increasing terminal target $b^*(s)$ in $n(s)$ building dates,
with $n$ a weakly decreasing step function of the signal. Only Voice ever crosses the threshold
$\tau$, and the legal clock reads the crossing off the stake path. There is no feedback from
realised order flow into the executed path.

A cutoff policy is a pair $k=(k_1,k_2)$ in the ordered polytope
\begin{equation}
\label{eq:ex-theta}
\Theta \;:=\; \bigl\{\, (k_1,k_2):\ s_{\mathrm{lo}}\le k_1\le k_2\le s_{\mathrm{hi}} \,\bigr\},
\end{equation}
with Exit on $[s_{\mathrm{lo}},k_1)$, Hold on $[k_1,k_2)$ and Voice on $[k_2,s_{\mathrm{hi}}]$. The
signal is taken on the compact interval $[s_{\mathrm{lo}},s_{\mathrm{hi}}]$ used at the calibration,
with the Gaussian density truncated and renormalised. Write $U_j(s;k)$ for the expected payoff of
plan $j$ at signal $s$ under the price system that $k$ induces, and write the adjacent-plan gaps
\begin{equation}
\label{eq:ex-gaps}
g^{\mathrm{EH}}(s;k) \;:=\; U_{\mathrm{Exit}}(s;k)-U_{\mathrm{Hold}}(s;k),
\qquad
g^{\mathrm{HV}}(s;k) \;:=\; U_{\mathrm{Hold}}(s;k)-U_{\mathrm{Voice}}(s;k).
\end{equation}
Write $\mathcal S_{\mathrm{free}}$ for the finite set of $k$-free breakpoints in
$(s_{\mathrm{lo}},s_{\mathrm{hi}})$: the jump points of $n(s)$, together with the signals at which
the Voice stake path first reaches $\tau$ on some date. Equivalently, $\mathcal S_{\mathrm{free}}$
is the breakpoint set of the menu computed with both cutoffs placed outside the support. These
points do not move with $k$. A \emph{down-crossing} of a gap $g(\cdot;k)$ is a point
$z\in[s_{\mathrm{lo}},s_{\mathrm{hi}}]$ at which $g(s_{\mathrm{lo}};k)\ge 0\ge g(s_{\mathrm{hi}};k)$,
$g(s;k)\ge 0$ for every $s<z$ off $\mathcal S_{\mathrm{free}}$, and $g(s;k)\le 0$ for every $s>z$
off $\mathcal S_{\mathrm{free}}$. The down-crossing is unique when no other point of the interval
satisfies those three properties. The $k$-free set is finite, so this is uniqueness of the sign
change of a function that is continuous in $s$ on the complementary open intervals.

The inner price at a public history solves $P=\Eop[Y\mid\mathcal I]$, equivalently
\begin{equation}
\label{eq:ex-inner}
P \;=\; \bigl(1-p(P)\bigr)\hat V \;+\; p(P)\bigl(P+\tilde m\bigr),
\qquad
p(P) \;=\; 1-\Phi\!\left(\frac{P+K+\tilde m-\bar S}{\sigma_\xi}\right),
\end{equation}
with $\hat V=\hat v+\pi\Delta_V$ and $\tilde m=m_0+\pi\Delta_m$ the belief summaries at that
history. Off-path pooled histories, those that no type selected by $k$ can produce, are priced from
a $k$-independent reference: each empty mark path is assigned the mean fundamental of the $n(s)$
cell that would produce it. Flagged histories are priced from the filing $(B^F,Q^F,a{=}1)$ alone.
The Voice target is
\begin{equation}
\label{eq:ex-bstar}
b^*(s) \;=\; b_0+(\bar b-b_0)\cdot\tfrac12\Bigl(1+\frac{x}{\sqrt{1+x^2}}\Bigr),
\qquad x=(s-\mu_v)/\sigma_s,
\end{equation}
so $b^{*\prime}(s)=\tfrac12(\bar b-b_0)(1+x^2)^{-3/2}/\sigma_s>0$ on the whole line whenever
$\bar b>b_0$ and $\sigma_s>0$. On the flagged cell $B^F+Q^F=b^*(s)$, and the strictly increasing
target therefore pins the signal from the filing. The flagged price at a signal is consequently
well-defined independently of $k$.

Given $k\in\Theta$ at which each gap in \eqref{eq:ex-gaps} has a unique down-crossing, write
$z_{\mathrm{EH}}(k)$ and $z_{\mathrm{HV}}(k)$ for those two points and set
\begin{equation}
\label{eq:ex-T}
\Tmap(k) \;:=\; \bigl(z_{\mathrm{EH}}(k),\, z_{\mathrm{HV}}(k)\bigr)
\end{equation}
when the zeros are ordered $z_{\mathrm{EH}}(k)\le z_{\mathrm{HV}}(k)$. That is the outer map. An
\emph{equilibrium} of the two-round game is a cutoff $k^\star\in\Theta$ at which, under the unique
inner price system induced by $k^\star$ and the on-path Bayes and off-path reference beliefs just
named, the plan that $k^\star$ selects maximises $U_j(s;k^\star)$ at every signal $s$. Equivalently,
$k^\star=\Tmap(k^\star)$, once the ordered unique down-crossings make adjacent indifference global
(Lemma~\ref{lem:ex-global} below).

\subsection*{Conditions}
\label{sec:pf-existence-conditions}

Let $B=[k_1^-,k_1^+]\times[k_2^-,k_2^+]$ be a compact axis-aligned box in the cutoff plane. The four
conditions below are named, and the theorem is conditional on all four.

\begin{enumerate}[label=(B\arabic*),leftmargin=2.6em,itemsep=4pt]
\item \label{cond:B1} \emph{Interior ordered box.} The box sits in the interior of $\Theta$ and is
  strictly ordered:
  \[
  s_{\mathrm{lo}} \;<\; k_1^- \;\le\; k_1^+ \;<\; k_2^- \;\le\; k_2^+ \;<\; s_{\mathrm{hi}}.
  \]
\item \label{cond:B2} \emph{Breakpoint-free Voice coordinate.} The Voice interval of the box is
  disjoint from the $k$-free set: $[k_2^-,k_2^+]\cap\mathcal S_{\mathrm{free}}=\emptyset$.
\item \label{cond:B3} \emph{Unique ordered down-crossings.} At every $k\in B$, each of
  $g^{\mathrm{EH}}(\cdot;k)$ and $g^{\mathrm{HV}}(\cdot;k)$ has a unique down-crossing on
  $[s_{\mathrm{lo}},s_{\mathrm{hi}}]$, and the zeros are ordered
  $z_{\mathrm{EH}}(k)\le z_{\mathrm{HV}}(k)$.
\item \label{cond:B4} \emph{Miranda face signs.} Writing $\Tmap=(\Tmap_1,\Tmap_2)$, the displacement
  $F(k):=\Tmap(k)-k$ points inward on each face of $B$:
  \begin{align}
  \label{eq:ex-miranda}
  \Tmap_1(k_1^-,k_2) &\ge k_1^-
    &&\text{for all }k_2\in[k_2^-,k_2^+],
  \nonumber\\
  \Tmap_1(k_1^+,k_2) &\le k_1^+
    &&\text{for all }k_2\in[k_2^-,k_2^+],
  \\
  \Tmap_2(k_1,k_2^-) &\ge k_2^-
    &&\text{for all }k_1\in[k_1^-,k_1^+],
  \nonumber\\
  \Tmap_2(k_1,k_2^+) &\le k_2^+
    &&\text{for all }k_1\in[k_1^-,k_1^+].
  \nonumber
  \end{align}
\end{enumerate}

\subsection*{Statements}
\label{sec:pf-existence-statements}

\begin{lemma}[Unique inner price]
\label{lem:ex-inner}
Assume $m_0>0$, $\Delta_m>0$ and $\sigma_\xi>0$. Then for every belief pair
$(\hat v,\pi)\in\mathbb R\times[0,1]$ the inner equation \eqref{eq:ex-inner} has a unique real root
$P$, and that root is continuous in $(\hat v,\pi)$.
\end{lemma}

\begin{lemma}[The Exit--Hold gap decreases in the signal]
\label{lem:ex-eh}
Assume $b_0>0$, $\sigma_v>0$, $\sigma_\varepsilon>0$ and the hypotheses of
Lemma~\ref{lem:ex-inner}. At every $k\in\Theta$, the gap $g^{\mathrm{EH}}(\cdot;k)$ is affine and
strictly decreasing on $[s_{\mathrm{lo}},s_{\mathrm{hi}}]$. A unique down-crossing of this gap is
therefore equivalent to the endpoint sign pattern
$g^{\mathrm{EH}}(s_{\mathrm{lo}};k)\ge 0\ge g^{\mathrm{EH}}(s_{\mathrm{hi}};k)$.
\end{lemma}

\begin{lemma}[Ordered adjacent indifference is global]
\label{lem:ex-global}
Fix $k\in\Theta$ at which both gaps have unique down-crossings $z_{\mathrm{EH}}\le z_{\mathrm{HV}}$.
Then, off the finite set $\mathcal S_{\mathrm{free}}$, Exit maximises $U_j(s;k)$ on
$[s_{\mathrm{lo}},z_{\mathrm{EH}}]$, Hold maximises it on $[z_{\mathrm{EH}},z_{\mathrm{HV}}]$, and
Voice maximises it on $[z_{\mathrm{HV}},s_{\mathrm{hi}}]$. The $k$-free set is null for the signal
law. In particular, if $k=\Tmap(k)$, the cutoff policy $k$ is an equilibrium.
\end{lemma}

\begin{theorem}[Cutoff equilibrium on a certified box]
\label{thm:existence}
Fix a disclosure rule $(\tau,T)$ and a liquidity $\kappa\in(0,1)$. Assume $m_0>0$, $\Delta_m>0$,
$\sigma_\xi>0$, $\sigma_v>0$, $\sigma_\varepsilon>0$, and $0<b_0<\tau<\bar b$. Let
$B=[k_1^-,k_1^+]\times[k_2^-,k_2^+]$ be a compact box, and assume (B1)--(B4). Then the outer map
$\Tmap$ is well-defined and continuous on $B$, and there exists $k^\star\in B$ with
$\Tmap(k^\star)=k^\star$. The cutoff $k^\star$, together with the unique inner price system it
induces, is an equilibrium of the two-round game at order size two.
\end{theorem}

\begin{remark}[What a probe grid does and does not show]
\label{rem:ex-probe}
The numerical record in \texttt{numerical\_v4/checks/t5\_existence\_conditions.json} builds, at each
calibration node, a box $B$ about the solver's candidate. It checks (B1) and (B2) on that box, and
it evaluates (B3) and (B4) on the stated $3\times 3$ probe grid on $B$ (the four vertices, the four
face midpoints, and the centre), together with the inner-root certificate of
Lemma~\ref{lem:ex-inner} and the flagged-target slope at those nine points. A calibration node is a
pair $(T,\tau_q)$ with $T\in\{5,10\}$ and $\tau_q$ one of the five frozen quantiles
$(0.1,0.3,0.5,0.7,0.9)$ of the seed equilibrium's Voice $b^*(s)$ distribution, at baseline
$\kappa=0.5$. At each probe the gaps are evaluated on a $2001$-point signal grid. The probe grid is
not a proof of (B3) at every point of $B$, nor of (B4) at every point of each face.
Theorem~\ref{thm:existence} is conditional on (B1)--(B4).
\end{remark}

\subsection*{Proofs}
\label{sec:pf-existence-proofs}

\begin{proof}[Proof of Lemma~\ref{lem:ex-inner}]
Write $\tilde m=m_0+\pi\Delta_m$. The standing signs give $\tilde m\ge m_0>0$ for every
$\pi\in[0,1]$. The entry map $p$ is $C^\infty$ and strictly decreasing, with values in $(0,1)$ at
every finite $P$, because $\sigma_\xi>0$ and $\Phi$ does not attain $0$ or $1$ at a finite argument.
Rearrange \eqref{eq:ex-inner} as $P=\psi(P)$ with
\[
\psi(P) \;:=\; \hat V \;+\; \tilde m\,\frac{p(P)}{1-p(P)}.
\]
The ratio $p/(1-p)$ is strictly increasing in $p\in(0,1)$, hence strictly decreasing in $P$, and
$\tilde m>0$, so $\psi$ is strictly decreasing. The identity map is strictly increasing, so they
cross at most once. For existence: as $P\to-\infty$, $p(P)\to 1$ and $\psi(P)\to+\infty$, so
$\psi(P)>P$; as $P\to+\infty$, $p(P)\to 0$ and $\psi(P)\to\hat V$, so $\psi(P)<P$. Continuity of
$\psi$ on $\mathbb R$ and the two endpoint inequalities give a root, which is unique by the opposite
monotonicities. The unique root of a continuous function that is strictly increasing in $P$ (namely
$P-\psi(P)$) and jointly continuous in $(P,\hat v,\pi)$ varies continuously with $(\hat v,\pi)$.
\end{proof}

\begin{proof}[Proof of Lemma~\ref{lem:ex-eh}]
Exit and Hold share the idle mark path, so both are priced off the same pooled histories. Exit has
terminal stake $0$ and sells $b_0$ at date $0$, hence
$U_{\mathrm{Exit}}(s;k)=b_0\,\Eop[P_0^P\mid \text{idle}]$, a number that does not depend on $s$.
Hold has terminal stake $b_0$, makes no trade, and carries $a=0$, so
\[
U_{\mathrm{Hold}}(s;k)
 \;=\; b_0\Bigl(
   \bigl(1-\Eop[p_H]\bigr)\bigl(\mu_v+\beta(s-\mu_v)\bigr)
   +\Eop[p_H P_H]
   +\Eop[p_H]\,m_0
 \Bigr),
\]
with $\beta=\sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)\in(0,1)$ and with $(p_H,P_H)$ the
control-node entry probability and price along the idle path, both independent of $s$. Lemma~\ref{lem:ex-inner}
puts every inner price at a finite value, so $p_H\in(0,1)$ and $\Eop[p_H]\in(0,1)$. Therefore
\[
g^{\mathrm{EH}}(s;k)
 \;=\; C(k) \;-\; b_0\bigl(1-\Eop[p_H]\bigr)\beta\, s
\]
for a constant $C(k)$ in $s$. The coefficient of $s$ is strictly negative, so the gap is affine and
strictly decreasing. A strictly decreasing continuous function of one variable has a unique
down-crossing on a compact interval if and only if it is nonnegative at the left endpoint and
nonpositive at the right endpoint.
\end{proof}

\begin{proof}[Proof of Lemma~\ref{lem:ex-global}]
Write $z_1=z_{\mathrm{EH}}$ and $z_2=z_{\mathrm{HV}}$, with $z_1\le z_2$ by hypothesis, and suppress
$k$. Unique down-crossing of $g^{\mathrm{EH}}$ gives $U_{\mathrm{Exit}}\ge U_{\mathrm{Hold}}$ on
$[s_{\mathrm{lo}},z_1]$ and $U_{\mathrm{Hold}}\ge U_{\mathrm{Exit}}$ on $[z_1,s_{\mathrm{hi}}]$.
Unique down-crossing of $g^{\mathrm{HV}}$ gives $U_{\mathrm{Hold}}\ge U_{\mathrm{Voice}}$ on
$[s_{\mathrm{lo}},z_2]$ and $U_{\mathrm{Voice}}\ge U_{\mathrm{Hold}}$ on $[z_2,s_{\mathrm{hi}}]$.

On $[s_{\mathrm{lo}},z_1]$ one has $s\le z_1\le z_2$, so $U_{\mathrm{Exit}}\ge U_{\mathrm{Hold}}\ge
U_{\mathrm{Voice}}$. On $[z_1,z_2]$ one has $s\ge z_1$ and $s\le z_2$, so
$U_{\mathrm{Hold}}\ge U_{\mathrm{Exit}}$ and $U_{\mathrm{Hold}}\ge U_{\mathrm{Voice}}$. On
$[z_2,s_{\mathrm{hi}}]$ one has $s\ge z_2\ge z_1$, so $U_{\mathrm{Voice}}\ge U_{\mathrm{Hold}}\ge
U_{\mathrm{Exit}}$. The three comparisons are on the complement of $\mathcal S_{\mathrm{free}}$,
where the gaps are continuous in $s$. At each such signal a maximiser is the plan the ordered
cutoffs $(z_1,z_2)$ select, with indifference between adjacent plans at the two cutoffs themselves.
If $k=\Tmap(k)$, then $(k_1,k_2)=(z_1,z_2)$ and the cutoff policy is an equilibrium.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:existence}]
\emph{Step 1 (inner prices).} Lemma~\ref{lem:ex-inner} supplies a unique inner price at every public
history, flagged or pooled, continuously in the belief summaries. The standing signs $m_0>0$ and
$\Delta_m>0$ make $\tilde m>0$ at every posterior engagement share, and $\sigma_\xi>0$ makes the
entry map strictly monotone, so uniqueness is not a property of $B$: it holds at every $k\in\Theta$.

\emph{Step 2 ($\Tmap$ is well-defined on $B$).} Condition (B3) gives, at every $k\in B$, unique
down-crossings of both gaps with $z_{\mathrm{EH}}(k)\le z_{\mathrm{HV}}(k)$. The right-hand side of
\eqref{eq:ex-T} is therefore a single point of $\Theta$, and $\Tmap:B\to\Theta$ is well-defined.
Lemma~\ref{lem:ex-eh} records that the Exit--Hold half of (B3) is the endpoint sign pattern of an
affine gap; the Hold--Voice half is the content of (B3) that is not supplied by the menu.

\emph{Step 3 (type masses are continuous on $B$, and the populated type set is constant).} The
$k$-free set $\mathcal S_{\mathrm{free}}$ is finite, hence closed. Condition (B2) says that the
compact interval $[k_2^-,k_2^+]$ is disjoint from it, so the two are a positive distance apart.
Condition (B1) puts $k_1^+<k_2^-$, so as $k$ ranges over $B$ the Voice region $[k_2,s_{\mathrm{hi}}]$
gains or loses only signals in $[k_2^-,k_2^+]$, none of which is an $n$-jump or a $\tau$-crossing
pull-back. The Voice types that carry positive mass are therefore the same at every $k\in B$: the
lowest Voice atom is $[k_2,s_{\mathrm{next}})$, where $s_{\mathrm{next}}$ is the next point of
$\mathcal S_{\mathrm{free}}\cup\{s_{\mathrm{hi}}\}$ above $k_2^+$, and every $n$-plateau lying
entirely above $s_{\mathrm{next}}$ is included in full. Type $0$, the idle path shared by Exit and
Hold, occupies $[s_{\mathrm{lo}},k_2)$ and has mass at least the Gaussian mass of
$[s_{\mathrm{lo}},k_2^-)$, which is positive by (B1). Types whose $n$-plateau lies entirely below
$k_2^-$ are empty throughout $B$, and their beliefs are the constant reference. Each populated
type's mass and truncated mean fundamental are Gaussian cdf and truncated-mean evaluations at
endpoints that are either fixed ($k$-free breakpoints, $s_{\mathrm{lo}}$, $s_{\mathrm{hi}}$) or
equal to $k_1$ or $k_2$. Those evaluations are continuous in $k$ on $B$, and the masses of
populated types are bounded away from zero on the compact box.

\emph{Step 4 (prices and payoffs are continuous in $k$).} At a pooled history the posterior
summaries $(\hat v,\pi)$ are ratios of linear forms in the type masses, with likelihoods that do not
depend on $k$. On histories feasible for a populated type the denominator is bounded away from zero
on $B$ by Step~3. On histories feasible only for types empty throughout $B$ the summaries equal the
$k$-independent reference. In both cases $(\hat v,\pi)$ is continuous in $k$ on $B$. Step~1 upgrades
that to continuity of every inner price. Expected execution prices along each mark path are finite
sums of those inner prices against $k$-free likelihoods, hence continuous in $k$. For each plan $j$
and each signal $s\notin\mathcal S_{\mathrm{free}}$, the stake path, the mark path, the clock and the
engagement cost are locally constant in $s$ and independent of $k$, so $U_j(s;k)$ is continuous in
$k$ on $B$. (The flagged price at a given $s$ is itself $k$-free, by injectivity of $b^*$,
and the remaining $k$-dependence is a continuous pre-filing trade cost.) Consequently both gaps in
\eqref{eq:ex-gaps} are continuous in $k$ at every $s\notin\mathcal S_{\mathrm{free}}$.

\emph{Step 5 ($\Tmap$ is continuous on $B$).} Let $k^n\to k$ in $B$ and write
$z^n=z_{\mathrm{EH}}(k^n)$. The sequence $z^n$ lives in the compact interval
$[s_{\mathrm{lo}},s_{\mathrm{hi}}]$, so a subsequence $z^{n_j}$ converges to some
$z_\infty$ in that interval. For any $s<z_\infty$ with $s\notin\mathcal S_{\mathrm{free}}$, one has
$s<z^{n_j}$ for large $j$, hence $g^{\mathrm{EH}}(s;k^{n_j})\ge 0$, and Step~4 passes to the limit
$g^{\mathrm{EH}}(s;k)\ge 0$. For any $s>z_\infty$ off $\mathcal S_{\mathrm{free}}$, the same
argument gives $g^{\mathrm{EH}}(s;k)\le 0$. The finite set $\mathcal S_{\mathrm{free}}$ is excluded from the down-crossing definition, so
$z_\infty$ is a down-crossing of $g^{\mathrm{EH}}(\cdot;k)$. Condition (B3) says that
down-crossing is unique, hence $z_\infty=z_{\mathrm{EH}}(k)$. Every convergent subsequence of $z^n$ has this same limit, so
$z_{\mathrm{EH}}(k^n)\to z_{\mathrm{EH}}(k)$. The identical argument with $g^{\mathrm{HV}}$ gives
continuity of $z_{\mathrm{HV}}$. Thus $\Tmap$ is continuous on $B$.

\emph{Step 6 (Miranda's theorem).} The box $B$ is a product of two compact intervals of positive
length, by (B1). Define $G(k):=k-\Tmap(k)$, continuous on $B$ by Step~5. Condition (B4) is exactly
the classical face-sign pattern for $G$: $G_1\le 0$ on the face $k_1=k_1^-$, $G_1\ge 0$ on the face
$k_1=k_1^+$, $G_2\le 0$ on the face $k_2=k_2^-$, and $G_2\ge 0$ on the face $k_2=k_2^+$. Miranda's
theorem (the intermediate-value theorem on a product of compact intervals) therefore supplies a
point $k^\star\in B$ with $G(k^\star)=0$, that is $\Tmap(k^\star)=k^\star$. The argument uses that
$\Tmap$ is a well-defined continuous map on the compact rectangle $B$. It does not require
$\Tmap(B)\subseteq B$.

\emph{Step 7 (the fixed point is an equilibrium).} The point $k^\star$ lies in $B\subset\Theta$. At
$k^\star$ the two unique down-crossings are the coordinates of $k^\star$ itself, and they are
ordered by (B3). Lemma~\ref{lem:ex-global} upgrades adjacent indifference to global optimality of
the selected plan at every signal off the null $k$-free set. The inner price system is unique by Step~1, on-path beliefs are
Bayes from the type masses of $k^\star$, and off-path beliefs are the model's $k$-independent
reference. This is an equilibrium of the two-round game at order size two.
\end{proof}

```

### 8.2 The attack's nits on 8.1

Not holes; recorded so that a new proof does not inherit them. (1) (B1) allows a degenerate box
while Step 6 claims positive length. (2) Equilibrium is defined at every signal but proved off
the null k-free set. (3) Step 5 omits the endpoint clause g(s_lo; k) ≥ 0 ≥ g(s_hi; k), which
follows from Step 4. (4) Step 4 calls the posterior summaries ratios of linear forms with k-free
likelihoods; the numerators also carry truncated means, which move with the cutoffs, and the
sentence about the stake path being locally constant in s is wrong (b*(s) is not; what is needed
is that it is free of k). (5) Step 1's pricing convention for pre-control dates should be stated.
(6) σ_s is used and never defined; κ in (0, 1) is assumed and never cited, though it keeps every
order-flow likelihood positive. (7) Lemma ex-global's closed intervals at a crossing inside S_free.

### 8.3 What the condition check found at the first node

Script `numerical_v4/checks/t5_existence_conditions.py`, node (T = 5, τ = 0.09239820), κ = 0.5,
box of half-width 0.002 around k̂, nine probes on a 3 × 3 grid of the box, signal grid of 2001
points. (B1) holds; (B2) holds (fourteen k-free breakpoints on the support, the nearest 0.013564
above the box's Voice coordinate); (B3) fails at all nine probes: the Exit-Hold gap has one sign
change, the Hold-Voice gap has three, so z_HV is undefined; (B4) fails as a consequence. The
inner price residual is 1.5e-16 with no multiple roots. The A7 certificate (minimum slope of the
flagged-posterior map, 2.2e-4) passes.

An independent judge then recomputed the Hold-Voice gap g(s) = U_Hold(s) − U_Voice(s) along the
signal at the candidate k̂ with one pooled pass (16 s; the record's endpoint values reproduce
exactly: g(s_lo) = +0.29779233, g(s_hi) = −0.15891846). Findings:

- g is a falling sawtooth: it declines on each plateau of n(s) and jumps up at each plateau edge,
  because U_Voice steps down at every decrement of n(s).
- On the 32001-point grid there are three sign changes; the same three appear at 2001 and 8001
  points; bisection to machine precision locates them at s = 1.8472640726 (a continuous crossing,
  the candidate k_2 to 3.4e-11), s = 1.8608284620 (a jump of +6.487e-4 at the k-free breakpoint
  where n goes from 6 to 5; g is −5.789e-4 just below and +6.98e-5 just above), and
  s = 1.8624646978 (a continuous crossing back down). The island on which Hold is again preferred
  has width 1.636e-3 and prior mass 4.4e-4. The plateau decline (slope −0.04261 times the plateau
  width 0.013564 gives −5.779e-4) is smaller than the breakpoint jump, which is why g returns
  above zero. The island's peak, 6.98e-5, is 1.8e-3 of the payoff level 0.0382 at the cutoff and
  7e4 times the 1e-9 payoff tolerance.
- The Exit-Hold gap has exactly one sign change (at 0.9425, the candidate k_1); it is affine and
  strictly decreasing in s with slope −0.005853.
- The solver's "payoff_scale 0.0" at k̂ is a coarse-grid effect: its 241-point deviation grid
  steps 0.0354 and steps over the 0.0016-wide island. The true adjacent-plan deviation at k̂ is
  7.0e-5, so the candidate is not an equilibrium at the P1 tolerance.
- (B2) clears only the box's own Voice coordinate; the breakpoint that breaks single crossing sits
  0.0136 above the box, so (B2) can hold while (B3) fails.

The gap g on each plateau of n(s) at k̂, sampled at 2, 25, 50, 75 and 98 percent of the plateau
(positive means Hold preferred; "filing lands by H" is the flagged cell):

| s from | s to | n(s) | filing lands by H | g at 2% | 25% | 50% | 75% | 98% |
|---|---|---|---|---|---|---|---|---|
| -3.242641 | 0.942504 | 11 | 0 | +2.812e-01 | +1.458e-01 | +7.094e-02 | +3.400e-02 | +1.938e-02 |
| 0.942504 | 1.408248 | 11 | 0 | +1.826e-02 | +1.671e-02 | +1.459e-02 | +1.199e-02 | +9.204e-03 |
| 1.408248 | 1.460179 | 11 | 0 | +8.918e-03 | +8.585e-03 | +8.218e-03 | +7.848e-03 | +7.504e-03 |
| 1.460179 | 1.517932 | 10 | 0 | +7.937e-03 | +7.471e-03 | +6.960e-03 | +6.444e-03 | +5.965e-03 |
| 1.517932 | 1.583333 | 9 | 0 | +7.506e-03 | +6.950e-03 | +6.341e-03 | +5.725e-03 | +5.153e-03 |
| 1.583333 | 1.659062 | 8 | 0 | +6.782e-03 | +6.113e-03 | +5.379e-03 | +4.638e-03 | +3.950e-03 |
| 1.659062 | 1.749269 | 7 | 0 | +5.733e-03 | +4.905e-03 | +3.996e-03 | +3.079e-03 | +2.228e-03 |
| 1.749269 | 1.847264 | 6 | 0 | +4.038e-03 | +3.101e-03 | +2.074e-03 | +1.041e-03 | +8.349e-05 |
| 1.847264 | 1.860828 | 6 | 0 | -1.156e-05 | -1.445e-04 | -2.892e-04 | -4.340e-04 | -5.673e-04 |
| 1.860828 | 1.889535 | 5 | 0 | +4.534e-05 | -2.367e-04 | -5.437e-04 | -8.512e-04 | -1.135e-03 |
| 1.889535 | 2.006231 | 5 | 1 | -1.254e-03 | -2.384e-03 | -3.623e-03 | -4.873e-03 | -6.032e-03 |
| 2.006231 | 2.211396 | 4 | 1 | -5.898e-03 | -7.955e-03 | -1.022e-02 | -1.250e-02 | -1.461e-02 |
| 2.211396 | 2.543033 | 3 | 1 | -1.523e-02 | -1.868e-02 | -2.246e-02 | -2.627e-02 | -2.979e-02 |
| 2.543033 | 3.264488 | 2 | 1 | -3.219e-02 | -3.988e-02 | -4.825e-02 | -5.661e-02 | -6.428e-02 |
| 3.264488 | 3.460075 | 1 | 1 | -6.935e-02 | -7.142e-02 | -7.368e-02 | -7.593e-02 | -7.801e-02 |
| 3.460075 | 4.565394 | 1 | 1 | -7.920e-02 | -9.086e-02 | -1.035e-01 | -1.160e-01 | -1.275e-01 |
| 4.565394 | 5.242641 | 1 | 1 | -1.291e-01 | -1.361e-01 | -1.437e-01 | -1.513e-01 | -1.583e-01 |

Payoff levels at k̂ at five signals (U_Exit is constant, 0.032929):

| s | U_Hold | U_Voice | n(s) | b*(s) |
|---|---|---|---|---|
| −3.242641 | 0.008432 | −0.289360 | 11 | 0.030476 |
| 0.942504 (k_1) | 0.032929 | 0.014545 | 11 | 0.062163 |
| 1.847264 (k_2) | 0.038225 | 0.038225 | 6 | 0.091871 |
| 3.544952 | 0.048162 | 0.130249 | 1 | 0.098723 |
| 5.242641 | 0.058099 | 0.217017 | 1 | 0.099524 |

The other four T = 5 nodes and the five T = 10 nodes were not run; the rule is that a hypothesis
failing at any node makes the result absent, and it fails at the first.

## 9. What a script can compute at a node

The project's code evaluates the model at a fixed cutoff policy k and parameter set in about ten
seconds and six gigabytes (a "pooled pass"): the law of the pooled order-flow history at every
date, the market's posterior and price at every public history (the inner price is the unique
root of a scalar equation, residual 1e-16), the flagged price, the bidder-entry probability, the
plan payoffs U_j(s) at any list of signals, the cell masses Ω and the premium objects. A cold
policy solve (the outer map iterated to the tolerances above) takes about four minutes. A
hypothesis that reduces to finitely many such evaluations at a node, with a stated tolerance, is
checkable. A hypothesis that needs the payoff gap on a continuum of signals or of policies is
checkable only through a reduction the proof supplies (a bound, a monotonicity, a finite set of
breakpoints, a certificate). The k-free breakpoints of n(s) and of the legal clock are computable
in closed form; the cutoffs k add their own.

## 10. For the session that receives the answer

The answer is input, not authority: it lands at `.scratch/v5-paper/external/gpt-sol-existence.md`,
enters as CONJECTURE, and reaches the paper only through the attack gate (an independent Opus
attacker, then a condition script run at every node, then the author's decision on the notion).
Suggested skills for that session: `writing-for-agents` for the attack brief, `unslop` for any
prose that moves toward the paper.
