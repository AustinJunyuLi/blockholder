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

**Wording batch applied 2026-08-29** — repairs **P1-R36–P1-R39, P1-R41–P1-R42 and P1-R46–P1-R56**,
each landed verbatim from the drafted text in `threads/2026-08-29_gpt_p1_polish_audit.md` (the
in-house audit of the GPT Pro polish pass filed at `threads/2026-08-29_gpt_p1_polish.md`).
**P1-R54–P1-R56 are same-day seam follow-ons**, drafted by the auditor after reviewing the
application of the first fourteen: R54 strikes the setup sentence P1-R52 left duplicating the
paragraph below it, and R55 and R56 carry P1-R46's and P1-R41's consequences to the heading,
disclaimer and failure-case sites that still read against them.
All are wording-grade by that audit's own grading: no
hypothesis is added, no step conclusion changes, and **no label moves**. Four drafted repairs are
**outstanding and deliberately not applied**: **P1-R40-A/-B** (finding F5, antecedent-touching —
pending Austin's route choice), **P1-R43** and **P1-R44** (findings F8 and F9,
statement-preserving but new derivation — pending the two-pass gate), and **P1-R45** (finding F10 —
ordered behind P1-R40, being drafted consistently with Package A). Every repair text below is
CONJECTURE-grade edit text until the lane's gate runs over the proof carrying it.

**Substance batch applied 2026-08-29, later the same day.** Austin ruled the F5 route this date:
**P1-R40-A** (Package A — name what h.6's bracket clause delivers); **P1-R40-B is not pursued**.
Applied accordingly: **P1-R40-A items A1–A3** (Step 13's corner clause rewritten as a totalisation
with the bracket clause written out, Step 14's consumption form appended, NOT CLAIMED 16 added),
**P1-R43** (Step 8's joint-continuity appendix in the belief pair, Step 5(a)'s citation sharpened
to joint continuity), **P1-R44** (Step 9(b) now defines $\pi_n$ and carries the pair through to
the limiting price, with the NOTATION DELTA row for $\pi_n$) and **P1-R45** (Step 15(ii) restated
as robust threshold identification — landed exactly as drafted, its route condition being the ruled
one, together with its note against P1-R40). **The outstanding list above is now empty and the
R-number sequence is closed at this application**: nothing drafted in the 2026-08-29 polish audit
remains unapplied. R43 and R44 are statement-preserving derivations, R45 is wording-grade under the
ruled route, and R40-A names an antecedent clause the pre-repair text had misread; no step
conclusion changes — but the batch is **pending the lane's two-pass gate** (adversarial
proof-read and statements-only re-derivation, both by fresh agents) before the row rests on it,
and every repair text below remains edit text until that gate runs.

**Gate repair round applied 2026-08-30.** After the adversarial proof-read's **PASS-WITH-REPAIRS**
verdict on the 2026-08-29 substance batch — one WRONG finding (Step 15's boxed conclusion asserted
the identification $\mathcal T_i=c_i$ without argument; the reader's skipped-plan witness refutes
it under (i)+(ii) as previously stated) and four minor ones — this file's one sanctioned repair
round lands all five, each labelled *gate repair round, 2026-08-30, item N* at its site: item 1
extends Step 15(ii) with the weak-ordering clause and argues the identification the box had
asserted; item 2 declares $d_i(s,k)$ and $c_i(k)$ in the NOTATION DELTA; item 3 re-credits Step
9(b)'s two envelope arguments to h.17-d with $L_j\le1$; item 4 qualifies Step 14's parenthetical to
the canonical dominated-top case; item 5 adds the a.e.-density qualifier at Step 9(b)'s
$\Lambda_k=0$ branch. No R-numbers are minted — the R-sequence stays closed at the 2026-08-29
application above — and nothing outside the candidate-condition commentary enters the theorem's
load-bearing path: P1 continues to assume h.6's continuity outright (Steps 15–16), and no label is
moved by this round. **The retry read pends.**

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
12. **h.12 = card §4.1's nonnegative-premium restriction** *(was [ADDITION]; card gap closed —
    see the status note)*. $m_0\ge0$. With $\Delta_m>0$ and $\pi\in[0,1]$ this gives
    $\bar m(\mathcal I):=m_0+\pi(\mathcal I)\Delta_m\ge0$.
    *Status corrected 2026-08-29 (**P1-R47**, polish-pass finding F12): the pre-repair item was
    marked [ADDITION] and read "Card §4.1 restricts only $m_1>m_0$ and $\Delta_m>0$; it does not
    sign $m_0$", which was true at the 2026-08-20 stamp this file was written against and is stale
    at the controlling stamp — card §4.1's $m_0,m_1$ row now carries "**and $m_0\ge0$** — adopted
    from P1's h.12". The restriction originated in this proof and has been absorbed into the card;
    it is no longer an addition outside it. LABEL CLAIMED reason 2 and P1-R15 already record the
    absorption, and this item now records it too, on the pattern h.14 already uses.*
    *Used: Steps 7, 8.*
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
$$\Theta\;:=\;\{k\in[\underline s,\overline s]^{J-1}:\underline s\le k_1\le\cdots\le k_{J-1}\le\overline s\}$$
is the ordered box built on h.6's common bracket. It is **a** polytope of the kind card §4.5
requires — nonempty, compact and convex as the intersection of a cube with the $J-2$ half-spaces
$\{k_i\le k_{i+1}\}$ — and this proof fixes it as **the** $\Theta$ throughout. Card §4.5 states the
properties $\Theta$ must have and names no particular set, so the choice is this file's and is made
here, once.

*Clarified 2026-08-29 (**P1-R42**, polish-pass finding F7), which read the pre-repair "is card
§4.5's compact ordered polytope" as importing a possibly proper card-given polytope. **The
finding's proposed consequence is not adopted**: it would move Step 13's derived
$\mathcal T(k)\in\Theta$ into h.6's self-map clause, and on the ordered box the ordering and
bracket inequalities of Step 13 do imply membership, so the derivation stands and is not weakened
into an assumption.*

Define
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
$\{0,\dots,H\}\cup\{+\infty\}$; and — this is the D1-R2 repair written out — the filing objects are
Borel through the finite decomposition
$$\widetilde B_j^F(s)\;=\;\sum_{\ell=T}^{H}\mathbf 1\{f_j(s)=\ell\}\cdot B_j(s,\ell),
\qquad \widetilde Q_j^F(s)\;=\;b_j^*(s)-\widetilde B_j^F(s),$$
each a finite sum of products of Borel functions, hence Borel. On $\{D_j=1\}$ one has
$f_j(s)\in\{T,\dots,H\}$ by h.9, so $\widetilde B_j^F(s)=B_j(s,f_j(s))=B_j^F(s)$ and
$\widetilde Q_j^F(s)=Q_j^F(s)$ there. Off $\{D_j=1\}$ every indicator vanishes and the tildes are
a conventional extension by $\widetilde B_j^F:=0$; card §4.2 defines $B_j^F$ and $Q_j^F$ on the
flagged set and no step reads them elsewhere, so the extension is never consumed. Suppressing the
tildes on the flagged set, $B_j^F$ and $Q_j^F$ are Borel there.

*Corrected 2026-08-29 (**P1-R36**, polish-pass finding F1). The pre-repair display summed
$\mathbf 1\{f_j(s)=d+T\}\cdot B_j(s,d)$ over $d=0,\dots,H-T$, whose surviving factor is
$B_j(s,c_j(s))$ — the stake at the **crossing** date — where this step's own definition three
lines above requires $B_j(s,f_j(s))$, the stake at the **filing** date; at $c_j=2$ and $T=3$ the
old display returned $B_j(s,2)$ for $B_j(s,5)$, and card §4.2's $\partial_dB_j\ge0$ on Voice makes
the two differ on any plan still accumulating inside the window. The index is now the filing date
itself over its whole admissible range. The step's conclusion is unchanged.*

By h.9 the disclosure indicator is
$D_j(s;\tau,T)=\mathbf 1\{a_j=1\}\cdot\mathbf 1\{B_j(s,H-T)\ge\tau\}$,
Borel in $s$. Composing with Step 1, all of these become Borel functions of $s$ alone at the fixed
conjecture $k$.

**Step 3 (the pooled public-history family is finite; the flagged family is empty or uncountable,
and in neither case a finite nonempty indexed family).**
Card §4.3 defines $\mathcal H_d^P=(X_0,\dots,X_d;\text{flag landed by }d)$ with
$X_d=q_{jd}+z_d$. By h.2 the image of $\Gamma$ is finite and $z_d\in\{-\bar z,0,+\bar z\}$, so each
$X_d$ takes values in a finite set; $d$ ranges over the finite calendar $\{0,\dots,H\}$; and the
flag coordinate is a single bit. Hence the collection of pooled public histories is finite. By
Step 2 the flagged tuple $\sigma_F:=(B^F,Q^F,a=1)$ — card §4.6's $\mathsf S_F$, the filing message
$F$ augmented by the flagged order $Q^F$ — is Borel with **codomain**
$[0,\bar b]^2\times\{1\}$, a continuum: card §4.2 puts $B_j(s,d)\in[0,\bar b]$ with $s$ Gaussian
and imposes monotonicity only, and no card row discretises the stake level. What the construction
below runs on is the **image** of the flagged-pair map $(j,s)\mapsto(B_j^F(s),Q_j^F(s),1)$ on
$\{(j,s):D_j(s;\tau,T)=1\}$, and that image obeys a dichotomy. **If no plan flags** — A8 is not
assumed in the existence half, and WHERE IT FAILS 6's $\tau>\bar b$ realises this — the
flagged-pair set and its image are empty, and Steps 6, 10 and 12 are vacuous, as WHERE IT FAILS 6
already records. **If some plan flags at one signal**, that plan is Voice (h.4), and with
$D_j(s)=\mathbf 1\{a_j=1\}\mathbf 1\{B_j(s,H-T)\ge\tau\}$ (h.9) and $\partial_sB_j\ge0$ on Voice
(h.17-c) its flagged signal set is a nonempty up-set of $\mathbb R$, hence contains a half-line
and is uncountable; h.7 maps it injectively, so the image is uncountable. **Either way the flagged
layer cannot be handled as a finite nonempty indexed family**, and that is what forces the two
layers of Part B to be treated differently. This is exactly the D1-R2 finding.

*Corrected 2026-08-29 (**P1-R37**, polish-pass finding F2): the pre-repair heading and paragraph
said the flagged family "is not" finite, categorically, and read a continuum codomain as a
continuum index set. The empty case is admissible because A8 is not assumed for existence, and
empty is finite. The step's use is unchanged — Step 6 constructs on the image, whatever the image
is.*

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
With $\xi\sim N(0,\sigma_\xi^2)$ by **h.17-d** — card §4.1's distributional forms; h.1 supplies
$\xi$'s independence from $(v,\varepsilon,z_{0:H})$, which is what the previous sentence used, and
the strict positivity of its variance, not the Gaussian law itself —
$p=1-\Phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)$, which is card §4.3's entry row verbatim and
lies in $(0,1)$ for every finite $P$. *(Citation corrected 2026-08-29, **P1-R48**, polish-pass
finding F13.)* Define the inner pricing map
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
$\mathcal P_{\mathcal I}$ from h.12 ($m_0\ge0$), with **joint** continuity in the belief pair
$(\hat v,\pi)$ from Step 8. This is a genuine fixed point: the price appears on both sides
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

*Superseded 2026-08-29 (**P1-R49**, polish-pass finding F14). The ambiguity is resolved on the card
at the controlling stamp: card §4.3's $P_d^P$ row reads "**The genuine fixed point sits at control
nodes.** At an earlier pooled date $d<H$ the price is a *tower expectation* of already-solved
control-node values, with no self-reference; only the control-node map is a fixed point to be
solved", and cites this split by name. Reading (b) is therefore the card's, the regeneration item
is discharged, and the two-reading text above stands as the record of why this step was written to
survive either.*

The conclusion this step is used for survives on either reading, and that is why nothing downstream
turns on the adjudication: a finite family requires no selection argument, and the pooled price
family $k\mapsto(P_d^P(\mathcal H_d^P;k))_{\mathcal H_d^P}$ is a **finite**
vector, indexed by Step 3's finite pooled alphabet — each entry an inner root at the belief
summaries carried at its own history by (a) with Steps 7–8 at the control-node cell, and at $d<H$
by (b) a conditional expectation of already-solved control-node values, which integrates over the
continuous signal law and, on flagged branches, over the flagged-tuple law, and is **not** a finite
sum over terminal states. **No continuity of this family in the conjecture $k$ is claimed here**:
continuity in the belief summaries is Steps 7–8; continuity of the composition through the
conditioning is not derived (Step 15) and enters only through h.6. Histories of zero probability
under $k$, and histories of zero probability under every profile, are handled in Step 9(b) and
9(c) respectively. *(Amended 2026-08-29, **P1-R41**, polish-pass findings F6 and F14.)*

**Step 6 (flagged layer: a measurably selected family, built from Steps 7–8 rather than assumed —
the D1-R2 point).**
Work on the image of the flagged-pair map (Step 3). If that image is empty, parts (a)–(d) below
are vacuous and no flagged price is constructed or needed. Otherwise Step 3 makes it uncountable,
its elements written $\sigma_F\in[0,\bar b]^2\times\{1\}$, and the construction applies.
A pointwise statement — "at each $\sigma_F$ there is a
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
$\varrho'(P)=p'(P)\bigl(P+\bar m-A\bigr)+p(P)-1$, and
$p'(P)=-\phi\bigl((P+K+\bar m-\bar S)/\sigma_\xi\bigr)/\sigma_\xi<0$. Take any $P\ge A$. Then
$P+\bar m-A\ge\bar m\ge0$ by h.12, so the first term is $\le0$; and $p(P)-1<0$ since $p<1$ (Step
4). Hence
$$\varrho'(P)<0\qquad\text{for every }P\ge A,$$
not merely at roots. By (i) every root lies in $[A,\infty)$, and a strictly decreasing function has
at most one zero on an interval, so there is at most one root; (ii) supplies existence, so the root
is unique. *Replaced 2026-08-29 (**P1-R50**, polish-pass finding F15): the pre-repair argument
established $\varrho'<0$ at roots only and then ran a two-adjacent-roots contradiction. The global
statement follows from the same three facts, is shorter, and is the form Step 8's
implicit-function argument consumes.*

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

**Continuity in the full belief pair.** The pooled layer moves both summaries, so the root is
needed as a function of $(\hat v,\pi)$ and not of $\hat v$ alone. Write the residual with both
arguments,
$$\varrho(P;\hat v,\pi)=\bigl(1-p(P;\pi)\bigr)\bigl(A(\hat v,\pi)-P\bigr)+p(P;\pi)\,\bar m(\pi),$$
$$A=\hat v+\pi\Delta_V,\qquad \bar m=m_0+\pi\Delta_m,\qquad
p(P;\pi)=1-\Phi\!\Bigl(\tfrac{P+K+\bar m(\pi)-\bar S}{\sigma_\xi}\Bigr).$$
$A$ and $\bar m$ are affine in $(\hat v,\pi)$ by card §4.1 and h.12, and $\Phi$ is smooth, so
$\varrho$ is $C^1$ jointly in $(P,\hat v,\pi)$ on $\mathbb R\times\mathbb R\times[0,1]$. By Step
7(iii) in its sharpened form, $\partial_P\varrho<0$ at every $P\ge A$, hence at every root. The
implicit function theorem therefore gives a locally $C^1$ root $P=P(\hat v,\pi)$ around every
belief pair, and Step 7(ii)–(iii)'s global existence and uniqueness make those local root functions
agree wherever their domains overlap. **Hence the unique inner root is a single-valued continuous
function of $(\hat v,\pi)$ jointly on $\mathbb R\times[0,1]$.** The displayed
$\partial P/\partial\hat v\in(0,1]$ is the non-expansiveness bound in the $\hat v$ direction at
fixed $\pi$, which is what Step 6(b) consumes on the flagged cell, where $\pi\equiv1$ by Step 6(a).

*Added 2026-08-29 (**P1-R43**, polish-pass finding F8): Step 5(a) cited "continuity in the belief
from Step 8" and Step 9(b) invoked "Step 8's 1-Lipschitz bound" at pooled histories where $\pi$
varies, while the pre-repair Step 8 differentiated in $\hat v$ at fixed $\pi$ only. This appendix
supplies the joint statement those citations consume. **No hypothesis is added** — the argument
runs on h.12, Step 4's reduction and Step 7 alone — and no step conclusion changes.*

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
posterior, not merely of the posterior over plans.* For integers $n\ge J$ write
$$w_n(j\mid s)=(1-t_n)\,\mathbf 1\{j=j_k(s)\}+\tfrac{t_n}{J},\qquad t_n:=\tfrac Jn\in(0,1],\quad
t_n\downarrow0,$$
for the stage-$n$ mixing weight: the weights are nonnegative, sum to one, and give every plan at
least $t_n/J=1/n>0$, which is Step 9's own parameterisation of the perturbation. (For $n<J$ the
display is not a probability distribution — $t_n>1$ makes $1-t_n<0$ — and Step 9's "every plan with
weight at least $1/n$" is infeasible there, since $J/n>1$; the limit is unaffected by dropping
finitely many initial indices.) *(Index range stated 2026-08-29, **P1-R51**, polish-pass finding
F16.)* $t_n$ is written for the perturbation mass because $\varepsilon$ is card §4.1's
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
A ratio of polynomials in $1/n$ with a denominator that is nonzero for all large $n$ converges as
$n\to\infty$, **pointwise in $(j,s)$**. Write $\mu_\infty$ for that limit. **Which law it is
depends on the same denominator split the envelope below needs, and the two cases are not the same
law**; both are displayed there. This is where h.2's finiteness pays: with a continuum of pooled
histories the limit would need a separate argument.

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
plan-uniform one, and $t_n=J/n$ the perturbation mass. *If $\Lambda_k>0$* — the history is on path
under $k$ — then $Z_n\ge\Lambda_k/2$ for all large $n$, and
$2\lvert\mu_v+\beta(s-\mu_v)\rvert\varphi_sL_j/\Lambda_k$ is an integrable envelope by
h.17-d's Gaussian tail — Gaussian integrability of $\lvert s\rvert\varphi_s$, the envelope's
signal factor growing only linearly in $\lvert s\rvert$, with $L_j\le1$ — so dominated convergence
applies *(credit reworded, gate repair round, 2026-08-30, item 3: the pre-repair credit ran
"h.17-d's Gaussian tail and h.2's integrability clause"; what is used is Gaussian integrability of
$\lvert s\rvert\varphi_s$ (h.17-d) with $L_j\le1$, the likelihood being a product of noise
probabilities and an indicator, and the h.2 credit is dropped — mathematics unchanged)*; and since
$w_n(j\mid s)\to\mathbf 1\{j=j_k(s)\}$ pointwise and $Z_n\to\Lambda_k$,
$$\mu_\infty(j,s)=\frac{\mathbf 1\{j=j_k(s)\}\,L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}{\Lambda_k},$$
**the ordinary Bayes posterior generated by the conjectured map $j_k$** — the uniform tremble
washes out and the limit is *not* the plan-uniform law. *If $\Lambda_k=0$* — the $k$-null case —
the $(1-t_n)$ term vanishes $\Phi_s$-a.e. in numerator and denominator alike, so
$$\mu_n(j,s)=\mu_\infty(j,s)=\frac{L_j(\mathcal H_d^P\mid s)\,\varphi_s(s)}{\Lambda_u}$$
**exactly and $n$-free** (as an a.e. density identity) — the plan-uniform posterior restricted to
the history — and there is nothing to pass to the limit. *(Parenthetical added, gate repair round,
2026-08-30, item 5: the identity holds as an a.e. density identity, as the vanishing of the
$(1-t_n)$ term already does, and not pointwise at every $s$.)* (Without the split the bare claim
would be false as stated:
$\mu_n\le\varphi_sL_j/Z_n$ with $Z_n\downarrow0$ is not a uniform envelope.) In both cases the
displayed density is a probability density at the history.

*Corrected 2026-08-29 (**P1-R38**, polish-pass finding F3). The pre-repair text characterised the
limit, unconditionally at every reachable history, as "the plan-uniform-weighted joint law
restricted to the history". That is false whenever $\Lambda_k>0$, and it contradicted this step's
own closing sentence that on path the belief agrees with the Bayes posterior. The two-case reading
is the one card §5's A6 evidence note already attributes to this step and the one Step 17(iii)
and 17(iv) consume.*

Both belief summaries have to be carried, because Step 4's pricing map depends on the information
set through the pair. Alongside $\hat v_n$ define the stage-$n$ engagement posterior
$$\pi_n\;:=\;\sum_{j\in\mathcal J}a_j\int\mu_n(j,s)\,\mathrm ds\;\in[0,1],$$
card §4.3's $\pi(\mathcal I)$ evaluated at $\mu_n$. If $\Lambda_k>0$, then $a_j\in\{0,1\}$ (card
§4.2) makes $a_j\mu_n(j,s)\le\mu_n(j,s)$, so the same denominator bound gives the integrable
envelope $2\varphi_sL_j/\Lambda_k$ — Gaussian integrability of $\varphi_s$ (h.17-d) with
$L_j\le1$ *(the same reworded credit, gate repair round, 2026-08-30, item 3)* — and dominated
convergence yields $\pi_n\to\pi_\infty$; if
$\Lambda_k=0$, then $\mu_n$ is $n$-free by the display above, so $\pi_n$ is constant and the
convergence is immediate. The same two cases give $\hat v_n\to\hat v_\infty$. Hence
$(\hat v_n,\pi_n)\to(\hat v_\infty,\pi_\infty)$, and by **Step 8's joint continuity of the unique
inner root in $(\hat v,\pi)$** the prices converge with them: $P_n\to P_\infty$. Step 8's bound
$\partial P/\partial\hat v\in(0,1]$ remains available for comparisons at fixed $\pi$.

*Added 2026-08-29 (**P1-R44**, polish-pass finding F9): the pre-repair sentence inferred price
convergence from $\hat v_n\to\hat v_\infty$ together with Step 8's 1-Lipschitz bound alone. The
price is a function of both summaries; $\pi_n$ was never defined, never shown to converge, and the
1-Lipschitz bound is a $\hat v$-direction bound at fixed $\pi$. **Depends on P1-R43.**
No hypothesis is added and no step conclusion changes.*

Hence the limiting belief **and the limiting price** exist at every reachable
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
here:** fix once and for all a **$k$-independent reference belief**
$(\hat v_\circ,\pi_\circ)\in\mathbb R\times[0,1]$ — for definiteness $(\mu_v,1)$, card §4.1's
prior mean of $v$ paired with certain engagement, and any other pair fixed independently of $k$
does equally — and assign to every unreachable pooled history the **inner root at that belief**,
i.e. the unique
$P_\circ$ with $\mathcal P_{(\hat v_\circ,\pi_\circ)}(P_\circ)=P_\circ$, which exists and is unique by
Step 7 under h.12. Then $U_j(s;k)$ is defined at **every**
$(j,s,k)$, and no §3 item is touched: §3(iii), §3(iv) and §3(vi) constrain beliefs and prices only at
histories carrying positive probability under some profile, and these carry none.
*Corrected 2026-08-29 (**P1-R39**, polish-pass finding F4). The pre-repair instantiation was
$(\mu_v,\Pr(a=1))$. $\mu_v$ is a card §4.1 primitive; $\Pr(a=1)$ is not. Engagement is attached to
the plan (card §4.2's $a_j$ row) and the model carries no prior over plans, so the unconditional
engagement probability is undefined without a strategy and, once one is supplied, equals
$\Pr(a_{j_k(s)}=1)$ — a functional of the conjecture. The convention has to be $k$-independent,
both because this step's own rider records that the reference belief can move $\mathcal T_i(k)$
through a $\Phi_s$-null signal set and because the card's P1 row requires one price system fixed
once and used at every $k\in\Theta$. The scalar $1$ is not substantive; what is essential is that
$\pi_\circ$ not be computed from the conjectured plan distribution.*
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
The requirement to be discharged is card §3(ii) at **every** flagged pair, including pairs the
date-0 cutoff policy does not select — h.11 defines an action set $\mathcal Q_j(s)$ at every
flagged pair, and a date-0 deviation to a non-selected plan that flags creates a genuine round-2
information set carrying §3(ii). The argument therefore **cannot** run through date-0 optimality:
at a non-selected pair there is none to appeal to, and that is exactly what lets the argument below
reach those nodes.
*(Restructured 2026-08-25, round 2 — **P1-R17**, on pass-1 finding 1 and pass-2 R16–R17; the
chronology is in the repair table at the foot of this file. Opening rewritten 2026-08-29,
**P1-R52**, polish-pass finding F17, to lead with the quantifier and the strategy rather than the
repair history; its closing setup sentence struck the same day by **P1-R54**, which duplicated the
paragraph below without that paragraph's class definition. The setup is the next paragraph's, and
parts (a)–(d) are unchanged.)*

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
$[\underline s,\overline s]$ by construction. The display's $\inf\emptyset:=\overline s$ is a
**totalisation, not a code for "never"**: it makes $\mathcal T_i$ defined at every $k$, and under
h.6 it is never triggered. **What h.6's bracket clause is assumed to deliver, written out.** h.6
asserts that all best-response cutoffs lie in the common compact ordered polytope $\Theta$; read at
the level Step 14 consumes it, that is: *for every $k\in\Theta$ and every $i\in\{1,\dots,J-1\}$ the
set $\{s\in\mathbb R:j^\star(s;k)\ge i+1\}$ is a **nonempty** up-set whose infimum lies in
$[\underline s,\overline s]$.* Under that clause, and because $j^\star(\cdot;k)$ is weakly
increasing so each such set **is** an up-set, the infima genuinely represent $j^\star$ on **all of
$\mathbb R$**: $j^\star(\cdot;k)$ agrees with Step 1's $j_{\mathcal T(k)}$ at every $s$ except
possibly the finitely many $\mathcal T_i(k)$ at which the up-set fails to contain its own infimum,
where the two differ by the boundary convention alone — card §3(i) pins no convention there.

*Corrected 2026-08-29 (**P1-R40-A**, polish-pass finding F5). The pre-repair text read
$\inf\emptyset:=\overline s$ as a live corner code — "a plan that is optimal nowhere contributes an
empty up-set and its cutoff sits at the top of the bracket, so it simply never appears in the range
of $j^\star$" — and **that reading is false as a representation claim**. Step 1 codes
$j_k(s)=1+\#\{i:k_i\le s\}$, so $k_i=\overline s$ does not retire plan $i+1$: it activates it at
every $s\ge\overline s$. Take $J=2$ on a menu whose plan 2 is dominated, so $j^\star(\cdot;k)\equiv1$
at every $k$ — admissible under h.3, and the same configuration this step's own tangency
counterexample below produces. Then $\{s:j^\star\ge2\}=\emptyset$, $\mathcal T_1\equiv\overline s$,
$\mathcal T$ is constant (so h.6's continuity and self-map halves both hold) and Brouwer returns
$k^\star=\overline s$, while $j_{k^\star}(s)=2$ for every $s\ge\overline s$. The signal is Gaussian
(h.17-d) and $\overline s$ is finite, so $\Pr(s\ge\overline s)>0$: the two maps disagree on a
**positive-probability** tail rather than at finitely many points, and Step 17(i)'s
$\Phi_s$-almost-sure consistency clause and Step 19's "$\Omega$ is unaffected" parenthetical both
fail there. The mirror case is the lower endpoint: if $j^\star\ge i+1$ at some $s<\underline s$,
the infimum over $[\underline s,\overline s]$ returns $\underline s$ and the two maps disagree on
$(-\infty,\underline s)$. The bracket clause as now stated excludes both.*

Hence $\mathcal T(k;\vartheta)\in\Theta$ for every
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

Said in the form Step 13 consumes: what h.6's bracket clause supplies is that **every** adjacent-pair
indifference signal **exists** and lies in $[\underline s,\overline s]$ — which is exactly what the
four-action argument above establishes in its specialisation, and exactly what excludes both an
adjacent pair with no crossing anywhere (in the canonical dominated-top case: the dominated top
plan is optimal nowhere, every plan above it with it) and an adjacent pair whose crossing sits
outside the bracket. A menu with a dominated top plan satisfies h.1–h.4, h.7 and h.9–h.17 and
**fails this clause**; on such a menu P1 asserts nothing.

*Qualified, gate repair round, 2026-08-30, item 4. The pre-repair parenthetical equated "an
adjacent pair with no crossing anywhere" with "a plan optimal nowhere, and with it every plan above
it" unconditionally. That equation holds in the canonical dominated-top case the surrounding
sentences are about — there the top pair's difference never crosses and the dominated top plan is
optimal nowhere — but not in general: a plan can be optimal nowhere while **every** adjacent pair
crosses, as the gate's skipped-plan witness shows ($U_1\equiv0$, $U_2=s-1$, $U_3=2s-1$ crosses in
both adjacent pairs yet plan 2 is argmax-absent everywhere; recorded at Step 15, gate repair
round, item 1). The parenthetical is narrowed to the case it actually names; the exclusion the
clause states — no adjacent pair without an in-bracket crossing, no crossing outside it — is
unchanged.*

**Step 15 (continuity: this is where h.6 assumes rather than derives, and here is exactly what it is
assuming).**
**Nothing in Steps 4–10 derives continuity of $k\mapsto U_j(s;k)$ at fixed $(j,s)$, and this step
does not assert it.** One link of the chain is derived: Step 7(iii) and Step 8 make the inner root
exist, be unique and be continuous in its **belief summaries** $(\hat v,\pi)$, and by Step 4 those
summaries are the only channel through which the information set enters the price. The other link
is not. The $k$-dependence runs through the **conditioning**: $(\hat v,\pi)$ are ratios of
integrals over signal intervals with endpoints $k$, continuous in $k$ only while the conditioning
event's probability stays bounded away from zero, and at a history whose probability vanishes as
$k$ moves it is Step 9's **construction**, not a continuity argument, that supplies the value —
and Step 9(b)'s two branches are *different laws* (the $j_k$-concentrated Bayes posterior where
$\Lambda_k>0$, the plan-uniform posterior where $\Lambda_k=0$), with no step here showing they
agree as $\Lambda_k\downarrow0$. Card §5's A5 evidence note draws exactly this distinction and
records the composition $k\mapsto(\hat v,\pi)\mapsto P$ as the underived one; card §5's A6 evidence
note records it **measured to jump**, on $\bigcup_h\partial\{k:\Lambda_k(h)>0\}$, at the implemented
calibration. **P1 therefore consumes h.6 as an assumption at precisely this point**: for the named
largest-weakly-increasing-selection tie-break, the $\inf\emptyset$ totalisation and Step 9(c)'s
reference-belief convention, $\mathcal T$ is a continuous self-map of $\Theta$ (Step 16).
Conditions (i) and (ii) below are **candidate primitive sufficient conditions** for that
assumption — the weakest pair this file can name — and are not consequences of the preceding steps:

*Corrected 2026-08-29 (**P1-R41**, polish-pass finding F6). The pre-repair opening asserted flatly
that "$U_j(s;k)$ is continuous in $k$ for each fixed $(j,s)$", carried a struck-h.5 clause marked
as commentary inside that assertion, and then reasoned from it ("**That is** continuity in $k$ at
fixed $(j,s)$, and it is not enough"). The assertion is derived nowhere in this file and the card's
A5 and A6 evidence notes record the composed object as measured to fail. Nothing downstream is
lost: this step's route to continuity of $\mathcal T$ was already h.6 asserting it outright at Step
16, as the struck h.5(c) records.*

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

 (ii) *Robust threshold identification.* For each adjacent pair write
 $d_i(s,k):=U_{i+1}(s;k)-U_i(s;k)$. The condition is: for every $k\in\Theta$ there is a **unique**
 $c_i(k)\in[\underline s,\overline s]$ with
 $$d_i(s,k)<0\ \text{ for } s<c_i(k),\qquad d_i(s,k)>0\ \text{ for } s>c_i(k).$$
 **And, across pairs, the thresholds are weakly ordered** — $c_1(k)\le c_2(k)\le\cdots\le
 c_{J-1}(k)$ for every $k\in\Theta$ — equivalently, no plan is argmax-absent everywhere.
 *(Weak-ordering clause added, gate repair round, 2026-08-30, item 1; the boxed conclusion below
 records why it is needed.)* This asks strictly more than h.3 plus a tie set of empty interior.
 h.3 says the difference
 **crosses** zero at most once, which admits two failures: an interval of ties — which the
 pre-repair (ii) excluded, and which is all it excluded — and an isolated **tangency**, at which
 $d_i\le0$ everywhere with one zero, so that there is no crossing, no sign change and no threshold
 at all. Step 13's own "Why not the largest maximiser" counterexample is that tangency, and it sits
 inside h.3.

**Under (i) and (ii) — with (ii) as extended above — each $\mathcal T_i=c_i$, and each $c_i$ is
continuous, by the following topological argument — the implicit function theorem is the wrong
tool here, since it would need $U$ differentiable in $(s,k)$ and no hypothesis supplies that
(batch-1 audit P1-R4).** *The identification, argued (gate repair round, 2026-08-30, item 1).* Fix
$k$ and $s$ and write $m:=\#\{i:s>c_i(k)\}$. By the weak-ordering clause the counted indices form
a prefix $\{1,\dots,m\}$, so the increments of the payoff sequence $U_1(s;k),\dots,U_J(s;k)$ read
$d_1,\dots,d_m>0$ and $d_{m+1},\dots,d_{J-1}<0$, each sign by the threshold clause: the sequence
strictly increases up to index $1+m$ and strictly decreases after it. Hence, off the finitely many
threshold points themselves, the argmax is single-valued and is the counting map
$$\arg\max_{j\in\mathcal J}U_j(s;k)\;=\;1+\#\{i:s>c_i(k)\},$$
Step 1's map; at a threshold point $s=c_i(k)$, (i)'s continuity in $s$ forces $d_i(s,k)=0$, so the
argmax there can only widen across the plans tied at that point. The counting map is weakly
increasing in $s$, so it is itself a weakly increasing selection from the argmax, and every
selection agrees with it off the threshold points: $j^\star(\cdot;k)$ is the counting map at the
cutoff vector $(c_1(k),\dots,c_{J-1}(k))$, and that vector represents it. Reading Step 13's infimum
off that representation — $\{s:j^\star(s;k)\ge i+1\}$ is $\{s:s>c_i(k)\}$ up to the threshold
points themselves, and below $c_i(k)$ the argmax never reaches plan $i+1$ — gives
$$\mathcal T_i(k)\;=\;\inf\{s:s>c_i(k)\}\;=\;c_i(k)\qquad\text{for every }i,$$
the identification. *Continuity.* Let $k_n\to k$ in $\Theta$ and take any convergent subsequence
$c_i(k_{n'})\to c$, which exists because $[\underline s,\overline s]$ is compact. For every $s<c$
one eventually has $s<c_i(k_{n'})$, so $d_i(s,k_{n'})<0$, and (i)'s joint continuity gives
$d_i(s,k)\le0$; symmetrically $d_i(s,k)\ge0$ for every $s>c$. Uniqueness of the sign threshold at
$k$ forces $c=c_i(k)$. Every convergent subsequence has the same limit, so $c_i(k_n)\to c_i(k)$ —
which, by the identification just argued, is continuity of each component $\mathcal T_i$ of
$\mathcal T$. These conditions are sufficient and are **not** claimed weakest; P1 continues to
assume their conclusion through h.6, and (i)+(ii) is the weakest pair this file can name that would
replace it.

*Gate repair round, 2026-08-30, item 1 — the gate's WRONG finding, repaired by the reader's first
route. The pre-repair boxed conclusion opened "Under (i) and (ii), each $\mathcal T_i=c_i$ is
continuous", an identification asserted nowhere and false under (i)+(ii) as previously stated. The
reader's skipped-plan witness: $J=3$ with $U_1\equiv0$, $U_2=s-1$, $U_3=2s-1$ on the bracket
$[-2,2]$ has adjacent thresholds $c_1=1$ and $c_2=0$, each the unique strict sign threshold of its
pair in-bracket, so the pre-repair (ii) held; the argmax runs $1\to3$ at $s=\tfrac12$, and both
upper level sets are nonempty up-sets with infima in the bracket, so (i), h.3 and h.6's bracket
clause held too — yet $\mathcal T_1=\mathcal T_2=\tfrac12\neq c_1,c_2$: plan 2 is argmax-absent
everywhere and is skipped. The weak-ordering clause is added to (ii) and the identification is now
argued in the box. The candidate conditions remain outside the theorem's load-bearing path — P1
assumes h.6's continuity outright (Steps 15–16) — so nothing the theorem rests on changes.*

*Corrected 2026-08-29 (**P1-R45**, polish-pass finding F10): the pre-repair (ii) asked only that
the indifference set have empty interior, and the boxed conclusion then ran on "the strict sign
change of $U_{i+1}-U_i$ at each crossing", which empty interior does not supply — the tangency case
satisfies h.3 and empty interior and has no crossing. **Note against P1-R40:** the finding's own
proposed condition additionally permitted $c_i(k)=\overline s$ to encode an upper plan never
preferred within the bracket, which is precisely the corner encoding finding F5 shows the finite
cutoff vector cannot carry; that permission is not adopted.*

Note also that (i) is not independent of h.7: a stake path that is flat on a signal interval
destroys injectivity there, which is the turn-2 audit's L2-R1 finding seen from the other side,
so the card cannot buy continuity by weakening monotonicity.

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

**Step 18 (a possible route, not part of the claim and not established here: Kakutani in place of
h.6's continuity half).**
Define instead the best-response correspondence
$\mathfrak T(k)=\{k'\in\Theta:k'\text{ represents some optimal weakly increasing plan selection at
}k\}$. It is nonempty by h.3, and its values are compact as closed subsets of the compact $\Theta$.
A Kakutani argument would additionally need a lemma that, **under this file's cutoff encoding**,
$\mathfrak T$ has **convex** values and a **closed graph**, and no such lemma is proved here. The
plateau picture — at an indifference plateau the admissible values of a component form an interval
and the ordering constraints cut the product by half-spaces — does not by itself show that every
admissible cutoff vector is an independent component-wise choice, and it does not cover skipped
plans or non-adjacent ties; and the maximum theorem, which concerns choice from a fixed set at a
parameter, does not by itself deliver a closed graph for a **selection-valued** problem whose
limits must remain *represented* under the corner conventions of Step 13 — conventions that
P1-R40's finding shows are not representation-faithful in general. **No Kakutani conclusion is
therefore drawn here.** Card §3 fixes the Brouwer route for P1, so this stays a remark; see NOT
CLAIMED 3.

*Scoped 2026-08-29 (**P1-R46**, polish-pass finding F11): the pre-repair text asserted convex
values and a closed graph outright and concluded that "Kakutani's theorem then gives a fixed point
without Step 15(ii) and without h.6's continuity clause". That conclusion is withdrawn as
unestablished. It is outside the claim (NOT CLAIMED 3) and no step reads it, so nothing the theorem
rests on changes.*

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
increases across plans by (c). Writing $s_F(k^\star)$ for the infimum of that upper interval, and
adopting **for this step alone** the extended-real conventions
$$\inf\emptyset:=+\infty,\qquad \inf\mathbb R:=-\infty$$
— **not** Step 13's $\inf\emptyset:=\overline s$, which totalises $\mathcal T_i$ inside the bracket
and is a different convention for a different object —
$$\Omega\;=\;1-\Phi_s\bigl(s_F(k^\star)\bigr)\;\in[0,1],$$
with endpoint values $\Omega=0$ at $s_F=+\infty$ (nothing flags — WHERE IT FAILS 6's $\tau>\bar b$)
and $\Omega=1$ at $s_F=-\infty$ (everything flags — the symmetric case named in the same item).
Hence
$$0<\Omega<1\quad\Longleftrightarrow\quad s_F(k^\star)\in\mathbb R,$$
which is h.8 restated as a single signal threshold. *(Tightened 2026-08-29, **P1-R53**, polish-pass
finding F18: the pre-repair sentence read "h.8 is equivalent to $s_F(k^\star)$ being finite and
strictly above $-\infty$", redundant on its face, and left the two degenerate flagged sets without
a stated $s_F$.)* **Conditions (a) and (c) are h.15 and h.13,
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
   not apply. The Brouwer route the card fixes does not apply here. Step 18's correspondence route
   is the natural candidate for a case of exactly this shape — an indifference plateau is where a correspondence is
   better behaved than a selection — but Step 18 draws no Kakutani conclusion, so **no route is
   claimed to survive this case**. *(Amended 2026-08-29, **P1-R55**, following **P1-R46**: the
   pre-repair clause read "The Kakutani route of Step 18 survives this case", which asserts what
   Step 18 no longer establishes.)*
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
| $\pi_n$ | the stage-$n$ engagement posterior at a pooled history, $\sum_ja_j\int\mu_n(j,s)\,\mathrm ds$ (Step 9(b)) | card §4.3's $\pi(\mathcal I)$ evaluated at $\mu_n$, not a new object; the subscript $n$ matches $\mu_n$, $w_n$, $t_n$ and $Z_n$ and keeps it clear of $\pi_\circ$, the reference-belief scalar of Step 9(c). Declared 2026-08-29, **P1-R44** |
| $\varphi_s$ | density of the Gaussian signal $s$ (Step 9(b)) | distinct from $\phi$, the unit-normal density, which appears only inside $p'(P)$ at Step 7(iii), and from $\Phi_s$, this table's signal c.d.f. Declared 2026-08-29 (**P1-R51**): the symbol was in use at Step 9(b) and named only inside the $t_n$ row's gloss, which card §8 rule 3 does not satisfy |
| $\mathcal S(k)$, $\mathfrak w$ | the set of **weakly increasing selections** from $s\mapsto\arg\max_jU_j(s;k)$, and a generic element of it (Step 13) | $\mathcal S(k)$ is calligraphic with its argument always written, so it is clear of card §4.4's $\mathcal S$, $\mathcal S_P$, $\mathcal S^{GE}$ (liquidity sensitivities, never argument-of-$k$) — and it appears only in Step 13. $\mathfrak w$ is **fraktur**, joining Step 18's $\mathfrak T$ in that family: distinct from Step 9(b)'s italic $w_n$, the mixing weight, which is the only other $w$ in the file. **These dummies replace an earlier $\sigma_1,\sigma_2,\sigma_s$** (confirm-pass sweep): lowercase $\sigma$ is reserved for the flagged tuple $\sigma_F$ and the declared variances $\sigma_v,\sigma_\varepsilon,\sigma_\xi$, and no other lowercase $\sigma$ appears in this file |
| $d_i(s,k)$ | the adjacent-pair payoff difference $U_{i+1}(s;k)-U_i(s;k)$ of Step 15(ii): a two-argument function of the signal $s$ and the cutoff vector $k$ | distinct from the calendar index $d$ of card §4.2 — the pooled date of $B_j(s,d)$, $q_{jd}$, $\mathcal H_d^P$: $d_i$ always carries its adjacent-pair subscript $i$ and never dates anything. Declared 2026-08-30, gate repair round, item 2 |
| $c_i(k)$ | the unique strict sign threshold of $d_i(\cdot,k)$ in the bracket (Step 15(ii)): indexed by the adjacent pair, a function of the conjecture $k$ | distinct from card §4.2's crossing date $c_j(s;\tau)$, which carries an $s$-argument (and the policy $\tau$): subscript $i$ against $j$, argument $k$ against $(s;\tau)$. Declared 2026-08-30, gate repair round, item 2 |
| $(\hat v_\circ,\pi_\circ)$, $P_\circ$ | the fixed **reference belief** of Step 9(c) — for definiteness the $k$-independent pair $(\mu_v,1)$ (**P1-R39**, 2026-08-29) — and the inner root at it, the price assigned at unreachable pooled histories | the open-circle subscript marks "reference/conventional" and is used nowhere else; $\hat v$ and $\pi$ are the card's own belief summaries (§4.3), so the objects are card objects at a named belief rather than new ones, which is the point of the convention (Step 9(c), retry finding 3) |
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
   *Amended 2026-08-29 (**P1-R55**, following **P1-R46**, polish-pass finding F11): **more is
   disclaimed, not less.** The clause above lists what the correspondence-valued argument "still
   needs" as Step 15(i) and Step 14's bracket. It also needs a lemma that $\mathfrak T$ has convex
   values and a closed graph under this file's cutoff encoding, and Step 18 as now scoped proves no
   such lemma and draws no Kakutani conclusion. So the route is not merely outside P1's statement; it
   is unestablished.*
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
    *Amended 2026-08-29 (**P1-R56**, following **P1-R41**, polish-pass finding F6): **strengthened,
    not narrowed.** The clause above records that continuity in $k$ at fixed $(j,s)$ "is established in
    Step 15". It is not, and Step 15 no longer says so: P1-R41 de-asserted it, because the
    $k$-dependence runs through the conditioning rather than through the pricing map, Step 9(b)'s two
    branches are different laws with no step showing they agree as $\Lambda_k\downarrow0$, and card
    §5's A5 and A6 evidence notes record the composition $k\mapsto(\hat v,\pi)\mapsto P$ as underived
    and as measured to jump. What this item now records is therefore **more** than it did: **neither**
    separate continuity is derived in this file — continuity in $k$ at fixed $(j,s)$ is not
    established, and continuity in $s$ at fixed $k$ is what (i) asks of the card — so the observation
    that their conjunction is strictly weaker than the joint statement the crossing-point argument
    consumes (batch-1 audit P1-R4) stands as a logical point but now names no available route.
    Continuity of $\mathcal T$ enters only through h.6 (Steps 15–16). The differentiability disclaimer
    above is unchanged.*
12. That card §4.3's $Y$ row has been disambiguated. Step 5 records the two readings of the $P$ inside
    the takeover branch and shows the step's conclusion survives both; pinning the row is a card
    edit and a regeneration item, not a claim of this file.
    *Amended 2026-08-29 (**P1-R49**): **discharged.** Card §4.3's $P_d^P$ row pins the reading at the
    controlling stamp — earlier pooled dates are tower expectations of solved control-node values, with
    no self-reference — so this item no longer disclaims a live ambiguity. What it now records is that
    the disambiguation is the card's and that this file's step was written to survive either reading.*
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

16. That P1 covers menus on which some adjacent plan pair has no indifference signal in the common
    bracket — in particular menus with a dominated top plan, where $\{s:j^\star(s;k)\ge i+1\}$ is
    empty. h.6's bracket clause as Steps 13–14 consume it excludes them, and Step 13's corrected
    corner note records why: under Step 1's coding the finite cutoff vector cannot represent
    $j^\star$ on the Gaussian tails there. *Added 2026-08-29, P1-R40-A, polish-pass finding F5.*

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
| **P1-R30** (retry finding 3, REPAIR) | **Step 9(c)'s unreachable-history convention changed from $\mathbb E[Y]$ to the inner root at a fixed reference belief** $(\hat v_\circ,\pi_\circ)$ — for definiteness the prior pair $(\mu_v,\Pr(a{=}1))$ — which exists and is unique by Step 7 under h.12. Reason: $\mathbb E[Y]$ is an unconditional average of realised control-node values and is in general **not** a root of $\mathcal P_{\mathcal I}$ at any belief, so the constructed object would have carried prices that are not inner fixed points at nodes where the blockholder does trade, while the card row's conclusion says "prices at their inner fixed points" without qualification. Card §4.3's $P_{-1}^P:=\mathbb E[Y]$ precedent does not transfer — that is the pre-trading node. With the reference-belief root **every price in the object is an inner fixed point at the belief carried there**, and the mismatch with the row is gone. NOT CLAIMED 13(b) updated. *Amended 2026-08-29 by **P1-R39** (polish-pass finding F4): the instantiation this row names, $(\mu_v,\Pr(a{=}1))$, is not $k$-independent — $\Pr(a=1)$ is a functional of the conjectured plan map — and is replaced by $(\mu_v,1)$. **The change of convention this row records — from $\mathbb E[Y]$ to the inner root at a fixed reference belief — stands unchanged**, together with its reason.* |
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
