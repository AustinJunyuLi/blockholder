# Addendum to the 2026-08-29 P1 polish-pass audit — seam follow-ons P1-R54, P1-R55, P1-R56

**Provenance, declared.** The parent audit (`threads/2026-08-29_gpt_p1_polish_audit.md`, filed at
commit `34d2695`) drafted its wording queue as P1-R36–P1-R53. After the fourteen-item batch was
applied (2026-08-29, application report in the applying session's scratchpad; independent
verification BATCH PASS), the application surfaced one flag and two report-only observations.
The auditor ruled on all three and drafted three follow-on repairs, all **WORDING-ONLY**, which
travelled to the application agent through that session's coordinator channel rather than a repo
file. **This addendum files them durably.** The texts below are reproduced from the applied
`proofs/P1_proof.md` (verified there by the applying agent's fidelity check and by the second,
independent verification pass recorded in the session log); they are the auditor's drafts as
applied, and any divergence between the coordinator-channel originals and these would be
invisible to this file — recorded, not hidden. All three remain **CONJECTURE-grade edit text**
until the lane's gate runs over the proof carrying them. **No label moves, no ledger entry.**

## Rulings that generated the follow-ons

- **The P1-R52 flag** (applied R52 left a setup sentence near-duplicating the untouched Step 12
  opening): ruled duplication, and worth striking now rather than leaving as emphasis → **P1-R54**.
- **Report-only observation 1** (Step 18's heading still announced the Kakutani strengthening its
  R46-scoped body withdraws) → **P1-R55**, which also carries the withdrawal to the two sites that
  still read against it: NOT CLAIMED 3 and WHERE IT FAILS 3.
- **Report-only observation 2** (NOT CLAIMED 11 still said continuity in $k$ at fixed $(j,s)$ "is
  established in Step 15", which the applied P1-R41 de-asserts) → **P1-R56**.

## Drafted texts, as applied

### P1-R54 — Step 12 opening: strike the duplicated setup sentence

Strike, from the end of the P1-R52-rewritten opening, the sentence "Fix an arbitrary flagged pair
$(j,s)$, with no assumption that $j=j_k(s)$, and let $j'$ range over the menu elements generating
h.11's action set $\mathcal Q_j(s)$." (it duplicated, without the class definition, the paragraph
that follows), and amend the provenance parenthetical to:

> *(Restructured 2026-08-25, round 2 — **P1-R17**, on pass-1 finding 1 and pass-2 R16–R17; the
> chronology is in the repair table at the foot of this file. Opening rewritten 2026-08-29,
> **P1-R52**, polish-pass finding F17, to lead with the quantifier and the strategy rather than the
> repair history; its closing setup sentence struck the same day by **P1-R54**, which duplicated the
> paragraph below without that paragraph's class definition. The setup is the next paragraph's, and
> parts (a)–(d) are unchanged.)*

The paragraph carrying the class definition ("Fix a flagged pair $(j,s)$ — no assumption that
$j=j_k(s)$ — and let $j'$ range over the class generating h.11's action set: $j'$ agrees with $j$
on the pooled path up to $f_j(s)$ and $a_{j'}=a_j$.") is untouched.

### P1-R55 — carry the R46 withdrawal to the heading and the two citing sites

**(a) Step 18 heading:**

> **Step 18 (a possible route, not part of the claim and not established here: Kakutani in place of
> h.6's continuity half).**

**(b) NOT CLAIMED 3, appended as list-item continuation:**

> *Amended 2026-08-29 (**P1-R55**, following **P1-R46**, polish-pass finding F11): **more is
> disclaimed, not less.** The clause above lists what the correspondence-valued argument "still
> needs" as Step 15(i) and Step 14's bracket. It also needs a lemma that $\mathfrak T$ has convex
> values and a closed graph under this file's cutoff encoding, and Step 18 as now scoped proves no
> such lemma and draws no Kakutani conclusion. So the route is not merely outside P1's statement; it
> is unestablished.*

**(c) WHERE IT FAILS 3, replacing "The Kakutani route of Step 18 survives this case; the Brouwer
route the card fixes does not.":**

> The Brouwer route the card fixes does not apply here. Step 18's correspondence route
> is the natural candidate for a case of exactly this shape — an indifference plateau is where a correspondence is
> better behaved than a selection — but Step 18 draws no Kakutani conclusion, so **no route is
> claimed to survive this case**. *(Amended 2026-08-29, **P1-R55**, following **P1-R46**: the
> pre-repair clause read "The Kakutani route of Step 18 survives this case", which asserts what
> Step 18 no longer establishes.)*

### P1-R56 — NOT CLAIMED 11, appended as list-item continuation

> *Amended 2026-08-29 (**P1-R56**, following **P1-R41**, polish-pass finding F6): **strengthened,
> not narrowed.** The clause above records that continuity in $k$ at fixed $(j,s)$ "is established in
> Step 15". It is not, and Step 15 no longer says so: P1-R41 de-asserted it, because the
> $k$-dependence runs through the conditioning rather than through the pricing map, Step 9(b)'s two
> branches are different laws with no step showing they agree as $\Lambda_k\downarrow0$, and card
> §5's A5 and A6 evidence notes record the composition $k\mapsto(\hat v,\pi)\mapsto P$ as underived
> and as measured to jump. What this item now records is therefore **more** than it did: **neither**
> separate continuity is derived in this file — continuity in $k$ at fixed $(j,s)$ is not
> established, and continuity in $s$ at fixed $k$ is what (i) asks of the card — so the observation
> that their conjunction is strictly weaker than the joint statement the crossing-point argument
> consumes (batch-1 audit P1-R4) stands as a logical point but now names no available route.
> Continuity of $\mathcal T$ enters only through h.6 (Steps 15–16). The differentiability disclaimer
> above is unchanged.*

### Provenance-header sentence (proof header, with the batch list now reading P1-R36–P1-R39, P1-R41–P1-R42 and P1-R46–P1-R56)

> **P1-R54–P1-R56 are same-day seam follow-ons**, drafted by the auditor after reviewing the
> application of the first fourteen: R54 strikes the setup sentence P1-R52 left duplicating the
> paragraph below it, and R55 and R56 carry P1-R46's and P1-R41's consequences to the heading,
> disclaimer and failure-case sites that still read against them.

## What did not move

The five outstanding repairs stand unchanged (P1-R40-A/-B, P1-R43, P1-R44, P1-R45 — the header's
outstanding list is untouched). No hypothesis is added, no step conclusion changes, no label moves.
The two in-file referrers to NOT CLAIMED 11 (Step 17(ii), NOT CLAIMED 8) cite it for the Step 15(i)
joint-continuity content and still resolve; P1-R56 strengthens what they lean on.
