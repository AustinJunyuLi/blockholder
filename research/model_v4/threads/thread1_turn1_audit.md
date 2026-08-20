# Audit — Thread 1, turn 1 (statement-only model card + theorem stack)

Source under audit: `research/model_v4/threads/thread1_turn1_answer.md` (verbatim, never edited;
read through the copy-paste mangling: display-math delimiters lost, stray `====` setext underlines
and `#` marks inside equations, citation glyphs dropped).

Auditor: Claude Code (theory lane), 2026-08-20, repo `blockholder_v4_theory` @ `5b34a40`.
Stance: adversarial — every item was attacked before it was passed.
Verdicts: **OK** / **WRONG** (a source contradicts it) / **MISCITED** (claim stands, citation does
not) / **UNCHECKED** (could not be checked here; listed, never triaged away).

---

## (a) O-1 facts vs the referee report

Authority: `quality_reports/reports/2026-08-19_framework_v3_referee_report.md` lines 116–124.

**A1 — the three ratios 1.06, 1.19, 1.14. OK.**
Answer l.5: "the reported ratios were (1.06), (1.19), and (1.14)".
Report l.116–117: "TV ratio (disc/no-disc) = 1.06 at ω_P=0.037 (baseline), 1.19 at 0.129, 1.14 at
0.286". Exact match, in order.
*Incidental (not a defect of the answer):* `docs/adr/0007-one-theorem-two-round-model-two-lanes.md`
states the middle ratio as **1.18**, not 1.19. The answer follows the referee report, which is the
executed record. The ADR is owned by the empirics lane; flagged for the convergence owner, not
edited here.

**A2 — "attenuation only at disclosed mass 0.50". OK.**
Answer l.5: "with attenuation appearing only at disclosed mass (0.50)".
Report l.118: "only at ω_P=0.50 does it fall (0.38)."

**A3 — "no attenuation below ~0.29". OK.**
Answer l.5: "did **not** attenuate ... when disclosed mass was below approximately (0.29)".
Report l.116: "is **not** lower under disclosure for ω_P ≤ ~0.29"; l.118: "Pointwise slopes:
disclosure is steeper at κ ≥ 0.7 for ω_P ≤ 0.29."

**A4 — the 0.38 number. OK.**
Answer l.1376 (T1 check request): "must reproduce the documented directions around (1.06,1.19,1.14,)
and (0.38)".
Report l.118: "only at ω_P=0.50 does it fall (0.38)." The answer uses 0.38 as a fourth documented
direction, which is what it is — the ratio at ω_P = 0.50, i.e. the one attenuating cell.

**A5 — old calibration: disclosed mass ≈ 0.037, "difference below one percent and even slightly
greater mean liquidity-sensitivity". OK.**
Answer l.1551: "The previous calibration's disclosed mass of approximately (0.037) produced a
difference below one percent and even slightly greater mean liquidity-sensitivity in the disclosed
comparison."
Report l.120–123: "ω_P ≈ 0.037 (k_D = 2.26, μ=1, σ_s=0.707), so the memo's headline figure ... shows
two curves whose ranges over κ∈[0.15,0.85] are 0.01107 vs 0.01117 — a <1% difference, and by mean
|slope| the *disclosed* regime is slightly more sensitive (0.0251 vs 0.0236)."
The answer does not reproduce the two curve ranges, but its two summary statements are both correct:
(0.01117 − 0.01107)/0.01107 = 0.90% < 1%, and 0.0251 > 0.0236 is the "slightly greater mean
liquidity-sensitivity". No inflation, no rounding in the answer's favour.

**A6 — unit of the 0.037. OK, with a mandatory note.**
The referee report's ω_P is `draft_v2.tex:424` — `\omega_P ≡ P(s ≥ k_D) = 1 − Φ(α_D)`, an
*unconditional* mass. In the new card that object is **Ω = Pr(D=1)**, *not* the answer's
**ω = Pr(D=1 | a=1)**. The answer never mislabels it (it writes "disclosed mass"), so this is OK —
but 0.037, 0.129, 0.286, 0.50 and the ~0.29 cut are all Ω-type numbers and must never be compared to
an ω-type calibration target. Carried into the card and into msg 2.

---

## (b) Invented references / reuse claims

The answer's §1.1 item 6 claims existence "should reuse the Gaussian signal, ordered cutoff,
competitive-pricing fixed point, and outer Brouwer machinery from draft_v2". Each checked in the
frozen manuscript:

**B1 — Gaussian signal. OK.** `draft_v2.tex:211` `s = v + \varepsilon, \varepsilon ~ N(0,
\sigma_\varepsilon^2)`; `:215` posterior mean linear, `\hat v(s) = \mu + \beta(s-\mu)`, `\beta =
\sigma_v^2/(\sigma_v^2+\sigma_\varepsilon^2)`; symbol table `:1837–1839`.

**B2 — ordered cutoffs. OK.** `draft_v2.tex:392` "cutoff rules with (weakly) ordered thresholds
k_1 ≤ k_0 ≤ k_D"; `:618` existence "in (weakly ordered) cutoff strategies"; `:1029` ordering
preserved, regions may collapse. The answer's "weak inequalities permit action regions to collapse,
including a collapsed Hold region" (l.833) matches `draft_v2.tex:622` and the referee's M3.

**B3 — competitive pricing fixed point. OK.** `draft_v2.tex:348` market maker competitive; `:354`
unique inner fixed point `P*(X,D)` assumed under (A5); `:492–501` the fixed point `eq:price-fp`
written out. The answer's A5 is the same assumption restated for the two-round history set.

**B4 — outer Brouwer existence. OK.** `draft_v2.tex:622` "Θ ... nonempty, compact and convex, and by
Lemma~\ref{lem:selfmap} `\Tmap`: Θ→Θ is continuous. Brouwer's fixed-point theorem yields
k* ∈ Θ"; restated `:2230`. The answer's A6 + P1 is the same architecture over a plan menu instead of
four named actions.

**B5 — no invented draft_v2 lemma numbers. OK.**
`grep -nE "\\\\ref|Lemma [0-9A-Za-z]|Proposition [0-9]|Theorem [0-9]|lem:|prop:|thm:|app:"` over the
answer returns **zero hits**. The answer cites no draft_v2 label at all, so failure mode (1) of the
handoff ("invents draft_v2 lemma numbers") did not fire. The flip side is that its reuse claim is
generic; the mapping above is the audit's own, and it holds.

**B6 — the chord is draft_v2's, unattributed. MISCITED (no citation to correct — a missing one).**
The answer's `C_h(π̄) = h(0) − 2h(π̄/2) + h(π̄)` (l.944, l.1237) is character-for-character
`draft_v2.tex:847–850`, where it is `\mathcal{C}(\bar\pi)` and the maintained primitive condition
**(C\*)**, `eq:d1-Cstar`, inside `lem:d1-jensen` (`:841`). draft_v2 also already has the *exact*
version of the answer's Taylor step, in mean-value form: `draft_v2.tex:2768` — "for `g ∈ C²[0,π̄]`
there is `ζ ∈ (0,π̄)` with `𝒞(π̄) = ¼π̄²g''(ζ)`". That is stronger than `¼h''(0)π̄² + o(π̄²)` and needs
no differentiability *at* zero, only on the interval. The claim stands — it is the same object
and the same chord identity — but it is presented as new notation under a new name with "NOTATION
DELTA — None beyond the card". Two consequences, both carried to msg 2: (i) `C_h` must be declared
as a rename of draft_v2's `𝒞`, not as a new object; (ii) draft_v2 maintains the **strict** `(C*) < 0`
while the answer maintains the **weak** `C_h ≤ 0` — the referee already flagged that `C = 0` is
unhandled (report l.139, "write 'if', not 'iff'"), so the weak version needs the `C_h = 0` case
handled or the strict version adopted.

---

## (c) Proof-by-assertion scan

**C1 — OK, no hits.** `grep -nE "clearly|it follows|standard|obviously"` returns exactly two lines,
both vocabulary, neither a proof step:
- l.985 "Mean and **standard** deviation of (v)" (symbol table);
- l.1562 "per one-**standard**-deviation increase in empirical liquidity" (reporting units).

Every PROOF block is literally "1. Deferred under the statement-only pacing instruction. 2. The
proof turn will …" — statements only, as instructed. Nothing to bounce this turn. The scan must be
re-run against the turn-2 proofs, where it is the live risk.

**C2 — one hedge word worth watching (not a hit, logged).** §2.6 l.334: "A shorter window
**generally** gives `B^F(s;τ,T') ≤ B^F(s;τ,T)`". At fixed policies this is not "generally" but
exactly true: `c_j(s;τ)` does not depend on `T`, `B_j(s,·)` is weakly increasing for Voice plans
(l.154), and `f = c + T`, so `T' < T ⟹ f' < f ⟹ B^F' ≤ B^F`. The word invites a hole in the L2/T1
proofs. Msg 2 asks for it as an equality-of-hypotheses statement, not a tendency.

### Arithmetic the audit executed on the statements themselves

- **L3's Taylor coefficient — correct.** With `h(0)=0`, `h(x) = h'(0)x + ½h''(0)x² + o(x²)`:
  `C_h = 0 − 2[h'(0)π̄/2 + ⅛h''(0)π̄²] + [h'(0)π̄ + ½h''(0)π̄²] = ¼h''(0)π̄² + o(π̄²)`. Matches the
  answer's `¼h''(0)π̄²` exactly.
- **T1's product rule — correct.** From L1 with `Ω` and `M_F` κ-free,
  `∂_κΔ^act = (1−Ω)∂_κM_P ⟹ 𝒮 = (1−Ω)𝒮_P`, hence
  `𝒮(τ',T)/𝒮(τ,T) = W_τ C_τ` with `W_τ, C_τ` as defined (l.1348–1358).
- **T1's local window condition — correct.**
  `∂_{r_T}𝒮 = −Ω_{r_T}𝒮_P + (1−Ω)∂_{r_T}𝒮_P ≤ 0 ⟺ ∂_{r_T}𝒮_P/𝒮_P ≤ Ω_{r_T}/(1−Ω)` given `𝒮_P > 0`.
- **§2.12's `Ω = Pr(a=1)·ω` — correct** given `D=1 ⟹ a=1` (which A4 imposes: "Only Voice plans cross
  the threshold in the core").
- **Monotonicity directions — consistent.** Lower `τ` ⟹ earlier `c` ⟹ larger flagged set (L4 h.1);
  lower `T` ⟹ `{c ≤ H−T}` larger ⟹ `Ω(τ,T') ≥ Ω(τ,T)` (T1 h.6). Both agree with the card's
  "lower = tighter" convention (l.59).

---

## (d) Notation delta / drift audit

Baselines: `CONTEXT.md`; `draft_v2.tex`; `numerical/takeover_game.py`;
`quality_reports/fixes/D8_GE_dominance_MCS.tex`.

| # | Symbol (answer) | Clash / status | Verdict |
|---|---|---|---|
| N1 | `κ` — "Noise-trading intensity; liquidity" (l.997, l.393) | `CONTEXT.md` **Liquidity**: "Noise-trading intensity, the model's κ". No drift to depth/volume/turnover anywhere in the answer. | **fine** — confirmed, no drift |
| N2 | `ψ` — "finite ordered coarsening map" from stake increment to order mark (l.368) | `draft_v2.tex:288–290`: `λ = 1 − q(1−γ)ψ`, **ψ is the bloc pivotality factor** of D7; the referee report M6 already had to repair ψ/φ/q labels once. Re-keying ψ is exactly failure mode (3). Replacement checked for freedom: `\Gamma` has 0 occurrences in draft_v2 (`\chi` has 19 — the cost parameter; `\zeta` is the mean-value point at `:2768`; `\varphi/\phi` is the normal density per referee M6). | **collision-must-rename → `Γ`** |
| N3 | `λ_s` — Gaussian projection coefficient (l.92–98) | Bare `λ` is D7's appropriability coefficient `1 − q(1−γ)ψ` (`draft_v2.tex:84, 288, 2500, 2606`; `numerical/takeover_game.py:8, 101`). Also, draft_v2 already names this exact projection **β** (`:215`, `:1839`). | **collision-tolerable-with-note** — subscript mandatory, never bare `λ`; map `λ_s → β` at .tex write-up |
| N4 | `k = (k_1,…,k_{J−1})` (l.816) | draft_v2's cutoff vector is `(k_1,k_0,k_D)` (`:392`, `:1029`). `k_1` means the lowest cutoff in both, so the roles agree, but `k_0` is a *named* cutoff there and would be index 0 here. | **collision-tolerable-with-note** — require an explicit map when the plan menu is instantiated as the four draft_v2 actions |
| N5 | `ω = Pr(D=1 | a=1)` (l.758–761) | draft_v2's `ω`-family is `ω_E, ω_H, ω_Q, ω_P` — action masses, all unconditional (`:422–424`); `ω_P` is the referee report's variable in the O-1 numbers. A bare `ω` in this literature reads as one of those. | **collision-must-rename** — subscript it (`ω_a`), and state `Ω ≡ ω_P` of draft_v2 |
| N6 | `Ω = Pr(D=1)` (l.741) | `\Omega` appears **0 times** in `draft_v2.tex`. Genuinely free. It equals draft_v2's `ω_P`. | **fine** — with the equality stated once |
| N7 | `T` — filing window in business days (l.1000) | `draft_v2.tex` uses `\Tmap` (12 occurrences) rendered as `T` for the outer best-response map, e.g. `:1963` "Assumption (A6) states that `T` is a contraction". The answer already scripts the map `𝒯(k;ϑ)`. | **collision-tolerable-with-note** — calligraphic `𝒯` for the map is now mandatory, upright `T` is the window |
| N8 | `a_κ` — derivative coefficient in A(τ) (l.930, declared as a delta) | `a` and `a_j` are the engagement indicator throughout (l.132, l.1011); `a_κ` reads as "engagement at κ". draft_v2's standardized cutoffs are `α_1, α_0, α_D` (`:422–435`), so `α_κ` is also taken. | **collision-must-rename** — write it `A'_κ` (it *is* the common derivative of the `A`-weights it is defined from) |
| N9 | `C_h(π̄)`, and the family `C_τ, C_T` (l.944, l.1058) | `C_h` is draft_v2's `𝒞(π̄)` (`:847–850`) — see B6. `C` is also the engagement cost `C_j(s)` (l.579) and `𝒞_F/𝒞_P/𝒞_j^trade` (l.260–270, l.570) in the answer itself. Four `C`s in one card. `C_τ/C_T` do match `CONTEXT.md`'s "composition effect" vocabulary, so renaming them would cost more than it buys. | **collision-tolerable-with-note** — keep both, declare `C_h` as draft_v2's `𝒞`, and never write a bare `C` |
| N10 | `W_τ, W_T` — weight-effect ratios (l.1057, declared as deltas) | No `\mathcal{W}` in draft_v2; `W` is otherwise unused there. Matches `CONTEXT.md` **Weight effect / Composition effect** vocabulary. | **fine** |
| N11 | `σ_κ` — "constant sign of the liquidity derivative" (l.1071) | Every other `σ` in both documents is a standard deviation (`σ_v, σ_ε, σ_ξ`; `draft_v2.tex:1838`). `σ_κ` reads as "s.d. of κ". | **collision-must-rename** — drop the symbol, write `sgn(dΔ^act/dκ)` inline |
| N12 | `𝓑_r^GE`, `L_𝓡`, `k̄_x` — C1's bound symbols (l.1482–1517) | D8's inversion-free bound is `B̄` (`quality_reports/fixes/D8_GE_dominance_MCS.tex:112, 186`, `eq:d8-Bbar`); D8's contraction modulus is `L` (`L ≤ 0.836 < 1`). Different symbols for the same-family objects, no clash. | **fine** — but state that `𝓑_r^GE` is the cross-derivative analogue of D8's `B̄`, so the two are not confused |
| N13 | `B_j(s,d)`, `B^F` — stake path / stake at filing (l.132, l.302) | `B(E), B(H), B(Q), B(P)` are draft_v2's payoff slopes (`:2230`, 5 occurrences); `B(κ)` at `:889` is another use. Arities differ (`B_j(s,d)` vs `B(action)`), so it is readable, but the proofs appendix will put them on the same page. | **collision-tolerable-with-note** |
| N14 | `Δ_V`, `Δ_m` (l.520, l.550) | draft_v2's baseline engagement value increase is plain `Δ = 0.25` (`:2860`); D7 has `Δ_eng`. Both new symbols are subscripted, `Δ_m = m_1 − m_0` matches `CONTEXT.md` **Premium wedge**. | **fine** |
| N15 | `A(τ)` as a hypothesis name, containing weights `A_0, A_{1/2}, A_1` (l.907–936) | Self-collision inside one hypothesis: the hypothesis and its weights share the letter. Cosmetic but it is the hypothesis the whole L3–L4–T1 chain hangs on. | **collision-tolerable-with-note** |
| N16 | `Θ` — compact ordered cutoff polytope (l.1065) | `draft_v2.tex:622` uses `Θ` for exactly that. Deliberate, correct reuse. | **fine** |
| N17 | `π(𝓘)`, `p(𝓘)`, `h = πp`, `Δ^act`, `D`, `q_{jd}` | All match draft_v2's `π(X,D)`, `p(X,D)`, `h`, `Δ^act`, `D`, `q ∈ {−1,0,+1}` (`:313`, `:344`, `:991`, `:152`). | **fine** |

Undeclared deltas found (the answer says "NOTATION DELTA — None beyond the model card" in D1, P1,
L1, L2): none of those four introduces a symbol, so the declarations are honest. The undeclared ones
are **N9/B6** (`C_h` is a rename) and the four-`C` overload. `a_κ` (N8) and `W/C_τ/C_T` (N10, N9)
*were* declared, as required.

---

## (e) Bundle-mandate coherence — the seven elements the answer says are fixed

1. **Partition-as-market-partition — respected.** §2.5 builds `𝒞_F/𝒞_P` as a partition of
   control-node histories generated by `D` itself, not an indicator bolted onto a static game.
   `docs/adr/0006`: the position is "the disclosure rule as the market's partition";
   `CONTEXT.md` **Partition**.
2. **τ and T separate primitives — respected.** `D = 1{a=1, c(τ) < ∞, c(τ)+T ≤ H}` (§2.5) uses both,
   and §2.4 makes `T ∈ {1,…,H}` a legal-time primitive. This is the direct repair of referee M1
   ("τ is not a primitive", report l.80) and of `docs/adr/0007` ("makes the window margin a genuine
   primitive instead of a reduced-form parameter").
3. **Run-up vs jump distinct — respected.** §2.11 defines `R` on the pooled path and `J = P^F −
   P_ND` at the *same realized order flow*, which is the referee's own definition (report l.127–128:
   "J(X) = P(X,1) − P_ND(X)"), and `CONTEXT.md` **Timing split**.
4. **Flagged-cell κ-invariance direct — respected, and now earned rather than assumed.** L2 derives
   it from A7 (filing sufficiency) instead of asserting it as draft_v2 does at
   `app:proof-disclosed-invariance` (report l.101–102 confirms `p̄₁` is genuinely κ-invariant there).
5. **Structural partition vs positive mass — respected.** §2.5 states both bullets explicitly and
   puts positive mass in a *separate* hypothesis A8, which is the handoff's named hazard
   ("Interior-crossing condition … belongs in the theorem's hypothesis").
6. **draft_v2 machinery reuse — respected and verified.** See B1–B4.
7. **No global window sign — respected.** T1 is stated as an if-and-only-if on `W_T Γ_T ≤ 1`, §8
   item 1 disclaims a global attenuation sign, and T1's WHERE-IT-FAILS item 5 names the old
   low-disclosed-mass calibration as the failure case. Matches `docs/adr/0007` and the O-1 finding.

---

## (f) UNCHECKED — listed, not triaged away

| U# | Claim | Why it could not be checked here |
|---|---|---|
| U1 | Every **NUMERICAL CHECK REQUEST** (D1, P1, L1, L2, L3, L4, T1, C1) | No two-round implementation exists. `numerical/` is the one-round repo model: `params.py`, `model.py`, `solver.py` have no calendar `d`, no `T`, no plan menu. Requests are logged in the card; none can move a label yet. |
| U2 | P1 existence — that adjacent-plan indifference over *complete contingent plans* yields a continuous self-map of an ordered polytope | draft_v2's Brouwer argument is over four named actions with a proved slope ordering `B(E)<B(H)=B(Q)<B(P)` (`draft_v2.tex:2230`). Whether an arbitrary finite plan menu inherits that ordering is exactly what A3 assumes. Proof turn must show it, not assume it. |
| U3 | A7 filing sufficiency / the injectivity strengthening | draft_v2's analogous injectivity claim was *itself* a referee finding (M2, report l.81: `lem:dropA7` asserts injectivity, contradicted by `app:proof-disclosed-invariance`, one price on all three disclosed cells). The two-round version may inherit the same defect. This is why msg 2 demands the conditional-independence step in full. |
| U4 | A(τ)'s symmetric ternary-kernel representation `A_0' = A_1' = a_κ`, `A_{1/2}' = −2a_κ` | draft_v2's `eq:d1-twopoint` law is stated for its own four-action `D=0` cell structure; whether the two-round pooled cell reduces to the same three-point symmetric law is unverified. If it does not, L3 and everything above it fall. |
| U5 | AGE / C1's `L_𝓡 < 1` on any region, and non-emptiness | D8 certified `L ≤ 0.836 < 1` for the *one-round* map on `κ∈[0.30,0.85]` (`D8_GE_dominance_MCS.tex:186`). Nothing transfers automatically to the two-round outer map. The answer correctly claims no nonempty region. |
| U6 | Design choices 1–4 (fixed horizon `H`, one strategic pooled round, complete contingent plans, filing sufficiency) | These are modelling stipulations, not claims about a source. Nothing in the repo contradicts them; nothing in the repo supports them either. They are the author's call. |

---

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| A1 ratios 1.06 / 1.19 / 1.14 | OK | referee report l.116–117 |
| A2 attenuation only at 0.50 | OK | referee report l.118 |
| A3 no attenuation below ~0.29 | OK | referee report l.116, l.118 |
| A4 the 0.38 figure | OK | referee report l.118 |
| A5 0.037 → "<1%", disclosed slightly more sensitive | OK | referee report l.120–123 (0.01107 vs 0.01117; 0.0251 vs 0.0236) |
| A6 those masses are Ω-type, not ω-type | OK (note mandatory) | draft_v2.tex:424 |
| B1 Gaussian signal reused | OK | draft_v2.tex:211, 215, 1837–1839 |
| B2 ordered cutoffs reused | OK | draft_v2.tex:392, 618, 1029 |
| B3 competitive pricing fixed point reused | OK | draft_v2.tex:348, 354, 492–501 |
| B4 outer Brouwer reused | OK | draft_v2.tex:622, 2230 |
| B5 no invented draft_v2 labels | OK | grep for `\ref`/`Lemma N`/`lem:`/`prop:`/`thm:`/`app:` → 0 hits |
| B6 chord `C_h` is draft_v2's `𝒞`, undeclared | MISCITED | draft_v2.tex:841–853 (`lem:d1-jensen`, `(C*)`); strict `<0` there vs weak `≤0` here |
| C1 proof-by-assertion scan | OK | only "standard deviation" at l.985, l.1562 |
| C2 "generally" in §2.6 monotonicity | OK (tighten in proof) | answer l.334 vs l.154 + `f = c+T` |
| N1 `κ` stays noise-trading intensity | fine | answer l.393, l.997 vs CONTEXT.md l.66–68 |
| N2 `ψ` → `Γ` | collision-must-rename | draft_v2.tex:288–290 (D7 pivotality); `\Gamma` free (0 hits) |
| N3 `λ_s` | collision-tolerable-with-note | draft_v2.tex:84, 288 (`λ` = appropriability); `β` at :215 |
| N4 `k` vector | collision-tolerable-with-note | draft_v2.tex:392 |
| N5 `ω` → `ω_a` | collision-must-rename | draft_v2.tex:422–424 (`ω_E, ω_H, ω_Q, ω_P`); `\omega_a` free (0 hits) |
| N6 `Ω` | fine | 0 occurrences in draft_v2.tex |
| N7 `T` vs `𝒯` | collision-tolerable-with-note | draft_v2.tex:1963, `\Tmap` ×12 |
| N8 `a_κ` → `A'_κ` | collision-must-rename | answer l.132 (`a_j` engagement); draft_v2.tex:422–435 (`α` taken) |
| N9 `C_h`, `C_τ`, `C_T` | collision-tolerable-with-note | draft_v2.tex:847; answer l.260, l.570, l.579 |
| N10 `W_τ, W_T` | fine | no `W` object in draft_v2; CONTEXT.md l.82–83 |
| N11 `σ_κ` → drop, write `sgn(·)` | collision-must-rename | draft_v2.tex:1838 (`σ` = s.d. throughout) |
| N12 `𝓑_r^GE`, `L_𝓡` | fine (note) | D8_GE_dominance_MCS.tex:112, 186 |
| N13 `B_j(s,d)`, `B^F` | collision-tolerable-with-note | draft_v2.tex:2230, 889 |
| N14 `Δ_V`, `Δ_m` | fine | draft_v2.tex:2860; CONTEXT.md l.73–74 |
| N15 `A(τ)` vs `A_0, A_{1/2}, A_1` | collision-tolerable-with-note | answer l.907–936 |
| N16 `Θ` | fine | draft_v2.tex:622 |
| N17 `π, p, h, Δ^act, D, q` | fine | draft_v2.tex:313, 344, 991, 152 |
| E1–E7 bundle mandate, seven elements | OK ×7 | §(e) above; ADR-0006, ADR-0007, CONTEXT.md |
| U1–U6 | UNCHECKED | §(f) above |

**Counts.** OK 20 · WRONG 0 · MISCITED 1 (B6) · UNCHECKED 6 (U1–U6) ·
notation: fine 7, collision-tolerable-with-note 6, **collision-must-rename 4** (ψ, ω, a_κ, σ_κ).

**Nothing blocks.** No WRONG item, so the one-retry rule does not fire. No result has any executed
check behind it, so all eight stay at **CONJECTURE**; no label may move until a committed check
script runs (or Thread 2 re-derives). The four must-rename items and the B6 attribution are instructions in
`thread1_msg2.md`.
