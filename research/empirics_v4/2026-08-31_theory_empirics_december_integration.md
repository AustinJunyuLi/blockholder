# How the theory and evidence can become one December paper

Research note, 31 August 2026. I treat the frozen theory record at `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4` as fixed. This note does not change a registered empirical object, a result label, or a theory artifact.

## Recommendation

My recommendation is blunt. Write a theory paper with one empirical fact. Do not present it as a causal empirical paper whose main estimate is still missing.

The paper asks a clean economic question. When a blockholder must disclose sooner, how does that change when the market learns about the blockholder's intentions? The model explains how learning can occur before the filing and when the filing arrives. The empirical section can show whether Schedule 13D filers shortened the time between crossing 5 percent and filing after the SEC changed the deadline from ten calendar days to five business days. [SEC final rule](https://www.sec.gov/files/rules/final/2023/33-11253.pdf)

Everything that does not answer that question belongs in the appendix or in later work.

| Place in the paper | Material |
|---|---|
| Main text | The model, the legal change, and a corrected trigger-to-filing delay result |
| Appendix | H1 and H2, with estimates, intervals, minimum detectable effects, or MDEs, and a clear warning that their return windows do not recover the model's objects |
| Outside the December argument | A causal BID12 DiD. It did not clear the balance or pre-trend checks, so there is no causal estimate to report |

This leaves a claim that is modest but coherent. The theory explains the timing of disclosure. The data show whether filing timing changed after compliance began. The paper does not claim that the rule caused a change in takeover activity or confirmed the model's return prediction.

## 1. The economic logic in plain English

Start with the sequence of events:

`quiet accumulation -> 5 percent crossing at TD -> filing interval -> public filing at FD* -> later control outcome`

Between the trigger date, TD, and the filing date, FD*, the market does not yet have the Schedule 13D. It can still learn from order flow. When the filing arrives, the market sees the disclosed stake and the activist's stated purpose. The model sorts histories at the later control decision. A history is pooled if disclosure has not arrived by then and flagged if it has. These are information states at one decision date, not two sections of an event-study window.

D1 is the bookkeeping result. Within a flagged history, it separates price movement before filing from the response when the flag arrives. Both movements belong to the same flagged price path. D1 does not call the run-up the pooled cell and the filing response the flagged cell. It also does not prove that the empirical variables called `RUNUP` and `JUMP` recover its two terms. [Frozen definition: `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:122-149`]

L2 is subtler. At fixed cutoff and trading policies, the flagged posterior, flagged price, bidder-entry probability, and flagged premium do not vary with model liquidity. The result does not come from the filing alone. Under L2's identification assumptions, the disclosed stake, flagged-round order, and engagement indicator form a tuple that identifies the relevant information. Earlier order-flow noise then stops changing those flagged objects. [Theory card: `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:655-656`]

That is a statement about the value after disclosure. It is not a statement about the filing-date return. A return compares the after-disclosure price with the price just before disclosure. Imagine that the flagged price is 110 in both a low-liquidity and a high-liquidity case. If the pre-filing prices are 100 and 107, the filing responses are 10 and 3. The flagged price is unchanged, exactly as L2 says, while the filing response changes. This is why a liquidity slope on the filing CAR cannot prove or refute L2. The frozen theory says so directly. It does not claim that its filing response, J, is liquidity-invariant. [`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/model_v4.md:146-149`, `:698`]

T1 keeps two legal changes separate. Changing the ownership threshold changes who must disclose. Changing the filing window changes whether disclosure has arrived by the control decision. At fixed policies, the theory signs the threshold margin. It does not give the window margin an unconditional sign. A shorter window puts less weight on histories that remain pooled, but the histories left in that group are selected differently. Their liquidity sensitivity may rise or fall. Total sensitivity falls only when the lower weight dominates that composition change. [`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:664`]

"At fixed policies" matters. The result holds the blockholder's plan and cutoff choices constant while the legal rule moves. It is not a general-equilibrium claim about how every investor changes strategy after a reform. The ten-to-five-day exercise finds attenuation at the checked nodes for one fixed-policy calibration. It is a numerical illustration, not validation of the chord mechanism. A support condition needed by that mechanism fails in this calibration, and the horizon-12 composition term uses the same chord route rather than an independent calculation. The result is not a theorem about the 2024 rule and does not predict an empirical coefficient's size. [`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/HANDOFF_sign.md:8-25`, `:390-560`]

P1 and C1 do important theory work, but they do not supply extra December estimands. P1 establishes equilibrium existence under its stated conditions. C1 gives conditions under which the threshold sign survives equilibrium feedback, with numerical evidence at individual nodes rather than a verified region. Keep their qualifications in the theory appendix. Do not turn them into new empirical predictions. [`/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/MODEL_CARD.md:659-671`]

The proof record no longer needs repair. Appendix B was re-transcribed from the frozen P1 proof, the horizon-12 caveat was restored, and both manuscript builds passed. The live draft still needs an empirical rewrite. It speaks as if the estimates have not been seen and treats a zero filing-return slope as L2, which the frozen record rejects. [`/Users/austinli/Projects/blockholder_v4_theory/draft_v3_trace.md:254-305`; `/Users/austinli/Projects/blockholder_v4_theory/draft_v3.tex:1017-1027`, `:1115-1130`, `:1229-1265`]

## 2. From model objects to observed measures

The model and the data do not line up one-for-one. The table shows the closest available measure and where the link breaks.

| Model idea | Available measure | What the measure can answer | Where the link breaks |
|---|---|---|---|
| D1 sorts histories by whether disclosure has arrived at the control decision | TD, FD*, and abnormal returns | When observed price movement occurs around the filing process | The registered `RUNUP` and `JUMP` both include FD* minus one, so they are not a clean partition. Event-time returns also do not reveal the model's control-date information cells. [Definitions: `research/empirics_v4/SPEC.md:328-362`; code: `empirics/estimate_h1.py:596-604`] |
| L2 fixes flagged objects across liquidity at fixed policies | No direct measure in the current data | H1 describes how filing-window returns vary with liquidity | A return is a change between prices. L2 concerns the flagged price, posterior, entry probability, and premium. H1 does not observe those objects directly. |
| T1 gives a conditional sign for a shorter window | `LIQ x Post` in H2 | Whether a liquidity-return association differs after compliance began | The theorem's sign is conditional and fixed-policy. `RUNUP5` may include the filing itself when firms file early, so the outcome mixes pre-filing learning with disclosure. [Code: `empirics/estimate_h1.py:607-615`] |
| The legal clock became shorter | Business days from TD to filing | Whether filers actually shortened their delays | A before-after comparison describes timing. Without an untreated group, it does not isolate the rule's causal effect. |
| The model contains bidder entry and a takeover premium | A bid within 365 days of TD | Whether later bid incidence changed in the matched sample | The model does not sign an aggregate bid hazard, and the registered DiD did not clear its design checks. |

There is another gap beneath every liquidity regression. The model's liquidity parameter is noise-trading intensity. Empirical `LIQ` is the negative of log Amihud illiquidity after standardizing that log measure within calendar quarter. Amihud is a proxy for the trading environment, not a direct observation of the model parameter. Even with clean return windows, the regression would test a proxy relationship rather than a literal model parameter. [`research/empirics_v4/SPEC.md:364-376`]

Two measurement problems deserve emphasis.

First, H1 labels its windows `RUNUP` and `JUMP`, but the names promise more than the code delivers. `RUNUP` ends at FD* minus one. `JUMP` starts on that same trading day. One day's return appears in both. Even if the model-to-data translation were otherwise exact, these windows would not divide price movement into two disjoint pieces.

Second, H2 fixes the outcome at TD through TD plus four. Many firms file before that window ends. For those observations, `RUNUP5` includes the public filing response. The amount of filing information inside the fixed window therefore differs across observations and can differ across regimes. The mixture can change even if the underlying price-learning process does not. A new, non-overlapping outcome could address this in future work, but estimates have already been seen. It cannot be substituted quietly into the December analysis.

## 3. What the evidence currently says

The data answer three different questions. They should not be compressed into one verdict on the model.

Did filing delays shorten? The audit says yes, but the publishable result does not exist yet. The old table says the median fell from 7 to 5 business days and the share filed within five days rose from 35.7 to 75.6 percent. That table uses an older parser and contains 300 rows but only 282 unique accessions. It cannot be quoted as the corrected result. [Old outputs: `empirics/output/fact1_filings.csv`, `empirics/output/fact1_summary.csv`]

A read-only check using the repaired parser finds the same broad pattern. In the deduplicated original draw, 98 pre observations and 97 post observations survive the existing screen. The median moves from 7 to 5 days, and the within-five-day share moves from 38.8 to 78.4 percent. The all-filing version gives 399 pre and 365 post observations, with a median shift from 7 to 4 days and shares of 37.6 and 78.6 percent. These are audit figures, not paper results. The appendix records the exact command and hashes. The project still needs to preserve the corrected outputs and reproduce them independently.

This timing fact matters because it checks whether the real-world disclosure clock moved in the direction the paper studies. It does not explain why delays changed. It also does not show that more filings had arrived by a particular control decision or that returns and bids changed because of the rule.

Did returns move as the numerical example suggests? The current data cannot tell us. H1 uses 979 filings and 1,958 stacked rows. Its contrast is 0.58 percentage points, with a two-way standard error of 1.56 points, a conservative p-value of 0.741, and an MDE of 4.38 points. Both component slopes are imprecise. The estimate also has the level-versus-change problem and the overlapping day described above. [Artifact: `empirics/output/h1_estimate.json`]

H2 is no more informative. Its `RUNUP5` interaction is 0.0175 percentage points, with a standard error of 4.42 points, a p-value of 0.997, and an MDE of 12.39 points. The three-day filing-window interaction is 0.54 points, with a standard error of 4.15 points, a p-value of 0.928, and an MDE of 11.62 points. These intervals are too wide to distinguish economically different signs, and the outcome does not cleanly isolate pre-filing learning. [Artifact: `empirics/output/h2_estimate.json`]

Did the rule change takeover activity? The registered DiD cannot answer that question. The blind BID12 audit found no disagreements in 30 readings, so the registered hand-audit gate passed. That small audit does not establish complete outcome coverage, and the separate outcome base-rate gate does not clear. The post-match balance gate also did not clear. The pre-trend result independently blocks causal language. The correct label is `NOT ESTIMATED`, not "null effect." [Audit: `research/empirics_v4/bid12_audit_result_2026-08-30.md:266-276`; artifacts: `empirics/output/did_estimate.json`, `empirics/output/did_diagnostics.json`, `empirics/output/bid12_gates.json`]

The re-parse reduced 4,639 unique initial filings to 3,710 with a parsed trigger date, 3,356 in the allowed date band, 1,465 CRSP matches, and 1,112 observations in the final estimation sample. The counts show where filings leave the sample at each step. They do not make the matched comparison causal. [`empirics/output/reparse_counts.json`; `research/empirics_v4/SPEC.md:150-197`]

## 4. What the paper may claim

If the corrected delay result reproduces, write that observed filing delays shortened after compliance began. Do not say the rule caused the change. The comparison has no untreated group.

For H1 and H2, report the estimates, intervals, and MDEs. Call them inconclusive. Do not call them evidence of no effect, attenuation, model confirmation, or a passed partition test.

For BID12, say that the DiD was not estimated because the post-match balance gate did not clear. The pre-trend result independently blocks causal language. Do not report a coefficient, a sign, or a causal null.

This wording matters because four statements that sound similar have different meanings:

| Statement | Meaning |
|---|---|
| The legal deadline changed | A fact about the rule |
| Filing delays shortened after compliance | A descriptive fact about observed filings |
| The rule caused filing delays to shorten | A causal claim that the current comparison cannot establish |
| The model's return prediction was confirmed | A model test that H1 and H2 do not provide |

## 5. What must stay fixed

The estimates have been seen, so the current specification is part of the research record. Changing windows, samples, controls, or liquidity measures now would make the design respond to its results.

1. Preserve `SPEC.md`, the current result JSONs, and their hashes. If a correction changes a reported value, retain the old value and record the change. [Lock rule: `research/empirics_v4/SPEC.md:55-73`]
2. Make one transparent correction to Fact 1. Keep the old 300-row file. Produce a deduplicated correction on the original draw, then the already planned all-filing extension using the same quarters and the same 0-to-60-business-day screen. Reconcile every denominator and exclusion. [`research/empirics_v4/data_inventory.md:131-140`]
3. Do not invent a new H1 or H2 after seeing the current estimates. Report the overlap and the mismatch with the model. A clean test belongs in a new specification after December.
4. Leave the frozen theory and repaired proof appendix alone. Edit only the live draft's empirical discussion. Remove the L2-to-JUMP equivalence and replace prospective language with the actual result status.
5. Preserve the `NOT ESTIMATED` DiD record. Do not search for another match specification before December and call the surviving version the original design.

## 6. The December paper

The introduction should ask where market learning occurs when an activist accumulates before disclosure. It should say at once that the model gives a conditional window result and that the empirical return tests are imprecise.

The institutional section should explain the 5 percent trigger, the old ten-calendar-day deadline, and the new five-business-day deadline. Its main figure should show the corrected delay distribution, with sample counts and exclusions visible.

The model section should move in the order a reader needs. D1 defines the pooled and flagged timing. L2 explains what disclosure reveals. T1 shows why shortening the window need not have one unconditional effect. P1 and C1 can remain in the appendix with their full conditions.

The empirical section should be short. Put the corrected delay result first. Put H1 and H2 in one appendix table with estimates, confidence intervals, MDEs, and the measurement warning. State that the DiD did not clear its registered checks. The SEC accumulation arithmetic can remain as a limit on plausible effects through the accumulation channel, not as a substitute causal estimate.

The conclusion should separate what the paper learns about implementation from what it does not learn about returns or takeovers.

This is a smaller paper than planned. I think it is better. If the department counts a corrected timing estimate as the empirical result, the package can meet the December goal. If it requires a causal estimate, the project is one result short. H1 cannot fill the gap because its outcome does not match the theorem. The DiD cannot fill it because it did not clear balance or pre-trend. Calling either one a positive result would make the paper less credible, not more complete. [`/Users/austinli/Projects/blockholder_v4_theory/CONTEXT.md:26-33`]

## 7. The decision

| Requirement | Current status | What remains |
|---|---|---|
| Theory statements and appendix match the frozen record | Passed | Preserve them |
| Corrected delay table is a saved, reproducible result | Open | Create the correction and planned extension, then reproduce both |
| Draft describes L2, H1, and H2 accurately | Open | Remove the JUMP equivalence and state the window overlap |
| Every table agrees with its source artifact and the manuscript builds | Open | Run one full numerical and document check |
| BID12 supports a causal policy estimate | `NOT ESTIMATED` | Keep it outside causal claims |

**Go in December as a focused theory paper if the corrected delay table reproduces, the draft states the limits of H1 and H2, and the integrated manuscript builds. No-go as a causal empirical paper. Nothing in the current results clears that bar.**

## 8. Work backward from December

| Date | Output |
|---|---|
| 1 to 7 September | Save hashes for the observed results. Build and independently reproduce the corrected Fact 1 outputs. Reconcile every count and caption. |
| 8 to 21 September | Rewrite the empirical discussion in the live draft. Remove the L2 and JUMP error. Add the model-to-measure table. |
| 22 September to 12 October | Assemble the paper. Put the corrected delay figure in the main text and H1 and H2 in one appendix table. Remove the DiD from main-text claims. |
| 13 October to 2 November | Fix the final claim after the delay result clears reproduction. Finish the source notes and data appendix. |
| 3 to 23 November | Reproduce every stated empirical command. Rebuild the paper and appendix. Check the proof transcription and every reported number. |
| 24 November to 10 December | Circulate the complete seminar draft and run the referee checklist. |
| 11 to 18 December | Freeze the PDF, code commit, hashes, limitations note, and specification for any later control-outcome study. |

## 9. What to do next

1. Record the hashes and labels of `h1_estimate.json`, `h2_estimate.json`, `did_estimate.json`, `did_diagnostics.json`, `bid12_gates.json`, and the re-parse counts before running anything new.
2. Rebuild Fact 1 as two preserved outputs. The first corrects the original accession draw. The second uses every unique filing in the same fixed quarter windows. Keep the existing calendar and 0-to-60-business-day screen, and record all exclusions.
3. Rewrite only the live draft's theory-to-data discussion. Explain the level-versus-change distinction, the overlapping H1 windows, and the filing contamination in H2.
4. Move H1 and H2 to supporting evidence. Move the `NOT ESTIMATED` DiD out of the main argument. Do not change their estimands to improve the result.
5. Reproduce every number, build both PDFs, and compare each table and caption with its saved source before circulation.

## Appendix: read-only Fact 1 feasibility audit

This audit supports planning only. It did not overwrite an output, change a registered label, or create an adopted result artifact. The command below was rerun on 31 August 2026 from `/Users/austinli/Projects/blockholder_v4` with Python 3.12.13, NumPy 2.5.2, and pandas 3.0.5.

Input hashes:

- `empirics/data/fact2_parsed.jsonl`: `cc0e3f9d4c264ca4a4d87b93db058f4c601253a622035815a26d6a31e3cf748f`
- `empirics/output/fact1_filings.csv`: `7f79cf6d6eda52ed1c9548cd0fc51b8f803e24f392424af915ca5ce3dd932d6d`
- `empirics/facts.py`: `6e755eb08a40727de60a689bae954eab23368838de315dc44ed17e93099545b9`

```sh
.venv/bin/python - <<'PY'
import pandas as pd
from empirics.facts import business_delay

df = pd.read_json(
    "empirics/data/fact2_parsed.jsonl",
    lines=True,
    dtype={"accession": str},
)
windows = {
    "pre (2023Q2-Q3)": {"2023Q2", "2023Q3"},
    "post (2024Q3-Q4)": {"2024Q3", "2024Q4"},
}
rows = []
for label, quarters in windows.items():
    sample = df[df["quarter"].isin(quarters)].drop_duplicates("accession").copy()
    sample["event"] = pd.to_datetime(sample["event"], errors="coerce")
    sample["filed"] = pd.to_datetime(sample["filed"], errors="coerce")
    sample["delay"] = [
        business_delay(event, filed)
        for event, filed in zip(sample["event"], sample["filed"])
    ]
    kept = sample[sample["delay"].between(0, 60, inclusive="both")]
    rows.append({
        "window": label,
        "enumerated_unique": len(sample),
        "parsed_event": int(sample["event"].notna().sum()),
        "retained_0_60": len(kept),
        "median": float(kept["delay"].median()),
        "share_le5": float((kept["delay"] <= 5).mean()),
    })
print(pd.DataFrame(rows).to_string(index=False))

old = pd.read_csv(
    "empirics/output/fact1_filings.csv",
    dtype={"accession": str},
)[["accession", "window"]].drop_duplicates("accession")
merged = old.merge(df[["accession", "event", "filed"]], on="accession", how="left")
merged["event"] = pd.to_datetime(merged["event"], errors="coerce")
merged["filed"] = pd.to_datetime(merged["filed"], errors="coerce")
merged["delay"] = [
    business_delay(event, filed)
    for event, filed in zip(merged["event"], merged["filed"])
]
for label, sample in merged.groupby("window"):
    kept = sample[sample["delay"].between(0, 60, inclusive="both")]
    print(label, {
        "draw_unique": len(sample),
        "retained": len(kept),
        "median": float(kept["delay"].median()),
        "share_le5": float((kept["delay"] <= 5).mean()),
    })
PY
```

Exact output:

```text
          window  enumerated_unique  parsed_event  retained_0_60  median  share_le5
 pre (2023Q2-Q3)                616           427            399     7.0   0.375940
post (2024Q3-Q4)                521           395            365     4.0   0.786301
post (2024Q3-Q4, 5-business-day rule) {'draw_unique': 141, 'retained': 97, 'median': 5.0, 'share_le5': 0.7835051546391752}
pre (2023Q2-Q3, 10-calendar-day rule) {'draw_unique': 141, 'retained': 98, 'median': 7.0, 'share_le5': 0.3877551020408163}
```

These values are evidence that the correction is worth formalising, not permission to quote them in the manuscript. The corrected-delay requirement remains open until the calculation is saved as a result artifact and independently reproduced.

## Sources and provenance

Primary institutional source: SEC Release No. 33-11253, *Modernization of Beneficial Ownership Reporting* (final rule and compliance information), [SEC final rule](https://www.sec.gov/files/rules/final/2023/33-11253.pdf) and [SEC rule page](https://www.sec.gov/rules-regulations/2023/10/33-11180).

Primary project sources: the frozen theory model/card/proofs under `/Users/austinli/Projects/blockholder_v4_theory/research/model_v4/`; registered empirical design at `research/empirics_v4/SPEC.md`; committed empirical artifacts under `empirics/output/`; and the dated audit records cited inline. The sources cited here are local project records or the rulemaker's original materials; no secondary treatment of the legal change is used for a material claim.
