# Matched DiD, §8.2 matching stage: result and design failure (2026-08-31)

Dated note under §0 rule 1. **No SPEC object changes.** This records the
realised matching draw, the registered balance gate it fails, and one
observation about the registered remedy that is a decision for Austin, not
for this session.

Artefacts: `empirics/output/did_match_pairs.csv`,
`did_match_quality.csv`, `did_match_shortfalls.csv`, `did_match_meta.json`,
`did_estimate.json` (label `NOT ESTIMATED`).

## 1. The realised treated sample is 465, not 569 / 543

SPEC §8.6 quotes 569 pre / 543 post for the S1 estimation sample. That is the
§2.3 funnel's estimation sample. This leg applies the §8 restrictions on top
of it, and they are all registered:

| step | rows |
|---|---|
| `bid12_treated.csv` rows with a trigger date | 3,710 |
| less 2025, the extension window (§8.5 row v) | 1,024 |
| less TDs after 2024-12-17, the structured-data regime break (§8.5 row v) | 1,083 |
| less unresolved BID12 (ambiguous or not extracted; rulebook §7, §5.1 item 5) | 241 |
| less already under an announced bid at TD (§8.3) | 207 |
| less §2.5 straddlers | 94 |
| less the §2.6 anticipation stub | 261 |
| less rows outside the H1 main sample | 1,364 |
| less rows with no 2-digit SIC in EDGAR | 29 |
| **treated matched sample** | **465** (325 pre / 140 post) |

The pre/post split is 325 / 140, not the 569 / 543 §8.6 computes on, because
§8.6's counts were taken before the §8 restrictions. On these counts the §8.6
arithmetic gives SE 4.17 pp, MDE **11.70 pp**, clustered **15.32 pp**, against
the printed 6.94 / 9.09. That is design arithmetic on registered anchors
(p_T = 0.181, p_C = 0.072, variance term 0.1705, multiplier 1.31), not a
realised MDE: no regression was estimated, so no fitted standard error exists.

The reading of §6 hardens rather than changes. The headline rung of the
bounded-null ladder is 3 pp. The design that was already three times too
coarse to see under it is now five times too coarse. The loose 20 pp rung is
still inside reach on paper.

## 2. The control pool

3,600 never-13D PERMNOs, all present in the CRSP panel. 2,763 carry a CIK
link after the recovery gate (419 recovered rows admitted, 0 refused, 701
unresolved delisted rows left out under option 1). 9 drop for a blank SIC in
EDGAR and none for a missing submissions file, leaving **2,754** usable
controls against 465 x 3 = 1,395 requested pairs.

Adequate in aggregate. Not adequate inside exact SIC-2 x quarter cells, which
is exactly where §8.2 said the tightness would bind.

## 3. The 3:1 shortfall, reported rather than assumed away

| | |
|---|---|
| SIC-2 x quarter cells | 221 |
| cells short of 3:1 | 181 |
| cells with no match at all | 80 |
| pairs requested | 1,395 |
| pairs matched | 839 |
| pair shortfall | 556 |
| treated rows at the full 3:1 | 236 of 465 (50.8%) |
| treated rows with 2 / 1 / 0 matches | 31 / 69 / 129 |

## 4. The balance gate fails, and the leg is NOT ESTIMATED

Standardised differences after matching, both attempts:

| covariate | matched dimension | 0.25 caliper | 0.20 caliper | above 0.10 |
|---|---|---|---|---|
| logcap | yes | -0.078 | -0.067 | no |
| logilliq | yes | 0.060 | 0.055 | no |
| turnover | no | 0.074 | 0.065 | no |
| ret12m | no | -0.119 | **-0.131** | **yes** |
| idiovol | no | 0.157 | **0.122** | **yes** |

SPEC §8.2 requires any standardised difference above 0.10 to be reported and
the match re-run at a tighter caliper; §8.9 makes differences that a tighter
caliper does not fix a **design failure**, and the leg is then demoted to
descriptive. The rerun ran once at the predeclared 0.20 caliper. Two
covariates remain above 0.10. `empirics/output/did_estimate.json` therefore
carries `label: NOT ESTIMATED`, `status: design_failure`, and no coefficient.

Three things this failure is not. It is not a coding bug: the gate fired on
the registered threshold, and the fixture suite covers the path. It is not a
failure of the two matched dimensions, which balance at 0.067 and 0.055. And
it is not obviously a matching artefact: worse trailing returns and higher
idiosyncratic volatility are the standard profile of an activist target, so
the imbalance is plausibly a real property of who gets a 13D.

## 5. One observation for Austin, not a fix

**The registered remedy cannot reach the covariates that failed.** The
caliper is defined on log size and log illiquidity. Tightening it moves the
matched dimensions, which already pass, and reaches `ret12m` and `idiovol`
only through whatever correlation they happen to have with size and
illiquidity. Between the 0.25 and 0.20 attempts, `idiovol` improved (0.157 to
0.122) while `ret12m` got worse (-0.119 to -0.131), which is what an
incidental channel looks like. A third tightening is not registered and was
not run.

Two post-registration options exist, and both change the registered rule, so
neither was adopted here:

1. Read "any standardised difference" as covering the two matched dimensions
   only, and the three book-to-market substitutes as reported diagnostics.
   The §8.2 sentence follows a list containing all five, so this is a
   narrowing of the registered text.
2. Add past return and idiosyncratic volatility as matching dimensions. That
   changes the matching design in §8.2 and would need its own power note
   against a pool that is already short in 181 of 221 cells.

Filed the way the Datavault rulebook-coverage observation was filed: recorded
with its numbers, not acted on.

## 6. What the failure does not block

The design failure is a bar on the §8 coefficient. It does not touch the
BID12 coder, so the control half of the blind audit proceeds unchanged and on
the same 30-pair threshold. `did_match_pairs.csv` exists, so the control-side
BID12 lookup and the §9 within-13D-targets leg both have their inputs. The
§8.7 placebo re-matches at every pseudo-date and inherits the failure.

`did_estimate.json` also carries `quote_as_result: false` and the signed
survivorship block (control bid rate biased down, gamma biased up, 701
unresolved delisted controls). Those hold whether or not a coefficient
exists, so they are written on this path too.
