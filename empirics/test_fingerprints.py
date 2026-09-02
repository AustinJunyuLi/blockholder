"""Gate checks, the number guard, and hand-dated unit checks for fingerprints.

Usage:
    PYTHONPATH=. .venv/bin/python -m empirics.test_fingerprints
"""

from __future__ import annotations

import datetime as dt
import json
import os
import unittest

import numpy as np
import pandas as pd

from empirics import fingerprints as fp

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(REPO, "paper.tex")


def _load(exercise: str) -> dict | None:
    return fp.load_result(exercise)


# ---------------------------------------------------------------------------
# Hand-dated unit checks: the reaction-day rule
# ---------------------------------------------------------------------------

class ReactionDayTest(unittest.TestCase):
    """Three hand-dated cases against the registered 16:00 rule."""

    # A trading calendar covering the three cases, hand-written: the
    # US sessions of 2024-01-11 through 2024-01-19, with 2024-01-15 (Martin
    # Luther King Jr. Day) closed.
    CALENDAR = np.array(
        ["2024-01-11", "2024-01-12", "2024-01-16", "2024-01-17",
         "2024-01-18", "2024-01-19"], dtype="datetime64[D]")

    def test_before_cutoff_is_same_day(self):
        # Accepted 15:59 on Thursday 2024-01-11: the filing can move the price
        # the same session.
        got = fp.reaction_day(dt.date(2024, 1, 11),
                              dt.datetime(2024, 1, 11, 15, 59, 0),
                              self.CALENDAR)
        self.assertEqual(got, dt.date(2024, 1, 11))

    def test_exactly_at_cutoff_rolls_forward(self):
        # Accepted 16:00:00 on Thursday 2024-01-11: "before 16:00" fails, so
        # the reaction day is the next session, Friday 2024-01-12.
        got = fp.reaction_day(dt.date(2024, 1, 11),
                              dt.datetime(2024, 1, 11, 16, 0, 0),
                              self.CALENDAR)
        self.assertEqual(got, dt.date(2024, 1, 12))

    def test_after_cutoff_on_friday_skips_the_holiday_weekend(self):
        # Accepted 16:30 on Friday 2024-01-12: the next session is Tuesday
        # 2024-01-16, because Monday 2024-01-15 is a market holiday.
        got = fp.reaction_day(dt.date(2024, 1, 12),
                              dt.datetime(2024, 1, 12, 16, 30, 0),
                              self.CALENDAR)
        self.assertEqual(got, dt.date(2024, 1, 16))


# ---------------------------------------------------------------------------
# Hand-dated unit checks: the delay rule
# ---------------------------------------------------------------------------

class DelayTest(unittest.TestCase):
    """Three hand-dated cases against the registered business-day count."""

    def test_weekend_and_holiday_are_skipped(self):
        # Trigger Friday 2024-01-12, filed Tuesday 2024-01-16. The count is
        # half-open: Friday counts, the weekend does not, and Monday
        # 2024-01-15 is Martin Luther King Jr. Day.
        self.assertEqual(
            fp.business_delay(dt.date(2024, 1, 12), dt.date(2024, 1, 16)), 1)

    def test_endpoint_is_the_filing_date_not_the_reaction_day(self):
        # Trigger Wednesday 2023-06-07, filed Wednesday 2023-06-14: five
        # business days, whatever the acceptance time would do to a reaction
        # day. The built table must use the same endpoint on every row.
        self.assertEqual(
            fp.business_delay(dt.date(2023, 6, 7), dt.date(2023, 6, 14)), 5)
        path = os.path.join(fp.OUT_DIR, "campaigns.csv")
        if not os.path.exists(path):
            self.skipTest("campaigns.csv not built yet")
        table = pd.read_csv(path)
        expected = [fp.business_delay(dt.date.fromisoformat(str(t)),
                                      dt.date.fromisoformat(str(f)))
                    for t, f in zip(table["trigger_date"], table["date_filed"])]
        self.assertEqual(table["delay_bdays"].tolist(), expected)

    def test_negative_delay_is_kept(self):
        # Trigger Monday 2022-03-14, filed the previous Thursday 2022-03-10.
        # A filing dated before its own trigger is counted, not screened.
        self.assertEqual(
            fp.business_delay(dt.date(2022, 3, 14), dt.date(2022, 3, 10)), -2)


# ---------------------------------------------------------------------------
# Measurement helpers
# ---------------------------------------------------------------------------

class ParserTest(unittest.TestCase):

    def test_stake_support_is_open_at_zero(self):
        self.assertEqual(
            fp.parse_stake("PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW 9: 0.0%"),
            (None, None))

    def test_stake_takes_the_max_across_reporting_persons(self):
        text = ("PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW 9: 4.1% "
                "PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW 9: 7.6%")
        value, route = fp.parse_stake(text)
        self.assertAlmostEqual(value, 7.6)
        self.assertEqual(route, "cover")

    def test_cusip_from_structured_xml(self):
        cusip, route, n = fp.parse_cusip("<issuerCUSIP>92942W107</issuerCUSIP>")
        self.assertEqual((cusip, route), ("92942W10", "xml"))

    def test_cusip_from_the_cover_page_with_internal_spaces(self):
        text = "Common Stock (Title of Class) 759141 104 (CUSIP Number) John Doe"
        cusip, route, n = fp.parse_cusip(text)
        self.assertEqual((cusip, route), ("75914110", "cover"))

    def test_bootstrap_is_deterministic(self):
        a = np.arange(50, dtype=float)
        b = np.arange(50, dtype=float) + 3.0
        first = fp.bootstrap_difference(a, b, np.mean, n_boot=200)
        second = fp.bootstrap_difference(a, b, np.mean, n_boot=200)
        self.assertEqual(first, second)


# ---------------------------------------------------------------------------
# Gate checks against the result files
# ---------------------------------------------------------------------------

class E1GateTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result = _load("e1")
        path = os.path.join(fp.OUT_DIR, "e1_campaigns.csv")
        cls.sample = pd.read_csv(path) if os.path.exists(path) else None

    def setUp(self):
        if self.result is None:
            self.skipTest("e1_estimate.json not written yet")

    def test_g1_recomputed_from_the_campaign_table(self):
        gate = self.result["gates"]["E1-G1_parse_coverage"]
        cov = self.result["coverage"]
        self.assertAlmostEqual(
            gate["share_with_stake"],
            cov["stake_readable"] / cov["campaigns"], places=12)
        self.assertEqual(gate["verdict"],
                         "PASS" if gate["share_with_stake"] >= fp.E1_G1_MIN_COVERAGE
                         else "NO-GO")

    def test_g3_gap_matches_its_two_shares(self):
        gate = self.result["gates"]["E1-G3_differential_coverage"]
        self.assertAlmostEqual(
            gate["absolute_gap"],
            abs(gate["share_with_stake_pre"] - gate["share_with_stake_post"]),
            places=12)
        self.assertEqual(gate["verdict"],
                         "PASS" if gate["absolute_gap"] <= fp.E1_G3_MAX_GAP
                         else "NO-GO")

    def test_g2_is_left_for_the_independent_audit(self):
        gate = self.result["gates"]["E1-G2_blind_audit"]
        # Before the audit the verdict is NOT RUN; the audit may write PASS.
        self.assertIn(gate["verdict"], ("NOT RUN", "PASS"))
        if gate["verdict"] == "PASS":
            # A PASS only the audit could have written: the runner's G2 block
            # carries no provenance, so these keys cannot come from it.
            for key in ("audit_file", "read_by", "n_audited", "seed"):
                self.assertIn(key, gate)
        # The runner itself leaves G2 to the audit, on any input it accepts.
        probe = fp.e1_gates(pd.DataFrame({"stake": [1.0], "period": ["pre"]}))
        self.assertEqual(probe["E1-G2_blind_audit"]["verdict"], "NOT RUN")

    def test_status_follows_the_gate_verdicts(self):
        verdicts = [g["verdict"] for g in self.result["gates"].values()]
        expected = ("NO-GO" if "NO-GO" in verdicts
                    else ("PENDING" if "NOT RUN" in verdicts else "GO"))
        self.assertEqual(self.result["status"], expected)
        self.assertEqual(self.result["headline_suppressed"],
                         self.result["status"] == "NO-GO")

    def test_sample_respects_the_registered_support(self):
        if self.sample is None:
            self.skipTest("e1_campaigns.csv not written yet")
        stake = self.sample["stake"].to_numpy(dtype=float)
        self.assertTrue(np.all(stake > fp.STAKE_LOW))
        self.assertTrue(np.all(stake <= fp.STAKE_HIGH))

    def test_campaign_unit_is_unique(self):
        if self.sample is None:
            self.skipTest("e1_campaigns.csv not written yet")
        pairs = self.sample[["subject_cik", "trigger_date"]]
        self.assertEqual(len(pairs), len(pairs.drop_duplicates()))

    def test_the_design_is_declared_descriptive(self):
        self.assertFalse(self.result["causal_claim"])
        self.assertEqual(self.result["design"], "descriptive")
        self.assertEqual(self.result["spec"], fp.SPEC)

    def test_clock_block_is_present(self):
        clock = self.result["clock"]
        self.assertEqual(clock["within_bdays"], fp.WITHIN_BDAYS)
        for period in ("pre", "post"):
            self.assertIn("share_within_5bd", clock["by_period"][period])
            self.assertIn("median_delay_bdays", clock["by_period"][period])


class E2GateTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.result = _load("e2")

    def setUp(self):
        if self.result is None:
            self.skipTest("e2_estimate.json not written yet")

    def test_g1_share_matches_its_counts(self):
        gate = self.result["gates"]["E2-G1_link_coverage"]
        if not gate["listed_campaigns"]:
            self.skipTest("no listed campaigns")
        self.assertAlmostEqual(
            gate["share"], gate["listed_linked"] / gate["listed_campaigns"],
            places=12)

    def test_g3_smallest_cell(self):
        gate = self.result["gates"]["E2-G3_cell_size"]
        self.assertEqual(gate["smallest"], min(gate["cells"].values()))

    def test_g4_gap_matches_its_two_shares(self):
        gate = self.result["gates"]["E2-G4_differential_coverage"]
        self.assertAlmostEqual(
            gate["absolute_gap"],
            abs(gate["link_share_pre"] - gate["link_share_post"]), places=12)

    def test_g2_is_left_for_the_independent_audit(self):
        gate = self.result["gates"]["E2-G2_link_audit"]
        self.assertIn(gate["verdict"], ("NOT RUN", "PASS"))
        if gate["verdict"] == "PASS":
            for key in ("audit_file", "read_by", "n_audited", "seed"):
                self.assertIn(key, gate)
        probe = fp.e2_gates(0, 0, 0, 0, {}, float("nan"), float("nan"))
        self.assertEqual(probe["E2-G2_link_audit"]["verdict"], "NOT RUN")

    def test_status_follows_the_gate_verdicts(self):
        verdicts = [g["verdict"] for g in self.result["gates"].values()]
        expected = ("NO-GO" if "NO-GO" in verdicts
                    else ("PENDING" if "NOT RUN" in verdicts else "GO"))
        self.assertEqual(self.result["status"], expected)


# ---------------------------------------------------------------------------
# The number guard
# ---------------------------------------------------------------------------

class NumberGuardTest(unittest.TestCase):
    """Every rendered manuscript number appears in paper.tex."""

    def setUp(self):
        if not os.path.exists(PAPER):
            self.skipTest("paper.tex does not exist yet")
        with open(PAPER, encoding="utf-8") as fh:
            self.paper = fh.read()

    def _guard(self, exercise: str) -> None:
        result = _load(exercise)
        if result is None:
            self.skipTest(f"{exercise}_estimate.json not written yet")
        rendered = fp.render(exercise)
        if result["status"] == "NO-GO":
            self.assertEqual(rendered, {},
                             "a NO-GO exercise renders no number")
            return
        missing = sorted(k for k, v in rendered.items()
                         if v and v not in self.paper)
        self.assertEqual(missing, [],
                         f"{exercise} numbers absent from paper.tex: {missing}")

    def test_e1_numbers_are_in_the_paper(self):
        self._guard("e1")

    def test_e2_numbers_are_in_the_paper(self):
        self._guard("e2")


if __name__ == "__main__":
    unittest.main(verbosity=2)
