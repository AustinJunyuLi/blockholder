# T2 check-script re-run verification (ticket 28 D-series discipline)

**Re-runner:** fresh Opus agent, wrote none of the eight scripts. Adversarial
stance: the goal was to break the claims, not to confirm them.

**Worktree:** `/Users/austinli/Projects/blockholder_v4_theory` (branch `v4-theory`).
**Interpreter:** `.venv/bin/python` (CPython 3.12.13), invoked from the worktree root.
**Run window:** 2026-08-21 23:16 CST -> 2026-08-22 02:07 CST.
**No git commands were run. No script and no committed JSON was edited.**

---

## Overall

**ALL REPRODUCE.**

All eight scripts ran to completion. Every one of the eight freshly written JSONs
is identical to its committed counterpart **in every field except wall-clock
timing fields** (`seconds`, `wall_seconds`, and per-row/per-node `seconds`).
**Zero numeric result differences of any size** — not merely below the 1e-12
relative bar, but bit-identical: every non-timing float compared equal under
Python `==`.

One MISCITED item, on a characterisation in the handoff text rather than in any
committed artefact — see "Discrepancies" below. It does not affect any verdict.

---

## Per-script table

| script | exit code | byte-match | field diffs | headline claims confirmed |
|---|---|---|---|---|
| `t2_l3_check.py` | 0 | no | 1, timing only (`/seconds` 0.0647 -> 0.0323) | YES |
| `t2_l1_check.py` | 0 | no | 1, timing only (`/seconds` 84.93 -> 79.60) | YES |
| `t2_l2_check.py` | 1 | no | 1, timing only (`/seconds` 135.64 -> 119.46) | YES |
| `t2_d1_check.py` | 0 | no | 1, timing only (`/seconds` 191.77 -> 179.79) | YES |
| `t2_l4_check.py` | 0 | no | 1, timing only (`/seconds` 414.66 -> 400.93) | YES |
| `t2_t1_check.py` | 1 (see note) | no | 1, timing only (`/seconds` 918.14 -> 989.65) | YES |
| `t2_p1_check.py` | 1 (see note) | no | 35, timing only (7 node-set-A row `seconds`, 27 sweep row `seconds`, top-level `seconds` 9349.99 -> 9492.92) | YES on the FAIL identity and 23/27; the "pi_bar_pr = 0 corners" gloss is MISCITED |
| `t2_c1_region_check.py` | 0 (see note) | no | 81, timing only (80 per-node `seconds` + `wall_seconds` 10339.31 -> 8905.50) | YES |

**Exit-code note.** `t2_t1`, `t2_p1` and `t2_c1_region_check` were run detached
(`nohup`) because they exceed the 10-minute foreground tool ceiling, so their
raw exit status was not captured by the shell. All three ran to completion,
printed their normal summary line, and wrote a complete JSON. Every script ends
with `sys.exit(main())` and `main()` returns `0 if all_pass else 1` (c1:
`0 if n_fail == 0 else 1`), so the codes above follow deterministically from the
JSONs those runs wrote: t1 `all_pass=false` -> 1, p1 `all_pass=false` -> 1, c1
`n_fail=0` -> 0. The five foreground runs' codes were captured directly.

**A first `t2_t1` attempt was killed at 10 minutes by the tool timeout, not by a
crash.** It had not yet reached its JSON write; `t2_t1_check.json` was verified
byte-unchanged afterwards. The script was then relaunched detached and completed
normally in 990 s. **No `--quick` mode was used anywhere. Every script was run
full.**

---

## Headline claims, verified against the fresh JSONs

- **D1** — `all_pass = true`, `n_fail = 0`, 9 checks (1 vacuous:
  `d1_QF_T_monotonicity`). CONFIRMED.
- **L1** — `all_pass = true`, `n_fail = 0`, and all 4 checks carry
  `kind = "wiring"`. Wiring-labelled as reported. CONFIRMED.
- **L2** — `all_pass = false`, `n_fail = 1`, and the single FAIL is
  `l2_placebo_M_P_sign_A_tau`. Core invariance is **exactly** zero:
  `l2_flagged_invariance_ranges.max_range` = `{v_hat: 0.0, pi_flagged: 0.0,
  P_F: 0.0, p_bid: 0.0, M_F: 0.0, Omega: 0.0}` and
  `l2_flagged_invariance_derivs.derivatives` = `{dM_F_dkappa: 0.0,
  dOmega_dkappa: 0.0, dP_F_dkappa: 0.0, dp_bid_dkappa: 0.0}` — literal `0.0`,
  not "below tolerance". CONFIRMED.
- **L3** — `all_pass = true`, `n_fail = 0`, 10 checks, 0 vacuous. The
  amended-tolerance provenance is present as a `tolerance_amendment` field
  reading "tolerance amended per design review 2026-08-21: relative criterion
  residual/|C_h| < 1e-6 for the standalone chord route (pi_bar < 1e-2);
  absolute 1e-10 retained on the full-model route (pi_bar >= 1e-2)". CONFIRMED.
- **L4** — `all_pass = true`, `n_fail = 0`, 10 checks. `n_sign_violations = 0`,
  `n_sign_violations_model_route = 0`, `n_violations = 0`, and both `violations`
  and `violations_model_route` are empty lists. CONFIRMED.
- **T1** — `all_pass = false`, `n_fail = 1`, single FAIL
  `t1_block3_chord_magnitude` with `max_residual_pp = 0.6279460912900146`
  (~0.628 pp). O-1 benchmark ratios recomputed as
  `1.0639720903628607 / 1.183730968801152 / 1.136311993800545 /
  0.37797840338096084` against committed `1.06397 / 1.18373 / 1.13631 /
  0.37798`, `max_abs_diff_vs_committed = 2.09e-06` under `tol_ratio = 1e-4`;
  `kD_star = 1.28618431`, `Omega_star = 0.34283956`. Composition factors
  `1.1051410553 / 1.3589694200 / 1.5910362300 / 0.7559568068` against predicted
  `1.1051 / 1.3590 / 1.5910 / 0.7560`, `max_abs_diff = 4.32e-05` under
  `tol = 1e-3`. CONFIRMED. ("Exact" here means agreement with the committed
  digits to within the script's own stated tolerance, which is what the JSON
  asserts — not bit-identity.)
- **P1** — `all_pass = false`, `n_fail = 1`, single FAIL
  `p1_multistart_existence_sweep`, `n_converged = 23` of `n_nodes = 27`.
  CONFIRMED. The four failing nodes: see the discrepancy below.
- **C1** — `all_pass = true`, `n_fail = 0`, 12 checks split **4 PASS / 8 RECORD /
  0 FAIL**; `n_error_nodes = 0`, 80 nodes, `empty_region = false`,
  `n_certified = 18` of 80, `L_min = 0.26358722`, `L_max = 0.50081835`
  (L_R in [0.264, 0.501]), `n_nodes_with_L_ge_1 = 0`,
  `eta_min = 0.05953542544265861` (~0.0595), `eta_median = 0.34671597`,
  `eta_max = 1.72272795`. CONFIRMED.

---

## Discrepancies

**One. MISCITED — P1's four failing nodes are not "pi_bar_pr = 0 corners".**

The re-run reproduces the FAIL exactly (23/27), but the handoff's gloss on *which*
four nodes fail is not supported by the artefact. The four rows with
`converged_payoff = false` are:

| kappa | tau | T | `corner` | `converged_cutoff` | `best_payoff_scale` |
|---|---|---|---|---|---|
| 0.15 | 0.05  | 5 | **false** | true | 1.488e-3 |
| 0.15 | 0.075 | 1 | **false** | true | 1.059e-3 |
| 0.85 | 0.05  | 5 | **false** | true | 3.984e-4 |
| 0.85 | 0.075 | 1 | **false** | true | 3.061e-4 |

`corner` is set at `t2_p1_check.py:557` as `bool(T == p.H)`, i.e. T at the
horizon H = 10. None of the four failing nodes is a corner in that sense; all
nine corner rows in the sweep converged. Nor is `pi_bar_pr` zero anywhere in the
file: the string `pi_bar_pr` occurs exactly once in `t2_p1_check.json`, with
value `0.10206126073370039`, and the word "corner" appears only as the field
name — there is no note anywhere in the JSON characterising the failures that
way.

What the artefact actually shows is different and more specific: all four
failures are at the **kappa extremes** (0.15 and 0.85), at the two **lower tau**
values, at T in {1, 5}; in every case the **cutoff** criterion converged and only
the **payoff** criterion did not, at a payoff scale of 3e-4 to 1.5e-3. The claim
stands; the citation does not. Swap the gloss for the table above.

Nothing blocks. No WRONG verdict on any script. No UNCHECKED claims — every
headline item was checked against a completed executed run.

---

## Determinism

No concerns.

- **RNG.** The only randomness anywhere in the dependency closure is
  `np.random.default_rng(seed)` at `numerical_v4/solver.py:148`, with an explicit
  integer seed (0 on the default path, `sd = 0..29` in P1's multistart), and
  `jitter = ... if seed else np.zeros(2)` — the seed-0 path takes no draw at all.
  The v2 `numerical/` package used by T1 contains no RNG at all. No unseeded RNG,
  no Monte Carlo.
- **Clock.** `time.perf_counter()` is used only for the reported `seconds` /
  `wall_seconds` / per-row `seconds` fields. No date, no `datetime`, no
  clock-dependent branching. These fields are the *entire* content of every
  byte-level difference observed across all eight scripts.
- **Inputs.** Zero. Grep across all eight scripts and all of `numerical_v4/`
  found no `open(..., "r")`, `json.load`, `read_csv`, `loadtxt`, `np.load`,
  `pickle`, `os.environ`, `getenv`, `subprocess`, `urllib`, `requests` or
  `socket`. Every script's only file operation is `open(OUT, "w")` on its own
  JSON. Everything is computed from `numerical_v4/` (and, for T1's block 6, the
  static `numerical/` package) at run time — nothing is read back from a result
  file. `sys.path` is set from `os.path.abspath(__file__)`, so the runs are
  cwd-independent.
- **Self-overwrite.** Each script writes to its own committed JSON path, so
  running it necessarily rewrote the committed file. All eight were copied to a
  scratch directory before the first run and **restored byte-for-byte
  afterwards**; the eight SHA-256 sums in the worktree now equal the as-found
  sums. C1 additionally writes incrementally per node
  (`t2_c1_region_check.py:594`), so a crash would leave a partial file — the
  fresh C1 output was checked complete (80 nodes, `wall_seconds` present).
- **Scheduling.** Wall time was compressed by overlapping the three long runs:
  `t2_l3` ran first to validate the environment, then `t2_c1_region_check` and
  `t2_p1_check` were launched detached while `l1 -> l2 -> d1 -> l4 -> t1` ran in
  the requested cheap-first order in the foreground. At most three Python
  processes ran at once on a 10-core machine. Since the scripts share no state
  and read no files, this affects only the timing fields — and indeed the only
  fields that moved were timing fields.

**Total runtime:** 20,168 s of script time (5 h 36 m summed: l3 0.03 s, l1 79.6 s,
l2 119.5 s, d1 179.8 s, l4 400.9 s, t1 989.7 s, p1 9,492.9 s, c1 8,905.5 s),
compressed into **2 h 51 m of wall time** by the overlap above.
