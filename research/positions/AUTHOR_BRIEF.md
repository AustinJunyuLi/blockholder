# Author brief

## 1. The decision you are being asked to make

Choose the paper's **position** — object, **disclosure-rule** margin, identification. Three options: winner P2, runner-up P4, or P2's **core model** plus P4's empirics.

## 2. The five positions in one line each

- **P1.** **Premium wedge** · **window** length (level in theory; **Feb-2024 acceleration** in the data) · five-business-day 13D deadline.
- **P2.** Expected premium (run-up vs filing jump) via bidder entry · the **partition** (threshold and deadline as keys) · Rule 13d-1(a).
- **P3.** Bidder entry and expected premium via the flagged stake · window as a deadline on the partition · same rule.
- **P4.** **Control outcome** (bid within twelve months of a 13D) · window as the Feb-2024 change · the acceleration, first stage in hand.
- **P5.** Bidder entry and premium across declared purpose · 13D vs 13G as a level (20% override as the change) · the purpose declaration.

## 3. The winner: P2

The paper would be about the disclosure rule as the market's partition — identity and **whitespace** W3.

**Main result and honesty label.** In a cutoff equilibrium the rule imposes a flagged/pooled split at the control-decision node. Expected premium decomposes; the flagged cell is **liquidity**-invariant; the pooled cell carries the entire liquidity derivative; tightening either key attenuates liquidity-sensitivity. Labels: **PROVED** at fixed cutoffs; region-certified **PROVED** in GE; **NUMERICAL** off-region. No global GE sign.

**December package.** Core rebuild 3–4 weeks; attenuation in days; region certificate 1–2 weeks; timing-split **clean result** ~1 week on data in hand. Premium specified only. Fallback already a full draft.

**Why the judges picked it.** Judges 1 and 2 ranked it first (Borda 14; 79/90): identity cell; reused machinery; first-class **deliverability**; fallback already a draft; repairs draft_v2's ad-hoc flag. Ties broken vs P3 (deliverability) and vs P4 (identity).

**Three amendments.** (1) Cite CCKV from its own words, not a card sentence at page 11. (2) CCKV Theorem 1 is predictability of order flow, not non-monotone inference. (3) Power figures are an author sketch; drop the false feasibility cite.

## 4. The runner-up: P4

Feb-2024 acceleration × control outcomes × matched never-13D DiD — **whitespace** W2 (clear on the cell; hard on execution).

**Main result and honesty label.** Effect on the twelve-month bid hazard versus matched controls, bounded and estimated; a companion model signs the per-campaign effect where stake-bargaining dominates certification. Label: **ESTIMATED**. **Power caveat:** constrained tail ~3% (~7/year); design detects ~6–10 pp on a ~17–18% base. Stands only if the **bounded null** is the headline.

**December package.** Parser, matching, matched DiD, bounded null, placebos, pre-trends. Pill split and causal premium specified only. ~16 weeks. Only complete **referee-checklist** design on a control outcome with a control group.

**Why it placed second.** Highest raw total (81/90); Judge 3's winner. Best empirical design. Loses the top spot: thin companion model; crowded **anchor**.

**Five amendments.** (1) First-stage t = 2.69; drop the t > 3 parenthetical. (2) 18.1% is acquired-within-twelve-months, not bid hazard. (3) Bound = accumulation tail only; estimate is reduced-form (accumulation, defense, selection); do not call ≤ ~3 pp the aggregate footprint. (4) **PROVED**: quadratic cost and the appropriability coefficient (including the pivotality jump); **PROVED-conditional**: interior stake; **ASSERTED-conditional**: entry sign. (5) Write never-13D, not never-targeted.

## 5. The package option (P2's model + P4's empirics)

Two judges said the natural paper is P2's partition core with P4's matched, bounded-null empirics as the control-outcome leg (Judge 3: P2 and P3 are near-identical in position). You keep the identity cell and get a December **clean result** that is a control outcome with a control group, plus P2's cheap timing split. Cost: P2's model 3–4 weeks plus 1–2 for the equilibrium region; P4's empirical track ~9–13 weeks — harder than P2 alone. This may be the real choice: identity plus a checklist-complete control-outcome claim.

## 6. What happens to the losers

- **P1.** Not the identity; its tender-game wedge survives inside P2 or as P4's sign model.
- **P3.** Folds into P2; its 13G-run-up placebo and accumulation skeleton travel with it.
- **P5.** Blocked on the walled Payne-Mann PDF; if that paper keys a control outcome to 13D vs 13G, the "first" claim dies.

## 7. Open hazards you own

- **Payne-Mann (SSRN).** Only you can download it. It decides whether P5's cell is open.
- **BLV Dec-2025 revision.** Unobtained. Live risk on the wedge for any position that keeps the appropriability coefficient.
- **Zeng's IA Table 2.** Not in hand. P2 treats the body-text size split as the nearest occupied cut; unchecked against the appendix.

## 8. What happens after you decide

The decision is written into the ticket comments and an ADR. Ticket 04 restates the **core model** from the chosen position. Once the winner is known, you will also be asked how much new theory to take on.
