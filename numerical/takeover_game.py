"""
Disagreement-node tender game: the microfounded premium wedge (Appendix D7).

Derives the appropriability coefficient ``lambda`` of the bargaining appendix
(Condition BG) from a complete Grossman-Hart free-rider tender game solved at
the disagreement node, per ``quality_reports/fixes/D7_takeover_game_microfound.tex``:

    lambda = 1 - q * (1 - gamma) * psi      in [0, 1],

where ``q`` is the fringe-raid probability, ``gamma`` the portability of the
activist's improvement under a fringe acquirer, and ``psi`` a pivotality
factor (psi = 1 when the bloc cannot block; psi < 1 when it can).

The premium wedge then follows from the Nash split of Appendix B:

    m1 - m0 = (1 - theta) * lambda * rho * Delta_eng .

This module is *additive*: the body's exogenous (m0, m1) calibration remains
the default everywhere. Endogenous-wedge mode is opt-in via
``params_with_endogenous_wedge``, which maps game primitives into a standard
``ModelParams`` (only ``m1`` changes), so the entire downstream pipeline
(solver, exports, figures) is reused unchanged.

Fringe synergy is S_F = s_min + Exp(mean=mu_S) (closed forms throughout);
fringe entry cost enters only through q = H(phi) (Lemma D7.2: entry is
dilution-financed and state-blind), so q is carried as the primitive.
"""

from __future__ import annotations

import dataclasses
import math
from dataclasses import dataclass

from numerical.params import ModelParams


@dataclass
class TenderGameParams:
    """Primitives of the disagreement-node tender game (Appendix D7).

    Notation follows the derivation record:

        q         -- fringe-raid feasibility probability q = H(phi)   [Lemma D7.2]
        gamma     -- portability of the activist's improvement under
                     a fringe acquirer (1 = complements, 0 = superseded)
        phi       -- charter dilution of non-tendering shareholders
        mu_S      -- mean of the exponential fringe-synergy distribution
        s_min     -- left shift of the fringe-synergy support
        alpha     -- control bloc's stake
        tau_c     -- control threshold (fraction of all shares)
        theta     -- bloc's Nash bargaining weight vs the incumbent bidder
        Delta_eng -- engagement improvement surviving into a sale
    """

    q: float = 0.5
    gamma: float = 0.6
    phi: float = 0.12
    mu_S: float = 0.6
    s_min: float = 0.0
    alpha: float = 0.30
    tau_c: float = 0.75
    theta: float = 0.5
    Delta_eng: float = 0.5159288344168262  # calibrated: wedge = 0.20 at baseline

    # -- Derived quantities ------------------------------------------------

    @property
    def pivotal(self) -> bool:
        """The bloc is pivotal iff the float alone cannot deliver control."""
        return (1.0 - self.alpha) < self.tau_c

    def survival(self, x: float) -> float:
        """Gbar(x) = P(S_F >= x) for S_F = s_min + Exp(mu_S)."""
        if x <= self.s_min:
            return 1.0
        return math.exp(-(x - self.s_min) / self.mu_S)

    @property
    def psi(self) -> float:
        """Pivotality factor: average survival along the forgone-improvement
        interval (Proposition D7.3). Equals 1 in the non-pivotal regime.
        """
        if not self.pivotal:
            return 1.0
        c = (1.0 - self.gamma) * self.Delta_eng
        if c <= 0.0:
            return 1.0  # multiplied by zero in lambda; convention
        a, b = self.phi, self.phi + c
        lo = max(a, self.s_min)
        integral = max(0.0, min(b, self.s_min) - a)  # region where Gbar = 1
        if b > lo:
            integral += self.mu_S * (
                math.exp(-(lo - self.s_min) / self.mu_S)
                - math.exp(-(b - self.s_min) / self.mu_S)
            )
        return integral / c

    @property
    def appropriability(self) -> float:
        """lambda = 1 - q (1 - gamma) psi  in [0, 1]  (Proposition D7.3)."""
        return 1.0 - self.q * (1.0 - self.gamma) * self.psi

    def wedge(self, rho: float) -> float:
        """Microfounded premium wedge m1 - m0 = (1-theta) lambda rho Delta_eng."""
        return (1.0 - self.theta) * self.appropriability * rho * self.Delta_eng

    # -- Convenience methods -----------------------------------------------

    def replace(self, **kwargs) -> TenderGameParams:
        """Return a copy with specified fields overridden."""
        return dataclasses.replace(self, **kwargs)

    @classmethod
    def baseline(cls) -> TenderGameParams:
        """Calibration-consistent baseline: reproduces the body's wedge 0.20
        (and hence m_tilde - m0 = 0.18 at rho = 0.9) with lambda ~ 0.861.
        Verified in quality_reports/fixes/d7_takeover_game_check.py.
        """
        return cls()


def calibrate_delta_eng(
    game: TenderGameParams,
    target_wedge: float,
    rho: float,
    lo: float = 1e-6,
    hi: float = 10.0,
) -> TenderGameParams:
    """Return a copy of ``game`` with Delta_eng bisected so that
    wedge(rho) == target_wedge (lambda depends on Delta_eng in the pivotal
    regime, so the map is solved jointly; it is strictly increasing).
    """
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if game.replace(Delta_eng=mid).wedge(rho) < target_wedge:
            lo = mid
        else:
            hi = mid
    return game.replace(Delta_eng=0.5 * (lo + hi))


def params_with_endogenous_wedge(
    base: ModelParams,
    game: TenderGameParams,
) -> ModelParams:
    """Map tender-game primitives into the body's calibration.

    Only ``m1`` changes: m1 = m0 + (1-theta) lambda rho Delta_eng, with the
    body's own rho applied in the fold (m_tilde recomputes automatically).
    The rest of the pipeline (solver, exports, figures) is reused unchanged.
    """
    return base.replace(m1=base.m0 + game.wedge(base.rho))
