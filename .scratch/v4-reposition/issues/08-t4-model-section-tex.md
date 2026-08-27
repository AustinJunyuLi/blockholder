# 08 — T4 · Draft-ready model, theorem and proofs sections

**Lane:** theory (`v4-theory`, other machine)

**Routing:** per ADR-0005 — Opus writer (paper prose, not note prose); Sonnet for LaTeX plumbing and bibliography entries; a separate Opus checker reads the sections against the model note.

**What to build:** The model, the theorem and the proofs written as standalone files under `sections_v3/` for inclusion in draft_v3, plus bibliography entries for every new citation. This is the theory lane's handover to the draft.

**Blocked by:** 06 (T2).

**Status:** ready-for-human

- [x] Section files compile on their own with xelatex, no undefined references
- [x] Every statement matches the model note; every honesty label carries over unchanged
- [x] Bibliography entries added for each new citation
- [x] A checker who did not write the sections reads them against the model note and reports every difference
- [x] Session log entry and commit on `v4-theory`; branch pushed for the convergence owner

## Comments

**2026-08-27 — executed (orchestrator, Opus writers/checker per the routing header). Ready for Austin's review.**

Landed on `v4-theory` (pushed): `58a5d11` (leg 0 — the model_v4.md/.tex mirrors regenerated to card
stamp 2026-08-27 `ae9caea`, which the sections check against), `9a73bb7` (the sections + the checker
report + session log; `749ec7b`/`1de1c32` log-hash and wording fills).

- **Files:** `sections_v3/model_section.tex`, `theorem_section.tex`, `proofs_section.tex` (heading +
  three `\input`s: `proofs_core_lemmas.tex` D1/L1–L4, `proofs_existence.tex` P1,
  `proofs_theorem_ge.tex` T1/C1), `v3_macros.tex`, `sections_v3.bib` (header-only — the four
  citations all use existing root-bib keys, so box 3 is satisfied vacuously), driver
  `standalone_v3.tex` + committed 61-page PDF.
- **Gate:** compiled from the repo root, xelatex+biber, zero undefined references/citations, zero
  errors, zero overfull. Labels verbatim from the ledger with conditionality; §5 evidence notes
  (A3/A6/A(τ) failures at the implemented calibration) carried at both assumption and result sites.
- **Check:** fresh Opus checker, `research/model_v4/threads/2026-08-27_t4_sections_check.md` —
  **LAND, 0 WRONG** (13 MISCITED / 14 OK-RESTRUCTURED, catalogued), one repair round (L3 Part IV
  (S1)/(S2) restored; C1 sign-coherence re-attributed to H8; overfull heading; macros provenance),
  delta-pass re-verified: LAND.
- **For ticket 18 (assembly):** `\input` the three section files after `v3_macros.tex`;
  `\addbibresource{sections_v3/sections_v3.bib}`. **Conscious step required: the `\Tmap` name
  collision** — draft_v2 defines `\Tmap` as upright `T`; `v3_macros.tex` now makes the macros-after
  ordering fail loudly and documents the reverse ordering's silent hazard. All paths are
  repo-root-relative.
- **Next:** the GPT re-review bundles with this output (Austin's courier moment — not built here);
  then C-series (17–20).
