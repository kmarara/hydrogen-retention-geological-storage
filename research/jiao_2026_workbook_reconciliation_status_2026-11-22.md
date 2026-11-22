# Jiao 2026 workbook reconciliation status — 2026-11-22

**Workbook:** user-provided supplementary Excel workbook for Jiao et al. (2026), *Tabular Deep Learning for Hydrogen–Brine Interfacial Tension Prediction with Uncertainty Quantification*.  
**Sheet audited:** `Experiment data from literature`.  
**Workbook SHA-256:** `9ef4197720c9f37237bda9de8bc666d5deca63d209ccb24c4f957f010efb6d84`.  
**Status:** structural re-audit and reconciliation against the existing source-verification records; this is not a new primary-source extraction or a benchmark release.

## 1. Workbook integrity and structure

Direct inspection of the uploaded workbook confirms:
- 450 numbered observations, IDs 1–450, in Excel rows 3–452.
- Nine reference groups, [1]–[9], with the row allocations listed below.
- The worksheet has two header rows. The 12 principal observation fields are observation number, pressure (MPa), temperature (K), four individual salt molalities, two gas mole-fraction columns (CH4 and CO2), method code, and IFT (mN/m). The source-reference label is populated at the first row of each group and is blank on subsequent rows by design.
- The worksheet also contains a method legend: code 0 = Pendant Drop; code 1 = Sessile Drop.
- No missing values were found in the 12 principal observation fields.
- All 450 observation numbers are unique; no exact duplicate rows were found across the 12 principal observation fields.
- Observed ranges: pressure 0.1–45.2 MPa; temperature 293–448.87 K; IFT 29.56–88.99 mN/m.

The workbook is retained as immutable secondary-source evidence. Any corrected chemistry mapping or canonical record must be made in a separate derivative with a documented transformation.

## 2. Row-group reconciliation

| Jiao reference | Study | Observation IDs | Count | Existing audit disposition |
|---|---|---:|---:|---|
| [1] | Chow et al. (2018) | 1–79 | 79 | 79/79 central IFT values match corrected primary tables at workbook precision. Pendant drop verified. Ternary CO2 phase-composition values are misassigned to the workbook CH4 column; canonical mapping must distinguish feed composition from equilibrium non-aqueous-phase y_CO2. |
| [2] | Hosseini et al. (2022) | 80–143 | 64 | 64/64 match original SI, but these are duplicate representations of the 64 primary-SI observations already canonicalized. Do not count them as additional independent observations. |
| [3] | Higgs et al. (2022) | 144–179 | 36 | 36/36 match the EarthArXiv preprint appendix at displayed precision. Final published-version reconciliation and salinity-basis review remain open; quarantined. |
| [4] | Esfandyari et al. (2022) | 180–195 | 16 | 16/16 match the corrected 2023 corrigendum's distilled-water table. IFT-specific drop configuration remains unresolved. A separate 16-row formation-brine block was extracted from the corrected table but is not part of this Jiao workbook. |
| [5] | Isfehani et al. (2023) | 196–267 | 72 | 72/72 central IFT values match primary SI Tables S1–S3. Workbook CO2 fractions are placed in the CH4 column; gas-percentage basis, exact salt recipe and uncertainty remain unresolved. |
| [6] | Al-Mukainah et al. (2022) | 268–273 | 6 | Numerical conflict remains: workbook endpoints differ from source-text endpoints. Primary paper supports pendant-drop IFT, while code 1 is sessile drop. Excluded pending exact data/author clarification. |
| [7] | Mirchi et al. (2022) | 274–288 | 15 | 15/15 match primary Table 6 central values. Pendant drop and gas compositions verified; source uncertainty omitted from workbook and retained in canonical derivative. |
| [8] | Janjua et al. (2024) | 289–423 | 135 | No primary-source row-level numerical verification. Secondary Ibrahim (2025) compilation cross-check is documented separately; all 135 remain excluded pending original-source reconciliation. |
| [9] | Daraii et al. (2025/2026) | 424–450 | 27 | Structural subset and gas-mixture assignments reviewed, but no complete row-level primary numerical match. Temperature, method and salinity metadata remain unresolved; excluded. |

## 3. Reconciled evidence counts

The existing source audits, consolidated without treating secondary duplicates as new measurements, yield:

- **218 Jiao workbook rows numerically matched** at the precision and source status documented in their individual audits: Chow 79, Higgs preprint 36, corrected Esfandyari distilled-water table 16, Isfehani primary SI 72, and Mirchi 15.
- **64 Hosseini rows** also match original primary SI, but are duplicate copies of the 64 Hosseini observations already independently extracted from that SI. They are not additional observations.
- **168 rows remain numerically unresolved or conflicting:** Al-Mukainah 6, Janjua 135, Daraii 27.
- Of the 218 matched rows, the 36 Higgs records are only matched to a preprint and remain quarantined; the 16 Esfandyari records have unresolved IFT drop configuration; the 72 Isfehani records have incomplete chemistry/gas-basis/uncertainty metadata. Numerical agreement does not itself establish primary benchmark eligibility.

These categories account for all 450 workbook rows: 218 + 64 + 168 = 450. They are audit-status counts, not counts of eligible, independent training observations.

## 4. Data defects and cautions retained

1. **Chow ternary composition:** the workbook CH4 column contains source-derived non-aqueous-phase CO2 composition values for observations 44–79. Do not use these as methane fractions or as nominal feed composition.
2. **Isfehani composition:** the workbook CH4 column contains the CO2 fractions for observations 196–267, while the CO2 column is zero. Correct only in a traceable derivative.
3. **Method codes:** code 0 is Pendant Drop and code 1 is Sessile Drop according to the workbook legend. Individual primary-source audits show that the method code is incorrect or unresolved for some groups, notably Al-Mukainah and Janjua/Daraii; the legend does not validate the source method.
4. **Concentration basis:** workbook salt columns are labelled molalities, but several primary studies report different original bases (e.g., wt%, ppm or molarity). Preserve original reported concentration and record conversions separately.
5. **Publication overlap:** exact duplicates within this workbook are absent, but that does not establish independence across cited publications, secondary compilations, validation sets or shared experimental campaigns.

## 5. Primary benchmark decision

**Do not use the 450-row Jiao workbook as the canonical benchmark dataset.** It is a secondary compilation and includes duplicate representations, metadata mapping errors, incomplete primary-source verification and unresolved method/concentration details.

The current conservative stage-1 canonical candidate remains 158 observations from three primary-source studies:
- Chow et al. (2018): 79;
- Hosseini et al. (2022): 64;
- Mirchi et al. (2022): 15.

That 158-row tranche is still subject to the global lineage/overlap and release gates described in `research/consolidated_provenance_matrix_2026-11-21.md`. No model training is authorized by this audit.

## 6. Next actions

1. Continue primary-source reconciliation for the 168 unresolved/conflicting records, prioritizing Janjua (135) and Daraii (27), then Al-Mukainah (6).
2. Resolve Higgs final-version discrepancies and metadata before any admission decision.
3. Obtain missing Isfehani metadata and resolve Esfandyari IFT-specific measurement configuration.
4. Audit the external blind-test dataset and determine whether it contains records reused from any of the nine source studies or from other publications.
5. Reconstruct the paper's validation workflow only to the extent supported by its main article, SI and available code; mark omitted implementation details as unknown rather than guessing.
6. Keep the original workbook unchanged and use publication-held-out validation for the independent benchmark after all release gates pass.

**Decision:** workbook structure and group allocation re-confirmed; previous source-audit dispositions retained; no new observations promoted to primary eligibility; no model training.
