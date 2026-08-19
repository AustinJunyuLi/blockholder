# Celentano & Levine (2025) — "Shareholder Activism, Takeovers, and Managerial Discipline"

**Venue / status:** **Swiss Finance Institute Research Paper No. 25-81**, dated 24 October 2025 · **Revise & Resubmit, *Review of Financial Studies*** · Semifinalist, Best Paper in Corporate Finance, FMA 2025. Affiliations: Univ. of Lausanne & SFI (Celentano); Univ. of Wisconsin–Madison (Levine). *(Venue confirmed 2026-08-19 from external metadata — see §9b. Neither the series number nor the R&R appears anywhere in the 62-page PDF read; both are sourced from the SFI catalogue entry <https://www.sfi.ch/en/publications/n-25-81-shareholder-activism-takeovers-and-managerial-discipline>, the RePEc/IDEAS record <https://ideas.repec.org/p/chf/rpseri/rp2581.html>, and Oliver Levine's own faculty page <https://oliverlevine.com/>.)*
**PDF read:** the working paper **dated October 1, 2025** on its own title page — i.e. **not** necessarily the 24-Oct-2025 SFI deposit, and SSRN records a later revision (17 Nov 2025) that was not obtained. **Every page cite below is to the 1-Oct-2025 PDF.**
**Full text from:** `lit/celentano-levine-2025-ssrn.pdf` (62 PDF pp.), re-extracted with `pdftotext -layout` · **Reader:** opus · **Read:** full text, 54 printed pp. + 7 pp. Internet Appendix
**Page numbering used below:** the working paper's own printed page numbers (footer), i.e. printed p. *n* = PDF p. *n+1* for the main text (pp. 1–54); the Internet Appendix restarts its own numbering (cited as "IA p. n", PDF pp. 56–62). Ligatures and en/em dashes normalised to ASCII in quotes; all other characters verbatim.
**Type:** structural (dynamic model + SMM estimation)   **Role for us:** competitor (direct)

## 1. Question

Do shareholder activism and takeovers *substitute* for each other as disciplinary devices, or do they *complement* each other, and what is the net equilibrium effect of activists on M&A volume and on shareholder value? The authors argue the sign is ex-ante ambiguous — activists facilitate deals by reducing board entrenchment, but they also improve managerial effort, which raises the standalone value of the firm and so shrinks takeover surplus. They build and structurally estimate a dynamic model to quantify both channels at once, and to split activist announcement returns into selection (private information) and treatment (intervention).

## 2. Model / data and method

**Primitives and state space.** Discrete time, infinite horizon, risk-neutral agents, common discount factor β = 0.952. One firm (manager + board), one potential activist, one potential acquirer. Profits `π_t = z_t k_t^α − c_k k_t`; capital is static (no adjustment cost or lag). **The only endogenous state variable is firm productivity `z_t`**, following `exp{ln z_{t+1}} = exp{(1−ρ_z)μ_z + ρ_z ln z_t + σ_z ε_{t+1}} + e_t p_t` (p. 9). Two i.i.d. per-period shocks: project quality `p_t ~ Exp(λ_p)` and acquirer quality `w_t ~ Exp(λ_w)`. The activist sees two noisy signals `s_{t,x} = x_t + σ_x η_{t,x}`, x ∈ {p, w} (eq. 3, p. 9), *before either shock is public*: `p_t` is drawn and revealed to the manager at the start of the period but reaches the market only after entry, and `w_t` is revealed to acquirer and board only in the takeover phase (pp. 9, 12). (verifier: the card previously said "before the shocks are realised", which is not what the paper does.) Decisions in order: activist entry `ν_t ∈ {0, ν̄}` → manager effort `e_t ∈ {0,1}` → board turnover `f_t ∈ {0,1}` → `z_{t+1}` realised → acquirer/board learn `w_t`, bargain over `P_t`, takeover `a_t ∈ {0,1}` (Fig. 1, p. 35). Manager and board decisions carry Type-I extreme-value preference shocks (location 0, scale 1); tiny T1EV shocks are also added to activist entry and the takeover decision purely for numerical convergence, sized to move values by ~10⁻⁵ percent (IA p. 1).

**Trading, prices, liquidity — this is the load-bearing point for us.** There is **no trading stage, no market maker, no order flow, no noise trading, no price impact and no liquidity variable** anywhere in the model. The share price is simply the shareholder value function `V(z_t) = π_t + β E[a_t P_t + (1−a_t)V(z_{t+1}) | z_t]` (p. 13), which "updates in response to new information as it's revealed." The activist buys a *fixed* fraction `ν̄` at a cost `(1+ξ)(V(z_t) − π_t)ν_t` (p. 10). **Liquidity appears exactly once in the entire paper's model**, as one of three things bundled into the scalar entry-cost parameter ξ (Q1 below). After entry, "the campaign and private signals become public information and the share price updates" (p. 10) — disclosure is instantaneous, complete, and costless in the model.

**Takeover premia — bargaining, not auction.** The acquirer's surplus is `V(w_t) − P_t`; the board's is `(1 − c_m(ν_t))P_t − V(z_{t+1})`, where `c_m(ν_t)` is board entrenchment (p. 12). Price is set by **Nash bargaining** with acquirer bargaining power θ_a (Q3), giving `P_t = (1−θ_a)V(w_t) + θ_a V(z_{t+1})/(1 − c_m(ν_t))` (p. 13). θ_a is **calibrated to 0.5**, not estimated ("Bargaining in merger negotiations assumes equal power between the target and acquirer", p. 16). There is no bidder entry margin: a single potential acquirer arrives every period with exogenous quality `w_t`; no auction, no competing bidders, no toehold.

**Data.** 2001–2019, US public firms, **52,666 firm-year observations** (Table 1, p. 40). CRSP/Compustat annual, dropping non-US, utilities (SIC 4900–4999), financials (6000–6999), quasi-governmental (9000–9999). M&A bids from SDC Platinum mapped via Ewens's SDC-to-Compustat crosswalk → **2,194 bids (4.2% of firm-years)** (p. 15). Activism from **Audit Analytics initial Schedule 13D filings** (amendments excluded, >50% owners dropped, first filing only within any 12-month window) → **2,083 campaigns (4.0% of firm-years)** (p. 15). Hedge-fund classification from Alon Brav's data (2001–2014, 1,374 HF campaigns = 87% of campaigns in that window). CEO turnover/compensation from Equilar (turnover rate 8.5%/yr).

**Measurement.** Bid premium = bid price ÷ CRSP price **25 days before the bid** (1 day after any intervening turnover/campaign), truncated to [0,1]; sample mean **36.6%** (33.2% with an activist present) (pp. 15–16, Table 1). Activist entry return = market-adjusted CAR over **[−30, +1]** around the 13D filing; sample mean **4.4%**.

**Estimation.** Simulated method of moments (Lee–Ingram), K = 20 simulations, weight matrix = inverse covariance of empirical moments via Erickson–Whited influence functions with the 2012 correction, minimised by a global genetic algorithm (IA p. 1). SEs follow Nikolov–Whited (2014) / Bazdresch et al. (2018) (IA p. 1) and are **clustered at the firm level** — that clustering statement is in the Table 3 note, p. 42, not in the IA (corrected by verifier). **12 parameters estimated against 15 moments.** Pre-set: α = 0.7, β = 0.952, c_k = 0.20, μ_z normalised, θ_a = 0.5, θ_d = 1.6%, and **ν̄ = 5%, taken directly from the 13D threshold** (Q6). Identification argument (§3, pp. 16–19): asymmetric mean-reversion in log sales → `c_e`; turnover frequency → `c_f(0)`; turnover frequency | activist → `c_f(ν̄)`; entry return → ξ; entry frequency → σ_w, σ_p; **mean bid premium and mean bid premium | activist → `c_m(0)` and `c_m(ν̄)`**; takeover frequency → λ_w. Elasticity plots supporting identification are in IA Figs. B.1–B.5 (IA pp. 3–7).

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Board's private cost of CEO turnover = 2.072 × profits without an activist, 1.618 with (a ~22% reduction) | ESTIMATED (SE 0.331; 0.296) | Table 3, p. 42; text p. 19–20 |
| R2 | Board's private cost of takeover = 15.1% of firm value without an activist, 13.5% with (11%, 1.6 pp reduction) | ESTIMATED (SE 0.011; **0.047**) | Table 3, p. 42; text p. 20 |
| R3 | Activist entry cost ξ = 0.030, i.e. 3.0% of the pre-campaign market price of the shares acquired | ESTIMATED (SE 0.004) | Table 3, p. 42; text p. 20 |
| R4 | Signal-to-noise ratio 3.2% for acquirer quality, 14.6% for project quality | ESTIMATED (derived from λ̂, σ̂) | p. 19 & fn. 10 |
| R5 | **An activist campaign raises the probability of takeover by 7.70% (12.46% → 11.57% counterfactual); ~7% of deals during a campaign are marginal to it** | NUMERICAL (model counterfactual at θ̂; **no SE reported**) | Table 4 Panel A, p. 43; text p. 22 |
| R6 | **Bid premium of completed deals is 13.69% (5.2 pp) lower with an activist present: 32.90% vs a no-activist counterfactual of 38.12%** | NUMERICAL (model counterfactual at θ̂; **no SE reported**) | Table 4 Panel A, p. 43; text p. 22 |
| R6b | **(added by verifier) In *general equilibrium* the premium effect is an order of magnitude smaller: economy-wide bid premium 36.70% with activists vs 36.92% without — a change of −0.60%.** R6's −13.69% is the *marginal* effect conditional on a campaign, not the equilibrium effect of activists existing | NUMERICAL (no SE) | Table 5 col (1) vs col (4), p. 44 |
| R7 | Net M&A-channel shareholder gain = +0.44% conditional on activist & takeover (+1.23% from higher deal probability, −0.78% from lower premium); +0.06% across all campaigns; bimodal: +15.7% on the 7.2% marginal deals, −0.75% on the other 92.8% | NUMERICAL | Table 4, p. 43; text pp. 22–23 |
| R8 | Effort channel: campaign raises P(effort) 30.76%, productivity 1.17%, shareholder value 0.35% | NUMERICAL | Table 4 Panel B, p. 43 |
| R9 | **Crowding out: the effort-incentive channel alone cuts takeover volume by 0.79%; the facilitation channel alone raises it 0.64%; the two net to −0.05% — takeover volume is essentially unchanged by the presence of activists** | NUMERICAL | Table 5 cols (2)(3)(4), p. 44; text pp. 24–25 |
| R10 | Threat of activism raises target shareholder value 0.33% economy-wide; aggregate target surplus −0.36%, acquirer surplus +0.22%, total M&A surplus −0.16% | NUMERICAL | Table 5, p. 44 |
| R11 | Removing takeovers entirely cuts shareholder value 26.64% and raises turnover-given-activism 69.23% | NUMERICAL | Table 6 col (2), p. 45 |
| R12 | Announcement return decomposition: total 4.07%, of which selection 3.69% (90.8%) — acquirer signal 3.10% (76.3%), project signal 0.59% (14.4%) — and treatment 0.38% (9.3%), of which effort 0.36% and takeover facilitation only 0.02% | NUMERICAL | Table 7, p. 46 |
| R13 | Killing the acquirer signal cuts activist entry 88.26%; killing both signals ends entry entirely and costs shareholders 0.32% of value | NUMERICAL | Table 8, p. 47 |
| R14 | **Policy experiment on the cost of activism**: ξ ±20% moves activist entry +72.18% / −41.06% and target shareholder value +0.28% / −0.15% | NUMERICAL | Table 9, p. 48 |
| R14b | **(added by verifier) Raising the cost of activism ξ makes activists demand a stronger signal before entering, so takeover-conditional-on-activism *rises* 11.10% (and falls 11.93% when ξ is cut). The scalar cost margin therefore works on control outcomes through activist *selection*, not only through entry volume** | NUMERICAL | Table 9, p. 48; text pp. 30–31 |
| R15 | Hedge-fund subsample: friction reductions 38.8% (turnover) and 8.3% (takeover) vs 36.5% / 7.5% in the matched all-activist 2001–2014 sample | ESTIMATED (SEs in table) | Table 10 cols (1)(2), p. 49; text p. 31 |
| R16 | Over time: takeover-friction reduction 0% (2001–2009) → 15.6% (2010–2019); acquirer signal-to-noise 3.2% → 5.4%. **(added by verifier) But the turnover-friction reduction *fell*, 35.3% → 28.9%, and the project signal-to-noise went from economically insignificant to 13.1% — efficacy improves only on the takeover leg** | ESTIMATED | Table 10 cols (3)(4), p. 49; text p. 32 |
| R17 | Severance pay (2.3% of profits, Rau–Xu method) has only negligible effect on estimates | ASSERTED ("In untabulated results…") | p. 32 |
| R18 | Model matches non-targeted moments: distributions of profit growth / profitability for activist, takeover and turnover targets, and the bid-premium histogram | NUMERICAL | Figs. 4–5, pp. 38–39 |

## 4. Institutional facts used

- **Schedule 13D 5% threshold** — used *only* to calibrate the activist's stake: "The size of the activist stake (ν̄) is set to the statutory disclosure threshold of 5 percent" (p. 16, Q6). Nothing else in the model depends on it; ν̄ is a fixed scalar, not a choice.
- **13D initial filings as the activism event**, from Audit Analytics; amendments excluded; multiple same-target filings within 12 months collapsed to the first (wolf-pack) (p. 15).
- **No filing window anywhere.** The words "ten days", "five business days", "filing window" and "2024" (as a rule date) do not occur. The **2024-02-05 acceleration is never mentioned**, which is consistent with a sample ending in 2019.
- Event-classification rules: turnovers and bids within 2 years of a 13D are attributed to activism (following Boyson et al. 2017); campaigns and turnovers within 1 year *after* a bid are dropped (pp. 15–16).
- The **only** place regulation touches the model is the ξ policy experiment, and even there it is a list of unmodelled cost shifters (Q11).
- **(added by verifier) They cite the whole liquidity-and-activism theory literature once, in fn. 1 on p. 6, and use none of it**: "For example, Maug (1998), Kahn and Winton (1998), Mello and Repullo (2004), DeMarzo and Urošević (2006), Burkart and Lee (2015), Back et al. (2018), Levit (2019), Brav et al. (2022), Gorbenko and Malenko (2024), Gryglewicz et al. (2025a), and Gryglewicz et al. (2025b)." Outside that footnote the word "liquidity" appears in the body text exactly once (Q1); every other occurrence is a bibliography entry.
- **(added by verifier) "Bebchuk et al., 2013" in Q11 is Bebchuk, Jackson & Jiang, *Pre-disclosure accumulations by activist investors: evidence and policy* (J. Corp. L. 39).** They name the pre-disclosure accumulation window by title in their policy paragraph and model none of it.

## 5. Referee-facing strengths / weaknesses

**Strengths:** the crowding-out vs facilitation decomposition (Table 5) is a genuinely new object and cleanly executed — two channels can be switched on and off separately in the same estimated equilibrium. The paper takes acquirer surplus seriously as a welfare component, which most activism papers ignore. Non-targeted moments (Figs. 4–5) fit well. The selection/treatment split (Table 7) speaks directly to Albuquerque–Fos–Schroth and the paper is candid about disagreeing with them (p. 7). Subsample re-estimation (hedge funds, early/late) is more than most structural papers do. **(added by verifier)** They explicitly bill themselves as the empirical validation of three papers in our competitor set: "Our estimates of a significant facilitation role of activism in the M&A market provide empirical support for Corum and Levit (2019), Burkart and Lee (2022), and Burkart et al. (2024)" (p. 6) — so a position of ours that quarrels with Corum–Levit now has to answer their estimates too.

**Weaknesses / open flanks:**
1. **Every headline number is a counterfactual without a standard error.** Tables 4–9 — including the 13.7% premium effect and the 0.79% crowding-out — report no SEs or CIs. Only the 12 structural parameters (Table 3) carry inference. Given `c_m(ν̄) = 0.135 (SE 0.047)` versus `c_m(0) = 0.151 (SE 0.011)`, **the takeover-friction reduction that drives both the facilitation result and the premium result is not individually distinguishable from zero**; the whole facilitation leg rests on a 1.6 pp gap with a 4.7 pp standard error on one side.
2. **The premium result is definitional as much as behavioural.** With Nash bargaining and θ_a fixed at 0.5, `P_t` falls mechanically in `c_m(ν_t)`; lowering board entrenchment *must* lower the price. The paper concedes the denominator is doing work too: the pre-announcement price already contains ν_t and s_{w,t} (Q9), so the "13.7%" compares model prices under two different information sets as well as two different frictions.
3. **Liquidity and disclosure are labels on a scalar, not mechanisms.** ξ bundles price impact, information leakage *and* campaign costs into one number (Q1). Their own policy experiment then interprets ξ as the channel through which "trade block disclosure requirements" operate (Q11) — a disclosure rule with no partition, no window, and no trading stage behind it.
4. **Internal inconsistencies in reported magnitudes.** p. 28 gives the acquirer signal-to-noise as "3.0 percent" where p. 19 and Table 3 give 3.2%. p. 31 compares hedge-fund estimates to "the 36.5 and 7.5 percent reductions in the baseline estimation", but those come from Table 10 col. (2) (all activists, 2001–2014), not from the Table 3 baseline (21.9% and 10.6%) — "baseline" names two different things. σ_p in Table 10 cols. (1)–(3) is reported with SEs of 0.001 and 0.000, implausibly tight.
5. **No bidder entry margin.** One acquirer arrives each period with exogenous quality; the paper cannot speak to whether activism attracts or deters bidders, only to whether an already-arrived deal closes.
6. Two correlations (turnover and takeover with lagged performance) are matched with t-stats of 4.12 and 2.50 — i.e. rejected (Table 2, p. 41).
7. Sample ends 2019: nothing after the 2024 rule change, and the "efficacy over time" split (Table 10) stops before it.

## 6. What they do NOT do (scope boundary)

- **No trading, no price formation, no liquidity as a variable.** Liquidity is one clause inside one scalar parameter (Q1). There is no κ, no noise trader, no order flow, no Kyle/Glosten-Milgrom market. "Kyle", "Amihud", "market maker", "noise trading", "order flow", "bid-ask" do not occur in the paper.
- **No disclosure-rule margin at all.** The 5% threshold is a calibration constant (Q6); the filing *window* is absent; the 2024-02-05 acceleration is never mentioned. Their only regulatory lever is the scalar cost ξ, and they park the underlying rules in a list: Q11.
- **No within-campaign escalation or staged costs — explicitly declared out of scope**: "Modeling the marginal costs of each stage of an activist campaign, and the activists' decision to escalate a campaign, is beyond the scope of this paper. See Gantchev (2013) and Johnson and Swem (2021) for studies that provide estimates of these within-campaign marginal costs and choices." (p. 10, fn. 5 — Q2)
- **No stake choice.** ν_t is binary, {0, 5%}; there is no accumulation path, no partial position, no exit.
- **No takeover auction, no bidder entry, no target/acquirer complementarities** — the last of these is conceded on p. 21 ("does not explicitly model complementarities between the target and acquirer assets").
- **No proxy fight, no settlement, no campaign tactics.** Activism is a single binary entry that shifts two friction parameters.
- **Identification is structural only** — SMM on 2001–2019 moments. There is no quasi-experiment, no event study beyond the CAR moment, no DiD, no policy shock.

## 7. Implications for our position

**What they occupy.** Object: takeover volume, bid premium, CEO turnover, shareholder value — *jointly*, in general equilibrium. Margin of the disclosure rule: **none** (threshold used only as a calibration number; window absent). Identification: **structural (SMM), 2001–2019, no design-based variation.** Their "liquidity" is a clause inside a scalar entry cost.

**How this constrains us.**
1. **The premium object is now taken, but only in their sense.** Any claim of ours about the takeover premium must acknowledge R6: they already report a signed, quantified activism→premium effect. Our differentiation cannot be "activism moves premia" — it has to be *what moves the premium*: for them it is board entrenchment `c_m(ν)` under fixed-θ_a Nash bargaining; for us it is the market's **partition** (flagged vs pooled) interacting with **κ**. Those are different objects and we should say so in one sentence.
1b. **(added by verifier) Their premium result is much weaker in general equilibrium than the headline suggests (R6b): −0.60%, not −13.7%.** The −13.7% is conditional on a campaign having happened. If our object is the economy-wide premium, the number to beat is 0.60%, and it is a counterfactual with no SE resting on a friction gap whose one side has a 4.7 pp standard error.
1c. **(added by verifier) Their ξ experiment already produces a control-outcome result through *selection* (R14b): make activism costlier and takeover-given-activism rises 11.10%.** That is the closest thing in the paper to our mechanism and it arrives with no market behind it — the cleanest place to say that a microfounded liquidity × partition model delivers the same comparative static from primitives rather than from a hand-moved scalar.
2. **Crowding out of disciplinary takeovers is claimed and quantified (R9): −0.79% from the effort channel, net −0.05%.** If our model produces a crowding-in or crowding-out result, it has to be stated against this number, and we should note that theirs is a *numerical* result with no SE, on parameters where one leg (`c_m(ν̄)`) is statistically weak.

**The whitespace they leave, in our vocabulary.**
- **Liquidity as a driving variable (κ) is entirely open.** They have no market at all. Their own ξ policy experiment (R14, Q11) is the cleanest possible invitation: they treat "trade block disclosure requirements" as a shifter of a scalar cost and show entry frequency swings ±40–72% in response. That is a reduced-form stand-in for exactly the mechanism we microfound.
- **The window margin is untouched by anyone in this paper.** The threshold is a calibration number; the window does not exist. Both the *threshold margin* and especially the *window margin* are free.
- **The partition is free.** In their model the activist's signals become common knowledge the instant she enters (p. 10) — there is no pooled state, so no partition, so no disclosure attenuation to speak of.
- **The Feb-2024 acceleration is free** with respect to this paper: sample ends 2019, rule never mentioned.
- **Design-based identification is free.** Everything they have is structural.
- **(added by verifier) Their own framing is a free-rider argument, which is our language too.** p. 29: activist private information "is analogous to the classic free-rider problem in corporate takeovers (Grossman and Hart, 1980)… An information advantage for the activist improves the outcomes of target shareholders by helping to overcome this free-rider problem." A disclosure rule that changes *what the market learns and when* is a direct lever on exactly that information advantage — they set the problem up and then hand it to a scalar.
- Note their information result cuts *toward* us: 76.3% of the activist announcement return is the acquirer signal (R12). A model in which the blockholder's private signal about control value is what the disclosure rule reveals is well aligned with their own estimated decomposition — we can cite them as corroboration rather than fighting them.

**One-line index.** WP Oct-2025 · object: takeover volume + bid premium + turnover in GE · margin: none (5% threshold used only to calibrate the stake; no window) · identification: structural SMM 2001–2019 · so-what: they own the activism→premium sign but with no market, no partition and no window, so κ × partition × window is untouched.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "For example, the term ξV (zt )νt reflects the costs arising from limited liquidity and information leakages associated with large share purchases as well as expected campaign costs." | p. 10 | **The entire "liquidity" content of the paper.** Pin down that liquidity is one clause inside a scalar entry cost, not a variable. |
| Q2 | "Modeling the marginal costs of each stage of an activist campaign, and the activists' decision to escalate a campaign, is beyond the scope of this paper." | p. 10, fn. 5 | Explicit scope declaration. |
| Q3 | "The board and potential acquirer negotiate a takeover price Pt via Nash bargaining with acquirer bargaining power of θa ." | p. 12 | Premia are set by bargaining, not auction; θ_a calibrated to 0.5. |
| Q4 | "Table 4 shows that in takeovers with an activist present, the bid premium is 13.7 percent (5.2 percentage points) lower than if the activist had not been present." | p. 22 | The headline premium result, exact statement. |
| Q5 | "All of the reduction in bid premium is due to activist intervention because the pre-announcement share price used to calculate the bid premium incorporates the activist's signal about a potential acquirer." | p. 22 | The denominator claim — they assert the selection effect is already priced out. |
| Q6 | "The size of the activist stake (ν̄) is set to the statutory disclosure threshold of 5 percent, which corresponds to the ownership threshold to file a Schedule 13D with the SEC." | p. 16 | The *only* use of the disclosure rule: threshold as a calibration constant. |
| Q7 | "Comparing Columns (1) and (2), we see that takeover activity declines 0.79 percent when activists are present in the economy." | p. 24 | Crowding-out magnitude. |
| Q8 | "We see that takeover volume is roughly unchanged by the presence of activists, as the crowded out takeover activity from the activists effort incentives is roughly offset by their facilitation role." | p. 25 | The net-zero headline. |
| Q9 | "Analogous to the data, in the model the bid premium is calculated as the takeover price, Pt , relative to the price just prior to the takeover announcement." | p. 18, fn. 9 | The premium denominator in the model. |
| Q10 | "We compute an activist's return upon entry as the cumulative abnormal return for the target firms from 30 days before the filing of a Schedule 13D form to 1 day after using the market-adjusted model." | p. 16 | The CAR window they use — [−30,+1], i.e. it straddles the pre-filing accumulation window without modelling it. |
| Q11 | "Examples include trade block disclosure requirements (Bebchuk et al., 2013; Back et al., 2018), universal proxy regulations (Hirst, 2018), and anti-activist poison pills (Eldar et al., 2023)." | p. 30 | Their entire treatment of the disclosure rule: a list of things that shift the scalar ξ. Our opening. |
| Q12 | "When an activist is present, this cost is reduced by 11 percent (1.6 percentage points), a meaningful reduction in the agency frictions to takeover." | p. 20 | The facilitation parameter — compare to SE 0.047 on c_m(ν̄). |

| Q13 | "Our estimates of a significant facilitation role of activism in the M&A market provide empirical support for Corum and Levit (2019), Burkart and Lee (2022), and Burkart et al. (2024)." | p. 6 | *(added by verifier)* They claim the structural-empirical ground under three of our competitor-set theory papers. |
| Q14 | "For example, Maug (1998), Kahn and Winton (1998), Mello and Repullo (2004), DeMarzo and Urošević (2006), Burkart and Lee (2015), Back et al. (2018), Levit (2019), Brav et al. (2022), Gorbenko and Malenko (2024), Gryglewicz et al. (2025a), and Gryglewicz et al. (2025b)." | p. 6, fn. 1 | *(added by verifier)* The entire liquidity-and-activism theory literature, cited once and used nowhere. |
| Q15 | "This is analogous to the classic free-rider problem in corporate takeovers (Grossman and Hart, 1980), as the costs of the campaign are borne solely by the activist, but the benefits are shared by all shareholders, leading to inefficiently low activism." | p. 29 | *(added by verifier)* Their own free-rider framing of the information channel. |
| Q16 | "When costs are higher, activists require a higher signal in order to launch a campaign." | p. 30 | *(added by verifier)* The selection reading of the ξ experiment (R14b) — a cost margin acting on control outcomes through who enters. |

## 9. Verification log

**Verifier: opus, 2026-08-19. Method:** every page of `lit/celentano-levine-2025-ssrn.pdf` re-extracted one page at a time (`pdftotext -f N -l N -layout`) into a page-marked file, then Unicode-normalised (NFKD + ligature/dash folding) and whitespace-collapsed before matching. Every quote, every number and every negative claim below was matched against that file, not against the reader's `research/txt/` copy. Page mapping independently re-derived from the printed footers: **printed p. n = PDF p. n+1** for pp. 1–54; IA = PDF pp. 56–62 = printed IA 1–7. Confirmed.

**Counts: 16 OK · 1 WRONG · 1 MISCITED · 1 UNCHECKED.**

**Quotes (§8).** Q1–Q12 all **OK** — verbatim text and printed page both confirmed: Q1 p. 10 (PDF 11), Q2 p. 10 fn. 5 (PDF 11), Q3 p. 12 (PDF 13), Q4 p. 22 (PDF 23), Q5 p. 22 (PDF 23), Q6 p. 16 (PDF 17), Q7 p. 24 (PDF 25), Q8 p. 25 (PDF 26), Q9 p. 18 fn. 9 (PDF 19), Q10 p. 16 (PDF 17), Q11 p. 30 (PDF 31), Q12 p. 20 (PDF 21). Q13–Q16 added by the verifier and matched the same way (pp. 6, 6 fn. 1, 29, 30).

**Results (§3).** All 18 re-read against the print; every number matches to the digit and every honesty label holds.
- R1 **OK** — Table 3 p. 42: 2.072 (0.331), 1.618 (0.296); 21.9% ✓ ("22 percent", p. 20).
- R2 **OK** — Table 3 p. 42: c_m(0) = 0.151 (**0.011**), c_m(ν̄) = 0.135 (**0.047**). The weak-leg claim in §5 stands: 1.6 pp gap, 4.7 pp SE on one side.
- R3 **OK** — ξ = 0.030 (0.004), Table 3 p. 42; "3.0 percent of the pre-campaign market price" p. 20.
- R4 **OK** — 3.2% / 14.6%, p. 19 + fn. 10; recomputed (1/2.285²)/2.438² = 3.22%, (1/11.909²)/0.220² = 14.57%.
- R5 **OK** — Table 4 Panel A p. 43: 12.46 / 11.57 / 7.70; "about 7 percent of successful deals" p. 22. **No SE anywhere in Table 4** — confirmed by reading the whole table.
- R6 **OK** — Table 4 Panel A p. 43: **32.90 vs 38.12, change −13.69**; text p. 22 "13.7 percent (5.2 percentage points)". **No SE** ✓.
- R6b **added by verifier** — Table 5 p. 44 gives the equilibrium premium as 36.70 (baseline) vs 36.92 (no activism), i.e. −0.60%. The card reported only the marginal −13.69% and would have overstated what they own.
- R7–R14 **OK** — Tables 4–9, pp. 43–48; every figure re-read (+0.44 / +1.23 / −0.78 / +0.06; 15.7% on 7.2% marginal deals and −0.75% on 92.8%, p. 23; −0.79 / +0.64 / −0.05; 0.33 / −0.36 / +0.22 / −0.16; −26.64 / 69.23; 4.07 = 3.69 + 0.38 with 3.10 / 0.59 and 0.36 / 0.02; −88.26 and −100.00 with −0.32; +72.18 / −41.06 and +0.28 / −0.15).
- R14b **added by verifier** — Table 9 p. 48 rows "Frequency of takeover | activist" −11.93 / +11.10, explained on p. 30 ("activists require a higher signal in order to launch a campaign"). The card had the entry-volume half of the ξ experiment and not the selection half.
- R15–R16 **OK**, R16 incomplete → **fixed**. Table 10 p. 49 recomputed: HF 2.570→1.572 = 38.8% and 0.144→0.132 = 8.3%; all-activist 2001–2014 2.552→1.621 = 36.5% and 0.146→0.135 = 7.5%; early 0.184→0.184 = 0%, late 0.186→0.157 = 15.6%. The card omitted that the *turnover*-friction reduction **falls** 35.3% → 28.9% (p. 32) — added.
- R17 **OK** — "In untabulated results", 2.3% of profits via Rau–Xu (2013), p. 32.
- R18 **OK** — Fig. 4 printed p. 38 (PDF 39, the page with no footer), Fig. 5 printed p. 39 (PDF 40).

**Scope claims (§6) — all confirmed by exhaustive search of the full 62-page extraction.** Zero occurrences of: Kyle, Amihud, "market maker", "order flow", "bid-ask", "ten days", "five business", "filing window", "price impact", "trading volume", "toehold", "auction", "competing bid". "Liquidity" occurs 6 times: **once in the body (p. 10, Q1)** and 5 times in the bibliography. "Noise" occurs 14 times and is *always* signal noise (σ_w, σ_p). "Disclosure" occurs in the body exactly twice — p. 16 (Q6, the calibration) and p. 30 (Q11, the policy list). "2024" occurs only as a citation year. The card's negative claims hold as written.

**Venue / status (header) — ~~UNCHECKED~~ CLOSED 2026-08-19, see §9b.** The PDF front matter carries no series number and no R&R line; the only SFI strings are the affiliation "University of Lausanne and Swiss Finance Institute" (title page) and "SFI Research Days" in the acknowledgements footnote (p. 1). So "SFI Research Paper 25-81, R&R at RFS" is **not in the paper** — the verifier was right about that. It **is** confirmed from external catalogue metadata; the header now carries the sources.

**Omissions found and added:** (a) the GE premium effect −0.60% vs the marginal −13.69% (R6b) — the most consequential, since it changes how much of the premium object they actually own; (b) the ξ→selection channel (R14b), their closest approach to our mechanism; (c) the turnover-efficacy *decline* over time (R16); (d) fn. 1 p. 6, where the whole liquidity-activism theory literature is cited and used nowhere (§4, Q14); (e) that "Bebchuk et al., 2013" inside Q11 is the *pre-disclosure accumulations* paper — they name our object by title (§4); (f) p. 6, they bill themselves as empirical support for Corum–Levit, Burkart–Lee and Burkart et al. (§5, Q13); (g) the Grossman–Hart free-rider framing of their information channel, p. 29 (§7, Q15).

**Corrections applied:** §2 signal timing ("before the shocks are realised" → before either shock is *public*; p_t is realised at the start of the period, p. 9) — **WRONG**, fixed. §2 SE clustering attributed to IA p. 1 — **MISCITED**, the clustering statement is the Table 3 note, p. 42; fixed. §2 bid/campaign counts given a page (p. 15).

**Overall verdict: the card is sound.** Every quote and every reported number survives an adversarial re-read, and the load-bearing negatives (no market, no window, no partition) are confirmed by exhaustive search. The one substantive gap was that it reported the marginal premium effect without its much smaller general-equilibrium counterpart.

Reader's own checks already run:
- All 12 quotes above were string-matched against a fresh `pdftotext -layout` extraction of `lit/celentano-levine-2025-ssrn.pdf` after normalising whitespace and ligatures; all 12 matched.
- Page mapping verified by reading the printed footer on every page: printed p. n = PDF p. n+1 for pp. 1–54 (PDF p. 39 carries no footer; it is printed p. 38 by position). Internet Appendix = PDF pp. 56–62, printed IA 1–7.
- Arithmetic cross-checks: (38.12 − 32.90)/38.12 = 13.69% ✓ and 5.22 pp ✓; (2.072 − 1.618)/2.072 = 21.9% ✓ (text "22 percent"); (0.151 − 0.135)/0.151 = 10.6% ✓ (text "11 percent"); (1/2.285²)/2.438² = 3.22% ✓ (text "3.2 percent" p. 19, but "3.0 percent" p. 28 — flagged).
- ~~**Open for the verifier:** the venue claim.~~ **CLOSED 2026-08-19 (§9b).** SFI Research Paper No. 25-81 and the RFS R&R are both confirmed from external metadata; the paper text still states neither, so cite the SFI/RePEc/author-page sources, never the PDF, for the venue.


## 9b. Metadata supplement-reader log — 2026-08-19

**Item closed:** the header's venue/status line (the single UNCHECKED item in §9).
**Source:** `research/txt_extracts/FETCH_LOG_C.md`, row `celentano_levine_2025_metadata` (status "OK (metadata only)"). No new full text
was fetched; nothing in §§1–8 of this card is affected, and **every page cite in this card still points at the 1-Oct-2025 PDF**.

| Claim | Verdict | Source, verbatim from the fetch log |
|---|---|---|
| **Swiss Finance Institute Research Paper No. 25-81** | **CONFIRMED, two independent catalogues** | SFI: <https://www.sfi.ch/en/publications/n-25-81-shareholder-activism-takeovers-and-managerial-discipline> — "N°25-81 … Authors F. Celentano, O. Levine. Date 24 Oct. 2025. Category Working Papers". RePEc: <https://ideas.repec.org/p/chf/rpseri/rp2581.html> — "Swiss Finance Institute Research Paper Series 25-81, Swiss Finance Institute" |
| **Revise & Resubmit, *Review of Financial Studies*** | **CONFIRMED from the author's own site** | <https://oliverlevine.com/>, under Working Papers: "Revise & Resubmit, Review of Financial Studies" |
| Semifinalist, Best Paper in Corporate Finance, FMA 2025 | **CONFIRMED, same source** | <https://oliverlevine.com/> |
| A newer version exists | **YES, and it was NOT obtained** | SSRN listing (seen only via a Google snippet, SSRN itself not opened) shows "Last revised: 17 Nov 2025". No open-access newer PDF was found; Celentano's Google Sites page timed out |

**Two cautions this creates (added by supplement reader):**
1. **Three dates are now in play** — the read PDF's own title-page date **1 Oct 2025**, the SFI deposit date **24 Oct 2025**, and
   SSRN's **last revised 17 Nov 2025**. They may or may not be the same document. Until the 17-Nov version is in hand, no page
   number in this card should be cited as "Celentano and Levine (2025), p. n" without naming the 1-Oct-2025 version, and no
   estimate quoted from §3 should be assumed to survive into the R&R'd manuscript.
2. **This is now the competitor with a *stronger* placement than the card implied.** An RFS R&R on the direct competitor raises
   the bar for the whitespace claim: whatever position we take must be defensible against a paper a top-3 journal has already
   sent back for revision, not against an unplaced working paper. Deliverability arguments that assumed "they are only at
   working-paper stage" should be dropped.

**Counts after this pass: UNCHECKED 1 → 0.** No result, quote or page in §§1–8 was touched.
