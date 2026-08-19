# Corum (2025) — "The Stick or the Carrot? The Role of Regulation and Liquidity in Activist Short-Termism"

**Venue / status:** Working paper, dated April 15, 2025 (SSRN 4319599). Adrian Aycan Corum, Johnson Graduate School of Management, Cornell University. Circulated earlier as "Governance through Regulation vs. Market Forces: Fighting Short-Termism under Moral Hazard and Adverse Selection" (p. 1). No R&R status stated.
**Full text from:** `research/txt_extracts/corum_2025_ssrn.pdf` and `research/txt_extracts/corum_2025_ssrn.txt` · **Reader:** opus · **Read:** full text, 77 pages (body 1–44, references 45–47, Appendix A 48–52, Internet Appendix B–F 53–77)
**Type:** theory (pure — no data, no figures, no tables, no simulations)   **Role for us:** competitor

**Page numbering:** printed page numbers of the April 15, 2025 SSRN version. Printed pages 1–77 coincide exactly with PDF page indices 1–77.

**Transcription note:** the `pdftotext -layout` extract mangles fi/ff/fl ligatures (`…rm` for `firm`, `e¤ort` for `effort`) and drops every Greek and math symbol. All quotes in §8 and all Greek notation in this card were transcribed from the rendered PDF page images, not from the `.txt`.

**Notation clash — read before citing him.** Corum's λ = looseness of the disclosure rule at the exit (selling) stage; our λ = appropriability coefficient in the tender game. Corum's κ = the activist's cost of intervention; our κ = noise-trading intensity. Corum's η = looseness of the disclosure rule at the entry (buying) stage. Corum's ρ = probability of effort; α = stake; φ = probability of a forced (liquidity-shock) sale.

## 1. Question

If a stricter disclosure rule, higher short-term capital gains taxes, or lower liquidity drive value-destroying activists out of the market *and* at the same time strengthen the surviving activists' incentive to work, does aggregate value created by activism always go up? Corum asks whether there is a tension between improving governance "forcefully" through policy and letting it improve endogenously through market forces, and if so which family of anti-short-termism policies is least likely to backfire (p. 4). The motivation is the policy debate — Clinton/Fink/Buffett proposals to punish quick exit, the Brokaw Act, and the SEC's 2022 Schedule 13D proposals and 2024 final rules (pp. 2–3, 26).

## 2. Model / data and method

Pure theory. Perfect Bayesian Equilibrium throughout; every numbered **Lemma and Proposition** has a written proof in Appendix A / Internet Appendix B–D. *(corrected by verifier: **Corollary 2 — the paper's headline — has no proof anywhere.** The string "Corollary 2" occurs exactly once in all 77 pages, at its statement on p. 33; there is no "Proof of Corollary 2" in A, B.1, C or D. Two further "proofs" are pointers, not arguments: Appendix A p. 48 says Lemma 1's proof "provided right after the lemma in the main text", and p. 64 says Proposition 5's proof "is analogous to the proof of part (iii) of Proposition 7, and thus not repeated here.")* No data, no calibration, no figures, no tables, no simulation grid. One numerical example, in footnote 31 (pp. 32–33).

**Baseline model (§2, pp. 9–17).** One firm, one activist, one competitive market maker. Status-quo firm value Q₀ (normalised to 0). The activist's intervention is *good* with probability 1−q or *bad* with probability q — his private information. Good + effort (cost c) raises firm value by Δ_H; good + shirk raises it by Δ_M; bad lowers it by Δ_L < 0, with Δ_H > Δ_M > 0 > Δ_L. Timing: t=1 intervene and (simultaneously) choose effort; t=2 exit stage; t=3 NPV becomes public. At t=2 the activist is *forced* to sell with probability φ (liquidity shock / outside option) and chooses freely with probability 1−φ. In the baseline he must disclose before selling, so the exit price P is fully revealing of the sale. ρ = probability of effort by the good-intervention activist.

**Main model (§3, pp. 18–34).** A continuum: measure μ̄_F of identical firms, measure μ̄_BL of ex-ante identical activists, one activist matched per firm; good with probability σ. Each activist chooses whether to buy a stake α (exogenous), whether to intervene, and (if good) whether to exert effort. Four things are added:
1. **Disclosure thresholds on both sides of the trade.** Buying: he accumulates α₀ silently, must then disclose the stake *and* state whether he intends to intervene, then buys the remaining α−α₀. Define **η ≡ α₀/α** — lower η = tighter entry disclosure. Selling: he sells α₁ silently, must disclose, then sells the rest. Define **λ ≡ α₁/α** — lower λ = tighter exit disclosure (pp. 19–20).
2. **Capital gains taxes** τ_s (short-term, on exit) and τ_l (long-term, on holding to t=3), τ_s ≥ τ_l.
3. **Long-term perks** b ≥ 0 per share for holding to t=3 (loyalty dividend, extra votes, proxy access).
4. **Intervention costs** κ for a good intervention, κ+Δκ for a bad one; Δκ > 0 proxies liability/accountability.

The resulting payoff algebra is the whole engine: buying costs α[Q₀+(1−η)V], selling raises α[Q₀+λV+(1−λ)P], where V is the expected NPV conditional on intervention and P the expected NPV conditional on exit (pp. 22–23). So **η and λ enter linearly as the weight on the *uninformed* price** — that linearity is what makes every comparative static signable in closed form.

**How liquidity enters — critical for us.** There is no Kyle market maker and no price-impact parameter. The market is assumed *perfectly liquid*; the market maker learns nothing from order flow and updates only on disclosures (p. 19). Liquidity is then imported by reinterpretation: §3.4 (p. 34) says higher η (λ) = higher ability to camouflage = "the liquidity at the entry (exit) stage", and Online Appendix E (p. 74) gives the microfoundation — a **two-state noise process**: with probability λ (η) noise is "very high" and the market maker infers nothing; with probability 1−λ (1−η) noise is "very low or non-existent" and he infers perfectly. Expected proceeds coincide with the disclosure-threshold reading, so nothing in the formal model changes. Liquidity is therefore a *probability of complete camouflage*, not a continuous depth or Amihud-type parameter.

**Functional forms that buy tractability.** Binary type (good/bad); binary effort; all-or-nothing exit; three additive NPV levels; risk neutrality; no discounting; exogenous stake α and exogenous φ; a competitive market maker pricing off disclosures alone; a continuum so that q is an aggregate pinned by a zero-profit entry condition; the assumption μ̄_B > (Δ_H/−Δ_L)μ̄_G ("good ideas are scarce and bad ideas are abundant", p. 30) to keep μ*_B interior; and three parameter restrictions each of which exists to kill an uninteresting case — c < min{c̄, ĉ} (else no effort ever, or multiple equilibria), b < min{κ, c}, and τ_s < τ̄_s (else the activist always holds and moral hazard vanishes) (pp. 21, 53).

**The mechanism in one line.** The good activist's indifference between (shirk, exit) and (effort, hold) pins a weighted sum of V and P. A higher q pushes P down, which makes holding relatively attractive, which raises ρ. Because the market knows an effort-exerting activist only exits when forced, a rise in ρ moves unconditional V more than it moves the exit price P — so V must rise for the indifference to be restored. Hence **V is strictly increasing in q up to a threshold q̲, maximised at q̲, decreasing thereafter** (Props 2, 3).

**The three regions of the main model** (Prop 7, pp. 30–31), indexed by κ+Δκ:
- (i) κ+Δκ > κ̄: q* = 0 — moral hazard binding, no adverse selection.
- (ii) κ+Δκ ∈ (κ̲, κ̄): q* ∈ (0, q̲) — adverse selection present *and* moral hazard binding. **This is the region that produces the paper's headline.**
- (iii) κ+Δκ < κ̲: q* > q̲ — adverse selection present, moral hazard not binding (ρ* = 1).

**Policy taxonomy (p. 26).** (A) punish short-termism: raise τ_s, tighten λ. (B) reward long-termism: cut τ_l, raise b. (C) blanket punishments: tighten η, raise κ. (D) make bad interventions harder: raise Δκ.

## 3. Results — with honesty labels

| # | Result (one line) | Label | Where (page / prop / table) |
|---|---|---|---|
| R1 | Without voluntary exit, first best obtains: the good activist never exerts effort if c > c̄ and always exerts effort if c < c̄ ≡ α(1−φ)(Δ_H−Δ_M); higher q always lowers firm value | PROVED | p. 10, Lemma 1, eq. (1); the firm-value sentence is on p. 11. *(verifier: Appendix A p. 48 gives no proof — it says the proof "provided right after the lemma in the main text")* |
| R2 | With voluntary exit: **given c < c̄**, if the intervention is good with certainty (q = 0) the activist shirks with positive probability (ρ < 1) — first best is never attained | PROVED | p. 11, Lemma 2(ii) (proof p. 48). *(verifier: the card previously said "for any c > 0"; the lemma conditions on c < c̄. For c > c̄, Lemma 2(i) gives ρ = 0, so first best fails there too, but that is a different statement.)* |
| R3 | Exit strategies: the bad activist always exits; the good activist who exerts effort exits only if forced; the good activist who shirks always exits | PROVED | p. 13, Lemma 3 (proof p. 48) |
| R4 | Closed-form equilibrium: unique ρ* and P* for every q; ρ* strictly increasing in q for q < q̲; ρ* = 1 for q ≥ q̲. Threshold q̲ ≡ [(φ/(1−φ))(c/α)] / [Δ_H − Δ_L − c/α], and P* = Δ_H − (1/(1−φ))(c/α) on q < q̲ | PROVED | p. 15, Prop. 1, eqs. (5)–(8) (proof pp. 49–51) |
| R5 | **Firm value is strictly increasing in the probability the intervention is value-destroying**, up to a unique maximum at q = q̲, decreasing after | PROVED | p. 16, Prop. 2 (proof pp. 51–52) |
| R6 | The increasing region is not knife-edge: it is the whole region where moral hazard binds (ρ* < 1), and q̲ strictly increases in c; V(q̲) rises as Δ_L falls (more destructive bad activists are *better*) | PROVED | p. 16, Corollary 1 (proof p. 52) |
| R7 | All baseline results survive the full model with taxes, perks, two-sided disclosure thresholds and intervention costs (closed forms lost) | PROVED | p. 22, Prop. 3 (proof pp. 57–63) |
| R8 | Holding q fixed: ρ* and V* weakly (strictly, if q < q̲) increase in τ_s and b, and decrease in τ_l and λ | PROVED | p. 27, Prop. 4 (proof pp. 63–64) |
| R9 | Holding ρ fixed: q* strictly decreases in τ_s and b, **strictly increases in λ**, weakly increases in τ_l; therefore V* strictly increases in τ_s and b, **strictly decreases in λ**, weakly decreases in τ_l | PROVED | p. 27, Prop. 5. *(verifier: the card previously read the moving parameter as Δκ — the print is **λ**, confirmed on the rendered page image. Δκ does not appear in Prop. 5. The "proof" on p. 64 is one line referring to the proof of Prop. 7(iii).)* |
| R10 | Endogenous entry: π*_exit(q) strictly decreasing, so q* is unique and pinned by π*_exit(q)−(κ+Δκ) = α(1−φ)b | PROVED | p. 30, Prop. 6 (proof pp. 65–67) |
| R11 | **Region (ii) [q* ∈ (0,q̲)]: total firm value (μ*_B+μ*_G)V* strictly *decreases* in τ_s and strictly *increases* in λ and η** — i.e. punishing exit and tightening disclosure destroy value; more liquidity creates it. V* itself does not change in τ_s or λ at all | PROVED | pp. 30–31, Prop. 7(ii)(b)(c) (proof pp. 67–70) |
| R12 | Region (i) [q*=0]: V* and total firm value do not change in κ or Δκ, **strictly increase in τ_s and b, weakly increase in η**, and strictly decrease in τ_l and λ. Region (iii) [q*>q̲]: both strictly increase in κ, Δκ, τ_s and b, **strictly decrease in λ and η**, and do not change in τ_l | PROVED | pp. 30–31, Prop. 7(i),(iii). *(verifier: the card previously said total firm value "falls in λ and η" in **both** regions. In region (i) it **weakly increases in η** — entry looseness is never harmful there. The η sign therefore differs across regions (i) and (iii), while the λ sign does not.)* |
| R13 | **Headline.** Policies that punish short-termism, act as blanket punishments, or raise the cost of bad interventions destroy total firm value whenever adverse selection is present *and* moral hazard binds — even though they cut only μ*_B and leave μ*_G untouched | PROVED **(immediate restatement of Prop. 7(ii)(c), which is proved pp. 67–70; Corollary 2 itself carries no proof — verifier)** | pp. 33–34, Corollary 2(i) |
| R14 | Policies rewarding long-termism are less likely to destroy value; raising b dominates every policy in R13; but b and τ_l do not dominate each other, and cutting τ_l is the least likely of all to destroy value. Corollary 2(iii) splits by μ*_B: (a) μ*_B = 0 → both b↑ and τ_l↓ raise total firm value; (b) μ*_B/(μ*_B+μ̄_G) ∈ (0,q̲) → τ_l↓ raises it, **the effect of b↑ is ambiguous**; (c) above q̲ → τ_l↓ has no impact, b↑ strictly raises it | **ASSERTED / NUMERICAL** — Corollary 2 has no proof anywhere in the paper, and the ambiguity in (iii)(b) is established only by the single parameter vector in fn. 31 *(label downgraded by verifier from PROVED)* | p. 34, Corollary 2(ii)(iii); fn. 32 p. 33 adds a further caveat (if b is a dividend rate, b may rise as τ_l falls, so total firm value could fall as τ_l falls) |
| R15 | Higher liquidity at the exit stage strictly raises total firm value in region (ii) — even though the activist never uses the extra liquidity to *buy*, only to sell | PROVED | pp. 34–35, §3.4 via Prop. 7(ii)(c) |
| R16 | Raising b can destroy total firm value in region (ii) | NUMERICAL | pp. 32–33, fn. 31 (single parameter vector, **corrected by verifier against the rendered fn. 31**: Δ_H=100, Δ_M=1, Δ_L=−1, μ̄_G=1, **φ=0.01, α=0.1**, c=6.5, τ_s=0.3, τ_l=0.2, **λ=0.1, η=0.83**, κ=0.18, Δκ=0.01; "the total firm value strictly decreases w.r.t. b if b ≤ 0.2". The card previously swapped α↔φ and λ↔η) |
| R17 | Under a proxy-access reading of b (the perk requires *not* intending to influence), raising b destroys total firm value throughout region (ii), like the R13 policies — and **can also decrease total firm value in the q*=0 region**, by pushing value-creating activists into not intervening (added by verifier) | ASSERTED (argued in text, no proposition, no proof) | p. 40, §4.6 |
| R18 | Results survive: bad activist able to exert effort; effort microfounded as project search; continuous effort; relaxing Δ_L<0<Δ_M to Δ_L<Δ_M; non-unilateral intervention; partial sales; dynamic (repeated) disclosure; endogenous stake size α; career concerns; VC/entrepreneur reinterpretation | ASSERTED (§4 discussion only; §4.2 is argued at length in Online Appendix F, pp. 74–77, but still yields no numbered result) | pp. 35–42, §§4.1–4.9 |
| R19 | Results survive relaxing "c > ĉ" (the paper's own wording; the maintained assumption on p. 21 is c < min{c̄, ĉ}, so fn. 18 is a sign typo in the source — verifier), and survive a large measure of activists (so the market maker's prior on being approached is non-negligible) | ASSERTED ("unreported analysis") | p. 21 fn. 18; p. 23 fn. 19 |
| R20 | Liquidity reinterpretation: η, λ can be read directly as noise-trading intensity with no change to the formal model | ASSERTED (one-paragraph derivation, no numbered result) | p. 74, Online Appendix E |

## 4. Institutional facts used

All institutional material is motivation and parameter-mapping; none of it is measured or tested.

- **Schedule 13D amendments, two business days, effective 2024.** "the SEC's new rules requires that Schedule 13D amendments be filed within two business days, which became effective in 2024" — cited to sec.gov, "SEC Adopts Amendments to Rules Governing Beneficial Ownership Reporting," 10/10/2023 (p. 3, fn. 5). Repeated at p. 39, §4.5, as the motivation for modelling *dynamic* disclosure.
- **(added by verifier) He reads the adopted 2024 rule as a *selling-side* tightening.** Body text, p. 3: the SEC "implemented in 2024 new rules that restrict activists' time window to two business days for making a disclosure **when they start selling their stake**." So the only *adopted* 2024 change he uses is mapped onto λ (exit), while the 10→5 initial window — the entry margin, and our anchor — is described as merely *proposed* (p. 26, fn. 22). This is the sharpest form of the datedness point in §5 and it matters for positioning: his headline λ result sits on the margin he thinks the 2024 rule moved.
- **SEC 2022 proposals, mapped into the model's parameters** (p. 26, fn. 22): 13D amendment window to one business day → reduces λ; **initial 13D filing window from ten to five business days → reduces η**; broadening the definition of who counts as collaborating → raises κ and makes a 13D disclosure more likely even below 5%. Note he calls the ten-to-five change *proposed*, not adopted, in an April 2025 paper.
- **The 5% ownership threshold** is named exactly twice, both in fn. 22 on p. 26, purely descriptively ("the public filing activists have to make once they cross the 5% ownership threshold"). It is never a model object and is never varied.
- **13D vs 13G**: the disclosure threshold may differ if the activist does not intend to influence firm value; he denotes those alternative thresholds α₀′ and α₁′ and then shows they are irrelevant to every result (pp. 19–20, fn. 17).
- **13D "purpose of transaction"**: filers must state their purpose; this is what makes the entry disclosure informative in his model (p. 19, fn. 15 and p. 23, fn. 20).
- Section 13 reporting called the SEC's "most obvious issue" on activist short-termism, SEC Commissioner Gallagher, 6/23/2015 (p. 26, fn. 23).
- **Brokaw Act** (2016, Baldwin/Sanders/Warren), p. 26 and fn. 24.
- **Florange law** (France, double voting rights after two years) and **Toyota loyalty shares** (2015, dividend yield 0.5% year one rising to 2.5% year five) as sources of b (p. 3, fn. 6).
- **Proxy access**: 76% of S&P 500 firms as of 2019 vs 1% in 2014; typically a three-year minimum holding period (p. 7, fn. 9); the 2016 GAMCO denial, on the ground that GAMCO had filed 13D and so failed the "ordinary course of business and not with the intent to change or influence control" requirement (p. 40, fn. 38).
- **Ackman / Wendy's / Tim Hortons** (2006 spin-off; share price ~\$15 → ~\$20, later \$4–5) as the motivating adverse-selection anecdote (p. 2, fn. 3).

## 5. Referee-facing strengths / weaknesses

**Strengths.**
- The central comparative static is genuinely counter-intuitive and cleanly proved: more value destruction raises average firm value, and it is not a knife-edge — it holds on the entire region where moral hazard binds (R5, R6).
- Full analytical closure. Every numbered result has a written proof; the baseline has closed forms (5)–(8); the paper never leans on a grid.
- The policy taxonomy (A)–(D) is a real contribution: it lets him rank instruments rather than just sign one, and delivers a usable ordering (cut τ_l ≻ raise b ≻ everything else) that a policymaker could act on.
- Honest about scope of the ranking: he immediately shows in §4.6 that the ranking's winner (b) reverses under the proxy-access reading, and says so.
- Robustness section is unusually broad (nine extensions) and each is argued, not just asserted in a list.

**Weaknesses / open flanks.**
- **Liquidity is two-state, not continuous.** The market is *assumed* perfectly liquid and the market maker never reads order flow; "liquidity" is a probability of total camouflage vs. total revelation (p. 74). There is no depth, no price impact, no Kyle λ, no continuous noise variance. A referee can ask what survives when the market maker makes a partial inference — which is the standard Kyle/Back-et-al. environment.
- **(added by verifier) His own model already breaks the entry/exit symmetry — and he never says so.** In region (ii), Prop. 7(ii)(b) has V* *strictly increasing* in η but *not changing at all* in λ; Prop. 4 has V* decreasing in λ with η absent entirely; Prop. 5 moves in λ only; and in region (i) total firm value *weakly increases* in η while it *strictly decreases* in λ. Entry looseness and exit looseness are therefore distinct objects in his algebra (η enters the purchase price directly, λ only through q*), yet §3.4 and the abstract present both as "liquidity" and the policy taxonomy (C) lumps tightening η with raising κ. A referee can use this against him — and it is a hinge for us, because it is the closest thing in the paper to a "which margin" statement, made implicitly.
- **The two disclosure margins are collapsed into one scalar per stage.** A window change (ten to five business days) and a threshold change both simply "reduce η" (p. 26, fn. 22). Nothing in the model distinguishes *how long you may wait* from *how much you may hold*, yet the paper's motivation is a window reform.
- **The 13D/13G purpose partition is introduced and then neutralised** (pp. 19–20). Whether an activist's *purpose* is flagged is exactly the object the institutional motivation is about, and the model is built so that it cannot matter.
- **No empirical content at all.** No predictions section, no proxies, no testable-implications paragraph, no discussion of how a researcher would find the three regions in data. Searching all 77 pages: "empirical" appears once (p. 2, describing others' work); "testable", "prediction", "Amihud" appear zero times. Which region a given market is in — and hence the sign of every policy comparative static — is unidentified and undiscussed.
- **Everything hinges on which region you are in**, and region membership is set by κ+Δκ, an unobservable cost. R13 and R12 have opposite signs; the paper's headline is a region-(ii) statement presented as the general lesson.
- The welfare object is total NPV of interventions; there is no consumer of governance other than the activist and diffuse shareholders, and no outside party at all.
- **(added by verifier) The headline corollary is unproved.** Corollary 2 (pp. 33–34) is the sentence the abstract and the title sell, and it is the only numbered result in the paper with no proof anywhere: part (i) is an immediate restatement of Prop. 7(ii)(c), but parts (ii) and (iii) rank policies *across* regions and rest, for the ambiguity in (iii)(b), on the single numerical vector in fn. 31. Prop. 5's proof is likewise a one-line referral to Prop. 7(iii) (p. 64), and Lemma 1's "proof" in Appendix A is a pointer back to the main text (p. 48).
- Two load-bearing robustness claims rest on "unreported analysis" (p. 21 fn. 18, p. 23 fn. 19), one of which — a non-negligible measure of activists — is the assumption that keeps entry-stage pricing simple.
- Datedness: describes the ten-to-five business-day initial 13D window as a 2022 *proposal* in an April 2025 paper. It was adopted and took effect 2024-02-05.

## 6. What they do NOT do (scope boundary)

**No takeover, bidder, premium, or control-transfer object appears anywhere in the paper.** Grepped across all 77 pages: "bidder", "premium", "tender", "merger", "proxy fight" return **zero** hits. "Takeover" returns two hits, both in reference titles on p. 47 (Kyle–Vila 1991, "Noise trading and takeovers"; Stein 1988, "Takeover threats and managerial myopia"). "Control" returns hits only in reference titles (p. 45, 47) and inside the quoted GAMCO proxy-access clause (p. 40, fn. 38). The intervention is an abstract NPV shift Δ ∈ {Δ_L, Δ_M, Δ_H} — a spin-off, a CEO firing, a cost cut (p. 3) — never a change of control and never a sale of the firm.

He states the boundary himself: "In contrast to these papers, in my paper, there is no other player that affects the firm value other than the blockholder." (p. 9). No bidder, no rival acquirer, no incumbent manager who acts (management appears only in §4.3, p. 38, as an entrenched or incompetent obstacle that cannot change the equilibrium).

**Where he positions on liquidity (added by verifier, p. 8).** His related-literature paragraph names the liquidity-and-voice set we also face — Kyle and Vila (1991), Bolton and von Thadden (1998), Kahn and Winton (1998), Maug (1998), Noe (2002), Aghion–Bolton–Tirole (2004), Faure-Grimaud–Gromb (2004), Back et al. (2018) — and says: "Among these, the closest paper to mine is Maug (1998), who shows that higher liquidity might increase firm value. However, in his model, this occurs because the blockholder utilizes higher liquidity to increase his stake." His claimed liquidity novelty is therefore narrow and precisely stated: higher liquidity raises value *without* the blockholder buying more. Cite p. 8 when we say what he owns.

Also out of scope:
- **Empirics.** No data, no identification design, no proxies, no predictions section. The paper is theory only.
- **The 5% threshold as a margin.** Named descriptively once (p. 26, fn. 22); never a choice variable, never varied.
- **The window margin as distinct from the threshold margin.** Both are absorbed into η and λ.
- **The 13D/13G purpose partition.** Explicitly modelled (α₀′, α₁′) and explicitly shown irrelevant: "as I show in the analysis, this particular disclosure threshold does not make any difference for the results" (p. 19); "I also show in the analysis that this particular threshold does not matter for the results" (p. 20, fn. 17).
- **Endogenous stake size**, treated as exogenous α with a robustness argument only (p. 39, §4.5).
- **Career concerns**, explicitly set aside: "While the arguments in the paper abstract from career concerns…" (p. 41, §4.7).
- **Multiple activists per firm / competition among activists**: one activist per firm by construction (p. 18); §4.8 is about a board *choosing* between activists, not about them competing in the market.
- **Future work he names**: "a possible path for future research is to model the other kinds of blockholders in more detail to do policy comparisons for them as well" (pp. 43–44) — i.e. VCs and entrepreneurs, not control outcomes.

## 7. Implications for our position

**Where he sits, exactly.**

- **OBJECT:** expected NPV of an implemented intervention V*, and aggregate value created (μ*_B+μ*_G)V*. Plus two intermediate objects — the probability of effort ρ* and the measure of value-destroying entrants μ*_B. **Not** takeover premium, **not** bidder entry, **not** campaign success, **not** announcement return.
- **MARGIN:** two scalars, η (entry) and λ (exit), each defined as the fraction of the stake tradable before disclosure bites. Formally these are *threshold*-margin objects (α₀/α, α₁/α); he then maps the 13D **window** reforms onto them (fn. 22, p. 26). So he occupies "disclosure looseness, one scalar per side of the trade" — not the threshold margin and not the window margin, but their conflation. He never varies the 5% level and never treats the 2024-02-05 acceleration as an event.
- **IDENTIFICATION:** theory only. Analytic proof for every numbered result; one footnote numerical example; zero data.

**What this leaves open for us — three separable claims.**

1. **The control outcome is untouched.** Zero occurrences of bidder/premium/tender/merger in 77 pages, and his own boundary sentence — "there is no other player that affects the firm value other than the blockholder" (p. 9) — is the cleanest possible statement that a bidder is outside his model. Our premium wedge and bidder entry are whitespace against him. Cite p. 9 rather than the absence.
2. **The threshold/window distinction is whitespace.** Corum needs the reader to accept that a ten-to-five-business-day change and a lower stake trigger are the same parameter move (both "reduce η", p. 26 fn. 22). Our position — that the sign and size of the effect differ by margin, and that only the window moved on 2024-02-05 — is a claim he cannot make and does not make. **(added by verifier)** Two facts sharpen this. First, in his body text (p. 3) he assigns the *adopted* 2024 rule to the **exit** side ("a disclosure when they start selling their stake" → λ) and leaves the entry-side 10→5 change as a 2022 *proposal* — so the margin our anchor actually moved is, in his paper, unadopted. Second, his own comparative statics already treat η and λ as different objects (Prop. 4 and Prop. 5 move in λ only; Prop. 7(ii)(b) has V* rising in η and flat in λ; Prop. 7(i) has total firm value *weakly rising* in η while *falling* in λ). We should say the entry/exit asymmetry is visible in his algebra and unexploited in his prose — that is a stronger, citable version of "he conflates the margins" than the absence claim.
3. **The partition by purpose is whitespace, and he says so.** He introduces the 13G-vs-13D purpose distinction (α₀′, α₁′) and proves it irrelevant (pp. 19–20). It is irrelevant *in his model* because his market maker's only inference channel is the trade disclosure itself and a non-intervening blockholder carries no NPV. Once the flag changes a control outcome — whether a bidder shows up, what he must pay — the purpose partition is load-bearing again. Our identity ("the disclosure rule is the market's partition") is therefore not merely unoccupied, it is a case he ruled out by construction. That is the strongest single positioning line available from this paper.

**Where he constrains us — do not walk into these.**

- **He owns the title-level claim.** "Regulation and liquidity in activist short-termism" is his. We cannot claim novelty on "liquidity and the 13D rule interact for activism". Our claim must be stated at the level of object (control outcome), margin (threshold vs window, separately), and identification (a dated rule change with data) — never at the level of topic.
- **He owns the "looser disclosure can be good" result, with a proof.** R11/R15: raising λ (looser exit disclosure / more liquidity) strictly raises total firm value in region (ii). Any statement of ours that a stricter rule lowers welfare must not read as a rediscovery. Our disclosure-attenuation claim (draft_v2's T2) is a *sensitivity* statement — how much control outcomes move with κ — which has no counterpart in him, because he has no κ-continuum and no control outcome. Keep it stated that way.
- **He supplies a sign-flip we should expect to meet.** If our core model has both a hidden-action margin and a hidden-type margin, his mechanism (a lower exit price is what disciplines effort, so removing bad types raises the exit price and kills effort) will operate in ours too. We should either reproduce the non-monotonicity in q, or state precisely why our object (premium, not effort) breaks it. Silence on this is the referee's first question, and a referee who knows Corum will ask it.
- **His "liquidity" is not our κ.** Two-state camouflage vs. Kyle-style continuous noise intensity. Say so explicitly when we cite him — otherwise a referee reads our κ comparative statics as contradicting his and we lose an argument we should not be having.
- **(added by verifier) Do not say "tightening disclosure destroys value" flatly in his name.** The sign is region-dependent *and* margin-dependent in his own print: in region (i) tightening η (lower η) weakly *lowers* total firm value, in region (iii) it *raises* it, and in region (ii) it lowers it. His only unconditional-looking sentence is Corollary 2(i), which is a region-(ii) statement, and it is unproved. If we cite him for "looser disclosure can be good", name the region and name the parameter.
- **His hump is not our hump.** Corum's non-monotonicity is V* in q (probability the intervention is bad), maximised at q̲, and it is PROVED. Our R1 hump is minority gains in κ (liquidity) and is certified only on a grid. Do not let the two be conflated: his is a stronger result about a different variable, and the comparison flatters him.

**Deliverability read.** He costs us nothing on the empirical leg — he has none, offers no proxies, and names no design. He costs us the topic sentence. The December package should cite him early and dispose of him on object, not on mechanism.

## 8. Quotes we may lean on (verbatim, page-cited)

Words the original sets in italics are wrapped in `*asterisks*`; everything else is character-for-character.

| # | Quote (verbatim) | Page | Used for |
|---|---|---|---|
| Q1 | "Changes in liquidity or policies that make activists' exit harder can *increase* firm value if there is only moral hazard (where activist's intervention creates more value if he exerts effort) or only adverse selection (where some interventions destroy value while others create value). However, these changes *destroy* total firm value when both moral hazard and adverse selection are present." | p. 1 | The headline, exactly as stated. (Italics on *increase* and *destroy* are the original's.) |
| Q2 | "Specifically, the SEC's new rules requires that Schedule 13D amendments be filed within two business days, which became effective in 2024" | p. 3, fn. 5 | The only 2024-rule fact he uses; note "requires" is his. He cites the amendment window, never the 10→5 initial window as adopted. |
| Q3 | "Specifically, in addition to proposing (i) reducing the filing window for 13D amendments to one business day (which would reduce λ), the SEC also proposed (ii) reducing the time window for activists' initial 13D filing (which is the public filing activists have to make once they cross the 5% ownership threshold) from ten to five business days (which would reduce η), as well as (iii) broadening the definition of who collaborate with activists." | p. 26, fn. 22 | The exact mapping of window reform onto his disclosure-looseness parameters — our evidence that he conflates threshold and window margins, and the paper's only mention of 5%. |
| Q4 | "I assume that the market is perfectly liquid and hence the market maker cannot infer any information about the activist's stock accumulation if the activist does not make any disclosure" | p. 19 | There is no price impact in his market; inference runs only through disclosure. |
| Q5 | "Note that in reality, the disclosure threshold might depend on whether the activist intends to influence firm value (e.g., due to filing 13G rather than 13D). Therefore, the disclosure threshold might be different if the activist does not intend to intervene upon buying shares. To capture this possibility, I denote the threshold for this case via α₀′, where α₀′ > 0. That said, as I show in the analysis, this particular disclosure threshold does not make any difference for the results." | p. 19 | He raises the purpose partition and rules it irrelevant. Our identity claim rests on this sentence. |
| Q6 | "Importantly, since higher η (λ) represents a higher ability of the activist to camouflage his trade at the entry (exit) stage, it can also be interpreted as the *liquidity* at the entry (exit) stage." | p. 34 | Liquidity in his paper is a reinterpretation of a disclosure parameter, not a primitive. |
| Q7 | "Indeed, the point that a tighter disclosure requirement is akin to a reduction in noise trading is previously made in the literature." | p. 34 | He concedes the equivalence is borrowed (cites Back et al. 2018 §7, fn. 33) — so the identification of disclosure with liquidity is not his innovation either. |
| Q8 | "With probability λ (η), the intensity of noise trading is very high, and hence the market maker cannot make any inference about the activist's trade from the total order flow. With probability 1 − λ (1 − η), the intensity of noise trading is very low or non-existent, and hence the market maker can perfectly infer the activist's trade from the order flow." | p. 74 | The two-state liquidity microfoundation, verbatim — the sharpest contrast with a continuous κ. |
| Q9 | "This implies that higher liquidity at the exit stage can strictly increase total firm value even though the activist *never* increases his stake as a result but utilizes this higher liquidity only to *sell* his shares." | p. 35 | His liquidity result. *(verifier: the Maug (1998) point of departure is stated at **p. 8**, not on p. 35 — cite p. 8 for that.)* |
| Q10 | "In contrast to these papers, in my paper, there is no other player that affects the firm value other than the blockholder." | p. 9 | The scope boundary that excludes a bidder — our single best citation for object whitespace. |
| Q11 | "Policies that punish short-termism, act as blanket punishments, or make it more difficult to implement a value-destroying intervention destroy total firm value whenever there is adverse selection (i.e., μ*_B > 0) and moral hazard is binding (i.e., ρ* < 1), even though they only decrease μ*_B and not μ*_G." | pp. 33–34, Corollary 2(i) | The headline in its precise, region-conditional form — note it is region (ii) only. |
| Q12 | "Therefore, a possible path for future research is to model the other kinds of blockholders in more detail to do policy comparisons for them as well." | pp. 43–44 | The only future-work sentence in the paper. It points at VCs and entrepreneurs, not at control outcomes. |

## 9. Verification log

**Verifier:** adversarial second reader (opus), 2026-08-19. Method: `pdftotext -layout` re-extract of `research/txt_extracts/corum_2025_ssrn.pdf` split on form feeds so every hit carries its PDF page (= printed page, confirmed on the rendered images); every symbol-bearing quote and every proposition statement re-read from `pdftoppm -r 140/150 -png` page images (pp. 15, 16, 19, 20, 22, 26, 27, 30, 31, 32, 33, 34, 35, 74) before any verdict.

**Counts: 20 OK · 6 WRONG · 3 MISCITED · 0 UNCHECKED.**

### Quotes (§8)
| Q | Verdict | Checked against |
|---|---|---|
| Q1 | OK | p. 1 abstract, verbatim including the italicised *increase* / *destroy* (image) |
| Q2 | OK | p. 3, fn. 5, verbatim (incl. the author's own "rules requires") |
| Q3 | OK | p. 26, fn. 22, verbatim; λ/η assignments confirmed on the page image — (i) 13D/A → λ, (ii) initial 13D 10→5 → η, (iii) collaboration definition → κ |
| Q4 | OK | p. 19, verbatim |
| Q5 | OK | p. 19, verbatim including α₀′ (image) |
| Q6 | OK | p. 34, verbatim, italics on *liquidity* confirmed |
| Q7 | OK | p. 34, verbatim; fn. 33 is "See, e.g., Section 7 in Back et al. (2018)" |
| Q8 | OK | p. 74, Online Appendix E, verbatim including the λ (η) / 1−λ (1−η) pairing (image) |
| Q9 | **MISCITED** | Text verbatim at p. 35, but the "point of departure from Maug (1998)" in the Used-for column is stated at **p. 8**, not p. 35. Annotation corrected. |
| Q10 | OK | p. 9, verbatim |
| Q11 | OK | pp. 33–34, Corollary 2(i), verbatim including "(i.e., μ*_B > 0)" and "(i.e., ρ* < 1)" |
| Q12 | OK | Sentence runs p. 43 → p. 44, verbatim |

### Results (§3)
| R | Verdict | Checked against |
|---|---|---|
| R1 | **MISCITED** | Lemma 1 and eq. (1) are on p. 10 ✔, but "higher q always lowers firm value" is on p. 11, and Appendix A p. 48 contains no proof — it says the proof is "provided right after the lemma in the main text". Both fixed. |
| R2 | **WRONG** | Lemma 2(ii) reads "Suppose that c < c̄" — not "for *any* c > 0". Restated to the print. |
| R3 | OK | p. 13, Lemma 3(i)(ii)(iii) verbatim in substance |
| R4 | OK | p. 15, Prop. 1: q̲ in (5), ρ* in (6), P* = Δ_H − (1/(1−φ))(c/α) in (7), P* in (8) — all as the card states; "For any q, the equilibrium is unique" ✔; proof pp. 49–51 ✔ |
| R5 | OK | p. 16, Prop. 2, verbatim; proof pp. 51–52 ✔ |
| R6 | OK | p. 16, Corollary 1(i)(ii); proof p. 52 ✔ |
| R7 | OK | p. 22, Prop. 3; proof pp. 57–63 ✔ |
| R8 | OK | p. 27, Prop. 4 — "ρ* and V* weakly (strictly) increase in τ_s and b and weakly (strictly) decrease in τ_l and λ (if q < q̲)". η does **not** appear in Prop. 4. Proof pp. 63–64 ✔ |
| R9 | **WRONG** | Prop. 5 (p. 27, page image) moves in **λ**, not Δκ: "q* strictly decreases in τ_s and b, strictly increases in λ, and weakly increases in τ_l. Therefore, V* strictly increases in τ_s and b, strictly decreases in λ, and weakly decreases in τ_l." Corrected; also flagged that p. 64's "proof" is a one-line referral to Prop. 7(iii). |
| R10 | OK | p. 30, Prop. 6, eq. (19); proof pp. 65–67 ✔ |
| R11 | OK | pp. 30–31, Prop. 7(ii)(b)(c) verbatim on the image: (b) V* rises in η and b, falls in κ, Δκ, τ_l, unchanged in τ_s and λ; (c) total firm value falls in κ, Δκ, τ_s, τ_l and rises in η and λ. Proof pp. 67–70 ✔ |
| R12 | **WRONG** | Prop. 7(i) has total firm value **weakly increasing in η**, not falling. Only region (iii) has it falling in both λ and η. Restated both regions in full. |
| R13 | **WRONG (label)** | Statement OK, but PROVED was too strong as written: Corollary 2 has no proof in the paper. Kept PROVED with the basis named (immediate restatement of Prop. 7(ii)(c)). |
| R14 | **WRONG (label)** | Downgraded to ASSERTED / NUMERICAL: Corollary 2 is unproved, its (iii)(b) ambiguity rests solely on fn. 31's one parameter vector, and fn. 32 (p. 33) adds a caveat the card omitted. Corollary 2(iii)(a)(b)(c) now stated in full. |
| R15 | OK | p. 35 text + Prop. 7(ii)(c) |
| R16 | **WRONG** | fn. 31 (spans pp. 32–33, read from both page images) prints **φ = 0.01, α = 0.1, λ = 0.1, η = 0.83** — the card had α↔φ and λ↔η swapped. Corrected. |
| R17 | OK (with addition) | p. 40, §4.6, argued in prose, no proposition, no appendix. Added the q*=0 extension the card dropped. |
| R18 | OK | §§4.1–4.9 pp. 35–42; Online Appendix F pp. 74–77 is the §4.2 argument and yields no numbered result ✔ |
| R19 | OK (source typo noted) | p. 21 fn. 18 and p. 23 fn. 19, both "unreported analysis" ✔. fn. 18 says "the assumption c > ĉ is relaxed" while p. 21 maintains c < min{c̄, ĉ} — a sign typo in the source, now flagged. |
| R20 | OK | p. 74, Online Appendix E, one paragraph, no numbered result ✔ |

### Scope claims (§6)
- "bidder", "premium", "tender", "merger", "proxy fight" → **0 hits** across all 77 pages. **CONFIRMED.**
- "takeover" → exactly 2 hits, both reference titles on p. 47 (Kyle–Vila 1991; Stein 1988). **CONFIRMED.**
- "control" → 6 hits: 5 reference titles (pp. 45, 47) + the quoted GAMCO clause (p. 40, fn. 38). **CONFIRMED.**
- "testable", "prediction", "Amihud" → **0 hits**. **CONFIRMED.**
- "empirical" → exactly 1 hit, p. 2, describing others' work. **CONFIRMED.**
- "5%" as an ownership threshold → exactly 2 hits, both in fn. 22 on p. 26 (the p. 3 hits are Toyota's 0.5%/2.5% dividend yields). **CONFIRMED.**
- "February", "02/05", any 2024-02-05 effective date → **0 hits**; the 2024 rule is only ever the 2-business-day 13D/A (p. 3 body + fn. 5; p. 39). **CONFIRMED.**
- Market perfectly liquid, market maker updates only on disclosures → confirmed twice, p. 19 (buying) and p. 20 (selling). **CONFIRMED.**
- η ≡ α₀/α and λ ≡ α₁/α as fractions traded before disclosure bites → confirmed on the p. 19 and p. 20 images. **CONFIRMED.**
- α₀′ / α₁′ purpose thresholds shown irrelevant → p. 19 body and p. 20 fn. 17, both verbatim. **CONFIRMED.**
- One activist per firm by construction → p. 18. **CONFIRMED.**

### Header / version
Cover p. 1: title, "Adrian Aycan Corum", "April 15, 2025", earlier-title footnote — all as the card states. PDF metadata: pdfTeX, CreationDate 2025-04-16, 77 pages. Structure confirmed: body 1–44, references 45–47, Appendix A 48–52, Internet Appendix B 53–62 (B.1 proofs 54–62), C 63, D 64–73, E 74, F 74–77. **OK.**

### Omissions added
1. **§4 — p. 3 body: he assigns the *adopted* 2024 rule to the exit side** ("restrict activists' time window to two business days for making a disclosure when they start selling their stake"). The only adopted change he uses moves λ; the entry-side 10→5 window he treats as unadopted. Decision-critical for our anchor.
2. **§5 and §7 — his own algebra already breaks the η/λ symmetry.** Prop. 4 and Prop. 5 move in λ alone; Prop. 7(ii)(b) has V* rising in η and flat in λ; Prop. 7(i) has total firm value weakly rising in η and strictly falling in λ. This is a citable, in-print entry/exit asymmetry he never draws — a stronger form of our "he conflates the margins" line than an absence claim.
3. **§5 — Corollary 2, the paper's headline, has no proof anywhere** (and Prop. 5's and Lemma 1's "proofs" are pointers). Referee-facing weakness the card had inverted into a strength.
4. **§6 — p. 8 related-literature paragraph.** He names the liquidity-and-voice set (Kyle–Vila, Bolton–von Thadden, Kahn–Winton, Maug, Noe, Aghion–Bolton–Tirole, Faure-Grimaud–Gromb, Back et al.) and states his liquidity novelty narrowly against Maug (1998): value rises *without* the blockholder buying more. Cite p. 8 for what he owns.
5. **§3 R14 — fn. 32, p. 33**: if b is a dividend rate, b may rise as τ_l falls, so total firm value could fall as τ_l falls. A stated limitation on the policy ranking the card presented as clean.
6. **§3 R17 — §4.6 also says b can destroy total firm value in the q*=0 region**, not only in region (ii).
7. **§7 — the sign of "tighter disclosure" is region- *and* parameter-dependent in his print.** Added a do-not-walk-into-this bullet.

### Overall verdict
**Sound on the boundary claim, unsound on three signed comparative statics and on one honesty label.** The positioning spine — no bidder/premium/tender/merger anywhere, the p. 9 boundary sentence, the two-state liquidity of Online Appendix E, the α₀′/α₁′ neutralisation, the datedness of the 10→5 window — survives every check verbatim. But Prop. 5's parameter was misread (Δκ for λ), Prop. 7(i)'s η sign was inverted, fn. 31's parameter vector was doubly transposed, and Corollary 2 was labelled PROVED when it has no proof. All four are corrected above; the last two are the ones that would have shown up in a seminar.
