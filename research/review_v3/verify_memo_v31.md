# Consistency verification — framework_v3.qmd v3.1 (post-referee revision)

Checked the revision's inserted numbers/claims against the named verification records and
primary files. Not a re-review of the paper; only checking that the revision matches what
was already verified, plus scanning for new internal inconsistencies. Budget used: ~17/35
tool calls.

## Tally

- Sub-facts checked: 55
- MATCH: 49
- MISMATCH: 4 (3 substantive citation/label errors, 1 minor misquote)
- CANNOT FULLY VERIFY: 1 (not located in the named sources)
- Minor caveats (not hard mismatches, worth a look): 2

No claim was found to be substantively wrong on the economics; all four MISMATCHes are
citation/label precision issues (a page number, a LaTeX symbol, a line number, and one
quotation-mark misquote). The revision correctly fixed every MISCITED/WRONG item flagged in
`verify_theory.md`, `verify_facts.md`, and `facts_verification.md` that I checked (C-T10,
C-T12 δ, D-2c "1,381"→"1,226", D-2d "448 rows/2.6%"→"438 rows/2.59%", F-1 "+7.7pp"→"+7.7%
relative", F-2 "70%"→"over one-third/22%", F-4 CDF-2015-vs-NBER-WP conflation, item 3b
Norli "(IV)" mislabel, item 8 Gantchev stage-label order).

## Table

| item | memo text (line) | verdict | correct value + source |
|---|---|---|---|
| 1a | Back et al. "fixed and common knowledge … endogenize the horizon" (p. 1454), l.60-62 | MATCH | `tmp_extract/Back-ACTIVISMSTRATEGICTRADING-2018.txt` — page header "1454 BACKETAL." immediately precedes this exact sentence |
| 1b | Burkart–Lee "do not endogenize the acquisition of the toehold…" (p. 1891) + "comprehensively studied by Back et al. (2018)", l.62-67 | MATCH | `research/txt/burkart_lee_rfs2022.txt` — explicit typesetting marker "Page: 1891" immediately precedes this exact text |
| 1c | Back et al. (2018, **p. 1436**): "what matters is σ²T … isomorphic to reducing noise trading volatility", l.206-208 | **MISMATCH** | Page is **1453**, not 1436. `tmp_extract/Back-ACTIVISMSTRATEGICTRADING-2018.txt` shows the running header "ACTIVISM, STRATEGIC TRADING, AND LIQUIDITY 1453" immediately before this exact sentence; the correctly-cited p.1454 quote (1a) begins on the very next page in the same file. No "1436" marker appears anywhere near the quote. |
| 2a | Trivedi SSRN 6866499, June 2026, +0.35 w/i 5bd, nulls on lag/spread/illiquidity, l.80-82 | MATCH | `verify_facts.md` N-1: CONFIRMED verbatim |
| 2b | Polk/Buchheit/Riley/Stone, JFRC 32(4):516–538, 2024, title "…will benefit non-activist investors", l.83-85 | MATCH | `verify_facts.md` N-2: CONFIRMED (published title, not SSRN's working title) |
| 2c | Corum 2025, SSRN 4319599, "The Stick or the Carrot?", no premium, l.86 | MATCH | `verify_facts.md` N-3: CONFIRMED |
| 2d | Bishop, Fos, Jiang, Partnoy 2026, SSRN 6061814, HSR-toehold avoidance, l.87-88 | MATCH | `verify_facts.md` N-4: CONFIRMED |
| 3a | D7: $r$=fringe-raid (renamed from D7's $q$), $\gamma$=portability, $\psi$=pivotality, l.124-125, 181 | MATCH | `D7_takeover_game_microfound.tex:68-73`: matches; memo's "(v3 … overloaded q; fixed)" is adequate acknowledgment that D7's $q$ clashes with the model's own order variable $q$ (defined `framework_v3.qmd:114`) |
| 3b | D7: $\varphi$=dilution, l.124-125, 181 | **MISMATCH** | D7 (`D7_takeover_game_microfound.tex:73`, footnote) reserves **$\phi$** (not $\varphi$) for dilution, and uses $\varphi$ for the standard normal density instead: "We write $\varphi$ for the standard normal density … and reserve $\phi$ for the dilution parameter below." The memo's symbol for dilution is swapped with D7's density symbol. |
| 4a | $\delta=0.95$ in `numerical/params.py`, $\delta=1$ only in the transfer-netting lemma, l.158-160 | MATCH | `numerical/params.py:130` `delta: float = 0.95` (grepped directly); resolves the old C-T12 finding correctly |
| 4b | draft_v2.tex Remark A5margins "l. 696": "$0.805+0.947>1$", l.226-227 | MATCH | `draft_v2.tex:696` is exactly `\label{rem:A5margins}` (grepped `-n` directly); quoted numbers exact |
| 4c | draft_v2.tex "§5 (l. 1009)": "$\delta/\sigma_\xi=2.375<2.507$", l.227-228 (also edit map l.582) | **MISMATCH** | The sentence "The baseline parameters satisfy the sufficient condition for Assumption (A5): δ/σ_ξ = 0.95/0.40 = 2.375…" is at **`draft_v2.tex:1010`**, not 1009 (grepped `-n` directly). Off-by-one; repeated in the edit-map table. |
| 5a | $\lvert\partial_\kappa E_{D=0}h\rvert$ 0.0153→0.00014 at $\tau_\theta$ 0→0.95, l.279-281 | MATCH | `theory_referee.md` Q2 table: τ=0.00 row = 0.015290, τ=0.95 row = 0.000143. Caveat: that table's "baseline masses" $(\omega_E,\omega_H,\omega_Q,\omega_P)=(0.35,0.05,0.40,0.20)$ are the referee's illustrative round numbers, not the paper's actual calibrated baseline $(0.400,0,0.562,0.037)$ from `verify_theory.md` O-1 — worth a qualifier ("illustrative masses") rather than "baseline masses" if precision matters. |
| 5b | TV of $\Delta^{\mathrm{act}}$ over $\kappa\in[0.15,0.85]$: $0.0180\to0.0040$ (disc, $\omega_P$ 0.012→0.50) and $0.0165\to0.0106$ (no-disc), l.283-286 | **CANNOT FULLY VERIFY** | Not present in `theory_referee.md` (grepped, 0 hits) or in `verify_theory.md`'s O-1 4-point table. The no-disc endpoints are close to O-1's independently-computed values at the true baseline and at $\omega_P\approx0.29$–$0.50$ (0.016537 and 0.010550–0.010658), and the direction/pattern matches O-1's confirmed monotonic trend, but O-1's grid never reaches $\omega_P=0.012$, so the two endpoint numbers (0.0180, 0.0040) are not independently confirmed by any file I was pointed to. |
| 5c | ratios 1.06/1.19/1.14/0.38 at $\omega_P$ 0.037/0.129/0.286/0.50, l.292-295 | MATCH | `verify_theory.md` O-1 (executed): 1.0640/1.1837/1.1363/0.3780 at $\omega_P$=0.0373/0.1289/0.2858/0.5000 |
| 5d | ranges 0.01107 vs 0.01117; mean $\lvert$slope$\rvert$ 0.0251 vs 0.0236, l.300-302 | MATCH | Independently recomputed from `numerical_output/data/disclosure_attenuation.csv` (35 rows, κ∈[0.15,0.85]): range = 0.011070 / 0.011170; mean $\lvert\Delta y/\Delta\kappa\rvert$ = 0.025124 / 0.023625 — all four match to the quoted precision |
| 5e | disclosure jump $E[J\mid D=1]$: 0.33/0.39/0.42 at $\kappa$=0.2/0.5/0.8, l.309-310 | MATCH | `verify_theory.md` O-2 (executed): 0.33130/0.39132/0.42070 |
| 5f | $\kappa^\dagger\approx0.58$ (CSV argmax), 0.60 (D8's coarser grid, "grid-resolution spread," not called a channel-(A) peak), l.346-348 | MATCH | `verify_theory.md` C-T10: this is precisely the corrected framing the verifier's MISCITED note prescribed (0.5824 CSV argmax; 0.60 is D8's `Dmin` peak on a 0.025 grid, not the `chanA` peak, which is actually at the grid edge 0.30) |
| 5g | $\lambda_{\mathrm{crit}}\approx0.07$, baseline $\lambda\approx0.86$, l.360-362 | MATCH | `d7_takeover_game_check.json`: `lambda_crit_numeric: 0.07`, `lambda: 0.8614452513529636` |
| 6 | certified $[0.35,0.825]$ (inversion-free), $[0.30,0.85]$ (exact IFT), $L\le0.836$; trough at $\sigma_\xi=0.60$, l.331-334, 349-350 | MATCH | Grepped `quality_reports/fixes/D8_GE_dominance_MCS.tex:186,194` directly: "$L\le0.836<1$…certifying $[0.30,0.85]$…certifying $[0.35,0.825]$" and "$\sigma_\xi=0.60$…exhibits an interior trough" — memo correctly pairs which bound goes with which interval |
| 7a | half-year CAR medians 4.4/3.0/1.7/0.4/1.0/6.0/2.8/0.8, l.391 | MATCH | `verify_facts.md` D-1: 4.38/2.96/1.69/0.36/1.01/5.95/2.80/0.82 — all round correctly (incl. 5.95→6.0) |
| 7b | parse rates 0.68/0.66/0.64/0.00, l.396-397 | MATCH | `verify_facts.md` D-2a: 0.6813/0.6637/0.6401/0.0000 |
| 7c | ≈990 matched events, 301 post in 7 clusters, 1,226 post-window filings, l.397-399 | MATCH | `verify_facts.md` D-4 (n=992, 301 post/7 months — "≈990" properly hedges vs. the old exact-but-wrong "989") and D-2c (Feb5–Aug31 = 1,226 exactly — correctly fixes the old MISCITED "1,381", which was the Feb5–Sep29 number) |
| 7d | F1: 188 filings (98 pre/90 post), parse rates 0.68/0.64, l.400 | MATCH | `verify_facts.md` D-3 and `empirics/output/fact1_summary.csv` (grepped directly): pre n=98 rate 0.68, post n=90 rate 0.64 |
| 7e | Manski bounds $[-7.9,+60.1]$pp, l.400-402 | MATCH | Independently recomputed per the specified formula using `fact1_summary.csv`'s own shares (pre 0.3571, post 0.7556) and rates (0.68/0.64): pre bounds [0.2428,0.5628], post bounds [0.4838,0.8438], Δ bounds = [0.4838−0.5628, 0.8438−0.2428] = [−0.0789,+0.6011] → **[−7.9,+60.1]pp**, exact |
| 7f | full-universe delay 7.0/7.0/5.0 bd; share≤5bd 31.9%/35.7%/70.6%, l.402-403 | MATCH | `verify_facts.md` D-2b |
| 7g | 438 rows exactly 2.59% (7.1% of 6,189), 307 at 0.0, 22.9% below 5%, l.404-406 | MATCH | `verify_facts.md` D-2d — correctly fixes the old MISCITED "448 rows … exactly 2.6%" (actual spike is 438 rows at 2.59); 438/6189=7.08%≈7.1% checks out |
| 7h | p90 23→11.1, l.416-417 | MATCH | `empirics/output/fact1_summary.csv` (grepped directly): p90 pre=23.0, post=11.100000000000009 |
| 8a | CDF stake at first 13D: median 6.2%, mean 7.68%; raw 2022-25 median 9.55%, l.421-423 | MATCH | `facts_verification.md` #2b (SUPPORTED) and D-2d (median=9.55) |
| 8b | "~23% of final stake" accumulated trigger→filing, l.424-425 | MATCH (secondary) | Not a clean standalone quote in `tmp_read/cdf_fos_jf2015.txt` (only a bare "1.8%" in a table row, l.1071); confirmed in `research/lit_liquidity-premia-empirics.md:53`: "Post-trigger…: **1.8% of outstanding ≈ 23% of the final stake**" — exactly the fallback the task anticipated |
| 8c | Greenwood–Schor 18.1%/7.2%/12.6% (≈+11pp), l.434-435 | MATCH | `verify_facts.md` item 6 (18.1%, 7.2%) + independently grepped `tmp_lit/greenwood_schor_2009.txt:1942`: "12.6% are subsequently acquired within a year" for the matched no-activism-stated sample |
| 8d | Boyson >1/3, 22% risk-arb-excluded; "v3's 70% was wrong", l.436-437 | MATCH | `verify_facts.md` F-2: correctly replaces the old wrong "70%" |
| 8e | C&L 36.6%, −13.7% (−5.2pp), "+7.7% relative" (not pp), l.556-558 | MATCH | `facts_verification.md` #5a/5b/5c — memo now correctly says "relative" instead of the old wrong "+7.7pp" |
| 8f | Norli 0.33%→0.73% labeled "baseline probit" (IV "somewhat larger," unquantified); 54%/8.5%, l.564, 573 | MATCH | `facts_verification.md` #3a/3b — correctly drops the old wrong "(IV)" label |
| 8g | EFZ −6.9pp, l.565 | MATCH | `facts_verification.md` #4 (6.88pp) |
| 8h | AFS 6.34%/75.2%; "+0.9pp/SD loading on both filing types", l.555, 542 | MATCH, minor caveat | `facts_verification.md` #1, #16n — AFS's derived coefficients are 0.90pp (13D) vs 0.81pp (13G), not identical; "both filing types" could read as implying one shared number |
| 8i | Gantchev negotiations \$2.9M / board \$1.8M / proxy \$5.9M, l.574 | MATCH | `facts_verification.md` #8 — this is exactly the label order the verifier's note required if labels were ever added (negotiations/board/proxy = 2.9/1.8/5.9), correctly applied |
| 8j | CDF JF2015 (1994-2010): ~3%/~2.5%; NBER WP 18452 (2001-2010): ~7%/~3%, l.516-518, 571 | MATCH | `verify_facts.md` F-4 — correctly separates the two versions instead of the old conflation ("7%/3%" mislabeled as JF 2015) |
| 8k | MDE: SE(β₂)≈1.0pp, t=2 needs ≈2.1pp/SD, l.464-466 | MATCH | Recomputed: $0.15/\sqrt{990\times0.3\times0.7}=0.0104\approx1.0$pp; $\times2=2.08\approx2.1$pp/SD |
| 9a | "three-branch menu" (l.136) vs. equilibrium's "$k_0=k_1$" (l.221) | CONSISTENT | Both are stated as consequences of the same (A2′) pruning assumption (l.142-148); $k_0=k_1$ is exactly the cutoff-space statement of "Hold has zero width," i.e., no Hold branch — not a contradiction |
| 9b | leftover "T3"/"one line" contradicting new T2 | NONE FOUND | "T3" appears once (l.313), explicitly labeled "a to-do, not a result," consistent with the edit map (l.583); "one line" appears once (l.269), self-critically describing what v3 called it |
| 9c | H1 called "flagship test of T2" unqualified | NONE FOUND | Only occurrence (l.296-297) is explicitly negated: "cannot be called … until …" |
| 9d-1 | "v3 said … 'the first formalization of how the market learns about activism-driven control events'", l.54-56 | MATCH | `framework_v3_pre-review_2026-08-19.qmd:32-33` (phrase wraps a line break): verbatim |
| 9d-2 | "v3 … 'Nobody … links market liquidity or the disclosure rule to takeover premia'", l.54-56 | MATCH | pre-review l.35-37: verbatim, ellipsis correctly elides the author list |
| 9d-3 | "v3 said 'Hold collapses at baseline anyway'", l.144-145 | **MISMATCH (minor)** | Pre-review l.88 actually reads "Hold folds into the trading decision; it collapses at baseline anyway" — the quoted string is a reconstruction (subject "Hold" + predicate from a different clause), not a verbatim quote, though meaning is preserved |
| 9d-4 (bonus) | "v3's '70% within 2 years' was wrong", l.436-437 | MATCH | pre-review l.239: `Boyson et al.'s $70\%$ within 2 years.` — verbatim, and independently confirmed wrong per 8d |
| 9e | section refs §2.3, §3.2 (+items 2/4), §4, Section 3, Section 4, Section 7 | MATCH | `grep -n "^# \|^## "` confirms: §2.3 = "Disclosure strictness…" (where $D$ is defined, l.196); §3.2 = T2 (whose numbered items 2 and 4 are exactly the window-margin and disclosure-jump items referenced); Section 7 = "Change log" (7th top-level heading); Section 3 = "Main Results and Proof Plan"; Section 4 = "Empirical Design". "H1 (§4)" is loose (H1 is technically §4.3) but not misleading. |
| 10 | LaTeX/markdown breakage (unbalanced \$, broken tables) | NONE FOUND | Full read-through of all 640 lines; all `$$...$$` blocks and `\|...\|` table rows are well-formed |

## Suggested one-line fixes

1. L207: change "Back et al. (2018, p. 1436)" → "Back et al. (2018, p. 1453)".
2. L124-125 and L181: change "$\varphi$ dilution" → "$\phi$ dilution" (D7 reserves $\varphi$ for the normal density, per its own footnote at `D7_takeover_game_microfound.tex:73`).
3. L227-228 and L582 (edit map): change "l. 1009" → "l. 1010" in both places.
4. L144-145: replace the quoted string with an accurate paraphrase, e.g. `Hold "folds into the trading decision" and "collapses at baseline anyway"` (two short quotes) or drop the quotation marks and just describe it indirectly.
5. L300-302, optional precision: relabel the Q2-table masses used for the 0.0153→0.00014 result as "illustrative masses" rather than implying they are the paper's calibrated baseline, since they differ from the true baseline ($\omega_P\approx0.037$ vs. the table's 0.20).
6. L283-286: either cite the script/source that produced the $0.0180\to0.0040$ / $0.0165\to0.0106$ TV-vs-$\omega_P$ sweep (it isn't in `theory_referee.md` or `verify_theory.md`), or replace it with the values that are already verified in `verify_theory.md` O-1 (TV_disc 0.017594→0.003988, TV_nodisc 0.016537→0.010550 over the four confirmed $\omega_P$ points).
7. L542: "AFS +0.9pp/SD loading on both filing types" — optionally note the actual split (0.90pp 13D / 0.81pp 13G) since they aren't identical.

## Summary (for caller)

49/55 checked sub-facts MATCH; every prior MISCITED/WRONG item from the referee round (C-T10, C-T12, D-2c, D-2d, F-1, F-2, F-4, Norli "(IV)", Gantchev order) was correctly fixed in v3.1. Four new issues, all citation/label precision, not economics:
1. `framework_v3.qmd:207` — Back et al. σ²T quote cited as p. 1436; primary source's page header shows **p. 1453**.
2. `framework_v3.qmd:124-125, 181` — dilution labeled $\varphi$; D7's own footnote (`D7_takeover_game_microfound.tex:73`) reserves $\varphi$ for the normal density and $\phi$ for dilution — symbols are swapped.
3. `framework_v3.qmd:227-228, 582` — draft_v2.tex line cited as "l. 1009"; the sentence is actually at **l. 1010** (confirmed by `grep -n`).
4. `framework_v3.qmd:144-145` — "Hold collapses at baseline anyway" given in quotes but is a reconstruction; pre-review source (`quality_reports/rewrites/framework_v3_pre-review_2026-08-19.qmd:88`) reads "Hold folds into the trading decision; it collapses at baseline anyway."

One item, `framework_v3.qmd:283-286` (TV 0.0180→0.0040 / 0.0165→0.0106), could not be located in the named sources (`theory_referee.md`, `verify_theory.md`) — endpoints are roughly consistent with independently-verified O-1 data but not independently confirmed. Full detail, all 55 rows, and one-line fixes are in `research/review_v3/verify_memo_v31.md`.
