# Chow et al. (2018) primary-source verification audit

**Audit date:** 2026-11-21  
**Primary article:** Y. T. Florence Chow, Geoffrey C. Maitland and J. P. Martin Trusler, “Interfacial tensions of (H2O + H2) and (H2O + CO2 + H2) systems at temperatures of (298–448) K and pressures up to 45 MPa,” *Fluid Phase Equilibria* 475 (2018), 37–44. DOI: [10.1016/j.fluid.2018.07.022](https://doi.org/10.1016/j.fluid.2018.07.022).  
**Erratum:** *Fluid Phase Equilibria* 503 (2020), 112315. DOI: [10.1016/j.fluid.2018.07.022](https://doi.org/10.1016/j.fluid.2018.07.022) (publisher erratum record: https://www.sciencedirect.com/science/article/abs/pii/S0378381219303760).  
**Jiao workbook group:** Ref [1], observations 1–79, sheet `Experiment data from literature`.  
**Primary source inspected:** Imperial College London accepted-version PDF; publisher erratum record; NIST ThermoML bibliographic/data record.

## 1. Scope and experimental identity

The article reports new pendant-drop IFT measurements for (H2O + H2) and (H2O + CO2 + H2), at 0.5–45 MPa and approximately 298–448 K. The paper specifies a hydrogen feed of mole fraction at least 0.9999 for the binary system and a premixed feed of (0.300 ± 0.015) CO2 + (0.700) H2 for the ternary system. Deionised, vacuum-degassed water was used. Pendant drops were formed by injecting water through a capillary into the pressurised gas-containing optical cell; IFT was evaluated by axisymmetric drop-shape analysis based on the Young–Laplace equation.

The source reports 43 binary-system measurements in Table 4 and 36 ternary-system measurements in Table 6, giving 79 tabulated observations in total. This count matches the 79-row Jiao workbook group.

## 2. Numerical reconciliation

### Binary H2-water block: observations 1–43

All 43 workbook IFT central values match the primary article's Table 4 at the workbook's displayed precision (0.1 mN/m). The workbook preserves the tabulated pressure, temperature and IFT values for this block. The source table includes calculated density difference Δrho, which is not retained in the Jiao workbook.

**Erratum control is essential:** the 2020 erratum states that Table 4 column headings had been misplaced and supplies the corrected table. Use the corrected Table 4 layout when reconstructing the source columns; do not rely on the misaligned original table layout. The corrected table retains the reported IFT values and gives the correct p, T, Δrho and gamma associations.

### Ternary H2-CO2-water block: observations 44–79

All 36 workbook IFT central values match Table 6 at 0.1 mN/m precision. The pressure, temperature and IFT values correspond row-for-row to the source table. The primary article additionally reports calculated aqueous-phase mole fractions (x1, x2, x3), non-aqueous-phase mole fractions (y1, y2, y3), and density differences. These are source-derived equilibrium-phase quantities, not simply the feed-gas composition.

## 3. Metadata defect: gas composition field mapping

The Jiao workbook's gas-composition headers are CH4 and CO2. For observations 44–79, the nonzero values (approximately 0.3, varying with state point) appear in the workbook's CH4 column, while the CO2 column is zero. These values match the primary paper's calculated non-aqueous-phase CO2 mole fraction y1 (CO2), not methane mole fraction. The paper contains no methane in this system.

This is a systematic feature-mapping error in the secondary compilation. For a canonical extraction:
- set gas identity to H2 + CO2 + H2O for observations 44–79;
- store the source's nominal feed composition separately (CO2 feed mole fraction 0.300 ± 0.015; H2 balance);
- if using the state-dependent composition, store the paper's y_CO2 (non-aqueous phase) and identify its phase basis explicitly;
- do not copy the Jiao CH4 column into a canonical CH4 feature;
- do not treat y_CO2 as the nominal feed-gas composition.

For observations 1–43, gas identity is H2 + H2O and CH4/CO2 mole fractions are zero.

## 4. Method and uncertainty

The source explicitly confirms pendant-drop IFT for both systems. Jiao method code 0 (Pendant Drop) is consistent for all 79 records.

For the binary block, the paper reports an expanded combined relative IFT uncertainty at 95% confidence of 1.7%, i.e. Uc(gamma) = 0.017 gamma. It reports three repeated measurements at each state point, with average relative standard deviation 0.3% and each below 0.9%.

For the ternary block, the paper also reports three repeated measurements at each state point, average relative standard deviation 0.2%, each below 0.5%, and expanded combined relative IFT uncertainty of 1.7%. The paper explains that uncertainty includes phase-composition contributions to density difference. Do not mislabel the 1.7% expanded uncertainty as a standard deviation.

## 5. Canonical extraction completed (stage 1)

A 79-row source-level canonical tranche has been created at `data/processed/canonical/chow_mirchi_2022_ift_observations_stage1.csv` (shared file with the 15 Mirchi rows) and incorporated into the combined stage-1 dataset `data/processed/canonical/ift_source_verified_stage1_158_observations.csv`.

- 43 binary H2-water rows are mapped to corrected Table 4 records 1–43.
- 36 ternary H2-CO2-water rows are mapped to Table 6 records 1–36.
- Source pressure, temperature and IFT central values are retained; source IFT expanded uncertainty is recorded as (U_c(\gamma)=0.017\gamma) at 95% confidence.
- Ternary feed composition is stored as 0.70 H2 + 0.30 CO2; state-dependent non-aqueous-phase (y_{CO2}) is stored separately in `gas_phase_y_CO2_non_aqueous`.
- The Jiao workbook's mislabeled ternary composition field is corrected in the derivative; the original workbook remains unchanged.
- All 79 rows have exact table-record coordinates, unique IDs, grouping IDs, and source-level eligibility flags.
- Combined stage-1 snapshot: 158 rows across three studies; SHA-256 `94fde4ebfcc76ab7a12437079467dcc0e24f2cc98a5966f6802238155a25d89a`.

## 6. Benchmark disposition

- **Numerical status:** 79/79 central IFT values matched to primary tables at the workbook's displayed precision and canonicalized with source-table coordinates.
- **Provenance:** `table_extracted`; canonical row-level records now carry primary table and record coordinates.
- **Method:** pendant drop, verified.
- **Uncertainty:** source-reported expanded uncertainty, 95% confidence, 1.7% of IFT for both blocks.
- **Gas metadata:** workbook feature mapping defect for ternary block; repair in a documented derivative, never by editing the original workbook.
- **Eligibility:** source-level candidate data are canonicalized and checksummed. Do not train until global duplicate/overlap review and frozen split manifests are complete.

## 6. Reproducibility references

- Accepted-version primary article: https://spiral.imperial.ac.uk/server/api/core/bitstreams/018a296b-730e-49e9-aa0f-857488525cf5/content
- Imperial repository publication record: https://spiral.imperial.ac.uk/entities/publication/c10f4a5e-7d08-4bb7-8766-acf0adafcd05
- NIST ThermoML record: https://trc.nist.gov/ThermoML/10.1016/j.fluid.2018.07.022.html
- Publisher article DOI: https://doi.org/10.1016/j.fluid.2018.07.022
- Erratum DOI/article record: https://www.sciencedirect.com/science/article/abs/pii/S0378381219303760

This audit verifies the secondary workbook's numerical values against the primary tables; it does not certify the entire 450-row Jiao workbook or complete global duplicate review.
