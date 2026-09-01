# Literature check, September 2026

Three questions, answered against sources read directly. An entry appears only where the hit
changes a sentence the paper will carry. Each entry names that sentence.

## Question 1: has anyone stated a composition or partition result on the filing window?

No. The searches covered the blockholder disclosure theory literature and working papers posted
between 2024 and 2026, on the terms "Schedule 13D", "five business days", "beneficial ownership",
"disclosure deadline", "pre-disclosure period", and on decompositions of price informativeness
into a weight leg and a selection leg. Two papers come close enough to matter and neither states
the result. Back, Kerry, Pierre Collin-Dufresne, Vyacheslav Fos, Tao Li, and Alexander Ljungqvist,
"Activism, Strategic Trading, and Liquidity", *Econometrica* 86(4), 2018, 1431 to 1463, doi
10.3982/ECTA14917, working paper text at https://www.nber.org/papers/w22893, is the one model that
puts the pre-disclosure period inside a trading model. It handles the window as a scale on noise
and not as a split of histories. Their own words: "what matters is σ²T, the cumulative amount of
noise trading over the entire trading period. So from the perspective of a potential activist,
reducing the trading horizon T is isomorphic to reducing noise trading volatility and keeping T
fixed." A shorter clock in that model changes how much noise accumulates. It does not change which
histories the filing catches, so no composition leg arises and none is signed. Ordóñez-Calafí,
Guillem, and Dan Bernhardt, "Blockholder Disclosure Thresholds and Hedge Fund Activism", *Journal
of Financial and Quantitative Analysis* 57(7), 2022, 2834 to 2859, doi 10.1017/S0022109022000059,
works the threshold dial alone, and works it for welfare: it asks how the threshold trades off the
cost to uninformed investors of trading against an informed activist against the benefit of
managerial discipline. It carries no window, no partition of histories into a flagged and a pooled
cell, and no factorisation of noise sensitivity. **Sentence this changes:** the clock dial result
and the who gets caught corollary are stated in the paper's own right, with no "following" or
"extending" clause attached, and the related work sentence beside them reads that existing trading
models treat a shorter clock as less cumulative noise, so the composition of the pooled cell never
moves and the question of its sign does not arise there.

## Question 2: is there a precedent for ordering order-flow experiments by noise intensity?

The ordering itself is Blackwell, David, "Equivalent Comparisons of Experiments", *Annals of
Mathematical Statistics* 24(2), 1953, 265 to 272, doi 10.1214/aoms/1177729032, which gives the
equivalence between a garbling by a stochastic kernel and the ranking of expected payoffs under
every convex objective. That is the right primary cite for the direction the garbling lemma uses.
For ordering signal structures by the dispersion they induce rather than by a kernel, the standard
reference is Ganuza, Juan-José, and José S. Penalva, "Signal Orderings Based on Dispersion and the
Supply of Private Information in Auctions", *Econometrica* 78(3), 2010, 1007 to 1030, doi
10.3982/ECTA6640, which defines supermodular precision and integral precision by combining
variability of conditional expectations with the dispersive and convex orders. The closest thing
in finance to the garbling lemma's conclusion is Back, Collin-Dufresne, Fos, Li, and Ljungqvist
(2018), cited above, Theorem 2 part 1: "An increase in the amount of noise trading increases
economic efficiency (∂P/∂σ ≥ 0) if V is convex and reduces economic efficiency (∂P/∂σ ≤ 0) if V is
concave." That is the same convexity-signed monotonicity in noise, and their route is a
mean-preserving spread in the Gaussian distribution of the market maker's posterior mean followed
by Jensen's inequality, not a kernel between two discrete experiments. Nothing found orders a
discrete order-flow experiment by noise intensity in the garbling sense. **Sentence this changes:**
the paragraph that introduces the garbling lemma cites Blackwell (1953) for the equivalence it
uses and Ganuza and Penalva (2010) for the dispersion route, and says that the finance precedent
for the same convexity-signed monotonicity is Back et al. (2018), whose route is a Gaussian
mean-preserving spread, while the lemma here writes the kernel explicitly at order size two so the
ordering holds on the five-valued order-flow experiment without a normality assumption.

## Question 3: who has split the 13D run-up from the filing-day jump by liquidity?

Nobody, on the evidence read. Collin-Dufresne, Pierre, and Vyacheslav Fos, "Do Prices Reveal the
Presence of Informed Trading?", *Journal of Finance* 70(4), 2015, 1555 to 1582, doi
10.1111/jofi.12260, working paper text at https://www.nber.org/papers/w18452, does document both
pieces, a positive and significant pre-filing run-up measured from sixty days before the filing
date to one day before it, and a positive and significant two-day jump at the filing date, and it
is the paper that ties activist accumulation to liquidity: "on days when activists accumulate
shares, measures of adverse selection and of stock illiquidity are lower, even though prices are
positively impacted." But their liquidity comparison runs in event time within a campaign, days on
which the filer trades against days on which it does not, and against matched stocks. They never
sort campaigns by pre-trigger liquidity and report the run-up and the jump separately across those
groups. The only sample splits in the paper are by profit quintile and by listing venue. Gantchev,
Nickolay, and Chotibhak Jotikasthira, "Institutional Trading and Hedge Fund Activism", *Management
Science* 64(6), 2018, 2930 to 2950, doi 10.1287/mnsc.2016.2654, puts liquidity at the centre of the
accumulation but on the other side of the question: institutional liquidity sales are what let the
activist camouflage purchases and are what times the campaign. The object measured is targeting and
timing, not the split of the revaluation. Duong, Truong, Shaoting Pi, and Travis R. A. Sapp,
"Betting on my enemy: Insider trading ahead of hedge fund 13D filings", *Journal of Corporate
Finance* 93, 2025, doi 10.1016/j.jcorpfin.2025.102794, is the recent paper that dates the pre-filing
window and reports a 13D announcement abnormal return of 7.72 percent, and it attributes part of the
pre-filing move to informed buying by corporate insiders rather than to the filer's own order flow.
It conditions on insider trading and on whether the activist talked to management, not on liquidity.
**Sentences this changes:** the paragraph placing E2 says that the existing work links liquidity to
the accumulation and to the choice and timing of the target, and measures the run-up and the jump
without conditioning either on pre-trigger liquidity, so sorting campaigns by pre-trigger Amihud
illiquidity and reporting the two pieces separately is the measurement E2 adds; and the sentence
reading E2's results notes that the run-up carries informed trading by parties other than the
filer, which the exercise measures together with the filer's own, since it is a descriptive split
of the total revaluation and separates no source.
