"""Numerical package for "Liquidity, Activism Disclosure, and Takeover Premia".

The public surface area is intentionally small. Most users should run:

    python -m numerical.export_data --output-dir numerical_output
    python -m numerical.figures     --output-dir numerical_output

or simply:

    make clean && make all
"""

from .params import ModelParams, Cutoffs, MinorityGains, Action
from .solver import solve_valid, solve_equilibrium
from .model import compute_minority_gains

__all__ = [
    "ModelParams",
    "Cutoffs",
    "MinorityGains",
    "Action",
    "solve_valid",
    "solve_equilibrium",
    "compute_minority_gains",
]
