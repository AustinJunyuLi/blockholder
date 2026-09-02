# Checkpoint 2 (2026-09-02, after batch 2)

Batch 2 returned PASS on every step (`runs/batch-2/result.txt`). Grok ran step 0, the figures
and the paper draft, then stopped before any gate; a Sol worker audited step 0 and the figures
and a second Sol worker finished the paper, so the batch result carries `approach.status =
"changed"`. The checker failed once on one phrase in a proof remark and passed on the
re-verification. The referee returned ten blocking and ten minor items. This note carries the
verdicts, the labels every result holds now, the commits, the decisions batch 3 needs, and the
feedback on approach.

## Verdicts

| Record | Question | Verdict | Outcome |
|---|---|---|---|
| `runs/batch-2/audit-step0-figures.md` | are the step-0 edits wording only; do the figures regenerate byte-stably and show only recorded cases | PASS with fixes | two ungrammatical clauses repaired in the proofs; figures made byte-stable, record checks added, the degenerate T = 10 cell marked |
| `runs/11/result.txt` | the paper to the batch-2 Done list plus seven model-statement constraints | PASS | 19-page paper, 24-page appendix, 39 cited entries, number guard green |
| `runs/11-check/result.txt` | labels, absences, compile, number guard (Opus, independent) | FAIL | one phrase: the Condition D grid remark in `proofs/02_garbling.tex` called the stake distribution an equilibrium object |
| `runs/11-check-2/result.txt` | the same after the fix | PASS | two lines differ in total; every label equal to checkpoint 1; every grid number traced to its record |
| `runs/12-referee/result.txt`, `referee_report.md` | referee at journal standard (Sol) | FAIL | 10 blocking, 10 minor; no number mismatch, no compile defect |

The who-gets-caught rerun on the step-0 script finished ALL PASS in 927 s at hash
`fbacc963f39422c3` with the same C_T values as before; the record now carries
`degenerate_T10`, `degenerate_T5`, `corner_T10_equals_H`, `t1_comparison` and `B_reading`.

## Labels at this moment

Unchanged from checkpoint 1. PROVED: partition and factorisation, the flagged cell's
κ-invariance, the garbling lemma, the threshold weight leg and the closed form of S_P, the clock
dial, the who-gets-caught identity and characterisation. NUMERICAL: the threshold composition
leg on the grid κ in [0.15, 0.85], mark 2, H 10, T 5, four adjacent pairs; directional
who-gets-caught sentences off the five-node record, naming the degenerate T = 10 cell.
ESTIMATED: E1. ABSENT: existence, E2.

The referee argues one label (blocking item 9): E1's ESTIMATED label covers objects with no
standard error, while `CLAUDE.md` requires one. The registered design (`empirics/spec.md`)
reports a bootstrap interval on the two post-minus-pre differences only. That is a decision for
the author, recorded below; no label moves in this note.

## External input

GPT 5.6 Sol Pro's answer on existence is at `.scratch/v5-paper/external/gpt-sol-existence.md`
(commit `5fb598b`). Its Theorem 1 proves existence under a commitment notion (the blockholder
binds to a cutoff rule before the signal); the proof is correct and the notion changes the game,
so it does not enter the paper. Its review found four ambiguities in the model statement, all
verified against the code and all now constraints on the paper (signal truncation, mark versus
order size, Exit's sale leaves no mark, filing-date timing), plus the rule that the calibration's
policy is the benchmark policy and never an equilibrium. A theory-upgrade hunt runs in a separate
thread under `.scratch/v5-paper/hunt/`; nothing from it enters before its own attack gate.

## Commits

`6ef6514` step-0 wording in the proofs; `2696e26` the who-gets-caught record with its new
fields; `75e43a7` the test-suite guard; `eb4a03b` the figures and their script; `48a0086` the
remark fix; `ad0f1e1` the paper; `5fb598b` the external consultation. Tree clean apart from the
hunt directory and the old untracked `numerical_v4/checks/t2_l3_check.json`.

## Referee items, triaged for batch 3

Blocking, fixable in batch 3 without a new result: 1 (13D trigger is "more than 5 percent", and
13G eligibility), 2 (state that T is in trading rounds and that the (10, 5) pair is a model
comparison, not the reform; no recalibration), 3 (the outcome is the engagement-related
component of the premium, said so everywhere), 5 (the iid and type-independence clauses enter
the garbling appendix's hypotheses), 6 (Ω < 1 enters the pooled-block hypotheses; the paper's
"null rather than empty" becomes "null, possibly empty"), 7 (the stale source comment in
`proofs/03_caught.tex` goes; the appendix prints the label of each statement), 8 (the closing
informal sentence of the corollary's proof states the attenuation criterion exactly: s_B between
0 and (2/φ) s_A), 10 (Figure 1 uses finite-difference notation, or plots the recorded point
derivatives).

Blocking, needs a small new result: 4. Three unlabelled analytic sentences. The pricing root's
uniqueness and continuity (a short lemma; proof and Opus attack in batch 3, or the sentence goes),
the fixed-policy timing claim that a shorter clock weakly lowers the stake at filing (a two-line
lemma from the monotone paths; same gate), and the calibration sentence that every selected Voice
path finishes building by the filing so that B^F equals the target (a record field or the
sentence goes).

Blocking, a decision: 9, the ESTIMATED scope.

Minor: all ten are wording, presentation, or production fixes except 1 (the policy is imposed;
answered by the fixed-policy framing and, if the hunt delivers it, a maximal-regret record) and
5 (the empirics measure filing stakes and delays, not market inference; the paper says so and
claims no more).

## Decisions batch 3 needs

1. ESTIMATED scope. Recommended: the label covers the two post-minus-pre differences, which
   carry the registered bootstrap interval; the by-year and by-period table is presented as the
   registered descriptive statistics it is, without the label. Alternative: a post-hoc bootstrap
   standard error for every displayed object from `empirics/output/e1_campaigns.csv`, recorded in
   a new file and stated as unregistered.
2. Framing. The referee reads the title and opening as a rule-design result and recommends a
   narrower information-accounting framing centred on the garbling lemma. The external review
   recommends "disclosure regulation changes what the market learns from silence". Recommended:
   keep the title, open with the silence framing, and state the fixed-policy scope and the
   narrow threshold grid in the first page, not after the two-dial language.
3. The flagged tuple makes Q^F public. Recommended: keep the assumption and state its
   institutional reading (the filing's Item 4 plans and the stated target) in the model section.
4. The three analytic sentences of blocking item 4: lemmas with an Opus attack, or deletion.
   Recommended: lemmas.
5. Builder. Recommended: a Sol worker at xhigh writes the fixes and the two lemmas; Opus attacks
   the lemmas and runs the final CHECK; the orchestrator renders every page at checkpoint 3.

## Feedback on the approach

Grok's `runs/batch-2/plan.md` was sound: step 0 before the paper, figures before the paper, each
step closed by its own gate, one advisory reviewer after drafting. It executed the first two
steps and drafted the third, then stopped before running any gate, so the number guard, the
compile and the label audit were first run by the finishing worker. Two observations. The draft's
label discipline held: the one defect the checker found was in a proof remark written in batch 1,
not in the draft. The one thing a plan cannot cover is a stop mid-step; the batch shape now has
`approach` so a finisher can say so, and this batch is the first to use it.
