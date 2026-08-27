# Session log — 2026-08-27 — ticket 08 (T4): draft_v3 theory sections

**Invocation.** Austin, in-session: implement the next ticket with Opus doing the writing and the
orchestrator doing the review. Ticket 08 (`.scratch/v4-reposition/issues/08-t4-model-section-tex.md`,
canonical copy on `v4` identical) was next on the record
(memory: R-series run closed 2026-08-27, "ticket 08 next; its first leg regenerates the mirrors").
Routing per the ticket header and ADR-0005: Opus writers, Sonnet plumbing, a separate Opus checker;
the orchestrator ran git, adjudications, and the final read. Card stamp throughout: 2026-08-27, A6
panel resolution, `ae9caea`.

**Leg 1 — mirrors regenerated: DONE, commit `58a5d11` (pushed).** One Opus agent brought
`model_v4.md`/`.tex` from card stamp 2026-08-23 to 2026-08-27 by content anchor, from the extracted
card delta (`d2ccf62..HEAD`): stamps and provenance, §5 A3/A6/A(τ) evidence notes, ledger preamble +
the P1 row (PROVED, amended statement; rendered as a five-row `longtable` split in tex), open-items
item 4. Same agent then repaired three note-original glosses its own sweep surfaced (a
"P1 is CONJECTURE" inventory row; two "A(τ) remains OPEN / until ticket 33 lands" passages —
ticket 33 landed and answered FAILS) and three wrong facts cross-references in tex (now
`\ref{sec:facts}`; md was correct as its own §6). Gate: xelatex ×2 exit 0; zero
undefined/Reference/Missing-character/Overfull/`^!`; PDF 23 pp. Mechanical fidelity sweeps
(numeric-token and 8-gram) ran clean; one vocabulary collision flagged, not fixed (the card's
$\mathcal S(k)$ selection set vs the note's §1 reservation of bare $\mathcal S$ for sensitivity).

**Leg 2 — `sections_v3/` written: DONE.** Sonnet scaffold first (driver `standalone_v3.tex`
compiled from the repo root; draft_v2's preamble family: authoryear biblatex with natbib commands,
the globally numbered theorem set, no cleveref; `v3_macros.tex` with the model_v4 macro block and
`\resultstatus{}`; aux lands at the repo root). Then one Opus section writer
(`model_section.tex` 652 lines; `theorem_section.tex` 466 lines) and three parallel Opus proof
writers on disjoint files (`proofs_core_lemmas.tex` 1108 lines after the repair round;
`proofs_existence.tex` 1025; `proofs_theorem_ge.tex` 747), each compiling against an isolated
test driver so gates could not race. Statements transcribe the card rows clause-complete (a ~150-row
crosswalk in the ticket-08 scratchpad maps every clause; the P1 row landed as 13 enumerated
hypotheses + 5 conclusion clauses + the three trailing readings). All eight honesty labels are
verbatim from the ledger with conditionality attached; the §5 evidence notes sit at the assumption
sites (`rem:A3record`, `rem:A6record`, `rem:AtauRecord`) and are re-consumed at the result sites
(`rem:P1record`, `rem:T1record`, `rem:C1record`). P1 is stated as a Proposition (one-theorem frame;
reasoned in the crosswalk and visible in the text). Proofs are full-content transcriptions of the
repaired sources — no pre-trimming (trimming is ticket 18's job), 1:1 step architecture for P1 so
audit citations resolve, hypothesis-consumption registers in the writer reports, honest negatives
kept in-proof ((T-15) consumed nowhere; H8 and AGE's sign-constancy both unused and kept apart;
uniqueness never claimed; the κ=1 positivity claim not proved, per its withdrawal). New bib
entries: none — four citations, all existing keys (Kyle1985, GlostenMilgrom1985, GrossmanHart1980,
EdmansGoldsteinJiang2015).

**Leg 3 — independent check: LAND, then a repair round, then LAND again.** A fresh Opus checker
(wrote nothing) read all six files end to end against the card and the regenerated note:
**0 WRONG · 13 MISCITED · 1 UNCHECKED · 14 OK-RESTRUCTURED · 2 flags**
(`research/model_v4/threads/2026-08-27_t4_sections_check.md`, 1526 lines with the delta section).
One sanctioned repair round fixed everything worth fixing: **M-4a** (the one real loss — L3's
Part IV was missing, so (S1)/(S2), the weakest sufficient conditions, appeared nowhere while two
sentences claimed them; +159 lines restore Steps 16–18 with source-aligned numbering, so the card's
"L3 Step 18's (S1) and (S2)" pointer resolves in-paper, and the openness sentence's attribution was
redirected to the proof), **T-10** (prop:C1's "sign-coherence" re-attributed from AGE to H8 by
content, matching `C1_proof.md:141/147`), **F-2** (the single overfull box — the C1 proof's long
amsthm run-in; all eight proof run-ins are now ID-only), **M-10** + **F-1 hardening**
(`v3_macros.tex` provenance corrected; `\Tmap` changed from `\providecommand` to `\newcommand` so a
draft_v3 carrying draft_v2's `\providecommand{\Tmap}{T}` fails loudly at `\input` time instead of
silently rendering the outer map as the filing window across 107 uses — ticket 18 must resolve the
name consciously, in either assembly order). The checker's delta pass re-verified every repair at
full grain (Part IV arithmetic re-done independently) and re-ran the compile from a clean state:
**LAND**, no WRONG before or after. The remaining MISCITEDs are deliberate paper-form pointer
thinnings (process anchors like audit step numbers and check-block names), all catalogued in the
report with the card retaining every anchor.

**Final gate (orchestrator).** From the repo root: xelatex → biber → xelatex → xelatex, exit 0;
`grep -in undefined standalone_v3.log` empty; 0 `^!`, 0 Overfull, 0 multiply-defined; **61 pages**.
`numerical_v4` untouched, so the smoke run was not in this ticket's gate set.

**Orchestrator adjudications.**
1. *Ω\* 0.29 vs 0.343 (the checker's one UNCHECKED, card-side).* Resolved for the sections:
   `HANDOFF_sign.md` §3 records that "≈0.29" was a grid-point rounding and the bisection-located
   boundary is **Ω\* = 0.343** — "anything that quotes ≈0.29 should quote 0.343". `rem:T1record`
   quotes 0.343. The card's §4.4 cell mentioning "the ≈0.29 cut" is a historical identification of
   draft_v2-era numbers, not a competing boundary; no card write was made (quiet window respected).
2. *L4 leg 2 "gap" → "difference between the two shares".* The glossary's _Avoid_ on "gap" targets
   positioning prose, not arithmetic; the substitution is harmless and stands (checker:
   OK-RESTRUCTURED, no substance change).
3. *Proof run-ins ID-only.* Adopted file-wide for the box-overflow reason; full titles stay on the
   statements one `\ref` away.

**Interface for ticket 18 (C2), stated for the convergence owner.** draft_v3 pulls the theory lane
in as `\input{sections_v3/model_section.tex}`, `\input{sections_v3/theorem_section.tex}`,
`\input{sections_v3/proofs_section.tex}` (which provides `\section{Proofs}\label{sec:proofs}` and
inputs the three proof part-files), after `\input{sections_v3/v3_macros.tex}` in the preamble and
`\addbibresource{sections_v3/sections_v3.bib}` (currently header-only; no new citations were
needed). **Known conscious step at assembly: the `\Tmap` name collision** (draft_v2 line 54 defines
`\Tmap` as upright `T`); `v3_macros.tex` now makes the wrong outcome a hard compile error in the
macros-after ordering and documents the reverse ordering's hazard. All `\input` paths inside
`sections_v3/` files are repo-root-relative, so the standalone driver and draft_v3 resolve
identically; compile from the repo root.

**Follow-ups on file, not started.** GPT re-review bundles with this output — Austin's courier
moment, not built here (not in the ticket's acceptance list). Then C-series (17–20). Standing items
from the R-series run unchanged: curate the decisive A6 probes into t2 checks; gate-check the
continuum-face lemma only if promoted; sweep the ticket-34 candidate account over the other three
nodes. The card-internal $\mathcal S(k)$ vocabulary collision (leg 1) is a candidate wording item
for the next card window.

**Commits this session (v4-theory, all pushed):** `58a5d11` (leg 1 mirrors);
`9a73bb7` (sections_v3 + checker report + this log). Ticket-file update
committed on `v4` separately.
