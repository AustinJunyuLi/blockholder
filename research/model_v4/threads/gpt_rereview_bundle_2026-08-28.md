# GPT Pro Re-Review Bundle — v4 two-round blockholder disclosure model

**CONTENTS**

| § | What it holds |
|---|---|
| 1 | The ask — the standing rule, the card stamp this bundle is built against, the inlining convention |
| 2 | The delta narrative — seven dated events since your 2026-08-22 review, written from the records in §5–§6 |
| 3 | MODEL CARD, verbatim and complete — the single source of truth |
| 4 | LABEL LEDGER, verbatim and complete — every label move with its evidence |
| 5 | The primary records — the audit of your own review, the P1 proof-read and re-derivation, both A6 panel reports, the ticket-08 checker report |
| 6 | Raw check verdicts — extracts from six executed-check JSONs |
| 7 | The draft_v3 theory sections — results and model sections in full, the eight proofs by opening |
| 8 | What is asked back — the response format |

## 1. THE ASK

Adversarial **re-review** of the v4 two-round blockholder disclosure model, after the repairs your
last review forced and the extensions that followed it.

You last saw this stack on **2026-08-22**. That review was audited inside the lane on 2026-08-23,
and everything after that date is new to you: a demotion, a repair, a restoration through the
two-pass gate, three executed applicability checks against named assumptions, an opposed-brief
panel on one of them, and the first draft_v3 theory sections written off the card. §2 is the
dated account of all of it. Nothing else exists — you see no repository, no source code, no chat
history. Everything you need to render a verdict is in this single paste, in the order it appears
below.

**Build the answer against this stamp.** This bundle is assembled against MODEL CARD version stamp
**2026-08-28 · follow-up curation · commit `926f58c`**, which is the stamp the card carries in §3
below. An answer written against a stale stamp is re-asked, not accepted; if the card text in §3
disagrees with anything in §2, the card wins.

**The standing rule, unchanged.** Your review can **DEMOTE** a label — send a PROVED row back to
CONJECTURE if you find a hole — but it can never **PROMOTE** one by prose; only a written proof
with an adversarial proof-read PASS and an independent statements-only re-derivation PASS, both
run inside the lane by agents who did not write the proof, can raise a label, and an executed,
committed check earns NUMERICAL and nothing more. The honesty labels and their conditionality are
the result: a row claims exactly what its label and its named conditions say, so "PROVED under
A($\tau$)" is a claim about an implication and not about the implemented model, and reading a
conditional as unconditional is itself a finding. **MISCITED** and **UNCHECKED** observations are
welcome and never block — return them in full rather than downgrading a decision-critical claim to
low priority because you could not check it here.

**Three standing pressure points, stated so you can attack rather than rediscover.**

1. **P1 was demoted on your finding and restored on a repair.** The row you sent back to CONJECTURE
   is PROVED again under an *amended* statement (A7-J for A7′, a continuation-cost clause, the
   $\kappa$ boundary by extension). The question for you is whether the amended statement is the
   theorem the model needs, or a statement retreated to what the proof happened to establish.
2. **Two named assumptions now fail at the implemented calibration and no label moved.** A($\tau$)
   fails at 180 of 180 non-degenerate nodes; A6's continuity clause fails at measured, reproduced
   jumps; A3 fails at two loci. Every affected row stays PROVED *as a conditional*. Attack the
   split: is "PROVED as a conditional whose antecedent is measured false at the only calibration we
   implement" honest labelling, or PROVED-adjacent language for something the paper cannot use?
3. **The draft_v3 sections are the first place these labels meet paper prose.** §7 carries the
   statements. Check them against §3's card rows for dropped conditionality — that is the failure
   mode a checker inside the lane is least able to see.

**The card's own rules bind your answer, too.** MODEL CARD §4 (Symbol table) is the only notation
you may use — do not renumber or re-key a symbol, and flag any notation you introduce that is not
already in §4. MODEL CARD §8 (Standing rules) governs how you write: no "clearly", "it follows",
"standard", or "obviously" without showing the step; cite only IDs that already appear in the card.

**Inlining convention.** Every block below sits between a `FILE:` descriptor line, an opening
`===== BEGIN <path> =====` marker and a closing `===== END <path> =====` marker. The descriptor
says which of three things the block is, and the distinction matters when you cite it:

- **`(verbatim, complete)`** — the whole file, byte-for-byte. Ten blocks below are whole files, and
  nothing inside them is this bundle's text.
- **`(excerpt, lines a–b)`** — a contiguous byte-for-byte slice of the file, with the line range in
  the marker. Eight blocks, all in §7.3, which says exactly what was cut and why.
- **`(extract)`** — used only in §6, for the check JSONs, which are far too large to paste. These
  are authored condensations: every `verdict` string and every number is reproduced unaltered,
  elisions inside a quoted string are marked `...`, but the layout is re-keyed for width and any
  bracketed remark is the bundle's, not the JSON's. Treat an extract as a pointer to the committed
  file, not as the file.

---

## 2. WHAT CHANGED SINCE YOUR 2026-08-22 REVIEW

Seven dated events, in order. Each is written from the primary record inlined later in this
bundle, and each names the record so you can go straight to it. Failures below are stated as
failures; where nothing moved, that is said too.

### (a) 2026-08-23 — your end review was audited, finding by finding, before anything moved

The audit is `threads/2026-08-23_gpt_end_review_audit.md`, §5 below. It was written against the
primary record, not against your prose, and it made no edit of its own: the demotion and the
wording batch it queued waited for approval.

**Scorecard: all eight of your findings UPHELD, three of them in narrowed form. None was
rejected.**

*Accepted outright, with consequences.*

- **Finding 1 — P1's recorded theorem is not established by its cited proof. UPHELD on three
  independent grounds.** (i) *The A7 form mismatch.* `proofs/P1_proof.md` h.7 consumes the **joint**
  injective form — $(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ injective on the whole flagged set — and Step 10
  consumes exactly that, while the card row recorded the weaker **on-path** form A7′, as did the
  2026-08-21 re-derivation. The two 2026-08-21 passes therefore covered two different statements,
  so the two-pass gate had never been satisfied for the row as recorded; under the on-path form
  Step 10 fails outright against the 40-collision witness already on file. (ii) *The sunk-cost gap.*
  Step 12 equated "the round-2 order strictly improves the flagged continuation" with "the first
  bracket is strictly larger at $j'$", where that bracket carries $-C_{j'}(s)$ — plan $j'$'s own
  engagement cost — while a round-2 deviator has already sunk $C_j(s)$. The two coincide only if
  $C_{j'}=C_j$ on the deviation set, which no hypothesis supplied. Your 0.01-vs-0.99 example is
  arithmetically correct; the gap is vacuous on single-Voice menus and live on any admissible menu
  with two Voice plans sharing a pooled path, and the row quantified over general finite menus.
  (iii) *The $\kappa=1$ false claim.* Step 9 asserted that every noise mark carries positive
  probability whenever $\kappa>0$; under card §4.1's noise law that is **false at $\kappa=1$**,
  which is in-domain.
  **Consequence: P1 PROVED → CONJECTURE**, approved 2026-08-23, logged in the ledger at
  commit `43a45f8`. No other label moved.
- **Findings 4, 6, 7, 8 — the wording-repair batch (ticket 32), landed 2026-08-25.** Finding 4:
  O-1 is a same-policy information-regime toggle, not a window-margin refutation; every place the
  record labelled its ratios $W_TC_T$ or called the window claim refuted was withdrawn or rewritten
  as analogy, and card §9 item 3 was withdrawn. Finding 6: `t2_c1_region_check`'s `certified` flag
  is two inequalities plus diagnostics, not C1's full antecedent, so "18 certified nodes" was
  renamed to "18 pointwise dominance-and-contraction nodes"; labels unchanged, and the audit
  records that your review endorsed the three-way C1 split itself. Finding 7: two false
  consequences in the card's A7′ gloss were corrected — strictness holds for flag-capable composed
  targets, not for every $b_j^*$, and injectivity forces the *tuple* $(B^F,Q^F)$ continuum-valued,
  not the coordinate $B^F$. Finding 8: the card was a mixed pre-/post-C1 snapshot and was
  regenerated with one consistent C1 status; the ledger's standing note was amended.

*Upheld but narrowed — the narrowing is the finding, and it cost no label.*

- **Finding 2 — L2's placebo. UPHELD; no consequence on L2.** The check demanded
  $\partial_\kappa M_P\le0$ under A($\tau$), but the identity
  $\partial_\kappa M_P=\Delta_m A'_\kappa C_h(\bar\pi)$ carries $A'_\kappa$, which A($\tau$) does
  **not** sign; the card's own witness Example A has $A'_\kappa=-1/4$ and predicts the opposite
  sign. The recorded FAIL was reclassified as a misformulated test and carries no information about
  A($\tau$). L2's own invariance checks are untouched and **L2 stays PROVED**.
- **Finding 3 — T1's chord check. UPHELD as MISCITED; T1 stays PROVED.** `t2_t1_check` hard-coded
  $|A'_\kappa|=0.25$ (Example A's witness value) and imposed level symmetry, neither of which is
  part of A($\tau$); the 0.628 pp residual refutes that witness calibration of the bridge, not
  A($\tau$). Two places in the record that read "A($\tau$) fails … in two independent places" were
  corrected to **OPEN**, and the decisive support-enumeration check was queued — it is (c) below.
- **Finding 5 — P1's four $\kappa$-extreme nodes. UPHELD as UNCHECKED.** The 30-seed budget applied
  to node set A only; the sweep where all four failures live ran five seeds with early stopping. The
  four nodes were neither existence nor nonexistence, and a 30-seed re-run was queued — it is the
  `t2_p1_fournode_recheck` verdict in §6.

### (b) 2026-08-25 — ticket 35: P1 repaired and restored to PROVED through the two-pass gate

The statement was amended to the hypotheses the proof actually consumes, which is the three
grounds of finding 1 answered one by one: **A7-J** (joint tuple injectivity on the whole flagged-pair
set, including pairs no cutoff vector selects) replaces A7′; **h.16**, a continuation-cost
equivalence clause on the round-2 deviation set, closes the sunk-cost gap (and is trivially true on
any single-Voice menu, where that set is a singleton); and the $\kappa$ boundary is handled **by
extension, not by restriction** — no cut to $\kappa\in[0,1)$ is taken, and the false positivity
claim at $\kappa=1$ is withdrawn, the boundary histories being null under every profile and so off
nature's path rather than the players'. The §4.1–§4.3 table restrictions the argument consumes were
enumerated, and h.5 (A5) was struck: A5's existence and uniqueness content is derived from
$m_0\ge0$, its continuity content from the same scalar reduction, its measurable-selection content
from A7-J plus the Borel clause.

The gate was satisfied afresh, by two agents neither of whom wrote the proof:

- **Adversarial proof-read: PASS, 0 FAIL** (`threads/2026-08-25_P1_proofread_retry.md`, §5 below).
  The reader attacked the new Step 12 lemma on the merits before accepting anything, checked its
  four parts independently, and records that **his own round-1 FAIL witness is refuted** — he tried
  to rebuild it and could not, because price invariance and the conditional-expectation identity
  together force the wedge to zero. Three REPAIRs and four OBSERVATIONs, all applied; the round-1
  FAIL and the single sanctioned repair round are on file at
  `threads/2026-08-25_P1_proofread_round1.md`.
- **Statements-only re-derivation: PASS-WITH-CHANGES**
  (`rederive/P1_rederivation_2026-08-25.md`, §5 below). Input was the card row alone plus
  `CONTEXT.md` — no proof, no thread, no check script opened. It found no obstruction, and its
  changes 1–5 are citation- and wording-level; all three items the demotion turned on reproduce
  independently there (A7-J at R13 and R16, with A7′ provably insufficient for both uses; h.16 at
  R17 with a matching converse; the $\kappa=1$ withdrawal at R10).

**P1 CONJECTURE → PROVED, 2026-08-25, commit `0cbdb37`.** The 2026-08-21 chain is retained in the
card row and is recorded as **not** having satisfied the gate for the recorded statement. The
re-derivation's **change 6 was withheld** for the principal rather than folded — a proposed OPEN
item on whether A6's continuity of $\mathcal T$ is satisfiable at the collapsed cutoff vectors the
equilibrium notion admits. That withheld item is (d).

### (c) 2026-08-25 — ticket 33: A($\tau$) FAILS at the implemented calibration

The decisive check your finding 3 asked for has run:
`quality_reports/fixes/t2_atau_support_check.py`/`.json`, verdict extracted in §6. The pooled cell's
engagement-posterior law was enumerated exactly — all $4^{H+1}=4{,}194{,}304$ order-flow paths, the
same law the package prices — at 200 nodes, frozen policies, $H=10$. Two gates pass first, so the
object measured is A($\tau$)'s own: an independent re-enumeration reproduces to 0.0 exactly, and the
enumerated mean equals the pooled share to $1.7\times10^{-16}$. Neither Example A's $|A'_\kappa|$
nor level symmetry is imposed anywhere.

**Result: 20 nodes degenerate (A($\tau$) vacuous, deciding nothing); at all 180 non-degenerate nodes
A($\tau$) fails; at none does it hold.**

- **(τ-ii), support half — FAILS.** The support carries 23–767 distinct posterior values, never
  three, at 0 of 180 nodes; there is no mass at $\bar\pi/2$ anywhere; between 0.57% and 91.8% of
  pooled mass sits off $\{0,\bar\pi/2,\bar\pi\}$. The interior atoms move with $\kappa$: adjacent-
  $\kappa$ Hausdorff distance reaches 0.4608 against a predicted $<10^{-12}$, at 0 of 18 series.
- **(τ-ii), $\bar\pi$ half — HOLDS.** $\bar\pi=1$ to $1.5\times10^{-13}$ at every non-degenerate
  node and $\kappa$-free to the same order, 18 of 18 series. Recorded as a separate finding and
  explicitly **not** a partial rescue: $\bar\pi=1$ is the one-round outcome, so L3 Step 18's
  conjecture that the two-round timing leaves a top atom strictly below 1 is false here.
- **Derivative pattern — FAILS**, independently of the support: $A_0'=A_1'$ at 0 of 180 nodes, with
  $|A_0'-A_1'|\in[0.041,2.306]$ against a predicted $<10^{-10}$, both derivatives changing sign over
  the grid — which independently corroborates your finding 2 that $A'_\kappa$ carries no sign.
- **Chord identity — FAILS**: $0.0013$–$0.0717$ (up to 7.17 premium pp) against $<10^{-10}$, at
  0 of 180 nodes and on the most favourable of three kernel conventions.

**No label moves, and none is licensed.** A($\tau$) is an assumption, not a labelled claim.
**L3, L4 leg 3 and T1 Part B stay PROVED as conditionals**, their proofs untouched; what is now on
record is that their antecedent is not satisfied by the implemented pooled cell at this
calibration, so at this calibration those legs say nothing about the implemented cell. The card
carries this as a dated NUMERICAL-class evidence note under A($\tau$) in §5.

### (d) 2026-08-27 — the A6 panel: continuity failure real, locus corrected, no label moved

The re-derivation's withheld change 6 was ruled on by two opposed-brief Opus analysts, one briefed
to **substantiate** and one to **defuse**, working read-only. Both reports are inlined verbatim in
§5 (`threads/2026-08-27_A6_panel_substantiate.md`, `threads/2026-08-27_A6_panel_defuse.md`); records
committed at `97abec2`.

- **The mechanism is real and reaches $\mathcal T$.** All $k$-dependence of $U_j$ runs through the
  finite pooled price vector, the flagged layer being $k$-free by A7-J. Step 9(b) gives the Bayes
  belief where $\Lambda_k(h)>0$ and a **$k$-free** plan-uniform belief where $\Lambda_k(h)=0$, so
  the price at $h$ can be discontinuous exactly on $\partial\{k:\Lambda_k(h)>0\}$ — and the jump
  passes into $U_j$, because $U_j$ weighs those prices under the **deviator's own** noise law, not
  by the probability the plan is played. The defusal brief was attempted and failed: its author
  states he could not rebuild the vanishing-mass argument.
- **N11's locus is wrong in both directions; the corrected locus is the cell-edge hyperplanes
  $\cup$ the sole-generator collapse faces** — a collapse face is a discontinuity only when the
  collapsing plan is the sole on-path generator of some positive-probability history.
- **Measured, at the paper's own menu and calibration.** $\mathcal T_2$ jumps of
  $6.33\times10^{-3}$, $1.09\times10^{-2}$ and $2.83\times10^{-2}$ across the three interior $n(s)$
  cell edges at $(\kappa{=}0.5,\tau_{50},T{=}5)$, against a $10^{-10}$ convergence tolerance, with
  the belief snap matching the Step 9(b) prediction and surviving-type controls at solver noise
  ($\sim3\times10^{-9}$). At $(\kappa{=}0.15,0.05,5)$ — one of the four ticket-34 unresolved nodes —
  a jump of $0.1647$, a **destroyed** diagonal crossing, and a fixed point sitting **on** an edge.
- **The Hold-collapse face is clean.** Exit and Hold pool perfectly at mark-path type 0, so the
  dying plan generates no reachable pooled history of its own; the pooled price system moves by at
  most $4.441\times10^{-16}$ as $k_1$ sweeps to full collapse. N11 named the right mechanism at the
  wrong locus for this menu.
- **No label moves.** A6 is a listed hypothesis of P1, not a claim of it, so this is applicability
  evidence on an antecedent, in the A($\tau$) pattern; **P1 stays PROVED as a conditional**.
  Nonexistence is neither claimed nor shown — a discontinuous self-map may still have fixed points,
  and two survive at the $\kappa=0.15$ node. Recorded as card §9 item 4 with a §5 A6 evidence note.
  The one honest counterweight both panellists record: a chamber-interior $\Theta$ restores A6 at
  the baseline and contains $k^\star$, but it is not what the proof's Steps 13–14 construct, and it
  fails at $\kappa=0.15$.

### (e) 2026-08-27, in passing — A3 itself fails at that calibration, at two loci

Found by the panel and deliberately **not** folded into the A6 note, because it is upstream of A6
and larger. (i) At $(\kappa{=}0.5,\tau_{50},T{=}5)$ with $k_2$ on an **open set** above cell edge 6,
$U_V-U_H$ has three strict sign changes, middle excursions $2.4$–$2.8\times10^{-4}$ against a
$10^{-9}$ payoff tolerance; the pointwise argmax runs H,V,H,V, so **no weakly increasing selection
exists** — $\mathcal S(k)=\emptyset$ and $\mathcal T$ is **undefined** there, not merely
discontinuous. (ii) At $(\kappa{=}0.15,0.05,5)$ the argmax reverses VOICE $\to$ HOLD across an edge
at both located fixed points: the preferred plan **decreases** in $s$. The card records why this
does not conflict with the recorded "A3 and A6 proxies pass at every achieving seed" — those proxies
are local screens and measure neither argmax monotonicity in $s$ nor continuity of $\mathcal T$ in
$k$. Carried as a dated §5 A3 evidence note. **No label moves.**

### (f) 2026-08-27 — ticket 08: the draft_v3 theory sections, checked independently

The first paper-form write-up of this stack landed under `sections_v3/` (commit `9a73bb7`): a model
section (652 lines), a results section carrying every statement, and three proof files carrying
full proofs of D1, L1–L4, P1, T1 and C1. **Labels are transcribed verbatim with their
conditionality**, and evidence notes are carried at the assumption sites as well as the result
sites.

An independent Opus checker who wrote none of the files verified them against the card at full
statement grain — report inlined in §5 (`threads/2026-08-27_t4_sections_check.md`). **Verdict LAND:
0 WRONG, 13 MISCITED, 1 UNCHECKED, 14 OK-RESTRUCTURED.** A repair round followed and was
re-checked: it closed M-4a at both sites, T-10, M-10 and F-2, narrowed P-3, introduced no WRONG,
weakened no label and added no unsourced claim; **delta-pass verdict LAND** with a clean build (0
undefined, 0 errors, 0 overfull, 61 pages).

### (g) 2026-08-28 — the A6 probes curated into executed checks, and the ticket-34 account swept

Two standing follow-ups, both landed at commit `926f58c` — the stamp this bundle is built against.

- **The A6 panel's decisive probes are now executed t2 checks** with JSON verdicts beside the
  scripts: `t2_a6_edge_jump_check` (both panellists' routes replayed at their own brackets, the
  three $\mathcal T_2$ jumps agreeing across routes to $1.3\times10^{-4}$ relative, 20 gates, 0
  failing), `t2_a6_node15_check`, and `t2_a6_collapse_face_check`. **Two card wordings were
  corrected and the numbers left intact**, both recorded in the checks' own
  `known_discrepancies` rather than smoothed: the belief snap matches the Step 9(b) prediction to
  $\sim10^{-8}$ at the declared $10^{-8}$ bracket, but at the probes' own $10^{-9}$ bracket two of
  the three edges give $1.2\times10^{-7}$ and $1.7\times10^{-7}$ — floating-point cancellation over
  the sliver, a bracket artifact rather than a gap in the prediction, and the card's wording was
  optimistic by about one order of magnitude for those two; and "$\mathcal T$ bit-identical" on the
  collapse face holds for $U$ but not for $\mathcal T_2$, which moves $6.66\times10^{-16}$ — three
  ulps — at the one $k_1$ where the price signature deviates most.
- **The ticket-34 candidate account was swept over its other three nodes**
  (`t2_t34_account_sweep`), under a three-way rule pre-registered before any node ran and
  calibrated on the already-probed node. **It HOLDS at all three.** Pinned non-achieving fixed
  points sit on $n(s)$ cell edges at $(\kappa{=}0.15,0.075,1)$ and $(\kappa{=}0.85,0.075,1)$ — the
  second reached by no seed and found only by the direct edge test — each with $U_H-U_V$ jumping
  through zero without crossing it; at $(\kappa{=}0.85,0.05,5)$ no pin was found at any candidate
  edge, but the achieving basin's worst deviation sits in the cell immediately above an edge
  carrying the same jump. This is **diagnostic evidence only**: an edge-pinned fixed point of the
  implemented cutoff map is not an equilibrium and a stalled search is not a nonexistence proof, so
  existence at those nodes stays **neither claimed nor denied**. **No label moves anywhere in this
  batch.**

### The one label move

**Across (b) through (g) the only label move is P1's restoration from CONJECTURE to PROVED, and it
went through the two-pass gate — a fresh adversarial proof-read and an independent statements-only
re-derivation, neither by the proof's writer — not through prose.** Every other event in this
window either moved nothing (c, d, e, f, g) or moved a label **down** on your own finding (a).

---

## 3. MODEL CARD

The single source of truth. Its version stamp is the first thing to read: this bundle is built
against **2026-08-28 · follow-up curation · commit `926f58c`**, and where the card disagrees with
anything in §2, the card wins.

FILE: research/model_v4/MODEL_CARD.md (verbatim, complete)

===== BEGIN research/model_v4/MODEL_CARD.md =====
# MODEL CARD — v4 two-round blockholder disclosure model

**Version stamp: 2026-08-28 · follow-up curation (§5 A6 curation note + A3 sweep note) · commit `926f58c`.** An answer written against a stale stamp is
re-asked, not accepted. Regenerated from `threads/thread1_turn1_answer.md` after the turn-1 audit
(`threads/thread1_turn1_audit.md`), revised after the turn-2 proof-read
(`threads/thread1_turn2_audit.md`), surgically edited for ticket 24's A7 construction, and
regenerated after the 2026-08-23 post-review repair batch. Seven result rows moved from
CONJECTURE to PROVED on 2026-08-21 (commit `627642c`); C1 moved on 2026-08-22 (commit `403ac8e`);
and P1 was demoted on 2026-08-23 after the GPT end review and its audit (commit `43a45f8`).
**This regeneration (2026-08-25) records two events**: P1 is **restored to PROVED** on its ticket-35
repair — the statement amended to the hypotheses the proof actually needs (A7-J in place of A7′, the
continuation-cost clause, the $\kappa$ boundary handled by extension) and the two-pass gate satisfied
afresh by an adversarial proof-read PASS and an independent statements-only re-derivation
PASS-WITH-CHANGES, both 2026-08-25 and both by agents who did not write the proof; and §5's A($\tau$)
block gains ticket 33's dated evidence note. **On 2026-08-27** the re-derivation's withheld change 6
was ruled on (Austin-authorized, opposed-brief panel): §5's A6 and A3 blocks gain dated evidence
notes and §9 gains item 4 — answered in substance, locus corrected, **no label moves**. **On
2026-08-28** two standing follow-ups landed (again no label moves): the A6 panel's decisive probes
are curated into executed t2 checks (§5's A6 note, curation note — two wordings corrected, the
numbers intact) and the ticket-34 candidate account is swept over its other three nodes — the
account HOLDS at all three (§5's A3 note, sweep note). Every §4/§5
change below is traceable
to a named audit or re-derivation finding; the label moves are logged in
`research/model_v4/LABEL_LEDGER.md`. Vocabulary is `CONTEXT.md`.

## 1. Position and object

The disclosure rule *is* the market's partition. The model asks how liquidity $\kappa$ moves bidder
entry and the expected takeover premium when a stake threshold $\tau$ and a filing window $T$ split
control-node histories into a **flagged** cell (the filing has landed before the control decision)
and a **pooled** cell (it has not). The control-outcome object is the expected engagement-related
premium $\Delta^{\mathrm{act}}(\kappa,\tau,T)$; the price-path objects are the run-up path $R_d$,
the cumulative run-up $R$, and the filing-day jump $J$. Lower $\tau$ = tighter threshold margin;
lower $T$ = tighter window margin.

## 2. Timing (the two rounds)

1. Nature draws $v$ and the blockholder's signal $s$; the blockholder picks one complete contingent
   plan $j$ from a finite ordered menu.
2. **Round 1 — pooled trading.** The plan's stake path executes over business days
   $d = 0,\dots,H$. Market makers see pooled order flow and set $P_d^P = \mathbb E[Y \mid
   \mathcal H_d^P]$. **No within-window re-optimisation** — hence no feedback from realised order
   flow or prices into the path: $B_j(s,d)$, $q_{jd}(s)$ and $Q_j^F$ are functions of $(j,s,d)$ and
   $(j,s,\tau,T)$ alone. L2 Steps 3 and 6 fail without this; cite it as a numbered hypothesis.
3. **Disclosure node.** The flag lands iff $D = 1$, i.e. iff the plan engages, crosses $\tau$ at
   some date $c < \infty$, and $c + T \le H$. The filing reveals $F = (B^F, a = 1)$.
   **The flag terminates the pooled round.** Pooled trading stops when the filing lands; the flagged
   round follows it and the bidder acts after that. Without this reading
   $Q^F = b^*_j(s) - B^F_j(s)$ is not the blockholder's whole residual position and P1's
   flagged-round step fails (P1 re-derivation change C5, `rederive/P1_rederivation.md` Step 2).
4. **Round 2 — flagged trading, then the bidder.** If $D = 1$ the blockholder submits $Q^F$, the
   market prices $P^F = P(F, Q^F)$, then the bidder decides. If $D = 0$ there is no flagged round
   and the bidder acts on the pooled history.

Sequence: pooled round $\to$ flag or no flag $\to$ flagged round if applicable $\to$ bidder decision.

## 3. Equilibrium notion

**Cutoff perfect Bayesian equilibrium.** (i) a weakly ordered cutoff vector
$k = (k_1 \le \dots \le k_{J-1})$ mapping $s$ into a plan; (ii) sequentially optimal pooled and
flagged components; (iii) Bayes-consistent beliefs on path; (iv) competitive pooled and flagged
prices at their fixed points; (v) the bidder-entry rule; (vi) off-path beliefs as limits of
full-support perturbations. Weak inequalities permit collapsed action regions (including Hold).
Existence is Brouwer on the compact ordered polytope $\Theta$ for the outer map
$\mathcal T(k;\vartheta)$; $k = \mathcal T(k;\vartheta)$. Uniqueness is **not** claimed.

## 4. Symbol table

### 4.1 Primitives

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $v$ | target standalone value | $v \sim N(\mu_v,\sigma_v^2)$ |
| $s = v + \varepsilon$ | blockholder's private signal | $\varepsilon \sim N(0,\sigma_\varepsilon^2)$, $\perp v$ |
| $\beta$ | Gaussian projection in $\mathbb E[v\mid s] = \mu_v + \beta(s-\mu_v)$; $\beta = \sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)$ | $\beta \in (0,1)$ — **draft_v2's name; the turn-1 answer wrote $\lambda_s$. Bare $\lambda$ is reserved for D7.** |
| $\xi$ | bidder's private synergy shock | $\xi \sim N(0,\sigma_\xi^2)$, $\perp (v,s)$ |
| $\bar S$, $K$ | mean bidder synergy; bidder entry cost | $K > 0$ |
| $m_0, m_1$ | takeover premia without / with engagement | $m_1 > m_0$; **and $m_0 \ge 0$** — adopted from P1's h.12, so $\bar m(\mathcal I) = m_0 + \pi(\mathcal I)\Delta_m \ge 0$. This is what makes the inner pricing fixed point exist, be unique and be continuous (see A5). Dropping it produces both nonexistence and three-root multiplicity in executed counterexamples (`proofs/P1_proof.md` Step 7; `rederive/P1_rederivation.md` Lemma 2, Checks A/B) |
| $\Delta_m = m_1 - m_0$ | premium wedge | $\Delta_m > 0$ |
| $\Delta_V$ | non-takeover value created by engagement | $\Delta_V \ge 0$ |
| $\kappa$ | **noise-trading intensity** (= liquidity; never depth/volume/turnover) | $\kappa \in [0,1]$ |
| $\bar z$ | size of a ternary noise mark; $\Pr(z_d = 0) = 1-\kappa$, $\Pr(z_d = \pm\bar z) = \kappa/2$ | $\bar z > 0$ |
| $\tau$ | stake threshold | lower $\tau$ = tighter |
| $T$ | filing window, business days | $T \in \{1,\dots,H\}$; lower $T$ = tighter |
| $H$ | control-decision horizon (business days) | $H$ finite |
| $b_0, \bar b$ | initial and maximum stake | $0 \le b_0 \le \bar b$; **maintained $b_0 < \tau$** — a pre-existing crossing is outside the core (turn-2 audit D1-O1) |

### 4.2 Plans and legal timing

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $\mathcal J$, $j$ | finite ordered plan menu, least to most aggressive; plan index | $|\mathcal J| = J < \infty$ |
| $a_j$ | engagement attached to plan $j$ | $a_j \in \{0,1\}$; $a_j = 1$ for Voice, $0$ for Exit/Hold |
| $B_j(s,d)$ | cumulative pooled stake at day $d$; $B_j(s,-1) = b_0$ | $\in [0,\bar b]$; for Voice: $\partial_d B_j \ge 0$ and $\partial_s B_j \ge 0$; Hold constant, Exit weakly decreasing. **And, for every plan and every $d$, $s \mapsto B_j(s,d)$ is Borel** — automatic for Voice (monotone in $s$) and Hold (constant), but a **genuine addition for Exit**, where the card supplied monotonicity in $d$ only; without it the pooled prices in D1's part (c) are not defined, because pooled pricing integrates over every type including Exit types (`rederive/core_D1_L1_L2_rederivation.md` §A hypothesis H9 and consolidated finding 1 — the re-derivation makes D1's PROVED label conditional on this clause being on the card). **Continuum-valued** — A2′'s finiteness covers the plan menu, $\Gamma$'s image, the noise support and the calendar, *not* the stake level. On the flagged set the **composed terminal target** $s \mapsto b^*_{j(s)}(s)$ must be strictly increasing **for every cutoff vector $k \in \Theta$** (hypothesis **A7′ (on-path composed target)**, `proofs/A7_construction.md`). This strictness applies only to flag-capable composed targets: passive plans that never flag need not have strictly increasing $b_j^*$, and there must be no backtracking of $b_j^*$ across admissible Voice-plan switches. The stronger **A7-J (joint tuple injectivity)** is the condition $(j,s) \mapsto (B_j^F,Q_j^F,a_j)$ is injective on the full flagged-pair set; it is distinct from A7′'s on-path condition. Strictness of $B^F$ is neither necessary (it fails at crossing-date jumps on the pro-rata menu) nor sufficient (multi-Voice backtracking). Replaces the 2026-08-20 strict-pair patch (turn-2 audit L2-R1) per ticket 24 |
| $b_j^*(s) = B_j(s,H)$ | terminal target stake | $\in [0,\bar b]$ |
| $c_j(s;\tau) = \inf\{d : B_j(s,d) \ge \tau\}$ | threshold-crossing date | $+\infty$ if never |
| $f_j = c_j + T$ | legal filing date | flag lands iff $f_j \le H \iff B_j(s,H-T) \ge \tau$ |
| $D_j(s;\tau,T)$ | disclosure indicator $\mathbf 1\{a_j=1,\ c_j<\infty,\ f_j \le H\}$ | $\in\{0,1\}$; $D=1 \Rightarrow a=1$ |
| $B_j^F = B_j(s,f_j)$ | stake at filing | $T' < T \Rightarrow B^F(T') \le B^F(T)$ at fixed policies |
| $Q_j^F = b_j^*(s) - B_j^F$ | flagged-round order | $Q^F \ge 0$ for Voice plans; $T' < T \Rightarrow Q^F(T') \ge Q^F(T)$ |
| $\Gamma$ | finite ordered coarsening, stake increment $\to$ pooled order mark | **renamed from the answer's $\psi$; $\psi$ is D7 pivotality, $\chi$ is draft_v2's cost parameter** |
| $q_{jd}(s) = \Gamma(B_j(s,d) - B_j(s,d-1))$ | informed pooled order mark | ordered in the increment |
| $z_d$, $X_d = q_{jd} + z_d$ | noise order; observed pooled order flow | $z_d \in \{-\bar z, 0, +\bar z\}$ |

### 4.3 Information, prices, control outcome

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $\mathcal H_d^P$ | pooled public history: $(X_0,\dots,X_d;$ flag landed by $d)$ | finite |
| $F = (B^F, a=1)$ | filing message | truthful (A4) |
| $\mathcal I_H$ | **control-node information set, now filled** (the row read "—" until this regeneration): the *public* information at the control node — $\mathcal I_H = \mathcal H_H^P$ on the pooled cell $\{D=0\}$, and the flagged tuple $\mathsf S_F = (B^F, Q^F, a{=}1)$ on the flagged cell $\{D=1\}$. The bidder's own $\xi$ is private, else §4.3's $p(\mathcal I)$ would be an indicator | fill required by D1's cell-map clause and by L2's posterior clause, both of which are claims *about* $\mathcal I_H$ (`rederive/core_D1_L1_L2_rederivation.md`, reading RD-1 and consolidated finding 2). RD-1 states the flagged fill as $(\mathcal H_{f^-}^P, F, Q^F)$; **L2 is exactly the statement that the two are informationally equivalent on the flagged set** (conditional on $\mathsf S_F$ the pooled residual is pure noise), and L2 was re-derived in a form robust to either fill |
| $\mathcal C_F, \mathcal C_P$ | flagged / pooled cells | exclusive and exhaustive by construction |
| $\pi(\mathcal I) = \Pr(a=1\mid\mathcal I)$ | engagement posterior | $\in[0,1]$; $=1$ on $\mathcal C_F$ |
| $p(\mathcal I)$ | bidder-entry probability $1 - \Phi\big((P+K+m_0+\pi\Delta_m-\bar S)/\sigma_\xi\big)$ | $\in(0,1)$ |
| $\mathsf B$, $Y$ | entry indicator; terminal shareholder payoff $ (1-\mathsf B)(v + a\Delta_V) + \mathsf B(P + m_0 + a\Delta_m)$ | — |
| $P_d^P$, $P^F$ | competitive pooled price; flagged price $P(F,Q^F)$ | $P(\mathcal I) = \mathbb E[Y\mid\mathcal I]$ (inner fixed point). **Convention $P_{-1}^P := \mathbb E[Y]$**, the pre-trading pooled price — needed whenever $c=0$, which $T=H$ forces on every flagged history (turn-2 audit D1-R3). **The genuine fixed point sits at control nodes.** At an earlier pooled date $d<H$ the price is a *tower expectation* of already-solved control-node values, with no self-reference; only the control-node map is a fixed point to be solved (batch-1 audit P1-R8, `proofs/P1_proof.md` Step 5, split (a)/(b)) |
| $P_{\mathrm{ND}}(\mathcal H_{f^-}^P)$ | the **not-yet-disclosed** price at $f^-$ — the last pre-filing pooled price, at the **same realised order flow** (its history already carries "flag not landed by $f-1$"). **Not** a never-disclosed counterfactual: under that reading D1's identity acquires a residual term | $= P_{f^-}^P$ by construction (`rederive/core_D1_L1_L2_rederivation.md`, reading RD-3 and consolidated finding 7) |
| $R_d = P_d^P - P_{c^-}^P$, $R = P_{f^-}^P - P_{c^-}^P$ | run-up path, cumulative run-up | unsigned |
| $J = P^F - P_{\mathrm{ND}}$ | filing-day jump | unsigned; **not** claimed $\kappa$-invariant |
|  | identity: $P^F - P_{c^-}^P = R + J$ | exact |
| $U_j(s)$ | **the blockholder's objective** (new row; both passes flagged the card had none). The expected terminal value of the position the plan builds, net of what it costs to build and to engage: $U_j(s) = \mathbb E\bigl[b_j^*(s)\,Y - \mathcal C_j^{\mathrm{trade}} - a_j C_j(s) \bigm\vert s, j\bigr]$, with $\mathcal C_j^{\mathrm{trade}}$ the execution outlay (increments valued at the pooled prices $P_d^P$ up to the plan's last pooled date, plus $Q^F_j(s)P^F$ when $D_j=1$) and $C_j(s)\ge 0$ the engagement cost | **Definition is `proofs/P1_proof.md` h.14** (displayed there in full; `rederive/P1_rederivation.md` H12 writes the same object out term by term). Only two properties are ever used: **plan-locality** — $U_j$ depends on $j$ only through the executed stake path, the prices paid on it, the terminal stake, the engagement flag and the cost — and **integrability**, $\mathbb E[\max_j\lvert U_j\rvert] < \infty$ under A2′. Card gap closed here per batch-1 audit P1-R6 and P1 re-derivation change C2 |

### 4.4 Premium and comparative statics

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $h(\mathcal I) = \pi(\mathcal I)p(\mathcal I)$ | engagement-premium kernel | $h \ge 0$, $h(0) = 0$ |
| $\Delta^{\mathrm{act}} = \Delta_m\,\mathbb E[h(\mathcal I_H)]$ | expected engagement-related premium | $\ge 0$ |
| $M_F$, $M_P$ | $\Delta_m\mathbb E[h\mid D=1]$, $\Delta_m\mathbb E[h\mid D=0]$ | defined when the cell has mass |
| $\Omega = \Pr(D=1)$ | unconditional flagged weight; $\Omega = \Pr(a=1)\,\omega_a$ | $\in[0,1]$; **$\Omega$ is draft_v2's $\omega_P$ — the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the $\approx 0.29$ cut are all $\Omega$-type** |
| $\omega_a = \Pr(D=1\mid a=1)$ | disclosed share of engagements; the calibration target | $\in[0,1]$; **renamed from bare $\omega$** |
| $\bar\pi$ | **upper support point of the pooled engagement posterior in the A($\tau$) representation** (corrected here; the old gloss "pre-order pooled engagement share in the chord" was wrong and generated the L3/L4 collision) | $\in[0,1]$. **The pooled engagement share is the *mean* $\mathbb E[\Pi_\kappa]$, not $\bar\pi$.** Under A($\tau$) that share is $\kappa$-**invariant** (a mean-preserving spread), so it cannot be the quantity whose $\kappa$-motion L3 describes; it is **strictly below $\bar\pi$ in any non-degenerate case**, and equals $\bar\pi/2$ only under level symmetry $A_0=A_1$, where the martingale property gives $\mathbb E[\Pi_\kappa]=\bar\pi/2$. Reading $\bar\pi$ as the mean forces a point mass at $\bar\pi$ with $A'_\kappa=0$ and zero interior motion for every kernel — degenerate, and excluded. Binding orchestrator ruling 2026-08-21; flagged independently by both writers (`proofs/L4_proof.md` head block; `proofs/L3_proof.md` Step 19) and re-derived independently (`rederive/L3_rederivation.md` CH1, Step 11; `rederive/L4_rederivation.md` CHANGE 8) |
| $\mathcal S = \lvert\partial_\kappa\Delta^{\mathrm{act}}\rvert$, $\mathcal S_P = \lvert\partial_\kappa M_P\rvert$ | liquidity-sensitivities | $\ge 0$; $\mathcal S = (1-\Omega)\mathcal S_P$ under L2 + fixed policies |
| $C_h(\bar\pi) = h(0) - 2h(\bar\pi/2) + h(\bar\pi)$ | the chord | **= draft_v2's $\mathcal C(\bar\pi)$, condition (C\*), `lem:d1-jensen`**; maintained $\le 0$, $\lvert C_h\rvert$ weakly increasing in $\bar\pi$ |
| $A'_\kappa$ | common derivative of the A(τ) weights ($A_0' = A_1' = A'_\kappa$, $A_{1/2}' = -2A'_\kappa$) | bounded on $[0,1]$; **renamed from $a_\kappa$; $a$ is engagement** |
| $W_\tau, W_T$ | weight-effect ratios, e.g. $W_T = (1-\Omega(\tau,5))/(1-\Omega(\tau,10))$ | $\le 1$ when $\Omega$ rises |
| $\eta_r$ | C1 slack (see §4.5) | $>0$ on dominance-and-contraction nodes |
| $C_\tau, C_T$ | composition-effect ratios, e.g. $C_T = \mathcal S_P(\tau,5)/\mathcal S_P(\tau,10)$ | unsigned; kept (CONTEXT.md's "composition effect") — but $C$ is overloaded: $C_h$ chord, $C_j(s)$ engagement cost, $\mathcal C_F/\mathcal C_P$ cells. Always keep the margin subscript |

### 4.5 Equilibrium and GE dominance/contraction

| Symbol | Meaning | Sign restriction |
|---|---|---|
| $k = (k_1,\dots,k_{J-1})$ | cutoff vector | $k_1 \le \dots \le k_{J-1}$; maps to draft_v2's $(k_1,k_0,k_D)$ when the menu is the four named actions |
| $\Theta$, $\vartheta$ | compact ordered cutoff polytope; parameter vector | $\Theta$ nonempty, compact, convex |
| $\mathcal T(k;\vartheta)$ | outer cutoff best-response map (**always calligraphic** — upright $T$ is the window) | continuous, $\Theta \to \Theta$ |
| $L_{\mathcal R} = \sup_{\mathcal R}\lVert D_k\mathcal T\rVert$ | contraction bound on region $\mathcal R$ | $< 1$ required by AGE |
| $r_\tau = -\tau$, $r_T = -T$ | strictness coordinates | higher $r$ = tighter |
| $g_r^{PE} = -\mathrm{sgn}(d\Delta^{\mathrm{act}}/d\kappa)\,\partial_{\kappa r}\Delta^{\mathrm{act}}$ | direct fixed-policy attenuation margin (**the sign is written inline; no symbol $\sigma_\kappa$**) | $> 0$ required by C1 |
| $\bar k_x = \lvert\partial_x\mathcal T\rvert/(1-L_{\mathcal R})$, $\bar k_{\kappa r}$ | inversion-free derivative bounds | $\ge 0$ |
| $\mathcal B_r^{GE} = \lvert\Delta_{\kappa k}\rvert\bar k_r + (\lvert\Delta_{kr}\rvert + \lvert\Delta_{kk}\rvert\bar k_r)\bar k_\kappa + \lvert\Delta_k\rvert\bar k_{\kappa r}$ | GE remainder bound (cross-derivative analogue of D8's $\bar B$) | $\ge 0$; C1 needs $g_r^{PE} > \mathcal B_r^{GE}$ |
| $\mathcal R_r$, $\eta_r = g_r^{PE} - \mathcal B_r^{GE}$ | dominance-and-contraction region; slack | $\eta_r > 0$ at dominance-and-contraction nodes; region may be empty |

### 4.6 Proof-local notation (turn-2 rulings, binding)

L2's proof symbols, after the turn-2 notation audit: $\Xi := (v,s,\xi)$ (**renamed from $W$** — $W$ is
draft_v2's total surplus *and* its D5 wedge *and* the card's $W_\tau/W_T$; **never a bare $W$**);
$\Upsilon_{j,s}$, noise $\to$ pre-filing pooled history (**renamed from $G$** — draft_v2's $G_{EH},
G_{HQ}, G_{QP}$ payoff gaps and D7's bargaining surplus); $\mathsf Z$ **dropped** (write "each object
listed"); $\mathsf S_F=(B^F,Q^F,a{=}1)$ kept, introduced once as "$F$ augmented by $Q^F$", **never
bare**; $\mathcal H^P$ kept as shorthand for $\mathcal H_{f^-}^P$, subscript written at first use in
every proof; $\mathbf z^H$ kept, $z_{0:H}$ preferred; $\iota_F$ free; $u_1,u_2$ proof-local, never a
bare $u$.

## 5. Standing hypotheses

- **A1 Independent primitives.** $v,\varepsilon,\xi$ and all $z_d$ mutually independent; all
  variances strictly positive.
- **A2′ Finite model, amended boundedness** (was A2; the boundedness clause was **false**). The
  finiteness clauses are unchanged: plan menu $\mathcal J$, the image of $\Gamma$ (order-mark
  support), the noise support $\{-\bar z,0,+\bar z\}$ and the calendar horizon $H$ are finite. The
  boundedness clause is **replaced** by: *prices and payoffs are locally bounded in $(s,\vartheta)$
  on the maintained parameter set, and $\mathbb E\bigl[\max_{j\in\mathcal J}\lvert U_j\rvert\bigr]
  < \infty$ for every $k\in\Theta$.*
  *Why (P1 re-derivation change C1, `rederive/P1_rederivation.md` H2, Steps 3 and 12; adjudicated
  2026-08-21).* Flat global boundedness is **inconsistent** with the rest of the card: $v$ is
  Gaussian (§4.1) and the flagged region is unbounded in $s$ under A7′, so $Y$ — and with it prices
  and $U_j$ — is unbounded. Integrability is all any proof actually consumes. Every prior citation
  of "A2" in the proofs on file should be read as A2′; nothing in D1, L1, L2, L3, L4, P1 or T1 used
  the flat bound.
- **A3 Ordered plans, single crossing.** At every belief/price system, adjacent-plan payoff
  differences cross zero at most once in $s$, and the preferred plan is weakly increasing in $s$.
  *Evidence note added 2026-08-27 (A6 panel, in passing — a separate finding, deliberately not
  folded into the A6 note).* At the implemented calibration **A3 itself fails, at two
  independently-found loci, upstream of A6.** (i) At $(\kappa{=}0.5, \tau_{50}, T{=}5)$ with $k_2$
  on an **open set** above cell edge 6 (verified at offsets $10^{-9}$ through $2\times10^{-2}$),
  $U_V - U_H$ has **three strict sign changes** ($s = 1.5754434 / 1.5833333 / 1.5902426$; middle
  excursions $2.4$–$2.8\times10^{-4}$ against a $10^{-9}$ payoff tolerance), the pointwise argmax
  runs H,V,H,V single-valued on each interval, so **no weakly increasing selection exists** —
  $\mathcal S(k) = \emptyset$ and Step 13's $\mathcal T$ is **undefined** there, not merely
  discontinuous. (ii) At $(\kappa{=}0.15, 0.05, 5)$ — a ticket-34 UNRESOLVED node — the argmax
  reverses **VOICE $\to$ HOLD** across cell edge $s = 1.659062163$ at **both** located fixed points:
  the preferred plan decreases in $s$. The route is the $s$-direction step of $U_{VOICE}$ ($n(s)$ is
  integer-valued — Step 15(i) / WHERE IT FAILS 4's card-legal counterexample, instantiated by the
  solver's own `N_GRID` note) interacting with the off-path price snap. **No conflict with ticket
  34's "the A3 and A6 proxies pass at every achieving seed"**: those proxies are local screens —
  the A3 proxy tests residual slope signs at the two candidate cutoffs and the A6 proxy tests
  $\Theta$-corner non-pinning at the closest seed (`t2_p1_fournode_recheck.py`) — and neither
  measures argmax monotonicity over $s$ nor continuity of $\mathcal T$ in $k$, so both are silent
  on these findings. **Candidate mechanical account of ticket 34's four UNRESOLVED nodes**, on file
  and UNCHECKED beyond the one node probed: at the $\kappa = 0.15$ node one fixed point sits exactly
  on the edge where $U_H - U_V$ **jumps through zero without crossing it**, and the panel's
  residuals (payoff $3.06\times10^{-4}$–$1.77\times10^{-3}$ at cutoff residuals of
  $10^{-11}$-grade) **bracket ticket 34's recorded range exactly**; the $k$-direction jump
  mechanism does **not** explain those nodes (no proximity correlation — the substantiate
  panellist's own recorded negative). *Swept 2026-08-28 over the other three nodes
  (`quality_reports/fixes/t2_t34_account_sweep.py`/`.json`, pre-registered three-way rule): the
  account **HOLDS at all three**. At $(\kappa{=}0.15, 0.075, 1)$ and $(\kappa{=}0.85, 0.075, 1)$ a
  located fixed point sits on an $n(s)$ cell edge — $1.460178993$ (offset ${\sim}10^{-13}$, where
  10 of the 30 recheck seeds land) and $1.517932397$ (offset ${\sim}10^{-12}$, reached by **no**
  seed and found only by the direct edge test) — with $U_H - U_V$ **jumping through zero without
  crossing**. Neither pin is its node's achieving basin: their payoff residuals, $1.398\times10^{-3}$
  and $1.314\times10^{-3}$, sit above the recorded bests $1.059\times10^{-3}$ and
  $3.061\times10^{-4}$, each equalling the larger one-sided jump to at most $2.7\times10^{-4}$
  relative — a recorded, non-gating quantity. At $(\kappa{=}0.85, 0.05, 5)$ **no pin was found at
  any candidate edge in $[1.29, 2.11]$**; the achieving basin's worst deviation instead sits in the
  cell immediately above edge $1.583333333$ ($0.0250\,\sigma_s$ from it), where the same jump
  through zero occurs, at a deviation/jump ratio of $0.366$ — inside the pre-registered factor of
  3. Every pin is $n(s)$-family; the $\tau$-crossing pullbacks yielded none. Probe 5(b)'s distances
  replicate ($0.0258/0.0437/0.0295\,\sigma_s$ vs $0.026/0.044/0.030$). **No node yields a second
  independent fixed point, so node 15's residual bracket does not recur** — criterion (ii) rests on
  reproduction of every recheck basin alone. Diagnostic evidence at one calibration; existence at
  these nodes stays neither claimed nor denied.* No label moves — A3 is a hypothesis; P1 stays
  PROVED as a conditional. Records: the same panel files as the A6 note.
- **A4 Legal-clock discipline.** $c$ is the first date the path reaches $\tau$; filing lands exactly
  at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in the core.
- **A5 Inner pricing regularity, mostly demoted to a theorem.** Each public-history pricing map has a
  unique fixed point, continuous in beliefs, cutoffs and parameters.
  *Note (ticket 27, 2026-08-21).* **Under $m_0 \ge 0$ — now a card restriction, §4.1 — existence,
  uniqueness and continuity of the *inner* fixed point are THEOREMS, not assumptions.** The pricing
  map reduces to a scalar equation in two belief summaries: with $\bar y(\mathcal I) =
  \mathbb E_\mu[v] + \pi\Delta_V$ and $\bar m(\mathcal I) = m_0 + \pi\Delta_m$, the right-hand side
  is $P \mapsto \bar y + \bar m\,p(P)/(1-p(P))$ — the ticket-25 build writes the same map as
  $P = \hat V + \tilde m\,p/(1-p)$ — and it is strictly decreasing in $P$ wherever $\bar m \ge 0$,
  so it crosses the identity exactly once. **Three independent confirmations**: `proofs/P1_proof.md`
  Step 7; `rederive/P1_rederivation.md` Lemma 2 (with an executed counterexample producing zero
  roots, and another producing three, once $m_0<0$); and the ticket-25 build, whose
  `multiple_root_nodes` counter is structurally $0$ for the same reason (`impl_design.md` §13 and
  the smoke output). **A5 is retained only as its continuity clause** — the pricing family is
  continuous in the cutoff vector and the parameters, and measurable in the flagged tuple (the
  flagged information sets are continuum-indexed, so "unique fixed point" must be read as a
  measurably selected *family*, not a finite list). Where a proof cites A5 for existence or
  uniqueness, it may now cite §4.1's $m_0\ge0$ instead.
- **A6 Compact outer self-map.** All best-response cutoffs lie in a common compact ordered polytope
  $\Theta$; $\mathcal T$ is continuous and maps $\Theta$ into itself.
  *Evidence note added 2026-08-27 (A6 panel, Austin-authorized; ruling at §9 item 4).* Two
  opposed-brief agents (substantiate / defuse) examined the re-derivation's withheld change 6 (N11)
  and **converged**; the orchestrator's adjudication is on file. **The continuity clause fails for
  the declared construction, and the locus is not the one N11 named.** All $k$-dependence of $U_j$
  runs through the pooled price vector (the flagged layer is $k$-free under A7-J), and Step 9(b)
  gives Bayes where $\Lambda_k(h) > 0$ but a $k$-free plan-uniform posterior on the frontier, so the
  price system can be discontinuous exactly on $\bigcup_h \partial\{k : \Lambda_k(h) > 0\}$ — a set
  inside (the finitely many **cell-edge hyperplanes** $\{k_i = a\}$) $\cup$ (the **collapse faces
  whose dying plan is the sole generator** of some reachable pooled history). The jump **reaches
  $\mathcal T$ with non-vanishing weight**: $U_j$ integrates those prices against the deviator's own
  noise law (weight $\ge \min(\kappa/2, 1-\kappa)^{d+1}$, independent of the dying plan's population
  mass), so the vanishing-mass defusal is **refuted — by both panellists, independently**; the
  largest-weakly-increasing-selection tie-break is pointwise in $k$ and passes the jump through; and
  no $k$-independent perturbation family reconciles the limits (at fixed $n$ the system is
  continuous in $k$; the discontinuity is created only as $t_n \to 0$ — an order-of-limits problem
  the family choice cannot fix). On collapse faces proper: for $J \ge 3$ menus where a middle plan
  owns a reachable **exclusive** pooled history entering some $U_j$, the interior limit
  $\mu_v + \beta(c - \mu_v)$ varies over the face while any $k$-free family supplies one constant,
  so continuity fails at **every face point but at most one** (continuum-face lemma — single-pass
  panel derivation, **not gate-checked**). The implemented menu is **not** in that class: Exit and
  Hold pool perfectly in order flow, and its Hold-collapse face is **measured clean** (pooled prices
  within $4.4\times10^{-16}$ and $\mathcal T$ bit-identical as $k_1$ sweeps to full collapse). At
  the implemented calibration the failure is live at the **interior $n(s)$ cell edges** instead:
  measured $\mathcal T_2$ jumps of $6.33\times10^{-3}$ / $1.09\times10^{-2}$ / $2.83\times10^{-2}$
  across $\le 2\times10^{-9}$ steps in $k_2$ at $(\kappa{=}0.5, \tau_{50}, T{=}5)$ — **measured
  independently by both panellists with separate scripts, agreeing to 3 s.f.**, the belief snap
  matching the Step 9(b) prediction to $\sim10^{-8}$, surviving-type controls $\sim3\times10^{-9}$,
  robust at $1000\times$ the breakpoint-merge tolerance; at $(\kappa{=}0.15, 0.05, 5)$ jumps reach
  $0.16$ and a diagonal crossing of $\mathcal T_2$ is **destroyed**. A chamber-interior
  $\Theta^+ = [1.23, 1.245] \times [1.5253, 1.5506]$ (exhibited) is compact, self-mapping and
  jump-free at the baseline — Brouwer runs verbatim on it and it contains $k^\star$ — but it is
  **not the $\Theta$ Steps 13–14 construct** (they build from the bracket $[s_{lo}, s_{hi}]$, which
  contains the edges), cannot be exhibited without approximately locating the fixed point first, and
  **no such chamber exists at the $\kappa = 0.15$ node**, where a fixed point sits exactly on the
  edge $k_2 = 1.659062163$. **No label moves and none is licensed** — A6 is a hypothesis; P1 stays
  PROVED as a conditional, in the A($\tau$) pattern: what is on record is that its antecedent, read
  with the $\Theta$ the proof constructs, is not satisfied by the implemented calibration. Repairs
  on file, both outside §3's declared Brouwer-with-one-fixed-family route: the $t$-constrained game
  + Kakutani + $t \downarrow 0$ (`proofs/P1_proof.md` Step 18), and a $k$-indexed concentration
  family (constructible; its $0/0$ corner unresolved). The implementation's
  `OFF_PATH_EPS` $= 10^{-14}$ **is** the fixed-$t$ constrained game — the standard repair already
  shipped, with the switch relocated by $\sim10^{-9}$ rather than removed. Coverage: probes at one
  node per claim class plus the 27-node census, **not swept over $(\kappa, \tau, T)$**; nonexistence
  is neither claimed nor shown ($23/27$ sweep nodes converge; a discontinuous self-map may still
  have fixed points). Records: `threads/2026-08-27_A6_panel_substantiate.md`,
  `threads/2026-08-27_A6_panel_defuse.md`; probes
  `quality_reports/fixes/a6_panel_probes_2026-08-27/` (analysis-grade, not curated t2 checks).
  *Curation note added 2026-08-28.* The three decisive measurements are now executed t2 checks:
  `quality_reports/fixes/t2_a6_edge_jump_check.py`/`.json` (both panellists' routes replayed at
  their own filed brackets — $\mathcal T_2$ jumps $6.33\times10^{-3}$ / $1.09\times10^{-2}$ /
  $2.83\times10^{-2}$, agreeing across routes to a relative $1.3\times10^{-4}$, controls
  $2.8$–$3.6\times10^{-9}$, $\pm10^{-6}$ robustness intact), `t2_a6_node15_check.py`/`.json` (jump
  $0.1647$, destroyed crossing $+1.0\times10^{-7}\to-6.70\times10^{-2}$, edge fixed point to
  $1.06\times10^{-12}$) and `t2_a6_collapse_face_check.py`/`.json` (pooled prices within
  $4.441\times10^{-16}$). **Every figure these checks touch reproduces; two wordings above are
  corrected, the numbers are not.** The belief snap matches the Step 9(b) prediction to
  $\sim10^{-8}$ at all three edges at the truncation/cancellation crossover bracket $10^{-8}$; at
  the probes' own $10^{-9}$ bracket the first edge still holds ($4.0\times10^{-8}$, Analyst A's
  "7–8 dp"), but the second and third are $1.2\times10^{-7}$ and $1.7\times10^{-7}$ —
  floating-point cancellation over a $10^{-9}$-wide sliver, not a gap in the prediction. And
  "$\mathcal T$ bit-identical" holds for $U$ but not for $\mathcal T_2$, which moves
  $6.66\times10^{-16}$ (3 ulps) at the one $k_1$ where the price signature itself deviates most
  ($4.441\times10^{-16}$); invariance holds at the map's own root-finder resolution. The analytic
  weight bound $\min(\kappa/2,1-\kappa)^{d+1}$ is **not** curated — no probe computes it; its
  measured counterpart (the jump entering the adjacent-plan payoff difference undiminished) is.
  **No label moves and none is licensed.**
- **A7 Filing sufficiency.** On flagged histories $(B^F,Q^F,a=1)$ identifies the informed component
  of the selected plan; conditional on it, the pooled order-flow residual is pure noise, independent
  of $(v,s,\xi)$. The weak identification wording is not enough for L2. The two injective forms are
  named separately:
  * **A7′ (on-path composed target).** At a fixed cutoff policy, the composed terminal target
    $s\mapsto b^*_{j(s)}(s)$ is strictly increasing on the flagged signal region. The card's §4.2
    row quantifies this over every cutoff vector $k\in\Theta$; strictness is required only for
    flag-capable composed targets, with no backtracking across admissible Voice-plan switches.
  * **A7-J (joint tuple injectivity).** The full map
    $(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ is injective on the flagged-pair set, including flagged pairs
    that are not selected on path. This is stronger than the on-path A7′ form and is the form the
    pre-review P1 proof consumed.
  *Note (turn-2 proof-read).* **L2 uses A7′ on path; the weak wording is not sufficient** — it permits
  two $(j,s)$ pairs with different pooled paths, which is exactly L2's first failure case. Under A7′,
  the flagged tuple is continuum-valued as a tuple: injectivity forces $(B^F,Q^F)$ to be
  continuum-valued, while the coordinates may trade the burden. Injectivity plus measurability
  already gives the measurable inverse (standard Borel spaces); no separate assumption is needed.
  *Note (ticket 24, 2026-08-21).* **Satisfiability is resolved for A7′.** A7′ + a fixed cutoff
  policy + $\Omega > 0$ deliver the on-path injective form (positive-probability flagged tuples) with
  an explicit inverse; a satisfying menu exists — the pro-rata single-Voice menu with terminal target
  strictly increasing on all of $\mathbb R$, which also satisfies A7-J
  (`proofs/A7_construction.md`; adversarial attack verdict SURVIVES WITH REPAIRS,
  `proofs/A7_attack_verdict.md`, repairs applied 2026-08-21). A7-J additionally needs $b^*$ strictly
  increasing off the Voice region — a target flat below the Voice cutoff breaks it (40-collision
  executed check) while leaving A7′ intact. Failure boundary: a binding stake cap, quantized stakes,
  a composed target repeating values across Voice-plan switches, $\Omega = 0$, and policy-dependence
  when the condition is stated only at one equilibrium's cutoffs. A7′-satisfying menus are fully
  separating on the flagged set — the burden moves to P1's incentive compatibility, not away.
- **A8 Interior crossing.** $0 < \Omega(\kappa,\tau,T) < 1$. Required only for positive cell mass,
  never for the structural partition.
- **A($\tau$) Threshold chord restriction.** The pooled posterior law has the symmetric ternary
  representation $\mathbb E[h] = A_0(\kappa)h(0) + A_{1/2}(\kappa)h(\bar\pi/2) + A_1(\kappa)h(\bar\pi)$
  with $A_0' = A_1' = A'_\kappa$ and $A_{1/2}' = -2A'_\kappa$; maintained orientation
  $C_h(\bar\pi)\le 0$ with $\lvert C_h\rvert$ weakly increasing in $\bar\pi$. (draft_v2's (C\*) is
  the strict version; the $C_h = 0$ case must be handled explicitly.)
  **Two clauses added at this regeneration, each established by both L3 passes:**
  * **(τ-i) The kernel depends on the information set only through the engagement posterior.**
    $h(\mathcal I) = h(\pi(\mathcal I))$, so the three numbers $h(0)$, $h(\bar\pi/2)$, $h(\bar\pi)$
    are well defined and $\kappa$-free. This is a **restriction, not a reading**: §4.4 defines
    $h = \pi p$ and §4.3's entry row makes $p$ depend on the price as well as on $\pi$, so in the
    model $h = \pi\,p(\hat v, \pi)$ is a function of *two* scalars. The clause says the
    standalone-value channel and the engagement channel do not co-move inside the pooled cell in a
    way that moves $h$ at a fixed posterior. (`proofs/L3_proof.md` Hypothesis 8, batch-1 audit
    L3-R1; `rederive/L3_rederivation.md` CH3.)
  * **(τ-ii) The support and $\bar\pi$ are $\kappa$-free; only the weights move.** The three points
    $\{0, \bar\pi/2, \bar\pi\}$ do not vary with $\kappa$, and $\bar\pi$ itself is $\kappa$-free at
    fixed $(\tau,T)$. **Without the second half L3's conclusion is FALSE** — the derivative gains a
    term that is first order in $\bar\pi$ and the vanishing fails. (`rederive/L3_rederivation.md`
    CH2, the one omission the re-deriver said could sink the result;
    `proofs/L3_proof.md` Hypothesis 1.)

  *Where A($\tau$)'s bite actually is (L3's finding, both passes).* The derivative restrictions
  $A_0'=A_1'=A'_\kappa$, $A_{1/2}'=-2A'_\kappa$ are **not** an extra assumption: given a
  $\kappa$-invariant three-point support they are **equivalent** to $\kappa$-invariance of the
  pooled block's total mass and of its unnormalised engagement moment, both of which the model
  delivers at fixed policies. **A($\tau$)'s entire remaining content is the support condition.**
  A one-round ternary-noise market with informed mark $2\bar z$ and pre-order engagement share
  $\tfrac12$ satisfies it; the frozen manuscript's own no-disclosure structure (informed mark
  $\bar z$) does **not** — its pooled law has four atoms, two of which move with $\kappa$.
  **Whether the two-round pooled cell of §2 satisfies the support condition is OPEN**
  (`proofs/L3_proof.md` Part IV, Steps 16–18, with the weakest sufficient conditions named there).
  Every L3-conditional result — and therefore L4 leg 3 and T1 Part B — inherits that conditionality.

  *Evidence note added 2026-08-25 (ticket 33).* **At the implemented calibration the support
  condition FAILS — and it fails on the support, not on the derivative pattern.** The pooled cell's
  engagement-posterior law was enumerated exactly (all $4^{H+1} = 4{,}194{,}304$ order-flow paths,
  the same law `pooled_premium` integrates) at **200 nodes**: $\kappa\in\{0.05,\dots,0.95\}$ × the
  five frozen $\tau$ percentiles × $T\in\{1,2,5,10\}$, frozen policies, $H=10$. Two gates pass
  first, so the object measured is A($\tau$)'s own: an independent re-enumeration reproduces
  `pooled_pass` to **0.0 exactly**, and the enumerated mean $\mathbb E[\Pi]$ equals the pooled share
  $\bar\pi_{\mathrm{pr}} = \Pr(a=1\mid D=0)$ to $1.7\times10^{-16}$. Neither Example A's
  $\lvert A'_\kappa\rvert = 0.25$ nor level symmetry is imposed anywhere, and $\bar\pi$ is read as
  the upper support point throughout, per the binding ruling. **20 nodes are degenerate**
  ($\bar\pi_{\mathrm{pr}} = 0$ at $T\in\{1,2\}$ with $\tau$ at the 10th percentile: no engaging atom
  survives into the pooled cell, the law is the point mass at $0$, $M_P = 0$ and $C_h(0) = 0$, so
  A($\tau$) holds vacuously and the node decides nothing). At **all 180 non-degenerate nodes
  A($\tau$) fails**; at none does it hold.

  * **(τ-ii), support half — FAILS, by some eleven orders of magnitude.** The support carries
    **23–767 distinct posterior values**, never three (0 of 180 nodes), and there is **no mass at
    $\bar\pi/2$ at any node** ($A_{1/2}\equiv 0$). Between **0.57% and 91.8% of the pooled mass sits
    off $\{0,\bar\pi/2,\bar\pi\}$** — 13.9% at the median node ($T=5$, median $\tau$, $\kappa=0.55$:
    107 atoms, $A_0 = 0.768$, $A_1 = 0.093$). The atoms are not dust: coarsening the cluster
    tolerance to $10^{-3}$ still leaves **6–332** of them, and the floor-free law (the
    $\varepsilon\downarrow 0$ limit of §3 clause vi, the law reported here) counts at most 51 atoms
    fewer than the floored law the package prices. The interior atoms move with $\kappa$: the
    two-sided Hausdorff distance between adjacent-$\kappa$ support sets reaches **0.4608** —
    unchanged when restricted to atoms carrying mass $\ge 10^{-6}$ — against A($\tau$)'s predicted
    $<10^{-12}$, at **0 of 18** series. This refutes L3 Step 18's (S1) and (S2) together at this
    calibration.
  * **(τ-ii), $\bar\pi$ half — HOLDS.** $\bar\pi = 1$ to $1.5\times10^{-13}$ at every non-degenerate
    node, and $\kappa$-free to the same order (18 of 18 series). This is a separate finding and it
    is not a partial rescue: $\bar\pi = 1$ is the **one-round** outcome L3 Step 18 derives from
    §4.2's mark structure, and that step's conjecture that "the two-round timing … leav[es] the
    pooled cell with a top atom strictly below $1$" is **false at this calibration** — unflagged
    Voice types still generate fully revealing order flows. $\bar\pi\in\{0,1\}$ across the whole
    grid and never interior, so L3's small-$\bar\pi$ corollary has no instance here either.
  * **Derivative pattern — FAILS, and independently of the support.** $A_0' = A_1'$ holds at
    **0 of 180** nodes: $\lvert A_0'-A_1'\rvert\in[0.041,\,2.306]$ against a predicted $<10^{-10}$,
    with $A_0'\in[-2.146,\,2.374]$ against $A_1'\in[-0.014,\,0.429]$ — an order of magnitude apart
    in level, and both change sign over the grid, which independently corroborates that $A'_\kappa$
    carries no sign (audit finding 2). $A_{1/2}' = -2A'_\kappa$ also fails at all 180, but with
    $A_{1/2}\equiv 0$ that residual is exactly $2\lvert A_0'\rvert$ and is recorded as
    **inherited** — a restatement of the support failure, not a second piece of evidence.
  * **Chord identity — FAILS.**
    $\lvert\mathcal S_P - \Delta_m\lvert A'_\kappa\rvert\lvert C_h(\bar\pi)\rvert\rvert$, with
    $A'_\kappa$ **recovered** from the enumerated weights and $\bar\pi$ the **actual** upper support
    point, is **0.0013–0.0717 (up to 7.17 premium pp)** against $<10^{-10}$, at 0 of 180 nodes and
    on the most favourable of three kernel conventions. Recovered
    $\lvert A'_\kappa\rvert\in[0.042,\,2.374]$; the value the identity would *require* is
    $[0.00023,\,0.392]$, **disjoint** from block 3's implied $[0.997,\,1.158]$ — which is a
    different object (mean absolute slope over the $\kappa$ grid, and the level-symmetric
    $\bar\pi = 2\bar\pi_{\mathrm{pr}}$), and the distance between the two measures what the
    level-symmetry assumption was doing.
  * **(τ-i), reported as a diagnostic and not part of the verdict.** Within a $\Pi$-cluster ($\Pi$
    constant to $10^{-12}$) the enumerated entry probability still spreads by up to **0.085**, and
    $h$ by up to **0.018** mass-weighted. The kernel does not reach the information set only through
    the posterior at this calibration either.

  **What this changes, and what it does not.** NUMERICAL-class **applicability** evidence at one
  calibration; **no label moves**, and none is licensed — A($\tau$) is an assumption, not a labelled
  claim. L3, L4 leg 3 and T1 Part B stay **PROVED as conditionals** with their proofs untouched;
  what is now on record is that their antecedent is **not satisfied by the implemented pooled cell
  at this calibration**, so at this calibration those legs say nothing about the implemented cell.
  The question stated above stays open as a question about A($\tau$)'s **domain** — a different
  menu, a different $H$, or a different calibration could still satisfy (S1)–(S2) — and the two
  prior "failures" remain misformulated tests; this is the first test that measures A($\tau$)'s own
  object. Coverage caveats carried forward: the 18 non-degenerate series are only **6 distinct
  pooled cells** ($T=1$ and $T=2$ induce identical $D$-partitions at every $\tau$; $T=5$ joins them
  at the three highest $\tau$ percentiles and repeats itself at the two lowest; all five $T=10$
  quantiles coincide), and all six fail; the 50 $T=10$ nodes sit at $\Omega = 0.000681$, below
  `MIN_CELL_MASS` (`HANDOFF_sign.md` §8.1). Script and record:
  `quality_reports/fixes/t2_atau_support_check.py` → `t2_atau_support_check.json` (200 nodes, 920
  pooled enumerations, 1002 s; top-level `verdict` field `FAILS at calibration`).

- **A(br) Chord–sensitivity bridge.** *(NEW at this regeneration. Consumed by L4 leg 3 and by T1
  Part B, and by nothing else. Statement transcribed from `proofs/L4_proof.md`'s top block as
  repaired on 2026-08-21, with (br-v) appended.)* For two compared thresholds $\tau' < \tau$ at
  fixed policies and a common $\kappa$:
  * **(br-i) Representation at both policies.** A($\tau$)'s symmetric ternary representation holds
    for the pooled class under $\tau$ *and* under $\tau'$, with chord endpoints $\bar\pi(\tau)$,
    $\bar\pi(\tau')$ and weight-derivative coefficients $A'_\kappa(\tau)$, $A'_\kappa(\tau')$.
  * **(br-ii) $\kappa$-localisation.** At fixed policies all $\kappa$-dependence of $M_P$ sits in
    the A($\tau$) weights: the three support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$
    *as a function of the posterior* do not move with $\kappa$. Hence
    $\partial_\kappa M_P = \Delta_m A'_\kappa C_h(\bar\pi)$ exactly, with no
    composition-through-$\kappa$ remainder. (Against the card's *literal* A($\tau$) display this
    would restate (br-i); it is written against the honest reading $h = \pi\,p(\hat v,\pi)$, and it
    is the clause that repairs that ambiguity rather than a fourth independent restriction — it
    names the same object as A($\tau$)(τ-i). The trailing "hence" is **derivable**, not assumed:
    `rederive/L4_rederivation.md` CHANGE 4, Step 16.)
  * **(br-iii) Coefficient stability across the threshold margin.**
    $\lvert A'_\kappa(\tau')\rvert \le \lvert A'_\kappa(\tau)\rvert$. Weakest sufficient form:
    equality — reclassification changes *which* histories are pooled, not the
    $\kappa$-responsiveness of the pooled weights.
  * **(br-iv) Endpoint linkage.** $\bar\pi$ is A($\tau$)'s chord endpoint — the **upper support
    point** of the pooled posterior law — and it is a weakly increasing function of the pooled
    prior engagement share $\bar\pi_{\mathrm{pr}} = \Pr(a=1\mid D=0)$, **the same function at
    $\tau$ and at $\tau'$**. (Support-point form, per the binding $\bar\pi$ ruling; the identity
    branch $\bar\pi = \bar\pi_{\mathrm{pr}}$ is excluded as degenerate, `proofs/L3_proof.md`
    Step 19.)
  * **(br-v) Comparability of the chord functional across thresholds.** $C_h(\cdot)$ — and the
    kernel $h$ it is built from — are the **same functions of the posterior** at both compared
    thresholds. Without it, leg 3 compares $\lvert C_h\rvert$ across two different functionals and
    the comparison is meaningless; $h = \pi p$ with $p$ priced off a cell whose composition the
    threshold moves, so $\tau$-invariance of $h$ is real content, not bookkeeping.
    **Independently required by three agents**: the T1 proof-reader (as "(br-v)", batch-2 audit),
    the L4 re-deriver (as "(br-ii′)", `rederive/L4_rederivation.md` CHANGE 3), and the T1
    re-deriver, who confirmed it is required **and** not implied by (br-i)–(br-iv)
    (`rederive/T1_rederivation.md`, Part B verdict). Canonical name is **(br-v)**; T1's proof
    carries it as H17.

  *Sharpening on file, recorded not assumed (`rederive/L4_rederivation.md` CHANGE 8, Steps 22–24).*
  $\bar\pi = \bar\pi_{\mathrm{pr}}/\rho$ with $\rho := \tfrac12 A_{1/2} + A_1$ provably
  $\kappa$-free, so (br-iv) $\iff$
  $\rho(\tau')/\rho(\tau) \ge \bar\pi_{\mathrm{pr}}(\tau')/\bar\pi_{\mathrm{pr}}(\tau)$. Under the
  level-symmetric reading $\rho = \tfrac12$ and $\bar\pi = 2\bar\pi_{\mathrm{pr}}$, which forces
  $\bar\pi_{\mathrm{pr}} \le 1/2$ — an inherited restriction on A($\tau$)'s domain that L4 does not
  resolve. (br-iii) is the clause with the least justification behind it; it is the one to attack
  first.
- **AGE GE differentiability and contraction.** On a candidate region $\mathcal R$ the outer map is
  twice continuously differentiable, $L_{\mathcal R} < 1$, and the sign of the equilibrium liquidity
  derivative is constant on $\mathcal R$.

## 6. Result ledger

**All eight results now carry two-pass evidence** (C1 moved on 2026-08-22, after its own
proof-read, re-derivation, and the independent re-run of every check script — ALL REPRODUCE,
`quality_reports/fixes/t2_rerun_verify_note.md`; **P1 was demoted on 2026-08-23 and restored on
2026-08-25** on a fresh pair of passes over the amended statement). The protocol (§7) requires an
adversarial
proof-read PASS **and** an independent statements-only re-derivation PASS, by different agents,
before a label moves. That gate is satisfied for D1, L1, L2, L3, L4, T1, C1 and — as of 2026-08-25 —
P1 again. **P1's 2026-08-21 chain never satisfied it**: the proof consumed A7-J while the row and
re-derivation carried A7′, so the two passes covered two different statements, which is what the
2026-08-23 demotion turned on. The pair on file now is
`threads/2026-08-25_P1_proofread_retry.md` (0 FAIL) and
`rederive/P1_rederivation_2026-08-25.md` (PASS-WITH-CHANGES, changes folded into the row). Every statement below is the *amended*
statement — the hypothesis sets are named in full and descriptively, and **no statement was weakened
silently**: each difference from the pre-regeneration row is traceable to the named finding beside
it. The label moves themselves are logged in `research/model_v4/LABEL_LEDGER.md`.

| ID | Statement (amended), with its full hypothesis set | Label | Evidence chain |
|---|---|---|---|
| D1 | Under **A1, A2′, A4, A5, the §4.1/§4.2 table restrictions, §3(i)'s cutoff selection map, the §4.3 conventions ($P_{-1}^P=\mathbb E[Y]$; $P_{\mathrm{ND}}=P^P_{f^-}$)**, and two hypotheses this regeneration wrote into the card — **Borel regularity of $s\mapsto B_j(s,d)$ for *every* plan including Exit** (now a §4.2 clause; needed only for part (c), since pooled pricing integrates over all types) and **a content for $\mathcal I_H$** (now filled in §4.3) — $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is **measurable** and maps every control-node history into exactly one cell; for every Voice plan $f_j\le H \iff B_j(s,H-T)\ge\tau$; and each flagged history yields $B^F, R_d, R, J$ with $P^F - P_{c^-}^P = R + J$. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `threads/thread1_turn2_answer.md`; **proof-read PASS 2026-08-20** `threads/thread1_turn2_audit.md` (3 non-blocking repairs: uncited public-flag bridge, $B^F$ continuum-valued, $P_{-1}^P$ convention); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/core_D1_L1_L2_rederivation.md` §A — the two added hypotheses are its changes, and both are now card rows, so the row no longer rests on anything the card lacks |
| L1 | Under **D1, the §4.3/§4.4 definitions, A5 (which pins *the* version of $\mathbb E[Y\mid\mathcal I]$), A2′ with §4.1 ($\Delta_m$ finite), and A1 (one probability space)**: whenever $0<\Omega<1$, $\Delta^{\mathrm{act}} = \Omega M_F + (1-\Omega)M_P$; at $\Omega=1$ it degenerates to $\Delta^{\mathrm{act}}=M_F$ and at $\Omega=0$ to $\Delta^{\mathrm{act}}=M_P$, the null-cell average being **undefined rather than imputed** — proved as a non-identification statement, not asserted. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `threads/thread1_turn2_answer.md`; **proof-read PASS 2026-08-20** `threads/thread1_turn2_audit.md` (clean; one cosmetic repair); **re-derivation PASS 2026-08-21, PROVED-AS-STATED** `rederive/core_D1_L1_L2_rederivation.md` §B — no change to the statement |
| L2 | At fixed cutoff and execution policies, under **A1; A2′ *with* the §4.1/§4.2 table restrictions; A4; A5; A7′ in its on-path injective form, consumed almost surely on the flagged set; D1; the no-feedback timing of §2; and $\Omega>0$** — together with an explicit bidder-entry rule (§4.3's, or any rule with the two properties named in the proof), carried as bookkeeping: $(B^F,Q^F,a{=}1)$ makes the pre-filing pooled history conditionally independent of $(v,s,\xi)$ on the flagged set, so the flagged posterior, price, entry probability and $M_F$ are invariant to $\kappa$. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `threads/thread1_turn2_answer.md`; **proof-read PASS 2026-08-20** `threads/thread1_turn2_audit.md` (4 non-blocking repairs; its largest flagged risk — A7 satisfiability — was closed by ticket 24, `proofs/A7_construction.md` + `proofs/A7_attack_verdict.md`); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/core_D1_L1_L2_rederivation.md` §C. **Statement changes, all traceable and none a weakening of the conclusion**: A2′, D1 and the entry rule were *used but not enumerated* in the old row (finding 3); "almost surely" is the re-derivation's own *permissive* reading of A7′, and it is the only coherent one when $B^F$ is continuum-valued, since then no individual flagged tuple has positive probability |
| L3 | **PROVED under A($\tau$)** — including its two new clauses (τ-i) kernel-through-posterior and (τ-ii) $\kappa$-free support **and $\kappa$-free $\bar\pi$** — plus: $h(0)=0$; $\kappa$-free pooled mass and engagement moment at fixed policies; D1 by statement; regularity *stated minimally* ($h$ continuous on $[0,\bar\pi]$, twice differentiable on the open $(0,\bar\pi)$ — Darboux does the rest, no continuity of $h''$); for the small-$\bar\pi$ corollary only, a second-order Peano expansion of $h$ at $0+$ and one and the same kernel along the shrinking family; and, for the seam where L4 consumes L3, $\lvert A'_\kappa\rvert$ bounded **uniformly in $\bar\pi$** along the limit. Then $\partial_\kappa\mathbb E_\kappa[h] = A'_\kappa C_h(\bar\pi)$ exactly; $C_h(\bar\pi) = \tfrac14\bar\pi^2 h''(\zeta)$ for some $\zeta\in(0,\bar\pi)$ — an identity, not an approximation; $C_h = \tfrac14 h''(0)\bar\pi^2 + o(\bar\pi^2)$, so the interior motion vanishes at rate $\bar\pi^2$ as $\bar\pi\downarrow 0$. **An "if", never an "iff"** ($A'_\kappa=0$ also kills the motion). **Conditional**: whether the two-round pooled cell satisfies A($\tau$)'s support condition is OPEN (§5, §9). | **PROVED** under A($\tau$) | statement `threads/thread1_turn1_answer.md`; proof `proofs/L3_proof.md` (repairs applied 2026-08-21); **proof-read PASS 2026-08-21** `threads/2026-08-21_batch1_proofread_audit.md` §2 (0 FAIL; L3-R1…R5 applied; executed checks reproduce to $\le 2\times10^{-18}$); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/L3_rederivation.md`. **Changes CH1–CH7 are all hypothesis-explicitness**, folded into A($\tau$)/§4.4 above; CH2 ($\kappa$-free $\bar\pi$) is the one whose omission would have made the conclusion false, and it is now a card clause |
| L4 | At fixed policies, for $b_0 < \tau' < \tau$ at a common window $T$ and a common $\kappa$, with $\Omega(\tau',T)<1$: **(leg 1, unconditional)** $\mathcal C_F(\tau,T)\subseteq\mathcal C_F(\tau',T)$ with every newly flagged history generated by a Voice plan, hence $\Omega(\tau',T)\ge\Omega(\tau,T)$; **(leg 2, unconditional)** the pooled engagement **share** falls, $\bar\pi_{\mathrm{pr}}(\tau')\le\bar\pi_{\mathrm{pr}}(\tau)$, with an exact identity for the gap; **(leg 3, PROVED under A(br))** $\mathcal S_P(\tau',T)\le\mathcal S_P(\tau,T)$, with equality whenever $C_h(\bar\pi(\tau))=0$. Legs 1–2 need only **D1's clock equivalence, the §2 no-feedback timing, fixed policies, $b_0<\tau'<\tau$ imposed at *both* thresholds, A1, A4, §4.2's $D=1\Rightarrow a=1$, and $\Omega(\tau')<1$** — the two "nestedness" clauses the old row implied are **conclusions, not hypotheses**. Leg 3 additionally needs **L3 by statement, A($\tau$)'s maintained *magnitude* monotonicity of $\lvert C_h\rvert$ (the sign half $C_h\le0$ is never used at this leg), and A(br) clauses (br-i)–(br-v)**. | **PROVED** (legs 1–2 outright; leg 3 **under A(br)**) | statement `threads/thread1_turn1_answer.md`; proof `proofs/L4_proof.md` (repairs applied 2026-08-21); **proof-read PASS 2026-08-21** `threads/2026-08-21_batch1_proofread_audit.md` §3 (0 FAIL; L4-R1…R5 applied); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES) `rederive/L4_rederivation.md`. **Traceable changes**: the old row's "under nested reclassification" is replaced by "under A(br)" because nestedness is a *conclusion* (L4 writer's deletion of turn-1 H1–H3, audit L4-R5); the old row's "$\bar\pi$" is replaced by the **share** $\bar\pi_{\mathrm{pr}}$ per the binding $\bar\pi$ ruling; (br-v) is added on three independent findings |
| P1 | Under **A1, A2′, A3, A4, A6, A7-J (joint tuple injectivity — §5's joint $(j,s)$ form of A7, on the whole flagged-pair set $\{(j,s):D_j=1\}$ *including pairs no cutoff vector selects*; strictly stronger than the on-path A7′, and the form the proof consumes where it pins *off-path* flagged beliefs. Amended from A7′ 2026-08-25: the pre-review row carried the on-path form while `proofs/P1_proof.md` h.7 consumed the joint form, so the two 2026-08-21 passes covered two different statements), D1 by statement *with its own hypotheses travelling*, the §2 no-feedback timing read with the flag-terminates-the-pooled-round clause, the definitional round-2 action-set hypothesis** (the flagged-round action set **is** the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements agreeing with $j$ on everything already played — *not* a closure condition; the closure form is jointly unsatisfiable with finiteness by cardinality), **continuation-cost equivalence on that same set** (the proof's h.16, added 2026-08-25: menu elements sharing $j$'s pooled path up to $f_j(s)$ with $a_{j'}=a_j$ carry the same engagement cost, $C_{j'}(s)=C_j(s)$. **Trivially true on any single-Voice menu**, where that set is a singleton. What it buys, **under the plan-completion reading of the $C_j(s)$ timing convention below** — under the sunk reading the continuation is constant on the deviation set with no clause at all and h.16 is not consumed, so the hypothesis is listed because the row does not commit to a reading, and it is what makes the conclusion hold under both: on that set the flagged price does not move and the order cancels, so the engagement cost is the only thing that can differ between staying and deviating — and at a flagged pair the cutoff vector does **not** select there is no date-0 optimality to fall back on, so without this clause the deviator takes the class member with the smallest cost and item (ii) of §3 fails at that node. Live only on menus with two or more Voice plans sharing a pooled path), **$m_0\ge0$, the §4.3 blockholder-objective definition $U_j$** (whose $-a_jC_j(s)$ display `proofs/P1_proof.md` h.14 now carries verbatim, which is what the row's "displayed there in full" asserts; **timing convention, stated here because §4.3 does not date $C_j(s)$**: the engagement cost may be booked either on completing the plan or as sunk once the filing has landed — the two give the same round-2 comparison on the round-2 deviation set, which is what the continuation-cost clause above buys, so the result does not depend on the choice), **and the §4.1–§4.3 table restrictions the argument consumes — in particular §4.3's $Y$ row with the price convention $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ and the entry row for $p(\mathcal I)$; §4.2's Borel-regularity clause for *every* plan including Exit (needed directly, not via D1, whose conclusion is measurability of $D$ and the cell map); §4.2's $D=1\Rightarrow a=1$, the $c/f/B^F/Q^F/b^*$ definitions and $\partial_sB_j\ge0$ for Voice; and §4.1's distributional forms with $\Delta_m>0$**: **at every $\kappa\in[0,1]$**, a cutoff PBE over complete contingent plans exists — $k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, prices at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs as limits of **one** full-support perturbation family over **plans — fixed once and used to define the price system at every $k\in\Theta$, not only at $k^\star$, since the deviation payoffs that define $\mathcal T$ read off-path pooled histories — at every pooled history reachable *with positive probability* under some plan profile** (at the boundary values $\kappa\in\{0,1\}$ the §4.1 noise support degenerates to $\{0\}$ and to $\{\pm\bar z\}$ respectively; a pooled history needing a mark outside it is null under *every* profile, so it is off nature's path rather than off the players', carries no §3(vi) requirement, and is read by no step. This is the extension route, not the restriction one: no cut to $\kappa\in[0,1)$ is taken, and the pre-repair claim of a belief at *every* pooled history — false at $\kappa=1$ — is withdrawn); **flagged-tuple beliefs supplied by A7-J** at every tuple in the image of the flagged-pair map $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$ — on path and off, since the image includes tuples generated by pairs the cutoff vector does not select — as the point mass at the unique generating pair, which is a **version** of the conditional law at every image tuple (the signal is continuous, so a version is what a conditional law is; any a.e.-equal version serves §3(iii)/(vi) equally) and is the version this equilibrium selects, with no tuple outside that image arising because the round-2 action-set hypothesis leaves no off-menu order to produce one; the §4.3 entry rule; and **a sequentially optimal flagged component at every flagged pair $(j,s)$, whether or not the cutoff vector selects it** — the flagged price is invariant across the round-2 deviation set (A7-J pins the belief at the same $s$ and $\pi=1$), so the order cancels out of the continuation and the continuation-cost clause makes what remains constant. **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$, its continuity content from the same scalar reduction, and its measurable-selection content from A7-J plus §4.2's Borel clause (see A5). **A6 is read** as asserting that $\mathcal T$ — under a named tie-break-and-corner selection, without which a correspondence cannot be called continuous — is a well-defined single-valued continuous self-map of $\Theta$, with $\Theta$ nonempty per §4.5. **At any such equilibrium at which A8 holds**, both cells carry strictly positive probability and are on path; for A8's restatement as a single signal threshold add **H-ord** (Voice stake monotonicity across plans — the writer's h.13, **renamed here to avoid collision with the objective row**) and the upper-set engagement-flag hypothesis. Uniqueness is not claimed. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `proofs/P1_proof.md` (repairs applied through P1-R35, ticket 35 rounds 1–2, close-out and confirm-pass sweep); **proof-read PASS 2026-08-25** `threads/2026-08-25_P1_proofread_retry.md` (**0 FAIL**; 3 REPAIRs + 4 OBSERVATIONs, all applied; the reader verified the Step 12 lemma part by part on the merits and records that his own round-1 FAIL witness is refuted — round-1 FAIL and the sanctioned repair round at `threads/2026-08-25_P1_proofread_round1.md`); **re-derivation PASS-WITH-CHANGES 2026-08-25** `rederive/P1_rederivation_2026-08-25.md` (fresh agent, card row alone; changes 1–5 folded into this statement cell — the §4.1–§4.3 citation block, D1's hypotheses travelling with the three-part A5 sentence, the one-family/every-$k$/positive-probability off-path clause, A6's tie-break-and-corner reading, the $C_j$ timing convention; **change 6 withheld for Austin** — a proposed §9 OPEN item on whether A6's continuity of $\mathcal T$ is satisfiable at the collapsed cutoff vectors §3 admits; **ruled 2026-08-27**: answered rather than filed OPEN — §9 item 4 and the §5 A6/A3 evidence notes carry the panel record, no label moved). **The 2026-08-21 chain is retained below and did not satisfy the gate for the recorded statement**: proof-read PASS 2026-08-21 `threads/2026-08-21_batch1_proofread_audit.md` §4 (0 FAIL; P1-R1…R8; inner fixed point executed on 20k random draws — 0 multiplicity, 0 sign failures) and re-derivation PASS 2026-08-21 (PROVED-WITH-CHANGES) `rederive/P1_rederivation.md` (changes C1–C8) covered **two different statements** — the proof's h.7 consumed the joint injective form of A7 while the row and re-derivation carried the on-path form — which is what the 2026-08-23 demotion turned on, together with Step 12's missing continuation-cost clause and the false positivity claim at $\kappa=1$; all three are repaired and independently reproduced by the 2026-08-25 re-derivation. **Numerical status, stated honestly and separately from the label (ticket 34, `quality_reports/fixes/t2_p1_fournode_recheck.json`):** the four sweep-unresolved nodes ($\kappa\in\{0.15,0.85\}\times(\tau,T)\in\{(0.05,5),(0.075,1)\}$) remain **STILL UNRESOLVED after 30 seeds each** — best payoff-scale residual $3.1\times10^{-4}$–$1.5\times10^{-3}$ against a $10^{-9}$ criterion, best cutoff-scale residual $10^{-14}$–$10^{-11}$; the A3 and A6 proxies pass at every achieving seed. **UNCHECKED**: existence at those four nodes is neither claimed nor denied by this evidence, and the label rests on the proof plus the two 2026-08-25 passes, not on the grid. |
| T1 | At fixed plan and cutoff policies, with $0<\Omega<1$ and $\mathcal S_P>0$: **(A)** $\mathcal S = (1-\Omega)\mathcal S_P$ exactly, and the same factorisation holds for the total-variation aggregate of $\Delta^{\mathrm{act}}$ over any $\kappa$-grid with no differentiability required; **(B)** threshold tightening attenuates — $\mathcal S(\tau')/\mathcal S(\tau) = W_\tau C_\tau \le 1$ because **both** ratios lie in $[0,1]$, no dominance condition needed; **(C)** window tightening attenuates **iff** $W_T C_T \le 1$, where $W_T\le1$ is **proved** (from D1's clock equivalence and the monotone Voice stake path) and $C_T$ is **unsigned** — "equivalently $\partial_{r_T}\mathcal S_P/\mathcal S_P \le \Omega_{r_T}/(1-\Omega)$" holds **on average along the tightening path** (integrated over $[-T,-T']$), exactly in the infinitesimal limit, and is **false read pointwise**. Hypotheses: **fixed policies; A8 at each compared policy; $\mathcal S_P>0$; L1; L2 (its own hypotheses travelling); D1; PE-$\Omega$ ($\partial_\kappa\Omega=0$ at fixed policies — derivable, not assumed, and it fails in GE, which is C1's term); $\kappa$-differentiability of $M_P$ (no card hypothesis supplies this — carried in-proof); A($\tau$) at both compared policies with the $\bar\pi$ ruling; L3; A(br) (br-i)–(br-v) at the threshold pair; L4; the §2 no-feedback timing; a smooth window interpolation for the local form; threshold-side smoothness (confirmed non-load-bearing)**. No unconditional window sign is claimed. | **PROVED** at fixed policies | statement `threads/thread1_turn1_answer.md`; proof `proofs/T1_proof.md`; **proof-read** `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15, non-propagating) → **fix round CLOSED**, `threads/2026-08-21_T1_fix_recheck.md` (T1-F1 discharged by H18; items N1–N4 applied; boxed displays byte-identical) → **PASS-equivalent**; **re-derivation PASS 2026-08-21** `rederive/T1_rederivation.md` (all parts PROVED-AS-STATED except the "equivalently" quantifier, PROVED-WITH-CHANGES). **Traceable change**: the old row's unqualified "equivalently" is false pointwise; the quantifier **"on average along the tightening path"** is added on the re-deriver's S28(ii) and matches what the fix round adopted |
| C1 | **The dominance-and-contraction implication, region carried as a named hypothesis.** Under: AGE's along-the-path contraction $L_{\mathcal R}<1$ **in one fixed norm convention** (an induced operator norm with its dual pairings — the re-derivation's N1; a mismatched pairing silently voids the implication); $\mathcal R_r$ relatively open in *both* coordinates with $\kappa\notin\{0,1\}$ (N2); an interior single-branch equilibrium; twice continuous differentiability of $\Delta^{\mathrm{act}}$ in $(k,\kappa,r)$; a non-vanishing **equilibrium** liquidity derivative (the equilibrium sensitivity $\mathcal S^{GE}$, distinguished from §4.4's fixed-policy $\mathcal S$); strict dominance $g_r^{PE} > \mathcal B_r^{GE}$ on the region; and the **threshold margin $r_\tau$ only** (the window coordinate is an integer — nothing local is claimed there): the fixed-policy attenuation sign survives in equilibrium on the region, $\partial_r\mathcal S^{GE} \le -\eta_r < 0$. The sign-coherence hypothesis is confirmed unused in the boxed conclusion. | **PROVED** (dominance-and-contraction implication; region-as-hypothesis) — **plus NUMERICAL node evidence**: 18 of 80 grid nodes are **pointwise dominance-and-contraction nodes** (largest contiguous block $T{=}5$, $\tau$-pct $\{50,70,90\}$, $\kappa\in\{0.65,0.75,0.85\}$; $\eta_r$ min 0.0595, median 0.3467; $L_{\mathcal R}\in[0.264,0.501]$ everywhere), by the executed committed check independently re-run 2026-08-22 (ALL REPRODUCE). These nodes verify the two pointwise inequalities and supporting diagnostics only; they do **not** verify the full C1 antecedent or a named nonempty region. The D8 $\varepsilon$-ball + integral-control pattern is the template for any future promotion. | proof `proofs/C1_proof.md` (repairs applied 2026-08-21, 13/13); **proof-read PASS 2026-08-21** `threads/2026-08-21_C1_proofread_audit.md` (0 FAIL); **re-derivation PASS 2026-08-21** (PROVED-WITH-CHANGES: N1, N2 added; H8 unused; bonus $\mathcal B_r^{GE} = O((1-L_{\mathcal R})^{-3})$ — dominance-and-contraction nodes are cubically bounded away from $L_{\mathcal R}=1$) `rederive/C1_rederivation.md`; check `quality_reports/fixes/t2_c1_region_check.py/.json` + re-run verify note. T1's PE-$\Omega$ hypothesis is exactly what fails in GE, so C1's remainder term is the object it bounds |

The old aspiration line ("C1 PROVED on a named nonempty region, NUMERICAL off-region") is
**retired as structurally undeliverable as worded** (the C1 proof-read's ruling): the deliverables
are the three objects the C1 row now carries — the implication PROVED with the region as a
hypothesis, the dominance-and-contraction nodes NUMERICAL, and a named-region promotion an open question with
the D8 ε-ball pattern as its template.

## 7. LABELS

- **PROVED** — a complete proof, independently re-derived and proof-read.
- **NUMERICAL** — verified on a grid by an executed, committed check script with committed output.
- **ESTIMATED** — an empirical estimate with a standard error and a stated design.
- **CONJECTURE** — everything else, including anything whose proof is deferred.

Dominance-and-contraction node is **not** a fifth label: it is pointwise numerical evidence for
$L_{\mathcal R}<1$ and $\eta_r>0$, with supporting diagnostics, not verification of the full C1
antecedent. A named-region promotion is not claimed. **Labels are never weakened by editing.** Only
an executed check or an independent re-derivation may move a label — never prose. Every move is logged as
`ID | old→new | evidence path | who | date | commit`, in
**`research/model_v4/LABEL_LEDGER.md`** (created 2026-08-21 with the seven ticket-27 moves).

## 8. Standing rules

1. The theorist cannot see the repo. Every input arrives pasted in the message.
2. Cite only IDs that appear in this card. No draft_v2 lemma numbers, no `\ref`, no citation the
   card does not carry.
3. **NOTATION DELTA is mandatory** in every answer: list every symbol used that is not in §4.
4. **Do not renumber or re-key any card symbol.** In particular: $\kappa$ is noise-trading
   intensity, never "liquidity depth"; bare $\lambda$ is D7's appropriability coefficient
   $1 - q(1-\gamma)\psi$ and is not available; $\psi$ is D7 pivotality; upright $T$ is the window and
   $\mathcal T$ is the best-response map.
5. State what you did **NOT** claim, in every answer.
6. Answer template, exactly these headings: `CLAIM` · `HYPOTHESES` (numbered, each used) · `PROOF`
   (numbered steps, each citing a hypothesis or an earlier step) · `WHERE IT FAILS` (≥2 concrete
   cases) · `LABEL CLAIMED` + why · `NUMERICAL CHECK REQUEST` (formula, grid, predicted sign *and*
   magnitude) · `NOTATION DELTA` · `NOT CLAIMED`.
7. No "clearly", "it follows", "standard", "obviously" in a proof step. Such a line is bounced with
   "show the step".

## 9. What the card does not claim

A global window-margin attenuation sign; $\kappa$-invariance of $J$; equilibrium uniqueness; a
nonempty GE region as a theorem; endogenous filing before the deadline; noisy or partially revealing
flagged-round trading; continuous-time execution; welfare or optimal rule design; that draft_v2's
hump result survives; that the prior calibration ($\Omega \approx 0.037$) is economically
meaningful; any empirical value for $\omega_a$.

**A7 satisfiability is no longer on this list** — it was never listed here, and it is now **resolved**
(§5's A7 note, ticket 24). Three items are **added** at this regeneration *(a fourth, item 4, added
2026-08-27)*:

1. **Whether the two-round pooled cell of §2 satisfies A($\tau$) — OPEN.** L3 proves the
   representation's entire remaining bite is the *support* condition, exhibits a one-round market
   that satisfies it and the frozen manuscript's own no-disclosure structure that does not, and
   declares the two-round case open with the weakest sufficient conditions named
   (`proofs/L3_proof.md` Part IV, Steps 16–18). **L3, L4 leg 3 and T1 Part B are all conditional on
   A($\tau$)**, so this is the largest single conditionality the ledger carries.
2. **Whether an equilibrium in which the blockholder chooses the fully separating plan exists on a
   given calibration — OPEN, and P1-adjacent.** A7′ menus are fully separating on the flagged set,
   so the burden did not disappear when ticket 24 resolved satisfiability; it **moved** to incentive
   compatibility, which P1 does not settle (`proofs/A7_attack_verdict.md`, sharpest new failure
   case; `proofs/P1_proof.md`; `rederive/P1_rederivation.md` NOT CLAIMED 3). Relatedly, P1 does not
   claim that an equilibrium satisfying A8 exists — only that A8 holding *at* an exhibited
   equilibrium puts both cells on path.
3. **O-1 is a disclosure-regime analogy, not a window-margin test.** This is a **known fact on file,
   not a claim the card makes**: O-1 compares the public buy flagged versus pooled at fixed policies
   in the static repo model. Its ratios $1.06397 / 1.18373 / 1.13631 / 0.37798$ at
   $\Omega = 0.037252 / 0.128950 / 0.285804 / 0.50$ are regime-comparison composition outcomes;
   they are not $W_TC_T$ and measure no window pair. The analogy is useful because it shows that a
   composition factor can exceed one, motivating T1's genuine window-margin iff. The genuine
   window-margin record is `t2_t1_check` block 4: $W_TC_T<1$ at every checked node at this
   calibration (with the $H=10$ corner caveat recorded in `HANDOFF_sign.md` §8.1). The O-1 cut
   $\Omega^\star \approx 0.343$ remains a disclosure-regime boundary, not a window boundary
   (`HANDOFF_sign.md` §3; `quality_reports/fixes/t1_o1_rerun_check.py`).
4. **Whether A6's continuity of $\mathcal T$ holds for the declared construction — ANSWERED IN
   SUBSTANCE 2026-08-27 (panel evidence; locus corrected; the open remainder is scoped below).**
   The re-derivation's withheld change 6 proposed filing this as OPEN at collapsed cutoff vectors.
   Ruled on Austin's 2026-08-27 authorization after a two-agent opposed-brief panel (substantiate
   vs defuse) with orchestrator adjudication — the briefs **converged on every load-bearing point**
   and **cross-replicated the decisive measurement** (the same three $\mathcal T_2$ jumps,
   independent scripts, 3 s.f. agreement). *Answered:* the discontinuity mechanism is real and
   reaches $\mathcal T$ with non-vanishing weight (the vanishing-mass defusal is refuted, twice
   independently); the locus is the **cell-edge hyperplanes $\cup$ sole-generator collapse faces**,
   not the collapsed vectors as such; the implemented menu's Hold-collapse face is measured clean,
   while A6 read with the $\Theta$ Steps 13–14 construct **fails at the implemented calibration**
   (measured $\mathcal T_2$ jumps $6.3\times10^{-3}$–$2.83\times10^{-2}$ at the baseline node, up
   to $0.16$ at $\kappa = 0.15$, against a $10^{-10}$ tolerance); and on $J \ge 3$ menus where a
   middle plan owns a reachable exclusive pooled history, **no $k$-independent perturbation family**
   restores continuity at more than one collapse-face point (continuum-face lemma; panel
   derivation, not gate-checked), so on that menu class P1 asserts nothing — the A($\tau$) pattern.
   *Still OPEN:* (a) whether a constructive $\Theta$ — or the Step 18 $t$-constrained Kakutani
   route already on file, which removes h.6's continuity half — replaces h.6 in the statement; the
   repair is identified, not executed; (b) the complementary menu class (every middle plan's
   histories shared with a survivor — the implemented menu is one such for its collapse face),
   where the collapse-face clause may be satisfiable; (c) nonexistence, which is neither claimed
   nor shown anywhere — $23/27$ sweep nodes converge and two fixed points survive even at the worst
   probed node. *Separately recorded, deliberately not folded in* (different hypothesis, different
   route): A3's own failure at this calibration and the candidate ticket-34 account — §5's A3
   evidence note. **No label moves on any of this**; P1's label rests on the proof and the two
   2026-08-25 passes and is untouched. Evidence: §5's A6 note;
   `threads/2026-08-27_A6_panel_substantiate.md` / `threads/2026-08-27_A6_panel_defuse.md`;
   `quality_reports/fixes/a6_panel_probes_2026-08-27/`. Follow-ups: the decisive-probe curation
   landed 2026-08-28 (§5's A6 note, curation note; the `t2_a6_*` checks); gate-check the
   continuum-face lemma only if it is ever promoted.
===== END research/model_v4/MODEL_CARD.md =====

---

## 4. LABEL LEDGER

Every label move in this lane, with the evidence that earned it and the standing notes governing
how one may be made. Both of P1's moves are here: the 2026-08-23 demotion on your finding, and the
2026-08-25 restoration on the repaired statement.

FILE: research/model_v4/LABEL_LEDGER.md (verbatim, complete)

===== BEGIN research/model_v4/LABEL_LEDGER.md =====
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

## Evidence note — independent re-run of every check script, 2026-08-22

All eight `t2_*` scripts (D1, L1, L2, L3, L4, T1, P1, C1-region) were re-run in full by a fresh
agent that wrote none of them: **ALL REPRODUCE** — every fresh JSON bit-identical to its committed
twin except wall-clock timing fields; zero numeric differences at any magnitude. One MISCITED
gloss corrected (the P1 failing-node description; the numbers were never wrong). Verdict:
`quality_reports/fixes/t2_rerun_verify_note.md`. The three substantive FAILs (L2's A(τ)-orientation
placebo, T1's chord-magnitude bridge, P1's four κ-extreme nodes) reproduce exactly and stand as
findings, not as errors.
===== END research/model_v4/LABEL_LEDGER.md =====

---

## 5. THE PRIMARY RECORDS OF THE CHANGES

Six files, verbatim and complete, in the order §2 tells them. They are the record §2 was written
from: where §2 summarises, these say it at full length and in the words of the agent who wrote it,
including the parts that do not flatter the stack. Two of them are adversarial reports whose
authors were briefed to break what they were reading, and one is a panel where the analyst briefed
to defuse a finding records that he could not.

- **5.1** `threads/2026-08-23_gpt_end_review_audit.md` — the audit of your own end review, finding
  by finding, with the demotion it produced.
- **5.2** `threads/2026-08-25_P1_proofread_retry.md` — pass 1 of P1's restoration: the adversarial
  proof-read of the repaired proof, PASS with 0 FAIL.
- **5.3** `rederive/P1_rederivation_2026-08-25.md` — pass 2: the statements-only re-derivation from
  the card row alone, PASS-WITH-CHANGES, with the withheld change 6 that became the A6 panel.
- **5.4** `threads/2026-08-27_A6_panel_substantiate.md` — A6 panel, the substantiate brief.
- **5.5** `threads/2026-08-27_A6_panel_defuse.md` — A6 panel, the defuse brief; verdict NARROWED.
- **5.6** `threads/2026-08-27_t4_sections_check.md` — the independent check of the §7 sections
  against the card, verdict LAND, plus the repair round and its delta pass.

---

### 5.1 The audit of your 2026-08-22 end review

FILE: research/model_v4/threads/2026-08-23_gpt_end_review_audit.md (verbatim, complete)

===== BEGIN research/model_v4/threads/2026-08-23_gpt_end_review_audit.md =====
# Audit of the GPT Pro end review — 2026-08-23

**Auditor:** Fable (session model), personally, per Austin's instruction 2026-08-23.
**Object:** `threads/2026-08-22_gpt_end_review.md` (courier copy, commit e46a071, SHA-256
`5e77bf246c915228ff2a0260cd0933bcbaf647e07a0d8a2ec1592207a8b25f8c`; source
`research/txt_extracts/gpt_pro`, Austin's drop 2026-08-22 22:32).
**Rules in force:** the review may demote, never promote (`LABEL_LEDGER.md` standing note 2).
This audit verifies each finding against the primary record before any label moves. **No label,
card, or handoff edit is made by this audit** — the stop-and-wait rule holds; the repair queue
below awaits Austin's approval.

## Scorecard

All eight findings verified against the record. **8/8 UPHELD** (three in narrowed form).
One label consequence: **P1 PROVED → CONJECTURE** (pending approval). No other label moves.

| # | GPT finding | Verdict | Consequence |
|---|---|---|---|
| 1 | P1's recorded theorem is not established by its cited proof | **UPHELD** | **P1 → CONJECTURE**; bounded repair path identified |
| 2 | L2's placebo predicts a sign A(τ) does not imply | **UPHELD** | none on L2; FAIL reclassified "misformulated test" |
| 3 | T1's chord check tests Example-A's calibration, not A(τ) | **UPHELD** (MISCITED) | none on T1; A(τ) applicability → OPEN; decisive check queued |
| 4 | O-1 is not a window-margin refutation | **UPHELD** | card §9 item 3 withdrawn; propagations listed below |
| 5 | P1's four failing nodes are unresolved, not refuting | **UPHELD** (UNCHECKED) | 30-seed re-run queued |
| 6 | "18 certified nodes" over-cited | **UPHELD** (naming) | rename; labels unchanged |
| 7 | Card's A7′ gloss carries two false consequences | **UPHELD** | wording repair; no label attaches |
| 8 | Card is a mixed pre-/post-C1 snapshot | **UPHELD** | regenerate card; amend ledger standing note |

---

## Finding 1 — P1 demotion. UPHELD on three independent grounds plus one citation nit.

**(a) Hypothesis-form mismatch; the two-pass gate was never satisfied for the recorded row.**
The proof's h.7 is the **joint** injective form — "$(j,s)\mapsto(B_j^F,Q_j^F,a_j)$ is injective
on the flagged set" (`proofs/P1_proof.md:55-57`) — and Step 10 consumes exactly that ("each
flagged tuple in its image is generated by exactly one pair $(j,s)$", `:309-313`). The card row
records the weaker **on-path** form ("A7′ (on-path injective)", `MODEL_CARD.md:314`), as does the
re-derivation (`rederive/P1_rederivation.md:27` and H6 at `:58`). So the proof-read pass covered a
joint-form theorem and the re-derivation covered an on-path-form theorem: **two passes over two
different statements**. Under the row's on-path form, Step 10 fails outright — on-path A7′ can
hold while the joint map collides (the 40-collision witness, `proofs/A7_attack_verdict.md` C-iii-c),
so the plan-tremble posterior is not pinned at collision tuples. GPT's reading is confirmed.

**(b) Step 12's cost gap.** Step 12 (`P1_proof.md:350-360`) equates "round-2 order $Q'$ strictly
improves the flagged continuation" with "the first bracket is strictly larger at $j'$", where the
first bracket (`:343`) includes $-C_{j'}(s)$ — plan $j'$'s **own** engagement cost. A round-2
deviator has already sunk $C_j(s)$; the deviation's continuation holds $C_j$ fixed. The two notions
coincide only if $C_{j'}(s)=C_j(s)$ on the deviation set, a clause no hypothesis supplies. GPT's
0.01-vs-0.99 example is arithmetically correct. The gap is vacuous for single-Voice menus (h.11's
deviation set is a singleton — $a_{j'}=a_j$ excludes Exit/Hold) but live for any admissible menu
with two Voice plans sharing a pooled path, and the row quantifies over general finite menus.

**(c) The κ=1 tremble gap.** Step 9 asserts "every noise mark carries positive probability
whenever $\kappa>0$" (`:302-303`). Under card §4.1's noise law ($\Pr(z_d=0)=1-\kappa$,
`MODEL_CARD.md:68`) this is **false at $\kappa=1$**, which is in-domain ($\kappa\in[0,1]$, `:67`).
The proof special-cases $\kappa=0$ and never $\kappa=1$; a pooled history requiring a zero noise
mark has probability zero under every plan profile there, so the plan-only perturbation leaves its
limit belief undefined. Patch: mirror the $\kappa=0$ sentence at $\kappa=1$ (the reachable-alphabet
argument) or restrict to $\kappa\in[0,1)$.

**(nit)** Card `:107` defines $U_j$ with $-a_jC_j(s)$ and says the definition "is
`proofs/P1_proof.md` h.14 (displayed there in full)"; h.14 (`:94`) displays $-C_j(s)$. MISCITED-class:
harmless if $C_j\equiv0$ for $a_j=0$ plans, but that is nowhere stated either.

**Not disturbed:** the inner pricing fixed point under $m_0\ge0$, the Brouwer outer argument, the
A5 derivation, and the **pinned pro-rata single-Voice menu instance** — post-repair it satisfies the
joint form (`MODEL_CARD.md:200-202`), its deviation set is a singleton, and every numerical node
sits at interior κ. The gaps kill the recorded generality, not the paper's instance.

**Repair path (bounded):** (i) state the row under the joint form the proof already uses; (ii) add a
one-line continuation-cost clause (menu elements sharing a pooled path and engagement status share
the engagement cost — trivially true on the pinned menu) or restate round-2 optimality against the
sunk-cost continuation; (iii) the κ=1 patch; (iv) fix the objective-display citation. Then a fresh
two-pass on the amended statement. Until then: CONJECTURE.

## Finding 2 — L2 placebo. UPHELD.

`t2_l2_check.py:296-345`: the check demands $\partial_\kappa M_P\le0$ "under A(tau)'s maintained
C_h(pi_bar) <= 0". The identity $\partial_\kappa M_P=\Delta_m A'_\kappa C_h(\bar\pi)$ holds under
A(τ)+(br-ii) (`T1_proof.md` Step 8), and **$A'_\kappa$ carries no sign** — the card requires it
bounded only (`MODEL_CARD.md:121`); A(τ)'s orientation clause signs $C_h$, not $A'_\kappa$. The
card's own witness Example A has $A_0=A_1=(2-\kappa)/4$, so $A'_\kappa=-1/4$ (`L3_proof.md:570`),
predicting the **opposite** sign. The hump-shaped $M_P$ is therefore compatible with A(τ) plus a
sign-changing $A'_\kappa$; the FAIL carries no information about A(τ). L2's own invariance checks
(exact-zero ranges) are untouched; L2 stays PROVED.

## Finding 3 — T1 chord check. UPHELD as MISCITED.

`t2_t1_check.py:79` hard-codes `A_PRIME_KAPPA = 0.25` (Example A's witness value) and `:335`
imposes level symmetry (`pi_bar_level_symmetric = 2.0 * pi_bar`). Neither is part of A(τ). The
0.628 pp residual refutes **that witness calibration** of the bridge, not A(τ). HANDOFF §8.3's own
numbers cut the other way: implied $|A'_\kappa|\in[0.997,1.158]$ (near-constant) with chord shape
stable to 0.48% — *consistent with* a genuine three-point representation at $|A'_\kappa|\approx1.07$.
T1 stays PROVED under its named hypotheses. A(τ) at the implemented cell is **OPEN** — which the
card's A(τ) block already states ("Whether the two-round pooled cell of §2 satisfies the support
condition is OPEN"); HANDOFF §8.3 and `model_v4.md` §6 fact 2 overstate ("fails … in two
independent places") and are corrected in the repair batch. The decisive test is cheap and queued:
enumerate the pooled posterior support directly and recover the weights (GPT's check request 1–3).

## Finding 4 — O-1. UPHELD.

O-1 is a **same-policy information-regime toggle**: flagged (market sees $(X,D)$) vs pooled (sees
$X$ only) at fixed cutoffs, four $k_D$ values, no window pair (`HANDOFF_sign.md` §2). T1's own
Step 16 remark (ii) says so ("the O-1 experiment toggles a flag", `T1_proof.md:512`). Yet the
record labels its ratios as $W_TC_T$ and as a window-margin refutation in four places:
`MODEL_CARD.md:379-383` (§9 item 3, "REFUTED at the O-1 calibration"), `model_v4.md:367-376`,
`:438`, `:460`, `HANDOFF_sign.md` §7 ("the live failure case that iff has to accommodate"), and —
cross-lane — `blockholder_v4/research/empirics_v4/SPEC.md:366-371` ("window-margin attenuation
claim is false at baseline"). All withdrawn/rewritten as analogy: O-1 shows a composition factor
can exceed one in a **regime** comparison, which motivates T1's iff; it measures no window.
The genuine T-pair measurement already exists and passes: `t2_t1_check` block 4
($W_T=(1-\Omega(\tau,5))/(1-\Omega(\tau,10))$, forced-attenuation audit with teeth) — $W_TC_T<1$
at **every checked node** at this calibration (HANDOFF §8). ADR-0007 and the pre-registered SPEC
carry the same mislabel; handling those is Austin's decision (this lane does not edit `docs/adr/`
or the SPEC).

## Finding 5 — P1's four nodes. UPHELD as UNCHECKED.

`t2_p1_check.py:104-105`: `N_SEEDS = 30` applies to node set A only; the sweep (node set B, where
all four failures live) ran `N_SEEDS_SWEEP = 5` with early stopping. The design asked 30 for the
P1 grid (`impl_design.md:25,138,320`). Status at the four nodes ($\kappa\in\{0.15,0.85\}$,
$\tau\in\{0.05,0.075\}$, $T\in\{5,1\}$): cutoff residual $\sim10^{-11}$, payoff residual
$3.1\times10^{-4}$–$1.5\times10^{-3}$ after 5 seeds — **neither existence nor nonexistence**, and
A3/A6 were not verified there. Re-run queued: exactly those four nodes × 30 seeds, reporting the
cutoff residual and the maximum profitable plan deviation.

## Finding 6 — C1 naming. UPHELD, narrow.

`t2_c1_region_check.py:452`: `certified = contract and eta > 0` — two inequalities (plus
diagnostics), not the full antecedent (C² smoothness, relative openness, interior single branch,
non-vanishing $\mathcal S^{GE}$). Rename at `MODEL_CARD.md:123`, `:138`, `:316` and
`LABEL_LEDGER.md:47`: "18 **pointwise dominance-and-contraction nodes** (supporting diagnostics;
not a verification of the full C1 antecedent)". The review endorses the three-way split itself
("doing real epistemic work"). Labels unchanged.

## Finding 7 — A7′ gloss. UPHELD.

Two false consequences confirmed in the card: (i) `:80` "for a menu this amounts to each $b_j^*$
strictly increasing" — over-broad; passive plans never flag, and the qualifying pro-rata menu has
Hold constant and Exit weakly decreasing. Correct form: strictness for **flag-capable composed
targets**, no backtracking across admissible Voice-plan switches. (ii) `:196-197` "Injectivity …
forces $B^F$ continuum-valued" — the tuple, not the coordinate; our own attack verdict flagged
precisely this (`A7_attack_verdict.md` S-10: "the true statement is 'forces $(B^F,Q^F)$
continuum-valued'") and the card note was never amended — a propagation miss in the batch.
`P1_proof.md:57` repeats it (folded into the P1 repair). Wording repairs only; L2 unaffected (its
proof uses the full tuple).

## Finding 8 — card snapshot. UPHELD.

`MODEL_CARD.md:3` (stamp 627642c, 2026-08-21) and `:7` ("all seven") vs `:297` ("All eight now
carry two-pass evidence … C1's moved 2026-08-22") vs `:301-302` ("C1 is untouched and stays
CONJECTURE") vs the C1 row PROVED at `:316`; the ledger's operative commit is 403ac8e. Also
`LABEL_LEDGER.md:15-16`'s standing note ("C1 is pending … does not appear below") contradicts its
own line 47. Cause: the C1 close-out patched the row and the first sentence but missed the middle
sentences and the ledger note (orchestrator error, this lane). Repair: regenerate the card with a
fresh stamp and one consistent C1 status; amend the ledger standing note. No label content is
affected — every underlying artifact is dated and internally consistent.

---

## Corrected narrative after this audit

1. **Two-round stack:** D1, L1, L2, L3, L4 PROVED; T1 PROVED at fixed policies (conditional as
   stated); C1 certificate implication PROVED + 18 pointwise nodes NUMERICAL (narrowly named);
   **P1 → CONJECTURE** pending a bounded repair. The paper's pinned menu instance is untouched by
   every P1 gap.
2. **A(τ) at the implemented pooled cell: OPEN**, previously misreported as failing. Both recorded
   "failures" were test-design artifacts; the near-constant implied coefficient is weak evidence
   *for* a representation at $|A'_\kappa|\approx1.07$. The support-enumeration check decides it.
3. **Window margin:** the only genuine measurement on file is two-round block 4 — attenuation
   ($W_TC_T<1$) at every checked node at this calibration. O-1 never measured the window.
4. All numerical reproductions (ALL REPRODUCE, 2026-08-22) stand; the review disputed none.

## Repair queue — pending Austin's approval, in order

1. **Demotion + wording batch** (ledger P1 move; card regeneration fixing findings 4, 6, 7, 8 and
   the P1 row; ledger standing-note amendment; HANDOFF §7/§8.3 rewrite; `model_v4` .md/.tex/.pdf
   regeneration; session log + memory).
2. **Two executed checks:** `t2_atau_support_check` (enumerate pooled posterior support; recover
   weights; test the derivative pattern and the identity with the recovered coefficient) and
   `t2_p1_fournode_recheck` (4 nodes × 30 seeds + max profitable deviation).
3. **P1 repair ticket** (amended statement per Finding 1's repair path; fresh writer + adversarial
   proof-read + fresh statements-only re-derivation; only then may P1 return to PROVED).
4. **Cross-lane flags for Austin:** E2 SPEC's "Note on the O-1 history" and ADR-0007 inherit the
   Finding-4 mislabel; corrigendum handling is Austin's call.
5. Ticket 08 (draft_v3 model/theorem sections) unblocks after items 1–2; whether it waits for
   item 3 is Austin's call (recommended: run item 3 first — existence is load-bearing).
===== END research/model_v4/threads/2026-08-23_gpt_end_review_audit.md =====

---

### 5.2 P1 restoration, pass 1 — adversarial proof-read

FILE: research/model_v4/threads/2026-08-25_P1_proofread_retry.md (verbatim, complete)

===== BEGIN research/model_v4/threads/2026-08-25_P1_proofread_retry.md =====
# Ticket 35 — Pass 1 (adversarial proof-read), retry verdict — 2026-08-25

Courier note (orchestrator): verbatim record of the proof-reader's single-retry verdict on the
round-2 repaired proof (HEAD `5394ed6` at read time). The same agent's round-1 FAIL findings are
filed at `threads/2026-08-25_P1_proofread_round1.md`; the round-2 repair traces to that file plus
`rederive/P1_rederivation_2026-08-25.md` under the orchestrator adjudication logged in
`quality_reports/session_logs/2026-08-25_post-review-repairs.md`.

---

Re-verified the amended file end to end against the amended row. I attacked the new Step 12 lemma on the merits first.

## Verification of the new Step 12 lemma (brief item (a))

I checked the four parts independently rather than accepting the write-up.

- **(a) price invariance** (`P1_proof.md:645-653`): holds. By Step 10 the belief at $\sigma_F(j',s)$ is the point mass at $(j',s)$, so $\hat v=\mu_v+\beta(s-\mu_v)$ carries no $j'$; $\pi\equiv1$ on the flagged cell gives $\bar m=m_1$; Step 4 makes the inner map a function of $(\hat v,\pi)$ only; Step 7 makes the root unique. So $P^F(\sigma_F(j',s))=\mathcal G_F(\hat v(s))$ for the whole class. It also survives the richer §4.3 fill $(\mathcal H^P_{f^-},F,Q^F)$, since $\sigma_F$ already pins $s$ and the pooled residual is $z$-measurable — so P1 does not need L2 here.
- **(b) $\mathbb E[Y\mid\cdot]=P^F(s)$** (`:655-667`): holds. $\mathcal H^P$ is $z$-measurable given the shared path and $z\perp(v,\varepsilon,\xi)$, so it drops; $\mathsf B$ is a function of $\xi$ alone given the $\sigma_F$-measurable $P^F$; the resulting $(1-p)(\mathbb E[v\mid s]+\Delta_V)+p(P^F+m_1)$ is literally $\mathcal P_{\mathcal I}(P^F(s))$ **because A7-J makes the market's posterior mean the blockholder's own**, and that equals $P^F(s)$ by the fixed-point equation. Not circular — it is the defining equation.
- **(c) cancellation** (`:669-680`): holds exactly. $b^*_{j'}=B^F_j+Q^F_{j'}$ (using $B^F_{j'}=B^F_j$ from the shared path), so $V(j')=(B^F_j+Q^F_{j'})P^F-P^FQ^F_{j'}-\text{cost}=B^F_jP^F-\text{cost}$. Every $Q^F_{j'}$ and every $b^*_{j'}$ is gone.
- **(d) h.16** (`:682-692`): holds. Under the sunk convention $V$ is constant with no clause; under plan-completion h.16 makes it constant. Every element of $\mathcal Q_j(s)$ ties, so the specified order is optimal at **every** flagged pair, with no appeal to date-0 optimality. §3(ii)'s flagged half is discharged at the non-selected nodes too.

**My pass-1 finding-1 witness is refuted, and the refutation note (`:704-715`) is correct on the merits, not merely asserted.** I tried to rebuild it and cannot: I was treating $G_{j'}$ as a free primitive, but (a)+(b) force $G_{j'}=B^F_j(s)P^F(s)$ for every class member, so $\delta\equiv0$. Any variant putting the wedge in the trading terms requires either a flagged price that is not the inner fixed point or a flagged belief other than the one A7-J pins — i.e. it must break §3(iv) or §3(vi), which are in force. The only surviving wedge is the engagement cost, which is exactly where WHERE IT FAILS 7 now puts it. The strengthened row clause ("at every flagged pair, whether or not the cutoff vector selects it") is genuinely proved.

## Findings

**1. REPAIR — `P1_proof.md:754-756` (Step 13) and `:854-855` (Step 17(i)): the newly named tie-break's monotonicity does not follow from h.3 as the same sentence reads h.3. Introduced by P1-R23.** Line 753 reads h.3 as "there is a weakly increasing selection $j^\star$ from $\arg\max$"; line 755 then names $j^\star(s;k):=\max\arg\max_j U_j(s;k)$ and asserts it "is weakly increasing in $s$ under h.3". That is a non sequitur under the file's own reading. Counterexample inside h.3: let $U_2-U_1\le0$ everywhere with equality at exactly one point $s_0$ (a tangential touch, not a crossing — zero crossings, so h.3's first clause holds; the constant selection $j\equiv1$ is weakly increasing, so its second clause holds under the reading line 753 uses). Then $\max\arg\max$ is $1,\dots,1,2,1,\dots,1$ — not weakly increasing, $\{s:j^\star\ge2\}=\{s_0\}$ is not an up-set, and $j^\star$ is **not representable by any cutoff vector**, so Step 17(i)'s "weakly increasing and is represented by $k^\star$" fails and with it §3(i)/(ii) at the fixed point. Brouwer itself is untouched ($\mathcal T\in\Theta$ needs only the nesting at `:763`). Determinate fix, using nothing new: take $j^\star$ to be the **largest weakly increasing selection** — the set of weakly increasing selections is nonempty by h.3, closed under pointwise max (the max of two selections is a selection since $\arg\max(s)$ is a set, and the pointwise max of two weakly increasing maps is weakly increasing), and with $\mathcal J$ finite the pointwise supremum is attained and is itself a weakly increasing selection. That is canonical, single-valued (which is what pass-2 N8 needs before h.6 can call $\mathcal T$ continuous), and monotone.

**2. REPAIR — `P1_proof.md:623-625` (Step 11) is stale against the repaired Step 9(c).** It still reads "By Step 9(c) every pooled history the second bracket weighs is reachable, so the prices it reads are the ones Steps 5 and 9 supply." Step 9(c) as rewritten by P1-R22 (`:536-539`, `:541-555`) says this holds for $\Phi_s$-**almost every** $s$, and that at the exceptional signals the bracket reads the *conventional* price, not one Steps 5 and 9 supply. Neighbour not updated by the patch. Fix: insert the a.e. qualifier and point the exceptional case at 9(c)'s convention, as Step 13 (`:750-751`) already does correctly.

**3. REPAIR — `P1_proof.md:546-548` (Step 9(c)'s convention) vs the row's unqualified "prices at their inner fixed points" (`MODEL_CARD.md:324`).** The adopted convention is $P^P_d(\mathcal H^P_d):=\mathbb E[Y]$ at unreachable pooled histories, and $\mathbb E[Y]$ — the unconditional average over realised control-node values — is in general **not** a root of $\mathcal P_{\mathcal I}$ for any belief. The constructed object therefore carries prices that are not inner fixed points at nodes where the blockholder does trade (the exceptional signals of finding 6/P1-R22), while the row's conclusion clause is unqualified. Free fix that removes the mismatch entirely: set the convention to the inner root at a fixed reference belief (e.g. the prior $(\hat v,\pi)=(\mu_v,\Pr(a{=}1))$), which exists and is unique by Step 7. The §4.3 $P^P_{-1}:=\mathbb E[Y]$ precedent cited at `:547` is a different node (pre-trading) and does not carry the fixed-point property across.

**4. OBSERVATION — `P1_proof.md:520-524` (Step 9(b)): the dominated-convergence envelope needs the case split it does not state.** As written the justification is "dominated by an integrable envelope under h.17-d's Gaussian tail and h.2's integrability", but $\mu_n\le\varphi_s L_j/Z_n$ with $Z_n\downarrow0$ at a $k$-null history is not a uniform envelope. The conclusion is right on a split: if $Z_0>0$ (history on-path under $k$) then $Z_n\ge Z_0/2$ eventually and $2\varphi_s/Z_0$ works; if $Z_0=0$ then the $(1-Jt)$ terms vanish identically and $\mu_n=L_j\varphi_s/\Lambda_u$ is exactly $n$-free — which is pass-2's own R9(b). One sentence.

**5. OBSERVATION — the cancellation makes Step 15(ii) fail identically on exactly the menus h.16 is for.** By Step 12(c), $U_{j'}(s;k)=B^F_j(s)P^F(s)-C_j(s)-E_j(s;k)$ is the *same function of $s$* for every member of a deviation class (shared path ⇒ common $B^F$ and $E$; h.16 ⇒ common $C$). So on any multi-Voice menu with two adjacent class members, $U_{i+1}-U_i\equiv0$ on the whole flagged region and Step 15(ii)'s transversality fails identically, not exceptionally. WHERE IT FAILS 3 still presents plateaus as an exotic case ("let the engagement cost be constant on an interval"); after R17 they are structural precisely where h.16 is live. Non-blocking — h.6 assumes continuity of $\mathcal T$ outright and the largest-selection tie-break covers the plateau — but the file should say that h.6 is now being assumed at the configuration where its own named sufficient condition provably fails.

**6. OBSERVATION — h.16 is convention-conditional, and the row does not say so.** Step 12(d) (`:686-687`) and h.16's "why" note (`:214-215`) both state that under the sunk convention $V$ is constant with **no clause at all**, so h.16 is consumed only under plan-completion. The row lists h.16 unconditionally and glosses it "without this clause the deviator takes the class member with the smallest cost and item (ii) of §3 fails at that node" — true only under (α). The row's $U_j$ timing parenthetical permits either convention. Card §8 rule 6 ("each hypothesis used") is satisfied on the (α) reading only. One clause on the row.

**7. OBSERVATION — NOTATION DELTA gaps (card §8 rule 3).** $j^\star(\cdot;k)$ appears 19 times and is now the equilibrium plan map (`:853-854`), and $\mathcal Q_j(s)$ carries h.11; neither is declared. Both pre-date round 2, but R23 promoted $j^\star$ from an internal selection to a named object in the conclusion's assembly.

## The other four re-verification items

**(b) REPAIRs 2–9 and OBSERVATIONs 11–12, whole-proof sweep.** All implemented as named, and I checked the neighbours rather than the patch sites alone. h.2 → A2′ (`:77-88`), with the *Used* list corrected to Steps 3, 9, 13 and Step 13's "finite and bounded" reworded to what A2′ supplies (`:750-752`). h.5 struck (`:95-110`) with the slot preserved; Step 5(a), Step 6(b) re-cited to Steps 7–8, Step 15 marked commentary, Step 7's heading and closing paragraph and WHERE IT FAILS 1's title all updated — a grep confirms no live A5 citation survives anywhere. Step 9(b) rebuilt on the joint $\mu_n(j,s)$ with $\hat v$ obtained by dominated convergence (finding 4 above is the only residue). Step 10's version statement (`:573-586`) is correct and Step 6(d) correctly keeps its stronger "pinned" for the *price* family given the belief (`:423-424`). Step 2's Borel justification now cites h.17-b (`:288-294`). h.10 gains clause (ii) and Step 11 and Step 12(c) cite it (`:137-149`, `:608-610`, `:669`). CLAIM's sweep corrected; Step 17(iv) now reaches reachable $k$-null histories at Step 9(b)'s limit belief (`:881-885`). WHERE IT FAILS 2 now names the off-image extension it needs instead of assuming a schedule into existence; WHERE IT FAILS 7 is correctly rebuilt with the wedge in the cost and the "$j$ non-selected" restriction stated; NUMERICAL CHECK 4's first half is correctly reclassified from prediction to derivation. Findings 1–3 above are the only breaks I found, and finding 1 is the only one a patch created.

**(c) Proof↔row hypothesis match, both directions.** Clean now, which is the defect class that caused the demotion. Row → proof: A1=h.1, A2′=h.2, A3=h.3, A4=h.4, A6=h.6 (with the tie-break-and-corner reading, Step 16 `:842-846`), A7-J=h.7, D1-with-hypotheses-travelling=h.9, §2 timing with flag-terminates=h.10(i)+(ii), action-set=h.11, continuation-cost=h.16, $m_0\ge0$=h.12, $U_j$=h.14, §4.1–§4.3 table restrictions=h.17(a–d), A8=h.8 (addendum only), H-ord + upper-set=h.13, h.15. Proof → row: no hypothesis consumed that the row does not list; A5 is gone in fact and not merely in name. The one construction element not on the row — Step 9(c)'s price convention — is a specification at nodes §3 does not constrain, not a hypothesis, and NOT CLAIMED 13 owns it (finding 3 is about its interaction with the conclusion's wording, not about it being unlisted).

**(d) Row folds vs pass-2 changes 1–5.** Faithful, all five. Change 1's §4.1–§4.3 block is transcribed item for item and matches h.17-a…d. Change 2's "D1 by statement with its own hypotheses travelling" plus the three-part A5 sentence (existence/uniqueness from $m_0\ge0$, continuity from the same scalar reduction, measurable selection from A7-J plus the Borel clause) is present and matches Steps 6(c)–(d), 7, 8. Change 3's one-family/every-$k\in\Theta$/positive-probability clause is present with N6's reason spelled out. Change 4's A6 reading is present with $\Theta$ nonempty per §4.5, matching Steps 13/16. Change 5's $C_j$ timing convention sits inside the row's own $U_j$ parenthetical. Change 6 is correctly absent, and the proof's R27 row records that it was withheld deliberately. One divergence worth naming, non-blocking: the row says A5's continuity content comes "from the same scalar reduction", while the file derives it from Step 8's implicit-function argument — a different route (pass-2's was IFT-free and 1-Lipschitz) but a valid one, since $\varrho$ is $C^1$ jointly and $\partial_P\varrho<0$ strictly at every root.

**(e) Repair table P1-R17…R27.** Every entry describes an edit actually present; I verified each against its cited line range, including the unnumbered P1-R24b. No weakening anywhere: the two conclusion clauses that moved — flagged beliefs from "pinned, not chosen" to the version formulation (R21), and reachability gaining "with positive probability" (R22/N7) — are both documented and both are repairs of overstatements, and the row's new "at every flagged pair" strengthening is proved by the lemma above. The round-1 ordering nit (R16 filed between R12 and R13) is fixed and annotated.

**Overall verdict: PASS (0 FAIL)** — 3 REPAIRs and 4 OBSERVATIONs, of which finding 1 (the largest-maximiser tie-break) is the only one touching a conclusion clause and has a one-line in-file fix.
===== END research/model_v4/threads/2026-08-25_P1_proofread_retry.md =====

---

### 5.3 P1 restoration, pass 2 — statements-only re-derivation

FILE: research/model_v4/rederive/P1_rederivation_2026-08-25.md (verbatim, complete)

===== BEGIN research/model_v4/rederive/P1_rederivation_2026-08-25.md =====
# Ticket 35 — Pass 2 (statements-only re-derivation) result, verbatim — 2026-08-25

Input was the card alone (stamp 2026-08-23 · `d2ccf62`) plus `CONTEXT.md`. No proof, no re-derivation file, no thread, no check script was opened.

Notation (proof-local to pass 2): `e_ℐ(·)` inner pricing excess function; `Ψ` the flagged-pair map `(j,s) ↦ (B^F_j, Q^F_j, a_j)`; `Λ_k(h)`, `Λ_u(h)` unnormalised pooled-history likelihood aggregates; `𝒪_j(s)` the pooled-execution component of `𝒞^trade_j`; `ν` the marginal law of `s`; `t ∈ (0,1)` the tremble weight; `𝒜(j,s)` the round-2 action set; `s_D` the A8 signal threshold.

## (1) Derivation skeleton

**R1. There are exactly two blockholder nodes.** §2 no-feedback ⇒ round 1 contains no decision node after date 0. A4 ⇒ the disclosure node is Nature's. So §3(ii) reduces to two checks. [§2 no-feedback; A4]

**R2. Unfolding the round-2 action set.** The definitional hypothesis gives `𝒜(j,s) = {Q^F_{j'}(s) : j' agrees with j on everything already played}` i.e. `B_{j'}(s,d) = B_j(s,d)` for all `d ≤ f_j(s)`. Then (a) `c_{j'} = c_j`; (b) `f_{j'} = f_j ≤ H`; (c) `B^F_{j'} = B^F_j`; (d) any `j'` whose `Q^F` exists has `D_{j'}=1`, hence `a_{j'}=1`. Every admissible deviation leaves `(j',s)` in the flagged-pair set and produces the tuple `Ψ(j',s)`, differing from `Ψ(j,s)` only in the `Q^F` coordinate. [round-2 action-set hypothesis; §4.2; A4]

**R3.** The closure reading would need `𝒜` an interval of orders, hence `J = ∞`, contradicting A2′. The definitional reading is forced. [A2′]

**R4. Reduction to a scalar equation.** At a control node with belief `μ`, put `ȳ(ℐ) = E_μ[v] + πΔ_V`, `m̄(ℐ) = m₀ + πΔ_m`. From §4.3's `Y` row and entry rule, with `ξ ⊥ (v,ε,z)` [A1] and `P,π` ℐ-measurable: `P = E[Y|ℐ]` becomes `e_ℐ(P) := ȳ + m̄·p(P)/(1−p(P)) − P = 0`. [§4.3 `Y` row AND the price convention `P(ℐ)=E[Y|ℐ]` — NOT on P1's row list (Finding N1); §4.3 entry rule; A1]

**R5. Existence and uniqueness.** `σ_ξ > 0` ⇒ `p(·) ∈ (0,1)` smooth strictly decreasing; `m₀ ≥ 0`, `π ∈ [0,1]`, `Δ_m > 0` ⇒ `m̄ ≥ 0` ⇒ `e_ℐ` strictly decreasing with slope ≤ −1. IVT + strict decrease ⇒ exactly one root `P*(ȳ,m̄;ϑ)`. This is A5's existence-and-uniqueness content, derived. [m₀ ≥ 0; A1; `Δ_m>0`; entry rule]

**R6. Continuity, without any IFT.** `|P*(ȳ) − P*(ȳ')| ≤ |ȳ−ȳ'|` (1-Lipschitz); joint continuity of `e` + strict decrease ⇒ `P*` jointly continuous in `(ȳ,m̄,ϑ)`. No differentiability, no non-vanishing derivative assumed. This is A5's retained continuity clause, derived.

**R7. Price integrability and the tower.** `P*` 1-Lipschitz in `ȳ`, `ȳ` affine in `E_μ[v]`, `v` Gaussian ⇒ every control-node price integrable. `P^P_d = E[P*(control node)|H^P_d]` tower with no self-reference; `P^P_{−1} := E[Y]` covers `c=0`. [§4.1 Gaussian — NOT on the row (N3); A2′ integrability]

**R8. The pooled likelihood factorises.** `Pr(h|j,s) = 1{flag consistent}·Π_d Pr(z_d = X_d − q_{jd}(s))`, ternary point masses, bounded by 1, Borel in `s` by §4.2's Borel clause (N2); `z ⊥ (v,ε,ξ)`. Pooled alphabet finite. [§2; A1; A2′; D1; §4.2 Borel clause]

**R9. One perturbation family, used at every `k ∈ Θ`.** Mix `j_k(s)` w.p. `1−t`, uniform over `𝒥` w.p. `t`. With `Λ_k`, `Λ_u`: (a) `Λ_k(h) > 0`: Bayes ⇒ §3(iii). (b) `Λ_k(h) = 0 < Λ_u(h)`: `μ_t = Λ_u(h;·)/Λ_u(h)` for every `t` — exact limit ⇒ §3(vi). (c) `Λ_u(h) = 0`: null under every profile; no §3(vi) requirement; read by no step.

**R10. Boundary `κ`.** At `κ=0` support `{0}`, at `κ=1` `{±z̄}`. A history needing a mark outside the live alphabet has `Λ_u(h)=0` ⇒ case (c). Reproduces the row's boundary-κ reading independently; confirms the pre-repair κ=1 claim was false.

**R11. Off-path prices are finite.** In R9(b), `μ ≪ ν` with density ≤ `1/Λ_u(h)` ⇒ `E_μ[v]` finite ⇒ R5–R6 apply at every reachable pooled history.

**R12. `Ψ` is Borel.** From §4.2's rows + Borel clause; finite `H`; A4.

**R13. Flagged beliefs pinned pointwise — and only A7-J does it.** Borel + injective between standard Borel spaces ⇒ image Borel and `Ψ⁻¹` Borel. At every image tuple the belief is the point mass at `Ψ⁻¹(t)`: pointwise; a version of every regular conditional; invariant to `t`; simultaneously on-path Bayes and off-path limit. A7′ cannot do this — on-path only, and R2's deviation tuples are generated by pairs the cutoff vector need not select. [A7-J; R12]

**R14.** By R2 every admissible round-2 order produces `Ψ(j',s)` flagged ⇒ no tuple outside the image ever arises.

**R15. P1 does not need L2.** (§4.3's two fills of `ℐ_H` equivalent here as a corollary.)

**R16. Lemma: the flagged price equals the deviator's own valuation.** At a flagged node the belief is the point mass at `(j',s)` and `π = 1`, so `ȳ = μ_v + β(s−μ_v) + Δ_V` and `m̄ = m₁` — both independent of `j'`. Hence `P^F(Ψ(j',s)) = P*(ȳ(s), m₁) =: P^F(s)`, the same for every `j' ∈ 𝒜(j,s)`: the round-2 order has no price impact across the menu. And the blockholder's extra information (realised pooled flow) is `z`-measurable given `(j,s)`, independent of `(v,ξ)`; so `E[Y | s, j, H^P] = E[Y | s] = (1−p)(E[v|s] + Δ_V) + p(P^F + m₁) = P^F(s)` — the fixed-point equation itself. [A7-J; A1; §2 no-feedback; §4.3 `Y` row + entry rule; m₀≥0; §4.1]

**R17. Indifference — and exactly where h.16 bites.** Flag-terminates ⇒ `b*_j = B^F_j + Q^F_j` is the whole residual; `𝒞^trade` splits into `𝒪_j(s)` (sunk, common across `𝒜`) plus `Q^F·P^F`. For `j' ∈ 𝒜(j,s)`: `V(j') = E[(B^F_j + Q^F_{j'})Y | s] − Q^F_{j'}P^F(s) − C_{j'}(s) = B^F_j(s)P^F(s) − C_{j'}(s)`. h.16 (antecedent `a_{j'}=a_j` automatic by R2(d)) ⇒ `C_{j'} = C_j` ⇒ `V` constant on `𝒜`. Every element, in particular `Q^F_j(s)`, is sequentially optimal ⇒ §3(ii)'s flagged half — at EVERY flagged `(j,s)`, selected or not. Converse: without h.16 the deviator strictly prefers the smallest `C_{j'}(s)`; date-0 optimality does not rule this out because `C_j(s)` is sunk. h.16 necessary and sufficient at this step; vacuous on single-Voice menus.

**R18. Date-0 optimality and the outer map.** `U_j(s) = B^F_j(s)P^F(s) − E[𝒪_j|s,j] − C_j(s)` on flagged plans; `U_j(s) = b*_j(s)E[Y|s,j] − E[𝒪_j|s,j] − a_jC_j(s)` otherwise; both finite. `𝒯(k;ϑ)` defined at every `k` only because R5 gives a unique price at every node AND R9 supplies off-path prices at every `k` (deviation payoffs read `Λ_k = 0` histories). A3's two clauses give cutoff structure. [A3; m₀≥0; R9; A2′]

**R19. Brouwer.** `Θ` compact ordered polytope, convex, nonempty [A6 + §4.5]; `𝒯` continuous [A6] ⇒ fixed point at every `κ ∈ [0,1]`.

**R20. `k*` is a cutoff PBE** — all seven §3 items check as listed. Uniqueness neither claimed nor obtained.

**R21. A8 addendum: positive cell mass** — immediate.

**R22. Threshold restatement** — D1 clock equivalence + Voice monotonicity + H-ord + upper-set hypothesis ⇒ `{D=1} = [s_D, ∞)`.

## (2) Points where the row does not state what was needed (each a finding)

**N1** — §4.3's `Y` row and the price convention `P(ℐ) = E[Y|ℐ]`. Consumed at R4. Sharpest omission: the conclusion's own "prices at their inner fixed points" presupposes a definition the hypothesis list never cites.

**N2** — §4.2's Borel-regularity clause (every plan incl. Exit). Consumed at R8, R11, R12 — needed DIRECTLY, not via D1 (D1's conclusion is measurability of `D`/cells, not of `Ψ`).

**N3** — §4.1's distributional forms (Gaussians, `β`) and `Δ_m > 0`. Consumed at R5, R7, R11/R16, R22.

**N4** — §4.2's `D=1 ⇒ a=1`, the `B^F/Q^F/c/f` definitions, `∂_sB_j ≥ 0` for Voice. Consumed at R2(d), R12, R17, R22.

**N5** — "D1 by statement" vs "A5 is not assumed": internal tension (D1's row lists A5). Favourable news: R5–R6 discharge A5's existence, uniqueness AND continuity from `m₀ ≥ 0`; R12–R13 its measurable-selection content from A7-J + Borel clause. Wording repair, not a new hypothesis.

**N6** — off-path prices needed at every `k ∈ Θ`, not only at `k*` (𝒯 reads deviation payoffs). One perturbation family must be fixed once; A6's continuity read relative to it.

**N7** — "reachable under some plan profile" needs "with positive probability" (`Λ_u(h) = 0` includes histories reachable only through a ν-null signal set).

**N8** — `𝒯` must be single-valued before A6 can call it continuous: needs a named tie-break at zero-length crossing intervals and a corner convention for never-optimal plans; A6's "all best-response cutoffs lie in Θ" read to cover corner representations.

**N9** — `Θ` nonempty (§4.5's row supplies it; Brouwer is vacuous otherwise).

**N10** — the card never says when `C_j(s)` is incurred; h.16 makes the two conventions agree on `𝒜` — discharged, clarity finding.

**N11** — recommended §9-style OPEN item: whether A6's continuity of `𝒯` is satisfiable at collapsed cutoff vectors, which §3 explicitly admits. Mechanism: as an interval shrinks to a point, on-path posteriors at histories generated only by the vanishing plan concentrate at the collapsing cutoff, while AT the collapsed vector R9(b) returns the plan-uniform posterior — generically discontinuous exactly at vectors §3 admits. Standard repair (t-constrained game, Kakutani, t ↓ 0) exists but is not §3's declared Brouwer route. NOT a derivability obstruction (A6 is on the row).

## (3) Hypotheses stated but never consumed

- A2′'s local-boundedness clause — never used (finiteness + integrability clauses only).
- A4 consumed thinly but genuinely (truthful `F`; disclosure node Nature's; `f_{j'} = f_j`).
- A7-J consumed twice, both uses need the joint form: R13 and R16. A7′ suffices for neither.
- L2 not on the row and not needed.

## (4) VERDICT

**PASS-WITH-CHANGES.** The row's conclusion is derivable at proof granularity from its hypothesis list plus the card rows below; nothing needed is absent from the CARD, but several load-bearing items are absent from the ROW. No obstruction found. Changes, old→new:

1. **Hypothesis list**: append `"and the §4.1–§4.3 table restrictions — in particular §4.3's Y row and the price convention P(ℐ)=E[Y|ℐ], §4.2's Borel-regularity clause for every plan including Exit, §4.2's D=1⇒a=1 and the B^F/Q^F/c/f definitions and ∂_sB_j ≥ 0 for Voice, and §4.1's distributional forms with Δ_m > 0"`. [N1–N4]
2. **A5/D1**: → `"D1 by statement, with its own hypotheses travelling; A5 is not assumed — its existence and uniqueness content is derived from m₀ ≥ 0, its continuity content from the same scalar reduction, and its measurable-selection content from A7-J plus §4.2's Borel clause"`. [N5]
3. **Off-path clause**: → `"off-path beliefs as limits of one full-support perturbation family over plans, fixed once and used to define the price system at every k ∈ Θ — not only at k*, since the deviation payoffs U_j that define 𝒯 read off-path pooled histories — at every pooled history reachable with positive probability under some plan profile"`. [N6, N7]
4. **A6's reading**: A6 read as asserting that `𝒯`, under a named tie-break-and-corner selection, is a well-defined single-valued continuous self-map of `Θ`, with `Θ` nonempty per §4.5. [N8, N9]
5. **`C_j(s)` timing**: state the convention explicitly (either works; h.16 makes them agree on the round-2 deviation set). [N10]
6. **Recommended, not a change to the implication**: add to §9 — whether A6's continuity of `𝒯` is satisfiable at collapsed cutoff vectors is OPEN. [N11]

None of 1–5 weakens the conclusion; all are citation- or wording-level. The three items the 2026-08-23 demotion turned on all reproduce independently here: A7-J in place of A7′ (R13, R16 — A7′ provably insufficient for both uses), h.16 with exactly the row's scoping including single-Voice vacuity (R17, with matching converse), and the withdrawal of the κ=1 positivity claim (R10).
===== END research/model_v4/rederive/P1_rederivation_2026-08-25.md =====

---

### 5.4 A6 panel — Analyst A, substantiate brief

FILE: research/model_v4/threads/2026-08-27_A6_panel_substantiate.md (verbatim, complete)

===== BEGIN research/model_v4/threads/2026-08-27_A6_panel_substantiate.md =====
# A6-continuity panel — Analyst A (substantiate brief) — filed verbatim 2026-08-27

**Filing note (orchestrator).** One of two opposed-brief Opus panellists dispatched 2026-08-27
under Austin's authorization to rule on the re-derivation's withheld change 6 (N11: whether A6's
continuity of 𝒯 is satisfiable at collapsed cutoff vectors). This analyst's brief: substantiate —
show the belief jump reaches 𝒯's values, test A6 satisfiability under the named tie-break, build
an explicit construction, probe the implemented menu. Read-only on the repo; probes and raw
findings filed at `quality_reports/fixes/a6_panel_probes_2026-08-27/`. The opposed report is
`2026-08-27_A6_panel_defuse.md`. Adjudication: card §9 item 4 (with §5 A6/A3 evidence notes) and
`quality_reports/session_logs/2026-08-27_follow-ups.md`. Report below is the agent's return,
unedited.

---

## ANALYST A — report

Scratch: `/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/a6_A_findings.md` + probes `a6_A_probe{1..8}_*.py`. No repo writes, no git.

---

## (1) MECHANISM VERDICT: **YES-PROVED** — and the jump reaches 𝒯's values with non-vanishing weight

**Where the k-dependence lives.** All of it is in the finite pooled price vector. The flagged layer is *k-free*: A7-J pins the belief at every image tuple to the point mass at ι_F(σ_F) (Step 10), so P^F(σ_F) = 𝒢_F(μ_v + β(ι_F(σ_F)_s − μ_v)) contains no k, and Step 11's flagged-continuation bracket is k-free. **A6's continuity clause is therefore exactly: k ↦ (P^P_d(h;k))_h continuous on Θ.**

**The jump does not die.** U_j(s;k) reads pooled prices at histories generated by plan j at signal s, integrated against the **true noise law conditional on (j,s)** — total weight 1. The probability that j is *played* under k appears nowhere. Two channels:
- **(E) execution cost:** Σ_d L_j(h_d|s)·ΔB_j(s,d)·P^P_d(h_d;k)
- **(T) terminal value:** 𝔼[Y|s,j] contains the control-node price P(𝓘_H) inside Y *and* inside 𝖡 = 1{ξ ≥ P + K + m̄ − S̄}; weight b*_j(s)L_j(h|s). This channel fires **even for a zero-trade plan** (Hold), which the execution channel misses.

Step 9's own load-bearing note concedes the premise ("Step 13 evaluates U_j for **every** j … including plans carrying zero probability under k on a collapse face … so those prices must be defined"). It requires them *defined*; it never requires them *continuous in k*. That is the gap.

**Discontinuity set (exact characterisation).** Λ_k(h) = Σ_j ∫_{I_j(k)} L_j(h|s)φ(s)ds is continuous in k. Step 9(b) gives the Bayes posterior where Λ_k(h) > 0 and the **plan-uniform, k-free** posterior where Λ_k(h) = 0 < Λ_u(h). Hence

  **Disc(𝒯) ⊇ ⋃_h ∂{k : Λ_k(h) > 0}.**

For a history exclusive to a middle plan i+1 this set is exactly the collapse face {k_i = k_{i+1}} — N11's set. In general it is *larger*: interior hypersurfaces where a cutoff exits a likelihood cell.

**CONTINUUM-FACE LEMMA (the decisive step, and it is stronger than N11).** On the face {k_i = k_{i+1} = c}, for h exclusive to plan i+1 with L_{i+1}(h|·) > 0 near c:
- interior limit (from every direction): the posterior concentrates at c, so v̂ → μ_v + β(c − μ_v);
- value *at* the face: the k-free family's own number, one constant.

β > 0, and c ranges over a **continuum** of face points. One constant equals μ_v + β(c − μ_v) for **at most one c**. Therefore: **no k-independent full-support perturbation family can make the price system continuous on a collapse face.** N11 says "generically discontinuous"; the truth is *provably discontinuous at every face point but at most one*, for every admissible k-free family. Requires J ≥ 3 (under Gaussian s, plans 1 and J always keep positive mass; only middle plans can collapse).

**Explicit toy** (derived, not executed): J = 3, H = 1, Γ image {−1, 0, +4}, z̄ = 1. Plan 1 Exit (q ≡ −1), plan 2 Hold (q ≡ 0, a = 0), plan 3 Voice (q ≡ +4). History h* = (X₀,X₁) = (1,1), flag 0, is plan-2-exclusive (needs z = +1 twice; Exit would need z = 2, Voice z = −3). Pr(h*|plan 2) = (κ/2)² > 0 at every s, so §3(vi) binds. Since L₂(h*|s) is constant in s, the face belief is the **prior**: v̂ = μ_v. Interior limit: μ_v + β(c − μ_v).

  **JUMP = β(c − μ_v), exact.** π ≡ 0 on both sides, so π is continuous and only v̂ moves. Price jump = γ·β(c−μ_v) with γ = ∂P/∂v̂ ∈ (0,1] (Step 8). Into U₂ via channel (T) with coefficient b₀(κ/2)²[p′(P)(P + m₀ − 𝔼[v|s]) + p(P)], nonzero off a null set of s. Only U₂ jumps (L₁ = L₃ = 0 at h*), so the argmax comparison jumps by exactly that amount.

**Honest layering of the 𝒯 step.** Belief/price jump: PROVED. U_{i+1} jump: PROVED. **𝒯 jump: proved wherever the vanishing plan sits within the jump size of optimality near c.** If plan i+1 is dominated by more than δ at and near the face, 𝒯 stays locally continuous — I state the escape and close it: A6 quantifies over *all* of Θ and all face points; the marginality condition is an **open** condition on primitives (tune C_j levels); and nothing on the card supplies the uniform domination margin that would rescue A6. Note the jump direction is self-undermining — off-path execution is cheaper, so the vanished plan looks *better* at the face than in the limit from inside (measured sign below).

**Which perturbation-family choices.** Real for **every k-independent family** (lemma above). Repaired by a **k-indexed** family whose tremble to plan i+1 concentrates near [k_i, k_{i+1}]: that returns the point mass at c, matches the interior limit, and is still "a limit of full-support perturbations" under §3(vi) as §3 words it. **What forbids it is the row's own 2026-08-25 amendment** — "one full-support perturbation family … **fixed once** and used to define the price system at every k ∈ Θ", folded from pass-2 change 3 to close N6. The repair that closed N6 is what pins the k-freeness that makes A6 false.

**Escapes I checked and closed.** (i) *"Version freedom"* (Step 10): unavailable. Pooled histories are atoms of a **finite** family with Λ_u(h*) > 0, so the conditional is pinned exactly; the a.e.-version latitude lives only on the flagged continuum. (ii) *"Convention freedom"* (Step 9(c), NOT CLAIMED 13): unavailable. h* is *reachable* with positive probability, so it falls under 9(b), not 9(c).

---

## (2) SATISFIABILITY

**False for THIS construction, on the stated menu class.** Precise hypothesis: J ≥ 3; some middle plan has a pooled history exclusive to it whose likelihood is positive on a non-degenerate interval of face points c; the price at that history enters some U_j with a nonzero coefficient. Then A6's continuity clause is false at every point of that face but at most one. A6 is not a free parameter — 𝒯 is *constructed* from primitives + the fixed family + the tie-break — so A6 is a restriction on primitives, and on this class the restriction is unsatisfiable. **P1 is then vacuous on that class**, exactly as L3/L4/T1 are vacuous where A(τ) fails.

**Not false for every construction.** Two repairs, both outside §3's declared route: the k-indexed concentration family (restores continuity, keeps Brouwer); and the t-constrained game + Kakutani + t ↓ 0, which is the re-deriver's route and is **Step 18** already on file. Both need Step 15(i) anyway.

**Third failure found — upstream of A6.** At the implemented calibration, on an **open** set of k, U_V − U_H has **three** strict sign changes, so argmax alternates H,V,H,V: **A3 fails in both clauses**, 𝒮(k) = ∅, and Step 13's largest-weakly-increasing-selection tie-break has nothing to select — **𝒯 is undefined**, not merely discontinuous. Numbers in (3).

**What this does NOT mean.** A6 false ≠ existence false ≠ the proof wrong. The proof is valid; its antecedent fails. The solver converging to 10⁻¹¹ at 23/27 nodes is fully consistent — fixed points sit in cell interiors where 𝒯 is locally continuous; Brouwer needs continuity on *all* of Θ. **P1 stays PROVED as a conditional.**

---

## (3) IMPLEMENTED MENU — collapse is live; the mechanism is live; but at *different* loci

**Collapse is live.** From `quality_reports/fixes/t2_p1_check.json`, `p1_multistart_existence_sweep`, 27 nodes: node **(κ,τ,T) = (0.5, 0.05, 1)** solves to **k = (1.35358624390523, 1.35358624390523), k₂ − k₁ = 0.000e+00 exactly** — Hold fully collapsed, Hold prior mass 0, and it *converged* (payoff residual 0.0, cutoff 4.36e−11). Near-collapse at (0.5, 0.075, 1): width 5.27e−02. Other 25 nodes: 1.06e−1 … 7.06e−1. And `numerical_v4/params.py:95` sets **C0 = 0.014** as "the smallest value at which the Hold region stays interior at the frozen tau; below it Voice and Exit meet and Hold collapses" — the calibration is tuned to the collapse boundary.

**But the collapse face is BELIEF-INERT here — a point against N11's literal wording.** Exit and Hold share the θ = 0 all-zero mark path ("Exit's day-0 increment is negative and marks 0, so Exit and Hold pool perfectly in order flow"), so Hold's death makes no history off-path. Measured at k₁ = k₂ vs k₁ = k₂ − {1e−9, 1e−4, 1e−2}: 𝔼[P₀^P|θ=0] = **1.1383084485 on all four to 10 d.p.**, live-type set identical, implementation 𝒯 identical, card 𝒯₂ = 1.31307280 identical.

**The same mechanism fires through the mark-type channel, on INTERIOR hypersurfaces of Θ.** As k₂ crosses an n(s) cell edge, a Voice mark-type's mass crosses zero and its exclusive histories snap from Bayes to the k-free `type_reference`. Node (κ=0.5, τ=τ₅₀, T=5), k₂ = edge ∓ 10⁻⁹:

| dying t | v̂ below | v̂ above | jump | predicted (ref − concentration) | **card \|𝒯₂ jump\|** |
|---|---|---|---|---|---|
| 11 | 1.23008952 | 0.84627187 | −3.84e−1 | −3.8382e−01 | 6.9e−10 |
| 10 | 1.25896614 | 1.24439195 | −1.46e−2 | −1.4574e−02 | 6.8e−10 |
| 9 | 1.29166663 | 1.27512024 | −1.65e−2 | −1.6546e−02 | **6.33e−03** |
| 8 | 1.32953120 | 1.31030216 | −1.92e−2 | −1.9229e−02 | **1.09e−02** |
| 7 | 1.37463449 | 1.35160560 | −2.30e−2 | −2.3029e−02 | **2.83e−02** |
| 6 | 1.43041441 | 1.40169048 | −2.87e−2 | −2.8724e−02 | **1.91e−02** |

"below" reproduces μ_v + β(edge − μ_v) to 7–8 d.p.; "above" reproduces the k-free reference exactly; **predicted = measured to ~1e−8**. Card 𝒯₂ is the inf-selection of Step 13 (lowest crossing, brentq, 4001-point grid). The implementation's own `outer_map` shows the *same* jumps. **2.83e−2 across a 2e−9 step in k₂, against a convergence tolerance of 1e−10** — eight orders of magnitude.

**Channel confirmed, with a control.** Dying type t's own aggregates jump; the surviving neighbour's move by ~3e−9:

| dying t | Σ_d \|𝔼[P_d\|θ] jump\| (channel E) | 𝔼[p_bid\|θ] jump (T) | 𝔼[p·P\|θ] jump (T) | control (neighbour) |
|---|---|---|---|---|
| 10 | 7.37e−2 | +1.63e−2 | +1.91e−2 | 3.79e−9 |
| 9 | 8.02e−2 | +8.99e−3 | +1.11e−2 | 3.60e−9 |
| 8 | 9.45e−2 | +6.49e−3 | +8.37e−3 | 3.29e−9 |
| 7 | 1.19e−1 | +5.55e−3 | +7.47e−3 | 2.83e−9 |

U_VOICE(s) on the dying cell jumps **+2.24e−4 … +4.39e−4** — positive: Voice looks *better* once its own type is off path, the self-undermining direction.

**`type_reference` IS the card's Step 9(b) plan-uniform limit** for this menu: at a t-exclusive h, L is constant on {n(s)=t}, so the limit posterior is the prior truncated to that cell = 𝔼[v|n(s)=t] = `ref.Ev[t]` — verified to 1e−8 in the table. `OFF_PATH_EPS` cancels in the ratio at an exclusive history. **So the measured discontinuity is the card's construction, not an implementation artifact.** Type-exclusive histories exist by construction (Γ binary, X ∈ {−1,0,1,2}; X_d = 2 forces q_d = 1, X_d = −1 forces q_d = 0 — `pooled.mark_stats`'s `ok`). *Why the jumps are percent-scale, not (κ/2)^{H+1} ≈ 2.4e−7:* the operative notion is exclusive-among-**alive** types, and those histories carry mass ~κ/2 per relevant date.

**A3 failure, verified and open.** k₂ = edge(6)+1e−9: three sign changes at s = 1.5754434, 1.5833333, 1.5902426; middle excursions max|gap| = **2.80e−4 and 2.40e−4** vs TOL_PAYOFF = 1e−9 (five orders above noise, and equal to the measured off-path bump). Argmax = H,V,H,V, single-valued on each interval ⇒ no weakly increasing selection exists. Open set: 3 crossings at edge(6) + {1e−9, 1e−4, 1e−3, 5e−3, 2e−2}; back to 1 at +5e−2. Width ≥ 2e−2 in s (≥ 0.028 σ_s). The middle excursion sits at s = 1.5833333 = edge(8), an n(s) step — the off-path bump interacting with the s-discontinuity of U_VOICE.

**Robustness (artifact attack closed).** Re-run at ±1e−6 (1000× `breakpoints`' 1e−9 merge tolerance): t=9 → 6.3331e−03 (vs 6.3333e−03), t=8 → 1.0860e−02 (vs 1.0859e−02), t=7 → 2.8281e−02 (vs 2.8279e−02). Identical.

**Honest negatives I am keeping.** (a) The collapse face is inert here — N11 named the right mechanism but the wrong locus for this menu. (b) Equilibria sit 0.004–0.054 σ_s from the nearest death surface, but the edge half-spacing there is 0.026–0.056 σ_s: they are **not** systematically close, the surfaces are just dense. (c) The four payoff-unresolved nodes sit at 0.031/0.026/0.044/0.030 σ_s — **no closer than the converged ones. The mechanism does not explain them; I claim no correlation.**

**Two corroborating repo artifacts.** `numerical_v4/menu.py:304–316`: *"Without this the pricing map has holes, and the outer map T(k) jumps by ~0.1 in the cutoff whenever a type's mass crosses zero — which is exactly where the equilibrium sits."* And `numerical_v4/solver.py:30–34` (N_GRID=241): *"U_Voice(s) steps down at every n(s) decrement … a bracket wider than an n-plateau lets brentq converge on the jump instead of the root"* — i.e. **Step 15(i)'s continuity of s ↦ U_j fails on this menu independently**, instantiating WHERE IT FAILS 4's card-legal counterexample. Also: `outer_map`'s `target=` nearest-bracket rule is a *different* tie-break from Step 13's inf-selection, and its fallback `k2 = k1 if gap_HV(...) ≤ 0` returns a collapsed vector.

---

## (4) CARD RECOMMENDATION — sharper than pass-2's proposed OPEN line

Do **not** file N11's line as "OPEN". The question is answered. Recommend the **A(τ) precedent**: a dated NUMERICAL-class evidence note under A6 in §5 plus a §9 item *replacing* change 6, with **no label move** (A6 is an assumption, not a labelled claim; P1 stays PROVED as a conditional). Proposed §9 text:

> **A6's continuity of 𝒯 — RESOLVED NEGATIVELY for the declared construction, and FAILING at the implemented calibration.** (i) *Analytic.* All k-dependence of U_j runs through the pooled price vector (the flagged layer is k-free by A7-J). Step 9(b) gives the Bayes belief where Λ_k(h) > 0 and a **k-free** plan-uniform belief where Λ_k(h) = 0, so 𝒯 is discontinuous on ⋃_h ∂{k : Λ_k(h) > 0}. On a collapse face {k_i = k_{i+1} = c} the interior limit is μ_v + β(c − μ_v), which varies over the face, while any **k-independent** family supplies one constant: they agree at **at most one** face point. Hence A6 is **false at every collapse-face point but at most one**, for every k-independent perturbation family, on any menu with J ≥ 3 carrying a reachable plan-exclusive pooled history that enters some U_j. This is not a derivability obstruction — A6 is on P1's row — but it makes P1 **vacuous on that menu class**. The row's own clause "one full-support perturbation family … fixed once and used to define the price system at every k ∈ Θ" (folded 2026-08-25 as pass-2 change 3, closing N6) is precisely what pins the k-freeness. Repairs exist and are §3(vi)-legal — a k-indexed concentration family, or the t-constrained game with Kakutani and t ↓ 0 (`proofs/P1_proof.md` Step 18) — but neither is §3's declared Brouwer-with-one-fixed-family route. (ii) *At the implemented calibration.* Plan collapse **is** live (1 of 27 sweep nodes solves to k₁ = k₂ exactly; C0 = 0.014 is tuned to the collapse boundary) but is **belief-inert**, because Exit and Hold share the θ = 0 mark path. The same mechanism fires instead on **interior** hypersurfaces of Θ, where a mark-type's mass crosses zero: measured jumps in the card's 𝒯₂ of **6.3e−3 to 2.8e−2** across a 2e−9 step in k₂, against a 1e−10 convergence tolerance, with the belief snap matching prediction to 1e−8 and a 3e−9 control on surviving types. (iii) *Separately, A3 fails* on an open set of k at the same calibration — three strict crossings of U_V − U_H with excursions of 2.4–2.8e−4 vs a 1e−9 tolerance — so no weakly increasing selection exists there and 𝒯 is **undefined**, upstream of continuity. (iv) *Separately, Step 15(i)'s continuity of s ↦ U_j fails* on this menu, since n(s) is integer-valued and U_VOICE steps at every decrement (`numerical_v4/solver.py` N_GRID note).

Keep the proof-reader's finding 5 (structural plateaus, multi-Voice only, vacuous on this single-Voice menu) as a **separate** failure mode from this one — two distinct routes by which A6's named sufficient conditions fail, only one of which is live at the implemented calibration.

---

## (5) UNCHECKED

1. **The toy is derived, not executed.** No numerical instantiation of the J=3/H=1 example; the jump β(c−μ_v) and the U₂ coefficient are analytic.
2. **No marginality-tuned collapse-face 𝒯-jump was executed.** The 𝒯-level jump *at a plan-collapse face* rests on the argument that the vanishing plan can be made near-optimal (an open condition), not on an exhibited instance.
3. **The k-indexed repair has an unresolved corner:** histories with L_{i+1}(h|c) = 0 (incompatible with the collapsing signal) give 0/0 again and need the concentration rate to resolve. Constructible, not constructed.
4. **Non-existence is neither claimed nor shown.** A discontinuous self-map may still have fixed points; the solver's 23/27 convergences are evidence it does here.
5. **The four sweep-unresolved nodes are NOT explained by this mechanism** — no proximity correlation to the death surfaces. Their status is unchanged from ticket 34.
6. **Coverage:** all implemented probes are at one node (κ=0.5, τ=τ₅₀, T=5) except the 27-node k-vector census and the collapse-face test at (0.5, 0.05, 1). The type-death jumps were not swept over κ or T.
7. **Menu-class scope:** the vacuity claim is scoped to J ≥ 3 menus with a reachable plan-exclusive pooled history. I did not characterise the complementary class (menus where every middle plan's histories are shared with a surviving plan — the implemented menu's Exit/Hold pooling is one such case), where A6's collapse-face clause may well be satisfiable.
===== END research/model_v4/threads/2026-08-27_A6_panel_substantiate.md =====

---

### 5.5 A6 panel — Analyst B, defuse brief

FILE: research/model_v4/threads/2026-08-27_A6_panel_defuse.md (verbatim, complete)

===== BEGIN research/model_v4/threads/2026-08-27_A6_panel_defuse.md =====
# A6-continuity panel — Analyst B (defuse brief) — filed verbatim 2026-08-27

**Filing note (orchestrator).** The second of two opposed-brief Opus panellists dispatched
2026-08-27 under Austin's authorization to rule on the re-derivation's withheld change 6 (N11).
This analyst's brief: defuse — build the vanishing-mass argument, probe the deviation-payoff
subtlety, test whether the perturbation-family choice reconciles the limits, probe the implemented
menu. Read-only on the repo; probes and raw findings filed at
`quality_reports/fixes/a6_panel_probes_2026-08-27/`. The opposed report is
`2026-08-27_A6_panel_substantiate.md`. Adjudication: card §9 item 4 (with §5 A6/A3 evidence notes)
and `quality_reports/session_logs/2026-08-27_follow-ups.md`. Report below is the agent's return,
unedited.

---

# ANALYST B — defusal brief on N11. Report.

## (1) VERDICT: **NARROWED**

I could not defuse it. The mechanism is real, it reaches `𝒯`'s returned cutoffs, and I measured it. But N11's *locus* is wrong in both directions, and the collapse face the paper's baseline would actually visit is provably clean.

**X, stated exactly.** Write `Λ_k(h) = ∫ L_{j_k(s)}(h|s) φ_s(s) ds`. Step 9(b)'s rule is: Bayes where `Λ_k(h) > 0`; the **k-independent** plan-uniform posterior where `Λ_k(h) = 0 < Λ_u(h)`; Step 9(c)'s reference root (also k-independent) where `Λ_u(h) = 0`. `Λ_k(h)` is continuous in `k`, and `L_j(h|·)` is a step function on the finitely many mark-and-flag level cells. Therefore the price at `h` can be discontinuous **only** on `∂{k : Λ_k(h) > 0}` — and generically is, the one-sided limit being the value concentrating at the touching interval endpoint and the value at the frontier being the plan-uniform mean. That set is contained in

> (finitely many **cell-edge hyperplanes** `{k_i = a}`, `a` ∈ the mark/flag cell edges) ∪ (the collapse faces `{k_{i-1} = k_i}`)

So: (a) N11 **misses** the cell-edge hyperplanes — non-collapsed vectors, and that is where the implemented instance's jumps actually live; (b) a collapse face is a discontinuity only when the collapsing plan is the *sole* on-path generator of some positive-probability history, which the implemented Hold-collapse face is not.

**Brief item 1 — the vanishing-mass defusal is refuted, and I could not rebuild it.** Step 11's bracket is `E_z[Σ_d P^P_d(H^P_d)(B_j(s,d) − B_j(s,d−1))]`, an expectation under the **deviator's own** noise law given `(s,j)`. Affected histories carry weight `Pr(z_{0:d}) ≥ min(κ/2, 1−κ)^{d+1}` — independent of the collapsing plan's population mass. The implementation is literally that object (`numerical_v4/pooled.py`: `EP[d][t] = np.dot(L_t, P_d)`; `numerical_v4/policy.py::plan_payoff` reads `res.EP[d][θ(j,s)]`).

**Brief item 2 — the tie-break does not absorb it.** The largest-weakly-increasing-selection resolves *s*-direction ties at fixed `k`; a `k`-discontinuity in the `U` levels passes straight through any pointwise-in-`k` selection. Nor does the crossing structure absorb it: `U_HOLD` does not move when `U_VOICE` jumps, so the adjacent-pair difference jumps by the full amount.

**Brief item 3 — the family does not reconcile the limits.** At fixed `n` the denominator is `≥ (t_n/J)Λ_u > 0`, so the whole price system is continuous in `k`; the discontinuity is created only by `t_n → 0`. The two limits do not commute — the family choice cannot fix an order-of-limits problem. Notably, `OFF_PATH_EPS = 1e-14` in `pooled.py` **is** a fixed-`t` constrained game, i.e. N11's own "standard repair", already shipped; and the reference it attaches, `Ev[t] = E[v | n(s)=t]` over the whole line, **is** Step 9(b)'s plan-uniform posterior restricted to that type.

**Brief item 4 — the implemented case.** Collapse is *not* live at the baseline (`k* = (1.2405757283, 1.5310222869)`, Hold width 0.290447), the Hold-collapse face is clean, and yet the jumps are live at non-collapsed vectors. A compact `Θ` interior to one chamber restores A6 at the baseline and contains `k*` — but that fails at κ = 0.15.

## (2) The counter-argument I could not overcome, verbatim

> A6 as the card states it is quantified over *all* best-response cutoffs: "All best-response cutoffs lie in a common compact ordered polytope Theta; T is continuous and maps Theta into itself." Steps 13-14 construct Theta from the *bracket* `[s_lo, s_hi]` — the union over adjacent pairs of every indifference signal, uniform in the conjecture. Any Theta built that way contains the cell-edge hyperplanes, and on it the constructed price system's `T` is provably discontinuous: I measured jumps of 6.3e-03, 1.09e-02 and 2.83e-02 in `T_2` on the paper's own menu and calibration. The chamber-interior `Theta+` that rescues A6 is not something Steps 13-14 supply — exhibiting it requires already knowing where `T` maps a small box into itself, i.e. already knowing roughly where the fixed point is. So A6 is satisfiable here, but only under a reading of Theta that the proof does not construct and that cannot be checked without effectively solving the model first. That is a real gap between the hypothesis as written and the object built.

## (3) Probe numbers

**Hold-collapse face is clean.** Exit and Hold share mark-path type 0 (Γ is a buy-indicator; Exit's day-0 decrement marks 0), so type-0 mass is `Φ_s([s_lo, k₂))` — a function of `k₂` alone. Varying `k₁ ∈ {0.5, 1.0, 1.2406, 1.40, 1.52, k₂}` at fixed `k₂`, last value = Hold fully collapsed: `max|EP − EP(k₁=0.5)| ≤ 4.441e-16`; `U_V(1.6)` bit-identical; `𝒯(k)` bit-identical. **The whole pooled price system, hence `𝒯`, moves with `k₂` alone.**

**The jump reaches `𝒯`, at non-collapsed vectors** (frozen τ = 0.090764058616, `k₁ = 1.2405757283`; left limits converged by δ = 1e-7):

| `n(s)` cell edge `S` | `𝒯₂(S⁻)` | `𝒯₂(S)` | jump in `𝒯₂` | `𝒯₁` jump |
|---|---|---|---|---|
| 1.583333333333 | 1.549728951 | 1.543395170 | **−6.334e-03** | 4e-09 |
| 1.659062162746 | 1.569659263 | 1.558798550 | **−1.086e-02** | 3e-09 |
| 1.749268649265 | 1.603724853 | 1.575443391 | **−2.828e-02** | 3e-09 |

At the first edge, `U_VOICE(s₀)` jumps `0.0362570819 → 0.0365064990` while `U_HOLD(s₀)` moves `< 1e-10` — **no cancellation**. Price at a date-7 history carrying an `X=2` mark: two-sided limits **1.543850 vs 1.400791** (a 0.143 gap; left limit stable over δ = 1e-4…1e-8, right value constant for all δ ≤ 1e-10 including 0).

**A6 *is* satisfiable at the baseline, on a chamber-interior Θ.** `k₂* = 1.5310222869` sits inside the open chamber `(1.517932397378, 1.583333333333)` between k-independent cell edges, 0.0131 above / 0.0523 below. On a 29-point grid `𝒯` is smooth there (max adjacent `|d𝒯₂| = 1.185e-03` at spacing 3.17e-03, slope ≈ 0.35), and `𝒯₂([1.525272, 1.550633]) = [1.529026, 1.537885]`, `𝒯₁(·) = [1.231449, 1.243303]`. So `Θ⁺ = [1.23, 1.245] × [1.5253, 1.5506]` is compact, ordered, self-mapping, discontinuity-free, and contains `k*`. Brouwer runs verbatim on it.

**But the chamber rescue fails on the card's own grid, and — the strongest thing here — ticket 34 is explained.** At κ = 0.15, τ = 0.05, T = 5 (one of the four sweep-UNRESOLVED nodes), `𝒯₂` jumps at edges by up to **−0.16**, the diagonal crossing at edge 1.583333333 is **destroyed** by the jump (gap +1.0e-07 just below → −6.70e-02 at it), and a fixed point sits **on** the edge 1.659062163. There, `U_H − U_V` = −1.765771e-03 just below (n=8) and +1.278166e-03 just above (n=7): it **jumps through zero, never crossing it**. `equilibrium_residual` gives cutoff 4.751e-10, payoff **1.766e-03**; the solver from its own seed gives payoff 1.488e-03, and from `k_init=(1.02,1.71)` it gives `k = (1.0260443221, 1.7104049079)`, cutoff 2.878e-11, payoff **3.055e-04**. Those bracket the card's ticket-34 record ("3.1e-4 – 1.5e-3"; "1e-14 – 1e-11") exactly.

**Honest attribution of that last result:** it is the ***s*-direction** jump (Step 15(i) / WHERE IT FAILS 4 — `n(s) = clip(ceil(...))` is integer-valued, so `B_VOICE(s,d)` steps in `s`), **not N11's *k*-direction one**. Worse, the pointwise argmax across edge 1.659062163 runs **VOICE below → HOLD above** (singletons, at *both* of that node's fixed points), so the preferred plan *decreases*: `𝒮(k)` is empty and **h.3/A3 fails**, upstream of A6. My `𝒯₂` jumps remain attributable to N11's mechanism, on these grounds: (α) can move `𝒯` in `k` only where a smooth level shift slides a branch across a fixed `s`-jump — at generic `k`, not pinned to the edges — whereas every jump I measured is bracketed at an edge to ±1e-8 *and* co-located with a measured `U_V(s₀;k)` level jump at a fixed `s₀` away from any edge.

## (4) Card recommendation: a **sharper §9 line**, not N11's as drafted

Full proposed text is in the findings file (§6). Its core: name the locus as the **cell-edge hyperplanes ∪ plan-unique-generator collapse faces** rather than "collapsed vectors"; state that the jump reaches `𝒯` because `U_j` weights those prices by the deviator's own noise law; record that the pinned menu's Hold-collapse face is clean by Exit/Hold mark pooling; give the measured `𝒯₂` jumps; note that a chamber-interior `Θ` rescues A6 at the baseline but is not what Steps 13–14 construct and fails at κ = 0.15; note Step 18's Kakutani route already removes h.6's continuity half. **The P1 label is untouched** — A6 is a listed hypothesis, so this is satisfiability, not derivability. Separately, the κ = 0.15 argmax reversal is a **different and larger** finding about h.3/A3 and ticket 34, and should not be folded into the A6 line.

## (5) UNCHECKED

- General-menu satisfiability of a chamber-interior `Θ` — verified on one menu, one calibration, a 29-point grid; not proved, and shown to fail at κ = 0.15.
- Whether a destroyed crossing can leave a calibration with **no** fixed point. At κ = 0.15 a crossing is destroyed yet two fixed points survive; nonexistence is demonstrated nowhere. Not swept over (κ, τ, T).
- Whether A3's monotone-preferred-plan clause survives at the κ = 0.15 node. The card records "the A3 and A6 proxies pass at every achieving seed"; I did not open the proxy definitions to reconcile that with the argmax reversal above. **This is the item I would escalate first.**
- Flag-coordinate contribution to the locus: in the implementation the flag enters through *aliveness* (`_alive_weights` drops atoms with `D=1, f≤d`), not mark feasibility, so τ-crossing pullbacks are additional candidate edges; I swept the `n(s)` edges only.

## Files (all scratchpad, read-only on the repo, no git run)

`/private/tmp/claude-501/-Users-austinli-Projects-blockholder-v4-theory/ab9c0696-e7f9-466e-8d38-08f559ee1613/scratchpad/` — `a6_B_findings.md` (the full write-up), `a6_B_struct.{py,json}`, `a6_B_sweep.{py,json,log}`, `a6_B_baseline.{py,json,log}`, `a6_B_chamber.{py,json,log}`, `a6_B_node15.{py,json,log}`, `a6_B_resid.py`, `a6_B_alt.py`, `a6_B_argmax.py`.
===== END research/model_v4/threads/2026-08-27_A6_panel_defuse.md =====

---

### 5.6 Independent check of the draft_v3 sections against the card

FILE: research/model_v4/threads/2026-08-27_t4_sections_check.md (verbatim, complete)

===== BEGIN research/model_v4/threads/2026-08-27_t4_sections_check.md =====
# T4 — independent check of `sections_v3/` against MODEL_CARD.md

**Role.** Independent checker for ticket 08 (T4). I wrote none of the files checked. My only write
is this file; nothing under `sections_v3/` or `research/` was edited, and I ran no git command.

**Date.** 2026-08-27.

**Stamps verified before checking.**

- `research/model_v4/MODEL_CARD.md` — header line 3: *"Version stamp: 2026-08-27 · A6 panel
  resolution (§5 A6/A3 evidence notes + §9 item 4) · commit `ae9caea`"*. **Matches the contract.**
- `research/model_v4/model_v4.md` line 12 and `model_v4.tex` line 68 — both carry *"version stamp
  2026-08-27, A6 panel resolution, commit `ae9caea`"*. **Note regenerated to the card stamp.**
- Five of the six section files carry the same stamp in their headers. The sixth,
  `proofs_section.tex`, is a seven-line plumbing file (`\section{Proofs}`, `sec:proofs`, three
  `\input` lines) with no header block — correctly, since it states nothing.
- `sections_v3/v3_macros.tex` header cites a **stale** stamp — see finding **M-10**.

**Objects checked.** `sections_v3/model_section.tex`, `theorem_section.tex`, `proofs_section.tex`,
`proofs_core_lemmas.tex`, `proofs_existence.tex`, `proofs_theorem_ge.tex`, plus `v3_macros.tex` and
`standalone_v3.tex` as build plumbing.

**Binding inputs.** `MODEL_CARD.md` (wins over the note wherever they differ), `model_v4.tex`/`.md`,
`CONTEXT.md`, the fidelity contract, and — as *claims* rather than evidence — the writers'
`crosswalk_model_theorem.md` and `labels_map.md`.

**Source proofs read for the transcription-grain check.** `proofs/P1_proof.md` (Step 12 block and
the h.1–h.17 register), `proofs/L3_proof.md` (Steps 1–6, 14–19), `proofs/L4_proof.md`,
`proofs/T1_proof.md` (H17/H18 and the Step-15/16 material), `proofs/C1_proof.md` (H8),
`rederive/C1_rederivation.md` (H8 verdict), `threads/thread1_turn2_answer.md` (referenced for D1/L1/L2
provenance only).

**Grain.** Statement fidelity at full grain (every clause of every card §6 row, plus §1–§5 and §9
material carried into the model section). Proof fidelity at transcription grain, with deep samples at
P1 Step 12, the L3 chord steps, T1 Step 16's quantifier, and C1's norm-convention preamble.

**Coverage.** I read all six section files end to end, plus `v3_macros.tex`, `standalone_v3.tex` and
`sections_v3.bib` in full. No stretch of any proof file is vouched for unread.

---

## 0. Verdict vocabulary as applied

- **WRONG** — substance mismatch (dropped or weakened clause, wrong number, invented claim, label or
  conditionality deviation). Blocks landing. **Count: 0.**
- **MISCITED** — a pointer, attribution or provenance is off; substance intact. Never blocks.
- **UNCHECKED** — could not verify. Never blocks.
- **OK-RESTRUCTURED** — deliberate paper-form restructuring that preserves substance; listed so the
  record is complete.

Two things are reported outside the four classes, in §3: a build-plumbing risk that is not a
difference from the card, and the correction to item 13's premise.

---

## 1. Findings by file

### 1.1 `sections_v3/model_section.tex`

---

**M-1 · `asm:TR`, lines 176–209 · OK-RESTRUCTURED**

The card carries the primitive restrictions as sign-restriction columns across three tables (§4.1,
§4.2, §4.3). The section gathers them into one `assumption` environment with clauses (TR-i)–(TR-iv).
A table has no citable target and three results cite the block wholesale, so the restructuring is
declared and reasoned at crosswalk §0 row 25. I walked all four clauses against the three card
tables: every sign restriction, the `b_0 < \tau` maintained restriction, the Borel-for-Exit addition,
the continuum-valued stake-level note, the legal-clock objects with the `T' < T` monotonicities, and
the pricing/entry conventions are present and unreworded.

---

**M-2 · `rem:A3record`, lines 265–291 · MISCITED (pointers only)**

Substance is complete against card §5's A3 evidence note. I verified every number: the three sign
changes at `s = 1.5754434 / 1.5833333 / 1.5902426`; middle excursions `2.4`–`2.8e-4` against a
`1e-9` payoff tolerance; offsets `1e-9` through `2e-2`; the H,V,H,V argmax; "the selection set is
empty and the outer map $\Tmap$ is *undefined* there, not merely discontinuous"; the
`(κ=0.15, 0.05, 5)` VOICE→HOLD reversal across `s = 1.659062163` at both located fixed points; the
integer-valued `n(s)` route and the off-path price snap; the proxies-are-local-screens paragraph; the
candidate mechanical account with residuals `3.06e-4`–`1.77e-3` at `1e-11`-grade cutoff residuals,
"bracket the recorded range exactly"; the panellist's own recorded negative on the *k*-direction
mechanism; and "No label moves … A3 is a hypothesis, and Proposition~\ref{prop:P1} stays PROVED as a
conditional."

Card pointers dropped: "Step 15(i) / WHERE IT FAILS 4's card-legal counterexample, instantiated by
the solver's own `N_GRID` note", and the proxy script `t2_p1_fournode_recheck.py`.

**Verdict:** MISCITED. Non-blocking; the proof-file and implementation IDs are internal record
anchors and do not belong in paper prose. The A3 proxy script is, however, named nowhere in the
sections while every other record in the file is given as a `\texttt{}` string — an inconsistency
worth one line of the orchestrator's attention.

---

**M-3 · `rem:A6record`, lines 324–373 · MISCITED (pointers only)**

Substance is complete against card §5's A6 evidence note and against contract gate (c)'s enumerated
element list. Verified present: the continuity clause fails for the declared construction and the
locus is not the one first proposed; the locus is *cell-edge hyperplanes* ∪ *sole-generator collapse
faces*, "not the collapsed cutoff vectors as such"; the jump reaches `\Tmap` with weight at least
`min(κ/2, 1−κ)^{d+1}`, independent of the dying plan's population mass; the vanishing-mass defusal
refuted by both panellists independently; the tie-break is pointwise and passes the jump through; the
order-of-limits argument against a *k*-independent family; the `J ≥ 3` continuum-face lemma with
`μ_v + β(c − μ_v)` and "fails at every face point but at most one", explicitly **not gate-checked**;
the implemented menu excluded from that class with the Hold-collapse face measured clean at
`4.4e-16` and `\Tmap` bit-identical; the measured `\Tmap_2` jumps `6.33e-3 / 1.09e-2 / 2.83e-2` at
`≤ 2e-9` steps, independently measured to three significant figures, belief snap to `~1e-8`,
surviving-type controls `~3e-9`, robust at `1000×` the merge tolerance; `0.16` and the destroyed
diagonal crossing at `κ = 0.15`; `Θ⁺ = [1.23, 1.245] × [1.5253, 1.5506]` with all three caveats; "No
label moves and none is licensed"; P1 stays PROVED as a conditional "in the same pattern as
$\Atau$"; both repairs; the `1e-14` off-path floor as the shipped fixed-*t* constrained game with the
switch relocated by `~1e-9`; coverage (one node per claim class plus the 27-node census, not swept);
`23` of `27` converge and nonexistence neither claimed nor shown; both `threads/` panel files and the
probes directory named as `\texttt{}` strings, "analysis-grade and not curated executed checks".

Card pointers dropped: the constant name `OFF_PATH_EPS`; "Step 9(b)" as the source of the frontier
posterior; "Step 18" as the location of the *t*-constrained repair; the proof-local symbol `Λ_k`
(rendered as "the reaching weight").

**Verdict:** MISCITED. All four are internal anchors; Step 9(b) and Step 18 both exist in
`proofs_existence.tex` under the same numbers, so a reader can still find them.

---

**M-4 · `rem:AtauRecord`, lines 464–533 · MISCITED (two pointer losses) + OK-RESTRUCTURED**

This covers **checklist item 11**. Substance is complete: I verified every figure against card §5's
A(τ) evidence note — `4^{H+1} = 4,194,304`; 200 nodes over `κ ∈ {0.05,…,0.95}` × five frozen `τ`
percentiles × `T ∈ {1,2,5,10}` at frozen policies with `H = 10`; both gates (`0.0` exactly and
`1.7e-16`); the 20 degenerate nodes with `M_P = 0`, `C_h(0) = 0`, "holds vacuously and the node
decides nothing"; 180 non-degenerate nodes all failing; 23–767 atoms at 0 of 180; no mass at `π̄/2`
so `A_{1/2} ≡ 0`; `0.57%`–`91.8%` off-support with `13.9%` at the median node (`T=5`, median `τ`,
`κ=0.55`: 107 atoms, `A_0 = 0.768`, `A_1 = 0.093`); the `1e-3` coarsening leaving 6–332; the
floor-free law at most 51 atoms fewer; Hausdorff `0.4608` unchanged at mass `≥ 1e-6` against a
predicted `<1e-12` at 0 of 18 series; `π̄ = 1` to `1.5e-13` at 18 of 18 and the named-false
conjecture; `π̄ ∈ {0,1}` never interior so the small-`π̄` corollary has no instance; `A_0' = A_1'` at
0 of 180 with `|A_0' − A_1'| ∈ [0.041, 2.306]`, `A_0' ∈ [−2.146, 2.374]` against
`A_1' ∈ [−0.014, 0.429]`, both changing sign; `A_{1/2}' = −2A'_κ` recorded as **inherited**, exactly
`2|A_0'|`; the chord residual `0.0013`–`0.0717` (up to `7.17` premium pp) at 0 of 180 on the most
favourable of three kernel conventions, with recovered `|A'_κ| ∈ [0.042, 2.374]`, required
`[0.00023, 0.392]`, disjoint from `[0.997, 1.158]`; the (τ-i) diagnostic `0.085` and `0.018`
mass-weighted; "NUMERICAL-class *applicability* evidence at one calibration. No label moves, and none
is licensed"; L3, L4 leg 3 and T1 Part (B) staying PROVED as conditionals and saying nothing about
the implemented cell; the domain reading of the open question; the six-distinct-pooled-cells caveat
with its full explanation; and the script, JSON, 200 nodes, 920 enumerations, 1002 seconds and
`FAILS at calibration` verdict field.

**M-4a — the "(S1) and (S2)" pointer. MISCITED, and a real loss.**

- Card, §5 A(τ) note, support-half bullet, final sentence: *"This refutes L3 Step 18's (S1) and (S2)
  together at this calibration."*
- Section, lines 480–489: the bullet ends at *"…against a predicted `<10^{-12}`, at 0 of 18
  series."* The sentence is absent.

I checked whether the record link survives via the L3 proof, as the checklist asks. It does **not**.
The tex L3 proof (`proofs_core_lemmas.tex`:484–725) ends at Step 15; the source's Part IV — Steps 16
(Example A), 17 (Example B) and 18, where (S1)–(S2) are defined — is not transcribed as proof steps.
`grep -n "(S1)\|(S2)" sections_v3/*.tex` returns nothing. Examples A and B *are* carried, relocated
into the discussion after `asm:Atau` (model_section.tex:456–459), but the two named sufficient
conditions are carried nowhere.

Two consequences follow, and both are pointer-grade rather than substance-grade:

1. The measured failure is fully on the paper's record; what is lost is the named connection between
   that failure and the two conditions L3 identified as sufficient. A reader of the paper cannot
   recover the connection; a reader of the card can.
2. **Two in-paper sentences now point at content the paper does not contain.**
   `theorem_section.tex:127–129`: *"the discussion after Assumption~\ref{asm:Atau} … names the
   weakest sufficient conditions for the two-round case."* And `theorem_section.tex:446–448`, in
   `sec:not-claimed` item (1): *"…and names the weakest sufficient conditions for the two-round
   case."* The discussion after `asm:Atau` does the first three things those sentences claim (the
   bite is the support condition; a one-round market satisfies it; the no-disclosure structure does
   not) but names no sufficient conditions.

   **Minimal fix, either of:** add (S1)–(S2) to the `asm:Atau` discussion, or reword both sentences
   to *"…and names, on the record, the weakest sufficient conditions for the two-round case."*

*Related mechanism, reported once here rather than per-pointer:* because the tex L3 proof omits the
source's Steps 16–19, **every card pointer into L3's proof by step number has no in-paper anchor** —
"L3 Step 18" (§5 A(τ)) and "`proofs/L3_proof.md` Step 19" (§4.4's `π̄` row, the binding ruling).
This contrasts with P1, where `proofs_existence.tex` declares and delivers 1:1 step numbering with
`P1_proof.md` (Steps 1–20, verified), so every P1 audit citation resolves in the paper. The L3
material itself is not lost: Step 19's degeneracy argument is carried at
`proofs_core_lemmas.tex`:716–724 and again at `model_section.tex`:650–652.

**M-4b — `MIN_CELL_MASS`. MISCITED.**

- Card: *"the 50 `T=10` nodes sit at `Ω = 0.000681`, below `MIN_CELL_MASS` (`HANDOFF_sign.md`
  §8.1)."*
- Section, line 528–529: *"the fifty `T = 10` nodes sit at `Ω = 0.000681`, below the
  implementation's minimum cell mass."*

**Verdict:** MISCITED, and this one I judge *correct as paper prose*. `HANDOFF_sign.md` is an
internal inter-lane record and `MIN_CELL_MASS` an implementation constant; neither belongs in a
department-reviewer-facing section. The number and the comparison — the whole substance — survive.
No fix needed.

**M-4c–e — three further thinnings. MISCITED / OK-RESTRUCTURED.**

- "block 3's implied `[0.997, 1.158]`" → "the separately implied `[0.997, 1.158]`" (block reference
  dropped; the object and its gloss survive). MISCITED.
- "Example A's `|A'_κ| = 0.25`" → "a particular value of `|A'_κ|`" (Example A is a proof-file
  object). OK-RESTRUCTURED.
- "the two prior 'failures' remain misformulated tests; this is the first test that measures A(τ)'s
  own object" → carried in substance as *"Two gates pass first, so the object measured is the one
  Assumption~\ref{asm:Atau} is about"*; the repo-history half is dropped. OK-RESTRUCTURED.

---

**M-5 · `asm:Abr` and its trailing discussion, lines 535–579 · OK-RESTRUCTURED + MISCITED (pointers)**

This covers **checklist item 2**. I compared all five clauses word by word against the card's A(br)
block.

- **(br-i)** representation at both policies, with chord endpoints `π̄(τ)`, `π̄(τ')` and coefficients
  `A'_κ(τ)`, `A'_κ(τ')` — **verbatim in substance**.
- **(br-ii)** κ-localisation, the three support points and the kernel-as-function-of-the-posterior
  not moving with κ, `∂_κ M_P = Δ_m A'_κ C_h(π̄)` exactly with no composition-through-κ remainder,
  the "against the literal display this would restate (br-i)" caveat, the honest reading
  `h = π p(v̂,π)`, "repairs that ambiguity rather than adding a fourth independent restriction",
  "naming the same object as clause (τ-i)", and **"The trailing 'hence' is derivable, not assumed"**
  — all present.
- **(br-iii)** `|A'_κ(τ')| ≤ |A'_κ(τ)|` with the weakest sufficient form equality and the
  reclassification gloss — **verbatim**.
- **(br-iv)** `π̄` as the chord endpoint and **upper support point**, weakly increasing in
  `π̄_pr = P(a=1|D=0)`, *"the same function at `τ` and at `τ'`"*, identity branch excluded as
  degenerate — **verbatim in substance**.
- **(br-v)** `C_h(·)` and the kernel are the same functions of the posterior at both thresholds; the
  "two different functionals and the comparison is meaningless" consequence; `h = π p` with `p`
  priced off a cell whose composition the threshold moves, so "τ-invariance of `h` is real content,
  not bookkeeping" — **verbatim in substance**.

Post-block discussion (lines 568–579), against the card:

- "consumed by leg 3 of Lemma L4 and by Part (B) of Theorem T1, and by nothing else" ✔
- "(br-v) was independently required by three agents, one of whom confirmed that it is not implied by
  (br-i)--(br-iv)" ✔ (card: the T1 proof-reader, the L4 re-deriver as "(br-ii′)", and the T1
  re-deriver who confirmed both required and not implied)
- the ρ sharpening: `ρ := ½A_{1/2} + A_1` provably κ-free, `π̄ = π̄_pr/ρ`, so (br-iv) ⟺
  `ρ(τ')/ρ(τ) ≥ π̄_pr(τ')/π̄_pr(τ)` ✔
- level-symmetric inheritance: `ρ = ½` and `π̄ = 2π̄_pr`, "which forces `π̄_pr ≤ 1/2`, an inherited
  restriction on the domain of Assumption A(τ) that Lemma L4 does not resolve" ✔
- "(br-iii) is the clause with the least justification behind it, and it is the one to attack first"
  ✔

Dropped: *"Canonical name is (br-v); T1's proof carries it as H17"*, and the `rederive/` CHANGE
pointers. **MISCITED**, non-blocking — H17 is a proof-file hypothesis number, and (br-v) is consumed
by name at `proofs_theorem_ge.tex`:208.

Added by the section (not in the card's A(br) block), line 577–579: *"Because (br-i) carries the
representation \eqref{eq:atau} at both thresholds, the record in Remark~\ref{rem:AtauRecord} bears
directly on Assumption~\ref{asm:Abr} as well."* This is an inference the card licenses elsewhere (the
T1 row's (T-11), and the A(τ) note's statement that L4 leg 3 and T1 Part B inherit the
conditionality). It tightens the honesty record rather than loosening it. **OK-RESTRUCTURED.**

---

**M-6 · `def:premium`, lines 618–652 · OK-RESTRUCTURED + one MISCITED**

This is half of **checklist item 9**. Verified against card §4.4: `h = π p` with `h ≥ 0`, `h(0)=0`;
`Δ^act = Δ_m E[h(I_H)] ≥ 0`; `M_F`/`M_P` "each defined when its cell has mass";
`Ω = P(D=1) ∈ [0,1]` factoring as `P(a=1) ω_a`; `ω_a = P(D=1|a=1)` the disclosed share of
engagements; **`π̄` as the upper support point of the pooled engagement posterior in the
representation \eqref{eq:atau}** — the corrected gloss, carried exactly; the mean-vs-`π̄` block
(the share is the *mean*, κ-invariant as a mean-preserving spread, so not the quantity whose
κ-motion L3 describes; strictly below `π̄` in any non-degenerate case; equals `π̄/2` only under
level symmetry `A_0 = A_1`); `S = |∂_κ Δ^act|`, `S_P = |∂_κ M_P|`; the chord display maintained
non-positive with `|C_h|` weakly increasing; `A'_κ` bounded on `[0,1]`; `W_τ`/`W_T` with the worked
`W_T` example, at most 1 when `Ω` rises; `C_τ`/`C_T` with the worked `C_T` example, unsigned; and
the margin-subscript rule with the full `C`-overloading list (`C_h`, `C_j(s)`, `C_F`/`C_P`). The
degeneracy of the mean-reading — point mass at `π̄` with `A'_κ = 0` and zero interior motion for
every kernel, "degenerate, and it is excluded throughout" — is carried in the paragraph immediately
after, lines 650–652. **The π̄ upper-support-point ruling and the mean-vs-π̄ degeneracy note are both
complete.**

Dropped and judged:

- `ω_a` "**the calibration target**" — a substantive descriptor of the object, dropped. Nothing in
  the sections consumes it, and no result depends on it. **MISCITED** (minor).
- "`Ω` is draft_v2's `ω_P` — the O-1 numbers … are all `Ω`-type"; "`ω_a` renamed from bare `ω`";
  "`C_h` = draft_v2's `C(π̄)`, `lem:d1-jensen`". Cross-draft notation mappings and rename history.
  The (C\*) half of the `C_h` row *is* relocated, to `asm:Atau` (line 434). The `Ω`-type
  identification survives implicitly, since `rem:T1record` writes the O-1 numbers as `Ω` values.
  **OK-RESTRUCTURED.**
- The martingale reason for `E[Π_κ] = π̄/2` under level symmetry. The claim is carried; the reason
  is not. **OK-RESTRUCTURED.**

---

**M-7 · `def:theta`, lines 591–616 · OK-RESTRUCTURED**

The other half of **item 9**. Verified against card §4.5: the cutoff vector with its ordering and the
frozen-manuscript mapping; `Θ` nonempty, compact, convex; `ϑ`; `\Tmap` as the outer cutoff
best-response map, **"always written calligraphically, since upright `T` is the filing window"**;
`L_R = sup_R ‖D_k \Tmap‖` required below 1 by AGE; `r_τ = −τ`, `r_T = −T`, higher `r` tighter;
`eq:gPE` with **"the sign written inline rather than carried by a symbol"**; `k̄_x` and `k̄_{κr}`;
`eq:BGE`; the dominance-and-contraction region `R_r` with slack `η_r = g_r^PE − B_r^GE` and **"the
region may be empty"**.

Dropped: the bare sign restrictions `≥ 0` on `k̄_x`/`k̄_{κr}`/`B_r^GE` (all are magnitudes of
magnitudes and non-negative by construction); "C1 needs `g_r^PE > B_r^GE`" (relocated to `prop:C1`
(C-6) ✔); "`η_r > 0` at dominance-and-contraction nodes" (relocated to `rem:C1record` ✔); draft_v2's
`(k_1, k_0, k_D)` names (replaced by "that draft's triple of cutoffs"). **OK-RESTRUCTURED.**

---

**M-8 · A7 satisfiability discussion, lines 400–417 · MISCITED (one scoping addition + pointers)**

This is **checklist item 8**, against card §5's A7 note (ticket 24). Verified present: satisfiability
resolved for A7′; A7′ + a fixed cutoff policy + `Ω > 0` deliver the on-path injective form on
positive-probability flagged tuples with an explicit inverse; **the pro-rata single-Voice menu with
terminal target strictly increasing on all of ℝ, which also satisfies A7-J**; A7-J additionally needs
`b*` strictly increasing off the Voice region, a target flat below the Voice cutoff breaking it in an
executed check producing **forty collisions** while leaving A7′ intact; the **failure boundary** in
full — a binding stake cap, quantized stakes, a composed target repeating values across Voice-plan
switches, `Ω = 0`, and policy dependence when the condition is stated only at one equilibrium's
cutoffs; and "Menus satisfying A7′ are fully separating on the flagged set, so the burden moves to
the incentive compatibility of Proposition P1, not away." The turn-2 proof-read note is also complete
(lines 381–383 and 403–406): the weak wording permits two `(j,s)` pairs with different pooled paths —
L2's first failure case; the tuple is continuum-valued as a tuple with coordinates able to trade the
burden; injectivity plus measurability already gives the measurable inverse on standard Borel spaces.

**The one difference:** the card states the failure-boundary list unscoped, immediately after the
A7-J sentence. The section writes *"The failure boundary **for the on-path form** is …"* (line 412).
Two of the five items (a binding stake cap, quantized stakes) break both forms, so the scoping
narrows what the card asserts about A7-J.

**Verdict: MISCITED** — an attribution narrowed, not a clause dropped. Nothing consumes the failure
boundary; A7-J's own additional requirement is stated separately and correctly two sentences earlier.
**Minimal fix:** delete "for the on-path form".

Also dropped: the adversarial attack verdict **SURVIVES WITH REPAIRS** and the
`proofs/A7_construction.md` / `proofs/A7_attack_verdict.md` pointers. **MISCITED**, non-blocking.

---

**M-9 · The eight displays · no difference**

**Checklist item 7.** Each checked symbol for symbol against the card's §4.1–§4.5 originals.

| Display | Line | Card source | Result |
|---|---|---|---|
| `eq:entry` | 126–130 | §4.3 `p(I)` row | identical, including the `∈ (0,1)` |
| `eq:Y` | 132–135 | §4.3 `B`, `Y` row | identical |
| `eq:Uj` | 155–159 | §4.3 `U_j` row | identical, `− a_j C_j(s)` term carried |
| `eq:m0` | 184–187 | §4.1 `m_0, m_1` row | identical, with the `m̄(I) ≥ 0` consequence and the nonexistence/three-root gloss |
| `eq:atau` | 428–431 | §5 A(τ) | identical |
| `eq:chord` | 637–640 | §4.4 `C_h` row | identical |
| `eq:gPE` | 601–604 | §4.5 `g_r^PE` row | identical |
| `eq:BGE` | 608–613 | §4.5 `B_r^GE` row | identical, all three groups |

---

**M-10 · `sections_v3/v3_macros.tex`, lines 2–3 · MISCITED (provenance)**

- File header: *"transcribed verbatim from `research/model_v4/model_v4.tex` **lines 28-37** (card
  stamp **2026-08-23**)."*
- Actual: the macro block is `model_v4.tex` **lines 42–51**; lines 28–37 are `\documentclass` and
  `\usepackage` lines. And `model_v4.tex` carries stamp **2026-08-27**, not 2026-08-23.

The macro *bodies* are correct: I diffed them against `model_v4.tex`:42–51 and all ten are identical,
the single deliberate change being `\providecommand` for `\Tmap` (documented in the same header, and
see **F-1**). `\Atau` expands to `\mathrm{A}(\tau)` and `\Abr` to `\mathrm{A}(\mathrm{br})` — the
card's own forms. `\resultstatus` renders as a visible `\textbf{Status.}` paragraph, which is what
gate (b) requires.

**Verdict: MISCITED** on both counts. **Minimal fix:** amend the header to "lines 42–51 (card stamp
2026-08-27)".

---

### 1.2 `sections_v3/theorem_section.tex`

---

**T-1 · `lem:D1`, lines 30–49 · OK-RESTRUCTURED**

**Checklist item 4, D1 half.** All card-row clauses land: A1, A2′, A4, A5; the table restrictions;
§3(i)'s cutoff selection map (as `Definition~\ref{def:cpbe}\,(i)`); **both** §4.3 conventions named
explicitly in the statement (`P_{-1}^P = E[Y]` and `P_ND = P^P_{f^-}`), and defined in full at
`def:prices` including the "not a never-disclosed counterfactual" reading; the **Borel-for-Exit**
addition, named in the statement *with its scope* ("needed only for part (c) below because pooled
pricing integrates over every type") and stated in full at (TR-ii) with the "genuine addition for
Exit" reason; and the **`I_H` content** addition, named and supplied by `def:prices`. All three
conclusion parts are present at full strength: (a) measurable *and* maps every control-node history
into exactly one cell; (b) the clock equivalence for every Voice plan; (c) `B^F, R_d, R, J` with
`eq:runup-jump`.

**The one difference:** the card names "the **§4.1/§4.2** table restrictions"; the statement cites
all of `asm:TR`, which includes (TR-iv)'s §4.3 pricing and entry conventions. D1 over-assumes
relative to its card row. Gate (a) tests clause *completeness*, not minimality, and part (c) is a
statement about prices in any case, so nothing is weakened in substance. Worth noting that the
crosswalk's own row D1.5 says "(TR-i)–(TR-iii)", understating what the statement actually cites.
**OK-RESTRUCTURED.**

---

**T-2 · `lem:L1`, lines 57–71 · no difference**

**Checklist item 4, L1 half.** Every card clause: D1; the §4.3/§4.4 definitions; **A5, which pins
*the* version of `E[Y|I]`** — the version-pinning gloss carried verbatim; **A2′ together with (TR-i),
under which `Δ_m` is finite**; **A1, which puts every object on one probability space**. Conclusion
`eq:L1` at `0 < Ω < 1`; both degenerate branches; **"the average over the null cell is *undefined
rather than imputed*"**; and the closing **"That last clause is a non-identification statement, and it
is proved rather than asserted."** The proof discharges the non-identification clause as a genuine
argument at `proofs_core_lemmas.tex`:228–242, exhibiting the one-parameter family of versions.
Complete.

---

**T-3 · `lem:L2`, lines 79–93 · OK-RESTRUCTURED**

All card clauses land, including "at fixed cutoff **and execution** policies", **A7′ named as the
form** with the "consumed almost surely on the flagged set" reading and its reason in a footnote (the
footnote carries a *reading*, not conditionality — permitted), D1, the no-feedback timing, `Ω > 0`,
and the entry rule "carried as bookkeeping" with the "or any rule with the two properties named in
the proof" alternative. Same TR-bundle over-assumption as T-1 (card: §4.1/§4.2). **OK-RESTRUCTURED.**

---

**T-4 · `lem:L3`, lines 103–122 · no difference**

Every card clause: A(τ) with both new clauses named; `h(0)=0`; κ-free pooled mass and engagement
moment at fixed policies; D1 **by statement**; the minimal regularity with **Darboux doing the rest
and no continuity of `h''`**; the part-(c)-only clauses (second-order Peano expansion at `0+`, one and
the same kernel along the shrinking family); the **L4-seam** clause (`|A'_κ|` bounded *uniformly in
`π̄`*); all three conclusions with "an identity, not an approximation" on (b); and **"an 'if' and
never an 'iff'"** with its reason. Complete.

---

**T-5 · `lem:L4` leg 2, lines 141–143 · OK-RESTRUCTURED**

**Checklist item 12(a).**

- Card: *"the pooled engagement **share** falls, `π̄_pr(τ') ≤ π̄_pr(τ)`, with an exact identity for
  the gap"*.
- Section: *"…with an exact identity for the difference between the two shares."*

The writers declare the substitution at crosswalk row L4.7, citing CONTEXT.md's _Avoid_ on "gap".
**My judgement: the substitution was not required, and it changed no substance.** The _Avoid_ sits
under the **Whitespace** entry and targets positioning language ("a gap in the literature");
CONTEXT.md's own **Premium wedge** entry uses "gap" arithmetically (*"The gap in expected takeover
premium…"*), as does the card (§4.3's `U_j` row: *"Card gap closed here"*). The replacement names
exactly the object the proof produces: `eq:L4-share` at `proofs_core_lemmas.tex`:827–831 gives
`π̄_pr(τ) − π̄_pr(τ') = (ν/ρ_P)(1 − π̄_pr(τ'))`, an exact identity for the difference between the
two shares. All other leg-1/2/3 clauses and the two hypothesis lists check out, including
**"Nestedness is a *conclusion* of leg 1, not a hypothesis of it"** and the **sign-half-unused**
qualifier on `C_h ≤ 0`. **OK-RESTRUCTURED.**

---

**T-6 · `prop:P1`, lines 174–270 · no difference — gate (a)'s known trap is COMPLETE**

I walked contract gate (a)'s P1 trap list item by item against the statement. Every one lands:

| Card / contract clause | Landed |
|---|---|
| A7-J named as the joint form | (P-6), with the whole-flagged-pair-set and "including pairs no cutoff vector selects" |
| form-mismatch history available in text or footnote | footnote on (P-6) — contract explicitly permits either |
| h.16 continuation-cost clause | (P-10), with the trivially-true-on-single-Voice, live-only-on-multi-Voice, what-it-buys, no-date-0-optimality-to-fall-back-on, and **requirement (ii) fails at that node** consequences |
| two-readings timing convention | (P-12) plus `rem:Ctiming`, with "the result does not depend on the choice" |
| D1's hypotheses travelling | (P-7), the travelling clause emphasised |
| flag-terminates-the-pooled-round reading | (P-8), read together with `asm:flagterm` |
| definitional round-2 action-set hypothesis | (P-9), including "not a closure condition; the closure form is jointly unsatisfiable with finiteness, by cardinality" |
| §4.1–§4.3 table-restrictions block | (P-13), enumerated: (TR-iv)'s `Y`/price/entry, (TR-ii)'s Borel-for-Exit **needed directly and not by way of D1**, (TR-iii)'s `D=1⇒a=1` and the `c/f/B^F/Q^F/b*` definitions and `∂_s B_j ≥ 0` for Voice, (TR-i)'s distributional forms with `Δ_m > 0` |
| `m_0 ≥ 0` | (P-11) → `eq:m0` |
| `κ ∈ [0,1]` via the extension route | (ii), with boundary supports, "off nature's path rather than off the players'", no §3(vi) requirement, read by no step, **"No cut to `κ ∈ [0,1)` is taken"**, and the false-at-`κ=1` claim **withdrawn** |
| one-family / every-`k` / positive-probability off-path belief clause | (i), all three, with the reason (deviation payoffs defining `\Tmap` read off-path pooled histories) |
| A7-J supplying flagged-tuple beliefs on and off path as a **version** | (iii), including "a version is what a conditional law is", "any a.e.-equal version serves (iii) and (vi) equally", and "no tuple outside that image arises" by (P-9) |
| sequentially-optimal flagged component at **every** flagged pair | (v), with the price-invariance / order-cancels / (P-10)-makes-what-remains-constant mechanism |
| A5 **not assumed** (derived from `m_0 ≥ 0`) | trailing ¶1, all three parts (existence and uniqueness, continuity, measurable selection from A7-J + (TR-ii)) |
| A6 read as the tie-break-and-corner selection | trailing ¶2, with "without which a correspondence cannot be called continuous" and `Θ` nonempty per `def:theta` |
| A8-at-equilibrium, with H-ord for the single-threshold restatement | final ¶, H-ord named as Voice stake monotonicity across plans, plus the upper-set engagement-flag hypothesis |
| uniqueness not claimed | final sentence, and again at `def:cpbe` and `sec:not-claimed` |

The conclusion stem carries **"at every `κ ∈ [0,1]`"** in emphasis. **Complete; no difference.**

---

**T-7 · `rem:P1record`, lines 275–297 · no substantive difference**

Card's P1 numerical block: four sweep-unresolved nodes at `κ ∈ {0.15, 0.85} × (τ,T) ∈ {(0.05,5),
(0.075,1)}`, **STILL UNRESOLVED after 30 seeds each**, payoff-scale residual `3.1e-4`–`1.5e-3`
against a `1e-9` criterion, cutoff-scale `1e-14`–`1e-11`, A3 and A6 proxies pass at every achieving
seed, **UNCHECKED**, and the label resting on the proof plus the two 2026-08-25 passes rather than the
grid. All present, with the JSON named as a `\texttt{}` string (the `.py` is not named — trivial).

The section adds a cross-reference the card licenses: *"which, as Remark~\ref{rem:A3record} explains,
is not evidence that those hypotheses hold: the proxies are local screens…"*. Card §5's A3 note says
exactly this ("both are silent on these findings"). The second paragraph carries card §9 item 4's
"no label moves … P1 stays PROVED as a conditional, in the A(τ) pattern" and the relocated 4(c)
material (`23` of `27`, two fixed points at the worst probed node). **Complete.**

**Note for item 13: this remark contains no overfull hbox.** See **F-2**.

---

**T-8 · `thm:T1`, lines 302–339 · no difference**

Every clause of the card's T1 row lands: the fixed-policy frame with `0 < Ω < 1` and `S_P > 0`;
Part (A) with the exact factorisation **and** the total-variation aggregate over any κ-grid with no
differentiability required; Part (B) with `eq:T1B`, **"because *both* ratios lie in `[0,1]`"** and
**"No dominance condition is needed"**; Part (C) as an **iff**, with `W_T ≤ 1` **proved** from the
clock equivalence and the monotone Voice stake path, `C_T` **unsigned**, and the equivalent form
`eq:T1C` carrying all three quantifier clauses **verbatim** — "holds *on average along the tightening
path*, integrated over `[-T,-T']`, and exactly in the infinitesimal limit; read pointwise,
\eqref{eq:T1C} is false". Hypotheses (T-1)–(T-15) match the card's list one for one, including
PE-Ω's three parts (derivable rather than assumed; exactly what fails in GE; the term C1 bounds),
(T-8)'s "no standing hypothesis supplies this … carried in the proof", (T-9)'s π̄ ruling, (T-11) at
the threshold pair, (T-14) scoped to the local form only, and (T-15) "confirmed non-load-bearing".
Closing: **"No unconditional window sign is claimed."**

---

**T-9 · `rem:T1record`, lines 349–369 · MISCITED (records) + OK-RESTRUCTURED + one UNCHECKED**

**Checklist item 1.** Checked against card §9 item 3 and the card's §4.4/O-1 material.

*Verified exact:*

- The four ratios: `1.06397`, `1.18373`, `1.13631`, `0.37798` — **all four, exact.**
- The four `Ω` values: `0.037252`, `0.128950`, `0.285804`, `0.50` — **all four, exact.**
- "For Part~(C) the genuine window-margin record is **block 4 of the executed T1 check**: `W_T C_T <
  1` at **every checked node** at this calibration, with an **`H = 10` corner caveat**" — the whole
  claim, present.
- "That is NUMERICAL node evidence at one calibration and not a sign theorem, which Part~(C) does not
  claim."
- The disclosure-regime/window distinction, in full: the ratios "are regime-comparison composition
  outcomes; they are not `W_T C_T` and they measure no window pair"; "The analogy is useful only
  because it shows that a composition factor can exceed one, which is what motivates the genuine
  window-margin 'if and only if' above"; "the O-1 cut at `Ω* ≈ 0.343` is a disclosure-regime
  boundary, not a window boundary."

*Difference (i) — record names thinned. MISCITED.* The card names `t2_t1_check` block 4,
`HANDOFF_sign.md` §8.1 for the `H=10` caveat, `HANDOFF_sign.md` §3 and
`quality_reports/fixes/t1_o1_rerun_check.py` for the `Ω*` cut. The section writes "block 4 of the
executed T1 check" and "recorded in the handoff", and names no script. The substance survives
entirely. This is the *only* one of the five numerical-record remarks that does not give its records
as `\texttt{}` strings — `rem:AtauRecord`, `rem:A6record`, `rem:P1record` and `rem:C1record` all do.
**Minimal fix:** name `t2_t1_check` and `t1_o1_rerun_check.py` as `\texttt{}` strings for
consistency; "the handoff" is fine as paper prose (see M-4b).

*Difference (ii) — the O-1 descriptor. OK-RESTRUCTURED.* Card: O-1 "compares the public buy flagged
versus pooled **at fixed policies** in the static repo model." Section: "is a *disclosure-regime*
comparison **at a fixed filing window** in the static repository model." The card's descriptor
("public buy flagged versus pooled", "at fixed policies") is replaced by CONTEXT.md's definitional
property of the disclosure-regime margin (*"the comparison that toggles whether the market sees the
flag, at a fixed filing window"*). Both are true of O-1 and the substitute is glossary-sourced.

*Difference (iii) — a card-internal tension the section inherits. UNCHECKED, card-side.* Card §4.4's
`Ω` row says *"the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the **≈ 0.29 cut** are all Ω-type"*;
card §9 item 3 says *"The O-1 cut **Ω\* ≈ 0.343**"*. The section carries `0.343`, following §9 item 3
— the O-1-specific and later-dated text. I cannot determine from the card alone whether `≈ 0.29` and
`≈ 0.343` are two different objects or an internal inconsistency, so I do not adjudicate it. The
section's choice is defensible either way. **Flagged for the orchestrator.**

*Also checked, gate (d):* "window test" is the one occurrence in all six files, and it is used to
*name and reject* the misreading ("are sometimes read as a window test, is a *disclosure-regime*
comparison"), which is exactly CONTEXT.md's own scoping of the _Avoid_ ("window test (when a regime
comparison is meant)"). **Not a violation.**

---

**T-10 · `prop:C1` closing sentence, line 401 · MISCITED**

**Checklist item 10.** I determined which object the card means, as asked.

- Card §6 C1 row, final sentence: *"The sign-coherence hypothesis is confirmed unused in the boxed
  conclusion."*
- Card §6 C1 row, evidence chain: *"re-derivation PASS 2026-08-21 (PROVED-WITH-CHANGES: N1, N2
  added; **H8 unused**; …)"*.
- `proofs/C1_proof.md`:141 — *"**H8 — Sign coherence (used only to name `g_r^PE`, never to reach the
  conclusion).**"*
- `rederive/C1_rederivation.md`:15 — *"one is **confirmed unused** for the boxed conclusion (H8,
  exactly as the sheet says)"*.

**The card means H8.** H8 is the agreement of the *fixed-policy* liquidity-derivative sign with the
*equilibrium* sign. Assumption AGE's third clause is a different object — *sign constancy*, that the
equilibrium sign is constant on `R` — and AGE has no clause named "sign coherence" at all.

- Section, line 401: *"The sign-coherence hypothesis **of Assumption~\ref{asm:AGE}** is confirmed
  unused in this conclusion."*

The statement attributes the card's H8 finding to AGE. However, the proofs file discharges **both**
objects and keeps them apart, at `proofs_theorem_ge.tex`:713–724: *"The constancy clause of
Assumption~\ref{asm:AGE} … is not used: Step~7 derives constancy on a connected neighbourhood from
hypotheses~(C-5) and~(C-2) … **Nor is the coherence of the fixed-policy sign with the equilibrium sign
used.** That coherence has one job and it is a job of naming…"* — which is H8, correctly identified
and correctly discharged, with its naming role spelled out exactly as `C1_proof.md`:141 has it.

**Verdict: MISCITED, not WRONG.** Two reasons. The card's H8 record *does* exist in the sections — at
the proof site rather than the statement site. And the sentence as written asserts nothing false:
AGE's constancy clause is likewise unused, and the proof says so. What is off is the label on the
card's finding at the statement site.

The crosswalk propagates the same conflation rather than hiding it — §0 row 27: *"C1's row consumes
AGE's contraction clause **and the sign-coherence clause**"*. So this is one traceable slip, not two.

**Minimal fix (propose only; I made no edit):** replace line 401 with

> The sign-coherence hypothesis --- that the fixed-policy liquidity-derivative sign agrees with the
> equilibrium sign --- is confirmed unused in this conclusion; so is the sign-constancy clause of
> Assumption~\ref{asm:AGE}.

All of (C-1)–(C-7) are otherwise verbatim against the card row, including (C-1)'s three parts (one
fixed norm convention, induced operator norm with its dual pairings, "a mismatched pairing silently
voids the implication"), (C-2)'s both-coordinates and `κ ∉ {0,1}`, (C-5)'s explicit distinction of
`S^GE` from `def:premium`'s fixed-policy `S`, and (C-7)'s both halves.

---

**T-11 · `rem:C1record`, lines 408–430 · MISCITED (attribution) — item 3 answered YES**

**Checklist item 3: does the card actually record this retirement?** **Yes.** `MODEL_CARD.md`:485–489,
immediately below the §6 ledger table:

> The old aspiration line ("C1 PROVED on a named nonempty region, NUMERICAL off-region") is
> **retired as structurally undeliverable as worded** (the C1 proof-read's ruling): the deliverables
> are the three objects the C1 row now carries — the implication PROVED with the region as a
> hypothesis, the dominance-and-contraction nodes NUMERICAL, and a named-region promotion an open
> question with the D8 ε-ball pattern as its template.

Section, lines 424–429, carries all four parts: the retirement with the phrase **"retired as
structurally undeliverable as worded"** verbatim, and the three deliverables. Dropped: the
attribution "(the C1 proof-read's ruling)". **MISCITED**, minor.

Every number in the first paragraph checks out against the card's C1 Label cell: 18 of 80; the
largest contiguous block `T = 5`, τ-percentiles `{50,70,90}`, `κ ∈ {0.65, 0.75, 0.85}`; `η_r` minimum
`0.0595`, median `0.3467`; `L_R ∈ [0.264, 0.501]` everywhere; the executed committed check
independently re-run on 2026-08-22 with all values reproducing; "they verify the two pointwise
inequalities `L_R < 1` and `η_r > 0` together with supporting diagnostics" and **"they do *not*
verify the full antecedent (C-1)--(C-7) … and they do *not* exhibit a named nonempty region"**;
**"A dominance-and-contraction node is not a fifth honesty label"**; both records named; and the
re-derivation bonus `B_r^GE = O((1−L_R)^{-3})` with the cubic-bounded-away gloss.

---

**T-12 · `sec:not-claimed`, lines 432–466 · OK-RESTRUCTURED + MISCITED (one dangling pointer)**

**Checklist item 5 — the prose list, item for item.** Card §9 preamble carries eleven items; the
section carries all eleven, in card order:

| # | Card | Section | |
|---|---|---|---|
| 1 | a global window-margin attenuation sign | identical | ✔ |
| 2 | κ-invariance of `J` | "κ-invariance of the filing-day jump `J`" | ✔ |
| 3 | equilibrium uniqueness | identical | ✔ |
| 4 | a nonempty GE region as a theorem | "a nonempty general-equilibrium region as a theorem" | ✔ |
| 5 | endogenous filing before the deadline | identical | ✔ |
| 6 | noisy or partially revealing flagged-round trading | identical | ✔ |
| 7 | continuous-time execution | identical | ✔ |
| 8 | welfare or optimal rule design | identical | ✔ |
| 9 | that draft_v2's hump result survives | "that the frozen manuscript's hump result survives" | ✔ |
| 10 | that the prior calibration (`Ω ≈ 0.037`) is economically meaningful | "at `Ω ≈ 0.037`" | ✔ |
| 11 | any empirical value for `ω_a` | "for the disclosed share of engagements `ω_a`" | ✔ |

Only substitution: "draft_v2's" → "the frozen manuscript's", consistent throughout the six files
(draft_v2 is an internal repo name). **OK-RESTRUCTURED.** The card's meta-note that A7 satisfiability
"was never listed here and is now resolved" is not carried into the list, correctly — it is card
bookkeeping, and the resolution itself is stated at `model_section.tex`:406.

**Checklist item 6 — the open-questions list.** The card has four §9 items; the section carries three
(card 1, 2, 4) and relocates item 3's substance into `rem:T1record`. The relocation is announced in
the section's own lead-in (lines 442–443): *"Three questions remain open, in whole or in part … The
third was answered in substance on 2026-08-27; what survives of it is scoped below."*

*Was anything of card item 3 lost in the move?* I compared its eight elements against
`rem:T1record`: the "disclosure-regime analogy, not a window-margin test" framing ✔; the four ratios
✔; the four `Ω` values ✔; "regime-comparison composition outcomes … not `W_T C_T` … measure no window
pair" ✔; the composition-factor-can-exceed-one motivation for T1's genuine iff ✔; the block-4
`W_T C_T < 1` record with the `H = 10` caveat ✔; the `Ω* ≈ 0.343` disclosure-regime boundary ✔.
**Nothing substantive was lost.** What thinned is covered at **T-9(i)** (record names) and
**T-9(ii)** (the descriptor swap). The card's "this is a known fact on file, not a claim the card
makes" is card bookkeeping about why the item sits in §9 and does not translate into paper prose;
the section's "One distinction is worth stating because it is easy to lose" does the same work.

*Are items 1/2/4 complete?*

- **Item (1)** (card item 1): the support condition as the entire remaining bite; the one-round market
  that satisfies it; the no-disclosure structure that does not; L3, L4 leg 3 and T1 Part (B) all
  conditional on it; **"the largest single conditionality the ledger carries"** ✔. **One dangling
  pointer** — see **M-4a**: the claim that the paper "names the weakest sufficient conditions for the
  two-round case" is not met by the paper (line 448, and again at line 129). **MISCITED.**
- **Item (2)** (card item 2): A7′ menus fully separating; the burden did not disappear when
  satisfiability was resolved, it **moved** to incentive compatibility, which P1 does not settle; and
  the "relatedly" clause that P1 does not claim an A8-satisfying equilibrium exists, only that A8
  holding *at* an exhibited equilibrium puts both cells on path ✔. Complete. ("P1-adjacent" dropped —
  a card tag, not content.)
- **Item (3)** (card item 4): answered-in-substance status with the date; locus corrected;
  cross-reference to `rem:A6record`; and all three still-open parts — **(a)** a constructive `Θ` or
  the *t*-constrained Kakutani route which removes the continuity half, the repair identified rather
  than executed; **(b)** the complementary menu class with the implemented menu as an instance for
  its collapse face, where the collapse-face clause may be satisfiable; **(c)** nonexistence, neither
  claimed nor shown ✔. Card item 4(c)'s supporting numbers (`23/27`, two surviving fixed points) are
  relocated to `rem:P1record` and are present ✔. Dropped: the proof-local IDs "Step 18" and "h.6".
  **The (a)/(b)/(c) scoping is complete.**

---

### 1.3 `sections_v3/proofs_section.tex`

Three `\input` lines and the `\section{Proofs}` / `sec:proofs` pair that every result statement points
at. The single permitted plumbing edit, declared at `labels_map.md`:9–12. **No difference.**

---

### 1.4 `sections_v3/proofs_core_lemmas.tex`

---

**P-1 · D1 proof, lines 19–178 · no difference at transcription grain**

Thirteen steps carrying the source argument, with the three turn-2 repairs the card names visible in
the text: the **public-flag bridge** made explicit and identified as what part (a) turns on
(Step 6); `B^F` continuum-valued with `eq:D1-BFmeas` supplying its measurability (Step 10); and the
`P_{-1}^P` convention consumed where `T = H` forces `c = 0` (Step 11). The `P_ND`
same-order-flow reading is carried as load-bearing at Step 12 ("under a never-disclosed
counterfactual reading the middle terms would not cancel"). Step 9 derives why the core carries
`b_0 < τ`, and Step 13 records that no probability restriction entered Steps 4–9, which is the card's
A8 gloss. No new mathematics, no dropped step the statement needs.

---

**P-2 · L3 proof Step 6, lines 543–548 · OK-RESTRUCTURED — flagged as the one added argument**

The MVT chain (tex Steps 1–6) is a faithful transcription of `L3_proof.md` Steps 1–6, with the
source's generic `g` specialised to `h` (the source's Step 10 does that specialisation; the tex folds
it in). Verified line by line: the first difference `δ_h`, the arithmetic cancellation leaving the
coefficient `−2`, the continuity/differentiability of `δ_h`, the first MVT giving `t_1 ∈ (0, π̄/2)`,
the containment `[t_1, t_1 + π̄/2] ⊂ (0, π̄)`, the second MVT giving `ζ`, and the chained
`C_h(π̄) = ¼π̄²h''(ζ)` with "the identity is exact" and "every use of `h` beyond continuity was at
points of the *open* interval".

**The addition:** lines 543–548 supply a **Darboux route** — *"The statement's gloss that Darboux's
theorem does the rest names the alternative route … `h''` is a derivative on `(0,π̄)` and therefore
has the intermediate value property, so the arithmetic mean of its values at two points of a compact
subinterval is itself a value of `h''` at some point between them. Neither route uses continuity of
`h''`, which is why the hypothesis does not carry it."* `grep -i darboux proofs/L3_proof.md` returns
nothing: this argument is **not in the source proof**.

**Verdict: OK-RESTRUCTURED, flagged.** Three reasons it does not rise higher. It discharges a gloss
the **card's own L3 row** asserts ("Darboux does the rest, no continuity of `h''`"), which the
statement at `lem:L3`:109–110 must therefore carry and which would otherwise stand unexplained. It is
presented as *the alternative route* and is not load-bearing — the MVT chain is the proof. And it is
sound as stated. **This is the only place in the three proof files where the tex supplies an argument
the source does not carry;** the orchestrator may want it either sourced or trimmed.

---

**P-3 · L3 proof scope, lines 484–725 · MISCITED (mechanism, reported once)**

The tex L3 proof runs Steps 1–15 and stops. The source's Part IV — Steps 16 (Example A), 17
(Example B), 18 (the OPEN two-round question, where (S1)–(S2) are defined) — and Step 19 (the `π̄`
ruling) are **relocated rather than transcribed**: Examples A and B into the `asm:Atau` discussion
(`model_section.tex`:456–459), Step 19's degeneracy argument into tex Step 15's closing
(`proofs_core_lemmas.tex`:716–724) and again at `model_section.tex`:650–652. **(S1)–(S2) are
relocated nowhere.** Consequence and fix: see **M-4a**. Reported here once so it is not double-counted.

---

**P-4 · L4 proof, lines 727–948 · no difference**

Seventeen steps. Leg 1's inclusion derived (Step 4) with nestedness explicitly a *conclusion*; leg 2's
exact identity at `eq:L4-share` — matching the statement's "the difference between the two shares"
(T-5); Step 11 recording why engagement share one delivers leg 2 unconditionally and what a weakened
Step 5 would cost; Step 14 recording that **only the magnitude half** of the maintained orientation is
read and **"The sign half `C_h ≤ 0` is consumed at no step of this leg"**, matching the card row;
Step 15 recording that (br-iii) cannot be dispensed with; Step 17 handling the vanishing-chord
equality case. The closing paragraph carries the three limits (fixed policies with the concrete
re-optimisation counterexample; no strict inequality; nothing about the window margin).

---

### 1.5 `sections_v3/proofs_existence.tex`

---

**P-5 · The h → P register, header lines 12–20 · verified, no difference**

The header maps `P1_proof.md`'s h.1–h.17 onto the statement's (P-1)–(P-13) plus the two non-hypothesis
destinations. I verified the map against the source's hypothesis list and against where each is
actually consumed. h.5 (A5) is marked **STRUCK** and lands in the trailing "A5 is not assumed"
paragraph — correct, and the proof derives all three of A5's contents (Steps 7, 8, 6(c)). h.8 (A8),
h.13 (H-ord) and h.15 (upper-set engagement flag) land in the final A8 paragraph and are consumed at
Steps 19–20 — correct, and Step 20 names which of the three the standing hypotheses supply. Every
(P-n) is consumed at a named step, or its non-consumption is declared: **(P-10) is explicitly not
consumed under the sunk reading** (Step 12(d), "Under the sunk reading it is not consumed at all"),
and **(P-5)'s two halves are separated** — the ordering and self-map content *derived* at Step 13,
the bracket and continuity *assumed* at Steps 14 and 15.

The header's claim that **"Step numbering is 1:1 with the source (Steps 1-20, Parts A-F)"** is
correct: I checked both step lists.

---

**P-5b · P1 proof Step 9, lines 312–459 · no difference**

Step 9 carries statement clauses (i) and (ii) and I read all four sub-blocks. **(a)** defines
*reachability* as a whole-history property of the menu and the noise law alone — explicitly
independent of `k` and of the perturbation stage — and separates the noise *alphabet* (finite at
every κ, which is all Step 3 needs) from `supp(z_d)` (the subset carrying positive probability at the
maintained κ, which is what a zero-probability argument must be quantified over). **(b)** fixes the
one family at `eq:P1-wn` with `t_n = J/n ↓ 0` (and says why the mass is not written with a Greek
letter: `ε` is the signal noise), gives the stage-`n` joint density `eq:P1-mun`, and splits on the
denominator `eq:P1-Zn`: at `Λ_k > 0` dominated convergence with an explicit integrable envelope; at
`Λ_k = 0` the limit is exact, free of `n`, and **does not depend on `k`** — *"which is what makes one
family serve at every `k ∈ Θ`"*, the card's own clause, derived rather than asserted. The block also
argues why the **joint** posterior is required (π is a functional of the plan posterior, `v̂` of the
signal posterior; integrating the signal out first leaves `v̂` undefined) and why it is load-bearing
where least obvious (Step 13 evaluates the payoff to plans carrying zero probability under `k`, whose
execution bracket reads `k`-null histories). **(c)** supplies the reference-belief root convention,
argues that `E[Y]` will **not** serve because it is in general not a root of `P_I` at any belief
while the conclusion says "prices at their inner fixed points" without qualification, and admits
without hedging that the choice can move a component of `\Tmap`. **(d)** handles `κ ∈ {0,1}` exactly
as card clause (ii) does, including *"no cut to `κ ∈ [0,1)` anywhere"*, the extension framing, the
withdrawn false claim, and *"Nothing here asserts that the flagged cell carries positive probability
at `κ = 1`."*

Incidentally this closes a loose end in **M-3**: `Λ_k` and `Λ_u` are *defined* at lines 389–392, so
`rem:A6record`'s rendering of the card's `Λ_k(h)` as "the reaching weight" is a paper-prose choice
with the symbol available in the proof, not an anchor loss.

---

**P-6 · P1 proof Step 12, lines 540–689 · deep sample — faithful, two differences**

Compared clause by clause against `P1_proof.md`:659–773.

*Carried in full:* the quantification over **every** flagged pair with no assumption that `j = j_k(s)`
and the reason it can be ("without appealing to date-0 optimality"); the class `Q_j(s)` and the
shared-path derivation of `c_{j'} = c_j`, `f_{j'} = f_j`, `B^F_{j'} = B^F_j`, `a_{j'} = a_j = 1`; the
deviation tuple differing in the `Q^F` coordinate alone and lying in the image; **(a)** price
invariance `eq:P1-PFinv` with uniqueness of the inner root making `P^F(s)` a number rather than a
selection; **(b)** the `E[Y|·] = P^F(s)` valuation and *"No informational rent survives into round 2:
full separation is what A7-J buys, and \eqref{eq:P1-EYflag} is what it costs"*; **(c)** the
cancellation of every appearance of `Q^F_{j'}` and with it `b^*_{j'}`; **(d)** both readings, the sunk
reading constant outright, the plan-completion reading closed by (P-10), and the convention-free
conclusion; the **"where (P-10) bites"** paragraph, including the selected-`j` case where date-0
optimality already does the work and the non-selected case where it does not; the **refutation note**
that a class with differing *trading* terms cannot be built (`δ = 0` necessarily); and the **converse**
about (P-9), with the off-image belief problem, "*a* sufficient condition" not the weakest, and the
question declared **open**.

*Difference (i) — line 625. OK-RESTRUCTURED.*

- Source, `P1_proof.md`:710: *"so on flagged plans `$U_{j}(s;k)=B_j^F(s)P^F(s)-C_j(s)-E_j(s;k)$`"*
- Tex, line 625: *"so on flagged plans `$U_{j'}(s;k) = B_j^F(s)P^F(s) - C_{j'}(s) - E_j(s;k)$`"*

The tex's indexing is the consistent one for a general class member, and it matches the **source's own
next paragraph** (`P1_proof.md`:726: *"by (c) `$U_{j'}=B_j^FP^F-C_{j'}-E_j$` within the class"*).
This is a source-typo correction, not new mathematics. Downstream use is consistent: the tex's Step 15
(line 823) reads the same display back with the `j'` indexing.

*Difference (ii) — lines 577–582. OK-RESTRUCTURED.* The tex adds, at `eq:P1-PFinv`: *"It is
Assumption~\ref{asm:A7J} (A7-J) that pins the belief at the same signal for every class member …
The argument at this display is where the joint form of the injectivity hypothesis is indispensable
and its on-path form … is not enough: the tuples in question are generated by pairs the cutoff vector
need not select."* Sourced from the card's P1 row ("the form the proof consumes **where it pins
off-path flagged beliefs**") and from the source's own (a). It makes the form-mismatch history's
locus visible at the step that turns on it. **Non-blocking; an improvement.**

---

**P-7 · P1 proof Step 18, lines 897–912 · no silent strengthening**

Titled *"Step 18 (a strengthening recorded here, **not part of the proposition**)"* and closing
*"Definition~\ref{def:cpbe} fixes the Brouwer route for this proposition, so this is a remark and not
a part of the claim."* It states exactly what the Kakutani route removes (condition (ii) of Step 15
and A6's continuity clause) and what it does **not** remove (condition (i) and Step 14's bracket) —
matching card §5's A6 note ("Repairs on file, both outside §3's declared Brouwer-with-one-fixed-family
route: the *t*-constrained game + Kakutani + `t ↓ 0` (`proofs/P1_proof.md` Step 18)"). **No
difference.**

---

**P-8 · P1 proof Step 15 and the Scope block, lines 777–833 and 969–1024 · no difference**

Step 15 declares precisely where (P-5) assumes rather than derives, names (i) joint continuity and
(ii) transversality as the weakest replacement pair, and records — honestly and unprompted — that
plateaus are **structural** on exactly the menus (P-10) exists for, so on multi-Voice shared-path
menus (P-5) "is being assumed at a configuration where its own named sufficient condition provably
fails". It then points at `rem:A6record` for the measured failure. The six-part Scope block covers
uniqueness in all four forms, the A8 addendum's conditionality, the `κ` boundary extension, the
convention-dependence of the constructed object (including both undecided readings), the flagged
order's non-uniqueness, and the sufficient-not-necessary status of A7-J, (P-9), (P-10) and A6. This
is the register the contract's gate (b)/(c) intent asks for.

---

### 1.6 `sections_v3/proofs_theorem_ge.tex`

---

**P-9 · T1 proof Step 16, lines 350–402 · deep sample — no difference**

The card's T1 row carries the traceable change *"the quantifier **'on average along the tightening
path'** is added on the re-deriver's S28(ii)"*. All three of the statement's quantifier clauses are
proved separately, and a fourth sub-claim supports them:

- **(i)** `W_T C_T = exp(∫_{r_0}^{r_1} Λ)` via the fundamental theorem of calculus on `log S`, hence
  `W_T C_T ≤ 1 ⟺ ∫Λ ≤ 0`, with "the product criterion is the local criterion integrated along the
  tightening path. This is the 'on average' reading, and it is exact at finite scale." ✔ the card's
  "integrated over `[-T,-T']`".
- **(ii)** pointwise `Λ ≤ 0` ⟹ `W_T C_T ≤ 1`, with the strict version.
- **(iii)** `W_T C_T ≤ 1` gives `Λ(r*) ≤ 0` at **one** point only, by the mean value theorem for
  integrals, plus an explicit counterexample shape (Λ positive on the first half, sufficiently
  negative on the second) — *"The implication in this direction is 'at some point', never 'at every
  point'."* ✔ the card's **"false read pointwise"**.
- **(iv)** the two forms coincide exactly in the infinitesimal limit, with the `Λ(r_0) = 0` boundary
  case **named rather than resolved**. ✔ the card's "exactly in the infinitesimal limit".

Step 15 keeps (T-14)'s monotonicity clause separate from Step 12's integer-window inequality, noting
that nothing outside (T-14) forbids a dipping interpolant — a distinction the statement needs and the
card implies.

---

**P-9b · T1 proof Steps 6 and 12–14, lines 117–137 and 242–313 · no difference**

**Step 6** proves Part (A)'s total-variation clause at `eq:T1-tv` using Steps 2 and 3 in their
**constancy** form — *"`M_F` and `Ω` are one and the same number at the two nodes, which a vanishing
derivative at a single κ would not deliver"* — and records that **(T-8) is not used**, matching the
card's "no differentiability required". It then generalises to any degree-one positively homogeneous
aggregator, with the reason this matters for measurement conventions.

**Step 12** proves `W_T ≤ 1` rather than assuming it, from exactly the two ingredients the card row
names: the clock equivalence of `lem:D1`(b) and `∂_d B_j ≥ 0` for Voice from (TR-ii), with A4's
only-Voice-plans-cross closing the argument — *"a consequence of Lemma~\ref{lem:D1} and the monotone
Voice stake path rather than a hypothesis of the theorem"*. ✔ the card's "**proved**".

**Step 13** gives three independent reasons `C_T` carries no sign, any one sufficient: A(br) is
quantified over the *threshold* pair and none of (br-i)–(br-v) says anything about two window
environments; the window moves trade across the filing date through (TR-iii)'s signed `B^F`/`Q^F`
monotonicities, which a threshold change does not; and the pooled history's own "no flag by `d`"
coordinate changes its content under a tighter window, a composition change at the `T` margin that
(br-ii) excludes only at the κ margin. ✔ the card's "`C_T` is **unsigned**".

**Step 14** gives `eq:T1-ratio-T` and the exact finite equivalence `eq:T1-iff` — the object Step 16
then integrates — and closes by saying precisely what "the weight effect dominates the composition
effect" does and does not mean (*"it does not mean `|1−W_T| ≥ |1−C_T|`, and it does not mean
`C_T ≤ 1`"*).

---

**P-10b · C1 proof Steps 1–6, lines 504–656 · no difference**

Read in full. Step 1 derives `eq:C1-neumann` by an explicit Neumann series, consuming exactly the
submultiplicativity the norm preamble said Step 1 would need. Step 2 establishes the branch's twice
continuous differentiability by a contraction-mapping argument followed by the `C²` implicit function
theorem, and names where (C-3)'s **single-branch** clause is consumed. Steps 3 and 4 reproduce
`def:theta`'s `k̄_x` and `k̄_{κr}` rows as *derived* bounds, with the "partial, not total" caveat on
`∂_x \Tmap`. Step 5's `eq:C1-decomp` is an exact five-term identity grouped in four, with two
miscount checks written out (no `Δ_κκ` or `Δ_rr` can appear; the last term is the only place a second
derivative of the equilibrium map enters, which is why Step 4 exists) and the observation that the
term T1 discards at `eq:T1-three` under (T-7) reappears here. Step 6 bounds the remainder to
**exactly `eq:BGE`**, term for term, and audits the four-terms-into-three-groups mapping explicitly;
the only inequalities used are the triangle inequality and the fixed norm pairings. The
`O((1−L_R)^{-3})` bonus is derived here rather than asserted. **No new mathematics, no dropped step,
no clause the statement needs left unsupported.**

---

**P-10 · (T-15) non-consumption, lines 417–422 · no difference**

*"Hypothesis~(T-15), threshold-side smoothness, is consumed by no step of the proof above. That is
the content of the statement's 'confirmed non-load-bearing' …"*, with the available-but-unclaimed
smooth local reading of Part (B) and "if (T-15) fails nothing above moves." Consistent with
`T1_proof.md`:235 (*"No boxed conclusion of this file rests on it"*). Note the tex T1 proof does not
transcribe the source's Step 15 (the *threshold*-side local form), which is why (T-15) is consumed by
no tex step at all; the statement's qualifier is satisfied either way. Tex T1 step numbers are
therefore **not** 1:1 with `T1_proof.md` — and, correctly, the file header makes no such claim
(unlike `proofs_existence.tex`, which claims 1:1 and delivers it).

---

**P-11 · C1 proof norm-convention preamble, lines 434–500 · deep sample — no difference**

Four conventions fixed before the argument: the margin, the norm, the equilibrium objects, and the
region's regularity. The **norm** block carries the card's N1 in full and then some: one norm fixed on
`R^{J-1}` by (C-1); the *induced* operator norm for the matrices; the **dual** norm
`‖φ‖_* = sup_{‖w‖≤1}|φ(w)|` for the covectors `Δ_k`, `Δ_{κk}`, `Δ_{kr}`; the bilinear-form norms for
`\Tmap_{kk}` and `Δ_{kk}`; and the two consequences — the operator norm must be induced, hence
submultiplicative, because Step 1 needs `‖A^n‖ ≤ ‖A‖^n`; and **"the pairing must be the matching one,
because pairing a covector with a vector through a magnitude that is not the dual norm can make
\eqref{eq:BGE} *understate* the remainder it is meant to bound, which voids the implication
silently"** — which is card N1's *"a mismatched pairing silently voids the implication"*, with the
mechanism supplied. The `J − 1 = 1` collapse note is a harmless addition. The equilibrium-objects
block does the card's (C-5) work of separating `S^GE` from `def:premium`'s `S` and pinning that every
partial below is a partial of the **fixed-policy** map evaluated on the equilibrium branch.

---

**P-12 · C1 proof closing discussion, lines 710–747 · no difference — and it is where item 10 is
discharged**

Three blocks. *"Sign coherence is not consumed"* separates and discharges both objects (see **T-10**).
*"The hypotheses are relative to the norm"* records that `L_R`, both `k̄` bounds, `B_r^GE` and hence
`η_r` all depend on the norm, that spectral radius below one does not give operator norm below one in
a *given* norm, and that this is why (C-1) fixes one convention. *"What is not delivered"* records
that nonemptiness of `R_r` is neither claimed nor provable here, restates exactly what the
dominance-and-contraction nodes verify and do not, names what a node-to-region promotion would need
(a modulus of continuity for `η_r` and a genuine supremum for `L_R`, "neither of which more grid nodes
can supply"), and records that `η_r ≤ 0` carries no information about the sign because `B_r^GE` is a
triangle-inequality bound.

---

**P-13 · Proof run-in citation style, all files · OK-RESTRUCTURED**

**Checklist item 12(b).** Five of the eight proof headings use the ID-only form
(`Proof of Lemma~\ref{lem:D1} (D1)`); three use a short descriptive title. In-proof run-ins cite by
`\ref` plus a parenthetical card ID — `Assumption~\ref{asm:A6} (A6)`, `Assumption~\ref{asm:A7J}
(A7-J)`, `Assumption~\ref{asm:A2p} (A2$'$)`. This is what `labels_map.md`:6–7 prescribes and it is
forced by the environment setup: the seven `\newtheorem`s are independently and globally numbered, so
`\ref` yields a bare number and the ID must be written by the citing prose. Gate (e) shows **zero**
undefined references, so every run-in resolves. **No substance at stake; the convention is consistent
and it satisfies card §8 rule 2 (cite only IDs the card carries).**

---

## 2. Gate-by-gate and item-by-item summary

### Contract gates

| Gate | Result | Basis |
|---|---|---|
| **(a) Clause completeness** | **PASS** | Every card §6 row walked clause by clause; P1's trap list (contract lines 13–22) walked item by item and **complete** (T-6). Two over-assumptions (D1, L2 cite the whole TR block where the card names §4.1/§4.2) affect minimality, not completeness — T-1, T-3. |
| **(b) Labels verbatim, conditionality attached** | **PASS** | All eight `\resultstatus` strings match the card ledger's Label cells character for character, including the four conditional ones the contract enumerates. `\resultstatus` renders a visible **Status.** paragraph, not a footnote. No label weakened, none promoted, no conditionality demoted. The one footnote in a statement (`lem:L2`) carries a *reading*, not conditionality. |
| **(c) Evidence-note substance present** | **PASS** | Every element the contract enumerates for A(τ), A6, A3, P1 numerics and C1 is present, at **both** an assumption site and a result site: `rem:AtauRecord` + `lem:L3`/`lem:L4` trailing ¶ + `rem:T1record` ¶1; `rem:A6record` + `rem:P1record` ¶2; `rem:A3record` + `rem:P1record` ¶2; `rem:P1record` ¶1; `rem:C1record`. Verified element by element at M-2, M-3, M-4, T-7, T-9, T-11. |
| **(d) Vocabulary (`CONTEXT.md`)** | **PASS** | Systematic sweep over all six files: **zero** hits for depth, volume, turnover, certified, certificate, region-certified, activist, investor, fund, reporting regime, transparency requirement, 13D, key(s), hook, pitch, angle, framing, motivation, novelty. κ glossed as **noise-trading intensity** (4×). The A7 form is named every time it matters — the three bare-"A7" hits are the assumption's own title, A7′'s title, and a meta-sentence about naming. "dominance-and-contraction" 9×, never "certified". Disclosure-regime ≠ window margin kept (T-9). Three borderline hits adjudicated below. |
| **(e) Compile** | **PASS** | My own clean four-pass run from the repo root after deleting every aux artifact: `xelatex → biber → xelatex → xelatex`. `grep -in undefined standalone_v3.log` returns **nothing** (count 0), references and citations both. `standalone_v3.blg` clean. One `Overfull \hbox` — located and fixed-proposed at **F-2**. |

### Contract "Citations" clause — also checked

The contract binds the checker here too. Result: **clean, and vacuously so.**

`sections_v3/sections_v3.bib` contains **no entries** — a single comment line
(*"New citations introduced by the v4 theory sections (ticket 08). Root bibliography.bib holds the
draft_v2-era entries."*). **No new bibliographic data was shipped**, so the rule that a new entry
needs data verified from a file on hand cannot have been broken.

All four citations used are pre-existing root keys, and all four appear in `bib_inventory.md`:
`Kyle1985`, `EdmansGoldsteinJiang2015` (both `model_section.tex`:36–38, for the discrete ternary-noise
order-flow structure), `GlostenMilgrom1985` (:38, competitive pricing), `GrossmanHart1980` (:40, the
free-rider reason the premium is the minority welfare object). All four resolve — gate (e) reports
zero undefined citations, and `standalone_v3.blg` is clean. Repo records are `\texttt{}` strings and
never citations throughout, as the contract requires: I checked every record mention in
`rem:AtauRecord`, `rem:A6record`, `rem:P1record` and `rem:C1record`.

*Gate (d) borderline hits, all adjudicated as legal:*

1. **"window test"**, `theorem_section.tex`:363 — used to *name and reject* the misreading (*"are
   sometimes read as a window test, is a disclosure-regime comparison"*). CONTEXT.md's _Avoid_ is
   scoped "(when a regime comparison is meant)", which is precisely the misuse the sentence corrects.
2. **"gap"**, six hits, all in `proofs_core_lemmas.tex` — five are "chord gap" / "chord-gap sum", the
   proof-local arithmetic object at `eq:L3-gap`; one is "The gap that (br-ii) closes". The _Avoid_
   sits under CONTEXT.md's **Whitespace** entry and targets positioning language; the glossary's own
   **Premium wedge** entry uses "gap" arithmetically. Not a violation. (Related: T-5.)
3. **"information structure"**, `proofs_core_lemmas.tex`:913 — *"the coefficient is a property of the
   pooled information structure"*. The _Avoid_ sits under **Partition** and forbids substituting the
   phrase *for* "partition"; here it describes what the pooled cell reveals, and the partition is
   named as "partition" 18 times across the six files. Not the forbidden substitution. If the orchestrator
   wants zero ambiguity, "the pooled cell's information content" is a drop-in.

### Checklist items 1–13

| # | Item | Verdict | Where |
|---|---|---|---|
| 1 | `rem:T1record`'s O-1 paragraph: four ratios, four Ω values, the block-4 / `W_T C_T < 1` / `H=10` claim, the disclosure-regime vs window distinction | **MISCITED** (record names thinned) + **OK-RESTRUCTURED** (descriptor swap) + **UNCHECKED** (card's 0.29 vs 0.343) — all numbers exact | T-9 |
| 2 | The A(br) block: (br-i)–(br-v), ρ sharpening, level-symmetric inheritance, (br-iii) attack-first, (br-v) three agents | **OK-RESTRUCTURED**; substance complete. MISCITED on the H17 / rederive pointers | M-5 |
| 3 | Does the card record the C1 aspiration retirement? | **YES** — `MODEL_CARD.md`:485–489, carried verbatim in substance. MISCITED on the "(C1 proof-read's ruling)" attribution | T-11 |
| 4 | D1 and L1 carry every clause (D1's three parts, `P^P_{-1}`/`P_ND`, Borel-for-Exit; L1's A5 version-pinning, degenerate-cell non-identification) | **Complete.** OK-RESTRUCTURED on D1's TR-bundle over-assumption | T-1, T-2 |
| 5 | `sec:not-claimed` prose list vs card §9 preamble, item for item | **Complete** — all eleven, card order. OK-RESTRUCTURED (draft_v2 → the frozen manuscript) | T-12 |
| 6 | Open-questions list: item 3's relocation lossless; items 1/2/4 complete incl. 4's (a)/(b)/(c) | **Nothing of item 3 lost**; 1/2/4 complete. One MISCITED dangling pointer in item (1) | T-12, M-4a |
| 7 | The eight displays, symbol for symbol | **No difference** — all eight identical to the card | M-9 |
| 8 | A7 satisfiability discussion (pro-rata menu, forty collisions, failure boundary) | **MISCITED** — one scoping addition ("for the on-path form") + dropped attack-verdict pointers; substance complete | M-8 |
| 9 | `def:premium` and `def:theta` (π̄ ruling, mean-vs-π̄ degeneracy, W/C conventions, margin subscripts) | **Complete.** MISCITED on ω_a "the calibration target"; OK-RESTRUCTURED on the notation-history drops | M-6, M-7 |
| 10 | Which object does the card's "sign-coherence hypothesis … unused" mean, and is `prop:C1`'s attribution exact? | **MISCITED** — the card means **H8**, not AGE; the statement attributes it to AGE; the proofs file discharges both and keeps them apart, so the record survives. **Not WRONG.** Fix proposed | T-10 |
| 11 | `rem:AtauRecord`'s two dropped pointers: (S1)/(S2), and MIN_CELL_MASS | (a) **MISCITED, a real loss** — the L3 proof does **not** carry Step 18's (S1)/(S2), so the link survives only via the card; two in-paper sentences now dangle. (b) **MISCITED, correct as paper prose** — substance fully intact | M-4a, M-4b |
| 12 | Two writer-flagged wordings: L4 leg 2's "gap", and ID-only proof run-ins | (a) **OK-RESTRUCTURED** — no substance change; the substitution was not required but is harmless. (b) **OK-RESTRUCTURED** — forced by the environment setup, zero undefined refs | T-5, P-13 |
| 13 | The one overfull hbox in `rem:P1record` — locate and propose the minimal fix | **Premise corrected.** It is **not** in `rem:P1record`; it is the C1 proof's optional heading | F-2 |

---

## 3. Flags outside the verdict classes

---

**F-1 · `\Tmap` name collision — a latent defect in the intended consumer, declared by the writers**

`sections_v3/v3_macros.tex`:29 binds `\Tmap` with `\providecommand{\Tmap}{\mathcal{T}}` and documents
why. I verified the collision it guards against: **`draft_v2.tex`:54 carries
`\providecommand{\Tmap}{T}`**, and uses `\Tmap` about ten times in its own body (e.g. line 575).

Consequence: in the standalone driver the binding is correct (`standalone_v3.tex` deliberately omits
draft_v2's macro block, so `\Tmap` → `\mathcal{T}`). But **in `draft_v3.tex` — a draft_v2 copy
carrying that block forward — `\Tmap` will silently resolve to upright `T`**, which is the filing
window. All **104** uses of `\Tmap` across the six section files (counted) would then render the
outer best-response map as the window symbol, in direct contradiction of card §4.5 (*"always
calligraphic — upright `T` is the window"*) and card §8 rule 4.

This is **not a difference from the card** — the checked artifact is correct as it compiles today, and
the writers flagged it themselves in the macro header. But it is the single highest-consequence item
I found for the next step in this lane, and it must be resolved (rename one of the two `\Tmap`s)
before draft_v3 assembly. Recorded here so it is not lost between tickets.

---

**F-2 · The overfull hbox — item 13's premise corrected**

The orchestrator's spot review located the one overfull hbox in `rem:P1record`. **It is not there.**

`standalone_v3.log`:669 (my own clean run, and the writers' run before it):

```
Overfull \hbox (14.3809pt too wide) in paragraph at lines 435--436
[]\TU/lmr/m/n/10.95 Four
```

The line numbers are read in the file open at that moment, which the log's page trace shows is
`sections_v3/proofs_theorem_ge.tex`. Lines 434–435 there are:

```latex
\begin{proof}[Proof of Proposition~\ref{prop:C1} (C1: the dominance-and-contraction implication in general equilibrium)]
Four conventions are fixed first, because the statement's hypotheses are stated against them.
```

`amsthm` sets a `proof`'s optional argument as an unbreakable label box at the head of the first
paragraph, which is why the box begins with "Four". The heading text —
*"Proof of Proposition 8 (C1: the dominance-and-contraction implication in general equilibrium)."* —
is the longest of the eight and overruns by 14.38pt. (`rem:P1record`'s second sentence also begins
"Four nodes of the equilibrium sweep", `theorem_section.tex`:278, which is the likely source of the
misattribution.)

**Minimal fix (proposed; I made no edit).** Shorten the optional argument on
`proofs_theorem_ge.tex`:434 to match the pattern the other five lemma proofs already use:

```latex
\begin{proof}[Proof of Proposition~\ref{prop:C1} (C1)]
```

That is a one-line change, touches no prose, changes no cross-reference, and clears the box with
room to spare. If the descriptive title is wanted,
`(C1: the dominance-and-contraction implication)` also fits.

---

## 4. Counts and overall verdict

| Class | Count |
|---|---|
| **WRONG** | **0** |
| MISCITED | 13 |
| UNCHECKED | 1 |
| OK-RESTRUCTURED | 14 |
| Flags (outside the classes) | 2 |

MISCITED (13): M-2 (A3 record pointers), M-3 (A6 record pointers), M-4a ((S1)/(S2) drop **plus** the
two dangling "weakest sufficient conditions" claims), M-4b (`MIN_CELL_MASS`/HANDOFF §8.1), M-4c
("block 3"), M-5 (H17 + rederive pointers), M-6 (ω_a "the calibration target"), M-8 (A7 failure
boundary scoped to the on-path form, + attack-verdict pointers), M-10 (`v3_macros.tex` provenance:
wrong line range **and** stale stamp), T-9i (`t2_t1_check`, HANDOFF §8.1, HANDOFF §3,
`t1_o1_rerun_check.py`), T-10 (sign-coherence attributed to AGE rather than H8), T-11 (C1
proof-read ruling attribution), P-3 (L3 step-number anchors have no in-paper home).

UNCHECKED (1): T-9iii — the card's own `≈ 0.29` (§4.4 Ω row) against `Ω* ≈ 0.343` (§9 item 3). Not
adjudicable from the card; the section follows §9 item 3 and is defensible either way. Card-side;
for the orchestrator.

---

### OVERALL VERDICT: **LAND** — no WRONG findings.

All five contract gates (a)–(e) pass, including a fresh compile I ran myself from a clean state, and
the contract's Citations clause is clean (no new bib entries shipped). The thirteen MISCITED findings
are pointer, attribution and provenance issues with substance intact; by the ticket's own vocabulary
none blocks. The five most worth acting on before landing, none of them blocking:

1. **M-4a** — restore (S1)–(S2), or reword the two sentences (`theorem_section.tex`:129 and :448)
   that claim the paper names them.
2. **T-10** — re-attribute the sign-coherence sentence (`theorem_section.tex`:401) from AGE to H8;
   the crosswalk's §0 row 27 carries the same conflation and should be corrected with it.
3. **F-2** — shorten `proofs_theorem_ge.tex`:434 to clear the overfull hbox. The ticket located this
   in `rem:P1record`; that premise is wrong and the correction belongs on the record.
4. **F-1** — resolve the `\Tmap` collision before draft_v3 assembly (104 uses would silently render
   the outer map as the window symbol).
5. **M-10** — fix `v3_macros.tex`'s provenance header, wrong on both the line range (42–51, not
   28–37) and the stamp (2026-08-27, not 2026-08-23).

*Checker's note on independence:* I read the writers' crosswalk and labels map as claims and verified
them against the files rather than accepting them. The crosswalk is honest — it declares the "gap"
substitution (row L4.7) and the P1 footnote relocation (row P1.9) without being asked. Two places
where it does not match what I found: row C1.10 records the sign-coherence clause as landed "final
sentence inside `prop:C1`" without recording that an attribution to AGE was added (§0 row 27 shows
the conflation was upstream of the sentence, not introduced at it); and row D1.5 says "(TR-i)–(TR-iii)"
where the statement cites all of `asm:TR`. Neither is concealment; both are logged above.

---
---

# Repair-round delta check — 2026-08-27 (appended)

Same checker, same rules: no git, no edit to any file under `sections_v3/` or `research/` other than
this append. Five repairs landed after the pass above; each is verified below against the same
sources, and the compile was re-run by me from a clean state.

**State at check.** `proofs_core_lemmas.tex` 949 → **1108** lines (L3 Part IV appended, lines
726–883, inside the L3 proof); `theorem_section.tex` 467 → **470**; `proofs_theorem_ge.tex` 748 →
**747**; `v3_macros.tex` 39 → **47**. `model_section.tex` (652), `proofs_existence.tex` (1025),
`proofs_section.tex` (6) and `standalone_v3.tex` (72) unchanged. Card stamp re-confirmed unchanged at
2026-08-27 / `ae9caea`.

---

## R-1 · L3 Part IV (`proofs_core_lemmas.tex`:726–883) — **PASS at full grain**

Checked line by line against `proofs/L3_proof.md` Part IV (Steps 16–18, source lines 327–453) and
against the card.

**(S1)/(S2) — named, and verbatim against the source.** `proofs_core_lemmas.tex`:865–870 sets them as
an `enumerate` with `label=(S\arabic*)`:

- (S1) source: *"every pooled order-flow cell is either fully revealing of `a=0`, fully revealing of
  `a=1` up to the pooled cell's own ceiling `π̄`, or a single cell whose posterior is `π̄/2`"*; tex
  identical, one "or" added for parallelism.
- (S2) source: *"that middle cell's likelihood ratio is free of `κ`, which in Example A came from the
  two contributing types reaching the cell through noise events of equal probability"*; tex
  identical, "Example A" → "Step 16" (the tex does not use the name "Example A").

The framing sentence is also verbatim — *"it suffices to establish the support condition alone: that
the pooled cell's engagement-posterior law, at fixed policies, is supported on exactly three points
`0 < π̄/2 < π̄` with none of them varying with `κ`"* — and the tex adds *"which are the weakest
sufficient conditions this lemma can name"*, de-first-personing the source's *"stated as the weakest
sufficient condition I can name"*. That addition is what makes the two sentences at issue in **M-4a**
true; see **R-2**.

**The one-round market (Step 16) — transcribed exactly.** Every element checked: the mark `2z̄`
against a non-engaging `0`; the share `ρ = ½`; the admissibility argument (`Γ` a finite ordered
coarsening with no ceiling of `z̄` on its image; the non-engaging mark as the constant Hold path of
(TR-ii)); the ternary noise and `X_0 = q_0 + z_0`. The table `eq:L3-exampleA` is cell-for-cell
identical to the source's, both rows. The three posteriors and their masses are exact —
`π = 1` and `π = 0` each at `(2−κ)/4`, `π = ½` at `κ/2` — as is the reason the middle atom sits at
`½` (*"the two types reach `X_0 = z̄` through noise realisations of equal probability `κ/2`, which
cancels"*). Support `{0,½,1} = {0,π̄/2,π̄}` with `π̄ = 1` ✔. Weights
`A_1 = A_0 = (2−κ)/4`, `A_{1/2} = κ/2` ✔; derivatives `A_0' = A_1' = −¼`,
`A_{1/2}' = +½ = −2·(−¼)` ✔; **`A'_κ = −¼`** stated explicitly ✔. The moment check
`A_{1/2}·½ + A_1·1 = κ/4 + (2−κ)/4 = ½ = ρ` ✔. Both load-bearing features carried verbatim: the
informed mark strictly outside the reach of uninformed-plus-noise (`2z̄ > 0 + z̄`) pinning the
endpoints at every `κ`, and the share being exactly `½`, *"which is what the word 'symmetric' in
Assumption A(τ) carries"*.

*Example A′* (the `π̄`-free family, tex 772–789) is also exact: `A_1 = A_0 = α − cκ`,
`A_{1/2} = 1 − 2α + 2cκ`, `A'_κ = −c`, with `α = 0.4`, `c = 0.3`. I checked the arithmetic myself —
the three weights are `0.4 − 0.3κ ∈ [0.1,0.4]` and `0.2 + 0.6κ ∈ [0.2,0.8]`, all inside `[0.1,0.8]`,
summing to 1; and `ρ = A_{1/2}(π̄/2) + A_1π̄ = π̄[0.1 + 0.3κ + 0.4 − 0.3κ] = π̄/2`, `κ`-free as
claimed. The likelihood display `eq:L3-likelihood` and the Bayes return `P(a=1|i) = π_i` match the
source exactly.

**The no-disclosure structure (Step 17) — transcribed exactly.** The mark `z̄` against `0` with
`ρ ∈ (0,1)`; `X_0 ∈ {−z̄,0,z̄,2z̄}`. The table `eq:L3-exampleB` is row-for-row identical to the
source's, including both contributing-mass columns and both interior posteriors
`π_∓`. **Four atoms** ✔. The monotonicity argument is verbatim and I checked it: the likelihood ratio
at `X_0 = 0` is `(κ/2)/(1−κ)`, strictly increasing on `(0,1)`, so `π_−` rises; at `X_0 = z̄` it is
`(1−κ)/(κ/2)`, strictly decreasing, so `π_+` falls. **The two-term derivative** `eq:L3-twoterm`
matches the source display exactly, with the underbrace labels reworded from *"the term A(τ)
keeps"* / *"…has no room for"* to *"the term the representation keeps"* / *"…it has no room for"* —
avoiding a card ID inside a display, same content. The follow-through is complete: the second sum
generically nonzero; the first sum *not* proportional to `C_h(π̄)`, being
`Σ_i A_i'(h−ℓ_h)(π_i)` over four atoms; and the identification of the structure as the frozen
manuscript's own, with *"Step 9 transfers to that structure; Step 8's clean proportionality does
not."*

Two thinnings here, both correct. The source's explicit posterior list
`{0, π(−1,0), π(0,0), π̄}` and its symbols `p_0`, `p_1` are dropped — those are draft_v2 symbols the
card does not carry, and card §8 rule 2 forbids citing IDs the card lacks, so dropping them is
required, not optional. And the source's closing *"That is a limitation of A(τ), stated here rather
than discovered later"* is dropped, its substance carried by the preceding sentence.
**OK-RESTRUCTURED.**

**Step numbering — the card's pointer resolves; here is exactly how far the 1:1 goes.** Tex Steps
**16, 17 and 18 land on their source numbers**, so **the card's "L3 Step 18's (S1) and (S2)" pointer
(MODEL_CARD.md:360) resolves exactly**, which is what the repair was for. The alignment is not an
accident and it is worth recording how it is achieved: promoting the source's unnumbered "Step 8′"
to a numbered tex Step 9 pushes everything down by one, and merging the source's Steps 14 and 15 into
tex Step 15 pulls it back, so the offset cancels precisely at 16.

The consequence is that the 1:1 holds **from Step 16 onward, not throughout**: tex Step 14 is the
source's Step 13, and tex Step 15 merges the source's Steps 14, 15 and 19. I checked every card
pointer into L3's proof against this. Steps 16–18 ✔ resolve; "Part IV, Steps 16–18" (§5 A(τ) and §9
item 1) ✔ resolves; "Hypothesis 8" and "Hypothesis 1" (§5 A(τ)'s (τ-i)/(τ-ii) clauses) are hypothesis
IDs, not step numbers, and are unaffected. **One pointer still does not resolve:
`proofs/L3_proof.md` Step 19**, cited twice — at §4.4's `π̄` row (the binding upper-support-point
ruling) and at A(br)'s (br-iv) — because source Step 19 is folded, unnumbered, into tex Step 15's
closing. This is the residue of **P-3**, now reduced from *"Steps 16–19 have no in-paper anchor"* to
*"Step 19 only"*, and its content is carried in two places
(`proofs_core_lemmas.tex`:716–724 and `model_section.tex`:650–652). **MISCITED, non-blocking**, and
noted so the record is exact rather than rounded up to "fixed".

**Internal cross-references — all correctly re-pointed.** I checked each of the six references the
new material makes into earlier steps: *"The moment check of Step 15"* (source said Step 14 — tex 15
carries `eq:L3-equiv` and the moment definition ✔); *"By Step 15 it suffices"* ✔; *"By Step 16 that
decomposes"* ✔; *"Step 17 fails (S1) and (S2) simultaneously"* (source: "Example B fails" ✔);
*"by Step 9 it equals `Σ_i A_i'(h−ℓ_h)(π_i)`"* (source: "by Step 8′" — and tex Step 9 at line 610–612
does carry exactly that formula ✔); *"the coefficient pattern (+1,−2,+1) that Step 8 factors"* ✔.

**No circularity, and the bridging paragraph's claim is true.** Lines 726–729 say the three new steps
*"fix the assumption's domain … none of them is used in the derivation of parts (a)--(c) above."* I
verified this: parts (a)–(c) are delivered at Steps 8, 6 and 12–13, none of which cites 16–18, and
every citation the new steps make runs backwards (18→15, 18→16, 17→9, 16→15, 16→8).

**Declared deviation (a) — the "second place with an unverified domain" sentence. CARD-FAITHFUL, and
required.** The source's Step 18 closes: *"**Declared OPEN.** It sits next to the A7-satisfiability
question as the second place where a maintained hypothesis of this model has an unverified domain,
and it is load-bearing for L3, L4 and T1 jointly."* The tex replaces the first clause and keeps the
second, sharpened: *"…it is load-bearing for this lemma, for leg 3 of Lemma L4 and for Part (B) of
Theorem T1 jointly."*

The removal is not optional. The source sentence predates ticket 24, and the card's post-ticket-24
state contradicts it twice: §5's A7 note records **"Satisfiability is resolved for A7′"**, and §9's
preamble records *"A7 satisfiability … is now **resolved** (§5's A7 note, ticket 24)"*. Card §9 item 1
then makes A(τ)'s domain not the *second* such place but **"the largest single conditionality the
ledger carries."** Keeping the source sentence would have put a stale claim in the paper that the
card's own §5 and §9 refute. The replacement's scoping to leg 3 and Part (B) matches card §9 item 1
and the A(τ) note exactly. And the A7-adjacent question that *does* remain open — incentive
compatibility, card §9 item 2 — is carried separately and correctly at `sec:not-claimed` item (2),
so nothing was lost by the removal. **Card-faithful.**

**Declared deviation (b) — the added `rem:AtauRecord` pointers. CARD-FAITHFUL; the count is two, but
they do two different jobs and the declaration describes only one.** I grepped: exactly **two**
`rem:AtauRecord` references inside 726–883, at lines 855 and 876.

- **Line 876** is the one the declaration describes. It maps the measured failures onto the two
  conditions: *"Remark~\ref{rem:AtauRecord} records a support carrying 23 to 767 distinct posterior
  values with no mass at `π̄/2` at any node, **which is (S1)**, and interior atoms that move with `κ`
  at a two-sided Hausdorff distance reaching 0.4608 between adjacent-`κ` support sets, **which is
  (S2)**."* This is **MODEL_CARD.md:360**'s own claim — *"This refutes L3 Step 18's (S1) and (S2)
  together at this calibration"* — decomposed onto which measurement hits which condition. Both
  attributions are correct against the (S1)/(S2) just defined: 23–767 distinct posteriors with no
  mass at `π̄/2` refutes both halves of (S1); interior atoms moving with `κ` refutes (S2)'s
  `κ`-free likelihood ratio. The tex says the two are *"refuted together"*, matching the card's
  "together", and adds *"That is applicability evidence at one calibration and it moves no label"* —
  the card's own label discipline. **Card-faithful.**
- **Line 855 does a different job and is not covered by the declaration.** Tex Step 18's second
  paragraph argues that the two-round structure is where an endpoint below one could come from —
  which restates a conjecture the card records as **false**. The writer guards it in place:
  *"Whether it does so is a separate question from whether it could, and the answer at the
  implemented calibration is that it does not: Remark~\ref{rem:AtauRecord} records `π̄ = 1` at every
  non-degenerate node there, because unflagged Voice types still generate fully revealing pooled
  order flows. The conjecture that the two-round timing leaves the pooled cell with a top atom
  strictly below one is therefore false at that calibration, and nothing below rests on it."* This is
  card §5's `π̄`-half bullet almost word for word — *"that step's conjecture that 'the two-round
  timing … leav[es] the pooled cell with a top atom strictly below 1' is false at this
  calibration — unflagged Voice types still generate fully revealing order flows"* — attached at the
  very step the card names. **Card-faithful, and load-bearing:** without it the transcription would
  have imported a conjecture into the paper that the card has already recorded as refuted. The
  declaration's undercount is a description gap, not a text defect. **MISCITED (declaration), text
  card-faithful.**

**New labels — collision-free.** `eq:L3-exampleA`, `eq:L3-likelihood`, `eq:L3-exampleB`,
`eq:L3-twoterm` follow the file's `eq:L3-` prefix convention. I ran a duplicate check over every
`\label{...}` in all six files: **no duplicates anywhere**, and the compile reports zero undefined
references, so no forward reference is broken either.

**One compression, verified.** The source spells out the weight sum
`(2−κ)/4 + κ/2 + (2−κ)/4 = (4−2κ)/4 + κ/2 = 1`; the tex writes *"summing to one"*. I checked the
arithmetic: correct. **OK-RESTRUCTURED.**

---

## R-2 · `theorem_section.tex`:126–131 and :450–452 — **PASS; M-4a closed at both sites**

The openness paragraph now splits the attribution (lines 126–131):

> the discussion after Assumption~\ref{asm:Atau} shows that the support condition is the assumption's
> entire remaining bite, and exhibits a one-round market that satisfies it and a no-disclosure
> structure that does not; **the weakest sufficient conditions for the two-round case are named in
> the closing steps of the proof in Section~\ref{sec:proofs}.**

**The redirect is accurate.** (S1)/(S2) are named at `proofs_core_lemmas.tex`:865–870, in Step 18 —
the last step of the L3 proof, inside `proofs_core_lemmas.tex`, which is `\input` under
`\section{Proofs}` / `sec:proofs`. *"The closing steps"* is a true description of Steps 16–18. And the
first half remains true: `model_section.tex`:451–459 does show the bite is the support condition and
does exhibit both structures. Both halves of the sentence now point at content that exists.

**Line 452's Lemma-attribution is now true as written.** The `sec:not-claimed` item (1) sentence
attributes all four verbs to Lemma L3 rather than redirecting, so I checked each against the L3 proof
as it now stands: *"shows that the entire remaining bite … is its support condition"* → Step 15 ✔;
*"exhibits a one-round market that satisfies it"* → Step 16 ✔ (newly true); *"and a no-disclosure
structure that does not"* → Step 17 ✔ (newly true); *"names the weakest sufficient conditions for the
two-round case"* → Step 18 ✔ (newly true). Before the repair only the first was true of the Lemma.

Worth recording: this now matches **card §9 item 1's own attribution**, which credits all four to L3
(*"L3 proves the representation's entire remaining bite is the support condition, exhibits a
one-round market that satisfies it and the frozen manuscript's own no-disclosure structure that does
not, and declares the two-round case open with the weakest sufficient conditions named"*). The paper
and the card now say the same thing about the same object. **M-4a closed.**

---

## R-3 · `theorem_section.tex`:402–405 (`prop:C1` closing) — **PASS; T-10 closed, and it exceeds the fix I proposed**

New text:

> The sign-coherence hypothesis --- that the fixed-policy attenuation sign agrees with the
> equilibrium sign --- is confirmed unused in \eqref{eq:C1}: its work is one of naming, fixing when
> that conclusion may be called a survival of the fixed-policy sign. The sign-constancy clause of
> Assumption~\ref{asm:AGE} is likewise unused.

Checked against `proofs/C1_proof.md`:141–148, whose H8 reads
*"`sgn(∂_κΔ^act(k(ϑ),ϑ)) = sgn(dΔ^act(k(κ,r),κ,r)/dκ)` on `R_r`: **the fixed-policy and equilibrium
liquidity derivatives point the same way.** Card §4.5 defines `g_r^PE` with the **equilibrium** sign
but calls it the *fixed-policy* attenuation margin; H8 is exactly the clause that makes both halves
of that name true at once. The boxed conclusion (C) does **not** use H8 — Step 9 is where it is
consumed, and Step 9 is a statement about what (C) may be called."*

- **Names H8 by content:** ✔ *"the fixed-policy attenuation sign agrees with the equilibrium sign"*
  is H8's own sentence.
- **Carries H8's naming role:** ✔ *"its work is one of naming, fixing when that conclusion may be
  called a survival of the fixed-policy sign"* is the source's *"Step 9 is a statement about what (C)
  may be called"*. I did not propose this half; the writer added it, and it is what makes the
  sentence informative rather than merely corrected.
- **Discharges AGE separately, under the right name:** ✔ a second sentence, and it says
  **sign-constancy**, not "sign-coherence" — AGE has no clause by the latter name, which was the
  original defect.
- **Matches the card:** ✔ card's *"confirmed unused in the boxed conclusion"* → *"unused in
  \eqref{eq:C1}"*, and `eq:C1` **is** the boxed conclusion; the evidence chain's "H8 unused" is now
  correctly targeted.
- **Matches the proof:** ✔ `proofs_theorem_ge.tex`:713–724 (unmoved) separates the same two objects
  in the same order and assigns the same naming role. Statement and proof now agree.

**T-10 closed.**

---

## R-4 · `proofs_theorem_ge.tex`:17 and :434 — **PASS; F-2 closed**

Both run-ins are now ID-only: `[Proof of Theorem~\ref{thm:T1} (T1)]` and
`[Proof of Proposition~\ref{prop:C1} (C1)]`. All eight proof headings across the three files now use
the same ID-only form, which is a consistency gain over the mixed convention I recorded at **P-13**.

**Fresh four-pass compile, run by me from the repo root after deleting every aux artifact**
(`standalone_v3.{aux,bcf,bbl,blg,log,out,run.xml,pdf}`), exactly the contract's sequence:

| Check | Result |
|---|---|
| `grep -in undefined standalone_v3.log` | **0 hits** |
| `grep -n "^!" standalone_v3.log` | **0 hits** |
| `grep -n "Overfull\|Underfull" standalone_v3.log` | **0 hits** — the box is gone |
| `standalone_v3.blg` warnings/errors | **0** |
| Exit code | 0 |
| Output | **61 pages** (was 58; +3 from L3 Part IV) |

Gate (e) passes with a strictly cleaner log than at the original pass, which carried one overfull box.

---

## R-5 · `sections_v3/v3_macros.tex` — **PASS on provenance (M-10 closed); hardening is correct, with two one-line residuals**

**Provenance (M-10).** Header now reads *"transcribed verbatim from
`research/model_v4/model_v4.tex` **lines 42-51** (card stamp **2026-08-27**)."* Both corrections
match what I verified: the macro block is `model_v4.tex`:42–51, and the note carries stamp
2026-08-27. **M-10 closed.**

**The hardening (F-1) — judged in both directions, as asked.** `\Tmap` is now plain `\newcommand`,
with a comment saying the collision must fail loudly rather than merge silently.

- **Standalone driver: behaves as the comment claims. Verified empirically, not by reading.**
  `standalone_v3.tex` contains no occurrence of `Tmap` (checked), and no package it loads defines
  one, so `\Tmap` is undefined when `v3_macros.tex` is `\input` and plain `\newcommand` binds it to
  `\mathcal{T}`. The decisive evidence is R-4's compile: exit 0, **zero `^!` lines**, 61 pages. Had
  the name been pre-defined, `\newcommand` would have raised `! LaTeX Error: Command \Tmap already
  defined.` It did not. ✔
- **A draft_v3 carrying draft_v2's guard: behaves as the comment claims.** `draft_v2.tex`:54 is
  `\providecommand{\Tmap}{T}`, in its preamble, so in a draft_v2 copy `\Tmap` is defined before any
  body `\input` reaches `v3_macros.tex`. `\newcommand` on an already-defined control sequence is a
  hard LaTeX error, so the build stops rather than silently merging. ✔
- **Is failing loudly the right call?** Yes, and it is the correct answer to F-1. The previous
  `\providecommand` guard converted a semantic corruption into a *clean-compiling* PDF in which the
  outer best-response map renders as the filing window — invisible on inspection. The new binding
  converts it into a build-time stop that ticket 18 must resolve consciously, and the comment
  forecloses the lazy fix (*"it is not free to silence the error by re-adding a guard"*). The
  contradiction with card §4.5 and §8 rule 4 is named in the comment itself. **Good hardening.**

Two residuals, both one line, neither blocking:

1. **The comment's "104 uses" is now 107.** I re-counted: `\Tmap` appears **107** times across the
   six section files; the L3 Part IV addition added three. The 104 figure is the one I supplied in
   this report before that repair landed. Trivial, but it is a number in a comment that a future
   reader may take as current. **MISCITED.**
2. **The loud failure depends on an `\input` ordering the comment states but does not defend.** It
   holds only if `v3_macros.tex` is `\input` **after** draft_v2's macro block — which the comment
   assumes (*"`\Tmap` is already defined by the time this file is `\input`"*) and which is the normal
   arrangement, draft_v2's block being preamble. Under the reverse ordering the failure mode inverts
   silently: `\newcommand` binds `\mathcal{T}` first, draft_v2's `\providecommand` then no-ops by
   design, and draft_v2's own ~10 body uses of `\Tmap` render the filing window as the calligraphic
   outer map. That direction is not named. **One added sentence would close it** — e.g. "this
   requires that `v3_macros.tex` be `\input` after draft_v2's macro block; loading it earlier makes
   draft_v2's `\providecommand` no-op silently and corrupts draft_v2's own uses instead."
   **MISCITED.**

F-1 itself remains **open by design**: the hardening makes the collision impossible to miss, but
ticket 18 must still rename one of the two `\Tmap`s.

---

## Delta summary

| # | Repair | Verdict |
|---|---|---|
| 1 | L3 Part IV (Steps 16–18) — the only substantive new content | **PASS at full grain.** (S1)/(S2), Example A (incl. `A'_κ = −¼`), Example A′, Example B and the two-term derivative all transcribed exactly; both declared deviations card-faithful; labels collision-free; no circularity |
| 2 | Openness paragraph redirect + `sec:not-claimed` item (1) | **PASS.** Redirect accurate; the Lemma-attribution is now true as written and matches card §9 item 1. **M-4a closed** |
| 3 | `prop:C1` closing sentence | **PASS.** Names H8 by content, carries its naming role, discharges AGE's constancy clause separately and correctly. **T-10 closed** |
| 4 | ID-only run-ins at `proofs_theorem_ge.tex`:17, :434 | **PASS.** Fresh four-pass compile: 0 undefined, 0 `^!`, **0 Overfull**, biber clean, 61 pages. **F-2 closed** |
| 5 | `v3_macros.tex` provenance + `\Tmap` hardening | **PASS.** **M-10 closed**; hardening verified correct in both directions, empirically for the driver. Two one-line residuals (stale "104"→107; reverse-`\input`-ordering case unnamed) |

**Findings closed by this round:** M-4a (both sites), T-10, M-10, F-2. **Narrowed:** P-3, from
"Steps 16–19 have no in-paper anchor" to "Step 19 only". **New:** two MISCITED, both in the
`v3_macros.tex` comment (R-5). **Unchanged and still open by design:** F-1, for ticket 18.

**No repair introduced a WRONG, weakened a label, or added an unsourced claim.** The five landed
edits touch four files; I re-read every changed region in full and re-ran every gate.

### UPDATED OVERALL VERDICT: **LAND** — no WRONG findings, before or after the repair round; gate (e) now passes with a fully clean log (0 undefined, 0 errors, 0 overfull, 61 pages).
===== END research/model_v4/threads/2026-08-27_t4_sections_check.md =====

---

## 6. RAW CHECK VERDICTS

Six executed checks bear on §2. Each block below is an **extract** in the sense §1 defines: the
top-level `verdict` field and the headline numbers. Every quoted string and every number is
reproduced unaltered and nothing is rounded; elisions inside a quoted string are marked `...`, the
tabular layouts are re-keyed for width, and any bracketed remark in parentheses is this bundle's
annotation rather than the JSON's. The full JSONs run from 8 KB to 514 KB — too large to paste —
and every one of them is **committed in the repository beside its script**, at the path named in
each block header; the per-node tables, the enumerated laws, the provenance blocks and the gate
lists live there.

Read the `verdict_semantics` lines where they appear. Three of these six checks are **inverted
relative to a proof check**: `pass` means the panel's measurement reproduced — that the
discontinuity is there at the quoted size and locus — and does **not** mean the assumption holds.

---

FILE: quality_reports/fixes/t2_atau_support_check.json (extract: top-level verdict fields and headline numbers)

===== BEGIN quality_reports/fixes/t2_atau_support_check.json (extract) =====
"verdict": "FAILS at calibration"
"all_pass": false,  "n_fail": 6,  "n_vacuous": 1,  "n_gate_fail": 0

"provenance": {
  "ticket": "33 (R3) -- A(tau) support enumeration, the decisive check",
  "statement_under_test": "research/model_v4/MODEL_CARD.md section 5, A(tau) Threshold chord
     restriction, clauses (tau-i) and (tau-ii), with the binding pi_bar ruling (pi_bar = the
     UPPER SUPPORT POINT of the pooled engagement posterior)",
  "not_imposed": ["Example A's |A'_kappa| = 0.25",
                  "level symmetry pi_bar = 2 pi_bar_pr",
                  "any three-point structure -- the enumeration never imposes A(tau)"],
  "label_class": "NUMERICAL -- applicability evidence for an assumption at one calibration;
     A(tau) carries no label and none moves on this run"
}

"verdict_detail": {
  "n_nodes_total": 200,
  "n_nodes_degenerate": 20,
  "n_nodes_nondegenerate": 180,
  "n_nodes_A_tau_holds": 0,
  "n_nodes_A_tau_fails": 180,
  "clause_breakdown": {
    "support_three_point_fails": 180,
    "support_kappa_free_series_fails": 18,
    "pi_bar_kappa_free_series_fails": 0,
    "derivative_pattern_A0_A1_fails": 180,
    "derivative_pattern_Ahalf_fails_inherited": 180,
    "chord_identity_fails": 180
  },
  "scope": "one calibration (params_hash in provenance), frozen policies, H = 10. This is
     evidence about A(tau)'s APPLICABILITY at the implemented two-round pooled cell, not about
     A(tau) as a hypothesis and not about any labelled result: L3, L4 leg 3 and T1 Part B are
     conditionals and their proofs are untouched"
}

"checks":  atau_wiring_reenumeration        pass=true
           atau_mean_equals_share           pass=true
           atau_support_three_point         pass=false
           atau_support_kappa_free          pass=false
           atau_pi_bar_kappa_free           pass=true
           atau_derivative_pattern_A0_A1    pass=false
           atau_derivative_pattern_Ahalf    pass=false
           atau_chord_identity              pass=false
           atau_tau_i_kernel_through_pi     pass=false   (diagnostic; not part of the verdict)

"grid": {"kappa": 10 values 0.05...0.95, "tau": 5 frozen percentiles, "T": [1,2,5,10],
         "H": 10, "n_nodes": 200, "policy": "frozen at the baseline equilibrium cutoffs"}
"n_pooled_evaluations": 920,  "seconds": 1002.43
===== END quality_reports/fixes/t2_atau_support_check.json (extract) =====

---

FILE: quality_reports/fixes/t2_p1_fournode_recheck.json (extract: top-level verdict fields and headline numbers)

===== BEGIN quality_reports/fixes/t2_p1_fournode_recheck.json (extract) =====
"verdict": "0/4 nodes RESOLVED-EXISTS after 30 seeds each; (kappa=0.15, tau=0.05, T=5): STILL
   UNRESOLVED after 30 seeds; (kappa=0.15, tau=0.075, T=1): STILL UNRESOLVED after 30 seeds;
   (kappa=0.85, tau=0.05, T=5): STILL UNRESOLVED after 30 seeds; (kappa=0.85, tau=0.075, T=1):
   STILL UNRESOLVED after 30 seeds"
"all_pass": false,  "n_fail": 4,  "nodes_so_far": 4

"provenance": {
  "ticket": "34 (R4)",
  "audit_finding": "research/model_v4/threads/2026-08-23_gpt_end_review_audit.md Finding 5
     (UPHELD as UNCHECKED)",
  "binding_criterion": "payoff scale, no adjacent-plan deviation above 1e-9 (design section 13,
     ruling 4); cutoff-scale 1e-10 diagnostic only"
}

"grid": {"n_seeds": 30, "early_stop": false}

"summary_table":
 kappa  tau     T   verdict                          best_cutoff_scale  best_payoff_scale  a3  a6
 0.15   0.05    5   STILL UNRESOLVED after 30 seeds  5.340172748e-13    1.488170939e-03    ok  ok
 0.15   0.075   1   STILL UNRESOLVED after 30 seeds  1.121325255e-14    1.059228202e-03    ok  ok
 0.85   0.05    5   STILL UNRESOLVED after 30 seeds  1.984989950e-11    3.984176881e-04    ok  ok
 0.85   0.075   1   STILL UNRESOLVED after 30 seeds  1.866240495e-11    3.061479140e-04    ok  ok

 (a3/a6 = the local proxy screens, pass at every achieving seed;
  "achieving_seed_meets_both": false at all four nodes;
  "payoff_reproduces_prior_5seed": true at all four)
===== END quality_reports/fixes/t2_p1_fournode_recheck.json (extract) =====

---

FILE: quality_reports/fixes/t2_a6_edge_jump_check.json (extract: top-level verdict fields and headline numbers)

===== BEGIN quality_reports/fixes/t2_a6_edge_jump_check.json (extract) =====
"kind": "A6 applicability evidence (panel-probe curation)"
"verdict": "A6 continuity failure REPRODUCED at calibration -- (kappa=0.5, tau_50, T=5): T_2
   jumps of 0.00633 / 0.0109 / 0.0283 across the three interior n(s) cell edges, 3/3 matching the
   card's quoted 3 s.f. figures, both panel routes agreeing to 3 s.f., the belief snap matching
   the Step 9(b) prediction and the surviving-type controls at solver noise. NO LABEL MOVES AND
   NONE IS LICENSED: A6 is a listed hypothesis of P1, so this is applicability evidence on its
   antecedent at the implemented calibration, in the A(tau) pattern -- P1 stays PROVED as a
   conditional."
"all_pass": true,  "n_fail": 0,  "checks": 20

"node": {"kappa": 0.5, "tau": 0.09076405861553302, "T": 5, "k1_held": 1.2405757282617416,
         "params_hash": "8ef7c5c2d3896bf8"}

"provenance.verdict_semantics": "INVERTED relative to a proof check. pass = the panel's
   measurement REPRODUCED, i.e. the discontinuity is there at the quoted size and locus. pass
   does NOT mean A6 holds. This file is applicability evidence and licenses no label move; A6 is
   a hypothesis of P1, not a claim of it."

"per_edge_summary":
 dying_type  edge            jump_routeA      jump_routeB      3sf     card_3sf  cross_route_rel  control_max
 9           1.583333333333  0.00633325300    0.00633378095    0.00633  0.00633   8.335746e-05     3.599697e-09
 8           1.659062162746  0.01085927707    0.01086071327    0.0109   0.0109    1.322469e-04     3.292045e-09
 7           1.749268649265  0.02827904723    0.02828146145    0.0283   0.0283    8.536777e-05     2.834033e-09

"known_discrepancies": [{
  "card_wording": "the belief snap matching the Step 9(b) prediction to ~1e-8",
  "reproduced": true,
  "measured_at_declared_bracket_1e-8": [6.7867e-09, 4.4344e-09, 5.6155e-09],
  "measured_at_probes_bracket_1e-9":   [3.9652e-08, 1.1722e-07, 1.6927e-07],
  "finding": "'~1e-8' holds at the probes' own 1e-9 bracket only for the first edge ...; at the
     other two edges the 1e-9 bracket gives 1.17e-7 and 1.69e-7. The cause is floating-point
     cancellation in Phi(b) - Phi(a) over a 1e-9-wide interval ... It is a bracket artifact, not
     a gap in the prediction: at the crossover bracket eps = 1e-8 all three residuals are ~5e-9
     ... The card's wording is optimistic by about one order of magnitude for two of the three
     edges; nothing else moves."
}]
"seconds": 164.77
===== END quality_reports/fixes/t2_a6_edge_jump_check.json (extract) =====

---

FILE: quality_reports/fixes/t2_a6_node15_check.json (extract: top-level verdict fields and headline numbers)

===== BEGIN quality_reports/fixes/t2_a6_node15_check.json (extract) =====
"kind": "A6 applicability evidence (panel-probe curation)"
"verdict": "A6 continuity failure REPRODUCED at calibration -- at (kappa=0.15, tau=0.05, T=5) the
   outer map's T_2 jumps by 0.1647 across a 1e-07 step in k_2 at the cell edge 1.749268649; the
   diagonal crossing at 1.583333333 is DESTROYED (gap +1.000e-07 just below the edge, -6.703e-02
   at it, with no zero in between); and a fixed point sits exactly ON the edge k_2 = 1.659062163
   (residual 1.064e-12), which no chamber-interior Theta can contain. NONEXISTENCE IS NEITHER
   CLAIMED NOR SHOWN -- a discontinuous self-map may still have fixed points, and two survive at
   this node. NO LABEL MOVES AND NONE IS LICENSED: A6 is a listed hypothesis of P1, so this is
   applicability evidence on its antecedent, in the A(tau) pattern -- P1 stays PROVED as a
   conditional."
"all_pass": true,  "n_fail": 0,  "checks": 5

"node": {"kappa": 0.15, "tau": 0.05, "T": 5, "k1_swept_at": 1.2, "params_hash": "77fdc51c849b2102",
         "ticket_34_status": "one of the four sweep-UNRESOLVED nodes
            (t2_p1_fournode_recheck.json)"}

"summary": {
  "jump_at_1p749268649":            0.16467681707353754,
  "destroyed_crossing_gap_below":   9.999989036835188e-08,
  "destroyed_crossing_gap_at_edge": -0.06703180149682852,
  "fixed_point_residual_on_edge":   1.06403774680075e-12,
  "full_2d_cutoff_residual":        4.750528859176484e-10
}
"seconds": 16.97
===== END quality_reports/fixes/t2_a6_node15_check.json (extract) =====

---

FILE: quality_reports/fixes/t2_a6_collapse_face_check.json (extract: top-level verdict fields and headline numbers)

===== BEGIN quality_reports/fixes/t2_a6_collapse_face_check.json (extract) =====
"kind": "A6 applicability evidence (panel-probe curation)"
"verdict": "Hold-collapse face MEASURED CLEAN at calibration -- as k_1 sweeps to full collapse
   (k_1 = k_2 = 1.5310222869) the pooled price system moves by at most 4.441e-16, U_VOICE and
   U_HOLD are bit-identical at every k_1 on the ladder and T(k) is invariant to 6.7e-16 (3 ulps at
   one row, not literally bit-identical -- see known_discrepancies). Exit and Hold pool perfectly
   at mark-path type 0, so the dying plan generates no reachable pooled history of its own and the
   continuum-face lemma does not bite. THIS IS NOT A RESCUE OF A6: the continuity clause still
   fails at this calibration, at the interior n(s) cell edges instead
   (t2_a6_edge_jump_check.json). What it establishes is that the LOCUS is not the one the
   re-derivation's change 6 named. NO LABEL MOVES AND NONE IS LICENSED -- P1 stays PROVED as a
   conditional."
"all_pass": true,  "n_fail": 0,  "checks": 5

"node": {"kappa": 0.5, "tau": 0.05, "T": 5, "k2_held": 1.5310222869, "s_eval": 1.6,
         "params_hash": "b4482d7fee83a8e8"}

"provenance.verdict_semantics": "pass = the face was measured CLEAN, i.e. N11's literal mechanism
   does not fire on this menu. That is a LOCUS finding, not a rescue of A6 and not a label move."

"ladder":
 k1            hold_region_width  max_abs_dev_from_k1_0p5  U_VOICE           U_HOLD            hold_mass
 0.5           1.0310222869       0.0                      0.04011309371544  0.03596824924978  0.5339172688
 1.0           0.5310222869       0.0                      0.04011309371544  0.03596824924978  0.2736673294
 1.2405757283  0.2904465586       4.440892098500626e-16    0.04011309371544  0.03596824924978  0.1405107031
 1.4           0.1310222869       0.0                      0.04011309371544  0.03596824924978  0.0594711515
 1.52          0.0110222869       2.220446049250313e-16    0.04011309371544  0.03596824924978  0.0047180136
 1.5310222869  0.0                0.0                      0.04011309371544  0.03596824924978  0.0

"known_discrepancies": [{
  "card_wording": "T bit-identical as k_1 sweeps to full collapse",
  "reproduced": "in substance, not literally",
  "measured_T_spread": 6.661338147750939e-16,
  "measured_T_spread_in_ulps": [0, 3],
  "U_bit_identical": true,
  "finding": "U_VOICE and U_HOLD are bit-identical at full precision, but T_2 is not: it differs
     by 6.66e-16 -- exactly 3 ulps of a double near 1.41 -- at k_1 = 1.2405757283, the row where
     the price signature itself deviates MOST ... The invariance is real and gated here at the
     map's own root-finder resolution (brentq xtol 2e-12), three orders above the observed
     spread; only the word 'bit-identical' is too strong, and only for T_2."
}]
"seconds": 10.60
===== END quality_reports/fixes/t2_a6_collapse_face_check.json (extract) =====

---

FILE: quality_reports/fixes/t2_t34_account_sweep.json (extract: top-level verdict fields and headline numbers)

===== BEGIN quality_reports/fixes/t2_t34_account_sweep.json (extract) =====
"verdict": "Ticket 34's candidate mechanical account, swept over the three nodes it had not been
   probed at: 3/3 HOLDS.  (kappa=0.15, tau=0.075, T=1): HOLDS; (kappa=0.85, tau=0.05, T=5):
   HOLDS; (kappa=0.85, tau=0.075, T=1): HOLDS.  This is diagnostic evidence about WHY the
   ticket-34 recheck stalls at these nodes; no label moves and none is licensed (A3 and A6 are
   listed hypotheses, P1 stays PROVED as a conditional), and existence at these nodes is neither
   claimed nor denied -- an edge-pinned fixed point of the implemented cutoff map is not an
   equilibrium, and a stalled search is not a nonexistence proof.  The account graduates from
   'candidate, UNCHECKED beyond one node' to exactly this per-node record.  The fourth node,
   (kappa=0.15, tau=0.05, T=5), is the one the A6 panel already probed and is not re-adjudicated
   here; its values are carried as the reference the thresholds were set against."
"all_pass": true,  "n_fail": 0,  "nodes_so_far": 3

"provenance": {
  "account_under_test": "a located fixed point of the implemented cutoff map sits ON an n(s) cell
     edge, where U_HOLD - U_VOICE jumps through zero without crossing it (n(s) is
     integer-valued)",
  "verdict_rule": "PRE-REGISTERED, see the module docstring.  HOLDS = signature (i) (edge-pinned
     jump through zero, manifestation A pinned fixed point or B at-edge worst deviation) AND (ii)
     (residual reproduction, plus bracketing where two or more independent configurations exist)
     AND (iii) (the a6_A proximity negative's per-node input replicates and the achieving fixed
     point is not itself pinned).  DIFFERENT MECHANISM = (i) absent with the diagnostic clean.
     INCONCLUSIVE = anything mixed or obstructed.",
  "framing": "DIAGNOSTIC EVIDENCE about why the ticket-34 recheck stalls at these nodes.  No
     label moves and none is licensed: A3 and A6 are listed hypotheses and P1 stays PROVED as a
     conditional.  Existence of equilibrium at these nodes is neither claimed nor denied -- an
     edge-pinned fixed point of the implemented cutoff map is NOT an equilibrium (its
     payoff-scale residual is 1e-3-grade against a 1e-9 criterion), and a stalled search is not a
     nonexistence proof.",
  "smoke_gate": ".venv/bin/python -m numerical_v4.smoke run before this script: exit 0,
     SMOKE COMPLETE in 66.9 s"
}

"summary_table":
 kappa tau    T  account  manifestation                 edge            offset_from_edge  gap_below      gap_above     jumps_through_zero_without_crossing
 0.15  0.075  1  HOLDS    A -- pinned fixed point       1.4601789933084  -1.4455e-13       -4.655791e-04  1.397725e-03  true
 0.85  0.05   5  HOLDS    B -- at-edge deviation        1.5833333333333  null              -1.352819e-03  1.087243e-03  true
 0.85  0.075  1  HOLDS    A -- pinned fixed point       1.5179323973782   9.7877e-13       -1.313775e-03  5.241067e-04  true

 (signatures i/ii/iii all true at all three nodes; recorded_best_payoff_scale
  1.059228e-03 / 3.984177e-04 / 3.061479e-04; sigma_s distances measured 0.0258 / 0.0437 / 0.0295
  against recorded 0.026 / 0.044 / 0.030; "diagnostic_clean": true at all three)
"seconds": 805.27
===== END quality_reports/fixes/t2_t34_account_sweep.json (extract) =====

---

## 7. THE DRAFT_V3 THEORY SECTIONS

These are the ticket-08 sections of §2(f): the first place this stack's labels meet paper prose.
They are the object of the independent checker report in §5, and they build from the repository
root as a standalone document (0 undefined references, 0 errors, 0 overfull boxes, 61 pages).

**The statements are what to re-read against the card.** `theorem_section.tex` carries every result
in §3's ledger, and it is transcribed with the labels and their conditionality intact — "PROVED
under A($\tau$)", "PROVED at fixed policies", "legs 1–2 outright, leg 3 under A(br)", and the
evidence notes that say where those antecedents are measured to fail. A dropped conditional here
would be the single most consequential error in this bundle, and it is the error a checker inside
the lane is least equipped to see. `model_section.tex` carries the primitives, the timing, the
equilibrium notion and the assumption block those statements quantify over, so the two are read
together.

**The proofs are represented by their openings only.** `sections_v3/` carries three proof files
totalling 2,880 lines — full proofs of D1, L1, L2, L3, L4, P1, T1 and C1. **Inlining them would
roughly double this bundle**, so §7.3 gives, for each of the eight proofs, its `\begin{proof}` line
through the end of its first step, plus a one-line pointer saying what the proof does and where its
weight sits. **The full files are in the repository**, at the paths named in each block header, and
the card rows in §3 carry the proof-read and re-derivation evidence for every one of them. If an
opening plus the statement in §7.1 is not enough to rule on a result, that is an **UNCHECKED**
finding and should be returned as one — do not treat a proof you could not read as a proof you
found sound.

---

### 7.1 The results section — every statement, with its label and conditionality

FILE: sections_v3/theorem_section.tex (verbatim, complete)

===== BEGIN sections_v3/theorem_section.tex =====
%==============================================================================
%  sections_v3/theorem_section.tex -- the results section of draft_v3.
%
%  SOURCE OF TRUTH: research/model_v4/MODEL_CARD.md, version stamp 2026-08-27
%  (A6 panel resolution, commit ae9caea), section 6 result ledger.  The eight
%  results appear in the ledger's own order and at its grain: D1, L1, L2, L3,
%  L4, P1, T1, C1.  Every hypothesis clause of every card row travels with the
%  statement that carries it; the crosswalk in the ticket 08 scratchpad walks
%  them one by one.  Honesty labels are transcribed verbatim from the ledger,
%  conditionality included.
%
%  Proofs live in sections_v3/proofs_section.tex; no proof environment appears
%  in this file.
%==============================================================================

\section{Results}
\label{sec:results}

Eight results follow, in the order the model builds them: the partition and its accounting
identities, then what liquidity does inside each cell, then existence, then the attenuation theorem,
then what survives the move from fixed policies to equilibrium. Each statement carries the honesty
label of the record it comes from, and each carries that label's conditionality with it. The
conditionality is not decoration; where a hypothesis has been measured and found to fail at the
calibration the accompanying implementation runs, the statement says so beside itself rather than in
an appendix.

\subsection{The partition and its accounting identities}
\label{sec:partition-results}

\begin{lemma}[D1: the disclosure partition and the price-path decomposition]
\label{lem:D1}
Assume Assumptions~\ref{asm:A1}, \ref{asm:A2p}, \ref{asm:A4} and \ref{asm:A5}; the primitive table
restrictions of Assumption~\ref{asm:TR}; the cutoff selection map of Definition~\ref{def:cpbe}\,(i); and the two price
conventions of Definition~\ref{def:prices}, namely $P_{-1}^P = \Eop[Y]$ and
$P_{\ND} = P_{f^-}^P$. Assume in addition the two clauses now carried as primitives: Borel
regularity of $s \mapsto B_j(s,d)$ for \emph{every} plan including Exit, clause (TR-ii), which is
needed only for part~(c) below because pooled pricing integrates over every type; and a content for
the control-node information set $\mathcal I_H$, supplied by Definition~\ref{def:prices}. Then:
\begin{enumerate}[label=(\alph*),leftmargin=2.4em,itemsep=3pt]
\item the disclosure indicator $D = \ind\{a = 1,\ c(\tau) + T \le H\}$ is measurable, and it maps
  every control-node history into exactly one cell;
\item for every Voice plan, $f_j \le H$ if and only if $B_j(s, H-T) \ge \tau$;
\item each flagged history yields $B^F$, $R_d$, $R$ and $J$, and these satisfy the exact identity
  \begin{equation}
  \label{eq:runup-jump}
  P^F - P_{c^-}^P \;=\; R + J.
  \end{equation}
\end{enumerate}
\end{lemma}
\resultstatus{PROVED}

The proof is in Section~\ref{sec:proofs}. Part~(b) is the \emph{clock equivalence} that
Lemma~\ref{lem:L4} and Theorem~\ref{thm:T1} both consume: it converts a statement about the filing
date into a statement about the stake path $T$ days before the horizon, which is what makes window
comparisons tractable.

\begin{lemma}[L1: two-cell decomposition of the engagement premium]
\label{lem:L1}
Assume Lemma~\ref{lem:D1}; the definitions of Definitions~\ref{def:prices} and \ref{def:premium};
Assumption~\ref{asm:A5}, which pins \emph{the} version of $\Eop[Y \mid \mathcal I]$;
Assumption~\ref{asm:A2p} together with clause (TR-i), under which $\Delta_m$ is finite; and
Assumption~\ref{asm:A1}, which puts every object on one probability space. Then whenever
$0 < \Omega < 1$,
\begin{equation}
\label{eq:L1}
\Dact \;=\; \Omega\,M_F \;+\; (1-\Omega)\,M_P .
\end{equation}
At $\Omega = 1$ the identity degenerates to $\Dact = M_F$, and at $\Omega = 0$ to $\Dact = M_P$; in
each degenerate case the average over the null cell is \emph{undefined rather than imputed}. That
last clause is a non-identification statement, and it is proved rather than asserted.
\end{lemma}
\resultstatus{PROVED}

The proof is in Section~\ref{sec:proofs}.

\subsection{Liquidity in the flagged cell}
\label{sec:flagged-results}

\begin{lemma}[L2: $\kappa$-invariance of the flagged cell]
\label{lem:L2}
At fixed cutoff \emph{and} execution policies, assume Assumption~\ref{asm:A1};
Assumption~\ref{asm:A2p} \emph{together with} the primitive table restrictions of
Assumption~\ref{asm:TR}; Assumption~\ref{asm:A4}; Assumption~\ref{asm:A5};
Assumption~\ref{asm:A7p} in its on-path injective form, consumed almost surely on the flagged
set;\footnote{``Almost surely'' is the permissive reading, and it is the only coherent one when
$B^F$ is continuum-valued, since then no individual flagged tuple has positive probability.}
Lemma~\ref{lem:D1}; the no-feedback timing of Assumption~\ref{asm:nofeedback}; and $\Omega > 0$.
Assume also an explicit bidder-entry rule --- either \eqref{eq:entry} or any rule with the two
properties named in the proof --- which is carried as bookkeeping. Then the flagged tuple
$\Sfl = (B^F, Q^F, a{=}1)$ makes the pre-filing pooled history conditionally independent of
$(v,s,\xi)$ on the flagged set, and consequently the flagged posterior, the flagged price, the entry
probability and $M_F$ are all invariant to $\kappa$.
\end{lemma}
\resultstatus{PROVED}

The proof is in Section~\ref{sec:proofs}. Assumption~\ref{asm:A7} in its weak identification wording
is not sufficient here: it permits two pairs $(j,s)$ with different pooled paths, which is this
lemma's first failure case. The form consumed is Assumption~\ref{asm:A7p}, named as such.

\subsection{Liquidity in the pooled cell}
\label{sec:pooled-results}

\begin{lemma}[L3: interior motion of the pooled premium under the chord restriction]
\label{lem:L3}
Assume $\Atau$ (Assumption~\ref{asm:Atau}), including both of its clauses: ($\tau$-i),
kernel-through-posterior, and ($\tau$-ii), $\kappa$-free support \emph{and} $\kappa$-free $\bar\pi$.
Assume in addition: $h(0) = 0$; $\kappa$-free pooled mass and $\kappa$-free pooled engagement moment
at fixed policies; Lemma~\ref{lem:D1} by statement; and regularity stated minimally --- $h$
continuous on $[0,\bar\pi]$ and twice differentiable on the open interval $(0,\bar\pi)$, Darboux's
theorem doing the rest, with no continuity of $h''$ required. For the small-$\bar\pi$ corollary
(part~(c)) assume also a second-order Peano expansion of $h$ at $0+$ and one and the same kernel
along the shrinking family; and for the seam at which Lemma~\ref{lem:L4} consumes this lemma, assume
$|\Akap|$ bounded \emph{uniformly in $\bar\pi$} along the limit. Then:
\begin{enumerate}[label=(\alph*),leftmargin=2.4em,itemsep=3pt]
\item $\partial_\kappa \Eop_\kappa[h] = \Akap\,C_h(\bar\pi)$, exactly;
\item $C_h(\bar\pi) = \tfrac14\bar\pi^2 h''(\zeta)$ for some $\zeta \in (0,\bar\pi)$ --- an identity,
  not an approximation;
\item $C_h = \tfrac14 h''(0)\,\bar\pi^2 + o(\bar\pi^2)$, so the interior motion vanishes at rate
  $\bar\pi^2$ as $\bar\pi \downarrow 0$.
\end{enumerate}
The statement is an ``if'' and never an ``iff'': $\Akap = 0$ also kills the interior motion.
\end{lemma}
\resultstatus{PROVED under $\Atau$}

The proof is in Section~\ref{sec:proofs}. The conditionality is the substance of the result, not a
caveat on it. Whether the two-round pooled cell of Section~\ref{sec:timing} satisfies the support
condition of $\Atau$ is \textbf{open}: the discussion after Assumption~\ref{asm:Atau} shows that the
support condition is the assumption's entire remaining bite, and exhibits a one-round market that
satisfies it and a no-disclosure structure that does not; the weakest sufficient conditions for the
two-round case are named in the closing steps of the proof in
Section~\ref{sec:proofs}. Remark~\ref{rem:AtauRecord} records that at the implemented calibration the
support condition fails at all $180$ non-degenerate nodes; at that calibration this lemma therefore
says nothing about the implemented pooled cell, and its label is untouched by that fact.

\begin{lemma}[L4: threshold tightening --- nesting, composition, and the pooled sensitivity]
\label{lem:L4}
At fixed policies, for $b_0 < \tau' < \tau$ at a common window $T$ and a common $\kappa$, with
$\Omega(\tau',T) < 1$:
\begin{enumerate}[label=(leg \arabic*),leftmargin=3.4em,itemsep=3pt]
\item \emph{(unconditional)} $\mathcal C_F(\tau,T) \subseteq \mathcal C_F(\tau',T)$, with every newly
  flagged history generated by a Voice plan; hence $\Omega(\tau',T) \ge \Omega(\tau,T)$.
\item \emph{(unconditional)} The pooled engagement \emph{share} falls,
  $\bar\pi_{\mathrm{pr}}(\tau') \le \bar\pi_{\mathrm{pr}}(\tau)$, with an exact identity for the
  difference between the two shares.
\item \emph{(under $\Abr$)} $\mathcal S_P(\tau',T) \le \mathcal S_P(\tau,T)$, with equality whenever
  $C_h(\bar\pi(\tau)) = 0$.
\end{enumerate}
Legs 1 and 2 need only: the clock equivalence of Lemma~\ref{lem:D1}\,(b); the no-feedback timing of
Assumption~\ref{asm:nofeedback}; fixed policies; $b_0 < \tau' < \tau$ imposed at \emph{both}
thresholds; Assumptions~\ref{asm:A1} and \ref{asm:A4}; clause (TR-iii)'s implication
$D = 1 \Rightarrow a = 1$; and $\Omega(\tau') < 1$. Nestedness is a \emph{conclusion} of leg 1, not a
hypothesis of it. Leg 3 additionally needs: Lemma~\ref{lem:L3} by statement; the maintained
\emph{magnitude} monotonicity of $|C_h|$ in $\bar\pi$ from Assumption~\ref{asm:Atau}, the sign half
$C_h \le 0$ being unused at this leg; and clauses (br-i)--(br-v) of Assumption~\ref{asm:Abr}.
\end{lemma}
\resultstatus{PROVED (legs 1--2 outright; leg 3 under $\Abr$)}

The proof is in Section~\ref{sec:proofs}. Leg 3 inherits the conditionality of
Assumption~\ref{asm:Abr}, and through clause (br-i) it inherits the representation \eqref{eq:atau} at
\emph{both} compared thresholds; Remark~\ref{rem:AtauRecord} therefore bears on leg 3 as directly as
it bears on Lemma~\ref{lem:L3}. At the implemented calibration leg 3's antecedent is not satisfied,
and at that calibration leg 3 says nothing about the implemented pooled cell. Legs 1 and 2 are
unaffected: they consume no chord restriction. Clause (br-iii) is the clause with the least
justification behind it and is the one to attack first.

\subsection{Existence}
\label{sec:existence-results}

The existence result is stated as a proposition rather than as a theorem: the paper has one theorem,
Theorem~\ref{thm:T1}, and existence is the standing-ground for it rather than the claim the paper is
making. Its hypothesis set is long, and every clause of it is load-bearing --- the 2026-08
demotion and restoration of this result turned on exactly which form of one hypothesis the argument
consumed --- so the hypotheses are enumerated rather than gathered into a sentence.

\begin{proposition}[P1: existence of a cutoff perfect Bayesian equilibrium]
\label{prop:P1}
Assume:
\begin{enumerate}[label=(P-\arabic*),leftmargin=3.2em,itemsep=3pt]
\item Assumption~\ref{asm:A1} (independent primitives);
\item Assumption~\ref{asm:A2p} (finite model, integrable objective);
\item Assumption~\ref{asm:A3} (ordered plans, single crossing);
\item Assumption~\ref{asm:A4} (legal-clock discipline);
\item Assumption~\ref{asm:A6} (compact outer self-map), read as in the second trailing paragraph
  below;
\item Assumption~\ref{asm:A7J}, \emph{joint tuple injectivity}: the map
  $(j,s) \mapsto (B_j^F, Q_j^F, a_j)$ is injective on the whole flagged-pair set
  $\{(j,s) : D_j = 1\}$, \emph{including pairs no cutoff vector selects}. This is strictly stronger
  than the on-path form, Assumption~\ref{asm:A7p}, and it is the form the argument consumes where it
  pins \emph{off-path} flagged beliefs;\footnote{The distinction is not cosmetic. Before 2026-08-25
  the recorded statement of this result carried the on-path form while the proof consumed the joint
  form, so the two verification passes on file covered two different statements; that mismatch is
  what the 2026-08-23 demotion turned on, and the statement here is the amended one, re-verified by
  a fresh adversarial proof-read and an independent statements-only re-derivation, both 2026-08-25
  and both by agents who did not write the proof. The form is named every time either appears.}
\item Lemma~\ref{lem:D1} by statement, \emph{with its own hypotheses travelling};
\item the no-feedback timing of Assumption~\ref{asm:nofeedback}, read together with the
  flag-termination clause of Assumption~\ref{asm:flagterm};
\item the \emph{definitional} round-2 action-set hypothesis: the flagged-round action set \emph{is}
  the plan-generated set $\{Q^F_{j'}(s)\}$ taken over menu elements agreeing with $j$ on everything
  already played. This is not a closure condition; the closure form is jointly unsatisfiable with
  finiteness, by cardinality;
\item \emph{continuation-cost equivalence on that same set}: menu elements sharing $j$'s pooled path
  up to $f_j(s)$ and carrying $a_{j'} = a_j$ have the same engagement cost, $C_{j'}(s) = C_j(s)$.
  This holds trivially on any single-Voice menu, where the set is a singleton, and it is live only on
  menus with two or more Voice plans sharing a pooled path. What it buys, under the
  plan-completion reading of the timing convention in Remark~\ref{rem:Ctiming}, is this: on that set
  the flagged price does not move and the flagged order cancels, so the engagement cost is the only
  thing that can differ between staying and deviating, and at a flagged pair the cutoff vector does
  not select there is no date-$0$ optimality to fall back on --- so without this clause the deviator
  takes the class member with the smallest cost and requirement (ii) of Definition~\ref{def:cpbe}
  fails at that node. Under the sunk reading the continuation is constant on the deviation set with
  no clause at all and this hypothesis is not consumed; it is listed because the statement does not
  commit to a reading, and it is what makes the conclusion hold under both;
\item the restriction $m_0 \ge 0$ of \eqref{eq:m0};
\item the blockholder-objective definition of Definition~\ref{def:U}, whose $-a_j C_j(s)$ term is
  the display \eqref{eq:Uj}, together with the timing convention for $C_j(s)$ in
  Remark~\ref{rem:Ctiming} --- the engagement cost may be booked on completing the plan or as sunk
  once the filing has landed, the two give the same round-2 comparison on the round-2 deviation set,
  and the result does not depend on the choice;
\item the primitive table restrictions \ref{asm:TR} that the argument consumes, in particular: the
  terminal payoff \eqref{eq:Y} with the price convention $P(\mathcal I) = \Eop[Y \mid \mathcal I]$
  and the entry rule \eqref{eq:entry}, both from clause (TR-iv); clause (TR-ii)'s Borel regularity
  for \emph{every} plan including Exit, needed here \emph{directly} and not by way of
  Lemma~\ref{lem:D1}, whose conclusion is measurability of $D$ and the cell map; clause (TR-iii)'s
  implication $D = 1 \Rightarrow a = 1$, the definitions of $c$, $f$, $B^F$, $Q^F$ and $b^*$, and
  $\partial_s B_j \ge 0$ for Voice; and clause (TR-i)'s distributional forms with $\Delta_m > 0$.
\end{enumerate}
Then \emph{at every $\kappa \in [0,1]$} a cutoff perfect Bayesian equilibrium over complete
contingent plans exists: there is $k^\star \in \Theta$ with $k^\star = \Tmap(k^\star;\vartheta)$,
prices at their inner fixed points and beliefs Bayes-consistent on path, together with the following.
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=3pt]
\item Off-path beliefs are limits of \emph{one} full-support perturbation family over plans, fixed
  once and used to define the price system at every $k \in \Theta$ and not only at $k^\star$ ---
  because the deviation payoffs that define $\Tmap$ read off-path pooled histories --- at every
  pooled history reachable \emph{with positive probability} under some plan profile.
\item The boundary values of $\kappa$ are handled by \emph{extension}, not by restriction. At
  $\kappa \in \{0,1\}$ the noise support degenerates to $\{0\}$ and to $\{\pm\bar z\}$ respectively;
  a pooled history needing a mark outside the surviving support is null under \emph{every} profile,
  so it is off nature's path rather than off the players', carries no requirement under
  Definition~\ref{def:cpbe}\,(vi), and is read by no step. No cut to $\kappa \in [0,1)$ is taken, and
  the earlier claim of a belief at \emph{every} pooled history --- false at $\kappa = 1$ --- is
  withdrawn.
\item Flagged-tuple beliefs are supplied by Assumption~\ref{asm:A7J} at every tuple in the image of
  the flagged-pair map $(j,s) \mapsto (B_j^F,Q_j^F,a_j)$, on path and off, since the image includes
  tuples generated by pairs the cutoff vector does not select. The belief is the point mass at the
  unique generating pair. That point mass is a \emph{version} of the conditional law at every image
  tuple --- the signal is continuous, so a version is what a conditional law is, and any a.e.-equal
  version serves requirements (iii) and (vi) of Definition~\ref{def:cpbe} equally --- and it is the
  version this equilibrium selects. No tuple outside that image arises, because the round-2
  action-set hypothesis (P-9) leaves no off-menu order to produce one.
\item The bidder follows the entry rule \eqref{eq:entry}.
\item There is a sequentially optimal flagged component at \emph{every} flagged pair $(j,s)$,
  whether or not the cutoff vector selects it. The flagged price is invariant across the round-2
  deviation set, since Assumption~\ref{asm:A7J} pins the belief at the same $s$ and at $\pi = 1$, so
  the flagged order cancels out of the continuation and hypothesis (P-10) makes what remains
  constant.
\end{enumerate}
Two readings belong to the statement rather than to the proof. First, \emph{Assumption~\ref{asm:A5}
is not assumed here}: its existence and uniqueness content is derived from $m_0 \ge 0$, its
continuity content from the same scalar reduction, and its measurable-selection content from
Assumption~\ref{asm:A7J} together with clause (TR-ii)'s Borel regularity. Second,
\emph{Assumption~\ref{asm:A6} is read} as asserting that $\Tmap$ --- under a named
tie-break-and-corner selection, without which a correspondence cannot be called continuous --- is a
well-defined, single-valued, continuous self-map of $\Theta$, with $\Theta$ nonempty as in
Definition~\ref{def:theta}.

Finally, \emph{at any such equilibrium at which Assumption~\ref{asm:A8} holds}, both cells carry
strictly positive probability and both are on path; and for the restatement of
Assumption~\ref{asm:A8} as a single signal threshold, add H-ord --- Voice stake monotonicity across
plans --- and the upper-set engagement-flag hypothesis. \emph{Uniqueness is not claimed.}
\end{proposition}
\resultstatus{PROVED}

The proof is in Section~\ref{sec:proofs}.

\begin{remark}[Numerical record for Proposition~\ref{prop:P1}]
\label{rem:P1record}
The label above rests on the proof and on the two 2026-08-25 verification passes, not on a grid, and
the grid evidence is stated separately for that reason. Four nodes of the equilibrium sweep ---
$\kappa \in \{0.15,\,0.85\}$ crossed with $(\tau,T) \in \{(0.05,\,5),\,(0.075,\,1)\}$ --- remain
STILL UNRESOLVED after $30$ seeds each: the best payoff-scale residual runs
$3.1\times10^{-4}$ to $1.5\times10^{-3}$ against a $10^{-9}$ criterion, while the best cutoff-scale
residual runs $10^{-14}$ to $10^{-11}$. The A3 and A6 proxies pass at every achieving seed, which,
as Remark~\ref{rem:A3record} explains, is not evidence that those hypotheses hold: the proxies are
local screens and are silent on argmax monotonicity over $s$ and on continuity of $\Tmap$ in $k$.
This evidence is UNCHECKED: existence at those four nodes is neither claimed nor denied by
it. Record: \texttt{quality\_reports/fixes/t2\_p1\_fournode\_recheck.json}.

Two hypotheses of this proposition carry their own measured failures at the implemented calibration.
Assumption~\ref{asm:A6}'s continuity clause fails there for the $\Theta$ this argument constructs
(Remark~\ref{rem:A6record}), and Assumption~\ref{asm:A3} fails there at two independently found loci
(Remark~\ref{rem:A3record}). Neither moves a label, and none is licensed to: both are hypotheses.
The proposition stays PROVED as a conditional, in the same pattern as $\Atau$ --- what is on
record is that its antecedent, read with the $\Theta$ the proof constructs, is not satisfied by the
implemented calibration, so at that calibration the proposition asserts nothing about the implemented
cell. Nonexistence is neither claimed nor shown anywhere: $23$ of $27$ sweep nodes converge, and two
fixed points survive even at the worst probed node.
\end{remark}

\subsection{Disclosure attenuation}
\label{sec:attenuation}

\begin{theorem}[T1: disclosure attenuation at fixed policies]
\label{thm:T1}
At fixed plan and cutoff policies, with $0 < \Omega < 1$ and $\mathcal S_P > 0$, and under the
hypotheses (T-1)--(T-15) listed below:
\begin{enumerate}[label=(\Alph*),leftmargin=2.4em,itemsep=3pt]
\item \emph{Factorisation.} $\mathcal S = (1-\Omega)\,\mathcal S_P$, exactly; and the same
  factorisation holds for the total-variation aggregate of $\Dact$ over any $\kappa$-grid, with no
  differentiability required.
\item \emph{Threshold margin.} Threshold tightening attenuates:
  \begin{equation}
  \label{eq:T1B}
  \frac{\mathcal S(\tau')}{\mathcal S(\tau)} \;=\; W_\tau\,C_\tau \;\le\; 1,
  \end{equation}
  because \emph{both} ratios lie in $[0,1]$. No dominance condition is needed.
\item \emph{Window margin.} Window tightening attenuates \emph{if and only if} $W_T C_T \le 1$, where
  $W_T \le 1$ is proved --- from the clock equivalence of Lemma~\ref{lem:D1}\,(b) and the monotone
  Voice stake path --- and $C_T$ is \emph{unsigned}. The equivalent form
  \begin{equation}
  \label{eq:T1C}
  \frac{\partial_{r_T}\mathcal S_P}{\mathcal S_P} \;\le\; \frac{\Omega_{r_T}}{1-\Omega}
  \end{equation}
  holds \emph{on average along the tightening path}, integrated over $[-T,-T']$, and exactly in the
  infinitesimal limit; read pointwise, \eqref{eq:T1C} is false.
\end{enumerate}
The hypotheses are: (T-1) fixed policies; (T-2) Assumption~\ref{asm:A8} at each compared policy;
(T-3) $\mathcal S_P > 0$; (T-4) Lemma~\ref{lem:L1}; (T-5) Lemma~\ref{lem:L2}, with its own
hypotheses travelling; (T-6) Lemma~\ref{lem:D1}; (T-7) PE-$\Omega$, that is
$\partial_\kappa\Omega = 0$ at fixed policies --- derivable rather than assumed, and it is exactly
what fails in general equilibrium, which is the term Proposition~\ref{prop:C1} bounds; (T-8)
$\kappa$-differentiability of $M_P$, which no standing hypothesis of Section~\ref{sec:hypotheses}
supplies and which is therefore carried in the proof; (T-9) Assumption~\ref{asm:Atau} at
\emph{both} compared policies, with $\bar\pi$ read as the upper support point; (T-10)
Lemma~\ref{lem:L3}; (T-11) clauses (br-i)--(br-v) of Assumption~\ref{asm:Abr} at the threshold pair;
(T-12) Lemma~\ref{lem:L4}; (T-13) the no-feedback timing of Assumption~\ref{asm:nofeedback}; (T-14) a
smooth window interpolation, for the local form \eqref{eq:T1C} only; and (T-15) threshold-side
smoothness, which has been confirmed non-load-bearing. \emph{No unconditional window sign is
claimed.}
\end{theorem}
\resultstatus{PROVED at fixed policies}

The proof is in Section~\ref{sec:proofs}. Part~(A) is the weight effect in its exact form: the
liquidity sensitivity of the expected engagement-related premium is the pooled cell's sensitivity,
scaled by the pooled cell's weight. Part~(B) is the threshold-margin result and needs no dominance
condition, because the weight ratio and the composition ratio both lie in $[0,1]$. Part~(C) is the
window-margin result, and it is an ``if and only if'' rather than a sign: the composition ratio $C_T$
is unsigned, so the model does not deliver window-margin attenuation as a theorem.

\begin{remark}[Numerical record for Theorem~\ref{thm:T1}]
\label{rem:T1record}
Part~(B) rests on Assumption~\ref{asm:Atau} at both compared policies (T-9), on Lemma~\ref{lem:L3}
(T-10), and on Assumption~\ref{asm:Abr} (T-11). Remark~\ref{rem:AtauRecord} records that the support
condition of $\Atau$ fails at all $180$ non-degenerate nodes of the implemented calibration, and
clause (br-i) carries that representation at both thresholds, so the record bears on (T-9) and (T-11)
alike. Part~(B) stays PROVED as a conditional with its proof untouched; at this calibration
it says nothing about the implemented pooled cell. No label moves.

For Part~(C) the genuine window-margin record is block 4 of the executed T1 check: $W_T C_T < 1$ at
every checked node at this calibration, with an $H = 10$ corner caveat recorded in the handoff.
That is NUMERICAL node evidence at one calibration and not a sign theorem, which Part~(C)
does not claim. One distinction is worth stating because it is easy to lose: the O-1 comparison,
whose ratios $1.06397$, $1.18373$, $1.13631$ and $0.37798$ at
$\Omega = 0.037252$, $0.128950$, $0.285804$ and $0.50$ are sometimes read as a window test, is a
\emph{disclosure-regime} comparison at a fixed filing window in the static repository model. Those
ratios are regime-comparison composition outcomes; they are not $W_T C_T$ and they measure no window
pair. The analogy is useful only because it shows that a composition factor can exceed one, which is
what motivates the genuine window-margin ``if and only if'' above; the O-1 cut at
$\Omega^\star \approx 0.343$ is a disclosure-regime boundary, not a window boundary.
\end{remark}

\subsection{From fixed policies to equilibrium}
\label{sec:ge-results}

Theorem~\ref{thm:T1} holds at fixed policies, and hypothesis (T-7) is exactly what fails once the
cutoff vector is allowed to move with $\kappa$. The next result asks what survives that move. It
carries the region as a \emph{named hypothesis} rather than exhibiting one.

\begin{proposition}[C1: the dominance-and-contraction implication in general equilibrium]
\label{prop:C1}
Assume:
\begin{enumerate}[label=(C-\arabic*),leftmargin=3.2em,itemsep=3pt]
\item the along-the-path contraction of Assumption~\ref{asm:AGE}, $L_{\mathcal R} < 1$, in
  \emph{one fixed norm convention} --- an induced operator norm with its dual pairings; a mismatched
  pairing silently voids the implication;
\item $\mathcal R_r$ relatively open in \emph{both} coordinates, with $\kappa \notin \{0,1\}$;
\item an interior single-branch equilibrium;
\item twice continuous differentiability of $\Dact$ in $(k,\kappa,r)$;
\item a non-vanishing \emph{equilibrium} liquidity derivative --- the equilibrium sensitivity
  $\mathcal S^{GE}$, which is distinguished from the fixed-policy sensitivity $\mathcal S$ of
  Definition~\ref{def:premium};
\item strict dominance $g_r^{PE} > \mathcal B_r^{GE}$ on the region, with $g_r^{PE}$ as in
  \eqref{eq:gPE} and $\mathcal B_r^{GE}$ as in \eqref{eq:BGE};
\item the \emph{threshold} margin $r_\tau$ only: the window coordinate is an integer, and nothing
  local is claimed there.
\end{enumerate}
Then the fixed-policy attenuation sign survives in equilibrium on the region:
\begin{equation}
\label{eq:C1}
\partial_r \mathcal S^{GE} \;\le\; -\eta_r \;<\; 0 .
\end{equation}
The sign-coherence hypothesis --- that the fixed-policy attenuation sign agrees with the equilibrium
sign --- is confirmed unused in \eqref{eq:C1}: its work is one of naming, fixing when that conclusion
may be called a survival of the fixed-policy sign. The sign-constancy clause of
Assumption~\ref{asm:AGE} is likewise unused.
\end{proposition}
\resultstatus{PROVED (dominance-and-contraction implication; region-as-hypothesis) plus NUMERICAL
node evidence}

The proof is in Section~\ref{sec:proofs}.

\begin{remark}[Numerical record for Proposition~\ref{prop:C1}]
\label{rem:C1record}
Eighteen of eighty grid nodes are pointwise \emph{dominance-and-contraction nodes}. The largest
contiguous block is $T = 5$ at $\tau$-percentiles $\{50,70,90\}$ with
$\kappa \in \{0.65,\,0.75,\,0.85\}$; the slack $\eta_r$ has minimum $0.0595$ and median $0.3467$, and
$L_{\mathcal R} \in [0.264,\,0.501]$ everywhere on the grid. These come from the executed committed
check, independently re-run on 2026-08-22, on which all values reproduce. What these nodes verify is
narrow and worth stating exactly: they verify the two pointwise inequalities $L_{\mathcal R} < 1$ and
$\eta_r > 0$ together with supporting diagnostics. They do \emph{not} verify the full antecedent
(C-1)--(C-7) above, and they do \emph{not} exhibit a named nonempty region. A dominance-and-contraction
node is not a fifth honesty label. Record:
\texttt{quality\_reports/fixes/t2\_c1\_region\_check.py} and \texttt{t2\_c1\_region\_check.json},
with the independent re-run verify note beside them. The re-derivation on file adds the bound
$\mathcal B_r^{GE} = O\bigl((1-L_{\mathcal R})^{-3}\bigr)$, so the dominance-and-contraction nodes
are cubically bounded away from $L_{\mathcal R} = 1$.

A named-region promotion is a separate step and is not claimed. The earlier aspiration --- this
result PROVED on a named nonempty region and NUMERICAL off it --- is retired as
structurally undeliverable as worded. What is deliverable is the three objects above: the
implication PROVED with the region as a hypothesis, the dominance-and-contraction nodes
NUMERICAL, and a named-region promotion left open, for which the $\varepsilon$-ball plus
integral-control pattern of the frozen manuscript's D8 is the template.
\end{remark}

\subsection{What is not claimed}
\label{sec:not-claimed}

The results above do not claim: a global window-margin attenuation sign; $\kappa$-invariance of the
filing-day jump $J$; equilibrium uniqueness; a nonempty general-equilibrium region as a theorem;
endogenous filing before the deadline; noisy or partially revealing flagged-round trading;
continuous-time execution; welfare or optimal rule design; that the frozen manuscript's hump result
survives; that the prior calibration at $\Omega \approx 0.037$ is economically meaningful; or any
empirical value for the disclosed share of engagements $\omega_a$.

Three questions remain open, in whole or in part, and are recorded as such. The third was answered in
substance on 2026-08-27; what survives of it is scoped below rather than left standing.
\begin{enumerate}[label=(\arabic*),leftmargin=2.4em,itemsep=3pt]
\item \emph{Whether the two-round pooled cell of Section~\ref{sec:timing} satisfies $\Atau$.}
  Lemma~\ref{lem:L3} shows that the entire remaining bite of the restriction is its support
  condition, exhibits a one-round market that satisfies it and a no-disclosure structure that does
  not, and names the weakest sufficient conditions for the two-round case. Lemma~\ref{lem:L3},
  leg 3 of Lemma~\ref{lem:L4} and Part~(B) of Theorem~\ref{thm:T1} are all conditional on it, which
  makes this the largest single conditionality the ledger carries.
\item \emph{Whether an equilibrium in which the blockholder chooses the fully separating plan exists
  on a given calibration.} Menus satisfying Assumption~\ref{asm:A7p} are fully separating on the
  flagged set, so the burden did not disappear when satisfiability was resolved; it moved to
  incentive compatibility, which Proposition~\ref{prop:P1} does not settle. Relatedly, that
  proposition does not claim that an equilibrium satisfying Assumption~\ref{asm:A8} exists --- only
  that Assumption~\ref{asm:A8} holding \emph{at} an exhibited equilibrium puts both cells on path.
\item \emph{Whether the continuity clause of Assumption~\ref{asm:A6} holds for the declared
  construction of $\Theta$.} This was answered in substance on 2026-08-27 and the locus was
  corrected --- see Remark~\ref{rem:A6record} --- and what remains open is scoped: (a) whether a
  constructive $\Theta$, or the $t$-constrained Kakutani route already on file, which removes the
  continuity half of the hypothesis, replaces that hypothesis in the statement, the repair being
  identified rather than executed; (b) the complementary menu class, in which every middle plan's
  histories are shared with a survivor --- the implemented menu is one such for its collapse face
  --- where the collapse-face clause may be satisfiable; and (c) nonexistence, which is neither
  claimed nor shown anywhere.
\end{enumerate}
===== END sections_v3/theorem_section.tex =====

---

### 7.2 The model section — primitives, timing, equilibrium notion, assumption block

FILE: sections_v3/model_section.tex (verbatim, complete)

===== BEGIN sections_v3/model_section.tex =====
%==============================================================================
%  sections_v3/model_section.tex -- the model section of draft_v3.
%
%  SOURCE OF TRUTH: research/model_v4/MODEL_CARD.md, version stamp 2026-08-27
%  (A6 panel resolution, commit ae9caea).  Every statement below transcribes a
%  card row; where a proof file and the card differ, the card wins.  Card IDs
%  survive into the bracket titles so the card record, HANDOFF_sign.md and the
%  assembler can find each object by its ID.
%
%  Proofs live in sections_v3/proofs_section.tex; no proof environment appears
%  in this file.
%==============================================================================

\section{The two-round model}
\label{sec:model-v4}

\subsection{Object and partition}
\label{sec:object}

The disclosure rule \emph{is} the market's partition. A stake threshold $\tau$ and a filing window
$T$ split the histories that reach the control node into two cells: a \emph{flagged} cell, on which
the filing has landed before the control decision, and a \emph{pooled} cell, on which it has not.
Nothing else in the model performs that split, and the two cells are exclusive and exhaustive by
construction. The paper's question is how noise-trading intensity $\kappa$ moves bidder entry and
the expected takeover premium once the rule has drawn that line, and how the answer changes when the
line is redrawn.

The control-outcome object is the expected engagement-related premium
$\Dact(\kappa,\tau,T)$. Beside it sit three price-path objects, all of them produced by the model
rather than assumed: the run-up path $R_d$, the cumulative run-up $R$, and the filing-day jump $J$.
Lower $\tau$ is a tighter threshold margin; lower $T$ is a tighter window margin. The two margins are
separate policy coordinates and the results below treat them separately, because the model does not
deliver the same answer at both.

Three primitives are inherited rather than built here. Order flow is the discrete, ternary-noise
structure of the Kyle tradition \citep{Kyle1985}, in the tractable discrete form used by
\citet{EdmansGoldsteinJiang2015}; prices are competitive in the sense of
\citet{GlostenMilgrom1985}, set equal to the expectation of the terminal payoff given the public
history; and the takeover premium is the welfare object for dispersed minority shareholders for the
free-rider reason of \citet{GrossmanHart1980}. What is new is not any of these pieces but the
partition that sits between them, and the sections that follow state it exactly.

\subsection{Timing: the two rounds}
\label{sec:timing}

Trading runs over business days $d = 0,\dots,H$, with $H$ finite. The sequence is: pooled round
$\to$ flag or no flag $\to$ flagged round if applicable $\to$ bidder decision.

\begin{enumerate}[label=(\arabic*),leftmargin=2.2em,itemsep=3pt]
\item Nature draws the standalone value $v$ and the blockholder's private signal $s$. The
  blockholder picks one complete contingent plan $j$ from a finite ordered menu $\mathcal J$.
\item \emph{Round 1 --- pooled trading.} The plan's stake path executes over $d = 0,\dots,H$. Market
  makers see pooled order flow and set $P_d^P = \Eop[Y \mid \mathcal H_d^P]$.
\item \emph{Disclosure node.} The flag lands if and only if $D = 1$: the plan engages, crosses
  $\tau$ at some date $c < \infty$, and $c + T \le H$. The filing reveals $F = (B^F, a = 1)$.
\item \emph{Round 2 --- flagged trading, then the bidder.} If $D = 1$ the blockholder submits the
  flagged order $Q^F$, the market sets the flagged price $P^F = P(F,Q^F)$, and then the bidder
  decides. If $D = 0$ there is no flagged round and the bidder acts on the pooled history.
\end{enumerate}

Two features of this timing are load-bearing, and each is stated as a hypothesis rather than left in
the prose, because named proof steps fail without them.

\begin{assumption}[\S2 no-feedback: no within-window re-optimisation]
\label{asm:nofeedback}
The blockholder does not re-optimise inside the filing window. There is no feedback from realised
order flow or from realised prices into the executed path: $B_j(s,d)$, $q_{jd}(s)$ and $Q_j^F$ are
functions of $(j,s,d)$ and of $(j,s,\tau,T)$ alone.
\end{assumption}

\begin{assumption}[\S2 flag termination: the flag terminates the pooled round]
\label{asm:flagterm}
Pooled trading stops when the filing lands. The flagged round follows the filing, and the bidder
acts after the flagged round.
\end{assumption}

Assumption~\ref{asm:nofeedback} is what makes the executed path a function of the plan and the
signal, and Steps 3 and 6 of the conditional-independence argument behind Lemma~\ref{lem:L2} fail
without it. Assumption~\ref{asm:flagterm} is what makes $Q^F_j(s) = b^*_j(s) - B^F_j(s)$ the
blockholder's whole residual position; read the other way, the flagged-round step of
Proposition~\ref{prop:P1} fails.

\subsection{Primitives}
\label{sec:primitives}

\begin{definition}[\S4.1 primitives: values, signals, noise and the disclosure policy]
\label{def:primitives}
The standalone value is $v \sim N(\mu_v,\sigma_v^2)$ and the blockholder's private signal is
$s = v + \varepsilon$ with $\varepsilon \sim N(0,\sigma_\varepsilon^2)$ independent of $v$, so that
$\Eop[v \mid s] = \mu_v + \beta(s-\mu_v)$ with the Gaussian projection
$\beta = \sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2) \in (0,1)$. The bidder draws a private synergy
shock $\xi \sim N(0,\sigma_\xi^2)$, independent of $(v,s)$; $\bar S$ is mean bidder synergy and
$K > 0$ the bidder's entry cost. Takeover premia without and with engagement are $m_0$ and $m_1$,
with premium wedge $\Delta_m = m_1 - m_0 > 0$, and $\Delta_V \ge 0$ is the non-takeover value
created by engagement. Noise trading is ternary: $z_d \in \{-\bar z, 0, +\bar z\}$ with $\bar z > 0$,
$\Prb(z_d = 0) = 1-\kappa$ and $\Prb(z_d = \pm\bar z) = \kappa/2$, where $\kappa \in [0,1]$ is
noise-trading intensity. The disclosure rule is the pair $(\tau,T)$ with $T \in \{1,\dots,H\}$; the
blockholder's initial and maximum stakes are $b_0$ and $\bar b$ with $0 \le b_0 \le \bar b$.
\end{definition}

\begin{definition}[\S4.2 plans and the legal clock]
\label{def:plans}
The plan menu $\mathcal J$ is finite and ordered from least to most aggressive, with
$|\mathcal J| = J < \infty$. Plan $j$ carries an engagement flag $a_j \in \{0,1\}$, equal to $1$ for
Voice and $0$ for Exit and Hold. Its cumulative pooled stake at day $d$ is $B_j(s,d) \in [0,\bar b]$
with $B_j(s,-1) = b_0$; the terminal target is $b_j^*(s) = B_j(s,H)$. The threshold-crossing date is
$c_j(s;\tau) = \inf\{d : B_j(s,d) \ge \tau\}$, equal to $+\infty$ if the path never reaches $\tau$,
and the legal filing date is $f_j = c_j + T$. The disclosure indicator is
$D_j(s;\tau,T) = \ind\{a_j = 1,\ c_j < \infty,\ f_j \le H\}$, so that $D = 1 \Rightarrow a = 1$. The
stake at filing is $B_j^F = B_j(s,f_j)$ and the flagged-round order is
$Q_j^F = b_j^*(s) - B_j^F$. A finite ordered coarsening $\Gamma$ maps the stake increment to the
pooled order mark, $q_{jd}(s) = \Gamma\bigl(B_j(s,d) - B_j(s,d-1)\bigr)$, and observed pooled order
flow is $X_d = q_{jd} + z_d$.
\end{definition}

\begin{definition}[\S4.3 information, prices and the control outcome]
\label{def:prices}
The pooled public history is $\mathcal H_d^P = (X_0,\dots,X_d;\ \text{flag landed by } d)$, which is
finite. The filing message is $F = (B^F, a{=}1)$, and the flagged tuple is $F$ augmented by the
flagged order, $\Sfl = (B^F,Q^F,a{=}1)$. The control-node information set is the \emph{public}
information at the control node: $\mathcal I_H = \mathcal H_H^P$ on the pooled cell $\{D=0\}$ and
$\mathcal I_H = \Sfl$ on the flagged cell $\{D=1\}$. The bidder's own $\xi$ is private. Write
$\mathcal C_F$ and $\mathcal C_P$ for the flagged and pooled cells; they are exclusive and
exhaustive by construction. The engagement posterior is $\pi(\mathcal I) = \Prb(a=1\mid\mathcal I)
\in [0,1]$, equal to $1$ on $\mathcal C_F$, and the bidder-entry probability is
\begin{equation}
\label{eq:entry}
p(\mathcal I) \;=\; 1 - \Phi\!\left(\frac{P + K + m_0 + \pi\Delta_m - \bar S}{\sigma_\xi}\right)
\;\in\;(0,1).
\end{equation}
With $\mathsf B$ the entry indicator, the terminal shareholder payoff is
\begin{equation}
\label{eq:Y}
Y \;=\; (1-\mathsf B)\,(v + a\Delta_V) \;+\; \mathsf B\,(P + m_0 + a\Delta_m),
\end{equation}
and prices satisfy the inner fixed point $P(\mathcal I) = \Eop[Y\mid\mathcal I]$. Two conventions are
part of the model rather than notation. First, $P_{-1}^P := \Eop[Y]$ is the pre-trading pooled
price, which is needed whenever $c = 0$ --- as $T = H$ forces on every flagged history. Second,
$P_{\ND}(\mathcal H_{f^-}^P) := P_{f^-}^P$: the not-yet-disclosed price is the last pre-filing pooled
price at the \emph{same} realised order flow, whose history already carries ``flag not landed by
$f-1$'', and not a never-disclosed counterfactual. The price-path objects are the run-up path
$R_d = P_d^P - P_{c^-}^P$, the cumulative run-up $R = P_{f^-}^P - P_{c^-}^P$, and the filing-day
jump $J = P^F - P_{\ND}$; $R_d$, $R$ and $J$ are unsigned, and $J$ is not claimed to be
$\kappa$-invariant.
\end{definition}

The genuine fixed point sits at the control nodes. At an earlier pooled date $d < H$ the price is a
tower expectation of already-solved control-node values, with no self-reference; only the
control-node map is a fixed point to be solved.

\begin{definition}[\S4.3 objective: the blockholder's payoff $U_j$]
\label{def:U}
The blockholder's objective is the expected terminal value of the position the plan builds, net of
what it costs to build and to engage:
\begin{equation}
\label{eq:Uj}
U_j(s) \;=\; \Eop\Bigl[\, b_j^*(s)\,Y \;-\; \mathcal C_j^{\mathrm{trade}} \;-\; a_j\,C_j(s)
\;\Bigm\vert\; s,\, j \,\Bigr],
\end{equation}
where $\mathcal C_j^{\mathrm{trade}}$ is the execution outlay --- increments valued at the pooled
prices $P_d^P$ up to the plan's last pooled date, plus $Q_j^F(s)\,P^F$ when $D_j = 1$ --- and
$C_j(s) \ge 0$ is the engagement cost. Only two properties of \eqref{eq:Uj} are ever used:
\emph{plan-locality}, that $U_j$ depends on $j$ only through the executed stake path, the prices paid
on it, the terminal stake, the engagement flag and the cost; and \emph{integrability},
$\Eop[\max_{j}|U_j|] < \infty$ under Assumption~\ref{asm:A2p}.
\end{definition}

\begin{remark}[Timing convention for the engagement cost]
\label{rem:Ctiming}
Display \eqref{eq:Uj} does not date $C_j(s)$. The engagement cost may be booked either on completing
the plan or as sunk once the filing has landed. The two readings give the same round-2 comparison on
the round-2 deviation set, so the existence result of Proposition~\ref{prop:P1} does not depend on
the choice; the statement there is written so as not to commit to a reading.
\end{remark}

\begin{assumption}[TR: the \S4.1--\S4.3 primitive table restrictions]
\label{asm:TR}
The primitives of Definitions~\ref{def:primitives}--\ref{def:U} satisfy the following, which several
results below consume as a block.
\begin{enumerate}[label=(TR-\roman*),leftmargin=3.2em,itemsep=3pt]
\item \emph{Distributional forms and signs.} The distributions of Definition~\ref{def:primitives}
  hold as stated, with $\sigma_v^2,\sigma_\varepsilon^2,\sigma_\xi^2 > 0$, $K > 0$, $\bar z > 0$,
  $\Delta_m > 0$, $\Delta_V \ge 0$, and
  \begin{equation}
  \label{eq:m0}
  m_0 \;\ge\; 0,
  \end{equation}
  so that $\bar m(\mathcal I) = m_0 + \pi(\mathcal I)\Delta_m \ge 0$. Restriction \eqref{eq:m0} is
  what makes the inner pricing fixed point exist, be unique and be continuous; dropping it produces
  both nonexistence and three-root multiplicity in executed counterexamples. The initial stake
  satisfies $b_0 < \tau$: a pre-existing crossing is outside the core model.
\item \emph{Stake-path regularity.} For Voice plans $\partial_d B_j \ge 0$ and
  $\partial_s B_j \ge 0$; Hold paths are constant and Exit paths weakly decreasing in $d$. For every
  plan and every $d$, the map $s \mapsto B_j(s,d)$ is Borel. Borel regularity is automatic for Voice
  (monotone in $s$) and for Hold (constant) and is a genuine addition for Exit, where the primitives
  supply monotonicity in $d$ only; without it the pooled prices are not defined, because pooled
  pricing integrates over every type including Exit types. Stake levels are continuum-valued: the
  finiteness of Assumption~\ref{asm:A2p} covers the plan menu, the image of $\Gamma$, the noise
  support and the calendar, not the stake level.
\item \emph{Legal-clock objects.} The definitions of $c_j$, $f_j$, $B_j^F$, $Q_j^F$ and $b_j^*$ in
  Definition~\ref{def:plans} hold as stated, together with $D = 1 \Rightarrow a = 1$; $Q^F \ge 0$ for
  Voice plans; and, at fixed policies, $T' < T$ implies $B^F(T') \le B^F(T)$ and
  $Q^F(T') \ge Q^F(T)$.
\item \emph{Pricing and entry.} The terminal payoff is \eqref{eq:Y}, prices obey the convention
  $P(\mathcal I) = \Eop[Y\mid\mathcal I]$, entry obeys \eqref{eq:entry}, the control-node information
  set is the fill given in Definition~\ref{def:prices}, and the two price conventions
  $P_{-1}^P = \Eop[Y]$ and $P_{\ND} = P_{f^-}^P$ hold.
\end{enumerate}
\end{assumption}

\subsection{Equilibrium notion}
\label{sec:equilibrium-notion}

\begin{definition}[\S3: cutoff perfect Bayesian equilibrium]
\label{def:cpbe}
A \emph{cutoff perfect Bayesian equilibrium} is:
\begin{enumerate}[label=(\roman*),leftmargin=2.4em,itemsep=3pt]
\item a weakly ordered cutoff vector $k = (k_1 \le \dots \le k_{J-1})$ mapping the signal $s$ into a
  plan;
\item sequentially optimal pooled and flagged components;
\item Bayes-consistent beliefs on path;
\item competitive pooled and flagged prices at their fixed points;
\item the bidder-entry rule \eqref{eq:entry};
\item off-path beliefs as limits of full-support perturbations.
\end{enumerate}
The inequalities in (i) are weak, so collapsed action regions --- including a collapsed Hold region
--- are permitted. Existence is a Brouwer argument on the compact ordered polytope $\Theta$ for the
outer map $\Tmap(k;\vartheta)$ of Section~\ref{sec:polytope}, at a fixed point
$k = \Tmap(k;\vartheta)$. Uniqueness is \emph{not} claimed.
\end{definition}

\subsection{Standing hypotheses}
\label{sec:hypotheses}

The hypotheses below are the model's standing assumptions. They are not all maintained at once by
every result: each result in Section~\ref{sec:results} names the subset it consumes, and three of
them carry dated numerical records showing that they fail at the calibration the accompanying
implementation runs. Those records are stated with the assumptions they bear on, not deferred.

\begin{assumption}[A1: independent primitives]
\label{asm:A1}
$v$, $\varepsilon$, $\xi$ and all $z_d$ are mutually independent, and all variances are strictly
positive.
\end{assumption}

\begin{assumption}[A2$'$: finite model, amended boundedness]
\label{asm:A2p}
The plan menu $\mathcal J$, the image of $\Gamma$ (the order-mark support), the noise support
$\{-\bar z,0,+\bar z\}$ and the calendar horizon $H$ are finite. Prices and payoffs are locally
bounded in $(s,\vartheta)$ on the maintained parameter set, and
$\Eop\bigl[\max_{j\in\mathcal J}|U_j|\bigr] < \infty$ for every $k \in \Theta$.
\end{assumption}

The boundedness clause is stated as integrability because flat global boundedness is inconsistent
with the rest of the model: $v$ is Gaussian and the flagged region is unbounded in $s$ under
Assumption~\ref{asm:A7p}, so $Y$ --- and with it prices and $U_j$ --- is unbounded. Integrability is
all any proof below consumes.

\begin{assumption}[A3: ordered plans, single crossing]
\label{asm:A3}
At every belief and price system, adjacent-plan payoff differences cross zero at most once in $s$,
and the preferred plan is weakly increasing in $s$.
\end{assumption}

\begin{remark}[Numerical record for Assumption~\ref{asm:A3}]
\label{rem:A3record}
At the implemented calibration Assumption~\ref{asm:A3} itself fails, at two independently found
loci, upstream of Assumption~\ref{asm:A6}. First, at $(\kappa = 0.5,\ \tau_{50},\ T = 5)$ with $k_2$
on an \emph{open set} above cell edge $6$ --- verified at offsets $10^{-9}$ through
$2\times10^{-2}$ --- the difference $U_V - U_H$ has three strict sign changes, at
$s = 1.5754434$, $1.5833333$ and $1.5902426$, with middle excursions of
$2.4$--$2.8\times10^{-4}$ against a $10^{-9}$ payoff tolerance. The pointwise argmax runs
$H,V,H,V$, single-valued on each interval, so no weakly increasing selection exists: the selection
set is empty and the outer map $\Tmap$ is \emph{undefined} there, not merely discontinuous. Second,
at $(\kappa = 0.15,\ 0.05,\ 5)$ --- one of the four unresolved nodes of
Remark~\ref{rem:P1record} --- the argmax reverses from Voice to Hold across cell edge
$s = 1.659062163$ at both located fixed points, so the preferred plan decreases in $s$. The route is
the $s$-direction step of the Voice payoff, whose interior count $n(s)$ is integer-valued,
interacting with the off-path price snap. This does not conflict with the recorded finding that the
A3 and A6 proxies pass at every achieving seed: those proxies are local screens --- the A3 proxy
tests residual slope signs at the two candidate cutoffs and the A6 proxy tests non-pinning at the
closest seed --- and neither measures argmax monotonicity over $s$ nor continuity of $\Tmap$ in $k$,
so both are silent on these findings. A candidate mechanical account of the four unresolved nodes is
on file and UNCHECKED beyond the one node probed: at the $\kappa = 0.15$ node one fixed
point sits exactly on the edge where $U_H - U_V$ jumps through zero without crossing it, and the
panel's residuals, $3.06\times10^{-4}$ to $1.77\times10^{-3}$ at cutoff residuals of
$10^{-11}$ grade, bracket the recorded range exactly; the $k$-direction jump mechanism does
\emph{not} explain those nodes, and the panellist who proposed it recorded that negative himself.
No label moves on any of this: A3 is a hypothesis, and Proposition~\ref{prop:P1} stays
PROVED as a conditional. Records: the panel files named in Remark~\ref{rem:A6record}.
\end{remark}

\begin{assumption}[A4: legal-clock discipline]
\label{asm:A4}
The crossing date $c$ is the first date the path reaches $\tau$; the filing lands exactly at $c+T$;
filings truthfully reveal stake and purpose; and only Voice plans cross in the core model.
\end{assumption}

\begin{assumption}[A5: inner pricing regularity, mostly demoted to a theorem]
\label{asm:A5}
Each public-history pricing map has a unique fixed point, continuous in beliefs, cutoffs and
parameters.
\end{assumption}

Assumption~\ref{asm:A5} is stated here for reference, and most of it is a theorem rather than an
assumption. Under \eqref{eq:m0}, existence, uniqueness and continuity of the \emph{inner} fixed point
are proved, not assumed. With the belief summaries $\bar y(\mathcal I) = \Eop_\mu[v] + \pi\Delta_V$
and $\bar m(\mathcal I) = m_0 + \pi\Delta_m$, the pricing map reduces to the scalar equation
$P \mapsto \bar y + \bar m\,p(P)/(1-p(P))$, which is strictly decreasing in $P$ wherever
$\bar m \ge 0$ and therefore crosses the identity exactly once. Three independent confirmations are
on file, one of them an executed counterexample producing zero roots and another producing three
once $m_0 < 0$. What Assumption~\ref{asm:A5} is retained for is its \emph{continuity} clause: the
pricing family is continuous in the cutoff vector and the parameters, and measurable in the flagged
tuple. Because the flagged information sets are continuum-indexed, ``unique fixed point'' must be
read as a measurably selected family, not a finite list. Where a result below cites
Assumption~\ref{asm:A5} for existence or uniqueness, it may cite \eqref{eq:m0} instead.

\begin{assumption}[A6: compact outer self-map]
\label{asm:A6}
All best-response cutoffs lie in a common compact ordered polytope $\Theta$; the outer map $\Tmap$
of Section~\ref{sec:polytope} is continuous and maps $\Theta$ into itself.
\end{assumption}

\begin{remark}[Numerical record for Assumption~\ref{asm:A6}]
\label{rem:A6record}
The continuity clause of Assumption~\ref{asm:A6} fails for the declared construction of $\Theta$,
and the locus is not the one first proposed. All $k$-dependence of $U_j$ runs through the pooled
price vector, the flagged layer being $k$-free under Assumption~\ref{asm:A7J}; Bayes applies where
the reaching weight is positive but a $k$-free, plan-uniform posterior is imposed on the frontier,
so the price system can be discontinuous exactly on the boundary of the reaching set of each pooled
history. That set lies inside the union of the finitely many \emph{cell-edge hyperplanes}
$\{k_i = a\}$ and the \emph{collapse faces whose dying plan is the sole generator} of some reachable
pooled history --- not the collapsed cutoff vectors as such. The jump reaches $\Tmap$ with
non-vanishing weight, because $U_j$ integrates those prices against the deviator's own noise law,
with weight at least $\min(\kappa/2,\,1-\kappa)^{d+1}$, independent of the dying plan's population
mass; the vanishing-mass defusal is therefore refuted, by both panellists independently. The
largest-weakly-increasing-selection tie-break is pointwise in $k$ and passes the jump through, and no
$k$-independent perturbation family reconciles the limits: at fixed perturbation size the system is
continuous in $k$, and the discontinuity is created only in the limit, which the choice of family
cannot fix. On collapse faces proper, for menus with $J \ge 3$ in which a middle plan owns a
reachable exclusive pooled history entering some $U_j$, the interior limit
$\mu_v + \beta(c - \mu_v)$ varies over the face while any $k$-free family supplies one constant, so
continuity fails at every face point but at most one --- a continuum-face lemma derived in a single
panel pass and \emph{not} gate-checked. The implemented menu is not in that class: Exit and Hold pool
perfectly in order flow, and its Hold-collapse face is measured clean, with pooled prices within
$4.4\times10^{-16}$ and $\Tmap$ bit-identical as $k_1$ sweeps to full collapse. At the implemented
calibration the failure is live at the interior $n(s)$ cell edges instead: measured $\Tmap_2$ jumps
of $6.33\times10^{-3}$, $1.09\times10^{-2}$ and $2.83\times10^{-2}$ across steps in $k_2$ of at most
$2\times10^{-9}$ at $(\kappa = 0.5,\ \tau_{50},\ T = 5)$, measured independently by both panellists
with separate scripts and agreeing to three significant figures, with the belief snap matching the
predicted value to about $10^{-8}$, surviving-type controls at about $3\times10^{-9}$, and
robustness at $1000$ times the breakpoint-merge tolerance; at $(\kappa = 0.15,\ 0.05,\ 5)$ the jumps
reach $0.16$ and a diagonal crossing of $\Tmap_2$ is destroyed. A chamber interior
$\Theta^+ = [1.23,\,1.245]\times[1.5253,\,1.5506]$ has been exhibited that is compact,
self-mapping and jump-free at the baseline node --- Brouwer runs on it verbatim and it contains
$k^\star$ --- but it is not the $\Theta$ the existence argument constructs, it cannot be exhibited
without approximately locating the fixed point first, and no such chamber exists at the
$\kappa = 0.15$ node, where a fixed point sits exactly on the edge $k_2 = 1.659062163$. No label
moves and none is licensed: A6 is a hypothesis, and Proposition~\ref{prop:P1} stays PROVED
as a conditional, in the same pattern as $\Atau$ --- what is on record is that its antecedent, read
with the $\Theta$ the proof constructs, is not satisfied by the implemented calibration. Two repairs
are on file, both outside the declared Brouwer-with-one-fixed-family route: a $t$-constrained game
with a Kakutani argument and $t \downarrow 0$, and a $k$-indexed concentration family, constructible
but with its $0/0$ corner unresolved. The implementation's off-path floor of $10^{-14}$ \emph{is} the
fixed-$t$ constrained game --- the standard repair already shipped, with the switch relocated by
about $10^{-9}$ rather than removed. Coverage: probes at one node per claim class plus a 27-node
census, not swept over $(\kappa,\tau,T)$. Nonexistence is neither claimed nor shown: $23$ of $27$
sweep nodes converge, and a discontinuous self-map may still have fixed points. Records:
\texttt{threads/\allowbreak 2026-08-27\_A6\_\allowbreak panel\_substantiate.md} and
\texttt{threads/\allowbreak 2026-08-27\_A6\_\allowbreak panel\_defuse.md}; probes
\texttt{quality\_reports/\allowbreak fixes/\allowbreak a6\_panel\_probes\_\allowbreak 2026-08-27/},
which are analysis-grade and not curated executed checks.
\end{remark}

\begin{assumption}[A7: filing sufficiency]
\label{asm:A7}
On flagged histories, $(B^F,Q^F,a{=}1)$ identifies the informed component of the selected plan;
conditional on it, the pooled order-flow residual is pure noise, independent of $(v,s,\xi)$.
\end{assumption}

This weak identification wording is not enough for Lemma~\ref{lem:L2}: it permits two pairs $(j,s)$
with different pooled paths, which is exactly that lemma's first failure case. Two injective forms
are therefore named separately, and the form is named every time either is used.

\begin{assumption}[A7$'$: on-path composed target]
\label{asm:A7p}
At a fixed cutoff policy, the composed terminal target $s \mapsto b^*_{j(s)}(s)$ is strictly
increasing on the flagged signal region, and this holds for every cutoff vector $k \in \Theta$.
Strictness is required only for flag-capable composed targets: passive plans that never flag need not
have strictly increasing $b_j^*$, and there is no backtracking of $b_j^*$ across admissible
Voice-plan switches.
\end{assumption}

\begin{assumption}[A7-J: joint tuple injectivity]
\label{asm:A7J}
The full map $(j,s) \mapsto (B_j^F,\,Q_j^F,\,a_j)$ is injective on the flagged-pair set
$\{(j,s) : D_j = 1\}$, including flagged pairs that are not selected on path.
\end{assumption}

Assumption~\ref{asm:A7J} is strictly stronger than Assumption~\ref{asm:A7p}, and it is the form the
existence argument consumes. Strictness of $B^F$ alone is neither necessary --- it fails at
crossing-date jumps on the pro-rata menu --- nor sufficient, because of multi-Voice backtracking.
Under Assumption~\ref{asm:A7p} the flagged tuple is continuum-valued as a tuple, since injectivity
forces $(B^F,Q^F)$ to be continuum-valued, though the coordinates may trade the burden between them;
injectivity plus measurability already gives the measurable inverse on standard Borel spaces, so no
separate assumption is needed for that. Satisfiability is resolved for Assumption~\ref{asm:A7p}:
together with a fixed cutoff policy and $\Omega > 0$ it delivers the on-path injective form on
positive-probability flagged tuples with an explicit inverse, and a satisfying menu exists --- the
pro-rata single-Voice menu with terminal target strictly increasing on all of $\mathbb R$, which also
satisfies Assumption~\ref{asm:A7J}. Assumption~\ref{asm:A7J} additionally needs $b^*$ strictly
increasing off the Voice region: a target flat below the Voice cutoff breaks it, in an executed
check producing forty collisions, while leaving Assumption~\ref{asm:A7p} intact. The failure boundary
for the on-path form is a binding stake cap, quantized stakes, a composed target repeating values
across Voice-plan switches, $\Omega = 0$, and policy dependence when the condition is stated only at
one equilibrium's cutoffs. Menus satisfying Assumption~\ref{asm:A7p} are fully separating on the
flagged set, so the burden moves to the incentive compatibility of Proposition~\ref{prop:P1}, not
away.

\begin{assumption}[A8: interior crossing]
\label{asm:A8}
$0 < \Omega(\kappa,\tau,T) < 1$. This is required only for positive cell mass, never for the
structural partition.
\end{assumption}

\begin{assumption}[$\Atau$: threshold chord restriction]
\label{asm:Atau}
The pooled posterior law has the symmetric ternary representation
\begin{equation}
\label{eq:atau}
\Eop[h] \;=\; A_0(\kappa)\,h(0) \;+\; A_{1/2}(\kappa)\,h(\bar\pi/2) \;+\; A_1(\kappa)\,h(\bar\pi),
\end{equation}
with $A_0' = A_1' = \Akap$ and $A_{1/2}' = -2\Akap$, and maintained orientation
$C_h(\bar\pi) \le 0$ with $|C_h|$ weakly increasing in $\bar\pi$. The strict version of the
orientation is the frozen manuscript's condition (C\textasteriskcentered); the case $C_h = 0$ must be
handled explicitly. Two further clauses are part of the restriction:
\begin{enumerate}[label=($\tau$-\roman*),leftmargin=3.2em,itemsep=3pt]
\item \emph{The kernel depends on the information set only through the engagement posterior:}
  $h(\mathcal I) = h(\pi(\mathcal I))$, so the three numbers $h(0)$, $h(\bar\pi/2)$, $h(\bar\pi)$ are
  well defined and $\kappa$-free. This is a restriction, not a reading. In the model
  $h = \pi\,p(\hat v,\pi)$ is a function of \emph{two} scalars, because \eqref{eq:entry} makes entry
  depend on the price as well as on the posterior; the clause says the standalone-value channel and
  the engagement channel do not co-move inside the pooled cell in a way that moves $h$ at a fixed
  posterior.
\item \emph{The support and $\bar\pi$ are $\kappa$-free; only the weights move.} The three points
  $\{0,\bar\pi/2,\bar\pi\}$ do not vary with $\kappa$, and $\bar\pi$ itself is $\kappa$-free at fixed
  $(\tau,T)$. Without the second half the conclusion of Lemma~\ref{lem:L3} is false: the derivative
  gains a term that is first order in $\bar\pi$ and the vanishing fails.
\end{enumerate}
\end{assumption}

Where the bite of Assumption~\ref{asm:Atau} actually sits is worth stating, because it is narrower
than the display suggests. Given a $\kappa$-invariant three-point support, the derivative
restrictions $A_0' = A_1' = \Akap$ and $A_{1/2}' = -2\Akap$ are not an extra assumption at all: they
are \emph{equivalent} to $\kappa$-invariance of the pooled block's total mass and of its
unnormalised engagement moment, both of which the model delivers at fixed policies. The entire
remaining content of Assumption~\ref{asm:Atau} is the support condition. A one-round ternary-noise
market with informed mark $2\bar z$ and pre-order engagement share $\tfrac12$ satisfies it; the
frozen manuscript's own no-disclosure structure, with informed mark $\bar z$, does not, since its
pooled law has four atoms, two of which move with $\kappa$. Whether the two-round pooled cell of
Section~\ref{sec:timing} satisfies the support condition is \textbf{open}, and every result
conditional on Assumption~\ref{asm:Atau} --- Lemma~\ref{lem:L3}, leg 3 of Lemma~\ref{lem:L4}, and
Part~(B) of Theorem~\ref{thm:T1} --- inherits that conditionality.

\begin{remark}[Numerical record for Assumption~\ref{asm:Atau}]
\label{rem:AtauRecord}
At the implemented calibration the support condition \textbf{fails}, and it fails on the support, not
on the derivative pattern. The pooled cell's engagement-posterior law was enumerated exactly --- all
$4^{H+1} = 4{,}194{,}304$ order-flow paths, the same law the implementation integrates --- at $200$
nodes: $\kappa \in \{0.05,\dots,0.95\}$ crossed with the five frozen $\tau$ percentiles and
$T \in \{1,2,5,10\}$, at frozen policies with $H = 10$. Two gates pass first, so the object measured
is the one Assumption~\ref{asm:Atau} is about: an independent re-enumeration reproduces the pooled
mass to $0.0$ exactly, and the enumerated mean equals the pooled share
$\bar\pi_{\mathrm{pr}} = \Prb(a=1\mid D=0)$ to $1.7\times10^{-16}$. Neither a particular value of
$|\Akap|$ nor level symmetry is imposed anywhere, and $\bar\pi$ is read as the upper support point
throughout. Twenty nodes are degenerate --- $\bar\pi_{\mathrm{pr}} = 0$ at $T \in \{1,2\}$ with
$\tau$ at the tenth percentile, where no engaging atom survives into the pooled cell, the law is the
point mass at $0$, $M_P = 0$ and $C_h(0) = 0$, so the restriction holds vacuously and the node
decides nothing. At all $180$ non-degenerate nodes $\Atau$ fails; at none does it hold.
\begin{itemize}[leftmargin=1.6em,itemsep=3pt]
\item \emph{Clause ($\tau$-ii), support half --- fails, by some eleven orders of magnitude.} The
  support carries $23$ to $767$ distinct posterior values, never three ($0$ of $180$ nodes), and
  there is no mass at $\bar\pi/2$ at any node, so $A_{1/2} \equiv 0$. Between $0.57\%$ and $91.8\%$
  of the pooled mass sits off $\{0,\bar\pi/2,\bar\pi\}$, and $13.9\%$ at the median node
  ($T = 5$, median $\tau$, $\kappa = 0.55$: $107$ atoms, $A_0 = 0.768$, $A_1 = 0.093$). The atoms are
  not dust: coarsening the cluster tolerance to $10^{-3}$ still leaves $6$ to $332$ of them, and the
  floor-free law counts at most $51$ atoms fewer than the floored law the package prices. The
  interior atoms move with $\kappa$: the two-sided Hausdorff distance between adjacent-$\kappa$
  support sets reaches $0.4608$, unchanged when restricted to atoms carrying mass at least
  $10^{-6}$, against a predicted $<10^{-12}$, at $0$ of $18$ series.
\item \emph{Clause ($\tau$-ii), $\bar\pi$ half --- holds.} $\bar\pi = 1$ to $1.5\times10^{-13}$ at
  every non-degenerate node, and $\kappa$-free to the same order, at $18$ of $18$ series. This is a
  separate finding and not a partial rescue: $\bar\pi = 1$ is the one-round outcome, and the
  conjecture that the two-round timing leaves the pooled cell with a top atom strictly below $1$ is
  false at this calibration, because unflagged Voice types still generate fully revealing order
  flows. Across the whole grid $\bar\pi \in \{0,1\}$ and never interior, so the small-$\bar\pi$
  corollary of Lemma~\ref{lem:L3} has no instance here either.
\item \emph{Derivative pattern --- fails, and independently of the support.} $A_0' = A_1'$ holds at
  $0$ of $180$ nodes: $|A_0' - A_1'| \in [0.041,\,2.306]$ against a predicted $<10^{-10}$, with
  $A_0' \in [-2.146,\,2.374]$ against $A_1' \in [-0.014,\,0.429]$, an order of magnitude apart in
  level, and both change sign over the grid, which independently corroborates that $\Akap$ carries
  no sign. The restriction $A_{1/2}' = -2\Akap$ also fails at all $180$, but with
  $A_{1/2} \equiv 0$ that residual is exactly $2|A_0'|$ and is recorded as inherited --- a
  restatement of the support failure, not a second piece of evidence.
\item \emph{Chord identity --- fails.} The residual
  $\bigl|\mathcal S_P - \Delta_m\,|\Akap|\,|C_h(\bar\pi)|\bigr|$, with $\Akap$ recovered from the
  enumerated weights and $\bar\pi$ the actual upper support point, is $0.0013$ to $0.0717$ --- up to
  $7.17$ premium percentage points --- against a predicted $<10^{-10}$, at $0$ of $180$ nodes and on
  the most favourable of three kernel conventions. Recovered $|\Akap| \in [0.042,\,2.374]$; the value
  the identity would require is $[0.00023,\,0.392]$, disjoint from the separately implied
  $[0.997,\,1.158]$, which is a different object (a mean absolute slope over the $\kappa$ grid, under
  level symmetry) --- and the distance between the two measures what the level-symmetry assumption
  was doing.
\item \emph{Clause ($\tau$-i), reported as a diagnostic and not part of the verdict.} Within a
  cluster on which the posterior is constant to $10^{-12}$, the enumerated entry probability still
  spreads by up to $0.085$ and $h$ by up to $0.018$ mass-weighted. The kernel does not reach the
  information set only through the posterior at this calibration either.
\end{itemize}
This is NUMERICAL-class \emph{applicability} evidence at one calibration. No label moves,
and none is licensed: $\Atau$ is an assumption, not a labelled claim. Lemma~\ref{lem:L3}, leg 3 of
Lemma~\ref{lem:L4} and Part~(B) of Theorem~\ref{thm:T1} stay PROVED as conditionals with
their proofs untouched; what is now on record is that their antecedent is not satisfied by the
implemented pooled cell at this calibration, so at this calibration those legs say nothing about the
implemented cell. The open question above is a question about the assumption's \emph{domain}: a
different menu, a different $H$ or a different calibration could still satisfy the support condition.
Coverage caveats carried forward: the $18$ non-degenerate series are only \emph{six distinct pooled
cells}, because $T = 1$ and $T = 2$ induce identical partitions at every $\tau$, $T = 5$ joins them
at the three highest $\tau$ percentiles and repeats itself at the two lowest, and all five $T = 10$
quantiles coincide --- and all six fail; and the fifty $T = 10$ nodes sit at $\Omega = 0.000681$,
below the implementation's minimum cell mass. Script and record:
\texttt{quality\_reports/fixes/t2\_atau\_support\_check.py} $\to$
\texttt{t2\_atau\_support\_check.json} ($200$ nodes, $920$ pooled enumerations, $1002$ seconds;
top-level verdict field \texttt{FAILS at calibration}).
\end{remark}

\begin{assumption}[$\Abr$: chord--sensitivity bridge]
\label{asm:Abr}
For two compared thresholds $\tau' < \tau$ at fixed policies and a common $\kappa$:
\begin{enumerate}[label=(br-\roman*),leftmargin=3.2em,itemsep=3pt]
\item \emph{Representation at both policies.} The symmetric ternary representation \eqref{eq:atau}
  holds for the pooled class under $\tau$ \emph{and} under $\tau'$, with chord endpoints
  $\bar\pi(\tau)$ and $\bar\pi(\tau')$ and weight-derivative coefficients $\Akap(\tau)$ and
  $\Akap(\tau')$.
\item \emph{$\kappa$-localisation.} At fixed policies all $\kappa$-dependence of $M_P$ sits in the
  weights of \eqref{eq:atau}: the three support points $\{0,\bar\pi/2,\bar\pi\}$ and the kernel $h$
  \emph{as a function of the posterior} do not move with $\kappa$. Hence
  $\partial_\kappa M_P = \Delta_m \Akap C_h(\bar\pi)$ exactly, with no
  composition-through-$\kappa$ remainder. Against the literal display \eqref{eq:atau} this would
  restate (br-i); it is written against the honest reading $h = \pi\,p(\hat v,\pi)$, and it repairs
  that ambiguity rather than adding a fourth independent restriction, naming the same object as
  clause ($\tau$-i). The trailing ``hence'' is derivable, not assumed.
\item \emph{Coefficient stability across the threshold margin.}
  $|\Akap(\tau')| \le |\Akap(\tau)|$. The weakest sufficient form is equality: reclassification
  changes \emph{which} histories are pooled, not the $\kappa$-responsiveness of the pooled weights.
\item \emph{Endpoint linkage.} $\bar\pi$ is the chord endpoint of \eqref{eq:atau} --- the upper
  support point of the pooled posterior law --- and it is a weakly increasing function of the pooled
  prior engagement share $\bar\pi_{\mathrm{pr}} = \Prb(a=1 \mid D=0)$, \emph{the same function at
  $\tau$ and at $\tau'$}. The identity branch $\bar\pi = \bar\pi_{\mathrm{pr}}$ is excluded as
  degenerate.
\item \emph{Comparability of the chord functional across thresholds.} The chord functional
  $C_h(\cdot)$ --- and the kernel $h$ it is built from --- are the same functions of the posterior at
  both compared thresholds. Without it, leg 3 of Lemma~\ref{lem:L4} compares $|C_h|$ across two
  different functionals and the comparison is meaningless: $h = \pi p$ with $p$ priced off a cell
  whose composition the threshold moves, so $\tau$-invariance of $h$ is real content, not
  bookkeeping.
\end{enumerate}
\end{assumption}

Assumption~\ref{asm:Abr} is consumed by leg 3 of Lemma~\ref{lem:L4} and by Part~(B) of
Theorem~\ref{thm:T1}, and by nothing else. Clause (br-v) was independently required by three agents,
one of whom confirmed that it is not implied by (br-i)--(br-iv). One sharpening is recorded rather
than assumed: with $\rho := \tfrac12 A_{1/2} + A_1$, which is provably $\kappa$-free,
$\bar\pi = \bar\pi_{\mathrm{pr}}/\rho$, so (br-iv) is equivalent to
$\rho(\tau')/\rho(\tau) \ge \bar\pi_{\mathrm{pr}}(\tau')/\bar\pi_{\mathrm{pr}}(\tau)$; under the
level-symmetric reading $\rho = \tfrac12$ and $\bar\pi = 2\bar\pi_{\mathrm{pr}}$, which forces
$\bar\pi_{\mathrm{pr}} \le 1/2$, an inherited restriction on the domain of
Assumption~\ref{asm:Atau} that Lemma~\ref{lem:L4} does not resolve. Clause (br-iii) is the clause
with the least justification behind it, and it is the one to attack first. Because (br-i) carries the
representation \eqref{eq:atau} at both thresholds, the record in Remark~\ref{rem:AtauRecord} bears
directly on Assumption~\ref{asm:Abr} as well.

\begin{assumption}[AGE: general-equilibrium differentiability and contraction]
\label{asm:AGE}
On a candidate region $\mathcal R$ the outer map is twice continuously differentiable,
$L_{\mathcal R} < 1$, and the sign of the equilibrium liquidity derivative is constant on
$\mathcal R$.
\end{assumption}

\subsection{The cutoff polytope and the outer map}
\label{sec:polytope}

\begin{definition}[\S4.5 equilibrium objects: $\Theta$, $\Tmap$, and the general-equilibrium bounds]
\label{def:theta}
The cutoff vector is $k = (k_1,\dots,k_{J-1})$ with $k_1 \le \dots \le k_{J-1}$; when the menu is the
four named actions of the frozen manuscript it maps to that draft's triple of cutoffs. The cutoff
polytope $\Theta$ is nonempty, compact and convex, and $\vartheta$ is the parameter vector. The
\emph{outer cutoff best-response map} is $\Tmap(k;\vartheta)$, a continuous self-map of $\Theta$; it
is always written calligraphically, since upright $T$ is the filing window. On a region $\mathcal R$
the contraction bound is $L_{\mathcal R} = \sup_{\mathcal R}\lVert D_k\Tmap\rVert$, required to be
below $1$ by Assumption~\ref{asm:AGE}. The strictness coordinates are $r_\tau = -\tau$ and
$r_T = -T$, so that higher $r$ is tighter. The direct fixed-policy attenuation margin is
\begin{equation}
\label{eq:gPE}
g_r^{PE} \;=\; -\operatorname{sgn}\!\bigl(d\Dact/d\kappa\bigr)\;\partial_{\kappa r}\Dact,
\end{equation}
with the sign written inline rather than carried by a symbol. The inversion-free derivative bounds
are $\bar k_x = |\partial_x\Tmap|/(1-L_{\mathcal R})$ and $\bar k_{\kappa r}$, and the
general-equilibrium remainder bound is
\begin{equation}
\label{eq:BGE}
\mathcal B_r^{GE} \;=\; |\Delta_{\kappa k}|\,\bar k_r
\;+\; \bigl(|\Delta_{kr}| + |\Delta_{kk}|\,\bar k_r\bigr)\bar k_\kappa
\;+\; |\Delta_k|\,\bar k_{\kappa r}.
\end{equation}
The \emph{dominance-and-contraction region} is $\mathcal R_r$, with slack
$\eta_r = g_r^{PE} - \mathcal B_r^{GE}$; the region may be empty.
\end{definition}

\begin{definition}[\S4.4 premium decomposition and comparative-statics objects]
\label{def:premium}
The engagement-premium kernel is $h(\mathcal I) = \pi(\mathcal I)\,p(\mathcal I)$, with $h \ge 0$ and
$h(0) = 0$, and the expected engagement-related premium is
\begin{equation}
\label{eq:Dact}
\Dact \;=\; \Delta_m\,\Eop\bigl[h(\mathcal I_H)\bigr] \;\ge\; 0.
\end{equation}
The cell averages are $M_F = \Delta_m\Eop[h \mid D=1]$ and $M_P = \Delta_m\Eop[h \mid D=0]$, each
defined when its cell has mass. The unconditional flagged weight is $\Omega = \Prb(D=1) \in [0,1]$,
which factors as $\Omega = \Prb(a=1)\,\omega_a$ with $\omega_a = \Prb(D=1 \mid a=1)$ the disclosed
share of engagements. The quantity $\bar\pi$ is the \emph{upper support point} of the pooled
engagement posterior in the representation \eqref{eq:atau}. The pooled engagement share is the
\emph{mean} of that law, not $\bar\pi$; under Assumption~\ref{asm:Atau} the share is
$\kappa$-invariant, being a mean-preserving spread, so it cannot be the quantity whose
$\kappa$-motion Lemma~\ref{lem:L3} describes, it is strictly below $\bar\pi$ in any non-degenerate
case, and it equals $\bar\pi/2$ only under the level symmetry $A_0 = A_1$. The liquidity
sensitivities are $\mathcal S = |\partial_\kappa\Dact|$ and $\mathcal S_P =
|\partial_\kappa M_P|$. The chord is
\begin{equation}
\label{eq:chord}
C_h(\bar\pi) \;=\; h(0) \;-\; 2h(\bar\pi/2) \;+\; h(\bar\pi),
\end{equation}
maintained non-positive with $|C_h|$ weakly increasing in $\bar\pi$, and $\Akap$ is the common
derivative of the weights in \eqref{eq:atau}, bounded on $[0,1]$. The weight-effect ratios are
$W_\tau$ and $W_T$ --- for instance $W_T = (1-\Omega(\tau,5))/(1-\Omega(\tau,10))$, at most $1$ when
$\Omega$ rises --- and the composition-effect ratios are $C_\tau$ and $C_T$, for instance
$C_T = \mathcal S_P(\tau,5)/\mathcal S_P(\tau,10)$, which are unsigned. The margin subscript on a
composition ratio is always written, because $C$ is otherwise overloaded by the chord $C_h$, the
engagement cost $C_j(s)$ and the cells $\mathcal C_F,\mathcal C_P$.
\end{definition}

Reading $\bar\pi$ as the mean of the pooled posterior law rather than as its upper support point
forces a point mass at $\bar\pi$ with $\Akap = 0$ and zero interior motion for every kernel. That is
degenerate, and it is excluded throughout.
===== END sections_v3/model_section.tex =====

---

### 7.3 The eight proofs, by opening

One block per proof: the `\begin{proof}` line through the end of that proof's first step, exactly
as the file carries it. The pointer above each block says what the proof does and where its weight
sits. Nothing is elided inside a block; everything after a block's last line is in the repository
file named in its header.

**D1 — the disclosure partition and the price-path decomposition.** Parts (a) and (b) are the
measurability and clock-equivalence content D1 exports by statement to L2, L4 and P1; part (c) is
the flagged price-path identity. Full proof: `sections_v3/proofs_core_lemmas.tex` lines 19–178,
Steps 1–13.

FILE: sections_v3/proofs_core_lemmas.tex (excerpt: proof opening only — D1, through Step 1)

===== BEGIN sections_v3/proofs_core_lemmas.tex (excerpt, lines 19-34) =====
\begin{proof}[Proof of Lemma~\ref{lem:D1} (D1)]
Throughout this proof, $j(\cdot)$ denotes the cutoff selection map of
Definition~\ref{def:cpbe}\,(i), the map carrying the signal into a plan at the cutoff vector in
force, and $\sigma(\cdot)$ the $\sigma$-algebra generated by its argument. Parts~(a) and~(b) are established first, under no restriction whatever on
the probability of either cell; part~(c) follows.

\emph{Step 1 (one probability space, and a Borel selection map).} By Assumption~\ref{asm:A1} the
vector $(v,\varepsilon,\xi,z_{0:H})$ has a joint law on a finite product of Polish spaces, the noise
coordinates taking values in the finite set $\{-\bar z,0,+\bar z\}$ of
Definition~\ref{def:primitives}, so every object below lives on one probability space. The signal
$s = v+\varepsilon$ is a sum of two coordinates and is Borel. By Definition~\ref{def:cpbe}\,(i),
$j(\cdot)$ is a step function with breakpoints $k_1 \le \dots \le k_{J-1}$, finitely many because the
plan menu is finite by Assumption~\ref{asm:A2p}. A step function with finitely many breakpoints is a
finite sum of indicators of half-lines, so $j(\cdot)$ is Borel and $\{s : j(s) = j\}$ is Borel for
every $j \in \mathcal J$.

===== END sections_v3/proofs_core_lemmas.tex (excerpt, lines 19-34) =====

**L1 — two-cell decomposition of the engagement premium.** The pointwise split and its integration,
with the two degenerate cases ($\Omega = 1$ and $\Omega = 0$) handled explicitly rather than assumed
away. Full proof: `sections_v3/proofs_core_lemmas.tex` lines 180–260, Steps 1–10.

FILE: sections_v3/proofs_core_lemmas.tex (excerpt: proof opening only — L1, through Step 1)

===== BEGIN sections_v3/proofs_core_lemmas.tex (excerpt, lines 180-185) =====
\begin{proof}[Proof of Lemma~\ref{lem:L1} (L1)]
\emph{Step 1 (the kernel is bounded).} By Definition~\ref{def:premium} the engagement-premium kernel
is $h(\mathcal I) = \pi(\mathcal I)p(\mathcal I)$, and by Definition~\ref{def:prices} the engagement
posterior satisfies $\pi \in [0,1]$ while the entry probability of \eqref{eq:entry} satisfies
$p \in (0,1)$. Their product satisfies $0 \le h \le 1$ pointwise.

===== END sections_v3/proofs_core_lemmas.tex (excerpt, lines 180-185) =====

**L2 — $\kappa$-invariance of the flagged cell.** The weight is Steps 3 and 6–10: the flagged tuple
pins the signal with a measurable inverse, the information sandwich, and the freezing lemma that
makes the flagged posterior $\kappa$-free. Full proof: `sections_v3/proofs_core_lemmas.tex` lines
262–482, Steps 1–13.

FILE: sections_v3/proofs_core_lemmas.tex (excerpt: proof opening only — L2, through Step 1)

===== BEGIN sections_v3/proofs_core_lemmas.tex (excerpt, lines 262-280) =====
\begin{proof}[Proof of Lemma~\ref{lem:L2} (L2)]
Write $\Xi := (v,s,\xi)$ for the triple whose conditional independence is at issue, $z_{0:H}$ for the
noise vector, $\mathcal H_{f^-}^P$ for the pre-filing pooled history on a flagged path, and $\Sfl$
for the flagged tuple $(B^F,Q^F,a{=}1)$ of Definition~\ref{def:prices}, that is, the filing message
$F$ augmented by the flagged order. The functions $u_1,u_2$ below are bounded and measurable and are
local to this proof.

\emph{Step 1 (where $\kappa$ lives).} At fixed cutoff and execution policies, and under the
no-feedback timing of Assumption~\ref{asm:nofeedback}, every policy object --- the selected plan
$j = j(s)$, the path $B_j(s,\cdot)$, the order marks $q_{jd}(s)$, the terminal target $b_j^*(s)$, the
crossing date $c_j(s)$, the filing date $f_j(s)$, the disclosure indicator $D_j(s)$, the filing stake
$B_j^F(s)$ and the flagged order $Q_j^F(s)$ --- is a function of $(s;\tau,T)$ alone.
Assumption~\ref{asm:nofeedback} removes any dependence on realised order flow or prices, and fixed
policies remove any dependence on $\kappa$ through re-optimised cutoffs. Inspecting the primitives of
Definition~\ref{def:primitives}, noise-trading intensity $\kappa$ appears in exactly one place, the
law of the ternary noise mark; the laws of $v$, $\varepsilon$ and $\xi$ and the remaining constants
carry no $\kappa$. Write $Q_\kappa$ for the law of $z_{0:H}$. At fixed policies, then, $\kappa$
enters the model only through $Q_\kappa$.

===== END sections_v3/proofs_core_lemmas.tex (excerpt, lines 262-280) =====

**L3 — interior motion of the pooled premium under the chord restriction.** Steps 1–6 are the two
mean-value applications that make $C_h(\bar\pi) = \tfrac14\bar\pi^2 h''(\zeta)$ an identity rather
than an approximation; Steps 7–11 carry A($\tau$) into $\partial_\kappa\mathbb E_\kappa[h] =
A'_\kappa C_h(\bar\pi)$. **Part IV, Steps 16–18, is where A($\tau$)'s satisfiability is argued and
where (S1)/(S2) are named** — the clauses §2(c) reports as refuted at the implemented calibration.
Full proof: `sections_v3/proofs_core_lemmas.tex` lines 484–884, Steps 1–18.

FILE: sections_v3/proofs_core_lemmas.tex (excerpt: proof opening only — L3, through Step 1)

===== BEGIN sections_v3/proofs_core_lemmas.tex (excerpt, lines 484-495) =====
\begin{proof}[Proof of Lemma~\ref{lem:L3} (L3)]
The order taken here is part~(b) first, since it is a statement about one fixed $\bar\pi$ and
consumes none of the chord restriction, then part~(a), then part~(c), which combines them.
Throughout, $\bar\pi > 0$ and $\kappa$ ranges over an open interval on which the weights of
\eqref{eq:atau} are differentiable.

\emph{Step 1 (what the minimal regularity gives).} By hypothesis $h$ is continuous on $[0,\bar\pi]$
and twice differentiable on the open interval $(0,\bar\pi)$. Twice differentiable on $(0,\bar\pi)$
means that $h'$ exists at every point of that interval and is itself differentiable at every point of
it; a differentiable function is continuous, so $h'$ is continuous on $(0,\bar\pi)$. Nothing is
assumed about $h'$ or $h''$ at either endpoint, and no continuity of $h''$ is assumed anywhere.

===== END sections_v3/proofs_core_lemmas.tex (excerpt, lines 484-495) =====

**L4 — threshold tightening: nesting, composition, and the pooled sensitivity.** Legs 1–2 are
unconditional (Steps 4–11); **leg 3 is the conditional one** (Steps 12–16), consuming L3 by
statement, A($\tau$)'s magnitude clause and A(br) (br-i)–(br-v). Full proof:
`sections_v3/proofs_core_lemmas.tex` lines 886–1107, Steps 1–16.

FILE: sections_v3/proofs_core_lemmas.tex (excerpt: proof opening only — L4, through Step 1)

===== BEGIN sections_v3/proofs_core_lemmas.tex (excerpt, lines 886-899) =====
\begin{proof}[Proof of Lemma~\ref{lem:L4} (L4)]
In this proof, $j(\cdot)$ is the plan the frozen cutoff vector selects at each signal,
$\mathcal N := \mathcal C_F(\tau',T)\setminus\mathcal C_F(\tau,T)$ the newly flagged set,
$\nu := \Prb(\mathcal N)$ for its mass, and $\rho_P := 1-\Omega(\tau,T)$ for the pooled mass at the
looser threshold. The three legs are proved in order; nestedness is derived at Step~4 as part of
leg~1 rather than assumed.

\emph{Step 1 (only the clock objects move with the threshold).} At fixed policies the selection map
$j(\cdot)$, the engagement labels and the path family $B_j(s,\cdot)$ are the same objects at $\tau$
and at $\tau'$. Definition~\ref{def:plans} writes the stake path with no threshold argument, whereas
the crossing date, the filing date, the stake at filing and the disclosure indicator all carry one.
In the comparison below, therefore, the only objects that move when the threshold moves are those
four; the path itself is common to the two environments.

===== END sections_v3/proofs_core_lemmas.tex (excerpt, lines 886-899) =====

**P1 — existence of a cutoff perfect Bayesian equilibrium.** The row your review demoted and the
repair restored. Weight sits in Step 9 (pooled beliefs as limits of one full-support perturbation
family, fixed once), Step 10 (A7-J pinning the flagged belief at every image tuple), **Step 12 (the
new lemma that closes the sunk-cost gap)**, Step 13 (the named tie-break and the self-map property)
and Steps 15–16 (continuity, where hypothesis (P-5)/A6 assumes rather than derives — the assumption
§2(d) reports as failing at the implemented calibration). Full proof:
`sections_v3/proofs_existence.tex` lines 32–1025, Steps 1–20, Parts A–F.

FILE: sections_v3/proofs_existence.tex (excerpt: proof opening only — P1, through Step 1)

===== BEGIN sections_v3/proofs_existence.tex (excerpt, lines 32-87) =====
\begin{proof}[Proof of Proposition~\ref{prop:P1} (P1: existence)]
The argument builds the equilibrium object rather than characterising it. Parts~A and~B fix a
conjectured cutoff vector and solve the price system it induces, separating a finite pooled layer
from a continuum-indexed flagged layer; Part~C supplies beliefs at every history that carries a
requirement, on path and off; Part~D discharges sequential optimality of the flagged component at
every flagged pair; Part~E builds the outer best-response map, applies Brouwer's fixed-point theorem
and assembles the six requirements of Definition~\ref{def:cpbe}; Part~F is the addendum under
Assumption~\ref{asm:A8} (A8). The parameter vector $\vartheta$ is fixed throughout and suppressed where it
does not vary.

\smallskip\noindent\emph{Notation used only in this proof.} Write $\sigma_F$ for a generic value of
the flagged tuple $\Sfl$ of Definition~\ref{def:prices}, and
$[\underline s,\overline s]$ for the common signal bracket underlying the polytope $\Theta$ of
Definition~\ref{def:theta}. Write $\Phi_s$ and $\varphi_s$ for the c.d.f.\ and density of the signal
$s$, reserving $\Phi$ for the standard normal c.d.f.\ of \eqref{eq:entry} and $\phi$ for its density.
At a control-node information set $\mathcal I$ put
\[
\hat v(\mathcal I) = \Eop[v \mid \mathcal I],
\qquad
\pi(\mathcal I) = \Prb(a = 1 \mid \mathcal I),
\qquad
\bar m(\mathcal I) = m_0 + \pi(\mathcal I)\,\Delta_m .
\]
Further symbols --- $\mathcal P_{\mathcal I}$, $\varrho$, $A$, $\mathcal G_F$, $\iota_F$, $j_k$,
$j^\star$, $\mathcal S(k)$, $\mathfrak w$, $\mathcal Q_j(s)$, $G_j$, $E_j$, $\mu_n$, $L_j$, $w_n$,
$t_n$, $Z_n$, $\Lambda_k$, $\Lambda_u$, $(\hat v_\circ,\pi_\circ)$, $P_\circ$,
$\operatorname{supp}(z_d)$, $s_F$ --- are declared where they are first used. The engagement cost
$C_j(s)$ and the execution outlay $\mathcal C_j^{\mathrm{trade}}$ of Definition~\ref{def:U} are
always written with their subscripts, so that neither collides with the chord $C_h$ of
\eqref{eq:chord}, the composition ratios $C_\tau,C_T$, or the cells $\mathcal C_F,\mathcal C_P$.

\medskip
\noindent\emph{Part A: the game at a fixed conjecture.}

\smallskip
\noindent\textbf{Step 1 (the conjecture induces a measurable plan-selection map).}
Fix a conjectured cutoff vector $k = (k_1 \le \dots \le k_{J-1})$ in
\[
\Theta \;=\; \bigl\{k \in [\underline s,\overline s]^{J-1} :
\underline s \le k_1 \le \dots \le k_{J-1} \le \overline s\bigr\},
\]
the cutoff polytope of Definition~\ref{def:theta}. It is nonempty, compact and convex, being the
intersection of a cube with the $J-2$ half-spaces $\{k_i \le k_{i+1}\}$; nonemptiness is not
decoration, since Brouwer's theorem is vacuous without it, and it is supplied by
Definition~\ref{def:theta}. Define the map induced by the conjecture,
\begin{equation}
\label{eq:P1-jk}
j_k(s) \;=\; 1 + \#\bigl\{i \in \{1,\dots,J-1\} : k_i \le s\bigr\}.
\end{equation}
Each set $\{s : k_i \le s\}$ is a half-line, so $j_k$ is a weakly increasing step function of $s$
with values in $\mathcal J$, and it is Borel. This is the object requirement~(i) of
Definition~\ref{def:cpbe} calls a weakly ordered cutoff vector mapping the signal into a plan. The
second clause of Assumption~\ref{asm:A3} (A3) --- hypothesis (P-3), that the preferred plan is weakly
increasing in $s$ --- is what makes a representation of this shape the right one for a best response;
Step~13 returns to that point and derives the representation rather than assuming it.

===== END sections_v3/proofs_existence.tex (excerpt, lines 32-87) =====

**T1 — disclosure attenuation at fixed policies.** Part (A) is the exact factorisation (Steps 1–6);
Part (B) is the threshold side, conditional through L4 leg 3 (Steps 7–11); **Part (C) is the window
side, an iff and not a sign** — Step 12 proves $W_T \le 1$, Step 13 records that $C_T$ carries no
sign, and Steps 15–17 fix the "on average along the tightening path" quantifier. Full proof:
`sections_v3/proofs_theorem_ge.tex` lines 17–413, Steps 1–17.

FILE: sections_v3/proofs_theorem_ge.tex (excerpt: proof opening only — T1, through Step 1)

===== BEGIN sections_v3/proofs_theorem_ge.tex (excerpt, lines 17-47) =====
\begin{proof}[Proof of Theorem~\ref{thm:T1} (T1)]
Throughout, policies are frozen in the sense of hypothesis~(T-1): the plan menu $\mathcal J$, the
execution policies $B_j(\cdot,\cdot)$, $b_j^*(\cdot)$ and $Q_j^F(\cdot)$, and the cutoff vector $k$
are held fixed in $\kappa$ and held fixed across the two rules compared at each margin. Nothing
below lets $k$ re-solve $k = \Tmap(k;\vartheta)$ at the second rule; that is the whole difference
between this theorem and Proposition~\ref{prop:C1}.

Two pieces of hypothesis traffic are worth naming before the argument starts, because several steps
draw on them. First, hypothesis~(T-5) imports Lemma~\ref{lem:L2} \emph{with its own hypotheses
travelling}, and those hypotheses are Assumption~\ref{asm:A1}, Assumption~\ref{asm:A2p} together
with the primitive table restrictions of Assumption~\ref{asm:TR}, Assumption~\ref{asm:A4},
Assumption~\ref{asm:A5}, Assumption~\ref{asm:A7p} in its on-path injective form,
Lemma~\ref{lem:D1}, the no-feedback timing of Assumption~\ref{asm:nofeedback}, $\Omega > 0$, and an
explicit bidder-entry rule. Where a step below consumes one of them it is cited by name, and it is
consumed as a travelling hypothesis of~(T-5) rather than as a free-standing assumption of this
theorem. The A7 form matters and is therefore named every time: the form
Lemma~\ref{lem:L2} consumes is Assumption~\ref{asm:A7p} (A7$'$), not the weak identification
wording of Assumption~\ref{asm:A7}, which permits two pairs $(j,s)$ with different pooled paths and
is that lemma's first failure case. Second, hypothesis~(T-8) --- $\kappa$-differentiability of
$M_P$ --- is supplied by no standing hypothesis of Section~\ref{sec:hypotheses} and is carried here
as a hypothesis of the theorem; Step~4 is where it is used, and the integrability clause of
Assumption~\ref{asm:A2p} is \emph{not} cited for it, since boundedness is not differentiability.

\medskip
\noindent\emph{Part~(A): the factorisation.}

\emph{Step 1 (the two-cell identity).} By hypothesis~(T-2), Assumption~\ref{asm:A8} holds at the
policy under consideration, so $0 < \Omega < 1$ and Lemma~\ref{lem:L1}, imported by
hypothesis~(T-4), applies in its non-degenerate branch: identity~\eqref{eq:L1} holds at
$(\kappa,\tau,T)$, with $M_F$ and $M_P$ the cell averages of Definition~\ref{def:premium}.

===== END sections_v3/proofs_theorem_ge.tex (excerpt, lines 17-47) =====

**C1 — the dominance-and-contraction implication in general equilibrium.** The three-way label split
your last review endorsed lives here: the implication is proved with the region named as a
hypothesis, its nonemptiness is not proved, and the grid nodes checked against it are NUMERICAL. The
opening carries the norm-convention preamble the whole argument is stated in. Full proof:
`sections_v3/proofs_theorem_ge.tex` lines 434–707, Steps 1–9.

FILE: sections_v3/proofs_theorem_ge.tex (excerpt: proof opening only — C1, through Step 1)

===== BEGIN sections_v3/proofs_theorem_ge.tex (excerpt, lines 434-520) =====
\begin{proof}[Proof of Proposition~\ref{prop:C1} (C1)]
Four conventions are fixed first, because the statement's hypotheses are stated against them.

\emph{The margin.} By hypothesis~(C-7) the strictness coordinate is the threshold one,
$r = r_\tau = -\tau$ of Definition~\ref{def:theta}, and $\vartheta = (\kappa,r)$.
Definition~\ref{def:primitives} restricts only the window to integers and places no discreteness on
$\tau$, so $r$ is a coordinate on an interval and the derivatives below have a domain to live on.
The window coordinate is excluded: $T$ takes values in $\{1,\dots,H\}$ there, so $\partial_{r_T}$,
$\partial_{\kappa r_T}\Dact$ and $g_{r_T}^{PE}$ have no meaning without an interpolation of the
model in $T$, and nothing local is claimed at that margin.

\emph{The norm.} By hypothesis~(C-1) one norm $\lVert\cdot\rVert$ is fixed on the cutoff space
$\mathbb R^{J-1}$, and every magnitude bar in the $\bar k_x$ and $\bar k_{\kappa r}$ rows of
Definition~\ref{def:theta}, in $L_{\mathcal R}$, and in \eqref{eq:BGE} is read as the member of the
family that norm induces: $\lVert\cdot\rVert$ itself for the vector-valued objects
$\partial_\kappa\Tmap$, $\partial_r\Tmap$ and $\Tmap_{\kappa r}$; the induced operator norm
$\sup_{\lVert w\rVert\le1}\lVert Aw\rVert$ for the matrices $D_k\Tmap$, $\Tmap_{\kappa k}$ and
$\Tmap_{rk}$; $\sup_{\lVert w_1\rVert,\lVert w_2\rVert\le1}\lVert\Tmap_{kk}[w_1,w_2]\rVert$ for the
vector-valued bilinear form $\Tmap_{kk}$; the \emph{dual} norm
$\lVert\phi\rVert_* = \sup_{\lVert w\rVert\le1}\lvert\phi(w)\rvert$ for the covectors $\Delta_k$,
$\Delta_{\kappa k}$ and $\Delta_{kr}$; and
$\sup_{\lVert w_1\rVert,\lVert w_2\rVert\le1}\lvert\Delta_{kk}[w_1,w_2]\rvert$ for the scalar
bilinear form $\Delta_{kk}$. Two consequences are used. The operator norm must be induced, hence
submultiplicative, because Step~1 needs $\lVert A^n\rVert \le \lVert A\rVert^n$; and the pairing
must be the matching one, because pairing a covector with a vector through a magnitude that is not
the dual norm can make \eqref{eq:BGE} \emph{understate} the remainder it is meant to bound, which
voids the implication silently. At $J-1 = 1$ the whole family collapses to the absolute value and
the convention is vacuous.

\emph{The equilibrium objects.} By hypothesis~(C-3) there is, at every $\vartheta$ in the region
$\mathcal R_r$, a cutoff vector $k(\vartheta)$ in the interior of $\Theta$ with
$k(\vartheta) = \Tmap(k(\vartheta);\vartheta)$, and $\vartheta\mapsto k(\vartheta)$ is one branch,
with no switch of selected equilibrium inside $\mathcal R_r$. Interiority is a genuine restriction:
Definition~\ref{def:cpbe}\,(i) has weak inequalities and so permits collapsed action regions, and a
collapsed region puts $k$ on the boundary of $\Theta$, where the fixed-point equation may hold only
as a one-sided condition. Write, for this proof,
\[
\mathcal D(\kappa,r) \;:=\; \Dact\bigl(k(\kappa,r),\kappa,r\bigr),
\qquad
\mathcal S^{GE} \;:=\; \Bigl\lvert \frac{d\mathcal D}{d\kappa} \Bigr\rvert ,
\]
so that $\mathcal D$ is the premium \eqref{eq:Dact} evaluated along the equilibrium branch --- not
the disclosure indicator $D$ --- and $\mathcal S^{GE}$ is the equilibrium liquidity sensitivity of
hypothesis~(C-5). It is a different object from the fixed-policy $\mathcal S = |\partial_\kappa\Dact|$
of Definition~\ref{def:premium}, which holds $k$ frozen; the two agree only where the cutoff
response contributes nothing, and the entire content of this proposition sits in the difference.
Every partial derivative of $\Dact$ and of $\Tmap$ written below is a partial of the
\emph{fixed-policy} map $(k,\kappa,r)\mapsto\Dact(k,\kappa,r)$, respectively of
$(k,\kappa,r)\mapsto\Tmap(k;\kappa,r)$, evaluated at the equilibrium point
$(k(\vartheta),\vartheta)$.

\emph{The region and its regularity.} Hypothesis~(C-1) puts Assumption~\ref{asm:AGE} in force on
$\mathcal R_r$, and names the clause that carries the weight: the contraction bound
$L_{\mathcal R} = \sup_{\mathcal R}\lVert D_k\Tmap\rVert < 1$ of Definition~\ref{def:theta}, read
along the equilibrium path, that is, as the supremum over $\vartheta \in \mathcal R_r$ of
$\lVert D_k\Tmap(k(\vartheta);\vartheta)\rVert$. That reading is the one used at Steps~1--4 and it
is the weaker of the two available; the stronger reading, a supremum over all of $\Theta$ as well,
is not consumed anywhere below. The differentiability clause of Assumption~\ref{asm:AGE} supplies
twice continuous differentiability of $\Tmap$ on a neighbourhood of the equilibrium graph
$\{(k(\vartheta),\vartheta) : \vartheta\in\mathcal R_r\}$, which is the weakest domain Steps~1--4
use; smoothness away from that graph is never called on. Hypothesis~(C-4) supplies twice continuous
differentiability of $\Dact$ in $(k,\kappa,r)$ on the same neighbourhood, and with it finiteness of
the derivatives named in \eqref{eq:BGE} and in $\bar k_{\kappa r}$. The integrability clause of
Assumption~\ref{asm:A2p} is not cited for that and cannot be: boundedness is not differentiability.
Finally, hypothesis~(C-2) makes $\mathcal R_r$ relatively open in both coordinates with
$\kappa\notin\{0,1\}$, so that every $\vartheta\in\mathcal R_r$ has a full two-dimensional
neighbourhood inside $\mathcal R_r$ --- which the implicit function theorem of Step~2, the mixed
partial of Step~5 and the sign argument of Step~7 all need, and which openness in $r$ alone would
not give, $\kappa$ ranging over $[0,1]$ in Definition~\ref{def:primitives}.

\emph{Step 1 (invertibility, without forming an inverse).} Fix $\vartheta\in\mathcal R_r$ and write
$A = D_k\Tmap(k(\vartheta);\vartheta)$, so $\lVert A\rVert \le L_{\mathcal R} < 1$ by~(C-1). By
submultiplicativity, $\lVert A^n\rVert \le L_{\mathcal R}^{\,n}$, so
$\sum_{n\ge0}\lVert A^n\rVert \le (1-L_{\mathcal R})^{-1} < \infty$. The space of
$(J-1)\times(J-1)$ matrices being finite dimensional and complete, the partial sums
$S_N = \sum_{n=0}^{N}A^n$ converge to a limit $S$ with
$\lVert S\rVert \le (1-L_{\mathcal R})^{-1}$; and from $(I-A)S_N = S_N(I-A) = I - A^{N+1}$ with
$\lVert A^{N+1}\rVert \le L_{\mathcal R}^{\,N+1} \to 0$, passing to the limit gives
$(I-A)S = S(I-A) = I$. Hence $I - D_k\Tmap$ is invertible at every point of the equilibrium graph,
with
\begin{equation}
\label{eq:C1-neumann}
\bigl\lVert (I-D_k\Tmap)^{-1} \bigr\rVert \;\le\; \frac{1}{1-L_{\mathcal R}} .
\end{equation}
The bound is a geometric sum of norms, so every derivative bound below is available from
$\lVert D_k\Tmap\rVert$ and one directional derivative of $\Tmap$, with no linear system solved.

===== END sections_v3/proofs_theorem_ge.tex (excerpt, lines 434-520) =====

---

## 8. WHAT IS ASKED BACK

Answer in this format. It is short on purpose: the lane can act on a verdict plus a clause
citation, and cannot act on a general impression.

**1. Per result, a verdict line.** Cover every row in §3's ledger — D1, L1, L2, L3, L4, P1, T1, C1 —
and, separately, the assumption blocks that now carry failure evidence: A($\tau$), A6, A3. For each,
exactly one of:

  - **LABEL STANDS** — the row's label and its stated conditionality survive your read.
  - **DEMOTE** — with the target label named.

  There is no third option in the upward direction. **Your review can demote a label; it cannot
  promote one by prose.** If you believe a row understates what has been established, say so as a
  finding and stop there: the lane will not raise a label on a reviewer's assessment, only on a
  written proof carried through the two-pass gate, or — for NUMERICAL — on an executed, committed
  check.

**2. Per result, findings classified.** Every finding you raise carries exactly one class:

  - **WRONG** — a source in this bundle, or a check you can execute or re-derive from the numbers
    given, contradicts the claim. This is the only class that blocks.
  - **MISCITED** — the claim stands, but the citation attached to it (a proof step, a check name, a
    file, a step number) is wrong, mismatched, or does not say what it is cited as saying.
  - **UNCHECKED** — you could not check it with what is in this paste. Return the claim itself, not
    a count. Do not silently downgrade a decision-critical claim to low priority because it is
    unchecked; §7.3's proof openings in particular will generate legitimate UNCHECKEDs.

  MISCITED and UNCHECKED never block, and both are wanted. A bundle that comes back with nothing in
  those two classes will be read as a bundle that was not checked.

**3. Every demotion must name the exact clause and the record it turns on.** A demotion is actioned
only if it says all three of:

  (i) **the clause** — quoted from §3's card row or from §7.1's statement, not paraphrased;
  (ii) **the record** — the file and location in this bundle that contradicts it (a proof step in
       §7.3, a paragraph in a §5 record, a field in a §6 verdict, a line of the card or ledger);
  (iii) **what it survives as** — the weaker statement that the existing argument still supports,
       or an explicit statement that nothing survives.

  A demotion with (i) and (ii) but not (iii) is still actioned, and is answered by a repair ticket
  rather than by an amendment. A demotion without (i) or without (ii) is returned to you for the
  clause, because the lane cannot supersede a landed record line without one.

**4. Three questions the lane wants answered whether or not a label moves.**

  (i) Is P1's **amended** statement the theorem the model needs, or a retreat to what the proof
      happened to establish? Name the gap if it is the second.
  (ii) Is "PROVED as a conditional, antecedent measured false at the only implemented calibration"
      honest labelling, or PROVED-adjacent language for something unusable? The three blocks at
      issue are A($\tau$) (L3, L4 leg 3, T1 Part B), A6 (P1) and A3 (P1).
  (iii) Does §7.1's paper prose drop any conditionality the card carries? Cite statement and card
      row side by side if so.

**5. Answer in the card's own §8 template** — CLAIM · HYPOTHESES · PROOF · WHERE IT FAILS · LABEL
CLAIMED + why · NUMERICAL CHECK REQUEST · NOTATION DELTA · NOT CLAIMED — for every result you rule
on. NOTATION DELTA and NOT CLAIMED are both mandatory, every time, including when the verdict is
LABEL STANDS and including when it is UNCHECKED.
