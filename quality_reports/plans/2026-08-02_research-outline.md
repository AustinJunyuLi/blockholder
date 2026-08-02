---
date: 2026-08-02
type: deliverable-build
status: APPROVED-BY-DIRECTIVE (user 2026-08-02: "Transform your verdict to a concrete research outline… deliverable is a latex doc and the rendered pdf")
branch: jmp-upgrade-2026-05
run_name: pivot-deep-research (same job family; outline rounds)
---

# Research outline build — "the reform is the paper; the window is the model"

## Deliverable
`proposal/outline.tex` + `proposal/outline.pdf` (XeLaTeX; own bib `proposal/outline.bib`),
sections: (1) research question; (2) the myth/common sense challenged; (3) literature review &
position (grounded in FULL texts — lit/txt corpus + three new fetches); (4) model setup & main
results (T2's neutralized deadline-accumulation spec); (5) empirical setup & data-acquisition
map (E1/E2-corrected designs, MDEs, gates, cut order); (6) main conclusion + 8-week workplan.

## Content authority
quality_reports/research/2026-08-02_pivot-deep-research-report.md (final verdict, Fable-corrected:
reform-first headline = chilling/substitution dose-response + Item 6 swap substitution;
anatomy second act; capitalization as measurement lemma; model = dealer/deadline microfoundation
with corner-solution window; target-level required-trading-days exposure).

## New full-text reads required (user: "Read the actual papers")
- Betton–Eckbo–Thompson–Thorburn 2014 JF (substitution mechanism — now load-bearing) [fetch]
- Boyson–Gantchev–Shivdasani 2017 JFE "Activism mergers" [fetch]
- Collin-Dufresne & Fos 2016 ECMA (deadline-Kyle anchor for the accumulation cost) [fetch]
- (opportunistic) Cetemen et al. NY Fed sr1030 PDF
- Harvest L4's already-fetched full texts into lit/txt (schwert1996, greenwood_schor2009,
  brav_jiang_partnoy_thomas2008, collin_dufresne_fos2015, gantchev2013, eckbo_malenko_thorburn2025).

## Lanes (user directive: qwen + gpt contribute; swap if unreliable)
Round A (parallel): W1a sonnet-high = fetch+quote-verify the 3 new papers; W2 opus-high = model
section LaTeX + executable sanity script (dealer-cost derivatives, horizon scaling); W3
sonnet-high = empirics + data-map section with numbers.json source-grounded; W4 kimi-k3-high =
framing sections (RQ, myth, contribution, conclusion, titles); W6 codex-LUNA-low = outline.bib
(mechanical, biber-checked).
Round B: W1b qwen3.8-max-preview-high = lit-review & position section from verified artifacts +
full texts (quote-grep check).
Round C: W5 codex-SOL-high = adversarial consistency review of assembled doc (thesis
consistency, numbers vs artifacts, citation integrity, compile) — also the decorrelated
GPT read Fable recommended.
Gate: ONE Fable-max read of the finished PDF draft (judicious budget, same as last round).
Boss: assembly, XeLaTeX compile, fixes, final delivery. Unreliable lane → swap per routing
table (qwen→deepseek; luna→deepseek; sol→opus review) and note in MODEL-NOTES.

## Checks
Per-section: tex-sanity + schema validators; W1a/W1b quote-grep against source txt; W2 sanity
script executed; W3 numbers spot-grepped in SEC txt/fact1 csv; W6 biber/parser run; W5 findings
schema. Boss compiles after every integration; final gate = clean xelatex+biber run, 0 errors,
0 undefined citations.
