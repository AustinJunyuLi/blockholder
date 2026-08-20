"""Assert-based self-checks for the ticket-09 parser fixes.

No framework: run directly (or ``python -m empirics.test_parse_13d``).
Each check fails on the pre-fix behaviour and passes on the fix.
"""

from __future__ import annotations

import datetime as dt
import os
import tempfile

from empirics.edgar_fetch import list_filings
from empirics.parse_13d import parse_event_date, parse_filing, parse_percent_of_class

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


_IDX_HEADER = (
    "Form Type   Company Name                                                  "
    "CIK         Date Filed  File Name\n"
    "---------------------------------------------------------------------------"
    "--------------------------------------------------------------\n"
)
_IDX_BODY = (
    "SC 13D           Old Corp                                                       "
    "1111111     2024-01-15  edgar/data/1111111/0001111111-24-000001.txt\n"
    "SCHEDULE 13D     New Corp                                                       "
    "2222222     2025-01-06  edgar/data/2222222/0002222222-25-000002.txt\n"
    "SCHEDULE 13D/A   Amend Corp                                                     "
    "3333333     2025-01-07  edgar/data/3333333/0003333333-25-000003.txt\n"
)


def _write_idx(tmpdir: str) -> str:
    path = os.path.join(tmpdir, "form_test.idx")
    with open(path, "w", encoding="latin-1") as fh:
        fh.write(_IDX_HEADER + _IDX_BODY)
    return path


def check_form_idx_accepts_schedule_13d_rename():
    # bug: EDGAR renamed "SC 13D" -> "SCHEDULE 13D" around 2024Q3; the old
    # default form_types=("SC 13D", "SC 13G") missed the new spelling
    # entirely, so 2025 filings would return zero rows.
    with tempfile.TemporaryDirectory() as tmp:
        path = _write_idx(tmp)
        rows = list_filings(path)
    forms = sorted(r["form"] for r in rows)
    assert forms == ["SC 13D", "SCHEDULE 13D"], f"expected both spellings, got {forms}"


def check_form_idx_amendment_not_truncated():
    # bug: the form-type column was sliced with a hard line[:12], but
    # "SCHEDULE 13D/A" is 14 chars -- it got truncated to "SCHEDULE 13D",
    # so requesting the amendment form explicitly returned zero rows (and,
    # worse, would have been silently miscounted as an original filing).
    with tempfile.TemporaryDirectory() as tmp:
        path = _write_idx(tmp)
        rows = list_filings(path, form_types=("SCHEDULE 13D/A",))
    assert len(rows) == 1, f"expected 1 amendment row, got {len(rows)}"
    assert rows[0]["form"] == "SCHEDULE 13D/A", rows[0]["form"]
    assert rows[0]["company"] == "Amend Corp", rows[0]["company"]


def check_percent_xml_2025():
    # bug: percent-of-class had no structured-XML path, so post-2024-12-18
    # filings (which carry <percentOfClass> instead of a free-text label)
    # parsed to None. Real filing 0001398344-25-000246: 5.17 / 4.86 -> max 5.17.
    text = (
        "<reportingPerson><percentOfClass>5.17</percentOfClass></reportingPerson>"
        "<reportingPerson><percentOfClass>4.86</percentOfClass></reportingPerson>"
    )
    got = parse_percent_of_class(text)
    assert got == 5.17, f"expected 5.17, got {got}"


def check_percent_discards_impossible_values():
    # >100% cannot be a real ownership stake; guard the max-across-persons
    # logic against stray boilerplate numbers that slip past the regex.
    text = "<percentOfClass>250.0</percentOfClass><percentOfClass>6.1</percentOfClass>"
    got = parse_percent_of_class(text)
    assert got == 6.1, f"expected 6.1 (250.0 discarded as noise), got {got}"


def check_event_date_label_split_across_tags():
    # bug found during hand-audit (filing 918251/0001214659-23-008382): the
    # cover-page label is split across HTML tags --
    # "...Requires</P>\n<P ...>Filing of this Statement)..." -- so the
    # label regex (which expects plain whitespace between words) never
    # matches and the event date parses to None even though "May 18, 2023"
    # is right there on the page.
    text = (
        '<TR><TD STYLE="border-bottom: Black 1pt solid"> '
        '<FONT><B>May 18, 2023</B></FONT> </TD></TR>'
        '<TR><TD><P STYLE="text-align: center">(Date of Event which Requires</P>'
        '<P STYLE="text-align: center">Filing of this Statement)</P></TD></TR>'
    )
    got = parse_event_date(text)
    assert got == dt.date(2023, 5, 18), f"expected 2023-05-18, got {got}"


def check_list_filings_explicit_form_types_get_rename_alias():
    # bug: facts.py calls list_filings(idx_path, form_types=("SC 13D",))
    # explicitly -- that overrides the alias-aware default, so post-rename
    # "SCHEDULE 13D" rows are silently dropped even though the caller
    # plainly wants 13D originals (2024Q3: 18, 2024Q4: 114 missed filings).
    with tempfile.TemporaryDirectory() as tmp:
        path = _write_idx(tmp)
        rows = list_filings(path, form_types=("SC 13D",))
    forms = sorted(r["form"] for r in rows)
    assert forms == ["SC 13D", "SCHEDULE 13D"], (
        f"expected explicit ('SC 13D',) to also match the renamed spelling, got {forms}")


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
        check_form_idx_accepts_schedule_13d_rename,
        check_form_idx_amendment_not_truncated,
        check_percent_xml_2025,
        check_percent_discards_impossible_values,
        check_event_date_label_split_across_tags,
        check_list_filings_explicit_form_types_get_rename_alias,
    ]
    for c in checks:
        c()
        print(f"PASS {c.__name__}")
    print(f"\n{len(checks)}/{len(checks)} checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
