# Session log — 2026-08-28 — standing follow-ups + GPT re-review bundle

**Invocation.** Same session as the 2026-08-27 ticket-08 log (the date rolled over mid-session;
new artifacts are dated 2026-08-28). Austin, asked "what's next?", answered **"both"** to the two
offered items: (1) the two standing theory-lane follow-ups from the R-series record, (2) the
paste-ready GPT re-review bundle. Routing unchanged: Opus builders and verifiers
(finder ≠ verifier, verifiers briefed to refute), orchestrator applies card text and runs git.

**Follow-up 1 — A6 decisive probes curated into executed t2 checks: DONE, commit `926f58c`.**
Three checks under `quality_reports/fixes/`, JSON verdicts beside the scripts, all deterministic
(verifier re-ran: REPRODUCE bit-exact modulo timing):
- `t2_a6_edge_jump_check` — both panellists' routes replayed at their own filed brackets; the
  three 𝒯₂ jumps 6.33e-3 / 1.09e-2 / 2.83e-2 agree across routes to 1.3e-4 relative; controls
  2.8–3.6e-9; ±1e-6 robustness intact. 20 gates, 0 failing.
- `t2_a6_node15_check` — jump 0.1647, destroyed diagonal crossing, edge fixed point to 1.06e-12.
- `t2_a6_collapse_face_check` — pooled prices within 4.441e-16 on the Hold-collapse face.
**Two card wordings corrected, the numbers intact** (recorded in the checks'
`known_discrepancies`, not smoothed): the belief snap matches the Step 9(b) prediction to ~1e-8
at all three edges only at the 1e-8 crossover bracket (at the probes' own 1e-9 bracket the first
edge still holds at 4.0e-8; the second and third are 1.2e-7 and 1.7e-7 — floating-point
cancellation over the sliver, not a prediction gap); and "𝒯 bit-identical" holds for U but not
for 𝒯₂, which moves 6.66e-16 = 3 ulps at the k₁ where the price signature deviates most. The
analytic weight bound is not curated (no probe computes it); its measured counterpart is. A
README route mis-attribution in the probe suite was found and recorded (B's jump route is
`a6_B_baseline.py`, not `a6_B_sweep.py` part (B)).

**Follow-up 2 — ticket-34 candidate account swept over its other three nodes: DONE, same
commit.** `t2_t34_account_sweep.py`/`.json`, pre-registered three-way rule (thresholds declared
before any node ran, calibrated on node 15 and validated there). **The account HOLDS at all
three**: pinned non-achieving fixed points on n(s) cell edges at (κ=0.15, 0.075, 1) (10 of 30
seeds in that basin) and (κ=0.85, 0.075, 1) (reached by no seed — found only by the direct edge
test), each with U_H − U_V jumping through zero without crossing; at (κ=0.85, 0.05, 5) no pin at
any candidate edge, but the achieving basin's worst deviation sits in the cell immediately above
an edge carrying the same jump (ratio 0.366, inside the pre-registered factor of 3). Node 15's
residual bracket does not recur (no node yields a second independent fixed point); the proximity
negative replicates at all three; every pin is n(s)-family — the τ-crossing pullbacks yielded
none, partially closing a6_B_findings §7's UNCHECKED item. Diagnostic evidence only; existence at
those nodes stays neither claimed nor denied; **no label moves anywhere in this batch**.

**Verification.** Two fresh Opus verifiers, briefed to refute. Both checks PASSed on
reproduction, gate quality, pre-registration, and provenance (the sweep verifier re-derived
probe 5(b)'s distances independently; the A6 verifier traced every constant to its filed source).
Both FAILed the builders' first drafted card sentences — five hard mismatches total (a wrong
numeral 7.1e-16 for a measured 6.66e-16, an over-broad "only", a dropped "deviates most"
qualifier, an understated 2.5e-4 for a measured 2.68e-4, and a misdescription of what criterion
(ii) rests on) — all fixed in one repair round per builder, conformance checked against the
verifiers' explicit prescriptions. The A6 verifier's re-run had rewritten three JSONs in place
(timing fields only); the builder originals were restored as the committed record. Two
tautological integrity clauses and two docstring overclaims in the sweep script were fixed as
comment-only edits; the JSON was not re-generated (verifier had already reproduced it bit-exact).

**Card write (orchestrator, quiet window, serialized).** One batched edit: stamp advanced to
**2026-08-28 · follow-up curation · `926f58c`** (hash filled in `998b88e`), provenance sentence,
§5 A6 curation note + §5 A3 sweep note (both agent sentences applied verbatim after verifier
conformance; two unicode tokens normalized to the card's math register), §9 item 4's follow-up
line updated (curation no longer "not started"). Mirrors synced by the mirror agent (same five
sites, tex in note macros), PDF regenerated 24 pp. **Gate correction on the record**: the mirror
agent discovered its earlier "Overfull hbox 0" greps were a shell-quoting false negative — the
true count had been 2 throughout (two pre-existing 1.43pt boxes from bold SIMPLIFY in the note's
draft_v2 comparison table, predating this session's content). Authorized fix: verdict column
0.12→0.13\textwidth with compensating trim; all gate counts now genuinely zero with `grep -F`.

**GPT re-review bundle.** `research/model_v4/threads/gpt_rereview_bundle_2026-08-28.md`,
assembled against stamp `926f58c` on the previous bundle's skeleton: the ask (demote-only rule
restated), the delta narrative since GPT's 2026-08-22 review (its own audit included — accepted
vs rejected findings), the full card and ledger, the primary records (P1 retry pass +
re-derivation, both A6 panel reports, the ticket-08 checker report), extracted JSON verdicts of
the six live t2 checks, and the theory sections (statements in full; proofs by opening + pointer).
Austin couriers it once; the paste is the next human step.

**Commits this session (v4-theory, pushed):** `926f58c` (follow-ups: 8 t2 files + card + mirrors
+ PDF); `998b88e` (stamp hash fill); `3af3c7c` (bundle + this log).

**Standing after this session.** Open theory-lane follow-up remaining: gate-check the
continuum-face lemma only if it is ever promoted. Card wording item still parked for a quiet
window: the 𝒮(k) selection-set vs bare-𝒮 collision. The critical path to draft_v3 is unchanged:
Austin's E2-spec approval → E3–E7 → tickets 16/17 → 18.
