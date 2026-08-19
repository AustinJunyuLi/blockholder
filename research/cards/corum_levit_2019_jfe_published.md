# Corum & Levit (2019) — "Corporate control activism"

**Venue / status:** *Journal of Financial Economics* 133(1), 1–17, 2019. Received 24 August 2017; revised 29 May 2018; accepted 11 June 2018; available online 6 February 2019. doi:10.1016/j.jfineco.2019.02.001. **This card reads the PUBLISHED version.** An earlier card (`corum_levit_2019_wp2016_superseded.md`) was written from the Aug-2016 working paper; see §10 below for what changed.
**Full text from:** `research/txt_extracts/corum_levit_2019_jfe_published.pdf` (+ `.txt`) · **Reader:** opus · **Read:** full text, 17 pages (all of §§1–5, Appendices A, B, C, footnotes 1–31, references)
**Page numbering:** printed journal pages 1–17. These coincide exactly with PDF page index 1–17. Quotes were checked against page images rendered at 150 dpi (`pdftoppm`), because `pdftotext -layout` interleaves the two columns and `pdftotext -raw` silently drops two glyphs — Δ (the synergy) renders as a control byte and the macron on ᾱ is lost, so ᾱ and α are indistinguishable in both text extracts. Every ᾱ/α distinction in this card was read off the page image.
**Type:** theory (pure; one 232-observation descriptive statistic) **Role for us:** competitor — the closest direct competitor in the set

**No Online Appendix / Internet Appendix / supplementary material is cited anywhere in the published article.** Everything the paper proves is in the 17 printed pages. (We do not hold one either, but there is no evidence one exists.)

---

## 0. SYMBOL WARNING — read before anything else

> **Their κ is the cost of running a proxy fight. Our κ is noise-trading intensity. These are unrelated.**
> p. 5: "If a proxy fight is initiated, the challenger incurs a non-reimbursable campaigning cost κ > 0."
> p. 12, fn 29: "κ is the cost of running a proxy fight".
> Their Prediction 7 ("the probability of a takeover is weakly decreasing in the cost of a proxy fight") reads, if you carry our κ across, as the *opposite* of a liquidity result. It is not a liquidity result at all. Every κ in this card is theirs unless flagged.

Full dictionary (theirs → ours, where a mapping exists):

| Theirs | Meaning in Corum–Levit | Our word |
|---|---|---|
| κ | non-reimbursable cost of launching a proxy fight | *(no counterpart; NOT our κ)* |
| ᾱ ("alpha-bar") | (a) largest order the market maker cannot price off, i.e. the point above which the stock stops being perfectly liquid; **and** (b) the disclosure threshold, "e.g., regulation 13D"; **and** (c) the poison-pill trigger. One scalar, three jobs. Calibrated ᾱ ∈ [5%, 10%] | threshold margin **and** liquidity, fused |
| α | the activist's actual stake; in the Section-4 equilibrium α* = ᾱ exactly | block size |
| Δ | synergy from the takeover when positive; x ∈ {Δ, −∞} | — |
| b ≡ B/n | incumbent's private benefit of control per share | — |
| γ | activist's private benefit from controlling the target *as an independent firm*; assumed γ < κ | — |
| s | probability the target board is the proposer = target bargaining power | — |
| τ | Pr[x = Δ] | — |
| c ~ f on [0,∞) | bidder's cost of due diligence | — |
| μ | Pr[y = 1], activist's private signal that a takeover is possible | — |
| δ ≡ γ + (κ − γ)/s | credibility cut-off for the activist's proxy-fight threat | — |
| π_z ≡ [sΔ + (1−s)z]·1_{z≤Δ} | expected takeover premium when the board's per-share private benefit is z | premium |
| θ* , θ** | probability of a takeover (θ** = μθ*(α*)) | control outcome |
| h* = θ*π* | expected target shareholder value | — |
| λ (App. B) | probability the board can still block after round II fails | — |

---

## 1. Question

Both bidders and activist hedge funds can, in principle, run a proxy fight to unseat a board that is blocking a sale. Empirically, only activists do — Fos (2017) finds 5% of 2003–2012 proxy fights were sponsored by corporations (p. 2, fn 3). Why? Corum and Levit answer that the bidder is the *counterparty* to the sale, so target shareholders will never hand him their board; the activist sits on the sell side, so they will. From that single asymmetry they derive the role of activists in the market for corporate control: activists are the mechanism that makes corporate assets available for sale. Two extensions then ask (i) when a proxy fight is launched *before* any bidder shows up, and (ii) whether the activist's stake causes the takeover ("treatment") or merely predicts it ("selection").

## 2. Model and method

Pure theory; Subgame Perfect Equilibrium in pure strategies (baseline), Perfect Bayesian Equilibrium in pure strategies (§4, p. 10 fn 26). All agents risk neutral, zero discounting.

**Players.** One bidder, one activist, passive shareholders (collectively > 50% of votes), one target run by an incumbent board. One share = one vote; shares normalised to 1 and perfectly divisible; acquisition requires ≥ 50% of votes (p. 4).

**Primitives.** Target standalone value normalised to 0. Post-acquisition value x ∈ {Δ, −∞}, Δ > 0, Pr[x = Δ] = τ ∈ (0,1). The bidder is initially uninformed; he may pay c ≥ 0 (drawn from a continuous density f with full support on [0,∞)) to learn x exactly. Incumbent owns n ≥ 0 shares, private benefit B > 0, per share b ≡ B/n. Activist owns α ≥ 0 shares, private benefit γ ≥ 0 from controlling the target *as an independent firm*, with γ < κ and the analysis focused on γ/α < b. Bidder holds **no** toehold in the baseline (p. 5) — see §6.

**Timing (Fig. 1, p. 4).** Bidder decides on due diligence → takeover negotiations round I (bidder vs. incumbent board) → shareholder vote → if disagreement/rejection, proxy-fight stage (bidder and activist decide *simultaneously* whether to run; challenger pays κ; shareholders elect) → round II (bidder vs. elected board) → vote → acquired or independent. In each round the proposer is the target board w.p. s and the bidder w.p. 1 − s, and makes a take-it-or-leave-it offer. Newly elected directors maximise the value of the party they are affiliated with; fiduciary duty is unenforceable, so neither bidder nor activist can commit (p. 5).

**Key tractability devices.** (i) x is binary and one branch is −∞, so the bidder never bids without due diligence. (ii) The board can *fully* block a tender offer in the baseline (poison pill, p. 4, fn 7); Appendix B relaxes this to partial blocking with probability λ. (iii) All payoffs collapse to the single index π_z ≡ [sΔ + (1−s)z]·1_{z≤Δ}, so "who controls the board" reduces to "what is that board's per-share private benefit z ∈ {b, γ/α, 0}".

**§3 extension.** The activist may run a proxy fight *before* the bidder arrives, not knowing c. Proxy fights then occur on the equilibrium path.

**§4 extension — the only place a market appears.** The activist privately observes y ∈ {0,1}, Pr[y=1] = μ; y = 0 ⇒ synergy = −∞ for sure. She submits an order for α ≥ 0 shares (no short sales) to a risk-neutral, competitive, uninformed **market maker**. Price = expected value conditional on total order flow, **but the market maker may condition on order flow if and only if the order strictly exceeds ᾱ ∈ (0,1)** (p. 10). There are **no noise traders and no noise-trading intensity** — the step at ᾱ is the entire market microstructure. In equilibrium α* = ᾱ exactly (a corner). After trading the activist's ownership becomes public unconditionally; then the bidder, who observes the stake, y and c, moves.

**Empirical exercise (p. 9).** FactSet SharkWatch, 232 proxy fights, 1994–2015, activist's stated goal = sell to a third party; "Using Center for Research in Security Prices (CRSP) data" *(corrected by verifier — the paper says CRSP data and "delisted due to an M&A event"; it never names delisting codes)*; 36% delisted via M&A within 24 months of announcement, against a 5% unconditional US takeover rate (Doidge et al., 2017). No regression, no standard error, no control group.

### How the disclosure threshold ᾱ actually enters — every mention, quoted

The rule appears in exactly one paragraph of body text, one footnote and two conditions. This is the complete set.

1. **p. 10** (the whole apparatus, one sentence at a time):
   - "For simplicity, we assume that the market maker can condition the price on the order flow if and only if the order is strictly larger than ᾱ ∈ (0, 1)."
   - "That is, the stock is perfectly liquid (illiquid) for small (large) orders."
   - "Parameter ᾱ can also be interpreted as a disclosure threshold (e.g., regulation 13D)."
   - "Moreover, buying up to ᾱ shares does not trigger a poison pill if such exists."
   - "Empirically, ᾱ ∈ [5%, 10%]."
   - "After trading, the activist's ownership in the target becomes public."
2. **p. 10, fn 23** (the demotion): "A previous version of the paper assumed the existence of liquidity traders a la Kyle (1985) and showed that similar results hold under this alternative formulation."
3. **p. 10, Prop. 5(i)–(ii)**: α* = ᾱ if y = 1 and either δ/ᾱ ≤ Δ < b or b < Δ, else 0; p*(α) = μh*(α*) if α ≤ ᾱ and h*(α*) if α > ᾱ.
4. **p. 11**: "To fully exploit her private information, the activist buys the maximum stake that keeps her trade concealed, that is, α* = ᾱ."
5. **p. 11, fn 27**: "Off equilibrium, if α > ᾱ, then the market maker assumes y = 1 and sets p = h*(α)."
6. **p. 11, §4.1**: "By contrast, if Δ < b and ᾱ ≥ δ/Δ, then the equilibrium exhibits treatment."
7. **p. 11, Cor. 2(i)**: "If b > Δ, then θ** is invariant to b, where θ** > 0 if and only if δ/ᾱ ≤ Δ."
8. **p. 14** (proof): the same condition, plus "if the activist buys more than ᾱ shares, which is an off-equilibrium event…".

**Is ᾱ a policy variable, a liquidity parameter, or both? — BOTH, and they are literally the same scalar.** This **confirms** the WP verifier's reading, and the published version is if anything more explicit about it: the same sentence that defines ᾱ as the liquidity break ("perfectly liquid (illiquid) for small (large) orders") is immediately followed by "Parameter ᾱ can also be interpreted as a disclosure threshold (e.g., regulation 13D)", and then by the poison-pill trigger. There is no separate liquidity parameter anywhere in the paper, and no separate disclosure parameter. A comparative static in ᾱ is simultaneously a liquidity comparative static, a disclosure comparative static and a takeover-defence comparative static — which is exactly why they never run one (see §3, R-none, and §5).

**Two structural facts about how the rule operates here, which matter for us:**
- **The flagged state is off the equilibrium path.** α* = ᾱ always; α > ᾱ never happens. p*(α) = h*(α*) is an off-equilibrium branch supported by the belief μ(α) = 1 (p. 14). So the *partition* the disclosure rule creates does no work on path — its only on-path role is to **cap the stake at ᾱ**.
- **Disclosure is unconditional and instantaneous.** "After trading, the activist's ownership in the target becomes public" (p. 10) — regardless of ᾱ, with no lag. ᾱ governs *price formation during* the trade, not *revelation after* it.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where |
|---|---|---|---|
| R1 | The bidder never starts a proxy fight — target shareholders anticipate he will lowball once he controls the board, so they never elect him. | PROVED | p. 6, Prop. 1 (argument in text, pp. 6) |
| R2 | The activist starts a proxy fight iff π_{γ/α} − π_b ≥ κ/α ⟺ δ/α ≤ Δ < b; if she starts it she wins it and sells at π_{γ/α} > 0. | PROVED | p. 6, Prop. 2; proof pp. 12–13 |
| R3 | Unique equilibrium. Bidder does due diligence iff min{b, δ/α} ≤ Δ and c ≤ τ(Δ − π*); on path the deal closes in **round I** at π* = π_b if b ≤ Δ, at π_{γ/α} if δ/α ≤ Δ < b. No proxy fight is ever observed. | PROVED | p. 7, Prop. 3; proof p. 13 |
| R4 | θ* is increasing in α, and h*(α) ≥ h*(0) for every α > 0 (shareholders are always weakly better off with the activist present). | PROVED | p. 7, Cor. 1 |
| R5 | With pre-emption allowed, a unique equilibrium exists; the activist fights *before* the bidder arrives iff Δ ≥ b **and** condition (8) holds. Proxy fights are then on the equilibrium path. | PROVED | pp. 8–9, Prop. 4; proof p. 13 |
| R6 | In the region where a pre-emptive fight occurs, condition (8) implies γ/α < b, hence **π_{γ/α} < π_b**: the activist wins and the target sells for a *lower* premium than the incumbent would have got — offset by a higher takeover probability. | PROVED | p. 9 (text) + p. 13 (proof) |
| R7 | Position building: α* = ᾱ if y = 1 and (δ/ᾱ ≤ Δ < b or b < Δ), else α* = 0; price p*(α) = μh*(α*) for α ≤ ᾱ and h*(α*) for α > ᾱ. Uniqueness needs a technical assumption. | PROVED, conditionally — fn 26 defers the assumption to the proof; p. 14 reveals it as "either γ = 0 or s is sufficiently close to one" | p. 10, Prop. 5; proof pp. 13–14 |
| R8 | Selection iff b ≤ Δ (activist predicts, does not cause); treatment iff Δ < b **and ᾱ ≥ δ/Δ** (activist causes). | PROVED | p. 11, §4.1 |
| R9 | θ** strictly decreasing in b on b ≤ Δ (zero at b = Δ); invariant to b on b > Δ, and there θ** > 0 iff δ/ᾱ ≤ Δ. θ** invariant to κ if b ≤ Δ; decreasing in κ if Δ < b. | PROVED | p. 11, Cor. 2; proof p. 14 |
| R10 | Appendix B (limited veto, board blocks only w.p. λ): the bidder still never runs a proxy fight; the activist runs one iff π_{γ/α} − π_b ≥ (κ/α)/λ, and the premium becomes (1−λ)φΔ + λπ_{γ/α}. | PROVED | p. 15, Prop. 6 + proof pp. 15 |
| R11 | Appendix C (bidder holds a toehold α and can raise standalone value without a majority): the bidder **does** run and win a proxy fight iff (κ/α)/(1−α) ≤ Δ/(1−α) < b. The impossibility in R1 is therefore specific to majority-only value creation. | PROVED | p. 16, Prop. 7 + proof p. 16 |
| R12 | 232 proxy fights (FactSet SharkWatch, 1994–2015) with stated goal of sale to a third party; 36% delisted for M&A within 24 months, vs. a 5% unconditional US takeover rate. | ESTIMATED — raw frequency; **no standard error, no CI, no control group, no regression reported**. The accompanying phrase "significantly larger than 5%" is ASSERTED (no test shown). | p. 9 |
| R13 | "Allowing the bidder to have a toehold will not change the main results." | ASSERTED (baseline; no proof. Appendix C studies a toehold bidder but in a *variant with no activist*, and there the conclusion flips — see R11) | p. 5 |
| R14 | A previous version with Kyle (1985) liquidity traders yields "similar results". | ASSERTED (no proof, no appendix, no online appendix; the reader cannot check it from the published article) | p. 10, fn 23 |
| R15 | Fig. 2: θ** against b (left) and against κ (right), showing the selection/treatment split, under γ = 0, c ~ U[0, c̄], c̄ ≥ τ(1−s)Δ, with δ/α < Δ (left) and Δ < b (right). | NUMERICAL — an illustration of Cor. 2 on a restricted parameterisation; the figure is schematic (axes marked 0, Δ and αsΔ only) and no grid, no solver output is reported | p. 12, Fig. 2 |
| R16 | **The takeover premium falls in the activist's stake.** "a higher α also implies that the activist puts less weight on her private benefits from controlling the target as an independent firm, which harms her ability to bargain a higher takeover premium (π_{γ/α} decreases in α)". Since α* = ᾱ (Prop. 5), this is a *stated* prediction that a higher disclosure threshold lowers the premium while raising the takeover probability (R4), with an ambiguous net effect on h*. | ASSERTED in text (the monotonicity of π_{γ/α} in α is immediate from Eq. (1); h*(α) ≥ h*(0) is the PROVED part) | p. 8 (text, immediately after Cor. 1) — **(added by verifier)** |
| R17 | **In the selection region (b ≤ Δ) the stake does nothing at all:** the proof of Prop. 5 shows "if b ≤ Δ, then h*(α) = θ_b π_b, which is independent of α". So ᾱ moves outcomes only where Δ < b — the treatment region. | PROVED | p. 14, proof of Prop. 5, fourth step — **(added by verifier)** |
| R-none | **There is no proposition, corollary or prediction whose statement is a comparative static in ᾱ.** ᾱ *does* appear in the statements of Prop. 5(i) (α* = ᾱ, the equilibrium stake level), Prop. 5(ii) (the kink of the price function p*(α) at ᾱ), Cor. 2(i) (θ** > 0 iff δ/ᾱ ≤ Δ) and §4.1 (treatment iff ᾱ ≥ δ/Δ) — *(second sentence corrected by verifier; the earlier text said ᾱ entered only the two region conditions, which understated Prop. 5)*. None of these is written as a derivative or a signed policy statement. **But note the near-miss:** on b > Δ, Cor. 2(i)'s "θ** > 0 if and only if δ/ᾱ ≤ Δ" is a discontinuous comparative static in ᾱ in all but name — raise ᾱ past δ/Δ and the takeover probability jumps from 0 to strictly positive. That θ** rises with ᾱ also follows in one line from R4 + α* = ᾱ. The paper never states either, never signs it as policy, and never mentions ᾱ in the conclusion. | — (absence, verified by reading all of §§2–5, Apps. A–C, Lemma 1, Props. 1–7, Cors. 1–2 and Predictions 1–7) | pp. 7, 10–12, 14 |

### The seven Predictions, verbatim

- **Prediction 1** (p. 9): "Proxy fights with a stated objective of selling the target to a third party are launched by activist investors before a specific bidder arrives."
- **Prediction 2** (p. 9): "Everything else held equal, proxy fights in which the activist's stated goal is selling the target to a third party increase the probability that the target receives a takeover offer afterward."
- **Prediction 3** (p. 9): "The announcement of a proxy fight in which the activist's stated goal is selling the firm to a third party generates positive abnormal returns for the target share. Following such a proxy fight, the share price experiences additional positive abnormal returns if the target is acquired and negative abnormal returns otherwise."
- **Prediction 4** (p. 10): "The frequency of proxy fights with a stated objective of selling the target to a third party has an inverted U-shape as a function of the private benefits of the incumbent board."
- **Prediction 5** (p. 11): "Policies and regulations that undermine shareholder activism, but do not directly affect bidders, will still have a negative effect on takeovers."
- **Prediction 6** (p. 11): "The probability of a takeover has a U-shape as a function of the private benefits of the incumbent board. Moreover, a positive association is an indication of the treatment effect."
- **Prediction 7** (p. 12): "The probability of a takeover is weakly decreasing in the cost of a proxy fight. Moreover, a negative association is an indication of the treatment effect."

All seven are ASSERTED as empirical statements (none is estimated in the paper), but each is derived from a PROVED result: P1 and P4 from Prop. 4; P2 and P3 from Prop. 4 + Cor. 1; P5 from §4.1; P6 and P7 from Cor. 2. P5 is illustrated only by an example, "the legalization of two-tier 'anti-activism' poison pills" (p. 11), not by a comparative static in any disclosure parameter.

## 4. Institutional facts used

| Fact | Page |
|---|---|
| Boards can resist takeovers via a poison pill; pills can be adopted on short notice ("shadow pills"), have never been intentionally triggered, and non-redeemable pills are illegal in most states including New York and Delaware | p. 4, fn 7 |
| In most jurisdictions incl. Delaware, merger proposals reach a shareholder vote only via the board; tender offers need no vote but are vulnerable to pills | pp. 1–2, fn 2 *(page corrected by verifier: fn 2 begins at the foot of p. 1 and finishes on p. 2)* |
| Fos (2017): only 5% of all proxy fights 2003–2012 were sponsored by corporations (i.e. potential bidders) | p. 2, fn 3 |
| Gardner Denver / KKR 2013: ValueAct "accumulated a 5% stake in the company, filed a schedule 13D, and agitated for its sale" — the only concrete 13D event in the paper | p. 2 |
| PetSmart / Jana Partners 2014, $8.7bn | p. 2 |
| **Regulation 13D as the interpretation of ᾱ; calibrated ᾱ ∈ [5%, 10%]** | p. 10 |
| SEC Rule 14a-9: "activists are required to disclose their net economic exposure to the target and the bidding firm as part of the proxy solicitation process" — used to argue away hidden bidder-activist side deals | p. 8, fn 19 |
| In 2013 only 11% of S&P 500 firms had a classified board, down from 57% in 2003 (sharkrepellent.net) | p. 5, fn 9 |
| Activists typically own 8%–9% of the target when running a campaign (Brav et al., 2008); directors typically earn ≤ $250,000 annually | p. 5, fn 13 |
| Boyson et al. (2017): a takeover bid is announced within two years in 70% of campaigns; the activist itself bids in 15% of events | p. 10 fn 24; p. 8 fn 20 |
| Fos (2017): CARs around a sell-the-company proxy fight are 10% in a one-year event window, positive for any window from −6 to +24 months | p. 10 |
| Doidge et al. (2017): 5% unconditional annual takeover probability for a US public firm | p. 9 |
| Jurisdictional variation in board blocking power: "the US in the 1980s or the UK" | p. 15 |

**Not used anywhere in the 17 pages:** no filing window, no filing deadline, no "business days", no 10-day or 5-day rule, no 13D/A, no **13G**, no Williams Act, no Hart-Scott-Rodino, no 2024 amendments, no beneficial-ownership timing of any kind. Grepping the full text for `13G`, `day(s)`, `window`, `delay`, `deadline`, `Williams`, `Hart-Scott` returns: `13G` = 0 hits; "days" only in the quoted phrase "in the old days" (p. 2); "window" only as *event window* in the CAR discussion (p. 10); "within two years" (p. 10, fn 24) refers to the empirical horizon, not a filing rule. **The window margin is untouched.**

## 5. Referee-facing strengths / weaknesses

**Strengths**
- One clean, memorable mechanism (the buyer cannot be trusted to sell), stated in one sentence and proved in one page. Occam's-razor framing is explicit (p. 2) and referees reward it.
- Everything is analytic. Propositions 1–7, Lemma 1 and Corollaries 1–2 are all proved; nothing central rests on a grid.
- Uniqueness is claimed and delivered in every main proposition (3, 4, 5).
- Robustness is done properly where it is done: Appendix B relaxes the "board can fully block" assumption to partial blocking (λ) and gets the same qualitative result; Appendix C is honest enough to show the main result *reverses* when the bidder can create value without a majority (Prop. 7). That is a strong, referee-proof way to state a scope condition.
- The selection-vs-treatment section is genuinely useful: it hands empiricists a *sign restriction* (∂θ**/∂b > 0 in the cross-section ⇒ treatment) rather than another correlation.
- The paper is candid that its central prediction 2 is only "consistent with" a 36%-vs-5% comparison, and does not dress it up as identification.

**Weaknesses / open flanks**
- **ᾱ is triple-loaded.** One scalar is the liquidity break, the disclosure threshold and the pill trigger. Any comparative static in it is uninterpretable as policy, which is presumably why none is stated. This is the single largest opening in the paper for us.
- **There is no market microstructure.** The market maker "can condition the price on the order flow if and only if the order is strictly larger than ᾱ" (p. 10) — a step function assumed "for simplicity", with no noise traders, no order-flow noise, no price impact, no Kyle λ. The activist's concealment works only because the market maker is *forbidden* to look, not because anything hides her.
- **Footnote 23 is the whole defence of that shortcut**, and it is unverifiable from the published article: no proof, no appendix, no online appendix — only the claim that "a previous version of the paper" showed similar results with Kyle (1985) liquidity traders.
- **The flagged state never occurs.** α* = ᾱ exactly; α > ᾱ is off path and rests on an assumed belief μ(α) = 1 (p. 14). The disclosure rule creates no on-path partition.
- **Uniqueness in §4 is bought with an unnamed assumption.** fn 26 says only "an additional technical assumption that we specify in the proof"; p. 14 discloses it as "either γ = 0 or s is sufficiently close to one". γ = 0 is exactly the case that kills the activist's private benefit and hence the only friction distinguishing her from a pure value-maximiser; s → 1 gives the target all bargaining power. Fig. 2 also imposes γ = 0.
- **§3 and §4 are never combined.** fn 25 (p. 10): "Assuming that the activist cannot launch a proxy fight before the bidder arrives is for simplicity."
- **The stake is a corner, not a choice.** α* ∈ {0, ᾱ}. There is no interior trade-off between size, price impact and concealment — the model cannot produce one.
- **Binary synergy.** x ∈ {Δ, −∞} makes the premium a two-point object and the takeover probability the only quantitative outcome.
- **Empirics are one number.** 232 events, one frequency, no SE, no controls, no pre-trend, no placebo. Prediction 3 is checked only against Fos (2017)'s figure, and the paper openly disagrees with Fos's own interpretation of it (p. 10, fn 22).
- **Predictions 6 and 7 need proxies for b and κ.** For b the authors concede "While challenging, parameter b can be proxied by a low managerial ownership in the target, distance of the CEO from retirement, strength of anti-takeover defenses, and low independence of the board" (p. 10); the κ proxies — "the dispersion of ownership of the target firm, the difficulty of proxy access, the existence of a staggered board, or low governance expertise of the activist" — are on p. 12 and carry no such concession *(pages corrected by verifier: the κ list is p. 12, not p. 10, and "challenging" attaches only to b)*. Several of these plausibly move both b and κ, so the sign test is not clean.
- No welfare analysis. h* ≥ h*(0) is a shareholder-value statement, not a welfare statement, and the incumbent's B and the activist's γ are never counted.

## 6. What they do NOT do (scope boundary)

**Objects they do not study.** No trading-profit or exit decision (the activist buys once and holds). No campaign success as an object separate from the takeover. No welfare. No effect of the activist on the target's *standalone* value — assumed away: "The activist cannot affect the standalone value of the target or make a takeover bid" (p. 5).

**Margins they do not open.**
- **Filing window / timing: entirely absent.** Nothing in the 17 pages refers to a filing deadline, a number of days, 13D/A, 13G, or any lag between crossing a threshold and disclosure. Disclosure in their model is instantaneous and unconditional: "After trading, the activist's ownership in the target becomes public" (p. 10).
- **Threshold level: present as a parameter, never varied.** ᾱ is fixed and calibrated ("Empirically, ᾱ ∈ [5%, 10%]", p. 10) and never appears in a stated comparative static, prediction or policy conclusion.
- **Liquidity as a distinct object: assumed away by construction.** "For simplicity, we assume that the market maker can condition the price on the order flow if and only if the order is strictly larger than ᾱ ∈ (0, 1). That is, the stock is perfectly liquid (illiquid) for small (large) orders." (p. 10). The Kyle alternative is relegated to fn 23.

**Things they explicitly flag as out of scope (quoted):**
- p. 5: "Bidder: The bidder initially does not own any shares of the target. Allowing the bidder to have a toehold will not change the main results." (asserted for the baseline; Appendix C shows a toehold bidder in a *no-activist* variant *does* win a proxy fight, Prop. 7, p. 16)
- p. 10, fn 25: "Assuming that the activist cannot launch a proxy fight before the bidder arrives is for simplicity. Identifying the activist's effect on the takeover, which is the focus of this section, is challenging when a proxy fight is only used as a threat."
- p. 10, fn 23: "A previous version of the paper assumed the existence of liquidity traders a la Kyle (1985) and showed that similar results hold under this alternative formulation."
- **p. 7, fn 17 — the region where the activist *raises* the premium, assumed away (added by verifier).** "If instead we assume b + κ/α⁄(1−s) < γ/α ≤ Δ, then the activist can credibly threaten the incumbent with a proxy fight if the incumbent does not demand a higher premium from the bidder (Jiang et al., 2018)." That is our premium wedge with the sign we want (m₁ > m₀), it is in their paper, and it is excluded by the maintained assumption γ/α < b (p. 5) plus γ < κ. They also name the case it fits — management buyouts, or incumbents promised large bonuses if the takeover succeeds.
- p. 15, fn 30: "For simplicity, we assume this possibility away." (the board leveraging shareholders' free-rider bargaining power by allowing a tender offer)
- p. 4: "The bidder cannot bypass the target board and make a tender offer directly to target shareholders" — relaxed only in Appendix B.
- p. 8, §2.3.2 / Appendix C: the main result is conditional on bidders needing ≥ 50% to create value; when they do not, "he can make such credible threats" (p. 8).

**Identification they do not attempt.** No event study of their own, no DiD, no structural estimation, no instrument, no policy change exploited. Their identification contribution is a *proposed* cross-sectional sign test (Predictions 6 and 7), explicitly offered to others: the comparative statics "can be used to create identification strategies for empirical research" (p. 3).

## 7. Implications for our position

**What Corum–Levit (published) occupies, stated precisely:**

- **OBJECT: the probability of a takeover, θ** — squarely and exclusively. They also carry an expected premium π*, but as a by-product of who sits on the board, not as an object of interest: it takes exactly two values, π_b and π_{γ/α}, and there is no premium comparative static anywhere in the seven Predictions. Secondary objects: proxy-fight frequency (P1, P4) and announcement CARs (P3).
- **MARGIN: threshold level — occupied, but sterile. Window — wide open.** ᾱ *is* the 13D threshold ("e.g., regulation 13D", "Empirically, ᾱ ∈ [5%, 10%]", p. 10) and it *is* the liquidity break, in the same two sentences. Because it is the same scalar, they can never move one without moving the other, and so they move neither: no proposition, corollary or prediction is a comparative static in ᾱ. Nothing in the paper touches the filing window; the words "day", "delay", "13G" and "deadline" do not occur in a rule sense anywhere in 17 pages.
- **IDENTIFICATION: theory only, plus a proposed cross-sectional sign test.** One descriptive frequency (36% vs 5%, N = 232) with no standard error. Nothing dated, nothing causal, no design.

**Five things this constrains for us** *(items 4–5 added by verifier)*

1. **"The activist's presence raises the probability of a takeover" is theirs.** Cor. 1 (θ* increasing in α, h*(α) ≥ h*(0)) and Prop. 5 own it, PROVED. We cannot claim it as a finding; we can only claim a *margin-specific* version of it.
2. **"The 5% threshold caps the stake and therefore caps the credibility of the voice threat" is theirs.** α* = ᾱ, and the treatment region exists iff ᾱ ≥ δ/Δ (p. 11). That is precisely the threshold-margin mechanism, already in print in the JFE. Our threshold-margin story must add something they do not have — and the obvious candidate is that they *cannot separate* the threshold from liquidity, so their ᾱ result is not a policy result and cannot be taken to an SEC rule change.
3. **The sign of our premium wedge is contested by them — but only in one region, and the card previously named the wrong one.** *(Corrected by verifier: the earlier text said "against us in their treatment region and with us in their baseline region"; it is the other way round.)* The two regions are:
   - **Δ ≥ b (the §3 pre-emption region; the same inequality that §4.1 calls *selection*).** Here condition (8) implies γ/α < b and hence **π_{γ/α} < π_b** (p. 9, proved p. 13): the activist wins the board and the firm sells for a *lower* premium than the entrenched incumbent would have extracted, offset by a higher takeover probability. **This is the region that runs against our wedge.**
   - **Δ < b with δ/α ≤ Δ (the §4.1 *treatment* region).** Here Prop. 3 (p. 7, Eq. 5) gives π* = π_{γ/α} > 0 *with* the activist, and without her the entrenched incumbent blocks and no deal happens at all (Lemma 1, p. 6). So the counterfactual premium is zero and **our wedge runs with them**.
   Note the two extensions are never combined (fn 25, p. 10), so mapping §3's region onto §4's selection/treatment labels is loose in their own paper; the inequality Δ ≥ b vs Δ < b is what actually decides the sign. Our draft must state which inequality we are in and confront the p. 9 result by name, or a referee who knows this paper will do it for us.
4. **They already have a signed, in-print statement about the *premium* and the threshold, and it points the other way from the probability result (added by verifier).** π_{γ/α} decreases in α (p. 8) and α* = ᾱ (Prop. 5) — so in their model a *higher* disclosure threshold means a *bigger* stake, a *higher* takeover probability (Cor. 1) and a *lower* premium. Any claim of ours that a looser threshold raises the premium collides with their p. 8 sentence directly, and any claim that it raises expected shareholder value has to net the two effects, which they never do. This is the single most competitively relevant sentence in the paper for a premium-based position and it is not in any of their seven Predictions.
5. **The threshold margin is inert in half their parameter space (added by verifier).** In the selection region b ≤ Δ, h*(α) = θ_b π_b is independent of α (p. 14, fourth step of the proof of Prop. 5), so ᾱ has no effect on anything. A threshold-margin claim of ours therefore has a scope condition already established in the JFE: it can only bite where the incumbent is entrenched enough to block (Δ < b). Say so before a referee does.

**Four pieces of whitespace this paper leaves us**

1. **Liquidity separated from the disclosure threshold.** They fuse them into one ᾱ, deliberately and "for simplicity", and demote the Kyle version to fn 23 with no proof anywhere. A model in which noise-trading intensity κ (ours) and the threshold are *two* parameters, so that ∂(control outcome)/∂(threshold) can be signed holding liquidity fixed, is genuinely not in this paper. This is our strongest claim to open ground and it survives the published version intact.
2. **The window margin.** Zero footprint here. It also carries the dated anchor (2024-02-05, 10 → 5 business days) that they have no analogue for. Their theory is *silent*, not opposed — which is the best kind of whitespace.
3. **An on-path partition.** Their flagged state is off the equilibrium path, so disclosure never actually informs anyone in equilibrium; it only truncates the stake. A model where the flagged and pooled states both occur on path, and where the market's inference differs across them, is a different object from theirs.
4. **Any identification at all.** They have 232 events and one frequency, and they explicitly hand identification to empiricists (p. 3). A clean dated design on a control outcome is unoccupied.

**One rival explanation they already own, which any cross-country design of ours must beat (added by verifier).** Appendix B's λ is a *jurisdictional* comparative static with an explicit empirical reading (p. 15): "one would expect activists to play a smaller role in the market for corporate control in jurisdictions in which boards have weaker power to block deals, such as the US in the 1980s or the UK." CONTEXT.md lists a cross-country contrast (US 5% vs UK 3%) as a candidate design for the threshold margin. If we run one, Corum–Levit's λ — board blocking power, not the disclosure threshold — is a published, proved alternative account of exactly the same US-vs-UK difference. We must control for or argue past it.

**What we must not do:** claim novelty for (i) activists raising takeover probability, (ii) the sell-side/buy-side credibility asymmetry, (iii) selection-vs-treatment as a framing, or (iv) the observation that a stake cap limits activist credibility. All four are theirs, in the JFE, PROVED.

## 8. Quotes we may lean on (verbatim, page-cited)

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "For simplicity, we assume that the market maker can condition the price on the order flow if and only if the order is strictly larger than ᾱ ∈ (0, 1). That is, the stock is perfectly liquid (illiquid) for small (large) orders." | p. 10 | Their liquidity is a step function assumed for tractability, not a modelled market — the core of our separation claim |
| Q2 | "Parameter ᾱ can also be interpreted as a disclosure threshold (e.g., regulation 13D). Moreover, buying up to ᾱ shares does not trigger a poison pill if such exists. Empirically, ᾱ ∈ [5%, 10%]." | p. 10 | Proof that liquidity, the disclosure threshold and the pill trigger are the *same* parameter; also their calibration |
| Q3 | "A previous version of the paper assumed the existence of liquidity traders a la Kyle (1985) and showed that similar results hold under this alternative formulation." | p. 10, fn 23 | The Kyle/noise-trading formulation is demoted to an unverifiable footnote — the published paper contains no noise trader |
| Q4 | "After trading, the activist's ownership in the target becomes public." | p. 10 | Disclosure is instantaneous and unconditional; there is no window, no lag, no timing margin |
| Q5 | "To fully exploit her private information, the activist buys the maximum stake that keeps her trade concealed, that is, α∗ = ᾱ." | p. 11 | The stake is a corner, never interior; no size/price-impact trade-off exists in their model |
| Q6 | "By contrast, if Δ < b and ᾱ ≥ δ/Δ, then the equilibrium exhibits treatment." | p. 11 | The only place the threshold does causal work: it determines whether the treatment region exists at all |
| Q7 | "Policies and regulations that undermine shareholder activism, but do not directly affect bidders, will still have a negative effect on takeovers." | p. 11, Prediction 5 | Their entire policy statement — generic, unsigned in any disclosure parameter, no margin named |
| Q8 | "Indeed, in the proof of Proposition 4, we show that if condition (8) holds, then γ /α < b, which implies πγ /α < πb." | p. 9 | Their activist wins the board and the firm sells for a *lower* premium — the direct challenge to our premium wedge |
| Q9 | "Bidder: The bidder initially does not own any shares of the target. Allowing the bidder to have a toehold will not change the main results." | p. 5 | The toehold claim is ASSERTED in the baseline; Appendix C's toehold bidder reverses Prop. 1 |
| Q10 | "If a proxy fight is initiated, the challenger incurs a non-reimbursable campaigning cost κ > 0." | p. 5 | Their κ is the proxy-fight cost, not our noise-trading intensity |
| Q11 | "Using the Factset Shark Watch Database, we identify 232 proxy fights from 1994–2015 in which the activist's stated goal was to sell the target company to a third party." | p. 9 | The whole of their empirical work — one descriptive frequency, no design |
| Q12 | "Assuming that the activist cannot launch a proxy fight before the bidder arrives is for simplicity. Identifying the activist's effect on the takeover, which is the focus of this section, is challenging when a proxy fight is only used as a threat." | p. 10, fn 25 | They never combine pre-emptive voice with position building — an open flank |

*Transcription note.* The PDF renders Δ, ᾱ and π subscripts as glyphs that `pdftotext` drops or mangles; the quotes above restore them from the page images and are otherwise character-for-character, including the typographic apostrophe and the en-dash in "1994–2015". Q8 preserves the paper's spacing around the slashes in "γ /α" and "πγ /α" as they appear in the printed line.

## 9. Verification log

**Verified 2026-08-19 (adversarial verifier, opus). Method:** whole paper re-read, all 17 pages, from per-page `pdftotext -raw` and `-layout` extracts; every ᾱ / α / Δ-bearing quote additionally read off page images rendered at 400 dpi (`pdftoppm -r 400 -png -x … -W … -H …`) of pp. 10 and 11. Front matter checked against `pdfinfo` and printed p. 1.

**Counts: 22 OK · 1 WRONG · 4 MISCITED · 1 UNCHECKED · 6 omissions added.**

### Header / venue
| Item | Verdict | Checked against |
|---|---|---|
| JFE 133 (2019) 1–17; doi:10.1016/j.jfineco.2019.02.001 | OK | Printed p. 1 masthead + `pdfinfo` Subject field. (The issue number "(1)" is not printed in the PDF; it is external bibliographic knowledge, not an error.) |
| Received 24 Aug 2017 / revised 29 May 2018 / accepted 11 Jun 2018 / online 6 Feb 2019 | OK | p. 1, "Article history" block, all four dates verbatim |
| 17 printed pages = PDF index 1–17; no online appendix cited | OK | Page count and every running head; no supplementary-material line anywhere |

### Quotes (§8)
| # | Verdict | Checked against |
|---|---|---|
| Q1 | **OK, character-for-character** | 400 dpi image of p. 10, right column, top. "…strictly larger than ᾱ ∈ (0, 1). That is, the stock is perfectly liquid (illiquid) for small (large) orders." The macron on ᾱ and the spacing "(0, 1)" both confirmed on the image; the raw text extract drops the macron, as the card warned |
| Q2 | **OK, character-for-character** | Same image. All three sentences run consecutively on the page, all three ᾱ carry the macron, and "[5%, 10%]" carries the space. Confirms the triple load: liquidity break → disclosure threshold ("e.g., regulation 13D") → pill trigger → calibration, in four consecutive sentences |
| Q3 | OK | p. 10, fn 23, verbatim |
| Q4 | OK | p. 10, image; sentence immediately follows "Empirically, ᾱ ∈ [5%, 10%]." |
| Q5 | **OK** | 400 dpi image of p. 11, left column. "…that is, α∗ = ᾱ." confirmed with the macron |
| Q6 | **OK** | 400 dpi image of p. 11, left column, §4.1 second paragraph. "By contrast, if Δ < b and ᾱ ≥ δ/Δ, then the equilibrium exhibits treatment." Δ and ᾱ both confirmed on the image |
| Q7 (Prediction 5) | OK | p. 11, verbatim |
| Q8 | OK | p. 9, verbatim including the printed spacing "γ /α" and "πγ /α" |
| Q9 | OK | p. 5, verbatim |
| Q10 | OK | p. 5, verbatim (print sets "κ >0" with no space before the sign; the card's "κ > 0" is a typographic normalisation, not a content change) |
| Q11 | OK | p. 9, verbatim including the en-dash in "1994–2015" |
| Q12 | OK | p. 10, fn 25, verbatim |

### Results (§3)
| # | Verdict | Checked against |
|---|---|---|
| R1–R5 | OK, labels stand | Props. 1–4 and Cor. 1 read in full, pp. 6–9; proofs pp. 12–13. Prop. 3's Eq. (5) and Cor. 1's Eq. (6) match the card exactly |
| R6 / Q8 | OK | p. 9 text and p. 13 proof, final paragraph ("we show that if condition (8) holds, then γ/α<b"). The region is Δ ≥ b — see the WRONG item below, which concerns how §7 *labelled* that region, not R6 itself |
| R7 | OK, incl. the conditional PROVED label | p. 10 fn 26 ("an additional technical assumption that we specify in the proof") and p. 14, fourth step: "Hereafter, we assume either γ = 0 or s is sufficiently close to one" — both verbatim |
| R8–R9 | OK | §4.1 p. 11 and Cor. 2 p. 11, proof p. 14. Cor. 2(i)'s "θ∗∗ >0 if and only if δ/ᾱ ≤ Δ" confirmed |
| R10 | OK | Prop. 6, p. 15, incl. (κ/α)/λ and the premium (1−λ)φΔ + λπ_{γ/α}. (Appendix B itself begins on p. 14; the proposition is on p. 15, as cited) |
| R11 | OK | Prop. 7 and its proof, p. 16; condition (22) matches. Appendix C's setup paragraph is on p. 15, the proposition and proof on p. 16 — the card's citation is right |
| R12 | OK, and the ESTIMATED/ASSERTED split is correct | p. 9. The paper reports one frequency and the bare phrase "significantly larger than 5%" with no test, no SE, no CI, no control group. Label upheld |
| R13, R14, R15 | OK | p. 5, p. 10 fn 23, p. 12 Fig. 2 caption (γ = 0, c ∼ U[0,c̄], c̄ ≥ τ(1−s)Δ, δ/ᾱ<Δ left, Δ<b right) |
| R-none | **MISCITED (fixed in place)** | The headline claim — no proposition/corollary/prediction is *stated* as a comparative static in ᾱ — is **confirmed** after reading Lemma 1, Props. 1–7, Cors. 1–2 and all seven Predictions. But the supporting sentence was wrong: ᾱ enters more than the two region conditions. It is also the equilibrium stake level in Prop. 5(i) and the kink of the price function in Prop. 5(ii). Row rewritten, and the Cor. 2(i) near-miss (a discontinuous comparative static in ᾱ in all but name) added |
| Predictions 1–7 | **OK, all seven verbatim, all seven pages correct** | P1–P3 p. 9; P4 p. 10; P5–P6 p. 11; P7 p. 12. Read against the printed statements one at a time |

### Scope claims (§4, §6)
| Claim | Verdict | Checked against |
|---|---|---|
| `13G` = 0 hits | OK | Case-insensitive regex over all 17 pages: 0 |
| "days" only in "in the old days" | OK | `\bdays?\b` → exactly 1 hit, p. 2, the George Roberts quotation |
| "window" only as *event window* | OK | 4 hits, all p. 10, all in the Fos (2017) CAR discussion |
| delay / deadline / Williams / Hart-Scott / business day | OK | 0 hits each |
| "amplif" = 0 | OK | 0 hits — the WP's 13D-filing-rules sentence really is gone |
| "Back et" = 0 | OK | 0 hits |
| No noise traders in the model | OK | "noise" has exactly 1 hit in 17 pages, p. 17, in the *reference title* "Kyle, A.S., Vila, J.L., 1991. Noise trading and takeovers." Nothing in §§2–5 or Apps. A–C |
| "13D" appears twice only | OK | p. 2 (ValueAct/Gardner Denver) and p. 10 (the ᾱ interpretation) |
| Kyle appears three times | OK | p. 3 (Kyle–Vila in related work), p. 10 fn 23, p. 17 references |
| §2 "CRSP delisting codes" | **MISCITED (fixed)** | p. 9 says "Using Center for Research in Security Prices (CRSP) data" and "delisted due to an M&A event". Delisting *codes* are the card's inference, not the paper's words |
| §4 fn 2 cited to p. 2 | **MISCITED (fixed)** | fn 2 begins at the foot of p. 1 and finishes on p. 2 |
| §5 "proxies … the authors concede are 'challenging' (p. 10)" | **MISCITED (fixed)** | "While challenging" attaches only to the *b* proxies (p. 10). The κ proxy list is on p. 12 and carries no concession |
| §6 "identification strategies for empirical research" (p. 3) | OK | p. 3, verbatim: "Importantly, this feature can be used to create identification strategies for empirical research." (The conclusion on p. 12 has a different, longer variant — the card quotes the p. 3 one and cites p. 3 correctly) |

### The one WRONG item
**§7 point 3 — the premium-wedge regions were stated backwards. Corrected in place.** The card said our wedge "runs against this in their treatment region and *with* it in their baseline region". The opposite is true. The π_{γ/α} < π_b result lives where Δ ≥ b (p. 9), which is the same inequality §4.1 calls **selection** (b ≤ Δ). In the **treatment** region (Δ < b, δ/α ≤ Δ) Prop. 3's Eq. (5) gives premium π_{γ/α} > 0 with the activist and *no deal at all* without her (Lemma 1, p. 6), so the counterfactual premium is zero and our wedge runs *with* them. Getting this backwards would have put a false concession into the draft's introduction. §7 point 3 rewritten with both regions spelled out and the caveat that §3 and §4 are never combined (fn 25).

### UNCHECKED
- **Whether an unpublished appendix or a "previous version" of the Kyle formulation (fn 23, p. 10) exists anywhere.** Not checkable from the article; the published text contains no proof, no appendix and no online-appendix pointer, and we hold no other version of the published paper. The card already labels R14 ASSERTED and says the reader cannot check it. Left in place, marked. **This one is decision-critical for positioning** — our whole "they have no noise trading" separation claim rests on the published version containing none, which *is* verified (0 in-model hits for "noise"), but the strength of their fn-23 defence cannot be assessed without that previous version. If the positioning memo leans hard on it, someone should try to obtain the pre-2019 SSRN/NBER version.

### Omissions added (§ where added)
1. **§3, new row R16 — the premium falls in the stake.** p. 8: "a higher α also implies that the activist puts less weight on her private benefits … which harms her ability to bargain a higher takeover premium (π_{γ/α} decreases in α)." With α* = ᾱ this is a published statement that a higher disclosure threshold *lowers* the premium while raising the takeover probability. This is the most competitively relevant sentence in the paper for a premium-based position and the card had it nowhere. Also carried into §7 as new constraint 4.
2. **§3, new row R17 — the threshold is inert in the selection region.** p. 14, fourth step of the proof of Prop. 5: if b ≤ Δ then h*(α) = θ_b π_b, independent of α. So ᾱ moves nothing unless Δ < b. Carried into §7 as new constraint 5 — it is a scope condition on any threshold-margin claim of ours, already in print.
3. **§3, R-none — Cor. 2(i) is a discontinuous comparative static in ᾱ in all but name.** On b > Δ, θ** flips from 0 to positive as ᾱ crosses δ/Δ. The card's "they never state one" is right; the sharper fact is that one is one line from their own results, so our novelty claim must be about *signing it as policy*, not about having it first.
4. **§6, new bullet — p. 7, fn 17.** The region b + (κ/α)/(1−s) < γ/α ≤ Δ, where the activist credibly forces the incumbent to demand a *higher* premium (citing Jiang, Li and Mei 2018). That is our premium wedge with our sign, present in their paper and assumed away by γ/α < b plus γ < κ. They name management buyouts and takeover-contingent bonuses as the fitting cases.
5. **§7, new paragraph — Appendix B's λ is a rival explanation for a cross-country design.** p. 15: "one would expect activists to play a smaller role … in jurisdictions in which boards have weaker power to block deals, such as the US in the 1980s or the UK." CONTEXT.md lists a US-vs-UK threshold contrast as a candidate; board blocking power is a published, proved alternative account of the same contrast.
6. **§7 constraints renumbered** from three to five to carry items 1 and 2 above.

### Overall verdict
**Sound, and unusually careful on the ᾱ/Δ glyph problem — the reader's warning about `pdftotext` was correct and every image check confirmed the card's transcription.** One substantive error, in §7's premium-wedge regions, now fixed; four citation slips fixed; six omissions added, two of which (the premium falling in the stake, and the threshold being inert unless Δ < b) materially change what we can claim on the threshold margin. The card's central competitive reading — ᾱ is one scalar doing three jobs, no comparative static in it is ever stated, and the filing window is untouched — survives every check.

---

## 10. Changes from the 2016 WP

Compared against `corum_levit_2019_wp2016_superseded.md` (the verified card for the 45-page working paper dated 11 August 2016), **after** this card was written. The published article is not a tidied WP; §4 was rebuilt and roughly two-thirds of the WP was cut. Anything in the WP card's §§3, 5, 6, 7 that turns on the trading block, the appendices, or the absence of a threshold no longer describes the paper the field cites.

**A. The trading block was replaced, and this is the change that matters to us.**

| | 2016 WP (pp. 19–24) | Published (p. 10) |
|---|---|---|
| Market | Kyle (1985) market maker + liquidity traders | Market maker who "can condition the price on the order flow if and only if the order is strictly larger than ᾱ" |
| Noise | liquidity traders buy L ∈ (0,½) w.p. ½, 0 w.p. ½ | **none — there are no liquidity traders and no noise at all** |
| Stake cap | 2L, "because of either wealth constraints or the concern of triggering a poison pill" — explicitly *not* a legal threshold | ᾱ, explicitly "a disclosure threshold (e.g., regulation 13D)", also the pill trigger, also the liquidity break |
| Calibration of the cap | none; L fixed at 0.1 in the figures, never varied | **"Empirically, ᾱ ∈ [5%, 10%]"** |
| Activist's strategy | **mixes**: 2L w.p. σ*, L w.p. 1 − σ*, σ* in closed form (Eq. 10) | **pure corner**: α* = ᾱ or 0 |
| Entry condition | h(2L)/h(L) < 2, with an interior case needing 1 + ½(μ̂−μ)/μ̂ < h(2L)/h(L); a no-entry region exists | **gone entirely** — no ratio condition, no no-entry region |
| Signal | binary y with precision φ, prior μ on ζ, posterior μ̂ | y ∈ {0,1}, Pr[y=1] = μ; y = 0 ⇒ synergy = −∞ for sure, so φ is degenerate and μ̂ is gone |
| Kyle | the model | footnote 23: "A previous version of the paper assumed the existence of liquidity traders a la Kyle (1985) and showed that similar results hold under this alternative formulation." |

**B. The threshold margin went from open to occupied; the window margin did not.** The WP card's flat claim "there is no 5% threshold in the model (the only threshold is 2L, and it is a wealth/poison-pill constraint, not a legal one)" is **false of the published article**. There is a threshold, it is named as regulation 13D, and it is calibrated to 5–10% — consistent with the paper's own fact that "Activists typically own 8%-9% of the target firm when they run a campaign" (p. 5, fn 13), which is new prominence in the published version. What survives from the WP card's negative claims: **no filing window, no delay, no 13G, no days, no timing margin of any kind** — verified by grep over the full published text (`13G` = 0 hits; "days" only in "in the old days", p. 2; "window" only as *event window*, p. 10).

**C. Liquidity got weaker, not stronger — but is now inseparable from the rule.** The WP at least had a noise distribution. The published version has none: the step at ᾱ is the whole microstructure and the activist's concealment works because the market maker is *forbidden* to condition, not because anything hides her. So the WP card's "their liquidity is degenerate" is *more* true, not less. What changes is the framing of our whitespace: we can no longer say "they have no threshold", only "they cannot move the threshold without moving liquidity, because it is the same scalar — and they never move it at all". That is a weaker but still decisive separation claim, and it must be argued, not asserted.

**D. The WP sentence the old card called "the single best sentence in the competitor set for our introduction" was CUT.** WP p. 5: *"Third, small regulatory changes, such as easing the access of shareholders to the ballot or modifying the rules that govern the filing of 13D schedules, can have an amplified effect on the aggregate volume of M&A."* The published article contains **no** occurrence of "amplif" (0 hits) and no 13D-filing-rules conjecture. What replaced it is Prediction 5 (p. 11), which is the WP's *fourth* implication (anti-activism pills) promoted to a numbered prediction, with the 13D sentence dropped. **Consequence: the WP card's §7 point 2 must not be used.** Quoting a cut WP sentence as "a JFE-published competitor's conjecture" would be a citation error a referee would catch immediately. The honest published-version framing is the reverse: they *have* the 13D threshold as a parameter and still say nothing about moving it.

**E. Seven numbered Predictions were added.** The WP had no "empirical implications" section and the word "testable" never appeared. The published article has Predictions 1–7 (pp. 9–12), reproduced verbatim in §3 above. Two are genuinely new objects: Prediction 4 (proxy-fight *frequency* is inverted-U in b) and Prediction 7 (takeover probability weakly decreasing in the proxy-fight cost κ, now a corollary rather than a remark).

**F. The headline non-monotonicity was cleaned up and re-labelled.** WP Prop. 4 ("If the equilibrium exhibits only selection then θ* is strictly decreasing in b. If the equilibrium exhibits treatment then θ* is non-monotonic in b.") was PROVED only inside a worked case (σ* = 0 and (κ/s)/L < b, WP p. 44), was a *local* comparative static by fn 28, and the shape was carried by a figure at one parameter vector. The published Corollary 2 (p. 11) is a clean global statement — strictly decreasing on b ≤ Δ, zero at b = Δ, flat and positive on b > Δ iff δ/ᾱ ≤ Δ — fully proved on p. 14, with the U-shape arising as a *jump* between the two branches. **The WP card's honesty caveat on this result no longer applies.** Do not carry it forward.

**G. A small empirical exercise was added.** The WP had none. Published p. 9: 232 FactSet SharkWatch proxy fights, 1994–2015, stated goal = sell to a third party; 36% delisted via M&A within 24 months vs 5% unconditional (Doidge et al., 2017). Still no regression, no standard error, no control group — so the WP card's "identification = theory only, no data" is now "theory plus one descriptive frequency", which does not change the competitive picture.

**H. Structural and notational changes to watch when carrying WP numbers across.**
- **Every proposition number moved.** WP Lemma 1 → published Lemma 1; WP Prop. 1(i) → Prop. 1; WP Prop. 1(ii) → Prop. 2; WP Prop. 2 → Prop. 3; WP Cor. 1 → Cor. 1; WP Prop. 3 → Prop. 5; WP Cor. 2 → §4.1 text; WP Prop. 4 → Cor. 2 + Predictions 6–7; WP §5.3 (λ) → Appendix B, Prop. 6 (now proved in the article, no longer ASSERTED); WP §2.3.2/Appendix C.? → Appendix C, Prop. 7. There is **no Online Appendix** in the published version.
- **Standalone value normalised away.** WP: q > 0, values are q + …. Published: "The standalone value of the target is normalized to zero" (p. 4), so π is the premium itself and h* = θ*π*.
- **Synergy simplified.** WP: Δ | ζ=1 ~ F with full support on ℝ and E[Δ|ζ=1] ≤ 0. Published: x ∈ {Δ, −∞}, Pr[x = Δ] = τ. The continuous synergy distribution is gone, and with it the (1 − F(b))/f(b) condition in the WP's Prop. 4 proof.
- **Bidder toehold removed from the baseline.** WP carried m ≥ 0 through Lemma 1 and Props. 1–2 (everything ran on Δ/(1−m)), then set m = 0 for the trading extension. Published: no toehold anywhere in the baseline, with the assertion "Allowing the bidder to have a toehold will not change the main results" (p. 5) and no proof. A toehold bidder survives only in Appendix C's *no-activist* variant, where Prop. 7 shows he **does** run and win a proxy fight — the sharpest scope condition on Prop. 1 in either version.
- **Figures.** WP Figures 2 and 3 were calibrated (L = 0.1, s = 0.75, κ = 0.225, μ = 0.6, φ = 0.5, Δ ~ N(0,5), c ~ LogN(−1.62, 0.13)). Published Fig. 2 (p. 12) is schematic — axes marked only 0, Δ and αsΔ — under γ = 0, c ~ U[0, c̄], c̄ ≥ τ(1−s)Δ. **The WP's numerical calibration is gone.**
- **§3.2's six candidate "solutions" to the commitment problem are cut**, and with them Sotheby's/Third Point (and its 10% ceiling), Valeant/Allergan/Pershing Square, Revlon, Entire Fairness vs Business Judgment, and Collin-Dufresne et al. on empty voting. All are 0 hits in the published text. Only fn 18 (Bebchuk–Hart) and fn 19 (SEC Rule 14a-9) survive from that block.
- **WP fn 24's modularity claim is cut.** "the results in this section continue to hold even if h(α) stems from a different microfoundation, as long as h(α) is an increasing function. See Back et al. (2016)…" does not appear in the published article ("Back et" = 0 hits). **The WP card's §7 point 7 — "our model can supply h(·) instead of competing with them" — has no published warrant.** The published analogue is Cor. 1 ("θ* increases in α and h*(α) ≥ h*(0)") plus p. 14's monotonicity step, which assumes γ = 0 or s near 1; it is a property they prove of *their* h*, not an invitation to substitute ours.
- **Fos's numbers changed.** WP cited Fos (2016): 632 proxy fights 2003–2012, 5% by corporations, 70% by activist hedge funds. Published cites Fos (2017) for the 5% only; the 632 count and the 70% share are gone. The published "70%" is a different statistic (Boyson et al. 2017, bid within two years, p. 10 fn 24).

**I. What survives unchanged.** κ is still the proxy-fight campaigning cost. The bidder still never runs a proxy fight (Prop. 1). The counterparty/commitment mechanism, the activism–takeover complementarity, and the selection-vs-treatment identification pitch are all intact and, if anything, sharper. The premium-can-fall point survives and is *upgraded*: the WP had it in fn 29 (p. 27); the published version proves it as an implication of condition (8) — "if condition (8) holds, then γ/α < b, which implies πγ/α < πb" (p. 9, proof p. 13). The WP card's §7 point 8 stands and should be carried forward with the published citation.

---

### One line for the orchestrator

**What the published version occupies that the WP did not:** the **threshold margin** — the 2016 WP's stake cap was 2L, an explicitly non-legal wealth/poison-pill constraint with no comparative static; the published version renames that cap ᾱ, declares it "a disclosure threshold (e.g., regulation 13D)", calibrates it to [5%, 10%], and makes the treatment region exist only if ᾱ ≥ δ/Δ — so "no 13D threshold in the competitor set" is dead, and our whitespace narrows to (i) the **filing window**, still untouched, and (ii) **separating liquidity from the threshold**, which they fuse into one scalar and never vary.
