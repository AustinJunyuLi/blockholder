# Fix-round recheck — T1, batch-2 audit (ticket 27)

File under recheck: `research/model_v4/proofs/T1_proof.md` (1050 lines, post-fix). Not edited.
Audit closed against: `threads/2026-08-21_batch2_T1_proofread_audit.md` (FAIL at Step 15 + R1–R9).

Checker: fresh Opus, theory lane, 2026-08-21, repo `blockholder_v4_theory` @ `v4-theory`. I wrote
neither the file, nor the audit, nor the fix. No git was run. Read in full: the audit, the fixed
file, `MODEL_CARD.md` (§2, §4.1–4.6, §5, §6, §7, §8, §9), and — for transcription checking only —
`proofs/L4_proof.md`'s A(br) block, CLAIM items, Step 19 and Step 20.

Classes follow the audit's: **WRONG/FAIL** blocks · **MISCITED** never blocks (claim stands,
citation does not) · **REPAIR** never blocks · **UNCHECKED** never blocks · **OBSERVATION**.

---

## VERDICT

**REOPEN — for one short citation round, not a bounce.**

- **T1-F1 is discharged.** H18 delivers everything Step 15 signs, the step's scope claim is true,
  and no boxed display moved. There is **no new FAIL** and **no new WRONG** anywhere in the file.
- **But four new items sit in text the fix itself wrote** (two MISCITED, two REPAIR). The stop
  condition for this round is "a fresh checker finds nothing new", and that is not satisfied.
  Every one is a one-clause fix; none touches an argument. Recommended handling: a single
  edit pass, then close — do not re-run the proof-read.

| # | Item | Class | Where | Blocks? |
|---|---|---|---|---|
| N1 | noise-mark law cited to card §4.2; it is §4.1's $\bar z$ row | MISCITED | line 293 (Step 5, R2 text) | no |
| N2 | $\bar\pi(\tau')\le\bar\pi(\tau)$ attributed to H14 leg 2 — leg 2 is about the **share** $\bar\pi_{\mathrm{pr}}$ | MISCITED | lines 772–774 (WHERE IT FAILS 4c, R6 text); root at lines 163–164 (H14) | no |
| N3 | cross-policy $\lvert C_h\rvert$ comparison with no (br-v)/H17 citation | REPAIR | lines 772–774 (same sentence) | no |
| N4 | "Nothing in **H1–H15** signs $C_T$" — the file now runs to H18 | REPAIR | lines 661–662 (Step 22) | no |

Two OBSERVATIONS (O1, O2) below. **No label moves: T1 remains CONJECTURE.** This is the
proof-read half only.

---

## 1. The FAIL — does H18 deliver what Step 15 signs?

**Verdict: YES, on all four counts. T1-F1 CLOSED.**

Step 15 (lines 445–484) signs four things. Checked one at a time against H18 (lines 210–235):

| Step 15 needs | H18 supplies | OK |
|---|---|---|
| $\Omega_{r_\tau}$ **exists** | clause 1: $t\mapsto\Omega(t,T)$ is $C^1$ on $I_\tau$, stated in both the $t$ and the $r_\tau=-t$ coordinate | ✓ |
| $\partial_{r_\tau}\mathcal S_P$ **exists** | clause 1 gives $C^1$ of $t\mapsto\partial_\kappa M_P(\kappa,t,T)$; clause 2 gives $\mathcal S_P>0$, so $\partial_\kappa M_P\ne0$ and $\lvert\cdot\rvert$ is differentiable there; Step 6's second consequence then transfers. The step names clause 1 as "the antecedent Step 6's second consequence now supplies" — which is the exact gap the audit found | ✓ |
| **interiority** $1-\Omega>0$ on the interval | clause 2: $\Omega(t,T)\in(0,1)$ at every $t\in I_\tau$, i.e. H2 extended off the two compared policies | ✓ |
| **A(br) on every pair in the interval** | clause 3: H13's A(br) *and* H17's (br-v) at every pair $t'<t$ in $I_\tau$ | ✓ |

Two things I attacked and could not break:

1. **Does clause 3 really carry A($\tau$) along?** Step 15 reads H14 leg 3 at every interior pair,
   and L4's leg 3 needs L3 *plus* A($\tau$)'s monotone $\lvert C_h\rvert$ *plus* A(br), not A(br)
   alone. It holds: A(br)'s own clause (br-i) asserts A($\tau$)'s representation at both policies
   of the pair (verified verbatim in `L4_proof.md` lines 36–38), and T1's H11 is headed
   "= A(br) clause (br-i)". Extending A(br) to every pair therefore extends H11 to every point of
   $I_\tau$. H12 (L3) is not pair-specific. No gap.
2. **Are the orientations right?** $r_\tau=-t$, higher $r_\tau$ = tighter (card §4.5 carries
   $r_\tau=-\tau$ as a strictness coordinate — cited correctly). Leg 1: lower $t$ raises $\Omega$
   ⟹ $\Omega$ weakly increasing in $r_\tau$ ⟹ $\Omega_{r_\tau}\ge0$ **given** differentiability
   (the step says exactly that, in bold). Leg 3: lower $t$ lowers $\mathcal S_P$ ⟹ $\mathcal S_P$
   weakly decreasing in $r_\tau$ ⟹ $\partial_{r_\tau}\mathcal S_P\le0$. Then
   $-\Omega_{r_\tau}\mathcal S_P\le0$ and $(1-\Omega)\partial_{r_\tau}\mathcal S_P\le0$; the sum is
   nonpositive. Monotone-plus-differentiable ⟹ signed derivative is used, not asserted. Correct.

**H18's card grounding checks out.** Card §4.1's $\tau$ row places no discreteness ✓ (so the
"continuous domain is not a smooth map" framing is right, and it is a *sharper* reason than H15's,
as claimed). Card §4.2 requires only weak $\partial_sB_j\ge0$ ✓, and the A7′ row constrains only
the **composed terminal target** $s\mapsto b^*_{j(s)}(s)$, never the interior date $B_j(s,H-T)$ ✓
— so the atom that kills $\Omega_{r_\tau}$ is genuinely permitted, exactly as H18 says.
$I_\tau\subset(b_0,\infty)$ respects card §4.1's maintained $b_0<\tau$ ✓.

**Scope claim is honest — checked, not taken.** Grepped every mention of Step 15 in the file:
lines 233, 235 (H18's own text), 445–484 (the step), 750 (WHERE IT FAILS 4, a failure aside),
831 (LABEL CLAIMED 3), 941 (NOTATION DELTA), 1012–1016 (NOT CLAIMED 13), 1031/1041 (changelog).
**No proof step cites Step 15.** Part B's conclusion is Step 13, finite-difference throughout;
Parts A and C never mention $r_\tau$. The scope paragraph (lines 480–484) is accurate.

**H18 does no work outside Step 15.** Its only appearances beyond the step are the two-word aside
in WHERE IT FAILS 4 ("or, with H18, in $r_\tau$"), the $I_\tau$ notation row, LABEL CLAIMED and
NOT CLAIMED 13. None of those is a derivation. ✓

**The boxed displays are untouched in substance.** Four displays carry `\boxed` — Step 6 (line
310), Step 13 (429), Step 18 (554), Step 20 (599). Each matches, symbol for symbol, the version the
audit transcribed and passed (audit §2 Step 6, §3 Step 13, §4 Steps 18 and 20). Step 7's TV
identity (line 330–332) and Step 21a's $W_TC_T=\exp(\int\rho)$ (line 618) likewise unchanged.
See O1 for a wording nit in the changelog's own count.

---

## 2. Repair-by-repair, against the audit's findings

**T1-R1 (Step 2) — DONE, correctly.** The differentiation is now licensed by H4 and H6 (two
factors constant in $\kappa$ ⟹ $\Delta^{\mathrm{act}}$ is an affine image of $M_P$) plus H7 on
$M_P$; boundedness is explicitly named as *not* what licenses it (lines 256–258), which is the
audit's point made out loud. Non-circularity of the forward references to Steps 3 and 5 is stated
and is true: Step 3 rests on H4, Step 5 on H5/H9/H16/A1, neither on Step 2. The three-term display
survives, correctly relabelled as bookkeeping.

**T1-R2 (Step 5) — DONE, with one miscitation (N1).** H16 exists (lines 183–189), is cited at
Steps 3 and 5, and is faithful to card §2 bullet 2 — including the card's own instruction, which I
verified verbatim: *"L2 Steps 3 and 6 fail without this; cite it as a numbered hypothesis."* The
independence-of-L2 framing (Step 5 derives H6, it does not invoke L2) is correct.

> **N1 (MISCITED).** Line 293: *"$\kappa$ appears in exactly one row of the card, the $z_d$
> noise-mark law of **§4.2**"*. The row that carries $\kappa$ is **§4.1's $\bar z$ row**
> ($\Pr(z_d=0)=1-\kappa$, $\Pr(z_d=\pm\bar z)=\kappa/2$); §4.2's $z_d$ row carries only the support
> $\{-\bar z,0,\bar z\}$ and no $\kappa$. The audit's own sentence said §4.1. The substance — no
> $\kappa$ in the law of $s$, $\kappa$ reaching only observed order flow — is right and the step
> stands. Fix: change "§4.2" to "§4.1".

**T1-R3 (H6, Step 7) — DONE.** H6 is now stated as constancy with the derivative form as its
corollary (lines 96–102), and it says which step uses which form. Step 7 cites "H6 **in its
constancy form**" and explains why a vanishing derivative at one node would not do (lines 321–323).
Steps 2 and 4 use the corollary. Step 5 derives constancy outright. No inconsistency between H6's
form and any step — I checked all four consumers.

**T1-R4 (H17 placement) — DONE, and the placement is honest.** H17 (lines 191–208) is a separate
numbered hypothesis, headed **"T1-LOCAL: an addition beyond L4's A(br)"**, and it argues clause by
clause why (br-i)–(br-iv) do not already carry it. H13's quotation of A(br) is left at L4's four
clauses with a pointer ("stated separately as H17 rather than smuggled into this quotation",
lines 157–160). I re-read `L4_proof.md` lines 33–58: A(br) there is four clauses, no fifth, and
(br-iv)'s "same function at $\tau$ and $\tau'$" is about the **endpoint map** only — so T1's
disclaimer is accurate and nothing is attributed to L4 that L4 does not say. Propagation is
complete: CLAIM (line 34), Step 11 item 3 (lines 401–408), Step 11's closing tally ("all four
clauses of A(br), **on (br-v) (H17), which A(br) does not supply**", lines 416–417), LABEL CLAIMED 3,
NOT CLAIMED 4, NOTATION DELTA row (line 939). **No claim that (br-v) is L4's.** ✓

**T1-R5 (Step 20) — DONE.** Monotonicity of $r\mapsto\Omega(r)$ now sits **inside H15** (line 174),
with the reason it is a hypothesis and not a consequence spelled out (lines 176–180: Step 16
compares integer windows; an interpolant is otherwise free to dip). Step 20 cites H15 and says in
terms "The citation is H15 and **not** Step 16" (line 583), and it records that the boxed iff is
pure algebra either way (lines 586–588). Block 5's predicted sign is re-pointed to H15's clause
(lines 903–906) and tells the implementer to report violating nodes rather than clip them. ✓

**T1-R6 (WHERE IT FAILS 4) — DONE on structure; two citation defects in the new text (N2, N3).**
Case 4 is now three routes (lines 747–782): (a) $\bar\pi\downarrow0$, (b) $A'_\kappa=0$ at
$\bar\pi$ bounded away from zero, (c) $C_h(\bar\pi)=0$ with $\bar\pi>0$. **Is $C_h=0$ genuinely
handled? Yes.** Route (c) does the four things card §5 asks for: it says the case is *inside*
A($\tau$)'s weak orientation (card §5: "draft_v2's (C\*) is the strict version; the $C_h=0$ case
must be handled explicitly" — quoted accurately), it propagates the degeneracy to the tighter
threshold, it records that H14 leg 3 then holds with equality so Step 13 reads $0\le0$, and it says
the conclusion must be read off Step 6 rather than through $W_\tau C_\tau$, with the NaN note for
the implementer. **H14's new equality qualifier is transcribed exactly**: L4's CLAIM item 4 reads
"with equality whenever $C_h(\bar\pi(\tau))=0$" (`L4_proof.md` line 108–109); T1's H14 line 165–166
reads the same. And L4 proves the propagation itself at its Step 20 (lines 405–411), so route (c)'s
first consequence is L4's result, not T1's invention.

> **N2 (MISCITED).** Lines 772–774: *"by H11's monotonicity of $\lvert C_h\rvert$ in $\bar\pi$ and
> **H14 leg 2's $\bar\pi(\tau')\le\bar\pi(\tau)$**"*. L4's leg 2 delivers
> $\bar\pi_{\mathrm{pr}}(\tau')\le\bar\pi_{\mathrm{pr}}(\tau)$ — the **prior engagement share**
> (`L4_proof.md` VERDICT bullet 2 and CLAIM item 3). Getting from the share to the chord **endpoint**
> $\bar\pi$ is clause (br-iv), which this file is scrupulous about everywhere else (Step 11 item 2,
> WHERE IT FAILS 3, NOTATION DELTA). This is the share/endpoint conflation the orchestrator's
> binding ruling forbids, appearing in new text. The root is upstream: **H14's own leg-2 wording**
> (lines 163–164) says "lower $\tau$ weakly lowers $\bar\pi$ in the pooled class", where L4 says the
> share — a pre-existing looseness the batch-2 audit's §6 sweep did not cover (its occurrence list
> was Steps 8, 11, 14, WHERE IT FAILS 3, Block 3, NOTATION DELTA; H14 and case 4 were not in it).
> Non-blocking: the conclusion is L4's Step 20 and is proved there. Fix: write
> $\bar\pi_{\mathrm{pr}}$ in H14 leg 2 and cite (br-iv) in 4c — or simply cite H14's equality
> qualifier, which now carries the whole propagation.

> **N3 (REPAIR).** Same sentence compares $\lvert C_h(\bar\pi(\tau'))\rvert$ with
> $\lvert C_h(\bar\pi(\tau))\rvert$ — one chord functional read at two policies — citing only H11.
> Step 11 item 3 says in terms, four hundred lines earlier, that H11's monotonicity is a property
> *at a policy* and that **(br-v)/H17 is what makes them one functional**. The new text does the
> move without the citation, so the file is internally inconsistent with its own R4 repair. Fix:
> add "and H17" (three words), or cite H14's equality qualifier instead.

**T1-R7 (stale stamp, four A7 citations) — DONE, and accurate against the live card.** Header and
H1 read "2026-08-21 · commit `a175202`+", identical to the card's stamp line. Zero occurrences of
`0c9185b` or `2026-08-20` remain. All four citations re-pointed:

- **H4** (lines 81–87) — the ticket-24 note is summarised faithfully: A7′ + fixed cutoff policy +
  $\Omega>0$ ⟹ **on-path** injective form with an explicit inverse; a satisfying menu exists (the
  pro-rata single-Voice menu); adversarial verdict SURVIVES WITH REPAIRS. Every element matches card
  §5's note word for word in substance.
- **WHERE IT FAILS 6** (lines 791–801) — the failure boundary list matches the card's: binding stake
  cap, quantized stakes, a composed target repeating values across a Voice-plan switch, $\Omega=0$,
  and a condition stated at one equilibrium's cutoffs rather than for every $k\in\Theta$. The §4.2
  A7′ row is correctly located and correctly quantified ("over the whole polytope" — the card's row
  says "for every cutoff vector $k\in\Theta$"). ✓
- **LABEL CLAIMED 3** and **NOT CLAIMED 5** — both now say satisfiability is resolved and narrow the
  live risk to whether *this model's* menu satisfies A7′, which the file does not check. Correct,
  and still conservative.
- The three surviving `open` mentions (lines 5, 793, 1038) are all historical ("recorded as open",
  describing the earlier draft). No stale claim survives.

**T1-R8 (NOTATION DELTA) — DONE and complete.** $\Omega^\*$/$k_D^\*$ (line 940, with the $k_D$
draft_v2-alias caveat the audit asked for), $I$/$I_\tau$ (941), (br-v) (939). I checked the new text
for any *further* undeclared symbol: the only new ones are $I_\tau$ (declared), $t$ (a bound
variable) and $r_\tau$ (card §4.5). Nothing missing.

**T1-R9 (the ledger's "equivalently") — DONE, as the audit wanted.** The flag (lines 954–973) now
proposes the **quantifier fix** rather than the infinitesimal demotion, displays the exact
finite-scale equivalence from 21a, names pointwise $\rho\le0$ as sufficient-not-necessary, and gives
proposed card wording in §5's house style. The ledger row it quotes is verbatim card §6's T1 row. ✓

---

## 3. New-damage hunt

Beyond N1–N3, I looked for the four failure modes the fix could have introduced.

**Numbered but unconsumed hypothesis: none.** H16 → Steps 3, 5 ✓. H17 → Steps 11, 15 ✓. H18 →
Step 15 ✓. H1–H15 all still consumed (re-checked each).

**Step citation broken by renumbering: one stale range (N4).** No step was renumbered — 22 steps,
same order, same part boundaries. But:

> **N4 (REPAIR).** Lines 661–662, Step 22: *"Nothing in **H1–H15** signs $C_T$ … so nothing in
> **H1–H15** signs $\partial_{r_T}\mathcal S$ or $W_TC_T-1$."* The file now runs to H18. The
> substance survives — H16 is timing, H17 and H18 are both threshold-side and neither touches the
> window margin — so the sentence is true, but the range no longer names the maintained list. Fix:
> "H1–H18" twice. (The same sentence's next clause, "every hypothesis maintained here", is fine.)

**H6's constancy form vs other steps: consistent.** Checked all four consumers; see R3 above.

**H18 working outside Step 15: no.** See §1.

**CLAIM/LABEL/NOT CLAIMED consistency with the new hypotheses: clean.** CLAIM (B) carries
"A(br) … plus the comparability clause (br-v) that this file adds as H17"; LABEL CLAIMED 3 names
H18 and (br-v) and states the would-be label as "PROVED under A($\tau$) and A(br)+(br-v) at fixed
policies"; NOT CLAIMED 13 is new and states Step 15's conditionality and the atom reason. All three
agree with the hypothesis block.

> **O1 (OBSERVATION).** The changelog (lines 1024–1027) says *"No boxed claim's substance changed"*
> and then lists **five** items — Steps 6, 13, 18, 20 and 22. Only four displays are `\boxed`;
> Step 22 is prose. All four boxed displays *and* Step 22's prose are in fact unchanged, so nothing
> is overstated about substance; the word "boxed" is just doing duty for five items where it fits
> four.

> **O2 (OBSERVATION).** T1-O7 persists in the new text: H9 is consumed at Steps 10 and 15 and H5 at
> Step 5 and inside H18, but neither bracket was updated. The changelog claims only H2, H6, H8, H13,
> H14 were corrected, so this is not a false claim — the brackets remain a navigation aid slightly
> behind the steps.

---

## 4. Mechanical scans (whole file, changed regions included)

- **Banned words** (`clearly` / `it follows` / `standard` / `obviously` / `evidently` / `trivially` /
  `straightforward` / `well-known` / `of course` / `easily seen` / `routine` / `clear that`):
  **0 hits**, case-insensitive, whole file. Card §8 rule 7 respected.
- **External citations** (`\ref`, `\cite`, `lem:`/`prop:`/`thm:`/`app:`/`eq:`, `et al`,
  `Lemma N`/`Proposition N`/`Theorem N`/`Appendix X`): **0 hits**. Three `draft_v2` mentions, all
  card-carried aliases and therefore inside card §8 rule 2: line 64 ($\omega_P$, card §4.4's own
  gloss), line 770 ("draft_v2's (C\*) is the strict version", quoted from card §5's A($\tau$) row),
  line 940 ($k_D$ alias, card §4.5's $k$ row). Checked each against the card; all three are the
  card's own words. Clean.
- **Reserved bare letters:** **0 hits**. No literal `$W$` or `$C$` anywhere; every $W$/$C$ carries a
  margin subscript ($W_\tau,W_T,W_{O1},C_\tau,C_T,C_{O1},C_h$) or is "Part C" / "$C^1$" / "C1" (the
  ledger ID). No `\lambda`, `\psi`, `\chi` at all; `\omega` appears only as $\omega_a$ and $\omega_P$.
  Card §8 rule 4 and §4.6 respected.
- **Template heading order** (card §8 rule 6): `CLAIM` (13) · `HYPOTHESES` (58) · `PROOF` (239) ·
  `WHERE IT FAILS` (673, 8 cases ≥ 2) · `LABEL CLAIMED` (816) · `NUMERICAL CHECK REQUEST` (844) ·
  `NOTATION DELTA` (929) · `NOT CLAIMED` (977) — **exact**, with `Retry fixes applied` (1020) as the
  authorized final extra section. 22 numbered steps, each citing a hypothesis or an earlier step.
- **Card stamp:** matches the live card's stamp line exactly.

---

## 5. What I did not check

- **UNCHECKED — L3's amended statement (H12).** I read only L4's A(br) block, CLAIM and Steps 19–20
  for transcription. H12's mean-value form was passed by the batch-2 audit and was not touched by
  this round, so I did not re-open `L3_proof.md`.
- **UNCHECKED — the O-1 arithmetic.** The audit executed it (four composition factors reproduce to
  4×10⁻⁵) and no fix touched WHERE IT FAILS case 1 or Block 6. Not re-run.
- **UNCHECKED — whether A(br)+(br-v) is satisfiable on any menu.** Out of scope for a proof-read,
  and the file claims nothing there (NOT CLAIMED 4).
- **Not in scope, still open:** the audit's seven OBSERVATIONS. The changelog declines them
  explicitly and says why, and three (T1-O2, T1-O3b, T1-O6) are card-owner-facing. T1-O6 in
  particular still stands: **the card's T1 ledger row states the threshold leg unconditionally**,
  while the file proves it only under A($\tau$), A(br) and now (br-v). If T1 ever lands, that row
  must absorb the weakening.

---

## 6. Counts

New **FAIL/WRONG 0** · new **MISCITED 2** (N1, N2) · new **REPAIR 2** (N3, N4) ·
new **OBSERVATION 2** (O1, O2) · **UNCHECKED 3**.

T1-F1 **discharged**. R1–R9 **all applied**; R2 and R6 applied with the citation defects above.
Banned words 0 · external citations 0 · bare reserved letters 0 · unused hypotheses 0 · bare steps 0
· template order exact · stamp current.

**T1 remains CONJECTURE. No label moves, and this file does not move the ledger.**
