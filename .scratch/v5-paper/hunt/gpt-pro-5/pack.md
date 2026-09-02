# Handoff: the framing question for "Who Gets Caught"

Prepared 2026-09-02 by the orchestrating session of the paper *Who Gets Caught: Blockholder
Disclosure Rules and Market Inference*. The reader has no access to the worktree; everything
needed is inline. Sections 2 to 4 are verbatim from the delivered paper and its records. Section 5
is the author's pitch for a change of question. Section 6 lists the alternatives considered.

## 1. The problem

The delivered paper (section 2 below) is exact and dull. Its results are fixed-policy accounting
on market inference: a factorisation, a garbling order, a cut identity, and a composition
condition verified on a grid. A theory-upgrade round added four gated results (section 3): a
Blackwell order in the rule, an order-size trichotomy, a threshold-margin cut identity with a
one-crossing certificate, and a benchmark regret bound. Their best headline is a contrast:
information is monotone in the rule, noise robustness is not. A careful reader will find that
contrast correct and unexciting, because the reversal sits where the looser pool's sensitivity
passes through zero, three to four orders of magnitude below the grid values (section 4).

An earlier version of this model, at order size one, had a result people noticed: the takeover
premium was hump-shaped in trading noise. Some noise gave the blockholder cover to accumulate
cheaply, so the premium rose with liquidity; past a point noise destroyed enough information that
it fell. That is the Kyle and Maug channel: liquidity enables activism. The current version
doubled the order size to two noise lumps to obtain a clean garbling lemma (only one order-flow
value is ambiguous between a building purchase and an idle date). That removed the cover. More
noise is now pure erasure, the pooled premium is a flat plateau that falls at high liquidity, and
the sign change the record shows is the ghost of the hump with its rising side gone. Fixed
policies then removed the blockholder's response. What remains cannot produce a striking result.

The question for you: given the machinery in sections 2 to 4, what is the most interesting
question this model can answer with a proof or a certified computation, and what is its headline?
The author's own proposal is section 5. Attack it, improve it, or replace it.


## 2. The delivered paper (verbatim LaTeX excerpts)

### 2.1 Abstract and introduction
```latex
share times the pooled cell's own sensitivity. The factorisation and the liquidity invariance of the
flagged endpoint are PROVED. Tightening the threshold lowers sensitivity through a PROVED weight
effect. Its composition effect is NUMERICAL on the order-size-two, $H=10$, $T=5$ grid at frozen
benchmark policy, for four adjacent threshold pairs and $\kappa$ from $0.15$ to $0.85$ in steps of
$0.01$. Shortening the clock lowers sensitivity exactly when the clock's weight and composition
ratios have product at most one, a PROVED equivalence. A PROVED corollary characterises the
composition ratio by the noise sensitivity of the premium mass the shorter clock removes from the
pool, including the re-pricing of survivors. Under a common nonzero sign, $C_T\leq1$ exactly when
the caught leg is at least as noise-sensitive as the pool and no more than
$\bigl((2-\varphi)/\varphi\bigr)$ times as sensitive, where $\varphi$ is the share caught. The
empirical measurement is descriptive, with the post-minus-pre differences labelled ESTIMATED. Among
initial Schedule 13D campaigns with readable stakes from 2021 to 2025, the median stake at filing is
$13.1$ percent of class before the February 2024 clock change and $12.8$ percent after. The share
filed within five business days rises from $32.7$ to $75.9$ percent.
\end{abstract}

\newpage

%==============================================================================
\section{Introduction}
\label{sec:intro}
%==============================================================================

A blockholder who learns that a company is worth more than the market price can sell, wait, or try
to change the company. If she builds a large enough position while she waits, the law makes her
disclose it. In the United States, Section 13(d) of the Williams Act requires beneficial owners of
more than 5 percent of a registered equity class who do not qualify for or elect Schedule 13G to
file a Schedule 13D. Until February 2024 the initial deadline was ten calendar days; it is now five
business days \citep{SEC2023}. That rule gives two policy variables: the threshold determines which
positions become public, and the clock determines how much trading can take place before the filing.
The central thesis of this paper is that disclosure regulation changes what the market learns from
silence. A disclosure rule releases information on filed histories and selects which informed
histories leave the unfiled pool. The resulting pool changes the market's inference when no filing
lands.

The disclosure rule divides all histories into a flagged cell and a pooled cell. After a filing,
Item 4 disclosures make public the blockholder's accumulated stake, intended plans, and engagement
intent, represented in the model by public disclosure of the stake, residual target order, and
engagement indicator. Before a filing lands, the market observes order flow alone and must infer
whether an informed holder is trading in secret. The formal outcome is the liquidity sensitivity of
the engagement-related component of the expected takeover premium, $\Dact = \Delta_m \Eop[\pi p]$,
which governs a potential bidder's takeover decision and omits the baseline entry term $m_0
\Eop[p]$. Liquidity changes inference in the pooled cell but not what the market learns from a
completed filing. At fixed trading policies, the flagged posterior, the flagged price, the bidder's
entry probability, and the flagged cell's average premium do not depend on the noise-trading
intensity $\kappa$.

The first result is the factorisation $\mathcal S = (1 - \Omega)\mathcal S_P$, where $\Omega$ is the
flagged probability and $\mathcal S_P$ is the pooled cell's own noise sensitivity. The factorisation
and the $\kappa$-invariance of the flagged cell are PROVED. All theoretical results hold trading
policies fixed at the benchmark profile. This isolates changes in market information from the
blockholder's endogenous policy response. The two dials then operate through distinct mechanisms.
Tightening the threshold weakly raises $\Omega$, so its weight effect attenuates noise sensitivity
by proof. Its composition effect is NUMERICAL on a five-node ladder of the stake-at-filing
distribution, $\tau \in [0.0924, 0.0970]$, under order size two, $H=10$, $T=5$, at frozen benchmark
policy, with $\kappa$ from $0.15$ to $0.85$ in steps of $0.01$. On that grid the composition ratio
$C_\tau$ is at most one at all four adjacent threshold pairs, and $W_\tau C_\tau$ is at most
$0.772$. For the clock, the model measures the window margin $T$ in discrete trading rounds. A
PROVED theorem establishes that a shorter window lowers noise sensitivity if and only if $W_T C_T
\le 1$. A PROVED corollary then characterises who gets caught. Write $\varphi$ for the share of the
long-clock pool removed by the shorter clock and $s_B$ for the sensitivity of the premium mass
removed, including the re-pricing of survivors. Under a common sign ($s_A s_B > 0$), the composition
ratio satisfies $C_T \le 1$ if and only if $s_B$ lies weakly between $s_A$ and
$((2-\varphi)/\varphi)s_A$, and the shorter clock lowers sensitivity overall, $W_T C_T \le 1$, if
and only if $s_B$ lies weakly between $0$ and $(2/\varphi)s_A$.

At order size two, a building purchase has the size of two noise lumps. Flow then has five values.
Only $+\bar z$ is ambiguous, arising either from a building purchase with negative noise or from no
building purchase with positive noise. The pooled experiment at higher $\kappa$ is a garbling of the
experiment at lower $\kappa$ in the sense of \citet{Blackwell1953}. The result is PROVED. It gives a
Markov kernel and an exact polynomial form for the pooled premium. The convexity-signed ordering
does not require normality. Section~\ref{sec:model} gives the rationale for the order-size choice.

The registered empirical analysis gives institutional context for the stake and clock parameters. It
does not measure market inference directly. The population is initial Schedule 13D campaigns from
2021 to 2025, taking the campaign (one subject firm and trigger date) as the unit, without screening
by Item 4 text, and reading the maximum percentage across reporting persons. Stakes are readable for
$91.6$ percent of campaigns. In that sample, the post-minus-pre differences in the stake at filing
$B^F$ are labelled ESTIMATED. The share of campaigns filed within five business days rises from
$32.7$ percent before the February 2024 clock change to $75.9$ percent after, and the median
trigger-to-filing delay falls from $7.0$ to $5.0$ business days. The comparison has no control group
and identifies no causal effect.

Standard discrete-order trading models with exogenous disclosure typically fix the composition of
the unfiled pool, so the question of its sign does not arise. This paper analyses the clock dial
result and the who-gets-caught characterisation. The exit-and-liquidity literature studies whether
liquidity finances monitoring, and the disclosure literature studies the level of the threshold;
neither separates the statutory rule into two distinct margins acting on a partition of histories.
Section~\ref{sec:lit} sets out both literatures and the institutional facts. Section~\ref{sec:model}
states the model. Section~\ref{sec:results} states the results, each with its label.
Section~\ref{sec:calibration} reads them against the calibration. Section~\ref{sec:empirics}
presents the empirics, and Section~\ref{sec:conclusion} closes. The proofs and the hypothesis lists
are in the appendix.

%==============================================================================
```

### 2.2 The model
```latex
\section{The model}
\label{sec:model}
%==============================================================================

\subsection{The object and the partition}
\label{sec:object}

The disclosure rule divides the market's information into two cases. A stake threshold $\tau$
and a window margin $T$ determine whether the filing has arrived by the control decision. In
the \emph{flagged} cell, the market sees the stake and the intention to engage. In the
\emph{pooled} cell, it sees only order flow and must infer whether an informed blockholder is
trading. The cells are exhaustive. The outcome of interest is the expected engagement-related
premium $\Dact(\kappa,\tau,T)$, its two cell averages $M_F$ and $M_P$, and their liquidity
sensitivities. A lower threshold is a tighter threshold margin; a shorter window is a tighter
window margin.

The model uses the discrete order-flow structure of \citet{Kyle1985} and
\citet{EdmansGoldsteinJiang2015}, competitive prices as in \citet{GlostenMilgrom1985}, and the
takeover premium as the dispersed shareholder's control-outcome measure in the spirit of
\citet{GrossmanHart1980}. The model adds the legal partition to these elements.

\subsection{Timing}
\label{sec:timing}

Trading dates are $d=0,\ldots,H$. Nature draws the standalone value and the blockholder's
signal. A cutoff vector then maps the signal into one of three plans. Exit sells the initial
stake on date zero and holds nothing thereafter. Hold keeps the initial stake. Voice builds
toward a signal-dependent target and carries the engagement indicator $a=1$. Only Voice can
cross the disclosure threshold.

On each date, a binary order mark records whether the Voice path schedules a building purchase. The
strategic order attached to that mark and the independent noise order form observed flow. Market
makers set the date's pooled price from the flow history and the fact that no filing has yet landed.
The blockholder pays the pooled price for the scheduled change in the stake. The path does not
respond to realised flow or prices.

For a Voice path, the clock starts at the first date $c$ on which the stake reaches $\tau$, and the
filing date is $f=c+T$ in trading rounds when $f\leq H$. The within-date order is explicit. The
blockholder pays the corresponding pooled price for every scheduled purchase through date $f$,
including the purchase that determines $B^F=B(s,f)$. The filing then lands. The blockholder pays the
flagged price for the remaining purchase $Q^F=b^*(s)-B^F$. The bidder acts after this update. If no
filing lands by $H$, the bidder acts on the pooled control-node history.

\subsection{Primitives}
\label{sec:primitives}

The firm's standalone value is $v\sim N(\mu_v,\sigma_v^2)$. The blockholder observes
$s=v+\varepsilon$, where $\varepsilon\sim N(0,\sigma_\varepsilon^2)$ is independent of $v$.
Thus $s\sim N(\mu_v,\sigma_s^2)$, with
$\sigma_s^2=\sigma_v^2+\sigma_\varepsilon^2$, and
\[
\Eop[v\mid s]=\mu_v+\beta(s-\mu_v),
\qquad
\beta=\frac{\sigma_v^2}{\sigma_v^2+\sigma_\varepsilon^2}.
\]
The analytic model uses the full signal line. The computations retain
$s\in[\mu_v-6\sigma_s,\mu_v+6\sigma_s]$ and renormalise the truncated Gaussian law on that
interval. A potential bidder has an independent shock $\xi\sim N(0,\sigma_\xi^2)$, mean synergy
$\bar S$, and entry cost $K>0$. Engagement adds $\Delta_V\geq0$ to standalone value and changes
the takeover premium from $m_0$ to $m_1$, where $\Delta_m=m_1-m_0>0$. The restriction
$m_0\geq0$ gives a unique continuous pricing root (Lemma~\ref{app:lem:pricing-root} in the appendix).

The Voice target follows the strictly increasing algebraic sigmoid used in the computations,
\[
b^*(s)=b_0+(\bar b-b_0)G\!\left(\frac{s-\mu_v}{\sigma_s}\right),
\qquad
G(x)=\frac{1+x/\sqrt{1+x^2}}{2}.
\]
Its accumulation length is
\[
n(s)=\operatorname{clip}\!\left(
\left\lceil n_{\rm scale}(H+1)
\left[1-G\!\left(\frac{s-\mu_v}{\sigma_s}\right)\right]\right\rceil,
1,H+1\right),
\]
which is weakly decreasing in $s$. The Voice stake path is
\[
B_V(s,d)=b_0+\bigl(b^*(s)-b_0\bigr)
\min\!\left\{1,\frac{d+1}{n(s)}\right\}.
\]
Exit has $B_E(s,-1)=b_0$ and $B_E(s,d)=0$ from date zero onward. Hold keeps $B_H=b_0$.
The threshold satisfies $b_0<\tau$. The first crossing is
$c_j(s;\tau)=\inf\{d:B_j(s,d)\geq\tau\}$, with value $+\infty$ if there is none, and
$D=\ind\{a=1,c+T\leq H\}$.

The order mark and order size are distinct. The mark
\[
g_{jd}(s)=\Gamma\bigl(B_j(s,d)-B_j(s,d-1)\bigr)\in\{0,1\},
\qquad
\Gamma(x)=\ind\{x\geq\bar\gamma\},
\]
is a building-purchase indicator. Its strategic order has size two noise lumps,
$q_{jd}(s)=2\bar z\,g_{jd}(s)$. Independent noise takes the values $-\bar z$, $0$, and
$+\bar z$, with probabilities $\kappa/2$, $1-\kappa$, and $\kappa/2$. Noise orders are
independent across dates and independent of the primitive draws. Observed pooled flow is
$X_d=q_{jd}+z_d$. Higher $\kappa$ is a noisier, more liquid market.

Under Exit, the blockholder sells the initial stake at the pooled date-zero price but leaves no
order mark. This is a model assumption. The public statistic records buy-side stake building, not
all signed inventory changes, and therefore keeps Exit and Hold in the same mark class. Modeling
signed liquidation would add a third strategic-order support and create a different information
experiment from the five-flow experiment studied here.

A pooled history records $(X_0,\ldots,X_d)$ and whether the filing has landed. A filing reports
$F=(B^F,a=1)$, and the flagged tuple adds the residual order, $\Sfl=(B^F,Q^F,a=1)$. Institutionally,
Item 4 of Schedule 13D requires disclosing the purpose of the acquisition and any plans or proposals
regarding future purchases. In the model, the public tuple $\Sfl$ captures this requirement: the filing
reveals the accumulated stake $B^F$, the activist's scheduled remaining purchase $Q^F = b^*(s) - B^F$
toward her target, and the engagement commitment $a=1$. This is a stronger information set than a
filing alone: Item 4 motivates the disclosure of plans, and the model takes the residual order and
the engagement commitment as exactly disclosed, which a filing does not guarantee. At the control
node, public information is the pooled history if $D=0$ and $\Sfl$ if $D=1$.
 The bidder's shock remains private. The engagement posterior is
$\pi(\mathcal I)=\Prb(a=1\mid\mathcal I)$ and equals one after a filing. The bidder enters with
probability
\begin{equation}
\label{eq:entry}
p(\mathcal I)=1-\Phi\!\left(
\frac{P+K+m_0+\pi\Delta_m-\bar S}{\sigma_\xi}
\right).
\end{equation}
With $\mathsf B$ the entry indicator, the terminal shareholder payoff is
\begin{equation}
\label{eq:Y}
Y=(1-\mathsf B)(v+a\Delta_V)+\mathsf B(P+m_0+a\Delta_m),
\end{equation}
and the competitive control-node price solves $P(\mathcal I)=\Eop[Y\mid\mathcal I]$. Earlier
pooled prices are tower expectations of the solved control-node payoff. Positive-probability
histories use Bayes' rule. The pricing map assigns a fixed full-support reference belief to an
empty mark-path history.

For plan $j$, the blockholder evaluates
\[
U_j(s)=\Eop\!\left[b_j^*(s)Y-C_j^{\rm trade}-a_jC_j(s)\mid s,j\right].
\]
The trading cost sums each position change times the price specified by the within-date timing.
The engagement cost is positive for Voice and zero for Exit and Hold. A weakly ordered cutoff
vector maps the signal into Exit, Hold, or Voice. The calibration uses the resulting cutoff
vector as its baseline policy and freezes it across the comparative statics. The blockholder
executes the selected path without responding to realised prices or flow. The finite menu,
bounded premium kernel, legal-clock rules, and single probability space are listed as (S1) to
(S11) in the appendix and apply to the results below.

\subsection{The order-size choice}
\label{sec:ordersize}

A stake-building order should be large enough to move outside an ordinary noise order, but not so
large that its sign reveals the blockholder in every round. Two noise lumps are a simple middle
scale. A building purchase is twice the size of one liquidity order, yet a noise sale can still
offset half of it and produce the same net flow as an idle blockholder facing a noise buy. The model
preserves one camouflage event while most flows reveal whether stake building occurred.

Flow takes the five values
$\{-\bar z,0,\bar z,2\bar z,3\bar z\}$. A building date produces
$\{\bar z,2\bar z,3\bar z\}$ and an idle date produces
$\{-\bar z,0,\bar z\}$. The supports meet only at $\bar z$. This single overlap makes higher
liquidity a garbling of lower liquidity and gives the pooled premium a polynomial form in
$\kappa$.

\subsection{Fixed policies and the two dials}
\label{sec:fixed-policies}

Every theoretical comparison holds the plan menu, cutoff vector, and execution paths fixed while
the disclosure rule $(\tau,T)$ moves. Each comparison holds $\kappa$ fixed across the two rules.
The numerics hold the solver's baseline policy fixed throughout. These comparisons isolate the market's
information problem rather than a policy response by the blockholder. The formal outcome is the
engagement-related component of the expected takeover premium,
\[
\Dact \;=\; \Delta_m\,\Eop\bigl[h(\mathcal I_H)\bigr], \qquad
h(\mathcal I) = \pi(\mathcal I)\,p(\mathcal I),
\]
omitting the baseline entry term $m_0\,\Eop[p]$. The cell averages are $M_F=\Delta_m\Eop[h\mid D=1]$
and $M_P=\Delta_m\Eop[h\mid D=0]$ with $D$ the disclosure indicator, the flagged weight is
$\Omega=\Prb(D=1)$, and the sensitivities are $\mathcal S=|\partial_\kappa\Dact|$ and
$\mathcal S_P=|\partial_\kappa M_P|$. The two dials act through the weight legs
\[
W_\tau \;=\; \frac{1-\Omega(\tau',T)}{1-\Omega(\tau,T)}
\quad(\tau' < \tau),
\qquad
W_T \;=\; \frac{1-\Omega(\tau,T')}{1-\Omega(\tau,T)}
\quad(T' < T),
\]
and the composition legs $C_\tau = \mathcal S_P(\tau',T)/\mathcal S_P(\tau,T)$ and
$C_T = \mathcal S_P(\tau,T')/\mathcal S_P(\tau,T)$, both unsigned.

By Lemma~\ref{app:lem:bf-monotone} in the appendix, under fixed policies, because Voice stakes are
weakly increasing in the calendar date and crossing dates are unchanged, shortening the window
margin lands the filing weakly earlier on every path flagged under both windows, and on those
paths the stake at filing $B^F$ weakly falls. The shorter window can also flag paths that the longer one leaves in the pool, so the set of
filers can change as well. The empirical section states this
pathwise monotonicity next to the measured stakes and draws nothing causal from the pairing.

%==============================================================================
```

### 2.3 Results at fixed policies (statements)
```latex
\section{Results at fixed policies}
\label{sec:results}
%==============================================================================

Each statement reports its status as PROVED, NUMERICAL, or ESTIMATED. PROVED marks an analytic
result. NUMERICAL marks a result on the grid named at the point of claim. ESTIMATED marks a
descriptive estimate with its design and uncertainty. The full hypothesis lists (S1) to (S11)
and (C-1) to (C-3) are in the appendix.

\subsection{The partition and the factorisation}
\label{sec:partition}

\noindent\textsc{Label: PROVED.}\par
\begin{lemma}[Disclosure partition; Appendix Section~\ref{app:sec:partition-factorisation}, Lemma~\ref{app:lem:partition}]
\label{lem:partition}
Under the standing conditions of Section~\ref{sec:model}, the disclosure indicator
$D = \ind\{a = 1,\ c(\tau) + T \le H\}$ is a measurable function of the control-node history,
and the flagged cell $\mathcal C_F = \{D = 1\}$ and the pooled cell $\mathcal C_P = \{D = 0\}$
are disjoint, cover the space, and are read off the observed history. No restriction on the
mass of either cell is used: $\Omega$ may be $0$ or $1$, and then the empty-weight cell is
null, possibly empty.
\end{lemma}

\noindent\textsc{Label: PROVED.}\par
\begin{lemma}[Two-cell decomposition; Appendix Section~\ref{app:sec:partition-factorisation}, Lemma~\ref{app:lem:two-cell}]
\label{lem:two-cell}
Under the same conditions, with the partition of Lemma~\ref{lem:partition} and whenever
$0 < \Omega < 1$,
\[
  \Dact \;=\; \Omega\,M_F \;+\; (1 - \Omega)\,M_P .
\]
At $\Omega = 1$ the identity reads $\Dact = M_F$ and at $\Omega = 0$ it reads $\Dact = M_P$;
in each of those cases the average over the null cell is undefined rather than zero, and it is
not determined by the law.
\end{lemma}

\noindent\textsc{Label: PROVED.}\par
\begin{proposition}[Factorisation of the liquidity sensitivity; Appendix Section~\ref{app:sec:partition-factorisation}, Proposition~\ref{app:prop:factorisation}]
\label{prop:factorisation}
Assume the standing conditions, an interior partition $0 < \Omega < 1$ at the policy under
consideration, the invariance of the flagged endpoint in $\kappa$ at fixed policies
(Lemma~\ref{lem:flagged}), and differentiability of $\kappa \mapsto M_P$. Then
\begin{equation}
\label{eq:factorisation}
  \mathcal S(\kappa,\tau,T) \;=\; \bigl(1 - \Omega(\tau,T)\bigr)\,\mathcal S_P(\kappa,\tau,T)
\end{equation}
exactly, and the same factor scales the total variation of $\Dact$ over any grid in $\kappa$,
where no differentiability is used. At order size two the differentiability hypothesis is
automatic: the closed form of Lemma~\ref{lem:garbling} exhibits $M_P$ as a polynomial in
$\kappa$.
\end{proposition}

\noindent\textsc{Label: PROVED.}\par
\begin{lemma}[The flagged cell does not move with liquidity; Appendix Section~\ref{app:sec:partition-factorisation}, Lemma~\ref{app:lem:flagged-kappa-free}]
\label{lem:flagged}
Fix the cutoff policy and the execution policy, and let the disclosure rule be fixed. Under
the standing conditions, with the composed terminal target strictly increasing on the flagged
signal region almost surely, uniqueness of the inner pricing fixed point, $\Omega > 0$, and a
bidder entry rule whose probability given the public information set neither depends on $v$
beyond it nor moves the entry shock, the flagged tuple $\Sfl$ makes the pre-filing pooled
history conditionally independent of the primitive triple $(v,s,\xi)$, and the flagged
posterior, the flagged price, the entry probability and $M_F$ do not depend on $\kappa$. In
addition $\Omega$ does not depend on $\kappa$ at fixed policies.
\end{lemma}

The appendix gives all four proofs. The partition is a measurable split of the history space.
The decomposition integrates a bounded kernel over its two cells. The factorisation then uses
the fact that the flagged endpoint and the flagged weight are constant in $\kappa$. The
invariance proof uses the flagged tuple to recover the signal and its posterior. The pre-filing
pooled price can still move with $\kappa$, and all four statements hold at fixed policies.

\subsection{The pooled experiment ordered by liquidity}
\label{sec:garbling}

\noindent\textsc{Label: PROVED.}\par
\begin{lemma}[Liquidity garbles the pooled experiment, and a closed form; Appendix Section~\ref{app:sec:pf-garbling}, Lemmas~\ref{app:lem:g1}--\ref{app:lem:g3}]
\label{lem:garbling}
Fix a policy with $\Omega(\tau,T)<1$ and $\kappa\in(0,1)$ at order size two. Write $R$ for
the set of rounds whose flow differs from one lump $\bar z$.
\begin{enumerate}[label=(\alph*),leftmargin=2.4em,itemsep=2pt]
\item The value $\bar z$ carries likelihood ratio one across types, so $R$ is independent of
  the blockholder's type, and on $R$ the flow determines the blockholder's order mark. The
  pooled posterior after any pooled history is therefore the pooled type law conditioned on
  the marks the history reveals, and nothing else.
\item For $0 < \kappa < \kappa' < 1$ there is a Markov kernel, not depending on the type, that
  carries the law of every pooled history at $\kappa$ into its law at $\kappa'$: the pooled
  experiment at $\kappa'$ is a garbling of the pooled experiment at $\kappa$, in the sense of
  \citet{Blackwell1953}.
\item The pooled premium is exactly
  $M_P = \Delta_m\sum_S (1-\varepsilon)^{|S|}\varepsilon^{H+1-|S|}\Grev(S)$ with
  $\varepsilon = \kappa/2$ and $\Grev(S)$ a number that does not depend on $\kappa$; it is a
  polynomial in $\kappa$, differentiable on $(0,1)$, with
  $\partial_\kappa M_P = -(\Delta_m/2)\sum_k (1-\varepsilon)^k\varepsilon^{H-k}c_k$ and
  coefficients $c_k$ that are closed forms in the pooled type weights. If the kernel's reduced
  form is concave on the pairs the pooled cell generates, every $c_k \le 0$ and
  $\partial_\kappa M_P \ge 0$; if convex, all inequalities reverse.
\end{enumerate}
\end{lemma}

The appendix constructs the kernel in part~(b) by deleting revealed rounds and redrawing the
rest. The pooled expectation of a convex or concave kernel is monotone in $\kappa$ in the
direction set by its curvature. This argument needs no normality assumption. \citet{BackEtAl2018}
obtain a related ordering from a Gaussian mean-preserving spread of the market maker's posterior
mean, while \citet{Ganuzapenalva2010} uses dispersion orderings of signal structures. The
threshold composition result uses the closed form in part~(c).

\begin{condition}[Revelation dominance at a threshold pair]
\label{cond:D}
Let $b_0 < \tau' < \tau$ at a common window $T$. The pair satisfies revelation dominance at
$\kappa$ if $\bigl|\Wrev_{\tau',T}(\kappa)\bigr| \le \bigl|\Wrev_{\tau,T}(\kappa)\bigr|$, where
$\Wrev$ is the coefficient sum of Lemma~\ref{lem:garbling}(c). The condition states exactly
that the composition ratio is at most one, $C_\tau \le 1$: it is the theorem's conclusion
restated on the closed form, not a restriction on primitives.
\end{condition}

\subsection{The two dials}
\label{sec:dials}

\noindent\textsc{Labels: PROVED and NUMERICAL.} Factorisation, the weight leg, and the closed-form
implication below are PROVED. The composition conclusion $C_\tau\leq1$ and the dial inequality
are NUMERICAL on the order-size-two, $H=10$, $T=5$ grid at frozen benchmark policy, for all four
adjacent threshold pairs and $\kappa\in[0.15,0.85]$ in steps of $0.01$.\par
\begin{theorem}[The threshold dial at fixed policies; Appendix Section~\ref{app:sec:pf-garbling}, Theorem~\ref{app:thm:g-threshold}]
\label{thm:threshold}
Fix the plan and cutoff policies and a window $T$, and take $b_0 < \tau' < \tau$ with
$0 < \Omega(\tau,T)$, $\Omega(\tau',T) < 1$ and $\mathcal S_P(\tau,T) > 0$. Assume the two-cell
decomposition and the $\kappa$-invariance of the flagged average, each with its own
hypotheses. Then:
\begin{enumerate}[label=(\Alph*),leftmargin=2.4em,itemsep=2pt]
\item \emph{Factorisation.} $\mathcal S = (1-\Omega)\,\mathcal S_P$ exactly, at every
  $\kappa \in (0,1)$.
\item \emph{Weight leg.} $\mathcal C_F(\tau,T) \subseteq \mathcal C_F(\tau',T)$ and every newly
  flagged history is generated by a Voice plan, so $\Omega(\tau',T)\geq\Omega(\tau,T)$ and
  $W_\tau\in[0,1]$. Equality holds when the threshold change reclassifies no history (almost surely).
\item \emph{Composition leg and the dial.} Under Condition~\ref{cond:D} at the pair and at
  $\kappa$, $C_\tau \le 1$, and therefore
  \begin{equation}
  \label{eq:threshold-dial}
  \frac{\mathcal S(\tau',T)}{\mathcal S(\tau,T)} \;=\; W_\tau\,C_\tau \;\le\; 1 .
  \end{equation}
\end{enumerate}
\end{theorem}

\noindent\textsc{Label: PROVED.}\par
\begin{theorem}[The clock dial at fixed policies; Appendix Section~\ref{app:sec:partition-factorisation}, Theorem~\ref{app:thm:clock}]
\label{thm:clock}
Fix the liquidity $\kappa$, the threshold margin $\tau$, and the plan and cutoff policies.
Compare two window margins $T' < T$. Assume $b_0 < \tau$, that Voice stake paths are weakly
increasing in the calendar date, that only Voice plans cross, $0 < \Omega(\tau,T) < 1$,
$0 < \Omega(\tau,T') < 1$, $\mathcal S_P(\kappa,\tau,T) > 0$, and the hypotheses of
Proposition~\ref{prop:factorisation} at both clocks, the differentiability of
$\kappa \mapsto M_P$ each instance carries included. Then:
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=2pt]
\item the weight leg attenuates: $0 < W_T \le 1$;
\item the sensitivity ratio factors as $\mathcal S(\kappa,\tau,T')/\mathcal S(\kappa,\tau,T)
  = W_T\,C_T$;
\item the shorter clock lowers noise sensitivity exactly when the product of the two legs is
  at most one,
  \[
  \mathcal S(\kappa,\tau,T') \;\le\; \mathcal S(\kappa,\tau,T)
  \qquad\Longleftrightarrow\qquad
  W_T\,C_T \;\le\; 1 .
  \]
\end{enumerate}
\end{theorem}

The two dials enter with different force. The threshold weight leg is PROVED. Its composition leg is
NUMERICAL on the order-size-two, $H=10$, $T=5$ grid at frozen benchmark policy, for four adjacent
threshold pairs and $\kappa\in[0.15,0.85]$ in steps of $0.01$. The clock result is PROVED as an
exact equivalence. The model does not sign $C_T$, so the effect of a shorter clock depends on which
histories leave the pooled cell. Because $W_T>0$, the attenuation criterion is equivalent to
$C_T\leq1/W_T$, and the right-hand side is at least one.

\subsection{Who gets caught}
\label{sec:caught}

Fix the threshold margin $\tau$ and the policies, and compare $T' < T$ at a common $\kappa$.
Write $A = \mathcal C_P(\tau,T)$ for the pooled cell under the longer clock and
$B = \mathcal C_F(\tau,T')\setminus\mathcal C_F(\tau,T)$ for the histories the shorter clock
newly flags, with $\varphi = \Prb(B)/\Prb(A)$ the share of the pool that is caught. Write
$s_A = \partial_\kappa\Eop[h^{(T)} \mid A]$ for the pool's own noise sensitivity in kernel
units and $s_B$ for the \emph{caught leg}: the derivative with respect to $\kappa$ of the
premium mass the shorter clock removes from the pool, per unit of caught mass, with the
survivors' re-pricing included. It is not the sensitivity of the caught histories at the old
prices; the difference is the re-pricing remainder $\delta$, and $s_B = \tilde s_B -
\bigl((1-\varphi)/\varphi\bigr)\delta$ with $\tilde s_B$ that old-price sensitivity.

\noindent\textsc{Label: PROVED.}\par
\begin{corollary}[Who gets caught; Appendix Section~\ref{app:sec:caught}, Corollary~\ref{app:cor:caught}]
\label{cor:caught}
Under (C-1) to (C-3) of the appendix, with the clock theorem's hypotheses also applying:
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=2pt]
\item the cut is nested, $B \subseteq A$, $A\setminus B = \mathcal C_P(\tau,T')$, and the
  weight leg is $W_T = 1-\varphi$;
\item the cell masses do not depend on $\kappa$, so $\varphi$ does not either;
\item the cut identity holds exactly:
  \[
  s_A \;=\; (1-\varphi)\,s_{A\setminus B} + \varphi\,s_B,
  \]
  the longer clock's pooled sensitivity is the mass-weighted average of what the shorter clock
  leaves in the pool and what it takes out;
\item the composition ratio satisfies
  \[
  C_T\leq1
  \quad\Longleftrightarrow\quad
  (s_B-s_A)\bigl(\varphi s_B-(2-\varphi)s_A\bigr)\leq0.
  \]
  Thus $C_T\leq1$ exactly when $s_B$ lies weakly between $s_A$ and
  $((2-\varphi)/\varphi)s_A$. The attenuation criterion $W_TC_T\leq1$ holds exactly when
  $s_B$ lies weakly between $0$ and $(2/\varphi)s_A$;
\item under a common nonzero sign, $C_T\leq1$ is equivalent to
  $|s_A|\leq|s_B|\leq((2-\varphi)/\varphi)|s_A|$. The caught leg must be at least as
  noise-sensitive as the pool and no more than that multiple.
\end{enumerate}
\end{corollary}

The caught leg turns $C_T$ into a statement about the premium mass removed from the pool. It has two
parts: the old-price sensitivity of the newly flagged histories and the re-pricing of the surviving
pool. Only when the re-pricing remainder is zero does $s_B$ measure the sensitivity of the caught
histories alone.

%==============================================================================
```

### 2.4 Calibration and figures
```latex
\section{The calibration and the figures}
\label{sec:calibration}
%==============================================================================

The calibration uses order size two and $H=10$. A seed policy at $\tau=0.05$, $T=5$, and
$\kappa=0.5$ supplies the Voice region. The threshold ladder uses the full-line signal quantiles
$0.1$, $0.3$, $0.5$, $0.7$, and $0.9$ of the stake-at-filing distribution under that seed policy.
The calculation clips signals only if a quantile crosses the computational support. The resulting
$\tau$ values run from $0.0924$ to $0.0970$. A second policy calculation at the median threshold,
$T=5$, $\kappa=0.5$, and $H=10$ gives the benchmark cutoff vector $k=(0.9425,1.8485)$. Every
comparative static freezes this benchmark policy. Expectation calculations use the renormalised
computational signal law stated in Section~\ref{sec:primitives}. The liquidity grid has seventy-one
nodes, $\kappa=0.15$ to $0.85$ in steps of $0.01$.

\paragraph{The factorisation on the grid.} The largest pointwise residual
$|\mathcal S-(1-\Omega)\mathcal S_P|$ over the order-size-two, $H=10$ grid at frozen baseline
policies is $5.1\times10^{-17}$. The flagged weight is flat in $\kappa$ to exactly $0.0$ at every
node. Figure~\ref{fig:sensitivity} draws the median threshold quantile and reports both factors.

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth]{figures/fig1_sensitivity_factors.pdf}
\caption{Noise sensitivity and its two factors against liquidity $\kappa$ at the calibration node
(the median threshold quantile, $\tau = 0.0945$), under both clocks, from the order-size-two
calibration record at frozen benchmark policy. Sensitivities are slopes over consecutive grid nodes
in premium percentage points per unit $\kappa$; the grid is $\kappa = 0.15$ to $0.85$ in steps of
$0.01$ with no gap. Left: $|\Delta \Dact / \Delta\kappa|$ (the finite-difference sensitivity).
Right: the two factors, the pooled finite-difference sensitivity $|\Delta M_P / \Delta\kappa|$ (left
axis, log scale) and the pooled share $1-\Omega$ (right axis, dotted), the factorisation $|\Delta
\Dact / \Delta\kappa| = (1-\Omega)|\Delta M_P / \Delta\kappa|$ holding to machine precision on every
node. At $H = 10$ the clock $T = 10$ is the corner $T = H$. Its flagged cell carries mass $\Omega =
6.8 \times 10^{-4}$ at every threshold node, below the code's degenerate-cell floor of $0.01$.}
\label{fig:sensitivity}
\end{figure}

\paragraph{The threshold dial on the grid.} The composition ratio is at most one at every adjacent
threshold pair in Table~\ref{tab:threshold}. This conclusion and the resulting dial inequality are
NUMERICAL on the order-size-two, $H=10$, $T=5$ grid at frozen benchmark policy, with
$\kappa\in[0.15,0.85]$ in steps of $0.01$. At $T=10$ the ladder reclassifies no mass, so both legs
equal one. The weight leg at $T=5$ lies between $0.975$ and $0.977$, with reclassified mass $0.0232$
at each pair. The composition leg reaches $0.791$. The largest value of $W_\tau C_\tau$ is $0.772$,
for the change from the $0.5$-quantile threshold to the $0.3$-quantile threshold. The claim covers
only the named grid.

\begin{table}[H]
\centering
\caption{The threshold dial at fixed policies, from the revelation record (NUMERICAL, grid
$\kappa \in [0.15, 0.85]$ in steps of $0.01$, order size two, $H=10$, $T=5$, frozen
benchmark policy). Each row
tightens the threshold from the $\tau$ quantile in the second column to the tighter one in the
first. $W_\tau$ is the weight leg; $C_\tau$ runs over the whole $\kappa$ grid; the last column
is the largest product on the grid.}
\label{tab:threshold}
\begin{tabular}{cccccc}
\toprule
Tighter $\tau$ quantile & From & Window $T$ & $W_\tau$ & $C_\tau$ range & $\max_\kappa W_\tau C_\tau$ \\
\midrule
0.1 & 0.3 & 5 & 0.975 & $[0.279, 0.456]$ & 0.445 \\
0.3 & 0.5 & 5 & 0.975 & $[0.219, 0.791]$ & 0.772 \\
0.5 & 0.7 & 5 & 0.976 & $[0.029, 0.587]$ & 0.573 \\
0.7 & 0.9 & 5 & 0.977 & $[0.140, 0.633]$ & 0.618 \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{The clock dial on the record.} The clock comparison is NUMERICAL on the order-size-two,
$H=10$ grid at frozen benchmark policy, with $\kappa\in[0.15,0.85]$ in steps of $0.01$, five
threshold nodes, and compares window margins $T=5$ against $T=10=H$ in discrete trading rounds.
This is a model comparison across trading-round horizons rather than a calibrated replica of the
statutory reform. The $T=10$ flagged cell is degenerate at every node, with
$\Omega=6.8\times10^{-4}$ below the code's $0.01$ floor, so this is a corner-to-interior
comparison. Table~\ref{tab:window} shows that the shorter clock reduces total-variation
sensitivity to between $2$ and $69$ percent of its long-clock value. The composition ratio runs
from $0.024$ to $0.699$, while the weight leg reduces the pooled share by between $1.1$ and
$10.4$ percent.

\begin{table}[H]
\centering
\caption{The window record at fixed policies (NUMERICAL, $\kappa\in[0.15,0.85]$ in steps of
$0.01$, order size two, $H=10$, frozen benchmark policy): cutting the clock from $T = 10$ to $T = 5$ at
each threshold node. Sensitivities are total variations of $\Dact$ and $M_P$ over the $\kappa$
grid. At $H = 10$ the clock $T = 10$ is the corner $T = H$ and its flagged cell is degenerate
($\Omega = 6.8\times10^{-4}$, below the code's floor of $0.01$), so the comparison is a
corner-versus-interior comparison.}
\label{tab:window}
\begin{tabular}{ccccc}
\toprule
$\tau$ quantile & $\Omega(\tau,5)$ & $W_T$ & $C_T$ & $W_T C_T$ \\
\midrule
0.1 & 0.10420 & 0.896 & 0.024 & 0.021 \\
0.3 & 0.08104 & 0.920 & 0.080 & 0.074 \\
0.5 & 0.05789 & 0.943 & 0.196 & 0.184 \\
0.7 & 0.03473 & 0.966 & 0.378 & 0.365 \\
0.9 & 0.01158 & 0.989 & 0.699 & 0.691 \\
\bottomrule
\end{tabular}
\end{table}

\paragraph{Who gets caught on the record.} On the five-node
clock-composition grid, the caught leg lies strictly inside the corollary's
band and $C_T<1$ at every node (NUMERICAL, frozen benchmark policy, point derivatives at
$\kappa=0.5$, order size two, $H=10$, $T'=5$ against $T=10=H$, with the $T=10$ flagged cell
degenerate at every node because $\Omega=6.8\times10^{-4}<0.01$). The pool sensitivity is
$s_A=0.0040$ in kernel units, $s_B$ ranges from $0.039$ to $0.135$, the upper multiple ranges
from $18$ to $182$, and $C_T$ ranges from $0.013$ to $0.643$.

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth]{figures/fig2_who_gets_caught.pdf}
\caption{The who-gets-caught record at five threshold nodes. The left panel places $s_B$
strictly between $s_A$ and $((2-\varphi)/\varphi)s_A$, and the right panel has $C_T<1$, at
every node (NUMERICAL, frozen benchmark policy, point derivatives at $\kappa=0.5$, order size
two, $H=10$, $T'=5$ against $T=10=H$, with the $T=10$ flagged cell degenerate at every node
because $\Omega=6.8\times10^{-4}<0.01$). The right panel marks $1$ as the ceiling.}
\label{fig:caught}
\end{figure}

%==============================================================================
```

### 2.5 Empirics and conclusion
```latex
\section{The empirics: the stake at filing and the clock}
\label{sec:empirics}
%==============================================================================

\subsection{Design and gates}
\label{sec:e1design}

The empirical layer is descriptive, reporting filing stakes and delays around the February 2024
rule change to provide institutional magnitudes for the model parameters rather than measuring
market inference directly. It identifies no effect, uses no control group, and makes no causal claim.
The design fixes the population and measurement before estimation. The measured object is the stake
at filing $B^F$, which the model produces at the filing date.

The population is every initial Schedule 13D filing (form types \texttt{SC 13D} and \texttt{SCHEDULE
13D}, both EDGAR spellings, no amendments) in the EDGAR quarterly form indexes from 2021 Q1 through
2025 Q4, with no screen on Item 4 purpose text. The unit is the campaign, one subject firm and
trigger date pair. The procedure collapses simultaneous group filings to the earliest acceptance.
The resulting sample has $4914$ campaigns. The procedure reads the stake from the cover page as the
percent of class and takes the maximum across reporting persons in a joint filing. The period split
is the rule date: pre if the trigger predates 2024-02-05, post otherwise. The delay of the clock
paragraph is the count of federal business days from the trigger date to the filing date.

The registered quality gates cover parsing, blind hand checks, and differential coverage. Readable
stakes cover $91.6$ percent of campaigns. The blind check reads sixty stratified campaigns and finds
zero material stake or trigger-date errors. The pre-to-post coverage gap is $7.0$ percentage points.
All three gates pass. The following subsection labels the post-minus-pre bootstrap differences
ESTIMATED; the registered design treats the remainder of the tables as descriptive statistics.

\subsection{The stake at filing}
\label{sec:e1results}

Table~\ref{tab:e1} reports $B^F$ by calendar year of the filing date and by period;
Figure~\ref{fig:e1} draws the distribution. Among campaigns with a readable stake, the median
is $13.1$ percent of class before the rule date and $12.8$ after, while the mean moves from
$22.3$ to $23.9$.

\noindent\textsc{Label: ESTIMATED.}\par
The post-minus-pre difference in the mean is $1.66$ percentage points with
a campaign-level percentile-bootstrap interval of $[0.20,3.11]$ based on $2{,}000$ draws and
seed 5. The median difference is $-0.30$ with interval $[-1.62,1.30]$.

\begin{table}[H]
\centering
\caption{The stake at filing $B^F$, percent of class, by calendar year of the filing date and
by period around the 2024-02-05 rule date. Campaigns with a readable stake; the coverage gate
E1-G1 passed at $91.6$ percent. The difference rows are post minus pre, campaign-level
bootstrap, $2{,}000$ draws, seed 5. Descriptive; no control group; no causal claim.}
\label{tab:e1}
\begin{tabular}{lccccc}
\toprule
 & $n$ & Mean & Median & P25 & P75 \\
\midrule
2021 & 1040 & 21.8 & 14.4 & 7.7 & 26.4 \\
2022 & 807 & 22.6 & 12.9 & 7.0 & 25.3 \\
2023 & 856 & 21.5 & 11.0 & 6.7 & 25.0 \\
2024 & 843 & 24.4 & 12.7 & 6.8 & 31.5 \\
2025 & 956 & 24.1 & 13.7 & 7.2 & 29.5 \\
\midrule
Pre (trigger before 2024-02-05)  & 2888 & 22.3 & 13.1 & 7.2 & 26.2 \\
Post (trigger from 2024-02-05)    & 1614 & 23.9 & 12.8 & 6.9 & 29.4 \\
\midrule
Difference in mean    & \multicolumn{5}{c}{$1.66 \; [0.20,\ 3.11]$} \\
Difference in median  & \multicolumn{5}{c}{$-0.30 \; [-1.62,\ 1.30]$} \\
\bottomrule
\end{tabular}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.62\textwidth]{figures/e1_stake.pdf}
\caption{The stake-at-filing distribution by period among campaigns with a readable stake,
from the campaign table behind Table~\ref{tab:e1}. The pre period has $n=2888$ and the post
period has $n=1614$. The medians are $13.1$ and $12.8$ percent of class. Descriptive; no
control group.}
\label{fig:e1}
\end{figure}

By Lemma~\ref{app:lem:bf-monotone} in the appendix, under fixed policies, a shorter window weakly
lowers the stake at filing on every path flagged under both windows. That statement is pathwise. The measured cross-section is not. The shorter clock can bring paths into the filing set that the
longer clock left in the pool, so the median and the mean of the filers can move either way. The
measured median difference is $-0.30$ percentage points, while the mean difference is $1.66$ points.
Table~\ref{tab:e1} reports their percentile-bootstrap intervals. This comparison is descriptive, and
the paper draws no causal conclusion from it. The rule date may coincide with other market changes,
so a before-and-after split carries no identification.

\subsection{The clock moved}
\label{sec:clock}

Table~\ref{tab:clock} documents the change in filing timing. It reports, by calendar year and by
period around the rule date, the share of campaigns filed within five
business days of the trigger and the median trigger-to-filing delay in federal business days.
Before the rule date, $32.7$ percent of campaigns were filed within five business days
(percentile-bootstrap interval $[31.1,34.3]$) and the median delay was $7.0$ business days;
after it, $75.9$ percent were filed within five business days ($[73.8,77.9]$) and the median
delay was $5.0$. By calendar year, the share within five business days rises from $27.8$
percent in 2021 to $39.0$ percent in 2023, then to $70.6$ percent in 2024 and $70.2$ percent in
2025. The median delay across those years is $7.0$, $7.0$, $6.0$, $5.0$, and $5.0$ days. The
statement is descriptive. It documents a change in realised timing at the rule date and
identifies no effect on another outcome.

The delay calculation uses all filings with a parsed trigger date and filing date. In the raw
records, two filings have a negative delay, reflecting typographical date errors
on the cover page, and $138$ filings have parsed trigger dates predating 2021 (the earliest reaching back
to 2010 with a delay of $2{,}870$ business days), reflecting multi-year legacy accumulations or late
disclosures. Retaining these filings preserves the registered descriptive protocol; because the primary
statistics are medians and shares within five business days, they are robust to extreme positive or
negative delays.

\begin{table}[H]
\centering
\caption{The filing clock, by calendar year of the filing date and by period around the
2024-02-05 rule date. The share is campaigns filed within five business days of the trigger;
the interval is a campaign-level bootstrap, $2{,}000$ draws, seed 5, reported for the two
period rows. Every campaign with a measured delay, no outcome screen. Descriptive.}
\label{tab:clock}
\begin{tabular}{lccc}
\toprule
 & Campaigns & Within 5 bus.\ days, \% & Median delay, bus.\ days \\
\midrule
2021 & 1167 & 27.8 & 7.0 \\
2022 & 903 & 33.9 & 7.0 \\
2023 & 962 & 39.0 & 6.0 \\
2024 & 918 & 70.6 & 5.0 \\
2025 & 964 & 70.2 & 5.0 \\
\midrule
Pre (before 2024-02-05)  & 3237 & 32.7 $[31.1,\ 34.3]$ & 7.0 \\
Post (from 2024-02-05)   & 1677 & 75.9 $[73.8,\ 77.9]$ & 5.0 \\
\bottomrule
\end{tabular}
\end{table}

%==============================================================================
\section{Conclusion}
\label{sec:conclusion}

A disclosure rule partitions the histories that reach a control decision. At fixed plan,
cutoff, and execution policies, the expected engagement premium's liquidity sensitivity equals
the pooled share times the pooled cell's sensitivity. This factorisation and the liquidity
invariance of the flagged endpoint are PROVED.

The two legal dials act differently on that partition. The threshold's weight effect is PROVED.
Its composition effect is NUMERICAL on the order-size-two, $H=10$, $T=5$ grid at frozen benchmark
policy, across four adjacent threshold pairs and $\kappa\in[0.15,0.85]$ in steps of $0.01$. For the clock, the
condition $W_TC_T\leq1$ is a PROVED necessary and sufficient condition for attenuation at fixed
policies. The who-gets-caught corollary is also PROVED. It characterises $C_T$ through the
sensitivity of the premium mass removed from the pool, including the re-pricing of the
survivors. The pooled experiment's garbling order and polynomial form are PROVED at order size
two.

The empirical measurement is descriptive, with the post-minus-pre differences labelled ESTIMATED.
Among initial Schedule 13D campaigns with readable stakes from 2021 to 2025, the median stake at
filing is $13.1$ percent of class before the 2024 clock change and $12.8$ percent after. Across all
measured delays, the share filed within five business days rises from $32.7$ to $75.9$ percent, while
the median delay falls from $7.0$ to $5.0$ business days. These measurements describe the stake at
filing and the change in realised filing timing at the rule date. They do not identify an effect of the
clock on the stake.

\printbibliography
```

### 2.6 Standing conditions (appendix)
```latex
\label{sec:partition-factorisation}

The disclosure rule $(\tau,T)$ acts on the model first as a partition of histories and only then as
a statement about prices. This subsection separates the two. The partition is combinatorial and
needs no restriction on cell mass; the two-cell decomposition of the premium needs an interior
partition; the factorisation of the liquidity sensitivity needs, in addition, that the flagged
endpoint and the flagged weight are both free of $\kappa$.

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

\subsubsection*{The partition}
```

### 2.7 The who-gets-caught corollary and its proof (appendix)
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
that question is who gets caught. Under a common sign, $s_A s_B > 0$, the composition ratio
satisfies $C_T \le 1$ if and only if the caught sensitivity $s_B$ lies weakly between $s_A$ and
$\bigl((2-\varphi)/\varphi\bigr)\,s_A$, which is part~(iv); and the shorter clock lowers noise
sensitivity overall, $W_T C_T \le 1$, if and only if $s_B$ lies weakly between $0$ and
$(2/\varphi)\,s_A$, which is part~(v). The two bands differ: the weight leg lets the overall
criterion accept a caught leg less sensitive than the pool, which the composition criterion alone
does not.
```

## 3. The four gated upgrades and the batch-4 spec

### 3.1 Hunt log
# Hunt log

Administered by Prime Agent session 01a062f7-8328-74d1-b3ab-65d6de96840e (Fable), started
2026-09-02T17:42. Handoff: /tmp/blockholder_v5_handoff/theory-hunt-handoff.md.

## Workers spawned

| Candidate | Directory | Worker | Model | Thinking | Child id |
|---|---|---|---|---|---|
| 4.1 erasure regime | 1-erasure-regime | hunt-erasure | openai-codex/gpt-5.6-sol | xhigh | sub-fd74c021 |
| 4.2 one cut identity | 2-one-cut-identity | hunt-cut-identity | openai-codex/gpt-5.6-sol | max | sub-b5ff30e8 |
| 4.3 Blackwell tightening | 3-blackwell-tightening | hunt-blackwell | openai-codex/gpt-5.6-sol | xhigh | sub-3ecbcf51 |
| 4.4 benchmark regret | 4-benchmark-regret | hunt-regret | openai-codex/gpt-5.6-sol | high | sub-8a6cab2a |

## Attacks

Attacker is Opus (`anthropic/claude-opus-5`) for every memo written by Sol.

| Candidate | Memo status | Memo received | Attacker | Child id | Verdict |
|---|---|---|---|---|---|
| 4.1 erasure regime | PASS | 2026-09-02T17:54 | attack-erasure | sub-978fb927 | PASS, five nits (attack.md) |
| 4.4 benchmark regret | PASS | 2026-09-02T17:58 | judge-regret | sub-860e781b | PASS, five nits (attack.md); one-node recompute bit for bit |
| 4.3 Blackwell tightening | PASS | 2026-09-02T18:03 | attack-blackwell | sub-ff4bf664 | PASS, eight nits (attack.md); 13500 kernel cases, 34560 LPs |
| 4.2 one cut identity | PASS (both parts) | 2026-09-02T18:04 | attack-cut-identity | sub-a6883c4c | PASS on both parts, eight nits (attack.md); certificate script byte-identical rerun |

## Verdicts

| Candidate | Writer | Memo | Attacker | Gate | Label the memo would support | My rank |
|---|---|---|---|---|---|---|
| 4.3 Tightening is a Blackwell improvement | Sol xhigh | PASS | Opus 5 | PASS, 8 nits | PROVED after nits | 1 |
| 4.1 Order size two is the erasure regime | Sol xhigh | PASS | Opus 5 | PASS, 5 nits | PROVED after nits | 2 |
| 4.2 One cut identity for both dials | Sol max | PASS (both parts) | Opus 5 | PASS, 8 nits | Part 1 PROVED; Part 2 implication PROVED, calibration NUMERICAL | 3 |
| 4.4 Certified benchmark regret | Sol high | PASS | Opus 5 (judge) | PASS, 5 nits | NUMERICAL, no label change | 4 (record, not a theorem) |

Paths: memo.md, attack.md and the attacker's scripts sit in each candidate directory under
`.scratch/v5-paper/hunt/`. Survivors hand to the writing thread's orchestrator at checkpoint 2 or 3
by path; labels are set there, not here. Nothing under `.scratch/v5-paper/issues/` was touched.

Why this order. 4.3 is a theorem that changes what the paper can say first ("tightening always
improves what the market knows"); its content is the identification hypothesis (S14), which the
attacker confirmed is the only load-bearing addition, and it is strict at T = 5 and an equality at
the corner T = 10. 4.1 is cheap and answers the referee's "why order size two" with a proposition
whose b = 2 half is Lemma g2 verbatim; the attacker corrected one side remark (the 2/3 turn and
"incomparable" are one-round facts). 4.2 unifies the composition legs into one corollary (Part 1
is a transcription) and adds a kappa-interval certificate whose largest root is the exact endpoint
of the Condition D failure; the attacker's nit 8 matters for the reading, since at the threshold
dial the caught leg is dominated by survivor re-pricing (1/phi about 40). 4.4 is a record: it
answers "why care about this benchmark" with one number per node (2.4e-4 at most, about 0.6% of
the payoff level at the cutoff) and belongs in the calibration section, not in a theory pack.

GPT Sol Pro pack 3 (`gpt-sol-pro-pack-3.md`, prompt `gpt-sol-pro-prompt-3.txt`) carries the top
three with the memos' statements and proofs and the attackers' verdicts and nits, and asks for a
ranking and appendix-level proof sketches. Pack 2 (`gpt-sol-pro-pack-2.md`) is the earlier,
pre-memo version and is superseded.

### 3.x Memo statement: 1-erasure-regime
# Order size two is the erasure regime

## 1. Statement

### Hypotheses

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

### Proposition

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


### 3.x Memo statement: 2-one-cut-identity
# One cut identity for both dials

## 1. Statement

### Standing hypotheses

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

### Part 1: threshold cut corollary

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

### Part 2: a single-crossing revelation certificate

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


### 3.x Memo statement: 3-blackwell-tightening
# Blackwell order under a tighter disclosure rule

## 1. Statement

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


### 3.x Memo statement: 4-benchmark-regret
# Certified benchmark-policy regret

## 1. Statement

### Hypotheses

The claim uses the standing-condition numbering of `proofs/04_inherited.tex`.

1. **(S1), one probability space.** The primitive vector, value $v$, signal noise
   $\varepsilon$, bidder draw $\xi$, and noise marks $z_{0:H}$ have a joint law on a finite
   product of Polish spaces. The noise marks lie in $\{-\bar z,0,+\bar z\}$, and
   $s=v+\varepsilon$.
2. **(S2), a finite menu and calendar.** The plan menu $\mathcal J$ is finite, $H$ is
   finite, and $T\in\{1,\ldots,H\}$.
3. **(S3), a cutoff selection map.** A step function with two ordered breakpoints carries the
   signal into Exit, Hold, or Voice.
4. **(S4), monotone Voice paths and a clean start.** Every plan has a stake path
   $B_j(s,\cdot)$ with $B_j(s,-1)=b_0<\tau$. The Voice path is weakly increasing in the signal
   and the date.
5. **(S5), legal-clock discipline.** Only Voice crosses the threshold. Its crossing date is the
   first date at which the path reaches $\tau$, or infinity if it never does. A truthful filing
   lands exactly $T$ dates later and only through the disclosure node.
6. **(S6), a public flag.** Every pooled history records whether the filing has landed by date
   $d$, and the control-node information contains the public history through that node.
7. **(S7), no-feedback timing.** The plan and signal determine the executed path, order marks,
   target, crossing date, filing date, filing stake, and flagged order. Realised flow and prices
   do not change them.
8. **(S8), a bounded pinned kernel.** The engagement-premium kernel is $h=\pi p$. The posterior
   $\pi$ lies in $[0,1]$. The bidder-entry probability $p$ lies in $(0,1)$ and is continuous in
   the posterior and price. The pricing rule pins one conditional-expectation version.
9. **(S9), a finite wedge.** $\Delta_m$ is finite and strictly positive, and
   $\Delta_{act}=\Delta_m\mathbb E[h(\mathcal I_H)]$.
10. **(S10), liquidity enters in one place.** $\kappa$ changes only the ternary noise-mark law.
    The laws of $v$, $\varepsilon$, and $\xi$ and all remaining constants do not change with
    $\kappa$.
11. **(S11), fixed policies.** The plan menu, execution policies, and benchmark cutoff vector
    remain fixed across all ten nodes.
12. **(S12), calibration.** The cutoffs are
    $k=(0.9425017266871091,1.8484512098302512)$. Also, $\kappa=0.5$, the order size is two noise
    lumps, and $H=10$. The rule has $T\in\{5,10\}$ and
    $\tau\in\{0.09239820387429526,0.09346755804663053,$
    $0.09453534811956685,0.09565657882778708,0.09703177146201895\}$.
    The remaining primitives equal `ParamsV4.baseline()`. The source parameter hash is
    `fbacc963f39422c3`, and `regret.json` gives the hash after each node's $T$ and $\tau$ are set.
13. **(S13), signal support.** The signal law is the calibrated Gaussian law restricted to
    $[s_{lo},s_{hi}]$, with $s_{lo}=1-6/\sqrt{2}$ and
    $s_{hi}=1+6/\sqrt{2}$. It has a continuous density. Finite breakpoint sets are null.
14. **(S14), fixed pooled pass.** At each node, `res` is the pooled pass at
    `atoms(frozen_k, p)` with the run-up path present. A deviation changes only the deviating
    signal and plan. It does not recompute `res`.

### Claim

Let $U_j(s)$ be `numerical_v4.policy.plan_payoff(j, s, res, p)`, let $j(s)$ be the benchmark
plan, and set
\[
 R(s)=\max_{j\in\{E,H,V\}} U_j(s)-U_{j(s)}(s).
\]
At every calibration node, the essential supremum of $R$ is no larger than the bound in the
last column. The certificate uses the full breakpoint partition, mesh width at most $10^{-5}$,
an analytic payoff-gap Lipschitz bound on each piece, and a $5\times10^{-12}$ arithmetic
allowance.

| Node | $T$ | $\tau$ | Certified upper bound |
|---:|---:|---:|---:|
| 1 | 5 | 0.092398203874295259 | `9.623219552034791e-05` |
| 2 | 5 | 0.093467558046630525 | `0.0001592462568311867` |
| 3 | 5 | 0.094535348119566848 | `0.00018783235544278404` |
| 4 | 5 | 0.095656578827787081 | `0.00020784219766716692` |
| 5 | 5 | 0.097031771462018954 | `0.0002248763859580155` |
| 6 | 10 | 0.092398203874295259 | `0.00024250934252785308` |
| 7 | 10 | 0.093467558046630525 | `0.00024250936609786458` |
| 8 | 10 | 0.094535348119566848 | `0.0002425093647088392` |
| 9 | 10 | 0.095656578827787081 | `0.00024250936470879758` |
| 10 | 10 | 0.097031771462018954 | `0.00024250936470879758` |

`regret.json` reports the attaining piece and its prior mass. It also reports every piece whose
certified upper bound is positive, all possible profitable alternatives on that piece, and a
sample witness when one exists. This conservative rule retains a piece even when only its
upper bound, rather than a computed payoff gap, is positive.


### 3.5 The batch-4 spec as it stands (the contrast headline)
# 15 · Theory upgrade: information is monotone in the rule, noise robustness is not

**Lane:** theory and paper. **Routing:** batch 4, on top of the delivered v5 paper (checkpoint 3).
**Blocked by:** 14 (delivered). **Blocks:** nothing. **Triage:** ready-for-agent.

Revised 2026-09-02 after GPT Pro's review of the first draft
(`.scratch/v5-paper/hunt/pro_response.md`) and an independent Fable review of that review. Both
are input, never authority, never cited. This file is final; the batch runs from it.

Inputs: the four hunt memos and attack records under `.scratch/v5-paper/hunt/` (every candidate
passed writer, then an independent Opus attacker), the committed grid records under
`numerical_v4/checks/`, and the delivered `paper.tex`, `appendix.tex`, `proofs/`.

## Problem statement

The delivered paper says that tightening a disclosure rule lowers the noise sensitivity of the
engagement premium at fixed policies, one leg proved and one leg on the grid, and that
shortening the clock does so when a composition ratio is at most one. A reader takes that as
"more disclosure, cleaner prices", which is the ordinary intuition, and the paper reads as a
refinement of it. The order size of two noise lumps reads as a convenience and the benchmark
policy as arbitrary.

The hunt proved four results that turn the paper's message from a refinement into a contrast,
and the record already contains the instance that makes the contrast bite. None of it is in the
paper.

## Solution

The paper states a contrast between two things a disclosure rule does, proves both halves, and
names the mechanism. The abstract's central sentences, as the batch prints them:

> At fixed policies and a common liquidity, tightening either dial makes the market's
> control-node experiment weakly more informative in Blackwell's order, because the filing tuple
> identifies the blockholder's signal. That order does not settle what liquidity does to prices.
> For either dial, the tighter rule lowers the liquidity sensitivity of the engagement premium
> exactly when the premium mass it removes from the pool, the re-pricing of what stays pooled
> included, lies in a band set by the pool's own sensitivity and the share removed. On the
> calibration the band holds on the whole liquidity interval from 0.15 to 0.85, and for every
> pair of both dials it fails on an open interval below it, around the liquidity at which the
> looser pool's sensitivity changes sign, where the tighter rule is the more noise-sensitive one.

1. **Information is monotone in the rule.** Tightening either dial at a common liquidity and
   fixed policies is a Blackwell improvement of the market's experiment at the control node. It
   holds under the standing conditions together with the noise channel and the flagged-tuple
   decoder, both stated as standing conditions. The market knows the blockholder is engaged and
   the filing tuple identifies her signal. This is the paper's first economic result.
2. **Noise robustness is not implied by it.** At the control node, liquidity enters the
   engagement premium only through the pooled cell. A tighter rule removes histories from the
   pooled cell, and the looser pool's sensitivity is a mass-weighted average of the survivors'
   sensitivity and the net cut leg, the sensitivity per unit mass of what was removed, survivor
   re-pricing included. The same identity holds for both dials. The composition ratio is at most
   one exactly when the net cut leg lies between the pool's sensitivity and (2 minus φ)/φ times
   it; total sensitivity falls exactly when the net cut leg lies between zero and 2/φ times the
   pool's sensitivity, so the weight leg can attenuate even when the removed histories were less
   sensitive than the pool. A one-crossing lemma on the liquidity-free coefficients decides the
   band on any liquidity interval above a computable cutoff; its calibration application is
   NUMERICAL.
3. **The reversal.** Each pool's sensitivity has one sign change in liquidity and the two pools'
   zeros differ, so on an open interval around the looser pool's zero the tighter rule has
   strictly larger total sensitivity. The paper reports that interval for every non-null pair of
   both dials, inward-rounded, with the magnitudes beside it (three to four orders below the
   grid values), and never says that thin-market prices are volatile.
4. **The mechanism is inference from silence.** The net cut leg splits into a caught-only leg
   and a re-pricing term δ scaled by (1 minus φ)/φ: the histories that stay pooled are re-priced
   because the absence of a filing now says more. This is the interpretation the paper gives
   and it carries no label. The split is reported at every node from a record. A sentence that
   one term dominates the other enters only if the record shows it at every node, with the
   record's ratio, never a round number.
5. **The order size and the benchmark are defended.** Among positive integer multiples of one
   noise lump, order size two is the unique size whose binary order-mark channel is an exact,
   non-trivial erasure family over the whole interior liquidity range: at size one the
   higher-liquidity experiment is never a garbling of the lower one on any nondegenerate mark-path
   set, and at sizes three and above each binary order mark is decoded. The benchmark policy's
   interim regret, a certified upper bound on the largest one-step deviation gain at benchmark
   prices and beliefs over the computational signal support, is reported at every node with the
   convention and a normaliser.

The abstract, the introduction and the conclusion are rewritten. The model, the factorisation,
the existing theorems and their proofs are not rewritten; they are reordered, relabelled and
extended as listed below.

## User stories

1. As a reader of the abstract, I want the two central sentences above, so that I know the contrast before the model.
2. As a reader of the introduction, I want the Blackwell result stated first among the results, so that the sensitivity results read as the surprise.
3. As a reader of the introduction, I want an explicit sentence that a Blackwell order at fixed liquidity does not sign the liquidity sensitivity of the premium, so that I do not conflate the two objects.
4. As a referee, I want the Blackwell theorem stated at the control date with every hypothesis numbered in the standing-condition scheme, the noise channel and the flagged-tuple decoder among them, so that I can check what it rests on.
5. As a referee, I want the theorem to name the flagged-tuple decoder as its load-bearing hypothesis and point to the model paragraph that defends the tuple, so that the result is not read as free.
6. As a referee, I want strictness and equivalence stated per comparison: strict on the threshold ladder at the five-round clock where the cut has positive mass, Blackwell-equivalent at the null ten-round threshold cuts, and the clock comparison a separate non-null comparison, so that no sentence overreaches the theorem.
7. As a referee, I want the paper never to claim a strict Blackwell order from a change in the flagged share alone, so that strictness rests on positive cut mass plus the decoder.
8. As a reader of the model section, I want one paragraph on the order-size trichotomy with the proof in the appendix, so that the normalisation reads as a transparency choice.
9. As a referee, I want the erasure proposition stated at the channel level and transferred to the pooled experiment only under a nondegenerate mark-path set, with the one-round decision-problem value scoped to one coordinate, so that no side remark is false over the horizon.
10. As a reader of the results section, I want the who-gets-caught corollary restated at the threshold margin with the same words after the clock-indexed sets and kernels are replaced by their threshold counterparts, so that both dials visibly obey one accounting law.
11. As a reader, I want the removed histories' leg called the net cut leg everywhere, the caught-only leg and the re-pricing term named, and the split reported at every node, so that "who gets caught" is read honestly.
12. As a referee, I want the composition condition on a liquidity interval decided by the gated one-crossing lemma on the coefficients, with the cutoff, the sign lists and their margins reported, so that the grid claim becomes an interval claim.
13. As a reader of the calibration section, I want the total-sensitivity reversal interval for every non-null pair of both dials, inward-rounded, with the composition interval beside it and the magnitudes at the interval and at the grid, so that the contrast is shown on the paper's own numbers and read at its true size.
14. As a referee, I want the reversal proved as a lemma from one crossing at both pools and distinct roots, so that the reversal is a structural fact and not a grid coincidence.
15. As a reader of the calibration section, I want the benchmark's interim regret bound at every node in one sentence and one table row, with the deviation convention and the normaliser stated, so that "why this policy" has a number and a definition.
16. As a referee, I want the ten-round threshold comparisons marked as boundary checks where the cut is null, so that a degenerate cell is not read as a finding.
17. As a referee, I want the standing conditions to state the noise channel and Borel regularity of the policy objects, so that every kernel expectation is well defined.
18. As a referee, I want one sentence reconciling the off-path belief floor in the records with the exact liquidity representation, with the perturbation bound compared to the smallest sign margin, so that the records and the lemma agree.
19. As a referee, I want the standing-condition citation in the corollary's hypothesis corrected (liquidity enters in one place is (S10), fixed policies is (S11)), so that the numbering is consistent.
20. As a reader, I want every new statement to carry the label it holds, every label to come from the attack gate and not from prose, and any post-gate edit to a statement or proof to reopen the gate, so that the honesty rules hold on the upgraded paper.
21. As a reader, I want every new number to render from a result file that the number guard asserts against, so that no number in the paper is typed by hand.
22. As the author, I want the existing theorems, corollary and proofs untouched except for the reorder, the renaming, the corrected citation and the reconciliation sentence, so that no PROVED result reopens its gate.
23. As the author, I want the paper to say nothing about the hunt, the memos, the external reviews, or any earlier version, so that the paper stays the only record.
24. As the author, I want both PDFs recompiled clean, inspected page by page, unslop-gated, and delivered, so that the upgraded paper replaces the delivered one in full.
25. As a reader of the conclusion, I want the fixed-policy scope stated plainly with the regret bound as its quantitative answer and no claim that it establishes existence or robustness to a reacting blockholder, so that the paper owns its limit.

## Implementation decisions

- **Placement.** In the results section the partition lemma stays first, because the theorem's
  statement uses the two cells and the flag. The Blackwell theorem follows it immediately, then
  the non-implication sentence of story 3, then the two-cell decomposition, the flagged cell's
  invariance and the factorisation as a following subsection. The introduction leads with the
  Blackwell result. The trichotomy paragraph goes into the order-size subsection of the model,
  its proposition and proof into the appendix's garbling section, stated before the order-size-two
  lemma with a local auxiliary integer order size. The threshold-margin restatement, the split
  identity, the one-crossing lemma and the reversal lemma go into the who-gets-caught subsection
  and its appendix section, retitled for nested cuts under both dials. The regret sentence and
  table row and the reversal intervals go into the calibration section.
- **Statements.** The Blackwell theorem is stated at the control date, on the flagged region of
  the tighter rule; corollaries (posterior risk, the two-parameter chain with the garbling lemma)
  are separate statements. The strictness corollary (positive newly flagged mass, nonatomic signal
  there, finite pooled range) is a separate gated statement. The trichotomy proposition follows
  the hunt memo's statement, with its nondegeneracy and noise hypotheses named, not the weaker
  order-size-one clause of the external review. The one-crossing lemma is the hunt memo's
  Descartes argument on the reversed coefficient polynomial: one sign change in each pool's
  coefficient list and one in their difference give one positive root each, and above the largest
  root the band holds. The reversal lemma states that one crossing at both pools with distinct
  roots gives a strict reversal of total sensitivity on an open interval around the looser pool's
  root. The regret statement is an upper bound on the essential supremum of the one-step
  deviation gain over the truncated signal support, at benchmark prices and beliefs.
- **The corollary is not restructured.** A generic nested-cut proposition replacing both
  corollaries is not adopted. The threshold-margin restatement carries the content.
- **Standing conditions.** Add the noise channel (independence of the noise marks from value,
  signal noise and bidder draw; independence across dates; the ternary law) and the flagged-tuple
  decoder as two new numbered conditions. Add Borel regularity to the selector, stake-path and
  no-feedback conditions as a clarification, recorded as such in the batch result, with the
  attacker asked to confirm that no existing proof changes. Update every "(S1) to (S11)" citation.
  Correct the corollary's (C-1) citation from (S11) to (S10) and cite (S11) separately.
- **Renaming.** The leg written s_B is the net cut leg everywhere: paper prose, corollary
  statement and proof, the reading paragraphs, the abstract, the Figure 2 legend and caption.
  The leg written with a tilde is the caught-only leg. One glossary entry "Net cut leg" is added
  to CONTEXT.md. The condition the paper prints as Condition 1 keeps that name; "Condition D" does
  not appear in the paper.
- **Labels at write time.** New statements carry no label until the attack gate returns. The
  expected outcome, set at the checkpoint and not by the writer: the Blackwell theorem, the
  trichotomy, the threshold-margin restatement, the split identity, the one-crossing lemma and
  the reversal lemma PROVED; the strictness corollary PROVED if it passes and absent otherwise;
  the sign lists, cutoffs, intervals, magnitudes, the split at the nodes and the regret bound
  NUMERICAL with the grid and the calibration named.
- **Records.** Two new check records under the theory-code checks, each with the provenance block
  of the existing records. The cut record carries, per non-null pair of either dial: the
  coefficient lists and sign lists with their smallest margins, the roots and the cutoff in
  high-precision arithmetic, the total-sensitivity reversal interval with a Lipschitz cover on a
  dense mesh and inward-rounded endpoints, the composition interval beside it, the magnitudes of
  both rules' sensitivities inside the interval and at three grid points, the split (pool
  sensitivity, survivor sensitivity, net cut leg, caught-only leg, re-pricing term, φ) at every
  grid node with the three residuals of the identities, a cancellation measure for the scaled
  re-pricing term, the off-path floor's uniform perturbation bound on the coefficients against the
  smallest sign margin, and the newly flagged masses per comparison. The regret record is the
  hunt's, re-run through a check run with provenance, the deviation convention (benchmark pass
  fixed, reference belief off path, truncated support, tie rule) and a normaliser in the record.
  The number guard grows by one test per record.
- **Compute.** No cold solve. The coefficients exist in the committed revelation record; the
  split needs level-set sums under both rules' kernels for the cell events, a handful of pooled
  passes; the finite-difference route needs about 120 pooled passes. Under an hour on the machine,
  one run at a time under the compute lock. The horizon is not lowered.
- **Certification standard.** No interval arithmetic and no coefficient enclosures. The word
  "certificate" is reserved for the PROVED one-crossing lemma; the calibration section says
  "the lemma applied to the record's coefficients" and labels it NUMERICAL. The reversal
  intervals are covered on a mesh by the polynomial's Lipschitz bound, the same method as the
  regret record.
- **Prose.** The abstract, the introduction and the conclusion are rewritten around the two
  central sentences. Section 2 of the session spec carries them. No ADR is written.
- **Sequence inside the batch.** Records first, then the appendix statements and proofs, then
  the attack gate per statement, then the paper prose, then the label-and-compile check, one
  referee read, one author fix, the gate reopened for any statement the fix touches, compile,
  inspect, deliver.

## Testing decisions

- A good check reads a statement and its proof and tries to break it, or reads a record and
  recomputes it by an independent route. It does not re-read the memo or the worker's reasoning.
- **Attack gate**, one per new statement: writer, then an independent Opus attacker with the
  statement, the model and the proof. Any edit to a statement, a hypothesis, a kernel, a
  polynomial or a proof step after the gate reopens it. Prior art: the `02-attack`, `03-attack`,
  `13-attack` and `13-attack-2` run records.
- **Check runs** for the two records, at every node rather than one: the sign lists, roots and
  cutoffs recomputed in high-precision arithmetic from the record's coefficients; the closed-form
  derivative compared with central finite differences of the pooled premium from pooled passes at
  three liquidities per node, one inside the reversal interval, with the tolerance stated against
  the derivative scale and the sign margin; the three identity residuals with absolute and
  scale-adjusted values; the regret bound recomputed at the attaining piece and every cutoff and
  beaten by a refined search. Prior art: `03-grid-judge`, `01-verify`, the hunt's attack scripts.
- **Number guard**: the existing test module, extended with one test per new record, asserting
  every rendered string appears in the paper verbatim.
- **Label-and-compile check** over the final tree, with a substantive hypothesis audit: every
  statement labelled; no absent result mentioned; no process language; every standing-condition
  citation resolves to the right condition; no "(S1) to (S11)" left; no differentiability claimed
  on a null cell; no ratio where the denominator sensitivity is zero; "prices" never used where
  only the engagement premium is proved; "caught leg" never used for the net quantity; compile
  clean in the order the project file gives; cross-document references regenerated from labels.
  Prior art: `11-check-2`, `13-check-2`.
- **One referee read** at journal standard, then one author fix pass, then the unslop gate.
  Prior art: `12-referee-3`, `14-unslop`.

## Out of scope

- Restructuring the who-gets-caught corollary into a generic nested-cut proposition.
- Equilibrium existence, a reacting blockholder, or any best-response layer. The regret bound
  quantifies the fixed-policy approximation under its stated convention and establishes nothing
  beyond that.
- The robustness neighbourhood around the benchmark policy. Deferred; it enters only if compute
  allows after every gate above has passed.
- Interval arithmetic in the pooled pass or the pricing root; coefficient enclosures; a keyed
  TeX-macro rendering refactor for the number guard.
- Any change to the calibration, the empirics, the registered spec, or the figures beyond
  regenerating the ones whose legend or record changes.
- Removing objects the external review flagged that are not in the paper.
- A new ADR or a CONTEXT.md rewrite beyond the one glossary entry.

## Further notes

- Fail twice, stop, per statement. A statement that fails its attack twice is absent from the
  paper, and the paper does not mention it. The strictness corollary and the reversal lemma are
  the two statements the abstract can survive without; the abstract's reversal clause then becomes
  a NUMERICAL sentence off the record.
- The multiplier (1 minus φ)/φ is near forty on the calibration. That number is not a finding.
  Whether the re-pricing term dominates the caught-only leg is decided by the split record.
- Any future external pack quotes the delivered paper, not the inherited draft, which produced
  three false alarms in the first review.

## 4. Facts from the committed record (order size two, H = 10, frozen benchmark policy)

Source: numerical_v4/checks/t2_threshold_revelation_check.json. Each node carries the kappa-free
coefficients c_0..c_10 of the exact representation d M_P / d kappa = -(Delta_m/2) L(kappa/2),
L(x) = sum_k c_k (1-x)^k x^(10-k), and the flagged share Omega. Total sensitivity
S = (1 - Omega) |d M_P / d kappa|. Recomputed 2026-09-02 from the record by the orchestrator.

Sign structure. At every node the coefficient list changes sign once, so d M_P / d kappa has one
root kappa* in (0,1): the pooled premium rises in kappa below kappa* and falls above it. Roots of
the looser pool at T = 5 by threshold quantile: q0.9: 0.0487, q0.7: 0.1086, q0.5: 0.1460,
q0.3: 0.1260. The T = 10 pools share a root near kappa = 0.019.

Reversal of total sensitivity (tighter rule has larger S), T = 5 adjacent threshold pairs:
  q0.9 -> q0.7: kappa in [0.0293, 0.0614]
  q0.7 -> q0.5: kappa in [0.0949, 0.1167]
  q0.5 -> q0.3: kappa in [0.1437, 0.1489]
  q0.3 -> q0.1: kappa in [0.1211, 0.1333]
The composition condition (C_tau <= 1) fails on almost the same intervals. Clock pairs T = 10 to
T = 5 reverse on a short interval around kappa = 0.019 at every threshold node. At T = 10 the
adjacent threshold cuts are null (no reclassified mass), so both legs equal one.

Magnitudes of S (per unit kappa, premium units), pair q0.5 -> q0.3:
  kappa   S_loose(q0.5)  S_tight(q0.3)
  0.146   1.6e-9         1.1e-7     (inside the reversal interval)
  0.15    1.7e-7         1.3e-7
  0.20    3.3e-6         7.2e-7
  0.50    1.0e-4         3.4e-5
  0.85    6.4e-4         2.9e-4
So the reversal sits where both sensitivities are three to four orders below their grid values.

Cut masses and the lever. At T = 5 each adjacent threshold pair reclassifies mass 0.0232;
phi = reclassified mass / pooled mass is 0.0234 to 0.0252; (1 - phi)/phi is 39 to 43. The ratio
s_B / s_A of the net cut leg to the pool sensitivity runs from 9.3 to 40.5 across the grid,
against the band's upper limit 1/phi of 40 to 43: near the low end of the grid the survivors'
sensitivity is close to zero and the net cut leg accounts for nearly all of the pool's. The split
of s_B into a caught-only leg and a re-pricing term has not been computed.

Benchmark regret (hunt memo 4, certified upper bound on the one-step deviation gain at benchmark
prices and beliefs over the truncated signal support): 9.6e-5 to 2.2e-4 at T = 5 nodes, 2.4e-4 at
T = 10 nodes; about 0.6 percent of the payoff level at the cutoff.

Order size one in this code. The pooled pass exists at order size one (the `mark` parameter);
flow then takes four values and two are ambiguous. No v5 calibration run at order size one has
been made. The hump result at order size one belongs to a predecessor model with a different
calibration and is not in the delivered paper.

## 5. The author's pitch: loudness is a choice

Make the order size a choice. The blockholder can accumulate at order size one, hidden and slow
(her buy is indistinguishable from a noise buy), or at order size two, loud and fast (only one
flow value is ambiguous). The clock makes this a trade-off: after crossing the threshold she has
T rounds before the filing lands, and a short clock rewards speed over cover. The disclosure rule
then sets how loudly blockholders trade, and the hump in liquidity returns through that choice.

Proposed headline: disclosure clocks do not mainly reveal blockholders; they set how loudly they
trade. A short clock pushes accumulation from cover into speed. Predictions: more of the
revaluation in the pre-filing run-up and less in the filing-day jump; the liquidity-activism
relation, positive under a long clock, flattens or reverses under a short one. The 2023 SEC
reform shortened the clock (ten to five business days, effective February 2024), so the run-up
versus jump split by pre-trigger liquidity before and after the change is the descriptive
fingerprint, and the model says which way it moves.

Why it is feasible with the current machinery: both pooled experiments exist in the code as the
order-size parameter (one and two); the factorisation and the cut identity hold at either size;
the garbling lemma is the size-two case and the trichotomy is the reason the choice is binary;
the choice is one discrete best response at fixed cutoffs, computed at every calibration node and
certified with the same Lipschitz-cover method as the regret record. No existence theorem is
needed: the choice is evaluated at benchmark prices and beliefs, the convention the regret record
already registers. The threshold becomes the supporting dial and the clock the lead dial.

What it costs: the paper's question changes; the abstract, introduction and the order of results
are rewritten; the Blackwell theorem and the cut identity become tools, not headline; the empirical
run-up versus jump exercise, absent at delivery because its gate failed, would need its gate rerun.

Known weaknesses the author sees: (a) a binary size choice at fixed cutoffs is a partial
response, and a referee will ask why the cutoffs do not move too; (b) with only one size choice
per path, the "speed" margin is coarse; (c) at order size one the paper loses the garbling lemma
for that branch and must sign the hump by another route; (d) whether the hump is visible at the
calibration is not known: the size-one experiment has not been evaluated at the v5 calibration.

## 6. Alternatives considered

- The silence lever. The threshold cut reclassifies about 2.3 percent of histories and the cut
  identity scales the survivors' re-pricing by (1 minus phi)/phi, near forty. If a split record
  shows the re-pricing term dominates the caught-only leg, the paper can say a rule that catches
  2 percent re-prices 98 percent. One NUMERICAL number on the flat model.
- Endogenous cutoffs. Best-response entry at each node, so the rule changes who becomes an
  activist. Reopens existence questions the paper escaped.
- Keep the contrast headline of the batch-4 spec (section 3.5) and accept a modest paper.

## 7. What to return

A. The question you would have the paper ask, in one sentence, and its headline in two.
B. The mechanism that delivers it, stated in the model's objects, and the result type it yields
   (a theorem with its hypotheses, or a certified computation with what is certified).
C. Your judgment of the loudness pitch: keep, modify, or replace, with the referee's first
   objection and the answer. If modify, the modified statement. If replace, the replacement.
D. What of the current machinery survives as headline, what becomes a tool, what is dropped.
E. The minimal computation that decides whether the hump is present at the calibration under
   your proposal, in the objects of section 4, with what a sign or a magnitude would have to be.
F. Risks: the two things most likely to kill it, and whether either can be checked before the
   rewrite starts.
Take the time the problem needs. A smaller question fully answered beats a larger one with a gap.
