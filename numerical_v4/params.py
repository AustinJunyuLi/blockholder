"""Parameters, tolerances and grids for the v4 model (design section 11, step 1).

House style follows ``numerical/params.py``: a dataclass with a baseline
calibration, a ``replace`` convenience, derived quantities as properties, and
named tolerance constants at module scope.

CALIBRATION MAP.  Every card section 4.1 primitive that has an analogue in the
frozen draft_v2 calibration takes that value verbatim; the mapping is recorded
field by field below.  The stake primitives have no draft_v2 analogue (draft_v2
counts shares held, h in {0,1,2}, not stake fractions) and are set from the
statutory 13D geometry instead.
"""

from __future__ import annotations

import dataclasses
from dataclasses import dataclass

import numpy as np

# Tolerances reused verbatim from the draft_v2 package (design section 7).
from numerical.params import (  # noqa: F401  (re-exported for the check scripts)
    TOL_CONVERGE,
    TOL_PROB,
    TOL_REGION,
    TOL_RESIDUAL,
)

# ---------------------------------------------------------------------------
# New v4 tolerances (design section 7)
# ---------------------------------------------------------------------------

TOL_IDENTITY: float = 1e-12     # accounting identities: P^F - P_{c-} = R + J
TOL_INVARIANCE: float = 1e-10   # L2: range over kappa of a flagged object


# ---------------------------------------------------------------------------
# Plan indices (design section 2: J = 3 -- Exit, Hold, one Voice family)
# ---------------------------------------------------------------------------

EXIT: int = 1
HOLD: int = 2
VOICE: int = 3
PLANS: tuple[int, int, int] = (EXIT, HOLD, VOICE)


@dataclass
class ParamsV4:
    """Primitives of the v4 model (card section 4.1) plus numerical settings."""

    # -- Fundamentals -------------------------------------------------------
    mu_v: float = 1.0        # ModelParams.mu          (draft_v2 baseline)
    sigma_v: float = 0.5     # ModelParams.sigma_v
    sigma_eps: float = 0.5   # ModelParams.sigma_eps

    # -- Bidder -------------------------------------------------------------
    sigma_xi: float = 0.40   # ModelParams.sigma_xi
    S_bar: float = 1.44      # ModelParams.S_bar
    K: float = 0.15          # ModelParams.K

    # -- Premia -------------------------------------------------------------
    m0: float = 0.10         # ModelParams.m0
    m1: float = 0.30         # ModelParams.m1  (card's m_1 is the premium *with*
    #                          engagement; draft_v2 reaches it only with prob rho,
    #                          so the card's m_1 is draft_v2's m1 taken directly)
    Delta_V: float = 0.225   # ModelParams.Delta_tilde = rho * Delta = 0.9 * 0.25
    #                          (the card has no rho: engagement value is realised)

    # -- Liquidity ----------------------------------------------------------
    kappa: float = 0.5       # ModelParams.kappa
    z_bar: float = 1.0       # one mark unit (design section 4)

    # -- Stake primitives (no draft_v2 analogue; statutory 13D geometry) -----
    b0: float = 0.03         # initial stake, 3% of shares; maintained b0 < tau
    b_bar: float = 0.10      # maximum stake, 10%
    tau: float = 0.05        # seed threshold = the statutory 13D 5%.  The
    #                          reported grid is re-frozen from the baseline
    #                          equilibrium's b*(s) distribution (design 6.2).
    T: int = 5               # filing window, business days
    H: int = 10              # control-decision horizon (design section 3)

    # -- Menu shape (design section 2; pinned here, see menu.py) -------------
    n_scale: float = 4.0     # spread of the accumulation-length map n(s);
    #                          4.0 spreads the Voice types over n = 2..11 and is
    #                          the smallest value at which some flagged type has
    #                          Q^F > 0 at a low tau percentile (see menu.py)
    gamma_bar: float = 1e-6  # Gamma bin edge: Gamma(x) = 1{x >= gamma_bar}

    # -- Engagement cost C_j(s), zero for non-Voice plans --------------------
    # draft_v2's shape C0 * exp(-chi * z), z = (s - mu)/sigma_s.  C0 is rescaled
    # from draft_v2's 0.12: there the payoff carries h in {1,2} whole shares,
    # here it carries a stake fraction b* ~ 0.03-0.10, so the payoff scale is
    # ~1/15th and an unscaled C0 would make Voice unreachable at every signal.
    # 0.014 is the smallest value at which the Hold region stays interior at
    # the frozen tau; below it Voice and Exit meet and Hold collapses.
    C0: float = 0.014
    chi: float = 0.5

    # -- Numerics -----------------------------------------------------------
    n_gl: int = 20           # Gauss-Legendre nodes per s-interval (design 1.4)
    s_span: float = 6.0      # signal support in sigma_s units
    kappa_floor: float = 1e-3   # kappa never takes 0 or 1 (design risk 9.3)

    # -- Derived ------------------------------------------------------------

    @property
    def sigma_s(self) -> float:
        """Signal standard deviation sqrt(sigma_v^2 + sigma_eps^2)."""
        return float(np.sqrt(self.sigma_v**2 + self.sigma_eps**2))

    @property
    def beta(self) -> float:
        """Gaussian projection beta = sigma_v^2 / (sigma_v^2 + sigma_eps^2)."""
        return self.sigma_v**2 / (self.sigma_v**2 + self.sigma_eps**2)

    @property
    def Delta_m(self) -> float:
        """Premium wedge Delta_m = m1 - m0 > 0."""
        return self.m1 - self.m0

    @property
    def n_theta(self) -> int:
        """Number of distinct mark paths: the all-zero path plus H+1 Voice ones."""
        return self.H + 2

    @property
    def n_hist(self) -> int:
        """Order-flow paths: |supp X|^(H+1) with supp X = {-1,0,1,2}."""
        return 4 ** (self.H + 1)

    @property
    def s_lo(self) -> float:
        return self.mu_v - self.s_span * self.sigma_s

    @property
    def s_hi(self) -> float:
        return self.mu_v + self.s_span * self.sigma_s

    # -- Convenience --------------------------------------------------------

    def replace(self, **kwargs) -> "ParamsV4":
        """Return a copy with the named fields overridden."""
        return dataclasses.replace(self, **kwargs)

    @classmethod
    def baseline(cls) -> "ParamsV4":
        return cls()

    def hash_str(self) -> str:
        """Stable digest of the calibration, for JSON provenance."""
        import hashlib
        import json

        payload = json.dumps(dataclasses.asdict(self), sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Ternary noise law (card section 4.1)
# ---------------------------------------------------------------------------

def noise_law(kappa: float) -> tuple[float, float, float]:
    """Pr(z = -z_bar), Pr(z = 0), Pr(z = +z_bar)."""
    return (kappa / 2.0, 1.0 - kappa, kappa / 2.0)


def kappa_grid(n: int = 10, lo: float = 0.05, hi: float = 0.95) -> np.ndarray:
    """Interior kappa grid; never touches 0 or 1 (design risk 9.3)."""
    return np.linspace(lo, hi, n)
