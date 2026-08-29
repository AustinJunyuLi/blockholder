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
