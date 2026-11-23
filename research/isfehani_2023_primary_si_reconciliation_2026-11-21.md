# Isfehani et al. (2023): primary supplementary-information reconciliation

**Date:** 2026-11-21  
**Primary study:** Isfehani ZD, Sheidaie A, Hosseini M, Fahimpour J, Iglauer S, Keshavarz A (2023), *Interfacial tensions of (brine + H2 + CO2) systems at gas geo-storage conditions*, Journal of Molecular Liquids 374, 121279. DOI: 10.1016/j.molliq.2023.121279.  
**Secondary compilation:** Jiao et al. (2026), supporting-information workbook Ref [5], observations 196-267.

## Primary-source tables inspected

The supplied four-page supporting-information DOCX contains three tables:

| Primary SI table | Page | Gas mixture as printed | Rows |
|---|---:|---|---:|
| Table S1 | 2 | 70% CO2 + 30% H2 | 24 |
| Table S2 | 3 | 50% CO2 + 50% H2 | 24 |
| Table S3 | 4 | 30% CO2 + 70% H2 | 24 |
| **Total** | | | **72** |

Each table spans two temperatures (50 and 80 °C), three reported molality values (0, 1.05 and 3.15 mol/kg), and four pressures (500, 1200, 2000 and 3000 psi). The table data were transcribed from the left and right blocks, preserving table/page/data-row coordinates.

## Reconciliation result

- Primary SI observations extracted: **72**.
- Jiao Ref [5] observations inspected: **72** (observation numbers 196-267).
- One-to-one matched records: **72/72**.
- Exact IFT central-value matches: **72/72** at source precision (two decimal places).
- Pressure, temperature and molality combinations: all reconcile after allowing for Jiao's rounded conversions from psi to MPa and °C to K.
- Jiao method code: 0 for all 72 rows. The workbook legend maps code 0 to Pendant Drop; the publisher abstract independently confirms pendant-drop IFT measurements.

This confirms the Jiao workbook's Isfehani central IFT values are faithful copies of the primary supplementary tables at displayed precision. It does not make the Jiao workbook an independent source.

## Secondary-workbook gas-species mapping error

For all 72 rows, Jiao stores the primary SI's CO2 percentage (0.3, 0.5 or 0.7) in the workbook's **CH4** column and leaves its **CO2** column at zero. The primary SI table titles explicitly identify CO2 + H2 mixtures. This is a systematic species/feature mapping error in the secondary workbook.

The corrected extraction preserves the primary SI wording and does not propagate the erroneous Jiao CH4 assignment into corrected CH4/CO2 numerical feature fields. The original workbook remains unchanged.

## Source and derived fields

- Original pressure retained in psi; normalized pressure calculated with 1 psi = 0.006894757293168 MPa.
- Original temperature retained in °C; normalized temperature calculated by adding 273.15.
- Original molality values retained as reported (0, 1.05, 3.15 mol/kg).
- Original IFT retained in mN/m.
- Exact source location recorded by table, page, data row and left/right temperature block.
- Duplicate lineage links each primary row to its matching Jiao workbook observation number.
- Measurement method recorded as pendant drop, supported by the publisher abstract and Jiao's code 0.
- No measurement uncertainty/repeatability value is reported in the supplied SI; the canonical uncertainty field is blank.

## Metadata gaps and eligibility

The supplied SI does not identify the salt species or full brine recipe, does not explicitly state the basis of the gas percentages, and does not report uncertainty/repeatability. Those fields are not filled by importing information from other papers, including later Isfehani studies.

All 72 rows are labelled `table_extracted` and `verified_with_metadata_gaps`, but `benchmark_eligible_primary=false`. They are retained as source-verified experimental observations outside the eligible model-training tranche until the missing chemistry and uncertainty metadata are clarified.

## Reproducibility artifacts

- Primary SI SHA-256: `61066a67d6e70991a3e0f60c476df23c143f802b2764b1c7fe194f3a07e0c033`.
- Jiao workbook SHA-256: `9ef4197720c9f37237bda9de8bc666d5deca63d209ccb24c4f957f010efb6d84`.
- Local 72-row derivative SHA-256: `02165e8fabe442b976716d5220e104253676f5c42f3fb39af64e3f4dc68c25cd`.
- Local 230-row extracted inventory SHA-256: `853a8c37882e94d53f8c304f4ac07c08ee49db3379e82afb03fe02867a59ac31`.

## Email decision

A request to Dr Mirhasan Hosseini for the 72 numerical values is no longer needed. A short clarification request may still be justified for (1) salt identity and brine preparation, (2) gas percentage basis, (3) uncertainty/repeatability, and (4) any reused validation measurements.

## Sources

- Primary supporting information supplied in this conversation, Tables S1-S3, pages 2-4.
- Publisher article record: https://www.sciencedirect.com/science/article/pii/S016773222300082X
- ECU repository record: https://ro.ecu.edu.au/ecuworks2022-2026/1859/
- DOI: https://doi.org/10.1016/j.molliq.2023.121279
