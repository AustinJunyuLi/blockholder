# Handoff 2: four theory upgrades for "Who Gets Caught"

Prepared 2026-09-02 by the orchestrating session of the paper *Who Gets Caught: Blockholder
Disclosure Rules and Market Inference* (worktree `blockholder_v5`, branch `v5`). The reader of
this document has no access to the worktree, so everything needed is inline. Each section names
the file it was taken from, for the session that receives the answer. This is a fresh
consultation: it does not assume any earlier exchange.

## 1. Objective

Four candidate results, stated in section 4 as conjectures. For each: a proof, a counterexample,
or a sharpened true statement, with every hypothesis in the statement. The four are ranked; the
first three are theory, the fourth is a numerical record whose method must be justified.

The paper is a fixed-policy paper. Every headline result compares two disclosure rules with the
blockholder's plan held fixed (standing condition (S11) in section 6). The calibration's policy
is a benchmark policy, the solver's baseline cutoffs; it is not an equilibrium of the paper's
game (section 4.3 below gives the numbers), and the paper says so by calling it the benchmark
policy and never an equilibrium. No candidate below needs an equilibrium, and none should be
proved by way of one.

## 2. Constraints

- The primitives are fixed as sections 5 and 7 state them: the menu, the stake paths, the
  building count n(s), the ternary noise law, the pricing rule, the bidder, the order size of two
  noise lumps, and the parameter values. Candidate 4.1 varies the order size on purpose; nothing
  else varies a primitive.
- Every hypothesis is stated in the theorem, numbered in the standing-condition scheme of
  section 6 where it is one of them, and named where it is new. Two assumptions the paper dropped
  stay out of every proof: the ternary pooled law of order size one (except as the b = 1 case of
  candidate 4.1), and any support assumption on the pooled posterior.
- A hypothesis quantified over a continuum (of signals, of policies, of kappa) is proved from the
  primitives, or is reduced to finitely many computations at a calibration node with the
  reduction proved and a tolerance stated. Section 9 says what a script can compute at a node.
- The proof is complete at the level of a journal appendix: every step follows from something in
  this document or from a named textbook result with its hypotheses checked. Finite Blackwell
  comparisons are established by an explicit Markov kernel, and refuted by an explicit decision
  problem or finite linear program.
- Anything not proved is labelled as such. The paper carries three labels, PROVED, NUMERICAL
  (verified on a stated grid) and ESTIMATED; a working conjecture is labelled CONJECTURE. Nothing
  in the answer awards a label; it says which label a result would support.
- The answer is in the notation of sections 5 to 8. LaTeX is welcome.

## 3. What to return

Two deliverables, in this order.

**Deliverable A: the four candidates.** For each of 4.1 to 4.4, in order:
1. The statement, with the full hypothesis list.
2. The proof, the counterexample, or the honest "open" with what blocks it.
3. "What a script computes at a node", if anything: each item a formula in the objects of
   section 9 with the tolerance the proof needs.
4. The cost of carrying it into the paper: which of the existing results (section 4.1 table and
   section 8 proofs) it touches, and what it would let the paper say that it cannot say now.

**Deliverable B: holistic comments.** As a top-journal referee and as a co-author: which of the
four is worth the paper's space and which is not; whether the two-dial framing (section 4.1)
has a better statement given what the four candidates would add; what a referee would say
first about a fixed-policy paper calibrated at a benchmark policy that is not an equilibrium;
anything in sections 5 to 8 that looks wrong.

## 4. The paper, the labels, and the candidates

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

### 4.2 The four candidates

The text below is the orchestrator's statement of each candidate, with the conjecture, why the
paper wants it, and the expected cost. Each is a conjecture to prove, disprove or sharpen.

(File paths in the candidate texts name where the objects live in the worktree; the proofs
they refer to are reproduced verbatim in section 8, the standing conditions in section 6, the
calibration in section 7. The grid records are summarised in section 4.1 and in the candidate
texts; their numbers are quoted where needed.)

Each candidate below is stated as the objective a worker receives. Per ADR 0007 the brief states
objective and constraints and leaves the method to the worker. The statements are conjectures by
the batch-2 orchestrator; the worker's job is to prove, disprove, or sharpen them.

#### Candidate 4.1 Order size two is the erasure regime

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

#### Candidate 4.2 One cut identity for both dials

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

#### Candidate 4.3 Tightening is a Blackwell improvement

Conjecture. At fixed policies, for τ' < τ at a common window, or T' < T at a common threshold,
the market's control-node experiment about the blockholder's type under the tighter rule is
Blackwell more informative than under the looser one. Sketch that the worker may ignore:
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

#### Candidate 4.4 A stated maximal regret for the benchmark policy (numerical, not theory)

Objective. A record giving, at each of the ten calibration nodes (T in {5, 10}, five thresholds
in the ladder of `numerical_v4/checks/t5_who_gets_caught.json` provenance), a rigorous upper bound
on the benchmark policy's maximal interim regret, ess sup over signals of the best plan's payoff
minus the assigned plan's payoff. The bound must come from a breakpoint-aware method (the free
breakpoints of n(s) and the legal clock are computable in closed form; see
`numerical_v4/menu.py` `breakpoints`), not from a uniform signal grid; the 241-point grid missed
the node-1 island. Reference numbers at node 1: regret 7.0e-5 on the island (1.8608, 1.8625),
zero elsewhere to solver tolerance; see `.scratch/v5-paper/runs/05-condition-judge/result.txt`
and `/tmp/judge05_gap.json` (plateau table, crossings).

Why it matters. It answers "why should the reader care about comparative statics at this
policy" with one number per node, at the cost of about ten pooled passes. It changes no label.

#### Not asked for

Existence or any equilibrium result under the paper's notion (the integer building count makes
the best-response correspondence non-monotone; no theorem edit fixes it short of a menu change,
which is a calibration change out of scope). A general-equilibrium comparative static (dropped
in ADR 0003). A Kyle-style "tighter rules lower informed profits" result (the cross-moment it
needs is not Blackwell-monotone in general).

### 4.3 The benchmark policy is not an equilibrium

At the first calibration node (T = 5, tau = 0.09239820, kappa = 0.5) the solver's candidate
cutoffs k-hat = (0.9425042193, 1.8472640726) assign Voice to signals in (1.8608284620,
1.8624646978) that strictly prefer Hold, with maximal gain 6.98e-5 against a payoff tolerance of
1e-9; the island has width 1.636e-3 and prior mass 4.4e-4. The Hold-Voice payoff gap is a falling
sawtooth in the signal: it declines on each plateau of n(s) and jumps up at each plateau edge,
because the Voice payoff steps down at every decrement of n(s). The 241-point deviation grid of
the solver steps over the island. The paper's benchmark policy is the baseline cutoffs
k = (0.9425017267, 1.8484512098), solved at the median threshold and T = 5, and frozen at every
node; the paper states every result at that fixed policy. Candidate 4.4 asks for a certified
bound on the benchmark's regret at every node.

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

The answer is input, not authority: it lands at `.scratch/v5-paper/external/gpt-sol-pack-2.md`,
enters as CONJECTURE, and reaches the paper only through the attack gate (an independent Opus
attacker per claimed proof, a node script for anything checkable, the orchestrator's label at a
checkpoint, and Austin's decision on what enters batch 3).
