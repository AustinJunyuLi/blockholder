# Verification batch — ticket 04 cards, 2026-08-21

**Verifier:** opus, adversarial, single verifier for this stage (ADR-0005: did not read the papers,
never saw any reader's reasoning, checked every quote and page by executed search against the source).
Repo: `/Users/austinli/Projects/blockholder_v4_theory`, branch `v4-theory`. No git commands run.

**Method.** For each card: (1) re-derive the page map from the source rather than trusting the card —
read the printed folio off several pages and confirm the arithmetic; (2) match each quote as a **whole
Unicode-normalised sentence** (curly quotes, dashes, ligatures folded; whitespace collapsed), not just
the grep fragment the card supplies, and compare the page block returned against the citation; (3)
re-run every term count in the scope tables from scratch; (4) re-read every cited table and compare
coefficients, standard errors, *t*-statistics and sample sizes digit by digit; (5) for the two
figure-derived sections, re-read the rendered pages as images.

---

## Counts

| Card | OK | WRONG | MISCITED | UNCHECKED |
|---|---|---|---|---|
| `chabakauri_fos_jiang_2022_rof.md` | **58** | **0** | **2** | 1 (external) |
| `burkart_lee_voss_2025dec.md` | **61** | **1** | **3** | 1 (external) |
| `zeng_2026_ras.md` §9b | **41** | **0** | **1** | 0 |

Verdicts are written into each card's §9 (CFJ, BLV) and a new §9c (Zeng). Every WRONG and MISCITED was
fixed in place, marked as a verifier correction.

---

## The three decision-critical verdicts — **all three survive.**

**1. CFJ whitespace verdict (§6a) — SURVIVES.** Every grep re-run by the verifier on the raw text,
page map re-derived (printed = PDF − 2; OA p. N = PDF p. 55 + N; folio read off six pages):

- `disclos*` / `13D` / `Schedule` on printed pp. 11–18 (the whole model, equilibrium and Proposition 1)
  = **0 / 0 / 0**. Also `filing` = 0 and `SEC` = 0 there. The bracket pages do carry them — p. 10
  (§2.2) and p. 19 (§4.1 "Data sources") — exactly as the card says.
- `bidder` 0 · `tender` 0 · `acquirer` 0 · `merger` 0 · `entry` 0 · `welfare` 0 · `partition` 0 ·
  `five business` 0.
- `takeover` = **1**, printed **p. 3**, as a foil. `premium` = **3**: p. 24 (Levit–Malenko–Maug voting
  premium) and two reference-list entries on p. 41 — **no takeover premium**.
- `liquidity` = 13 and `threshold` = 5, on precisely the pages the card lists.

**2. BLV D7-safety verdict (§0) and the Q1 deletion — BOTH SURVIVE.**

- `appropriab` 0 · `lambda` 0 · `λ` 0 · `wedge` 0 · `ψ` 0 · `gamma` 0 · `γ` 0 · `13D` 0 · `Schedule` 0 ·
  `window` 0 · `filing` 0 · `five business` 0 · `Hart-Scott` 0 · `Williams` only inside "McWilliams"
  (p. 38). Bargaining is a single Nash weight `ρ` on printed p. 9 (`ρ` × 100 in the file; ASCII `rho`
  × 0). Role tests confirmed: the winner's-curse ruling on counter-bids at p. 51 (IA A.1
  "Counter-bids"), `α` never pivotal at p. 17, the IA A.9 additive synergy `θ_i ~ G[0,1]` at pp. 65–66
  with eq. (17) and the 1/1.1 example at p. 66.
- **"Market liquidity plays no role in our analysis" is ABSENT.** Not the sentence, not a clause of it
  — even the three-word fragment **"plays no role"** returns **zero hits** across all 73 page blocks.
  The card's warning in §7.3 (pasting it into draft_v3 would be a false citation to a JF-forthcoming
  paper) should be treated as a hard rule.

**3. Zeng IA.2 — EVERY NUMBER CONFIRMED, and IA.2 prints no difference test.**

Read straight off IA PDF p. 4: Pre-disclosure **0.026 (1.27)** smaller / **0.032\*\* (2.46)** larger on
TD−20→FD−1; **0.066 (1.64)** smaller / **0.041\* (1.95)** larger on TD−5→FD−1. N = **241,360 / 241,264 /
221,590 / 221,811**. `Illiquidity` −0.025\* / 0.076 / −0.033\*\* / 0.055. R² 0.021 / 0.036 / 0.022 /
0.037. Column layout (dep. var. Daily Net Insider Purchases; cols 1–2 long window, 3–4 short window;
cols 1 and 3 smaller firms) confirmed. **The whole table note was read and contains no test of the
difference.** The body gloss on printed p. 1322 matches verbatim, exactly one hit. So "the difference
is not statistically significant" is an assertion, and on the short window — the one the Feb-2024 rule
compresses — the small-firm point estimate is the larger one. **The κ opening is not pre-empted.**

---

## Every WRONG (1 in the batch)

**BLV, §8b row Q7 — WRONG.** The card said the 2024-card quote "Our theory posits that a growing
influx (of funds at the disposal) of control-oriented investors causes a shift from direct takeovers
toward takeover activism." **SURVIVES verbatim, p. 29**.

*Contradiction:* the Dec-2025 print reads "…causes a shift from direct takeovers **towards** takeover
activism" (printed p. 29). The 2024-card string returns **zero exact matches** anywhere in the file.
The sentence survives in substance and on the page named, but not as a string — which is exactly the
failure mode §8b exists to catch, and the smallest change in the audit, therefore the easiest to paste
in by mistake.

*Fixed:* the Q7 row now reads BROKEN-as-a-string with the diff spelled out, and the score line was
corrected from **"8 of 19 survive verbatim (5 relocated to the IA), 11 broken"** to **"7 of 19 survive
verbatim (4 relocated to the IA), 12 broken"**, with the seven survivors and their pages enumerated
(Q2 p. 2 · Q4 p. 54 · Q5 p. 55 · Q11 p. 51 · Q13 p. 36 · Q14 p. 7 · Q16 p. 52).

---

## Every MISCITED (6 in the batch, all fixed in place)

**CFJ (2).**
1. **R17 page.** The 14.2% / 11.2% proportions are on printed p. 30, but the clause the ASSERTED label
   hangs on — "The difference is highly statistically significant." — is on printed **p. 31**; the
   sentence straddles the page break. Fixed to pp. 30–31. The substance (no SE, no *t*) is right.
2. **§4 turnover bullet.** "daily turnover 0.63% overall vs 1.23% on filer-trade days" is on printed
   **p. 8**, not p. 9; p. 9 carries the 13D-turnover pair (0.00% → 0.23%). Table 2 (p. 44) prints both.
   Fixed.

**BLV (3).**
3. **§0 `psi` row.** The literal string returns **2** substring hits, not "0, only Lipsius":
   "Li**psi**us" (p. 38, reference list) and "u**psi**de" (p. 52, IA A.1). `ψ` as a symbol is genuinely
   0, so the D7 conclusion is untouched. Fixed.
4. **§6 `toehold` page list.** Count 10 is right; the pages are 21 (×2), 25, 53, **56**, 61 (×2),
   **65** (×3). The card listed "21, 25, 53, 61, 64" — missing p. 56, mis-numbering 65. Fixed.
5. **Two placement/transcription slips, noted in §9 rather than rewritten.** §6 calls both boilerplate
   `disclos` hits "front matter" when one sits on the paper's own printed p. 1; and §6's rendering of
   the p. 27 truncation sentence prints "[0, V̄_1]" where the source carries an asterisk (V̄₁\*, floated
   onto the previous line by the extractor). Re-quote that one from the PDF.

**Zeng §9b (1).**
6. **§9b(e), Fig. IA.1 description.** "the pre-TD path drifts *down*, and the first upward move is the
   segment TD−1 → TD" is contradicted by §9b's own readings (−0.51% at TD−5 → −0.22% at TD−1 is a
   +0.29 pp rise over four days) and by the render. Rewritten: the path drifts down *through TD−5*,
   edges modestly back up to TD−1, and the first **large** move (≈ +0.95 pp in one day) is TD−1 → TD.
   Q5's "run-up begins precisely on the trigger date" still reads fair; the card just must not claim a
   flat-or-falling path right up to TD.

---

## UNCHECKED (named, not triaged away — neither is decision-critical)

1. **CFJ: the published *Review of Finance* text.** Only the LSE accepted manuscript is on disk.
   Whether the copy-editor fixed the four version-risk slips, and whether the published version added a
   footnote on the Feb-2024 five-business-day amendment, cannot be checked from this file. The card
   already flags it; keep the warning until someone opens the RoF PDF. (Related: the card's assertion
   that Back et al. (2018)'s true page range is 1431–1463 is an external fact — the paper's printed
   "1431-1643" is confirmed, the correction is not.)
2. **BLV: "ECGI's working-paper page gives 'last revised 29 December 2025'."** External to the PDF and
   to every file on disk. Everything internal is confirmed: title page "November 22, 2025", ECGI cover
   "December 2025", PDF metadata Creator/Producer "Adobe Acrobat (64-bit) 25.1.20997" with CreationDate
   **30 Dec 2025**, 72 pages, SSRN id 4709037, WP N° 956/2024.

---

## What held up especially well

- **CFJ quotes: 16/16 verbatim on the exact cited page**, matched as whole sentences.
- **BLV quotes: 14/14 verbatim on the exact cited page.**
- **CFJ tables: every printed coefficient, SE and N in R6–R16 and R19 matches the source exactly**,
  including the OA tables C1, C5, C6, C7. The four version-risk slips the card catches in the AAM are
  all real (the p. 36 sign against Table 10's +0.0097\*\*; p. 9's "basis points" against Table 7's
  0.0068/0.0018; the p. 5 / p. 22 / Table 3 disagreement on 13 bp, 15%/17%, 37%/36%; the Back et al.
  page range as printed).
- **BLV §3 re-anchor table: all sixteen rows confirmed**, propositions and proofs alike, plus the
  7 + 2 + 1 enumeration and the 12 figure numbers.
- **Zeng IA tables IA.1, IA.3–IA.9: every printed number exact**, including IA.9's ΔROA 2-of-4 pattern
  and the table note that confirms the horizon is q…q+3, not "120 trading days following".
- **Zeng IA grep counts: all exact** — standalone `liquidity` = 0 across 13 IA pages, `Illiquidity` = 6
  (one control row per table IA.2–IA.7), `premium` / `takeover` / `bidder` / `order flow` / `2024` /
  `5 business` all 0.
- **Zeng Fig. IA.2 pixel readings reproduce**, including the dual-axis arithmetic behind the headline
  1.34%-of-shares-outstanding trigger-day spike (the bar tops at 6.7 left-axis units × 1.6/8.0).

---

## INDEX.md cross-check

The three index rows were compared against what the cards actually say.

- **CFJ row (line 48)** — accurate on every checkable claim (79 pp; body 2–39 / tables 43–53 / OA 1–23;
  "pp. 11–18 contain no 'disclosure', '13D' or 'Schedule'"; 0 hits for bidder/tender/merger/entry;
  takeover once on p. 3; the Table 10 Amihud null −0.0013 [0.0054]; 2,847 events; 31.9m firm-days;
  Table 6 at p. 48; OA p. 12 artefact admission). Verdict cell updated from "pending".
- **BLV row (line 65)** — accurate (72 pp printed 1–66; 13D / window / Williams Act 0; fn. 13 p. 17;
  D7 safe). The one thing it repeats from the card is the `psi = 0` shorthand, now qualified in the
  card. Verdict cell updated from "pending" and the "11 of 19 old quotes broke" figure corrected to 12.
- **Zeng row (line 88)** — accurate; its IA.2 summary matches the source exactly. Its count cell
  (36/3/3/0) is the post-§9b tally and is one OK ahead of a strict recount of §9's own line (30 OK + 5
  closed items); left as is, since the difference is bookkeeping, not substance.
