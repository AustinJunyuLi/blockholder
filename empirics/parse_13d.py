"""Parse Schedule 13D/13G submissions: event date, filing date, ownership.

The object of interest for Fact 1 is the disclosure delay
    delay = (date filed) - (date of event which requires filing),
in business days. Pre-Feb-5-2024 the 13D deadline was 10 calendar days;
after, 5 business days (SEC release 33-11253; structured XML mandatory for
filings from Dec 18, 2024).

Two parsing paths:
  * structured XML (post Dec-2024): <eventDateRequiresFilingThisStatement>
  * cover-page regex (any era): the date adjacent to the label
    "(Date of Event Which Requires Filing of this Statement)"
plus header fields (FILED AS OF DATE, ACCESSION NUMBER, SUBJECT COMPANY /
FILED BY blocks) and a best-effort percent-of-class extraction.
"""

from __future__ import annotations

import datetime as dt
import re
from typing import Optional

# -- header fields -----------------------------------------------------------

RE_ACCESSION = re.compile(r"ACCESSION NUMBER:\s*(\S+)")
RE_FILED_DATE = re.compile(r"FILED AS OF DATE:\s*(\d{8})")
RE_SUBJECT_CIK = re.compile(
    r"SUBJECT COMPANY:.*?CENTRAL INDEX KEY:\s*(\d+)", re.S)
RE_FILER_CIK = re.compile(
    r"FILED BY:.*?CENTRAL INDEX KEY:\s*(\d+)", re.S)

# -- event date --------------------------------------------------------------

EVENT_LABEL = re.compile(
    r"\(?\s*Date\s+of\s+Event\s+Which\s+Requires\s+Filing\s+of\s+(?:this|the)\s+Statement\s*\)?",
    re.I)
XML_EVENT = re.compile(
    r"<dateOfEvent>\s*(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\s*"
    r"</dateOfEvent>", re.I)

MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"])}

DATE_PATTERNS = [
    # December 18, 2024 / Dec. 18, 2024
    re.compile(r"([A-Za-z]{3,9})\.?\s+(\d{1,2})\s*,?\s+(\d{4})"),
    # 12/18/2024 or 12-18-2024
    re.compile(r"(\d{1,2})[/-](\d{1,2})[/-](\d{4})"),
    # 2024-12-18
    re.compile(r"(\d{4})-(\d{2})-(\d{2})"),
]


def _to_date(m: re.Match, pattern_idx: int) -> Optional[dt.date]:
    try:
        if pattern_idx == 0:
            month = MONTHS.get(m.group(1).lower().rstrip("."))
            if month is None:
                month = MONTHS.get(next(
                    (k for k in MONTHS if k.startswith(m.group(1).lower()[:3])), ""), None)
            if month is None:
                return None
            return dt.date(int(m.group(3)), month, int(m.group(2)))
        if pattern_idx == 1:
            return dt.date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def parse_event_date(text: str) -> Optional[dt.date]:
    """Event date from XML tag if present, else from the cover-page label."""
    xm = XML_EVENT.search(text)
    if xm:
        raw = xm.group(1)
        for idx in (1, 2):
            m = DATE_PATTERNS[idx].search(raw)
            if m:
                d = _to_date(m, idx)
                if d:
                    return d
    lab = EVENT_LABEL.search(text)
    if not lab:
        return None
    # the date is printed adjacent to the label -- search a window BEFORE the
    # label first (standard cover-page layout), then after.
    for window in (text[max(0, lab.start() - 400):lab.start()],
                   text[lab.end():lab.end() + 400]):
        candidates = []
        for idx, pat in enumerate(DATE_PATTERNS):
            for m in pat.finditer(window):
                d = _to_date(m, idx)
                if d and 1990 <= d.year <= 2030:
                    candidates.append((m.start(), d))
        if candidates:
            # nearest to the label: last match in the before-window
            return candidates[-1][1]
    return None


RE_PERCENT = re.compile(
    r"PERCENT\s+OF\s+CLASS\s+REPRESENTED.*?([0-9]{1,3}(?:\.[0-9]+)?)\s*%", re.I | re.S)
RE_TAG = re.compile(r"<[^>]+>")


def parse_percent_of_class(text: str) -> Optional[float]:
    """Percent of class from the cover page.

    A 13D cover page repeats the "PERCENT OF CLASS REPRESENTED" block once
    per reporting person (joint filers each report their own row-11 value,
    which can differ). Take the max across all matches -- the group's
    largest disclosed stake -- rather than the first, which may belong to a
    minor joint filer.

    Many filings are HTML cover pages where the label is immediately
    followed by ``<font style="...line-height:120%">`` before the real
    number; without stripping tags first, the CSS percentage itself gets
    matched as if it were the ownership stake. Strip tags before matching.
    """
    plain = RE_TAG.sub(" ", text)
    vals = []
    for raw in RE_PERCENT.findall(plain):
        try:
            vals.append(float(raw))
        except ValueError:
            continue
    return max(vals) if vals else None


def parse_filing(text: str) -> dict:
    """Extract the Fact-1 fields from one master submission text."""
    out: dict = {}
    m = RE_ACCESSION.search(text)
    out["accession"] = m.group(1) if m else None
    m = RE_FILED_DATE.search(text)
    out["filed"] = (dt.datetime.strptime(m.group(1), "%Y%m%d").date()
                    if m else None)
    m = RE_SUBJECT_CIK.search(text)
    out["subject_cik"] = m.group(1) if m else None
    m = RE_FILER_CIK.search(text)
    out["filer_cik"] = m.group(1) if m else None
    out["event"] = parse_event_date(text)
    out["pct_of_class"] = parse_percent_of_class(text)
    out["has_xml"] = bool(XML_EVENT.search(text))
    return out
