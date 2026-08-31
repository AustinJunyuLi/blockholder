# Three decisions for Austin, empirical lane (2026-08-31)

Dated note under §0 rule 1. **No SPEC object changes and none is proposed
here.** Each item below would change a registered rule, which is a
post-registration call and therefore yours. Nothing has been adopted. This is
filed the way the Datavault rulebook observation and the balance-gate
observation are filed: with the numbers attached, not acted on.

Where the leg stands, in three lines. The BID12 outcome coder is audited on
both sides and passes, 0 disagreements of 30. The §8 coefficient is
`NOT ESTIMATED` on two independent registered grounds, the §8.2 balance gate
and the §8.8 pre-trend joint F of 3.249 at p = 0.0214. §9 is `ESTIMATED` and
uninformative, which is what §9 registered as expected. `quote_as_result` is
false and stays false while either bar is live.

---

## Decision 1. What "any standardised difference" covers in §8.2

**The registered text.** §8.2, after the matching table: *"Any standardised
difference above 0.10 after matching is reported and the match is re-run with a
tighter caliper."* The sentence follows a list of seven reported quantities,
four matched dimensions plus three book-to-market substitutes, of which five
are continuous and carry a standardised difference. §8.9 turns a difference a
tighter caliper does not fix into a design failure.

**What the numbers say.** Both attempts, from `did_match_meta.json`:

| covariate | matched dimension | 0.25 | 0.20 |
|---|---|---|---|
| logcap | yes | -0.078 | -0.067 |
| logilliq | yes | 0.060 | 0.055 |
| turnover | no | 0.074 | 0.065 |
| ret12m | no | -0.119 | **-0.131** |
| idiovol | no | 0.157 | **0.122** |

The registered remedy is a caliper on log size and log illiquidity. Neither of
the two failing covariates is a caliper dimension, so tightening reaches them
only through incidental correlation. It shows: between the two attempts
`idiovol` improved and `ret12m` got worse.

**Option A, stand pat.** Cost: nothing to run. §8 stays `NOT ESTIMATED`, the §6
bounded null carries the leg alone, and the December sentence is the bounded
null quoted against the design arithmetic, 15.32 pp clustered against a 3 pp
headline rung.

**Option B, narrow the gate to the two matched dimensions.** This is not only a
relabel, and the fork inside it needs your ruling too. Under a narrowed gate
the 0.25 attempt passes on first look at -0.078 and 0.060, so the predeclared
0.20 rerun would never have fired. That leaves two candidate draws: 0.25 with
932 pairs, which is not on disk, or the 0.20 draw that is, at 839 pairs. Say
which one carries the estimate. Either way §9 re-runs: `bidder_entry_estimate.json`
records `did_match_pairs.csv` among its inputs by hash, and `tau` currently
carries the 0.20 draw's `failed_balance` status in its own record. Cost is
local compute, minutes, no SEC fetch. §8.8 still blocks causal language, so
what comes out is reported as a descriptive difference and the word "effect" is
not used.

**Option C, add past return and idiosyncratic volatility as matching
dimensions.** This changes §8.2's design table. The power note has to be
written first, against a pool that is already short: 839 of 1,395 requested
pairs, 181 of 221 SIC-2 x quarter cells below 3:1, 129 treated rows with no
match at all. Two more dimensions make that worse before it gets better. No SEC
fetch, but the note plus the re-run is a session's work.

---

## Decision 2. Two §5.1 pattern gaps in the BID12 rulebook

**The registered text.** Rulebook §5.1 items 1 and 4.

**What the numbers say.** The control-half auditor derived both gaps from the
rulebook text alone, and the coder had independently landed on the same two
filings from the other side of the blind. Item 4's added patterns leave the gap
operator as an ellipsis where the §5 patterns write `[^.]{0,80}`, so a
permissive reading matches target-side boilerplate ("each option to purchase
shares granted under the Company's equity incentive plans") and flips a §5 row
1 confirmation to a row 5 ambiguous. The coder's `confirm_detail` on G1's
2024-08-07 8-K reads `target:1;acquirer:1`, which is that false fire. Item 1's
bare acquirer form cannot see the sentence subject, so it fires on "Parent, as
the parent of Purchaser, acquired control of the company".

Neither changes a verdict in the audit. G1's BID12 = 1 rests on form-list
tender events decided by §2 and §4 without touching §5. The exposure is a
treated-side case resting on an 8-K alone. The audit puts that population at
768 of 1,323 treated ambiguous 8-Ks on §5 row 6. Counted today off the
committed ambiguous files, 550 treated ambiguous 8-Ks and 69 control ones
record both directions firing, which is the population an item-4 tightening
would re-read.

**The cost, and it is the large one.** `rules_sha256` hashes the whole rulebook
file. I verified it: `shasum -a 256 research/empirics_v4/bid12_coding_rules.md`
returns `e95c4f9f87d4224597f91b659251fd3b7f8d81ca748843ef7cc4a2c9255de0c6`,
the hash in `bid12_run_meta.json`. So any edit to that file, however small,
re-stamps it, and a re-stamp forces:

- a re-derive of every event cache, treated 2,735, control 3,991, recovered
  419, since the caches carry verdicts derived under the old rule;
- a control-side and treated-side re-lookup, then the 14 gates again;
- **a fresh 30-pair blind audit.** The 0-of-30 result is against hash
  `e95c4f9f`, verified against `bid12_audit_manifest.json` by both halves. It
  does not survive the re-stamp, and the leg's audit bar is unmet until a new
  audit with fresh agents passes.

The treated pass alone is hours of SEC-fetch lane, under a host lock that
allows two lanes.

**Direction, stated as an expectation and not as a computed number.**
Tightening item 4 should move some row 5 ambiguous back to row 1
confirmations, raising the treated BID12 rate. Gate 4 is a recorded fail low,
12.61% on the universe denominator against the 18.1% Greenwood-Schor anchor,
with the H1/S1 comparison at 18.66% quoted beside it.

**Options.** Adopt and pay the re-derive. Defer, and state both gaps as a
limitation in the paper against the audit that passed under the frozen rule.
Reject.

---

## Decision 3. Two minor text gaps, which do not cost the same

They are separate rulings because they live in different files.

**3a. Rulebook §3 has no intra-day tie-break.** When a form-list event and a
confirming 8-K share a filing date, the ordering is undetermined. Only the
`first_event_form` label turns on it, never a verdict. But §3 is in the same
file as §5.1, so a tie-break carries **all of decision 2's cost**: re-stamp,
full re-derive, fresh audit, for a label. If you adopt both 2 and 3a, adopt
them as one edit and pay that cost once.

**3b. SPEC §8.7 fixes the pre/post length ratio but not the window-selection
rule around a pseudo-date.** This is SPEC text, not the rulebook. No hash
moves and nothing re-derives. It also does not unblock the placebo on its own:
of the four recorded blockers, `did_not_estimated` and `rematch_inputs_missing`
both survive it, and `pseudo_date_support` (106 of 568 dates lack treated
observations on one side) is a property of the sample, not of the text.

---

## Landed today, needing no ruling

The §8.1 and §8.6 supersession notes, under the 2026-08-30 corrigendum pattern:
§8.1 records the realised §8 treated matched sample, 465 split 325 pre / 140
post, beside the printed 569 / 543, which is one funnel stage above it and is
not struck; §8.6 records the same section's arithmetic on 325 / 140, SE 4.17
pp, MDE 11.70 pp, 15.32 pp clustered, labelled design arithmetic rather than a
realised MDE. No test, rule or prediction moved.

Sources for everything above: `research/empirics_v4/did_matching_2026-08-31.md`,
`research/empirics_v4/bid12_audit_result_2026-08-30.md`,
`empirics/output/did_estimate.json`, `did_match_meta.json`,
`bidder_entry_estimate.json`, `bid12_run_meta.json`, `bid12_gates.json`.
