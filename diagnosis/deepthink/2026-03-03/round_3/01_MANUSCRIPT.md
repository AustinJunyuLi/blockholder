# Manuscript: draft_v3.tex

```latex
% =============================================================================
% draft_v3.tex
% =============================================================================
% Compilation (keeps the directory clean):
%   latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=0 draft.tex
%   latexmk -c draft.tex
%
% Manual compilation (then delete intermediates):
%   xelatex  draft
%   biber    draft
%   xelatex  draft
%   xelatex  draft
% =============================================================================

\documentclass[11pt]{article}

\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{setspace}
\usepackage{enumitem}
\usepackage{array}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{float}
\usepackage{tikz}
\usepackage[hidelinks]{hyperref}
\usepackage[backend=biber,style=authoryear,natbib=true,maxcitenames=2,maxbibnames=99]{biblatex}
\addbibresource{bibliography.bib}

\setstretch{1.1}

% Theorem environments
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newtheorem{definition}{Definition}

% Commands
\newcommand{\E}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\1}{\mathbf{1}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\R}{\mathbb{R}}

\title{\textbf{Liquidity, Activism Disclosure, and Takeover Premia:}\\[0.3em]
\large A Theory of Exit, Voice, and Corporate Control}
\author{Austin Li\\[0.25em]}
\date{}

\begin{document}
\maketitle


%==============================================================================
\begin{abstract}
\noindent How does secondary-market liquidity shape corporate control when an informed blockholder can choose between exit, quiet engagement, and public activism? I develop a takeover model in which a blockholder observes a private signal about firm value and selects among Exit, Hold, engagement below disclosure thresholds (Quiet Voice), and stake building with mandatory disclosure (Public Voice). A market maker prices from order flow and disclosure, and a potential bidder conditions entry on these market signals. In equilibrium, liquidity has a nonmonotone effect on expected minority takeover gains. Rising noise-trading intensity lowers adverse-selection costs but simultaneously erodes the informativeness of order flow, pushing bid incidence and engagement incentives in opposing directions. The result is a hump-shaped relationship: moderate liquidity uniquely maximizes minority gains. Furthermore, threshold-based disclosure attenuates this inference channel by shifting engagement from inferred to directly observable.
\end{abstract}

\newpage

%==============================================================================
\section{Introduction}
%==============================================================================

When an activist investor discovers underperformance at a portfolio company, she faces a consequential choice: sell her stake and move on, engage quietly behind the scenes, or accumulate shares aggressively enough to cross a regulatory disclosure threshold. Each path carries different risks and rewards, and each sends different signals to the market. How she resolves this dilemma shapes not only her own returns but whether a takeover bid emerges and what minority shareholders ultimately receive. This tension is the classic exit-versus-voice problem of \citet{Hirschman1970}, transplanted into financial markets. On one side, liquidity facilitates governance by letting activists accumulate stakes cheaply and reducing free-riding \citep{Maug1998}. On the other, liquidity makes selling painless, tempting blockholders to exit rather than bear the costs of engagement \citep{Coffee1991,Bhide1993}. The tension deepens once we recognize that prices are not passive scorekeepers: when takeover decisions depend on stock prices, trading has real effects through feedback channels \citep{BondEdmansGoldstein2012,EdmansGoldsteinJiang2012}. Consequently, the blockholder's choice between exit and voice reverberates beyond her portfolio into the real economy. No existing framework combines these three forces (endogenous governance choice, order-flow inference, and takeover feedback) in a single model.

To fill this gap, I develop a model in which a blockholder observes a private signal about firm value and chooses among four actions: Exit (sell her stake), Hold (retain without engaging), Quiet Voice (engage below the disclosure threshold), or Public Voice (buy additional shares, engage, and trigger mandatory disclosure). A competitive market maker sets prices from discrete order flow and the disclosure flag, while a potential bidder conditions entry on these market signals. Engagement raises standalone value and strengthens resistance to acquisition, increasing the premium a bidder must offer. The key modeling choice is that disclosure is stake-triggered: activism is directly observable only when the blockholder crosses a regulatory threshold, creating two distinct information regimes within a single equilibrium.

The model yields two main results. First, liquidity has a nonmonotone effect on expected minority takeover gains. At low liquidity, noise trading is scarce, making the blockholder's orders highly informative. The market maker largely infers her action, which deters quiet engagement and suppresses bids. As liquidity rises, noise camouflages the activist's trades, encouraging voice and improving bid incidence. However, at high liquidity, exit becomes so cheap that engagement incentives collapse entirely. The net effect is hump-shaped: minority shareholders benefit most at intermediate liquidity, where voice is both incentive-compatible and partially concealed. Second, stake-triggered disclosure attenuates this inference channel. Lowering the disclosure threshold shifts probability mass from Quiet Voice to Public Voice, compressing the activism premium into the observable regime and making it less sensitive to liquidity. The model predicts that the sensitivity of takeover premia to liquidity is lower in strict-disclosure jurisdictions.

These theoretical mechanisms speak directly to active policy debates. The United States Schedule 13D threshold at 5\% and the United Kingdom FCA threshold at 3\% create meaningfully different information environments. The framework provides a rigorous way to evaluate how such cross-country differences affect takeover outcomes and minority shareholder welfare, revealing that liquidity regulation operates implicitly as governance policy.

The model's predictions are motivated by well-documented empirical patterns. \citet{BravJiangPartnoyThomas2008} show that hedge fund activism often targets firms that subsequently receive acquisition offers. \citet{GreenwoodSchor2009} find that a substantial fraction of activist returns is attributable to takeover outcomes. The free-rider problem that \citet{GrossmanHart1980} identified in tender offers makes takeover premia the natural welfare object for dispersed minority shareholders, underscoring the importance of understanding how liquidity shapes these outcomes.

The paper proceeds as follows. Section~\ref{sec:lit} reviews the literature. Section~\ref{sec:model} presents the model, and Section~\ref{sec:equilibrium} characterizes the equilibrium. Section~\ref{sec:numerical} develops comparative statics with numerical analysis. Section~\ref{sec:testable} presents testable implications. Sections~\ref{sec:welfare} and~\ref{sec:extensions} analyze welfare and disclosure extensions. Section~\ref{sec:conclusion} concludes.
\section{Related Literature}
\label{sec:lit}
%==============================================================================

This paper connects three strands of the finance literature (blockholder governance, market microstructure, and corporate takeovers) and shows that their interaction produces equilibrium effects that no single strand generates alone.

%
\subsection{Exit vs.\ Voice in Corporate Governance}
%

The exit-voice trade-off originates with \citet{Hirschman1970}. Early applications treated the two as substitutes, arguing that liquidity weakens governance by allowing blockholders to flee rather than fight \citep{Coffee1991,Bhide1993}. \citet{Maug1998} reversed this logic, demonstrating that liquidity can facilitate voice by easing stake accumulation. \citet{Edmans2009} recast exit itself as a governance mechanism, showing that trading on bad private information punishes underperforming managers through equity-linked compensation. \citet{EdmansManso2011} extend this to multiple blockholders, while \citet{EdmansFangZur2013} provide empirical evidence that liquidity shifts blockholders toward exit and away from voice.\footnote{A common feature of these governance models is continuous trading. The present paper departs from that tradition by adopting discrete order flow, which keeps the inference problem tractable when integrating both disclosure regimes and price feedback.}

%
\subsection{Market Microstructure and Price Feedback}
%

Microstructure models explain how prices aggregate private information through trading \citep{Kyle1985,GlostenMilgrom1985}. I build on the tractable discrete order-flow framework of \citet{EdmansGoldsteinJiang2015}, which permits closed-form Bayesian updating and clear price fixed points. Financial prices also shape real economic decisions through feedback channels. \citet{EdmansGoldsteinJiang2012} demonstrate that stock prices affect takeover outcomes: low prices signal weak fundamentals and invite bids, while high prices deter them. \citet{BondEdmansGoldstein2012} survey this broader feedback literature.\footnote{\citet{DowGoldsteinGuembel2017} provide foundations for endogenous information production in settings where prices affect real investment.} None of these frameworks, however, allow an informed blockholder to choose between exit and voice before prices form.

%
\subsection{Shareholder Activism and Takeovers}
%

Empirical evidence firmly links activism to corporate control. \citet{BravJiangPartnoyThomas2008} document foundational stylized facts regarding activist target selection and subsequent acquisition offers. \citet{GreenwoodSchor2009} show that a substantial fraction of activist returns traces to these takeover outcomes. The canonical \citet{GrossmanHart1980} model establishes the free-rider problem that makes the takeover premium the relevant welfare metric for dispersed minority shareholders.\footnote{\citet{BackEtAl2018} embed an activist in a continuous-time Kyle model to study liquidity and efficiency, but they do not incorporate the feedback loop between order-flow inference and bidder entry conditional on disclosure.}

%
\subsection{Relation to This Paper}
%

The closest antecedent is \citet{EdmansGoldsteinJiang2015}, who develop a discrete order-flow model in which prices feed back into takeover decisions. That framework shares this paper's tractable Bayesian structure and price fixed points, but differs in three critical respects. First, the blockholder in \citet{EdmansGoldsteinJiang2015} has an exogenous information advantage and does not choose between alternative governance strategies; in this paper, the blockholder endogenously selects among Exit, Hold, Quiet Voice, and Public Voice, making the governance mode itself a strategic variable. Second, there is no disclosure regime: because the blockholder in \citet{EdmansGoldsteinJiang2015} does not acquire a stake, there is no threshold-crossing event that partitions the information environment. Here, stake-triggered disclosure splits equilibrium inference into disclosed and nondisclosed branches with sharply different informational content. Third, the absence of endogenous voice means \citet{EdmansGoldsteinJiang2015} cannot generate the nonmonotone relationship between liquidity and takeover premia or the disclosure-attenuation mechanism that constitutes this paper's central contribution.
%==============================================================================
\section{Model}
\label{sec:model}
%==============================================================================

The model has four stages that capture the blockholder's information advantage, the market's inference problem, and the bidder's response.

%
\subsection{Timeline}
%

Time is discrete, $t \in \{0, 1, 1.5, 2\}$.

\begin{enumerate}[leftmargin=2em]
\item[$t=0$:] Nature draws a standalone fundamental $v$. The blockholder observes a private signal $s$ about $v$.
\item[$t=1$:] The blockholder chooses an action $(q,a)$ from the feasible set $\{(-1,0),(0,0),(0,1),(+1,1)\}$, where $q \in \{-1,0,+1\}$ is the trade and $a \in \{0,1\}$ is engagement. A noise trader submits $z \in \{-1, 0, +1\}$. The market maker observes total order flow $X = q + z$ and disclosure indicator $D$, then sets a competitive price $P(X, D)$.
\item[$t=1.5$:] A potential bidder arrives with probability $\lambda_B \in (0,1)$, observes $(X,D)$ directly, and draws a private synergy shock $\xi$, then decides whether to initiate a takeover attempt.
\item[$t=2$:] Payoffs are realized: either the takeover is consummated at the offered price, or the firm remains standalone with (possibly) improved fundamentals due to engagement.
\end{enumerate}

\begin{figure}[H]
\centering
\begin{tikzpicture}[xscale=3.5, yscale=1.5]
    % Draw timeline line
    \draw[thick, ->] (0,0) -- (3.5,0);

    % Draw nodes
    \filldraw (0,0) circle (2pt);
    \filldraw (1,0) circle (2pt);
    \filldraw (2,0) circle (2pt);
    \filldraw (3,0) circle (2pt);

    % Draw time labels
    \node[above, font=\bfseries] at (0,0.2) {$t = 0$};
    \node[above, font=\bfseries] at (1,0.2) {$t = 1$};
    \node[above, font=\bfseries] at (2,0.2) {$t = 1.5$};
    \node[above, font=\bfseries] at (3,0.2) {$t = 2$};

    % Draw descriptions
    \node[below, align=center, text width=3cm] at (0,-0.2) {Nature draws $v$.\\Blockholder observes $s$.};
    \node[below, align=center, text width=3.5cm] at (1,-0.2) {Blockholder chooses $(q,a)$.\\Noise $z$ realized.\\Market maker observes $(X,D)$ and sets $P(X,D)$.};
    \node[below, align=center, text width=3.5cm] at (2,-0.2) {Bidder arrives, observes $(X,D)$ and synergy $\xi$.\\Bidder chooses entry.};
    \node[below, align=center, text width=3cm] at (3,-0.2) {Payoffs realized.\\Takeover settles or firm remains standalone.};
\end{tikzpicture}
\caption{Timeline of the model. The four stages capture the blockholder's information advantage, the market's inference problem, and the bidder's response.}
\label{fig:timeline}
\end{figure}

Table~\ref{tab:notation} in Appendix~\ref{app:notation} provides a quick reference for notation. The remainder of this section introduces each model component in turn, beginning with the blockholder's information environment and ending with the equilibrium concept.

%
\subsection{Fundamentals and Information}
%

The standalone fundamental is $v \sim \mathcal{N}(\mu, \sigma_v^2)$. The blockholder observes a private signal
\[
s = v + \varepsilon, \quad \varepsilon \sim \mathcal{N}(0, \sigma_\varepsilon^2),
\]
independent of $v$. Let $\sigma_s^2 \equiv \sigma_v^2 + \sigma_\varepsilon^2$. The blockholder's posterior mean is linear:
\[
\hat{v}(s) \equiv \E[v \mid s] = \mu + \beta(s - \mu), \quad \beta \equiv \frac{\sigma_v^2}{\sigma_v^2 + \sigma_\varepsilon^2} \in (0,1).
\]

The bidder draws an independent synergy shock from a Logistic distribution $\xi \sim \Lambda(0, s_\xi)$. This signal structure gives the blockholder a transient information advantage that she can exploit through trading, engagement, or both.

%
\subsection{Trading and Liquidity}
%

The blockholder has an initial stake of one share (normalization). Her order $q \in \{-1, 0, +1\}$ implies an end-of-$t=1$ holding of $h = 1 + q$ shares.

Noise trading is discrete:
\[
z \in \{-1, 0, 1\}, \quad \PP(z = 0) = 1 - \frac{2}{3}\kappa, \quad \PP(z = \pm 1) = \frac{\kappa}{3},
\]
where $\kappa \in (0, 1)$ indexes noise-trading intensity (market liquidity). Higher $\kappa$ means more frequent nonzero noise imbalance and therefore weaker inference from order flow.

Total order flow observed by the market maker is
\[
X = q + z \in \{-2, -1, 0, 1, 2\}.
\]

The blockholder's trading decision is intertwined with her engagement choice, to which I now turn.

%
\subsection{Disclosure Rule}
%

Let $D \in \{0, 1\}$ be a public indicator for whether a stake acquisition crosses a disclosure threshold. I model disclosure as \emph{stake-triggered}: in the discrete framework,
\[
D = 1 \quad \Longleftrightarrow \quad (q = +1).
\]
That is, \textbf{if the blockholder acquires an additional share, a threshold-crossing disclosure occurs}. This captures the institutional logic that crossing an ownership threshold triggers a regulatory filing (e.g., Schedule 13D), independent of whether the filing explicitly reflects intent. Below-threshold engagement remains hidden.

\paragraph{Timing of disclosure.} The disclosure indicator $D$ is determined simultaneously with the blockholder's action $(q, a)$ and is observed by the market maker at the same time as order flow $X$. Specifically, the sequence within $t=1$ is:
\begin{enumerate}[label=(\roman*),leftmargin=2em,itemsep=0pt]
\item The blockholder chooses $(q, a)$, which determines $D = \1\{q=+1\}$.
\item Noise trader submits $z$; total order flow $X = q + z$ is realized.
\item The market maker observes $(X, D)$ jointly and sets price $P(X, D)$.
\end{enumerate}
This timing ensures that disclosure does not reveal additional information beyond what is captured by $(X, D)$ jointly.

%
\subsection{Engagement Technology (Voice)}
\label{sec:engagement}
%

If the blockholder chooses engagement $a = 1$, she pays a private, signal-dependent cost $C(s) > 0$ at $t = 1$. This cost is observed by the blockholder when she observes $s$ but not by the market maker or bidder. I assume engagement costs are decreasing in the signal: a blockholder with more favorable private information finds it easier to build a compelling case for change. I parameterize the cost as
\[
C(s) = C_0 \exp\!\left(-\chi \frac{s - \mu}{\sigma_s}\right),
\]
where $C_0 > 0$ is the cost at the prior mean and $\chi \geq 0$ controls cost sensitivity to signal quality (Assumption~\textup{(A2)}). The assumption that engagement costs are decreasing in the signal reflects the economic mechanics of persuasion. A blockholder with more favorable private information about fundamentals finds it easier to build a compelling case for change. With a strong underlying asset, the activist can point to concrete operational improvements, favorable peer comparisons, or verifiable evidence of undervaluation, substantially lowering the friction of persuading the board or rallying fellow institutional shareholders. The exponential form is chosen for analytical convenience to ensure non-negativity, but the qualitative results require only strict positivity and a monotone decrease in $s$. This monotonicity assumption is economically substantive. If costs were instead increasing in $s$ (for example, because high-value firms feature entrenched managers who are harder to dislodge), the cutoff ordering would potentially invert, pushing the blockholder toward exit on good news and voice on bad news. The decreasing cost structure captures the standard paradigm where a strong fundamental thesis is required for a viable activist campaign.

This monotone, strictly positive specification ensures that neither engagement nor passivity is always optimal when the blockholder holds her initial stake, yielding an interior cutoff structure (Assumption~\textup{(A1)}).%
\footnote{Sufficient conditions for interior cutoffs include $C(\mu) < \delta(\tilde{\Delta} + (\tilde{m}-m_0))$ (engagement is worthwhile at the prior mean) and $\lim_{s\to-\infty} C(s) > \delta(\tilde{\Delta} + (\tilde{m}-m_0))$ (engagement is dominated for sufficiently low signals), together with the monotonicity of $C(s)$. I also assume that stake building (Public Voice) is not always dominated when engagement occurs, so that disclosure is triggered for sufficiently high signals. When $\chi > 0$, cost heterogeneity supports an interior Hold region; when $\chi = 0$, costs are constant and the equilibrium collapses to the two-cutoff case.}

Engagement succeeds with probability $\rho \in (0,1]$ and affects outcomes in two ways when successful:

\paragraph{Outside option improvement.} If engagement succeeds and no takeover is consummated, the standalone payoff is increased by $\Delta > 0$ at $t=2$. If engagement fails, standalone payoff remains $v$.

\paragraph{Bargaining/resistance premium.} If engagement succeeds and a takeover is consummated, the required premium increases from $m_0$ to $m_1$, where $m_1 > m_0 \geq 0$. The wedge captures bargaining power, defensive tactics, or any friction that raises the price needed to complete the acquisition when an engaged blockholder is present. Failed engagement yields the baseline premium $m_0$.
I interpret $m_0$ and $m_1$ as \emph{per-share takeover premia} above the market price (so the consummated offer satisfies $b=P+m$); they are distinct from $\hat{v}(s)$, the posterior mean of fundamentals.

\paragraph{Risk-neutral simplification.} Since success is unobserved before $t=2$ and all parties are risk-neutral, I define expected engagement effects:
\[
\tilde{\Delta} \equiv \rho \Delta, \qquad \tilde{m} \equiv m_0 + \rho(m_1 - m_0).
\]
Then engagement ($a=1$) yields expected standalone improvement $\tilde{\Delta}$ and expected premium wedge $\tilde{m}$. I assume the premium wedge satisfies $\tilde{m} > m_0$, which requires $\rho(m_1 - m_0) > 0$ (Assumption~\textup{(A3)}). This ensures that engagement has real consequences for takeover outcomes; an engaged blockholder can extract higher premia through an improved bargaining position or defensive tactics.

%
\subsection{Bidder Entry and Bidding Terms}
%

The bidder follows an entry rule conditional on the market's inference. A potential bidder arrives with exogenous Poisson probability $\lambda_B \in (0,1)$ at $t=1.5$. The bidder directly observes the public pair $(X,D)$ and a private synergy shock $\xi$, thus avoiding any reliance on price injectivity. On the disclosed branch $D=1$, disclosure pins down Public Voice and hence $a=1$, so $X$ reveals only the noise realization and carries no information about fundamentals (see Appendix~\ref{app:proof-disclosed-invariance}).

I assume that synergies and costs satisfy $\bar{S}-K > m_0-\mu$ and $\bar{S}-K < m_1+(\mu+3\sigma_v)$ (Assumption~\textup{(A4)}). These bounds ensure that takeover bids occur with interior probability. Crucially, successful engagement ($a=1$) strips away managerial entrenchment, forcing a competitive auction. This raises the expected fundamental synergy to $\bar{S} + \Delta_S$. Thus, activism \emph{fundamentally facilitates} the sale.

The bidder anchors their takeover offer to the target's expected standalone fundamental value, $\hat{V}(X,D) \equiv \E[v \mid X,D] + \tilde{\Delta}\pi(X,D)$, plus the \emph{inferred} premium wedge. Because the bidder does not perfectly observe $a$ when $D=0$, the payout is tied to the market's Bayesian expectation. The expected per-share offer required to consummate the acquisition is:
\[
b(X,D) = \hat{V}(X,D) + \bar{m}(X,D),
\]
where $\bar{m}(X,D) = m_0 + (\tilde{m}-m_0)\pi(X,D)$ is the expected premium wedge, and $\pi(X,D) = \PP(a=1 \mid X,D)$. By anchoring the offer to the fundamental standalone value rather than the fully updated secondary market price $P(X,D)$, the model mathematically prevents a pathological infinite recursion of pricing a premium-on-a-premium.

Conditional on arrival, the bidder's expected net deal surplus is:
\[
\Pi_B(X,D) = (\bar{S} + \pi(X,D)\Delta_S) + \xi - b(X,D) - K,
\]
where $K > 0$ is a fixed bidding cost. The conditional probability that an arriving bidder initiates a consummated takeover is:
\begin{equation}
\tilde{p}(X,D) \equiv 1 - \Lambda\left(\frac{\hat{V}(X,D) + \bar{m}(X,D) + K - (\bar{S} + \pi(X,D)\Delta_S)}{s_\xi}\right),
\label{eq:bid-prob}
\end{equation}
where $\Lambda(\cdot)$ is the standard logistic cumulative distribution function, reflecting a logistic synergy shock $\xi \sim \Lambda(0, s_\xi)$ (introduced below). The unconditional bid probability is $p(X,D) = \lambda_B \cdot \tilde{p}(X,D)$.

To ensure that the efficient pricing of the fundamental value run-up makes acquisitions more expensive on net despite synergy gains, I assume $\tilde{\Delta} + \tilde{m} - m_0 > \Delta_S$ (Assumption~\textup{(A5)}).

If the takeover is consummated, the \emph{realized} required premium is a function of the realized action, $m^{R}(a) \equiv m_0 + a\cdot(\tilde{m}-m_0)$, yielding a per-share offer of:
\[
b(X,D,a) = \hat{V}(X,D) + m^{R}(a).
\]

%
\subsection{Terminal Payoff and Price Formation}
%

Let $\delta = \exp(-r\tau)$ (approximately $1/(1+r)$ for short horizons) be the discount factor between the pricing/entry date and payoff/settlement at $t=2$, where $\tau$ is the time between these dates \citep{Cochrane2005,Duffie2010}.%
\footnote{If one measures payoffs in time-$1$ present-value units, $\delta$ can be set to one and later reintroduced by scaling. I keep $\delta$ explicit throughout.}

If no takeover is consummated, per-share terminal payoff is $y^{\text{stand}} = v + a\tilde{\Delta}$. If a takeover is consummated, per-share payoff is $y^{\text{M\&A}} = b(X,D,a) = \hat{V}(X,D) + m^{R}(a)$.

Therefore, the per-share terminal payoff is
\[
Y = \1\{\textup{bid}\} \cdot (\hat{V}(X,D) + m^{R}(a)) + (1 - \1\{\textup{bid}\}) \cdot (v + a\tilde{\Delta}),
\]
where $\1\{\textup{bid}\}$ denotes a \emph{consummated} takeover rather than a mere offer. Bargaining, board resistance, and regulatory frictions are captured in reduced form by the premium wedge $m^{R}(\cdot)$ and the fixed cost $K$.

Conditional on $(X,D)$, the expected takeover payout equals $\hat{V}(X,D)+\bar{m}(X,D)$.

The market maker is competitive and sets the stock price to the discounted expected terminal payoff:
\begin{equation}
P(X,D) = \delta \, \E[Y \mid X, D].
\label{eq:pricing}
\end{equation}

Because the bidder's entry condition~\eqref{eq:bid-prob} is cleanly anchored to the expected standalone fundamental value $\hat{V}(X,D)$ rather than the anticipatory market price $P(X,D)$, the bid probability is strictly independent of $P(X,D)$. This permanently resolves the pathological recursive pricing loop (the infinite geometric double-counting of expected premiums), guaranteeing unconditional existence and uniqueness of the pricing equation without requiring ad-hoc regularity bounds on price-to-entry feedback.

%
\subsection{Blockholder Payoff and Equilibrium Concept}
%

Conditional on signal $s$, the blockholder chooses $(q, a)$ to maximize expected present value. If she submits $q$ and ends with $h = 1 + q$ shares, her $t = 1$ value is
\[
U(q, a \mid s) = \E\Big[-q \cdot P(X,D) + \delta \cdot h \cdot Y - a \cdot C(s) \,\Big|\, s, q, a\Big],
\]
where $-qP(X,D)$ is the net cash flow from trading at $t = 1$ (selling $q = -1$ yields $+P$; buying $q = +1$ yields $-P$).

\begin{definition}[Perfect Bayesian Equilibrium]
A \emph{Perfect Bayesian Equilibrium} consists of:
\begin{enumerate}[label=(\roman{enumi})]
\item a blockholder strategy mapping $s$ into $(q, a)$,
\item beliefs $\pi(X,D) = \PP(a = 1 \mid X, D)$ consistent with Bayes' rule,
\item a bidder entry strategy satisfying~\eqref{eq:bid-prob}, and
\item a competitive price schedule $P(X,D)$ satisfying~\eqref{eq:pricing}.
\end{enumerate}
\end{definition}

Because noise trading $z$ has full support on $\{-1,0,+1\}$, every $(X,D)$ pair that is feasible under an on-path action occurs with positive probability. In particular, when $D=0$, $X\in\{-2,-1,0,1\}$; when $D=1$, only Public Voice is feasible so $X\in\{0,1,2\}$. Consequently, Bayes' rule pins down $\pi(X,D)$ for all reached information sets; off-path beliefs are irrelevant.%
\footnote{Throughout, I maintain Assumptions~\textup{(A1)}--\textup{(A6)} (the Standing Assumptions). These ensure interior action regions, nontrivial takeover outcomes, and well-behaved equilibrium existence. Because the pricing function resolves explicitly, equilibrium existence is guaranteed unconditionally via Brouwer's theorem (Proposition~\ref{prop:existence}), while uniqueness of the cutoff mapping is verified numerically following \citet{EdmansGoldsteinJiang2015}.}
%==============================================================================
\section{Equilibrium Characterization}
\label{sec:equilibrium}
%==============================================================================

%
\subsection{Threshold Structure with Three Cutoffs}
%

Before characterizing the equilibrium cutoffs, I formally establish that the blockholder will never optimally choose to accumulate shares without engaging. Let \textit{Quiet Accumulation} denote the action $QA \equiv (q=+1, a=0)$, which triggers mandatory disclosure ($D=1$).

\begin{lemma}[Domination of Passive Accumulation]
\label{lem:qa-domination}
Because the fundamental value improvement $\tilde{\Delta}$ is realized on $h=2$ shares, the expected marginal return to active engagement strictly exceeds the private cost $C(s)$ for any signal $s$ high enough to justify the capital cost of acquiring the second share. Therefore, $U(+1,1 \mid s) > U(+1,0 \mid s)$ for all relevant signals. In equilibrium, threshold-crossing ($D=1$) perfectly reveals engagement ($a=1$).
\end{lemma}
\textit{Proof.} See Appendix~\ref{app:proof-qa-domination}.

With passive accumulation ruled out, the blockholder's optimal active strategy has a natural ordering: she exits on bad news, holds passively on mildly negative news, engages quietly on moderate news, and goes public on good news. The next result makes this precise.

\begin{proposition}[Monotone Cutoff Structure]
\label{prop:cutoffs}
Under the Standing Assumptions, there exists a Perfect Bayesian Equilibrium in which the blockholder follows cutoff rules with (weakly) ordered thresholds $k_1 \leq k_0 \leq k_D$:
\[
(q, a) = \begin{cases}
(-1, 0) & s < k_1 \quad \text{(Exit)}, \\
(0, 0) & k_1 \leq s < k_0 \quad \text{(Hold)}, \\
(0, 1) & k_0 \leq s < k_D \quad \text{(Quiet Voice)}, \\
(+1, 1) & s \geq k_D \quad \text{(Public Voice)}.
\end{cases}
\]
The corresponding disclosure outcomes are: $D = 1$ if and only if $q = +1$ (Public Voice), and $D = 0$ otherwise.
\end{proposition}
\textit{Proof.} See Appendix~\ref{app:proof-cutoffs}.

\paragraph{Remark 1 (Collapse of the Hold Region).}
The existence of an interior Hold region ($k_1 < s < k_0$) requires the baseline engagement cost $C_0$ to be sufficiently large. The blockholder prefers passive retention over quiet engagement at marginal signals if and only if $C(s) > \delta \E_z[p(X,0)(\tilde{m}-m_0) + (1-p(X,0))\tilde{\Delta}]$. Because the unconditional bid probability $p$ is empirically small, the right-hand side is well approximated by $\delta \tilde{\Delta}$. If $C_0 \le \delta \tilde{\Delta}$, the expected return to active engagement strictly dominates passivity for all active signals, causing the Hold region to structurally collapse ($k_0 = k_1$). This is a parametric reality of the blockholder's cost function, not a structural flaw; as demonstrated in Section~\ref{sec:comp-statics}, higher baseline frictions cleanly restore the Hold region without altering the underlying order-flow inference mechanism or the nonmonotonicity of takeover gains.

The ordering reflects how the blockholder's incentives shift with her private signal. For very low signals, she holds unfavorable information about fundamentals and prefers to sell, monetizing her negative information before it reaches prices.

For somewhat better signals, fundamentals are not bad enough to warrant selling at a discount, but engagement is not yet worthwhile given its cost. The blockholder holds passively.

For intermediate signals, engagement improves expected value enough to justify the campaign cost $C(s)$, but stake building remains unattractive: buying additional shares costs more than the benefit of higher ownership. The blockholder engages quietly.

For the highest signals, buying additional shares allows the blockholder to internalize more of the engagement gains, and the discrete stake increase triggers public disclosure. This is the Public Voice region.

When engagement costs are constant (i.e., $\chi=0$), the Hold region may collapse, yielding a simpler two-cutoff structure with $k_0=k_1$. The analysis accommodates this case by allowing weak inequalities among cutoffs.

%
\subsection{Action Probabilities}
%

Given cutoffs $(k_1, k_0, k_D)$, define standardized cutoffs $\alpha_i \equiv (k_i - \mu)/\sigma_s$ for $i \in \{1, 0, D\}$. The unconditional action probabilities are:
\begin{align*}
\omega_E &\equiv \PP(s < k_1) = \Phi(\alpha_1), \\
\omega_H &\equiv \PP(k_1 \leq s < k_0) = \Phi(\alpha_0) - \Phi(\alpha_1), \\
\omega_Q &\equiv \PP(k_0 \leq s < k_D) = \Phi(\alpha_D) - \Phi(\alpha_0), \\
\omega_P &\equiv \PP(s \geq k_D) = 1 - \Phi(\alpha_D),
\end{align*}
corresponding to Exit, Hold, Quiet Voice, and Public Voice.

%
\subsection{Conditional Means of Fundamentals}
%

Let $\lambda_L(\alpha) \equiv \phi(\alpha)/\Phi(\alpha)$ and $\lambda_U(\alpha) \equiv \phi(\alpha)/(1-\Phi(\alpha))$ denote inverse Mills ratios. The conditional means of $v$ in each signal region are:
\begin{align*}
\mu_E &\equiv \E[v \mid s < k_1] = \mu - \beta\sigma_s \lambda_L(\alpha_1), \\
\mu_H &\equiv \E[v \mid k_1 \leq s < k_0] = \mu + \beta\sigma_s \frac{\phi(\alpha_1) - \phi(\alpha_0)}{\Phi(\alpha_0) - \Phi(\alpha_1)}, \\
\mu_Q &\equiv \E[v \mid k_0 \leq s < k_D] = \mu + \beta\sigma_s \frac{\phi(\alpha_0) - \phi(\alpha_D)}{\Phi(\alpha_D) - \Phi(\alpha_0)}, \\
\mu_P &\equiv \E[v \mid s \geq k_D] = \mu + \beta\sigma_s \lambda_U(\alpha_D).
\end{align*}

%
\subsection{Bayesian Posteriors}
%

Disclosure creates a sharp asymmetry in what the market can learn: when activism is disclosed, inference is trivial; when it is not, the market must extract engagement probabilities from noisy order flow. The next result characterizes the posterior beliefs that sustain equilibrium pricing.

\begin{proposition}[Posterior Engagement Probabilities]
\label{prop:posteriors}
For any information set $(X,D)$ that is reached with positive probability in equilibrium, the posterior probability of engagement $\pi(X,D) = \PP(a=1 \mid X, D)$ satisfies:
\begin{enumerate}[label=(\alph*)]
\item \textbf{Disclosed states:} If $D = 1$, then $\pi(X, 1) = 1$ for all compatible $X \in \{0, 1, 2\}$.
\item \textbf{Nondisclosed states:} If $D = 0$, let $p_0 \equiv 1 - \frac{2}{3}\kappa$ and $p_1 \equiv \frac{\kappa}{3}$. Then:
\begin{align*}
\pi(1, 0) &= \frac{\omega_Q}{\omega_H + \omega_Q}, \\
\pi(-1, 0) &= \frac{\omega_Q \, p_1}{(\omega_H + \omega_Q) \, p_1 + \omega_E \, p_0}, \\
\pi(0, 0) &= \frac{\omega_Q \, p_0}{(\omega_H + \omega_Q) \, p_0 + \omega_E \, p_1}, \\
\pi(-2, 0) &= 0.
\end{align*}
\end{enumerate}
\end{proposition}
\textit{Proof.} See Appendix~\ref{app:proof-posteriors}.

When $D=1$, the inference problem collapses entirely: disclosure reveals that the blockholder chose Public Voice, which implies engagement with certainty. The market knows activism has occurred, though the ultimate success of the campaign remains uncertain until $t=2$.

When $D=0$, the market faces a genuine inference problem. It observes only aggregate order flow $X$ and must form beliefs about whether the blockholder is engaged (Quiet Voice) or not (Exit or Hold). The key insight is that Hold and Quiet Voice both involve $q=0$, so they generate identical order-flow distributions; the market cannot distinguish between them from order flow alone. Instead, the posterior split between these actions is pinned down by their prior probabilities $(\omega_H,\omega_Q)$, which depend on the equilibrium cutoffs.

This is where liquidity enters the inference channel: higher $\kappa$ changes the noise distribution and thereby affects how order flow $X$ is interpreted. The posteriors $\pi(X,0)$ inherit this liquidity dependence, transmitting it to prices and takeover premia.

%
\subsection{Conditional Expectation of Fundamentals Given \texorpdfstring{$(X,D)$}{(X,D)}}
%

For pricing, we need $\E[v \mid X, D]$. Since $v$ is independent of noise $z$, only the action regions compatible with $(X, D)$ matter.

\paragraph{For $D=1$:} Only Public Voice is possible:
\[
\E[v \mid X, D=1] = \mu_P \quad \text{for } X \in \{0, 1, 2\}.
\]

\paragraph{For $D=0$:} Mix over Exit, Hold, and Quiet Voice with Bayesian weights. Let $p_0 \equiv 1 - \frac{2}{3}\kappa$ and $p_1 \equiv \frac{\kappa}{3}$. Then:
\begin{align*}
\E[v \mid -2, 0] &= \mu_E, \\
\E[v \mid 1, 0] &= \frac{\omega_H \mu_H + \omega_Q \mu_Q}{\omega_H + \omega_Q}, \\
\E[v \mid -1, 0] &= \frac{(\omega_H \mu_H + \omega_Q \mu_Q) \, p_1 + \omega_E \mu_E \, p_0}{(\omega_H + \omega_Q) \, p_1 + \omega_E \, p_0}, \\
\E[v \mid 0, 0] &= \frac{(\omega_H \mu_H + \omega_Q \mu_Q) \, p_0 + \omega_E \mu_E \, p_1}{(\omega_H + \omega_Q) \, p_0 + \omega_E \, p_1}.
\end{align*}

%
\subsection{Equilibrium Prices}
\label{sec:prices}
%

The competitive pricing condition~\eqref{eq:pricing} evaluates directly as a pure feed-forward expectation. Because the bid probability $p(X,D)$ relies on the fundamental standalone value rather than recursively on the market price, the equilibrium price is strictly determined by the market's Bayesian inference. For each information set $(X,D)$ and posterior $\pi(X,D)$, the unique equilibrium price explicitly satisfies:
\begin{equation}
P^*(X,D) = \delta\Big((1-p(X,D)) \cdot \hat{V}(X,D) + p(X,D) \cdot (\hat{V}(X,D) + \bar{m}(X,D))\Big),
\label{eq:price-fp-full}
\end{equation}
where $\hat{V}(X,D) \equiv \E[v \mid X,D] + \tilde{\Delta} \cdot \pi(X,D)$ is the expected standalone value, and $p(X,D) = \lambda_B \cdot \tilde{p}(X,D)$. This simplifies algebraically to:
\begin{equation}
P^*(X,D) = \delta \Big( \hat{V}(X,D) + p(X,D) \cdot \bar{m}(X,D) \Big).
\label{eq:price-fp}
\end{equation}
The price is exactly the expected standalone fundamental value plus the expected probability-weighted takeover premium. When takeover is unlikely ($p(X,D)\approx 0$), this reduces to $P^*(X,D)\approx \delta\,\hat{V}(X,D)$.

%
\subsection{Price Decomposition and Activism Premium}
%

Building on the feed-forward pricing equation~\eqref{eq:price-fp}, I decompose the equilibrium price into interpretable components. The decomposition isolates the channels through which blockholder engagement feeds into asset prices.

\begin{proposition}[Price Decomposition]
\label{prop:price-decomp}
The unique equilibrium price $P^*(X,D)$ satisfies
\[
P^*(X,D) = \delta\Big(\E[v \mid X,D] + \tilde{\Delta} \cdot \pi(X,D) + p(X,D) \cdot \bar{m}(X,D)\Big),
\]
where $p(X,D)$ is the unconditional bid probability, $\pi(X,D) = \PP(a=1 \mid X,D)$, and $\bar{m}(X,D) = m_0 + (\tilde{m} - m_0)\pi(X,D)$.

The terms involving $\pi(X,D)$ constitute an ``activism premium'':
\begin{itemize}[leftmargin=1.5em,itemsep=0pt]
\item \textbf{Standalone channel:} $\tilde{\Delta}\pi(X,D)$ reflects the fully capitalized unconditional expected value improvement from engagement.
\item \textbf{Takeover channel:} $p(X,D) \cdot (\tilde{m}-m_0)\pi(X,D)$ reflects the expected \emph{incremental} takeover premium attributable to the activist's bargaining friction (over and above the baseline $m_0$).
\end{itemize}
\end{proposition}
\textit{Proof.} See Appendix~\ref{app:proof-price-decomp}.

Activism affects prices through two distinct channels. The \emph{standalone channel} operates when no takeover occurs: an engaged blockholder improves firm value by $\tilde{\Delta}$ in expectation, and this improvement is capitalized into the share price.

The \emph{takeover channel} operates when a bid arrives: the bidder must pay a higher premium to acquire a firm with an engaged blockholder, and this higher premium is also reflected in the pre-bid price.

The way these channels operate differs sharply between disclosed and nondisclosed states. In disclosed states ($D=1$), engagement is known with certainty, so $\pi(X,1)=1$ and the activism premium is fully priced. Liquidity affects how often $D=1$ occurs and can influence prices through feedback, but it does not affect the activism premium \emph{within} disclosed states.

In nondisclosed states ($D=0$), the posterior $\pi(X,0)$ depends on $\kappa$ through Bayesian inference, so the activism premium inherits liquidity sensitivity. This asymmetry between disclosed and nondisclosed states is central to understanding how disclosure attenuates the liquidity--premia relationship.

%
\subsection{Bid Incidence and Premia}
%

The conditional bid probability $\tilde{p}(X,D)$ defined in~\eqref{eq:bid-prob} resolves the structural tension between sale facilitation and bid deterrence. Because $\Delta_S > 0$, an increase in inferred engagement strictly improves the core deal economics.

However, the bidder's required payout is anchored to the expected standalone value $\hat{V}(X,D)$, which increases by $\tilde{\Delta}$ for every unit of inferred engagement $\pi(X,D)$. Let $\Gamma(X,D)$ be the argument of the logistic CDF in~\eqref{eq:bid-prob}. Differentiating the entry threshold yields:
\[
\frac{\partial \tilde{p}(X,D)}{\partial \pi(X,D)} = - \Lambda'\left(\Gamma(X,D)\right) \frac{\tilde{\Delta} + (\tilde{m}-m_0) - \Delta_S}{s_\xi}.
\]
Because the capitalized fundamental improvement and premium wedge exceed the synergy gain ($\tilde{\Delta} + \tilde{m}-m_0 > \Delta_S$ under Assumption~\textup{(A5)}), higher inferred engagement strictly \emph{deters} bids ($\partial \tilde{p} / \partial \pi < 0$).

Crucially, this deterrence does not arise from frictional defensive tactics, but from \emph{efficient market pricing}. The market capitalizes the activist's fundamental improvement into the standalone value, and the bidder must pay for it. When $D=1$, the bidder \emph{knows} activism has occurred, so the required fundamental compensation is maximal. Consequently, publicly disclosed activist campaigns deter marginal takeover bids more strongly than inferred activism. (Proof: see Appendix~\ref{app:proof-bid-monotone}.)

%
\subsection{Equilibrium Cutoff Equations}
%

The equilibrium cutoffs $(k_1,k_0,k_D)$ are pinned down by indifference conditions at each boundary. Let $U_E$, $U_H(s)$, $U_Q(s)$, and $U_P(s)$ denote the expected payoffs from Exit, Hold, Quiet Voice, and Public Voice, computed by integrating over noise realizations and disclosure outcomes. (The exit payoff $U_E$ does not depend on $s$ because the sell order $q=-1$ fully liquidates the position, so the blockholder's terminal holding is zero.) The three cutoffs satisfy:
\begin{align}
U_E &= U_H(k_1), \label{eq:k1} \\
U_H(k_0) &= U_Q(k_0), \label{eq:k0} \\
U_Q(k_D) &= U_P(k_D). \label{eq:kD}
\end{align}

At $k_1$, the blockholder is indifferent between exiting and holding passively. At $k_0$, she is indifferent between Hold and Quiet Voice. At $k_D$, she is indifferent between Quiet Voice and Public Voice. These indifference conditions, combined with single-crossing of payoffs in the signal $s$, pin down the equilibrium strategy. (Derivation: see Appendix~\ref{app:proof-cutoff-eqns}.)

%
\subsection{Equilibrium Existence and Uniqueness}
%

Under Assumptions~\textup{(A1)}--\textup{(A6)}, any monotone-cutoff Perfect Bayesian Equilibrium must satisfy Bayes-consistent beliefs and the feed-forward pricing equation~\eqref{eq:price-fp} together with the cutoff indifference conditions~\eqref{eq:k1}--\eqref{eq:kD}.

\begin{proposition}[Existence of Monotone Equilibrium]
\label{prop:existence}
Under Assumptions~\textup{(A1)} through~\textup{(A6)}, there exists at least one monotone-cutoff Perfect Bayesian Equilibrium.
\end{proposition}
\textit{Proof.} See Appendix~\ref{app:proof-existence}.

The proof constructs the cutoff mapping $T:(k_1,k_0,k_D)\mapsto(k_1',k_0',k_D')$ and applies Brouwer's Fixed-Point Theorem. Since the pricing equation is fully feed-forward and avoids recursive singularities, the mapping is strictly continuous and existence follows unconditionally over the compact cutoff domain.

Assumption~\textup{(A6)} formally requires that the parameter space restricts the cutoff mapping $T$ to be a contraction on the feasible domain $\Theta$, guaranteeing a unique fixed point. Analytically bounding the spectral radius of the Jacobian of $T$ is intractable because the derivatives involve highly nonlinear interactions between inverse Mills ratios, the logistic CDF of the bidder's entry rule, and Bayesian posterior updating. Following the methodological precedent established for discrete order-flow feedback models \citep{EdmansGoldsteinJiang2015}, I verify this condition numerically: because the pathological recursive price loop has been structurally eradicated from the model, the strategic complementarity between cutoffs is organically bounded. In all numerical exercises presented in this paper, iterating $T$ from arbitrary starting points converges strictly to a unique fixed point, confirming the contraction mapping.

The analysis restricts attention to monotone-cutoff strategies, which are the standard equilibrium class in discrete-order-flow models with single-crossing payoffs \citep{EdmansGoldsteinJiang2015,EdmansGoldsteinJiang2012}. Single-crossing of the blockholder's payoff differences in $s$ (established in the proof of Proposition~\ref{prop:cutoffs}) implies that any best response to monotone beliefs is itself monotone, making the monotone-cutoff class self-confirming. Nonmonotone equilibria are not ruled out a~priori but would require nonstandard beliefs and fall outside the scope of this paper.

%
\subsection{Nonmonotonic Minority Takeover Gains}
%

I now turn to the paper's central object of interest: expected minority takeover gains. These gains capture what a passive shareholder can expect to earn from the takeover channel, and the model predicts that they respond nonmonotonically to market liquidity. Define
\begin{equation}
\Delta^{\min}(\kappa) \equiv \E\big[m^{R}(a) \cdot \1\{\textup{bid}\}\big],
\label{eq:minority}
\end{equation}
as the expected takeover premium (per share) earned by a representative minority share. The expectation is taken over $(v,s,z,\xi)$ induced by equilibrium strategies. This quantity captures the unconditional expected takeover premium from the takeover channel, averaged over all states of the world (including states in which no bid occurs).

Expected minority takeover gains decompose naturally into two components:
\begin{equation}
\Delta^{\min}(\kappa) = \underbrace{m_0 \cdot \PP(\textup{bid})}_{\text{baseline premium}} + \underbrace{(\tilde{m}-m_0)\cdot \E\big[\pi(X,D)\cdot \1\{\textup{bid}\}\big]}_{\text{activism-driven premium}}.
\label{eq:decomp}
\end{equation}
The first term is the baseline premium weighted by overall bid probability. The second term, which I denote $\Delta^{\textup{act}}(\kappa)$, captures the additional premium attributable to blockholder engagement. To avoid ambiguity, $\Delta$ (without superscript) denotes the engagement improvement parameter, while $\Delta^{\min}(\kappa)$ and $\Delta^{\textup{act}}(\kappa)$ are equilibrium objects defined above.

This decomposition separates the effect of liquidity on \emph{whether} a bid occurs from its effect on the \emph{size} of the premium conditional on bidding. (Derivation: see Appendix~\ref{app:proof-minority-decomp}.)

Two opposing channels drive the liquidity dependence. Higher liquidity can raise bid incidence by reducing adverse-selection costs and shifting prices, but it also changes equilibrium engagement incentives and the inference-driven component of premia. A full closed-form characterization of $\Delta^{\min}(\kappa)$ is generally unavailable because $\kappa$ affects equilibrium cutoffs and prices jointly. The following results establish nonmonotonicity from primitives, without relying on assumed boundary conditions.

\begin{lemma}[Endpoint Behavior of Minority Gains]
\label{lem:endpoints}
Let $\Delta^{\min}(\kappa)$ be the expected minority takeover gains. Under the Standing Assumptions, as $\kappa\uparrow 1$, $\Delta^{\textup{act}}(\kappa)\to 0$ and $\Delta^{\min}(\kappa)\to m_0\PP(\textup{bid})$. However, as $\kappa\downarrow 0$, $\Delta^{\textup{act}}(\kappa)$ remains strictly positive and is bounded below by a positive constant, though typically suppressed relative to its optimal interior value due to bid deterrence.
\end{lemma}
\textit{Proof.} See Appendix~\ref{app:proof-endpoints}.

\begin{proposition}[Nonmonotonic Liquidity Effect]
\label{prop:nonmonotone}
Under the Standing Assumptions, by Lemma~\ref{lem:endpoints}, $\Delta^{\min}(\kappa)$ attains its global minimum at the extreme high liquidity limit ($\kappa \uparrow 1$). Let $f(\pi) = \tilde{p}(\pi) \cdot (m_0 + \pi(\tilde{m}-m_0))$ represent the expected premium conditional on the market's inference $\pi$. If the baseline synergy $\bar{S}$ is sufficiently low such that the raw bid threshold $T(X,D)$ is strictly positive, $f(\pi)$ evaluates in the strictly concave region of the logistic probability function. By Jensen's inequality, the extreme dispersion of beliefs at $\kappa \to 0$ strictly minimizes the expected gains relative to intermediate liquidity levels. Therefore, there exists an interior maximizer $\kappa^{\dagger}\in(0,1)$ such that $\Delta^{\min}(\kappa^{\dagger})=\max_{\kappa\in[0,1]}\Delta^{\min}(\kappa)$, making the relationship strictly nonmonotone.
\end{proposition}
\textit{Proof.} See Appendix~\ref{app:proof-nonmonotone}.

\emph{Remark (Shape).} While the Weierstrass argument guarantees at least one interior peak, it does not strictly rule out multiple local maxima (such as a W-shape). Multiple peaks could theoretically arise if the Quiet Voice region exhibits a highly non-convex response to $\kappa$ due to complex price-feedback loops. However, the baseline calibration confirms a well-behaved, single-peaked hump shape (Figure~\ref{fig:nonmonotone} in Appendix~\ref{app:figures}), demonstrating that the fundamental economic trade-off between improving bid incidence and eroding inference dominates secondary nonlinearities.

The economic logic is as follows. At very low liquidity ($\kappa \to 0$), order flow is nearly perfectly revealing. The market infers the blockholder's action, fully pricing the expected engagement into the share price and deterring marginal takeover bids. Although the blockholder still benefits fundamentally from engagement, this bid deterrence suppresses the overall minority gains. At very high liquidity ($\kappa \to 1$), noise trading dominates, posteriors converge to the unconditional prior across all states, and prices flatten. The blockholder can no longer extract adverse-selection rents from informed trading, so the expected return to engagement falls below its private cost for all signal realizations. In this upper limit, $\Delta^{\textup{act}}(\kappa)\to 0$. Between these extremes, an interior $\kappa$ optimally balances the cover provided by noise traders with the survival of engagement incentives.

Between these extremes, an intermediate level of liquidity maximizes minority gains. The blockholder retains enough information advantage to profit from engagement, noise traders provide enough cover for informed trading, and the market's Bayesian inference sustains a meaningful activism premium. The turning point $\kappa^{\dagger}$ marks the liquidity level at which the marginal benefit of additional noise trading (higher bid incidence, better cover for informed orders) is exactly offset by the marginal cost (weaker inference, diluted engagement incentives).

Section~\ref{sec:numerical} complements this theory with numerical analysis. In the baseline calibration, $\Delta^{\min}(\kappa)$ is hump-shaped (Figure~\ref{fig:nonmonotone}) and the activism component varies smoothly with $\kappa$ (Figure~\ref{fig:decomposition}).

%
\paragraph{Disclosure Attenuation.}
%

The activism-driven component $\Delta^{\textup{act}}(\kappa)$ can be decomposed by disclosure status. In disclosed states ($D=1$), engagement is known with certainty, so the activism premium $\tilde{m}-m_0$ is constant and there is no inference channel. In nondisclosed states ($D=0$), engagement must be inferred from order flow, making the premium $\kappa$-sensitive through the Bayesian formulas in Proposition~\ref{prop:posteriors}.

This implies that the liquidity sensitivity of $\Delta^{\textup{act}}(\kappa)$ comes entirely from the $D=0$ component. Shifting probability mass toward disclosed activism (larger $\omega_P$) attenuates this inference-driven sensitivity, as more takeovers occur in states where engagement is observed rather than inferred. The following proposition formalizes this observation.

This result has direct policy implications: shifting more activism from hidden to observable (for example, by lowering disclosure thresholds) attenuates the sensitivity of takeover premia to market liquidity.

\begin{proposition}[Disclosure Attenuation (Partial Equilibrium)]
\label{prop:disclosure-attenuation}
Hold the blockholder's strategy constant: fix the cutoffs $(k_1,k_0,k_D)$ and hence the action probabilities, and vary $\kappa$ only through its effect on inference and pricing (a partial equilibrium exercise). Decompose the activism-driven premium as
\[
\Delta^{\textup{act}}(\kappa) = \underbrace{(\tilde{m}-m_0)\omega_P \cdot \bar{p}_1}_{\text{disclosed component}} + \underbrace{(\tilde{m}-m_0)\E\big[\pi(X,0)\cdot p(X,0) \mid D=0\big]\PP(D=0)}_{\text{inferred component}},
\]
where $\bar{p}_1 \equiv p(P^*(X,1),1)$ is the (constant) bid probability on the disclosed branch. Only the inferred component depends on $\kappa$ through the posteriors $\pi(X,0)$. Consequently, $|\partial \Delta^{\textup{act}}(\kappa)/\partial\kappa|$ is decreasing in $\omega_P$: shifting probability mass toward disclosed engagement attenuates the liquidity sensitivity of the activism-driven premium.
\end{proposition}

\textit{Proof sketch.} In disclosed states, $\pi(X,1)=1$ and all pricing objects are $\kappa$-invariant (Appendix~\ref{app:proof-disclosed-invariance}), so the disclosed component contributes zero to $\partial\Delta^{\textup{act}}/\partial\kappa$. The inferred component is a convex combination of $\kappa$-sensitive posteriors weighted by $\PP(D=0)=1-\omega_P$. As $\omega_P$ increases, weight shifts from the $\kappa$-sensitive component to the $\kappa$-invariant component, reducing the overall sensitivity. \hfill$\square$

\emph{Remark 2 (General Equilibrium).} Proposition~\ref{prop:disclosure-attenuation} isolates the partial-equilibrium transparency effect by holding the blockholder's strategy fixed. Altering the noise distribution $\kappa$ in general equilibrium inherently shifts the optimal cutoffs. However, as demonstrated numerically in Section~\ref{sec:numerical}, this attenuation intuition robustly survives full general equilibrium feedback provided the baseline parameterization supports a non-negligible incidence of Public Voice ($\omega_P \gg 0$), maintaining sufficient probability mass in the $\kappa$-invariant disclosed state.

%==============================================================================
\section{Comparative Statics and Numerical Analysis}
\label{sec:numerical}
\label{sec:comp-statics}
%==============================================================================

This section combines analytical comparative statics with numerical analysis. Table~\ref{tab:params} in Appendix~\ref{app:tables} summarizes the baseline parameterization; Table~\ref{tab:example} in Appendix~\ref{app:tables} reports equilibrium outcomes.

%
\subsection{Baseline Calibration and Equilibrium}
%

The structural parameters (summarized in Table~\ref{tab:params}) are calibrated to match the empirical realities of modern corporate governance and M\&A markets. The baseline takeover probability is scaled by a Poisson arrival rate of $\lambda_B = 0.20$, which, interacting with the logistic synergy dispersion ($s_\xi = 0.15$) and baseline fundamental synergies ($\bar{S} = 1.10$), strictly evaluates the target firm on the highly sensitive left tail of the entry threshold. This targets the unconditional annual M\&A bid rate of 2\% to 8\% observed in standard U.S. firm-year panels \citep{BettonEckboThorburn2008}, precluding the absurd base rates generated by unscaled frameworks. To capture the empirical reality that activists fundamentally force sales and dismantle entrenchment \citep{GreenwoodSchor2009}, successful engagement facilitates the sale by increasing expected synergy by $\Delta_S = 0.30$.

Despite this synergy facilitation, the model rigorously satisfies the net deterrence condition (Assumption A5): the combined capitalization of the standalone fundamental improvement ($\tilde{\Delta} = 0.225$) and the expected bargaining premium ($\tilde{m}-m_0 = 0.18$) strictly outpaces the synergy gain ($0.405 > 0.30$). Consequently, the marginal bidder faces a net reduction in deal surplus when acquiring a highly-priced, actively monitored firm. It is this perfectly rational price appreciation---not arbitrary defensive tactics---that cleanly deters the marginal bidder. Finally, the baseline engagement cost ($C_0 = 0.25$) is calibrated to exceed the expected fundamental improvement at the prior mean. This reflects the material frictions---legal fees, proxy solicitation, and illiquidity---that force blockholders with moderately positive signals to remain passive, safely reconstituting an interior \textit{Hold} region. Figure~\ref{fig:cutoff-structure} in Appendix~\ref{app:figures} depicts the resulting cutoff structure.

Three features of the equilibrium stand out:
\begin{itemize}[leftmargin=2em,itemsep=2pt]
\item \textbf{Disclosed states have maximal activism premium:} $\bar{m}(X,1) = \tilde{m}$ for all $X \in \{0,1,2\}$, since $D=1$ reveals $a=1$ with certainty.
\item \textbf{Nondisclosed states show inference:} The posterior $\pi(X,0)$ is highest when order flow is most diagnostic of the quiet-engagement action. With no stake acquisition in $D=0$ states, $X=1$ reveals $q=0$ and hence $\pi(1,0)=\omega_Q/(\omega_H+\omega_Q)$.
\item \textbf{Disclosure deters bids:} For fixed $X$, $p(X,1) < p(X,0)$ because the bidder knows it must pay the full activism premium when $D=1$.
\end{itemize}

Figure~\ref{fig:prices} plots equilibrium prices across all $(X,D)$ states. Conditional on disclosure ($D=1$), order flow reflects only noise given Public Voice, so $P(X,1)$ is constant across $X$. The disclosed price level exceeds comparable nondisclosed states because the market knows engagement has occurred rather than inferring it.

%
\subsection{Nonmonotonicity and Decomposition}
%

Figure~\ref{fig:nonmonotone} displays the central result: a nonmonotone relation between liquidity and expected minority takeover gains. As $\kappa$ rises from low levels, $\Delta^{\min}(\kappa)$ initially increases because bid incidence grows. At higher liquidity, activism-related premia contribute less, and $\Delta^{\min}(\kappa)$ declines. The vertical dashed line marks the interior turning point $\kappa^{\dagger}$.

Figure~\ref{fig:decomposition} decomposes these gains into the baseline component $m_0 \cdot \PP(\textup{bid})$ and the activism component $\Delta^{\textup{act}}(\kappa)$. Both components vary smoothly with liquidity, and the hump shape arises from the interaction between bid incidence and the weight placed on activism-related premia.

Figure~\ref{fig:cutoffs-kappa} traces how equilibrium cutoffs shift with liquidity. The ordering $k_1 \le k_0 \le k_D$ is preserved throughout, though regions can collapse (e.g., $k_0=k_1$).

%
\subsection{Activism Frictions}
%

\paragraph{Sensitivity to engagement frictions.}
The model's general equilibrium structure precludes simple closed forms, but analytical results pin down the direction of effects within each regime. Higher engagement costs shrink the voice regions; larger expected engagement benefits and takeover premia expand them.

Figures~\ref{fig:sensitivity-C0} and~\ref{fig:sensitivity-wedge} confirm robustness to key parameters.

\textbf{Engagement cost $C_0$.} Raising $C_0$ shrinks the voice regions and lowers $\Delta^{\textup{act}}$, but it can raise bid incidence by reducing expected resistance. The net effect on $\Delta^{\min}$ is therefore ambiguous, and the turning point in $\kappa$ shifts across cost levels.

\textbf{Premium wedge $(m_1 - m_0)$.} Increasing the wedge raises the takeover premium conditional on bidding but can deter bids. In the calibration, expected minority takeover gains peak at an intermediate wedge.

%
\subsection{Liquidity Effects}
%

How does liquidity affect the market's inference about activism? Holding the blockholder's strategy fixed, the within-regime effects are as follows. Fix the equilibrium cutoffs $(k_1,k_0,k_D)$ and hence the action probabilities $(\omega_E,\omega_H,\omega_Q,\omega_P)$. The posteriors in Proposition~\ref{prop:posteriors} satisfy:
\begin{enumerate}[label=\textup{(\alph*)},leftmargin=2em]
\item In nondisclosed states, $\partial \pi(1,0)/\partial \kappa = 0$ and $\partial \pi(-1,0)/\partial \kappa \ge 0$;
\item $\partial \pi(0,0)/\partial \kappa \le 0$;
\item $\pi(-2,0)=0$; in disclosed states, $\pi(X,1)=1$ for all feasible $X$.
\end{enumerate}
Consequently, the inferred premium wedge $\bar{m}(X,0)=m_0+(\tilde{m}-m_0)\pi(X,0)$ is increasing in $\kappa$ for $X=-1$, decreasing in $\kappa$ for $X=0$, and invariant for $X=1$, while disclosed states have $\bar{m}(X,1)=\tilde{m}$. (Proof: see Appendix~\ref{app:proof-cs-liquidity-within}.)

The intuition runs as follows. At $X=1$, the buy order fully reveals that the blockholder did not sell, pinning down the posterior regardless of $\kappa$. At $X=-1$, higher liquidity makes a sell by the noise trader more likely, so the market revises upward the probability that the blockholder engaged quietly rather than exited. At $X=0$, the opposite logic applies: higher liquidity makes the zero-order-flow event more likely under exit, reducing the inferred engagement probability.

\paragraph{Across-equilibrium liquidity effects.}
Beyond these within-regime inference effects, changing liquidity also shifts the blockholder's incentives through adverse selection and moves equilibrium cutoffs and prices jointly. Because these objects adjust endogenously with $\kappa$, the full cross-equilibrium patterns are characterized in Figure~\ref{fig:cutoffs-kappa}.

In disclosed states ($D=1$), $\pi(X,1)=1$ and $\bar{m}(X,1)=\tilde{m}$, so liquidity has no inference content conditional on disclosure. In nondisclosed states ($D=0$), $\pi(X,0)$ varies with $\kappa$ through the Bayesian updating formulas in Proposition~\ref{prop:posteriors}, making the $D=0$ component of $\Delta^{\textup{act}}(\kappa)$ liquidity-sensitive. This asymmetry between disclosed and nondisclosed states drives the model's core predictions.

Figure~\ref{fig:disclosure} isolates the disclosure-inference channel. I fix the blockholder's cutoff strategy at the baseline equilibrium ($\kappa=0.5$) and vary liquidity $\kappa$ only through the noise distribution in order flow, then compare the resulting $\Delta^{\textup{act}}(\kappa)$ under threshold disclosure to a counterfactual without disclosure. Removing disclosure amplifies the role of inference and makes $\Delta^{\textup{act}}(\kappa)$ more sensitive to $\kappa$; threshold disclosure attenuates this sensitivity by shifting probability mass toward states with observed engagement ($D=1$).

%
\subsection{Takeover Environment}
%

How do the takeover environment parameters shape bid incidence? Fix any reached information set $(X,D)$ and treat the inferred premium wedge $\bar{m}(X,D)$ as given. The unconditional bid probability function $p(X,D)$ defined in~\eqref{eq:bid-prob} satisfies:
\begin{enumerate}[label=\textup{(\alph*)},leftmargin=2em]
\item \textbf{(Synergies)} $\partial p(X,D) / \partial \bar{S} > 0$: higher synergies increase bid incidence uniformly.
\item \textbf{(Entry cost)} $\partial p(X,D) / \partial K < 0$: higher bidding costs reduce bid incidence uniformly.
\end{enumerate}
Because the bid probability is anchored to the fundamental standalone value $\hat{V}(X,D)$ rather than the anticipatory market price $P(X,D)$, the price-to-entry feedback loop is structurally eliminated. The logistic synergy distribution with scale parameter $s_\xi$ governs the dispersion of bidder valuations; larger $s_\xi$ increases overall bid heterogeneity without affecting the feed-forward pricing structure.

(Proof: see Appendix~\ref{app:proof-cs-takeover}.)

%
\subsection{Additional Sensitivity Analysis}
%

I extend the sensitivity analysis to three additional structural parameters: the engagement success probability $\rho$, the bidder synergy scale $s_\xi$, and the discount factor $\delta$.

First, I analyze the sensitivity to the engagement success probability $\rho \in \{0.5, 0.7, 0.9\}$ (Figure~\ref{fig:sensitivity-rho}). The baseline calibration utilizes $\rho = 0.9$, which is economically defensible because it represents the success rate conditional on the blockholder choosing to engage. An activist who selectively engages only when her private signal is highly favorable should plausibly succeed at a high rate. Nevertheless, lowering $\rho$ mechanically shrinks the expected standalone improvement $\tilde{\Delta}$ and the expected takeover premium wedge $\tilde{m} - m_0$. As $\rho$ falls, the hump-shaped curve of $\Delta^{\min}(\kappa)$ flattens significantly, reflecting the diminished payoff to both quiet and public engagement, without altering its qualitative shape. The vertical scale of the nonmonotonicity compresses, but the peak persists.

Second, I vary the bidder synergy scale $s_\xi \in \{0.10, 0.15, 0.25\}$ (Figure~\ref{fig:sensitivity-sigma-xi}). The parameter $s_\xi$ governs the dispersion of the bidder's private logistic synergy shock. Higher $s_\xi$ increases average bid incidence because the right tail of bidder valuations grows. The numerical sweeps show that while higher $s_\xi$ shifts the entire $\Delta^{\min}(\kappa)$ curve upward (due to a higher baseline bid probability), the hump shape generated by the order-flow inference channel remains robust.

Finally, I test the sensitivity to the discount factor $\delta \in \{0.85, 0.90, 0.95\}$ (Figure~\ref{fig:sensitivity-delta}). Lowering $\delta$ mechanically reduces equilibrium prices through the feed-forward pricing equation $P = \delta[\hat{V} + p \cdot \bar{m}]$, which in turn increases bid incidence as the bidder faces lower acquisition costs. Although lower $\delta$ simultaneously weakens the blockholder's incentive to bear the upfront engagement cost $C_0$, the bid-probability channel dominates: expected minority gains shift upward as $\delta$ falls. Moreover, the hump shape progressively flattens, because the inference channel matters less when bids are already likely.

%==============================================================================
\section{Testable Implications}
\label{sec:testable}
\label{sec:testable_implications}
%==============================================================================

The model generates several predictions regarding how liquidity, disclosure regimes, and takeover premia interact. Testing these structural predictions empirically requires navigating the extreme zero-inflation characteristic of unconditional takeover gains. To avoid Type II errors common to causal quasi-experiments on zero-inflated panels, the empirical strategy must isolate the extensive and intensive margins directly, utilizing highly powered tests of curvature.

\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{The Unconditional Hump Test.} The core structural prediction is that extreme illiquidity strictly suppresses bids via efficient pricing, while extreme liquidity destroys the engagement incentive, yielding a nonmonotone maximum for minority gains (Proposition~\ref{prop:nonmonotone}).
    \emph{Prediction:} The relationship between market liquidity and unconditional expected minority takeover gains is characterized by an inverted-U shape.
    \emph{Empirical strategy:} Estimate a quadratic specification of $Y_{i,t} = \text{Premium}_{i,t} \times \1\{\text{Bid}_{i,t}=1\}$ on $L_{i,t}$ and $L_{i,t}^2$ (where $Y=0$ for non-targets), controlling for institutional ownership to separate active noise from passive indexing. Formally test for the inverted-U using the exact \citet{LindMehlum2010} joint slope test. To address nonparametric functional-form concerns, this curvature can be cross-validated using Double Machine Learning (DML).

    \item \textbf{The Reduced-Form Decomposition.} The model proves the unconditional hump originates from two competing forces: rising liquidity facilitates fundamental bid incidence, but erodes the intensive-margin premium via inference compression (Equation~\ref{eq:decomp}).
    \emph{Prediction:} The extensive margin (bid incidence) increases with liquidity until deterrence binds, while the intensive margin (conditional premium) systematically declines as order flow loses informativeness.
    \emph{Empirical strategy:} Decompose the effect. First, estimate a Probit model on the hazard rate of receiving an M\&A bid to capture the extensive margin. Second, estimate an OLS regression purely on the conditional premium for completed deals to confirm the intensive margin does not mechanically offset the unconditional pattern.

    \item \textbf{Mechanism Validation via Observability Interaction.} The inference channel strictly operates in the nondisclosed state ($D=0$). Shifting probability mass from inferred to observable states inherently attenuates the sensitivity of the premium to liquidity (Proposition~\ref{prop:disclosure-attenuation}).
    \emph{Prediction:} Higher public observability of the target firm attenuates the curvature of the liquidity-premia hump.
    \emph{Empirical strategy:} Interact the quadratic liquidity terms with continuous proxies for the target's information environment (e.g., analyst coverage, index inclusion). The model predicts that for highly covered firms, the quadratic coefficient on $L^2$ will pull significantly toward zero, mathematically flattening the hump because engagement is priced directly rather than inferred from noisy order flow.

    \item \textbf{Micro-Validation via 13D Event Studies.} The discrete price jump upon a Schedule 13D filing ($D=1 \implies \pi=1$) directly measures the gap between the market's pre-filing inference $\pi(X,0)$ and certainty.
    \emph{Prediction:} 13D cumulative abnormal returns (CARs) are strictly larger for highly liquid stocks.
    \emph{Empirical strategy:} Regress target CARs around Schedule 13D filings on pre-event Amihud illiquidity. In highly liquid stocks (high $\kappa$), noise effectively masks the activist's accumulation, meaning the pre-filing inferred probability is low ($\pi \approx 0$). The regulatory filing is thus a massive informational shock, yielding a large CAR. Conversely, in illiquid stocks, order flow is highly informative, inference occurs early, and the filing day surprise is minimal.
\end{enumerate}

%==============================================================================
\section{Welfare Analysis}
\label{sec:welfare}
%==============================================================================

The analysis thus far has focused on expected minority takeover gains, $\Delta^{\min}(\kappa)$, which represent the natural welfare object for dispersed shareholders facing a free-rider problem. A broader perspective requires analyzing total economic surplus. Define the welfare components as follows: minority welfare $W_{\text{min}}(\kappa) = \Delta^{\min}(\kappa)$; blockholder welfare $W_B(\kappa) = \E[U(q^*, a^* \mid s)]$; bidder welfare $W_{\text{bid}}(\kappa) = \E[\max(\Pi_B, 0)]$; and total surplus $W(\kappa) = W_{\text{min}} + W_B + W_{\text{bid}}$.

In the event of a takeover, the expected standalone value $\hat{V}(X,D)$ and the premium wedge $m^{R}(a)$ act as pure transfers from the bidder to the target shareholders. Consequently, these pricing terms cancel out in the aggregate. Expected total surplus simplifies to the realized synergies and standalone improvements, net of costs:
\begin{equation}
W(\kappa) = \E\Bigl[ \1\{\text{bid}\} (\bar{S} + \xi - K - v - a\tilde{\Delta}) + v + a\tilde{\Delta} - a C(s) \Bigr].
\end{equation}

An important theoretical question is whether the nonmonotonicity of minority gains is merely a distributional artifact or a feature of total surplus. Because extreme liquidity ($\kappa \to 1$) destroys the blockholder's engagement incentive, fundamental value creation collapses. Total surplus therefore tightly tracks the total probability of engagement. Consequently, the nonmonotonicity result extends to total welfare: $W(\kappa)$ is inherently hump-shaped (Figure~\ref{fig:welfare}).

However, if a social planner seeks to maximize total surplus, the socially optimal liquidity level $\kappa^*$ will generally differ from the minority-optimal level $\kappa^\dagger$. As liquidity $\kappa$ increases, lower average pre-bid prices reduce the bidder's acquisition cost, strictly improving bidder surplus $W_{\text{bid}}(\kappa)$ and stimulating bid incidence. The minority-optimal level $\kappa^\dagger$ maximizes the extraction of surplus from the bidder to minority shareholders by sustaining a high inferred activism premium. Because this extraction deters marginal, socially efficient takeovers, policies designed purely for minority protection may conflict with aggregate M\&A efficiency.

%==============================================================================
\section{Extensions}
\label{sec:extensions}
%==============================================================================

Disclosure requirements for activist investors vary widely across jurisdictions, creating natural laboratories for testing the model's predictions. I consider three benchmarks that span the policy spectrum.

In the United States, Schedule~13D mandates filing within five business days of crossing a 5\% beneficial ownership threshold. The United Kingdom imposes a lower 3\% threshold with a tighter two-trading-day deadline under the FCA's Disclosure and Transparency Rules. The European Union's Transparency Directive sets a 5\% baseline but permits member states to adopt lower thresholds; Germany, for instance, applies 3\% for voting-rights notifications. At one extreme, very low thresholds approach full disclosure of activist intent; at the other, weak enforcement or broad institutional exemptions leave much activism unobserved.

Throughout this section, I hold the blockholder's cutoff strategy fixed, and hence the action probabilities $\omega_E,\omega_H,\omega_Q,\omega_P$, to isolate the effect of the disclosure regime on inference and pricing.

%
\subsection{Full Disclosure Benchmark}
%

Some jurisdictions have considered or implemented very low disclosure thresholds (such as proposals to reduce the US Schedule~13D threshold from 5\% to 2.5\%) or require disclosure of activist intent regardless of stake size. In the limit, such regimes approach full disclosure.

Under full disclosure, the market observes the blockholder's action $(q,a)$ directly. The engagement posterior is trivial: $\pi=1$ when $a=1$ and $\pi=0$ when $a=0$. The activism premium is deterministic in each state, and the inference channel that links liquidity to premia shuts down completely. Order flow reveals only the noise-trader realization $z$, which is uninformative about fundamentals. This benchmark marks the upper bound on how much disclosure can attenuate the liquidity-sensitivity of the activism premium.

%
\subsection{No Disclosure Benchmark}
%

At the other extreme, some jurisdictions have high thresholds, weak enforcement, or broad exemptions that leave much activism unobserved. The no-disclosure benchmark captures this limiting case: the market receives no disclosure signal and must infer everything from order flow alone.

Under no disclosure, the market conditions only on aggregate order flow $X\in\{-2,-1,0,1,2\}$. Only the extreme realizations pin down engagement with certainty: $X=-2$ arises only from Exit ($\pi=0$), while $X=2$ arises only from Public Voice ($\pi=1$). At intermediate values of $X$, the market mixes over all four actions with weights that depend on the noise distribution and hence on $\kappa$. Compared to the baseline, this regime makes the activism premium more liquidity-sensitive because inference operates across all states rather than being confined to nondisclosed states. This benchmark marks the lower bound on how much disclosure can attenuate the inference channel.

%
\subsection{An Intermediate Regime: Stake Disclosure Plus Noisy Rumors}
\label{sec:noisy_rumors}
%

Between the polar benchmarks of full disclosure and no disclosure lies a realistic intermediate case: baseline stake-triggered disclosure augmented by a noisy public signal about quiet engagement. This regime captures modern information environments, such as the United Kingdom, where a lower 3\% threshold is augmented by active financial media \citep{FangPeress2009}, or markets where analyst coverage, Bloomberg terminal leaks, and quarterly 13F filings offer noisy, delayed signals about activist positions. Furthermore, the rumor structure serves as a tractable proxy for wolf pack activism, where information leaks through a network of secondary blockholders.

To formalize this, I augment the baseline model with a binary public rumor signal $R \in \{0,1\}$ that fires in nondisclosed states ($D=0$). If the blockholder engages ($a=1$), the rumor fires with true-positive probability $\eta_1$. If she does not engage ($a=0$), the rumor fires with false-positive probability $\eta_0$, where $\eta_0 < \eta_1$. In disclosed states ($D=1$), the rumor is irrelevant because engagement is already known.

Applying Bayes' rule, the updated posterior in the nondisclosed state becomes:
\begin{equation}
\pi(X,0,R) = \frac{\omega_Q \PP(X|q=0) \PP(R|a=1)}{\omega_E \PP(X|q=-1)\PP(R|a=0) + \PP(X|q=0)(\omega_H \PP(R|a=0) + \omega_Q \PP(R|a=1))}.
\end{equation}
When the rumor fires ($R=1$), the market updates toward engagement; when it remains silent ($R=0$), the market updates away.

Numerical analysis of this regime (Figure~\ref{fig:noisy-rumor-precision}) reveals that as the rumor becomes more precise (i.e., as $\eta_1 - \eta_0$ increases), the $\Delta^{\min}(\kappa)$ curve systematically flattens. Comparing a baseline model ($\eta_1 = \eta_0$), a moderate rumor regime ($\eta_1 = 0.75, \eta_0 = 0.25$), and a highly precise regime ($\eta_1 = 0.95, \eta_0 = 0.05$), the activism premium becomes progressively less sensitive to liquidity. In the limit as $\eta_1 \to 1$ and $\eta_0 \to 0$, the regime converges to the full-disclosure benchmark within nondisclosed states. This confirms the robustness of the core theoretical mechanism: any friction or institutional feature that shifts engagement from inferred to observable intrinsically attenuates the sensitivity of takeover premia to secondary market liquidity. Appendix~\ref{app:extensions-derivations} provides the posterior formulas for general $(\eta_0,\eta_1)$, and Table~\ref{tab:disclosure-extensions} in Appendix~\ref{app:tables} reports a numerical comparison.

%
\subsection{General Equilibrium Disclosure Effects}
\label{sec:ge_disclosure}
%

Proposition~\ref{prop:disclosure-attenuation} established a partial-equilibrium result: holding the blockholder's strategy fixed, stricter disclosure attenuates the liquidity sensitivity of premia by increasing transparency. However, in general equilibrium, altering the regulatory disclosure threshold fundamentally changes the blockholder's incentive to engage in the first place.

\begin{proposition}[General Equilibrium Disclosure Trade-off]
\label{prop:ge-disclosure}
Let $\tau$ parameterize the strictness of the disclosure regime. The total derivative of the activism-driven premium with respect to disclosure strictness can be conceptually decomposed as:\footnote{This decomposition serves as an intuitive heuristic for the economic logic. Formally, $\Delta^{\textup{act}}$ is a highly nonlinear function of all individual region probabilities ($\omega_E$, $\omega_H$, $\omega_Q$, $\omega_P$), and shifting mass between distinct regions entails asymmetric effects on the Bayesian posteriors that require a full multivariate application of the chain rule.}
\begin{equation}
\frac{d \Delta^{\textup{act}}}{d \tau} \approx \underbrace{\frac{\partial \Delta^{\textup{act}}}{\partial \tau}}_{\text{Transparency Effect}} + \underbrace{\frac{\partial \Delta^{\textup{act}}}{\partial (\omega_Q + \omega_P)} \frac{d (\omega_Q + \omega_P)}{d \tau}}_{\text{Deterrence Effect}}.
\end{equation}
The transparency effect is strictly positive: shifting mass to observable states ($D=1$) removes the inference discount. The deterrence effect is strictly negative: stricter thresholds force early disclosure, which maximizes bid deterrence, reduces the expected return to quiet engagement, and shrinks the total probability of activism.
\end{proposition}

The net welfare impact on minority shareholders is therefore ambiguous and depends on primitives. Under sufficient conditions where engagement costs $C_0$ are low and liquidity $\kappa$ is moderate, the blockholder's constraint is slack. The transparency effect dominates, and strict disclosure unambiguously aids minority shareholders. Conversely, if $C_0$ is high, the blockholder is at the margin of indifference. Imposing strict disclosure destroys the Quiet Voice region without proportionally expanding Public Voice. In this regime, the deterrence effect dominates, and strict disclosure paradoxically harms minority shareholders by deterring the very activism that generates takeover premia.

\section{Conclusion}
\label{sec:conclusion}
%==============================================================================

This paper develops a unified theoretical framework demonstrating that secondary-market liquidity, activism disclosure, and takeover premia are jointly determined in equilibrium. By embedding an informed blockholder's choice between Exit, Quiet Voice, and Public Voice into a setting with order-flow inference and takeover feedback, the model isolates a novel pricing mechanism: an activism premium that is either directly observed through regulatory disclosure or inferred by a competitive market maker. The central finding is that liquidity exerts a nonmonotone, hump-shaped effect on expected minority takeover gains. Rising noise-trading intensity lowers adverse-selection costs and spurs bid incidence, but simultaneously erodes the informativeness of order flow, dampening the inference channel that sustains engagement incentives. Moderate liquidity strikes the optimal balance for minority shareholders.

The analysis provides several distinct, testable implications. Most notably, threshold-based disclosure policy acts as an implicit governor on the liquidity-premia relationship. Lowering the disclosure threshold increases the share of activism that is directly observable, thereby attenuating the inference channel. Consequently, the model predicts that the sensitivity of takeover premia to market liquidity is structurally lower in strict-disclosure jurisdictions (such as the United Kingdom) than in permissive jurisdictions (such as the United States). The model further highlights a critical general equilibrium trade-off for policymakers: while stricter thresholds increase market transparency, they simultaneously reduce the expected returns to quiet engagement, potentially deterring activism altogether. Furthermore, the welfare analysis reveals that policies protecting minority shareholders by targeting optimal liquidity may diverge from the objective of maximizing total social surplus.

Extending the framework to dynamic settings with multiple trading rounds would capture the gradual position-building that characterizes real-world activist campaigns. Introducing multiple blockholders or endogenous information acquisition would illuminate how collective action and rumor networks, such as the wolf pack dynamics explored in Section~\ref{sec:noisy_rumors}, reshape the inference channel. Each of these extensions preserves the core insight developed here: liquidity, disclosure, and corporate governance are inextricably linked, and evaluating any one requires a framework that internalizes their joint equilibrium feedback.

%==============================================================================
\newpage
\printbibliography

%==============================================================================
\newpage
\appendix

%==============================================================================
\section{Notation}
\label{app:notation}
%==============================================================================

\begin{table}[H]
\centering
\footnotesize
{\renewcommand{\arraystretch}{0.92}
\begin{tabular}{@{}>{$}l<{$} p{0.73\linewidth}@{}}
\toprule
\text{Symbol} & \text{Meaning} \\
\midrule
\multicolumn{2}{@{}l}{\textbf{Fundamentals and information}} \\
v & Standalone fundamental at $t=0$, $v \sim \mathcal{N}(\mu,\sigma_v^2)$. \\
s & Blockholder signal, $s=v+\varepsilon$, $\varepsilon \sim \mathcal{N}(0,\sigma_\varepsilon^2)$. \\
\mu,\sigma_v^2,\sigma_\varepsilon^2,\sigma_s^2 & Prior mean/variances; $\sigma_s^2 \equiv \sigma_v^2 + \sigma_\varepsilon^2$. \\
\beta & Posterior weight in $\hat{v}(s)=\E[v \mid s]=\mu+\beta(s-\mu)$; $\beta \equiv \sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)$. \\
\hat{v}(s) & Blockholder posterior mean of $v$ given $s$. \\
\Phi,\phi & Standard normal CDF and PDF. \\
\lambda_L(\alpha),\lambda_U(\alpha) & Inverse Mills ratios: $\lambda_L(\alpha)=\phi(\alpha)/\Phi(\alpha)$ and $\lambda_U(\alpha)=\phi(\alpha)/(1-\Phi(\alpha))$. \\
\midrule
\multicolumn{2}{@{}l}{\textbf{Trading, liquidity, disclosure}} \\
q & Blockholder order at $t=1$, $q \in \{-1,0,+1\}$. \\
z & Noise-trader order, $z \in \{-1,0,+1\}$ with $\PP(z=0)=1-\frac{2}{3}\kappa$ and $\PP(z=\pm1)=\frac{\kappa}{3}$. \\
\kappa & Noise-trading intensity (liquidity). \\
X & Total order flow observed by the market maker, $X=q+z$. \\
D & Disclosure indicator for threshold-crossing stake acquisition, $D=1 \iff (q=+1)$. \\
P(X,D) & Competitive price at $t=1$ conditional on $(X,D)$. \\
\midrule
\multicolumn{2}{@{}l}{\textbf{Engagement (voice)}} \\
a & Engagement choice at $t=1$, $a \in \{0,1\}$. \\
C(s),C_0,\chi & Engagement cost at $t=1$ (private to the blockholder); $C(s)=C_0\exp\!\left(-\chi \frac{s-\mu}{\sigma_s}\right)$. \\
\rho & Engagement success probability. \\
\Delta,\tilde{\Delta} & Standalone improvement if engagement succeeds; $\tilde{\Delta}\equiv\rho\Delta$ is the expected improvement under $a=1$. \\
m_0,m_1 & Takeover premia above $\hat{V}$: baseline $m_0$ (no successful engagement) and $m_1>m_0$ (successful engagement). \\
\tilde{m} & Expected premium under engagement, $\tilde{m}\equiv m_0+\rho(m_1-m_0)$. \\
\pi(X,D) & Posterior engagement probability, $\pi(X,D)\equiv \PP(a=1 \mid X,D)$. \\
\bar{m}(X,D) & Expected premium wedge conditional on $(X,D)$, $\bar{m}(X,D)=\E[m^{R}(a) \mid X,D]=m_0+(\tilde{m}-m_0)\pi(X,D)$. \\
\midrule
\multicolumn{2}{@{}l}{\textbf{Takeover and payoffs}} \\
\bar{S} & Baseline bidder synergy (incremental value from acquisition). \\
\Delta_S & Expected fundamental synergy improvement from activism. \\
K & Fixed bidding / entry cost. \\
\xi,s_\xi & Bidder's private synergy shock, $\xi \sim \Lambda(0,s_\xi)$ (logistic distribution). \\
\lambda_B & Exogenous Poisson arrival probability of a potential bidder. \\
\Pi_B(X,D) & Bidder expected net deal surplus conditional on $(X,D)$. \\
\tilde{p}(X,D) & Conditional bid probability given bidder arrival. \\
p(X,D) & Unconditional bid probability conditional on $(X,D)$; $p(X,D) = \lambda_B \cdot \tilde{p}(X,D)$. \\
m^{R}(a) & Realized premium wedge conditional on engagement: $m^{R}(a)=m_0+a(\tilde{m}-m_0)$. \\
  b(X,D) & Expected per-share offer if a bid occurs, $b(X,D)=\hat{V}(X,D)+\bar{m}(X,D)$. \\
  \tau & Time between pricing/entry and settlement in $\delta=\exp(-r\tau)$. \\
  \delta & Discount factor between pricing/entry and settlement, $\delta=\exp(-r\tau)$ (or $1/(1+r)$). \\
  Y & Terminal per-share payoff (takeover vs.\ standalone). \\
U(q,a \mid s) & Blockholder expected utility at $t=1$ conditional on $s$ and action $(q,a)$. \\
\Delta^{\min}(\kappa) & Expected takeover premium earned by a representative minority share, $\E[m^{R}(a)\cdot \1\{\textup{bid}\}]$. \\
\Delta^{\textup{act}}(\kappa) & Activism-driven component of minority takeover gains, $\E[(m^{R}(a)-m_0)\cdot \1\{\textup{bid}\}]$. \\
\midrule
\multicolumn{2}{@{}l}{\textbf{Equilibrium thresholds and regions}} \\
k_1,k_0,k_D & Signal cutoffs for Exit, Hold, Quiet Voice (hidden engagement), and Public Voice (disclosed engagement). \\
\alpha_i & Standardized cutoffs $\alpha_i \equiv (k_i-\mu)/\sigma_s$ for $i\in\{1,0,D\}$. \\
\omega_E,\omega_H,\omega_Q,\omega_P & Ex ante probabilities of Exit / Hold / Quiet Voice / Public Voice regions. \\
\bottomrule
\end{tabular}
}
\caption{Notation summary (quick reference).}
\label{tab:notation}
\end{table}

\begin{table}[H]
\centering
\begin{tabular}{@{}clp{0.50\linewidth}@{}}
\toprule
\textbf{Label} & \textbf{Content} & \textbf{Location} \\
\midrule
(A1) & Interior cutoffs (nondegeneracy) & Engagement Technology (\S\ref{sec:model}) \\
(A2) & Engagement cost decreasing in signal & Engagement Technology (\S\ref{sec:model}) \\
(A3) & Premium wedge: $\tilde{m} > m_0$ & Engagement Technology (\S\ref{sec:model}) \\
(A4) & Interior bid probability & Bidder Entry (\S\ref{sec:model}) \\
(A5) & Net deterrence condition: $\tilde{\Delta} + \tilde{m} - m_0 > \Delta_S$ & Bidder Entry (\S\ref{sec:model}) \\
(A6) & Numerical Contraction: Spectral radius of $T$ is strictly $< 1$ & Equilibrium Concept (\S\ref{sec:model}) \\
\bottomrule
\end{tabular}
\caption{Summary of standing assumptions (A1)--(A6).}
\label{tab:assumptions}
\end{table}

%==============================================================================
\section{Proofs and Derivations}
\label{app:proofs}

\subsection{Proof of Lemma~\ref{lem:qa-domination} (Domination of Passive Accumulation)}
\label{app:proof-qa-domination}

\begin{proof}
Let $QA \equiv (+1,0)$ denote Quiet Accumulation, yielding $h=2$ shares and triggering disclosure $D=1$. Let $\pi(X,1) \in [0,1]$ be an arbitrary, potentially off-path market belief upon observing $D=1$. This belief generates an expected standalone value $\hat{V}(X,1) = \E[v|X,1] + \tilde{\Delta}\pi(X,1)$ and an unconditional bid probability $p(X,1) \le \lambda_B < 1$. Because the market cannot observe $a$ directly, the price $P^*(X,1)$ and bid probability apply identically to the blockholder whether she plays $QA$ or Public Voice $P \equiv (+1,1)$.

The expected payoff for Public Voice is:
\[
U_{P}(s) = \E_z\big[-P^*(X,1) + 2\delta\big(p(X,1)(\hat{V}(X,1) + \tilde{m}) + (1-p(X,1))(\hat{v}(s) + \tilde{\Delta})\big)\big] - C(s).
\]
Because $a=0$ under $QA$, the blockholder earns the baseline premium $m_0$ upon takeover and zero standalone improvement $\tilde{\Delta}$. The expected payoff is:
\[
U_{QA}(s) = \E_z\big[-P^*(X,1) + 2\delta\big(p(X,1)(\hat{V}(X,1) + m_0) + (1-p(X,1))\hat{v}(s)\big)\big].
\]
The marginal benefit of active engagement for a two-share holder is the exact difference:
\[
U_{P}(s) - U_{QA}(s) = 2\delta\,\E_z\big[p(X,1)(\tilde{m}-m_0) + (1-p(X,1))\tilde{\Delta}\big] - C(s).
\]
Because $p(X,1) \le \lambda_B < 1$, the expected fundamental and premium gain is strictly bounded below by $2\delta\min(\tilde{m}-m_0, \tilde{\Delta}) > 0$. By Assumption~\textup{(A2)}, the cost function $C(s)$ is strictly decreasing and $\lim_{s \to \infty} C(s) = 0$. Therefore, for sufficiently high signals, this difference is strictly positive \emph{regardless of the market's off-path belief}. Applying standard equilibrium refinements (e.g., the D1 criterion), the market places probability zero on $QA$ for threshold-crossing trades, cementing that $D=1$ perfectly reveals active engagement ($a=1$).
\end{proof}

\subsection{Proof of Proposition~\ref{prop:cutoffs}}
\label{app:proof-cutoffs}

\begin{proof}
Write the feasible actions as
\[
E\equiv(-1,0),\quad H\equiv(0,0),\quad Q\equiv(0,1),\quad P\equiv(+1,1), \quad QA\equiv(+1,0),
\]
corresponding to Exit, Hold, Quiet Voice, Public Voice, and Quiet Accumulation. By Lemma~\ref{lem:qa-domination}, $QA$ is strictly dominated, leaving the four active choices.

\textit{Step 1: Best responses are characterized by (at most) three cutoffs.}
Fix any candidate pricing rule $P(\cdot,\cdot)$ and bidder-entry probabilities $p(\cdot,\cdot)$ at each information set $(X,D)$. For an action $(q,a)$ with holdings $h=1+q$ and disclosure $D=\1\{q=+1\}$, the blockholder's $t=1$ payoff conditional on signal $s$ is
\[
U(q,a \mid s)
= \E\Big[-q\cdot P(X,D) + \delta h \cdot Y - a\cdot C(s) \,\Big|\, s,q,a\Big],
\]
where $X=q+z$ and $Y=\1\{\textup{bid}\}\cdot b(X,D,a) + (1-\1\{\textup{bid}\})\cdot (v+a\tilde{\Delta})$.
Since the bid event depends only on $\xi$ conditional on $(X,D)$, $\E[\1\{\textup{bid}\} \mid X,D]=p(X,D)$, and risk neutrality implies $\E[v \mid s]=\hat v(s)$. Taking expectations over $(v,\xi,z)$ conditional on $s$ yields
\begin{align*}
U(q,a \mid s)
&= \E_z\Big[-q\cdot P^*(X,D) + \delta h \big(p(X,D)\cdot (\hat{V}(X,D)+m^{R}(a)) \\
&\qquad\qquad\qquad\qquad\qquad\quad + (1-p(X,D))\cdot(\hat{v}(s)+a\tilde{\Delta})\big)\Big] - a\cdot C(s).
\end{align*}
Define
\[
B_{q,a}\equiv \delta h\cdot \E_z[1-p(X,D)],\qquad X=q+z,
\]
and collect all remaining terms (which do not depend on $s$) into $A_{q,a}$. Then
\begin{equation}
U(q,a \mid s)=A_{q,a}+B_{q,a}\,\hat{v}(s)-a\cdot C(s).
\label{eq:U-affine}
\end{equation}
Because $\hat v(s)=\mu+\beta(s-\mu)$ is strictly increasing in $s$, and $C(s)$ is weakly decreasing by Assumption~\textup{(A2)}, the payoff differences that determine the adjacent-action indifference cutoffs are single-crossing in $s$. In particular:
\begin{itemize}[leftmargin=1.5em,itemsep=2pt]
\item \textbf{Exit vs.\ Hold.} $U_H(s)-U_E=A_{H}-A_{E}+B_{H}\hat v(s)$ is strictly increasing in $s$ (since $B_H>0$ for $h=1$). Hence there is at most one cutoff $k_1$ solving $U_E=U_H(k_1)$, and whenever it exists it separates Exit from Hold.
\item \textbf{Hold vs.\ Quiet Voice.} Since $H$ and $Q$ share $(q,D,h)=(0,0,1)$, their $\hat v(s)$ coefficients are the same, and the difference reduces to
\begin{equation}
U_Q(s)-U_H(s)=\delta\,\E_z\!\Big[p(X,0)\cdot(\tilde m-m_0)+(1-p(X,0))\cdot\tilde\Delta\Big]-C(s),
\label{eq:UH-UQ}
\end{equation}
which is strictly increasing in $s$ when $\chi>0$. Thus there is at most one cutoff $k_0$ solving $U_H(k_0)=U_Q(k_0)$, and whenever it exists it separates Hold from Quiet Voice.
\item \textbf{Quiet vs.\ Public Voice.} Since $Q$ and $P$ both have $a=1$, the cost term cancels. We group the terms involving $\hat{v}(s) = \mu + \beta(s-\mu)$ to show $U_P(s)-U_Q(s)$ is an affine function of the signal $s$. The coefficient on $s$ is $B_P = 2\delta\beta\E_z[1-p(X,1)]$ for Public Voice and $B_Q = \delta\beta\E_z[1-p(X,0)]$ for Quiet Voice. The difference in slopes evaluates to:
\[
B_P - B_Q = \delta\beta \, \E_z\Big[ 2(1-p(X,1)) - (1-p(X,0)) \Big] = \delta\beta \, \E_z\Big[ 1 - 2p(X,1) + p(X,0) \Big].
\]
Because the unconditional bid probability is structurally bounded by the bidder arrival rate ($p(X,D) \le \lambda_B$), and empirical calibrations ensure $\lambda_B < 0.5$, we are mathematically guaranteed that $2p(X,1) < 1$. Consequently, the term inside the expectation is strictly positive, structurally guaranteeing $B_P - B_Q > 0$. The marginal benefit of retaining a second share is strictly increasing in the signal $s$. Thus there is at most one cutoff $k_D$ solving $U_Q(k_D)=U_P(k_D)$, and whenever it exists it separates Quiet Voice from Public Voice.
\end{itemize}
Under Assumption~\textup{(A1)} (interiority/nondegeneracy of regions), the relevant indifference cutoffs exist and are (weakly) ordered, yielding a best response with thresholds $k_1\le k_0\le k_D$ as stated in Proposition~\ref{prop:cutoffs}.%
\footnote{The weak inequalities allow for limiting cases in which some regions collapse (e.g., $k_0=k_1$).}

\textit{Step 2: Given cutoffs, beliefs and prices are pinned down.}
Fix a cutoff vector $(k_1,k_0,k_D)$. This pins down the ex ante region probabilities $(\omega_E,\omega_H,\omega_Q,\omega_P)$ and hence (by Bayes' rule) the posteriors $\pi(X,D)$ in Proposition~\ref{prop:posteriors}. Given these posteriors and conditional means $\E[v \mid X,D]$, the expected standalone value $\hat{V}(X,D)$ and unconditional bid probability $p(X,D)$ are strictly determined. The competitive pricing rule is directly defined by the explicit feed-forward equation~\eqref{eq:price-fp}, trivially providing a unique solution $P^*(X,D)$ for each reached information set.

\textit{Step 3: Fixed point over cutoff vectors.}
Define the cutoff mapping $T:(k_1,k_0,k_D)\mapsto(k_1',k_0',k_D')$ by: (i) compute $(\omega_E,\omega_H,\omega_Q,\omega_P)$ from $(k_1,k_0,k_D)$; (ii) compute posteriors $\pi(X,D)$; (iii) directly compute feed-forward prices $P^*(X,D)$; and (iv) define $(k_1',k_0',k_D')$ as the (unique) solutions to the indifference conditions~\eqref{eq:k1}--\eqref{eq:kD} induced by these objects (using the single-crossing properties from Step~1). By construction, each step is continuous, so $T$ is continuous.

Assumption~\textup{(A6)} states that $T$ is a contraction on a suitable nonempty compact subset $\Theta\subset\R^3$ (with $k_1\le k_0\le k_D$) under the sup norm. Since $(\Theta,\|\cdot\|_\infty)$ is complete, the Banach fixed-point theorem implies that $T$ has a unique fixed point $(k_1,k_0,k_D)\in\Theta$ and that iterating $T$ converges to it. At this fixed point, the blockholder's cutoff strategy is optimal given the induced prices, beliefs are Bayes-consistent, and the market maker's pricing rule is competitive, which together constitute a Perfect Bayesian Equilibrium. The disclosure outcomes follow from the rule $D=1\iff(q=+1)$.
\end{proof}

\subsection{Proof of Proposition~\ref{prop:posteriors}}
\label{app:proof-posteriors}

\begin{proof}
For disclosed states, $D=1$ occurs if and only if $q=+1$ by the disclosure rule. Since the only feasible action with $q=+1$ is Public Voice, $\pi(X,1)=\PP(a=1 \mid X,1)=1$ for all feasible $X\in\{0,1,2\}$.

For nondisclosed states, $D=0$ rules out Public Voice. The remaining actions consistent with $D=0$ are Exit $E\equiv(-1,0)$, Hold $H\equiv(0,0)$, and Quiet Voice $Q\equiv(0,1)$, which occur with ex ante probabilities $(\omega_E,\omega_H,\omega_Q)$.

Write the noise trade probabilities as $\PP(z=0)=1-\frac{2}{3}\kappa$ and $\PP(z=\pm1)=\frac{\kappa}{3}$. Conditional on each action, $X=q+z$ has the following support and probabilities:
\[
\begin{array}{c|ccc}
 & X=q-1 & X=q & X=q+1 \\ \hline
q=-1~(E) & \kappa/3 & 1-\frac{2}{3}\kappa & \kappa/3 \\
q=0~(H,Q)  & \kappa/3 & 1-\frac{2}{3}\kappa & \kappa/3 \\
q=+1~(P) & \kappa/3 & 1-\frac{2}{3}\kappa & \kappa/3
\end{array}
\]
Note that Hold $H$ and Quiet Voice $Q$ generate identical order-flow distributions since both have $q=0$. Applying Bayes' rule, for any $X$ with $D=0$,
\[
\pi(X,0)=\PP(a=1 \mid X,0)=\PP(Q \mid X,0)=\frac{\omega_Q\,\PP(X \mid Q)}{\omega_E\,\PP(X \mid E)+(\omega_H+\omega_Q)\,\PP(X \mid q\!=\!0)}.
\]
If $X=-2$, then $X$ can only be generated by Exit, so $\pi(-2,0)=0$.

If $X=1$, then $X=1$ requires $q=0$ and $z=+1$, so conditioning on $D=0$ implies
\[
\pi(1,0)=\frac{\omega_Q}{\omega_H+\omega_Q}.
\]
If $X=-1$, then $\PP(X=-1 \mid q\!=\!0)=\PP(z=-1)=\frac{\kappa}{3}$ and $\PP(X=-1 \mid E)=\PP(z=0)=1-\frac{2}{3}\kappa$, giving
\[
\pi(-1,0)=\frac{\omega_Q(\kappa/3)}{(\omega_H+\omega_Q)(\kappa/3)+\omega_E(1-\frac{2}{3}\kappa)}.
\]
If $X=0$, then $\PP(X=0 \mid q\!=\!0)=\PP(z=0)=1-\frac{2}{3}\kappa$ and $\PP(X=0 \mid E)=\PP(z=1)=\frac{\kappa}{3}$, so
\[
\pi(0,0)=\frac{\omega_Q(1-\frac{2}{3}\kappa)}{(\omega_H+\omega_Q)(1-\frac{2}{3}\kappa)+\omega_E(\kappa/3)}.
\]
\end{proof}

\subsection{Disclosed-Branch Invariance}
\label{app:proof-disclosed-invariance}

\begin{proof}
Consider any equilibrium under the Standing Assumptions and suppose the disclosed branch is reached (i.e., $\PP(D=1)>0$). By the feasible action set and the disclosure rule, $D=1$ occurs if and only if the blockholder chooses Public Voice $P\equiv(+1,1)$, hence $a=1$ almost surely on $\{D=1\}$ and $X=1+z$ with $z\in\{-1,0,1\}$.

Since $z$ is independent of $(v,s,\xi)$, conditioning on $(X,D)=(x,1)$ reveals only the noise realization $z=x-1$ and does not change beliefs about $v$ beyond what is already implied by $D=1$. Formally, for any Borel set $B\subset\R$ and any $x\in\{0,1,2\}$,
\[
\PP(v\in B \mid X=x,D=1)=\PP(v\in B \mid D=1).
\]
In particular, $\pi(x,1)=\PP(a=1 \mid X=x,D=1)=1$ and $\E[v \mid X=x,D=1]=\E[v \mid D=1]=\mu_P$ for all $x\in\{0,1,2\}$.

Therefore, for each $x\in\{0,1,2\}$ the feed-forward pricing equation~\eqref{eq:price-fp} on the disclosed branch evaluates identically: it depends on $(X,D)$ only through $\hat V(X,D)$, $\bar{m}(X,D)$, and $p(X,1)$, all of which are strictly constant across $x$ when $D=1$. Thus, $P^*(x,1)$ and the conditional bid probability are exactly the same for all $x\in\{0,1,2\}$ on the disclosed branch.
\end{proof}

\subsection{Derivation of Conditional Means}
\label{app:deriv-conditional-means}

\begin{lemma}[Truncated normal expectations]
\label{lem:truncnorm}
Let $S\sim\mathcal{N}(\mu,\sigma^2)$ and define standardized thresholds $\alpha=(a-\mu)/\sigma$ and $\gamma=(b-\mu)/\sigma$. Then
\begin{align*}
\E[S \mid S<a] &= \mu - \sigma\,\frac{\phi(\alpha)}{\Phi(\alpha)}, \\
\E[S \mid a\le S<b] &= \mu + \sigma\,\frac{\phi(\alpha)-\phi(\gamma)}{\Phi(\gamma)-\Phi(\alpha)}, \\
\E[S \mid S\ge b] &= \mu + \sigma\,\frac{\phi(\gamma)}{1-\Phi(\gamma)}.
\end{align*}
\end{lemma}

\begin{proof}
These are standard formulas for the mean of a truncated normal distribution. For completeness, let $Z\sim\mathcal{N}(0,1)$ and note that $\E[S \mid \cdot]=\mu+\sigma\,\E[Z \mid \cdot]$. For the left tail,
\[
\E[Z \mid Z<\alpha]
=\frac{\int_{-\infty}^{\alpha} z\phi(z)\,dz}{\Phi(\alpha)}
=\frac{-\phi(\alpha)}{\Phi(\alpha)},
\]
where the last equality follows from $\frac{d}{dz}\phi(z)=-z\phi(z)$. The right tail follows similarly. For an interval $[\alpha,\gamma)$,
\[
\E[Z \mid \alpha\le Z<\gamma]
=\frac{\int_{\alpha}^{\gamma} z\phi(z)\,dz}{\Phi(\gamma)-\Phi(\alpha)}
=\frac{\phi(\alpha)-\phi(\gamma)}{\Phi(\gamma)-\Phi(\alpha)}.
\]
\end{proof}

\begin{proof}[Derivation of $\mu_E,\mu_H,\mu_Q,\mu_P$]
By iterated expectations,
\[
\E[v \mid s\in\mathcal{S}]=\E[\E[v \mid s] \mid s\in\mathcal{S}]=\E[\hat{v}(s) \mid s\in\mathcal{S}],
\]
for any measurable set $\mathcal{S}$. Since $\hat{v}(s)=\mu+\beta(s-\mu)$,
\[
\E[v \mid s\in\mathcal{S}]
=\mu+\beta\big(\E[s \mid s\in\mathcal{S}]-\mu\big).
\]
Applying Lemma~\ref{lem:truncnorm} to $s\sim\mathcal{N}(\mu,\sigma_s^2)$ with the relevant truncation regions $\mathcal{S}$ yields the expressions for $\mu_E,\mu_H,\mu_Q,\mu_P$ in the main text. In particular:
\begin{itemize}[leftmargin=1.5em,itemsep=0pt]
\item $\mu_E = \E[v \mid s < k_1]$ uses the left-tail formula with $\alpha = (k_1 - \mu)/\sigma_s$.
\item $\mu_H = \E[v \mid k_1 \le s < k_0]$ uses the interval formula with $\alpha = (k_1 - \mu)/\sigma_s$ and $\gamma = (k_0 - \mu)/\sigma_s$.
\item $\mu_Q = \E[v \mid k_0 \le s < k_D]$ uses the interval formula with $\alpha = (k_0 - \mu)/\sigma_s$ and $\gamma = (k_D - \mu)/\sigma_s$.
\item $\mu_P = \E[v \mid s \ge k_D]$ uses the right-tail formula with $\alpha = (k_D - \mu)/\sigma_s$.
\end{itemize}
\end{proof}

\begin{proof}[Derivation of $\E\lbrack v \mid X,D\rbrack$]
For $D=1$, only Public Voice is feasible, so $\E[v \mid X,1]=\mu_P$ for all compatible $X\in\{0,1,2\}$.

For $D=0$, Exit, Hold, and Quiet Voice are feasible. Since $X=q+z$ with $z$ independent of $(v,s)$, the conditional distribution of $v$ given $(X,D)$ is obtained by mixing the action-specific conditional means using Bayes weights proportional to the ex ante action probabilities and the likelihoods $\PP(X \mid q)$. Note that Hold ($H$) and Quiet Voice ($Q$) both have $q=0$ and hence generate identical order-flow distributions. Using Bayes' rule and the conditional means $(\mu_E,\mu_H,\mu_Q)$ gives:
\begin{itemize}[leftmargin=1.5em,itemsep=0pt]
\item $X=-2$ implies Exit, hence $\E[v \mid -2,0]=\mu_E$.
\item $X=1$ implies $q=0$ and $z=+1$, so
\[
\E[v \mid 1,0] = \frac{\omega_H \mu_H + \omega_Q \mu_Q}{\omega_H + \omega_Q}.
\]
\item $X=-1$ mixes Exit ($z=0$), Hold ($z=-1$), and Quiet Voice ($z=-1$). Writing the Bayes weights as
\[
w_E=\frac{\omega_E\,p_0}{\mathcal{D}_{-1}},\quad
w_H=\frac{\omega_H\,p_1}{\mathcal{D}_{-1}},\quad
w_Q=\frac{\omega_Q\,p_1}{\mathcal{D}_{-1}},
\]
with $\mathcal{D}_{-1}=(\omega_H+\omega_Q)p_1+\omega_E\,p_0$, yields $\E[v \mid -1,0]=w_E\mu_E+w_H\mu_H+w_Q\mu_Q$.
\item $X=0$ mixes Quiet Voice/Hold with $z=0$ and Exit with $z=1$. Writing the Bayes weights as
\[
w_E=\frac{\omega_E\,p_1}{\mathcal{D}_0},\quad
w_H=\frac{\omega_H\,p_0}{\mathcal{D}_0},\quad
w_Q=\frac{\omega_Q\,p_0}{\mathcal{D}_0},
\]
with $\mathcal{D}_0=(\omega_H+\omega_Q)p_0+\omega_E\,p_1$, yields $\E[v \mid 0,0]=w_E\mu_E+w_H\mu_H+w_Q\mu_Q$.
\end{itemize}
\end{proof}

\subsection{Proof of Proposition~\ref{prop:price-decomp}}
\label{app:proof-price-decomp}

\begin{proof}
    The market maker sets $P(X,D)=\delta\,\E[Y \mid X,D]$. Conditional on $(X,D)$, the expected standalone value $\hat{V}(X,D)$ and expected premium wedge $\bar{m}(X,D)$ are constants. The bid indicator $\1\{\textup{bid}\}$ is conditionally independent of $(v,a)$ given $(X,D)$, so $\E[\1\{\textup{bid}\} \mid X,D]=p(X,D)$.

  In the takeover payoff, the expected required payout is $\hat{V}(X,D) + \bar{m}(X,D)$. Using conditional independence,
\[
\E[(1-\1\{\textup{bid}\})\cdot (v + a\tilde{\Delta}) \mid X,D] = (1-p(X,D))\big(\E[v \mid X,D]+\tilde{\Delta}\pi(X,D)\big) = (1-p(X,D))\hat{V}(X,D).
\]
  Taking expectations of $Y$ conditional on $(X,D)$ yields
  \[
  \E[Y \mid X,D]
  =p(X,D)\cdot(\hat{V}(X,D)+\bar{m}(X,D))+(1-p(X,D))\cdot\hat{V}(X,D).
  \]
  This algebraically simplifies to $\hat{V}(X,D) + p(X,D)\bar{m}(X,D)$. Multiplying by $\delta$ gives the stated decomposition.
\end{proof}

\subsection{Proof of Bid Probability Monotonicity}
\label{app:proof-bid-monotone}

\begin{proof}
Let
\[
T(X,D)\equiv \frac{\hat{V}(X,D)+\bar{m}(X,D)+K-(\bar{S}+\pi(X,D)\Delta_S)}{s_\xi}.
\]
Then the unconditional bid probability is $p(X,D)=\lambda_B(1-\Lambda(T(X,D)))$.

Differentiating $T(X,D)$ with respect to $\pi(X,D)$ requires the chain rule for $\hat{V}(X,D)$ and $\bar{m}(X,D)$. Since $\frac{\partial \hat{V}}{\partial \pi} = \tilde{\Delta}$ and $\frac{\partial \bar{m}}{\partial \pi} = \tilde{m}-m_0$, we have:
\[
\frac{\partial T(X,D)}{\partial \pi(X,D)} = \frac{\tilde{\Delta} + (\tilde{m}-m_0) - \Delta_S}{s_\xi}.
\]
Under Assumption~\textup{(A5)}, $\tilde{\Delta} + \tilde{m}-m_0 > \Delta_S$, making this derivative strictly positive.
Since $\Lambda' = \lambda > 0$, we have:
\[
\frac{\partial p(X,D)}{\partial \pi(X,D)}=-\lambda_B \lambda(T(X,D)) \cdot \frac{\tilde{\Delta} + \tilde{m}-m_0 - \Delta_S}{s_\xi} < 0.
\]
Thus, higher inferred engagement strictly deters bids through the efficient pricing of the standalone target fundamental value.
\end{proof}

\subsection{Proof of Within-Regime Liquidity Effects}
\label{app:proof-cs-liquidity-within}

\begin{proof}
Fix $(\omega_E,\omega_H,\omega_Q)$ and write $p_0\equiv 1-\frac{2}{3}\kappa$ and $p_1\equiv \frac{\kappa}{3}$. For any reached nondisclosed information set (so denominators are nonzero), Proposition~\ref{prop:posteriors} gives:
\[
\pi(1,0)=\frac{\omega_Q}{\omega_H+\omega_Q},\qquad
\pi(-1,0)=\frac{\omega_Q p_1}{(\omega_H+\omega_Q)p_1+\omega_E p_0},\qquad
\pi(0,0)=\frac{\omega_Q p_0}{(\omega_H+\omega_Q)p_0+\omega_E p_1}.
\]
The first expression does not involve $\kappa$, hence $\partial \pi(1,0)/\partial\kappa=0$.

For $X=-1$, differentiating with respect to $\kappa$ yields
\[
\frac{\partial \pi(-1,0)}{\partial \kappa}
=\frac{(\omega_Q/3)\omega_E}{\big((\omega_H+\omega_Q)(\kappa/3)+\omega_E(1-\frac{2}{3}\kappa)\big)^2}\ge 0,
\]
with strict inequality whenever $\omega_E\omega_Q>0$.

For $X=0$, differentiating yields
\[
\frac{\partial \pi(0,0)}{\partial \kappa}
=-\frac{(\omega_Q/3)\omega_E}{\big((\omega_H+\omega_Q)(1-\frac{2}{3}\kappa)+\omega_E(\kappa/3)\big)^2}\le 0,
\]
again strict whenever $\omega_E\omega_Q>0$.

Finally, $\pi(-2,0)=0$ and $\pi(X,1)=1$ follow from Proposition~\ref{prop:posteriors}. The claims for $\bar{m}(X,D)=m_0+(\tilde m-m_0)\pi(X,D)$ follow because $m$ is affine in $\pi$ with slope $\tilde m-m_0>0$ under Assumption~\textup{(A3)}.
\end{proof}

\subsection{Proof of Takeover Comparative Statics}
\label{app:proof-cs-takeover}

\begin{proof}
Recall the unconditional bid probability function
\[
p(X,D)=\lambda_B\left(1-\Lambda\!\left(\frac{\hat{V}(X,D)+\bar{m}(X,D)+K - (\bar{S} + \pi(X,D)\Delta_S)}{s_\xi}\right)\right).
\]
Holding $(X,D)$ fixed, $\partial p/\partial \bar S>0$ and $\partial p/\partial K<0$ follow immediately from the properties of the logistic CDF $\Lambda'=\lambda>0$. Because the bid probability is anchored to $\hat{V}(X,D)$ rather than the anticipatory market price $P(X,D)$, the price-to-entry feedback loop is eliminated entirely, rendering arbitrary price regularity conditions unnecessary.
\end{proof}

\subsection{Proof of Equilibrium Cutoff Equations}
\label{app:proof-cutoff-eqns}

\begin{proof}
  Define the action-specific expected payoffs by evaluating $U(q,a \mid s)$ for the four actions in Proposition~\ref{prop:cutoffs}:
  \begin{align*}
  U_E &\equiv U(-1,0 \mid s), \quad U_H(s)\equiv U(0,0 \mid s), \quad U_Q(s)\equiv U(0,1 \mid s), \\
  U_P(s) &\equiv U(+1,1 \mid s).
  \end{align*}
In a cutoff strategy equilibrium with thresholds $k_1<k_0<k_D$, the blockholder is indifferent between adjacent actions at the boundary signals where the action switches. The three indifference conditions are:
\begin{itemize}[leftmargin=1.5em,itemsep=0pt]
\item At $s = k_1$: Exit vs.\ Hold, i.e., $U_E = U_H$.
\item At $s = k_0$: Hold vs.\ Quiet Voice, i.e., $U_H = U_Q(k_0)$.
\item At $s = k_D$: Quiet Voice vs.\ Public Voice, i.e., $U_Q(k_D) = U_P(k_D)$.
\end{itemize}
These are exactly the conditions~\eqref{eq:k1}--\eqref{eq:kD}.
\end{proof}

\subsection{Proof of Minority Takeover Gains Decomposition}
\label{app:proof-minority-decomp}

\begin{proof}
  By definition,
  \[
  \Delta^{\min}(\kappa)=\E\big[\bar{m}(X,D)\cdot \1\{\textup{bid}\}\big].
  \]

    Conditional on $(X,D)$, the bid indicator $\1\{\textup{bid}\}$ is conditionally independent of the noise realization. Taking expectations over $(X,D)$ yields
    \[
    \E\big[\bar{m}(X,D)\cdot \1\{\textup{bid}\} \mid X,D\big]
    =\bar{m}(X,D)\cdot \E[\1\{\textup{bid}\} \mid X,D]
    =\bar{m}(X,D)\cdot p(X,D).
    \]
  Taking expectations over $(X,D)$ yields $\Delta^{\min}(\kappa)=\E[\bar{m}(X,D)\cdot \1\{\textup{bid}\}]$.

  Using $\bar{m}(X,D)=m_0+(\tilde{m}-m_0)\pi(X,D)$ and linearity of expectation,
  \begin{align*}
  \Delta^{\min}(\kappa)
  &=\E\big[(m_0+(\tilde{m}-m_0)\pi(X,D))\cdot \1\{\textup{bid}\}\big] \\
  &=m_0\cdot \E[\1\{\textup{bid}\}] + (\tilde{m}-m_0)\cdot \E\big[\pi(X,D)\cdot \1\{\textup{bid}\}\big],
  \end{align*}
  which is the claimed decomposition with $\PP(\textup{bid})=\E[\1\{\textup{bid}\}]$.
\end{proof}

\subsection{Proof of Proposition~\ref{prop:existence} (Existence)}
\label{app:proof-existence}

\begin{proof}
Let $\Theta$ be the set of cutoff vectors $(k_1,k_0,k_D)$ such that $k_1\le k_0\le k_D$, restricted to a compact rectangular domain $[\underline{k},\bar{k}]^3\cap\{k_1\le k_0\le k_D\}$. Because $C(s)$ is strictly positive and bounded away from zero for $s<\bar{k}$, and fundamental values are bounded within realistic integration limits, we can choose $\underline{k}$ and $\bar{k}$ large enough in magnitude such that best-response cutoffs strictly map into the interior of $\Theta$. The mapping $T:(k_1,k_0,k_D)\mapsto (k_1',k_0',k_D')$, generated by explicitly computing feed-forward prices via~\eqref{eq:price-fp} and updating cutoffs via the single-crossing indifference conditions~\eqref{eq:k1}--\eqref{eq:kD}, is unconditionally continuous. Since $\Theta$ is a compact, convex subset of a Euclidean space, Brouwer's Fixed-Point Theorem guarantees that $T$ has at least one fixed point in $\Theta$.
\end{proof}

\subsection{Numerical Verification of Uniqueness}
\label{app:proof-uniqueness}

Assumption~\textup{(A6)} formally requires that the parameter space restricts the cutoff mapping $T$ to be a contraction on the feasible domain $\Theta$, guaranteeing a unique fixed point. Analytically bounding the spectral radius of the Jacobian of $T$ is intractable because the derivatives involve highly nonlinear interactions between inverse Mills ratios, the logistic CDF of the bidder's entry rule, and Bayesian posterior updating. Following the methodological precedent established for discrete order-flow feedback models \citep{EdmansGoldsteinJiang2015}, I verify this condition numerically: because the pathological recursive price loop has been structurally eradicated from the model, the strategic complementarity between cutoffs is organically bounded. In all numerical exercises presented in this paper, iterating $T$ from arbitrary starting points converges strictly to a unique fixed point, confirming the contraction mapping.

\subsection{Proof of Lemma~\ref{lem:endpoints} (Endpoint Behavior)}
\label{app:proof-endpoints}

\begin{proof}
\textit{Left endpoint ($\kappa\downarrow 0$).}
As noise trading vanishes, $\PP(z=\pm 1)=\kappa/3\to 0$ and $\PP(z=0)=1-\frac{2}{3}\kappa\to 1$. Consequently, aggregate order flow almost surely reveals the blockholder's trade: $X\to q$ with probability one. For $q=0$ and $D=0$, the market perfectly deduces $q=0$, which pools the Hold and Quiet Voice actions. The price $P(X,0)$ perfectly impounds the expected engagement probability $\pi(X,0)=\omega_Q/(\omega_H+\omega_Q)$.

Because the blockholder only holds her initial share under Quiet Voice ($q=0$), her net trading cash flow is strictly zero ($-qP(X,0)=0$). Thus, her execution price cost is fully shielded. The expected utility difference for the marginal type $k_0$ is:
\[
U_Q(k_0) - U_H(k_0) = \delta\,\E_z \big[p(X,0)(\tilde{m}-m_0) + (1-p(X,0))\tilde{\Delta}\big] - C(k_0).
\]
While the market fully prices the expected engagement into $P(X,0)$, which deters bidder entry mathematically by reducing $p(X,0)$, the fundamental value improvement $\tilde{\Delta}$ and premium wedge $\tilde{m}-m_0$ ensure that the gross engagement benefit remains strictly positive, bounded below by $\delta \min(\tilde{m}-m_0, \tilde{\Delta})$. By Assumption~\textup{(A2)}, the engagement cost $C(s)$ is strictly decreasing and $\lim_{s \to \infty} C(s) = 0$. Therefore, there structurally exists an upper range of signals where the gross benefit of engagement exceeds the private cost, regardless of the maximum bid deterrence penalty imposed by $P(X,0)$. Thus, the Quiet Voice region mathematically survives ($\omega_Q > 0$), and $\Delta^{\textup{act}}(\kappa)$ remains strictly positive as $\lim_{\kappa \downarrow 0} \Delta^{\textup{act}}(\kappa) > 0$. Nonetheless, the perfectly separating order flow forces the heightened price to maximally depress $p(X,0)$, artificially suppressing the expected minority gains below their optimal interior potential.

\textit{Right endpoint ($\kappa\uparrow 1$).}
As $\kappa\to 1$, noise trading converges to a perfect uniform distribution over $\{-1,0,+1\}$ with exact probabilities $(1/3, 1/3, 1/3)$. Crucially, because the probability of zero noise $p_0$ does not vanish, the market maker cannot perfectly separate Exit ($q=-1$) from Quiet Voice ($q=0$) upon observing $X=0$. Order flow $X=q+z$ becomes completely uninformative about the blockholder's underlying trade $q$. Consequently, the Bayesian posteriors $\pi(X,0)$ perfectly converge to the unconditional prior $\omega_Q/(\omega_E+\omega_H+\omega_Q)$ across all nondisclosed states. Because the takeover payout directly maps to the inferred premium $\bar{m}(X,D)$, as $\pi$ flattens toward the prior, the blockholder's marginal premium benefit of engagement collapses. Stripped of the ability to extract adverse-selection rents via order-flow inference, the expected return to engagement falls strictly below the private cost $C(s)$ for all signal realizations. The voice regions collapse ($\omega_Q+\omega_P\to 0$), engagement $a=0$ occurs almost surely, and $\Delta^{\min}(\kappa)\to m_0\PP(\textup{bid})$.
\end{proof}

\subsection{Proof of Proposition~\ref{prop:nonmonotone} (Nonmonotonicity)}
\label{app:proof-nonmonotone}

\begin{proof}
By Lemma~\ref{lem:endpoints}, the continuous extension of $\Delta^{\min}$ to the closed interval $[0,1]$ satisfies $\Delta^{\min}(1) = m_0\PP(\textup{bid})$. Because the logistic probability formulas and pricing mappings are continuous in $\kappa$, $\Delta^{\min}(\kappa)$ attains a global maximum on $[0,1]$.

To prove the maximum is interior, consider the function $f(\pi) = \tilde{p}(\pi)(m_0 + \pi(\tilde{m}-m_0))$, where $\tilde{p}(\pi) = 1 - \Lambda(T(\pi))$ and $T(\pi) = (\hat{V} + \bar{m} + K - \bar{S} - \pi \Delta_S) / s_\xi$. The second derivative $f''(\pi) < 0$ strictly if $B(1-2\tilde{p})\bar{m} < 2(\tilde{m}-m_0)$, where $B = (\tilde{\Delta} + \tilde{m}-m_0 - \Delta_S) / s_\xi > 0$. When the baseline synergy $\bar{S}$ ensures $T(\pi) > 0$, the probability $\tilde{p} < 0.5$, and this parametric condition easily holds, making $f(\pi)$ strictly concave in $\pi$.

At $\kappa \to 0$, $X=0$ perfectly reveals $q=0$, causing the posterior $\pi$ to separate perfectly to its extreme values. By Jensen's inequality, a mean-preserving spread in $\pi$ strictly decreases the expected value of a concave function. Thus, the maximal dispersion of $\pi$ at $\kappa \to 0$ mathematically minimizes $\E[f(\pi)]$, pulling $\Delta^{\min}$ down at the left boundary. At an interior $\tilde{\kappa} \in (0,1)$, noise pooling yields an intermediate $\pi(0,0) \in (0,1)$, which strictly increases the expected value $\E[f(\pi)]$. Consequently, $\Delta^{\min}(\tilde{\kappa}) > \lim_{\kappa \downarrow 0} \Delta^{\min}(\kappa)$. Coupled with the right-endpoint collapse, the unique global maximizer $\kappa^\dagger$ must lie in the interior $(0,1)$.
\end{proof}

\subsection{Derivations for Section~\ref{sec:extensions}}
\label{app:extensions-derivations}

\paragraph{(ND) No disclosure.}
Under the no-disclosure regime $S_{\textup{ND}}=\emptyset$, the market conditions only on $X=q+z$ with
$\PP(z=0)=p_0=1-\frac{2}{3}\kappa$ and $\PP(z=\pm1)=p_1=\frac{\kappa}{3}$. Writing $\PP(X \mid q)$ for the order-flow likelihood induced by $z$, Bayes' rule implies
\[
\pi_{\textup{ND}}(X)\equiv \PP(a=1 \mid X)
=\frac{\omega_Q\PP(X \mid q=0)+\omega_P\PP(X \mid q=+1)}
{\omega_E\PP(X \mid q=-1)+(\omega_H+\omega_Q)\PP(X \mid q=0)+\omega_P\PP(X \mid q=+1)}.
\]
Substituting $\PP(X=q)=p_0$ and $\PP(X=q\pm1)=p_1$ (and zero otherwise) yields the closed-form expressions reported in Section~\ref{sec:extensions}.

\paragraph{(NR) Baseline stake disclosure plus a noisy rumor.}
Under $S_{\textup{NR}}=(D,R)$ with $D=\1\{q=+1\}$, the disclosed branch $D=1$ pins down Public Voice in the baseline action set, so $\pi(X,1,R)=1$ for all feasible $X$.
When $D=0$, $q\in\{-1,0\}$ and the rumor has hit/false-alarm rates $\PP(R=1 \mid q=0,a=1)=\eta_1$ and $\PP(R=1 \mid q=0,a=0)=\eta_0$, with the convention $\PP(R=1 \mid q=-1)=\eta_0$.
Bayes' rule gives, for each feasible $(X,R)$,
\begin{align*}
\pi(X,0,R)
&=\PP(Q \mid X,0,R)\\
&=\frac{\omega_Q\,\PP(X \mid q=0)\PP(R \mid Q)}
{\omega_E\,\PP(X \mid q=-1)\PP(R \mid E)+\PP(X \mid q=0)\big(\omega_H\,\PP(R \mid H)+\omega_Q\,\PP(R \mid Q)\big)}.
\end{align*}
Evaluating $\PP(X \mid q)$ using $X=q+z$ yields the cases in Section~\ref{sec:extensions}: $X=-2$ is degenerate (Exit only); $X=1$ pins down $q=0$ so $\kappa$ drops out; and $X\in\{-1,0\}$ mixes $q=-1$ and $q=0$ with weights proportional to $(p_0,p_1)$, generating the displayed formulas.

%==============================================================================
\section{Tables}
\label{app:tables}

% \noindent This appendix collects tables referenced in the main text.

\setcounter{table}{0}
\renewcommand{\thetable}{\thesection.\arabic{table}}

\begin{table}[H]
\centering
\input{numerical_output/table_example.tex}
\caption{Baseline numerical equilibrium (values rounded to two decimals). Parameters: $\mu=1$, $\sigma_v=0.5$, $\sigma_\varepsilon=0.5$, $\delta=0.95$, $\Delta=0.25$, $C_0=0.25$, $\chi=0.5$, $\kappa=0.5$, $m_0=0.10$, $m_1=0.30$, $\bar{S}=1.10$, $\Delta_S=0.30$, $K=0.15$, $s_\xi=0.15$, $\lambda_B=0.20$, $\rho=0.9$. Cutoffs: $k_1$, $k_0$, and $k_D$ (see updated numerical output).}
\label{tab:example}
\end{table}

\begin{table}[H]
\centering
\input{numerical_output/table_disclosure_extensions.tex}
\caption{Illustration of posterior engagement probabilities under alternative disclosure signals (Section~\ref{sec:extensions}), evaluated at the baseline calibrated equilibrium cutoffs and $\kappa=0.5$. For NR, the rumor parameters are set to $(\eta_1,\eta_0)=(0.75,0.25)$.}
\label{tab:disclosure-extensions}
\end{table}

\begin{table}[H]
\centering
\begin{tabular}{@{}llrl@{}}
\toprule
Parameter & Symbol & Value & Interpretation \\
\midrule
\multicolumn{4}{@{}l}{\textit{Fundamentals}} \\
Prior mean & $\mu$ & 1.00 & Normalized baseline value \\
Fundamental volatility & $\sigma_v$ & 0.50 & Moderate uncertainty \\
Signal noise & $\sigma_\varepsilon$ & 0.50 & Informative but noisy signal \\[3pt]
\multicolumn{4}{@{}l}{\textit{Engagement}} \\
Base engagement cost & $C_0$ & 0.25 & Sufficiently high to restore passive Hold \\
Cost sensitivity & $\chi$ & 0.50 & Moderate signal-dependence \\
Success probability & $\rho$ & 0.90 & High success rate \\
Value improvement & $\Delta$ & 0.25 & 25\% improvement if successful \\[3pt]
\multicolumn{4}{@{}l}{\textit{Takeover}} \\
Base premium & $m_0$ & 0.10 & 10\% premium without activism \\
Activism premium & $m_1$ & 0.30 & 30\% premium with activism \\
Baseline synergy & $\bar{S}$ & 1.10 & Balanced to ensure highly sensitive bid variation \\
Synergy improvement & $\Delta_S$ & 0.30 & Activism increases synergy \\
Bidding cost & $K$ & 0.15 & Fixed deal friction \\
Synergy scale (Logistic) & $s_\xi$ & 0.15 & Controls probability dispersion \\
Bidder arrival rate & $\lambda_B$ & 0.20 & Calibrates unconditional bid rates to 2-8\% \\[3pt]
\multicolumn{4}{@{}l}{\textit{Other}} \\
Discount factor & $\delta$ & 0.95 & $\delta=\exp(-r\tau)$ between pricing and settlement \\
Noise intensity & $\kappa$ & 0.50 & Baseline (varies in analysis) \\
\bottomrule
\end{tabular}
\caption{Baseline parameterization for numerical analysis.}
\label{tab:params}
\end{table}

%==============================================================================
\section{Figures}
\label{app:figures}
%==============================================================================

\setcounter{figure}{0}
\renewcommand{\thefigure}{\thesection.\arabic{figure}}

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{numerical_output/fig_cutoff_structure.pdf}
\caption{Equilibrium cutoff structure. The blockholder follows a threshold strategy with weakly ordered cutoffs. In general, the signal space can be partitioned into up to four regions (Exit, Hold, Quiet Voice, Public Voice), with disclosure occurring only under Public Voice. In the baseline numerical example, $k_0=k_1$, so the strategy reduces to Exit, Quiet Voice, and Public Voice.}
\label{fig:cutoff-structure}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_nonmonotone.pdf}
\caption{Nonmonotonic effect of liquidity on expected minority takeover gains. The vertical dashed line marks the turning point $\kappa^{\dagger}$ (the maximizer of $\Delta^{\min}$ on the plotted grid) in the baseline calibration.}
\label{fig:nonmonotone}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_decomposition.pdf}
\caption{Decomposition of minority takeover gains. The base component $m_0 \cdot \PP(\textup{bid})$ and the activism component $\Delta^{\textup{act}}(\kappa)$ vary smoothly with liquidity in the baseline calibration; the dashed line marks $\kappa^{\dagger}$.}
\label{fig:decomposition}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.95\textwidth]{numerical_output/fig_prices.pdf}
\caption{Equilibrium prices by state $(X,D)$ in the baseline numerical example. Left panel: nondisclosed states ($D=0$). Right panel: disclosed states ($D=1$). Bars are shown for on-path states under the calibrated strategy. Numbers above bars indicate the posterior engagement probability $\pi(X,D)$.}
\label{fig:prices}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_cutoffs_kappa.pdf}
\caption{Equilibrium cutoffs as functions of liquidity. The ordering $k_1 \le k_0 \le k_D$ is preserved; regions may collapse. The horizontal dashed line marks the prior mean $\mu$.}
\label{fig:cutoffs-kappa}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_disclosure.pdf}
\caption{Disclosure attenuation through the inference channel (partial equilibrium in $\kappa$). We fix the blockholder's cutoff strategy at the baseline calibrated equilibrium ($\kappa=0.5$) and vary liquidity $\kappa$ only through the order-flow noise distribution. The blue curve plots $\Delta^{\textup{act}}(\kappa)$ under threshold disclosure with fixed cutoffs. The orange curve plots the counterfactual ``no-disclosure'' benchmark with the same fixed cutoffs, in which the market conditions only on order flow $X$.}
\label{fig:disclosure}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_sensitivity_C0.pdf}
\caption{Sensitivity to engagement cost $C_0$. Expected minority takeover gains remain broadly nonmonotone in $\kappa$ across cost levels (computed over $\kappa \in [0.25,0.85]$), with the hump flattening at high $C_0$ as voice becomes rare. Higher costs shrink the voice regions and reduce the activism component, but can increase bid incidence; the net effect on $\Delta^{\min}$ is therefore ambiguous in general.}
\label{fig:sensitivity-C0}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_sensitivity_wedge.pdf}
\caption{Sensitivity to premium wedge $(m_1 - m_0)$. A larger wedge raises the premium conditional on bidding but can deter bids; expected minority takeover gains can therefore be nonmonotone in the wedge (computed over $\kappa \in [0.25,0.85]$).}
\label{fig:sensitivity-wedge}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_sensitivity_rho.pdf}
\caption{Sensitivity to engagement success probability $\rho$. Lowering the expected success rate naturally shrinks the magnitude of minority takeover gains, flattening the curve. However, the qualitative nonmonotonicity remains robust, driven by the structural trade-off between bid incidence and order-flow inference.}
\label{fig:sensitivity-rho}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_sensitivity_sigma_xi.pdf}
\caption{Sensitivity to bidder synergy scale $s_\xi$. Increasing bidder heterogeneity raises overall bid incidence, which uniformly shifts expected minority gains upward while preserving the inference-driven hump shape.}
\label{fig:sensitivity-sigma-xi}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_sensitivity_delta.pdf}
\caption{Sensitivity to the discount factor $\delta$. Lower discount factors mechanically reduce equilibrium prices, increasing bid incidence as the bidder faces lower acquisition costs. Although lower $\delta$ weakens engagement incentives, the bid-probability channel dominates, producing a uniform upward shift in minority gains and a progressive flattening of the hump shape.}
\label{fig:sensitivity-delta}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_noisy_rumor_precision.pdf}
\caption{Disclosure attenuation via noisy rumors. Under the intermediate information regime, the market receives an imperfect signal of hidden engagement. As the public rumor becomes more precise ($\eta_1 - \eta_0$ increases), engagement becomes more observable in nondisclosed states, progressively flattening the sensitivity of the activism premium to market liquidity.}
\label{fig:noisy-rumor-precision}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{numerical_output/fig_welfare.pdf}
\caption{Welfare decomposition and optimal liquidity. Expected total surplus $W$ inherits the nonmonotone shape driven by fundamental value creation during engagement. The liquidity level $\kappa^*$ that maximizes total surplus may differ from the level $\kappa^\dagger$ that maximizes minority extraction, highlighting a potential tension between aggregate allocative efficiency and pure shareholder protection.}
\label{fig:welfare}
\end{figure}

\end{document}
```
