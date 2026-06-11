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
    r"<eventDateRequiresFilingThisStatement>\s*(\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2})\s*"
    r"</eventDateRequiresFilingThisStatement>", re.I)

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
    r"PERCENT\s+OF\s+CLASS\s+REPRESENTED.*?([0-9]{1,2}(?:\.[0-9]+)?)\s*%", re.I | re.S)

# -- entity names (header blocks) --------------------------------------------

RE_SUBJECT_NAME = re.compile(
    r"SUBJECT COMPANY:.*?COMPANY CONFORMED NAME:\s*([^\r\n]+)", re.S)
RE_FILER_NAME = re.compile(
    r"FILED BY:.*?COMPANY CONFORMED NAME:\s*([^\r\n]+)", re.S)

# -- acceptance datetime (after-hours filings hit the tape next session) ------

RE_ACCEPTANCE = re.compile(r"<ACCEPTANCE-DATETIME>\s*(\d{14})")


def parse_acceptance(text: str) -> Optional[dt.datetime]:
    m = RE_ACCEPTANCE.search(text)
    if not m:
        return None
    try:
        return dt.datetime.strptime(m.group(1), "%Y%m%d%H%M%S")
    except ValueError:
        return None


# -- CUSIP (Fact 2: links the subject security to CRSP) -----------------------
#
# Cover pages print the class CUSIP near a "CUSIP No./Number" label, in
# layouts like "037833100", "037833 10 0", or "037833-10-0"; the label often
# repeats once per cover page, so we vote across occurrences. Structured XML
# (mandatory from 2024-12-18) carries an explicit tag.

XML_CUSIP = re.compile(
    r"<(?:issuer)?cusip>\s*([0-9A-Za-z][0-9A-Za-z\s\-]{4,16}[0-9A-Za-z])\s*"
    r"</(?:issuer)?cusip>", re.I)
CUSIP_LABEL = re.compile(r"CUSIP\s*(?:No\.?|Number|NUMBER|#)?", re.I)
CUSIP_TOKEN = re.compile(
    r"\b([0-9A-Z]{6})[\s\-]{0,2}([0-9A-Z]{2})[\s\-]{0,2}([0-9A-Z])?\b")

_CUSIP_CHARVAL = {c: i for i, c in enumerate("0123456789")}
_CUSIP_CHARVAL.update({c: 10 + i for i, c in
                       enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")})
_CUSIP_CHARVAL.update({"*": 36, "@": 37, "#": 38})


def cusip_check_digit_ok(cusip9: str) -> bool:
    """Validate the 9th (check) character of a CUSIP."""
    if len(cusip9) != 9 or cusip9[8] not in "0123456789":
        return False
    total = 0
    for i, ch in enumerate(cusip9[:8]):
        v = _CUSIP_CHARVAL.get(ch)
        if v is None:
            return False
        if i % 2 == 1:
            v *= 2
        total += v // 10 + v % 10
    return (10 - total % 10) % 10 == int(cusip9[8])


def _normalize_cusip(raw: str) -> Optional[str]:
    s = re.sub(r"[\s\-]", "", raw.upper())
    if len(s) not in (8, 9):
        return None
    if sum(ch.isdigit() for ch in s) < 4:      # reject prose tokens
        return None
    if len(set(s)) == 1:                       # reject 000000000-style junk
        return None
    return s


def parse_cusip(text: str) -> Optional[str]:
    """Subject-class CUSIP: XML tag if present, else vote near cover labels.

    Returns 9 characters when a check-digit-valid 9-char CUSIP is found,
    otherwise the best 8/9-char candidate (or None).
    """
    xm = XML_CUSIP.search(text)
    if xm:
        c = _normalize_cusip(xm.group(1))
        if c:
            return c
    votes: dict = {}
    for lab in CUSIP_LABEL.finditer(text):
        for window in (text[max(0, lab.start() - 120):lab.start()],
                       text[lab.end():lab.end() + 120]):
            for m in CUSIP_TOKEN.finditer(window.upper()):
                raw = "".join(g for g in m.groups() if g)
                c = _normalize_cusip(raw)
                if c is None:
                    continue
                weight = 2 if (len(c) == 9 and cusip_check_digit_ok(c)) else 1
                votes[c] = votes.get(c, 0) + weight
    if not votes:
        return None
    # prefer check-valid 9-char candidates, then vote count
    best = max(votes.items(),
               key=lambda kv: (len(kv[0]) == 9 and cusip_check_digit_ok(kv[0]),
                               kv[1]))
    return best[0]


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
    m = RE_PERCENT.search(text)
    try:
        out["pct_of_class"] = float(m.group(1)) if m else None
    except ValueError:
        out["pct_of_class"] = None
    out["has_xml"] = bool(XML_EVENT.search(text))
    return out


def parse_filing_fact2(text: str) -> dict:
    """Fact-1 fields plus the Fact-2 extras (CUSIP, names, acceptance)."""
    out = parse_filing(text)
    out["cusip"] = parse_cusip(text)
    m = RE_SUBJECT_NAME.search(text)
    out["subject_name"] = m.group(1).strip() if m else None
    m = RE_FILER_NAME.search(text)
    out["filer_name"] = m.group(1).strip() if m else None
    acc = parse_acceptance(text)
    out["accepted"] = acc.isoformat(sep=" ") if acc else None
    out["accepted_after_4pm"] = (acc.time() >= dt.time(16, 0)) if acc else None
    return out
