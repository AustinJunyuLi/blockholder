# Referee report

## What I would say first

I would not recommend acceptance in the current form. The status labels and numerical trail are unusually careful, and the Blackwell garbling result is the strongest part of the paper. But the legal clock does not map into the calibrated clock, several formal claims are unlabelled, and the appendix has proof and boundary defects. The current economic result is a fixed-policy information experiment, not yet a result about equilibrium behavior or the effect of the disclosure reform.

## Is this the strongest framing?

No. The title and opening invite a rule-design result about observable blockholders who are caught. The strongest defensible framing for the current results is a narrower note on information accounting in a fixed-policy order-flow model, centered on the garbling lemma. The paper could sustain its present framing only after it gives the legal clock a coherent unit, makes the public information set institutionally credible, and either supplies an equilibrium foundation or states much more plainly that the cutoff assignment is exogenous. The "who gets caught" language is also too literal because the caught leg includes the re-pricing of survivors and is not, in general, a statistic of the newly flagged histories.

## Blocking items

1. **The statement of the US filing obligation is false as written.** [FIXED: Corrected statutory trigger in Sections 1 and 2.1 (`paper.tex:78-82, 158-164`) to beneficial owners of more than 5% of a registered equity class who do not qualify for or elect Schedule 13G.]

2. **The legal clock and the numerical clock use different units.** [FIXED: Clarified in Sections 1, 2.1, 3.2, and 5 (`paper.tex:83-85, 165-171, 280-284, 725-731`) that $T$ is denominated in discrete trading rounds, and that comparing $T=10$ with $T=5$ is a model comparative static across trading-round windows (with $T=10=H$ being a corner horizon with a degenerate flagged cell) rather than a calibrated replica of the statutory reform.]

3. **The literature section misnames the formal outcome.** [FIXED: In Sections 1, 2.2-2.3, and 3.5 (`paper.tex:90-95, 184-192, 407-414`), the formal outcome is explicitly defined and named as the engagement-related component of the expected takeover premium, $\Delta^{\mathrm{act}} = \Delta_m \mathbb{E}[\pi p]$, omitting the baseline entry term $m_0 \mathbb{E}[p]$.]

4. **Several shipped analytic and numerical claims have no honesty label.** [FIXED: Added Lemma 1 (pricing root) and Lemma 2 (window monotonicity of $B^F$ under fixed policies) to `proofs/06_lemmas.tex` and cited them in `paper.tex:308, 432, 863`. Both lemmas remain unlabelled pending the orchestrator attack gate. Deleted unrecorded assertion about selected Voice paths finishing building by filing date from Section 5 (`paper.tex:663-667`).]

5. **The pooled-experiment proofs use missing independence hypotheses.** [FIXED: Added explicit clauses for i.i.d. noise across rounds and type independence to `proofs/02_garbling.tex:28-56, 91-125, 236-242, 283-310`.]

6. **The pooled-experiment block is undefined at a null pooled cell, while the paper also overstates the endpoint cells.** [FIXED: Required $\Omega < 1$ for definition of $\rho_P$ and Lemma 6, and required $\Prb(\mathcal A) > 0$ for Lemma 5(c) in `proofs/02_garbling.tex`. In `paper.tex:454-457`, corrected "null set rather than an empty one" to "null, possibly empty".]

7. **The appendix artifact does not carry a consistent honesty status.** [FIXED: Configured automated `\noindent\textsc{Label: PROVED.}\par` prepending hooks in `appendix.tex` for proved theorem/lemma environments (with `\unlabelledtrue` scoping for new lemmas). Deleted stale conjecture comment in `proofs/03_caught.tex:14`.]

8. **The appendix's final reading of the clock criterion is false.** [FIXED: In `proofs/03_caught.tex:354-358`, corrected the informal closing sentence to state the exact attenuation criterion: $s_B$ between $0$ and $(2/\varphi)s_A$ under common sign $s_A \ge 0$.]

9. **The `ESTIMATED` label does not meet the paper's stated label rule.** [FIXED: In `paper.tex:782-812`, scoped the `ESTIMATED` label strictly to the post-minus-pre bootstrap differences in Section 6.2; presented the by-year and by-period tables as registered descriptive statistics.]

10. **Figure 1 identifies finite differences as analytic derivatives.** [FIXED: In Figure 1, `numerical_v4/checks/figures.py`, and `paper.tex:682-689`, replaced point derivative notation with finite-difference notation $|\Delta \Delta^{\mathrm{act}} / \Delta\kappa|$ and $|\Delta M_P / \Delta\kappa|$.]

## Minor items

1. **The economic policy is imposed rather than derived.** [FIXED: Clarified throughout (`paper.tex:103-107, 375-378, 400-405`) that economic policies are imposed as a disciplined benchmark policy profile isolating the information-accounting decomposition without claiming equilibrium existence.]

2. **The flagged information set is stronger than a Schedule 13D filing.** [FIXED: Supplied Item 4 purpose and plans disclosure as the institutional reading for public $(B^F, Q^F, a=1)$ in Sections 1 and 3.4 (`paper.tex:87-91, 345-352`).]

3. **The threshold result is much narrower than the two-dial framing.** [FIXED: Silence-first framing adopted; noted narrow 5-node threshold ladder ($9.24\%$ to $9.70\%$) upfront on page 2 in `paper.tex:105-110, 544-550`.]

4. **The empirical population does not map cleanly to Voice.** [FIXED: Clarified empirical population (all initial Schedule 13Ds unfiltered by Item 4 text, maximum across reporting persons in joint filings) in Sections 1 and 6.1 (`paper.tex:126-130, 788-796`).]

5. **The surviving empirical section does not measure market inference.** [FIXED: Clarified in Sections 1, 2.4, and 6 (`paper.tex:126-132, 235-240, 780-786`) that empirics measure filing stakes and delays ($B^F$ and $T$) to provide descriptive institutional context for parameters, while market inference is evaluated via the model.]

6. **The delay data need an outlier and validity discussion.** [FIXED: Added data validity and outlier discussion in Section 6.3 (`paper.tex:865-874`) regarding the 2 negative delays and 138 pre-2021 triggers, explaining robustness of medians and within-5-day shares.]

7. **Paper and appendix numbering do not map.** [FIXED: Added explicit pointers in Section 4 of `paper.tex` (`paper.tex:447-620`) to corresponding appendix sections and lemmas using `xr` with `app:` prefix.]

8. **Several set-equality readings need "almost surely."** [FIXED: Added "almost surely" / "up to a null set of histories" to set equality and reclassification claims in `proofs/02_garbling.tex:193-204, 388-407` and `paper.tex:560-563`.]

9. **The novelty claims are categorical.** [FIXED: Toned down categorical novelty claims in Sections 1 and 2 (`paper.tex:133-138, 200-213`).]

10. **The PDFs have avoidable production defects.** [FIXED: In `numerical_v4/checks/figures.py`, configured `pdf.fonttype = 42` and `ps.fonttype = 42`, eliminating Type 3 fonts in all 3 figures; decluttered Figure 2 labels; verified appendix p. 12 begins with a clean full paragraph; adjusted bibliography item spacing and font in `paper.tex` so page 19 contains 14 entries without trailing orphan lines.]

## Checks with no finding

- I found no manuscript-number mismatch. The E1 values match `empirics/output/e1_estimate.json` after the stated rounding. The factorisation, threshold, clock-table, and who-gets-caught numbers match the named JSON records under `numerical_v4/checks/`.
- The paper reports neither a run-up and jump result nor an existence result.
- `paper.log` and `appendix.log` have no TeX errors, undefined references, undefined citations, overfull boxes, or underfull boxes. The PDFs render without clipping.
