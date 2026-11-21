#!/usr/bin/env python3
"""Ingest the ACS Jiao et al. (2026) supplementary XLSX without losing provenance.

This script does not invent or reconstruct observations. It reads the original
supplementary workbook supplied by the researcher, preserves source columns,
and writes a sheet/row-indexed audit copy for schema inspection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

DOI = "10.1021/acs.energyfuels.6c01887"
ARTICLE_URL = f"https://doi.org/{DOI}"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path, help="Path to the original ACS supplementary XLSX")
    parser.add_argument("--out", type=Path, default=Path("data/processed/jiao_2026_audit"))
    args = parser.parse_args()

    if not args.workbook.is_file():
        raise SystemExit(f"Workbook not found: {args.workbook}")

    args.out.mkdir(parents=True, exist_ok=True)
    book = pd.ExcelFile(args.workbook, engine="openpyxl")
    inventory = []
    for sheet_index, sheet_name in enumerate(book.sheet_names):
        frame = pd.read_excel(book, sheet_name=sheet_name, dtype=object)
        # Preserve the workbook's original fields; add audit-only row identity.
        frame.insert(0, "source_excel_row", range(2, len(frame) + 2))
        frame.insert(0, "source_sheet", sheet_name)
        output = args.out / f"sheet_{sheet_index + 1:02d}.csv"
        frame.to_csv(output, index=False)
        inventory.append({
            "sheet": sheet_name,
            "rows": int(len(frame)),
            "columns": list(map(str, frame.columns)),
            "csv": str(output),
        })

    metadata = {
        "source_doi": DOI,
        "source_article_url": ARTICLE_URL,
        "source_filename": args.workbook.name,
        "source_sha256": sha256(args.workbook),
        "ingestion_status": "workbook_read; scientific validation pending",
        "sheets": inventory,
        "warnings": [
            "Do not assume all rows are independent experiments.",
            "Trace each observation to its original publication and experimental campaign.",
            "Do not merge with the existing project CSV until units, fluid system, salt basis and duplicates are audited.",
            "This ingestion output is a faithful workbook extraction, not a verified benchmark dataset.",
        ],
    }
    (args.out / "ingestion_manifest.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
