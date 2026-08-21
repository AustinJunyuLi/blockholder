# LABEL LEDGER — v4 two-round blockholder disclosure model

The log of label moves required by `MODEL_CARD.md` §7. One line per move, in the format

`ID | old→new | evidence paths (proof; audit; re-derivation; fix/recheck if any) | who | date | commit`

**Rules this file obeys** (§7 of the card). Only an executed check or an independent re-derivation
moves a label — never prose. A move needs **both** passes: an adversarial proof-read PASS *and* an
independent statements-only re-derivation PASS, written by different agents, the re-deriver working
from the card statement alone with `proofs/` and `threads/` unopened. Labels are never weakened by
editing. Region-certified is not a label: it is PROVED with the region named in the hypothesis.

**Two standing notes.**

* **C1 is pending.** It has no proof on file and no pass of either kind; ticket 29 is in flight. It
  stays CONJECTURE and does not appear below.
* **GPT Pro's end review may demote, never promote.** A finding from that review can send any row
  below back to CONJECTURE. It cannot move anything *to* PROVED — that needs the two passes, run
  inside this lane, on file.

---

## Moves — ticket 27, theory-lane batch, 2026-08-21

D1 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §A (PASS as PROVED-WITH-CHANGES, 2026-08-21; its two added hypotheses are now card clauses — §4.2 Borel rider, §4.3 $\mathcal I_H$ fill) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

L1 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §B (PASS as PROVED-AS-STATED, 2026-08-21) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

L2 | CONJECTURE→PROVED | proof `threads/thread1_turn2_answer.md`; audit `threads/thread1_turn2_audit.md` (proof-read PASS 2026-08-20); re-derivation `rederive/core_D1_L1_L2_rederivation.md` §C (PASS as PROVED-WITH-CHANGES, 2026-08-21 — hypothesis set re-enumerated, A7′ consumed a.s. on the flagged set); satisfiability of A7 closed by `proofs/A7_construction.md` + `proofs/A7_attack_verdict.md` (ticket 24) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

L3 | CONJECTURE→PROVED under A($\tau$) | proof `proofs/L3_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §2 (PASS, 0 FAIL, L3-R1…R5 applied 2026-08-21); re-derivation `rederive/L3_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; CH1–CH7 folded into card §4.4 and A($\tau$)) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

L4 | CONJECTURE→PROVED (legs 1–2 outright; leg 3 under A(br)) | proof `proofs/L4_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §3 (PASS, 0 FAIL, L4-R1…R5 applied 2026-08-21); re-derivation `rederive/L4_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; (br-v) added, (br-iv) sharpened) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

P1 | CONJECTURE→PROVED | proof `proofs/P1_proof.md`; audit `threads/2026-08-21_batch1_proofread_audit.md` §4 (PASS, 0 FAIL, P1-R1…R8 applied 2026-08-21); re-derivation `rederive/P1_rederivation.md` (PASS as PROVED-WITH-CHANGES, 2026-08-21; changes C1–C8 — A2→A2′, A5 derived from $m_0\ge0$, objective row added) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

T1 | CONJECTURE→PROVED at fixed policies | proof `proofs/T1_proof.md`; audit `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15, non-propagating); fix/recheck `threads/2026-08-21_T1_fix_recheck.md` (T1-F1 discharged by H18; N1–N4 applied; fix round CLOSED → proof-read PASS-equivalent); re-derivation `rederive/T1_rederivation.md` (PASS, 2026-08-21; PROVED-AS-STATED except the "equivalently" quantifier, now written as *on average along the tightening path*) | theory-lane batch (Fable orchestrating) | 2026-08-21 | commit: recorded at commit time

---

## Not moved

C1 | CONJECTURE (unchanged) | no proof on file; ticket 29 in flight | — | 2026-08-21 | —
