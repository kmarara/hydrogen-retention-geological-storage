# Jiao et al. (2026) supplementary workbook: remaining source-group triage

**Audit date:** 2026-11-21  
**Workbook:** `ef6c01887_si_002.xlsx`, sheet `Experiment data from literature`  
**Workbook DOI:** 10.1021/acs.energyfuels.6c01887  
**Scope:** Structural triage of source groups [1] and [3]-[9], following the completed Hosseini [2] primary-source and duplicate-lineage audit. This is not yet a full row-by-row primary-source verification.

## Workbook structure

The sheet contains 450 numbered records across nine cited source groups:

| Ref | Study | Rows | Workbook observation numbers |
|---|---|---:|---:|
| [1] | Chow et al. (2018) | 79 | 1-79 |
| [2] | Hosseini et al. (2022) | 64 | 80-143 |
| [3] | Higgs et al. (2022) | 36 | 144-179 |
| [4] | Esfandyari et al. (2022) | 16 | 180-195 |
| [5] | Isfehani et al. (2023) | 72 | 196-267 |
| [6] | Al-Mukainah et al. (2022) | 6 | 268-273 |
| [7] | Mirchi et al. (2022) | 15 | 274-288 |
| [8] | Janjua et al. (2024) | 135 | 289-423 |
| [9] | Daraii et al. (2025/2026 publication record) | 27 | 424-450 |

## Source-specific triage

### [1] Chow et al. (2018) — 79 records
DOI: 10.1016/j.fluid.2018.07.022. The paper reports pendant-drop IFT measurements for H2O+H2 and H2O+CO2+H2 over 0.5-45 MPa and 298.15-448.15 K. The workbook records zero salt and varies CO2 mole fraction; its CH4 fraction is zero. The paper reports an empirical correlation and expanded IFT uncertainty. The 79 workbook rows require row-by-row matching against the primary article tables/data before eligibility is approved.

### [3] Higgs et al. (2022) — 36 records
DOI: 10.1016/j.ijhydene.2022.02.022. The study investigates H2-brine-quartz wettability and IFT using captive-bubble, pendant-drop and in-situ 3D micro-CT methods. The workbook's 36 records cover pure water and three low NaCl molalities, with pendant-drop method code 0. The published abstract reports a narrow 6.89-20.68 MPa pressure range for IFT and no clear salinity correlation over 1000 and 5000 ppm NaCl. Need match exact 36 rows against source tables/figures and separate IFT from wettability-related measurements.

### [4] Esfandyari et al. (2022) — 16 records
DOI: 10.1016/j.est.2022.104866; corrigendum DOI: 10.1016/j.est.2022.106162. The 16 workbook values are the corrected H2/distilled-water values in the corrigendum's replacement Table 2 (four pressures × four temperatures). The corrigendum states the original Figure 6 data had a systematic error due to surfactant in the experimental system and that experiments were repeated. This is a positive value-level match to the corrected publication, not to the superseded original figure. The workbook assigns method code 1 (Sessile Drop); the method metadata must be checked against the article's IFT-specific procedure before acceptance. Formation-brine values in the corrigendum are not represented in this 16-row workbook group.

### [5] Isfehani et al. (2023) — 72 records
DOI: 10.1016/j.molliq.2023.121279. The paper studies brine + H2 + CO2 systems and reports IFT changes with CO2 fraction, pressure, temperature and salinity. Workbook group has three NaCl molalities (0, 1.05, 3.15 mol/kg) and three CO2 fractions (0.3, 0.5, 0.7), with method code 0 (Pendant Drop). Need row-level match to source tables and verify whether any values were reused from other publications for method validation rather than newly measured.

### [6] Al-Mukainah et al. (2022) — 6 records
DOI: 10.1016/j.egyr.2022.07.004. Primary full text inspected (ResearchGate-hosted author-uploaded article PDF; CC BY-NC-ND 4.0). Section 2.2 explicitly distinguishes modified sessile-drop contact-angle measurements from pendant-drop H2/brine IFT measurements using Young-Laplace fitting. The six workbook rows therefore have a confirmed method-code error: workbook code 1 means Sessile Drop, but the source method for all six IFT records is Pendant Drop (code 0 in the Jiao legend). Preserve the raw workbook unchanged and record a source-backed metadata correction in the canonical extraction/audit layer.

The primary article states 10 wt% NaCl brine, 50 °C, and 14.7-1000 psi. The workbook's 1.91 mol/kg NaCl is a plausible derived conversion from 10 wt% solution (approximately 1.90 mol/kg, assuming 10 g NaCl per 100 g solution); the paper itself reports wt%, not molality. Preserve 10 wt% as the original concentration basis and label molality as a derived conversion with its calculation convention.

The six workbook pressures map closely to the paper's six plotted pressure positions (14.7, 200, 400, 600, 800, 1000 psi), and 323 K is a rounded representation of 50 °C. However, the IFT values are not yet source-verified: the workbook endpoints are 64.46 and 52.02 mN/m, while the article text explicitly reports 63.68 and 51.29 mN/m at 14.7 and 1000 psi. Figure 4's intermediate points are graphical, not tabulated in the inspected article text; visual reading is insufficient to certify exact values. Thus all six Jiao records remain excluded from primary benchmark eligibility pending recovery of the authors' underlying numerical data or exact point-level confirmation. See `research/al_mukainah_2022_source_verification_audit.md`.

### [7] Mirchi et al. (2022) — 15 records
DOI: 10.1016/j.ijhydene.2022.08.056. The study reports IFT for H2-CH4/brine mixtures and contact angles on oil-wet rocks. Workbook group uses a fixed NaCl molality of 0.349 and five gas-composition entries across CH4/CO2 columns, with method code 0. Need confirm that the source paper's measured gas mixtures and IFT data map to these columns as represented; source article includes both pendant-drop and rising/captive-bubble techniques, so method must be resolved per observation rather than inferred from a single study-level label.

### [8] Janjua et al. (2024) — 135 records
DOI: 10.1016/j.est.2024.112510. The article reports density and IFT for deionized water, seawater/mixed brine and individual NaCl, KCl, MgCl2, CaCl2 and Na2SO4 brines at 1 and 3 M, 25/50/70 °C and pressures up to 20 MPa. Workbook group has 9 salt identities/concentrations, 3 temperatures and 5 pressures, method code 1. The 135 = 9 × 3 × 5 design is structurally consistent with the reported experimental matrix. Need check the workbook's molality columns against the paper's concentration basis (the article abstract describes M concentrations) and compare exact values, including whether all 135 are direct measurements.

### [9] Daraii et al. (2025/2026) — 27 records
DOI: 10.1016/j.ptlrs.2025.11.004. The article record is in Petroleum Research volume 11, issue 2, June 2026. It reports H2-N2, H2-CO2 and H2-CH4 mixtures (70:30) in distilled water and 30,000 ppm NaCl brine at 25/50/70 °C and 1/5/10 MPa. The workbook group contains 27 rows: 3 temperatures × 3 pressures × 3 represented conditions, including CH4 and CO2 cases; it does not show an N2 column. This is a potential coverage/omission issue: the workbook subset is not the full study matrix as described in the later article abstract. The workbook reference text names a 2025 study, while the journal issue record shows publication in 2026; preserve both DOI and publication chronology accurately.

## Cross-cutting data-quality flags

1. **Method coding needs source-specific review.** The workbook's legend maps 0 to Pendant Drop and 1 to Sessile Drop. Group [6] appears to assign Sessile Drop to IFT observations although its paper describes pendant-drop IFT and sessile-drop contact-angle measurement. Group [4] also needs method verification.
2. **Concentration basis must be preserved.** Janjua's article abstract describes molar concentrations; the workbook columns are headed molalities. Do not silently treat M and mol/kg as interchangeable.
3. **Mixed-system features are not homogeneous.** Chow has CO2 composition but no salt; Isfehani has H2-CO2 and NaCl; Mirchi has H2-CH4 and CO2 composition fields; Daraii has cushion-gas mixtures. They need explicit gas identity and composition semantics, not generic CH4/CO2 columns alone.
4. **A cited source is not proof of independent measurement.** Some papers use validation measurements from earlier work. Check each row against its primary source and references before assigning independent-observation status.
5. **Corrected literature must supersede erroneous values.** For Esfandyari, use the corrigendum's corrected table and exclude any superseded Figure 6 values.

## Current decisions

- Hosseini [2]: primary-source extraction completed; 64 canonical source rows retained; 64 Jiao workbook copies identified as duplicates and excluded from independent row counts.
- Esfandyari [4]: 16/16 IFT values match the corrigendum's corrected distilled-water table; method metadata remains under review.
- All other source groups [1], [3], [5]-[9]: structurally triaged but not yet certified against primary source tables. Do not yet promote their workbook rows to primary benchmark eligibility.
- No model training or benchmark metrics are authorised by this audit.

## Immediate next verification targets

1. Resolve the method-code conflict for Al-Mukainah [6] and verify its six IFT values.
2. Verify Janjua [8] concentration units and 135-row source correspondence.
3. Verify Esfandyari [4] IFT-specific measurement method against the article.
4. Obtain primary source tables/supplementary data for Chow [1], Higgs [3], Isfehani [5], Mirchi [7], and Daraii [9].
