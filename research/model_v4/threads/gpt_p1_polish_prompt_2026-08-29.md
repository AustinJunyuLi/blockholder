# P1 Proof — Full-Grain Polish Pass

**CONTENTS**

| § | What it holds |
|---|---|
| 1 | The ask — the task, the four finding classes, the completion criterion, the standing discipline, the scope fences |
| 2 | The history in six sentences — demotion, repair, restoration, your own 2026-08-28 verdict, the correction since |
| 3 | The statement of record — MODEL CARD's P1 row, verbatim and complete |
| 4 | The definitions the proof stands on — MODEL CARD §§3–5, verbatim |
| 5 | The proof, complete — `proofs/P1_proof.md`, all 1,489 lines |
| 6 | What is asked back — the response format |

## 1. THE ASK

**Do a step-by-step polish pass over the P1 existence proof in §5: verify each step on its own
merits, and where a step is correct but rough, propose the concrete text that repairs it.**
Soundness first, exposition second — a step that does not hold is not a wording problem, and a step
that holds but reads badly is not to be waved through because it holds.

You have no memory of this project and no repository. Everything needed to do the pass is in this
one paste, in the order it appears below. Nothing else exists.

**Build the answer against this stamp.** The MODEL CARD version stamp is
**2026-08-28 · re-review audit repairs · commit `59c0dfc`**, and §3 and §4 below are cut from the
card at that stamp. An answer written against a stale stamp is re-asked, not accepted.

**The four finding classes, defined once.** Every finding you return carries exactly one of these
labels, and the label tells the lane what to do with it.

- **WRONG** — the step does not establish what it claims. State the exact failure: name the
  inference that does not go through, and give either the witness that breaks it or the corrected
  claim the argument actually reaches.
- **GAP** — the step needs an argument it does not carry. Name the missing argument, say where in
  the step it belongs, and say what it would have to establish.
- **POLISH** — the step is sound, and rough: wordy, misordered, a load-bearing move buried in a
  subordinate clause, a citation standing where a computation belongs, or a computation standing
  where a citation would serve. **Every POLISH finding carries its proposed replacement text,
  drop-in ready** — the sentence or paragraph as you would have it read, not a description of the
  improvement.
- **UNCLEAR** — the step cannot be verified from this paste. Name exactly what is missing: the file,
  the definition, the number, the earlier result.

**The completion criterion, which is the contract.** **Every numbered step and every lettered or
roman sub-part of the proof, exactly as printed in §5, receives one row in a closing per-step
verdict table — SOUND AS WRITTEN / POLISH (finding #) / GAP or WRONG (finding #) / UNCLEAR
(finding #) — and an answer with a missing row is an incomplete answer.** The proof text in §5 is
the authority on what the rows are: read off its own step numbering and its own sub-part letters,
including sub-parts written bare in running text, and give each one a row. A step you have nothing
to say about still gets a row, reading SOUND AS WRITTEN. That row is the finding.

**The standing discipline, unchanged and restated compactly.** Your findings can support a
**demotion** — a PROVED row sent back to CONJECTURE on a hole you find — and can never **promote**
anything; only a written proof carrying an adversarial proof-read PASS and an independent
statements-only re-derivation PASS, both run inside the lane by agents who did not write the proof,
moves a label upward, and an executed committed check earns NUMERICAL and nothing more. Every text
you propose is **CONJECTURE-grade edit text** until that same gate is run over the proof carrying
it: a repair adopted on your prose alone would put the row back in the position the 2026-08-23
demotion punished. Your response will be **filed verbatim and audited finding by finding**, so
anchor each finding to a step number and quote the current text you are replacing — a finding the
audit cannot localise is a finding the audit records as unactionable.

**Scope fences.** The object of this pass is the **proof text** of `proofs/P1_proof.md` (§5),
checked against the card's **P1 row** (§3) as the statement of record. Three things sit outside it.

1. **The applicability record is settled and is ground truth here.** A3, A6 and A($\tau$) are
   measured false at the implemented calibration; the card's §5 hypothesis blocks, inlined in §4
   below, carry the measurements, the loci and the check names. Take those as given. Direct
   applicability commentary only at the one place it belongs in this pass: **where the proof text
   itself claims more than that record supports.**
2. **The paper sections are another thread's object.** The draft_v3 theory sections transcribe the
   card; their staleness against this stamp was your own 2026-08-28 finding cluster and is being
   repaired separately.
3. **The other seven proofs and the numerical implementation are other threads' objects.** Cite
   them where P1 consumes them by statement — D1 travels into P1 with its own hypotheses — but do
   not audit them here.

**The card's rules bind your answer.** The MODEL CARD's **§4 Symbol table** (inlined in §4 below) is
the only notation available: do not renumber or re-key a card symbol, and list in a NOTATION DELTA
every symbol you use that the table does not already carry. The MODEL CARD's **§8 Standing rules**
governs how proof prose is written: no "clearly", "it follows", "standard" or "obviously" standing
in for a step that is not shown. Hold your own replacement text to that rule, and raise it as a
POLISH finding wherever the proof breaks it.

**Reading the section numbers.** Bare `§1`–`§6` always mean this document's own sections. The
MODEL CARD has its own §1–§9 and the proof has its own numbered steps; both are named explicitly
("card §4.2", "Step 12(c)") wherever they appear.

**Inlining convention.** Every block below sits between a `FILE:` descriptor line, an opening
`===== BEGIN <path> =====` marker and a closing `===== END <path> =====` marker. Two descriptor
classes are used, and the distinction matters when you cite a block.

- **`(verbatim, complete)`** — the whole file, byte-for-byte. §5 is the only one, and nothing
  inside it is this document's text.
- **`(excerpt, lines a–b)`** — a contiguous byte-for-byte slice of the named file, with the line
  range in the descriptor. §3 and §4 are excerpts of `MODEL_CARD.md`; §4 says below exactly what
  was cut and why.

No commentary of this document appears inside any marked block: everything between a BEGIN and its
END is the named file's own bytes.

---

## 2. THE HISTORY IN SIX SENTENCES

Six sentences, written from the lane's own records; every date, commit and quotation below is on
file.

**One.** On 2026-08-22 you reviewed this stack and your finding 1 sent P1 from PROVED back to
CONJECTURE on three independent grounds — the proof's h.7 consumed the **joint** injective form of
A7 while the card row and the 2026-08-21 re-derivation carried the weaker **on-path** form A7′, so
the two-pass gate had never covered a single statement; Step 12 equated "the round-2 order strictly
improves the flagged continuation" with a bracket carrying plan $j'$'s own engagement cost, while a
round-2 deviator has already sunk $C_j(s)$, a gap that is vacuous on single-Voice menus and live on
any admissible menu with two Voice plans sharing a pooled path; and Step 9 asserted that every noise
mark carries positive probability whenever $\kappa>0$, which is **false at $\kappa=1$** under card
§4.1's noise law and $\kappa=1$ is in-domain — the demotion landing 2026-08-23 at commit `43a45f8`
after an in-house audit that upheld all three grounds against the primary record.

**Two.** Ticket 35 then repaired the statement to the hypotheses the proof actually consumes, one
answer per ground: **A7-J** — joint tuple injectivity of $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$ on the
whole flagged-pair set, *including pairs no cutoff vector selects* — replaces A7′; **h.16**, a
continuation-cost equivalence clause on the round-2 deviation set, closes the sunk-cost gap and is
trivially true on any single-Voice menu, where that set is a singleton; and the $\kappa$ boundary is
handled **by extension, not by restriction** — no cut to $\kappa\in[0,1)$ is taken, the false
positivity claim is withdrawn, and the boundary histories are null under *every* profile, hence off
nature's path rather than off the players'.

**Three.** The two-pass gate was satisfied afresh on 2026-08-25 by two agents neither of whom wrote
the proof — an adversarial proof-read returning **PASS, 0 FAIL**, whose reader attacked the
restructured Step 12 lemma part by part before accepting anything and records that **his own round-1
FAIL witness is refuted**, and an independent **statements-only re-derivation** returning
PASS-WITH-CHANGES from the card row alone, with all three demotion items reproducing there
independently — and P1 returned to PROVED at commit `0cbdb37`.

**Four.** Your re-review of 2026-08-28, built against the previous stamp, returned **LABEL STANDS**
for P1 and for all eleven labels with zero demotions, recording that the three ticket-35 repairs
"are not arbitrary retreats" and that **"the theorem is not merely a proof-driven retreat on A7-J,
continuation cost, or the $\kappa$ boundary"** — and locating the remaining inadequacy in model
applicability, A3 and A6 assuming structure the implementation fails to possess, rather than in the
implication.

**Five.** That same re-review found one WRONG inside the P1 row's trailing A5 sentence — the scalar
reduction establishes continuity of the unique inner root **in its belief summaries**
$(\hat v,\pi)$, not continuity of the **composed** pooled price family **in the cutoff vector $k$**,
and the A6 record exhibits exactly that composition jumping — and the in-house audit UPHELD it: the
row's clause was corrected in place with a dated marker, the card's §5 A5 block gained a dated
evidence note keeping the two continuities apart, and the hypothesis set, the conclusion and the
label are unchanged, P1's label surviving because A6 separately assumes the outer-map continuity
Brouwer uses.

**Six.** That correction is the current stamp — **2026-08-28 · re-review audit repairs · commit
`59c0dfc`** — which is what §3 and §4 carry, and the one thing your re-review could not do was read
the proof, which it recorded as its own UNCHECKED item ("the full 20-step proof is not pasted; only
its opening is available"): closing that is why this thread exists.

---

## 3. THE STATEMENT OF RECORD

The card's P1 row, complete. It is one table row — `ID | Statement (amended), with its full
hypothesis set | Label | Evidence chain` — and it is long because the hypothesis set is enumerated
in full rather than gestured at. **This row is the statement the proof in §5 must establish.** Where
the proof and this row disagree, that disagreement is a finding, and the row is what the lane has
published.

FILE: `research/model_v4/MODEL_CARD.md` (excerpt, line 551 — the P1 row of the card's §6 result ledger)

===== BEGIN research/model_v4/MODEL_CARD.md:551 =====
| P1 | Under **A1, A2′, A3, A4, A6, A7-J (joint tuple injectivity — §5's joint $(j,s)$ form of A7, on the whole flagged-pair set $\{(j,s):D_j=1\}$ *including pairs no cutoff vector selects*; strictly stronger than the on-path A7′, and the form the proof consumes where it pins *off-path* flagged beliefs. Amended from A7′ 2026-08-25: the pre-review row carried the on-path form while `proofs/P1_proof.md` h.7 consumed the joint form, so the two 2026-08-21 passes covered two different statements), D1 by statement *with its own hypotheses travelling*, the §2 no-feedback timing read with the flag-terminates-the-pooled-round clause, the definitional round-2 action-set hypothesis** (the flagged-round action set **is** the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements agreeing with $j$ on everything already played — *not* a closure condition; the closure form is jointly unsatisfiable with finiteness by cardinality), **continuation-cost equivalence on that same set** (the proof's h.16, added 2026-08-25: menu elements sharing $j$'s pooled path up to $f_j(s)$ with $a_{j'}=a_j$ carry the same engagement cost, $C_{j'}(s)=C_j(s)$. **Trivially true on any single-Voice menu**, where that set is a singleton. What it buys, **under the plan-completion reading of the $C_j(s)$ timing convention below** — under the sunk reading the continuation is constant on the deviation set with no clause at all and h.16 is not consumed, so the hypothesis is listed because the row does not commit to a reading, and it is what makes the conclusion hold under both: on that set the flagged price does not move and the order cancels, so the engagement cost is the only thing that can differ between staying and deviating — and at a flagged pair the cutoff vector does **not** select there is no date-0 optimality to fall back on, so without this clause the deviator takes the class member with the smallest cost and item (ii) of §3 fails at that node. Live only on menus with two or more Voice plans sharing a pooled path), **$m_0\ge0$, the §4.3 blockholder-objective definition $U_j$** (whose $-a_jC_j(s)$ display `proofs/P1_proof.md` h.14 now carries verbatim, which is what the row's "displayed there in full" asserts; **timing convention, stated here because §4.3 does not date $C_j(s)$**: the engagement cost may be booked either on completing the plan or as sunk once the filing has landed — the two give the same round-2 comparison on the round-2 deviation set, which is what the continuation-cost clause above buys, so the result does not depend on the choice), **and the §4.1–§4.3 table restrictions the argument consumes — in particular §4.3's $Y$ row with the price convention $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ and the entry row for $p(\mathcal I)$; §4.2's Borel-regularity clause for *every* plan including Exit (needed directly, not via D1, whose conclusion is measurability of $D$ and the cell map); §4.2's $D=1\Rightarrow a=1$, the $c/f/B^F/Q^F/b^*$ definitions and $\partial_sB_j\ge0$ for Voice; and §4.1's distributional forms with $\Delta_m>0$**: **at every $\kappa\in[0,1]$**, a cutoff PBE over complete contingent plans exists — $k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, prices at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs as limits of **one** full-support perturbation family over **plans — fixed once and used to define the price system at every $k\in\Theta$, not only at $k^\star$, since the deviation payoffs that define $\mathcal T$ read off-path pooled histories — at every pooled history reachable *with positive probability* under some plan profile** (at the boundary values $\kappa\in\{0,1\}$ the §4.1 noise support degenerates to $\{0\}$ and to $\{\pm\bar z\}$ respectively; a pooled history needing a mark outside it is null under *every* profile, so it is off nature's path rather than off the players', carries no §3(vi) requirement, and is read by no step. This is the extension route, not the restriction one: no cut to $\kappa\in[0,1)$ is taken, and the pre-repair claim of a belief at *every* pooled history — false at $\kappa=1$ — is withdrawn); **flagged-tuple beliefs supplied by A7-J** at every tuple in the image of the flagged-pair map $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$ — on path and off, since the image includes tuples generated by pairs the cutoff vector does not select — as the point mass at the unique generating pair, which is a **version** of the conditional law at every image tuple (the signal is continuous, so a version is what a conditional law is; any a.e.-equal version serves §3(iii)/(vi) equally) and is the version this equilibrium selects, with no tuple outside that image arising because the round-2 action-set hypothesis leaves no off-menu order to produce one; the §4.3 entry rule; and **a sequentially optimal flagged component at every flagged pair $(j,s)$, whether or not the cutoff vector selects it** — the flagged price is invariant across the round-2 deviation set (A7-J pins the belief at the same $s$ and $\pi=1$), so the order cancels out of the continuation and the continuation-cost clause makes what remains constant. **A5 is not assumed**: its existence and uniqueness content is derived from $m_0\ge0$; its continuity content **in the belief summaries $(\hat v,\pi)$** from the same scalar reduction (`proofs/P1_proof.md` Step 7(iii)'s strict $\varrho'<0$ at every root, with Step 8's implicit-function bound $\partial P/\partial\hat v\in(0,1]$ as a second recorded route — the proof file records both as valid and names neither as the only one); and its measurable-selection content from A7-J plus §4.2's Borel clause. **What is *not* derived is A5's cutoff clause** — continuity of the *composed* pooled price family in the cutoff vector $k$, which runs through the conditioning $(\hat v,\pi)$ rather than through the pricing map (`proofs/P1_proof.md` Step 7, closing paragraph; the struck h.5(c), which marks Step 15's cutoff-continuity citation non-load-bearing). That continuity enters only through **A6 as read**, and §5's A6 evidence note records it **measured to fail** at the implemented calibration (see A5). *Clause corrected in place 2026-08-28 on re-review audit finding 1 (`threads/2026-08-28_gpt_rereview_audit.md`); the hypothesis set, the conclusion and the label are unchanged.* **A6 is read** as asserting that $\mathcal T$ — under a named tie-break-and-corner selection, without which a correspondence cannot be called continuous — is a well-defined single-valued continuous self-map of $\Theta$, with $\Theta$ nonempty per §4.5. **At any such equilibrium at which A8 holds**, both cells carry strictly positive probability and are on path; for A8's restatement as a single signal threshold add **H-ord** (Voice stake monotonicity across plans — the writer's h.13, **renamed here to avoid collision with the objective row**) and the upper-set engagement-flag hypothesis. Uniqueness is not claimed. | **PROVED** | statement `threads/thread1_turn1_answer.md`; proof `proofs/P1_proof.md` (repairs applied through P1-R35, ticket 35 rounds 1–2, close-out and confirm-pass sweep); **proof-read PASS 2026-08-25** `threads/2026-08-25_P1_proofread_retry.md` (**0 FAIL**; 3 REPAIRs + 4 OBSERVATIONs, all applied; the reader verified the Step 12 lemma part by part on the merits and records that his own round-1 FAIL witness is refuted — round-1 FAIL and the sanctioned repair round at `threads/2026-08-25_P1_proofread_round1.md`); **re-derivation PASS-WITH-CHANGES 2026-08-25** `rederive/P1_rederivation_2026-08-25.md` (fresh agent, card row alone; changes 1–5 folded into this statement cell — the §4.1–§4.3 citation block, D1's hypotheses travelling with the three-part A5 sentence, the one-family/every-$k$/positive-probability off-path clause, A6's tie-break-and-corner reading, the $C_j$ timing convention; **change 6 withheld for Austin** — a proposed §9 OPEN item on whether A6's continuity of $\mathcal T$ is satisfiable at the collapsed cutoff vectors §3 admits; **ruled 2026-08-27**: answered rather than filed OPEN — §9 item 4 and the §5 A6/A3 evidence notes carry the panel record, no label moved). **The 2026-08-21 chain is retained below and did not satisfy the gate for the recorded statement**: proof-read PASS 2026-08-21 `threads/2026-08-21_batch1_proofread_audit.md` §4 (0 FAIL; P1-R1…R8; inner fixed point executed on 20k random draws — 0 multiplicity, 0 sign failures) and re-derivation PASS 2026-08-21 (PROVED-WITH-CHANGES) `rederive/P1_rederivation.md` (changes C1–C8) covered **two different statements** — the proof's h.7 consumed the joint injective form of A7 while the row and re-derivation carried the on-path form — which is what the 2026-08-23 demotion turned on, together with Step 12's missing continuation-cost clause and the false positivity claim at $\kappa=1$; all three are repaired and independently reproduced by the 2026-08-25 re-derivation. **Numerical status, stated honestly and separately from the label (ticket 34, `quality_reports/fixes/t2_p1_fournode_recheck.json`):** the four sweep-unresolved nodes ($\kappa\in\{0.15,0.85\}\times(\tau,T)\in\{(0.05,5),(0.075,1)\}$) remain **STILL UNRESOLVED after 30 seeds each** — best payoff-scale residual $3.1\times10^{-4}$–$1.5\times10^{-3}$ against a $10^{-9}$ criterion, best cutoff-scale residual $10^{-14}$–$10^{-11}$; the A3 and A6 proxies pass at every achieving seed. **UNCHECKED**: existence at those four nodes is neither claimed nor denied by this evidence, and the label rests on the proof plus the two 2026-08-25 passes, not on the grid. |
===== END research/model_v4/MODEL_CARD.md:551 =====

---

## 4. THE DEFINITIONS THE PROOF STANDS ON

Three card sections, contiguous and verbatim: **card §3**, the equilibrium notion the proof must
deliver all six items of; **card §4**, the symbol table in all six subsections — every primitive,
every plan and timing object, every price and information object, the premium and
comparative-statics block, the equilibrium and GE block, and the proof-local notation rulings; and
**card §5**, the standing hypotheses with their dated evidence notes, which is where the A3, A6, A5
and A($\tau$) applicability record lives.

**Not inlined, deliberately:** card §§1–2 (position and object; timing) and card §§6–9 (the rest of
the result ledger, the label definitions, the standing rules, and what the card does not claim). The
full card exists and your 2026-08-28 re-review read it complete at the previous stamp; nothing in
those sections has moved except through the repairs §2 records. Card §8's writing rules and card
§7's label definitions are restated where they bind, in §1 above.

FILE: `research/model_v4/MODEL_CARD.md` (excerpt, lines 62–525 — card §3 Equilibrium notion, card §4 Symbol table §§4.1–4.6, card §5 Standing hypotheses)

===== BEGIN research/model_v4/MODEL_CARD.md:62-525 =====
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
| $\Omega = \Pr(D=1)$ | unconditional flagged weight; $\Omega = \Pr(a=1)\,\omega_a$ | $\in[0,1]$; **$\Omega$ is draft_v2's $\omega_P$ — the O-1 numbers 0.037 / 0.129 / 0.286 / 0.50 and the $\approx 0.29$ cut are all $\Omega$-type** (the $\approx 0.29$ is the largest **grid point** at which failure was confirmed in the draft_v2-era record, not a located boundary; the crossing itself was found by bisection at $\Omega^\star = 0.3428$, which is the number §9 item 3 and `HANDOFF_sign.md` §3 carry. This cell identifies the quantity's *type* and states no boundary.) |
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
  *Evidence note added 2026-08-28 (re-review audit finding 1;
  `threads/2026-08-28_gpt_rereview_audit.md`).* **The retained continuity clause is an assumption
  about the *composed* family, and it is measured to fail at the implemented calibration.** Two
  continuities must be kept apart, because only one of them is a theorem. (i) Continuity of the
  inner root **in its belief summaries** $(\hat v,\pi)$ follows from $m_0\ge0$ —
  `proofs/P1_proof.md` Steps 7–8, two independent routes on file. (ii) Continuity of the
  **composition** $k\mapsto(\hat v,\pi)\mapsto P$ **in the cutoff vector** is what the clause above
  retains, and no step derives it: the $k$-dependence runs through the conditioning, not through the
  pricing map (`proofs/P1_proof.md` Step 7, closing paragraph). The A6 note below measures exactly
  that composition jumping — the price system is discontinuous on
  $\bigcup_h\partial\{k:\Lambda_k(h)>0\}$, with $\mathcal T_2$ jumps of $6.33\times10^{-3}$ /
  $1.09\times10^{-2}$ / $2.83\times10^{-2}$ at $(\kappa{=}0.5,\tau_{50},T{=}5)$
  (`quality_reports/fixes/t2_a6_edge_jump_check.json`). Clause (ii) and A6's continuity clause
  therefore fail together, at one locus, for the declared construction. **Where each citing row
  stands:** D1 cites A5 for a unique competitive price at every public history and L2 for one
  flagged fixed point — the existence/uniqueness content, released above to $m_0\ge0$; L1 cites it
  to pin *the* version of $\mathbb E[Y\mid\mathcal I]$. **No result row consumes clause (ii)**, so
  no row is touched. **No label moves and none is licensed** — A5 is a hypothesis.
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

  *Evidence note added 2026-08-25 (ticket 33; **lead sentence corrected 2026-08-28** on re-review
  audit finding 2 — every number, bullet and verdict below is unchanged).* **At the implemented
  calibration A($\tau$) FAILS. The decisive representation failure is already established by the
  support condition alone; the derivative pattern also fails, and independently.** The support half
  carries the verdict because it is A($\tau$)'s entire remaining content (see the bite paragraph
  above); the derivative-pattern bullet is a second and independent failure, of which only the
  $A_{1/2}'$ residual is inherited from the support. *(The superseded lead read "it fails on the
  support, not on the derivative pattern", which the third bullet below contradicts on its own
  terms.)* The pooled cell's
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

===== END research/model_v4/MODEL_CARD.md:62-525 =====

---

## 5. THE PROOF, COMPLETE

`proofs/P1_proof.md` in full — 1,489 lines: the CLAIM, the hypotheses h.1–h.17 (h.5 struck), the
PROOF in six parts and twenty numbered steps, WHERE IT FAILS, LABEL CLAIMED, NUMERICAL CHECK
REQUEST, NOTATION DELTA, NOT CLAIMED, and the four repair tables at the foot. This is the object of
the pass.

**Two orientation notes, which belong here and not inside the block.** First, the file's own head
and foot were written before the gate ran and say so: they carry the stamps the file was patched
against and the line "P1 remains CONJECTURE — the label is the orchestrator's to move, on the
passes, not this file's to claim." That is the file's pre-gate state, correctly recorded and
deliberately not rewritten; **the controlling label is §3's row, PROVED as of 2026-08-25.** A
finding that the file's label line contradicts the card row is a finding about a frozen provenance
note, not about the mathematics. Second, the four *Repairs applied* tables at the foot are the
audit trail for how the proof reached its current text — P1-R1 through P1-R35, each tracing to a
numbered finding — and they are inside the block because the block is the whole file. They are
part of the record; they are not proof steps, and they take no verdict-table rows.

FILE: `research/model_v4/proofs/P1_proof.md` (verbatim, complete)

===== BEGIN research/model_v4/proofs/P1_proof.md =====
# P1 — Cutoff PBE existence (full proof)

**Written against MODEL CARD v4, version stamp 2026-08-20 · commit `0c9185b`.**
Sources consumed: card §§2–5 and §8; `threads/thread1_turn1_answer.md` §P1 (the statement);
`threads/thread1_turn2_audit.md` (the D1 repairs, in particular D1-R2 on the flagged continuum,
and L2-R1/L2-R2 on the injective form of A7 and the no-feedback timing).

**Patched 2026-08-25 (ticket 35 / R5) against MODEL CARD stamp 2026-08-23 · commit `d2ccf62`**, to
match the amended P1 row: A7-J in place of A7′ at h.7, the new h.16, the $\kappa$ boundary in Step 9,
and the objective display at h.14. **Round 2, same date**, applies the sanctioned repair round after
the two passes came back (proof-read FAIL on one finding; re-derivation PASS-WITH-CHANGES): Step 12
is restructured into the price-invariance-and-cancellation lemma that discharges card §3(ii) at
*every* flagged pair, h.2 is corrected to A2′, h.5 is struck, h.17 is added, and eight further
repairs land. Every change is listed in the two *Repairs applied (2026-08-25)* tables at the
foot of this file and traces to a numbered finding of
`threads/2026-08-23_gpt_end_review_audit.md` or of the two passes. **No step conclusion is weakened
and no label moves: P1 remains CONJECTURE** — the label is the orchestrator's to move, on the
passes, not this file's to claim.

---

## CLAIM

Fix the parameter vector $\vartheta$. Under hypotheses h.1–h.4, h.6, h.7, h.9–h.12, h.14, h.16 and
h.17 below (h.5 is **struck**, h.8 is used only for the addendum, h.13 and h.15 only for Step 20) —
A1–A4 and A6 of card
§5 together with A7 in its **A7-J (joint tuple injectivity)** form, the card's §2 no-feedback timing
read with the flag-terminates-the-pooled-round clause,
D1 by statement with its own hypotheses travelling, the round-2 action-set stipulation h.11, the
continuation-cost equivalence h.16, the sign
convention h.12, the blockholder payoff definition h.14 (card §4.3's $U_j$ row, absorbed there at
the 2026-08-23 regeneration) and the card's §4.1–§4.3 table restrictions h.17 — the two-round model
has, **at every $\kappa\in[0,1]$**, at least one
**cutoff perfect Bayesian equilibrium over
complete contingent plans** in the sense of card §3: a weakly ordered cutoff vector
$k^\star\in\Theta$ with $k^\star=\mathcal T(k^\star;\vartheta)$, together with pooled and flagged
price families at their inner fixed points, Bayes-consistent on-path beliefs, off-path beliefs
obtained as limits of one full-support perturbation family over **plans** — fixed once and used to
define the price system at every $k\in\Theta$, not only at $k^\star$ — at every pooled history
reachable with positive probability
under some plan profile; flagged-tuple beliefs given by **the point mass that h.7 supplies** at every
tuple in the image of the
flagged-pair map $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$ — on path and off, this being a version of the
conditional law at every image tuple and the version this equilibrium selects — with no tuple outside
that image arising under h.11 (Step 10); the card §4.3 bidder-entry rule; and a
sequentially optimal flagged component **at every flagged pair $(j,s)$, selected or not** (Step 12).
Under A8 (h.8) evaluated at $k^\star$, both cells $\mathcal C_F$
and $\mathcal C_P$ carry strictly positive probability, hence both are on path; A8 is used for that
addendum and for nothing in the existence half.

*On the belief clause.* "Reachable **with positive probability**" is Step 9's, and it is a precision
about which
information sets carry a card §3(vi) requirement, not a weakening of the requirement at any of them.
The positive-probability qualifier is load-bearing in its own right (pass-2 N7): a history reachable
only through a $\Phi_s$-null set of signals has probability zero under every profile just as surely as
one needing a mark outside $\mathrm{supp}(z_d)$, and Step 9(c) covers both.
At $\kappa\in\{0,1\}$ the noise support degenerates — $\mathrm{supp}(z_d)=\{0\}$ at $\kappa=0$ and
$\{-\bar z,+\bar z\}$ at $\kappa=1$ — and a pooled history that needs a mark outside it has
probability zero under **every** plan profile and every perturbation stage, so it is null under
nature rather than off path under the players and §3(vi) asks nothing of it. At every reachable
history, on path and off, the limit exists and pins the belief.

h.13 and h.15 are not needed for either half of the claim; they are used only in Step 20, to turn A8
from an assumption about $\Omega$ into a statement about a single signal threshold.

Uniqueness of $k^\star$ is **not** claimed (card §3 and §9; see NOT CLAIMED).

---

## HYPOTHESES

Each is cited by number at the step that consumes it. Items marked **[ADDITION]** are not in card
§5; they are named here because a step needs them and the card as written does not supply them.

1. **h.1 = A1 (independent primitives).** $v,\varepsilon,\xi$ and all $z_d$ mutually independent,
   all variances strictly positive. *Used: Steps 4, 7, 9, 10.*
2. **h.2 = A2′ (finite model, amended boundedness).** Plan menu $\mathcal J$, the image of $\Gamma$,
   the noise support $\{-\bar z,0,+\bar z\}$ and the calendar horizon $H$ are finite; prices and
   payoffs are **locally bounded in $(s,\vartheta)$** on the maintained parameter set, and
   $\mathbb E[\max_{j}\lvert U_j\rvert]<\infty$ for every $k\in\Theta$.
   *Amended 2026-08-25 (round 2, pass-1 finding 2) from "A2 … prices and payoffs bounded on the
   maintained parameter set": card §5 struck that flat bound as **false** and inconsistent with the
   rest of the card ($v$ is Gaussian and the flagged region is unbounded in $s$), and the card's P1
   row cites A2′. Carrying a card-declared-false clause would have proved the row vacuously rather
   than validly. Every use survives: Steps 3 and 9 consume the finiteness clauses only, and Step 13
   needs finiteness of the menu together with finiteness of each $U_j(s;k)$, which A2′ supplies
   pointwise (local boundedness) and in expectation (integrability). The 2026-08-25 round-1 staleness
   sweep (P1-R15) reached LABEL CLAIMED and Step 14 and missed this.* *Used: Steps 3, 9, 13.*
3. **h.3 = A3 (ordered plans, single crossing).** At every belief/price system, adjacent-plan
   payoff differences cross zero at most once in $s$, and the preferred plan is weakly increasing
   in $s$. *Used: Steps 1, 13.*
4. **h.4 = A4 (legal-clock discipline).** $c$ is the first date the path reaches $\tau$; the filing
   lands exactly at $c+T$; filings truthfully reveal stake and purpose; only Voice plans cross in
   the core; $D=1\Rightarrow a=1$. *Used: Steps 2, 6, 19.*
5. **h.5 — STRUCK 2026-08-25 (round 2, pass-1 finding 3). A5 is not a hypothesis of P1.** The slot is
   kept, not renumbered, so that every "h.6"…"h.16" citation in this file and in the audit record
   still resolves. The card's P1 row says "**A5 is not assumed**"; this file carried A5 as a numbered
   hypothesis and consumed it at Steps 5(a), 6(b) and 15 — a proof-vs-row mismatch of the same
   species as the A7 one that caused the demotion. It is eliminable inside the file, use by use:
   (a) Step 5(a)'s unique pooled control-node root is **derived** at Step 7 from h.12 ($m_0\ge0$);
   (b) Step 6(b)'s single-valuedness of $\mathcal G_F$ likewise from Step 7(iii), and its
   continuity in the belief — the one genuinely load-bearing use, since Step 6(d) composes a Borel
   map with a continuous one — from Step 8's implicit-function argument ($\varrho$ is $C^1$ jointly
   in $(P,\hat v)$ and $\partial_P\varrho<0$ strictly at every root by Step 7(iii)); Steps 7–8 do not
   depend on Step 6, so the re-citation is not circular;
   (c) Step 15's "by h.5 the inner prices are continuous in the cutoffs" is **non-load-bearing**,
   because this proof's route to continuity of $\mathcal T$ is h.6 asserting it outright (Steps 15–16)
   — it is marked there as commentary.
   What remains of A5's *measurable-selection* content is delivered by h.7 (A7-J) plus h.17's Borel
   clause at Step 6(c)–(d), not by an assumption. *Used: nowhere. Cited historically at Steps 5, 6, 15.*
6. **h.6 = A6 (compact outer self-map).** All best-response cutoffs lie in a common compact ordered
   polytope $\Theta$; $\mathcal T$ is continuous and maps $\Theta$ into itself. Steps 13–15 split
   this into three parts and show only two of them are genuine assumptions. *Used: Steps 14, 15, 16.*
7. **h.7 = A7-J (joint tuple injectivity)** — card §5's **joint** form of A7, not its on-path form
   A7′. $(j,s)\mapsto (B_j^F(s),Q_j^F(s),a_j)$ is injective on the flagged-**pair** set
   $\{(j,s):D_j(s;\tau,T)=1\}$, **including flagged pairs that no cutoff vector $k\in\Theta$
   selects**. Per card §5's turn-2 note the weak wording of A7 ("identifies the informed component")
   is not sufficient, and injectivity forces the **tuple** $(B^F,Q^F)$ to be continuum-valued — *not*
   the coordinate $B^F$ on its own, which may be non-monotone and may jump downward while the tuple
   still separates through the sum coordinate $B^F+Q^F=b_j^*(s)$; the coordinates trade the burden
   (card §5's A7 note; `proofs/A7_construction.md` Steps 8–9 with its numeric witness;
   `proofs/A7_attack_verdict.md` S-10; audit Finding 7(ii)).
   **This is strictly stronger than A7′** — on-path injectivity can hold while the joint map collides
   at pairs off the selected policy (the 40-collision executed witness in the attack verdict) — and
   it is the form Steps 6 and 10 consume: Step 10 pins the *off-path* flagged belief, which is a
   statement about pairs the conjecture does not select. It is **satisfiable**: the pinned pro-rata
   single-Voice menu with terminal target strictly increasing on all of $\mathbb R$ satisfies A7-J
   (`proofs/A7_construction.md` Step 7; card §5's A7 note, ticket 24). *Used: Steps 6, 10.*
8. **h.8 = A8 (interior crossing), evaluated at the fixed point.** $0<\Omega(\kappa,\tau,T)<1$ at
   $k^\star$. *Used: Step 19 only.*
9. **h.9 = D1 (rule-keyed partition and timing split).** $D=\mathbf 1\{a=1,\ c(\tau)+T\le H\}$ is
   measurable and maps every control-node public history into exactly one cell; for every Voice
   plan $f_j\le H\iff B_j(s,H-T)\ge\tau$. D1 carried the card's label CONJECTURE when this proof was
   written, so P1 inherited that conditionality; **at stamp `d2ccf62` D1 is PROVED** (moved
   2026-08-21 with both passes on file), and what P1 inherits is D1's own hypothesis set as listed in
   the card's D1 row, not a provisional label. *Used: Steps 2, 6, 19, 20.*
10. **h.10 = the card §2 no-feedback timing, read with the flag-terminates-the-pooled-round clause.**
    *(i) No within-window re-optimisation:* $B_j(s,d)$,
    $q_{jd}(s)$ and $Q_j^F$ are functions of $(j,s,d)$ and $(j,s,\tau,T)$ alone, never of realised
    order flow or realised prices. The turn-2 audit (L2-R2) required this to be lifted from prose
    into a numbered hypothesis for L2; P1 needs it at the same load-bearing places.
    *(ii) The flag terminates the pooled round* (card §2 bullet 3, added here 2026-08-25 on pass-1
    finding 9): pooled trading stops when the filing lands, the flagged round follows it, and the
    bidder acts after that — so the pooled execution runs over $d\le f_j(s)$ and
    $Q_j^F=b_j^*(s)-B_j^F(s)$ is the blockholder's **whole** residual position. The card's P1 row
    lists the timing hypothesis in exactly this two-clause form; clause (ii), not clause (i), is what
    Step 11's decomposition consumes when it sums the pooled bracket to $f_j$ and treats $Q^F_j$ as
    the entire remaining position, and what Step 12(c) consumes when it calls the pooled execution
    sunk at round 2. *Used: Steps 2, 11, 12.*
11. **h.11 [ADDITION] — the round-2 action set is the plan-generated set.** For every
    $j\in\mathcal J$ and every $s$ on the flagged set, the blockholder's round-2 action set at
    $(j,s)$ **is** $\mathcal Q_j(s):=\{Q_{j'}^F(s):j'\in\mathcal J\text{ shares }j\text{'s pooled
    path up to }f_j(s)\text{ and }a_{j'}=a_j\}$ — the orders generated by menu elements that agree
    with $j$ on everything already played — rather than the full interval $[0,\bar b-B_j^F(s)]$.
    *Used: Step 12.*
    **Why this and not the closure form (batch-1 audit P1-R1).** An earlier draft stated h.11
    primarily as a *closure* condition: for every feasible $Q'\in[0,\bar b-B_j^F(s)]$ there is a menu
    element $j'$ delivering $Q_{j'}^F(s)=Q'$. **That form is jointly unsatisfiable with h.2 and is
    struck.** h.2 makes $\mathcal J$ finite, so $\{Q_{j'}^F(s):j'\in\mathcal J\}$ has at most
    $\lvert\mathcal J\rvert$ elements and cannot cover an interval of positive length; the closure
    form therefore forces $B_j^F(s)=\bar b$, i.e. $Q^F\equiv0$ and an empty round 2, contradicting
    card §4.2's $Q^F$ row (Voice plans have $Q^F\ge0$ with $T'<T\Rightarrow Q^F(T')\ge Q^F(T)$, so
    $Q^F$ genuinely varies). The surviving form above is consistent with h.2 and is all Step 12
    consumes — Step 12 runs on it verbatim. It is **not** a closure condition and is not called one:
    it is a modelling stipulation about what the round-2 action set *is*, which is a different and
    much weaker thing.
12. **h.12 [ADDITION] — nonnegative premia.** $m_0\ge 0$. Card §4.1 restricts only $m_1>m_0$ and
    $\Delta_m>0$; it does not sign $m_0$. With $\Delta_m>0$ and $\pi\in[0,1]$ this gives
    $\bar m(\mathcal I):=m_0+\pi(\mathcal I)\Delta_m\ge 0$. *Used: Steps 7, 8.*
13. **h.13 [ADDITION] — Voice stake monotonicity across plans.** For Voice plans $j'>j$,
    $B_{j'}(s,d)\ge B_j(s,d)$ for every $(s,d)$. Not in the card; the card orders the menu by
    "aggressiveness" without tying that order to the stake path. *Used: Step 20 only, for the
    threshold reformulation of A8 — not for existence.*
14. **h.14 [ADDITION, card gap closed 2026-08-23] — the blockholder's payoff.** For plan $j$ at
    signal $s$,
    $$U_j(s)=\mathbb E\bigl[b_j^*(s)\,Y-\mathcal C_j^{\mathrm{trade}}-a_j\,C_j(s)\ \big\vert\ s,j\bigr],$$
    with $\mathcal C_j^{\mathrm{trade}}$ the plan's execution outlay — the stake increments valued at
    the pooled prices $P_d^P$ up to the plan's last pooled date, plus $Q_j^F(s)P^F$ when $D_j=1$ —
    and $C_j(s)\ge0$ the engagement cost, which enters **weighted by the engagement flag $a_j$**, so
    that plans with $a_j=0$ pay no engagement cost whatever $C_j$ is written as. *Display aligned
    2026-08-25 with card §4.3's $U_j$ row, which carries $-a_jC_j(s)$ and cites this hypothesis as
    "displayed there in full"; the pre-repair display wrote $-C_j(s)$ (audit Finding 1, citation
    nit). The $a_j$ factor is immaterial to every step that consumes h.14: Steps 11–12 run on the
    flagged set, where $a_j=1$ by h.4.* No step consumes the sign $C_j\ge0$; it is transcribed
    because the card row carries it.
    **History:** when this proof was written the card carried no blockholder payoff row — no §2.10,
    no $U_j$, no $\mathcal C_j^{\mathrm{trade}}$ — and the object was stated here as this proof's own
    numbered definition, faithful to `threads/thread1_turn1_answer.md` §2.10. The 2026-08-23
    regeneration absorbed it as card §4.3's $U_j$ row (batch-1 audit P1-R6, P1 re-derivation change
    C2), so h.14 is now a transcription of a card row rather than a card gap. *Used: Steps 11, 13,
    14, 15 — it is the optimand of Steps 11–13 and the object Step 15 asks to be continuous.*
15. **h.15 [ADDITION] — engagement flags on an upper set of the menu.** $a_j=1$ exactly on an upper
    set of the ordered menu: there is $j_a$ with $a_j=1$ for $j\ge j_a$ and $a_j=0$ for $j<j_a$.
    Card §4.2 says $a_j=1$ for Voice and $0$ for Exit/Hold and orders the menu "least to most
    aggressive", but never ties the two; card §4.5's four-action gloss happens to satisfy this and a
    general finite menu need not. *Used: Step 20 only, alongside h.13 — not for existence.*
16. **h.16 [ADDITION] — continuation-cost equivalence on the round-2 deviation set.** For every
    $(j,s)$ on the flagged set and every $j'$ in the generating set of h.11's action set
    $\mathcal Q_j(s)$ — every $j'\in\mathcal J$ that shares $j$'s pooled path up to $f_j(s)$ and has
    $a_{j'}=a_j$ — the engagement costs agree:
    $$C_{j'}(s)=C_j(s)\qquad\text{on each h.11 deviation set.}$$
    Equivalently: within a deviation set the engagement cost is a function of $(a_j,s)$ alone and not
    of which round-2 order the plan carries. *Used: Step 12.*

    **Why this clause is needed, and where (audit Finding 1(b); restated 2026-08-25 round 2 on
    pass-2 R16–R17).** Step 12 shows that on a deviation class the flagged price is invariant and the
    flagged order cancels out of the payoff, leaving
    $V(j')=B_j^F(s)P^F(s)-\text{(engagement cost)}$. **The engagement cost is therefore the only
    thing that can move across the class**, and whether it does is exactly h.16. Two conventions are
    available and the card fixes neither (card §4.3's $U_j$ row does not date $C_j$): **(α) plan
    completion** — submitting $Q_{j'}^F(s)$ *is* completing plan $j'$, so the deviator bears
    $C_{j'}(s)$; **(β) sunk cost** — the filing has landed and $D=1\Rightarrow a=1$ is public (h.4),
    so the engagement cannot be unmade and the deviator bears $C_j(s)$ whatever order is submitted.
    Under (β) the continuation is constant on the class with no clause at all. Under (α) it is
    constant **iff** the cost is constant on the class, which is h.16.
    *Where it bites:* under (α) at a **selected** $j$, date-0 optimality already suffices — Step 12(c)
    gives $U_{j'}=B_j^FP^F-C_{j'}-E_j$ within the class, so $U_j\ge U_{j'}$ *is* $C_j\le C_{j'}$ —
    but at a **non-selected** flagged pair there is no date-0 optimality to appeal to, and the
    deviator strictly prefers the class member with the smallest $C_{j'}(s)$. Those non-selected
    flagged nodes are pass-1 finding 1's node class, they carry card §3(ii) exactly as the selected
    ones do, and h.16 is what discharges them under (α).
    **Why it is stated as an equality rather than one-sidedly.** (1) *The sharing relation is
    symmetric.* If $j'$ agrees with $j$ on the pooled path up to $f_j(s)$ then $c_{j'}(s)=c_j(s)$ —
    the crossing date is a first-hitting index of a path they share, and $c_j\le f_j-T\le f_j$ —
    hence $f_{j'}(s)=f_j(s)$, so the agreement is mutual; with $a_{j'}=a_j$, "shares the pooled path
    and the engagement flag" is an equivalence relation on the flagged set at each $s$, and each h.11
    deviation set is one of its classes. A clause imposed at every pair of a class in one direction
    is imposed in both. (2) *The clause cannot be indexed by the equilibrium's selection*: Brouwer
    does not say which $k^\star$ it returns, and the requirement lands at flagged pairs that **no**
    cutoff vector selects, where "the selected $j$" does not name anything. So the uniform equality is
    the honest form, and it is also what **spec MAY-11's** alternative route arrives at: restating
    round-2 optimality against the sunk-cost continuation is convention (β), which settles the step
    only by settling a card ambiguity this proof has no standing to settle. **h.16 makes (α) and (β)
    the same number**, so the conclusion is convention-free. **Card ambiguity, regeneration item: card
    §4.3's $U_j$ row should say when $C_j(s)$ is incurred.**

    **Satisfiability.** h.16 is **trivially true on any single-Voice menu**, the pinned pro-rata menu
    included: on the flagged set $a_j=1$ (h.4), so a deviation set contains only Voice plans, and
    with one Voice plan it is the singleton $\{j\}$ and $\mathcal Q_j(s)=\{Q_j^F(s)\}$
    (`proofs/A7_construction.md` Steps 5–7: Exit and Hold never cross $\tau$ when $b_0<\tau$). It is
    a genuine restriction only on menus carrying two or more Voice plans that share a pooled path
    (WHERE IT FAILS 7).
17. **h.17 [ADDITION 2026-08-25, round 2] — the card's §4.1–§4.3 table restrictions, enumerated
    rather than silently consumed.** Added on pass-2 findings N1–N4, which showed several load-bearing
    card rows were absent from the hypothesis list of both this file and the card's P1 row (they are
    on the **card**, so nothing new is assumed; they were simply never cited). The card row now cites
    the same block. Four items:
    * **(h.17-a) §4.3's $Y$ row and the price convention $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$**,
      with §4.3's entry row for $p(\mathcal I)$. Without it "prices at their inner fixed points" in
      the conclusion names an equation the antecedent never supplied. *Used: Steps 4–8, 12.*
    * **(h.17-b) §4.2's Borel-regularity clause for *every* plan including Exit** —
      $s\mapsto B_j(s,d)$ Borel, the clause the card calls "a genuine addition for Exit". Needed
      **directly**, not through h.9: D1's conclusion is measurability of $D$ and of the cell map, not
      of the flagged tuple. *Used: Steps 2, 3, 6, 9.*
    * **(h.17-c) §4.2's structural rows** — $D=1\Rightarrow a=1$; the definitions of
      $c_j,f_j,B_j^F,Q_j^F,b_j^*$; $\partial_sB_j\ge0$ and $\partial_dB_j\ge0$ on Voice, Hold
      constant, Exit weakly decreasing. *Used: Steps 2, 3, 12, 19, 20.*
    * **(h.17-d) §4.1's distributional forms** — $v,\varepsilon,\xi$ Gaussian with the projection
      $\beta$, $\Delta_m>0$, $\Delta_V\ge0$, $\kappa\in[0,1]$ with the ternary noise law, $b_0<\tau$.
      *Used: Steps 4, 7, 8, 9, 10, 12, 20.*
    None of these is a new restriction on the model: each is a card row P1 was consuming already, and
    listing them is what card §8 rule 6 (every hypothesis enumerated and used) requires.

---

## PROOF

### Part A — the game at a fixed conjecture

**Step 1 (the conjecture induces a measurable plan-selection map).**
Fix $k=(k_1\le\cdots\le k_{J-1})\in\Theta$, where
$\Theta=\{k\in[\underline s,\overline s]^{J-1}:\underline s\le k_1\le\cdots\le k_{J-1}\le\overline s\}$
is card §4.5's compact ordered polytope, nonempty, compact and convex as the intersection of a cube
with the $J-2$ half-spaces $\{k_i\le k_{i+1}\}$. Define
$$
j_k(s)\;=\;1+\#\{i\in\{1,\dots,J-1\}:k_i\le s\}.
$$
$j_k$ is a weakly increasing step function of $s$ with values in $\mathcal J$, and it is Borel
measurable because each $\{s:k_i\le s\}$ is a half-line. This is the object card §3(i) calls "a
weakly ordered cutoff vector mapping $s$ into a plan", and h.3's second clause (preferred plan
weakly increasing in $s$) is what makes such a representation the right shape for a best response;
Step 13 returns to that.

**Step 2 (under h.10 every date-0 object is a deterministic measurable function of $(j,s)$).**
By h.10 the pooled path carries no feedback from realised order flow or prices, so for each
$j\in\mathcal J$ the objects $B_j(s,d)$ ($d=0,\dots,H$), $q_{jd}(s)=\Gamma(B_j(s,d)-B_j(s,d-1))$,
$c_j(s;\tau)$, $f_j(s)=c_j(s)+T$, $B_j^F(s)=B_j(s,f_j(s))$ and $Q_j^F(s)=b_j^*(s)-B_j^F(s)$ are
functions of $(j,s)$ and the policy pair $(\tau,T)$ alone. Measurability in $s$: $s\mapsto B_j(s,d)$
is Borel **for every plan by h.17-b**, card §4.2's explicit Borel-regularity clause — *corrected
2026-08-25 (round 2, pass-1 finding 8) from "monotone by card §4.2, hence Borel", which is false for
Exit: §4.2 imposes $\partial_sB_j\ge0$ on **Voice** only, Exit is weakly decreasing in $d$ and
unrestricted in $s$, and the card supplies Borel-in-$s$ for Exit as a separate clause it calls "a
genuine addition for Exit". The correction is load-bearing, since Step 9's reachability and the
pooled prices integrate over all types including Exit;* $\Gamma$ is a finite ordered coarsening (h.2), hence Borel;
$c_j(\cdot;\tau)=\inf\{d:B_j(\cdot,d)\ge\tau\}$ is the pointwise minimum over the finite calendar
(h.2) of the indices of the Borel sets $\{B_j(\cdot,d)\ge\tau\}$, hence Borel with values in
$\{0,\dots,H\}\cup\{+\infty\}$; and — this is the D1-R2 repair written out —
$$
B_j^F(s)\;=\;\sum_{d=0}^{H-T}\mathbf 1\{f_j(s)=d+T\}\cdot B_j(s,d)
$$
is a finite sum of products of Borel functions, hence Borel, and likewise $Q_j^F$. By h.9 the
disclosure indicator is $D_j(s;\tau,T)=\mathbf 1\{a_j=1\}\cdot\mathbf 1\{B_j(s,H-T)\ge\tau\}$,
Borel in $s$. Composing with Step 1, all of these become Borel functions of $s$ alone at the fixed
conjecture $k$.

**Step 3 (the pooled public-history family is finite; the flagged family is not).**
Card §4.3 defines $\mathcal H_d^P=(X_0,\dots,X_d;\text{flag landed by }d)$ with
$X_d=q_{jd}+z_d$. By h.2 the image of $\Gamma$ is finite and $z_d\in\{-\bar z,0,+\bar z\}$, so each
$X_d$ takes values in a finite set; $d$ ranges over the finite calendar $\{0,\dots,H\}$; and the
flag coordinate is a single bit. Hence the collection of pooled public histories is finite. By
Step 2 the flagged tuple $\sigma_F:=(B^F,Q^F,a=1)$ — card §4.6's $\mathsf S_F$, the filing message
$F$ augmented by the flagged order $Q^F$ — is Borel but takes values in $[0,\bar b]^2\times\{1\}$,
a continuum: card §4.2 puts $B_j(s,d)\in[0,\bar b]$ with $s$ Gaussian and imposes monotonicity
only, and no card row discretises the stake level. This is exactly the D1-R2 finding, and it is
what forces the two layers of Part B to be treated differently.
*Note on scope.* The finiteness of the pooled family rests on the card's own §4.3 row, in which the
flag enters $\mathcal H_d^P$ as a bit and the filing content $B^F$ does not. Were the card to let
post-filing pooled histories carry $B^F$, the pooled family would join the continuum and the
selection argument of Step 6 would have to be run there too.

### Part B — inner prices

**Step 4 (every control-node pricing fixed point reduces to one scalar equation, and depends on the
information set only through the pair $(\hat v,\pi)$).**
Fix a control-node information set $\mathcal I$ and write $\hat v(\mathcal I)=\mathbb E[v\mid
\mathcal I]$, $\pi(\mathcal I)=\Pr(a=1\mid\mathcal I)$ and
$\bar m(\mathcal I)=m_0+\pi(\mathcal I)\Delta_m$. Card §4.3 gives
$Y=(1-\mathsf B)(v+a\Delta_V)+\mathsf B(P(\mathcal I)+m_0+a\Delta_m)$ and, from card §4.3's entry
row, $\mathsf B=\mathbf 1\{\xi\ge P(\mathcal I)+K+\bar m(\mathcal I)-\bar S\}$. Given $\mathcal I$,
the quantities $P(\mathcal I)$ and $\bar m(\mathcal I)$ are $\mathcal I$-measurable constants, so
$\mathsf B$ is a function of $\xi$ alone. By h.1, $\xi$ is independent of $(v,\varepsilon)$ and of
every $z_d$, hence independent of $(v,s,z_{0:H})$ and therefore of $(v,a,\mathcal I)$ jointly;
conditionally on $\mathcal I$, $\mathsf B$ is independent of $(v,a)$. Writing
$p=\Pr(\mathsf B=1\mid\mathcal I)$ and taking conditional expectations term by term,
$$
\mathbb E[Y\mid\mathcal I]
=(1-p)\bigl(\hat v+\pi\Delta_V\bigr)+p\,(P+m_0)+\Delta_m\,p\,\pi
=(1-p)\bigl(\hat v+\pi\Delta_V\bigr)+p\bigl(P+\bar m\bigr).
$$
With $\xi\sim N(0,\sigma_\xi^2)$ (h.1), $p=1-\Phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)$, which
is card §4.3's entry row verbatim and lies in $(0,1)$ for every finite $P$. Define the inner
pricing map
$$
\mathcal P_{\mathcal I}(P)\;=\;\bigl(1-p(P)\bigr)\bigl(\hat v+\pi\Delta_V\bigr)+p(P)\bigl(P+\bar m\bigr),
\qquad
p(P)=1-\Phi\!\Bigl(\tfrac{P+K+\bar m-\bar S}{\sigma_\xi}\Bigr).
$$
The card's requirement $P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ is the scalar fixed-point equation
$\mathcal P_{\mathcal I}(P)=P$. **The map depends on $\mathcal I$ only through the two scalars
$(\hat v(\mathcal I),\pi(\mathcal I))$.** That is the fact Steps 5–7 use.

**Step 5 (pooled layer on a finite index set — stated in two parts, because only one of them is
a fixed point; the inner root comes from Steps 7–8, not from A5).**
By Step 3 there are finitely many pooled public histories. Step 4's map is derived at a **control
node**, which is where $\mathsf B$ is a function of $\xi$ alone given the conditioning, so the two
layers of the pooled family must be treated separately.

(a) *The pooled control-node cell ($D=0$ at date $H$).* Here $\mathcal I=\mathcal I_H$ is a control
node, Step 4 applies as derived, and **Step 7 supplies a unique fixed point** of
$\mathcal P_{\mathcal I}$ from h.12 ($m_0\ge0$), with continuity in the belief from Step 8. This is a
genuine fixed point: the price appears on both sides
through the entry indicator. *(Re-cited 2026-08-25, round 2, pass-1 finding 3: this clause read "h.5
supplies …" while the card's P1 row says A5 is not assumed. Steps 7–8 do not depend on Step 5, so
the re-citation is not circular, and h.5 is struck.)*

(b) *Intermediate pooled dates $d<H$.* $\mathcal H_d^P$ is **not** a control node. Card §4.3's $Y$ row
writes the takeover branch as $\mathsf B(P+m_0+a\Delta_m)$ with $P$ unqualified; under the natural
economic reading — and it is the reading Step 4 itself adopts — that $P$ is the **control-node** price
$P(\mathcal I_H)$, so
$$P_d^P=\mathbb E\bigl[Y\mid\mathcal H_d^P\bigr]=\mathbb E\bigl[P(\mathcal I_H)\ \text{-branch value}\mid\mathcal H_d^P\bigr]$$
is, by the tower property, a plain conditional expectation of already-solved control-node values: **no
self-reference and no fixed point**. Under the other reading of §4.3's $Y$ row (the $P$ inside $Y$ is
the price at whichever information set is conditioning) part (a)'s fixed-point argument applies at
these dates too. **Card ambiguity, regeneration item: card §4.3's $Y$ row should pin which $P$ it
means** (batch-1 audit P1-R8).

The conclusion this step is used for survives on either reading, and that is why nothing downstream
turns on the adjudication: a finite family requires no selection argument, and the pooled price family
$k\mapsto (P_d^P(\mathcal H_d^P;k))_{\mathcal H_d^P}$ is a finite vector of continuous functions of
$k$ — at the control-node cell by (a) with Steps 7–8, and at $d<H$ by (b) as a finite-sum
conditional expectation of continuous functions — on those histories that carry positive probability
under the conjecture $k$. Histories of zero probability under $k$, and histories of zero probability
under every profile, are handled in Step 9(b) and 9(c) respectively.

**Step 6 (flagged layer: a measurably selected family, built from Steps 7–8 rather than assumed —
the D1-R2 point).**
By Step 3 the flagged information sets are indexed by the continuum
$\sigma_F\in[0,\bar b]^2\times\{1\}$. A pointwise statement — "at each $\sigma_F$ there is a
unique root" — does not by itself yield a *function* of $\sigma_F$ that the model can integrate
against, which is what card §4.4's $M_F=\Delta_m\mathbb E[h\mid D=1]$ and h.9's timing split both
require. The family is constructed as follows.

(a) On the flagged cell $\pi\equiv 1$: h.4 gives $D=1\Rightarrow a=1$ and h.9 makes $\{D=1\}$ an
event of the control-node history, so $\Pr(a=1\mid\sigma_F,D=1)=1$, matching card §4.3's row
"$\pi=1$ on $\mathcal C_F$". Hence $\bar m=m_0+\Delta_m=m_1$ on the whole flagged cell, a constant.

(b) By Step 4 the flagged pricing map therefore depends on $\sigma_F$ only through the single
scalar $\hat v(\sigma_F;k)=\mathbb E[v\mid\sigma_F,D=1]$. Write $\mathcal G_F(\cdot)$ for the map
sending a belief $\hat v$ to the unique root of $\mathcal P(\cdot)-\mathrm{id}$ at $(\hat v,\pi=1)$.
**Step 7(ii)–(iii) makes $\mathcal G_F$ single-valued** (existence and uniqueness of the root under
h.12) **and Step 8 makes it continuous** in the belief — indeed 1-Lipschitz, since
$\partial P/\partial\hat v\in(0,1]$ there. *Re-cited 2026-08-25 (round 2, pass-1 finding 3) from
"h.5's uniqueness clause … h.5's continuity-in-beliefs clause"; this was the one genuinely
load-bearing A5 use in the file, because (d) below composes a Borel map with a continuous one. Steps
7–8 are self-contained and do not depend on Step 6, so there is no circularity.* (The symbol is
$\mathcal G_F$ and not $g$: the turn-2 notation ruling
reserves $g$ for L3's mean-value form, and card §4.5 carries $g_r^{PE}$.)

(c) $\sigma_F\mapsto\hat v(\sigma_F;k)$ is Borel measurable. Two routes, both available: it is a
conditional expectation with respect to $\sigma(\sigma_F)$ and hence $\sigma(\sigma_F)$-measurable
by construction; and under h.7 the map $(j,s)\mapsto\sigma_F$ is injective on the flagged set and
Borel by Step 2, so — both $\mathcal J\times\mathbb R$ and $[0,\bar b]^2\times\{1\}$ being Borel
subsets of Polish spaces — Lusin–Souslin gives a Borel inverse $\iota_F$ on the image, and
$\hat v(\sigma_F;k)=\mu_v+\beta\bigl(\iota_F(\sigma_F)_s-\mu_v\bigr)$ with $\beta$ the card §4.1
projection coefficient. Injectivity plus measurability already delivers the measurable inverse; no
separate assumption is introduced.

(d) Therefore $P^F(\sigma_F;k)=\mathcal G_F\bigl(\hat v(\sigma_F;k)\bigr)$ is the composition of a Borel map
with a continuous map, hence Borel. **This is the measurably selected family — built here from
h.7 and h.17-b at (c) and from Steps 7–8 at (b), not read off A5 — and it is pinned rather than
chosen: uniqueness of the root at each $\sigma_F$ leaves no freedom,
so no selection principle is invoked and no two runs of the argument can produce different
families.** (This is a statement about the *price* family given the belief; the sense in which the
flagged *belief* is pinned is Step 10's, and is weaker — a version, not a forcing.) The turn-2 audit flagged (D1-R2) that D1 Step 11 and L2 Steps 8–9 both consume this
reading; P1 consumes it here, at the point where the flagged price enters the blockholder's payoff.

**Step 7 (under h.12 the inner root exists and is unique by derivation — which is why A5 is not a
hypothesis of P1 and h.5 is struck).**
Write $A=\hat v+\pi\Delta_V$ and $\varrho(P)=\mathcal P_{\mathcal I}(P)-P=(1-p(P))(A-P)+p(P)\bar m$,
continuous in $P$ because $\Phi$ is. By h.12, $\bar m\ge 0$.

(i) *No root below $A$.* For $P<A$ both terms of $\varrho$ are nonnegative and the first is strictly
positive since $p(P)<1$ (Step 4), so $\varrho(P)>0$.

(ii) *A root exists.* $\varrho(A)=p(A)\bar m\ge 0$. If $\bar m=0$ then $P=A$ is a root. If $\bar m>0$,
then $\varrho(A)>0$; and as $P\to+\infty$, $p(P)\to 0$ while $(A-P)\to-\infty$, so $\varrho(P)\to-\infty$.
An explicit bracket: for $P\ge\bar S-K-\bar m+\sigma_\xi$ one has $p(P)\le 1-\Phi(1)<0.159$, whence
$\varrho(P)\le 0.159\,\bar m-0.841\,(P-A)\le 0$ once additionally $P\ge A+0.19\,\bar m$. The
intermediate value theorem on $[A,\max\{\bar S-K-\bar m+\sigma_\xi,\ A+0.19\bar m\}]$ gives a root.

(iii) *The root is unique.* $\varrho$ is differentiable with
$\varrho'(P)=p'(P)\bigl(P+\bar m-A\bigr)+p(P)-1$, and $p'(P)=-\phi\bigl((P+K+\bar
m-\bar S)/\sigma_\xi\bigr)/\sigma_\xi<0$. At any root, (i) gives $P\ge A$, so
$P+\bar m-A\ge\bar m\ge 0$ and the first term is $\le 0$; the second is $<0$ since $p<1$. Hence
$\varrho'<0$ **strictly at every root**. Suppose two roots $P_1<P_2$ with no root between them.
$\varrho'(P_1)<0$ forces $\varrho<0$ immediately to the right of $P_1$, and since $\varrho$ has no zero on
$(P_1,P_2)$ it is negative throughout that interval; $\varrho'(P_2)<0$ forces $\varrho>0$ immediately to
the left of $P_2$. The two conclusions contradict each other, so there is at most one root.

Consequently, on the maintained sign h.12 the existence-and-uniqueness content of A5 is a theorem
rather than an assumption, and Step 8 adds its continuity-in-the-belief content. What is left over is
continuity of the *composition* in the conjecture $k$, which runs through the conditioning
$(\hat v,\pi)$ rather than through the pricing map; Step 15 takes that up and says where it is
assumed. This is why h.5 is struck rather than retained in weakened form.

**Step 8 (the inner root is monotone and non-expansive in the belief, which is the object the
numerical check can hit).**
At the root, $\varrho'<0$ (Step 7(iii)), so the implicit function theorem applies to
$\varrho(P;\hat v)=0$ and yields
$$
\frac{\partial P}{\partial\hat v}
=\frac{1-p}{\,1-p+|p'(P)|\,(P+\bar m-A)\,}\;\in\;(0,1],
$$
the denominator being at least $1-p>0$ by h.12 and Step 7(i). The bound is used in NUMERICAL CHECK
REQUEST item 3.

### Part C — beliefs, on path and off

**Step 9 (pooled off-path beliefs as limits of full-support perturbations, on the reachable history
set — stated for every $\kappa\in[0,1]$, endpoints included).**
Card §3(vi) requires off-path beliefs to be limits of full-support perturbations. Index the
perturbation by $n$: at stage $n$ every signal type plays every plan $j\in\mathcal J$ with weight at
least $1/n$, the remaining mass following $j_k$.

*(a) The alphabet, said honestly.* Card §4.1's noise law is $\Pr(z_d=0)=1-\kappa$ and
$\Pr(z_d=\pm\bar z)=\kappa/2$ on the in-domain range $\kappa\in[0,1]$, so the **realised** support is
$$\mathrm{supp}(z_d)=\{0\}\ \text{at }\kappa=0,\qquad \{-\bar z,+\bar z\}\ \text{at }\kappa=1,\qquad
\{-\bar z,0,+\bar z\}\ \text{at every }\kappa\in(0,1).$$
No conflict with h.2: h.2's $\{-\bar z,0,+\bar z\}$ is the noise **alphabet**, finite at every
$\kappa$ and the only thing Step 3's finiteness argument needs; $\mathrm{supp}(z_d)$ is the subset of
that alphabet carrying positive probability at the maintained $\kappa$, and it is the object a
zero-probability argument has to be quantified over.
Call a pooled history $\mathcal H_d^P=(X_0,\dots,X_d;\text{flag landed by }d)$ **reachable** if it
carries strictly positive probability under some plan and a positive-probability set of signals:
some $j\in\mathcal J$ and some Borel $S$ with $\Pr(s\in S)>0$ such that
$X_{d'}-q_{jd'}(s)\in\mathrm{supp}(z_{d'})$ for every $d'\le d$ and every $s\in S$, with the flag
coordinate agreeing with $\mathbf 1\{f_j(s)\le d\}$. Reachability is a property of the menu and the
noise law alone: it does not depend on the conjecture $k$ and it does not depend on $n$, because the
perturbation gives every plan weight at least $1/n>0$ at every type and the noise law is common
across plans. This is the whole-history form, and it is what the argument needs — a history each of
whose marks is individually attainable under *some* plan need not be attainable under any *one*
plan.

*(b) The limit exists at every reachable history — and it is the limit of the **joint** $(j,s)$
posterior, not merely of the posterior over plans.* Write
$$w_n(j\mid s)=(1-t_n)\,\mathbf 1\{j=j_k(s)\}+\tfrac{t_n}{J},\qquad t_n:=\tfrac Jn\downarrow0,$$
for the stage-$n$ mixing
weight — every plan carries at least $t_n/J=1/n$, which is Step 9's own parameterisation of the
perturbation, and $t_n$ is written for the perturbation mass because $\varepsilon$ is card §4.1's
signal noise and is not available (card §8 rule 4) — with $\varphi_s$ the signal density and
$L_j(\mathcal H_d^P\mid s)=\prod_{d'\le d}\Pr(z_{d'}=X_{d'}-q_{jd'}(s))\cdot\mathbf 1\{\text{flag
coordinate}=\mathbf 1\{f_j(s)\le d\}\}$ for the likelihood of Step 9(a). The stage-$n$ joint density
over $(j,s)$ at the history is
$$\mu_n(j,s)=\frac{w_n(j\mid s)\,L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}
{\sum_{j'\in\mathcal J}\int w_n(j'\mid s')\,L_{j'}(\mathcal H_d^P\mid s')\,\varphi_s(s')\,
\mathrm ds'}.$$
By h.2 the plan menu is finite and by Step 3 the pooled history alphabet is finite, so numerator and
denominator are finite sums of terms
polynomial in $1/n$ with coefficients that do not depend on $n$. At a reachable history the
denominator is strictly positive for every $n$: the witnessing pair $(j,S)$ contributes at least
$(1/n)\int_S L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)\,\mathrm ds$, strictly
positive because each factor is positive on $S$ by the definition of reachability and, by h.2, the
mark $q_{jd'}(\cdot)$ takes finitely many values, so $L_j$ takes finitely many positive values
on $S$ and is bounded below by their minimum; every other term in the denominator is nonnegative.
A ratio of polynomials in $1/n$ with a denominator that is nonzero
for all large $n$ converges as $n\to\infty$, **pointwise in $(j,s)$**, and the limit is the
plan-uniform-weighted joint law restricted to the history. This is where h.2's
finiteness pays: with a continuum of pooled histories the limit would need a separate argument.

The joint form is what the step must deliver, not a flourish (pass-1 finding 4): Step 4 shows the
pricing map depends on the information set through $(\hat v,\pi)$, and while $\pi$ is a functional of
the *plan* posterior alone, $\hat v(\mathcal I)=\mathbb E[v\mid\mathcal I]$ is a functional of the
**signal** posterior. Integrating $s$ out first would deliver $\pi$ and leave $\hat v$ undefined.
Passing from $\mu_n$ to $\hat v$: $\hat v_n=\sum_j\int\bigl(\mu_v+\beta(s-\mu_v)\bigr)\mu_n(j,s)\,
\mathrm ds$,
and $\mu_n\to\mu_\infty$ pointwise. **The envelope needs a case split on the denominator $Z_n$, and
here it is (retry finding 4):** write $Z_n=(1-t_n)\Lambda_k+(t_n/J)\Lambda_u$ for
the denominator — the display above with $w_n$ expanded — where
$\Lambda_k=\int L_{j_k(s')}(\mathcal H_d^P\mid s')\varphi_s(s')\,\mathrm ds'$ is the unperturbed
aggregate, $\Lambda_u=\sum_{j'}\int L_{j'}(\mathcal H_d^P\mid s')\varphi_s(s')\,\mathrm ds'$ the
plan-uniform one, and $t_n=J/n$ the perturbation mass. *If $\Lambda_k>0$* — the history is on path under
$k$ — then $Z_n\ge\Lambda_k/2$ for all large $n$, and $2\lvert\mu_v+\beta(s-\mu_v)\rvert\varphi_s
L_j/\Lambda_k$ is an integrable envelope by h.17-d's Gaussian tail and h.2's integrability clause, so
dominated convergence applies. *If $\Lambda_k=0$* — the $k$-null case — the $(1-t_n)$ term
vanishes $\Phi_s$-a.e. in numerator and denominator alike, so $\mu_n=L_j\varphi_s/\Lambda_u$ **exactly
and $n$-free**, and there is nothing to pass to the limit. (Without the split the bare claim would be
false as stated: $\mu_n\le\varphi_sL_j/Z_n$ with $Z_n\downarrow0$ is not a uniform envelope.) Either
way $\hat v_n\to\hat v_\infty$ and, by Step 8's 1-Lipschitz bound, the prices converge
with them. Hence the limiting belief **and the limiting price** exist at every reachable
pooled history, on path and off, and on path the belief agrees with the Bayes posterior.
*Load-bearing where it is least obvious:* Step 13 evaluates $U_j(s;k)$ for **every** $j\in\mathcal J$,
including plans carrying zero probability under $k$ on a collapse face, whose pooled-execution
bracket reads prices at $k$-null histories — so those prices must be defined, not merely
constrained.

*(c) Unreachable histories carry no requirement; a convention makes the payoff defined at every
signal anyway.* An unreachable history
has probability zero under **every** plan profile, perturbed or not — it is null under nature, not
off path under the players — so card §3(vi) asks nothing of it and card §3(iv) prices nothing there.
Almost everything downstream is already clear of them: Step 11's pooled-execution bracket integrates
$P_d^P(\mathcal H_d^P)$ against the law of $z_{0:H}$ under the plan actually played, which for
$\Phi_s$-almost every $s$ puts mass only on reachable histories, and the same holds for every
deviation in h.11's action set, since those share $j$'s pooled path.

**The exceptional signals, said plainly (pass-1 finding 6).** Reachability in (a) requires a
*positive-probability* signal set. The joint mark-and-flag vector
$\bigl((q_{jd'}(s))_{d'\le d},\mathbf 1\{f_j(s)\le d\}\bigr)$ takes finitely many values (h.2), so its
level sets partition $\mathbb R$ into finitely many Borel cells — and a particular cell may be
$\Phi_s$-null while being nonempty. At such an $s$, plan $j$'s own realised pooled histories are
unreachable and Step 11's bracket would read a price that (b) has not defined. **Convention adopted
here:** fix once and for all a **reference belief** $(\hat v_\circ,\pi_\circ)$ — for definiteness the
prior pair $\bigl(\mu_v,\Pr(a=1)\bigr)$, and any other admissible pair does equally — and assign to
every unreachable pooled history the **inner root at that belief**, i.e. the unique
$P_\circ$ with $\mathcal P_{(\hat v_\circ,\pi_\circ)}(P_\circ)=P_\circ$, which exists and is unique by
Step 7 under h.12. Then $U_j(s;k)$ is defined at **every**
$(j,s,k)$, and no §3 item is touched: §3(iii), §3(iv) and §3(vi) constrain beliefs and prices only at
histories carrying positive probability under some profile, and these carry none.
*The reference-belief form matters, and $\mathbb E[Y]$ will not do (retry finding 3).* This step
first adopted $P_d^P:=\mathbb E[Y]$ on the strength of card §4.3's $P_{-1}^P$ convention. But
$\mathbb E[Y]$ — an unconditional average of realised control-node values — is in general **not** a
root of $\mathcal P_{\mathcal I}$ at any belief, so the constructed object would have carried prices
that are not inner fixed points at nodes where the blockholder does trade, while the card row's
conclusion clause says "prices at their inner fixed points" without qualification. The §4.3 precedent
does not transfer: $P_{-1}^P$ is the pre-trading node, a different object. With the reference-belief
root, **every price in the constructed object is an inner fixed point at the belief carried there**,
and the row's clause is literally true everywhere. The choice is not
innocuous in one narrow respect and the file does not pretend otherwise: it can change $U_j(s;k)$ on a
$\Phi_s$-null set of signals, hence can move $\mathcal T_i(k)$, which is an infimum over a pointwise
condition. What follows is that the theorem is an existence statement **about the object built from
this fixed convention** — a different admissible convention yields another equilibrium, not a failure
of this one (NOT CLAIMED 13).

*(d) The $\kappa$ boundary (audit Finding 1(c)).* The pre-repair text asserted that "every noise mark
carries positive probability whenever $\kappa>0$", with $\kappa=0$ special-cased. That is **false at
$\kappa=1$**, which is in-domain: there $\Pr(z_d=0)=0$, and a pooled history requiring a zero mark is
null under every plan profile, so the plan-only perturbation leaves its limit belief undefined —
exactly the mirror of the $\kappa=0$ case, where only the zero mark survives. Parts (a)–(c) replace
both special cases with one sentence quantified over $\mathrm{supp}(z_d)$, and the claim therefore
holds on the card's **full domain $\kappa\in[0,1]$, both endpoints included**, with no restriction to
$\kappa\in[0,1)$. What the endpoints change is *which* histories are reachable, never whether the
reachable ones carry a limit. Note the correction runs the other way too: the pre-repair claim
"the limiting belief exists at every pooled history" was false as stated at $\kappa\in\{0,1\}$, so
naming the reachable set is a repair of a false assertion, not a retreat from a true one.

**Step 10 (the flagged belief is the point mass at the generating pair — a version, at every image
tuple, and the one this equilibrium selects).**
By h.7 the map $(j,s)\mapsto\sigma_F$ is injective on the flagged set, so each flagged tuple in its
image is generated by exactly one pair $(j,s)$, and $\iota_F$ of Step 6(c) returns it.
**The version, stated explicitly (pass-1 finding 5).** The signal is Gaussian (h.17-d), so the pair
$(j,s)$ carries probability zero under every stage-$n$ perturbation — what carries positive weight is
the *plan* conditional on the type. A conditional law given $\sigma_F$ is therefore defined only up to
$\Phi_s$-null sets, and the sentence "that pair has strictly positive weight, so the perturbed
posterior at $\sigma_F$ places probability one on $\iota_F(\sigma_F)$" — which this file carried
before 2026-08-25 — applies a positive-probability argument to a null event. What is true, and is all
that is needed: because $\iota_F$ is a genuine pointwise Borel map, $\delta_{\iota_F(\sigma_F)}$ is a
**version** of the regular conditional law given $\sigma_F$ at every stage $n$ — the defining
disintegration identity holds tuple by tuple, since the conditioning $\sigma$-field separates the
generating pairs — and it is invariant in $n$, so it is also its own limit. This proof **selects that
version**, at every tuple in the image; any $\Phi_s$-a.e.-equal version satisfies card §3(iii) and
§3(vi) equally well, and nothing below distinguishes them. So "pinned" is a statement that the
point mass is available and forced up to null sets, not that no other version exists — the same hedge
`proofs/A7_construction.md` NOT CLAIMED already carries ("pinned only up to null sets"). Therefore the
flagged belief is $\hat v(\sigma_F)=\mu_v+\beta(\iota_F(\sigma_F)_s-\mu_v)$ at every image tuple,
on path and off, and Step 6's family is simultaneously the on-path Bayes family and the off-path
limit family. **What "off path" covers here, said precisely (batch-1 audit P1-R3).** It covers flagged
tuples generated by $(j,s)$ pairs the conjecture $k$ does not select. It does *not* by itself cover
tuples outside the **image** of $(j,s)\mapsto\sigma_F$ — the tuples a round-2 deviation to an
off-menu order would produce — and no step assigns those a belief. This step stands on **h.11**: under
h.11 the round-2 action set is the plan-generated set, so no such tuple arises, and the image
exhausts the flagged tuples that can be reached. Step 17(vi) inherits the pinning on that reading and
on no other. Off-path beliefs at flagged nodes carry no free parameter — a consequence of h.7
worth recording, since it removes the usual arbitrariness in item (vi) of card §3 at exactly the
nodes the paper's disclosure mechanism runs through. By h.1 the pair $(v,\xi)$ remains conditionally
independent of the pooled residual given $s$, so nothing further is needed to price the node.

### Part D — sequential optimality

**Step 11 (the blockholder has exactly two decision points, and the flagged continuation is
deterministic given $(j,s)$).**
Card §2 places the plan choice at date 0 and, when $D=1$, the flagged order $Q^F$ in round 2, with
no within-window re-optimisation in between (h.10(i)). So there is no pooled decision node after date
0: item (ii) of card §3, read on the pooled component, is satisfied by the timing itself rather
than by an argument, and the only genuine sequential-optimality requirement is the round-2 order.
Two features of the decomposition below are **h.10(ii)**, the flag-terminates-the-pooled-round clause,
and not h.10(i): that the pooled execution runs over $d\le f_j$ and stops there, and that
$Q_j^F=b_j^*(s)-B_j^F(s)$ is the blockholder's whole residual position (pass-1 finding 9).

On the flagged branch, by Step 2 the objects $B_j^F(s)$ and $Q_j^F(s)$ are deterministic in
$(j,s)$; by Step 6 the flagged price $P^F$ is a function of $\sigma_F$ alone and hence deterministic
in $(j,s)$; and by card §4.3 the control-node price on that branch is $P^F$. The blockholder payoff
of **h.14** — $U_j(s)=\mathbb E[b_j^*(s)Y-\mathcal C_j^{\mathrm{trade}}-a_jC_j(s)\mid s,j]$, now
card §4.3's $U_j$ row and transcribed at h.14 — therefore splits as
$$
U_j(s;k)\;=\;\underbrace{b_j^*(s)\,\mathbb E\bigl[Y\mid s,j,D=1\bigr]-P^F(\sigma_F)\,Q_j^F(s)-a_jC_j(s)}_{\text{flagged continuation: deterministic in }(j,s)}
\;-\;\underbrace{\mathbb E_{z}\Bigl[\textstyle\sum_{d\le f_j}P_d^P\bigl(\mathcal H_d^P\bigr)\bigl(B_j(s,d)-B_j(s,d-1)\bigr)\Bigr]}_{\text{pooled execution: determined by the pooled path alone}} ,
$$
where the pooled expectation is over the noise $z_{0:H}$ only. **On the flagged branch $a_j=1$ by
h.4**, so the engagement term of the first bracket is $C_j(s)$ and the $a_j$ factor — carried here to
match card §4.3's display (audit Finding 1, citation nit) — changes nothing in Steps 12–13. By Step
9(c), for $\Phi_s$-**almost every** $s$ every pooled history the second bracket weighs is reachable,
so the prices it reads are the ones Steps 5 and 9 supply; at the exceptional signals — the
$\Phi_s$-null cells named there — it reads Step 9(c)'s conventional price instead, which is itself an
inner root and which is what keeps $U_j(s;k)$ defined at every $s$ for Step 13's pointwise argmax.
*(Qualifier added in the finishing round, retry finding 2: this sentence had been left unqualified
when P1-R22 rewrote Step 9(c), and Step 13 already carried the correct reading.)* The noise enters the first bracket
nowhere: $\mathbb E[Y\mid s,j,D=1]$ depends on $(v,\xi)$ and on $P^F$, and $\xi$ is independent of
$z$ by h.1 while $P^F$ is $z$-free by Step 6.

**Step 12 (the flagged component is sequentially optimal at *every* flagged pair, selected or not:
price invariance, cancellation, and h.16 — and nothing in A1–A7 does this).**
*Restructured 2026-08-25 (round 2) on pass-1 finding 1 and pass-2 R16–R17. The pre-round-2 argument
ran the deviation back to date-0 optimality and therefore reached only the flagged nodes on the
selected plan; h.11 defines an action set $\mathcal Q_j(s)$ at **every** flagged pair, and a date-0
deviation to a non-selected plan that flags creates a genuine round-2 information set carrying card
§3(ii). The argument below discharges the requirement at all of them, and it does so **without
appealing to date-0 optimality**, which is exactly what lets it cover the non-selected nodes.*

Fix a flagged pair $(j,s)$ — no assumption that $j=j_k(s)$ — and let $j'$ range over the class
generating h.11's action set: $j'$ agrees with $j$ on the pooled path up to $f_j(s)$ and
$a_{j'}=a_j$. The shared path forces $c_{j'}(s)=c_j(s)$, hence $f_{j'}(s)=f_j(s)$ and
$B_{j'}^F(s)=B_j^F(s)$ (Step 2, h.9); $a_{j'}=a_j=1$ on the flagged set (h.4). So the deviation's
flagged tuple is $\sigma_F(j',s)=(B_j^F(s),Q_{j'}^F(s),1)$ — in the image of the flagged-pair map,
where Step 10 applies — and it differs from $\sigma_F(j,s)$ in the $Q^F$ coordinate alone.

**(a) The flagged price does not move across the class.** By Step 10 the belief at $\sigma_F(j',s)$
is the point mass at $(j',s)$, so $\hat v(\sigma_F(j',s))=\mu_v+\beta(s-\mu_v)$ — a function of $s$
alone, the same for every class member — and $\pi=1$ on the flagged cell (Step 6(a)), so
$\bar m=m_1$. By Step 4 the inner pricing map depends on the information set only through
$(\hat v,\pi)$. Hence
$$P^F\bigl(\sigma_F(j',s)\bigr)=\mathcal G_F\bigl(\hat v(s)\bigr)=:P^F(s)\qquad\text{for every }j'
\text{ in the class:}$$
**the round-2 order carries no price impact across the menu.** Uniqueness of the inner root (Step 7)
is what makes $P^F(s)$ a number rather than a selection.

**(b) At a flagged node the blockholder values a share at exactly $P^F(s)$.** The blockholder knows
$(j,s)$ and the realised pooled history; given $(j,s)$ the latter is a function of $z_{0:f_j}$
(Step 2), and $z\perp(v,\varepsilon,\xi)$ by h.1, so it carries no information about $Y$:
$\mathbb E[Y\mid s,j',\mathcal H_{f^-}^P,D=1]=\mathbb E[Y\mid s,j',D=1]$. By h.1 again $\mathsf B$ is a
function of $\xi$ alone given the $\sigma_F$-measurable $P^F$, so with $p=p(P^F(s))$ from Step 4,
$$\mathbb E[Y\mid s,j',D=1]=(1-p)\bigl(\mathbb E[v\mid s]+\Delta_V\bigr)+p\bigl(P^F(s)+m_1\bigr).$$
**A7-J makes the market's flagged posterior the blockholder's own** — $\hat v(\sigma_F(j',s))
=\mathbb E[v\mid s]$ by (a) — so the right-hand side is $\mathcal P_{\mathcal I}(P^F(s))$ at the
flagged information set, which equals $P^F(s)$ because $P^F(s)$ solves the inner fixed point (Steps 4,
6). Hence
$$\mathbb E\bigl[Y\mid s,j',\mathcal H_{f^-}^P,D=1\bigr]=P^F(s).$$
There is no informational rent left in round 2: full separation is what A7-J buys, and this is what
it costs.

**(c) The $Q^F$ terms cancel.** The flag terminates the pooled round (h.10), so at round 2 the pooled
execution is complete, sunk, and common to every class member — Step 11's second bracket $E_j(s;k)$,
which the shared path makes identical across the class for every noise draw. The continuation of
choosing $Q_{j'}^F(s)$ is the terminal position valued at the control node, less what the flagged
order costs, less the engagement cost the deviator bears:
$$V(j')=\bigl(B_j^F(s)+Q_{j'}^F(s)\bigr)\,\mathbb E[Y\mid\cdot]\;-\;P^F(s)\,Q_{j'}^F(s)\;-\;
\text{(engagement cost)}\;=\;B_j^F(s)\,P^F(s)\;-\;\text{(engagement cost)},$$
using (b) for $\mathbb E[Y\mid\cdot]=P^F(s)$ and (a) for the price at the deviation tuple. **Every
appearance of $Q_{j'}^F$ has cancelled, and with it every appearance of $b_{j'}^*$**: the class
member's identity survives only through the engagement cost. In Step 11's notation the same
computation reads $G_{j'}(s;k)=B_j^F(s)P^F(s)$ for every class member, so on flagged plans
$U_{j}(s;k)=B_j^F(s)P^F(s)-C_j(s)-E_j(s;k)$.

**(d) h.16 closes it, and the conclusion is convention-free.** The card does not say at which date
$C_j(s)$ is incurred, so the engagement cost in (c) is $C_{j'}(s)$ under the **plan-completion**
convention (submitting $Q_{j'}^F$ is completing plan $j'$ and paying its engagement cost) and
$C_j(s)$ under the **sunk** convention (the filing has landed and $D=1\Rightarrow a=1$ is public by
h.4, so the engagement cannot be unmade). Under the sunk convention $V$ is constant on the class
outright. Under the plan-completion convention **h.16** gives $C_{j'}(s)=C_j(s)$ and $V$ is constant
again. Either way
$$V(j')=B_j^F(s)\,P^F(s)-C_j(s)\qquad\text{for every }j'\text{ in the class,}$$
so every element of $\mathcal Q_j(s)$ — the specified $Q_j^F(s)$ included — attains the maximum.
**The flagged component is sequentially optimal at every flagged pair $(j,s)$, on the selected plan
and off it**, which is card §3(ii)'s flagged half in full. $\square$

**Where h.16 bites, exactly.** Under the sunk convention h.16 is not consumed at this step. Under the
plan-completion convention: at a **selected** $j$, date-0 optimality would already do the work — by
(c) $U_{j'}=B_j^FP^F-C_{j'}-E_j$ within the class, so "$U_j\ge U_{j'}$" *is* "$C_j\le C_{j'}$", which
is what defeats the deviation — but at a **non-selected** flagged pair there is no date-0 optimality
to appeal to, and without h.16 the deviator strictly prefers the class member with the smallest
$C_{j'}(s)$. So h.16's bite is precisely: **PBE at flagged nodes off the equilibrium plan under the
plan-completion convention**, and it is what makes the conclusion hold under both conventions without
this proof adjudicating a card silence. It stays vacuous on any single-Voice menu (singleton class)
and a restriction only on menus with two or more Voice plans sharing a pooled path (WHERE IT FAILS 7).

**Refutation note: a shared-path class on which the *trading* terms differ cannot be built.** A
witness that fixes $G_{j'}(s;k)-G_j(s;k)=\delta>0$ across a class — $G_j$ being Step 11's trading
terms — is inconsistent with card §3(iv) and §3(vi) in force: by (a)–(b), at pinned beliefs and
inner-fixed-point prices $G_{j'}=B_j^F(s)P^F(s)$ for **every** class member, so $\delta=0$
necessarily. Such a witness fixes as a primitive ($G$, equivalently a trading gain on the flagged
order) what equilibrium determines; it is available only where the flagged price is not the fixed
point of card §4.3's pricing equation, or the flagged belief is not the one A7-J pins. This disposes
of the trading-gain framing of audit Finding 1(b) that this file's own first 2026-08-25 draft
carried, and of pass-1 finding 1's witness: **the review's arithmetic is right about the cost wedge
and about the demotion, and wrong only in locating the wedge in $G$**. It also makes the
class-argmax construction proposed as finding 1's bounded repair unnecessary — all class members tie,
so the equilibrium object is unchanged and no selection has to be specified.

The converse direction is the honest part, and it is about **h.11**, not about the argument above.
Without h.11 — if round 2 offers the full interval $[0,\bar b-B_j^F(s)]$ — an order outside the
plan-generated set produces a flagged tuple **outside the image** of $(j,s)\mapsto\sigma_F$, where
Step 10 pins nothing and no step assigns a belief; the deviation's price, and with it the whole
comparison, is then undefined until a belief is supplied, and the supplied belief decides the answer.
By (c) the on-image flagged payoff is $B_j^F(s)P^F(s)-C_j(s)$ with the order cancelled out, so an
off-image deviation is profitable or not entirely according to how the assigned off-image belief
compares with $\mathbb E[v\mid s]$ — and Step 9's plan-only perturbation constrains that choice at no
$n$. **Sequential optimality of the flagged component does not follow from A1–A7 and is not a free
consequence of complete contingent plans; h.11 is *a* sufficient condition that delivers it, and it is
a restriction on the round-2 action set rather than on the menu.** Strengthening A7 to **A7-J** does
not change this: WHERE IT FAILS 2's menu may be taken with $b^*$ strictly increasing on all of
$\mathbb R$, so it satisfies A7-J and still fails item (ii). The turn-1 statement of P1 listed "sequential optimality of the flagged component" as
its Hypothesis 6 without content; h.11 is one way of supplying that content.

**Not claimed: that h.11 is the *weakest* such condition (batch-1 audit P1-R2).** An earlier draft
said so, and the claim was not established. The textbook route to sequential rationality at an
unreached node is not a restriction on the action set at all — it is **off-path beliefs**. Card §3(vi)
requires off-path beliefs to be limits of full-support perturbations, and Step 9's perturbation
perturbs **only the plan menu** (each type plays each $j\in\mathcal J$ with weight $\ge1/n$). Round-2
orders outside the menu image are then reached at no $n$, so their limit beliefs are unconstrained by
that perturbation and the modeller may choose them. Whether some admissible choice deters every
off-menu deviation is a genuine question and not an obvious one: by Step 12(c) an off-image deviation
to $Q'$ at belief $\hat v'$ earns $B_j^F\,\mathbb E[Y\mid\cdot]+Q'\bigl(\mathbb E[Y\mid\cdot]-P'\bigr)$
less the cost, so the assigned belief moves the deviation's gain and the incumbent's own valuation at
once, in opposite directions — and **no step in this proof addresses it**. So: h.11 delivers Step 12;
whether an off-path-belief route also delivers item (ii), and whether it would be weaker, is **open**.

### Part E — the outer map and Brouwer

**Step 13 (h.3 gives a well-defined weakly ordered best-response map; A6's ordering content is a
consequence, not an assumption).**
Fix $k\in\Theta$. Steps 5, 6, 9 and 10 determine the pooled and flagged price families and the
belief system; Step 11 then determines $U_j(s;k)$ for every $j$ and $s$ — at **every** $s$, by Step
9(c)'s convention — and each $U_j(s;k)$ is finite by h.2 (A2′: locally bounded in $(s,\vartheta)$
pointwise, integrable in expectation; the struck flat bound of the old A2 is not used).
By h.3 the preferred plan is weakly increasing in $s$, so the set $\mathcal S(k)$ of **weakly
increasing selections** from $s\mapsto\arg\max_{j\in\mathcal J}U_j(s;k)$ is **nonempty** — that is
h.3's second clause. **The selection is named, not merely asserted to exist** (pass-2 N8):
$$j^\star(\cdot;k)\;:=\;\text{the largest element of }\mathcal S(k),\qquad
j^\star(s;k)=\max\{\mathfrak w(s):\mathfrak w\in\mathcal S(k)\}.$$
It exists and is itself a weakly increasing selection. *Closed under pointwise max:* for
$\mathfrak w_1,\mathfrak w_2\in\mathcal S(k)$ the map
$s\mapsto\max\{\mathfrak w_1(s),\mathfrak w_2(s)\}$ takes at each
$s$ one of the two values, both in $\arg\max(s)$, so it is a selection, and a pointwise max of two
weakly increasing maps is weakly increasing. *The supremum is attained and lies in $\mathcal S(k)$:*
$\mathcal J$ is finite (h.2), so the pointwise supremum is a maximum; fix $s$ and let
$\mathfrak w\in\mathcal S(k)$ attain it there. Then $j^\star$ is a selection because
$j^\star(s;k)=\mathfrak w(s)\in\arg\max(s)$, and it
is weakly increasing because for $s<s'$, $j^\star(s';k)\ge\mathfrak w(s')\ge\mathfrak w(s)
=j^\star(s;k)$.
So $j^\star(\cdot;k)$ is canonical, single-valued — which is what h.6 needs before it can call
$\mathcal T$ continuous — **and monotone**.

*Why not the largest maximiser (retry finding 1).* An earlier version of this step took
$j^\star(s;k):=\max\arg\max_jU_j(s;k)$ and asserted monotonicity "under h.3". That is a **non
sequitur** on this file's own reading of h.3, and the counterexample sits inside the hypothesis: let
$U_2-U_1\le0$ everywhere with equality at exactly one point $s_0$ — a tangential touch, so zero
crossings and h.3's first clause holds, and the constant selection $j\equiv1$ is weakly increasing,
so h.3's second clause holds too. The largest maximiser is then $1,\dots,1,2,1,\dots,1$: not weakly
increasing, $\{s:j^\star\ge2\}=\{s_0\}$ is not an up-set, and no cutoff vector represents it, which
would break Step 17(i). The largest **weakly increasing** selection is $j\equiv1$ there, as it should
be. Note what the change does *not* touch: Brouwer needs only the nesting below, and that holds for
any selection. Define
$$
\mathcal T_i(k;\vartheta)\;=\;\inf\bigl\{s\in[\underline s,\overline s]:j^\star(s;k)\ge i+1\bigr\},
\qquad i=1,\dots,J-1,\qquad \inf\emptyset:=\overline s .
$$
Since $\{s:j^\star\ge i+2\}\subseteq\{s:j^\star\ge i+1\}$, the infima satisfy
$\mathcal T_1(k)\le\mathcal T_2(k)\le\cdots\le\mathcal T_{J-1}(k)$, and every component lies in
$[\underline s,\overline s]$ by construction. The **corner convention** is the display's
$\inf\emptyset:=\overline s$: a plan that is optimal nowhere contributes an empty up-set and its
cutoff sits at the top of the bracket, so it simply never appears in the range of $j^\star$ (pass-2
N8's second half). Because $j^\star(\cdot;k)$ is weakly increasing, each $\{s:j^\star\ge i+1\}$ **is**
an up-set, so these infima genuinely represent it: $j^\star(\cdot;k)$ agrees with Step 1's
$j_{\mathcal T(k)}$ at every $s$ except possibly the finitely many $\mathcal T_i(k)$ at which the
up-set fails to contain its own infimum, where the two differ by the boundary convention alone —
card §3(i) pins no convention there. Hence $\mathcal T(k;\vartheta)\in\Theta$ for every
$k\in\Theta$, including on the collapse faces where consecutive components coincide and the
corresponding plan carries zero probability. **So the "maps $\Theta$ into itself" and
"weakly ordered" halves of h.6 are derived here from h.3's monotone-preferred-plan clause; what
remains genuinely assumed in h.6 is the bracket $[\underline s,\overline s]$ and the continuity of
$\mathcal T$.** Steps 14 and 15 take those two in turn.

**Step 14 (the bracket: derivable in the four-action specialisation, assumed at the card's level of
generality — said plainly).**
In the four-action version of this model that the frozen manuscript works with, the bracket is
proved rather than assumed: there the blockholder's payoff to each action is affine in the
posterior mean $\hat v(s)$ with intercepts that are bounded uniformly over conjectures (prices lie
in a bounded interval and the entry probability lies in $[0,1]$) and with totally ordered slopes,
zero for Exit, one for Hold and Quiet Voice, and strictly more than one for Public Voice; the
engagement cost is continuous, strictly positive and strictly decreasing with full range on the
half-line. Each adjacent indifference condition then equates two affine functions whose slope gap
is nonzero — except the Hold/Quiet pair, where the slopes tie and the comparison reduces to the
strictly decreasing cost schedule meeting a bounded constant — so every indifference signal is
finite and bounded uniformly in the conjecture, and taking the union over the finitely many
adjacent pairs gives one bracket that works for all of them. That argument uses the affine-in-$\hat
v$ payoff form with ordered slopes. Neither **h.14**'s payoff definition nor card §5's A3 imposes that
form on a general finite menu: A3 imposes single crossing and a monotone preferred plan only, and
h.14 fixes the accounting of the payoff without restricting its shape in $\hat v$. (Card §4.3's $U_j$
row, which absorbed h.14 on 2026-08-23, imposes nothing here either: it names only plan-locality and
integrability as the properties ever used, and neither is a shape restriction in $\hat v$.) At the
card's level of generality the common bracket is
therefore **assumed**, and it is the first of the two things h.6 is doing.

**Step 15 (continuity: this is where h.6 assumes rather than derives, and here is exactly what it is
assuming).**
$U_j(s;k)$ is continuous in $k$ for each fixed $(j,s)$: the pooled and flagged inner prices
are continuous in the cutoffs — *commentary, not a consumed hypothesis (pass-1 finding 3): this
clause read "by h.5", but h.5 is struck and this step's actual route to continuity of $\mathcal T$ is
h.6 asserting it outright at Step 16; what is derived rather than assumed is that the pricing map is
continuous in its belief arguments (Step 8), and the belief arguments move continuously with $k$ only
under (i) below* — and by Step 4 they enter $U_j$ only through $(\hat v,\pi)$, which are
ratios of integrals over signal intervals with endpoints $k$ and are continuous in $k$ wherever the
conditioning event has probability bounded away from zero; at histories of vanishing probability
the Step 9 perturbation limit supplies the value. **That is continuity in $k$ at fixed $(j,s)$, and it
is not enough**: continuity in $k$ at fixed $s$ together with continuity in $s$ at fixed $k$ is
strictly weaker than continuity in the pair, and it is the joint statement the crossing-point argument
below consumes (batch-1 audit P1-R4). Continuity of $\mathcal T$ in $k$ needs two more
things that the card does not supply:

 (i) *joint continuity*: $(s,k)\mapsto U_j(s;k)$ is continuous on
 $[\underline s,\overline s]\times\Theta$ for each $j$ — **stated as the condition, not inferred from
 the two separate continuities**. It is plausible from the structure (finitely many $j$ by h.2, the
 inner root 1-Lipschitz in the belief by Step 8, and $(\hat v,\pi)$ ratios of integrals over signal
 intervals with
 endpoints $k$), and what it needs in the signal direction is
 $s\mapsto\bigl(B_j(s,\cdot),b_j^*(s),C_j(s)\bigr)$ continuous, so
 that $s\mapsto U_j(s;k)$ is continuous. Card §4.2 imposes monotonicity on the stake path and
 nothing else; a plan that acquires a block discontinuously at a signal trigger is permitted by the
 card and makes $U_j(\cdot;k)$ jump, at which point the best-response cutoff is a jump point rather
 than a crossing point and moves discontinuously with $k$.

 (ii) *transversality*: for every adjacent pair $(i,i+1)$ and every $k\in\Theta$, the indifference
 set $\{s:U_{i+1}(s;k)=U_i(s;k)\}$ has empty interior. h.3 says the difference crosses zero "at
 most once", which does not exclude an interval on which it is identically zero; on such an
 interval the cutoff is indeterminate, and as the interval opens and closes with $k$ the selection
 $\mathcal T_i$ jumps.

**Under (i) and (ii), continuity of $\mathcal T$ follows from (i)'s joint continuity together
with the strict sign change of $U_{i+1}-U_i$ at each crossing: the sign change locates the crossing
and the joint continuity moves it continuously with $k$. That is a topological argument, not a
calculus one — the implicit function theorem is the wrong tool here, since it would need $U$
differentiable in $(s,k)$ and no hypothesis supplies that (batch-1 audit P1-R4). h.6 assumes the
conclusion instead: it asserts continuity of
$\mathcal T$ directly. That is the single largest assuming-rather-than-deriving step in this proof,
and (i)+(ii) is the weakest pair of conditions I can name that would replace it.** Note also that
(i) is not independent of h.7: a stake path that is flat on a signal interval destroys injectivity
there, which is the turn-2 audit's L2-R1 finding seen from the other side, so the card cannot buy
continuity by weakening monotonicity.

**Step 16 (Brouwer).**
By Step 1 and card §4.5's $\Theta$ row, $\Theta$ is **nonempty**, compact and convex — nonemptiness is
not decoration, since Brouwer is vacuous without it (pass-2 N9). By Step 13,
$\mathcal T(\cdot;\vartheta)$ is a **single-valued** self-map of $\Theta$ under the named
largest-weakly-increasing-selection tie-break and the $\inf\emptyset:=\overline s$ corner convention,
and this is the
reading of h.6 the step uses: h.6 asserts that $\mathcal T$, so selected, is a continuous self-map of
$\Theta$ (pass-2 N8 — a correspondence cannot be called continuous, so the selection must be named
before the hypothesis can be applied). Brouwer's fixed-point theorem then gives $k^\star\in\Theta$ with
$k^\star=\mathcal T(k^\star;\vartheta)$. The fixed point may lie on a collapse face, in which case
the corresponding plan carries zero probability; card §3's weak inequalities admit this, and it is
the shape the frozen manuscript's baseline takes when the passive action collapses.

**Step 17 (assembling the six items of card §3).**
Take $k^\star$ from Step 16 and check the definition item by item.
(i) *Weakly ordered cutoff vector.* $k^\star\in\Theta$ by Step 16, and the equilibrium plan map is
**$j^\star(\cdot;k^\star)$ of Step 13** — the **largest weakly increasing selection** from the
pointwise argmax, which is weakly increasing by construction (Step 13, and *not* by an appeal to h.3
after the fact) and is represented by $k^\star$ because a weakly increasing $\mathcal J$-valued map
has up-sets for its upper level sets. *Changed 2026-08-25 (round 2, pass-1 finding 7) from
$j_{k^\star}$, Step 1's induced map; the selection itself corrected in the finishing round from the
largest maximiser, which is not monotone in general (retry finding 1).* The two agree off the cutoff points and can differ **at** them: $\mathcal T_i$
is an infimum that need not be attained, so at $s=k_i^\star$ one may have
$j^\star(k_i^\star;k^\star)\le i$ while Step 1's $\le$ convention gives $j_{k^\star}(k_i^\star)\ge
i+1$. Card §3(i) asks for a weakly ordered vector mapping $s$ into a plan and does not pin the tie
convention at the cutoffs themselves, so taking the map to be $j^\star$ — optimal at **every** $s$ by
construction — is admissible and is what (ii) needs. **Consistency with the conjecture the prices are
built on:** Steps 5, 6 and 9 price against the conjecture $k^\star$, whose induced map is Step 1's
$j_{k^\star}$; that map and $j^\star(\cdot;k^\star)$ agree off the finitely many cutoff points, hence
$\Phi_s$-almost surely, so every conditional probability, posterior and price is the same under
either — the disagreement is invisible to (iii), (iv) and (v), which are statements about
probabilities.
(ii) *Sequentially optimal pooled and flagged components.* Pooled: no decision node after date 0
(Step 11). Flagged: Step 12 under h.11 **and h.16**, at every flagged pair, selected or not. Date-0
plan optimality: $k^\star$ is a fixed point of
$\mathcal T$ and the plan map is $j^\star(\cdot;k^\star)$, so
$j^\star(s;k^\star)\in\arg\max_j U_j(s;k^\star)$ at **every** $s$ by the definition of the selection —
no appeal to indifference at the cutoff points is needed, and none is available: indifference there
would require continuity of $s\mapsto U_j(s;k)$, which is Step 15(i), explicitly not a hypothesis and
explicitly not derived (NOT CLAIMED 11), and WHERE IT FAILS 4 exhibits a card-legal plan making
$U_j(\cdot;k)$ jump.
(iii) *Bayes-consistent on-path beliefs.* Step 9 for pooled histories of positive probability under
$k^\star$; Step 10 for flagged tuples, where injectivity supplies the point mass on
$\iota_F(\sigma_F)$ as the selected version.
(iv) *Competitive pooled and flagged prices at their fixed points.* Step 5 for the finite pooled
family and Step 6 for the measurable flagged family, both solving
$P(\mathcal I)=\mathbb E[Y\mid\mathcal I]$ by Step 4 — **at the beliefs of (iii) where the history
carries positive probability under $k^\star$, and at Step 9(b)'s limit belief at the reachable
histories that do not** (pass-1 observation 12; those are the histories the deviation payoffs of
Step 13 read, so (iv) has to reach them). At unreachable histories §3(iv) requires nothing and
Step 9(c)'s convention supplies a value.
(v) *Bidder-entry rule.* Card §4.3's $p(\mathcal I)$ is the entry probability implied by the same
$(P,\pi)$ at each control-node information set, by Step 4's derivation.
(vi) *Off-path beliefs as limits of full-support perturbations.* Steps 9 and 10.
All six hold, so the assembled object is a cutoff perfect Bayesian equilibrium.

**Step 18 (a strengthening that is not part of the claim: Kakutani removes h.6's continuity half).**
Define instead the best-response correspondence
$\mathfrak T(k)=\{k'\in\Theta:k'\text{ represents some optimal weakly increasing plan selection at
}k\}$. It is nonempty by h.3; its values are convex, because at an indifference plateau the
admissible values of a component form an interval and the ordering constraints cut the product of
those intervals by half-spaces; its values are compact, being closed subsets of the compact
$\Theta$; and its graph is closed by the maximum theorem, given that $U_j(s;k)$ is jointly
continuous in $(s,k)$ — which is exactly what Step 15(i) now states as a condition rather than
deriving. Kakutani's theorem then gives a fixed point without
Step 15(ii) and without h.6's continuity clause. This removes the transversality condition but
neither Step 15(i) nor Step 14's bracket. Card §3 fixes the Brouwer route for P1, so this is
recorded as a remark; see NOT CLAIMED.

### Part F — A8 and both cells on path

**Step 19 (A8 gives positive mass to both cells).**
At $k^\star$, h.9 makes $\mathcal C_F=\{D=1\}$ and $\mathcal C_P=\{D=0\}$ exclusive and exhaustive,
so $\Pr(\mathcal C_F)=\Omega(\kappa,\tau,T)$ and $\Pr(\mathcal C_P)=1-\Omega(\kappa,\tau,T)$ with
$\Omega$ evaluated under the equilibrium plan map $j^\star(\cdot;k^\star)$ of Step 17(i)
*(symbol updated 2026-08-25 round 2 with P1-R23; $\Omega$ is unaffected by the change, since
$j^\star(\cdot;k^\star)$ and Step 1's $j_{k^\star}$ can differ only at the finitely many cutoff
points, a $\Phi_s$-null set)*. h.8 asserts
$0<\Omega<1$, so both probabilities are strictly positive: both cells are reached with positive
probability under the equilibrium, that is, both are on path. This is also the condition under
which card §4.4's $M_F$ and $M_P$ are defined, which is what the cell decomposition needs; h.4's
$D=1\Rightarrow a=1$ makes the flagged cell an engagement cell throughout.

**Step 20 (what A8 does and does not do — said plainly).**
h.8 is a restriction on an *equilibrium object*: $\Omega$ is computed at $k^\star$, not from
primitives. No step above rules out $\Omega(k^\star)\in\{0,1\}$, and P1 therefore does not produce
an equilibrium satisfying h.8; it states that if the constructed equilibrium satisfies h.8 then
both cells are on path. Read literally, Step 19 is close to a restatement of h.8, and its content
is the consistency check that h.9's partition is non-degenerate at the fixed point.

The reformulation that gives h.8 something to bite on: suppose in addition (a) **h.15** — the
engagement flags $a_j$ are $1$ exactly on an upper set of the ordered menu — (b) $\partial_s B_j\ge0$
on Voice plans (card §4.2), and (c) h.13. Of these only (b) is card-backed; (a) and (c) are both
[ADDITION]s, numbered as h.15 and h.13 and cited here, which is the one step that consumes them. Then
the flagged set
$\{s:a_{j^\star(s;k^\star)}=1\text{ and }B_{j^\star(s;k^\star)}(s,H-T)\ge\tau\}$ — the equivalence
$f_j\le H\iff B_j(s,H-T)\ge\tau$ is h.9 — is an upper interval of signals: the first condition is
an upper set because $j^\star(\cdot;k^\star)$ is weakly increasing (Step 13's selection is the largest
weakly increasing one, so monotonicity is by construction) and h.15;
within it, $s\mapsto
B_{j^\star(s;k^\star)}(s,H-T)$ is weakly increasing because it increases in $s$ at fixed plan by (b) and
increases across plans by (c). Writing $s_F(k^\star)$ for the infimum of that upper interval,
$\Omega=1-\Phi_s\bigl(s_F(k^\star)\bigr)$ with $\Phi_s$ the signal c.d.f., and h.8 is equivalent to
$s_F(k^\star)$ being finite and strictly above $-\infty$. **Conditions (a) and (c) are h.15 and h.13,
neither of which is in the card**: the card orders the menu by aggressiveness without tying that order
either to the engagement flags (h.15) or to the stake path (h.13), so without them the flagged set
need not be an interval and $\Omega$ need not be a single-threshold object.

$\blacksquare$

---

## WHERE IT FAILS

1. **h.12 fails: the inner root is not unique at the flagged layer.** *(Retitled 2026-08-25, round 2:
   the case used to be filed under h.5, which is now struck — with A5 no longer assumed, nothing in
   the hypothesis set can be invoked to restore uniqueness, so this case is if anything sharper.)*
   Let $m_0<0$ be large enough
   in absolute value that $\bar m=m_0+\Delta_m<0$ on the flagged cell. Then Step 7(i) breaks, roots
   below $A$ become possible, and $\varrho$ can dip below zero, rise, and fall again — three roots at a
   positive-measure set of flagged tuples. A measurable selection still exists (the root
   correspondence is closed-valued and measurable, so Kuratowski–Ryll-Nardzewski applies), but it is
   no longer unique. Distinct selections give distinct $\mathcal T$ and distinct fixed points, so P1
   becomes selection-dependent; worse for the paper, a selection that varies with $\kappa$ destroys
   the flagged-cell invariance that L2 needs, since L2's Step-9 analogue relies on the fixed point
   being pinned rather than picked.
2. **h.11 fails: round 2 offers orders the menu does not generate.** Suppose the model gives the
   blockholder the full interval $[0,\bar b-B^F]$ in round 2 rather than the plan-generated set
   $\mathcal Q_j(s)$. Take
   $\mathcal J=\{\text{Exit},\text{Hold},\text{one Voice plan}\}$ with the Voice plan's terminal
   target $b^*(s)$ chosen for its pooled-execution properties, **and extend the flagged pricing
   schedule to off-image orders by any rule under which the market's posterior mean at
   $(B^F,Q',a{=}1)$ falls short of $\mathbb E[v\mid s]$ for some feasible $Q'$** — the extension is
   the modeller's to choose, since Step 10 pins nothing off the image and Step 9's plan-only
   perturbation reaches no such tuple (Step 12's converse paragraph). Then the round-2 problem
   $\max_{Q}\ b^*Y-P(F,Q)Q$ has a first-order condition that the single plan-generated
   $Q^F=b^*-B^F$ generically does not satisfy, and the improving $Q'$ is available.
   *(Clause added 2026-08-25 round 2: on the plan-generated set no such gain can exist — Step 12(c)
   cancels the order out — so this case is genuinely about what happens off the image, and it needs
   the extension named rather than assumed into existence.)* The fixed point of $\mathcal T$ then exists and satisfies items
   (i), (iii)–(vi) of card §3 but fails item (ii) at the flagged node: it is a date-0 equilibrium,
   not a PBE. This is one of the two concrete cases in which P1's claim is false as stated under
   A1–A7 alone — case 7 is the other — and it survives the strengthening of A7 to A7-J: take the
   Voice plan's $b^*$ strictly increasing on all of $\mathbb R$ and A7-J holds on the menu while
   item (ii) still fails.
3. **h.6's continuity fails through an indifference plateau (Step 15(ii)).** Let the engagement cost
   $C_j(s)$ be constant on a signal interval $[s_1,s_2]$ and let the conjecture be such that
   $U_{i+1}(\cdot;k)-U_i(\cdot;k)\equiv 0$ there. Every $k_i\in[s_1,s_2]$ represents a best
   response, and as $k$ moves the plateau opens and closes, so $\mathcal T_i$ jumps and Brouwer does
   not apply. The Kakutani route of Step 18 survives this case; the Brouwer route the card fixes
   does not.
   **Plateaus are structural, not exotic, on exactly the menus h.16 is for (retry finding 5).** By
   Step 12(c), $U_{j'}(s;k)=B_j^F(s)P^F(s)-C_j(s)-E_j(s;k)$ is the *same function of $s$* for every
   member of an h.11 deviation class: the shared pooled path gives a common $B^F$ and a common $E$,
   and h.16 gives a common $C$. So on any multi-Voice menu carrying two **adjacent** class members,
   $U_{i+1}-U_i\equiv0$ on the whole flagged region — Step 15(ii)'s transversality fails
   *identically*, not on a knife-edge, and the failure is co-extensive with the configuration h.16
   exists to handle. This is **not** a break in the proof: h.6 asserts continuity of $\mathcal T$
   outright (Step 16) and Step 13's largest-weakly-increasing selection is single-valued across the
   plateau. But it should be said plainly that **h.6 is being assumed at a configuration where its own
   named sufficient condition (Step 15(i)+(ii)) provably fails**, so on multi-Voice shared-path menus
   h.6 is doing more work than Step 15 makes it look like it is doing.
4. **h.6's continuity fails through a discontinuous stake path (Step 15(i)).** A Voice plan that
   acquires a fixed block the moment $s$ exceeds a trigger $s_0$ is permitted by card §4.2's
   monotonicity-only restriction. Then $B_j(\cdot,d)$, $b_j^*$, $B^F$, $Q^F$ and $U_j(\cdot;k)$ all
   jump at $s_0$; the best response is defined by a jump rather than a crossing and $\mathcal T$ is
   not continuous. The same plan makes the flagged tuple constant on the flat stretches on either
   side of $s_0$, so h.7's injectivity fails there too — the two failures are one failure.
5. **h.3 fails: two crossings.** Suppose the engagement cost is non-monotone in $s$, so that Exit is
   optimal at very low signals, Hold in a middle band, Quiet Voice above it, but Exit again in a
   thin band where an execution cost spikes. The preferred plan is not weakly increasing, the best
   response is not a cutoff partition, and $\Theta$ is the wrong domain: Step 13's construction
   returns a vector that does not represent the best response, so its fixed point is not an
   equilibrium.
6. **h.8 fails at the fixed point.** Set $\tau>\bar b$. No plan can cross, so $D\equiv 0$,
   $\Omega(k^\star)=0$, the flagged cell is off path, $M_F$ is undefined, and Steps 6, 10 and 12 are
   vacuous. The equilibrium of Step 17 still exists; only the "both cells on path" half of the
   claim fails. Symmetrically, a menu on which every plan is Voice and crosses gives $\Omega=1$ and
   an empty pooled cell.
7. **h.16 fails: two Voice plans share a pooled path at different engagement costs.** Take an
   admissible menu with Voice plans $j\ne j'$ agreeing on the pooled path up to $f_j(s)$ and
   differing only in the flagged order — then h.11's deviation class at $(j,s)$ is a genuine pair,
   not a singleton — with $C_j(s)=0.99$ and $C_{j'}(s)=0.01$, and adopt the plan-completion
   convention (α) of h.16. By Step 12(a)–(c) the flagged price is common to the class and the order
   cancels, so the continuations are $V(j)=B_j^F(s)P^F(s)-0.99$ and $V(j')=B_j^F(s)P^F(s)-0.01$: the
   deviation to $Q^F_{j'}(s)$ gains $0.98$. Nothing upstream is disturbed — Step 13's construction
   and Brouwer run unchanged and the fixed point satisfies items (i), (iii)–(vi) of card §3 — and
   item (ii) fails at the flagged node, so the object is a date-0 equilibrium, not a PBE. Two things
   to keep straight. *First*, this is the GPT end review's arithmetic (audit Finding 1(b)) with the
   wedge in the **engagement cost**, which is where equilibrium leaves room for one; a witness that
   put the wedge in the trading terms would not be constructible (Step 12's refutation note).
   *Second*, at a **selected** $j$ date-0 optimality forces $C_j\le C_{j'}$ and kills this deviation,
   so the live failure is at flagged pairs the cutoff vector does not select — pass-1 finding 1's
   node class — which is precisely the range of nodes Step 12 now covers and h.16 now pays for. It is
   **vacuous on any single-Voice menu**, the pinned pro-rata menu included, where $a_{j'}=a_j=1$
   forces $j'=j$; that is why the paper's instance is untouched by it. Under convention (β) the case
   is empty, which is the sense in which h.16 buys convention-freeness rather than the theorem.

---

## LABEL CLAIMED

**PROVED** — as of the ticket-35 close-out, 2026-08-25. *This section read CONJECTURE from
2026-08-21 through the two repair rounds of 2026-08-25; the three reasons it gave are kept below,
each annotated with how it was discharged, because the record of why the label was withheld is worth
more than a clean slate.*

The label rests on **the two 2026-08-25 passes over the amended statement**, not on this document's
say-so: an adversarial proof-read **PASS, 0 FAIL** (`threads/2026-08-25_P1_proofread_retry.md`, whose
reader verified Step 12's lemma part by part and recorded his own round-1 FAIL witness as refuted on
the merits) and an independent statements-only re-derivation **PASS-WITH-CHANGES**
(`rederive/P1_rederivation_2026-08-25.md`, a fresh agent working from the card row alone, whose
changes 1–5 are folded into the row and whose change 6 is withheld for Austin). Both agents are
fresh and neither wrote this proof. The move itself is the orchestrator's, logged in
`LABEL_LEDGER.md`; what this file claims is that the gate the card §7 protocol specifies has been
met for **the statement now in the card's P1 row** — which is the precise thing the 2026-08-21 chain
did not do.

1. Card §7: a label moves only on an executed check or an independent re-derivation, never on
   prose. This document is prose. The card's ledger carries P1 at CONJECTURE and this proof does not
   touch the ledger. **Discharged 2026-08-25 by the two passes, not by this file**: the independent
   re-derivation and the adversarial proof-read both landed, and the orchestrator made the ledger
   move. The rule stands exactly as written — nothing in this section moved the label.
2. The proof consumes hypotheses that are not card §5 assumptions — **h.11** (the round-2 action set
   is the plan-generated set) and **h.16** (continuation-cost equivalence on that set) — plus h.13
   and h.15 for the Step 20 reformulation. "Under A1–A7" was never an accurate antecedent for this
   proof, because sequential optimality of the flagged component (item (ii) of card §3) is not among
   A1–A7's consequences (Step 12, WHERE IT FAILS 2 and 7). *Status at stamp `d2ccf62`:* h.12
   ($m_0\ge0$) is now card §4.1's sign restriction and h.14 is now card §4.3's $U_j$ row, so those
   two are discharged; h.11 and h.16 are carried **descriptively in the card's P1 row itself**
   (ticket 35's amended statement), not as §5 assumptions, and A7 is cited there in its **A7-J**
   form, which is what h.7 consumes. *Round 2 (2026-08-25) moved two more items into the card's
   column and one out of the hypothesis set altogether:* **h.17**'s §4.1–§4.3 table restrictions were
   being consumed silently and are now enumerated here and cited in the row — they are card rows, so
   nothing new is assumed — and **h.5 is struck**, which removes the last mismatch between this file's
   hypothesis list and the row's "A5 is not assumed". **Discharged 2026-08-25:** the retry proof-read
   checked the proof↔row hypothesis match in *both* directions and found it clean — every hypothesis
   this file consumes is listed on the row, and the row lists nothing this file does not consume. That
   is the defect class the demotion turned on, and it is closed.
3. The proof cites h.9 = D1 by statement. *Status at stamp `d2ccf62`:* D1 moved to PROVED on
   2026-08-21 with both passes on file, so the inherited-label conditionality of the original reason
   3 is discharged; what P1 still inherits is D1's own hypothesis set, listed in the card's D1 row.

**What the label does *not* rest on, stated as plainly as the reasons above.** Not on the four
$\kappa$-extreme nodes of `quality_reports/fixes/t2_p1_fournode_recheck.json`, which remain **STILL
UNRESOLVED after 30 seeds each** (ticket 34): best payoff-scale residual $3.1\times10^{-4}$ to
$1.5\times10^{-3}$ against a $10^{-9}$ criterion, with the A3 and A6 proxies passing at every
achieving seed. That is **UNCHECKED** — neither existence evidence at those nodes nor evidence
against it — and the card row says so in the same words. Not on the 2026-08-21 chain, which covered
a different statement. Not on D1, beyond D1's own hypotheses travelling with h.9. And the
conditionality this file has always carried travels with the label: the theorem holds **under** its
enumerated hypotheses, of which h.6 (Steps 14–15), h.11 and h.16 are the ones doing work the card's
A1–A7 do not do on their own — see NOT CLAIMED, which is unchanged in substance by the promotion.

---

## NUMERICAL CHECK REQUEST

**Grid.** $\kappa\in\{0.05,0.10,\dots,0.95\}$ (19 nodes); $\tau\in\{0.03,0.05,0.075,0.10\}$;
$T\in\{1,2,5,10,H\}$; at each node also $\pm20\%$ perturbations of $\sigma_\xi$, of $\Delta_m$, and
of the engagement-cost scale, one at a time. All prices and premia reported in premium percentage
points, not normalised indices.

1. **Existence of the outer fixed point (Step 16).** At each node run a 30-seed multistart on
   $\Theta$ for $k=\mathcal T(k;\vartheta)$ and report
   $\min_{\text{seeds}}\lVert k-\mathcal T(k;\vartheta)\rVert_\infty$. *Predicted sign and
   magnitude:* at every node at least one seed converges with residual $<10^{-10}$; the median
   across nodes of the best-seed residual is predicted below $10^{-12}$. No prediction that seeds
   agree with one another, and disagreement across seeds is **not** a failure of this check.
2. **Inner root: existence, uniqueness, transversality (Step 7).** At each node and each
   information set — the finite pooled list of Step 3 and a sample of 5{,}000 flagged tuples drawn
   from the equilibrium flagged law — evaluate $\varrho(P)=\mathcal P_{\mathcal I}(P)-P$ on a
   2{,}001-point grid spanning $[\hat v-5\sigma_v,\ \hat v+5\sigma_v+m_1]$ and count sign changes.
   *Predicted sign and magnitude:* exactly one sign change at every information set; the reported
   fraction of information sets with two or more sign changes is predicted to be $0.000$ (upper
   bound $10^{-4}$ allowing grid artefacts). At the root, $\varrho'<0$ strictly, with
   $|\varrho'|\ge 1-p\ge 0.10$ at a baseline-like $p\approx0.85$; report the fifth percentile of
   $|\varrho'|$ across flagged tuples and predict it exceeds $0.05$.
3. **The flagged family is single-valued, measurable and non-expansive in the belief (Steps 6, 8).**
   Over the same 5{,}000 flagged tuples, regress the solved $P^F$ on $\hat v(\sigma_F)$ and also
   compute the analytic slope
   $\partial P/\partial\hat v=(1-p)/\bigl[1-p+|p'(P)|(P+m_1-\hat v-\Delta_V)\bigr]$.
   *Predicted sign and magnitude:* the map $\hat v\mapsto P^F$ is single-valued and strictly
   increasing with slope in $(0,1]$; at a baseline-like $p\approx0.85$ and
   $|p'|(P+m_1-\hat v-\Delta_V)\approx0.10$ the slope is predicted at
   $0.15/0.25=0.60\pm0.10$; the maximum absolute discrepancy between the numerical slope and the
   analytic formula is predicted below $10^{-6}$. Any tuple where two distinct $P^F$ values are
   returned by different solver initialisations refutes the Step 6 family.
4. **Flagged sequential optimality — a direct test of h.11 (Step 12).** At each node, for each
   on-path flagged $(j,s)$ in the sample, re-optimise the round-2 order over a 401-point grid on
   $[0,\bar b-B^F]$ holding the flagged pricing schedule at its equilibrium family, and report
   $\max_{Q'}\bigl[\text{continuation}(Q')-\text{continuation}(Q_j^F)\bigr]$. *Predicted sign and
   magnitude:* the gain is $\ge 0$ by construction (the grid contains $Q_j^F$ up to grid
   resolution). The sharp prediction is conditional: **under h.11 — round 2 restricted to the
   plan-generated set $\mathcal Q_j(s)$ — the maximum gain is $0$ to within $10^{-9}$ premium
   percentage points at every tuple; with round 2 opened to the full interval, a strictly positive
   gain of order $10^{-2}$ premium percentage points appears at a positive fraction of tuples.**
   Reporting a positive gain on the full interval therefore measures what h.11 is buying on that
   menu; it does not refute P1. *Amended 2026-08-25 (round 2): the first half is now **derived**, not
   predicted — Step 12(a)–(d) makes the continuation exactly constant on the plan-generated set, so a
   nonzero gain there indicates an implementation defect (a flagged tuple priced off something other
   than its generating pair's belief, or a pooled-path mismatch inside the class) rather than a
   refutation of h.11. The full-interval half stays a genuine prediction, and what it measures is the
   off-image belief the implementation happens to supply (Step 12's converse paragraph).*
5. **Both cells on path (Step 19), and the threshold reformulation (Step 20).** Report
   $\Omega(k^\star)$ and, where h.13 holds by construction of the menu, the implied threshold
   $s_F(k^\star)$ with $\Omega=1-\Phi_s(s_F)$. *Predicted sign and magnitude:* $0<\Omega<1$ at every
   interior $(\tau,T)$ node, with $\Omega$ weakly increasing as $\tau$ falls and as $T$ falls;
   $\Omega$ in the range $0.03$ to $0.30$ at the card §4.4 calibration nodes; $\Omega=0$ exactly at
   $\tau>\bar b$. The two reported $\Omega$ values — direct simulation and $1-\Phi_s(s_F)$ — are
   predicted to agree to within $10^{-10}$ wherever h.13 holds, and to disagree wherever the menu
   violates h.13, which makes the check a test of h.13.

---

## NOTATION DELTA

Symbols used above that are not in card §4. Nothing in card §4 is renumbered or re-keyed; $\kappa$
is noise-trading intensity throughout, bare $\lambda$ does not appear, upright $T$ is the window and
$\mathcal T$ is the best-response map.

| Symbol | Meaning | Collision check |
|---|---|---|
| $j_k(s)=1+\#\{i:k_i\le s\}$ | the plan selected at signal $s$ under conjecture $k$ | card §4.2's $j$ is the plan index; the subscript $k$ marks the induced map |
| $j^\star(\cdot;k)$ | the **best-response** plan map at conjecture $k$: the largest weakly increasing selection from $s\mapsto\arg\max_jU_j(s;k)$ (Step 13), and the equilibrium plan map at $k^\star$ (Step 17(i)) | declared here on retry finding 7, having been promoted by P1-R23 from an internal selection to a named object in the conclusion's assembly. Distinct from $j_k$ above — that is the *conjecture's* induced map, this is the *best response* to it; the two agree $\Phi_s$-a.e. at a fixed point (Step 17(i)). The star is written always; card §4 carries no $j^\star$ |
| $\mathcal Q_j(s)$ | the round-2 action set at the flagged pair $(j,s)$: the plan-generated set $\{Q^F_{j'}(s)\}$ over menu elements sharing $j$'s pooled path up to $f_j(s)$ with $a_{j'}=a_j$ (**h.11**) | declared here on retry finding 7; it has carried h.11 since the batch-1 round. Calligraphic $\mathcal Q$ against card §4.2's italic $Q^F_j$ (the order itself) and $q_{jd}$ (the pooled mark); card §4 has no $\mathcal Q$ |
| $U_j(s;k)$ | blockholder's conditional expected payoff to plan $j$ at signal $s$ under conjecture $k$; the object **defined at h.14** with the conjecture displayed | matches the frozen manuscript's blockholder utility; **never a bare $U$**. **Card gap closed 2026-08-23:** the object is now card §4.3's $U_j$ row, and h.14 transcribes it (the row cites h.14 as "displayed there in full", which the 2026-08-25 display alignment makes literally true) |
| $\mathcal C_j^{\mathrm{trade}}$ | plan $j$'s execution outlay: increments valued at the pooled prices $P_d^P$ up to the plan's last pooled date, plus $Q_j^F(s)P^F$ when $D_j=1$ (h.14) | calligraphic and always subscripted $j$ with the superscript written, so it is clear of card §4.4's $C_h$ (chord), $C_\tau/C_T$ (composition ratios) and $\mathcal C_F/\mathcal C_P$ (cells); **never a bare $C$**. Now carried by card §4.3's $U_j$ row in the same words |
| $C_j(s)$ | plan $j$'s engagement cost at signal $s$; enters $U_j$ as $a_jC_j(s)$, so plans with $a_j=0$ pay nothing (h.14) | named in card §4.4's $C$-overload note and carried by card §4.3's $U_j$ row; subscripted, never bare. **h.16** constrains it across each h.11 deviation set; card §4.3 does not say at which date it is incurred (regeneration item, Step 12) |
| $G_j(s;k)$ | the **trading terms** of Step 11's first bracket: $b_j^*(s)\mathbb E[Y\mid s,j,D=1]-P^F(\sigma_F)Q_j^F(s)$, i.e. the flagged continuation net of the engagement cost. Step 12(c) evaluates it: $G_{j'}=B_j^F(s)P^F(s)$, constant on each h.11 deviation class | proof-local to Step 12 and WHERE IT FAILS 7, introduced 2026-08-25 so the cost-honest comparison has a name. Card §4.4 carries no $G$; $\mathcal G_F$ (this table) is calligraphic and is the inner-root map, a different object |
| $P^F(s)$ | the flagged price written as a function of the signal alone, $P^F(s)=\mathcal G_F(\hat v(s))$ — legitimate on the flagged set by Step 12(a), where A7-J and $\pi=1$ make the tuple's price depend on $\sigma_F$ only through $s$ | the same object as $P^F(\sigma_F)$ of card §4.3, re-argumented; introduced 2026-08-25 (round 2) at Step 12 and used only there and in WHERE IT FAILS 7. The argument is always written, so $P^F(s)$ and $P^F(\sigma_F)$ never collide |
| $V(j')$ | the round-2 continuation value of submitting $Q^F_{j'}(s)$ at a flagged node (Step 12(c)–(d)) | proof-local to Step 12; card §4 carries no bare $V$, and $\Delta_V$ (§4.1) is always written with its $\Delta$ |
| $\mu_n(j,s)$, $L_j(\mathcal H_d^P\mid s)$, $w_n(j\mid s)$ | the stage-$n$ joint $(j,s)$ posterior density at a pooled history; the pooled-history likelihood; the stage-$n$ mixing weight (Step 9(b)) | proof-local to Step 9. $\mu$ is the belief symbol card §5's A5 note already uses ($\mathbb E_\mu[v]$), and $\mu_v$ — card §4.1's prior mean — never appears without its subscript $v$, so the subscript $n$ keeps them apart. **$\rho$ was rejected**: card §5's A(br) sharpening note carries $\rho:=\tfrac12A_{1/2}+A_1$. $L$ and $w$ have no card §4/§5 usage |
| $t_n=J/n$, $Z_n$, $\Lambda_k$, $\Lambda_u$ | the stage-$n$ perturbation mass (so every plan carries $t_n/J=1/n$, Step 9's own parameterisation); the denominator of $\mu_n$; the unperturbed and plan-uniform likelihood aggregates $\int L_{j_k(s')}\varphi_s$ and $\sum_{j'}\int L_{j'}\varphi_s$ (Step 9(b)) | **$t_n$ replaces an earlier $\varepsilon_n$** (confirm-pass sweep): $\varepsilon$ is card §4.1's signal noise and is unavailable under card §8 rule 4; roman $t$ is free in card §4 (upright $T$ is the window, $\mathcal T$ the outer map, and $t_n$ always carries its subscript). $\Lambda$ has zero card §4/§5 occurrences; $Z_n$ is subscripted always and is clear of card §4.1's $z_d$, which is lowercase |
| $\mathcal S(k)$, $\mathfrak w$ | the set of **weakly increasing selections** from $s\mapsto\arg\max_jU_j(s;k)$, and a generic element of it (Step 13) | $\mathcal S(k)$ is calligraphic with its argument always written, so it is clear of card §4.4's $\mathcal S$, $\mathcal S_P$, $\mathcal S^{GE}$ (liquidity sensitivities, never argument-of-$k$) — and it appears only in Step 13. $\mathfrak w$ is **fraktur**, joining Step 18's $\mathfrak T$ in that family: distinct from Step 9(b)'s italic $w_n$, the mixing weight, which is the only other $w$ in the file. **These dummies replace an earlier $\sigma_1,\sigma_2,\sigma_s$** (confirm-pass sweep): lowercase $\sigma$ is reserved for the flagged tuple $\sigma_F$ and the declared variances $\sigma_v,\sigma_\varepsilon,\sigma_\xi$, and no other lowercase $\sigma$ appears in this file |
| $(\hat v_\circ,\pi_\circ)$, $P_\circ$ | the fixed **reference belief** of Step 9(c) — for definiteness the prior pair $(\mu_v,\Pr(a{=}1))$ — and the inner root at it, the price assigned at unreachable pooled histories | the open-circle subscript marks "reference/conventional" and is used nowhere else; $\hat v$ and $\pi$ are the card's own belief summaries (§4.3), so the objects are card objects at a named belief rather than new ones, which is the point of the convention (Step 9(c), retry finding 3) |
| $E_j(s;k)$ | Step 11's second bracket, the pooled-execution expectation | proof-local, same steps as $G_j$. Distinct from any card symbol; $\mathbb E$ is the expectation operator and is never subscripted by a plan |
| $\mathrm{supp}(z_d)$ | the realised support of the noise mark at the maintained $\kappa$: $\{0\}$ at $\kappa=0$, $\{-\bar z,+\bar z\}$ at $\kappa=1$, all three marks in between | roman operator on card §4.1's $z_d$ row, not a new model symbol; used only in Step 9, where the $\kappa$-boundary argument is quantified over it |
| $\mathcal G_F(\hat v)$ | the flagged inner root as a function of the belief: the unique $P$ solving $\mathcal P(P)=P$ at $(\hat v,\pi=1)$ (Step 6b) | **replaces the bare $g$ of an earlier draft**: the turn-2 ruling reserves $g$ for L3's mean-value form, and card §4.5 carries $g_r^{PE}$. $\mathcal G$ has zero occurrences in card §4 and in the other batch-1 proofs; subscript $F$ matches $\mathcal C_F$, $\sigma_F$, $\iota_F$ |
| $s_1,s_2$ | endpoints of the indifference-plateau signal interval in WHERE IT FAILS 3 | **replaces $[\alpha,\beta]$**: $\beta$ is card §4.1's Gaussian projection coefficient, which this file also uses (Steps 6, 10), and one symbol may not carry both meanings. $s$ is the card's signal, so numbered signal values are in-family |
| $\mathcal P_{\mathcal I}(P)$ | the inner pricing map at information set $\mathcal I$, whose fixed point is card §4.3's $P(\mathcal I)$ | calligraphic $\mathcal P$ is unused in the card and has zero occurrences in the frozen manuscript |
| $\varrho(P)=\mathcal P_{\mathcal I}(P)-P$ | inner pricing residual | $\varrho$ has zero occurrences in the card and in the frozen manuscript. It is used here **because $\psi$ is not available**: card §8 rule 4 reserves $\psi$ for D7 pivotality. Appears only in Steps 7–8 and in the WHERE-IT-FAILS and check items that refer back to them |
| $\phi$ | unit normal density, paired with card §4.3's $\Phi$ | appears only inside $p'(P)$ at Step 7(iii) |
| $\bar m(\mathcal I)=m_0+\pi(\mathcal I)\Delta_m$ | expected premium at $\mathcal I$; equals $m_1$ on $\mathcal C_F$ | built from card §4.1's $m_0,\Delta_m$; the frozen manuscript writes the same object $\bar m(\pi)$ |
| $\hat v(\mathcal I)=\mathbb E[v\mid\mathcal I]$ | posterior mean of $v$ at $\mathcal I$ | the frozen manuscript's posterior-mean symbol, same meaning |
| $A=\hat v+\pi\Delta_V$ | no-takeover branch value at $\mathcal I$; proof-local to Steps 7–8 | card §4.4's $A_0,A_{1/2},A_1$ carry subscripts and belong to A($\tau$); this $A$ never appears subscripted |
| $[\underline s,\overline s]$ | the common signal bracket underlying $\Theta$ | card §4.5 posits $\Theta$ compact without naming its bracket |
| $\sigma_F$ | a generic value of the flagged tuple $\mathsf S_F=(B^F,Q^F,a{=}1)$ of card §4.6 | lowercase, always subscripted $F$; distinct from the variances $\sigma_v,\sigma_\varepsilon,\sigma_\xi$, which never appear without their own subscripts. **Swept clean 2026-08-25 (confirm pass):** in the body of this file the *only* lowercase-$\sigma$ objects are $\sigma_F$ and those three variances. The two other appearances of the letter are $\sigma(\cdot)$ as the generated-$\sigma$-field operator (Steps 6(c), 10) — an operator, not an object — and the retired dummies $\sigma_1,\sigma_2,\sigma_s$ named where their supersession is recorded (this table's $\mathcal S(k)$ row and P1-R35), which is the house pattern for a rename |
| $\iota_F$ | the Borel inverse of $(j,s)\mapsto\sigma_F$ on the flagged set | card §4.6 records $\iota_F$ as free |
| $\mathfrak T(k)$ | the best-response *correspondence* of Step 18 | fraktur, used only in Step 18; $\mathcal T$ remains the single-valued map |
| $s_F(k)$ | infimum of the flagged signal set at conjecture $k$ (Step 20) | subscript $F$ matches $\mathcal C_F$ |
| $\Phi_s$ | c.d.f. of the signal $s$ | $\Phi$ alone remains the unit normal c.d.f. of card §4.3 |
| $1/n$ | size of the full-support perturbation in Steps 9–10 | no Greek symbol introduced; $\varepsilon$ is reserved for card §4.1's signal noise |

---

## NOT CLAIMED

1. **Uniqueness of the equilibrium.** Not claimed, in any form: not uniqueness of $k^\star$, not
   local uniqueness, not uniqueness of the induced price system, not uniqueness within a collapse
   face. Brouwer is an existence theorem and nothing above bounds $\lVert D_k\mathcal T\rVert$. Card
   §3 and §9 both disclaim uniqueness and this proof does not weaken that.
2. That A6 is derivable at the card's level of generality. Steps 14–15 name what it assumes; they do
   not prove it. In particular the common bracket and the transversality of adjacent indifference
   are assumed, not shown.
3. That the Step 18 Kakutani route is part of P1. It is a remark. Card §3 fixes the Brouwer route
   for P1's statement, and the correspondence-valued argument still needs Step 15(i) and Step 14's
   bracket.
4. That **A7-J** (h.7) holds on a general finite menu. *Updated 2026-08-25:* satisfiability is no
   longer open — ticket 24 exhibits a menu on which A7-J holds, the pro-rata single-Voice menu with
   $b^*$ strictly increasing on all of $\mathbb R$ (`proofs/A7_construction.md` Step 7, attack
   verdict SURVIVES WITH REPAIRS), and that menu is the paper's pinned instance. What is **not**
   claimed is A7-J beyond it: this file exhibits no other menu, and card §5 records the failure
   boundary (a binding stake cap, quantized stakes, a composed target repeating values across
   Voice-plan switches, $\Omega=0$, and a target flat off the Voice region — the last leaves the
   on-path A7′ intact while breaking A7-J, on a 40-collision executed witness). Steps 6 and 10
   consume A7-J as a hypothesis and do not verify it menu by menu.
5. That h.11 holds on any particular menu, or that any menu in the calibration satisfies it.
   NUMERICAL CHECK 4 is designed to measure what it buys, not to assume it. **Nor is h.11 claimed to
   be the weakest condition delivering item (ii)** — Step 12 says why: the off-path-belief route
   permitted by card §3(vi) is untouched by Step 9's menu-only perturbation and is not analysed
   anywhere in this file. Open. *Added 2026-08-25:* the same three disclaimers attach to **h.16**.
   It is trivially true on any single-Voice menu, the pinned pro-rata menu included (the deviation
   set is a singleton), and a genuine restriction on multi-Voice menus whose Voice plans share pooled
   paths; no step verifies it there, and no menu outside the single-Voice family is exhibited
   satisfying it. h.16 is claimed to be the weakest *uniform* form of the sunk-cost route's one-sided
   condition (h.16's "why" note) — a narrower claim than weakest-overall, which is not made for
   either hypothesis.
6. That an equilibrium satisfying A8 exists at any parameter. Step 20 says this plainly: h.8 is
   imposed at the fixed point, and no step produces a fixed point with $\Omega\in(0,1)$.
7. That $k^\star$ is interior, differentiable in $\vartheta$, or that any comparative static in
   $(\kappa,\tau,T)$ follows from existence. The GE certification machinery of card §4.5 is
   untouched here.
8. That the two adjacent plans are indifferent at a cutoff point. *Rewritten 2026-08-25 (round 2,
   pass-1 finding 7): the old text asserted that indifference, which needs continuity of
   $s\mapsto U_j(s;k)$ — Step 15(i), not a hypothesis and not derived (NOT CLAIMED 11), and refuted as
   automatic by WHERE IT FAILS 4.* Step 17(i)–(ii) no longer needs it: the equilibrium plan map is the
   largest weakly increasing selection $j^\star(\cdot;k^\star)$, optimal at **every** $s$ by
   construction.
   What is not claimed is that $j^\star$ is the only admissible representation of $k^\star$, or that
   the value of the plan map **at** a cutoff point is pinned by §3 — a different tie convention gives
   a different map, and possibly a different equilibrium object at a $\Phi_s$-null set of signals.
9. Anything about welfare, optimal $(\tau,T)$ design, endogenous filing before the deadline, or
   noisy flagged-round trading. Card §9's disclaimers stand unchanged.
10. That the frozen manuscript's four-action results transfer to the $J$-plan menu. Step 14 borrows
    an *argument shape* from it and says explicitly that the shape needs a payoff form the card does
    not impose.
11. That Step 15(i)'s joint continuity is derived. It is **stated as a condition**: continuity in $k$
    at fixed $(j,s)$ is established in Step 15, continuity in $s$ at fixed $k$ is what (i) asks of
    the card, and the conjunction of the two is strictly weaker than the joint statement the
    crossing-point argument consumes. Nor is any differentiability of $U$ in $(s,k)$ claimed — the
    crossing argument is topological, not an implicit-function-theorem argument.
12. That card §4.3's $Y$ row has been disambiguated. Step 5 records the two readings of the $P$ inside
    the takeover branch and shows the step's conclusion survives both; pinning the row is a card
    edit and a regeneration item, not a claim of this file.
13. That a belief is *derived* at a pooled history that is null under **every** plan profile. Step
    9(a)–(c) names the reachable set — reachable **with positive probability**, which excludes both a
    history needing a mark outside $\mathrm{supp}(z_d)$ (nonempty at $\kappa\in\{0,1\}$) and a history
    reachable only through a $\Phi_s$-null set of signals (pass-2 N7) — and confines the §3(vi) limit
    and the §3(iv) price to it. The pre-repair sentence "the limiting belief exists at every pooled
    history" is **withdrawn**, being false at the endpoints (audit Finding 1(c)). Two consequences the
    file owns rather than hides: (a) card §3 requires nothing at an unreachable history, so the
    assembled equilibrium of Step 17 is complete; (b) to keep $U_j(s;k)$ defined at **every** signal —
    which Step 13's pointwise argmax needs — Step 9(c) fixes the convention that the price there is
    the **inner root at a fixed reference belief** (existing and unique by Step 7), so that every
    price in the object is an inner fixed point as the row's conclusion clause says; a different
    admissible reference belief could change $U_j$ on a $\Phi_s$-null signal set and
    so move $\mathcal T$. **The theorem is therefore an existence statement about the object built
    from that fixed convention**; it does not claim the equilibrium is convention-independent
    (pass-1 finding 6).
14. That the date at which the engagement cost $C_j(s)$ is incurred has been settled. Step 12 records
    both readings — plan completion and sunk cost — and shows its conclusion survives either **under
    h.16**, which makes them numerically identical on each deviation set; dating the cost is a card
    edit and a regeneration item, not a claim of this file. Without h.16 the conclusion does *not*
    survive both (WHERE IT FAILS 7).
15. That the flagged order is **uniquely** optimal. Step 12 proves the opposite: on each h.11
    deviation class the flagged price is invariant and the order cancels, so every element of
    $\mathcal Q_j(s)$ delivers the same continuation and the blockholder is exactly indifferent over
    the whole action set. The specified $Q_j^F(s)$ is *a* maximiser, which is all card §3(ii) asks;
    the model does not pin the flagged order by incentives, and any claim that it does — in this file
    or downstream — would be unsupported. This is the round-2 face of the full separation A7-J buys
    (`proofs/A7_construction.md` WHERE IT FAILS 8): once the filing reveals $s$ and the price is
    competitive, no informational rent survives to make one order strictly better than another.

---

## Repairs applied (2026-08-21, batch-1 audit)

Source: `threads/2026-08-21_batch1_proofread_audit.md` (Opus proof-read, verdict PASS, no failing
steps), together with the orchestrator's binding adjudications of the same date. Every change below
is a citation, a hypothesis restated in a satisfiable form, a hypothesis lift, a wording fix or a
notation declaration. **No claim or step conclusion was altered in substance, and no step was
renumbered**; three hypotheses were added at the end of the list (h.14, h.15) or restated in place
(h.11). The label is untouched: P1 remains CONJECTURE.

| Finding | Change made |
|---|---|
| **P1-R1** | h.11's **primary (closure) form is struck** — it is jointly unsatisfiable with h.2 by cardinality, as the hypothesis now records with the argument written out. The definitional reading is **the** hypothesis: the round-2 action set **is** the plan-generated set $\mathcal Q_j(s)$. It is no longer called a closure condition. Step 12 restated on that reading (it already ran on it), together with WHERE IT FAILS 2, the CLAIM's hypothesis summary, LABEL CLAIMED 2, NOT CLAIMED 5 and NUMERICAL CHECK 4. |
| **P1-R2** | "h.11 is the weakest condition that delivers it" **withdrawn**. Step 12 now says h.11 is *a* sufficient condition and sets out the untaken off-path-belief route (card §3(vi); Step 9 perturbs only the plan menu, so off-menu round-2 orders are reached at no $n$ and their limit beliefs are unconstrained), declaring the question open. Recorded again in NOT CLAIMED 5. |
| **P1-R3** | Step 10 now says which reading its "on path and off" stands on: it covers $(j,s)$ pairs the conjecture does not select, and tuples outside the image of $(j,s)\mapsto\sigma_F$ do not arise **because of h.11**, cited there. Step 17(vi) inherits the pinning on that reading only. |
| **P1-R4** | Step 15(i) restated as **joint continuity of $(s,k)\mapsto U_j(s;k)$, a stated condition** — with the explicit note that separate continuity in each argument is strictly weaker — and the boxed conclusion now runs on joint continuity plus the strict sign change, a **topological** argument; the implicit function theorem is named as the wrong tool (it needs differentiability nobody supplies). Step 18's Kakutani remark corrected to match. New NOT CLAIMED 11. |
| **P1-R5** | Step 20's unnumbered condition (a) lifted into **h.15 [ADDITION]** — engagement flags $1$ exactly on an upper set of the ordered menu — cited at Step 20, the one step that consumes it, with (b) card-backed and (c) = h.13 marked as such. |
| **P1-R6** | All three "card §2.10" citations removed. The blockholder payoff is now **h.14 [ADDITION — CARD GAP]**, a numbered definition of this proof faithful to `threads/thread1_turn1_answer.md` §2.10, with "the card carries no blockholder payoff row, no $\mathcal C_j^{\mathrm{trade}}$; card gap, regeneration item" flagged inline at the hypothesis, at Step 11, at Step 14 and in the NOTATION DELTA. Recommendation to absorb the row into the card recorded at h.14. |
| **P1-R7** | NOTATION DELTA completed. (a) The bare $g$ of Step 6 is renamed **$\mathcal G_F$** (zero card §4 hits; $g$ stays reserved for L3's mean-value form per the turn-2 binding ruling) and declared. (b) WHERE IT FAILS 3's $[\alpha,\beta]$ renamed **$[s_1,s_2]$**, so $\beta$ carries only card §4.1's Gaussian projection meaning; declared. (c) $\mathcal C_j^{\mathrm{trade}}$ and $C_j(s)$ declared, as consequences of P1-R6. |
| **P1-R8** | Step 5 split in two: (a) the pooled **control-node** cell, a genuine fixed point of Step 4's map under h.5; (b) intermediate dates $d<H$, a **tower-property** conditional expectation of already-solved control-node values with no self-reference. Both readings of card §4.3's $Y$ row are recorded, the step's conclusion is shown to survive either, and the ambiguity is flagged as a regeneration item (also NOT CLAIMED 12). |

Not applied here, by scope: P1-O1 … P1-O5 are OBSERVATIONs, not REPAIRs.

---

## Repairs applied (2026-08-25, ticket 35 / R5 — post-review P1 repair, route A)

Source: `threads/2026-08-23_gpt_end_review_audit.md` **Finding 1** (three gaps — (a) hypothesis-form
mismatch, (b) Step 12's cost gap, (c) the $\kappa=1$ tremble gap — plus the objective-display
citation nit) and **Finding 7(ii)** (the continuum sentence names the coordinate where it should name
the tuple), against `MODEL_CARD.md` stamp 2026-08-23 · `d2ccf62`. Route **A** per spec
`quality_reports/specs/2026-08-23_post-review-repairs.md` (Austin's Q4 decision): keep the general
finite-menu theorem and state the hypotheses the proof actually needs.

**What moved and what did not.** The **conclusion is unchanged** — same equilibrium object, same six
card §3 items, same $\Theta$, same Brouwer route, and now stated explicitly for the card's full
domain $\kappa\in[0,1]$ rather than restricted to $[0,1)$. Two **hypotheses are strengthened**: h.7
becomes A7-J (strictly stronger than the on-path A7′ the pre-review card row carried) and h.16 is
added. One clause of the conclusion is **made precise**: card §3(vi)'s off-path beliefs are supplied
at every *reachable* pooled history, which repairs a sentence that was false at $\kappa\in\{0,1\}$
rather than retreating from a true one. No step was renumbered; WHERE IT FAILS gains item 7 at the
end and NOT CLAIMED gains items 13–14 at the end, so every pre-existing cross-reference still
resolves. **The label is untouched: P1 remains CONJECTURE**, and ticket 35's two fresh passes — an
adversarial proof-read of this file and a statements-only re-derivation of the amended card row —
are the only things that may move it.

| Finding | Change made |
|---|---|
| **P1-R9** (Finding 1(a)) | **h.7 renamed A7-J (joint tuple injectivity)** and restated on the flagged-**pair** set $\{(j,s):D_j=1\}$, including pairs no $k\in\Theta$ selects, with the note that this is strictly stronger than A7′ and is what Step 10's *off-path* pinning consumes. The pre-review card row recorded the weaker on-path A7′ while this proof consumed the joint form — the mismatch that meant the 2026-08-21 passes covered two different statements. CLAIM's antecedent updated from "A1–A7 of card §5" to "A1–A6 together with A7 in its A7-J form". Steps 6 and 10 already read "injective on the flagged set" and are unchanged in substance. Two neighbours checked and annotated rather than changed: **WHERE IT FAILS 2** and Step 12's converse paragraph each gain one sentence recording that the counterexample menu there can be taken A7-J-satisfying ($b^*$ strictly increasing on all of $\mathbb R$), so strengthening A7 does not silently repair a failure case or make item (ii) follow from the card's assumptions after all. |
| **P1-R10** (Finding 7(ii)) | h.7's continuum sentence corrected: injectivity forces the **tuple** $(B^F,Q^F)$ to be continuum-valued, **not the coordinate $B^F$** — which on the pinned pro-rata menu is not even monotone, jumping down at every crossing-date boundary while the sum $B^F+Q^F=b^*_j(s)$ carries the separation (`proofs/A7_construction.md` Steps 8–9; `proofs/A7_attack_verdict.md` S-10, where our own attack flagged this and the card note was never amended). Card §5's A7 note already carries the corrected form. |
| **P1-R11** (Finding 1(b); spec MAY-11) | **h.16 [ADDITION] added** — continuation-cost equivalence, $C_{j'}(s)=C_j(s)$ on each h.11 deviation set — with a "Why" note deriving it, and **Step 12 rewritten cost-honestly**: the trading terms $G_j$ are named and separated from the engagement cost, the deviation's two possible continuations (plan completion, sunk cost) are displayed, and the contradiction now runs on $G_{j'}>G_j$ with the middle bracket $C_{j'}-C_j$ shown to vanish under h.16. **MAY-11 route considered and declined with a reason:** restating optimality against the sunk-cost continuation does not discharge the gap on its own — date-0 optimality gives $G_j-G_{j'}\ge C_j-C_{j'}$ where sunk-cost optimality needs $G_j-G_{j'}\ge0$, so it needs $C_{j'}\le C_j$ at the selected $j$; and since the deviation set is an equivalence class (shared path $\Rightarrow c_{j'}=c_j\Rightarrow f_{j'}=f_j$, so the relation is symmetric) and P1's hypotheses must hold uniformly on $\Theta$ (Brouwer does not say which $k^\star$ it returns), that one-sided clause collapses to h.16's equality. h.16 additionally makes the two readings *coincide*, so the step never adjudicates the card's silence on when $C_j$ is incurred. The Θ-uniformity leg is stated with its one exceptional signal named ($s=\overline s$, where $j_k(\overline s)=J$ for every $k$; immaterial, since h.16 is imposed at every $s$ regardless). Propagated to the CLAIM, Step 17(ii), **WHERE IT FAILS 7** (new, carrying the review's $0.01$-vs-$0.99$ arithmetic), NOT CLAIMED 5 and 14, and LABEL CLAIMED 2. |
| **P1-R12** (Finding 1(c)) | **Step 9 rewritten** in four parts: (a) $\mathrm{supp}(z_d)$ is displayed at $\kappa=0$, $\kappa=1$ and in between, and a pooled history is defined **reachable** when some plan and a positive-probability signal set make the *whole* history positive-probability; (b) the perturbed-posterior limit is established at every reachable history, with the denominator bound written out; (c) unreachable histories are shown to carry no card §3(vi) or §3(iv) requirement **and to be consumed by no step** (Step 11's pooled bracket and every h.11 deviation integrate over the played plan's own reachable set); (d) the false sentence is named and withdrawn. **The $\kappa=1$ route is the extension, not the restriction** — the theorem now holds on $\kappa\in[0,1]$ with both endpoints, and the $\kappa=0$ special case becomes the same sentence. Propagated to the CLAIM's belief clause (with its own "on the belief clause" note), Step 11, and NOT CLAIMED 13. The integrating measure in (b) is written $\mathrm d\Phi_s$, the NOTATION DELTA's declared signal c.d.f., so the step introduces no undeclared symbol. |
| **P1-R13** (Finding 1, citation nit) | **h.14's display aligned with card §4.3's $U_j$ row**: $-a_jC_j(s)$ in place of $-C_j(s)$, the $\mathcal C_j^{\mathrm{trade}}$ gloss expanded to the card's own words (increments at the pooled prices up to the last pooled date, plus $Q^F_jP^F$ when $D_j=1$), and $C_j(s)\ge0$ transcribed, so the card's "displayed there in full" is literally true. The card row was **not** edited (it is outside this ticket's edit surface; the fix is on the proof side, which the ticket permits). Step 11's display carries $-a_jC_j(s)$ with the note that $a_j=1$ on the flagged branch (h.4), so Steps 12–13 are unchanged. NOTATION DELTA rows for $U_j$, $\mathcal C_j^{\mathrm{trade}}$ and $C_j(s)$ updated; new rows for $G_j$, $E_j$ and $\mathrm{supp}(z_d)$. |
| **P1-R14** (staleness against `d2ccf62`; audit Finding 1's "not disturbed" paragraph) | **NOT CLAIMED 4 refreshed.** It said A7 satisfiability was open and a Thread 2 target; ticket 24 closed it — the pinned pro-rata single-Voice menu with globally strict $b^*$ satisfies A7-J (`proofs/A7_construction.md` Step 7). The item now disclaims what is genuinely undisclaimed: A7-J on menus beyond that one, with card §5's failure boundary quoted. |
| **P1-R15** (Finding 8, card-snapshot staleness) | **LABEL CLAIMED reasons 2 and 3 brought to stamp `d2ccf62`**, and Step 14's parenthetical with them. Reason 2 previously listed h.12 and h.14 as absent from the card; $m_0\ge0$ is now card §4.1's sign restriction and $U_j$ is now card §4.3's row, while h.11 and h.16 are carried descriptively in the card's amended P1 row rather than as §5 assumptions. Reason 3 previously called D1 a CONJECTURE; D1 moved to PROVED on 2026-08-21. **No label is moved by this row** — the section header still claims CONJECTURE, now resting on reason 1 alone (prose never moves a label; ticket 35's two fresh passes are not this file's to claim). |
| **P1-R16** (two-pass protocol; no change of substance) | The amended card row's belief clause covered only the **pooled** layer once the reachability qualifier was added, and the row is the statements-only re-deriver's sole input. Both the row and this file's CLAIM now name the **flagged** layer explicitly: flagged-tuple beliefs are supplied by A7-J at every tuple in the image of $(j,s)\mapsto(B^F_j,Q^F_j,a_j)$, on path and off, with no tuple outside the image arising under the round-2 action-set hypothesis. This states what Step 10 has always proved (and what Step 17(iii)/(vi) has always assembled); nothing in the proof changes. *Filed here, after R15, on 2026-08-25 round 2 (pass-1 repair-table nit: it had been inserted between R12 and R13).* |

**The pinned instance, clause by clause (round 1).** The paper's pro-rata single-Voice menu satisfies every
strengthened clause, so route A's repairs cost the paper's instance nothing: **A7-J** holds on it
(`proofs/A7_construction.md` Step 7 — only the Voice plan ever flags, so the flagged-pair set is
$\{(V,s)\}$, and globally strict $b^*$ separates it through the sum coordinate); **h.16** holds
trivially (on the flagged set $a_j=1$, Exit and Hold never cross $\tau$ under $b_0<\tau$, so the
deviation set is the singleton $\{V\}$ — the same fact that makes h.11's action set a singleton
there); and the **$\kappa$** repair is an extension, so no boundary clause has to be satisfied at
all, with every numerical node of `t2_p1_check` sitting at interior $\kappa$ regardless.

---

## Repairs applied (2026-08-25, ticket 35 / R5 — round 2, the sanctioned pass-1 repair round)

Sources: the **adversarial proof-read** (verdict FAIL: 1 FAIL, 8 REPAIRs, 3 OBSERVATIONs) and the
**statements-only re-derivation** (verdict PASS-WITH-CHANGES: six row changes, none weakening), both
2026-08-25, together with the orchestrator's binding adjudication of the same date. Findings are cited
as *pass-1 finding n* and *pass-2 Nn / change n*.

**The FAIL, and how it is discharged.** Pass-1 finding 1 is **upheld as a gap in this file**: the
pre-round-2 Step 12 ran the deviation back to date-0 optimality, which reaches only the flagged nodes
on the *selected* plan, while h.11 defines an action set at **every** flagged pair and card §3(ii)
binds at all of them. The adjudicated repair is **not** finding 1's class-argmax construction, which
would have changed the equilibrium object; it is pass-2's R16–R17, which discharges §3(ii) everywhere
with the object unchanged: A7-J pins the belief at the same $s$ for every class member and $\pi=1$, so
the flagged price is invariant across the class (Step 12(a)); the blockholder's control-node valuation
is then the fixed-point equation itself, $\mathbb E[Y\mid\cdot]=P^F(s)$ (Step 12(b)); the $Q^F$ terms
cancel, leaving $V(j')=B_j^F(s)P^F(s)-\text{cost}$ (Step 12(c)); and h.16 makes the cost constant, so
**every** element of the action set is optimal at **every** flagged pair (Step 12(d)). The
cancellation was checked against this file's own $G/E$ decomposition before it was written in, and it
holds there in the form $G_{j'}=B_j^F(s)P^F(s)$ for every class member — which is also what refutes
finding 1's witness and the trading-gain framing this file's round-1 draft carried (Step 12's
refutation note).

**Conclusion strength.** Unchanged, and in one respect the file now proves *more* than the row claims:
§3(ii)'s flagged half is established at every flagged pair rather than only at selected ones. No
hypothesis was added except **h.17**, which enumerates card rows the proof was already consuming;
**h.5 was struck**, which is a removal. No step was renumbered; WHERE IT FAILS keeps items 1–7 with 1
retitled, and NOT CLAIMED gains item 15 at the end.

| Finding | Change made |
|---|---|
| **P1-R17** (pass-1 finding 1 FAIL; pass-2 R16–R17) | **Step 12 restructured** into the four-part lemma above and restated to quantify over *every* flagged pair, selected or not, with no appeal to date-0 optimality; the h.16 "why" note rewritten around the cost wedge; **Step 17(ii)** updated; **WHERE IT FAILS 7** rebuilt with the wedge in the engagement cost (the trading-terms version is not constructible); **NOT CLAIMED 15** added (the flagged order is optimal but not *uniquely* so — the class is an indifference set); **NUMERICAL CHECK 4**'s first half reclassified from prediction to derivation. Also recorded: at a **selected** $j$ date-0 optimality already forces $C_j\le C_{j'}$, so h.16's bite is exactly the non-selected flagged nodes under the plan-completion cost convention. |
| **P1-R18** (pass-1 finding 2) | **h.2 = A2 → A2′.** The old text carried "prices and payoffs bounded on the maintained parameter set", a clause card §5 declares **false**; the row cites A2′. Replaced by A2′'s finiteness clauses plus local boundedness in $(s,\vartheta)$ and $\mathbb E[\max_j\lvert U_j\rvert]<\infty$; Step 13's "finite and bounded by h.2" re-worded to what A2′ supplies; h.2's *Used* list corrected to Steps 3, 9, 13 (Step 16 never cites it — pass-1 observation 11). |
| **P1-R19** (pass-1 finding 3) | **h.5 struck**; the slot is kept so no citation renumbers. Re-cited use by use: Step 5(a) and Step 6(b) now run on **Steps 7–8** (existence and uniqueness from h.12; continuity in the belief from Step 8's implicit-function argument, which is the one genuinely load-bearing A5 use); Step 15's clause is marked **commentary**; Step 7's heading and closing paragraph, Step 6's heading and (d), and WHERE IT FAILS 1's title updated accordingly. Removes the last proof-vs-row mismatch behind the row's "A5 is not assumed". |
| **P1-R20** (pass-1 finding 4) | **Step 9(b) re-run on the joint $(j,s)$ posterior** $\mu_n(j,s)$, with the likelihood and mixing weight named, the positive-denominator bound rewritten in those terms, and the passage to $\hat v$ made by **dominated convergence** under h.17-d's Gaussian tail and h.2's integrability. The plan-only posterior delivers $\pi$ but not $\hat v=\mathbb E[v\mid\mathcal I]$, which is a functional of the *signal* posterior — load-bearing because Step 13 evaluates $U_j$ for plans carrying zero probability on a collapse face. NOTATION DELTA gains $\mu_n$, $L_j$, $w_n$ ($\rho$ rejected: card §5's A(br) note carries $\rho$). |
| **P1-R21** (pass-1 finding 5) | **Step 10 states the version explicitly.** The signal is Gaussian, so $(j,s)$ is null under every perturbation stage and "that pair has strictly positive weight" was a positive-probability argument on a null event. Replaced by: $\delta_{\iota_F(\sigma_F)}$ is a **version** of the regular conditional law at every image tuple, invariant in $n$, hence its own limit, and this proof selects it; any a.e.-equal version satisfies §3(iii) and §3(vi) equally. The CLAIM and the card row are softened from "pinned, not chosen" to the version formulation, matching `proofs/A7_construction.md`'s own hedge. Step 6(d)'s "pinned" is left standing and marked as being about the *price* family given the belief, which is a different and stronger statement. |
| **P1-R22** (pass-1 finding 6; pass-2 N7) | **Step 9(c) rewritten.** Reachability requires a *positive-probability* signal set, so a $\Phi_s$-null cell of the mark-and-flag level-set partition can leave a plan's own histories unreachable at those signals. Fix adopted (the one consistent with Step 11): **fix the convention $P_d^P:=\mathbb E[Y]$ at unreachable histories**, so $U_j(s;k)$ is defined at every signal for Step 13's pointwise argmax, with the honest rider that a different admissible convention could move $\mathcal T$ through a $\Phi_s$-null signal set — recorded in **NOT CLAIMED 13**, which also absorbs N7's positive-probability point. *Superseded in part by **P1-R30**: the convention adopted here was $P_d^P:=\mathbb E[Y]$, which is not a root of $\mathcal P_{\mathcal I}$ at any belief and so clashed with the row's unqualified "prices at their inner fixed points"; it is now the inner root at a fixed reference belief. Everything else in this row stands.* |
| **P1-R23** (pass-1 finding 7; pass-2 N8) | **The equilibrium plan map is $j^\star(\cdot;k^\star)$, not $j_{k^\star}$.** $\mathcal T_i$ is an infimum that need not be attained, so Step 1's $\le$ convention could disagree with the argmax *at* a cutoff, and the old Step 17(ii) patched that with an indifference claim that needs Step 15(i)'s continuity — not a hypothesis, and refuted as automatic by WHERE IT FAILS 4. Step 13 now **names the selection**, Step 16 reads h.6 as applying to that single-valued selection, Step 17(i)–(ii) run on it with optimality at **every** $s$, and **NOT CLAIMED 8** is rewritten. *Superseded in part by **P1-R28**: R23 named the largest **maximiser**, which is not weakly increasing in general; the selection is now the largest **weakly increasing selection**. Everything else in this row stands.* |
| **P1-R24** (pass-1 finding 8) | **Step 2's Borel justification corrected.** "Monotone by card §4.2, hence Borel" is false for Exit ($\partial_sB_j\ge0$ is a **Voice** row); the card supplies Borel-in-$s$ for every plan as a separate clause it calls "a genuine addition for Exit". Now cited as **h.17-b**. Load-bearing: Step 9's reachability and the pooled prices integrate over all types including Exit. |
| **P1-R24b** (consequence of P1-R17, no finding) | **WHERE IT FAILS 2 made precise.** Its improving off-menu order presupposes a flagged pricing schedule defined at off-image tuples; Step 12(c) shows no gain can exist on the plan-generated set, so the case now names the off-image extension it needs (a posterior mean short of $\mathbb E[v\mid s]$ at some feasible $Q'$) instead of assuming a schedule into existence. Steps 19–20 and Step 17(i) also updated to the $j^\star(\cdot;k^\star)$ symbol with a note that the two maps agree $\Phi_s$-a.s., so $\Omega$, the prices and the posteriors are unchanged. |
| **P1-R25** (pass-1 finding 9) | **h.10 gains clause (ii)**, the flag-terminates-the-pooled-round clause the row lists and Step 11 consumes — pooled execution over $d\le f_j$ and $Q^F_j$ the whole residual position — cited at Step 11 and again at Step 12(c) where the pooled outlay is called sunk. h.10(i) is the no-feedback half and does not deliver either. |
| **P1-R26** (pass-1 observations 11–12) | CLAIM's hypothesis sweep corrected — it read "h.1–h.12, h.14 and h.16", which swept in h.8 (used only for the A8 addendum) and the now-struck h.5; the A8 sentence says so explicitly. **Step 17(iv)** now states §3(iv) at reachable $k$-null histories as the inner fixed point **at Step 9(b)'s limit belief**, which is what the deviation payoffs read. Observation 10 (h.11's type-indexed action set excludes mimicry by fiat) is left as it stands, per adjudication: h.11 is owned descriptively by the row and card §9 item 2 already records the IC burden. |
| **P1-R27** (pass-2 changes 1–5) | **h.17 [ADDITION] added** — the §4.1–§4.3 table restrictions (N1–N4), in four labelled items with their *Used* lists — so the proof cites what it consumes instead of consuming it silently; the card row now carries the same block. The row's other four changes are card-side and logged there: D1's hypotheses travelling and the expanded A5 sentence (N5); the one-perturbation-family/every-$k\in\Theta$/positive-probability off-path clause (N6, N7); A6's tie-break-and-corner reading with $\Theta$ nonempty per §4.5 (N8, N9); and the $C_j(s)$ timing convention stated in the row's own $U_j$ parenthetical (N10). **Pass-2 change 6 (a §9 OPEN item on A6's continuity at collapsed cutoff vectors) is deliberately not applied** — it is Austin's call, not this round's. |

---

## Repairs applied (2026-08-25, ticket 35 close-out — the finishing round)

Source: the **proof-read retry verdict**, `threads/2026-08-25_P1_proofread_retry.md` — **PASS, 0
FAIL**, 3 REPAIRs and 4 OBSERVATIONs, all applied below. The reader verified the new Step 12 lemma
part by part on the merits before turning to findings, and records that his own round-1 FAIL witness
is refuted: "I tried to rebuild it and cannot… (a)+(b) force $G_{j'}=B^F_j(s)P^F(s)$ for every class
member, so $\delta\equiv0$." Only finding 1 touches a conclusion clause, and only finding 1 was
created by a previous patch (P1-R23).

**Effect on the label.** With this round applied the two-pass gate is satisfied for the statement in
the card's amended P1 row, and the orchestrator has moved P1 **CONJECTURE→PROVED** in
`LABEL_LEDGER.md`. The LABEL CLAIMED section above is updated accordingly, with the three historical
reasons kept and annotated rather than deleted.

| Finding | Change made |
|---|---|
| **P1-R28** (retry finding 1, REPAIR — the one conclusion-touching item) | **The tie-break is now the largest *weakly increasing* selection**, not the largest maximiser. R23's `$j^\star(s;k):=\max\arg\max_jU_j(s;k)$` was a **non sequitur**: the reader's counterexample sits inside h.3 — $U_2-U_1\le0$ everywhere with equality at one point $s_0$ (a tangential touch: zero crossings, and the constant selection $j\equiv1$ is weakly increasing, so both clauses of h.3 hold) makes the largest maximiser $1,\dots,1,2,1,\dots,1$, which is not monotone, whose up-set $\{s:j^\star\ge2\}=\{s_0\}$ is not an up-set at all, and which **no cutoff vector represents** — breaking Step 17(i) and with it §3(i)/(ii). Step 13 now takes $j^\star(\cdot;k)$ to be the largest element of the set $\mathcal S(k)$ of weakly increasing selections, with the reader's own three-line construction written out: $\mathcal S(k)\ne\emptyset$ by h.3; closed under pointwise max (the max of two selections is one of the two values, hence a selection, and a pointwise max of monotone maps is monotone); the supremum is attained on a finite menu (h.2) and is itself in $\mathcal S(k)$ ($j^\star(s';k)\ge\mathfrak w(s')\ge\mathfrak w(s)=j^\star(s;k)$ for $\mathfrak w\in\mathcal S(k)$ attaining the max at $s$). Canonical, single-valued (pass-2 N8), monotone **by construction** rather than by an appeal to h.3 after the fact. Swept to every site: Step 13's definition and its representation sentence, Step 16's h.6 reading, Step 17(i), Step 20's monotonicity appeal, NOT CLAIMED 8, and P1-R23 (annotated as superseded in part). Brouwer is untouched — the nesting that gives $\mathcal T(k)\in\Theta$ holds for any selection. |
| **P1-R29** (retry finding 2, REPAIR) | **Step 11's forward reference to Step 9(c) de-staled.** It still read "By Step 9(c) every pooled history the second bracket weighs is reachable"; P1-R22 had made that true for $\Phi_s$-**almost every** $s$ only, with the conventional price at the exceptional signals. The qualifier is inserted and the exceptional case pointed at 9(c)'s convention, matching what Step 13 already said correctly. A neighbour the round-2 patch missed. |
| **P1-R30** (retry finding 3, REPAIR) | **Step 9(c)'s unreachable-history convention changed from $\mathbb E[Y]$ to the inner root at a fixed reference belief** $(\hat v_\circ,\pi_\circ)$ — for definiteness the prior pair $(\mu_v,\Pr(a{=}1))$ — which exists and is unique by Step 7 under h.12. Reason: $\mathbb E[Y]$ is an unconditional average of realised control-node values and is in general **not** a root of $\mathcal P_{\mathcal I}$ at any belief, so the constructed object would have carried prices that are not inner fixed points at nodes where the blockholder does trade, while the card row's conclusion says "prices at their inner fixed points" without qualification. Card §4.3's $P_{-1}^P:=\mathbb E[Y]$ precedent does not transfer — that is the pre-trading node. With the reference-belief root **every price in the object is an inner fixed point at the belief carried there**, and the mismatch with the row is gone. NOT CLAIMED 13(b) updated. |
| **P1-R31** (retry finding 4, OBSERVATION) | **Step 9(b)'s dominated-convergence envelope gains its case split.** As written, "$\mu_n\le\varphi_sL_j/Z_n$ with $Z_n\downarrow0$" is not a uniform envelope. Split now stated: if $\Lambda_k>0$ then $Z_n\ge\Lambda_k/2$ eventually and $2\lvert\mu_v+\beta(s-\mu_v)\rvert\varphi_sL_j/\Lambda_k$ dominates; if $\Lambda_k=0$ the $(1-t_n)$ terms vanish $\Phi_s$-a.e. and $\mu_n=L_j\varphi_s/\Lambda_u$ is exactly $n$-free, so there is nothing to pass to the limit. This is pass-2's own R9(b) structure. |
| **P1-R32** (retry finding 5, OBSERVATION) | **WHERE IT FAILS 3 records that plateaus are structural on exactly the menus h.16 is for.** By Step 12(c), $U_{j'}=B_j^FP^F-C_j-E_j$ is the same function of $s$ for every member of a deviation class, so on a multi-Voice menu with two **adjacent** class members $U_{i+1}-U_i\equiv0$ on the whole flagged region and Step 15(ii)'s transversality fails *identically*, not exceptionally. Non-blocking — h.6 asserts continuity of $\mathcal T$ outright and R28's selection is single-valued across the plateau — but the file now says plainly that **h.6 is being assumed at a configuration where its own named sufficient condition provably fails**, which is a real cost of h.16's range of application and was previously invisible. |
| **P1-R33** (retry finding 6, OBSERVATION) | **Card row: h.16's gloss qualified "under the plan-completion reading".** Step 12(d) and h.16's why-note both say that under the sunk reading the continuation is constant with no clause at all, so h.16 is consumed on the (α) reading only; the row glossed it unconditionally. The row now says so, and says why the hypothesis is nonetheless listed: the row does not commit to a reading, and h.16 is what makes the conclusion hold under both. Card §8 rule 6 ("each hypothesis used") is now satisfied on either reading. |
| **P1-R34** (retry finding 7, OBSERVATION) | **NOTATION DELTA gains $j^\star(\cdot;k)$ and $\mathcal Q_j(s)$** (card §8 rule 3). Both pre-date round 2, but R23 promoted $j^\star$ from an internal selection to a named object in the conclusion's assembly, and $\mathcal Q_j(s)$ has carried h.11 since batch 1. Collision checks written: $j^\star$ against Step 1's $j_k$ (conjecture's map vs best response, agreeing $\Phi_s$-a.e. at a fixed point), $\mathcal Q$ against card §4.2's $Q^F_j$ and $q_{jd}$. |

| **P1-R35** (confirm pass, mechanical; card §8 rules 3–4) | **Notation sweep, no mathematics touched.** (a) The perturbation mass $\varepsilon_n$ introduced by P1-R31 is renamed **$t_n$** at all four occurrences and tied to Step 9's own parameterisation, $t_n=J/n$ so that each plan carries $t_n/J=1/n$ — $\varepsilon$ is card §4.1's signal noise and card §8 rule 4 does not release it; the $w_n$ display is written out so the Step 9(b) case split reads off it directly. (b) Step 13's selection dummies $\sigma_1,\sigma_2,\sigma_s$ are renamed **$\mathfrak w_1,\mathfrak w_2,\mathfrak w$** (fraktur, joining Step 18's $\mathfrak T$), and Step 9(b)'s integration dummy $\sigma$ becomes $s'$, so that **lowercase $\sigma$ now carries only $\sigma_F$ and the declared variances**, as $\sigma_F$'s own collision-check row requires. (c) NOTATION DELTA gains three rows: $\mathcal S(k)$ with its elements $\mathfrak w$; $t_n$, $Z_n$, $\Lambda_k$, $\Lambda_u$; and the reference-belief triple $(\hat v_\circ,\pi_\circ)$, $P_\circ$. (d) P1-R22 annotated as superseded in part by P1-R30, on the pattern of P1-R28's annotation of P1-R23. |

**Not applied, deliberately.** The retry's divergence note in item (d) — the row says A5's continuity
content comes "from the same scalar reduction" while this file derives it from Step 8's
implicit-function argument — is left standing: the reader records both routes as valid ($\varrho$ is
$C^1$ jointly with $\partial_P\varrho<0$ strictly at every root), and pass 2's route is IFT-free and
1-Lipschitz. Two valid derivations of the same clause is not a defect, and rewriting the row to name
only one would misreport the re-derivation. Pass-2 change 6 (a §9 OPEN item on A6's continuity at
collapsed cutoff vectors) remains withheld for Austin, now with retry finding 5 as further motivation
for it.
===== END research/model_v4/proofs/P1_proof.md =====

---

## 6. WHAT IS ASKED BACK

Three parts, in this order. The whole response is filed verbatim in the lane's thread record and
audited finding by finding, so write it to be localised: a step number on every finding, and the
current text quoted before the text that replaces it.

### Part 1 — the findings, numbered, grouped by class

Number the findings **F1, F2, F3, …** in one continuous sequence across the whole response, and
group them under four headings in this order: **WRONG**, **GAP**, **POLISH**, **UNCLEAR**. A
heading with nothing under it is written out with "none" — that is information, not an omission.
Each finding carries, in this shape:

- **Step anchor.** The step and sub-part the finding lands on, as printed in §5 (for example
  "Step 12(c)", "Step 7(iii)", "HYPOTHESES h.16"). One anchor per finding; if the same defect
  recurs at three sites, either give three findings or give one finding listing all three anchors
  explicitly.
- **Current text, quoted.** The sentence or passage as it stands, quoted, long enough to be found
  by string search and short enough to read.
- **Proposed text** — required for POLISH, required for GAP, optional for WRONG (where the failure
  statement is the deliverable and a repair may not exist), not applicable for UNCLEAR. Write it as
  the replacement itself, drop-in ready in the file's own register and notation, not as a
  description of what should change.
- **One line on why the change preserves the statement.** Name what the step establishes and say
  that the replacement establishes the same thing — or, if it does not, say plainly what it changes
  and treat that as a WRONG or GAP finding instead of a POLISH one. This line is what the lane's
  proof-read pass checks first.

### Part 2 — the per-step verdict table

One row per numbered step and per lettered or roman sub-part as printed in §5, in the proof's own
order, with these columns:

| Step | Verdict | Finding | One line |
|---|---|---|---|

**Verdict** is exactly one of **SOUND AS WRITTEN** · **POLISH** · **GAP** · **WRONG** · **UNCLEAR**.
**Finding** carries the finding numbers from Part 1, or `—` for SOUND AS WRITTEN. **One line** says
in a clause what the step establishes and what, if anything, is wrong with how it establishes it.
A missing row is an incomplete answer.

### Part 3 — the overall judgment, one paragraph

Close with a single paragraph, and answer the question directly: **is this proof, as written, at the
standard of the best published existence proofs in this literature?** If it is, say what carries it
there. If it is not, name **the three changes that close most of the distance** — ranked, each one
sentence, each pointing at the step it lands on. Judge the proof as a piece of published
mathematics: the ordering of the argument, what is asserted versus derived, where a reader has to
reconstruct a move the writer had in hand, and whether the statement in §3 is the theorem this
argument proves. The applicability record — A3, A6 and A($\tau$) measured false at the implemented
calibration — is settled and is not the question here; it enters this paragraph only if the proof
text itself claims more than that record supports.

### Answer template

Card §8 rule 6's template governs a *new* result, not a review; this response uses the six headings
above plus two of the card's own, in this order:

`FINDINGS — WRONG` · `FINDINGS — GAP` · `FINDINGS — POLISH` · `FINDINGS — UNCLEAR` ·
`PER-STEP VERDICT TABLE` · `OVERALL JUDGMENT` · `NOTATION DELTA` (card §8 rule 3 — every symbol you
use that the card's §4 Symbol table does not carry) · `NOT CLAIMED` (card §8 rule 5 — what this pass
did not check, said plainly).
