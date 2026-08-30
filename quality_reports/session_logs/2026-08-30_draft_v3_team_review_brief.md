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
