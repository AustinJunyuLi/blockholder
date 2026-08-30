"""BID12 outcome coding: bid events within 365 calendar days of a 13D trigger.

Implements the registered coding rule of SPEC §8.3
(``research/empirics_v4/SPEC.md``) as operationalised in
``research/empirics_v4/bid12_coding_rules.md`` — read that file first; it is
the authority on what is counted, and it was written before the coding pass.

Two extraction routes per firm (both cached under ``empirics/data/bid12_cache/``,
gitignored, so re-runs are free):

  Route A — the firm's own EDGAR submissions feed
    (``data.sec.gov/submissions/CIK##########.json``). Carries ``SC TO-T``,
    ``SC TO-C``, ``SC 14D9``, ``DEFM14A``, ``PREM14A`` (counted by form string)
    and ``8-K`` rows whose ``items`` field carries Item 1.01 or 2.01 (counted
    only after text confirmation, §5 of the rulebook). The feed indexes a
    filing under both filer and subject CIK, so bidder-filed tender forms
    appear in the target's feed (verified live 2026-08-30).

  Route B — EDGAR full-text search over the bidder-filed forms
    (``efts.sec.gov/LATEST/search-index``, forms ``SC TO-T,SC TO-C``, target
    core name in quotes). A hit is accepted only if the target's CIK appears
    in the hit's ``display_names`` — name search alone returns other firms'
    filings that merely mention the name.

Everything is deterministic and resumable: per-firm results land in
``bid12_cache/events/{cik}.json`` and the network layer reads cache first.
Bulk extraction acquires the session-wide SEC fair-access lock
(``/tmp/sec_edgar_bulk.lock``) in holds of at most ``REQUESTS_PER_HOLD``
network requests, releasing between holds so peer lanes get in; lookup is
cache-only and needs no lock.

Usage:
    .venv/bin/python -m empirics.bid12 extract-treated [--limit N] [--ciks ...]
    .venv/bin/python -m empirics.bid12 lookup-treated
    .venv/bin/python -m empirics.bid12 extract-control   # when the universe lands
    .venv/bin/python -m empirics.bid12 status
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.parse
from typing import Iterator, Optional

from empirics.edgar_fetch import DATA_DIR, fetch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "output")
CACHE_DIR = os.path.join(DATA_DIR, "bid12_cache")

FACT2_PATH = os.path.join(DATA_DIR, "fact2_parsed.jsonl")
RULEBOOK_PATH = os.path.join(HERE, "..", "research", "empirics_v4",
                             "bid12_coding_rules.md")
CONTROL_UNIVERSE_PATH = os.path.join(OUT_DIR, "never13d_control_universe.csv")
CONTROL_MAP_PATH = os.path.join(OUT_DIR, "permno_cik_map.csv")

SEC_BULK_LOCK = "/tmp/sec_edgar_bulk.lock"
LOCK_POLL_SECONDS = 60
# SEC fair access (host-wide): bulk extraction holds the lock for at most
# REQUESTS_PER_HOLD network requests, then releases and pauses so peer lanes
# polling the lock can get in. Cache hits do not count against the cap.
REQUESTS_PER_HOLD = 500
LOCK_RELEASE_GAP_SECONDS = 20
_NET_REQUESTS = [0]  # actual fetch() calls made inside the current hold

# -- the registered rule -----------------------------------------------------

# Exact EDGAR form strings counted by form type alone (rulebook §2).
# Originals only: '/A' amendments, SC14D9C/SC14D9F communications, SC TO-I
# issuer tenders and SC 13E3 going-private forms are NOT in the registered
# list and are never matched here (exact string equality, no prefix match).
FORM_EVENTS = ("SC TO-T", "SC TO-C", "SC 14D9", "DEFM14A", "PREM14A")
EIGHT_K_ITEMS = ("1.01", "2.01")
ROUTE_B_FORMS = ("SC TO-T", "SC TO-C")  # bidder-filed; route B covers recall

WINDOW_DAYS = 365                       # the twelve-month clock, calendar days
EXTRACT_START = dt.date(2021, 1, 1)     # covers TD-365 for TD >= 2022-01-01
EXTRACT_END = dt.date(2026, 12, 31)     # covers TD+365 for TD <= 2025-12-31
PRIOR_BID_LOOKBACK_DAYS = 365           # rulebook §6 primary exclusion

FTS_URL = "https://efts.sec.gov/LATEST/search-index"
FTS_PAGE_SIZE = 100
FTS_MAX_PAGES = 10

# -- 8-K text confirmation (rulebook §5) -------------------------------------

RE_TAG = re.compile(r"<[^>]+>")
RE_WS = re.compile(r"\s+")

_MERGER_PATTERNS = [
    r"agreement and plan of (?:merger|reorganization|consolidation)",
    r"\bmerger agreement\b",
    r"\bbusiness combination (?:agreement|transaction)\b",
    r"\bplan of merger\b",
    r"\b(?:cash )?(?:tender|exchange) offer\b[^.]{0,200}\b(?:shares|stock)\b",
]

# {C} is replaced by an alternation of 'the Company' / 'the registrant' and
# the firm's core name (regex-escaped). Direction patterns decide whether the
# firm is the target (counts) or the acquirer (does not count).
_TARGET_PATTERNS = [
    r"merg\w+[^.]{0,120}with and into (?:the\s+Company|the\s+[Rr]egistrant|{C})",
    r"(?:the\s+Company|{C})\s+merg\w+[^.]{0,60}with and into",
    # Rulebook §5 bullet 2 verbatim ('(the Company|{name})[^.]{0,120}
    # wholly[-]owned subsidiary of') — the becoming/surviving restriction is
    # the rulebook's for the ACQUIRER side only ('subsidiary of the Company').
    r"(?:the\s+Company|{C})[^.]{0,120}wholly[- ]owned subsidiary of",
    r"acquisition of (?:the\s+Company|{C})\b",
    r"(?:the\s+Company|{C})\s+(?:will|would) be acquired",
    r"(?:the\s+Company|{C})[^.]{0,40}to be acquired",
    r"tender offer for (?:all|any)[^.]{0,80}(?:shares|stock) of "
    r"(?:the\s+Company|{C})\b",
    # Rulebook §5 bullet 6 ('would become a (wholly-owned )?subsidiary');
    # 'will' kept as well.
    r"(?:the\s+Company|{C})\s+(?:will|would) become a[^.]{0,40}subsidiary",
    r"\bacquire (?:the\s+Company|{C})\b",
    r"all[^.]{0,20}outstanding (?:shares|stock)[^.]{0,40}of "
    r"(?:the\s+Company|{C})\b",
    r"(?:each|every) (?:share|shares)[^.]{0,60}of (?:the\s+Company|{C})"
    r"[^.]{0,80}converted into",
]

_ACQUIRER_PATTERNS = [
    r"acquisition by (?:the\s+Company|{C})\b",
    r"(?:the\s+Company|{C})['’]s[^.]{0,40}acquisition of\b",
    r"(?:the\s+Company|{C})[^.]{0,40}(?:complet\w+|consummat\w+)"
    r"[^.]{0,30}(?:its )?acquisition of\b",
    r"(?:the\s+Company|{C})[^.]{0,120}(?:has |have )?agreed to acquir",
    r"(?:the\s+Company|{C})[^.]{0,120}\bwill acquir",
    # Rulebook §5 acquirer bullet 1 'plans to' variant.
    r"(?:the\s+Company|{C})[^.]{0,120}\bplans to acquir",
    r"(?:the\s+Company|{C})[^.]{0,120}entered into[^.]{0,120}to acquir",
    # Rulebook §5 acquirer bullet 3 'sign ... to (acquire|purchase)' variant.
    r"(?:the\s+Company|{C})[^.]{0,120}\bsign(?:ed|s|ing)?[^.]{0,120}"
    r"to (?:acquir|purchas)",
    r"(?:the\s+Company|{C})[^.]{0,120}to purchase[^.]{0,80}"
    r"(?:shares|assets|stock)",
    # A party BECOMING/SURVIVING as a subsidiary of the Company => the
    # Company is the parent => acquirer. The bare phrase 'a wholly owned
    # subsidiary of the Company' is NOT evidence: holdco/double-dummy
    # structures describe the target's own vehicle that way (VMware 2022).
    r"becom\w+[^.]{0,40}wholly[- ]owned subsidiary of "
    r"(?:the\s+Company|{C})\b",
    r"surviv\w+[^.]{0,60}wholly[- ]owned subsidiary of "
    r"(?:the\s+Company|{C})\b",
]

# Non-merger instruments that dominate Item 1.01 volume (debt offerings,
# facilities, commercial contracts). They reject a candidate only when no
# target-direction language fired — a genuine target 8-K always carries it
# (all six positive fixtures do), so this row only clears the instrument
# pile. 'stock purchase agreement' is deliberately absent: an acquisition of
# the firm can be structured as one, so those fall through to ambiguous.
_NONMERGER_PATTERNS = [
    r"\bunderwriting agreement\b",
    r"\bcredit agreement\b",
    r"\bloan agreement\b",
    r"\bindenture\b",
    r"\bsenior notes\b",
    r"\bnotes due\b",
    r"\bsupply agreement\b",
    r"\blease agreement\b",
    r"\blicense agreement\b",
    r"\bcollaboration agreement\b",
    r"\bsettlement agreement\b",
    r"\bseparation agreement\b",
    r"\bdistribution agreement\b",
    r"\bmaster services agreement\b",
    r"\bemployment agreement\b",
    r"\bconsulting agreement\b",
    r"\basset purchase agreement\b",
    r"\bpurchase and sale agreement\b",
]

# Defence instruments: a rights-plan 8-K (Item 1.01 on a Rights Agreement)
# discusses 'tender offer' at length and would otherwise land in the
# ambiguous pile. A rights plan is a defence, not a bid — rejected when no
# target-direction language accompanies it (a genuine merger 8-K that
# mentions the plan still carries direction language and is unaffected).
_DEFENCE_PATTERNS = [
    r"\brights agreement\b",
    r"\bright[s]? plan\b",
    r"\bpoison pill\b",
    r"\bstockholder[s]? rights\b",
    r"\bshareholder[s]? rights\b",
]

# Legal-suffix stripping for the full-text-search core name (rulebook §4).
_SUFFIX_RE = re.compile(
    r"[,\s]+(?:Inc\.?|Corp\.?|Corporation|LLC|L\.L\.C\.|Ltd\.?|Limited|PLC|"
    r"N\.?V\.?|S\.?A\.?|A\.?G\.?|SE|L\.?P\.?|Co\.?|Company|Gp\.?|Bhd\.?|"
    r"S\.A\.B\.?\s*de\s*C\.?V\.?)\s*\.?\s*$", re.I)
_EDGAR_TAG_RE = re.compile(r"/[A-Z&]{1,6}/?$")  # '/DE/', '/NEW/', ...


def normalize_cik(cik) -> str:
    """10-digit zero-padded CIK string."""
    return str(int(str(cik).strip())).zfill(10)


def clean_core_name(name: Optional[str]) -> str:
    """Core company name for full-text search and in-text matching.

    Strips EDGAR '/DE/'-style tags, trailing legal suffixes (applied twice for
    'ABC Holdings, Inc.'-style stacks) and punctuation. Keeps the distinctive
    part of the name — over-stripping would hurt route-B recall.
    """
    if not name:
        return ""
    core = str(name).strip()
    core = _EDGAR_TAG_RE.sub("", core).strip().rstrip(",.")
    for _ in range(2):
        core = _SUFFIX_RE.sub("", core).strip().rstrip(",.")
    return core


def plain_text(raw: str) -> str:
    """HTML -> searchable plain text.

    ``html.unescape`` must run BEFORE tag stripping: 8-K bodies write item
    headings as ``Item&#160;1.01``, and an un-decoded entity silently breaks
    the confirmation regexes (found on live Reata filings, 2026-08-30).
    """
    t = html.unescape(raw)
    t = RE_TAG.sub(" ", t)
    t = t.replace("\xa0", " ")
    return RE_WS.sub(" ", t)


# First tokens too generic to stand for the firm on their own.
_COMMON_FIRST_TOKENS = {
    "american", "national", "first", "united", "general", "international",
    "global", "new", "group", "holdings", "the", "us", "usa", "western",
    "eastern", "central", "pacific", "atlantic", "royal", "imperial",
}


def _name_alternation(core_name: str) -> str:
    """Regex alternation standing for the firm in its own 8-K: the full core
    name, plus its first token when distinctive. 8-K bodies routinely shorten
    the firm to its first token after first reference ('Merger Sub will be
    merged with and into Reata'), which a full-name-only pattern misses."""
    if not core_name:
        return r"(?!x)x"  # never matches
    alts = [re.escape(core_name)]
    first = core_name.split()[0] if core_name.split() else ""
    if len(first) >= 4 and first.lower() not in _COMMON_FIRST_TOKENS \
            and first.lower() != core_name.lower():
        alts.append(re.escape(first))
    return "(?:" + "|".join(alts) + ")"


def _compile(patterns, core_name: str) -> list:
    alt = _name_alternation(core_name)
    return [re.compile(p.replace("{C}", alt), re.I) for p in patterns]


def confirm_8k_text(text: str, core_name: str) -> tuple:
    """Apply the rulebook §5 decision table to one 8-K's plain text.

    Returns (verdict, detail) with verdict in {"confirmed", "rejected",
    "ambiguous"}; detail records the patterns fired so the hand audit can
    retrace the decision without re-fetching.
    """
    merger = [p for p in _compile(_MERGER_PATTERNS, core_name) if p.search(text)]
    target = [p for p in _compile(_TARGET_PATTERNS, core_name) if p.search(text)]
    acquirer = [p for p in _compile(_ACQUIRER_PATTERNS, core_name) if p.search(text)]
    defence = [p for p in _compile(_DEFENCE_PATTERNS, core_name) if p.search(text)]
    nonmerger = [p for p in _compile(_NONMERGER_PATTERNS, core_name)
                 if p.search(text)]
    fired = []
    if merger:
        fired.append(f"merger:{len(merger)}")
    if target:
        fired.append(f"target:{len(target)}")
    if acquirer:
        fired.append(f"acquirer:{len(acquirer)}")
    if defence:
        fired.append(f"defence:{len(defence)}")
    if nonmerger:
        fired.append(f"nonmerger:{len(nonmerger)}")
    detail = ";".join(fired) or "no-patterns"
    if not merger:
        return "rejected", "non-merger-item(" + detail + ")"
    if target and not acquirer:
        return "confirmed", detail
    if acquirer and not target:
        return "rejected", "firm-is-acquirer(" + detail + ")"
    if defence and not target:
        return "rejected", "rights-plan(" + detail + ")"
    if nonmerger and not target:
        return "rejected", "non-merger-instrument(" + detail + ")"
    return "ambiguous", detail


# -- cache layer ---------------------------------------------------------------

def _cache_path(category: str, key: str) -> str:
    d = os.path.join(CACHE_DIR, category)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, key)


def _cached_bytes(url: str, category: str, key: str,
                  max_bytes: int, cache_only: bool = False) -> Optional[bytes]:
    path = _cache_path(category, key)
    if os.path.exists(path):
        with open(path, "rb") as fh:
            return fh.read()
    if cache_only:
        return None
    data = fetch(url, max_bytes=max_bytes)
    _NET_REQUESTS[0] += 1
    with open(path, "wb") as fh:
        fh.write(data)
    return data


def _cached_json(url: str, category: str, key: str,
                 max_bytes: int = 8_000_000, cache_only: bool = False) -> Optional[dict]:
    raw = _cached_bytes(url, category, key, max_bytes, cache_only)
    return json.loads(raw.decode("utf-8", errors="replace")) if raw else None


# -- SEC fair-access lock ------------------------------------------------------

@contextlib.contextmanager
def sec_bulk_lock(poll_seconds: int = LOCK_POLL_SECONDS) -> Iterator[None]:
    """Session-wide mutex for bulk EDGAR pulls (other agents pull concurrently).

    Acquired only around bulk pull phases; code-building, testing and the
    cache-only lookup need no lock.
    """
    waited = 0
    while True:
        try:
            os.mkdir(SEC_BULK_LOCK)
            break
        except FileExistsError:
            if waited == 0:
                print(f"  lock {SEC_BULK_LOCK} held by another agent; "
                      f"polling every {poll_seconds}s", flush=True)
            time.sleep(poll_seconds)
            waited += poll_seconds
    if waited:
        print(f"  lock acquired after {waited}s", flush=True)
    try:
        yield
    finally:
        os.rmdir(SEC_BULK_LOCK)


# -- route A: submissions feed -------------------------------------------------

def fetch_submissions(cik: str, cache_only: bool = False) -> Optional[dict]:
    """Merged filing rows for one CIK: recent table + paginated history files.

    Returns {"rows": [...], "name": str}. Rows carry form, filingDate,
    accessionNumber, items, primaryDocument. The recent table is capped, so
    any ``filings.files[]`` page overlapping the extraction window is merged
    in; rows are de-duplicated by accession number.
    """
    cik10 = normalize_cik(cik)
    url = f"https://data.sec.gov/submissions/CIK{cik10}.json"
    data = _cached_json(url, "submissions", f"{cik10}.json", cache_only=cache_only)
    if data is None:
        return None
    rows = []
    seen = set()

    def _add(table: dict) -> None:
        n = len(table.get("accessionNumber", []))
        for i in range(n):
            acc = table["accessionNumber"][i]
            if acc in seen:
                continue
            seen.add(acc)
            rows.append({
                "form": table["form"][i],
                "filingDate": table["filingDate"][i],
                "accessionNumber": acc,
                "items": (table.get("items") or [""] * n)[i],
                "primaryDocument": (table.get("primaryDocument") or [""] * n)[i],
            })

    recent = data.get("filings", {}).get("recent", {})
    _add(recent)
    for f in data.get("filings", {}).get("files", []) or []:
        # page covers [filingFrom, filingTo]; fetch only if it overlaps the
        # extraction window
        if f.get("filingTo", "") < str(EXTRACT_START) or \
           f.get("filingFrom", "") > str(EXTRACT_END):
            continue
        page = _cached_json(f"https://data.sec.gov/submissions/{f['name']}",
                            "submissions", f"{cik10}_{f['name']}",
                            cache_only=cache_only)
        if page:
            _add(page)
    return {"rows": rows, "name": data.get("name", "")}


def _parse_date(s: str) -> Optional[dt.date]:
    try:
        return dt.date.fromisoformat(str(s)[:10])
    except ValueError:
        return None


def route_a_candidates(rows: list) -> tuple:
    """Split one firm's submission rows into (form-confirmed events, 8-K
    candidates) inside the extraction window."""
    events, candidates = [], []
    for r in rows:
        d = _parse_date(r["filingDate"])
        if d is None or not (EXTRACT_START <= d <= EXTRACT_END):
            continue
        if r["form"] in FORM_EVENTS:
            events.append({"event_date": r["filingDate"], "form": r["form"],
                           "accession": r["accessionNumber"], "route": "A"})
        elif r["form"] == "8-K":
            items = {t.strip() for t in (r["items"] or "").split(",") if t.strip()}
            if items & set(EIGHT_K_ITEMS):
                candidates.append(r)
    return events, candidates


# -- route B: full-text search ---------------------------------------------------

def _display_name_ciks(hit: dict) -> set:
    out = set()
    for n in hit.get("_source", {}).get("display_names") or []:
        m = re.search(r"\(CIK\s+(\d+)\)", n)
        if m:
            out.add(str(int(m.group(1))))
    return out


def route_b_hits(cik: str, name: str, cache_only: bool = False) -> dict:
    """CIK-verified SC TO-T / SC TO-C full-text-search hits for one firm.

    Cached per firm as the *processed* result; delete ``fts/{cik}.json`` to
    re-query. Hits are de-duplicated by accession (the search indexes every
    document in a filing). Name matches whose display_names do not contain the
    target CIK are discarded and counted — they are other firms' filings
    mentioning the name (fund holdings lists, comparable-company tables).
    """
    cik10 = normalize_cik(cik)
    path = _cache_path("fts", f"{cik10}.json")
    if os.path.exists(path):
        with open(path) as fh:
            return json.load(fh)
    if cache_only:
        return {"hits": [], "discarded": 0, "total": 0, "query": None,
                "cached": False}
    core = clean_core_name(name)
    result = {"hits": [], "discarded": 0, "total": 0, "query": None,
              "cached": True, "pages": 0}
    if not core:
        result["error"] = "empty-core-name"
        with open(path, "w") as fh:
            json.dump(result, fh)
        return result
    q = urllib.parse.quote(f'"{core}"')
    forms = urllib.parse.quote(",".join(ROUTE_B_FORMS))
    seen = set()
    for page in range(FTS_MAX_PAGES):
        url = (f"{FTS_URL}?q={q}&dateRange=custom&startdt={EXTRACT_START}"
               f"&enddt={EXTRACT_END}&forms={forms}"
               f"&from={page * FTS_PAGE_SIZE}")
        data = _cached_json(url, "fts_pages",
                            hashlib.md5(url.encode()).hexdigest() + ".json",
                            max_bytes=4_000_000)
        if data is None:
            break
        result["query"] = url
        result["pages"] = page + 1
        hits = data.get("hits", {})
        result["total"] = hits.get("total", {}).get("value", 0)
        page_hits = hits.get("hits", [])
        if not page_hits:
            break
        for h in page_hits:
            s = h.get("_source", {})
            acc = s.get("adsh")
            if not acc or acc in seen:
                continue
            # The FTS 'root_forms' filter files amendments under the root
            # form (SC TO-T/A comes back for forms=SC TO-T). The registered
            # list is originals only — exact string match, /A dropped here.
            if s.get("form") not in ROUTE_B_FORMS:
                continue
            seen.add(acc)
            if str(int(cik10)) in _display_name_ciks(h):
                result["hits"].append({
                    "accession": acc, "form": s.get("form"),
                    "event_date": s.get("file_date"),
                    "display_names": s.get("display_names") or [],
                })
            else:
                result["discarded"] += 1
        if (page + 1) * FTS_PAGE_SIZE >= result["total"]:
            break
    with open(path, "w") as fh:
        json.dump(result, fh)
    return result


# -- filing-text fetches ---------------------------------------------------------

def fetch_8k_text(cik: str, accession: str, primary_doc: str,
                  cache_only: bool = False) -> tuple:
    """The 8-K's primary document as plain text; falls back to the master
    submission .txt (the 8-K body leads it, so truncation keeps the body).
    A failed primary fetch (e.g. a stale primaryDocument name) falls back
    instead of propagating, which would abort the firm's whole route-A pass;
    a failed master fetch yields "unavailable" (rulebook §5 row 8), not an
    exception. Returns (plain text or None, how)."""
    key = accession.replace("-", "") + ".txt"
    raw = None
    how = "primary"
    if primary_doc:
        url = (f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
               f"{accession.replace('-', '')}/{primary_doc}")
        try:
            raw = _cached_bytes(url, "texts", key, max_bytes=2_000_000,
                                cache_only=cache_only)
        except Exception:
            raw = None  # fall through to the master .txt
    if raw is None and not cache_only:
        how = "master-txt"
        url = (f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
               f"{accession}.txt")
        try:
            raw = _cached_bytes(url, "texts", key, max_bytes=1_500_000,
                                cache_only=cache_only)
        except Exception:
            raw = None
    if raw is None:
        return None, "unavailable"
    return plain_text(raw.decode("utf-8", errors="replace")), how


def header_parties(cik: str, accession: str,
                   cache_only: bool = False) -> Optional[dict]:
    """SUBJECT COMPANY / FILED BY CIKs and names from a filing's SGML header.

    Used on SC TO-T / SC TO-C events: verifies the event really names the
    target (subject CIK must equal the firm's CIK) and yields the bidder CIK
    for the filer's-own-bid flag. Verified live: the master .txt resolves
    under the target's CIK directory as well as the filer's.
    """
    url = (f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
           f"{accession}.txt")
    raw = _cached_bytes(url, "headers",
                        accession.replace("-", "") + ".hdr",
                        max_bytes=60_000, cache_only=cache_only)
    if raw is None:
        return None
    head = raw.decode("latin-1", errors="replace")
    sub = re.search(r"SUBJECT COMPANY:.*?CENTRAL INDEX KEY:\s*(\d+)", head, re.S)
    fil = re.search(r"FILED BY:.*?CENTRAL INDEX KEY:\s*(\d+)", head, re.S)
    subn = re.search(r"SUBJECT COMPANY:.*?COMPANY CONFORMED NAME:\s*(.+)", head, re.S)
    filn = re.search(r"FILED BY:.*?COMPANY CONFORMED NAME:\s*(.+)", head, re.S)
    return {
        "subject_cik": str(int(sub.group(1))) if sub else None,
        "filer_cik": str(int(fil.group(1))) if fil else None,
        "subject_name": subn.group(1).strip() if subn else None,
        "filer_name": filn.group(1).strip() if filn else None,
    }


# -- per-firm extraction ---------------------------------------------------------

def extract_firm_events(cik: str, name: str = "",
                        cache_only: bool = False) -> dict:
    """All bid events for one firm over the extraction window, both routes.

    Returns the per-firm record also cached to ``events/{cik}.json``:
    {"cik", "name", "events": [...], "n_8k_rejected", "errors": [...]}.
    Each event: event_date, form, accession, route ("A"/"B"/"A+B"),
    bidder_cik, bidder_name, ambiguous (0/1), confirm_detail.
    """
    cik10 = normalize_cik(cik)
    path = _cache_path("events", f"{cik10}.json")
    if os.path.exists(path):
        with open(path) as fh:
            return json.load(fh)

    record = {"cik": cik10, "name": name, "events": [],
              "n_8k_candidates": 0, "n_8k_rejected": 0, "errors": [],
              "extracted_at": dt.datetime.now().isoformat(timespec="seconds")}
    if cache_only:
        record["errors"].append("not-extracted")
        return record

    by_acc: dict = {}

    def _add(ev: dict) -> None:
        acc = ev["accession"]
        if acc in by_acc:
            old = by_acc[acc]
            if ev["route"] not in old["route"]:
                old["route"] = "+".join(sorted(set(old["route"].split("+"))
                                               | {ev["route"]}))
            for k in ("bidder_cik", "bidder_name"):
                if not old.get(k) and ev.get(k):
                    old[k] = ev[k]
            old["ambiguous"] = min(old["ambiguous"], ev["ambiguous"])
            if ev.get("confirm_detail") and ev["confirm_detail"] not in old["confirm_detail"]:
                old["confirm_detail"] = (old["confirm_detail"] + "|"
                                         + ev["confirm_detail"]).strip("|")
        else:
            by_acc[acc] = dict(ev)

    # Route A
    subs = fetch_submissions(cik10)
    if subs is None:
        record["errors"].append("submissions-unavailable")
    else:
        if not record["name"]:
            record["name"] = subs["name"]
        try:
            form_events, candidates = route_a_candidates(subs["rows"])
            for ev in form_events:
                _add({**ev, "bidder_cik": None, "bidder_name": None,
                      "ambiguous": 0, "confirm_detail": "form-type"})
            record["n_8k_candidates"] = len(candidates)
            core = clean_core_name(record["name"] or name)
            for r in candidates:
                text, how = fetch_8k_text(cik10, r["accessionNumber"],
                                          r["primaryDocument"])
                if text is None:
                    verdict, detail = "ambiguous", f"text-unavailable"
                else:
                    verdict, detail = confirm_8k_text(text, core)
                    detail = f"{detail};via-{how}"
                if verdict == "rejected":
                    record["n_8k_rejected"] += 1
                    continue
                _add({"event_date": r["filingDate"], "form": "8-K",
                      "accession": r["accessionNumber"], "route": "A",
                      "bidder_cik": None, "bidder_name": None,
                      "ambiguous": 1 if verdict == "ambiguous" else 0,
                      "confirm_detail": f"8k-text:{detail}"})
        except Exception as exc:  # keep the pass going; firm is retried next run
            record["errors"].append(f"route-a:{type(exc).__name__}:{exc}")

    # Route B
    try:
        rb = route_b_hits(cik10, record["name"] or name)
        record["fts_total"] = rb.get("total")
        record["fts_discarded"] = rb.get("discarded")
        for h in rb.get("hits", []):
            others = [n for n in h["display_names"]
                      if str(int(cik10)) not in n]
            bidder_cik = bidder_name = None
            m = re.search(r"\(CIK\s+(\d+)\)", others[0]) if others else None
            if m:
                bidder_cik = str(int(m.group(1)))
                bidder_name = others[0].split("(CIK")[0].strip()
            _add({"event_date": h["event_date"], "form": h["form"],
                  "accession": h["accession"], "route": "B",
                  "bidder_cik": bidder_cik, "bidder_name": bidder_name,
                  "ambiguous": 0, "confirm_detail": "fts-cik-verified"})
    except Exception as exc:
        record["errors"].append(f"route-b:{type(exc).__name__}:{exc}")

    # Bidder identity + subject verification for tender-offer events
    for ev in by_acc.values():
        if ev["form"] in ROUTE_B_FORMS and not ev.get("bidder_cik"):
            try:
                parties = header_parties(cik10, ev["accession"])
            except Exception as exc:
                parties = None
                record["errors"].append(
                    f"header:{ev['accession']}:{type(exc).__name__}")
            if parties:
                ev["bidder_cik"] = parties.get("filer_cik")
                ev["bidder_name"] = ev.get("bidder_name") or parties.get("filer_name")
                if parties.get("subject_cik") and \
                        parties["subject_cik"] != str(int(cik10)):
                    ev["ambiguous"] = 1
                    ev["confirm_detail"] += "|subject-cik-mismatch"

    record["events"] = sorted(by_acc.values(),
                              key=lambda e: (e["event_date"], e["accession"]))
    # A route-level failure (submissions feed, the route-A pass, the route-B
    # pass) makes the record PARTIAL: do not cache it, so the next run
    # re-derives the firm. The per-file caches (submissions / fts pages /
    # texts / headers) are written as fetched, so the retry is mostly
    # network-free. Event-level outcomes are still cached: an unfetchable
    # 8-K text is an ambiguous verdict (rulebook §5 row 8), and a failed
    # tender-header probe just leaves bidder_cik unknown.
    fatal = [e for e in record["errors"]
             if e.startswith(("submissions", "route-a:", "route-b:"))]
    if fatal:
        print(f"  {cik10}: route-level errors {fatal}; not cached, "
              f"retried on the next pass", flush=True)
    else:
        with open(path, "w") as fh:
            json.dump(record, fh, indent=1)
    return record


# -- BID12 lookup ---------------------------------------------------------------

def _own_bid(ev: dict, filer_cik: Optional[str], filer_name: Optional[str],
             cik: str) -> bool:
    """Is this confirmed bid event the 13D filer's own bid? (rulebook §7.)

    CIK comparison where a bidder CIK exists (tender-offer headers / FTS
    display names); normalised core-name containment in the confirming 8-K
    text otherwise. Positive identification only — absence of evidence is 0.
    """
    if filer_cik and ev.get("bidder_cik"):
        try:
            if int(ev["bidder_cik"]) == int(str(filer_cik)):
                return True
        except (TypeError, ValueError):
            pass
    if ev["form"] == "8-K" and filer_name:
        core = clean_core_name(filer_name)
        if len(core) >= 6:
            raw = None
            path = _cache_path("texts", ev["accession"].replace("-", "") + ".txt")
            if os.path.exists(path):
                with open(path, "rb") as fh:
                    raw = fh.read()
            if raw is not None and core.lower() in plain_text(
                    raw.decode("utf-8", errors="replace")).lower():
                return True
    return False


def lookup_bid12(events: list, td: dt.date,
                 filer_cik: Optional[str] = None,
                 filer_name: Optional[str] = None,
                 cik: str = "") -> dict:
    """BID12 and flags for one (firm, TD) pair from its event table.

    Window [TD, TD+365] inclusive, calendar days. A confirmed in-window event
    => 1; no in-window evidence => 0; only ambiguous in-window evidence =>
    None (never forced — rulebook §7). Prior-bid flags implement the
    already-under-bid exclusion (rulebook §6).
    """
    hi = td + dt.timedelta(days=WINDOW_DAYS)
    confirmed, ambiguous, prior = [], [], []
    for e in events:
        d = _parse_date(e["event_date"])
        if d is None:
            continue
        if td <= d <= hi:
            (ambiguous if e["ambiguous"] else confirmed).append(e)
        elif d < td and not e["ambiguous"]:
            prior.append(e)
    confirmed.sort(key=lambda e: (e["event_date"], e["accession"]))
    prior.sort(key=lambda e: (e["event_date"], e["accession"]))
    first = confirmed[0] if confirmed else None
    lookback = td - dt.timedelta(days=PRIOR_BID_LOOKBACK_DAYS)
    prior365 = [e for e in prior if _parse_date(e["event_date"]) >= lookback]
    own = any(_own_bid(e, filer_cik, filer_name, cik) for e in confirmed)
    return {
        "bid12": 1 if confirmed else (None if ambiguous else 0),
        "first_bid_date": first["event_date"] if first else "",
        "first_bid_form": first["form"] if first else "",
        "first_bid_route": first["route"] if first else "",
        "first_bid_accession": first["accession"] if first else "",
        "n_bid_events": len(confirmed),
        "filer_own_bid": int(own),
        "ambiguous": int(bool(ambiguous) and not confirmed),
        "n_ambiguous_events": len(ambiguous),
        "excluded_prior_bid": int(bool(prior365)),
        "prior_bid_any": int(bool(prior)),
        "prior_bid_last_date": prior[-1]["event_date"] if prior else "",
    }


# -- universes -------------------------------------------------------------------

def _file_meta(path: str) -> dict:
    st = os.stat(path)
    with open(path, "rb") as fh:
        digest = hashlib.md5(fh.read()).hexdigest()
    return {"path": path, "mtime": dt.datetime.fromtimestamp(st.st_mtime)
            .isoformat(timespec="seconds"), "md5": digest, "bytes": st.st_size}


def load_treated_universe(path: str = FACT2_PATH) -> dict:
    """Unique subject CIKs (+ best name) and per-filing TD rows from the
    parsed 13D universe. Re-deduplicated at run time; the file's mtime/MD5
    are recorded because another ticket may re-parse it."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    names: dict = {}
    counts: dict = {}
    filings = []
    for r in rows:
        if not r.get("subject_cik"):
            continue
        cik10 = normalize_cik(r["subject_cik"])
        nm = r.get("subject_name") or ""
        key = (cik10, nm)
        counts[key] = counts.get(key, 0) + 1
        if cik10 not in names or counts[key] > counts.get(
                (cik10, names[cik10]), 0):
            names[cik10] = nm
        td = _parse_date(r.get("event") or "")
        filings.append({"cik": cik10, "td": td,
                        "accession": r.get("accession", ""),
                        "date_filed": r.get("date_filed", ""),
                        "filer_cik": r.get("filer_cik", ""),
                        "filer_name": r.get("filer_name", ""),
                        "subject_name": nm})
    return {"ciks": sorted(names), "names": names, "filings": filings,
            "meta": {**_file_meta(path), "n_rows": len(rows),
                     "n_unique_subject_ciks": len(names)}}


def load_control_universe() -> Optional[dict]:
    """Control CIKs once SPEC §11 row 23 lands; None until then."""
    if not (os.path.exists(CONTROL_UNIVERSE_PATH)
            and os.path.exists(CONTROL_MAP_PATH)):
        return None
    import pandas as pd
    m = pd.read_csv(CONTROL_MAP_PATH, dtype=str)
    ciks = sorted({normalize_cik(c) for c in m["cik"].dropna()})
    return {"ciks": ciks, "names": {}, "meta": {
        "map": _file_meta(CONTROL_MAP_PATH),
        "universe": _file_meta(CONTROL_UNIVERSE_PATH)}}


# -- pipeline phases ---------------------------------------------------------------

def extract_universe(ciks: list, names: dict, limit: int = 0,
                     use_lock: bool = True) -> None:
    """Bulk extraction phase. Extracts every firm not already cached.

    SEC fair access: unless --no-lock, the host-wide lock is held for at
    most REQUESTS_PER_HOLD network requests at a time (cache hits are
    free), then released for LOCK_RELEASE_GAP_SECONDS so peer lanes
    polling the lock can get in. A single firm may push a hold past the
    cap (the counter is checked between firms, never mid-firm)."""
    todo = [c for c in ciks
            if not os.path.exists(_cache_path("events", f"{c}.json"))]
    if limit:
        todo = todo[:limit]
    print(f"extract: {len(todo)} firms to do "
          f"({len(ciks) - len(todo)} already cached)", flush=True)
    if not todo:
        return
    t0 = time.time()

    def _extract_one(i: int, cik: str) -> None:
        try:
            rec = extract_firm_events(cik, names.get(cik, ""))
            err = f" errors={rec['errors']}" if rec["errors"] else ""
            print(f"[{i + 1}/{len(todo)}] {cik} {rec['name'][:40]!r} "
                  f"events={len(rec['events'])}"
                  f" 8k_cand={rec.get('n_8k_candidates', 0)}{err}",
                  flush=True)
        except Exception as exc:
            print(f"[{i + 1}/{len(todo)}] {cik} FAILED "
                  f"{type(exc).__name__}: {exc}", flush=True)
        if (i + 1) % 100 == 0:
            rate = (i + 1) / max(time.time() - t0, 1e-9)
            eta = (len(todo) - i - 1) / max(rate, 1e-9) / 60
            print(f"  ... {i + 1}/{len(todo)} "
                  f"({rate:.2f} firms/s, ETA {eta:.0f} min)", flush=True)

    def _hold() -> int:
        """One lock hold (or one unlocked stretch): firms until the
        request cap. Returns how many firms were done."""
        n = 0
        while done[0] < len(todo) and _NET_REQUESTS[0] < REQUESTS_PER_HOLD:
            _extract_one(done[0], todo[done[0]])
            done[0] += 1
            n += 1
        return n

    done = [0]
    while done[0] < len(todo):
        _NET_REQUESTS[0] = 0
        if use_lock:
            with sec_bulk_lock():
                _hold()
        else:
            _hold()
        if done[0] < len(todo):
            print(f"  fair-access: released lock after "
                  f"{_NET_REQUESTS[0]} requests ({done[0]}/{len(todo)} "
                  f"firms); resuming in {LOCK_RELEASE_GAP_SECONDS}s",
                  flush=True)
            time.sleep(LOCK_RELEASE_GAP_SECONDS)


def _events_csv(records: list, out_path: str, universe_label: str) -> None:
    import pandas as pd
    rows = []
    for rec in records:
        for e in rec["events"]:
            rows.append({"cik": rec["cik"], "event_date": e["event_date"],
                         "form": e["form"], "accession": e["accession"],
                         "route": e["route"],
                         "bidder_cik": e.get("bidder_cik") or "",
                         "bidder_name": e.get("bidder_name") or "",
                         "ambiguous": e["ambiguous"],
                         "confirm_detail": e.get("confirm_detail", "")})
    df = pd.DataFrame(rows, columns=["cik", "event_date", "form", "accession",
                                     "route", "bidder_cik", "bidder_name",
                                     "ambiguous", "confirm_detail"])
    df = df.sort_values(["cik", "event_date", "accession"])
    df.to_csv(out_path, index=False)
    print(f"wrote {out_path}: {len(df)} events "
          f"across {df['cik'].nunique() if len(df) else 0} firms", flush=True)


def lookup_treated() -> None:
    """Cache-only lookup over the parsed 13D universe; writes the three
    treated-side CSVs plus the run-metadata JSON. No network, no lock."""
    import pandas as pd
    uni = load_treated_universe()
    records, missing = [], 0
    for cik in uni["ciks"]:
        path = _cache_path("events", f"{cik}.json")
        if os.path.exists(path):
            with open(path) as fh:
                records.append(json.load(fh))
        else:
            missing += 1
    os.makedirs(OUT_DIR, exist_ok=True)
    _events_csv(records, os.path.join(OUT_DIR, "bid12_events_treated.csv"),
                "treated")

    out_rows = []
    n_no_td = 0
    for f in uni["filings"]:
        if f["td"] is None:
            n_no_td += 1
            continue
        path = _cache_path("events", f"{f['cik']}.json")
        if os.path.exists(path):
            with open(path) as fh:
                events = json.load(fh)["events"]
            status = "ok"
        else:
            events, status = [], "not-extracted"
        r = lookup_bid12(events, f["td"], f["filer_cik"], f["filer_name"],
                         f["cik"])
        coverage = ("full" if f["td"] >= EXTRACT_START
                    and f["td"] + dt.timedelta(days=WINDOW_DAYS) <= EXTRACT_END
                    else "partial")
        out_rows.append({"cik": f["cik"], "accession": f["accession"],
                         "td": str(f["td"]), "date_filed": f["date_filed"],
                         "filer_cik": f["filer_cik"],
                         "filer_name": f["filer_name"],
                         "subject_name": f["subject_name"],
                         "extraction_status": status,
                         "window_coverage": coverage, **r})
    df = pd.DataFrame(out_rows)
    df = df.sort_values(["cik", "td", "accession"])
    out_path = os.path.join(OUT_DIR, "bid12_treated.csv")
    df.to_csv(out_path, index=False)
    print(f"wrote {out_path}: {len(df)} 13D filings with a TD "
          f"({n_no_td} filings without a TD skipped; "
          f"{missing} CIKs not yet extracted)", flush=True)

    amb = []
    for rec in records:
        for e in rec["events"]:
            if e["ambiguous"]:
                amb.append({"cik": rec["cik"], "name": rec["name"],
                            "event_date": e["event_date"], "form": e["form"],
                            "accession": e["accession"], "route": e["route"],
                            "confirm_detail": e.get("confirm_detail", "")})
    amb_path = os.path.join(OUT_DIR, "bid12_ambiguous_cases.csv")
    pd.DataFrame(amb).to_csv(amb_path, index=False)
    print(f"wrote {amb_path}: {len(amb)} ambiguous events", flush=True)

    # Aggregates for the run metadata: the rulebook (§4) requires discarded
    # route-B hits to be logged in the run metadata, and the recall split
    # (A only / B only / A+B) makes the output self-documenting for the
    # blind hand audit (§10).
    route_counts: dict = {}
    n_8k_cand = n_8k_rej = fts_discarded = 0
    for rec in records:
        n_8k_cand += rec.get("n_8k_candidates", 0)
        n_8k_rej += rec.get("n_8k_rejected", 0)
        fts_discarded += rec.get("fts_discarded") or 0
        for e in rec["events"]:
            route_counts[e["route"]] = route_counts.get(e["route"], 0) + 1

    rules_hash = ""
    if os.path.exists(RULEBOOK_PATH):
        with open(RULEBOOK_PATH, "rb") as fh:
            rules_hash = hashlib.sha256(fh.read()).hexdigest()
    meta = {"generated_at": dt.datetime.now().isoformat(timespec="seconds"),
            "rules_sha256": rules_hash,
            "rulebook": os.path.relpath(RULEBOOK_PATH, HERE),
            "fact2_parsed": uni["meta"],
            "n_filings_without_td": n_no_td,
            "n_ciks_missing_extraction": missing,
            "window_days": WINDOW_DAYS,
            "extraction_window": [str(EXTRACT_START), str(EXTRACT_END)],
            "n_firms_extracted": len(records),
            "n_events": sum(route_counts.values()),
            "events_by_route": dict(sorted(route_counts.items())),
            "n_8k_candidates": n_8k_cand,
            "n_8k_rejected": n_8k_rej,
            "fts_discarded_route_b_hits": fts_discarded,
            "treated_lookup": {
                "n_rows": len(df),
                "bid12_1": int((df["bid12"] == 1).sum()),
                "bid12_0": int((df["bid12"] == 0).sum()),
                "bid12_empty_ambiguous": int(df["ambiguous"].sum()),
                "excluded_prior_bid": int(df["excluded_prior_bid"].sum()),
                "prior_bid_any": int(df["prior_bid_any"].sum()),
                "filer_own_bid": int(df["filer_own_bid"].sum()),
            } if len(df) else {}}
    meta_path = os.path.join(OUT_DIR, "bid12_run_meta.json")
    with open(meta_path, "w") as fh:
        json.dump(meta, fh, indent=1)
    print(f"wrote {meta_path}", flush=True)


def status() -> None:
    """Summary of what is cached and written."""
    ev_dir = os.path.join(CACHE_DIR, "events")
    n = len([f for f in os.listdir(ev_dir) if f.endswith(".json")]) \
        if os.path.isdir(ev_dir) else 0
    print(f"cached firm extractions: {n}")
    for f in ("bid12_events_treated.csv", "bid12_treated.csv",
              "bid12_ambiguous_cases.csv", "bid12_run_meta.json"):
        p = os.path.join(OUT_DIR, f)
        print(f"  {f}: {'present' if os.path.exists(p) else 'absent'}")
    print(f"control universe: "
          f"{'landed' if load_control_universe() else 'not landed'}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="BID12 outcome coding (SPEC §8.3).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("extract-treated", "extract-control"):
        p = sub.add_parser(name)
        p.add_argument("--limit", type=int, default=0)
        p.add_argument("--ciks", default="",
                       help="comma-separated CIKs to restrict to")
        p.add_argument("--no-lock", action="store_true",
                       help="skip the SEC bulk lock (small pulls only)")
    sub.add_parser("lookup-treated")
    sub.add_parser("status")
    args = ap.parse_args(argv)

    if args.cmd == "status":
        status()
        return 0
    if args.cmd == "lookup-treated":
        lookup_treated()
        return 0

    if args.cmd == "extract-treated":
        uni = load_treated_universe()
        print(f"treated universe: {uni['meta']['n_unique_subject_ciks']} unique "
              f"subject CIKs from {uni['meta']['n_rows']} rows "
              f"(md5 {uni['meta']['md5']}, mtime {uni['meta']['mtime']})",
              flush=True)
    else:
        uni = load_control_universe()
        if uni is None:
            print("control universe has not landed "
                  f"({CONTROL_UNIVERSE_PATH} / {CONTROL_MAP_PATH}); "
                  "extraction is one re-run once it does", flush=True)
            return 1
    ciks = uni["ciks"]
    if args.ciks:
        keep = {normalize_cik(c) for c in args.ciks.split(",")}
        ciks = [c for c in ciks if c in keep]
    extract_universe(ciks, uni["names"], limit=args.limit,
                     use_lock=not args.no_lock)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
