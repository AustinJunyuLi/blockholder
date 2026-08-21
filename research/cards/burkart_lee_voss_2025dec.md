# Burkart, Lee & Voss (Dec 2025 revision) — "The Evolution of the Market for Corporate Control"

> **This card is an UPDATE, not a re-read.** It records what the December-2025 revision changed
> against `burkart_lee_voss_2024.md` (the February-2024 version). Anything not mentioned here is
> unchanged in substance. Do not cite this paper from the 2024 card's page numbers any more —
> **every printed page moved.**

**Venue / status:** **ECGI Finance Working Paper N° 956/2024, cover date December 2025.** Two
internal dates: the ECGI cover and inner cover say "December 2025"; the paper's own title page says
"November 22, 2025" (printed p. 1). The PDF was produced 30 Dec 2025 (Adobe Acrobat 25.1.20997);
ECGI's working-paper page gives "last revised 29 December 2025". SSRN abstract id 4709037 (unchanged).
**THE STATUS FLAG IS CLOSED: the title page now prints "Journal of Finance, forthcoming"** (printed
p. 1). The 2024 card's open question ("no journal placement found") is answered — it is a JF accept.
The 2025 ECGI Intesa Sanpaolo Finance Prize is *not* mentioned anywhere in this file either (search
`prize`, `award`, `Intesa`, `Sanpaolo` → 0 hits), exactly as in the Feb-2024 file.

**Full text from:** `/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4/d06ccee3-762c-4331-a587-d3581e6a875e/scratchpad/lit/blv_2025dec_ecgi.txt`
(and the paired `.pdf`), fetched from
<https://www.ecgi.global/sites/default/files/2025-12/the-evolution-of-the-market-for-corporate-control.pdf>
· **Reader:** opus · **Read:** full text, 72 PDF pages (front matter, body Sections 1–6, References,
Main Proofs, Internet Appendix A.1–A.9, ECGI back matter)

**Page numbering used:** the paper's own **printed page numbers**, and the map is the same arithmetic
as the old card — **printed p. = PDF page − 3** — but it now runs to a higher number because the paper
grew. Printed pp. 1–66 (Feb 2024: 1–64); PDF pp. 70–72 are ECGI back matter with no printed folio.
Layout of the revision:

| Part | Printed pages |
|---|---|
| Body, Sections 1–6 | 1–36 |
| References | 36–41 |
| "Main Proofs" (the old Appendix A, now untitled `A.1–A.8` numbering dropped) | 41–49 |
| Internet Appendix A.1–A.9 | 50–66 |

**Type:** theory   **Role for us:** competitor (adjacent) / antecedent — **unchanged**: same object
(mode of control change), same margin (none), same identification (theory only)

---

## 0. THE APPROPRIABILITY-COEFFICIENT VERDICT (the reason this ticket exists)

**No. The revision does not derive, name, or overlap `lambda = 1 - q(1-gamma)psi`, and it contains no
microfounded premium wedge comparable to D7.** This is a clean negative on all three tests:

**Test 1 — by name.** Whole-file search of the 72-page revision:

| term | hits |
|---|---|
| `appropriab` | **0** |
| `lambda`, `λ` | **0** |
| `wedge` | **0** |
| `psi`, `ψ` | **0 as a symbol.** `ψ` = 0. The literal string `psi` returns **2** substring hits, both inside ordinary words — "Li**psi**us" (reference list, printed p. 38) and "u**psi**de" (IA A.1, printed p. 52) *(count corrected by verifier; the card said the only substring was "Lipsius")* |
| `gamma`, `γ` | **0** |
| `disclos` | 3 — two are the boilerplate "no conflicts of interest to be disclosed", one is footnote 13 (Q4 below) |
| `13D`, `Schedule`, `window`, `filing`, `Williams Act` | **0** each |

**Test 2 — by role (the harder test: does anything play lambda's part?).** In D7, `lambda` is a scalar
in [0,1] measuring *how much of the engagement improvement the bloc can appropriate at the bargaining
table*, built from a fringe-raid probability `q`, a portability parameter `gamma` (does the improvement
survive under a rival acquirer), and a pivotality factor `psi`. BLV have none of these three primitives:

- **No fringe raider.** Competing bids against the blockholder's tender offer are ruled out *by result,
  not assumption*: "any winning bid by B would result in an expected loss due to the winner's curse"
  (printed p. 51, IA A.1 "Counter-bids"). There is no outside-acquirer threat at a disagreement node,
  so nothing plays `q`.
- **No portability parameter.** BLV is a **common-value** model: every acquirer has the same
  restructuring technology, so the improvement is fully portable by construction (`gamma = 1`,
  degenerate). The one place bidders differ is Internet Appendix A.9 (printed pp. 65–66), where an
  *additive* idiosyncratic synergy `theta_i ~ G[0,1]` is bolted on top of the common `V` — an add-on
  synergy, not a discount on portability.
- **No pivotality factor.** The bloc is assumed never pivotal for control: `alpha < 1/2` throughout, and
  with several blockholders "α is sufficiently small so that the combined stake of multiple Ls never
  exceeds 1/2" (printed p. 17). `psi` has no counterpart.

**What BLV *do* have, and why it is not the same object.** Their bargaining is a plain random-proposer
Nash protocol with a single exogenous weight `rho`: with prob. `rho` the blockholder posts `P_L`, else
the bidder posts `P_B` (printed p. 9). `rho` is a primitive, never derived, and it multiplies the whole
merger price rather than an improvement. Their appropriability *is* pinned down — by the
Grossman–Hart free-rider condition `P >= E[V|P]`, which forces the pooled tender price up to the
posterior so the blockholder's only rent is on her toehold `alpha` — but they never collapse this into a
coefficient, and it has no `q`, no `gamma`, no `psi` in it.

**Test 3 — is there any premium wedge at all?** There is a *predicted ordering* of premia, and it is
now stated in the main text rather than buried, but it is a comparative statement about which mode
carries the higher price, not a derived wedge:

- Baseline (common value): "direct takeovers should be associated with larger premia and value
  improvements than takeover activism" (printed p. 13, footnote 11) — **direct takeover premium >
  activism premium**.
- With heterogeneous bidder abilities (IA A.9): the ranking **flips** — "merger invitations typically
  lead on average to higher prices and returns compared to tender offers" (printed p. 52), formalised as
  Lemma 2 and a worked example on printed p. 66 where the tender price `1/1.1` is below the expected
  merger price `1`.

The size of the gap in A.9 is the expected **second order statistic of bidder synergies**
`E[theta_2^(n)]` entering L's indifference condition (eq. 17, printed p. 66). That is a
bidder-competition object, not an appropriability coefficient: it comes from how many bidders show up,
not from what fraction of the improvement the bloc can hold up.

**Consequence for us:** D7 is safe. Our `lambda` is not scooped, not renamed, and not implicitly
derived. What *did* change is that BLV now state the premium-ordering prediction in the main text
(printed p. 13), so a referee is likelier to have it in mind — our wedge must be positioned against
footnote 11, not only against the buried IA discussion the old card cited.

---

## 1. Question

**Unchanged.** Same question, same answer, restated. The abstract was rewritten and is now shorter and
less market-evolution-forward; the new closing sentence names the mechanism as intermediation: "Our
model shows how such an evolution, characterized by a symbiotic relationship between investor activism
and private equity, arises to overcome asymmetric information and collective action problems through
intermediated transactions" (printed p. 1). The intermediation framing (bidder chains as intermediation
chains à la Glode & Opp) is promoted from a footnote to a stated contribution.

## 2. Model / data and method — what changed

**The model is unchanged in every primitive, assumption and equilibrium notion.** `alpha` exogenous and
bought at price 0; `V ~ F[0,1]` log-concave; A1 (tendering rule), A2 (Grossman–Perry credible beliefs),
A3 (log-concavity), A4 (the market-model parameter restriction); Perfect Sequential Equilibrium;
random-proposer Nash bargaining with weight `rho`. Proposition 1's cutoff condition is character-for-
character the same equation. The Figure 4 numeric example is the same (`U[0,1]`, `alpha = 25%`,
`V_1* ≈ 0.67` vs `V_0* = 0.6`; `alpha = 10%` → `V_1* ≈ 0.86`, printed p. 14), and the footnote parameter
check is the same (`rho < 0.958851`, now footnote 16, printed p. 19).

**What moved (this is the whole delta).** The paper was reorganised for the journal: two in-body
discussion subsections were emptied into a much larger Internet Appendix, and the empirics section grew.

| Feb 2024 | Dec 2025 |
|---|---|
| §2.4 "Discussion" (counter-bids, bidding competition, value-decreasing changes, defences, means of payment) in the body, printed pp. 19–20 | **Moved out.** Body keeps only a one-paragraph pointer, "Discussion of Assumptions. Internet Appendix A.1 discusses…" (printed p. 16); the content is IA A.1, printed pp. 50–53 |
| §3.3 "Discussion of Market Modeling Assumptions" (stake prices, Kyle/Kyle–Vila, multiple Ls, dilution, endogenous growth) in the body, printed pp. 30–32 | **Moved out.** Body keeps a one-paragraph pointer (printed p. 25); content is IA A.3, printed pp. 54–59 |
| Online Appendix A.1–A.2 only (bidder heterogeneity + one example) | **Internet Appendix A.1–A.9**, printed pp. 50–66 — nine subsections. New/expanded: A.2 (formal proof that L's profit rises in `alpha`), A.4 (expected-profit case analysis), A.5 (market growth without frictions), A.6 (relation to intermediation chains), A.7 (a list of real Icahn/Singer/Ackman campaigns), A.8 (alternative explanations — the legal-change discussion), A.9 (the old bidder-heterogeneity appendix, now with the "Bidder Heterogenity" typo fixed and the Appendix-A name collision resolved) |
| §3.4 "Disciplinary Ownership Changes: Empirical Patterns", printed pp. 32–36, **one** own-drawn data figure (IMAA hostile-takeover counts) | **§5, same title**, printed pp. 29–35, **three** own-drawn data figures: Fig. 10 (hostile takeovers vs total M&A vs M&A by financial acquirers, IMAA), Fig. 11 (hostile takeovers normalised by the number of listed US firms, World Bank), Fig. 12 (public-to-private buyouts vs hostile takeovers vs hedge-fund activism, data "generously provided by" Renneboog & Vansteenkiste 2017 and Brav et al. 2022) |
| 8 figures total | **12 figures total** (Figs. 1–9 model, Figs. 10–12 data) |
| 70 PDF pages, printed 1–64 | 72 PDF pages, printed 1–66 |

**Method: still pure theory.** Section 5 is still narrative, still estimates nothing. The three data
figures are re-plots of public or donated series with no test, no regression and no calibration — the
2024 card's ASSERTED label on this section survives untouched. The addition is *more* re-plotted series
and a normalisation (Fig. 11), not identification.

## 3. Results — with honesty labels

**No proposition was added, dropped, renumbered or restated.** The count is identical: **7 propositions
+ 2 lemmas + 1 corollary**, with the same content and the same labels as R1–R16 on the 2024 card. Only
the page anchors moved. Use this table to re-anchor:

| 2024 card | Result | Label (unchanged) | Feb-2024 printed p. | **Dec-2025 printed p.** |
|---|---|---|---|---|
| R1 | Lemma 1 (SV 1986 benchmark) | PROVED (proof deferred to SV) | 13 | **11** (proof p. 41) |
| R2 | Proposition 1 (unique cutoff `V_1*`) | PROVED | 16 | **13** (proof pp. 41–44) |
| R3 | Corollary 1 (substitution + complementarity ⇒ efficiency) | PROVED, still **no proof of its own** | 17 | **15** |
| R4 | Smaller `alpha` raises `V_1*` | PROVED | 19 | **15–16** |
| R5 | Proposition 2 (three market stages) | PROVED | 24 | **19** (proof pp. 44–45) |
| R6 | Proposition 3 (activism rises with `n`) | PROVED | 27 | **21** (proof pp. 45–46) |
| R7 | Efficiency decomposition, eqs. (7)–(8) | **DERIVED IN TEXT** (no proposition, no proof) — label survives | 29–30 | **24** |
| R8 | Proposition 4 (block trade replicates `V_1*`) | PROVED | 37 | **26** (proof p. 46) |
| R9 | Proposition 5 (informed bidder, two cutoffs) | PROVED | 38 | **26** (proof pp. 46–47) |
| R10 | Proposition 6 (bidder chain, existence only) | PROVED (existence) | 40 | **28** (proof pp. 47–49) |
| R11 | Proposition 7 (chain → efficiency in the limit) | PROVED | 41 | **28** (proof p. 49) |
| R12 | Lemma 2 (bidder heterogeneity) | PROVED | 56 (Online App.) | **66** (IA A.9) |
| R13 | Fig. 4 numeric example | NUMERICAL | 17 | **14** |
| R14 | Second numeric example, `V* = (1−α)/(1+α) = 0.9/1.1`, `P* = 1/1.1` | NUMERICAL | 57 | **66** (IA A.9) — the print is unchanged, so the 2024 card's *corrected* version of R14 is the right one |
| R15 | The four secular trends "broadly match" | ASSERTED | 32–36 | **29–35** |
| R16 | Takeover-defence explanation incomplete | ASSERTED | 35–36 | **63–64** (moved into IA A.8) |

**One new result-bearing sentence (not a proposition).** The premium-ordering prediction is now stated
in the main text: footnote 11, printed p. 13 (see §0 and Q3). Label: **ASSERTED in the body / PROVED in
IA A.9 for the reversed case** (Lemma 2 + eq. 17 + the printed-p.-66 example).

## 4. Institutional facts used — what changed

Still **no legal rule, threshold or filing window is used anywhere in the model.** But the revision adds
three institutional touches the 2024 version did not have, and one of them lands on our margin:

1. **A disclosure-regulation sentence, new.** Footnote 13 (begins printed p. 16, the clause sits on
   printed p. 17) now says the stake size is capped by, among other things, disclosure rules — see Q4.
   In Feb 2024 the word `disclos` appeared **zero** times in the whole paper. It now appears once in
   substance. This is a *concession* in a footnote, not a model ingredient: `alpha` remains exogenous
   and remains bought at the current share value of 0.
2. **The 1992 proxy-communication reform, new.** Two mentions: as a supply-side driver, "regulatory
   changes enabling active shareholders to press for changes more effectively (Sharara &
   Hoke-Witherspoon 1993, Fos 2017)" (printed p. 30); and in IA A.8, "The reform of shareholder
   communication laws in 1992 made it easier for shareholders to challenge management, e.g., through
   proxy fights" (printed p. 63). This is the first named US securities-law change in the paper.
3. **A 5-percent block figure, new but not the 13D threshold.** Barclay & Holderness (1992), "a sample
   of 106 block trades (all involving blocks of at least 5 percent of the outstanding shares)", of which
   "half … ultimately lead to the firm being acquired by the block purchaser or a subsequent owner of
   the same block", and "most block purchasers pay minority shareholders at least as much per share as
   they report paying the block seller" (printed p. 29). This is Barclay–Holderness's *sample* cut, not
   a statutory trigger, and BLV use it as evidence that block-trade-then-tender sequences occur.

New empirical magnitudes added in §5 (all second-hand): Fos (2017) — dissidents demand governance
changes in about 39% and a sale of the target in about 29% of proxy fights (printed pp. 33–34);
Greenwood & Schor (2009) — only 18.11% of "sale of asset" campaigns involve a bid by the activist
(printed p. 35); Brav et al. (2021, Fig. 1) — campaigns grew from below 10 in 1994 to around 200 (175
funds) in 2018 (printed p. 34). The Brav et al. (2021) Table-1 numbers survive with the two categories
**swapped in the sentence order**: now "'Governance' and 'Sale of target' … about 35.5% and 18.5%"
(printed p. 33; the Feb-2024 sentence read "'Sale of target company' and 'Governance' … 18.5% and
35.5%"). Same numbers, different word order — the old Q10 no longer matches character-for-character.

Dropped from the body: the Statista hedge-fund-AUM ×50 figure, the Bain buyout deal-value $30bn →
$1,121bn figure, the Kaplan–Stromberg $200m → $200bn figure and the Braun et al. ~$300bn → ~$2.4tn
figure are all **gone as printed numbers**. §5 now cites the same sources but in prose, without the
magnitudes ("have grown enormously over the last decades in terms of capital inflow, assets under
management, and number of funds", printed p. 30). If we were going to borrow BLV's AUM numbers, they
are no longer in the paper — go to the primary sources.

## 5. Referee-facing strengths / weaknesses — what changed

**Strengths, added.** (i) The paper is now a JF acceptance, which raises its standing as the reference
theory of the control market — our whitespace argument must survive a reader who has just seen this in
JF, not a working paper. (ii) The empirical section is materially better: three figures instead of one,
a normalisation by the number of listed firms (Fig. 11) that pre-empts the obvious "it is just the
delisting wave" objection, and donated campaign/buyout series. (iii) IA A.5 ("Market Growth without
Frictions", printed pp. 60–61) is a new and genuinely useful robustness argument: they show that entry
*alone*, absent free-riding and asymmetric information, produces only a scale effect and no shift in
mode — closing the "your result is just more capital" hole a referee would have poked.

**Weaknesses, mostly unchanged, one softened and one sharpened.**
- The empirical section is **still narrative**. More figures, still no test that discriminates their
  mechanism from the takeover-defence story. The Feb-2024 concession that AUM numbers "considerably
  overstate" the relevant subset survives in gentler wording: "Not all of this growth maps directly into
  a growth of the 'control-oriented investors' in our model" (printed p. 30). The blunt "considerably
  overstate" sentence (old Q9) is **gone**.
- The stake is **still bought at price zero**, and the concession is still there but now in the Internet
  Appendix (printed pp. 54–55), plus the new footnote-13 acknowledgement (Q4). Weaker placement, same
  admission.
- The dilution / "lead L" tractability device is unchanged, and the "formalizing them would be rather
  cumbersome" line survives verbatim in IA A.3 (printed p. 56).
- **New, and it cuts our way:** the main text now concedes on the record that the mature-stage result is
  an artefact — "a formal analysis of this is not feasible in the market model" (printed p. 21),
  referring to competition for toeholds among multiple Ls. In Feb 2024 this admission sat in a
  discussion subsection; it is now in the body next to Proposition 2.
- The Feb-2024 Online-Appendix mislabelling ("A Online Appendix / A.1 Bidder Heterogenity", sic) is
  **fixed**: the Internet Appendix is now cleanly `A.1`–`A.9` and the typo is gone. Do not repeat that
  criticism.

## 6. What they do NOT do (scope boundary) — the part most at risk, re-checked

The 2024 card's core scope claim **survives**, but two of its supporting sentences do not. Re-run,
whole-file, on the Dec-2025 text:

| term | Feb 2024 | **Dec 2025** | where |
|---|---|---|---|
| `disclos` | 0 | **3** | 2 × "no conflicts of interest to be disclosed" (front matter); **1 substantive**, footnote 13, printed p. 17 — Q4 |
| `13D`, `Schedule`, `window`, `filing`, `five business`, `Hart-Scott` | 0 | **0** | — |
| `Williams` | 1 (inside "McWilliams") | **1** (inside "McWilliams", Denes–Karpoff–McWilliams reference, printed p. 38) | no Williams Act |
| `liquid` | 2 lines | **3 lines** | footnote 13 "stock market liquidity" (p. 17); "liquidate or sell the company" inside the 1976 Icahn quote (p. 35); the Maug (1998) reference title (p. 40) |
| `toehold` | 2 | **10** | pp. 21 (×2), 25, 53, **56**, 61 (×2), **65** (×3) *(page list corrected by verifier; the card said "21, 25, 53, 61, 64" — the count 10 was right, the pages were not)* — mostly the new IA A.3/A.5/A.9 passages |
| `5 percent` | 0 | **1** | Barclay & Holderness sample cut, printed p. 29 |

**The margin is still unoccupied.** There is still no disclosure rule, no filing window, no Schedule
13D, no Williams Act, no regulator threshold anywhere in 72 pages. `alpha` is still exogenous and still
bought at price 0, so there is still **no stake-accumulation margin for a threshold rule to bind on.**

**But the "market liquidity plays no role" sentence is GONE.** This is the single most consequential
break for us. The Feb-2024 sentence — "Market liquidity plays no role in our analysis, whose distinct
feature is that the large shareholder chooses which party ultimately acquires control and implements the
restructuring" (Feb-2024 printed p. 9) — was the 2024 card's Q1 and the INDEX's headline whitespace
quote. **It does not exist in the Dec-2025 revision.** The paragraph that contained it (the Maug 1998
discussion in the related-literature section) was rewritten and compressed to a single sentence,
"Four papers in this literature allow for a choice between intervention modes…" (printed p. 7, Q1).
Nothing replaced the liquidity disclaimer. In its place we get the weaker, opposite-signed footnote 13,
which *acknowledges* stock market liquidity as a real constraint on stake size (Q4).

**What replaces Q1 as our whitespace evidence.** Q5/Q6 below — the Kyle/Kyle–Vila abstraction — survive
**verbatim**, just relocated from the body (Feb-2024 printed p. 30) to Internet Appendix A.3 (Dec-2025
printed pp. 54–55). They are strictly better quotes anyway: they name the exact price-formation channel,
describe the comparative static it would produce, and declare it "orthogonal" on purpose. **Use Q5/Q6
where the old card used Q1, and note that they now sit in the Internet Appendix** — a referee who checks
will find them in the IA, and citing them as body text would be a miscite.

**Exit is still declared out of scope, verbatim** — "We abstract here from exit as an intervention mode"
(footnote 6, printed p. 7, moved from Feb-2024 printed p. 8, footnote 9). Q2 below. Our second signed
absence survives intact.

**Revelation is still by action, not by rule.** The Proposition 5 truncation logic and the bidder-chain
signalling are unchanged; the sentence the 2024 card quoted (Q17) was reworded slightly — it now reads
"The fact that L abstained from making a tender offer credibly reveals that the possible value
improvements are truncated to the subset [0, V̄_1] when B makes her bid" (printed p. 27; the Feb-2024
version opened "The very fact that…"). Same mechanism, new wording. IA A.6 (printed pp. 61–62) makes the
same point in the intermediation frame: "each consecutive block trade further truncates the
shareholders' posterior belief."

**Explicitly deferred / open questions.** Same list, new locations, with two changes: the collusion /
insider-trading open question ("warrant further scrutiny that is beyond the scope of this paper",
Feb-2024 printed p. 43) is **deleted** — the whole discussion paragraph about cross-over
activist/buyout firms is gone from the revision. And a new deferral appears: "It is beyond the scope of
this paper to incorporate a fully fledged model of endogenous growth in the control investment sector"
(printed p. 58, IA A.3) — Q9.

**Identification.** Theory only, unchanged.

## 7. Implications for our position

**The verdict in one line: our position is unharmed, our page cites all move, and one of our two
headline whitespace quotes has to be swapped.**

1. **D7 is safe.** See §0. No `lambda`, no appropriability coefficient, no microfounded wedge. Our
   tender-game microfoundation remains ours.
2. **The margin is still empty.** Zero `13D`, zero window, zero threshold in 72 pages. The one new
   `disclos` hit (Q4) is a footnote that *acknowledges disclosure regulation as a real-world cap on
   stake size and then abstracts from it*. Read carefully, this is **better for us than silence**: the
   leading theory of the control market, in JF, now says on the record that disclosure regulation
   constrains the blockholder's stake — and does not model it. That is a competitor naming our margin
   as a real friction and declining it. Pair Q4 with Q5/Q6 in the introduction.
3. **Swap Q1 for Q5/Q6 everywhere.** "Market liquidity plays no role in our analysis" no longer exists.
   If it goes into draft_v3 or the INDEX as a live quote it is a false citation to a JF-forthcoming
   paper — the worst kind of error to make. Replace with Q5 ("In a setting with rational investors and
   noise traders (e.g., Kyle (1985), Kyle & Vila (1991))…") and Q6 ("We intentionally abstract from this
   effect because it is orthogonal to our main result…"), both Internet Appendix A.3, printed pp. 54–55.
4. **Position our wedge against footnote 11, not against the appendix.** The premium-ordering prediction
   ("direct takeovers should be associated with larger premia … than takeover activism", printed p. 13)
   is now in the main text. If our `m_1 − m_0` says an engaged target fetches *more*, we must state
   plainly that our engagement is not their merger invitation — a referee who has read the JF version
   will have footnote 11 fresh. Their own reversal (heterogeneous abilities, printed p. 52, Q8) and
   Boyson et al. (2017) are the counterweight to cite alongside.
5. **The prize + JF acceptance raise the bar.** This is no longer "a working paper in the adjacent
   cell"; it is the JF paper on the mode of control change. Our contribution paragraph must not read as
   a correction of it. Frame ours as the complement they explicitly declined (Q5/Q6) on a margin they
   explicitly name and skip (Q4).
6. **Their "entry alone is not enough" argument (IA A.5) is a template we should borrow.** They pre-empt
   "your result is just more capital" by showing what the model gives with the frictions switched off
   (printed pp. 60–61). Our analogue — showing what our model gives with the *partition* switched off,
   so that liquidity alone does not produce the result — is the same defensive move, and a referee who
   has seen theirs will expect ours.

**Constraints on us: unchanged.** Do not claim novelty on the buy-side/sell-side choice (Prop. 1), on
"activism displaced hostile tender offers" (Prop. 3), or on full efficiency from the sell-side option
(Corollary 1 — still firm-level; the market-level caveat survives at printed p. 23, Q7).

## 8. Quotes we may lean on (verbatim, page-cited)

All quotes below were located in the December-2025 full text and are reproduced character-for-character
from it. Page = the paper's own **printed** page number. The "unique search string" column is the
shortest substring a verifier can grep to land on the quote uniquely.

| # | Quote (verbatim) | Printed p. | Unique search string | Used for |
|---|---|---|---|---|
| Q1 | "Four papers in this literature allow for a choice between intervention modes: Shleifer & Vishny (1986), Bebchuk & Hart (2001), Maug (1998), and Burkart & Lee (2022)." | p. 7 | `allow for a choice between intervention modes` | Their map of the intervention-mode literature — the slot our four-action model claims. **Replaces the 2024 card's Q15, which said "Only four papers … allow the large shareholder to choose between intervention modes" and no longer exists.** |
| Q2 | "We abstract here from exit as an intervention mode." | p. 7, fn. 6 | `abstract here from exit as an intervention mode` | Signed absence on our exit margin — survives the revision verbatim (was p. 8, fn. 9) |
| Q3 | "This implies that direct takeovers should be associated with larger premia and value improvements than takeover activism." | p. 13, fn. 11 | `larger premia and value improvements than takeover activism` | **New in the main text.** Their premium-ordering prediction — the sign our wedge must be distinguished from |
| Q4 | "assumed that the size of L's initial take is limited by constraints such as disclosure regulation and stock market liquidity." | p. 17, fn. 13 (footnote begins p. 16) | `limited by constraints such as disclosure regulation` | **The single new sentence on our margin.** Disclosure regulation named as a real cap on stake size, then abstracted from. Note: the print says "initial take", not "initial stake" — a typo in the paper; quote it as printed |
| Q5 | "In a setting with rational investors and noise traders (e.g., Kyle (1985), Kyle & Vila (1991)), share prices should generally reflect that control investors buy shares in some firms and bring about value improvements." | p. 54, **Internet Appendix A.3** | `rational investors and noise traders` | They name the price-formation channel they omit. Survives verbatim; **relocated from the body to the IA** |
| Q6 | "We intentionally abstract from this effect because it is orthogonal to our main result that takeover activism increasingly replaces direct takeovers as the prevalent mode of control change when more control investors enter the market." | p. 55, **Internet Appendix A.3** | `intentionally abstract from this effect because it is orthogonal` | The explicit out-of-scope declaration on trading and price formation. **This is now our best whitespace quote, in place of the deleted Q1 of the 2024 card** |
| Q7 | "While all potential value improvements are realized in case (a), the market does not attain full efficiency in case (b)." | p. 23 | `does not attain full efficiency in case` | Market-level efficiency caveat — stops us overstating their benchmark. (2024 card's Q18; "Case" is now lowercase "case", so the old string no longer matches) |
| Q8 | "If one adds idiosyncratic restructuring abilities to our common value framework, merger invitations typically lead on average to higher prices and returns compared to tender offers." | p. 52, **Internet Appendix A.1** | `idiosyncratic restructuring abilities to our common value framework` | The reversal of Q3 — the version of their premium prediction that runs *with* our wedge |
| Q9 | "It is beyond the scope of this paper to incorporate a fully fledged model of endogenous growth in the control investment sector." | p. 58, **Internet Appendix A.3** | `fully fledged model of endogenous growth` | Their live open question in the revision (replaces the deleted collusion/insider-trading deferral) |
| Q10 | "A different narrative for the observed trends is based on legal changes. It is in our view incomplete." | p. 63, **Internet Appendix A.8** | `A different narrative for the observed trends is based on legal changes` | Their anti-legal-explanation claim, now demoted to the IA. Quote alongside Q11 to avoid a straw man |
| Q11 | "This trend is typically attributed to legal changes. But as we show, it emerges endogenously as the capital available to investors who seek to implement control changes in underperforming firms grows." | p. 36 | `it emerges endogenously as the capital available to investors` | The conclusion's one-liner; survives verbatim (2024 card's Q13, was p. 42) |
| Q12 | "Barclay & Holderness (1992) study a sample of 106 block trades (all involving blocks of at least 5 percent of the outstanding shares)." | p. 29 | `sample of 106 block trades` | **New.** The only 5-percent figure in the paper — a sample cut, not a statutory trigger |
| Q13 | "The reform of shareholder communication laws in 1992 made it easier for shareholders to challenge management, e.g., through proxy fights." | p. 63, **Internet Appendix A.8** | `reform of shareholder communication laws in 1992` | **New.** The first named US securities-law change in the paper — and it is the 1992 proxy reform, not the Williams Act |
| Q14 | "Journal of Finance, forthcoming" | p. 1 | `Journal of Finance, forthcoming` | Status: closes the 2024 card's open placement flag |

### 8b. Old-card quotes: survival audit

Checked by whitespace-normalised substring match against the Dec-2025 full text, page by page.

| 2024 card | Verdict in the Dec-2025 revision |
|---|---|
| Q1 "Market liquidity plays no role in our analysis…" | **BROKEN — deleted.** No trace anywhere in 72 pages. Do not cite. |
| Q2 "the mode of control change has since shifted…" | SURVIVES verbatim, p. 2 (was p. 2) |
| Q3 "The equilibrium features a simple cut-off structure…" | **REWORDED.** The revision reads "The equilibrium features a simple cut-off structure: For all firm types above the cutoff, the large shareholder takes over the firm herself, whereas she initiates a sale to the outside bidder otherwise." (p. 3). Opening clause identical, remainder rewritten — re-quote from the new text |
| Q4 (Kyle/Kyle–Vila) | SURVIVES verbatim → **now Q5**, moved to IA A.3, p. 54 |
| Q5 ("intentionally abstract … orthogonal") | SURVIVES verbatim → **now Q6**, moved to IA A.3, p. 55 |
| Q6 "Strikingly, the control allocation is fully efficient…" | **BROKEN — deleted.** Replaced by the plainer "The control allocation in Proposition 1 is efficient: All firms are successfully restructured." (p. 15). The word "Strikingly" and the "for any initial stake size α > 0 however small" clause are gone |
| Q7 "Our theory posits that a growing influx…" | **BROKEN as a string — one word changed** *(corrected by verifier 2026-08-21; the card said "SURVIVES verbatim")*. The Dec-2025 print reads "…causes a shift from direct takeovers **towards** takeover activism" (printed p. 29); the 2024 card's string has "toward". Zero exact matches in the file. Substance and page are right — re-quote from the new text, do **not** paste the 2024 string |
| Q8 "…warrant further scrutiny that is beyond the scope of this paper." | **BROKEN — deleted** with the whole cross-over collusion paragraph. Use Q9 instead |
| Q9 "…considerably overstate the growth of the subset of funds…" | **BROKEN — deleted**, softened to "Not all of this growth maps directly into a growth of the 'control-oriented investors' in our model" (p. 30) |
| Q10 Brav Table 1 campaign objectives | **BROKEN as a string** — the two categories were swapped in the sentence: now "'Governance' and 'Sale of target' … respectively, about 35.5% and 18.5% of activist campaigns" (p. 33). Same numbers, re-quote from the new text |
| Q11 "In our common value model, a merger invitation signals a lower value improvement…" | SURVIVES verbatim, moved to IA A.1, p. 51 |
| Q12 "Our model presupposes a large shareholder with sufficient influence to remove takeover defenses…" | **BROKEN — deleted.** The defences discussion was rewritten into IA A.1 "Takeover defenses" (pp. 52–53), which now argues the *shareholders* would not restrict L's mode choice. Different argument, no equivalent sentence |
| Q13 "This trend is typically attributed to legal changes…" | SURVIVES verbatim → **now Q11**, p. 36 (was p. 42) |
| Q14 "We abstract here from exit as an intervention mode." | SURVIVES verbatim → **now Q2**, p. 7, fn. 6 (was p. 8, fn. 9) |
| Q15 "Only four papers in this literature allow the large shareholder to choose between intervention modes…" | **BROKEN — reworded** to Q1 above. Same four papers, new sentence |
| Q16 Boyson et al. on larger premia | SURVIVES verbatim, moved to IA A.1, p. 52 |
| Q17 "The very fact that L abstained…" | **BROKEN — reworded** to "The fact that L abstained from making a tender offer credibly reveals that the possible value improvements are truncated to the subset [0, V̄_1] when B makes her bid." (p. 27). Same mechanism |
| Q18 "…the market does not attain full efficiency in Case (b)." | **BROKEN as a string** — "Case" → "case". Re-quote as Q7 above, p. 23 |
| Q19 "In the extant literature, this shift is commonly attributed to…" | **BROKEN — rewritten.** The revision's body says "In the extant literature this shift is usually attributed to the proliferation of takeover defenses and legal changes that facilitate shareholder activism. We contend that this does not provide a comprehensive explanation." (p. 5) — note "usually", the dropped "We agree that these changes impact the market for corporate control", and the different list. Re-quote from the new text; the concession is now weaker |

**Score: 7 of 19 old quotes survive verbatim (4 of them relocated into the Internet Appendix), 12 are
broken.** *(Corrected by verifier 2026-08-21: the card said 8 / 5 / 11. Q7 is a one-word change, not a
survival — see its row.)* The seven survivors are **Q2** (p. 2), **Q4** (IA A.3, p. 54), **Q5** (IA A.3,
p. 55), **Q11** (IA A.1, p. 51), **Q13** (p. 36), **Q14** (p. 7, fn. 6) and **Q16** (IA A.1, p. 52); the
four in the Internet Appendix are Q4, Q5, Q11 and Q16. Of the broken ones, four (Q1, Q6, Q8, Q9) are
outright deletions with no replacement sentence; the rest are rewordings, of which Q7's is the
smallest and therefore the easiest to paste in by mistake.

## 9. Verification log

*(To be filled by an independent verifier. Every quote in §8 carries a printed page and a unique search
string; the §8b survival audit and the §0 grep counts are the two items a verifier should re-run first,
since the whole point of this card is the delta. Source of record: the Dec-2025 PDF/text named in the
header, `pdftotext -layout`, 73 form-feed-delimited pages = 72 real + 1 empty trailer, printed
p. = PDF page − 3, confirmed by reading the printed folio at the foot of PDF pp. 4 (printed 1) through
69 (printed 66).)*

**Reader's own checks, already run:**
- Page map: folio read off every page; `printed = PDF − 3` holds from PDF p. 4 to PDF p. 69. Last
  printed page is 66.
- §0 term counts: run whole-file on the `pdftotext -layout` extraction, case-insensitive.
- §8 quotes: each located by whitespace-normalised substring match against the single PDF page implied
  by its printed-page citation; all 14 matched on exactly one page.
- §8b: each 2024-card quote normalised (curly quotes, dashes, non-breaking spaces folded) and searched
  across all 73 page blocks; "BROKEN" means zero matches anywhere in the file, not merely a page move.
- Proposition/lemma enumeration: 7 propositions + 2 lemmas + 1 corollary, identical to Feb 2024.
- Figure enumeration: 12 figure captions (Figs. 1–12); Figs. 10–12 are the data figures.

**Open flag (one).** The claim that ECGI's page says "last revised 29 December 2025" is external to this
PDF and is carried over from the 2024 card's §9b fetch log; the document itself is dated November 22,
2025 (title page) / December 2025 (ECGI cover), and the PDF was created 30 Dec 2025. Nothing in the
card's substance depends on which of these dates is used.

---

### Independent verification (opus, adversarial, 2026-08-21 — ticket 04 batch)

Separate agent; did not read the paper for content and never saw the reader's reasoning. Everything
below was executed against `…/scratchpad/lit/blv_2025dec_ecgi.txt` (73 form-feed blocks), with the page
map **re-derived, not assumed**: the printed folio was read off PDF pp. 53 (→ 50) and 69 (→ 66), giving
**printed = PDF − 3**, and PDF p. 73 is an empty trailer. All searches Unicode-normalised and
whitespace-collapsed. PDF metadata read directly: **72 pages, Creator/Producer "Adobe Acrobat (64-bit)
25.1.20997", CreationDate 30 Dec 2025** — the header's production claims hold.

**Counts: 61 OK · 1 WRONG · 3 MISCITED · 1 UNCHECKED.**

#### DECISION-CRITICAL 1 — the D7-safety verdict (§0). **SURVIVES. Greps re-run from scratch.**

| Term | Verifier's own count | Verdict |
|---|---|---|
| `appropriab` | **0** | OK |
| `lambda` / `λ` | **0 / 0** | OK |
| `wedge` | **0** | OK |
| `ψ` | **0** | OK |
| `gamma` / `γ` | **0 / 0** | OK |
| `13D`, `Schedule`, `window`, `filing`, `five business`, `Hart-Scott` | **0 each** | OK |
| `Williams` | **1**, inside "McWilliams", printed p. 38 (reference list) — no Williams Act | OK |
| `disclos` | **3** — printed p. −1 (ECGI inner cover) and printed p. 1 (the paper's own title page), both the boilerplate "There are no conflicts of interest to be disclosed"; plus **one substantive**, footnote 13, printed p. 17 | OK on the count; see MISCITED 3 on where the two boilerplate hits sit |
| `liquid` | **3 lines**, printed pp. 17, 35, 40 — exactly the three the card describes | OK |
| `5 percent` | **1**, printed p. 29 | OK |
| `prize`, `award`, `Intesa`, `Sanpaolo` | **0 each** | OK |
| `psi` (literal string) | **2** — see MISCITED 1 | MISCITED |
| `toehold` | **10**, but on different pages — see MISCITED 2 | MISCITED |

**Test 2 (role) — every supporting anchor confirmed.** "any winning bid by B would result in an
expected loss due to the winner's curse" is on printed **p. 51**, under the IA A.1 heading
"Counter-bids" (both on that page). "α is sufficiently small so that the combined stake of multiple Ls
never exceeds 1/2" is on printed **p. 17**. The bargaining protocol with the single weight `ρ` is on
printed **p. 9** (`ρ` occurs 100 times across pp. 9–46; the ASCII string `rho` occurs 0 times, so the
card's `rho` is a transliteration, not a quotation). Grossman–Perry credible beliefs (A2) confirmed on
pp. 9, 10, 42. **Test 3** — the IA A.9 add-on synergy `θ_i ~ G[0,1]` is on printed pp. 65–66, eq. (17)
and the `1/1.1` vs `1` example are on printed **p. 66**, and the "Bidder Heterogenity" typo returns
**0** hits (fixed, as the card says); the A.9 heading now reads "Bidder Heterogeneity", printed p. 65.

**Verdict: D7 is safe, exactly as §0 claims.** No `lambda`, no appropriability coefficient, no
microfounded wedge; and no primitive plays `q`, `gamma` or `psi`.

#### DECISION-CRITICAL 2 — is the 2024 card's Q1 really deleted? **YES. Confirmed, hard.**

"Market liquidity plays no role in our analysis, whose distinct feature is that the large shareholder
chooses which party ultimately acquires control and implements the restructuring." was searched
whole-file, normalised, and then progressively shortened. **Not only the full sentence but the
three-word fragment "plays no role" returns zero hits in all 73 page blocks.** The sentence does not
exist in the Dec-2025 revision in any form. §7 item 3 ("if it goes into draft_v3 it is a false citation
to a JF-forthcoming paper") is correct and should be treated as a hard rule.

#### Quotes (§8) — **14/14 OK.**

Each matched as a whole normalised sentence and returned exactly one page block, equal to the citation:
Q1 p. 7 · Q2 p. 7 · Q3 p. 13 · Q4 p. 17 · Q5 p. 54 · Q6 p. 55 · Q7 p. 23 · Q8 p. 52 · Q9 p. 58 ·
Q10 p. 63 · Q11 p. 36 · Q12 p. 29 · Q13 p. 63 · Q14 p. 1. Q4's "initial take" (not "initial stake") is
genuinely the print. The IA-location flags on Q5, Q6, Q8, Q9, Q10 and Q13 are all correct.

#### §8b survival audit — 18 of 19 rows correct, **1 WRONG.**

Every 2024-card quote was normalised and searched across all 73 blocks. Seventeen rows reproduced the
card's verdict exactly (Q1, Q3, Q6, Q8, Q9, Q10, Q12, Q15, Q17, Q18, Q19 absent everywhere; Q2 p. 2,
Q4 p. 54, Q5 p. 55, Q11 p. 51, Q13 p. 36, Q14 p. 7, Q16 p. 52 present verbatim on the cited pages).

- **WRONG — Q7.** The card said "SURVIVES verbatim, p. 29". It does not: the Dec-2025 print reads
  "…causes a shift from direct takeovers **towards** takeover activism" (printed p. 29) against the
  2024 card's "toward". Zero exact matches. **Fixed in §8b, and the score line corrected from
  "8 survive / 5 in the IA / 11 broken" to "7 survive / 4 in the IA / 12 broken".** Substance
  unaffected — the sentence is still there, on the page the card names.

#### §2, §3, §4, §5, §6 anchors — all OK.

- **Page-map table.** "Main Proofs" heading on printed p. 41; Internet Appendix heading on printed
  p. 50; §5 "Disciplinary Ownership Changes: Empirical Patterns" on printed p. 29; last printed folio
  66. Layout as the card states.
- **§3 re-anchor table — every row confirmed.** Lemma 1 p. 11 (proof p. 41) · Prop 1 p. 13 (proof
  pp. 41–44, i.e. from "Proof of Proposition 1" on p. 41 to "Proof of Proposition 2" on p. 44) ·
  Corollary 1 p. 15 · Prop 2 p. 19 (proof pp. 44–45) · Prop 3 p. 21 (proof pp. 45–46) · Prop 4 p. 26
  (proof p. 46) · Prop 5 p. 26 (proof pp. 46–47) · Prop 6 p. 28 (proof pp. 47–49) · Prop 7 p. 28
  (proof p. 49) · Lemma 2 p. 66 · Fig. 4 example p. 14 (0.67, 0.6, 0.86, α = 25% all on that page) ·
  eqs. (7)–(8) p. 24. **Enumeration confirmed: 7 propositions + 2 lemmas + 1 corollary**, and
  **12 distinct figure numbers** (Figs. 1–12), with the three data figures captioned on pp. 31–33.
- **§2 delta table.** "Discussion of Assumptions. Internet Appendix A.1 discusses…" p. 16; the IA A.3
  pointer p. 25; IA A.3's own heading "Discussion of Market Modeling Assumptions" p. 54; `0.958851`
  p. 19; IMAA named on p. 31 and World Bank on p. 32 (Figs. 10–11 sources); Renneboog cited pp. 32–33.
- **§4 new institutional facts.** Sharara & Hoke-Witherspoon p. 30 · "reform of shareholder
  communication laws in 1992" p. 63 · "106 block trades" and "5 percent" p. 29 · Fos 39% p. 33 and 29%
  p. 34 · Greenwood–Schor 18.11% p. 35 · "about 35.5% and 18.5%" p. 33 (order swapped, as the card
  says) · 175 funds p. 34 · "Not all of this growth maps directly…" p. 30.
- **§5.** "Market Growth without Frictions" heading p. 60 · "a formal analysis of this is not feasible
  in the market model" p. 21 · "cumbersome" p. 56.
- **§6.** "The control allocation in Proposition 1 is efficient" p. 15 · "The equilibrium features a
  simple cut-off structure" p. 3 · "this shift is usually attributed to the proliferation of takeover
  defenses" p. 5 · "each consecutive block trade further truncates" p. 61 · the reworded "The fact that
  L abstained…" sentence on printed **p. 27** (found; the card's exact-substring test would fail only
  because the extractor floats the superscript ∗ — see MISCITED 3).

#### MISCITED (3, all fixed above, none affecting substance)

1. **§0 Test 1, `psi` row.** The literal string returns **2** hits, not 0-with-one-Lipsius: "Lipsius"
   (p. 38) and "upside" (p. 52). `ψ` as a symbol is genuinely 0, so the D7 conclusion is untouched.
2. **§6 term table, `toehold` pages.** Count 10 is right; the pages are 21 (×2), 25, 53, **56**,
   61 (×2), **65** (×3) — the card listed "21, 25, 53, 61, 64", missing p. 56 and mis-numbering 65.
3. **Two small placement/transcription slips, noted not fixed.** (i) §6 calls both boilerplate `disclos`
   hits "front matter"; one of them is on the paper's own printed p. 1. (ii) The §6 rendering of the
   p. 27 sentence prints the truncation set as "[0, V̄_1]" where the source carries an asterisk
   (V̄₁\*, floated onto the previous line by the extractor). Re-quote from the PDF, not from the card,
   if that sentence goes into draft_v3.

#### UNCHECKED (named, not decision-critical)

- **"ECGI's working-paper page gives 'last revised 29 December 2025'."** External to the PDF; not
  verifiable from any file on disk. Everything internal to the document — title page "November 22,
  2025", ECGI cover "December 2025", PDF creation 30 Dec 2025, SSRN id 4709037, WP N° 956/2024 — is
  confirmed. The card's own open flag already says nothing depends on it.

**Overall verdict: the card SURVIVES, and its two decision-critical calls are both correct.** D7 is
safe on a re-run of every term test, and the deletion of the 2024 card's headline whitespace quote is
confirmed to the point where even a three-word fragment of it is absent. One WRONG (§8b Q7, with the
score line corrected), three MISCITED, one external UNCHECKED. The positioning advice in §7 — swap Q1
for Q5/Q6, position the wedge against footnote 11, pair Q4 with Q5/Q6 — is supported by the source as
written.
