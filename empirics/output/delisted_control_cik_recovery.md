# Delisted-control CIK recovery (option 2)

Generated 2026-08-31T08:49:18+01:00.

Austin selected option 2 as the primary treatment: Geode 13F CUSIP to issuer name to CIK, with a validation gate. Option 1 is the fallback for unresolved rows.

Delisted controls: 1120. Validated: 419. Unresolved: 701. Gate: passed_with_validated_rows. Fallback: option_1_for_unresolved_rows.

A recovered CIK enters `permno_cik_map.csv` only after its validation row is written. Ambiguous names and failed dates keep a blank CIK.

Unresolved delisted controls stay out of matching. That conditions the control group on survival, so the control bid rate is biased down and gamma is biased up.
