"""
Exit-Voice-Takeover Model: Numerical Analysis Package.

Modules
-------
params       -- Model parameters, Action enum, Cutoffs/MinorityGains types
model        -- Core economic functions (posteriors, prices, payoffs)
solver       -- Equilibrium solver and comparative statics
export_data  -- CSV data export and LaTeX table generation
"""

from numerical.params import Action, Cutoffs, MinorityGains, ModelParams
from numerical.solver import solve_equilibrium, solve_valid, compute_series_over_kappa
from numerical.export_data import export_all

__all__ = [
    "Action",
    "Cutoffs",
    "MinorityGains",
    "ModelParams",
    "solve_equilibrium",
    "solve_valid",
    "compute_series_over_kappa",
    "export_all",
]
