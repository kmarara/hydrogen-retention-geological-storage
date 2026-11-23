#!/usr/bin/env python3
"""Screen canonical IFT observations for cross-publication overlap candidates.

This is a candidate-finding audit, not an automatic duplicate deletion tool.
Only rows with matching declared fluid identity/composition are compared.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import pandas as pd


def fluid_key(row: pd.Series) -> tuple:
    def norm(v):
        return None if pd.isna(v) else str(v).strip().lower()
    return (
        norm(row.get("electrolyte_identity")),
        norm(row.get("electrolyte_composition_original")),
        *(None if pd.isna(row.get(c)) else round(float(row[c]), 8)
          for c in ("gas_H2_mole_fraction", "gas_CO2_mole_fraction", "gas_CH4_mole_fraction")),
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--pressure-tol-mpa", type=float, default=0.02)
    ap.add_argument("--temperature-tol-k", type=float, default=0.5)
    ap.add_argument("--ift-tol-mn-m", type=float, default=0.10)
    ap.add_argument("--out", type=Path, default=Path("outputs/data_audit/cross_study_overlap.json"))
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    required = {"observation_id", "source_study_id", "electrolyte_identity",
                "electrolyte_composition_original", "gas_H2_mole_fraction",
                "gas_CO2_mole_fraction", "gas_CH4_mole_fraction",
                "pressure_MPa", "temperature_K", "IFT_mN_m"}
    missing = sorted(required - set(df.columns))
    if missing:
        raise SystemExit(f"Missing required columns: {missing}")
    if df["observation_id"].duplicated().any():
        raise SystemExit("Duplicate observation_id values found")

    exact, near = [], []
    studies = sorted(df["source_study_id"].dropna().unique())
    for i, study_a in enumerate(studies):
        a = df[df.source_study_id == study_a]
        for study_b in studies[i + 1:]:
            b = df[df.source_study_id == study_b]
            for _, ra in a.iterrows():
                ka = fluid_key(ra)
                for _, rb in b.iterrows():
                    if ka != fluid_key(rb):
                        continue
                    dp = abs(float(ra.pressure_MPa) - float(rb.pressure_MPa))
                    dt = abs(float(ra.temperature_K) - float(rb.temperature_K))
                    dg = abs(float(ra.IFT_mN_m) - float(rb.IFT_mN_m))
                    pair = {
                        "study_a": study_a, "observation_a": ra.observation_id,
                        "study_b": study_b, "observation_b": rb.observation_id,
                        "delta_pressure_MPa": dp, "delta_temperature_K": dt,
                        "delta_IFT_mN_m": dg,
                    }
                    if dp <= 1e-10 and dt <= 1e-10 and dg <= 1e-10:
                        exact.append(pair)
                    elif (dp <= args.pressure_tol_mpa and
                          dt <= args.temperature_tol_k and
                          dg <= args.ift_tol_mn_m):
                        near.append(pair)

    report = {
        "input": str(args.csv), "rows": int(len(df)),
        "studies": {str(k): int(v) for k, v in df.source_study_id.value_counts().items()},
        "unique_observation_ids": int(df.observation_id.nunique()),
        "tolerances": {"pressure_MPa": args.pressure_tol_mpa,
                       "temperature_K": args.temperature_tol_k,
                       "IFT_mN_m": args.ift_tol_mn_m},
        "exact_cross_study_matches": exact,
        "near_cross_study_candidates": near,
        "interpretation": "Screening only. A zero result does not prove independent experiments; inspect source lineage, validation tables, and author data reuse manually.",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": report["rows"], "studies": report["studies"],
                      "exact_matches": len(exact), "near_candidates": len(near),
                      "report": str(args.out)}, indent=2))


if __name__ == "__main__":
    main()
