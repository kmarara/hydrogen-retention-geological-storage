# Jiao et al. (2026) supplementary workbook: ingestion and first-pass audit

**Source:** Jiao et al., *Tabular Deep Learning for Hydrogen–Brine Interfacial Tension Prediction with Uncertainty Quantification*, Energy & Fuels (2026), DOI [10.1021/acs.energyfuels.6c01887](https://doi.org/10.1021/acs.energyfuels.6c01887).  
**Workbook:** ef6c01887_si_002.xlsx  
**SHA-256:** 9ef4197720c9f37237bda9de8bc666d5deca63d209ccb24c4f957f010efb6d84  
**Worksheet:** Experiment data from literature; Excel rows 3–452.

## Structural audit
- 450 numbered observations; 9 study-reference groups.
- No missing values in required observation fields.
- No exact duplicate records across measured numeric fields.
- Method codes: 0 = Pendant Drop (266); 1 = Sessile Drop (184).
- Ranges: pressure 0.1–45.2 MPa; temperature 293–448.87 K; IFT 29.56–88.99 mN/m.

| Ref. | Study | Rows |
|---|---|---:|
| [1] | Chow et al. (2018) | 79 |
| [2] | Hosseini et al. (2022) | 64 |
| [3] | Higgs et al. (2022) | 36 |
| [4] | Esfandyari et al. (2022) | 16 |
| [5] | Isfehani et al. (2023) | 72 |
| [6] | Al-Mukainah et al. (2022) | 6 |
| [7] | Mirchi et al. (2022) | 15 |
| [8] | Janjua et al. (2024) | 135 |
| [9] | Daraii et al. (2025) | 27 |
| | **Total** | **450** |

## Provenance limitation
The workbook supplies study-level reference markers, but not original page/table/figure coordinates for every row. The audit export therefore marks all rows `provenance_status=unknown` and `benchmark_eligible_primary=False`. These are not certified primary-source measurements. Each study block must be checked against its cited publication and supplementary data.

## Critical Hosseini discrepancy
The workbook's 64 Hosseini et al. (2022) observations distinguish 16 pure-water records from mixed-electrolyte records. At P = 2.76 MPa and T = 298.15 K:
- pure water (NaCl = 0, KCl = 0): **73.57 mN/m**;
- mixed brine (NaCl = 0.907 mol/kg, KCl = 0.143 mol/kg): **74.97 mN/m**.

The legacy `data/raw/ift_experimental.csv` labels 74.97 mN/m at the same P/T as pure water and repeats it in the 63,660-ppm brine block. This is a material inconsistency requiring resolution against the original Hosseini source. Do not merge or silently overwrite either dataset.

## Decisions
1. Original XLSX remains unchanged and is identified by the SHA-256 above.
2. The normalized audit CSV preserves observation number, Excel row, individual salt molalities, gas fractions, method, IFT and study group.
3. All observations remain ineligible for the primary benchmark pending row-level provenance verification.
4. No merge with the legacy 91-row CSV; no model training or performance claims.
5. The extraction script writes a CSV, source-reference list and manifest reproducibly.

## Status
**Gate 1 — workbook acquisition: complete.**  
**Gate 2 — provenance and overlap: in progress; not passed.**
