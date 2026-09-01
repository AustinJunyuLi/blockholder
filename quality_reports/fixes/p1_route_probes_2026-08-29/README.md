# P1 correspondence-route exploration — probes, 2026-08-29

**Analysis-grade, NOT curated t2 checks.** Same status as
`a6_panel_probes_2026-08-27/`: single-pass, written and run by one agent
(the route-exploration agent on `.scratch/p1-existence-route/issues/01-route-exploration.md`),
**not** independently reproduced and **not** gate-checked. They license no
label move and no card write. Everything they support is CONJECTURE-grade.

They are filed here rather than left in a session scratchpad because the
ticket's GO-WITH-CHANGES verdict cites their numbers.

Each script monkeypatches `numerical_v4.pooled._alive_weights` in memory and
restores it; nothing under `numerical_v4/` is modified on disk. Run with
`.venv/bin/python <script>` from the repo root.

## What they measure

The shipped off-path belief floor (`numerical_v4/pooled.py:225–235`) is

    if Wm[t] > 0.0: continue          # hard switch at exactly-zero mass
    Wm[t] = OFF_PATH_EPS              # same floor for every dead type

which differs from card Step 9(b)'s plan-uniform limit in two independent
ways — the switch is discontinuous where the limit's stage-`n` object is
continuous, and the floor is **uniform across types** where
`Λ_u(h) = Σ_{j'} ∫ L_{j'}(h|s')φ_s(s')ds'` is **mass-proportional**. The
probes vary those two axes separately.

| file | question | result |
|---|---|---|
| `t_blend_a3_probe.py` | does the A3 failure at `(κ=0.5, τ₅₀, T=5)` survive a continuous fixed-`t` blend? | pre-registered prediction **falsified**: 3 sign changes → 1. Diagnosed by the next script. |
| `t_blend_diagnose.py` | which axis moved it — continuity, or the floor's shape? | **the floor's shape.** `{switch, blend} × uniform` → 3 sign changes at every `ε`; `{switch, blend} × massprop` → 1. Continuity is irrelevant to the A3 pattern. |
| `t_blend_settle.py` | (A) does the blend restore `k`-continuity of `𝒯₂`? (B) does locus (ii)'s VOICE→HOLD argmax reversal survive every family? | (A) **yes** — local step at a fixed `1e−8` bracket across `edge(8)` falls `6.334e−3 → 6.8e−6`, the same total move spread monotonically over a `~1e−5` window. (B) **yes** — reversal holds in 8 of 8 variants at the node-15 pinned fixed point, with 5 sign changes throughout. |

## Independent verification, 2026-08-29 (`v_offpath_*`)

A **fresh verifier agent who did not write the exploration or the `t_blend_*`
probes above** rebuilt the two single-pass findings from scratch. Its report is
`offpath_verification_2026-08-29.md` in this directory; its four probes are
`v_offpath_family_facts`, `v_offpath_locus1_ladder`, `v_offpath_locus2_node15`
and `v_offpath_switch_vs_fixedt` (script + JSON each, 20 gates across three of
them, 0 failed). Those four are **pre-registered and gated**, run at the
committed `t2_a3_ordered_plans_check.py` protocol rather than at the
exploration's, and three carry a declared post-run-1 gate restructure with the
run-1 table preserved. They are still **single-verifier** and license no label
move and no card write.

Headline: the `OFF_PATH_EPS` finding is **confirmed** (with one narrowing on
"the `t = 0` construction"), and the locus-(i) finding is **narrowed** — the
Step-9(b) family gives 1 sign change over the offsets the card quotes but 3 at
offsets `4e-2 ... 1e-1`, where the shipped family gives 1, so it **relocates**
the A3 failure rather than removing it. Locus (ii) is confirmed and widened
(10/10 at the pinned point, both fixed points covered). The `t_blend_*` numbers
above all reproduce; the caveat below about `uniform_type_mass` being an
approximation is **resolved at locus (i)** — every floored type there is
`(D, f)`-constant with `D = 0`, so `Pr(n(s)=t)` is exactly Step 9(b)'s weight,
and the `m[0] = 0` error is inert because type 0 is alive at every ladder
point. **It is NOT resolved at locus (ii)**: type 11 is floored there and its
`n(s)` cell is not `(D, f)`-constant, while `menu.type_reference` reads one
midpoint clock for it — a third, independent implementation-vs-card gap,
common to every family tested and therefore orthogonal to the
uniform-vs-mass-proportional axis. See `v_offpath_locus2_node15.json`
(`exactness_caveat`) and the report's section 2(e).

## Caveats carried

- One node per claim except where stated; not swept over `(κ, τ, T)`.
- `uniform_type_mass` is `Pr(n(s) = t)` on the whole signal line — an
  **approximation** of `Λ_u`, omitting the Exit/Hold plans' contribution and
  the `1/J` factor. It is unambiguously closer to Step 9(b) than a
  `φ_s`-blind uniform floor, and it is not Step 9(b) exactly.
- The locus-(i) result is a proposition about a landed card evidence note and
  **must be independently verified before anything is done with it**. It is
  not a claim that the card is wrong.
- Nonexistence is neither claimed nor shown anywhere here.
