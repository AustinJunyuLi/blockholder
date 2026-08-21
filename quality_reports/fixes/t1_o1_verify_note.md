# t1_o1_rerun_check — verifier note

Adversarial re-check of ticket 05's verification box: `t1_o1_rerun_check.py`, its
committed `t1_o1_rerun_check.json`, and the claims in `research/model_v4/HANDOFF_sign.md`.
Written by a fresh verifier who did not write the script.

## Verifier re-run (2026-08-21)

### 1. Determinism

| Property | Result |
|---|---|
| RNG | None. No `random`, no `numpy.random`, no seed needed. |
| Wall clock | None. `results["experiment"]["date"]` is the hardcoded string `"2026-08-21"`, not `datetime.now()`. |
| Network | None. |
| File reads | None. The only file IO is the JSON write at the end. |
| Recomputes from `numerical/` | **Yes.** Imports `numerical.model`, `numerical.params`, `numerical.solver` only. No CSV is read — notably not `numerical_output/data/disclosure_attenuation.csv`, which the *original* v3 verifier did read for its O-1b block (`verify_theory.md:54`). The docstring's claim "the exported CSV is NOT read" is true. |
| `numerical/` modules themselves | `grep` for `random|seed|time\.|datetime|urllib|requests|open(` over `solver.py`, `model.py`, `params.py` → zero hits. |

### 2. Re-run

```
.venv/bin/python quality_reports/fixes/t1_o1_rerun_check.py
EXIT = 0
```

Six checks recorded, `n_fail = 0`, `all_pass = true`.

**JSON byte-match: YES.** `sha256` of the freshly produced file equals the `sha256` of
the committed file taken before the run:

```
b31962b5ccb2360e7e555fa63f1f18b49fe1c61e60e771a49f6abda0f508148a
```

`cmp` → byte-identical. No field diff to report.

### 3. Independent recompute (not the script)

Written from the claim text, different grid construction (`0.15 + i*step`, not
`linspace`), mean |slope| computed directly rather than derived from TV:

| `k_D` | Ω | TV disc | TV nodisc | ratio TV | ratio mean-slope |
|---|---|---|---|---|---|
| 2.26113 | 0.037252 | 0.017594 | 0.016537 | 1.06397 | 1.06397 |
| 1.80000 | 0.128950 | 0.015981 | 0.013500 | 1.18373 | 1.18373 |
| 1.40000 | 0.285804 | 0.012110 | 0.010658 | 1.13631 | 1.13631 |
| 1.00000 | 0.500000 | 0.003988 | 0.010550 | 0.37798 | 0.37798 |

Identical to the script's output. The result is not self-confirming.

### 4. Per-claim verdicts

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Script is deterministic, recomputes from `numerical/`, reads no CSV | **CONFIRMED** | Source read + grep over the three imported modules; only `open()` is the JSON write |
| 2 | Re-run reproduces the committed JSON | **CONFIRMED** | exit 0, sha256 byte-identical |
| 3 | Committed ratios 1.0640 / 1.1837 / 1.1363 / 0.3780 appear at `verify_theory.md:32` | **CONFIRMED** | Line 32 verbatim: "Ratios 1.0640 / 1.1837 / 1.1363 / 0.3780" |
| 4 | The executed 41-point table sits at `verify_theory.md:42-53` | **CONFIRMED** | Lines 42–53 exactly: header at 45, four data rows at 47–50, reading at 51–52 |
| 5 | Ω values 0.037 / 0.129 / 0.286 / 0.50 appear in the referee report | **CONFIRMED** | Referee report lines 116–117 |
| 6 | The committed claim lives at referee report **lines 113–120** | **MISCITED** | The window/timing bullet is **114–119** (113 is the tail of the *previous*, threshold-margin bullet). The figure-magnitude claim the script also reproduces (`0.01107` / `0.01117` / `0.0251` / `0.0236`) is at **122–123**, i.e. *outside* the cited range; its bullet spans 120–124. Correct range: **114–124**. Carried identically by `t1_o1_rerun_check.py:26` (`COMMITTED["source"]`) and `HANDOFF_sign.md:52`. Fact right, line range wrong. |
| 7 | Handoff: baseline cutoffs `k1 = k0 = 0.821738`, `k_D = 2.261127` | **CONFIRMED** | JSON `checks[0]`: 0.8217375898536412 / 2.2611270959836602 |
| 8 | Handoff: ratios 1.064 / 1.184 / 1.136 / 0.378 and per-row diffs 2.8e-05 / 3.1e-05 / 1.2e-05 / 2.2e-05 | **CONFIRMED** | JSON `numbers[]`, `abs_diff_vs_committed` matches every digit |
| 9 | Handoff: Ω values 0.037252 / 0.128950 / 0.285804 / 0.500000; masses (0.400481, 0, 0.562266, 0.037252) | **CONFIRMED** | JSON `numbers[].Omega` and `checks[0]` |
| 10 | Handoff: `k_D* = 1.28618`, `Ω* = 0.3428` → condition "Ω < 0.343" | **CONFIRMED** | JSON `crossing`: 1.28618407726065 / 0.342839683502031 |
| 11 | Handoff: ranges 0.01107 vs 0.01117, a **0.9%** gap, at most **2.5%** apart at any κ; mean slope 0.02512 vs 0.02362 | **CONFIRMED** | JSON `figure_magnitude`: 0.011069979939 / 0.011170435095; `relative_range_gap` 0.008993 (0.90%); `max_pointwise_relative_gap` 0.024763 (2.48% ≤ 2.5%); 0.025123586 / 0.023624545 |
| 12 | Handoff: flagged curve steeper at *every* grid point above κ = 0.7 for all three low-Ω rows | **CONFIRMED** | JSON `pointwise.per_kD`: `true` for k_D 2.261 / 1.800 / 1.400, `false` at 1.000 (Ω = 0.50), as the claim requires |
| 13 | Handoff §4.1: "a **6%** difference in κ-sensitivity at the paper's own calibration" | **CONFIRMED** | Baseline ratio 1.06397 → 6.4% |
| 14 | Handoff §1 Evidence: "**Five checks**, all pass" | **WRONG** | The JSON records **six** checks (`baseline_cutoffs_and_masses`, `o1_ratios_match_committed_claim`, `o1_substance_attenuation_fails_below_Omega_029`, `o1_pointwise_slopes_above_kappa_07`, `o1b_figure_magnitude_at_baseline`, `o1_sign_flip_located`), `n_fail = 0`. Substance ("all pass") is right; the count is off by one. Touches no result. `HANDOFF_sign.md:31` — change "Five" to "Six". |
| 15 | ω_a anchor — Becht, Franks, Grant & Wagner (2017 RFS), fn. 2 and fn. 15 | **CONFIRMED** | `research/cards/becht_franks_grant_wagner_2017_rfs.md:119` carries the fn. 2 quote verbatim ("What we cannot capture is private activism…"), tagged "PDF p. 10 (printed 5), fn. 2"; line 96 carries "currently not available to us (PDF p. 27, fn. 15)". Both cited lines correct. |
| 16 | ω_a anchor — Norli, Østergaard & Schindele (2015 RFS), n. 10 | **CONFIRMED** | `research/cards/norli_ostergaard_schindele_2015_rfs.md:101`: "The paper concedes that private engagement may matter and that data on it do not exist (printed p. 10, n. 10)." Line and footnote both correct. |
| 17 | ω_a anchor — Edmans (2014 survey), p. 35 | **CONFIRMED** | `research/cards/edmans_2014_arfe_survey.md:114`: "In practice, investors may cluster just below 5% to avoid disclosure, and thus be missed by Schedule 13 filings" (p. 35). Quote verbatim, page correct. |
| 18 | Proxy — BJPT (2008 JF) **97.5%**, 1,032 of 1,059, +27 via a 13F sweep | **CONFIRMED** | `brav_jiang_partnoy_thomas_2008_jf.md:16` ("236 funds, 1,032 events"; "a 13F sweep to catch sub-5% activism at firms with market value > $1bn where the fund held > 2%, which added 27 non-13D events"), `:17` (N = 1,059). **executed**: 1032/1059 = 0.97450 → 97.5%. The handoff's "upper bound only" caveat matches the card's own construction wording. |
| 19 | Proxy — Gantchev (2013 JFE) **98.2%**, 21 sub-5% of 1,164, fn. 21 nonrandom | **CONFIRMED** | `gantchev_2013_jfe.md:26` (1,164 campaigns), `:62` (21 sub-5% campaigns + fn. 21 verbatim "represent a nonrandom sample … large and newsworthy targets with above-average press coverage", PDF p. 20). **executed**: (1164−21)/1164 = 0.98196 → 98.2%. *Nit:* the handoff puts the word "nonpublic" in quotes against `:26, 62`; Gantchev's own word "nonpublic" is on the same card at `:114` (Q3). Format only. |
| 20 | Proxy — SEC Release 33-11253 **12.1%**, 1,161 initial 13D vs 8,433 initial 13G | **CONFIRMED** | `_institutional_sec_33_11253.md:98` (1,161 initial 13D filings; section header at `:93` reads "Table 1, p. 177"), `:102` (8,433 initial 13G filings, p. 190). **executed**: 1161/(1161+8433) = 0.12101 → 12.1%. Page citations "p. 177; p. 190" both correct. |
| 21 | Handoff §6 identity Ω = Pr(a=1)·ω_a | **CONFIRMED** | **executed**: at baseline Pr(a=1) = ω_Q + Ω = 0.599519, so ω_a = 0.037252/0.599519 = 0.06214, and 0.599519 × 0.06214 = Ω. Definitional, holds. |

### 5. Two things flagged for the record (neither blocks)

- **The referee report's own 2 dp rounding is wrong at one cell.** Line 117 prints
  "1.19 at ω_P=0.129"; the value is 1.1837, which rounds to **1.18**. The handoff's §3
  table compares against `verify_theory.md`'s 4 dp figures and is unaffected, but the
  script's docstring asserts the referee report's 2 dp numbers are the same numbers.
  If anyone re-quotes the referee report at 2 dp, quote 1.18.
- **`TOL_MATCH = 5e-3` is ~100× looser than the committed record's printed precision**
  (4 dp). It passed with `max_abs_diff = 3.1e-05`, i.e. with two orders of magnitude to
  spare, so nothing was hidden — but the gate as written would also pass a real drift of
  4e-3. Tightening it to 1e-4 would cost nothing and make the check mean what it says.

### 6. Overall

**PASS.** The script is deterministic and recomputes from `numerical/`; the re-run exits 0
and reproduces the committed JSON byte for byte; an independently written recompute
reproduces all four ratios; every economic number in `HANDOFF_sign.md` traces to a JSON
field; and all six ω_a anchor citations are confirmed against the cards. The single WRONG
(#14) is a miscounted check tally in one prose cell — six checks, not five — and refutes
no result. One MISCITED (#6): the referee-report line range should read 114–124.
