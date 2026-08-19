# P5—The purpose flag as the market's information set

## 1. Object
Bidder entry (tender offer or merger within 12 months of filing) and the takeover premium
conditional on entry, asked of the *purpose partition*: whether a block's declared purpose is
flagged (13D) or pooled (13G), and how the gap moves with liquidity.

## 2. Margin
The 13D-vs-13G purpose margin, as a **LEVEL**: 13G is available only to a holder without
control purpose (Rule 13d-1(b)/(c); Zeng card Q1, p. 1303). The one **CHANGE** object: the 20%
override—above 20% the 13G route closes regardless of intent (EFZ card, n. 17, p. 14).

## 3. Anchor
The purpose declaration is law, not cheap talk: 13G requires the stake not be held with the
"purpose or effect of changing or influencing control"; a mislabelled 13G risks fraud (NACCO
v. Applica, EFZ card, p. 11). Declared purpose is heterogeneous and measured (36.6%
investment-only / 43.3% communicated / 20.0% explicit activism—Zeng, p. 1315) but nowhere
load-bearing on a control outcome.

## 4. Main result to be proved
*The purpose partition is load-bearing and liquidity-tilted: at fixed economic state (stake,
signal, κ), bidder entry and the expected premium differ across the 13D and 13G flags, and the
gap widens in κ—the pooled 13G state loses information content in κ while the flagged 13D
state is κ-invariant.* Proof route (declared-purpose model on draft_v2's primitives): the flag
D becomes {none, 13G, 13D}, the 13G state pooling passive and activist-in-waiting types;
posteriors and prices are draft_v2's Prop 2 / Prop 3; the bidder enters on (P, D, ξ), D7's λ
making the flagged bloc pivotal; flagged-branch κ-invariance is proved
(`app:proof-disclosed-invariance`), pooled-state variance is closed form (`lem:d1-variance`),
and the cross-partial sign follows. Label: **PROVED** at fixed cutoffs; **NUMERICAL**
(grid-certified D8-style region) for magnitudes. Biggest technical risk: the 13G mixture
breaks monotonicity of the bidder's entry condition in κ off the certified region (D8's
counterexample logic).

## 5. Empirical design
Sample: the EDGAR pipeline extended to SC 13G; all 13D + 13G originals 2022–25 matched to the
on-disk CRSP 2021–25 snapshot. Identification: (a) the 20% eligibility boundary—the purpose
partition flips while the stake barely moves: bunching plus a fuzzy contrast; (b) the
workhorse cross-section: entry ~ purpose flag × lagged Amihud, filer-type FE, size/sector
controls. Control group / bounded null / placebo: 13G filers; EFZ's 0.7% 13G CAR; QII 13Gs.
Confounds: anticipation (Zeng: the run-up begins at the trigger date—our pooled state is
*pooled for the price-setting market*); selection into 13D (the object, not a nuisance);
bunching manipulation below 20%; EDGAR cut-off and T+1 (not operative—no 2024-02-05
contrast). Power: Greenwood–Schor base rates (18.1% vs 7.2%, p. 372), ~2–4k matched events →
MDE ≈ 5 pp on entry; ≤300 hand-collected offer prices → MDE ≈ 8–10 pp on premia. Run by
December: 13G enumeration, outcome matching, leg (b); specced only: premium hand-collection,
leg (a).

## 6. What is new vs the competitor map
Cell **W7** (**NARROW**). The named card: AFS's partition is *the blockholder's declaration of
purpose*; their object is the announcement-return decomposition—no takeover premium, bidder
entry or M&A outcome exists in the paper (card §6). Ours is *the market's information set*
(their card §7 states the distinction verbatim). They concede it—fn. 16, p. 34: the 13G
price "may already incorporate the possibility of subsequent 13D filings". A bias conceded is
not an object modelled: no bidder ever conditions on their partition.

**Payne-Mann contingency (required).** If SSRN 5076900 delivers its abstract—a "Potentially
Activist" middle category from the 13D/13G split reporting M&A activity, executive turnover
and returns—control-outcome measurement keyed to the purpose split is occupied; "first to
key a control outcome to 13D-vs-13G" dies. Surviving: the theory object (a signed liquidity
slope is not a data construction), the liquidity interaction (absent from the abstract), and
the rule-keyed 20% variation. Pivot: the mechanism paper for their fact—replicate it as
validation, then add slope and model. If their PDF adds a liquidity interaction or a
structural purpose-choice model with a control outcome, W7 is CONTESTED; fall back to W6,
purpose margin as the rule.

## 7. Deliverability by December
13G enumeration + parsing: 0.5–1 wk (flag change on the fetcher). Outcome matching (SC TO-T /
DEFM14A / 8-K; audit §2.3): 1–3 wk. Cross-sectional leg: 1 wk. Theory: 2–3 wk (draft_v2
machinery reused). Premium subsample: 1–2 wk, specced. Total ≈ 7–9 wk. Failure modes: 13G
parse yield (only flag, CIK, dates needed); thin 20% bins; M&A volume (widen to 18 months).
Fallback: theory alone; empirics revert to the W6 liquidity-slope design on the in-hand 13D
sample.

## 8. Supervisor continuity
Recognisable: the privately informed blockholder, κ as driver, the flagged/pooled partition
read on the declaration margin, the bidder's entry condition, D7's λ. Dropped: the four-action
menu, the hump R1, the welfare section, the Feb-2024 anchor (ADR-0003).

## 9. Self-assessed weakest point
The declaration-vs-information-set distinction is real but subtle: a referee holding AFS's
fn. 16 can say we relabel their conceded bias as our object; the defence—no bidder or
control outcome ever nears their partition—must be argued, not assumed. Worse, W7 is
provisional: if Payne-Mann et al. occupy it, "first" degrades to "mechanism for someone
else's fact". The workhorse leg is a lagged-liquidity interaction exposed to the
no-instrument critique EFZ concede (fn. 27, p. 1473); the sharp design (20% boundary) is
power-poor.
