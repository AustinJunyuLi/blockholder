# Brief for Austin — draft_v3 team review, 2026-08-30

**Verdict: yes, move on to the empirics — the theory lane owes the empirics lane nothing and
the written spec is executable today. But draft_v3 is not showable to anyone until Appendix B
is re-transcribed: it prints the pre-repair P1 proof.** Two separate gates; do not blur them.
Executing the spec is gated only by empirics-lane engineering. Showing the PDF is gated by the
draft fix below.

Your ordered review ran at your ten-agent cap: six fresh Opus readers over disjoint slices vs
the frozen record, four adversarial Opus verifiers on blocking findings (finder never verified
its own), the orchestrator verifying the rest directly. Twelve blocking findings, all confirmed
(one with a nuance, noted below). Full record:
`quality_reports/reports/2026-08-30_draft_v3_team_review_findings.md`.

## Proved / holding

- The frozen record is untouched. No reviewer found a theorem-level defect anywhere. The
  Proposition 1 **statement** in §4 is clean — all thirteen hypotheses, the bracket clause,
  the A8 addendum, the applicability remark stated once with every number right.
- §3 model, §5 statements, Appendices A and C, Table 1, and the three numerical remarks are
  faithful: every checked number reproduces its card/HANDOFF source. §6's design tracks SPEC.md
  paragraph for paragraph; Table 2's statistics reproduce exactly from `fact1_summary.csv`.
- Mechanical gates green: compile 0 errors / 0 undefined / 81pp; all 124 refs resolve; 0 curly
  quotes; 0 AI-tell vocabulary; em-dash policy holds; only the sanctioned §6.3 placeholder.

## At risk — the one systemic defect

**Appendix B transcribes the pre-freeze P1 proof.** It is a near-verbatim copy of
`sections_v3/proofs_existence.tex`, whose content was synced from P1_proof.md only through
ticket 35 while its header carries the 65b8db3 stamp — the R36–R56 wording batch, the R40-A
substance batch, and the gate repair round never reached it, and the draft writer trusted the
stamp. Ten confirmed blocking passages, including: a wrong printed equation (eq:P1-BF returns
the stake at the crossing date, contradicting its own definition thirteen lines up); Step 13
printing the corner reading the record ruled "false as a representation claim"; Step 15
asserting the continuity the record de-asserts and the card measures to fail; the superseded
transversality condition; the pre-R38/R39/R43/R44 belief and price-convergence passages.
Nuance on Step 18: the Kakutani withdrawal IS printed — the stale sketch before it still
asserts the withdrawn reasoning, so the passage contradicts itself. Damage is confined to
Appendix B (verified: the late batch was P1-only; zero dated markers in L3/L4/T1/C1 proofs).

**Two more confirmed blockers, both small:** (1) Table 2's caption calls its 188 observations
"the 188 whose trigger date parses" — recomputed from the raw CSV, 198 parse (0.68×150=102,
0.64×150=96); the 98/90 follow an unreported 0–60bd screen in `facts.py`, which SPEC §2.3 says
must be reported as a count. A referee catches this in one multiplication, on the paper's only
executed table. (2) The H=12 column is presented as confirming attenuation with no mention its
C_T travels the chord route — the exact caveat HANDOFF §8.3 addresses to the empirics lane.

Plus ~46 minors/notes (abstract's C1 apposition reads as region evidence; "three legs" vs
§6.2's five; figure titles contradicting captions; card section IDs leaking into nine
environment titles; Φ/ϱ symbol collisions; power numbers quoted on their post-re-parse basis
without saying so; "only if and only if" in the conclusion). All fixable with the December
write-up.

## Needs me

1. **Authorize the fix round.** draft_v3's one-review-one-fix budget was spent at `991a7ec`;
   this was your ordered second review, so the fix needs your explicit go. Recommended scope:
   re-transcribe Appendix B **directly from `research/model_v4/proofs/P1_proof.md` at 65b8db3,
   not from the mirror**; fix the Table 2 caption (198 → screen reported as a count → 188);
   add the one-sentence H=12 chord-route provenance; take the minors in the same pass.
2. **Rule on `sections_v3/proofs_existence.tex`.** Its header advertises the freeze stamp over
   ticket-35-era content; the next writer who trusts it repeats this failure. Re-sync it or
   stamp it stale — your call under the freeze.
3. **A/B/C headline** — does not block execution; every candidate leg is independently
   runnable and the choice only decides what fills §6.3. Note SPEC §3/§8.6 already designates
   the timing split (A) as the headline, so B or C is a permissible but loggable departure.
4. **Empirics-lane gates** (there, not here): the re-fetch/re-parse (SPEC §13 item 2, the only
   package-wide BLOCKING item; all four quoted MDEs are on the post-re-parse projection);
   CIK→CUSIP rebuild (gates the DiD); BID12 coder (§11 row 22, "the long pole", 1–3 weeks).
   Operational risk: `empirics/data/` symlinks the unbacked 1.2GB CRSP snapshot. Lane-sync
   fact: SPEC §0.1/§13 still record HANDOFF_sign.md as absent; the sign has landed, so the
   spec's three directional placeholders are fillable. ω_a remains absent and non-gating.
5. Q6–Q13 remain open from the 2026-08-29 handoff; nothing here re-litigates them.

---

## Amendment, 2026-08-30 (fix round landed)

The authorized fix round is complete. All twelve blocking findings are cured at source, and all
76 minor/note findings are dispositioned in
`quality_reports/session_logs/2026-08-30_draft_v3_minor_ledger.md` (57 FIXED-ALREADY, 11
FIXED-NOW, 8 DEFERRED-with-reason). Final gates: four-pass build, 0 errors, 0 undefined, 86
pages; duplicate-label / unresolved-ref / citation-key / quote-dash / workflow-register scans
all clean; Table 2 arithmetic reconciles (0.68 × 150 = 102, 0.64 × 150 = 96); the diff is
intended-only.

**Landed.** Appendix B re-transcribed directly from `research/model_v4/proofs/P1_proof.md` at
65b8db3 (B1–B10, including the scoped Step 18 and the filing-date-indexed eq:P1-BF); the D1
display in Appendix A repaired to the same filing-date-indexed form; Table 2's caption now
reports the full attrition (300 sampled, 198 parsed, 10 screened by the 0–60 business-day band
reported as a count, 188 retained) per SPEC §2.3 (B12); the H=12 chord-route caveat is in
rem:T1record and the Table 1 caption, calling the column directional corroboration, not a
second independent magnitude (B11). The same pass removed the remaining repository
workflow/register wording, applied the notation map (ρ_ch(τ), 𝔯_ℐ, δ_ϑ, Ψ; Φ reserved for the
normal c.d.f.; no ϱ remains), repaired the A5 counterexample sentence, synchronized the three
open questions across §5.5 and the conclusion with ω_a carried separately as an open,
non-load-bearing input, named the MDE basis at the two remaining sites, rewrote the Figure 1
caption to identify curves by style and marker with the crossing stated, fixed the O-1 prose
(k₁, k₀ at baseline; only k_D moves), and corrected the CCKV and Trivedi bib entries.

**Decisions that remain yours.**
1. **Stale mirror handling.** `sections_v3/proofs_existence.tex` still advertises the freeze
   stamp over ticket-35-era content — the defect that fed B1–B10. Re-sync it or stamp it stale;
   the fix round left it untouched per the freeze.
2. **The frozen D1 erratum.** The superseded crossing-date display also survives in the frozen
   mirrors (`sections_v3/proofs_existence.tex` line 112, `sections_v3/proofs_core_lemmas.tex`
   line 129). The draft carries the repaired form; the mirrors are read-only under the freeze,
   so the erratum stands until you rule.
3. **Headline choice.** Still pending and still non-blocking; the draft records the timing
   split as the specification's default headline with final selection pending.
4. **Empirical gates.** Unchanged from the list above: re-fetch/re-parse, CIK→CUSIP rebuild,
   BID12 coder — all empirics-lane.
5. **Deferred figure internals.** The two embedded figure PDFs keep their baked-in titles,
   axis labels and legend placement (minor findings 43, 46, 60, 71); the captions now describe
   the curves correctly, but the PDFs themselves need a `pyfig` regeneration pass that this
   round was scoped not to run. Worth doing before anyone outside the project sees the PDF.

## Amendment, 2026-08-30 (second entry: proof split, unslop pass, deliverable folder)

**Landed.** The three proof appendices moved verbatim (mechanically verified) out of
`draft_v3.tex` into a new standalone `draft_v3_onlineappendix.tex` at the repo root, which
cross-references the main text through `xr-hyper` (build main first). The main text keeps every
statement, status line, hypothesis tag and proof sketch; the ten appendix cross-reference sites
are now the prose pointer "the online appendix". The same pass carried the unslop/econ-register
edit you ordered: two register words ("features", "the fact that"), the §4 opener now leads
with what the section is for instead of the proposition-versus-theorem taxonomy, and one
abstract sentence split. The pass found the prose otherwise already clean — no AI-vocabulary
hits, no prose em dashes; the 35 that remain sit inside formal statement bodies and are
frozen-record transcription, so they stay. Deliverables now live in `deliverable/`:
`draft_v3.pdf` (36 pp) and `draft_v3_onlineappendix.pdf` (51 pp); sources stay at the root;
gitignored intermediates deleted. Gates: both documents build clean (0 errors, 0 undefined;
zero `??` in the appendix text); Unicode scan clean; diff is intended-only (20 added lines,
each enumerated in the trace amendment).

**Not done, by design.** No placeholder for the future empirical appendix exists in the online
appendix; it gets added when the empirics land. The pre-existing uncommitted deletions under
`deliverables/` (the v2-era folder) are yours; this pass preserved and did not commit them.

## Amendment, 2026-08-30 (third entry: Gorbenko-style restructure, reviewed and fixed)

**What you ordered.** The draft read like a math paper; the reference style was Gorbenko's
"Auctions with Endogenous Initiation": abstract under 150 words, results in plain prose, no
status-line/record machinery in the reader's path.

**Landed.** Sixteen one-clause assumptions are now six displayed assumptions (clause content
verbatim, original labels retained on clauses, so every reference reprints as e.g.
Assumption 4(a) with no \ref edits). The four assumption essays and six numerical-record
remarks moved to the online appendix, which now runs A. Discussion of assumptions, B. Numerical
records, C--E. Proofs (proof sections untouched). All nine status lines are deleted; their
content lives in the statements' hypothesis lists, the new §5.6 ("The model at the implemented
calibration", which also keeps Table 1 in the main text), and appendix Section B. Result titles
no longer carry the D1/L1--L4/T1/P1/C1 codenames (the codenames survive in the appendix proof
titles and the trace). §5.5 "What is not claimed" is folded into the conclusion as one
paragraph; the three open questions live only in the conclusion. The abstract is 149 words;
the intro states the three results in plain English with every number and every conditionality
intact. Main text: 32 pages, 0 errors, 0 undefined. Appendix: 56 pages, 0 errors, every
cross-reference into the main text resolves. `deliverable/` ships both current PDFs.

**The review you required.** One fresh Opus agent (none of the restructure its own) checked
fidelity against the pre-restructure commit: all sixteen clauses, six remarks, four essays and
Table 1 verbatim; seven of eight statements byte-identical; every number in the new prose
matched to the record; no dangling references; frozen record untouched. It returned 4 blocking
+ 11 minor findings, all fixed once: the abstract had dropped "at fixed policies" from the
threshold-margin result (restored) and the seeded-sample qualifier (restored within the word
cap); the intro had dropped the H=12 chord-route qualifier (restored); `deliverable/` still
shipped the pre-restructure PDFs (refreshed); one "two parts" sentence miscounted the regrouped
timing assumption (fixed). Minors included two orphaned deictics in the moved essays, an
unglossed A(br) symbol that Lemma 5's frozen body prints (the clause title now carries the
symbol), a semicolon capital, two imprecise lines in §5.6 (the 0.16 jump at the second node;
H=10 now named before 4^{H+1}), the dead \resultstatus macro, and two wrong lines in my own
trace amendment (the grouping description and an example label). The trace amendment records
every pointer repair inside statement bodies.

**Judgment calls you may want to revisit.**
1. Assumption 1 gathers four clauses under "Timing and the legal clock", including interior
   crossing (0 < Ω < 1), which is a regularity condition rather than timing — grouped there
   because it is small and filing-related. Moving it now would renumber the assumptions.
2. The main text no longer prints the codenames D1/L1--L4/T1/P1/C1 anywhere; readers of the
   frozen record map through the trace file or the appendix proof titles.
3. The conclusion now carries both the non-claims paragraph and the open questions; §5 reads
   results-then-calibration with no "not claimed" section.

**Nothing theorem-level surfaced.** No new decisions are required of you beyond the three
judgment calls above; the standing list (stale mirrors, frozen D1 erratum, headline choice,
empirical gates, figure regeneration) is unchanged.
