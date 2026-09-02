# Handoff 3: rank three theory upgrades for "Who Gets Caught" and sketch their proofs

Prepared 2026-09-02 by the orchestrating session of the paper *Who Gets Caught: Blockholder
Disclosure Rules and Market Inference* (worktree `blockholder_v5`, branch `v5`). The reader of
this document has no access to the worktree and no earlier exchange with us; everything needed
is inline. Each section names the file it was taken from, for the session that receives the
answer.

## 1. Objective

Three candidate results, each already written up by one worker and read by an independent
attacker from another model family (section 9 has both texts verbatim). We want two things from
a fresh reader.

First, a ranking of the three by what they are worth to the paper, with reasons a referee would
accept. Second, for each candidate, a proof sketch at the level the paper's appendix needs: the
cleanest statement (sharper than the worker's where you can make it so), the argument in steps
with the load-bearing hypothesis named at the step that consumes it, the weakest step, and what
a referee would attack first. The sketches are what we will write the appendix from, so
economy and exactness matter more than length.

The paper is a fixed-policy paper. Every headline result compares two disclosure rules with the
blockholder's plan held fixed (standing condition (S11) in section 6). The calibration's policy
is a benchmark policy, the solver's baseline cutoffs; it is not an equilibrium of the paper's
game, and section 4.3 gives the certified regret numbers. No candidate needs an equilibrium, and
none is to be proved by way of one.

## 2. Constraints

- The primitives are fixed as sections 5 and 7 state them: the menu, the stake paths, the
  building count n(s), the ternary noise law, the pricing rule, the bidder, the order size of two
  noise lumps, and the parameter values. Candidate 4.1 varies the order size on purpose; nothing
  else varies a primitive.
- Every hypothesis is stated, numbered in the standing-condition scheme of section 6 where it is
  one of them and named where it is new. Two assumptions the paper dropped stay out of every
  proof: the ternary pooled law of order size one (except as the b = 1 case of candidate 4.1),
  and any support assumption on the pooled posterior.
- A hypothesis quantified over a continuum (of signals, of policies, of kappa) is proved from the
  primitives, or is reduced to finitely many computations at a calibration node with the
  reduction proved and a tolerance stated. Section 10 says what a script can compute at a node.
- Finite Blackwell comparisons are established by an explicit Markov kernel and refuted by an
  explicit decision problem or finite linear program.
- Anything not proved is labelled as such. The paper carries three labels, PROVED, NUMERICAL
  (verified on a stated grid) and ESTIMATED; a working conjecture is labelled CONJECTURE. Nothing
  in the answer awards a label; it says which label a result would support.
- The answer is in the notation of sections 5 to 8. LaTeX is welcome.

## 3. What to return

Three deliverables, in this order.

**Deliverable A: the ranking.** Order the three candidates by value to the paper. For each,
one paragraph: what it lets the paper say that it cannot say now, what it costs in pages and
in hypotheses, and the referee's first objection. Say whether any of the three should be
dropped or merged, and whether the three together support the two-dial framing of section 4.1
better in some other order of presentation.

**Deliverable B: the proof sketches.** For each candidate, in ranking order:
1. The statement, with the full hypothesis list, in the form you would print. Where the
   worker's statement can be sharpened, simplified, or given fewer hypotheses, do it and say
   what changed and why.
2. The proof sketch in numbered steps. At each step name the hypothesis it consumes. Where a
   step is a citation to an existing result in section 8, cite it by label and say what it
   supplies.
3. The weakest step, and the attacker's nits (section 9) you would act on versus ignore.
4. What a referee attacks first, and the one-line answer.
5. "What a script computes at a node", if anything: each item a formula in the objects of
   section 10 with the tolerance the proof needs.

**Deliverable C: holistic comments.** As a top-journal referee and as a co-author: whether the
paper should present the Blackwell order before the sensitivity results or after; whether the
unified cut identity (4.2) should replace the present two-corollary presentation or sit beside
it; whether the erasure proposition (4.1) belongs in the model section or the appendix; what a
referee says first about a fixed-policy paper calibrated at a benchmark that is not an
equilibrium, given the regret numbers in section 4.3; anything in sections 5 to 9 that looks
wrong.

## 4. The paper, the labels, and the benchmark

### 4.1 The paper in brief

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

Labels now (from `grok/checkpoint-1.md`, 2026-09-02). PROVED: the partition and factorisation,
the flagged cell's kappa-invariance, the garbling lemma, the threshold weight leg and the closed
form of S_P in kappa, the clock dial, the who-gets-caught identity and characterisation.
NUMERICAL: the threshold composition leg on the grid kappa in [0.15, 0.85] at order size two,
H = 10 (Condition D fails just below the grid, on the T = 5 pair quantile 0.5 to quantile 0.3 for
kappa in [0.1440, 0.1485], so no "for every kappa" claim is made); any directional
who-gets-caught sentence off the five-node grid record. ESTIMATED: E1 (stake at filing).
ABSENT: existence, and E2. Two grid facts that matter for candidate 4.2: the curvature
hypothesis of Lemma g3(c) (section 8) fails at every calibration node, and the kappa-free
sufficient form of Remark rem:g-Dstar holds at no threshold pair, because the top coefficients
c_k change sign. The garbling machinery is a proved result in its own right and contributes to
neither leg on this grid.

### 4.2 The labels the candidates would support

The candidates of section 9 would support: 4.3 PROVED (a theorem with an explicit kernel);
4.1 PROVED (a proposition beside Lemma g1); 4.2 Part 1 PROVED and Part 2 an implication PROVED
with a calibration check that is NUMERICAL. Labels are set by the paper's orchestrator at a
checkpoint after the attack gate; the memos and this document award none.

### 4.3 The benchmark policy is not an equilibrium, and how far from one it is

The paper's benchmark policy is the baseline cutoffs k = (0.9425017267, 1.8484512098), solved at
the median threshold and T = 5 and frozen at every node; the paper states every result at that
fixed policy and never calls it an equilibrium. At the first calibration node the solver's own
candidate assigns Voice to a signal island (1.8608, 1.8625) of prior mass 4.4e-4 that strictly
prefers Hold by up to 7.0e-5, so the cutoff PBE the solver targets is not attained there; the
Hold-Voice payoff gap is a falling sawtooth in the signal (it declines on each plateau of n(s)
and jumps up at each plateau edge, because the Voice payoff steps down at every decrement of
n(s)), and the solver's 241-point deviation grid stepped over the island.

A certified record now bounds the benchmark's maximal interim regret at every node. Regret at a
signal s is max over the three plans of U_j(s) minus the payoff of the plan the benchmark
assigns, at the price system the benchmark induces; the bound is a proved piecewise Lipschitz
cover on the breakpoint partition of the signal line (mesh width 1e-5, analytic derivative
bounds, 5e-12 float allowance), independently judged and reproduced at one node bit for bit.
The certified bounds are, at T = 5 across the five thresholds, 9.6e-5, 1.6e-4, 1.9e-4, 2.1e-4,
2.2e-4, and at T = 10 (the corner T = H) 2.4e-4 at every threshold. The maximum sits at every
node just to the right of the n(s) jump at s = 1.8608, where Voice is assigned and Hold is
better. For scale, the payoff level at the Hold-Voice cutoff is 0.038, so the largest regret is
about 0.6 per cent of it. This record is not one of the three candidates below; it is context
for Deliverable C.

### 4.4 How the three candidates were produced and checked

Each candidate was posed as a conjecture (its text is reproduced under "The conjecture as first
posed"), given to one worker with the objective and the constraints but no method, and written
up as a memo with a statement, a proof, a node computation and a cost. An independent attacker
from a different model family then read the memo and tried to break it, recomputing what it
doubted; its verdict and nits are reproduced verbatim. All three passed. You are a third,
independent reader. Treat the memos and verdicts as input, not authority.

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

## 8. The proofs the candidates build on (verbatim, LaTeX)

Three files from `proofs/`. The first two are reproduced in full; from the third, the
statements only (its standing conditions are section 6, its proofs are not needed for the
candidates beyond what the statements carry).

### 8.1 `proofs/02_garbling.tex` (in full)

```latex
% =============================================================================
% proofs/02_garbling.tex
% The garbling lemma at order size two and the threshold dial.
% Statements first, then the proofs.  Assembled into appendix.tex.
% Needs amsmath, amssymb, amsthm and enumitem in the assembling preamble.
% =============================================================================

\providecommand{\Eop}{\mathbb{E}}
\providecommand{\Prb}{\mathbb{P}}
\providecommand{\ind}{\mathbf{1}}
\providecommand{\Dact}{\Delta^{\mathrm{act}}}
\providecommand{\Wrev}{\mathcal{W}}
\providecommand{\Grev}{\mathcal{G}}

\makeatletter
\@ifundefined{c@theorem}{\newtheorem{theorem}{Theorem}}{}
\@ifundefined{c@lemma}{\newtheorem{lemma}{Lemma}}{}
\@ifundefined{c@condition}{\newtheorem{condition}{Condition}}{}
\@ifundefined{c@remark}{\newtheorem{remark}{Remark}}{}
\makeatother

\section{Order size two: the pooled experiment and the threshold dial}
\label{sec:pf-garbling}

\subsection*{Setting and notation}
\label{sec:pf-garbling-setup}

Trading runs over rounds $d = 0,\ldots,H$. Noise takes the values $-\bar z$, $0$ and $+\bar z$
with probabilities $\kappa/2$, $1-\kappa$ and $\kappa/2$. The blockholder's order while she is
building the stake is two noise lumps, so the pooled order mark is $q_{jd}(s) \in \{0, 2\bar z\}$
and pooled order flow is $X_d = q_{jd}(s) + z_d$. The support of $X_d$ is
$\{-\bar z, 0, \bar z, 2\bar z, 3\bar z\}$: a round in which the blockholder buys, an
\emph{active} round, produces $X_d \in \{\bar z, 2\bar z, 3\bar z\}$, and a round in which she
does not, an \emph{idle} round, produces $X_d \in \{-\bar z, 0, \bar z\}$. The two supports meet
at $\bar z$ and nowhere else. Write
\begin{equation}
\label{eq:g-eps}
\varepsilon \;:=\; \kappa/2 \;\in\;(0,\tfrac12) \qquad\text{for }\kappa\in(0,1).
\end{equation}

Policies are fixed throughout: the plan menu, the cutoff vector and the execution paths are held
at one setting while the disclosure rule $(\tau,T)$ moves. Let $\theta$ denote the blockholder's
type, the pair of plan and signal, and let
\[
m_d(\theta) \;\in\; \{0,\,2\bar z\}, \qquad d = 0,\ldots,H,
\]
be its mark path, equal to $2\bar z$ on the rounds in which the plan buys and $0$ elsewhere. The
mark path is a deterministic function of the type and takes finitely many values. The disclosure
indicator $D(\theta) = \ind\{a(\theta) = 1,\ c(\theta;\tau) + T \le H\}$ is a function of the type
alone, because the stake path does not respond to realised order flow and the crossing date reads
off that path. Write $\rho$ for the prior law of $\theta$, $\Omega(\tau,T) = \Prb(D=1)$ for the
flagged weight, and
\[
\rho_P^{\tau,T} \;:=\; \rho(\,\cdot \mid D = 0\,)
\]
for the pooled type law, which does not depend on $\kappa$.

The kernel is $h(\mathcal I) = \pi(\mathcal I)\,p(\mathcal I)$, with $\pi$ the engagement
posterior and $p$ the entry probability. The price and the entry probability at an information
set are pinned by the posterior engagement share $\pi$ and the posterior mean $\hat v$ of the
fundamental, so
\begin{equation}
\label{eq:g-kernel}
h(\nu) \;=\; \mathsf h\bigl(\pi(\nu),\,\hat v(\nu)\bigr),
\end{equation}
where $\nu$ is the posterior over types and $\pi(\nu)$, $\hat v(\nu)$ are both linear in $\nu$.
The map $\mathsf h$ itself carries no $\kappa$: $\kappa$ enters $h(\nu)$ only through the
posterior $\nu$. Lemma~\ref{lem:g3}(a) rests on that, treating each $\Grev(S)$ as a
$\kappa$-free number. A curvature statement about $h$ is read as a statement about $\mathsf h$
on the convex hull of the pairs $(\pi,\hat v)$ the pooled cell generates. The premium objects are
$\Dact = \Delta_m \Eop[h(\mathcal I_H)]$, $M_F = \Delta_m \Eop[h \mid D=1]$,
$M_P = \Delta_m \Eop[h \mid D=0]$, and the sensitivities are
$\mathcal S = |\partial_\kappa \Dact|$ and $\mathcal S_P = |\partial_\kappa M_P|$. For a
threshold pair $\tau' < \tau$ at a common window,
\[
W_\tau \;=\; \frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)},
\qquad
C_\tau \;=\; \frac{\mathcal S_P(\tau',T)}{\mathcal S_P(\tau,T)} .
\]

For a set of rounds $S$, the \emph{$S$-record} is the pair
$\bigl(S,\ (m_e(\theta))_{e \in S}\bigr)$; Lemma~\ref{lem:g1}(b) shows that the pooled history
determines it. Finally, call an event $\mathcal A$ a \emph{cell event} when it is determined by
the type alone, so that conditioning on it leaves the noise law untouched. The pooled cell
$\{D = 0\}$ is a cell event, and so is the event that the filing has not landed by a date $d$.
For a cell event $\mathcal A$ write $\rho_{\mathcal A} := \rho(\,\cdot \mid \mathcal A\,)$.

\subsection*{Statements}
\label{sec:pf-garbling-statements}

\begin{lemma}[Erasure form of the pooled experiment]
\label{lem:g1}
Fix a policy $(\tau,T)$, a depth $d \le H$ and $\kappa \in (0,1)$, and let
\[
R_d \;:=\; \{\, e \le d \;:\; X_e \neq \bar z \,\}
\]
be the set of rounds whose flow differs from one lump. Then:
\begin{enumerate}[label=(\alph*),leftmargin=2.4em,itemsep=3pt]
\item $\Prb(X_e = \bar z \mid \theta) = \varepsilon$ for every type and every round, so the value
  $\bar z$ carries likelihood ratio one across types and its probability rises with $\kappa$;
  consequently $R_d$ is independent of $\theta$ and each round belongs to it independently with
  probability $1-\varepsilon$;
\item on $\{R_d = S\}$ the flow determines $m_e(\theta)$ for every $e \in S$, and conditional on
  the $S$-record the law of $X_{0:d}$ does not depend on $\theta$;
\item consequently the $S$-record is sufficient: for every cell event $\mathcal A$ the posterior
  after observing $X_{0:d}$ on $\mathcal A$ is
  \[
  \nu_{0:d} \;=\; \rho_{\mathcal A}\bigl(\,\cdot \mid (m_e)_{e \in R_d}\,\bigr),
  \]
  and in particular the pooled posterior at the control node takes this form with
  $\mathcal A = \{D=0\}$ and $d = H$.
\end{enumerate}
\end{lemma}

\begin{lemma}[Liquidity garbles the pooled experiment]
\label{lem:g2}
Fix a policy and a depth $d \le H$, and let $0 < \kappa < \kappa' < 1$. There is a Markov kernel
$\Lambda$ from histories to histories, not depending on the type, such that for every type
$\theta$ the image under $\Lambda$ of the law of $X_{0:d}$ at $\kappa$ is its law at $\kappa'$.
One such kernel deletes each element of $R_d$ independently with probability
$(\kappa'-\kappa)/(2-\kappa)$, emits $\bar z$ on every deleted round and on every round outside
$R_d$, and redraws the flow on the surviving rounds from the $\kappa'$ conditional law given the
mark. The pooled experiment at $\kappa'$ is therefore a garbling of the pooled experiment at
$\kappa$, and the law of the pooled posterior at $\kappa'$ is a mean preserving contraction of
its law at $\kappa$.
\end{lemma}

\begin{lemma}[Exact liquidity representation of the pooled premium]
\label{lem:g3}
Fix a policy $(\tau,T)$, a cell event $\mathcal A$ of positive prior mass and a depth $d \le H$.
For $S \subseteq \{0,\ldots,d\}$ define
\begin{equation}
\label{eq:g-G}
\Grev^{\,\mathcal A, d}(S) \;:=\;
\Eop_{\rho_{\mathcal A}}\Bigl[\, h\bigl(\rho_{\mathcal A}(\,\cdot \mid (m_e)_{e\in S})\bigr)
\,\Bigr],
\end{equation}
a number that does not depend on $\kappa$. The three parts below are written for the pooled cell
at the control node, $\mathcal A = \{D=0\}$ and $d = H$, where
$\Grev_{\tau,T} := \Grev^{\,\{D=0\},H}$ and $\Omega(\tau,T) < 1$; each holds verbatim for any
cell event and any depth $d \le H$, with $H$ replaced by $d$ throughout.
\begin{enumerate}[label=(\alph*),leftmargin=2.4em,itemsep=3pt]
\item \emph{Representation.} For every $\kappa \in (0,1)$,
  \begin{equation}
  \label{eq:g-rep}
  M_P(\tau,T;\kappa) \;=\; \Delta_m \sum_{S \subseteq \{0,\ldots,H\}}
  (1-\varepsilon)^{|S|}\,\varepsilon^{\,H+1-|S|}\; \Grev_{\tau,T}(S).
  \end{equation}
\item \emph{Derivative.} With the $\kappa$-free coefficients
  \begin{equation}
  \label{eq:g-ck}
  c_k(\tau,T) \;:=\; \sum_{d=0}^{H}\ \
  \sum_{\substack{S \subseteq \{0,\ldots,H\}\setminus\{d\} \\ |S| = k}}
  \Bigl[\,\Grev_{\tau,T}(S \cup \{d\}) - \Grev_{\tau,T}(S)\,\Bigr],
  \qquad k = 0,\ldots,H,
  \end{equation}
  the pooled premium is differentiable in $\kappa$ on $(0,1)$ and
  \begin{equation}
  \label{eq:g-deriv}
  \partial_\kappa M_P(\tau,T;\kappa) \;=\; -\,\frac{\Delta_m}{2}\,\Wrev_{\tau,T}(\kappa),
  \qquad
  \Wrev_{\tau,T}(\kappa) \;:=\; \sum_{k=0}^{H}(1-\varepsilon)^k \varepsilon^{\,H-k}\,c_k(\tau,T).
  \end{equation}
\item \emph{Sign.} If $\mathsf h$ of \eqref{eq:g-kernel} is concave on the convex hull of the
  pairs $(\pi,\hat v)$ the pooled cell generates, then every increment in \eqref{eq:g-ck} is at
  most zero, hence $c_k(\tau,T)\le 0$ for every $k$ and $\partial_\kappa M_P \ge 0$ at every
  $\kappa \in (0,1)$. If $\mathsf h$ is convex there, all three inequalities reverse. The pooled
  expectation of the kernel is therefore monotone in $\kappa$, in the direction the sign of the
  chord of $\mathsf h$ gives, and the same holds at every depth $d \le H$.
\end{enumerate}
\end{lemma}

\begin{condition}[Revelation dominance at a threshold pair]
\label{cond:D}
Let $b_0 < \tau' < \tau$ at a common window $T$, and let $\Wrev$ be as in \eqref{eq:g-deriv}. The
pair satisfies revelation dominance at $\kappa$ if
\begin{equation}
\label{eq:g-D}
\bigl|\Wrev_{\tau',T}(\kappa)\bigr| \;\le\; \bigl|\Wrev_{\tau,T}(\kappa)\bigr| .
\end{equation}
\end{condition}

\begin{theorem}[The threshold dial at fixed policies]
\label{thm:g-threshold}
Fix the plan and cutoff policies and a window $T$, and take $b_0 < \tau' < \tau$ with
$0 < \Omega(\tau,T)$, $\Omega(\tau',T) < 1$ and $\mathcal S_P(\tau,T) > 0$; part~(B) then puts
$\Omega(\tau,T) \le \Omega(\tau',T) < 1$, so both pooled cells carry positive mass. Assume the
two cell decomposition $\Dact = \Omega M_F + (1-\Omega)M_P$ and the $\kappa$-invariance of the
flagged average $M_F$, each with its own hypotheses. Then:
\begin{enumerate}[label=(\Alph*),leftmargin=2.4em,itemsep=3pt]
\item \emph{Factorisation.} $\mathcal S = (1-\Omega)\,\mathcal S_P$, exactly, at every
  $\kappa \in (0,1)$.
\item \emph{Weight leg.} $\mathcal C_F(\tau,T) \subseteq \mathcal C_F(\tau',T)$ and every newly
  flagged history is generated by a Voice plan, so $\Omega(\tau',T)\ge\Omega(\tau,T)$ and
  $W_\tau \in [0,1]$, with equality when no history is reclassified. This leg carries no
  condition beyond the standing ones.
\item \emph{Composition leg and the dial.} Under Condition~\ref{cond:D} at the pair and at
  $\kappa$, $C_\tau \le 1$, and therefore
  \begin{equation}
  \label{eq:g-dial}
  \frac{\mathcal S(\tau',T)}{\mathcal S(\tau,T)} \;=\; W_\tau\,C_\tau \;\le\; 1 .
  \end{equation}
  Equality holds when no history is reclassified, since the two rules then induce the same
  partition and both factors are one.
\end{enumerate}
\end{theorem}

\begin{remark}[A $\kappa$-free sufficient form of Condition~\ref{cond:D}]
\label{rem:g-Dstar}
The coefficients $c_k(\tau,T)$ of \eqref{eq:g-ck} do not depend on $\kappa$, so
Condition~\ref{cond:D} is a comparison of two vectors in $\mathbb R^{H+1}$. If the $H+1$ numbers
$c_0(\tau,T),\ldots,c_H(\tau,T)$ share one sign and
\begin{equation}
\label{eq:g-Dstar}
|c_k(\tau',T)| \;\le\; |c_k(\tau,T)| \qquad\text{for every } k = 0,\ldots,H,
\end{equation}
then Condition~\ref{cond:D} holds at every $\kappa \in (0,1)$ at once.
\end{remark}

\begin{remark}[What the coefficients are]
\label{rem:g-cells}
By Lemma~\ref{lem:g1} the $S$-record partitions the pooled type set into the level sets of the
restricted mark path $\theta \mapsto (m_e(\theta))_{e \in S}$, so $\Grev_{\tau,T}(S)$ is a finite
sum over those level sets of the cell mass times the kernel at the cell posterior. Each
$c_k(\tau,T)$ is therefore a closed form expression in the pooled type weights, computable
without reference to $\kappa$ and without enumerating order flow.
\end{remark}

\subsection*{Proofs}
\label{sec:pf-garbling-proofs}

\begin{proof}[Proof of Lemma~\ref{lem:g1}]
Condition on a type $\theta$ and a round $e \le d$. If the round is active the mark is $2\bar z$
and $X_e$ takes the values $\bar z$, $2\bar z$, $3\bar z$ with probabilities $\kappa/2$,
$1-\kappa$, $\kappa/2$. If the round is idle the mark is zero and $X_e$ takes the values
$-\bar z$, $0$, $\bar z$ with the same three probabilities in the same order. In both cases
\[
\Prb(X_e = \bar z \mid \theta) \;=\; \kappa/2 \;=\; \varepsilon ,
\]
which proves the first claim of part~(a); the noise draws are independent across rounds and
independent of the type, so the indicators $\ind\{e \in R_d\}$, $e \le d$, are independent
Bernoulli variables with success probability $1-\varepsilon$, independent of $\theta$. That is
part~(a).

For part~(b), the two supports meet only at $\bar z$: an active round produces
$X_e \in \{2\bar z, 3\bar z\}$ and an idle round produces $X_e \in \{-\bar z, 0\}$ whenever
$X_e \neq \bar z$. So on $\{e \in R_d\}$ the flow determines the mark. It remains to check that
nothing else is carried. Conditional on the round being active and revealing,
\[
\Prb(X_e = 2\bar z \mid \text{active},\, e \in R_d) = \frac{1-\kappa}{1-\varepsilon},
\qquad
\Prb(X_e = 3\bar z \mid \text{active},\, e \in R_d) = \frac{\varepsilon}{1-\varepsilon},
\]
and conditional on the round being idle and revealing the values $0$ and $-\bar z$ carry those
same two probabilities. The two conditional laws are the same pair of numbers, so once the mark
is given, which of its two revealing values was realised is a draw whose law does not depend on
the type. Rounds outside $R_d$ carry the single value $\bar z$ and no residual randomness at all.
Combining across rounds by independence, the conditional law of $X_{0:d}$ given the $S$-record
does not depend on $\theta$, which is part~(b).

Part~(c) is the sufficiency conclusion. Write $\mathcal R$ for the $S$-record. Since the
conditional law of $X_{0:d}$ given $(\mathcal R,\theta)$ does not depend on $\theta$,
$\theta$ and $X_{0:d}$ are conditionally independent given $\mathcal R$, and Bayes' rule gives
$\Prb(\theta \in \cdot \mid X_{0:d}, D=0) = \Prb(\theta \in \cdot \mid \mathcal R, D=0)$. The
event $\{D=0\}$ is a type event, so conditioning on it is conditioning $\rho$ down to
$\rho_P^{\tau,T}$, and the displayed posterior is the one stated.
\end{proof}

\begin{proof}[Proof of Lemma~\ref{lem:g2}]
Let $\varepsilon = \kappa/2 < \varepsilon' = \kappa'/2$ and put
\[
\delta \;:=\; \frac{\varepsilon' - \varepsilon}{1-\varepsilon}
\;=\; \frac{\kappa' - \kappa}{2 - \kappa} \;\in\;(0,1).
\]
Define $\Lambda$ on a $\kappa$-history as follows. First read off the record
$(R_d, (m_e)_{e \in R_d})$, which Lemma~\ref{lem:g1}(b) allows without knowing the type. Second,
delete each element of $R_d$ independently with probability $\delta$, obtaining $R'_d$. Third,
emit the flow value $\bar z$ on every round outside $R'_d$, and on every round $e \in R'_d$ emit
one of the two revealing values consistent with $m_e$, drawn with probabilities
$(1-\kappa')/(1-\varepsilon')$ for the zero noise value and $\varepsilon'/(1-\varepsilon')$ for
the other. The kernel reads only the history, never the type.

Fix a type. Under the $\kappa$ law each round lies in $R_d$ independently with probability
$1-\varepsilon$, so under $\Lambda$ each round lies in $R'_d$ independently with probability
\[
(1-\varepsilon)(1-\delta) \;=\; (1-\varepsilon) - (\varepsilon'-\varepsilon)
\;=\; 1-\varepsilon' .
\]
On the rounds of $R'_d$ the emitted marks are the type's own marks, and the revealing value is
drawn from the $\kappa'$ conditional law computed in the proof of Lemma~\ref{lem:g1}. By that
lemma's factorisation across rounds, the emitted history has exactly the $\kappa'$ law given the
type. So $\Lambda$ carries the $\kappa$ experiment to the $\kappa'$ experiment and the second is
a garbling of the first.

For the final claim, run $\Lambda$ on the $\kappa$ history to build a joint law of the type, the
$\kappa$ history and the $\kappa'$ history. Because $\Lambda$ reads only the history, those three
form a Markov chain in that order, so
\[
\Prb\bigl(\theta \in \cdot \bigm| X^{\kappa'}_{0:d}\bigr)
\;=\; \Eop\Bigl[\,\Prb\bigl(\theta \in \cdot \bigm| X^{\kappa}_{0:d}\bigr)
\Bigm| X^{\kappa'}_{0:d}\Bigr].
\]
The $\kappa'$ posterior is therefore a conditional expectation of the $\kappa$ posterior, so the
law of the first is a mean preserving contraction of the law of the second, and both have mean
$\rho_P^{\tau,T}$.
\end{proof}

\begin{proof}[Proof of Lemma~\ref{lem:g3}]
Part~(a). By Lemma~\ref{lem:g1}(a) the revealed set $R_H$ has the product Bernoulli law
$\Prb(R_H = S) = (1-\varepsilon)^{|S|}\varepsilon^{\,H+1-|S|}$, and that law is the same under
$\rho$ and under $\rho_P^{\tau,T}$, because $\{D=0\}$ is a type event and $R_H$ is independent of
the type. By Lemma~\ref{lem:g1}(c) the pooled posterior on $\{R_H = S\}$ is
$\rho_P^{\tau,T}(\cdot \mid (m_e)_{e \in S})$. Conditioning on $R_H$ and applying the tower
property,
\[
\Eop\bigl[h(\nu_{0:H}) \mid D=0\bigr]
\;=\; \sum_{S} \Prb(R_H = S)\;
\Eop_{\rho_P^{\tau,T}}\Bigl[h\bigl(\rho_P^{\tau,T}(\cdot\mid (m_e)_{e\in S})\bigr)\Bigr]
\;=\; \sum_S \Prb(R_H = S)\,\Grev_{\tau,T}(S),
\]
and multiplying by $\Delta_m$ gives \eqref{eq:g-rep}. Nothing in the argument used the depth or
the particular cell event, so the same identity holds with $H$ replaced by any $d \le H$ and
$\{D=0\}$ replaced by any cell event. The numbers $\Grev_{\tau,T}(S)$ are built from
$\rho_P^{\tau,T}$ and the mark paths only, and neither depends on $\kappa$.

Part~(b). Write $q := 1-\varepsilon$ and $F(q) := \sum_S q^{|S|}(1-q)^{H+1-|S|}\Grev(S)$, the
expectation of $\Grev(R_H)$ under the product Bernoulli measure with success probability $q$ on
each of the $H+1$ rounds. Read $F$ as a function of $H+1$ separate success probabilities, one
per round. It is affine in each of them, because the rounds enter the product measure
independently, and its partial derivative in the $d$-th is
$\Eop[\Grev(R_{-d}\cup\{d\})] - \Eop[\Grev(R_{-d})]$, with $R_{-d}$ the random set on the other
rounds. Setting every coordinate to $q$ and summing the $H+1$ partial derivatives,
\[
F'(q) \;=\; \sum_{d=0}^{H}
\Eop_{q}\Bigl[\,\Grev\bigl(R_{-d}\cup\{d\}\bigr) - \Grev\bigl(R_{-d}\bigr)\Bigr],
\]
Expanding the expectation over $R_{-d}$ and collecting terms by $|S| = k$,
\[
F'(q) \;=\; \sum_{d=0}^{H}\ \sum_{S \subseteq \{0,\ldots,H\}\setminus\{d\}}
q^{|S|}(1-q)^{H-|S|}\bigl[\Grev(S\cup\{d\})-\Grev(S)\bigr]
\;=\; \sum_{k=0}^{H} q^{k}(1-q)^{H-k} c_k(\tau,T).
\]
Since $M_P = \Delta_m F(q)$ and $q = 1-\kappa/2$ gives $dq/d\kappa = -1/2$, the chain rule yields
\eqref{eq:g-deriv} with $1-\varepsilon = q$ and $\varepsilon = 1-q$.

Part~(c). Fix $S$ and $d \notin S$, and write $\nu_S$ and $\nu_{S\cup\{d\}}$ for the two
posteriors. The record on $S$ is coarser than the record on $S\cup\{d\}$, so
$\nu_S = \Eop[\nu_{S\cup\{d\}} \mid (m_e)_{e\in S}]$. Both $\pi$ and $\hat v$ are linear in the
posterior, so the pair $(\pi,\hat v)$ evaluated at these two posteriors is an $\mathbb R^2$ valued
martingale over the two records, and its values lie in the convex hull named in the statement. If
$\mathsf h$ is concave there, the conditional Jensen inequality in $\mathbb R^2$ gives
\[
\Eop\bigl[\mathsf h(\pi_{S\cup\{d\}},\hat v_{S\cup\{d\}}) \bigm| (m_e)_{e\in S}\bigr]
\;\le\; \mathsf h(\pi_S, \hat v_S)
\quad\text{almost surely,}
\]
and taking expectations, $\Grev(S\cup\{d\}) \le \Grev(S)$. Every increment in \eqref{eq:g-ck} is
then at most zero, so $c_k \le 0$ for every $k$. The weights $(1-\varepsilon)^k\varepsilon^{H-k}$
are strictly positive on $\kappa \in (0,1)$ and $\Delta_m > 0$, so \eqref{eq:g-deriv} gives
$\partial_\kappa M_P \ge 0$ there. Reversing the curvature reverses each of the three steps. The
depth played no role, so the statement holds at every $d \le H$.
\end{proof}

\begin{proof}[Proof of Theorem~\ref{thm:g-threshold}]
Part~(A). At fixed policies the disclosure indicator is a function of the type alone: the plan
fixes the stake path, the path fixes the crossing date, and the filing lands by the control date
exactly when the crossing date is at most $H-T$. Liquidity enters only the noise law, which
touches order flow and not the stake path, so $\Omega$ does not move with $\kappa$. The flagged
average $M_F$ does not move with $\kappa$ by the flagged invariance assumed in the statement.
Differentiating $\Dact = \Omega M_F + (1-\Omega)M_P$,
\[
\partial_\kappa \Dact
= (\partial_\kappa \Omega)(M_F - M_P) + \Omega\,\partial_\kappa M_F
  + (1-\Omega)\,\partial_\kappa M_P
= (1-\Omega)\,\partial_\kappa M_P ,
\]
the first two terms vanishing term by term rather than by cancellation. Differentiability of
$M_P$ in $\kappa$ is not a hypothesis here: Lemma~\ref{lem:g3}(a) exhibits $M_P$ as a polynomial
in $\kappa$. Taking absolute values and using $1-\Omega \ge 0$ gives
$\mathcal S = (1-\Omega)\mathcal S_P$.

Part~(B). Let a history be flagged at $\tau$, so $a = 1$ and $c(\tau) + T \le H$, where
$c(\tau) = \inf\{d : B(s,d) \ge \tau\}$. Since $\tau' < \tau$, every date at which the stake
reaches $\tau$ is a date at which it reaches $\tau'$, so $c(\tau') \le c(\tau)$ and therefore
$c(\tau') + T \le H$. The engagement flag is unchanged, so the history is flagged at $\tau'$ as
well, and $\mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T)$. Disclosure implies engagement, so
every history in the difference carries $a=1$ and is generated by a Voice plan. Taking masses,
$\Omega(\tau',T)\ge\Omega(\tau,T)$, and with $\Omega(\tau',T) < 1$,
\[
W_\tau = \frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)} \in [0,1],
\]
with $W_\tau = 1$ exactly when the two flagged sets have the same mass, that is when no history
is reclassified. The argument used no property of the kernel.

Part~(C). Both thresholds are evaluated at the same $\kappa$ and at the same policies, so
Lemma~\ref{lem:g3}(b) applies at each and gives
\[
\mathcal S_P(\tau,T) = \frac{\Delta_m}{2}\bigl|\Wrev_{\tau,T}(\kappa)\bigr|,
\qquad
\mathcal S_P(\tau',T) = \frac{\Delta_m}{2}\bigl|\Wrev_{\tau',T}(\kappa)\bigr| .
\]
Since $\mathcal S_P(\tau,T) > 0$ the ratio $C_\tau$ is defined, and
Condition~\ref{cond:D} states exactly that its numerator is at most its denominator, so
$C_\tau \le 1$. Part~(A) applied at each threshold gives
$\mathcal S(\tau',T)/\mathcal S(\tau,T) = W_\tau C_\tau$, and part~(B) puts $W_\tau$ in $[0,1]$.
The product of a number in $[0,1]$ with a number in $[0,1]$ is at most one, which is
\eqref{eq:g-dial}, with equality exactly when both factors are one.
\end{proof}

\begin{proof}[Proof of Remark~\ref{rem:g-Dstar}]
Write $w_k = (1-\varepsilon)^k\varepsilon^{H-k} > 0$. By the triangle inequality and
\eqref{eq:g-Dstar},
\[
\bigl|\Wrev_{\tau',T}(\kappa)\bigr| \;\le\; \sum_{k} w_k\,|c_k(\tau',T)|
\;\le\; \sum_{k} w_k\,|c_k(\tau,T)| .
\]
If the numbers $c_k(\tau,T)$ share one sign then the last sum equals
$\bigl|\sum_k w_k c_k(\tau,T)\bigr| = |\Wrev_{\tau,T}(\kappa)|$. The bound holds at every
$\kappa \in (0,1)$ because the hypothesis does not involve $\kappa$.
\end{proof}

\begin{remark}[Verification of Condition~\ref{cond:D}]
\label{rem:g-grid}
Condition~\ref{cond:D} is checked, and the coefficients $c_k$ of \eqref{eq:g-ck} are reported, at
order size two on the calibration grid: the frozen baseline policy, the two windows
$T \in \{5,10\}$, the five threshold quantiles $0.1$, $0.3$, $0.5$, $0.7$, $0.9$ of the
equilibrium terminal stake distribution taken in adjacent pairs, and the $71$ node liquidity grid
$\kappa = 0.15, 0.16, \ldots, 0.85$. The record is
\texttt{numerical\_v4/checks/t2\_threshold\_revelation\_check.json}. Its status on that grid is
NUMERICAL.
\end{remark}

```

### 8.2 `proofs/03_caught.tex` (in full)

```latex
% proofs/03_caught.tex
% Who gets caught: signing the composition ratio of the window margin.
% Fragment, to be \input by appendix.tex.
%
% appendix.tex must supply: amsmath, amssymb, amsthm (the proof environment), enumitem,
%   \newtheorem{corollary}{Corollary}, and the macros \Eop, \Prb, \ind.
% Cross-references to the partition result, the clock equivalence and the clock
%   theorem are written in words here; ticket 11 owns the \ref targets.
% Notation notes for ticket 11: (a) B below is the set of newly caught histories. It
%   is unrelated to the stake symbols B_j(s,t) and B^F. (b) The caught share is
%   written \varphi, not \beta, because \beta is the signal weight
%   sigma_v^2/(sigma_v^2 + sigma_eps^2) in the model section. Rename either if the
%   collision reads badly.
% Label at write time: CONJECTURE. The two-pass gate and the grid check are separate items.

\subsection{Who gets caught}
\label{sec:caught}

The clock theorem makes window attenuation equivalent to $W_T C_T \le 1$ and signs only the weight
leg. This section signs the composition leg. It writes the longer clock's pooled sensitivity as a
mass-weighted average of what the shorter clock leaves in the pool and what it takes out, and reads
both $C_T \le 1$ and $W_T C_T \le 1$ off that average.

\paragraph{Setup.}
Fix the threshold margin $\tau$ and the plan and cutoff policies, and compare two window margins
$T' < T$ at a common $\kappa$. Write
\begin{equation}
\label{eq:caught-sets}
A \;=\; \mathcal{C}_P(\tau,T),
\qquad
B \;=\; \mathcal{C}_F(\tau,T')\setminus\mathcal{C}_F(\tau,T),
\end{equation}
so $A$ is the pooled cell under the longer clock and $B$ collects the histories the shorter clock
newly flags. Write
\begin{equation}
\label{eq:caught-phi}
\varphi \;=\; \frac{\Prb(B)}{\Prb(A)}
\end{equation}
for the share of the longer clock's pooled cell that the shorter clock catches.

Each rule pins its own premium kernel. The control-node information set carries the coordinate
``the filing has landed by date $d$'', so the pooled history at window margin $T$ and the pooled
history at window margin $T'$ are different observables, and the engagement posterior
$\pi = \Prb(a = 1 \mid \cdot)$ and the price are taken with respect to whichever of the two the
rule supplies. Write $h^{(T)}$ and $h^{(T')}$ for the kernel $h = \pi p$ evaluated at the
control-node information set of the rule $(\tau,T)$ and of the rule $(\tau,T')$. The two pooled
averages of the clock theorem are then
\begin{equation}
\label{eq:caught-MP}
M_P(\tau,T) \;=\; \Delta_m\,\Eop\bigl[h^{(T)} \bigm| A\bigr],
\qquad
M_P(\tau,T') \;=\; \Delta_m\,\Eop\bigl[h^{(T')} \bigm| A\setminus B\bigr],
\end{equation}
the second reading of the pooled cell at the shorter clock being part~(i) below. Set
\begin{equation}
\label{eq:caught-sens}
s_A \;=\; \partial_\kappa\Eop\bigl[h^{(T)} \bigm| A\bigr],
\qquad
s_{A\setminus B} \;=\; \partial_\kappa\Eop\bigl[h^{(T')} \bigm| A\setminus B\bigr],
\end{equation}
so that, with $\Delta_m > 0$ finite,
\begin{equation}
\label{eq:caught-SP}
\mathcal{S}_P(\tau,T) \;=\; \Delta_m\,|s_A|,
\qquad
\mathcal{S}_P(\tau,T') \;=\; \Delta_m\,|s_{A\setminus B}|,
\qquad
C_T \;=\; \frac{|s_{A\setminus B}|}{|s_A|} ,
\end{equation}
by the definitions of the two pooled sensitivities and no more.

Two further quantities separate what the catch removes from how the surviving pool is re-read:
\begin{equation}
\label{eq:caught-raw}
\tilde s_B \;=\; \partial_\kappa\Eop\bigl[h^{(T)} \bigm| B\bigr],
\qquad
\delta \;=\; \partial_\kappa\Eop\bigl[h^{(T')} - h^{(T)} \bigm| A\setminus B\bigr] .
\end{equation}
Here $\tilde s_B$ is the noise sensitivity of the newly caught histories, priced as the longer
clock priced them, and $\delta$ is the \emph{re-pricing remainder}: the pooled posterior conditions
on the pool the rule leaves behind, so the histories that stay pooled are read against a smaller
pool once the clock shortens, and $\delta$ is the rate at which that re-reading moves their noise
sensitivity. Define the \emph{caught leg} by
\begin{equation}
\label{eq:caught-sB}
s_B \;:=\; \frac{1}{\Prb(B)}\,
\partial_\kappa\Bigl(
\Eop\bigl[h^{(T)}\ind_A\bigr] - \Eop\bigl[h^{(T')}\ind_{A\setminus B}\bigr]
\Bigr) .
\end{equation}
The pooled cell contributes to the expected engagement premium an amount
\[
\begin{aligned}
\Delta_m\,\Eop\bigl[h^{(T)}\ind_A\bigr]
  \;&=\; \bigl(1-\Omega(\tau,T)\bigr)\,M_P(\tau,T)
  &&\text{at the longer clock,} \\[3pt]
\Delta_m\,\Eop\bigl[h^{(T')}\ind_{A\setminus B}\bigr]
  \;&=\; \bigl(1-\Omega(\tau,T')\bigr)\,M_P(\tau,T')
  &&\text{at the shorter one.}
\end{aligned}
\]
So $s_B$ is the derivative of $\Lambda_T - \Lambda_{T'}$ per unit of pooled mass removed: it is
the noise sensitivity of the premium mass the shorter clock removes from the pool, and it
carries the survivors' re-pricing. It is not $\tilde s_B$. Under the extra clause of (C-2) it
splits into the two parts just named,
\begin{equation}
\label{eq:caught-split}
s_B \;=\; \tilde s_B \;-\; \frac{1-\varphi}{\varphi}\,\delta ,
\end{equation}
which part~(iii) proves.

The hypotheses are:
\begin{enumerate}[label=(C-\arabic*),leftmargin=3.2em,itemsep=3pt]
\item \emph{Fixed policies.} The plan menu, the execution policies and the cutoff vector are held
  fixed in $\kappa$ and held fixed across the two window margins, the threshold margin $\tau$ is
  common, the noise intensity $\kappa$ is common, and the timing carries no feedback from order
  flow into the blockholder's executed order path. Liquidity enters the primitives in one place
  only, the law of the ternary noise mark, which is standing condition (S11) of the partition
  subsection; part~(ii) consumes that.
\item \emph{Differentiability.} The two conditional expectations in \eqref{eq:caught-sens} are
  differentiable in $\kappa$ at the point compared. For the split \eqref{eq:caught-split} into
  $\tilde s_B$ and $\delta$, $\Eop[h^{(T)}\mid B]$ is also differentiable. The kernel is the
  pinned version of
  standing condition (S8), so $h^{(T)}$ and $h^{(T')}$ are well-defined random variables rather
  than equivalence classes; part~(iii) consumes that.
\item \emph{Non-degeneracy.} $\Prb(B) > 0$, $0 < \Omega(\tau,T)$, $\Omega(\tau,T') < 1$, and
  $s_A \ne 0$, equivalently $\mathcal{S}_P(\tau,T) > 0$. The clause $0 < \Omega(\tau,T)$ is there
  so that the clock theorem applies. Wherever this corollary is used to read the criterion
  $W_T C_T \le 1$ in Theorem~\ref{thm:clock}, that theorem's hypotheses also apply. They include
  the hypotheses of Proposition~\ref{prop:factorisation} at both clocks, including the invariance
  of the flagged endpoint in $\kappa$ at fixed policies.
\end{enumerate}

\begin{corollary}[Who gets caught]
\label{cor:caught}
Under (C-1) to (C-3):
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=3pt]
\item \emph{The cut is nested.} $\mathcal{C}_F(\tau,T)\subseteq\mathcal{C}_F(\tau,T')$, hence
  $B \subseteq A$ and $A\setminus B = \mathcal{C}_P(\tau,T')$, and the weight leg is
  \begin{equation}
  \label{eq:caught-WT}
  W_T \;=\; 1-\varphi \;\le\; 1 ,
  \qquad \varphi\in(0,1).
  \end{equation}
\item \emph{The cell masses are $\kappa$-free.}
  $\partial_\kappa\Prb(A) = \partial_\kappa\Prb(B) = 0$, so $\varphi$ does not depend on $\kappa$.
\item \emph{The cut identity.}
  \begin{equation}
  \label{eq:caught-identity}
  s_{A\setminus B}
  \;=\;
  \frac{\Prb(A)\,s_A - \Prb(B)\,s_B}{\Prb(A)-\Prb(B)}
  \;=\;
  \frac{s_A - \varphi\,s_B}{1-\varphi}
  \;=\;
  \frac{s_A - \varphi\,\tilde s_B}{1-\varphi} \;+\; \delta ,
  \end{equation}
  the last expression under the extra differentiability of (C-2). Equivalently
  $s_A = (1-\varphi)\,s_{A\setminus B} + \varphi\,s_B$: the longer clock's pooled sensitivity is
  the mass-weighted average of the sensitivity of what the shorter clock leaves in the pool and
  $s_B$, the derivative of $\Lambda_T-\Lambda_{T'}$ per unit of pooled mass removed, which
  carries the survivors' re-pricing.
\item \emph{The composition ratio.}
  \begin{equation}
  \label{eq:caught-CT}
  \begin{aligned}
  C_T \;&=\; \frac{|s_A-\varphi s_B|}{(1-\varphi)\,|s_A|}, \\[3pt]
  C_T \le 1 \quad&\Longleftrightarrow\quad
  (s_B-s_A)\bigl(\varphi s_B-(2-\varphi)s_A\bigr) \le 0 ,
  \end{aligned}
  \end{equation}
  that is, if and only if $s_B$ lies weakly between $s_A$ and
  $\bigl((2-\varphi)/\varphi\bigr)s_A$.
\item \emph{The attenuation criterion.}
  \begin{equation}
  \label{eq:caught-WTCT}
  \begin{aligned}
  W_T C_T \;&=\; \frac{|s_A-\varphi s_B|}{|s_A|}, \\[3pt]
  W_T C_T \le 1 \quad&\Longleftrightarrow\quad
  s_B\bigl(2s_A-\varphi s_B\bigr) \ge 0 ,
  \end{aligned}
  \end{equation}
  that is, if and only if $s_B$ lies weakly between $0$ and $(2/\varphi)s_A$.
\item \emph{Readings.} Write $\rho = s_B/s_A$, which is well defined by (C-3).
  \begin{enumerate}[label=(\alph*),leftmargin=2.2em,itemsep=2pt]
  \item If $s_A s_B \le 0$, including $s_B = 0$, then $C_T > 1$ strictly.
  \item If $s_A s_B > 0$, then
    $C_T \le 1$ if and only if
    $|s_A| \le |s_B| \le \bigl((2-\varphi)/\varphi\bigr)|s_A|$.
  \item If the cut does not reverse the pooled sensitivity, $s_{A\setminus B}\,s_A \ge 0$, then
    $C_T \le 1$ if and only if $\rho \ge 1$. The inequality $\rho \ge 1 > 0$ already forces a
    common sign, so that reading is $|s_B| \ge |s_A|$. Under a common sign the proviso
    $\sigma \ge 0$ is $|s_B| \le |s_A|/\varphi$.
  \item $W_T C_T \le 1$ if and only if $s_B$ shares the sign of $s_A$ or is zero, and
    $|s_B| \le (2/\varphi)|s_A|$.
  \item The two upper limits $(2-\varphi)/\varphi$ and $2/\varphi$ are strictly decreasing in
    $\varphi$ and diverge as $\varphi\downarrow0$. For every $M \ge 1$ and every cut with
    $\varphi \le 2/(1+M)$ and $|s_B| \le M|s_A|$, the upper limits in (b) and (d) are slack, so
    there $C_T \le 1$ reads: a common sign together with $|s_B| \ge |s_A|$; and $W_T C_T \le 1$
    reads: a common sign or $s_B = 0$.
  \end{enumerate}
\end{enumerate}
\end{corollary}

\begin{proof}
\emph{Part (i).} The disclosure indicator at window margin $T$ is
$D(\tau,T) = \ind\{a=1,\ c(\tau)+T\le H\}$, where $c(\tau)$ is the round in which the executed
stake path crosses $\tau$. If $D(\tau,T)=1$ then $c(\tau)+T' \le c(\tau)+T \le H$ because
$T'<T$, so $D(\tau,T')=1$. Hence $\mathcal{C}_F(\tau,T)\subseteq\mathcal{C}_F(\tau,T')$ and, taking
complements, $\mathcal{C}_P(\tau,T')\subseteq\mathcal{C}_P(\tau,T)=A$. Therefore
$B = \mathcal{C}_F(\tau,T')\cap A \subseteq A$ and
$A\setminus B = A\cap\mathcal{C}_P(\tau,T') = \mathcal{C}_P(\tau,T')$. Taking probabilities,
$\Omega(\tau,T) \le \Omega(\tau,T') < 1$, so both pooled cells carry positive mass; since
$B\subseteq A$, $\Prb(A\setminus B) = \Prb(A)-\Prb(B)$, and
\[
W_T \;=\; \frac{1-\Omega(\tau,T')}{1-\Omega(\tau,T)}
\;=\; \frac{\Prb(A\setminus B)}{\Prb(A)}
\;=\; 1-\varphi .
\]
By (C-3), $\Prb(B)>0$ gives $\varphi>0$ and $\Omega(\tau,T')<1$ gives $\Prb(A\setminus B)>0$, hence
$\varphi<1$.

\emph{Part (ii).} Under fixed policies the selected plan and the executed order path are functions
of the plan index and the signal alone, and by the no-feedback clause of (C-1) the order placed in
a round does not read realised order flow. So the crossing round $c(\tau)$, and with it
$D(\tau,T)$ and $D(\tau,T')$, are measurable with respect to the plan and signal. The intensity
$\kappa$ parametrises the noise law only; the laws of the value, the signal noise and the bidder
draw carry no $\kappa$, and (C-1) holds the cutoff vector fixed in $\kappa$, so the joint law of
the plan and the signal is one and the same at every $\kappa$. Hence $\Prb(A)$ and $\Prb(B)$ do not
vary with $\kappa$, and neither does their ratio $\varphi$. This is the same constancy the clock
theorem uses for the flagged weight, applied at both window margins.

\emph{Part (iii).} By part (i), $B$ and $A\setminus B$ partition $A$ and both have positive mass.
Write the pooled contributions to the expected premium at the two clocks, in kernel units, as
\[
\begin{aligned}
\Lambda_T \;&=\; \Eop\bigl[h^{(T)}\ind_A\bigr]
  \;=\; \Prb(A)\,\Eop\bigl[h^{(T)}\mid A\bigr], \\[3pt]
\Lambda_{T'} \;&=\; \Eop\bigl[h^{(T')}\ind_{A\setminus B}\bigr]
  \;=\; \Prb(A\setminus B)\,\Eop\bigl[h^{(T')}\mid A\setminus B\bigr] .
\end{aligned}
\]
By part (ii) the two masses are constants in $\kappa$, so the derivative that (C-2) supplies passes
through them and leaves them alone:
\[
\partial_\kappa \Lambda_T \;=\; \Prb(A)\,s_A ,
\qquad
\partial_\kappa \Lambda_{T'} \;=\; \bigl(\Prb(A)-\Prb(B)\bigr)\,s_{A\setminus B} .
\]
Definition \eqref{eq:caught-sB} reads
$s_B = \partial_\kappa(\Lambda_T - \Lambda_{T'})/\Prb(B)$, a division by a positive number, so
\[
\Prb(B)\,s_B \;=\; \Prb(A)\,s_A - \bigl(\Prb(A)-\Prb(B)\bigr)\,s_{A\setminus B} ,
\]
and solving for $s_{A\setminus B}$, which the positive mass $\Prb(A)-\Prb(B)$ permits, gives the
first equality of \eqref{eq:caught-identity}. Dividing numerator and denominator by $\Prb(A)$ gives
the second. Multiplying through by $1-\varphi$ and collecting terms gives
$s_A = (1-\varphi)s_{A\setminus B}+\varphi s_B$.

For the third expression, add and subtract $\Eop[h^{(T)}\ind_{A\setminus B}]$ inside
$\Lambda_T-\Lambda_{T'}$. Since $\ind_A = \ind_{A\setminus B}+\ind_B$ by part (i),
\[
\begin{aligned}
\Lambda_T - \Lambda_{T'}
\;&=\; \Eop\bigl[h^{(T)}\ind_B\bigr]
  \;-\; \Eop\bigl[\bigl(h^{(T')}-h^{(T)}\bigr)\ind_{A\setminus B}\bigr] \\[3pt]
\;&=\; \Prb(B)\,\Eop\bigl[h^{(T)}\mid B\bigr]
  \;-\; \Prb(A\setminus B)\,\Eop\bigl[h^{(T')}-h^{(T)}\mid A\setminus B\bigr] .
\end{aligned}
\]
Both masses are $\kappa$-free by part (ii), and the extra clause of (C-2) makes the first term
differentiable, hence so is the second. Differentiating and dividing by $\Prb(B)$ gives
$s_B = \tilde s_B - \bigl((1-\varphi)/\varphi\bigr)\delta$, which is \eqref{eq:caught-split}.
Substituting it into the second equality of \eqref{eq:caught-identity} gives
the third.

\emph{Part (iv).} By \eqref{eq:caught-SP} and part (i), $C_T = |s_{A\setminus B}|/|s_A|$, and by
\eqref{eq:caught-identity} with $1-\varphi>0$,
\[
C_T \;=\; \frac{|s_A-\varphi s_B|}{(1-\varphi)|s_A|} .
\]
The denominator is non-zero because $s_A \ne 0$ in (C-3). Both sides of $C_T\le 1$ are
non-negative, so $C_T\le 1$ if and only if $s_{A\setminus B}^2\le s_A^2$, and multiplying by
$(1-\varphi)^2>0$, if and only if $u^2-w^2\le 0$, where $u=s_A-\varphi s_B$ and
$w=(1-\varphi)s_A$. Since $u-w=\varphi(s_A-s_B)$ and $u+w=(2-\varphi)s_A-\varphi s_B$,
\[
u^2-w^2 \;=\; (u-w)(u+w) \;=\; \varphi\,(s_A-s_B)\bigl((2-\varphi)s_A-\varphi s_B\bigr).
\]
Since $\varphi>0$, the sign of the whole is the sign of
$(s_A-s_B)\bigl((2-\varphi)s_A-\varphi s_B\bigr)$, and negating both factors leaves the product
unchanged, which gives the stated form
$(s_B-s_A)\bigl(\varphi s_B-(2-\varphi)s_A\bigr)\le 0$. Writing that product as
$\varphi(s_B-s_A)\bigl(s_B-\bigl((2-\varphi)/\varphi\bigr)s_A\bigr)$ shows it is non-positive
exactly when $s_B$ lies weakly between the two roots $s_A$ and
$\bigl((2-\varphi)/\varphi\bigr)s_A$.

\emph{Part (v).} By part (i) and part (iv),
\[
W_T C_T \;=\; (1-\varphi)\,\frac{|s_{A\setminus B}|}{|s_A|}
\;=\; \frac{\bigl|(1-\varphi)s_{A\setminus B}\bigr|}{|s_A|}
\;=\; \frac{|s_A-\varphi s_B|}{|s_A|} .
\]
As in part (iv), $W_T C_T\le 1$ if and only if $u^2-s_A^2\le 0$ for $u=s_A-\varphi s_B$, and since
$u-s_A=-\varphi s_B$ and $u+s_A=2s_A-\varphi s_B$,
\[
u^2-s_A^2 \;=\; (u-s_A)(u+s_A) \;=\; -\varphi\,s_B\bigl(2s_A-\varphi s_B\bigr),
\]
so the criterion is $s_B(2s_A-\varphi s_B)\ge 0$. Writing it as
$\varphi\,s_B\bigl((2/\varphi)s_A-s_B\bigr)\ge 0$ shows it holds exactly when $s_B$ lies weakly
between $0$ and $(2/\varphi)s_A$.

\emph{Part (vi).} Since $\varphi\in(0,1)$, the factor $(2-\varphi)/\varphi$ is strictly positive,
so the two roots in part (iv) are non-zero and share the sign of $s_A$, and the closed interval
they bound does not contain zero. If $s_As_B\le 0$ then $s_B$ is zero or lies on the far side of
zero from both roots, so it is strictly outside that interval, the product in
\eqref{eq:caught-CT} is strictly positive, and $C_T>1$. That is (a). For (b), divide the interval
condition by $s_A$: with a common sign, $\rho>0$ and $s_B$ between $s_A$ and
$\bigl((2-\varphi)/\varphi\bigr)s_A$ reads $1\le\rho\le(2-\varphi)/\varphi$, and multiplying by
$|s_A|$ gives the stated magnitudes. For (c), set
$\sigma = s_{A\setminus B}/s_A = (1-\varphi\rho)/(1-\varphi)$ by \eqref{eq:caught-identity}. The
proviso $s_{A\setminus B}s_A\ge0$ is $\sigma\ge0$, so $C_T = |\sigma| = \sigma$, and $C_T\le1$ if
and only if $1-\varphi\rho\le1-\varphi$, that is $\rho\ge1$. The inequality $\rho\ge1>0$ already
forces a common sign, under which $\rho\ge1$ is $|s_B|\ge|s_A|$. Under a common sign the proviso
$\sigma\ge0$ is $\varphi\rho\le1$, that is $|s_B|\le|s_A|/\varphi$. For (d), divide the interval
condition of part (v) by $s_A$: it reads $0\le\rho\le2/\varphi$, which is a common sign or
$s_B=0$, together with $|s_B|\le(2/\varphi)|s_A|$. For (e), both $(2-\varphi)/\varphi$ and
$2/\varphi$ are strictly decreasing on $(0,1)$ and tend to $+\infty$ as $\varphi\downarrow0$. Fix
$M\ge1$ and $\varphi\le2/(1+M)$. Then $(2-\varphi)/\varphi\ge M$, because that inequality is
$2-\varphi\ge M\varphi$, and $2/\varphi\ge(2-\varphi)/\varphi\ge M$. So $|s_B|\le M|s_A|$ makes
the upper limits in (b) and (d) slack, leaving in (b) the common sign with $|s_B|\ge|s_A|$ and in
(d) the common sign or $s_B=0$.
\end{proof}

\paragraph{Reading.}
Part~(iii) is the whole content in one line: the longer clock's pooled sensitivity is an average
over what the shorter clock leaves in the pool and what it takes out of the pool, with weights the
two masses, and those weights do not move with liquidity. So shortening the clock pulls the pooled
sensitivity down only if what it takes out sat above the average. Parts~(iv) and~(vi) put the
bound on how far above. What the clock removes must move with the pool in $\kappa$ and be at least
as noise-sensitive as the pool, and it must not be so much more sensitive that the remaining pool
is driven through zero to a larger magnitude than the pool started with. A cut that takes a small
share of the pool faces only the first two requirements when, as part~(vi)(e) states, there is
some $M\ge 1$ with $\varphi \le 2/(1+M)$ and $|s_B|\le M|s_A|$. Part~(v) does the same for the criterion
the clock theorem states, $W_T C_T\le1$, where the weight leg is already working in the same
direction: there what the clock removes need only move with the pool and stay inside $2/\varphi$
times its sensitivity.

What the clock removes has two parts, and \eqref{eq:caught-split} separates them. The first is the
noise sensitivity of the newly caught histories themselves, read at the prices the longer clock
gave them. The second is the re-pricing remainder: the surviving pool is a smaller pool once the
clock shortens, and the market reads it against that smaller pool, so its own sensitivity moves
too. The criterion runs on the sum, which is the sensitivity of the premium mass that leaves the
pool. When the re-pricing remainder is zero the sum is the first part alone, and the criterion is
a statement about the caught histories and nothing else.

The corollary turns the ratio $C_T$ into a question with an answer at every calibration node, and
that question is who gets caught: the shorter clock lowers noise sensitivity when what it takes
out of the pool is what the market was reading most from order flow.

```

### 8.3 `proofs/04_inherited.tex` (statements only, in file order)

```latex
\begin{lemma}[The flagged cell does not move with liquidity]
\label{lem:flagged-kappa-free}
Fix the cutoff policy and the execution policy, and let the disclosure rule $(\tau,T)$ be fixed.
Assume the primitive draws are mutually independent with strictly positive variances; the menu, the
image of the coarsening $\Gamma$, the noise support and the calendar are finite; every stake path
$s\mapsto B_j(s,d)$ is Borel, with Voice stakes weakly increasing in the signal and in the date; the
blockholder does not revise the stake path in response to realised order flow or prices; the legal-clock definitions
hold, including $D=1\Rightarrow a=1$ and the restriction that only Voice plans cross; the composed
terminal target $s\mapsto b^*_{j(s)}(s)$ is strictly increasing on the flagged signal region, almost
surely on the flagged set; the inner pricing fixed point is unique; the flagged weight satisfies
$\Omega>0$; and the bidder's entry rule has the two properties
\begin{equation}
\label{eq:entry-props}
\Prb(\mathsf B=1\mid\mathcal I_H)=p(\mathcal I_H)
\qquad\text{and}\qquad
\mathsf B \perp v \mid \mathcal I_H .
\end{equation}
Then, on the flagged cell $\mathcal C_F$, the flagged tuple $\Sfl=(B^F,Q^F,a{=}1)$ makes the
pre-filing pooled history conditionally independent of $(v,s,\xi)$, and the flagged posterior, the
flagged price, the bidder's entry probability and the flagged cell average $M_F$ do not depend on
$\kappa$. In addition $\Omega$ does not depend on $\kappa$, so $\partial_\kappa\Omega=0$ at fixed
policies.
\end{lemma}

\begin{lemma}[Disclosure partition]
\label{lem:partition}
Under \ref{p:space}--\ref{p:public}, the disclosure indicator
$D = \ind\{a = 1,\ c(\tau) + T \le H\}$ is a measurable function of the control-node history, and
the flagged cell $\mathcal C_F = \{D = 1\}$ and the pooled cell $\mathcal C_P = \{D = 0\}$ are
disjoint and cover the space. Consequently the flagged weight $\Omega = \Prb(D = 1)$ is defined and
$\Prb(D = 0) = 1 - \Omega$. No restriction on the mass of either cell is used.
\end{lemma}

\begin{lemma}[Two-cell decomposition of the premium]
\label{lem:two-cell}
Under \ref{p:space}--\ref{p:wedge}, with the partition of Lemma~\ref{lem:partition}, and whenever
$0 < \Omega < 1$,
\begin{equation}
\label{eq:two-cell}
  \Dact \;=\; \Omega\,M_F \;+\; (1 - \Omega)\,M_P,
  \qquad
  M_F = \Delta_m\Eop[h \mid D = 1],
  \quad
  M_P = \Delta_m\Eop[h \mid D = 0].
\end{equation}
At $\Omega = 1$ the identity reads $\Dact = M_F$ and at $\Omega = 0$ it reads $\Dact = M_P$; in each
of those two cases the average over the null cell is undefined rather than zero, and it is not
determined by the law. That $M_P$ is defined as a number, rather than an equivalence class, rests
on \ref{p:kernel} pinning a version of the price: \ref{p:paths} states Borel regularity for Voice
paths only.
\end{lemma}

\begin{proposition}[Factorisation of the liquidity sensitivity]
\label{prop:factorisation}
Assume \ref{p:space}--\ref{p:fixed}, the partition of Lemma~\ref{lem:partition}, the two-cell
decomposition of Lemma~\ref{lem:two-cell}, an interior partition $0 < \Omega < 1$ at the policy under
consideration, the invariance of the flagged endpoint in $\kappa$ at fixed policies, and, as an
explicit hypothesis, differentiability of $\kappa \mapsto M_P$. Then
\begin{equation}
\label{eq:factorisation}
  \mathcal S(\kappa,\tau,T) \;=\; \bigl(1 - \Omega(\tau,T)\bigr)\,\mathcal S_P(\kappa,\tau,T),
\end{equation}
exactly. The same factor scales the total variation of $\Dact$ over any grid in $\kappa$, and there
no differentiability is used.
\end{proposition}

\begin{lemma}[The weight leg at the threshold margin]
\label{lem:threshold-weight}
Fix the liquidity $\kappa$, the window margin $T$, and the plan and cutoff policies. Compare two
threshold margins with $b_0 < \tau' < \tau$, so that $\tau'$ is the tighter threshold, and assume
$\Omega(\tau',T) < 1$. The configuration $b_0 < \tau'$ is what puts the clock equivalence in force
at both thresholds, together with Voice date-monotonicity (standing condition \ref{p:paths}) and
the restriction that only Voice plans cross (standing condition \ref{p:clock}). Then
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=3pt]
\item the flagged cells are nested, $\mathcal C_F(\tau,T) \subseteq \mathcal C_F(\tau',T)$, and
every history the tighter threshold newly flags carries the engagement flag $a=1$;
\item the flagged weight rises, $\Omega(\tau',T) \ge \Omega(\tau,T)$, so the weight leg
\begin{equation}
\label{eq:threshold-weight-leg}
W_\tau \;=\; \frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)}
\end{equation}
is defined and attenuates: $0 < W_\tau \le 1$;
\item if in addition $\Omega(\tau,T) > 0$, $\mathcal S_P(\kappa,\tau,T) > 0$, and the hypotheses of
Proposition~\ref{prop:factorisation} hold at both thresholds, the sensitivity
ratio at this margin factors into the weight leg and the composition leg
$C_\tau = \mathcal S_P(\kappa,\tau',T)/\mathcal S_P(\kappa,\tau,T)$,
\begin{equation}
\label{eq:threshold-ratio}
\frac{\mathcal S(\kappa,\tau',T)}{\mathcal S(\kappa,\tau,T)} \;=\; W_\tau\,C_\tau .
\end{equation}
\end{enumerate}
\end{lemma}

\begin{theorem}[The clock dial]
\label{thm:clock}
Fix the liquidity $\kappa$, the threshold margin $\tau$, and the plan and cutoff policies. Compare
two window margins $T' < T$, so that $T'$ is the shorter clock. Assume $b_0 < \tau$, that Voice
stake paths are weakly increasing in the calendar date (standing condition \ref{p:paths}), and
that only Voice plans cross (standing condition \ref{p:clock}), which is the configuration that
puts the clock equivalence in force at both windows. Assume $0 < \Omega(\tau,T) < 1$ and
$0 < \Omega(\tau,T') < 1$, and $\mathcal S_P(\kappa,\tau,T) > 0$. Assume that the hypotheses of
Proposition~\ref{prop:factorisation} hold at both clocks. Write
\begin{equation}
\label{eq:clock-legs}
W_T \;=\; \frac{1-\Omega(\tau,T')}{1-\Omega(\tau,T)},
\qquad
C_T \;=\; \frac{\mathcal S_P(\kappa,\tau,T')}{\mathcal S_P(\kappa,\tau,T)} .
\end{equation}
Then
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=3pt]
\item the weight leg attenuates: $0 < W_T \le 1$;
\item the sensitivity ratio factors into the two legs,
\begin{equation}
\label{eq:clock-ratio}
\frac{\mathcal S(\kappa,\tau,T')}{\mathcal S(\kappa,\tau,T)} \;=\; W_T\,C_T ;
\end{equation}
\item the shorter clock lowers noise sensitivity exactly when the product of the two legs is at
most one,
\begin{equation}
\label{eq:clock-iff}
\mathcal S(\kappa,\tau,T') \;\le\; \mathcal S(\kappa,\tau,T)
\qquad\Longleftrightarrow\qquad
W_T\,C_T \;\le\; 1 .
\end{equation}
\end{enumerate}
\end{theorem}
```

## 9. The three candidates, with the worker memos and the attack verdicts

Our provisional ranking is 4.3, then 4.1, then 4.2. Reasons, briefly: 4.3 is a theorem that
changes what the paper can say first ("tightening always improves what the market knows; the
sensitivity results say how the improvement is composed"); its content is the identification
hypothesis, and the order is strict at T = 5 and an equality at the corner T = 10. 4.1 is
cheap and answers "why order size two" with a proposition whose b = 2 half is Lemma g2 verbatim.
4.2 unifies the two composition legs into one corollary and adds a kappa-interval certificate
whose largest root is the exact endpoint of the Condition D failure; but at the threshold dial
the caught leg is dominated by survivor re-pricing, which weakens the "who gets caught" reading
there. Rank them yourself; do not defer to this.

### Candidate 4.3: Tightening is a Blackwell improvement

#### The conjecture as first posed

Conjecture. At fixed policies, for τ' < τ at a common window, or T' < T at a common threshold,
the market's control-node experiment about the blockholder's type under the tighter rule is
Blackwell more informative than under the looser one. A sketch offered at the time, not binding:
flagged sets are nested; a flagged type is identified exactly since b* is strictly increasing
(S6 of the calibration; standing condition (S4) gives monotone paths); from the tighter rule's
output one can simulate the looser rule's output by drawing fresh noise for types flagged only
under the tighter rule, because no-feedback timing (S7) makes the mark path a function of the
type alone.

Corollaries to state if it holds: expected posterior variance of engagement falls in tightness
unconditionally; the expected premium level rises when the kernel 𝗁 of Lemma g3 is convex on
the hull the pooled cell generates.

Why it matters. It gives the paper a first theorem under the framing "tightening always
improves what the market knows; the sensitivity results say how the improvement is composed,
into a κ-free flag part and a silence part". Risk: a referee may find it obvious; it is a spine,
not a headline.

#### Gate outcome

Writer: GPT 5.6 Sol at xhigh effort, memo status PASS. Attacker: Claude Opus 5, verdict PASS with eight nits. The attacker ran 13,500 explicit kernel cases with error 0.0 and 34,560 linear programmes over a wider model class (10,148 with real reclassification), none infeasible; its main line of attack, that the date-d flagged information cannot hold Q^F before the control node, failed against the model code.

#### The worker's statement (from the memo, verbatim)

For a rule \(r=(\tau,T)\), let \(D_r^d\) indicate that the filing has landed by date
\(d\leq H\). Let \(r_+\) denote the tighter rule and \(r_-\) the looser rule. At date \(d\),
the tagged output is
\[
 Y_r^d=
 \begin{cases}
  (F,\mathsf S_{F,r}),&D_r^d=1,\\
  (P,\mathcal H_{r,d}^P),&D_r^d=0,
 \end{cases}
 \qquad
 \mathsf S_{F,r}=(B_r^F,Q_r^F,a=1).
\]
The pooled history is
\[
 \mathcal H_{r,d}^P=
 \bigl(X_0,\ldots,X_d;L_{r,0},\ldots,L_{r,d}\bigr),
 \qquad
 L_{r,e}=\mathbf 1\{\text{the filing has landed by }e\}.
\]
On a pooled path every \(L_{r,e}\) through date \(d\) is zero. Prices can be appended to either
output. They are pinned measurable functions of the displayed information and do not enlarge the
experiment.

The hypotheses are the standing conditions, stated here in full, and three added conditions.

1. **(S1) One probability space.** The primitive vector \((v,\varepsilon,\xi,z_{0:H})\)
   has a joint law on a finite product of Polish spaces, the noise marks take values in
   \(\{-\bar z,0,+\bar z\}\), and \(s=v+\varepsilon\).
2. **(S2) A finite menu and calendar.** The plan menu is finite, \(H<\infty\), and each
   compared window belongs to \(\{1,\ldots,H\}\).
3. **(S3) A cutoff selection map.** A Borel step function \(j(s)\) selects the plan.
4. **(S4) Monotone Voice paths and a clean start.** Voice stake paths are weakly increasing
   in the signal and the date. Also \(B_j(s,-1)=b_0\), with \(b_0<\tau\) at every compared
   threshold. Thus the threshold comparison has \(b_0<\tau'<\tau\).
5. **(S5) Legal-clock discipline.** Only Voice plans cross. The crossing date is the first
   date the stake reaches the threshold. A truthful filing lands at \(f=c+T\), and only at the
   disclosure node.
6. **(S6) The flag is public.** Every pooled history contains \(L_{r,e}\), and the date-\(d\)
   information set contains the pooled history through \(d\).
7. **(S7) No-feedback timing.** The executed path, order marks, terminal target, crossing and
   filing dates, filing stake, and flagged order are Borel functions of the plan and signal alone.
   Realised flow and prices do not enter them. Write \(m_d(\theta)\) for the common strategic
   order mark at date \(d\).
8. **(S8) A bounded, pinned kernel.** The premium kernel is \(h=\pi p\), with
   \(\pi=\Pr(a=1\mid\mathcal I)\), \(p\in(0,1)\) continuous in the posterior and price, and
   the pricing rule pins a version of each conditional expectation.
9. **(S9) A finite wedge.** \(0<\Delta_m<\infty\) and
   \(\Delta_{\rm act}=\Delta_m\mathbb E[h(\mathcal I_H)]\).
10. **(S10) Liquidity enters in one place.** The value of \(\kappa\) changes only the law of
    the ternary noise mark.
11. **(S11) Fixed policies.** The menu, cutoff vector, and execution policies are common to
    the two rules and are not re-optimised with \(\kappa\).
12. **(S12) A common noise channel.** The vector \(z_{0:H}\) is independent of
    \((v,\varepsilon,\xi)\) and has the common rule-invariant law \(Q_\kappa\). Pooled flow is
    \(X_d=m_d(\theta)+z_d\). In the order-size-two model the noise marks are independent across
    dates and have probabilities \((\kappa/2,1-\kappa,\kappa/2)\).
13. **(S13) The control-node convention.** On the flagged cell the information set is exactly
    \(\sigma(\mathsf S_{F,r})\), up to pinned price coordinates. On the pooled cell it is
    exactly the displayed public pooled history, again up to pinned prices. The same convention
    applies at each depth \(d\).
14. **(S14) Identified flagged types.** On the tighter rule's flagged signal region, the
    composed terminal target
    \[
       g(s)=b^*_{j(s)}(s)
    \]
    is strictly increasing and
    \(B_{r_+}^F+Q_{r_+}^F=g(s)\). Pointwise strict increase gives a pointwise experiment
    comparison. Strict increase outside a prior-null set gives the same comparison modulo that
    null set and is enough for all posterior conclusions below.

**Theorem.** Fix a common \(\kappa\in[0,1]\). Suppose (S1) to (S14) hold. Compare either
\[
 \tau'<\tau\quad\text{at a common }T,
 \qquad r_+=(\tau',T),\quad r_-=(\tau,T),
\]
with \(b_0<\tau'<\tau\), or
\[
 T'<T\quad\text{at a common }\tau,
 \qquad r_+=(\tau,T'),\quad r_-=(\tau,T).
\]
For every \(d\leq H\), the tighter experiment is Blackwell more informative about
\(\theta=(j(s),s)\). In particular, there is a Markov kernel \(K_d\), independent of the type,
such that
\[
 \mathcal L(Y_{r_-}^d\mid\theta)
 =\int K_d(y,\mathord\cdot)\,
       \mathcal L(Y_{r_+}^d\in \mathrm dy\mid\theta).
\]
No positive-mass condition on either cell is needed. The result includes \(\kappa=0\),
\(\kappa=1\), and the corner \(T=H\). The noise law remains a probability law at both liquidity
endpoints, and nestedness of the filing events does not use an interior window or an interior cell
mass.


Condition (S14) is a transparent sufficient condition, not the logically weakest one. The minimal
replacement is a measurable fiber condition: on each tighter flagged-tuple fiber, the looser-output
channel must factor through that tuple by one type-independent kernel. A measurable decoder supplies
such a factorisation because every fiber is a singleton. Strict monotonicity supplies the decoder in
the paper's model.

The theorem is formally about \(\theta\). It gives the same Blackwell order for the price-relevant
state \((v,a)\). The reason is specific to this model. The engagement flag is a function of
\(\theta\), the conditional law of \(v\) given \(\theta\) is rule-invariant, and, by (S7) and
(S12), both rule outputs are conditionally independent of \(v\) given \(\theta\). Thus the same
kernel also maps the tighter conditional channel given \((v,a)\) into the looser one. Equivalently,
for any posterior \(\nu\) over types,
\[
 \pi(\nu)=\mathbb E_\nu[a(\theta)],
 \qquad
 \widehat v(\nu)=\mathbb E_\nu[\mathbb E(v\mid\theta)],
\]
so the pair used by the price is a linear image of the type posterior. The two state spaces are not
literally identical. Their information ordering agrees here.

The conditions carry the argument as follows.

| Condition | Use |
|---|---|
| (S1) | Gives standard Borel output spaces, measurable conditional laws, and a measurable garbling kernel. |
| (S2) | Makes dates and tagged histories finite and permits the same construction at every \(d\leq H\). |
| (S3) | Makes the plan a measurable function of the recovered signal. |
| (S4), (S5) | Give first-crossing dates and the nesting of filing events at both margins. |
| (S6) | Makes the cell tag observable and makes the public flag coordinates agree on common pooled paths. |
| (S7) | Makes the path and marks common across rules and functions of \(\theta\), so common pooled histories agree. |
| (S8) | Makes appended prices functions of the output. Its kernel content is used in the premium corollary, not in the Blackwell order itself. |
| (S9) | Fixes the sign and scale in the premium corollary. It is not used in the Blackwell order itself. |
| (S10), (S12) | Supply the same type-independent noise channel at the common \(\kappa\), which the kernel redraws. |
| (S11) | Keeps the type-to-path map common when the rule changes. |
| (S13) | States the exact experiment being compared. |
| (S14) | Recovers \(s\), hence \(j(s)\) and \(\theta\), from every tighter flagged output. |

Three corollaries follow.

1. **Posterior variance of engagement.** Under (S1) to (S7) and (S10) to (S14),
   \[
      \mathbb E\!\left[\operatorname{Var}(a\mid\mathcal I_{H,r_+})\right]
      \leq
      \mathbb E\!\left[\operatorname{Var}(a\mid\mathcal I_{H,r_-})\right].
   \]
   More generally, the same inequality holds for every square-integrable function of the type.
2. **Expected premium under curvature.** Assume in addition (S8), (S9),
   \(\mathbb E|v|<\infty\), and equation (g-kernel),
   \(h(\nu)=\mathsf h(\pi(\nu),\widehat v(\nu))\). For \(r\in\{r_+,r_-\}\), define
   \[
      Z_r=\bigl(\Pr(a=1\mid\mathcal I_{H,r}),
                 \mathbb E[v\mid\mathcal I_{H,r}]\bigr)
   \]
   and define the exact curvature set by
   \[
      \mathcal K=
      \overline{\operatorname{co}}\!\left(
        \operatorname{essran} Z_{r_+}\ \cup\
        \operatorname{essran} Z_{r_-}
      \right).
   \]
   Here the closure is part of the definition, so conditional barycentres remain in the set.
   If \(\mathsf h\) is convex on \(\mathcal K\), then
   \[
       \Delta_{\rm act}(r_+)\geq\Delta_{\rm act}(r_-).
   \]
   If it is concave there, the inequality reverses. Every flagged posterior point that occurs with positive probability is in the curvature set.
   More precisely, for prior-almost every signal flagged by rule \(r\),
   \[
      Z_r=\bigl(1,\mathbb E[v\mid s]\bigr).
   \]
   When the flagged cell has positive mass, these \(\pi=1\) points belong to
   \(\operatorname{essran}Z_r\) or its closure and hence to \(\mathcal K\). When its mass is zero,
   no flagged point enters the expected premium. A curvature check that covers only pooled posterior
   pairs is not enough when a flagged cell has positive mass.
3. **Depth and liquidity composition.** Under the date-\(d\) form of (S13), the same Blackwell
   order holds at every \(d\leq H\). If Lemma g2 is also applied to the full tagged experiment,
   using its pooled garbling and the identity map on the flagged cell, then for
   \(0<\kappa_L<\kappa_H<1\),
   \[
      \mathcal E_{r_+}(\kappa_L)
      \succeq_B \mathcal E_{r_+}(\kappa_H)
      \succeq_B \mathcal E_{r_-}(\kappa_H),
   \]
   and also
   \[
      \mathcal E_{r_+}(\kappa_L)
      \succeq_B \mathcal E_{r_-}(\kappa_L)
      \succeq_B \mathcal E_{r_-}(\kappa_H).
   \]
   Thus a tighter rule at lower liquidity intensity dominates a looser rule at higher intensity.
   A tighter rule at higher \(\kappa\) and a looser rule at lower \(\kappa\) have no general
   order. A three-type example below makes the non-order explicit.

#### The worker's proof (from the memo, verbatim)

##### Nested cells

For either margin, a filing event is a type event by (S7). At the threshold margin, the first
crossing of \(\tau'<\tau\) occurs no later than the first crossing of \(\tau\). Hence
\[
 D_{(\tau,T)}^d(\theta)=1\quad\Longrightarrow\quad
 D_{(\tau',T)}^d(\theta)=1.
\]
At the clock margin, \(c(\theta;\tau)+T\leq d\) implies
\(c(\theta;\tau)+T'\leq d\) when \(T'<T\). Therefore, at either margin,
\[
 \mathcal C_{F,r_-}^d\subseteq\mathcal C_{F,r_+}^d,
 \qquad
 \mathcal C_{P,r_+}^d\subseteq\mathcal C_{P,r_-}^d.
\]
This is the nesting used in `lem:threshold-weight` and the weight leg of `thm:clock`, now read at
an arbitrary depth.

##### Recovery on the tighter flagged cell

On \(\mathcal C_{F,r_+}^d\), the observed first two coordinates satisfy
\[
 B_{r_+}^F+Q_{r_+}^F=g(s).
\]
By (S14), this sum has a measurable inverse \(\iota_+\) on its image. Thus
\[
 s=\iota_+(B_{r_+}^F+Q_{r_+}^F),
 \qquad
 \theta=\bigl(j(s),s\bigr).
\]
This is the strictly increasing composed-terminal-target hypothesis carried by
`lem:flagged-kappa-free`. It does the main work. Truthful revelation of \(B^F\) alone would not
suffice. The flagged order \(Q^F\) and the accounting identity for their sum are needed.

##### The garbling kernel

The output space is a disjoint union of the flagged-tuple space and the pooled-history space.
Define \(K_d\) on a tighter output \(y\) as follows.

* If \(y=(P,\mathfrak h)\), retain the core history and set \(K_d(y,\cdot)=\delta_{(P,\mathfrak h)}\). If prices are recorded, discard the tighter price coordinates and append the pinned looser price functions of \(\mathfrak h\).
* If \(y=(F,\mathsf s_F)\), recover \(\widehat\theta\) with \(\iota_+\). If
  \(D_{r_-}^d(\widehat\theta)=1\), emit the deterministic looser flagged tuple
  \((F,\mathsf S_{F,r_-}(\widehat\theta))\).
* If \(y=(F,\mathsf s_F)\) and \(D_{r_-}^d(\widehat\theta)=0\), draw a fresh
  \(z'_{0:d}\sim Q_\kappa\) and emit the looser pooled history
  \[
    \left(P,
      \bigl(m_0(\widehat\theta)+z'_0,\ldots,
            m_d(\widehat\theta)+z'_d;0,\ldots,0\bigr)
    \right).
  \]
  Append the pinned looser prices if the output convention records them.

Every branch reads only \(y\). It never reads the true type. The inverse is measurable by strict
monotonicity. The disclosure test, flagged tuple, and order marks are measurable functions of the
recovered type. The last branch uses a fixed probability law. Define the kernel arbitrarily at
flagged tuples outside the actual tighter image. Thus \(K_d\) is a Markov kernel on the whole
output space.

Fix a type. If it is pooled under the tighter rule, nestedness says it is pooled under the looser
rule. By (S6), (S7), and (S11), the two histories then have the same order flows and the same
all-zero flag coordinates. The first branch is exact for the core history. Recomputing any recorded prices with the looser rule preserves exactness. If the type is flagged under both rules,
the second branch returns its looser tuple. If the tighter rule newly flags it, the third branch
uses its recovered mark path and an independent draw from the same \(Q_\kappa\) that generates the
looser pooled experiment. Its output therefore has exactly the looser conditional law. These cases
prove the displayed Blackwell identity.

The actual control-node information set on a flagged path contains the flagged tuple, not the
pre-filing pooled history. That omitted history does not weaken the claim. Steps 3 to 9 of
`lem:flagged-kappa-free` show that the tuple pins the signal and that the pre-filing history is
conditionally independent of \((v,s,\xi)\) given the tuple. The kernel can redraw all noise needed
for the looser path. If an alternative convention retained the pre-filing history on flagged paths, the order still
follows, but the kernel needs one extra step. On a tighter flagged output it recovers the type,
discards the observed pre-filing noise, redraws \(Q_\kappa\), and appends the lower rule's simulated
pre-filing history whether the lower output is flagged or pooled. Merely projecting and emitting a
bare lower flagged tuple would not reproduce that richer output convention.

##### Posterior corollaries

Use \(K_H\) to couple the two outputs so that
\((v,a,\theta)\), \(Y_{r_+}^H\), and \(Y_{r_-}^H\) form a Markov chain in that order. Put
\(M_r=\mathbb E[a\mid Y_r^H]\). Then
\[
 M_{r_-}=\mathbb E[M_{r_+}\mid Y_{r_-}^H].
\]
The conditional variance identity gives
\[
 \mathbb E\operatorname{Var}(a\mid Y_{r_-}^H)
 -\mathbb E\operatorname{Var}(a\mid Y_{r_+}^H)
 =\mathbb E\operatorname{Var}(M_{r_+}\mid Y_{r_-}^H)\geq0.
\]
Replacing \(a\) by any square-integrable function of \(\theta\) proves the stated extension.

For the premium corollary, the same tower property gives
\[
 Z_{r_-}=\mathbb E[Z_{r_+}\mid Y_{r_-}^H].
\]
Conditional Jensen on \(\mathcal K\) yields
\(\mathbb E\mathsf h(Z_{r_-})\leq\mathbb E\mathsf h(Z_{r_+})\) under convexity. Multiplication by
\(\Delta_m>0\) preserves the inequality. Concavity reverses the Jensen step. This is the same
posterior-martingale step used in Lemma g3(c), but the hull here contains the cells of both full
experiments, including their flagged points.

##### Why the opposite cross-comparison has no order

A three-type experiment gives a direct check. Let types \(A\), \(B\), and \(C\) have positive
prior mass. The looser rule pools all three. The tighter rule newly flags \(A\) and continues to
pool \(B\) and \(C\). Choose \(A\) and \(B\) to have the same coarsened mark path, and choose
\(C\) to differ from them in one round. Such paths are allowed because the order coarsening need
not reveal the size of every stake increment. At \(\kappa_L=0\), the looser flow reveals the mark
path exactly. It separates \(C\) from \(\{A,B\}\), but it cannot separate \(A\) from \(B\). At
\(\kappa_H=1\), the tighter rule separates \(A\) from \(B\) by the cell tag. It does not perfectly
separate \(B\) from \(C\), because an active and an idle round both produce flow \(+\bar z\) with
positive probability. The looser experiment cannot simulate the tighter rule's \(A\)-versus-\(B\)
separation, and the tighter experiment cannot simulate the looser rule's exact \(B\)-versus-\(C\)
separation. The two cross-experiments are Blackwell incomparable.

##### Why identification cannot be dropped without a fiber condition

The conclusion is not guaranteed when the flagged tuple fails to identify the type, even when
no-feedback timing holds. Here is a two-type clock example. Let \(H=2\), \(b_0=0\), \(\tau=1\), \(T'=1\), and \(T=2\). Both types choose Voice and
have signals \(s_L<s_U\), each with prior probability one half. Their stake paths at dates
\((-1,0,1,2)\) are
\[
 B_L=(0,0,1,2),
 \qquad
 B_U=(0,1/2,1,2).
\]
They are weakly increasing in the date and in the signal. Both cross at date 1. Under the shorter
clock both file at date 2 and produce the same flagged tuple
\[
 (B^F,Q^F,a)=(2,0,1).
\]
The terminal target is constant at 2, so (S14) fails.

Let the binary order coarsening be
\(m_d=2\bar z\,\mathbf 1\{B(d)-B(d-1)\geq3/4\}\). The two mark paths are
\[
 m_L=(0,2\bar z,2\bar z),
 \qquad
 m_U=(0,0,2\bar z).
\]
Under the longer clock both types remain pooled because their filing date would be 3. Its date-1
flow has different conditional laws for the two types. At any \(\kappa\in[0,1]\), an active mark
and an idle mark have different flow distributions. The tighter output is the same constant tuple
under both types. A type-independent kernel applied to that constant must have the same output law
under both types, so it cannot reproduce the looser experiment. This example satisfies the nested
clock and monotone-path conditions. The flagged fiber contains two types with different looser-output laws, so neither a decoder nor the weaker fiberwise kernel exists.

No-feedback timing has a separate role. Without (S7), the disclosure rule can change prices, those
prices can change later orders, and the type-to-path map need not be common across rules. The
identity branch on the common pooled set then fails. The filing event and terminal target may also
depend on realised flow rather than on \(\theta\). Nothing in the remaining conditions rules out a
feedback system whose tighter pooled channel is constant while its looser pooled channel separates
two types. The Blackwell order therefore needs either no feedback or a direct replacement
hypothesis that supplies nested cell events and a garbling on the common pooled region.

##### What the theorem does not give

The theorem does not sign the noise sensitivity \(\mathcal S\) or the pooled sensitivity
\(\mathcal S_P\). It orders two level experiments at one common \(\kappa\). Even under convexity,
a pointwise order of expected premiums does not order the absolute derivatives of those premiums
with respect to \(\kappa\). The pooled experiments also use different conditional type laws because
tightening changes who remains in the pool. Their sensitivities still require the weight and
composition analysis.

Once nestedness and (S14) are in hand, the kernel is short. Those inputs are not automatic. The two
information sets are not nested as sigma-algebras because a newly flagged path replaces a pooled
history with a different tuple. The strict target turns that replacement into full type revelation,
which makes simulation possible. The public flag and no-feedback timing make the common pooled
branch identical. This is the content. The theorem fits as the structural link in the two-dial
framing, not as a quantitative headline.

#### What the worker says a script computes at a node

No script or model evaluation is needed. The calibration supplies an exact analytic certificate:
`numerical_v4/menu.py` defines
\[
 b^{*\prime}(s)=
 \frac{\bar b-b_0}{2\sigma_s}
 \left(1+\left(\frac{s-\mu_v}{\sigma_s}\right)^2\right)^{-3/2}>0
\]
when \(\bar b>b_0\) and \(\sigma_s>0\). The same file defines
\(Q^F=b^*(s)-B^F\), so \(B^F+Q^F=b^*(s)\) exactly. `legal_clock` computes the first crossing and
\(f=c+T\). These are algebraic facts, so there is no numerical tolerance to set. A floating-point
check would be weaker than the source formula.

#### The attacker's verdict and nits (verbatim)

Verdict: PASS. Reasons: The kernel construction is exact on all three branches and the branches are chosen by functions of the observed output, so the looser tagged experiment is a garbling of the tighter one at every depth, at both margins, at every kappa in [0,1] and at T = H. (S14) is the only load-bearing addition, it holds at the calibration by the exact identity B^F + Q^F = b*(s) with min slope 2.199e-4 and zero collisions, and the memo's necessity example shows it cannot be dropped under (S13). My main attack line, that the date-d flagged information set cannot contain Q^F before the control node, fails: the model makes the flagged round the filing date, so the tuple is public from that date. A search over a wider model class, 34560 linear programmes asking for any kernel rather than the memo's kernel, with 10148 cases that actually reclassify, found no counterexample; the posterior variance corollary, the alternative convention paragraph and the three-type non-order example all check out, the last also at interior kappa. Eight nits, none of them a hole.

Nits: none of these is a hole and none of them changes the verdict.

1. The theorem writes "In particular, there is a Markov kernel K_d". The kernel is the definition
   of the order being used, not a consequence of it. Read as a definition, the sentence is
   backwards.
2. (S14) carries the accounting identity B^F + Q^F = g(s) only at the tighter rule. Corollary 2's
   sentence that Z_r = (1, E[v | s]) for prior-almost every signal flagged by rule r uses the
   identity at the looser rule too. The fix is one clause, since the looser flagged region sits
   inside the tighter one and `menu.legal_clock` defines Q^F as b*(s) - B^F at every rule. The
   containment of the flagged points in the curvature set does not depend on the fix, because the
   set is defined as the closed convex hull of the two essential ranges.
3. The necessity example is convention dependent, and the memo does not say so. Under the
   alternative convention the memo itself discusses, where a flagged path keeps its pre-filing
   history, the two types are separated by rounds 0 and 1 and the one round the tighter output
   drops carries the same mark for both, so a kernel does exist. I checked it: feasible at kappa
   in {0, 0.3, 0.6, 1}. The example shows that (S14) cannot be dropped under (S13), which is the
   convention in force, and the sentence should say so.
4. Corollary 3 puts the identity map on the flagged cell when it applies Lemma g2 in kappa. That
   step needs the flagged output to be free of kappa, including any appended flagged price. It is
   free of kappa, but the one line that says so is missing at the place it is used.
5. The theorem includes kappa in {0, 1}. That is correct for the order. The calibration never
   evaluates there: `ParamsV4.kappa_floor` is 1e-3 and the grid runs on [0.15, 0.85]. A reader
   may want the endpoint claim marked as a statement about the primitive law.
6. The memo's restatement of (S7) writes "the common strategic order mark", where common means
   common across the two rules. That invariance is (S11) plus the fixed execution policy, not
   (S7). In the code it holds because the mark path never reads the threshold or the window.
7. Part 4 does not say where the result bites at the paper's own grid. At T = 5 the reported
   ladder reclassifies (flagged mass 0.1042, 0.0810, 0.0579, 0.0347, 0.0116), so the order is
   strict. At T = 10, which is the corner T = H, only a type crossing on date 0 can file, and
   every threshold in the ladder gives the same flagged set with mass 0.000681, so the two
   experiments coincide and the order is an equality there.
8. The RESULT block lists only `memo.md` under `files_changed`, which was right when it was
   written. This attack adds four scripts and four records in the same directory.

### Candidate 4.1: Order size two is the erasure regime

#### The conjecture as first posed

Conjecture. With a ternary noise lump of size one and a building order of b lumps, the pooled
experiment at liquidity κ is a garbling of the one at κ' < κ for every pair (monotone in κ) if
and only if b = 2. At b = 1 informativeness is non-monotone in κ (the flow reveals the mark at
κ = 0 and again at κ = 1 by parity; the ambiguous values 0 and 1 carry likelihood ratios
(κ/2)/(1−κ) and its inverse). At b ≥ 3 the two flow supports are disjoint and the pool hides
nothing. So b = 2 is the only ratio at which noise garbles building without confounding it.

Why it matters. It turns the one primitive change (ADR 0003, defended today by a paragraph) into
a proposition, and answers the referee objection that the order size was chosen to make the
theorem work. Lemma g1 in `proofs/02_garbling.tex` already carries most of the b = 2 half.

Expected cost: low. Expected outcome: true, with a short proof and a two-line counterexample at
b = 1 (a finite Blackwell comparison, checkable by a linear program).

#### Gate outcome

Writer: GPT 5.6 Sol at xhigh effort, memo status PASS. Attacker: Claude Opus 5, verdict PASS with five nits. The attacker rebuilt the Lemma g2 kernel from its text (residual 1e-16), ran a Blackwell linear programme over 1,176 interior kappa pairs at order size one (no upward garbling), and confirmed the decision-problem values exactly. Its first nit corrects a side remark: the exact turn at 2/3 and the word "incomparable" are one-round facts and fail for the full history.

#### The worker's statement (from the memo, verbatim)

##### Hypotheses

The proposition uses the paper's standing conditions with the following names.

1. (S1) One probability space. The primitive vector and the noise marks have a joint law on a
   finite product of Polish spaces.
2. (S2) A finite menu and a finite calendar. The plan menu is finite and the depth satisfies
   $d\leq H<\infty$.
3. (S3) A cutoff selection map. A step function maps the signal into a plan.
4. (S4) Monotone Voice paths and a clean start. The stake paths satisfy the paper's monotonicity
   and initial-stake conditions.
5. (S5) Legal-clock discipline. Only Voice plans cross the threshold, and a filing lands through
   the disclosure node after the window margin.
6. (S6) The flag is public. The history records whether a filing has landed.
7. (S7) No-feedback timing. At fixed policies, the type determines the mark path. Realised flow
   and price do not change it.
8. (S8) A bounded, pinned kernel. The paper uses one pinned version of the engagement-premium
   kernel.
9. (S9) A finite wedge. The premium wedge is finite and strictly positive.
10. (S10) Liquidity enters in one place. The intensity $\kappa$ changes only the noise law.
11. (S11) Fixed policies. The plan menu, execution policies, and cutoff vector stay fixed in
    $\kappa$ and across the experiments compared.
12. (E1) Exact independent ternary noise. For a fixed $\bar z>0$, the variables $z_e$ are
    independent across rounds and independent of the type, with
    \[
    \Pr_\kappa(z_e=-\bar z)=\Pr_\kappa(z_e=+\bar z)=\kappa/2,
    \qquad
    \Pr_\kappa(z_e=0)=1-\kappa.
    \]
13. (E2) Integral order size. For one positive integer $b$, every mark is
    $m_e\in\{0,b\bar z\}$ and $X_e=m_e+z_e$.
14. (E3) Nondegenerate mark experiment. The state set $\mathcal M$ is any subset of
    $\{0,b\bar z\}^{d+1}$ that contains at least two distinct mark paths. In a pooled cell,
    $\mathcal M$ is the set of paths with positive conditional probability. The cell event is a
    type event of positive mass, so it does not change the conditional noise law.

Conditions (S3) to (S6), (S8), and (S9) place the experiment inside the paper's model. The
information comparison itself uses (S1), (S2), (S7), (S10), (S11), and (E1) to (E3).

For $m=(m_0,\ldots,m_d)\in\mathcal M$, let $P^b_\kappa(\cdot\mid m)$ be the law of
$X_{0:d}$. Say that $E^b_{\kappa'}$ is a garbling of $E^b_\kappa$ if there is a Markov kernel
$\Lambda$ on flow histories, independent of $m$, such that
\[
P^b_{\kappa'}(y\mid m)
 =\sum_x P^b_\kappa(x\mid m)\Lambda(y\mid x)
\quad\text{for every }m\in\mathcal M\text{ and every }y.
\]
The experiment fully reveals the mark path if a decoder $g$ satisfies
$g(X_{0:d})=m$ with $P^b_\kappa(\cdot\mid m)$ probability one for every $m\in\mathcal M$.
Equivalently, distinct rows of the finite experiment have disjoint supports. Under any
full-support prior, this is equivalent to a degenerate posterior over the mark path almost
surely.

##### Proposition

Under (S1) to (S11) and (E1) to (E3), the following two properties hold together if and only if
$b=2$:

1. for every $0<\kappa<\kappa'<1$, $E^b_{\kappa'}$ is a garbling of
   $E^b_\kappa$;
2. for every $\kappa\in(0,1)$, $E^b_\kappa$ does not fully reveal the mark path.

The three regimes are exact.

1. If $b=2$, the garbling result holds more widely for
   $0\leq\kappa<\kappa'\leq1$. The experiment fails to reveal any nondegenerate mark-path state
   set for every $\kappa\in(0,1]$, while $\kappa=0$ fully reveals it.
2. If $b=1$, the experiment is not fully revealing for $\kappa\in(0,1)$, but
   $E^1_{\kappa'}$ is not a garbling of $E^1_\kappa$ for any
   $0<\kappa<\kappa'<1$. Both endpoint experiments, at $\kappa=0$ and $\kappa=1$, fully reveal
   the one-round mark.
3. If $b\geq3$, every experiment fully reveals the mark path for every
   $\kappa\in[0,1]$. All liquidity nodes are Blackwell equivalent because each one reveals the
   state and can simulate every other node.

For $b=1$, one round also gives the exact Blackwell turn. Write $E_t=E^1_t$ on the two-state
space $\{0,\bar z\}$. For $0<\kappa<\kappa'<1$,
\[
E_\kappa\text{ is a garbling of }E_{\kappa'}
\quad\Longleftrightarrow\quad
2\kappa'+\kappa\geq2.
\]
The reverse relation never holds. Thus experiments with
$0<\kappa<\kappa'<2/3$ are incomparable. On $[2/3,1)$, higher $\kappa$ is strictly more
informative, which is the reverse of the proposed liquidity ordering. Across $2/3$, higher
$\kappa'$ dominates lower $\kappa$ exactly when $\kappa'\geq1-\kappa/2$; otherwise they are
incomparable. The value of the symmetric correct-guess problem falls up to $\kappa=2/3$ and
rises after it. The overlapping signals exchange their likelihood ranking at that same point.

This is a statement about the mark path. At fixed policies, type maps deterministically into
mark path and then into flow. The $b=2$ kernel therefore also garbles the experiment about the
paper's type, including after conditioning on a pooled cell event. Full revelation of the mark
path need not reveal the type when two types have the same path, so the uniqueness claim is not
stated for type revelation. One round settles both only-if regimes. The full-history statement
is needed for the positive $b=2$ result and is already supplied by Lemma g2.

#### The worker's proof (from the memo, verbatim)

Scale flows by $\bar z$ and write
\[
a_t=t/2,\qquad c_t=1-t.
\]
This loses no information because $\bar z>0$.

##### The regime $b=2$

The garbling claim for interior liquidity nodes is exactly Lemma g2 in
`proofs/02_garbling.tex`. Its kernel reads the revealed set
\[
R_d=\{e\leq d:X_e\neq1\},
\]
deletes each member independently with probability
\[
\delta=\frac{\kappa'-\kappa}{2-\kappa},
\]
emits $1$ on deleted and already erased rounds, and redraws a surviving flow from the
$\kappa'$ conditional law given the mark. Lemma g1 shows that the input history identifies the
mark on every member of $R_d$. Lemma g2 then verifies the kernel identity for every type and
hence for every mark path. This memo does not re-prove that lemma.

The same formula covers $\kappa=0$ and $\kappa'=1$. For
$0\leq\kappa<\kappa'\leq1$, its deletion probability lies in $[0,1]$. At $\kappa=0$ every round
starts in $R_d$, and at $\kappa'=1$ the conditional redraw puts all surviving mass on the
nonzero-noise revealing value. Thus no limiting argument is needed.

It remains to settle revelation. Take two distinct paths $m,m'$. At a coordinate where they
differ, flow $1$ has probability $\kappa/2$ under either mark. At a coordinate where both marks
are zero, flow $-1$ has probability $\kappa/2$ under both paths. At a coordinate where both
marks are two, flow $3$ has probability $\kappa/2$ under both paths. These choices give one
common flow history with positive probability under both paths whenever $\kappa>0$. Their row
supports overlap, so no decoder can fully reveal the path. At $\kappa=0$, flow equals the mark
coordinate by coordinate and does reveal it.

##### The regime $b=1$

For one round, with rows indexed by marks $0,1$ and columns indexed by flows $-1,0,1,2$, the
experiment is
\[
A_t=
\begin{pmatrix}
a_t&c_t&a_t&0\\
0&a_t&c_t&a_t
\end{pmatrix}.
\tag{1}
\]
For interior $t$, the rows overlap at flows $0$ and $1$. Products of these common-support
values give a common history for any two mark paths, so the path is not fully revealed.
At $t=0$, the flow equals the mark. At $t=1$, the row supports are $\{-1,1\}$ and $\{0,2\}$.
Both endpoints are fully revealing.

Now fix $0<\kappa<\kappa'<1$. Give the two one-round marks equal prior probability. There are
two actions, abstain and claim that the mark is zero. Abstention pays zero. A correct claim pays
one and a false claim pays $-C$, where
\[
C>
\max_{t\in\{\kappa,\kappa'\}}
\left\{\frac{a_t}{c_t},\frac{c_t}{a_t}\right\}.
\]
All displayed ratios are finite. Under either experiment, the unique flow at which a claim has
positive conditional value is $-1$. The value of the decision problem at node $t$ is therefore
$a_t/2=t/4$. It is strictly larger at $\kappa'$ than at $\kappa$. A garbling cannot raise the
value of any decision problem. Hence $E_{\kappa'}$ is not a garbling of $E_\kappa$. This
one-round counterexample also applies to a longer nondegenerate path experiment. Put prior mass
on two distinct paths and let $q$ be the number of coordinates at which they differ. Choose the
false-claim loss above every finite likelihood ratio at both nodes. A claim then pays only on
histories that have zero likelihood under the other path. Under the claimed path, their total
probability is $1-(1-a_t)^q$. It rises strictly with $t$, so the decision value is again larger
at $\kappa'$.

For completeness, the reverse Blackwell relation has a closed form. Suppose
$2\kappa'+\kappa\geq2$, put
\[
r=\frac{\kappa'-\kappa}{3\kappa'-2},
\]
and index both the rows and columns of the following kernel by $-1,0,1,2$:
\[
K_{\kappa'\to\kappa}=
\begin{pmatrix}
\kappa/\kappa'&1-\kappa/\kappa'&0&0\\
0&1-r&r&0\\
0&r&1-r&0\\
0&0&1-\kappa/\kappa'&\kappa/\kappa'
\end{pmatrix}.
\tag{2}
\]
The inequality implies $\kappa'>2/3$ and $0\leq r\leq1$, so (2) is a Markov kernel. Direct
multiplication gives
\[
A_{\kappa'}K_{\kappa'\to\kappa}=A_\kappa.
\]
Thus $E_\kappa$ is a garbling of $E_{\kappa'}$. Applying the kernel independently across rounds
proves the same relation for every mark-path state set.

If $2\kappa'+\kappa<2$, consider instead the two-action problem that pays one for a correct
mark guess and zero for a wrong guess, under the uniform prior. Its value at node $t$ is
\[
V(t)=\frac{1+\operatorname{TV}(A_t(\cdot\mid0),A_t(\cdot\mid1))}{2}
=
\begin{cases}
1-t/2,&0\leq t\leq2/3,\\
t,&2/3\leq t\leq1.
\end{cases}
\tag{3}
\]
The inequality $2\kappa'+\kappa<2$ gives $V(\kappa)>V(\kappa')$. Therefore
$E_\kappa$ cannot be a garbling of $E_{\kappa'}$. The false-claim problem already showed that
the relation in the other direction also fails. This proves incomparability and the exact
condition. Formula (3) has its unique minimum at $2/3$. At that node $a_t=c_t$, so flows $0$
and $1$ have likelihood ratio one. Their likelihood rankings reverse on the two sides of the
node.

##### The regime $b\geq3$

The idle support is $\{-1,0,1\}$ and the building support is
$\{b-1,b,b+1\}$. They are disjoint when $b\geq3$. The decoder reads mark zero from a flow at
most one and mark $b$ from a flow at least two, coordinate by coordinate. It works at every
$\kappa\in[0,1]$.

There is also an explicit kernel between any two liquidity nodes. Read the mark from the input
flow, draw fresh ternary noise with the target node's law, and emit the decoded mark plus the
fresh noise. The kernel does not use the unknown state beyond what the input already reveals.
It maps every row at the source node to the corresponding row at the target node. Reversing the
nodes gives the reverse kernel, so all nodes are Blackwell equivalent.

The $b=2$ regime satisfies both properties in the proposition. The $b=1$ regime fails the first.
The $b\geq3$ regime fails the second. This proves the equivalence.

##### Wider symmetric noise support

The same support argument gives a short extension. Suppose integer noise has support
$\{-L,\ldots,L\}$ and a symmetric law. The supports under marks zero and $b$ meet in exactly
one flow if $b=2L$. The common flow is $L$, and symmetry gives it the same probability under
both marks. Thus $b=2L$ is the erasure form guaranteed by symmetry alone. If a family of laws
raises the endpoint mass $\Pr(z=L)=\Pr(z=-L)$, the deletion and conditional-redraw kernel from
Lemma g2 applies. Orders $b>2L$ fully reveal the mark. Orders $b<2L$ have several common flows
and need extra equalities such as $p(z)=p(z-b)$ on the overlap to be an erasure experiment.
Those equalities can hold for special laws, including a uniform law, but symmetry alone does not
imply them.

#### What the worker says a script computes at a node

No calibration computation is needed. The result is an exact comparison of finite channel
matrices and does not depend on the policy cutoffs, threshold ladder, horizon calibration, or
premium kernel.

A regression test would only check algebra already displayed here. For selected interior pairs,
it could require nonnegative kernel entries and row sums within $10^{-12}$ of one, and require
$\lVert A_{\kappa'}K-A_\kappa\rVert_\infty\leq10^{-12}$ for (2). No pooled pass, policy solve,
or compute lock is needed.

#### The attacker's verdict and nits (verbatim)

Verdict: PASS. Reasons: I could not break the proposition. The order size two kernel of Lemma g2, rebuilt from its own text, reproduces the target channel to 1.1e-16 at interior pairs and exactly at the endpoints (0,0.3), (0.5,1) and (0,1), and the two supports meet at one flow value, so no two distinct mark paths are separated at any kappa in (0,1]. At order size one a Blackwell program over 1176 interior pairs finds no upward garbling, the memo's two-action false-claim value is exactly t/4 and its multi-round value is exactly 1-(1-t/2)^q, and the reverse kernel matches its stated region 2*kappa'+kappa>=2 at every grid pair with residual 2.2e-16. At order size three and four the supports are disjoint and the nodes are Blackwell equivalent both ways. The added hypotheses (E1) to (E3) are named, are needed, and match the model, and I found no use of the order-size-one pooled law and no support assumption on the pooled posterior. Nits only: the exact turn at two thirds and the word incomparable are one-round facts and fail for the full history (at order size one, two rounds, paths (0,0) and (1,1), kappa=0.55 and kappa'=0.70 with 2*kappa'+kappa=1.95 the lower node is an exact garbling of the higher one, certified in exact fractions); the Lemma g2 citation covers types while (E3) admits unrealised mark paths; the threshold theorem uses Lemma g3(b), not Lemma g2; the summary sentence about one round understates the memo's own multi-round argument; and (E3) is left unchecked at the calibration.

Nits:

1. The exact turn at two thirds is a one-round fact and does not describe the paper's experiment.
   The memo scopes it correctly, writing "one round also gives the exact Blackwell turn" and
   fixing the two-state space. That scoping is what saves it, and the paper must keep it. The
   necessity half fails for the full mark-path history. Counterexample: order size one, two
   rounds, mark paths (0, 0) and (1, 1), kappa = 0.55 and kappa' = 0.70. Then
   2 kappa' + kappa = 1.95 < 2, so the memo's rule says the two nodes are incomparable, yet the
   two-round experiment at 0.55 is an exact garbling of the two-round experiment at 0.70. The
   exact rational check certifies it with no linear program: the two posterior laws under the
   uniform prior have the same mean and every call payoff is weakly larger at 0.70, which is the
   two-state Blackwell criterion. The linear program independently returns a kernel with residual
   below 1e-16. The same happens at (0.62, 0.68) and at (0.45, 0.75), and at path length three
   also at (0.15, 0.9) and (0.25, 0.85). The region grows with the path length, so the sentence
   "otherwise they are incomparable" is true for one round and false for the model's history. The
   direction the paper actually needs is untouched: higher liquidity is never a garbling of lower
   liquidity at order size one, at every path length I checked. If any of this reaches the paper,
   the turn must be stated as a single-round fact and the word incomparable must carry the same
   qualifier.

2. The citation of Lemma g2 covers types, while (E3) admits mark paths. (E3) lets the state set
   be any subset of the mark-path cube, which may contain paths that no type in the model
   realises. Lemma g2 is stated and proved for every type. The memo writes "for every type and
   hence for every mark path", and that inference runs the wrong way for an unrealised path. The
   content is fine, because the conditional law of flow depends on the type only through its mark
   path and the g2 proof is verbatim a per-path argument, and I checked the kernel identity row by
   row for all four two-round paths. One clause fixes the wording.

3. Section 4 says the threshold theorem "already fixes order size two and uses Lemma g2". In
   `proofs/02_garbling.tex` the threshold theorem rests on the factorisation, the combinatorial
   weight leg and Lemma g3(b). Lemma g2 is not invoked in its proof. The conclusion, that nothing
   changes there, is right; the reason given is not.

4. "One round settles both only-if regimes" understates the memo's own work. A one-round failure
   does not by itself give the failure for an arbitrary, possibly non-product, state set of paths.
   The memo supplies the q-coordinate argument that does, so only the summary sentence is loose.

5. The memo says no calibration computation is needed, which is right, but (E3) is an added
   hypothesis about the model and is left unchecked. One line would close it: the pooled cell of
   a policy carries at least two accumulation lengths, so it carries at least two mark paths.
   Where it does not, the pooled premium is free of kappa and the threshold theorem's own
   non-degeneracy hypothesis already fails.

### Candidate 4.2: One cut identity for both dials

#### The conjecture as first posed

Conjecture. The cut identity of `cor:caught` (`proofs/03_caught.tex`, part (iii): the looser
rule's pooled sensitivity is the mass-weighted average of what the tighter rule leaves in the
pool and what it removes, with the survivors' re-pricing term) holds verbatim for the threshold
margin, because tightening the threshold also produces nested flagged cells
C_F(τ,T) ⊆ C_F(τ',T) for τ' < τ (crossing dates are weakly earlier and monotone in the signal,
standing conditions (S4) and (S5)). Under both dials the removed set is the top slice of the
silent pool's Voice types. Condition D (C_τ ≤ 1) is then the same band condition on the removed
set's sensitivity as (iv) of the corollary.

Second, harder part. A sufficient condition on primitives for the band condition, for instance
that a type-level sensitivity contribution is monotone in the signal on the pool's Voice region.
Any such condition will be conditional: the grid record
`numerical_v4/checks/t2_threshold_revelation_check.json` shows Condition D failing just below
κ = 0.15, so a universal claim is false. A condition that holds where the grid holds and is
checkable at a node is the target.

Why it matters. One identity, two dials, one question ("is what gets caught more noise-sensitive
than what stays"), instead of a Condition D for the threshold and a separate corollary for the
clock. The first part is close to transcription; the second is the real mathematics.

#### Gate outcome

Writer: GPT 5.6 Sol at max effort, memo status PASS on both parts. Attacker: Claude Opus 5, verdict PASS on both parts with eight nits. The attacker reproduced every number from the record's coefficients with independent code, ran 400,000 random draws against the Part 1 algebra and 7,585 random coefficient triples against the Part 2 implication with no violation, and sharpened one fact: for the pair q0.5 to q0.3, C_tau > 1 exactly on [0.143673, 0.149012], so the certificate cutoff is the exact endpoint of the Condition D failure.

#### The worker's statement (from the memo, verbatim)

##### Standing hypotheses

Both parts use the standing conditions from the partition subsection.

1. **(S1) One probability space.** The primitive vector has a joint law on a finite product of Polish spaces. The signal is $s=v+\varepsilon$, and each noise mark lies in $\{-\bar z,0,+\bar z\}$.
2. **(S2) A finite menu and calendar.** The plan menu is finite, $H<\infty$, and $T\in\{1,\ldots,H\}$.
3. **(S3) A cutoff selection map.** A step function with finitely many breakpoints maps the signal into a plan.
4. **(S4) Monotone Voice paths and a clean start.** Each plan has $B_j(s,-1)=b_0$. Voice paths are weakly increasing in the signal and in the date. The clean-start inequality for the pair appears in (C$\tau$-1).
5. **(S5) Legal-clock discipline.** Only Voice plans cross. The crossing date is the first date at which the stake reaches the threshold. A filing lands at $c_j+T$ through the disclosure node and reports the stake truthfully.
6. **(S6) The flag is public.** A pooled history records whether the filing has landed by each date, and the control-node information set contains the pooled history.
7. **(S7) No-feedback timing.** The executed path, order marks, terminal target, crossing date, filing date, filing stake, and flagged order depend only on the plan and signal. They do not depend on realised order flow or prices.
8. **(S8) A bounded, pinned kernel.** The kernel is $h(\mathcal I)=\pi(\mathcal I)p(\mathcal I)$. The pricing rule pins a version at every information set. The entry probability is continuous in the posterior and price.
9. **(S9) A finite positive wedge.** $0<\Delta_m<\infty$ and $\Delta^{\rm act}=\Delta_m\mathbb E[h(\mathcal I_H)]$.
10. **(S10) Liquidity enters once.** $\kappa$ enters the primitives only through the ternary noise law. The laws of $v$, the signal noise, and the bidder draw do not depend on $\kappa$.
11. **(S11) Fixed policies.** The menu, execution policies, and cutoff vector are held fixed in $\kappa$ and across the two rules.

The following hypotheses are the threshold analogues of (C-1) to (C-3).

1. **(C$\tau$-1) A fixed threshold cut.** Fix a common $T$ and $\kappa$ and compare $b_0<\tau'<\tau$. The tighter rule is $(\tau',T)$. Conditions (S4), (S5), and (S7) make both disclosure indicators functions of the same plan and signal. Conditions (S10) and (S11) hold throughout the liquidity comparison.
2. **(C$\tau$-2) Differentiability and pinned versions.** The maps
   
   $$
   \kappa\longmapsto \mathbb E[h^{(\tau)}\mid A]
   \quad\text{and}\quad
   \kappa\longmapsto \mathbb E[h^{(\tau')}\mid A\setminus B]
   $$
   
   are differentiable at the compared $\kappa$. The superscript identifies the information set supplied by that rule. Condition (S8) pins both kernels. For the optional split of the caught leg, $\mathbb E[h^{(\tau)}\mid B]$ is also differentiable.
3. **(C$\tau$-3) Non-degeneracy and factorisation.** $0<\Pr(B)<\Pr(A)$, $0<\Omega(\tau,T)$, $\Omega(\tau',T)<1$, and
   
   $$
   s_A:=\partial_\kappa\mathbb E[h^{(\tau)}\mid A]\ne0.
   $$
   
   The hypotheses of Proposition `prop:factorisation`, including flagged-endpoint invariance, hold at both thresholds whenever the aggregate criterion is invoked.
4. **(C$\tau$-4) Erasure representation.** Only the identification with Condition D and Part 2 require order size two and $\kappa\in(0,1)$, so that Lemmas g1 to g3 apply. Parts (i) to (vi) of the cut result do not require this clause.

Set

$$
A=\mathcal C_P(\tau,T),\qquad
B=\mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T),\qquad
\varphi=\frac{\Pr(B)}{\Pr(A)}.
$$

Define

$$
\begin{aligned}
s_{A\setminus B}
  &=\partial_\kappa\mathbb E[h^{(\tau')}\mid A\setminus B],\\
\widetilde s_B
  &=\partial_\kappa\mathbb E[h^{(\tau)}\mid B],\\
\delta
  &=\partial_\kappa\mathbb E[h^{(\tau')}-h^{(\tau)}\mid A\setminus B],
\end{aligned}
$$

and define the caught leg by

$$
 s_B:=\frac{1}{\Pr(B)}\partial_\kappa\left(
 \mathbb E[h^{(\tau)}\mathbf 1_A]
 -\mathbb E[h^{(\tau')}\mathbf 1_{A\setminus B}]
 \right). \tag{1}
$$

This $s_B$ includes the re-pricing of the histories that remain pooled.

##### Part 1: threshold cut corollary

**Status: PASS.** Under (S1) to (S11) and (C$\tau$-1) to (C$\tau$-3), the who-gets-caught corollary holds at the threshold margin as follows.

1. **Nestedness.**
   
   $$
   \mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T),\qquad
   B\subseteq A,\qquad
   A\setminus B=\mathcal C_P(\tau',T).
   $$
   
   Also $\varphi\in(0,1)$ and
   
   $$
   W_\tau=\frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)}=1-\varphi\le1. \tag{2}
   $$
2. **Kappa-free masses.** $\partial_\kappa\Pr(A)=\partial_\kappa\Pr(B)=0$, so $\varphi$ does not depend on $\kappa$.
3. **Cut identity.**
   
   $$
   \begin{aligned}
   s_{A\setminus B}
   &=\frac{\Pr(A)s_A-\Pr(B)s_B}{\Pr(A)-\Pr(B)}\\
   &=\frac{s_A-\varphi s_B}{1-\varphi}\\
   &=\frac{s_A-\varphi\widetilde s_B}{1-\varphi}+\delta, \tag{3}
   \end{aligned}
   $$
   
   where the last line uses the extra differentiability in (C$\tau$-2). Equivalently,
   
   $$
   s_A=(1-\varphi)s_{A\setminus B}+\varphi s_B,
   \qquad
   s_B=\widetilde s_B-\frac{1-\varphi}{\varphi}\delta. \tag{4}
   $$
4. **Composition ratio.**
   
   $$
   C_\tau=\frac{|s_A-\varphi s_B|}{(1-\varphi)|s_A|}, \tag{5}
   $$
   
   and
   
   $$
   C_\tau\le1
   \quad\Longleftrightarrow\quad
   (s_B-s_A)\bigl(\varphi s_B-(2-\varphi)s_A\bigr)\le0. \tag{6}
   $$
   
   Thus $C_\tau\le1$ exactly when $s_B$ lies weakly between $s_A$ and $((2-\varphi)/\varphi)s_A$. Under (C$\tau$-4), Lemma g3 gives $\mathcal S_P=(\Delta_m/2)|\mathcal W|$, so Condition D is equivalent to (6).
5. **Aggregate criterion.**
   
   $$
   W_\tau C_\tau=\frac{|s_A-\varphi s_B|}{|s_A|}, \tag{7}
   $$
   
   and
   
   $$
   W_\tau C_\tau\le1
   \quad\Longleftrightarrow\quad
   s_B(2s_A-\varphi s_B)\ge0. \tag{8}
   $$
   
   This is equivalent to $s_B$ lying weakly between $0$ and $(2/\varphi)s_A$. With the factorisation hypotheses in (C$\tau$-3), (8) is also equivalent to the tighter threshold weakly lowering the aggregate liquidity sensitivity.
6. **Readings.** Let $\rho=s_B/s_A$.
   
   a. If $s_As_B\le0$, including $s_B=0$, then $C_\tau>1$.
   
   b. If $s_As_B>0$, then $C_\tau\le1$ if and only if
   
   $$
   |s_A|\le|s_B|\le\frac{2-\varphi}{\varphi}|s_A|.
   $$
   
   c. If $s_{A\setminus B}s_A\ge0$, then $C_\tau\le1$ if and only if $\rho\ge1$. Under the common sign this says $|s_B|\ge|s_A|$. Under that same sign, the proviso itself is $|s_B|\le|s_A|/\varphi$.
   
   d. $W_\tau C_\tau\le1$ if and only if $s_B$ has the sign of $s_A$ or is zero, and $|s_B|\le(2/\varphi)|s_A|$.
   
   e. The upper limits $(2-\varphi)/\varphi$ and $2/\varphi$ fall as $\varphi$ rises and diverge as $\varphi\downarrow0$. If $M\ge1$, $\varphi\le2/(1+M)$, and $|s_B|\le M|s_A|$, the upper limits are slack. The composition condition then asks for a common sign and $|s_B|\ge|s_A|$. The aggregate condition asks only for a common sign or $s_B=0$.

The threshold version needs one clean-start clause that the clock comparison does not: $b_0<\tau'$. It puts the first-passage and clock equivalence in force at the tighter threshold as well as at $\tau$. Order size two is not needed for the cut algebra. It is needed only to call the resulting band Condition D through Lemma g3.

##### Part 2: a single-crossing revelation certificate

**Status: PASS for the implication, with a numerical calibration check.** Inherit Part 1 and (C$\tau$-4). Write

$$
c^A_k=c_k(\tau,T),\qquad
c^R_k=c_k(\tau',T),\qquad
d_k=c^R_k-c^A_k,
$$

where $R=A\setminus B$ is the pool that remains under the tighter threshold. These are the kappa-free coefficients of Lemma g3. For any vector $v=(v_0,\ldots,v_H)$ define its reversed polynomial

$$
P_v(x)=\sum_{k=0}^H v_kx^{H-k},
\qquad
x=x(\kappa):=\frac{\kappa}{2-\kappa}. \tag{9}
$$

Add the following hypotheses.

1. **(R1) One crossing for each pooled cell.** After coefficients with value zero are deleted, both sequences $(c^A_0,\ldots,c^A_H)$ and $(c^R_0,\ldots,c^R_H)$ change sign exactly once, from negative to positive. Their first and last coefficients are strictly negative and strictly positive, respectively.
2. **(R2) One crossing for the survivor difference.** After zeros are deleted, $(d_0,\ldots,d_H)$ changes sign exactly once, from positive to negative. Its first and last coefficients are strictly positive and strictly negative, respectively.
3. **(R3) Liquidity is above the three revelation roots.** Let $r_A,r_R,r_D$ be the unique positive roots of $P_{c^A}$, $P_{c^R}$, and $P_d$. Then
   
   $$
   x(\kappa)\ge r_*:=\max\{r_A,r_R,r_D\}. \tag{10}
   $$

Under (R1) to (R3),

$$
0\le s_{A\setminus B}\le s_A,
$$

and the caught leg satisfies the stronger bounds

$$
s_A\le s_B\le\frac{s_A}{\varphi}
<\frac{2-\varphi}{\varphi}s_A. \tag{11}
$$

The strict last inequality uses $s_A>0$, which follows from (C$\tau$-3) and the displayed slope order. Hence the band condition and $C_\tau\le1$ hold. This condition says that more erasure raises the pooled premium in both pools, while the pool that survives the tighter rule is weakly less sensitive to that erasure. The cut identity assigns the missing sensitivity to the premium mass removed by the tighter threshold. That caught leg includes survivor re-pricing. It is more noise-sensitive than the original pool, but not enough to reverse the survivor sensitivity.

Once the common slope direction is known, the difference-root clause is algebraically the same order that Condition D tests. The certificate is therefore an interval certificate on kappa-free objects, not a deeper shape restriction on the kernel. Its gain is that three one-crossing sign lists reduce a continuum of liquidity comparisons to one root cutoff. The roots also locate why the below-grid pair fails.

At the frozen calibration, the certificate holds on the full continuous interval $\kappa\in[0.15,0.85]$ for each of the four non-null $T=5$ pairs. The table reports each root after conversion to the $\kappa$ scale:

| threshold quantiles $q\to q'$ | $\kappa(r_A)$ | $\kappa(r_R)$ | $\kappa(r_D)$ | $\kappa_*$ |
|---|---:|---:|---:|---:|
| $0.9\to0.7$ | 0.048670563 | 0.108569232 | 0.028758461 | 0.108569232 |
| $0.7\to0.5$ | 0.108569232 | 0.145962695 | 0.094456809 | 0.145962695 |
| $0.5\to0.3$ | 0.145962695 | 0.126033933 | 0.149012173 | 0.149012173 |
| $0.3\to0.1$ | 0.126033933 | 0.091805343 | 0.133523094 | 0.133523094 |

The smallest gap between a cutoff and the grid's lower endpoint is $0.15-0.149012173=0.000987827$. The $0.5\to0.3$ cutoff also separates the reported failure interval. On $[0.1440,0.145962695)$ the two pooled slopes do not have the required common direction. At $0.145962695$ the original-pool slope is zero, so the ratio is undefined. On $(0.145962695,0.149012173)$ both slopes have the same direction, but the survivor is more sensitive than the original pool. The reported failure endpoint $0.1485$ is below the certificate cutoff. At $T=10$ all four cuts are null: the reclassified mass is zero and the paired coefficient vectors are identical. Thus $C_\tau=1$ wherever their common sensitivity is nonzero, including every recorded grid node. The ratio is undefined at a zero of that common sensitivity. The caught share and caught leg are not defined for these null cuts.

#### The worker's proof (from the memo, verbatim)

##### Part 1

For each threshold, the clock equivalence from (S4), (S5), and the clean start gives

$$
D(\tau,T)=\mathbf 1\{a=1\}\mathbf 1\{B(s,H-T)\ge\tau\}.
$$

If $D(\tau,T)=1$, then the same path satisfies $B(s,H-T)\ge\tau>\tau'$, so $D(\tau',T)=1$. This proves the flagged-set inclusion. Taking complements gives $A\setminus B=\mathcal C_P(\tau',T)$. The mass identities then give (2). The strict inequalities in (C$\tau$-3) give $0<\varphi<1$.

By (S7), both disclosure indicators are functions of the plan and signal. By (S10), $\kappa$ moves only the order-flow noise. By (S11), neither the cutoff selection nor the executed paths move with it. Thus $A$, $B$, and their probabilities do not move with $\kappa$. This proves part 1(ii).

Let

$$
\Lambda_\tau=\mathbb E[h^{(\tau)}\mathbf1_A],
\qquad
\Lambda_{\tau'}=\mathbb E[h^{(\tau')}\mathbf1_{A\setminus B}].
$$

The kappa-free masses and (C$\tau$-2) imply

$$
\partial_\kappa\Lambda_\tau=\Pr(A)s_A,
\qquad
\partial_\kappa\Lambda_{\tau'}=
(\Pr(A)-\Pr(B))s_{A\setminus B}.
$$

Definition (1) therefore gives

$$
\Pr(B)s_B=\Pr(A)s_A-(\Pr(A)-\Pr(B))s_{A\setminus B}.
$$

Solving and dividing by $\Pr(A)>0$ proves the first two lines of (3) and the average identity in (4).

For the split, use $\mathbf1_A=\mathbf1_B+\mathbf1_{A\setminus B}$:

$$
\begin{aligned}
\Lambda_\tau-\Lambda_{\tau'}
&=\Pr(B)\mathbb E[h^{(\tau)}\mid B]\\
&\quad-\Pr(A\setminus B)
\mathbb E[h^{(\tau')}-h^{(\tau)}\mid A\setminus B].
\end{aligned}
$$

Differentiate and divide by $\Pr(B)$. This gives the second identity in (4), and substitution gives the last line of (3). Notice that the second term uses the two rules' own kernels. It is the survivor re-pricing term.

By (S9),

$$
\mathcal S_P(\kappa,\tau,T)=\Delta_m|s_A|,
\qquad
\mathcal S_P(\kappa,\tau',T)=\Delta_m|s_{A\setminus B}|.
$$

Use (3) and $1-\varphi>0$ to obtain (5). To test $C_\tau\le1$, square its two nonnegative sides. Put $u=s_A-\varphi s_B$ and $w=(1-\varphi)s_A$. Then

$$
u^2-w^2
=\varphi(s_A-s_B)((2-\varphi)s_A-\varphi s_B).
$$

Since $\varphi>0$, this is nonpositive exactly when $s_B$ lies between the two roots $s_A$ and $((2-\varphi)/\varphi)s_A$. This proves (6). Under (C$\tau$-4), Lemma g3 gives the exact derivative formula at both thresholds. Condition D compares the corresponding absolute revelation values, so it is equivalent to $C_\tau\le1$.

Multiplying (5) by (2) gives (7). Squaring the two sides of (7) yields

$$
(s_A-\varphi s_B)^2-s_A^2
=-\varphi s_B(2s_A-\varphi s_B).
$$

This proves (8). Proposition `prop:factorisation` at both thresholds turns the left side of (7) into the aggregate sensitivity ratio, as claimed.

For the readings, the two roots in (6) are nonzero and have the sign of $s_A$. A value with the opposite sign, or zero, lies strictly outside their interval. Under a common sign, divide the two endpoints and $s_B$ by $s_A$. If $s_A<0$, their order reverses. In either case the image interval is $1\le\rho\le(2-\varphi)/\varphi$. If $s_{A\setminus B}s_A\ge0$, then

$$
\frac{s_{A\setminus B}}{s_A}
=\frac{1-\varphi\rho}{1-\varphi}\ge0,
$$

so $C_\tau\le1$ is equivalent to $\rho\ge1$. The proviso is $\varphi\rho\le1$. Dividing the interval in (8) by $s_A$ gives $0\le\rho\le2/\varphi$. Finally, both upper limits fall in $\varphi$ and diverge at zero. If $\varphi\le2/(1+M)$, then $(2-\varphi)/\varphi\ge M$ and $2/\varphi\ge M$. This proves all five readings.

##### Part 2

Let $\epsilon=\kappa/2$. Lemma g3 gives, in kernel units,

$$
 s_A=-\frac12\sum_{k=0}^H(1-\epsilon)^k\epsilon^{H-k}c^A_k,
 \qquad
 s_{A\setminus B}=-\frac12\sum_{k=0}^H(1-\epsilon)^k\epsilon^{H-k}c^R_k. \tag{12}
$$

Since $x=\epsilon/(1-\epsilon)=\kappa/(2-\kappa)$,

$$
\sum_{k=0}^H(1-\epsilon)^k\epsilon^{H-k}v_k
=(1-\epsilon)^H P_v(x). \tag{13}
$$

Under (R1), the coefficient list of each pooled-cell polynomial has one sign change. Descartes' rule of signs gives exactly one positive root. The strict endpoint signs give $P_{c^A}(0)>0$ and $P_{c^R}(0)>0$, while both polynomials tend to $-\infty$ as $x\to\infty$. Each is therefore nonpositive at and above its positive root. Under (R2), $P_d(0)<0$, its leading coefficient is positive, and Descartes' rule again gives one positive root. Thus $P_d$ is nonnegative at and above that root.

Condition (R3), (13), and the positive factor $(1-\epsilon)^H$ give

$$
\mathcal W_A\le0,\qquad
\mathcal W_R\le0,\qquad
\mathcal W_R-\mathcal W_A\ge0.
$$

Hence $\mathcal W_A\le\mathcal W_R\le0$. Equation (12) gives

$$
0\le s_{A\setminus B}\le s_A.
$$

Condition (C$\tau$-3) rules out $s_A=0$, so $s_A>0$. Solve the cut identity for $s_B$:

$$
s_B=\frac{s_A-(1-\varphi)s_{A\setminus B}}{\varphi}.
$$

The lower band margin is

$$
s_B-s_A=\frac{1-\varphi}{\varphi}
(s_A-s_{A\setminus B})\ge0.
$$

The stronger upper margin is

$$
\frac{s_A}{\varphi}-s_B
=\frac{1-\varphi}{\varphi}s_{A\setminus B}\ge0.
$$

Since $0<\varphi<1$ and $s_A>0$, $s_A/\varphi<((2-\varphi)/\varphi)s_A$. This proves (11), and Part 1 gives $C_\tau\le1$.

#### What the worker says a script computes at a node

A calibration check needs no finite difference in $\kappa$.

1. For each $(\tau,T)$, compute the pooled measure type weights and the separate market weights used for beliefs. The existing route is `_alive_weights`. Measure weights set cell masses. Market weights include the off-path floor and set the posteriors.
2. For each revealed-round set $S$, partition the pooled type law by its restricted mark path. Compute each cell posterior $(\pi,\widehat v)$ as in Lemma g1, price it with `inner_price`, and integrate $h=\pi p$ using the measure weights. This gives the kappa-free $\mathcal G_{\tau,T}(S)$.
3. Form $c_k(\tau,T)$ from the finite sums in Lemma g3. For a pair, form $d_k=c_k(\tau',T)-c_k(\tau,T)$.
4. Classify a coefficient as zero when its absolute value is at most $10^{-12}$. Reject the certificate if any nonzero sign list lacks the orientation in (R1) or (R2). At the calibration, the smallest absolute $c_k$ used in a sign decision is $1.07\times10^{-7}$ and the smallest absolute $d_k$ is $1.34\times10^{-6}$.
5. Bisect each unique positive polynomial root to absolute tolerance $10^{-13}$ in $x$. Convert it by $\kappa=2x/(1+x)$. Certify an interval beginning at $\underline\kappa$ only if $\underline\kappa-\kappa_*\ge10^{-8}$.
6. As a check, evaluate (12) at each reported node and require both band margins to be at least $-10^{-12}$. For a null cut, require reclassified mass at most $10^{-12}$, paired coefficient differences at most $10^{-12}$, and $|C_\tau-1|\le10^{-12}$.

`single_crossing_certificate.py` performs steps 4 to 6 from the frozen c-coefficient record. Its record is `single_crossing_certificate.json`. All six checks pass. The largest residual against the source record's revelation values and $C_\tau$ is $3.89\times10^{-15}$. The source record already performs steps 1 to 3 and matches the pooled pass within $4.99\times10^{-18}$.

The computation is finite. It uses the pooled type law, the Lemma g1 cell posteriors, the Lemma g3 coefficients, and the two rules' own kernels. The tolerances separate the recorded float values, but they are not certified error bounds for those inputs. Because the coefficients come from numerical pricing rather than interval arithmetic, the calibration conclusion remains a numerical check. The implication from (R1) to (R3) is the proved part.

#### The attacker's verdict and nits (verbatim)

Verdict: PASS. Reasons: Part 1 is a sound transfer: the clock is used only in the nesting step of cor:caught, first passage at a lower threshold replaces it under (S4) and (S5), the added clean start b_0 < tau' is named, and parts (ii) to (vi) never touch the dial. I found no missing hypothesis, no use of the order size one pooled law and no support assumption on the pooled posterior; 400000 random draws produced no counterexample to (6), (8) or the five readings. Part 2's implication is correct: the reversed polynomial is oriented as the memo says, one sign change gives exactly one positive root with the right sign either side, the three root cutoff gives W_A <= W_R <= 0 and so 0 <= s_{A-B} <= s_A, and the two band margins follow from the part 1 identity; 7585 random coefficient triples satisfying (R1) to (R3) gave no violation. Every reported number reproduces from the record's c_k with my own code: W_rev to 1.04e-17, C_tau to 3.89e-15, the four cutoffs to every printed digit, the 0.000987827 gap, and the quoted coefficient minima. The cutoff for the q0.5 to q0.3 pair is in fact the exact upper endpoint of the Condition D failure region, and the quoted 0.1485 is the coarse mesh endpoint of the dial failure. The T = 10 pairs are genuinely null: mass exactly zero, bitwise identical coefficient vectors, and a common sensitivity whose only positive root sits at kappa 0.019, so C_tau = 1 on the whole grid and the memo's refusal to read them as evidence is right. Eight nits, none of them a hole.

Nits

Nits: (1) The memo says the source record "matches the pooled pass within 4.99e-18". The record's
wiring check runs at one node, T = 5 and quantile 0.9, at three kappa values. The other nine
nodes inherit the same code path but are not checked against `pooled_premium`; the sentence
should say so. (2) Step 2 of the calibration section says the cell posteriors are computed "as in
Lemma g1". In the code the cell mass uses the measure weights and the cell belief uses the market
weights, which carry the off path floor `OFF_PATH_EPS = 1e-14` in `_alive_weights`. So the
record's `G(S)` is not literally `E_rho[h(rho(. | marks))]` of Lemma g3. Nothing in part 2 breaks,
because only g3(a) and g3(b) are used and they need only that `G` is kappa free, but the two
weight systems should be named where the identification is made, as step 1 does and step 2 does
not. (3) The script's check name `failure_region_is_below_certificate_cutoff` and the memo's
phrase "the reported failure endpoint" attach to the dial's coarse bracket, not to the Condition
D failure; the sharper statement above is available from the same coefficients. (4) (R1) says the
first and last coefficients are strictly signed after zeros are deleted. If a trailing
coefficient were classified as zero, `P(0) = 0` and the argument needs the factor `x^j` peeled
off before Descartes is applied. The conclusion survives either reading, but the clause should
pick one. (5) (R3) is stated with a weak inequality. At `x(kappa) = r_A` exactly, `s_A = 0` and
(C-tau-3) fails, so the conclusion is not available at that single point; the check should be
strict, which the script's 1e-8 gap already is. (6) The step from a cutoff in `x` to an interval
in kappa uses that `kappa/(2-kappa)` rises in kappa. True and trivial, but neither the memo nor
the script says it. (7) (C-tau-1) leans on (S5) at the tighter threshold as well as at the
looser one; say it, as the memo says the clean start clause. (8) The certificate's stronger upper
bound `s_B <= s_A/phi` is close to binding on the grid: the ratio `s_B/s_A` runs from 9.3 to 40.5
while `1/phi` is about 40 to 43. The memo could say that, and could also say that with
`(1-phi)/phi` near 40 the caught leg is dominated by the survivor re-pricing remainder, so the
"who gets caught" reading of the threshold dial is a statement about the sum and not about the
newly caught histories alone. The memo does flag that the caught leg carries re-pricing, and
reports no split, so this is a reading nit and not a claim I can falsify.

#### Files I wrote

- `.scratch/v5-paper/hunt/2-one-cut-identity/attack.md`, this file.
- `.scratch/v5-paper/hunt/2-one-cut-identity/attack_recheck.py` and its record
  `attack_recheck.json`: the independent rebuild of the record's revelation values, the sign
  lists, the roots, the root sensitivity, the T = 10 check, the below grid scan, the brute force
  test of the part 1 algebra, and the band margins at every grid node.
- `.scratch/v5-paper/hunt/2-one-cut-identity/attack_implication_test.py`: the randomised test of
  the part 2 implication on synthetic coefficient vectors. It prints its result and writes
  nothing.

I changed no other file. I ran the memo's `single_crossing_certificate.py` through a temporary
output path; it returns PASS and its output is byte identical to the committed record.

#### Record excerpt for candidate 4.2 (from `numerical_v4/checks/t2_threshold_revelation_check.json`)

The kappa-free coefficients c_k of Lemma g3 at the ten calibration nodes (frozen benchmark
cutoffs, kappa grid 0.15 to 0.85 in steps of 0.01, mark 2, H = 10). Omega is the flagged weight.
The T = 10 rows are identical across thresholds (the corner T = H; nothing is reclassified).

| T | tau quantile | Omega | c_0 ... c_10 |
|---|---|---|---|
| 5 | 0.1 | 0.104197 | -0.035923, -0.203162, -0.476964, -0.594695, -0.41507, -0.153634, -0.0235252, 1.28479e-05, 4.81798e-06, 1.07066e-06, 1.07066e-07 |
| 5 | 0.3 | 0.0810423 | -0.102431, -0.603309, -1.48007, -1.93579, -1.4235, -0.557887, -0.0908597, 0.000173862, 6.51982e-05, 1.44885e-05, 1.44885e-06 |
| 5 | 0.5 | 0.0578874 | -0.150544, -0.939687, -2.48683, -3.60764, -3.08663, -1.54803, -0.416251, -0.0441275, 0.000971156, 0.00021014, 2.04468e-05 |
| 5 | 0.7 | 0.0347324 | -0.186268, -1.2155, -3.4059, -5.33123, -5.07114, -2.97829, -1.04143, -0.192923, -0.0126462, 0.000616569, 5.61165e-05 |
| 5 | 0.9 | 0.0115775 | -0.207636, -1.41475, -4.19542, -7.08474, -7.47705, -5.08316, -2.20189, -0.571602, -0.0746293, -0.00225371, 0.000112413 |
| 10 | 0.1 | 0.000681272 | -0.210793, -1.46351, -4.4564, -7.81635, -8.71835, -6.43449, -3.15738, -0.997838, -0.183893, -0.0144589, 0.000156943 |
| 10 | 0.3 | 0.000681272 | -0.210793, -1.46351, -4.4564, -7.81635, -8.71835, -6.43449, -3.15738, -0.997838, -0.183893, -0.0144589, 0.000156943 |
| 10 | 0.5 | 0.000681272 | -0.210793, -1.46351, -4.4564, -7.81635, -8.71835, -6.43449, -3.15738, -0.997838, -0.183893, -0.0144589, 0.000156943 |
| 10 | 0.7 | 0.000681272 | -0.210793, -1.46351, -4.4564, -7.81635, -8.71835, -6.43449, -3.15738, -0.997838, -0.183893, -0.0144589, 0.000156943 |
| 10 | 0.9 | 0.000681272 | -0.210793, -1.46351, -4.4564, -7.81635, -8.71835, -6.43449, -3.15738, -0.997838, -0.183893, -0.0144589, 0.000156943 |

The eight adjacent pairs (tau' = the tighter, lower threshold; W_tau = (1 - Omega(tau'))/(1 - Omega(tau))):

| T | pair (q to q') | W_tau | reclassified mass | Condition D on the grid | C_tau min | C_tau max |
|---|---|---|---|---|---|---|
| 5 | 0.9 to 0.7 | 0.976574 | 0.0232 | True | 0.1395 | 0.6333 |
| 5 | 0.7 to 0.5 | 0.976012 | 0.0232 | True | 0.02945 | 0.5874 |
| 5 | 0.5 to 0.3 | 0.975422 | 0.0232 | True | 0.2191 | 0.791 |
| 5 | 0.3 to 0.1 | 0.974803 | 0.0232 | True | 0.2794 | 0.4564 |
| 10 | 0.9 to 0.7 | 1 | 0 | True | 1 | 1 |
| 10 | 0.7 to 0.5 | 1 | 0 | True | 1 | 1 |
| 10 | 0.5 to 0.3 | 1 | 0 | True | 1 | 1 |
| 10 | 0.3 to 0.1 | 1 | 0 | True | 1 | 1 |

## 10. What a script can compute at a node

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

## 11. For the session that receives the answer

The answer is input, not authority: it lands at `.scratch/v5-paper/external/gpt-sol-pack-3.md`,
enters as CONJECTURE where it goes beyond the attacked memos, and reaches the paper only through
the writing thread's orchestrator at a checkpoint (labels are set there), with any new claim
passing the attack gate first.
