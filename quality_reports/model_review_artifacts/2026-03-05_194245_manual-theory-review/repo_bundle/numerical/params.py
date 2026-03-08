"""Parameter and type definitions for the numerical exercise.

Notation matches `draft_v3.tex`.

Key objects:
- Action set: Exit, Hold, Quiet Voice, Public Voice
- Cutoffs: (k1, k0, kD)
- ModelParams: baseline calibration + derived quantities
"""

from __future__ import annotations

import dataclasses
import enum
from dataclasses import dataclass
from typing import NamedTuple

import numpy as np

# -----------------------------------------------------------------------------
# Numerical tolerances
# -----------------------------------------------------------------------------

TOL_PROB: float = 1e-12        # treat probabilities below as 0
TOL_CONVERGE: float = 1e-7     # fixed-point cutoff convergence
TOL_RESIDUAL: float = 5e-3     # acceptable max cutoff indifference residual
TOL_REGION: float = 1e-5       # treat regions narrower than this as collapsed

# Integration / grids
SIGMA_GRID: float = 6.0        # integrate over s in [mu-6*sigma_s, mu+6*sigma_s]


# -----------------------------------------------------------------------------
# Actions
# -----------------------------------------------------------------------------

class Action(enum.Enum):
    """Blockholder action.

    EXIT   : (q=-1, a=0)
    HOLD   : (q=0,  a=0)
    QUIET  : (q=0,  a=1)
    PUBLIC : (q=+1, a=1)  (stake-triggered disclosure)
    """

    EXIT = "E"
    HOLD = "H"
    QUIET = "Q"
    PUBLIC = "P"


class Cutoffs(NamedTuple):
    """Equilibrium cutoffs (k1, k0, kD) with weak ordering k1 <= k0 <= kD."""

    k1: float
    k0: float
    kD: float


class MinorityGains(NamedTuple):
    """Minority takeover gains decomposition (Eq. (decomp) in the paper)."""

    total: float
    base: float
    activism: float


@dataclass(frozen=True)
class ModelParams:
    """Model parameters.

    Fundamentals:
        v ~ N(mu, sigma_v^2)
        s = v + eps, eps ~ N(0, sigma_eps^2)

    Liquidity:
        z ∈ {-1,0,1} with P(0)=1-2kappa/3, P(±1)=kappa/3

    Engagement:
        C(s) = C0 * exp(-chi * (s-mu)/sigma_s)
        success prob rho; improvement Delta; premium wedge m0→m1

    Takeover:
        bidder arrives with prob lambda_B
        synergy shock xi ~ Logistic(0, s_xi)
        entry depends on inferred engagement π(X,D)

    Discounting:
        delta

    Baseline calibration defaults match the paper.
    """

    # Fundamentals
    mu: float = 1.0
    sigma_v: float = 0.50
    sigma_eps: float = 0.50

    # Liquidity
    kappa: float = 0.50

    # Engagement
    C0: float = 0.25
    chi: float = 0.50
    rho: float = 0.90
    Delta: float = 0.25

    # Takeover terms
    m0: float = 0.10
    m1: float = 0.45
    S_bar: float = 1.10
    Delta_S: float = 0.30
    K: float = 0.15
    s_xi: float = 0.15
    lambda_B: float = 0.20

    # Discount factor
    delta: float = 0.95

    # ------------------------------------------------------------------
    # Derived quantities
    # ------------------------------------------------------------------

    @property
    def sigma_s(self) -> float:
        return float(np.sqrt(self.sigma_v**2 + self.sigma_eps**2))

    @property
    def beta(self) -> float:
        # Posterior weight on signal (E[v|s] = mu + beta(s-mu))
        return float(self.sigma_v**2 / (self.sigma_v**2 + self.sigma_eps**2))

    @property
    def Delta_tilde(self) -> float:
        # Expected fundamental improvement under engagement
        return float(self.rho * self.Delta)

    @property
    def m_tilde(self) -> float:
        # Expected premium wedge under engagement
        return float(self.m0 + self.rho * (self.m1 - self.m0))

    @property
    def net_deterrence(self) -> bool:
        # Assumption (A5): Delta_tilde + m_tilde - m0 > Delta_S
        return (self.Delta_tilde + self.m_tilde - self.m0) > self.Delta_S

    def replace(self, **kwargs) -> "ModelParams":
        return dataclasses.replace(self, **kwargs)
