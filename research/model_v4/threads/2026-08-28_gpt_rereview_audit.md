# Audit of the GPT Pro re-review — 2026-08-28

**Auditor role.** Audit agent for the 2026-08-28 re-review. I wrote none of the material under
audit — not the card, not the sections, not the proofs, not the bundle. My only write is this file.
I ran no git command.

**Object.** `threads/2026-08-28_gpt_rereview.md` — GPT Pro's re-review, filed verbatim. Its verdict
index: all eleven labels STAND, zero demotions. It returns five items classed WRONG, three MISCITED,
and several UNCHECKED, plus eleven numerical check requests.

**Primary records consulted.** `MODEL_CARD.md` (§4 symbol table, §5 A3/A5/A6/A7/A(τ)/A(br) blocks,
§6 result ledger, §9); `proofs/P1_proof.md` (h.5, Steps 7–8, the repair table, the not-applied note);
`proofs/L3_proof.md` Step 19; `threads/thread1_turn2_answer.md` (the D1/L1/L2 proofs);
`threads/2026-08-27_t4_sections_check.md` (the in-house checker, finding M-8 and its stamp
verification); `threads/gpt_rereview_bundle_2026-08-28.md` (the delta narrative and the bundle's own
declared design); `HANDOFF_sign.md` §3; `sections_v3/` (`model_section.tex`, `theorem_section.tex`,
`proofs_existence.tex`, `proofs_core_lemmas.tex`, `proofs_theorem_ge.tex`, `v3_macros.tex`);
`quality_reports/fixes/` (the `t2_*` inventory).

**Card stamp verified before starting.** `MODEL_CARD.md` line 3 reads *"Version stamp: 2026-08-28 ·
follow-up curation (§5 A6 curation note + A3 sweep note) · commit `926f58c`."* This is the
controlling stamp and the stamp the re-review was run against. **Match.**

**HEADLINE.** **No label moves anywhere in this audit, and none is licensed.** GPT demoted nothing;
nothing in the record licenses a demotion; nothing here promotes. **No `LABEL_LEDGER.md` entry
results from this audit.** Every repair below is wording, transcription, scoping or provenance.

**Rules in force.** The review may demote, never promote (`LABEL_LEDGER.md` standing note 2). No
repair lands before this audit. Nothing moves until the orchestrator applies it — this file drafts,
it does not edit. Verification vocabulary: WRONG blocks with one retry; MISCITED and UNCHECKED never
block.

---

## Scorecard

Fifteen rulings — fourteen GPT findings plus one asserted spillover (1b). **8 UPHELD (five of them
with-scope) · 4 NARROWED · 3 REJECTED.** No label consequence on any of them.

| # | GPT finding | Class GPT gave | Verdict | Consequence |
|---|---|---|---|---|
| 1 | P1 row's A5-continuity clause does not distinguish belief-continuity from cutoff-continuity | WRONG (blocking) | **UPHELD** | card row clause + A5 block note + 2 section sites; no label |
| 1b | "affects every row that literally carries full A5" (D1, L1, L2) | asserted spillover | **REJECTED** | no row edits; their proofs consume existence/uniqueness/version-pinning only |
| 2 | A(τ) note's lead sentence contradicts its own derivative-pattern bullet | WRONG (blocking) | **UPHELD** | card §5 lead + 1 section site + 2 mirrors; no number changes |
| 3 | model_section still says "$\mathcal T$ bit-identical" on the collapse face | WRONG (blocking) | **UPHELD-WITH-SCOPE** | section transcription from the card's curation note |
| 4 | model_section still says the A6 probes are "analysis-grade, not curated" | WRONG (blocking) | **UPHELD-WITH-SCOPE** | section transcription from the card's curation note |
| 5 | rem:A3record still says the account is "UNCHECKED beyond the one node probed" | WRONG (blocking) | **UPHELD-WITH-SCOPE** | section transcription from the card's sweep note |
| 6 | belief-snap "about $10^{-8}$" needs the bracket qualifier | MISCITED | **UPHELD-WITH-SCOPE** | section transcription; same site family as 3–5 |
| 7 | section headers cite card stamp 2026-08-27 `ae9caea` | MISCITED | **UPHELD-WITH-SCOPE** | six provenance headers advance; three dated-fact sites stay |
| 8 | "The failure boundary **for the on-path form**" narrows an unscoped card list | MISCITED | **UPHELD** | delete four words; converges with in-house M-8 |
| 9 | card cites L3 Step 19 where the paper folds it into Step 15 | MISCITED | **NARROWED** | **no repair** — the card's anchor targets the proof file and resolves |
| 10 | O-1's $\approx0.29$ vs $0.343$ is an unresolved discrepancy | UNCHECKED | **REJECTED-AS-DISCREPANCY** | pre-adjudicated in `HANDOFF_sign.md` §3; one optional parenthetical |
| 11 | proofs and JSONs available only by opening / as extracts | UNCHECKED | **REJECTED** | the bundle's declared design, stated in its own §1 and §7.3 |
| 12 | no complete witness satisfying the full P1 hypothesis set | UNCHECKED | **NARROWED** | agreement with card §9 items 2 and 4, not a finding |
| 13 | continuum-face lemma citable as observation, not proved extension | UNCHECKED | **NARROWED** | agreement with the card's own "not gate-checked" label |
| 14 | eleven numerical check requests | request | **NARROWED** | none executed; one (A3) recorded on-file-not-started |

**Two registers are in play and the orchestrator should not mix them.** The **card** and its §5 notes
are landed record: a correction there carries a dated marker and an audit pointer, never a silent
rewrite. The **sections** are pre-acceptance draft text being conformed to the controlling card:
repairs there are straight in-place replacement, because the section is a transcription of the card
and the card is the source of truth.

---

## Finding 1 — the P1 row's A5-continuity clause. UPHELD.

**What the card says.** The P1 row (`MODEL_CARD.md:521`) closes its hypothesis block with:

> **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$, its
> continuity content from the same scalar reduction, and its measurable-selection content from A7-J
> plus §4.2's Borel clause (see A5).

**What "(see A5)" points at.** The A5 block (`MODEL_CARD.md:239-242`):

> **A5 is retained only as its continuity clause** — the pricing family is continuous in the cutoff
> vector and the parameters, and measurable in the flagged tuple.

Read together, the row asserts that the content A5 is *retained for* — continuity in the **cutoff
vector** — is derived from the scalar reduction. That is the reading GPT took, and it is the natural
one, because the row's three-part sentence is a part-by-part release of the A5 block's three clauses.

**What the proof actually derives.** `proofs/P1_proof.md` Step 7's closing paragraph (`:450-454`)
adjudicates this in the lane's own words:

> Consequently, on the maintained sign h.12 the existence-and-uniqueness content of A5 is a theorem
> rather than an assumption, and Step 8 adds its continuity-in-the-belief content. **What is left
> over is continuity of the *composition* in the conjecture $k$, which runs through the conditioning
> $(\hat v,\pi)$ rather than through the pricing map; Step 15 takes that up and says where it is
> assumed.**

Step 8 (`:456-465`) is titled "the inner root is monotone and non-expansive in **the belief**" and
delivers $\partial P/\partial\hat v\in(0,1]$ — a bound in the belief summary, not in $k$. The struck
h.5 (`:106-108`) is explicit that the cutoff route was never load-bearing:

> Step 15's "by h.5 the inner prices are continuous in the cutoffs" is **non-load-bearing**, because
> this proof's route to continuity of $\mathcal T$ is h.6 asserting it outright (Steps 15–16) — it
> is marked there as commentary.

So: continuity **in the belief summaries** is derived; continuity **in the cutoff vector** is not
derived anywhere — it enters through A6-as-read. GPT's mathematics is correct.

**The paper's own proof already says the right thing.** `sections_v3/proofs_existence.tex:288-290`
carries Step 7's closing sentence verbatim ("What is left over is continuity of the *composition* in
the conjecture $k$…"), and `:294` opens Step 8 with "Continuity in the belief comes from the same
scalar reduction." The **proof** is disambiguated; the **statement's trailing paragraph** is not.
That asymmetry is the whole defect, and it localises the repair.

**Why this is UPHELD and not merely narrowed.** The task anticipated a NARROWED reading on the
grounds that the card "ALREADY distinguishes the two continuities." It does not. The A5 block's
*statement* sweeps all three variables together ("continuous in beliefs, cutoffs and parameters",
`:227-228`), and its **retained** clause names only the cutoff-vector one (`:239-240`). The row's
sentence is a part-by-part release of the block's clauses — existence, uniqueness, continuity,
measurable selection — so the "continuity content" it releases reads as the clause the block
retains. Nothing in the card tells a reader that the derived continuity is a different object from
the retained one. The clause is not loose; it is wrong under the only pointer the row supplies.

**Two things narrow the consequence, and both are on record.** First, GPT concedes P1's label
survives — "P1's label survives because A6 separately assumes the outer-map continuity used by
Brouwer" — which matches h.5(c) exactly. Second, the P1 proof's not-applied note (`:1482-1489`)
records that the retry reader read the row's clause as **belief**-continuity and left it standing
deliberately:

> The retry's divergence note in item (d) — the row says A5's continuity content comes "from the
> same scalar reduction" while this file derives it from Step 8's implicit-function argument — is
> left standing: the reader records both routes as valid … Two valid derivations of the same clause
> is not a defect.

That adjudication is about **which route** derives belief-continuity (Step 7's monotone reduction vs
Step 8's IFT), and it stands. The repair below must not overturn it: it disambiguates the
**variable**, and it keeps both routes.

**Mechanic.** The P1 row is regenerated wholesale at each stamp, so an in-place clause correction
with this audit as its traceable finding is the house pattern (ticket 32's precedent, where the A7′
gloss's two false consequences were corrected in place at regeneration). The §5 A5 block instead
takes the **A6-curation mechanic**: a dated note appended, the original clause left standing.

### DRAFTED REPAIR — card amendment C-1 (P1 row, `MODEL_CARD.md:521`)

Replace the sentence beginning "**A5 is not assumed**" with:

> **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$; its
> continuity content **in the belief summaries $(\hat v,\pi)$** from the same scalar reduction
> (`proofs/P1_proof.md` Step 7(iii)'s strict $\varrho'<0$ at every root, with Step 8's
> implicit-function bound $\partial P/\partial\hat v\in(0,1]$ as a second recorded route — the proof
> file records both as valid and names neither as the only one); and its measurable-selection
> content from A7-J plus §4.2's Borel clause. **What is *not* derived is A5's cutoff clause** —
> continuity of the *composed* pooled price family in the cutoff vector $k$, which runs through the
> conditioning $(\hat v,\pi)$ rather than through the pricing map (`proofs/P1_proof.md` Step 7,
> closing paragraph; the struck h.5(c), which marks Step 15's cutoff-continuity citation
> non-load-bearing). That continuity enters only through **A6 as read**, and §5's A6 evidence note
> records it **measured to fail** at the implemented calibration (see A5). *Clause corrected in
> place 2026-08-28 on re-review audit finding 1
> (`threads/2026-08-28_gpt_rereview_audit.md`); the hypothesis set, the conclusion and the label are
> unchanged.*

### DRAFTED REPAIR — card amendment C-2 (A5 block, append after `MODEL_CARD.md:243`)

> *Evidence note added 2026-08-28 (re-review audit finding 1;
> `threads/2026-08-28_gpt_rereview_audit.md`).* **The retained continuity clause is an assumption
> about the *composed* family, and it is measured to fail at the implemented calibration.** Two
> continuities must be kept apart, because only one of them is a theorem. (i) Continuity of the
> inner root **in its belief summaries** $(\hat v,\pi)$ follows from $m_0\ge0$ —
> `proofs/P1_proof.md` Steps 7–8, two independent routes on file. (ii) Continuity of the
> **composition** $k\mapsto(\hat v,\pi)\mapsto P$ **in the cutoff vector** is what the clause above
> retains, and no step derives it: the $k$-dependence runs through the conditioning, not through the
> pricing map (`proofs/P1_proof.md` Step 7, closing paragraph). The A6 note below measures exactly
> that composition jumping — the price system is discontinuous on
> $\bigcup_h\partial\{k:\Lambda_k(h)>0\}$, with $\mathcal T_2$ jumps of $6.33\times10^{-3}$ /
> $1.09\times10^{-2}$ / $2.83\times10^{-2}$ at $(\kappa{=}0.5,\tau_{50},T{=}5)$
> (`quality_reports/fixes/t2_a6_edge_jump_check.json`). Clause (ii) and A6's continuity clause
> therefore fail together, at one locus, for the declared construction. **Where each citing row
> stands:** D1 cites A5 for a unique competitive price at every public history and L2 for one
> flagged fixed point — the existence/uniqueness content, released above to $m_0\ge0$; L1 cites it
> to pin *the* version of $\mathbb E[Y\mid\mathcal I]$. **No result row consumes clause (ii)**, so
> no row is touched. **No label moves and none is licensed** — A5 is a hypothesis.

### DRAFTED REPAIR — section S-1 (`sections_v3/theorem_section.tex:258-262`)

Current:

```latex
Two readings belong to the statement rather than to the proof. First, \emph{Assumption~\ref{asm:A5}
is not assumed here}: its existence and uniqueness content is derived from $m_0 \ge 0$, its
continuity content from the same scalar reduction, and its measurable-selection content from
Assumption~\ref{asm:A7J} together with clause (TR-ii)'s Borel regularity. Second,
```

Replacement:

```latex
Two readings belong to the statement rather than to the proof. First, \emph{Assumption~\ref{asm:A5}
is not assumed here}: its existence and uniqueness content is derived from $m_0 \ge 0$, its
continuity content \emph{in the belief summaries} $(\hat v,\pi)$ from the same scalar reduction, and
its measurable-selection content from Assumption~\ref{asm:A7J} together with clause (TR-ii)'s Borel
regularity. What is \emph{not} derived is the cutoff clause of Assumption~\ref{asm:A5}: continuity
of the composed pooled price family in the conjecture $k$, which runs through the conditioning pair
$(\hat v,\pi)$ rather than through the pricing map, as Step~7 of the proof says where it says what
is left over. That continuity enters only through the reading of Assumption~\ref{asm:A6} given next,
and Remark~\ref{rem:A6record} records it measured to fail at the implemented calibration. Second,
```

### DRAFTED REPAIR — section S-2 (`sections_v3/model_section.tex`, append after `:316`)

Every other stressed assumption in the model section carries an adjacent record remark; A5 carries
none. Append after "…it may cite \eqref{eq:m0} instead.":

```latex
Two continuities must be kept apart here, since only one of them is proved. Continuity of the inner
root \emph{in its belief summaries} $(\hat v,\pi)$ follows from \eqref{eq:m0}. Continuity of the
\emph{composition} $k \mapsto (\hat v,\pi) \mapsto P$ in the cutoff vector is what the clause above
retains as an assumption: the $k$-dependence runs through the conditioning rather than through the
pricing map, and no step derives it. Remark~\ref{rem:A6record} records that composition measured
discontinuous at the implemented calibration, at the same loci and by the same checks, so this
clause carries adverse applicability evidence of its own. No label moves on that:
Assumption~\ref{asm:A5} is a hypothesis, and no result below consumes its cutoff clause.
```

## Finding 1b — the spillover to D1, L1 and L2. REJECTED.

GPT: *"That affects every row that literally carries full A5, even where its proof only needs a
narrower fixed-point or version-pinning property."* The concessive half of that sentence is the
answer, and the record confirms it clause by clause.

- **D1** — `threads/thread1_turn2_answer.md:8`: "Well-defined prices. A5 holds, so every pooled or
  flagged public history used below has a unique competitive price." Uniqueness. Its WHERE IT FAILS
  4 (`:85`) confirms the concern is a price-*selection* rule, not continuity.
- **L2** — `threads/thread1_turn2_answer.md:244`: "Unique flagged price. A5 holds, so the flagged
  competitive-pricing map has one fixed point at every on-path flagged information set." Uniqueness
  again; `:449` and `:476` confirm the same.
- **L1** — the card row itself (`MODEL_CARD.md:517`) glosses the citation: "A5 (which pins *the*
  version of $\mathbb E[Y\mid\mathcal I]$)". Version-pinning.

None of the three consumes the cutoff-continuity clause, and the A5 block already carries the
release for what they do consume: "Where a proof cites A5 for existence or uniqueness, it may now
cite §4.1's $m_0\ge0$ instead" (`MODEL_CARD.md:242-243`). **No row text needs a touch.** The one
real residue is that the A5 block asserted the retained clause with no adjacent evidence note while
the card's own A6 note measures that very family jumping in $k$ — discharged by C-2 above, which is
also the substance of GPT's blocking repair 1.

---

## Finding 2 — the A(τ) note's lead sentence. UPHELD.

**The lead** (`MODEL_CARD.md:375-376`):

> *Evidence note added 2026-08-25 (ticket 33).* **At the implemented calibration the support
> condition FAILS — and it fails on the support, not on the derivative pattern.**

**Its own third bullet** (`MODEL_CARD.md:409-413`):

> **Derivative pattern — FAILS, and independently of the support.** $A_0' = A_1'$ holds at **0 of
> 180** nodes: $\lvert A_0'-A_1'\rvert\in[0.041,\,2.306]$ against a predicted $<10^{-10}$, with
> $A_0'\in[-2.146,\,2.374]$ against $A_1'\in[-0.014,\,0.429]$ …

**Is there a defensible narrow reading?** There is a defensible *intent*. The bite paragraph above
the note (`:363-367`) establishes that "**A($\tau$)'s entire remaining content is the support
condition**" — the derivative restrictions being equivalent, given a $\kappa$-invariant three-point
support, to two conservation laws the model delivers. On that reading the lead means "the failure is
attributable to the support clause, since the derivative clause is not independent content." But the
bullet's own four words — "**and independently of the support**" — destroy that reading, and the
bullet is what the check measured. `t2_atau_support_check.json` measures both: the support half at
0/180 and the derivative pattern at 0/180, each on its own gate. Both fail; the lead denies that one
of them is where the failure is. **The two sentences cannot stand together, exactly as GPT says.**

**What must be preserved that GPT's flatter wording drops.** The card's taxonomy is finer than
"both fail": $A_0'=A_1'$ fails independently, while the $A_{1/2}'=-2A'_\kappa$ residual "is exactly
$2\lvert A_0'\rvert$ and is recorded as **inherited** — a restatement of the support failure, not a
second piece of evidence" (`:413-415`). The repair adopts GPT's surviving sense, not GPT's sentence.

**Mechanic.** In-line dated amendment, not an appended correction. The defect *is* the lead
sentence; an appended note would leave a self-contradicting sentence at the top of the block, which
is precisely how a careful external reader hit it. The amendment carries its date and its audit
pointer in the note header, so it is not a silent rewrite. Numbers, bullets and verdict unchanged.

### DRAFTED REPAIR — card amendment C-3 (`MODEL_CARD.md:375-376`)

> *Evidence note added 2026-08-25 (ticket 33; **lead sentence corrected 2026-08-28** on re-review
> audit finding 2 — every number, bullet and verdict below is unchanged).* **At the implemented
> calibration A($\tau$) FAILS. The decisive representation failure is already established by the
> support condition alone; the derivative pattern also fails, and independently.** The support half
> carries the verdict because it is A($\tau$)'s entire remaining content (see the bite paragraph
> above); the derivative-pattern bullet is a second and independent failure, of which only the
> $A_{1/2}'$ residual is inherited from the support. *(The superseded lead read "it fails on the
> support, not on the derivative pattern", which the third bullet below contradicts on its own
> terms.)* The pooled cell's …

### DRAFTED REPAIR — section S-3 (`sections_v3/model_section.tex:466-467`)

Current:

```latex
At the implemented calibration the support condition \textbf{fails}, and it fails on the support, not
on the derivative pattern.
```

Replacement:

```latex
At the implemented calibration Assumption~\ref{asm:Atau} \textbf{fails}. The decisive representation
failure is already established by the support condition alone; the derivative pattern also fails, and
independently. The support half carries the verdict because it is the entire remaining content of
the restriction, and of the derivative-pattern failure only the $A_{1/2}'$ residual is inherited
from the support.
```

**Mirror sites (mechanical, not drafted):** `model_v4.tex:558`, `model_v4.md:428`.

---

## Findings 3–7 — the staleness cluster in the sections. UPHELD-WITH-SCOPE.

**The scope first, because it changes the class.** The sections were written against the 2026-08-27
card and checker-LANDed against it, by design. The in-house checker's own stamp verification
(`threads/2026-08-27_t4_sections_check.md`, inlined at bundle `:1657-1665`):

> **Stamps verified before checking.** `research/model_v4/MODEL_CARD.md` — header line 3: *"Version
> stamp: 2026-08-27 · A6 panel resolution (§5 A6/A3 evidence notes + §9 item 4) · commit
> `ae9caea`"*. **Matches the contract.** … Five of the six section files carry the same stamp in
> their headers.

And the bundle's delta narrative puts the corrections *after* that landing — event (f) is the
sections landing at `9a73bb7` with "**Verdict LAND: 0 WRONG, 13 MISCITED, 1 UNCHECKED, 14
OK-RESTRUCTURED**", and event (g) is 2026-08-28's curation, "the stamp this bundle is built
against", where "**Two card wordings were corrected**" (bundle `:265-284`).

So these are **not errors at the sections' own stamp**. They are staleness against a card that moved
one day later. GPT's "blocking WRONG" class is right about the *text as it now stands against the
controlling card* and wrong about the *sections having erred*. Every repair is pure transcription
from card texts that already passed verifier conformance — the transcription is the whole job, and
the numbers must be copied byte-for-byte.

### 3(a) — "$\mathcal T$ bit-identical". UPHELD.

Section (`model_section.tex:344-346`): "…its Hold-collapse face is measured clean, with pooled prices
within $4.4\times10^{-16}$ and $\Tmap$ bit-identical as $k_1$ sweeps to full collapse."

Card's 2026-08-28 curation note (`MODEL_CARD.md:306-308`):

> And "$\mathcal T$ bit-identical" holds for $U$ but not for $\mathcal T_2$, which moves
> $6.66\times10^{-16}$ (3 ulps) at the one $k_1$ where the price signature itself deviates most
> ($4.441\times10^{-16}$); invariance holds at the map's own root-finder resolution.

**DRAFTED REPAIR — section S-4** (`model_section.tex:344-346`):

```latex
The implemented menu is not in that class: Exit and Hold pool
perfectly in order flow, and its Hold-collapse face is measured clean, with pooled prices within
$4.441\times10^{-16}$ as $k_1$ sweeps to full collapse. The payoffs $U$ are bit-identical across
that sweep; $\Tmap_2$ is not, moving $6.66\times10^{-16}$ --- three ulps --- at the one $k_1$ where
the price signature itself deviates most, so the invariance holds at the map's own root-finder
resolution rather than bit for bit.
```

### 3(b) / Finding 6 — the belief-snap bracket qualifier. UPHELD.

Section (`model_section.tex:350-351`): "with the belief snap matching the predicted value to about
$10^{-8}$".

Card (`MODEL_CARD.md:301-305`):

> The belief snap matches the Step 9(b) prediction to $\sim10^{-8}$ at all three edges at the
> truncation/cancellation crossover bracket $10^{-8}$; at the probes' own $10^{-9}$ bracket the
> first edge still holds ($4.0\times10^{-8}$, Analyst A's "7–8 dp"), but the second and third are
> $1.2\times10^{-7}$ and $1.7\times10^{-7}$ — floating-point cancellation over a $10^{-9}$-wide
> sliver, not a gap in the prediction.

**DRAFTED REPAIR — section S-5** (`model_section.tex:350-351`), replacing "with the belief snap
matching the predicted value to about $10^{-8}$":

```latex
with the belief snap matching the predicted value to about $10^{-8}$ at all three edges at the
truncation-and-cancellation crossover bracket of $10^{-8}$ --- at the probes' own $10^{-9}$ bracket
the first edge still holds, at $4.0\times10^{-8}$, while the second and third are
$1.2\times10^{-7}$ and $1.7\times10^{-7}$, which is floating-point cancellation over a sliver
$10^{-9}$ wide and not a gap in the prediction ---
```

### 3(c) / Finding 4 — "analysis-grade, not curated executed checks". UPHELD.

Section (`model_section.tex:371-372`): "…probes `quality_reports/fixes/a6_panel_probes_2026-08-27/`,
which are analysis-grade and not curated executed checks."

Card's curation note (`MODEL_CARD.md:293-311`) supplies the replacement content, including the
carve-out that must travel with it ("The analytic weight bound … is **not** curated").

**DRAFTED REPAIR — section S-6** (`model_section.tex:366-372`), keeping through "…may still have
fixed points." and replacing the Records sentence:

```latex
The three decisive measurements are now curated executed checks, each with a JSON verdict beside its
script. \texttt{t2\_a6\_edge\_jump\_check} replays both panellists' routes at their own filed
brackets and reproduces the three $\Tmap_2$ jumps, which agree across routes to a relative
$1.3\times10^{-4}$, with controls at $2.8$--$3.6\times10^{-9}$ and the $\pm10^{-6}$ robustness
intact. \texttt{t2\_a6\_node15\_check} reproduces the $0.1647$ jump, the destroyed crossing
($+1.0\times10^{-7} \to -6.70\times10^{-2}$) and the edge fixed point to $1.06\times10^{-12}$.
\texttt{t2\_a6\_collapse\_face\_check} reproduces the pooled prices within $4.441\times10^{-16}$.
Every figure these checks touch reproduces; two wordings of the panel record were corrected and the
numbers were not. The analytic weight bound $\min(\kappa/2,\,1-\kappa)^{d+1}$ is \emph{not} curated,
since no probe computes it; what is curated is its measured counterpart, the jump entering the
adjacent-plan payoff difference undiminished. Records:
\texttt{threads/\allowbreak 2026-08-27\_A6\_\allowbreak panel\_substantiate.md} and
\texttt{threads/\allowbreak 2026-08-27\_A6\_\allowbreak panel\_defuse.md}; the analysis-grade probes
behind them at
\texttt{quality\_reports/\allowbreak fixes/\allowbreak a6\_panel\_probes\_\allowbreak 2026-08-27/};
and the curated checks at
\texttt{quality\_reports/\allowbreak fixes/\allowbreak t2\_a6\_\allowbreak edge\_jump\_check},
\texttt{t2\_a6\_\allowbreak node15\_check} and \texttt{t2\_a6\_\allowbreak collapse\_face\_check},
each with its \texttt{.py} and \texttt{.json}.
```

### 3(d) / Finding 5 — rem:A3record's "UNCHECKED beyond the one node probed". UPHELD.

Section (`model_section.tex:283-284`): "A candidate mechanical account of the four unresolved nodes
is on file and UNCHECKED beyond the one node probed…"

Card's sweep note (`MODEL_CARD.md:206-224`) supersedes it: "*Swept 2026-08-28 over the other three
nodes … the account **HOLDS at all three**.*" GPT is explicit that the existence-unresolved clause
must survive the replacement — "while retaining that existence remains unresolved" — and the card's
own closer does exactly that ("existence at these nodes stays neither claimed nor denied").

**DRAFTED REPAIR — section S-7** (`model_section.tex:283-290`). Open the passage without the
UNCHECKED clause, keep the existing $\kappa=0.15$ sentence and the recorded negative, then insert
the sweep and close as the card closes:

```latex
A candidate mechanical account of the four unresolved nodes is on file: at the $\kappa = 0.15$ node
one fixed point sits exactly on the edge where $U_H - U_V$ jumps through zero without crossing it,
and the panel's residuals, $3.06\times10^{-4}$ to $1.77\times10^{-3}$ at cutoff residuals of
$10^{-11}$ grade, bracket the recorded range exactly; the $k$-direction jump mechanism does
\emph{not} explain those nodes, and the panellist who proposed it recorded that negative himself.
That account has since been swept over the other three unresolved nodes under a pre-registered
three-way rule, and it holds at all three. At $(\kappa = 0.15,\ 0.075,\ 1)$ and
$(\kappa = 0.85,\ 0.075,\ 1)$ a located fixed point sits on an $n(s)$ cell edge --- at
$1.460178993$, offset about $10^{-13}$, where $10$ of the $30$ recheck seeds land, and at
$1.517932397$, offset about $10^{-12}$, reached by no seed and found only by the direct edge test
--- with $U_H - U_V$ again jumping through zero without crossing. Neither pin is its node's
achieving basin: their payoff residuals, $1.398\times10^{-3}$ and $1.314\times10^{-3}$, sit above
the recorded bests of $1.059\times10^{-3}$ and $3.061\times10^{-4}$, and each equals the larger
one-sided jump to at most $2.7\times10^{-4}$ relative. At $(\kappa = 0.85,\ 0.05,\ 5)$ no pin was
found at any candidate edge in $[1.29,\,2.11]$; the achieving basin's worst deviation instead sits
in the cell immediately above edge $1.583333333$, $0.0250\,\sigma_s$ from it, where the same jump
through zero occurs, at a deviation-to-jump ratio of $0.366$, inside the pre-registered factor of
three. Every pin is of the $n(s)$ family and the $\tau$-crossing pullbacks yielded none; the
distances of probe~5(b) replicate, at $0.0258/0.0437/0.0295\,\sigma_s$ against
$0.026/0.044/0.030$; and no node yields a second independent fixed point, so the residual bracket at
the first node does not recur. This is diagnostic evidence at one calibration, and existence at
these nodes stays neither claimed nor denied. No label moves on any of it: Assumption~\ref{asm:A3}
is a hypothesis, and Proposition~\ref{prop:P1} stays PROVED as a conditional. Records: the panel
files named in Remark~\ref{rem:A6record}, and
\texttt{quality\_reports/fixes/t2\_t34\_account\_sweep.py} with
\texttt{t2\_t34\_account\_sweep.json}.
```

### 3(e) / Finding 7 — the section stamps. UPHELD, with three sites that must NOT move.

**Six provenance headers to advance.** The orchestrator will advance the card stamp once more before
the sections are touched, so these carry a placeholder:

| # | Site | Current | Replacement |
|---|---|---|---|
| 1 | `model_section.tex:4-5` | `version stamp 2026-08-27` / `(A6 panel resolution, commit ae9caea).` | `version stamp 2026-08-28` / `(re-review audit repairs, commit <pending-orchestrator-hash>).` |
| 2 | `theorem_section.tex:4-5` | same | same |
| 3 | `proofs_core_lemmas.tex:6-7` | same | same |
| 4 | `proofs_existence.tex:5-6` | `stamp 2026-08-27 (A6 panel resolution, commit ae9caea), section 6 P1 row` | `stamp 2026-08-28 (re-review audit repairs, commit <pending-orchestrator-hash>), section 6 P1 row` |
| 5 | `proofs_theorem_ge.tex:5-6` | same as 1 | same as 1 |
| 6 | `v3_macros.tex:3` | `(card stamp 2026-08-27).` | `(card stamp 2026-08-28).` |

**Three sites that stay 2026-08-27 — dated facts, not provenance.** Moving them would falsify the
record:

- `v3_macros.tex:26` — "107 at the checker's **2026-08-27 delta-pass count**"; a dated count.
- `model_section.tex:369-371` — the panel **filenames**
  `2026-08-27_A6_panel_substantiate.md` / `_defuse.md` and the probe directory
  `a6_panel_probes_2026-08-27/`; these are paths.
- `theorem_section.tex:447` and `:462` — "answered in substance **on 2026-08-27**"; a dated event.

`proofs_section.tex` (6 lines of `\input` plumbing) and `standalone_v3.tex` carry no stamp — no
action, as the in-house checker already recorded.

---

## Finding 8 — L2's A7 failure-boundary scoping. UPHELD; converges with in-house M-8.

**GPT's site is wrong; its substance is right.** GPT attributes the phrase to "§7.2", the results
section. It is in the **model** section: `sections_v3/model_section.tex:412-413`:

> The failure boundary **for the on-path form** is a binding stake cap, quantized stakes, a composed
> target repeating values across Voice-plan switches, $\Omega = 0$, and policy dependence when the
> condition is stated only at one equilibrium's cutoffs.

The card states the same list unscoped, immediately after its A7-J sentence (`MODEL_CARD.md:312-323`
and the A7 note it heads).

**The convergence is exact.** `threads/2026-08-27_t4_sections_check.md:325-332`, finding M-8:

> **The one difference:** the card states the failure-boundary list unscoped, immediately after the
> A7-J sentence. The section writes *"The failure boundary **for the on-path form** is …"* (line
> 412). Two of the five items (a binding stake cap, quantized stakes) break both forms, so the
> scoping narrows what the card asserts about A7-J.
>
> **Verdict: MISCITED** — an attribution narrowed, not a clause dropped. Nothing consumes the
> failure boundary … **Minimal fix:** delete "for the on-path form".

GPT reached the same conclusion independently, including the same two counterexample items. **The
in-house fix was recorded as non-blocking and never landed** — the phrase is still at `:413`. Two
independent readers now converge on it, which is reason enough to land it.

### DRAFTED REPAIR — section S-8 (`sections_v3/model_section.tex:412-413`)

```latex
The failure boundary is a binding stake cap, quantized stakes, a composed target repeating values
across Voice-plan switches, $\Omega = 0$, and policy dependence when the condition is stated only at
one equilibrium's cutoffs.
```

**M-8's second residue** (the dropped `SURVIVES WITH REPAIRS` attack verdict and the
`proofs/A7_construction.md` / `proofs/A7_attack_verdict.md` pointers) remains on file as
non-blocking. GPT did not raise it. Orchestrator's discretion; not queued here.

---

## Finding 9 — the L3 "Step 19" pointer. NARROWED. No repair.

**The card's anchor targets the proof file, and it resolves.** `proofs/L3_proof.md:455`:

> **Step 19 (a reading of $\bar\pi$ that must be fixed, or L3 is vacuous).**

That is the degeneracy argument, and the file carries it under that number. Both card citations name
the file explicitly:

- `MODEL_CARD.md:132` — "flagged independently by both writers (`proofs/L4_proof.md` head block;
  **`proofs/L3_proof.md` Step 19**)".
- `MODEL_CARD.md:471-472` — "(Support-point form, per the binding $\bar\pi$ ruling; the identity
  branch $\bar\pi = \bar\pi_{\mathrm{pr}}$ is excluded as degenerate, **`proofs/L3_proof.md`
  Step 19**.)"

**The card is correct as written.** GPT's own phrasing concedes the scope — "The claim is present,
but that *in-paper* step citation does not resolve" — so what it has found is a card→paper mapping
gap, not a miscitation.

**And no paper citation dangles.** A sweep of `sections_v3/` for "Step 19" returns exactly one hit,
`proofs_existence.tex:918`, which is P1's own Step 19 on A8 and cell mass — unrelated. The paper
nowhere points a reader at an L3 Step 19. The material is present in the paper at
`proofs_core_lemmas.tex:697` ff., folded into L3's Step 15, as GPT says.

**Repair: none.** Editing the card would break a resolving anchor; adding a parenthetical to the
paper's Step 15 would document a mapping the paper never asserts. At most this warrants a LaTeX
comment beside Step 15, and the brief's preference for none is the right call.

---

## Finding 10 — O-1's $\approx0.29$ vs $0.343$. REJECTED-AS-DISCREPANCY.

GPT: *"the card itself contains an unresolved O-1 numerical discrepancy: approximately $0.29$ in the
§4.4 gloss versus approximately $0.343$ in §9 and the paper. The bundle does not establish whether
these are distinct cuts or inconsistent descriptions."*

**The record establishes it, and did so before the card was written.** `HANDOFF_sign.md:76-85`:

> **One thing this run adds.** The committed record reports the sign at four grid points and rounds
> the cut to "≈0.29". That 0.29 is simply the largest grid point at which failure was confirmed —
> **the crossing itself was never located.** Bisecting on `k_D` puts it at `k_D* = 1.28618`, i.e.
>
> > **Ω\* = 0.3428.** Attenuation fails below it, holds above it.
>
> The correct condition is therefore **Ω < 0.343**, not Ω < 0.29. … anything that quotes "≈0.29" as
> the boundary should quote 0.343 instead, and should say it came from this run.

They are the same cut at two resolutions: a grid point and the bisection-located crossing. Not
distinct cuts, not inconsistent descriptions — one superseded by the other, with the supersession on
file and dated.

**And the card's §4 cell does not compete with §9.** `MODEL_CARD.md:130` reads: "**$\Omega$ is
draft_v2's $\omega_P$ — the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the $\approx 0.29$ cut are
all $\Omega$-type**". That is a *historical identification of quantity type* — it tells a reader
that draft_v2-era numbers under those names are $\Omega$-type objects. It states no boundary. §9
item 3 states the boundary, and states it at 0.343 (`:596`). `theorem_section.tex:369` carries the
same, at 0.343, and no `0.29` appears anywhere in `sections_v3/`.

**Optional card amendment C-4, and my reasoning for flagging it.** A strong external reader read the
§4 cell as a competing boundary claim. That is direct evidence the cell reads ambiguously in
isolation, and the fix is a ticket-32-class wording clarification carrying no label content. I
recommend it as **optional, low priority** — the cell is not wrong, and there is a real
over-editing risk in annotating a glossary row that is doing its job.

### DRAFTED REPAIR — card amendment C-4 (OPTIONAL) (`MODEL_CARD.md:130`)

Append inside the notes cell:

> (The $\approx 0.29$ is the largest **grid point** at which failure was confirmed in the draft_v2-era
> record, not a located boundary; the crossing itself was found by bisection at
> $\Omega^\star = 0.3428$, which is the number §9 item 3 and `HANDOFF_sign.md` §3 carry. This cell
> identifies the quantity's *type* and states no boundary.)

---

## Finding 11 — proofs by opening, JSONs as extracts. REJECTED.

Not a record gap; the bundle's declared design, stated twice in the bundle's own voice.

Bundle `:3471-3477`:

> **The proofs are represented by their openings only.** `sections_v3/` carries three proof files
> totalling 2,880 lines — full proofs of D1, L1, L2, L3, L4, P1, T1 and C1. **Inlining them would
> roughly double this bundle**, so §7.3 gives, for each of the eight proofs, its `\begin{proof}`
> line through the end of its first step … **The full files are in the repository** … If an opening
> plus the statement in §7.1 is not enough to rule on a result, that is an **UNCHECKED** finding and
> should be returned as one.

Bundle `:73-76` declares the same for the JSONs: `(extract)` "used only in §6, for the check JSONs,
which are far too large to paste … Treat an extract as a pointer to the committed file."

GPT did exactly what the bundle asked — returned UNCHECKED rather than ruling. That is the protocol
working, not a defect. **No repair.** If a future courier round needs line-by-line proof review, the
answer is a different bundle scope, not a change to the record.

## Finding 12 — no complete witness for the full P1 hypothesis set. NARROWED (agreement).

GPT: *"no complete witness in the bundle satisfies A3, A6, A7-J, continuation-cost equivalence, and
the other P1 hypotheses jointly over the claimed $\kappa$ domain."*

This is the card's own position, in the card's own words. §9 item 2 (`MODEL_CARD.md:581-587`):

> **Whether an equilibrium in which the blockholder chooses the fully separating plan exists on a
> given calibration — OPEN, and P1-adjacent.** … the burden did not disappear when ticket 24
> resolved satisfiability; it **moved** to incentive compatibility, which P1 does not settle …
> Relatedly, P1 does not claim that an equilibrium satisfying A8 exists.

And §9 item 4 records A6's continuity as answered-in-substance with the open remainder scoped. The
P1 row itself carries the same honesty on the numerical side ("**UNCHECKED**: existence at those four
nodes is neither claimed nor denied"). **Agreement, not a finding. No repair.**

## Finding 13 — the continuum-face lemma. NARROWED (agreement).

GPT: *"the continuum-face lemma is expressly a single-pass panel derivation and has not passed the
two-pass gate. It may be cited as an analytic observation, not as a proved extension of P1."*

The card already labels it exactly so (`MODEL_CARD.md:264-265`): "(continuum-face lemma — single-pass
panel derivation, **not gate-checked**)". `model_section.tex:343-344` transcribes it: "a
continuum-face lemma derived in a single panel pass and \emph{not} gate-checked." **Agreement. No
repair.**

---

## Finding 14 — the eleven numerical check requests. NARROWED; none executed here.

**None is a repair, and none is executed by this audit.** They are a wish list. Three observations
the orchestrator should have on file.

**(a) The A6 request is already satisfied, and GPT's own predictions prove it.** Its request reads
"First, update the paper record and rerun the three curated checks", with predicted magnitudes:
baseline jumps $0.00633$, $0.0109$, $0.0283$; controls below $4\times10^{-9}$; the $\kappa=0.15$ jump
$\approx0.1647$; collapse-face pooled-price spread at most $4.441\times10^{-16}$; collapse-face
$\mathcal T_2$ spread $\approx6.66\times10^{-16}$, **not zero**. Those are the card's curated numbers
(`MODEL_CARD.md:293-308`), read back from the bundle. The rerun is `t2_a6_edge_jump_check`,
`t2_a6_node15_check` and `t2_a6_collapse_face_check`, all committed. What survives of the request is
its *first four words* — update the paper record — which is repairs S-4 to S-6 above. Its second
half (implement the replacement existence route and require no edge discontinuity above $10^{-10}$)
is a research programme, not a check.

**(b) The per-result identity requests overlap committed checks.** Present in
`quality_reports/fixes/`, each with a `.py` and a `.json`: `t2_d1_check`, `t2_l1_check`,
`t2_l2_check`, `t2_l3_check`, `t2_l4_check`, `t2_t1_check`, `t2_p1_check` (plus
`t2_p1_fournode_recheck`), `t2_c1_region_check`, `t2_atau_support_check`. I state this at
**existence level only**: I did not read the scripts, so I do not certify that any committed check
covers a given request's exact grid, tolerance or gate. Before commissioning anything from GPT's
list, diff the request against the script.

**(c) One legitimate follow-up candidate: the dedicated A3 check.** GPT's A3 request asks for "a
dedicated executed A3 check … At the first locus, evaluate $U_V-U_H$ on a dense $s$ grid for every
$k_2$ offset from $10^{-9}$ through $2\times10^{-2}$", predicting exactly three strict sign changes
near $1.5754434$, $1.5833333$, $1.5902426$, middle excursions between $2.4\times10^{-4}$ and
$2.8\times10^{-4}$, and the H,V,H,V argmax order; and a reproduced Voice-to-Hold reversal at the
second locus. This is the same curation move the lane already performed for A6 on 2026-08-28: the A3
finding currently rests on panel records rather than a curated `t2_` check, which is precisely the
gap the A6 curation closed for its own findings. The predictions are the card's A3-note numbers
(`MODEL_CARD.md:185-195`), so the check would be pre-registered by construction. **Recorded as
on-file-not-started.** It is a NUMERICAL-class confirmation of an existing applicability finding, not
a label question — nothing in the current record depends on running it.

**The remaining requests — recorded, not committed to the lane:** P1's "construct and commit at least
one nontrivial menu/calibration satisfying the entire P1 hypothesis set" (this is §9 item 2's open
question, restated as a task); C1's certified-neighbourhood bounds ($\sup L_{\mathcal R}<1$,
$\inf\eta_r>0$, target slack above $0.05$ against the current pointwise minimum $0.0595$); L3's
synthetic A($\tau$)-satisfying laws; A($\tau$)'s three alternative menus at $H\in\{5,10,20\}$;
D1/L1/L2/L4/T1's identity sweeps.

---

# REPAIR QUEUE

Nothing here moves a label. Nothing here writes to `LABEL_LEDGER.md`. Card items are landed record
and carry dated markers; section items are draft text conformed to the controlling card.

## (i) Card amendments — 3 required, 1 optional

| ID | Site | Mechanic | Drafted at |
|---|---|---|---|
| **C-1** | `MODEL_CARD.md:521`, P1 row, the "A5 is not assumed" sentence | in-place clause correction at regeneration, audit as traceable finding (ticket-32 precedent) | Finding 1 |
| **C-2** | `MODEL_CARD.md`, A5 block, append after `:243` | dated evidence note, original clause left standing (A6-curation precedent) | Finding 1 |
| **C-3** | `MODEL_CARD.md:375-376`, A(τ) note lead | in-line dated amendment; note header records the correction; numbers and bullets untouched | Finding 2 |
| **C-4** *(optional)* | `MODEL_CARD.md:130`, $\Omega$ symbol-table cell | parenthetical addition | Finding 10 |

C-1 discharges GPT's blocking repair 1 in the row; C-2 discharges it in the assumption block and
supplies the missing evidence adjacency; C-3 discharges blocking repair 2.

## (ii) Section repairs — 9 sites

| ID | Site | What | Drafted at |
|---|---|---|---|
| **S-1** | `theorem_section.tex:258-262` | disambiguate the A5 continuity reading; name the underived cutoff clause; point at `rem:A6record` | Finding 1 |
| **S-2** | `model_section.tex`, append after `:316` | give the A5 paragraph its record adjacency | Finding 1 |
| **S-3** | `model_section.tex:466-467` | A(τ) lead sentence | Finding 2 |
| **S-4** | `model_section.tex:344-346` | "$\Tmap$ bit-identical" → $U$ bit-identical, $\Tmap_2$ moves $6.66\times10^{-16}$ (3 ulps); spread $4.441\times10^{-16}$ | Finding 3(a) |
| **S-5** | `model_section.tex:350-351` | belief-snap bracket qualifier | Finding 3(b) |
| **S-6** | `model_section.tex:366-372` | curated `t2_a6_*` records + the uncurated weight-bound carve-out | Finding 3(c) |
| **S-7** | `model_section.tex:283-290` | drop "UNCHECKED beyond the one node probed"; transcribe the three-node sweep; keep existence unresolved | Finding 3(d) |
| **S-8** | `model_section.tex:412-413` | delete "for the on-path form" | Finding 8 |
| **S-9** | six provenance headers | advance to `2026-08-28` / `<pending-orchestrator-hash>`; **do not touch** `v3_macros.tex:26`, `model_section.tex:369-371`, `theorem_section.tex:447` and `:462` | Finding 3(e) |

Order: apply C-1 to C-3 and re-stamp the card first, then S-1 to S-9 against the new stamp, then fill
`<pending-orchestrator-hash>`.

## (iii) Mechanical follow-ons — listed, not drafted

- **Mirrors of C-1:** `model_v4.tex:874-875` and `model_v4.md:559` carry the P1 row's A5 sentence
  verbatim.
- **Mirrors of C-3:** `model_v4.tex:558` and `model_v4.md:428` carry the A(τ) lead verbatim.
- Card stamp advance; `model_v4.md`/`.tex` regeneration; PDF rebuild; `sections_v3/standalone_v3.pdf`
  rebuild; session log.
- **A fresh verifier pass on the amended sentences**, per the 2026-08-28 precedent (two independent
  passes, amendment sentences conformed). C-1 and C-2 touch a PROVED row's hypothesis gloss and
  deserve it most.

## (iv) No-action items, with reasons

| Item | Reason |
|---|---|
| GPT's spillover to D1, L1, L2 rows | their proofs consume A5 for unique price / one flagged fixed point / version-pinning; none consumes the cutoff clause; the A5 block's release sentence already covers them |
| L3 "Step 19" pointer (card) | `proofs/L3_proof.md:455` exists and carries the degeneracy argument; both card citations name the file and resolve |
| L3 Step 19 (paper) | no paper citation dangles — the only "Step 19" in `sections_v3/` is P1's own, at `proofs_existence.tex:918` |
| O-1 $\approx0.29$ vs $0.343$ | pre-adjudicated in `HANDOFF_sign.md` §3; §4 cell identifies a quantity type, §9 item 3 states the boundary at 0.343; no `0.29` in `sections_v3/` |
| proofs-by-opening / JSON extracts | the bundle's declared design (bundle §1 and §7.3); GPT returned UNCHECKED as instructed |
| no complete P1 witness | the card's own §9 items 2 and 4 |
| continuum-face lemma not gate-checked | the card and the section already say exactly that |
| M-8's dropped attack-verdict pointers | non-blocking in-house residue; GPT did not raise it; orchestrator's discretion |
| all eleven numerical check requests | none is a repair; A6's is already satisfied by `t2_a6_*`; A3's recorded on-file-not-started |

---

## Where I differ from GPT's classification

1. **"WRONG" 3, 4 and 5 are staleness by design, not error at the sections' own stamp.** The
   sections were written and checker-LANDed against `ae9caea` (2026-08-27); the corrections they
   lack landed at `926f58c` the next day. The repairs are required — the sections must not ship
   against a superseded card — but the class is UPHELD-WITH-SCOPE, and no one wrote anything false
   at the time of writing.
2. **MISCITED b (L3 Step 19) resolves on the card and warrants no repair.** GPT's own wording
   concedes the scope; the card's anchor targets the proof file, which has the step.
3. **T1's O-1 UNCHECKED is pre-adjudicated, not open.** `HANDOFF_sign.md` §3 reconciled 0.29 and
   0.343 before the card was written; the §4 cell states no boundary.
4. **"Affects every row that literally carries full A5" is over-broad.** No result row consumes the
   cutoff-continuity clause; three primary quotes settle it, and GPT's own concessive clause
   anticipates the answer.
5. **On "WRONG" 1 I am harder on the card than the brief anticipated.** The brief suggested the card
   "ALREADY distinguishes the two continuities." It does not — the A5 block names only the cutoff
   continuity, so the P1 row's "(see A5)" pointer makes the clause wrong rather than loose. UPHELD,
   not NARROWED. The consequence is still only wording, and no label moves.
6. **GPT's site for MISCITED a is wrong.** The phrase is in `model_section.tex:413`, not the results
   section. The substance is right and converges with in-house M-8.
