"""
Model parameters and type definitions for the Exit-Voice-Takeover model.

This is the foundational module — all other modules in the numerical package
import from here. It defines:

- Named tolerance constants used across the solver and equilibrium routines
- The ``Action`` enum encoding the blockholder's four action choices
- ``Cutoffs`` and ``MinorityGains`` named tuples for structured return values
- The ``ModelParams`` dataclass with baseline calibration and derived quantities
"""

from __future__ import annotations

import dataclasses
import enum
from dataclasses import dataclass
from typing import NamedTuple

import numpy as np
from scipy.stats import norm

# ---------------------------------------------------------------------------
# Tolerance constants
# ---------------------------------------------------------------------------

TOL_PROB: float = 1e-10        # Near-zero probability threshold
TOL_CONVERGE: float = 1e-6    # Fixed-point convergence criterion
TOL_RESIDUAL: float = 5e-3    # Equilibrium quality gate
TOL_REGION: float = 1e-4      # Cutoff region collapse detection


# ---------------------------------------------------------------------------
# Action enum
# ---------------------------------------------------------------------------

class Action(enum.Enum):
    """Blockholder action choice (Definition 2 in the paper).

    EXIT   -- Sell stake  (q = -1, a = 0)
    HOLD   -- Passive hold (q = 0,  a = 0)
    QUIET  -- Quiet Voice: engage below disclosure threshold (q = 0,  a = 1)
    PUBLIC -- Public Voice: buy, engage, trigger disclosure  (q = +1, a = 1)
    """

    EXIT = "E"
    HOLD = "H"
    QUIET = "Q"
    PUBLIC = "P"


# ---------------------------------------------------------------------------
# Named tuples
# ---------------------------------------------------------------------------

class Cutoffs(NamedTuple):
    """Equilibrium signal cutoffs (Proposition 1).

    k1: Exit/Hold boundary -- signals below k1 trigger exit
    k0: Hold/Quiet Voice boundary -- signals above k0 trigger engagement
    kD: Quiet/Public Voice boundary -- signals above kD trigger disclosure

    Satisfies k1 <= k0 <= kD (weak ordering allows region collapse).
    """

    k1: float
    k0: float
    kD: float


class MinorityGains(NamedTuple):
    """Expected minority takeover gains decomposition (Section 5).

    total: Total expected minority gains Delta^min
    base:  Base component m0 * Pr(bid)
    activism: Activism-driven component Delta^act
    """

    total: float
    base: float
    activism: float


# ---------------------------------------------------------------------------
# Model parameters
# ---------------------------------------------------------------------------

@dataclass
class ModelParams:
    """Parameters for the Exit-Voice-Takeover model.

    Notation follows the paper:

        mu, sigma_v     -- Prior: v ~ N(mu, sigma_v^2)              [Section 2.1]
        sigma_eps       -- Signal noise: s = v + eps                 [Eq. 1]
        kappa           -- Noise trading intensity                   [Definition 1]
        C0, chi         -- Engagement cost: C(s) = C0*exp(-chi*z)   [Eq. 3]
        rho, Delta      -- Success probability and value improvement [Eq. 4]
        m0, m1          -- Takeover premia without/with engagement   [Eq. 5]
        S_bar, K        -- Baseline synergy and bidding cost         [Eq. 8]
        sigma_xi        -- Synergy shock volatility                  [Eq. 8]
        delta           -- Discount factor                           [Eq. 6]

    Default values correspond to the baseline calibration used throughout
    the paper.
    """

    # Fundamentals
    mu: float = 1.0                # Prior mean of v
    sigma_v: float = 0.5           # Std dev of v
    sigma_eps: float = 0.5         # Std dev of signal noise

    # Liquidity
    kappa: float = 0.5             # Noise trading intensity

    # Engagement
    C0: float = 0.12              # Base engagement cost
    chi: float = 0.5              # Cost sensitivity to signal
    rho: float = 0.9              # Engagement success probability
    Delta: float = 0.25           # Value improvement from engagement

    # Takeover
    m0: float = 0.10              # Base takeover premium
    m1: float = 0.30              # Premium with successful engagement
    S_bar: float = 1.44           # Baseline synergy
    K: float = 0.15               # Bidding cost
    sigma_xi: float = 0.40        # Synergy shock volatility

    # Discounting
    delta: float = 0.95           # Discount factor

    # -- Derived quantities ------------------------------------------------

    @property
    def sigma_s(self) -> float:
        """Signal standard deviation: sqrt(sigma_v^2 + sigma_eps^2)."""
        return np.sqrt(self.sigma_v**2 + self.sigma_eps**2)

    @property
    def beta(self) -> float:
        """Posterior weight on the signal in v_hat(s).

        beta = sigma_v^2 / (sigma_v^2 + sigma_eps^2)
        """
        return self.sigma_v**2 / (self.sigma_v**2 + self.sigma_eps**2)

    @property
    def m_tilde(self) -> float:
        """Expected takeover premium under engagement.

        m_tilde = m0 + rho * (m1 - m0)
        """
        return self.m0 + self.rho * (self.m1 - self.m0)

    @property
    def Delta_tilde(self) -> float:
        """Expected value improvement under engagement.

        Delta_tilde = rho * Delta
        """
        return self.rho * self.Delta

    # -- Convenience methods -----------------------------------------------

    def replace(self, **kwargs) -> ModelParams:
        """Return a copy with specified fields overridden."""
        return dataclasses.replace(self, **kwargs)

    @classmethod
    def baseline(cls) -> ModelParams:
        """Baseline calibration used in the paper."""
        return cls()
