# LABEL LEDGER — v4 two-round blockholder disclosure model

The log of label moves required by `MODEL_CARD.md` §7. One line per move, in the format

`ID | old→new | evidence paths (proof; audit; re-derivation; fix/recheck if any) | who | date | commit`

**Rules this file obeys** (§7 of the card). Only an executed check or an independent re-derivation
moves a label — never prose. A move needs **both** passes: an adversarial proof-read PASS *and* an
independent statements-only re-derivation PASS, written by different agents, the re-deriver working
from the card statement alone with `proofs/` and `threads/` unopened. Labels are never weakened by
editing. ~~Region-certified is not a label: it is PROVED with the region named in the hypothesis.~~
**Amended 2026-08-23 (post-review):** a **dominance-and-contraction node** is not a fifth label;
it records the pointwise inequalities $L_{\mathcal R}<1$ and $\eta_r>0$ with supporting
diagnostics, not verification of the full C1 antecedent. Region-level certification remains unclaimed.

**Two standing notes.**

* ~~**C1 is pending.** It has no proof on file and no pass of either kind; ticket 29 is in flight. It
  stays CONJECTURE and does not appear below.~~ **Superseded 2026-08-23 (post-review):** C1 moved
  to PROVED on 2026-08-22 (commit `403ac8e`) and appears below; P1 was demoted to CONJECTURE on
  2026-08-23 (commit `43a45f8`) and remains recorded in the move section.
  **Superseded 2026-08-25:** restored to PROVED, see the ticket-35 move below.
* **GPT Pro's end review may demote, never promote.** A finding from that review can send any row
  below back to CONJECTURE. It cannot move anything *to* PROVED — that needs the two passes, run
  inside this lane, on file.

---

## Moves — ticket 27, theory-lane batch, 2026-08-21

D1 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §A (PASS as PROVED-WITH-CHANGES, 2026-08-21; its two added hypotheses are now card clauses — §4.2 Borel rider, §4.3 $\mathcal I_H$ fill) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L1 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §B (PASS as PROVED-AS-STATED, 2026-08-21) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L2 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §C (PASS as PROVED-WITH-CHANGES, 2026-08-21 — hypothesis set re-enumerated, A7′ consumed a.s. on the flagged set); satisfiability of A7 closed by `proofs/A7_construction.md` + `proofs/A7_attack_verdict.md` (ticket 24) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L3 | CONJECTURE→PROVED under A($\tau$) | proof `proofs/L3_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §2 (PASS, 0 FAIL, L3-R1…R5 applied 2026-08-21); re-derivation `rederive/L3_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; CH1–CH7 folded into card §4.4 and A($\tau$)) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

L4 | CONJECTURE→PROVED (legs 1–2 outright; leg 3 under A(br)) | proof `proofs/L4_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §3 (PASS, 0 FAIL, L4-R1…R5 applied 2026-08-21); re-derivation `rederive/L4_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; (br-v) added, (br-iv) sharpened) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

P1 | CONJECTURE→PROVED | proof `proofs/P1_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §4 (PASS, 0 FAIL, P1-R1…R8 applied 2026-08-21); re-derivation `rederive/P1_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; changes C1–C8 — A2→A2′, A5 derived from $m_0\ge0$, objective row added) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

T1 | CONJECTURE→PROVED at fixed policies | proof `proofs/T1_proof.md`; audit `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15, non-propagating); fix/recheck `threads/2026-08-21_T1_fix_recheck.md` (T1-F1 discharged by H18; N1–N4 applied; fix round CLOSED → proof-read PASS-equivalent); re-derivation `rederive/T1_rederivation.md` (PASS, 2026-08-21; PROVED-AS-STATED except the "equivalently" quantifier, now written as *on average along the tightening path*) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: 627642c

---

## Not moved

C1 | CONJECTURE (unchanged as of 2026-08-21) | no proof on file; ticket 29 in flight | — | 2026-08-21 | — **(superseded by the 2026-08-22 move below)**

## Move — ticket 29 close-out, 2026-08-22

C1 | CONJECTURE→PROVED (certificate implication, region-as-hypothesis; 18 certified nodes NUMERICAL evidence; region-level certification NOT claimed) | proof `proofs/C1_proof.md` (repairs 13/13); audit `threads/2026-08-21_C1_proofread_audit.md` (PASS, 0 FAIL); re-derivation `rederive/C1_rederivation.md` (PASS as PROVED-WITH-CHANGES: N1 norm convention, N2 two-sided openness; H8 unused); executed check `quality_reports/fixes/t2_c1_region_check.py/.json`, independently re-run 2026-08-22 ALL REPRODUCE (`quality_reports/fixes/t2_rerun_verify_note.md`) | theory-lane batch (Fable orchestrating) | 2026-08-22 | commit: 403ac8e

[**Amended 2026-08-23 (post-review), naming only** — per the GPT end-review audit finding 6
(`threads/2026-08-23_gpt_end_review_audit.md`): "certificate implication" → **"dominance-and-contraction
implication"**; "18 certified nodes" → **"18 pointwise dominance-and-contraction nodes"**; "region-level
certification NOT claimed" → **"a named-region promotion is not claimed"**. The executed check tests
pointwise $L_{\mathcal R}<1$ and $\eta_r>0$ with supporting diagnostics, not the full C1 antecedent
(C² smoothness, relative openness, interior single branch, non-vanishing $\mathcal S^{GE}$). The
original words of the move line above stand unaltered; the move itself, its evidence paths, its date
and commit, and the **PROVED** label are untouched.]

## Move — GPT end review + audit, 2026-08-23

P1 | PROVED→CONJECTURE | GPT Pro end review `threads/2026-08-22_gpt_end_review.md` finding 1, upheld by `threads/2026-08-23_gpt_end_review_audit.md`: the proof's h.7 consumes the joint injective form of A7 while the card row and the re-derivation carry the on-path form — the two-pass gate never covered a single statement; independently, Step 12 lacks a continuation-cost clause (sunk-cost gap, live for multi-Voice menus) and Step 9's positivity claim fails at κ=1 under card §4.1's noise law. The pinned single-Voice menu instance is untouched by all three gaps. Demotion per standing note 2 (the review may demote, never promote); approved by Austin 2026-08-23. Repair: ticket 35. | theory lane (Fable orchestrating) | 2026-08-23 | commit: 43a45f8

## Move — ticket 35 close-out (P1 repair, route A), 2026-08-25

P1 | CONJECTURE→PROVED | proof `proofs/P1_proof.md` (statement amended to the hypotheses the proof consumes — A7-J for A7′, continuation-cost clause h.16, $\kappa$ boundary by extension, §4.1–§4.3 table restrictions enumerated as h.17, h.5 struck; repairs P1-R9…R35); proof-read **PASS** `threads/2026-08-25_P1_proofread_retry.md` (0 FAIL; 3 REPAIRs + 4 OBSERVATIONs applied; round-1 FAIL and the single sanctioned repair round at `threads/2026-08-25_P1_proofread_round1.md`, where the reader's own finding-1 witness is recorded as refuted on the merits); re-derivation **PASS-WITH-CHANGES** `rederive/P1_rederivation_2026-08-25.md` (fresh agent, card row alone; changes 1–5 folded into the row, change 6 withheld for Austin); numerical status carried separately and UNCHECKED — the four κ-extreme nodes remain STILL UNRESOLVED after 30 seeds (`quality_reports/fixes/t2_p1_fournode_recheck.json`, ticket 34), which is neither existence evidence nor its absence. Both passes are fresh and neither agent wrote the proof; the 2026-08-21 chain is retained in the card row and did **not** satisfy the gate. | theory lane (Fable orchestrating) | 2026-08-25 | commit: 0cbdb37

## Move — F5 route ruled R40-A, batched gate over the amended proof, theory-record freeze, 2026-08-30

P1 | PROVED→PROVED (statement amended in place — no label move) | Austin ruled F5 = **P1-R40-A** (2026-08-29); the substance batch (R40-A items A1–A3, P1-R43, P1-R44, P1-R45) was applied to `proofs/P1_proof.md` 2026-08-29, followed by a five-item gate repair round 2026-08-30. The batched two-pass gate over the amended proof: adversarial proof-read **PASS** (PASS-WITH-REPAIRS → one sanctioned repair round → **RETRY PASS**; the single WRONG — Step 15's candidate-condition passage asserting $\mathcal T_i=c_i$ without argument, refuted by a card-legal skipped-plan witness — was non-load-bearing, the theorem running on h.6's continuity assumed outright, and was closed under a weak-ordering clause with an argued counting-map identification) and statements-only re-derivation **PASS-WITH-CHANGES** (fresh agent, card row alone, `proofs/`+`threads/`+`rederive/` unopened; changes 1–2 — the bracket defined in the row's A6-as-read clause and the domain narrowing recorded — folded into the row at this stamp). Both verdicts filed verbatim at `rederive/P1_gate_2026-08-30.md`; both agents fresh, neither wrote the proof. **P1 remains PROVED on the amended statement**; what remains open is antecedent-satisfiability at the implemented calibration (§5's A6 and A3 evidence notes — the A($\tau$) pattern), with any consequence Austin's. This entry **freezes the theory record**: the R-number sequence is closed, `threads/` is archive, and from the freeze the only artifacts under review in this repo are draft_v3 and code. | orchestrator (ZCode session) | 2026-08-30 | commit: 65b8db3

## Evidence note — independent re-run of every check script, 2026-08-22

All eight `t2_*` scripts (D1, L1, L2, L3, L4, T1, P1, C1-region) were re-run in full by a fresh
agent that wrote none of them: **ALL REPRODUCE** — every fresh JSON bit-identical to its committed
twin except wall-clock timing fields; zero numeric differences at any magnitude. One MISCITED
gloss corrected (the P1 failing-node description; the numbers were never wrong). Verdict:
`quality_reports/fixes/t2_rerun_verify_note.md`. The three substantive FAILs (L2's A(τ)-orientation
placebo, T1's chord-magnitude bridge, P1's four κ-extreme nodes) reproduce exactly and stand as
findings, not as errors.
