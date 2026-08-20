"""Assert-based self-checks for the ticket-09 parser fixes.

No framework: run directly (or ``python -m empirics.test_parse_13d``).
Each check fails on the pre-fix behaviour and passes on the fix.
"""

from __future__ import annotations

import datetime as dt

from empirics.parse_13d import parse_event_date, parse_filing

# minimal fake header so parse_filing() doesn't choke on missing fields
_HEADER = "ACCESSION NUMBER: 0001-25-000001\nFILED AS OF DATE: 20250106\n"


def check_percent_three_digit():
    # bug: RE_PERCENT capped at 2 digits, so "100.0%" parsed as "00.0" -> 0.0
    text = _HEADER + "PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW (11)\n100.0%"
    got = parse_filing(text)["pct_of_class"]
    assert got == 100.0, f"expected 100.0, got {got}"


def check_percent_multi_person_takes_max():
    # bug: .search() took the FIRST label match, which can be a minor joint
    # filer's stake rather than the group's largest disclosed stake.
    text = _HEADER + (
        "PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW (11)\n1.4%\n"
        "... more cover page ...\n"
        "PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW (11)\n7.2%"
    )
    got = parse_filing(text)["pct_of_class"]
    assert got == 7.2, f"expected max 7.2, got {got}"


def check_percent_ignores_css_noise():
    # bug found during hand-audit (filing 1909747/0001628280-23-031213):
    # HTML cover pages put "line-height:120%" (CSS) between the label and
    # the real number; naive digits-then-% matching grabs the CSS value.
    text = _HEADER + (
        'PERCENT OF CLASS REPRESENTED BY AMOUNT IN ROW (11)</font></div>'
        '<div><font style="line-height:120%">&#160;</font></div>'
        '<div><font style="line-height:120%">3.24% (6)</font></div>'
    )
    got = parse_filing(text)["pct_of_class"]
    assert got == 3.24, f"expected 3.24 (real value, not CSS 120), got {got}"


def check_event_date_xml_2025():
    # bug: XML_EVENT looked for <eventDateRequiresFilingThisStatement>, but
    # the real SEC schema (mandatory from 2024-12-18) uses <dateOfEvent>.
    text = (
        '<edgarSubmission><formData><coverPageHeader>'
        '<securitiesClassTitle>Common Stock</securitiesClassTitle>'
        '<dateOfEvent>01/02/2025</dateOfEvent>'
        '</coverPageHeader></formData></edgarSubmission>'
    )
    got = parse_event_date(text)
    assert got == dt.date(2025, 1, 2), f"expected 2025-01-02, got {got}"


def check_business_delay_skips_holidays():
    # bug: np.busday_count with no holidays= counts MLK Day (2024-01-15,
    # a Monday) as a business day, undercounting the delay by 1.
    from empirics.facts import business_delay
    # 2024-01-12 (Fri) -> 2024-01-16 (Tue): weekdays between = Mon 1/15 (MLK) + Tue 1/16 = 2
    # but MLK is a federal holiday, so only Tue 1/16 is a real business day = 1
    got = business_delay(dt.date(2024, 1, 12), dt.date(2024, 1, 16))
    assert got == 1.0, f"expected 1.0 (MLK Day excluded), got {got}"


def main() -> int:
    checks = [
        check_percent_three_digit,
        check_percent_multi_person_takes_max,
        check_percent_ignores_css_noise,
        check_event_date_xml_2025,
        check_business_delay_skips_holidays,
    ]
    for c in checks:
        c()
        print(f"PASS {c.__name__}")
    print(f"\n{len(checks)}/{len(checks)} checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
