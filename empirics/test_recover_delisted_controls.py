"""Synthetic public-seam check for delisted-control CIK recovery.

No network, shared cache, or shared output is touched. The check drives the
whole ``run_recovery`` seam with temporary quarterly indexes, 13F masters,
submissions documents, a control universe, and a canonical PERMNO-CIK map.

Run:
    .venv/bin/python -m empirics.test_recover_delisted_controls
"""

from __future__ import annotations

import csv
import json
import os
import tempfile

from empirics import recover_delisted_controls as recovery


def _idx_line(form: str, company: str, cik: str, filed: str,
              edgar_path: str) -> str:
    return (f"{form:<18}{company:<61}{cik:<12}{filed:<12}{edgar_path}\n")


def _write_indexes(index_dir: str) -> list[str]:
    accessions: list[str] = []
    rows: dict[tuple[int, int], list[str]] = {}
    for year in range(2021, 2026):
        accession = f"0001214717-{year % 100:02d}-000001.txt"
        accessions.append(accession)
        rows.setdefault((year, 2), []).append(_idx_line(
            "13F-HR", "GEODE CAPITAL MANAGEMENT, LLC", "1214717",
            f"{year}-05-15", f"edgar/data/1214717/{accession}"))

    rows.setdefault((2021, 1), []).extend([
        _idx_line("10-K", "ALPHA CORP", "100", "2021-03-01", "edgar/a.txt"),
        _idx_line("10-K", "BETA INC", "200", "2021-03-02", "edgar/b.txt"),
        _idx_line("8-K", "BETA CORP", "201", "2021-03-03", "edgar/c.txt"),
        _idx_line("10-K", "GAMMA CORP", "300", "2021-03-04", "edgar/d.txt"),
        _idx_line("10-K", "DELTA CORP", "400", "2021-03-05", "edgar/e.txt"),
    ])
    rows.setdefault((2022, 2), []).append(
        _idx_line("10-Q", "ALPHA CORP", "100", "2022-06-30", "edgar/g.txt"))

    for year in range(2021, 2026):
        for quarter in range(1, 5):
            path = os.path.join(index_dir, f"form_{year}_QTR{quarter}.idx")
            with open(path, "w", encoding="latin-1") as fh:
                fh.write(
                    "Form Type         Company Name                         "
                    "                         CIK         Date Filed  "
                    "File Name\n")
                fh.write("-" * 80 + "\n")
                fh.writelines(rows.get((year, quarter), []))
    return accessions


def _master(year: int, include_holdings: bool = True,
            close_table: bool = True) -> str:
    holdings = ""
    if include_holdings:
        holdings = (
            "<infoTable><nameOfIssuer>ALPHA CORP</nameOfIssuer>"
            "<cusip>111111111</cusip></infoTable>"
            "<infoTable><nameOfIssuer>BETA INC</nameOfIssuer>"
            "<cusip>333333333</cusip></infoTable>"
            "<infoTable><nameOfIssuer>GAMMA CORP</nameOfIssuer>"
            "<cusip>444444444</cusip></infoTable>"
            "<infoTable><nameOfIssuer>DELTA CORP</nameOfIssuer>"
            "<cusip>555555555</cusip></infoTable>")
    closing = "</informationTable>" if close_table else ""
    return (f"CONFORMED PERIOD OF REPORT: {year}0331\n"
            f"<informationTable>{holdings}{closing}\n")


def _write_csv(path: str, fields: list[str], rows: list[dict[str, str]]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _read_csv(path: str) -> list[dict[str, str]]:
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_recovery_public_seam() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        index_dir = os.path.join(tmp, "indexes")
        holdings_dir = os.path.join(tmp, "holdings")
        submissions_dir = os.path.join(tmp, "submissions")
        output_dir = os.path.join(tmp, "output")
        for path in (index_dir, holdings_dir, submissions_dir, output_dir):
            os.makedirs(path)

        accessions = _write_indexes(index_dir)
        for year, accession in zip(range(2021, 2026), accessions):
            with open(os.path.join(holdings_dir, accession), "w",
                      encoding="latin-1") as fh:
                fh.write(_master(year, include_holdings=year == 2021,
                                 close_table=year != 2025))

        control_path = os.path.join(tmp, "controls.csv")
        map_path = os.path.join(tmp, "permno_cik_map.csv")
        recovery_path = os.path.join(output_dir, "recovery.csv")
        meta_path = os.path.join(output_dir, "recovery_meta.json")
        controls = [
            {"permno": str(i), "permco": str(i * 11),
             "hdrcusip": f"{i}{i}{i}{i}{i}{i}{i}{i}",
             "cusip": f"{i}{i}{i}{i}{i}{i}{i}{i}",
             "last_date": "2021-01-01" if i == 5 else "2021-06-30",
             "still_listed": "False"}
            for i in range(1, 6)
        ]
        _write_csv(control_path, list(controls[0]), controls)

        map_fields = ["permno", "permco", "hdrcusip", "cusip", "ticker",
                      "primary_exch", "first_date", "last_date",
                      "still_listed", "cik", "map_route", "ambiguous_ciks",
                      "map_route_before_recovery"]
        map_rows = []
        for row in controls:
            stale = row["permno"] == "2"
            map_rows.append({
                **{field: row.get(field, "") for field in map_fields},
                "cik": "999" if stale else "",
                "map_route": (
                    "13f_name_unique" if stale else "no_edgar_ticker"),
                "map_route_before_recovery": (
                    "no_edgar_ticker" if stale else ""),
            })
        _write_csv(map_path, map_fields, map_rows)
        map_before = open(map_path, "rb").read()

        submissions = {
            "100": {"cik": "100", "name": "ALPHA CORP", "tickers": [],
                    "exchanges": [], "sic": "1000"},
            "300": {"cik": "300", "name": "GAMMA RENAMED CORP",
                    "tickers": [], "exchanges": [], "sic": "3000"},
            "400": {"cik": "400", "name": "DELTA CORP", "tickers": [],
                    "exchanges": [], "sic": "4000", "filings": {
                        "recent": {"filingDate": ["2022-01-03"]}}},
        }
        for cik, body in submissions.items():
            with open(os.path.join(submissions_dir, f"CIK{int(cik):010d}.json"),
                      "w", encoding="utf-8") as fh:
                json.dump(body, fh)

        try:
            recovery.run_recovery(
                index_dir=index_dir,
                holdings_dir=holdings_dir,
                submissions_dir=submissions_dir,
                control_path=control_path,
                map_path=map_path,
                recovery_path=recovery_path,
                meta_path=meta_path,
                allow_fetch=False,
            )
        except ValueError as exc:
            assert "closing informationTable" in str(exc)
        else:
            raise AssertionError("truncated 13F information table was accepted")
        assert open(map_path, "rb").read() == map_before
        assert not os.path.exists(recovery_path)

        with open(os.path.join(holdings_dir, accessions[-1]), "w",
                  encoding="latin-1") as fh:
            fh.write(_master(2025, include_holdings=False))

        meta = recovery.run_recovery(
            index_dir=index_dir,
            holdings_dir=holdings_dir,
            submissions_dir=submissions_dir,
            control_path=control_path,
            map_path=map_path,
            recovery_path=recovery_path,
            meta_path=meta_path,
            allow_fetch=False,
        )
        rows = {row["permno"]: row for row in _read_csv(recovery_path)}
        assert rows["1"]["status"] == "validated"
        assert rows["1"]["cik"] == "100"
        assert rows["2"]["status"] == "cusip_absent"
        assert rows["3"]["status"] == "index_name_ambiguous"
        assert set(rows["3"]["candidate_ciks"].split(";")) == {"200", "201"}
        assert rows["4"]["status"] == "submissions_name_mismatch"
        assert rows["5"]["status"] == "filing_after_grace"
        assert all(rows[p]["cik"] == "" for p in ("2", "3", "4", "5"))

        enriched = {row["permno"]: row for row in _read_csv(map_path)}
        assert enriched["1"]["cik"] == "100"
        assert enriched["1"]["map_route"] == "13f_name_unique"
        assert enriched["1"]["map_route_before_recovery"] == "no_edgar_ticker"
        assert enriched["2"]["cik"] == ""
        assert enriched["2"]["map_route"] == "no_edgar_ticker"
        assert enriched["2"]["map_route_before_recovery"] == ""
        assert sum(row["map_route"] == "13f_name_unique"
                   for row in enriched.values()) == 1

        assert meta["n_holdings_filings"] == 5
        assert meta["n_validated"] == 1
        assert meta["n_unresolved"] == 4
        assert meta["grace_days"] == 365
        assert meta["gate_status"] == "passed_with_validated_rows"
        assert meta["fallback_status"] == "option_1_for_unresolved_rows"
        assert meta["map_updated"] is True
        note_path = os.path.join(output_dir, "delisted_control_cik_recovery.md")
        assert os.path.exists(note_path)
        note = open(note_path, encoding="utf-8").read()
        assert "option 2" in note.lower() and "validated" in note.lower()
        assert "unresolved" in note.lower()

        first_map = open(map_path, "rb").read()
        recovery.run_recovery(
            index_dir=index_dir,
            holdings_dir=holdings_dir,
            submissions_dir=submissions_dir,
            control_path=control_path,
            map_path=map_path,
            recovery_path=recovery_path,
            meta_path=meta_path,
            allow_fetch=False,
        )
        assert open(map_path, "rb").read() == first_map

        zero_control_path = os.path.join(tmp, "zero_controls.csv")
        zero_map_path = os.path.join(tmp, "zero_map.csv")
        zero_recovery_path = os.path.join(output_dir, "zero_recovery.csv")
        zero_meta_path = os.path.join(output_dir, "zero_recovery_meta.json")
        _write_csv(zero_control_path, list(controls[1]), [controls[1]])
        zero_fields = map_fields[:-1]
        zero_row = {
            **{field: controls[1].get(field, "") for field in zero_fields},
            "cik": "", "map_route": "no_edgar_ticker",
        }
        _write_csv(zero_map_path, zero_fields, [zero_row])
        zero_before = open(zero_map_path, "rb").read()
        zero_meta = recovery.run_recovery(
            index_dir=index_dir,
            holdings_dir=holdings_dir,
            submissions_dir=submissions_dir,
            control_path=zero_control_path,
            map_path=zero_map_path,
            recovery_path=zero_recovery_path,
            meta_path=zero_meta_path,
            allow_fetch=False,
        )
        assert zero_meta["n_validated"] == 0
        assert zero_meta["gate_status"] == "fallback_option_1"
        assert zero_meta["fallback_status"] == "option_1_full"
        assert zero_meta["map_updated"] is False
        assert open(zero_map_path, "rb").read() == zero_before


def main() -> int:
    test_recovery_public_seam()
    print("1/1 recovery public-seam checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
