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
3. The generated extraction has SHA-256 `736b993088600539d49dfa07771dbae68f9fa4bcb103e71c73c7ce1c0eb34cd3`.
4. Rows are marked `provenance_status=table_extracted` and reviewer status `verified` for transcription against the SI. `benchmark_eligible_primary=false` remains in place pending cross-source duplicate/overlap review, including comparison against the Jiao et al. (2026) 450-row workbook and other compilations.
5. No claim is made that the 64 rows are 64 independent experiments. They are 64 source-table observations from one study.

## Remaining work

- Compare all 64 observations against the Hosseini block in the Jiao et al. (2026) workbook, including values, uncertainty availability, chemistry and any duplicated representation.
- Resolve source lineage and independence before setting primary benchmark eligibility.
- Review the original article methods for the exact meaning of reported uncertainty and confirm any details not defined in the SI.
- Keep the old CSV unchanged; any later migration should preserve an explicit link to this audit.

## Reproducibility note

The SI source document was supplied by the user in this conversation. It is not copied into this repository. The extracted CSV was generated in the working session and provided separately; the SHA-256 above identifies that exact export.
