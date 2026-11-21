#!/usr/bin/env python3
"""Audit and extract Jiao et al. (2026) ACS supplementary observations.

The normalized CSV is an audit copy, not a certified experimental benchmark:
the workbook gives a study-level reference marker but not row-level original
page/table/figure coordinates. Original workbook is never modified.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
import pandas as pd

DOI = "10.1021/acs.energyfuels.6c01887"
ARTICLE_URL = f"https://doi.org/{DOI}"
SHEET = "Experiment data from literature"
DATA_START_EXCEL_ROW, DATA_END_EXCEL_ROW = 3, 452
COLUMNS = ["observation_no","pressure_MPa","temperature_K","NaCl_mol_kg","KCl_mol_kg",
"CaCl2_mol_kg","MgCl2_mol_kg","CH4_mole_fraction","CO2_mole_fraction","method_code",
"IFT_mN_m","reference_marker"]
NUMERIC = COLUMNS[:-1]

def sha256(path: Path) -> str:
    digest=hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""): digest.update(chunk)
    return digest.hexdigest()

def extract(workbook: Path):
    raw=pd.read_excel(workbook,sheet_name=SHEET,header=None,engine="openpyxl")
    frame=raw.iloc[DATA_START_EXCEL_ROW-1:DATA_END_EXCEL_ROW,:12].copy()
    if len(frame)!=450: raise ValueError(f"Expected 450 numbered observations; found {len(frame)}")
    frame.columns=COLUMNS
    frame["source_excel_row"]=range(DATA_START_EXCEL_ROW,DATA_END_EXCEL_ROW+1)
    frame["reference_marker"]=frame["reference_marker"].ffill()
    frame["study_id"]=frame["reference_marker"].str.extract(r"\[(\d+)\]").astype("Int64")
    for col in NUMERIC: frame[col]=pd.to_numeric(frame[col],errors="coerce")
    frame["method_label"]=frame["method_code"].map({0:"Pendant Drop",1:"Sessile Drop"})
    frame["provenance_status"]="unknown"
    frame["benchmark_eligible_primary"]=False
    frame["eligibility_reason"]="Study-level reference supplied; original publication coordinates and row-level extraction lineage not yet verified"
    if frame[NUMERIC].isna().any().any(): raise ValueError("Missing or non-numeric required observation values")
    if frame["study_id"].isna().any(): raise ValueError("Observation lacks a preceding study reference marker")
    if not frame["method_code"].isin([0,1]).all(): raise ValueError("Unexpected measurement-method code")
    if not frame["study_id"].between(1,9).all(): raise ValueError("Unexpected study reference marker")
    if frame["observation_no"].tolist()!=list(range(1,451)): raise ValueError("Observation numbers are not exactly 1-450")
    if frame.duplicated(subset=NUMERIC).any(): raise ValueError("Exact duplicate records found")
    return frame,raw

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("workbook",type=Path)
    parser.add_argument("--out",type=Path,default=Path("data/processed/jiao_2026"))
    args=parser.parse_args()
    if not args.workbook.is_file(): raise SystemExit(f"Workbook not found: {args.workbook}")
    args.out.mkdir(parents=True,exist_ok=True)
    frame,raw=extract(args.workbook)
    output=args.out/"observations_audit.csv"
    frame.to_csv(output,index=False)
    refs=[]
    for _,row in raw.iloc[452:,:].iterrows():
        value=next((str(v).strip() for v in row if isinstance(v,str) and re.match(r"^\s*\[\d+\]",v)),None)
        if value:
            marker=re.match(r"^\s*\[(\d+)\]",value)
            refs.append({"study_id":int(marker.group(1)),"workbook_reference_text":value})
    refs_path=args.out/"source_references.csv"
    pd.DataFrame(refs).to_csv(refs_path,index=False)
    manifest={
      "source_doi":DOI,"source_article_url":ARTICLE_URL,"source_filename":args.workbook.name,
      "source_sha256":sha256(args.workbook),"source_sheet":SHEET,
      "source_excel_data_rows":[DATA_START_EXCEL_ROW,DATA_END_EXCEL_ROW],
      "observation_count":int(len(frame)),
      "study_counts":{str(int(k)):int(v) for k,v in frame.study_id.value_counts().sort_index().items()},
      "method_code_counts":{str(int(k)):int(v) for k,v in frame.method_code.value_counts().sort_index().items()},
      "numeric_ranges":{c:{"min":float(frame[c].min()),"max":float(frame[c].max())} for c in ["pressure_MPa","temperature_K","IFT_mN_m"]},
      "missing_required_values":int(frame[NUMERIC].isna().sum().sum()),
      "exact_duplicate_records":int(frame.duplicated(subset=NUMERIC).sum()),
      "source_reference_count":len(refs),"normalized_csv":output.name,"source_references_csv":refs_path.name,
      "status":"extracted_and_structurally_audited; scientific provenance verification pending",
      "important_limitations":[
        "Study references are forward-filled from workbook markers; original page/table/figure coordinates are not provided per row.",
        "All row-level provenance statuses are unknown pending verification against original publications.",
        "No observation is certified for the primary benchmark by this ingestion step.",
        "No legacy project data are merged or modified.",
        "Method codes follow workbook legend: 0=Pendant Drop; 1=Sessile Drop."
      ]}
    (args.out/"ingestion_manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2,ensure_ascii=False))

if __name__=="__main__": main()
