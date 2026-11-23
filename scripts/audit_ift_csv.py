#!/usr/bin/env python3
"""Profile the legacy IFT CSV without modifying it or certifying its data.

The report is a diagnostic inventory. Repeated values are warnings for source
verification, not automatic proof of transcription errors or data leakage.
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

REQUIRED = ("P_MPa", "T_K", "Salinity_ppm", "IFT_mN_m", "Source", "Salinity_type")
NUMERIC = ("P_MPa", "T_K", "Salinity_ppm", "IFT_mN_m")


def read_observations(path: Path) -> tuple[list[dict], list[str]]:
    rows: list[dict] = []
    errors: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        filtered = (line for line in stream if not line.lstrip().startswith("#") and line.strip())
        reader = csv.DictReader(filtered)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row")
        missing = [name for name in REQUIRED if name not in reader.fieldnames]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        for line_number, row in enumerate(reader, start=2):
            parsed = dict(row)
            for field in NUMERIC:
                try:
                    parsed[field] = float(row[field])
                except (TypeError, ValueError):
                    errors.append(f"line {line_number}: {field} is not numeric")
            rows.append(parsed)
    return rows, errors


def profile(path: Path) -> dict:
    rows, parse_errors = read_observations(path)
    valid = [r for r in rows if all(isinstance(r.get(k), float) for k in NUMERIC)]
    source_counts = Counter(r["Source"] for r in rows)
    system_counts = Counter(r["Salinity_type"] for r in rows)

    exact_groups = defaultdict(list)
    condition_groups = defaultdict(list)
    for idx, row in enumerate(valid, start=1):
        exact_key = tuple(row[k] for k in NUMERIC) + (row["Source"], row["Salinity_type"])
        exact_groups[exact_key].append(idx)
        condition_key = (row["P_MPa"], row["T_K"])
        condition_groups[condition_key].append(row)

    exact_duplicates = [
        {"key": list(key), "count": len(indices), "profile_row_ids": indices}
        for key, indices in exact_groups.items() if len(indices) > 1
    ]
    repeated_ift_across_salinity = []
    for (pressure, temperature), group in condition_groups.items():
        by_ift = defaultdict(list)
        for row in group:
            by_ift[row["IFT_mN_m"]].append({
                "source": row["Source"],
                "salinity_ppm": row["Salinity_ppm"],
                "salinity_type": row["Salinity_type"],
            })
        for ift, entries in by_ift.items():
            salinities = {entry["salinity_ppm"] for entry in entries}
            if len(salinities) > 1:
                repeated_ift_across_salinity.append({
                    "P_MPa": pressure,
                    "T_K": temperature,
                    "IFT_mN_m": ift,
                    "records": entries,
                })

    invalid_physical = []
    for idx, row in enumerate(valid, start=1):
        if row["P_MPa"] <= 0 or row["T_K"] <= 0 or row["IFT_mN_m"] <= 0 or row["Salinity_ppm"] < 0:
            invalid_physical.append({"profile_row_id": idx, "values": {k: row[k] for k in NUMERIC}})

    def bounds(field: str):
        values = [r[field] for r in valid]
        return {"min": min(values), "max": max(values)} if values else None

    return {
        "input_file": str(path),
        "row_count": len(rows),
        "numeric_rows": len(valid),
        "parse_errors": parse_errors,
        "source_counts": dict(source_counts),
        "salinity_type_counts": dict(system_counts),
        "numeric_ranges": {field: bounds(field) for field in NUMERIC},
        "exact_duplicate_groups": exact_duplicates,
        "same_P_T_and_IFT_across_distinct_salinity": repeated_ift_across_salinity,
        "physically_invalid_rows": invalid_physical,
        "warnings": [
            "This script checks file structure and numerical consistency only; it does not verify observations against publications.",
            "Salinity_ppm is an ambiguous legacy field. Preserve original molality, salt identity and conversion basis before modelling.",
            "Repeated IFT values across salinities require source inspection; they are not automatically errors.",
            "Rows described as representative or correlation-generated must not be labelled independent measurements.",
        ],
        "benchmark_eligibility": "NOT_CERTIFIED_SOURCE_VERIFICATION_REQUIRED",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--out", type=Path, default=Path("outputs/data_audit/legacy_ift_profile.json"))
    args = parser.parse_args()
    report = profile(args.csv_file)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
