"""EDGAR fetching utilities (stdlib-only, SEC fair-access compliant).

Approach: quarterly ``form.idx`` master indexes enumerate every filing
(form type, company, CIK, date filed, path); we filter exact form types
(``SC 13D``/``SCHEDULE 13D``, ``SC 13G``/``SCHEDULE 13G`` -- EDGAR renamed
the former to the latter around 2024Q3) and fetch each filing's master
``.txt`` submission for parsing. Throttled well below the SEC's 10
requests/second guidance.

Usage:
    .venv/bin/python -m empirics.edgar_fetch --quarters 2023Q2 2023Q3 2024Q3 2024Q4

Raw downloads land in empirics/data/ (gitignored).
"""

from __future__ import annotations

import argparse
import os
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
USER_AGENT = "blockholder-research austin.junyu.li@gmail.com"
THROTTLE_SECONDS = 0.25  # ~4 req/s, well under SEC's 10/s guidance

_last_request = [0.0]


def fetch(url: str, max_bytes: int = 400_000, retries: int = 3) -> bytes:
    """Throttled GET with the SEC-required User-Agent header."""
    wait = THROTTLE_SECONDS - (time.monotonic() - _last_request[0])
    if wait > 0:
        time.sleep(wait)
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept-Encoding": "identity",
    })
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read(max_bytes)
            _last_request[0] = time.monotonic()
            return data
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError("unreachable")


def form_index_url(year: int, quarter: int) -> str:
    return (f"https://www.sec.gov/Archives/edgar/full-index/"
            f"{year}/QTR{quarter}/form.idx")


def download_form_index(year: int, quarter: int) -> str:
    """Download (cached) the quarterly form.idx; return local path."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"form_{year}_QTR{quarter}.idx")
    if not os.path.exists(path):
        data = fetch(form_index_url(year, quarter), max_bytes=80_000_000)
        with open(path, "wb") as fh:
            fh.write(data)
    return path


# EDGAR renamed 'SC 13D'/'SC 13G' to 'SCHEDULE 13D'/'SCHEDULE 13G' (and their
# '/A' amendments) around 2024Q3. Aliases apply both directions so a caller
# asking for either spelling transparently gets both -- callers that pass an
# explicit form_types= (bypassing the alias-aware default below) still see
# renamed rows instead of silently dropping them.
_FORM_ALIASES = {
    "SC 13D": "SCHEDULE 13D", "SCHEDULE 13D": "SC 13D",
    "SC 13G": "SCHEDULE 13G", "SCHEDULE 13G": "SC 13G",
    "SC 13D/A": "SCHEDULE 13D/A", "SCHEDULE 13D/A": "SC 13D/A",
    "SC 13G/A": "SCHEDULE 13G/A", "SCHEDULE 13G/A": "SC 13G/A",
}


def _expand_form_type_aliases(form_types: tuple) -> set:
    return set(form_types) | {_FORM_ALIASES[f] for f in form_types if f in _FORM_ALIASES}


def list_filings(idx_path: str,
                  form_types: tuple = ("SC 13D", "SC 13G",
                                        "SCHEDULE 13D", "SCHEDULE 13G")) -> list:
    """Parse a form.idx into rows for exactly the requested form types
    (plus their EDGAR-renamed aliases -- see ``_FORM_ALIASES``).

    Returns dicts: form, company, cik, date_filed, edgar_path.
    (Amendments 'SC 13D/A' / 'SCHEDULE 13D/A' are distinct form strings and
    excluded unless requested explicitly.)

    The form-type column is NOT a fixed 12-char field -- 'SCHEDULE 13D/A'
    (14 chars) overflows a hard ``line[:12]`` slice and gets truncated to
    look like the un-amended 'SCHEDULE 13D', so the field is split on the
    first run of 2+ spaces (the real column separator) instead.
    """
    import re
    tail = re.compile(r"(\d+)\s+(\d{4}-\d{2}-\d{2})\s+(edgar/\S+?\.txt)\s*$")
    form_field = re.compile(r"^(\S+(?: \S+)*?)\s{2,}")
    wanted = _expand_form_type_aliases(form_types)
    rows = []
    with open(idx_path, "r", encoding="latin-1") as fh:
        in_body = False
        for line in fh:
            if line.startswith("Form Type"):
                in_body = True
                continue
            if not in_body or line.startswith("---"):
                continue
            fm = form_field.match(line)
            if not fm:
                continue
            form = fm.group(1)
            if form not in wanted:
                continue
            m = tail.search(line)
            if not m:
                continue
            cik, date_filed, path = m.group(1), m.group(2), m.group(3)
            company = line[fm.end():m.start()].strip()
            rows.append({"form": form, "company": company, "cik": cik,
                         "date_filed": date_filed, "edgar_path": path})
    return rows


def fetch_filing_text(edgar_path: str, max_bytes: int = 400_000) -> str:
    """Fetch the master submission text for one filing (truncated)."""
    url = f"https://www.sec.gov/Archives/{edgar_path}"
    return fetch(url, max_bytes=max_bytes).decode("latin-1", errors="replace")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Download EDGAR quarterly form indexes.")
    ap.add_argument("--quarters", nargs="+", required=True,
                    help="e.g. 2023Q2 2023Q3 2024Q3 2024Q4")
    args = ap.parse_args(argv)
    for q in args.quarters:
        year, qtr = int(q[:4]), int(q[-1])
        path = download_form_index(year, qtr)
        n = len(list_filings(path))
        print(f"{q}: {path} ({n} SC 13D/13G originals)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
