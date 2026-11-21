# Hosseini et al. (2022) supporting-information verification audit

**Audit date:** 2026-11-21  
**Source:** Hosseini M, Fahimpour J, Ali M, Keshavarz A, Iglauer S (2022), *H2-brine interfacial tension as a function of salinity, temperature, and pressure; implications for hydrogen geo-storage*, Journal of Petroleum Science and Engineering 213, 110441. DOI: 10.1016/j.petrol.2022.110441.  
**Primary evidence inspected:** `SupportingInformationforH2-brineinterfacialtensionatgeologicalconditions.docx`, 3 pages, Tables S1-S4 and Figure S1.  
**Uploaded source SHA-256:** `16b6ae258043a370db31e85d5deaf5062bfbd873d3ed152762def30083b8e2d2`.

## Findings

The supporting information contains 64 tabulated observations: 16 per system, across four temperatures (298.15, 323.15, 373.15, 423.15 K) and four pressures (2.76, 13.79, 27.58, 34.47 MPa).

- Table S1: H2O + H2 (pure water; 0 mol/kg added salt).
- Table S2: H2 + mixed brine (0.864 NaCl + 0.136 KCl), total salt molality 1.05 mol/kg.
- Table S3: same mixed-brine composition, 3.15 mol/kg.
- Table S4: same mixed-brine composition, 4.95 mol/kg.

The SI reports pressure, temperature, density difference (Delta rho), IFT, and an uncertainty term (±). The SI does not define the statistical interpretation of the uncertainty term; it is therefore retained literally and not reinterpreted as a standard deviation or confidence interval. The method is pendant drop as described in the article. Figure S1 (page 3) shows example recorded hydrogen-drop images for the 4.95 mol/kg brine at 298.15 K and 13.79 MPa, with a reported IFT of 78.65 ± 0.18 mN/m.

## Comparison against the legacy repository CSV

The 64 Hosseini rows in `data/raw/ift_experimental.csv` were compared in block order against Tables S1-S4.

| System / source table | Exact IFT matches | Mismatches |
|---|---:|---:|
| Pure water, S1 | 0/16 | 16 |
| 1.05 mol/kg mixed brine, S2 | 2/16 | 14 |
| 3.15 mol/kg mixed brine, S3 | 14/16 | 2 |
| 4.95 mol/kg mixed brine, S4 | 16/16 | 0 |
| **Total** | **32/64** | **32/64** |

This is not explained by rounding. For example, at 298.15 K and 2.76 MPa, Table S1 reports 73.57 ± 0.09 mN/m for pure water, while Table S2 reports 74.97 ± 0.03 mN/m for 1.05 mol/kg mixed brine. The legacy CSV assigns 74.97 to both systems. At 298.15 K and 13.79 MPa, the source reports 71.81 ± 0.01 (pure water) and 73.17 ± 0.14 (1.05 mol/kg brine), while the legacy CSV again assigns 73.17 to both.

The complete mismatch counts above are based on exact comparison of the two-decimal source IFT values with the legacy CSV values. The 3.15 mol/kg block's two mismatches are at 423.15 K and 27.58 / 34.47 MPa (legacy 54.10 / 53.60 versus source 53.70 / 53.54 mN/m).

## Data-governance decision

1. **Do not use the legacy 64 Hosseini rows in any benchmark or model training.** Retain the original file unchanged for audit history.
2. A separate 64-row extraction was generated from Tables S1-S4, preserving source table/row coordinates, source units, density difference, IFT uncertainty, electrolyte identity/composition, and method.
3. The generated extraction has SHA-256 `0e1d4715ffd66d01ee7963652621bbfaa6dcb387920cecf69775c3d394adbc1d`.
4. Rows are marked `provenance_status=table_extracted`, reviewer status `verified`, and `benchmark_eligible_primary=true` as canonical source observations. Each has a row-specific duplicate group ID linking its matching Jiao workbook copy. `benchmark_eligible_primary=false` remains in place pending cross-source duplicate/overlap review, including comparison against the Jiao et al. (2026) 450-row workbook and other compilations.
5. No claim is made that the 64 rows are 64 independent experiments. They are 64 source-table observations from one study.

## Remaining work

- Global overlap review across the remaining literature sources is still required; the Hosseini/Jiao duplicate pair is resolved and recorded.
- Resolve source lineage and independence before setting primary benchmark eligibility.
- Review the original article methods for the exact meaning of reported uncertainty and confirm any details not defined in the SI.
- Keep the old CSV unchanged; any later migration should preserve an explicit link to this audit.

## Reproducibility note

The SI source document was supplied by the user in this conversation. It is not copied into this repository. The extracted CSV was generated in the working session and provided separately; the SHA-256 above identifies that exact export.


## Cross-publication duplicate-lineage check: Jiao et al. (2026)

The uploaded Jiao et al. (2026) supplementary workbook `ef6c01887_si_002.xlsx`, sheet `Experiment data from literature`, contains the Hosseini reference [2] block at Excel rows 82-145 (workbook observation numbers 80-143). The workbook reference register identifies [2] as Hosseini et al. (2022), DOI 10.1016/j.petrol.2022.110441.

A one-to-one comparison against the 64 observations in Tables S1-S4 found:

- 64/64 exact IFT matches.
- 64/64 exact pressure matches.
- 64/64 exact temperature matches.
- 64/64 matching total salt molality after summing the workbook's NaCl, KCl, CaCl2 and MgCl2 columns (the mixed NaCl/KCl component values are rounded in the workbook).
- 64/64 method codes equal 0; the workbook legend maps 0 to Pendant Drop.
- The workbook does not retain the original SI density differences or IFT uncertainty values.

This confirms that Jiao et al. [2] is a re-compilation of the Hosseini observations, not an independent experimental dataset. Retain the Hosseini 2022 table-extracted rows as canonical. Assign one unique duplicate-group ID per paired observation and exclude the Jiao workbook copies from additional independent-observation counts and model training.

The corrected extraction now has SHA-256 `0e1d4715ffd66d01ee7963652621bbfaa6dcb387920cecf69775c3d394adbc1d`. The 64 Hosseini primary-source rows are marked primary-benchmark eligible at the source-observation level. This does not certify the entire 450-row Jiao workbook or complete global overlap review across every literature source; those checks remain open.
