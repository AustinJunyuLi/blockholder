"""Recover delisted-control CIKs through annual Geode 13F holdings.

The route is deliberately conservative:

1. Identify Geode Capital Management's Q1 holdings, filed as one 13F-HR in
   Q2 of each year from 2021 through 2025, from the local quarterly indexes.
2. Match a control's CRSP CUSIP prefix to ``nameOfIssuer`` in those five
   information tables.
3. Resolve the exact normalised issuer name to one CIK across every local
   2021-2025 quarterly index.
4. Require the SEC submissions name to normalise to the same name. Reject a
   candidate if any indexed filing falls after CRSP ``last_date`` plus 365
   calendar days. The grace period allows routine post-delisting filings but
   rejects CIKs that plainly continued as another issuer.

Absent, ambiguous, name-mismatched, and date-failing rows keep a blank CIK.
Only validated rows enter ``permno_cik_map.csv`` under
``map_route=13f_name_unique``. The recovery CSV lands before the canonical
map changes, so no recovered CIK enters matching without its validation row.

Usage:
    .venv/bin/python -m empirics.recover_delisted_controls
    .venv/bin/python -m empirics.recover_delisted_controls --fetch-bid12
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter
from typing import Optional

from empirics.edgar_fetch import DATA_DIR, fetch, list_filings
from empirics.link_cik_cusip import (
    OUTPUT_DIR,
    SUBMISSIONS_MAX_BYTES,
    SUBMISSIONS_URL,
    norm_name,
    parse_submissions,
    sec_bulk_lock,
)

GEODE_CIK = "1214717"
YEARS = tuple(range(2021, 2026))
GRACE_DAYS = 365
HOLDINGS_MAX_BYTES = 100_000_000

HOLDINGS_DIR = os.path.join(DATA_DIR, "13f_holdings")
SUBMISSIONS_DIR = os.path.join(DATA_DIR, "submissions")
CONTROL_PATH = os.path.join(OUTPUT_DIR, "never13d_control_universe.csv")
MAP_PATH = os.path.join(OUTPUT_DIR, "permno_cik_map.csv")
RECOVERY_PATH = os.path.join(OUTPUT_DIR, "delisted_control_cik_recovery.csv")
META_PATH = os.path.join(
    OUTPUT_DIR, "delisted_control_cik_recovery_meta.json")

_OPEN_INFORMATION_TABLE = re.compile(
    rb"<(?:[A-Za-z_][\w.-]*:)?informationTable\b", re.I)
_CLOSE_INFORMATION_TABLE = re.compile(
    rb"</(?:[A-Za-z_][\w.-]*:)?informationTable\s*>", re.I)
_PERIOD_HEADER = re.compile(
    r"CONFORMED PERIOD OF REPORT:\s*(\d{8})", re.I)
_PERIOD_XML = re.compile(
    r"<(?:[A-Za-z_][\w.-]*:)?periodOfReport>\s*([^<]+)", re.I)

RECOVERY_FIELDS = [
    "permno", "permco", "last_date", "grace_end", "cusip8",
    "holding_cusips", "issuer_name", "norm_name", "source_accessions",
    "candidate_ciks", "submissions_name", "latest_index_filing_date",
    "latest_submissions_filing_date", "cik", "map_route", "status",
]


def _norm_cik(raw: object) -> str:
    return str(int(str(raw).strip()))


def _norm_cusip(raw: object) -> str:
    return re.sub(r"[^A-Z0-9]", "", str(raw or "").upper())


def _is_false(raw: object) -> bool:
    return str(raw).strip().lower() in {"0", "false", "f", "no", "n"}


def _sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_csv(path: str) -> tuple[list[str], list[dict[str, str]]]:
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            raise ValueError(f"CSV has no header: {path}")
        return list(reader.fieldnames), list(reader)


def _temporary_path(path: str) -> tuple[int, str]:
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    return tempfile.mkstemp(prefix=f".{os.path.basename(path)}.",
                            suffix=".tmp", dir=directory)


def _atomic_write_bytes(path: str, data: bytes) -> None:
    fd, tmp = _temporary_path(path)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def _atomic_write_csv(path: str, fields: list[str],
                      rows: list[dict[str, object]]) -> None:
    fd, tmp = _temporary_path(path)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields,
                                    extrasaction="ignore",
                                    lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def _atomic_write_json(path: str, value: dict[str, object]) -> None:
    fd, tmp = _temporary_path(path)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(value, fh, indent=1)
            fh.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def _index_path(index_dir: str, year: int, quarter: int) -> str:
    return os.path.join(index_dir, f"form_{year}_QTR{quarter}.idx")


def identify_geode_holdings(index_dir: str) -> list[dict[str, str]]:
    """Return the five exact Geode 13F-HR master rows from local Q2 indexes."""
    filings: list[dict[str, str]] = []
    for year in YEARS:
        path = _index_path(index_dir, year, 2)
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        matches = [
            row for row in list_filings(path, form_types=("13F-HR",))
            if _norm_cik(row["cik"]) == GEODE_CIK
        ]
        if len(matches) != 1:
            raise ValueError(
                f"expected one Geode 13F-HR in {os.path.basename(path)}, "
                f"found {len(matches)}")
        row = dict(matches[0])
        row["year"] = str(year)
        row["accession"] = os.path.basename(
            row["edgar_path"]).removesuffix(".txt")
        filings.append(row)
    return filings


def _holdings_cache_path(holdings_dir: str, filing: dict[str, str]) -> str:
    return os.path.join(holdings_dir, os.path.basename(filing["edgar_path"]))


def _complete_information_table(raw: bytes) -> bool:
    return bool(_OPEN_INFORMATION_TABLE.search(raw)
                and _CLOSE_INFORMATION_TABLE.search(raw))


def ensure_holdings_cached(filings: list[dict[str, str]],
                           holdings_dir: str,
                           allow_fetch: bool = True) -> list[str]:
    """Cache complete 13F masters under the shared SEC bulk lock."""
    os.makedirs(holdings_dir, exist_ok=True)
    missing: list[tuple[dict[str, str], str]] = []
    invalid: list[tuple[dict[str, str], str]] = []
    for filing in filings:
        path = _holdings_cache_path(holdings_dir, filing)
        if not os.path.exists(path):
            missing.append((filing, path))
            continue
        with open(path, "rb") as fh:
            raw = fh.read()
        if not _complete_information_table(raw):
            invalid.append((filing, path))

    if not allow_fetch:
        if invalid:
            raise ValueError(
                f"13F master lacks closing informationTable tag: "
                f"{invalid[0][1]}")
        if missing:
            raise FileNotFoundError(missing[0][1])
    todo = missing + invalid
    if todo:
        with sec_bulk_lock():
            for filing, path in todo:
                url = f"https://www.sec.gov/Archives/{filing['edgar_path']}"
                raw = fetch(url, max_bytes=HOLDINGS_MAX_BYTES)
                if not _complete_information_table(raw):
                    raise ValueError(
                        f"13F master hit the {HOLDINGS_MAX_BYTES}-byte cap "
                        f"without a closing informationTable tag: {url}")
                _atomic_write_bytes(path, raw)
    return [_holdings_cache_path(holdings_dir, filing)
            for filing in filings]


def _period_of_report(raw: bytes) -> dt.date:
    text = raw.decode("latin-1", errors="replace")
    header = _PERIOD_HEADER.search(text)
    if header:
        return dt.datetime.strptime(header.group(1), "%Y%m%d").date()
    xml = _PERIOD_XML.search(text)
    if not xml:
        raise ValueError("13F master has no period of report")
    value = xml.group(1).strip()
    for fmt in ("%Y-%m-%d", "%m-%d-%Y", "%Y%m%d"):
        try:
            return dt.datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"unreadable 13F period of report: {value!r}")


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].rsplit(":", 1)[-1].lower()


def _child_text(element: ET.Element, name: str) -> str:
    for child in element.iter():
        if _local_name(child.tag) == name.lower():
            return " ".join("".join(child.itertext()).split())
    return ""


def parse_information_table(raw: bytes) -> list[tuple[str, str]]:
    """Return ``(CUSIP, nameOfIssuer)`` rows from a complete 13F master."""
    start = _OPEN_INFORMATION_TABLE.search(raw)
    closes = list(_CLOSE_INFORMATION_TABLE.finditer(raw))
    if start is None or not closes:
        raise ValueError("13F master lacks closing informationTable tag")
    fragment = raw[start.start():closes[-1].end()]
    try:
        root = ET.fromstring(fragment)
    except ET.ParseError as exc:
        raise ValueError(f"13F informationTable XML is invalid: {exc}") from exc

    rows: list[tuple[str, str]] = []
    for element in root.iter():
        if _local_name(element.tag) != "infotable":
            continue
        issuer = _child_text(element, "nameOfIssuer")
        cusip = _norm_cusip(_child_text(element, "cusip"))
        if issuer and len(cusip) >= 8:
            rows.append((cusip, issuer))
    return rows


def load_holdings(filings: list[dict[str, str]],
                  cache_paths: list[str]) -> tuple[
                      dict[str, dict[str, object]], list[dict[str, object]]]:
    """Build CUSIP-prefix evidence and reproducibility records."""
    by_cusip: dict[str, dict[str, object]] = {}
    records: list[dict[str, object]] = []
    for filing, path in zip(filings, cache_paths):
        with open(path, "rb") as fh:
            raw = fh.read()
        if not _complete_information_table(raw):
            raise ValueError(
                f"13F master lacks closing informationTable tag: {path}")
        period = _period_of_report(raw)
        expected = dt.date(int(filing["year"]), 3, 31)
        if period != expected:
            raise ValueError(
                f"Geode {filing['year']} filing reports {period}, "
                f"expected Q1 ending {expected}")
        rows = parse_information_table(raw)
        for cusip, issuer in rows:
            key = cusip[:8]
            entry = by_cusip.setdefault(
                key, {"names": {}, "cusips": set(), "accessions": set()})
            names = entry["names"]
            assert isinstance(names, dict)
            normalised = norm_name(issuer)
            if normalised:
                names.setdefault(normalised, set()).add(issuer)
            cusips = entry["cusips"]
            accessions = entry["accessions"]
            assert isinstance(cusips, set) and isinstance(accessions, set)
            cusips.add(cusip)
            accessions.add(filing["accession"])
        records.append({
            "year": int(filing["year"]),
            "quarter": 2,
            "company": filing["company"],
            "cik": _norm_cik(filing["cik"]),
            "date_filed": filing["date_filed"],
            "period_of_report": str(period),
            "edgar_path": filing["edgar_path"],
            "accession": filing["accession"],
            "cache_path": path,
            "cache_sha256": _sha256(path),
            "information_table_rows": len(rows),
        })
    return by_cusip, records


def scan_local_indexes(index_dir: str) -> tuple[
        dict[str, set[str]], dict[str, str], list[str]]:
    """Exact normalised name to CIK sets and each CIK's latest filing date."""
    by_name: dict[str, set[str]] = {}
    latest: dict[str, str] = {}
    paths: list[str] = []
    for year in YEARS:
        for quarter in range(1, 5):
            path = _index_path(index_dir, year, quarter)
            if not os.path.exists(path):
                raise FileNotFoundError(path)
            paths.append(path)
            for row in list_filings(path, form_types=None):
                cik = _norm_cik(row["cik"])
                name = norm_name(row["company"])
                if name:
                    by_name.setdefault(name, set()).add(cik)
                latest[cik] = max(latest.get(cik, ""), row["date_filed"])
    return by_name, latest, paths


def _submissions_path(submissions_dir: str, cik: str) -> str:
    return os.path.join(submissions_dir, f"CIK{int(cik):010d}.json")


def ensure_submissions_cached(ciks: set[str], submissions_dir: str,
                              allow_fetch: bool = True) -> dict[str, str]:
    """Cache candidate submissions documents, holding failures out."""
    os.makedirs(submissions_dir, exist_ok=True)
    missing = [cik for cik in sorted(ciks, key=int)
               if not os.path.exists(_submissions_path(submissions_dir, cik))]
    errors: dict[str, str] = {}
    if missing and allow_fetch:
        with sec_bulk_lock():
            for cik in missing:
                try:
                    raw = fetch(SUBMISSIONS_URL.format(cik=int(cik)),
                                max_bytes=SUBMISSIONS_MAX_BYTES)
                    _atomic_write_bytes(
                        _submissions_path(submissions_dir, cik), raw)
                except Exception as exc:
                    errors[cik] = f"{type(exc).__name__}: {exc}"
    return errors


def _parse_submission_validation(raw: bytes) -> dict[str, object]:
    """Submissions name plus the complete recent-filing date array.

    ``link_cik_cusip`` deliberately tolerates a body truncated after the
    header fields. This gate also needs dates. A closed ``filingDate`` array
    in an otherwise truncated body is enough; if even that array is cut off,
    the candidate stays unresolved.
    """
    document: dict[str, object] = dict(parse_submissions(raw))
    text = raw.decode("utf-8", errors="replace")
    dates: list[str] = []
    dates_complete = True
    try:
        parsed = json.loads(text)
        recent = parsed.get("filings", {}).get("recent", {})
        dates = [str(value)[:10] for value in recent.get("filingDate", [])
                 if str(value).strip()]
    except (AttributeError, json.JSONDecodeError):
        match = re.search(r'"filingDate"\s*:\s*\[(.*?)\]', text, re.S)
        if match:
            dates = re.findall(r'"(\d{4}-\d{2}-\d{2})"', match.group(1))
        else:
            dates_complete = False
    document["recent_filing_dates"] = dates
    document["filing_dates_complete"] = dates_complete
    return document


def load_submissions(ciks: set[str], submissions_dir: str) -> dict[
        str, dict[str, object]]:
    documents: dict[str, dict[str, object]] = {}
    for cik in ciks:
        path = _submissions_path(submissions_dir, cik)
        if os.path.exists(path):
            with open(path, "rb") as fh:
                documents[cik] = _parse_submission_validation(fh.read())
    return documents


def _single_holding_name(entry: dict[str, object]) -> tuple[str, str]:
    names = entry["names"]
    assert isinstance(names, dict)
    if len(names) != 1:
        return "", ""
    normalised = next(iter(names))
    raw_names = names[normalised]
    assert isinstance(raw_names, set)
    return sorted(raw_names)[0], normalised


def _candidate_ciks(controls: list[dict[str, str]],
                    map_by_permno: dict[str, dict[str, str]],
                    holdings: dict[str, dict[str, object]],
                    names_to_ciks: dict[str, set[str]]) -> set[str]:
    candidates: set[str] = set()
    for control in controls:
        mapped = map_by_permno.get(control["permno"], {})
        if not mapped:
            continue
        if str(mapped.get("cik", "")).strip():
            continue
        cusip8 = (_norm_cusip(control.get("hdrcusip"))
                  or _norm_cusip(control.get("cusip")))[:8]
        entry = holdings.get(cusip8)
        if entry is None:
            continue
        _, normalised = _single_holding_name(entry)
        if not normalised:
            continue
        ciks = names_to_ciks.get(normalised, set())
        if len(ciks) == 1:
            candidates.update(ciks)
    return candidates


def _reset_prior_routes(rows: list[dict[str, str]]) -> None:
    for row in rows:
        if row.get("map_route") != "13f_name_unique":
            continue
        prior = row.get("map_route_before_recovery", "").strip()
        if not prior:
            prior = ("ambiguous_ticker" if row.get("ambiguous_ciks", "").strip()
                     else "no_edgar_ticker")
        row["cik"] = ""
        row["map_route"] = prior
        row["map_route_before_recovery"] = ""


def _recovery_row(control: dict[str, str], mapped: dict[str, str],
                  holdings: dict[str, dict[str, object]],
                  names_to_ciks: dict[str, set[str]],
                  latest_by_cik: dict[str, str],
                  submissions: dict[str, dict[str, object]]) -> dict[str, object]:
    last_date = str(control.get("last_date", ""))[:10]
    base: dict[str, object] = {
        "permno": control["permno"],
        "permco": control.get("permco", ""),
        "last_date": last_date,
        "grace_end": "",
        "cusip8": "",
        "holding_cusips": "",
        "issuer_name": "",
        "norm_name": "",
        "source_accessions": "",
        "candidate_ciks": "",
        "submissions_name": "",
        "latest_index_filing_date": "",
        "latest_submissions_filing_date": "",
        "cik": "",
        "map_route": "",
        "status": "",
    }
    if not mapped:
        base["status"] = "map_row_absent"
        return base
    if str(mapped.get("cik", "")).strip():
        base["status"] = "existing_map_cik"
        return base
    try:
        grace_end = dt.date.fromisoformat(last_date) + dt.timedelta(
            days=GRACE_DAYS)
    except ValueError:
        base["status"] = "crsp_last_date_invalid"
        return base
    base["grace_end"] = str(grace_end)

    cusip8 = (_norm_cusip(control.get("hdrcusip"))
              or _norm_cusip(control.get("cusip")))[:8]
    base["cusip8"] = cusip8
    entry = holdings.get(cusip8)
    if entry is None:
        base["status"] = "cusip_absent"
        return base
    cusips = entry["cusips"]
    accessions = entry["accessions"]
    assert isinstance(cusips, set) and isinstance(accessions, set)
    base["holding_cusips"] = ";".join(sorted(cusips))
    base["source_accessions"] = ";".join(sorted(accessions))

    issuer, normalised = _single_holding_name(entry)
    if not normalised:
        base["status"] = "holding_name_ambiguous"
        return base
    base["issuer_name"] = issuer
    base["norm_name"] = normalised
    ciks = sorted(names_to_ciks.get(normalised, set()), key=int)
    base["candidate_ciks"] = ";".join(ciks)
    if not ciks:
        base["status"] = "index_name_absent"
        return base
    if len(ciks) != 1:
        base["status"] = "index_name_ambiguous"
        return base

    cik = ciks[0]
    document = submissions.get(cik)
    if document is None or not document.get("name"):
        base["status"] = "submissions_absent"
        return base
    submissions_name = str(document["name"])
    base["submissions_name"] = submissions_name
    if norm_name(submissions_name) != normalised:
        base["status"] = "submissions_name_mismatch"
        return base
    if not bool(document.get("filing_dates_complete")):
        base["status"] = "submissions_dates_unreadable"
        return base

    latest_index = latest_by_cik.get(cik, "")
    recent_values = document.get("recent_filing_dates", [])
    recent_dates = ([str(value)[:10] for value in recent_values]
                    if isinstance(recent_values, list) else [])
    latest_submissions = max(recent_dates, default="")
    latest = max(latest_index, latest_submissions)
    base["latest_index_filing_date"] = latest_index
    base["latest_submissions_filing_date"] = latest_submissions
    if not latest or latest > str(grace_end):
        base["status"] = "filing_after_grace"
        return base
    base["cik"] = cik
    base["map_route"] = "13f_name_unique"
    base["status"] = "validated"
    return base


def run_recovery(*, index_dir: str = DATA_DIR,
                 holdings_dir: str = HOLDINGS_DIR,
                 submissions_dir: str = SUBMISSIONS_DIR,
                 control_path: str = CONTROL_PATH,
                 map_path: str = MAP_PATH,
                 recovery_path: str = RECOVERY_PATH,
                 meta_path: str = META_PATH,
                 allow_fetch: bool = True) -> dict[str, object]:
    """Run the complete local recovery gate and atomically enrich the map."""
    filings = identify_geode_holdings(index_dir)
    cache_paths = ensure_holdings_cached(
        filings, holdings_dir, allow_fetch=allow_fetch)
    holdings, holdings_records = load_holdings(filings, cache_paths)
    names_to_ciks, latest_by_cik, index_paths = scan_local_indexes(index_dir)

    _, all_controls = _read_csv(control_path)
    controls = [row for row in all_controls
                if _is_false(row.get("still_listed", ""))]
    original_fields, original_map_rows = _read_csv(map_path)
    control_permnos = [row["permno"] for row in controls]
    map_permnos = [row["permno"] for row in original_map_rows]
    if len(control_permnos) != len(set(control_permnos)):
        raise ValueError("duplicate PERMNO in control universe")
    if len(map_permnos) != len(set(map_permnos)):
        raise ValueError("duplicate PERMNO in canonical map")
    map_rows = [dict(row) for row in original_map_rows]
    _reset_prior_routes(map_rows)
    map_by_permno = {row["permno"]: row for row in map_rows}

    candidate_ciks = _candidate_ciks(
        controls, map_by_permno, holdings, names_to_ciks)
    fetch_errors = ensure_submissions_cached(
        candidate_ciks, submissions_dir, allow_fetch=allow_fetch)
    submissions = load_submissions(candidate_ciks, submissions_dir)

    recovery_rows = [
        _recovery_row(control, map_by_permno.get(control["permno"], {}),
                      holdings, names_to_ciks, latest_by_cik, submissions)
        for control in sorted(controls, key=lambda row: int(row["permno"]))
    ]
    validated = {str(row["permno"]): str(row["cik"])
                 for row in recovery_rows if row["status"] == "validated"}

    for row in map_rows:
        cik = validated.get(row["permno"])
        if cik is None:
            continue
        if str(row.get("cik", "")).strip():
            raise ValueError(
                f"refusing to overwrite existing CIK for PERMNO {row['permno']}")
        prior = row.get("map_route", "")
        row["cik"] = cik
        row["map_route"] = "13f_name_unique"
        row["map_route_before_recovery"] = prior

    map_fields = list(original_fields)
    if "map_route_before_recovery" not in map_fields:
        map_fields.append("map_route_before_recovery")
    map_changed = bool(validated) and (
        map_fields != original_fields or map_rows != original_map_rows)

    statuses = Counter(str(row["status"]) for row in recovery_rows)
    n_validated = len(validated)
    n_unresolved = len(recovery_rows) - n_validated
    meta: dict[str, object] = {
        "generated_at": dt.datetime.now().astimezone().isoformat(
            timespec="seconds"),
        "gate_status": ("passed_with_validated_rows" if n_validated
                        else "fallback_option_1"),
        "fallback_status": (
            "not_needed" if not n_unresolved
            else "option_1_for_unresolved_rows" if n_validated
            else "option_1_full"),
        "map_route": "13f_name_unique",
        "normalisation": "exact norm_name match; no fuzzy matching",
        "date_rule": (
            "reject when the candidate CIK has any filing in the local "
            "2021-2025 indexes or its SEC submissions recent feed after "
            "CRSP last_date plus 365 calendar days"),
        "grace_days": GRACE_DAYS,
        "holdings_max_bytes": HOLDINGS_MAX_BYTES,
        "n_holdings_filings": len(filings),
        "holdings_filings": holdings_records,
        "index_files": [os.path.basename(path) for path in index_paths],
        "n_delisted_controls": len(recovery_rows),
        "n_candidate_ciks": len(candidate_ciks),
        "n_validated": n_validated,
        "n_unresolved": n_unresolved,
        "status_counts": dict(sorted(statuses.items())),
        "validated_ciks": sorted(set(validated.values()), key=int),
        "submissions_fetch_errors": fetch_errors,
        "recovery_csv": recovery_path,
        "canonical_map": map_path,
        "map_updated": map_changed,
        "map_sha256_before": _sha256(map_path),
    }

    # Record every validation result before any recovered CIK enters the map.
    _atomic_write_csv(recovery_path, RECOVERY_FIELDS, recovery_rows)
    if map_changed:
        _atomic_write_csv(map_path, map_fields, map_rows)
    meta["map_sha256_after"] = _sha256(map_path)
    note_path = os.path.join(os.path.dirname(os.path.abspath(meta_path)),
                             "delisted_control_cik_recovery.md")
    _atomic_write_bytes(note_path, _recovery_note(meta).encode("utf-8"))
    meta["research_note"] = note_path
    if os.path.dirname(os.path.abspath(meta_path)) == os.path.abspath(OUTPUT_DIR):
        dated = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "research", "empirics_v4",
            "delisted_control_recovery_2026-08-30.md")
        _atomic_write_bytes(dated, _recovery_note(meta).encode("utf-8"))
        meta["dated_note"] = dated
    _atomic_write_json(meta_path, meta)
    return meta


def _recovery_note(meta: dict[str, object]) -> str:
    n_validated = meta.get("n_validated", 0)
    n_unresolved = meta.get("n_unresolved", 0)
    n_delisted = meta.get("n_delisted_controls", 0)
    fallback = meta.get("fallback_status", "")
    lines = [
        "# Delisted-control CIK recovery (option 2)",
        "",
        f"Generated {meta.get('generated_at', '')}.",
        "",
        "Austin selected option 2 as the primary treatment: Geode 13F CUSIP "
        "to issuer name to CIK, with a validation gate. Option 1 is the "
        "fallback for unresolved rows.",
        "",
        f"Delisted controls: {n_delisted}. Validated: {n_validated}. "
        f"Unresolved: {n_unresolved}. Gate: {meta.get('gate_status')}. "
        f"Fallback: {fallback}.",
        "",
        "A recovered CIK enters `permno_cik_map.csv` only after its "
        "validation row is written. Ambiguous names and failed dates keep a "
        "blank CIK.",
        "",
        "Unresolved delisted controls stay out of matching. That conditions "
        "the control group on survival, so the control bid rate is biased "
        "down and gamma is biased up.",
        "",
    ]
    return "\n".join(lines)


def fetch_bid12_for_validated(recovery_path: str = RECOVERY_PATH) -> None:
    """Fetch BID12 event caches for validated recovered CIKs."""
    from empirics import bid12

    _, rows = _read_csv(recovery_path)
    valid = [row for row in rows if row.get("status") == "validated"]
    ciks = sorted({bid12.normalize_cik(row["cik"]) for row in valid})
    names = {bid12.normalize_cik(row["cik"]): row["submissions_name"]
             for row in valid}
    if ciks:
        bid12.extract_universe(ciks, names, use_lock=True)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--fetch-bid12", action="store_true",
        help="after the gate, fetch BID12 event caches for validated CIKs")
    args = parser.parse_args(argv)
    meta = run_recovery()
    print(json.dumps({
        key: meta[key] for key in (
            "gate_status", "fallback_status", "n_delisted_controls",
            "n_validated", "n_unresolved", "status_counts", "map_updated")
    }, indent=1))
    if args.fetch_bid12:
        fetch_bid12_for_validated()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
