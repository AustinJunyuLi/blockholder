# CLAUDE.md

## Project

One paper on how a blockholder disclosure threshold and filing clock shape public-market
inference and corporate control. The live manuscript is `draft_v3`; `draft_v2` and its figure
pipeline are a frozen reference.

One branch, `v4`, one worktree, at `/Users/austinli/Projects/blockholder_v4`.

Read `CONTEXT.md` before naming any paper or model object. Its honesty labels are exact:
PROVED, NUMERICAL, ESTIMATED, CONJECTURE. A review may demote a claim. Prose never promotes one.

## Authority by area

| Area | Authority | Rule |
|---|---|---|
| Frozen theory | `research/model_v4/MODEL_CARD.md`, `research/model_v4/`, `sections_v3/` | Preserve both trees byte-for-byte. The R-number sequence and the label gate are closed. Reopen only when Austin authorises correcting a genuine logical error. |
| Theory implementation | `numerical_v4/`, `quality_reports/fixes/t2_*` | Keep the code consistent with the frozen card. The smoke run is the minimum gate. |
| Empirics | `research/empirics_v4/e1_spec.md`, `empirics/e1.py`, `empirics/output/e1_*` | E1 is the only empirical exercise. The spec is registered; correct it with a dated amendment inside the file, never a silent edit. |
| Paper position | `research/empirics_v4/2026-08-31_gpt_pro_integration_angle_review.md` | The surviving statement of what the paper argues. |
| Live paper | `draft_v3.tex`, `draft_v3.bib`, `draft_v3_onlineappendix.tex`, `draft_v3_trace.md`, `deliverable/` | Edit presentation without touching the frozen theory record. Trace theory claims to the card and empirical numbers to `e1_estimate.json`. |
| Frozen v2 reference | `draft_v2.tex`, `numerical/`, `pyfig/`, `pres/`, D-series records | Historical reference. Regenerate only to verify or to make an authorised repair. |
| Teaching and provenance | `teach/`, `quality_reports/`, `.scratch/`, `docs/adr/` | Preserve learning state, checks, audits, and session records unless the active ticket names the exact file. |

## The empirical record was cleared on 2026-09-01

Every estimator, committed output, registered specification, and audit from the August
empirical lane was deleted, along with the Codex E1 protocol and evidence manifest. All of it
remains reachable in history at `9b98089`. `draft_v3` still cites some of those artifacts; strip
those references when the manuscript is next revised.

What survived: `parse_13d.py` and its tests, `edgar_fetch.py`, and `facts.py`, which seed the
rebuild, plus the GPT Pro review.

## E1

E1 asks whether the realised 13D filing delay fell after the Feb-2024 acceleration moved the
window margin from 10 calendar days to 5 business days. It is descriptive. It identifies no
effect on liquidity, returns, activism, bidder entry, takeover premia, or control outcomes, and
it tests neither L2 nor T1. Say so wherever it appears.

`research/empirics_v4/e1_spec.md` is the registered specification. Committing it before the run
is the registration; git commit order is the evidence. Three binding gates: G1 the worst-case
bound on the difference, G2 differential coverage, G3 parser validation. A failed gate writes a
`NO-GO` and suppresses the headline. It never licenses editing the spec.

`empirics/output/e1_estimate.json` is the single result authority. Every manuscript number comes
from it.

## Operational invariants

- T1 signs threshold tightening only under its stated fixed-policy conditions. Window tightening
  carries an if-and-only-if condition, because composition is unsigned.
- L2 concerns a flagged endpoint, not a filing return.
- A before-after filing-delay comparison is descriptive. It identifies no effect and no mechanism.
- The orchestrator owns git. Workers edit assigned paths, preserve concurrent work, run no git,
  and report every file changed. Land one concern per commit.
- One independent review and one author fix pass per artifact. A theorem-level defect stops the
  affected draft section and goes to Austin.
- Add a ticket, ADR, protocol layer, manifest, or abstraction only when a registered requirement
  cannot be met without it.

## Verification

Run the gates that match the changed files.

```bash
# theory implementation
.venv/bin/python -m numerical_v4.smoke

# empirics
PYTHONPATH=. .venv/bin/python empirics/test_e1.py
PYTHONPATH=. .venv/bin/python empirics/test_parse_13d.py
PYTHONPATH=. .venv/bin/python -m empirics.e1 run

# frozen v2 numerical and figure pipeline
make venv                 # once per environment
make clean && make all

# live paper and online appendix
xelatex -interaction=nonstopmode draft_v3.tex
biber draft_v3
xelatex -interaction=nonstopmode draft_v3.tex
xelatex -interaction=nonstopmode draft_v3.tex
xelatex -interaction=nonstopmode draft_v3_onlineappendix.tex
xelatex -interaction=nonstopmode draft_v3_onlineappendix.tex
```

TeX delivery requires zero errors, zero undefined references, zero undefined citations, and
visual inspection of both PDFs.
