# Supporting Files

## recalibrate.py (Systematic Parameter Sweep)

This script was run to verify that no parameter combination in (λ_B, C₀, S̄, s_ξ, Δ_S) space can simultaneously achieve all 8 calibration targets. It evaluates 640 configurations.

**Key finding:** Zero configurations achieved the "triple win" (hump + hold + disclosure effect > 1%). The disclosure effect is structurally zero across all tested parameters when A5 holds.

```python
"""
Systematic recalibration sweep for the EVT model.

Explores (lambda_B, C0, S_bar, s_xi) space to find parameters that produce:
1. Interior hump in Delta^min (peak at kappa in [0.25, 0.70])
2. Hold region exists (k0 > k1 + 0.01)
3. Disclosure effect (baseline != no-disclosure)
4. Realistic bid rates (unconditional ~2-8%)
5. Hump amplitude > 5% of peak value
"""

import itertools
import warnings
from dataclasses import dataclass
from typing import List, Optional, Tuple

import numpy as np

from numerical.params import ModelParams, Cutoffs
from numerical.solver import solve_equilibrium, equilibrium_residual
from numerical.model import (
    compute_action_probabilities,
    compute_equilibrium_prices,
    compute_minority_gains,
    compute_minority_gains_no_disclosure_given_strategy,
    bid_probability,
    noise_probs,
)

# [Full implementation in recalibrate.py - parameter grid:]
# lambda_B_grid = [0.10, 0.15, 0.20, 0.30]
# C0_grid = [0.15, 0.20, 0.25, 0.30, 0.40]
# S_bar_grid = [0.60, 0.80, 1.00, 1.20]
# s_xi_grid = [0.10, 0.15, 0.20, 0.30]
# Delta_S_grid = [0.20, 0.35]
# Total: 640 combinations
#
# Result: 0 configurations achieved hump + hold + disclosure simultaneously
```

## Makefile

```makefile
# Build pipeline
all: data figures

data:
	python -m numerical.export_data --output-dir numerical_output

figures:
	Rscript R/render_all.R --data-dir numerical_output/data --output-dir numerical_output

clean:
	rm -f numerical_output/data/*.csv numerical_output/*.pdf
```
