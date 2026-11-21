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

### [1] Chow et al. (2018) — 79 records — primary numerical audit completed
DOI: 10.1016/j.fluid.2018.07.022; erratum in *Fluid Phase Equilibria* 503 (2020), 112315. Direct comparison against the Imperial College accepted-version primary PDF and corrected Table 4 in the erratum confirms all 43 H2-water observations (Jiao observations 1–43) match Table 4 at 0.1 mN/m precision, and all 36 H2-CO2-water observations (44–79) match Table 6 at the same precision. The erratum corrects misplaced Table 4 column headings; use its corrected table layout for source coordinates and p/T/Δρ/IFT associations. The paper confirms pendant-drop IFT for both systems. Expanded combined IFT uncertainty is 1.7% at 95% confidence for both blocks; repeatability statistics are separately reported. **Important secondary-workbook defect:** the 36 ternary rows place the state-dependent non-aqueous-phase CO2 mole fractions (source Table 6 y1) under the workbook CH4 column, while the CO2 column is zero. The source system contains CO2/H2, not CH4. Canonical extraction must separate nominal feed composition (CO2 0.300 ± 0.015; H2 balance) from equilibrium-phase y_CO2 and must not copy the erroneous CH4 field. Classify as source-verified candidate data, but retain the global overlap/schema release gate. See `research/chow_2018_source_verification_audit.md`.

### [3] Higgs et al. (2022) — 36 records
DOI: 10.1016/j.ijhydene.2022.02.022. The study investigates H2-brine-quartz wettability and IFT using captive-bubble, pendant-drop and in-situ 3D micro-CT methods. The workbook's 36 records cover pure water and three low NaCl molalities, with pendant-drop method code 0. The published abstract reports a narrow 6.89-20.68 MPa pressure range for IFT and no clear salinity correlation over 1000 and 5000 ppm NaCl. Need match exact 36 rows against source tables/figures and separate IFT from wettability-related measurements.

### [4] Esfandyari et al. (2022) — 16 records
DOI: 10.1016/j.est.2022.104866; corrigendum DOI: 10.1016/j.est.2022.106162. Direct row-by-row comparison confirms all 16 Jiao workbook IFT values exactly match the corrigendum's replacement Table 2 for H2/distilled water: four pressures (10, 40, 70, 100 bar) × four temperatures (20, 40, 60, 80 °C). Workbook pressure values (1, 4, 7, 10 MPa) are exact bar-to-MPa conversions; temperatures (293, 313, 333, 353 K) are rounded Kelvin representations of 20, 40, 60, 80 °C. The corrigendum states the original Figure 6 data had a systematic error due to surfactant contamination and that all experiments were repeated; the replacement Table 2 is the authoritative numerical source. This is a fully verified numerical match to corrected data, not to superseded Figure 6.

The workbook assigns method code 1 (Sessile Drop) to these IFT rows. The accessible publisher abstract and institutional record do not expose the IFT-specific drop configuration in the original methods section. Do not infer the method from the instrument or from the contact-angle technique. Method code therefore remains unverified pending inspection of the full methods text or author confirmation. Formation-brine values in the corrigendum are not represented in this 16-row workbook group. Retain the 16 values as source-verified corrected observations, but keep method as unresolved metadata and do not use the method feature as if it were verified. See research/esfandyari_2022_source_verification_audit.md.

### [5] Isfehani et al. (2023) — 72 records
DOI: 10.1016/j.molliq.2023.121279. The paper studies brine + H2 + CO2 systems and reports IFT changes with CO2 fraction, pressure, temperature and salinity. Workbook group has three NaCl molalities (0, 1.05, 3.15 mol/kg) and three CO2 fractions (0.3, 0.5, 0.7), with method code 0 (Pendant Drop). Need row-level match to source tables and verify whether any values were reused from other publications for method validation rather than newly measured.

### [6] Al-Mukainah et al. (2022) — 6 records
DOI: 10.1016/j.egyr.2022.07.004. Primary full text inspected (ResearchGate-hosted author-uploaded article PDF; CC BY-NC-ND 4.0). Section 2.2 explicitly distinguishes modified sessile-drop contact-angle measurements from pendant-drop H2/brine IFT measurements using Young-Laplace fitting. The six workbook rows therefore have a confirmed method-code error: workbook code 1 means Sessile Drop, but the source method for all six IFT records is Pendant Drop (code 0 in the Jiao legend). Preserve the raw workbook unchanged and record a source-backed metadata correction in the canonical extraction/audit layer.

The primary article states 10 wt% NaCl brine, 50 °C, and 14.7-1000 psi. The workbook's 1.91 mol/kg NaCl is a plausible derived conversion from 10 wt% solution (approximately 1.90 mol/kg, assuming 10 g NaCl per 100 g solution); the paper itself reports wt%, not molality. Preserve 10 wt% as the original concentration basis and label molality as a derived conversion with its calculation convention.

The six workbook pressures map closely to the paper's six plotted pressure positions (14.7, 200, 400, 600, 800, 1000 psi), and 323 K is a rounded representation of 50 °C. However, the IFT values are not yet source-verified: the workbook endpoints are 64.46 and 52.02 mN/m, while the article text explicitly reports 63.68 and 51.29 mN/m at 14.7 and 1000 psi. Figure 4's intermediate points are graphical, not tabulated in the inspected article text; visual reading is insufficient to certify exact values. Thus all six Jiao records remain excluded from primary benchmark eligibility pending recovery of the authors' underlying numerical data or exact point-level confirmation. See `research/al_mukainah_2022_source_verification_audit.md`.

### [7] Mirchi et al. (2022) — 15 records
DOI: 10.1016/j.ijhydene.2022.08.056. Full publisher HTML and Table 6 inspected. All 15 Jiao workbook IFT values (observations 274-288) match the primary Table 6 central values exactly at two-decimal precision. The five gas mixtures are 100/0, 80/20, 50/50, 40/60 and 20/80 H2/CH4; workbook CH4 fractions 0, 0.2, 0.5, 0.6 and 0.8 are correct and H2 is the balance. The source confirms pendant-drop IFT; sessile-drop/captive-bubble is for contact-angle work. The paper reports 2 wt% NaCl (20,000 ppm), while workbook 0.349 mol/kg is a derived conversion (2 g NaCl / 58.44 g mol-1 / 0.098 kg water = 0.3489 mol/kg). Source conditions are 1000 psi and 22, 40, 60 °C; workbook 6.89 MPa and 295, 313, 333 K are rounded conversions. Table 6 reports uncertainty for every observation, omitted from Jiao; capture it separately and verify its definition before assigning statistical semantics. Table 4 includes apparatus-validation literature comparisons, not additional H2-CH4 mixture observations. Classify the 15 records as table_extracted and eligible for the source-verified layer subject to global duplicate/overlap and schema validation. See research/mirchi_2022_source_verification_audit.md.

### [8] Janjua et al. (2024) — 135 records
DOI: 10.1016/j.est.2024.112510. The primary publisher abstract and KFUPM institutional record confirm density measurements using an Anton Paar DMA-HP densitometer and IFT measurements using a Krüss DSA-100. The published design is five pressures (0.1, 5, 10, 15, 20 MPa), three temperatures (25, 50, 70 °C), and DI water, seawater/mixed brine, and five individual salts (NaCl, KCl, MgCl2, CaCl2, Na2SO4) at 1 and 3 M. This is 12 fluid conditions × 15 P-T combinations = 180 IFT conditions if the full matrix was completed.

Direct inspection of Jiao workbook observations 289-423 confirms 135 rows: exactly nine fluid conditions × 15 P-T combinations. The represented conditions are DI water plus 1 M and 3 M nominal solutions for NaCl, KCl, CaCl2 and MgCl2. The workbook has no seawater or Na2SO4 records. Thus it is a 135-row subset of the article's stated 12-condition design, not a complete transcription of the published design. All nine conditions contain the full 5-pressure × 3-temperature grid. Workbook temperatures are rounded to 298, 323 and 343 K, corresponding approximately to 25, 50 and 70 °C; preserve the workbook precision and record the source nominal temperatures separately.

The paper's abstract describes salt-solution concentrations as 1 and 3 M (mol/L), whereas Jiao's columns are explicitly labelled molalities (mol/kg). The workbook values are not simply 1 and 3 for every salt: NaCl 1.00/3.21; KCl 1.00/3.47; CaCl2 1.05/3.28; MgCl2 1.00/3.23 mol/kg. These are plausible M-to-m conversions, but the conversion calculation, density basis, and source coordinate are not documented in the workbook. Treat molality as a secondary derived feature pending confirmation of the authors' preparation densities/conversion procedure; do not overwrite the original 1/3 M basis.

The workbook assigns method code 1 (Sessile Drop) to all 135 IFT records. The publisher abstract identifies a Krüss DSA-100 but the accessible abstract/institutional record does not specify the IFT drop configuration. A DSA-100 instrument alone does not establish pendant versus sessile drop. Method therefore remains unverified.

The exact 135 IFT values have not yet been compared row-by-row with primary tables, figures or an author data file. Keep all 135 rows quarantined from primary benchmark eligibility until the numerical source and extraction coordinates are obtained. See `research/janjua_2024_source_verification_audit.md`.

### [9] Daraii et al. (2026 issue; DOI registered 2025) — 27 records — structural and publisher-metadata audit completed; numerical verification pending
DOI: 10.1016/j.ptlrs.2025.11.004. The publisher's journal page identifies *Petroleum Research* 11(2), pp. 545-555, with issue publication date 2026-06-10; the same page separately displays an online date of 2026-07-29. Preserve both publisher date fields pending clarification. The article reports systematic IFT and density measurements for H2-N2, H2-CO2 and H2-CH4 mixtures (70:30 mol%) in distilled water and 30,000 ppm NaCl brine, at 25, 50 and 70 °C and 1, 5 and 10 MPa. This is a 3 gas × 2 aqueous-phase × 3 temperature × 3 pressure design (54 conditions).

Direct inspection of Jiao workbook observations 424-450 confirms only 27 records (three 9-condition blocks): 424-432 H2-CH4/distilled water; 433-441 H2-CH4/NaCl brine; 442-450 H2-CO2/NaCl brine. The workbook therefore omits all H2-N2 records and the H2-CO2/distilled-water block. It is a 27-row subset, not a full transcription of the 54-condition programme. Workbook temperatures are 293, 323 and 343 K, while publisher abstract reports 25, 50 and 70 °C; 323 and 343 K are rounded equivalents of 50 and 70 °C, but 293 K is approximately 20 °C, not 25 °C. Preserve this mismatch; do not silently normalize 293 K to 298.15 K.

The workbook encodes CH4=0.3 for H2-CH4 rows and CO2=0.3 for H2-CO2 rows, consistent with the 70:30 molar gas mixtures. Its NaCl field is 0.514 mol/kg for brine records, whereas the article reports 30,000 ppm; retain the source's ppm basis and treat 0.514 mol/kg as a derived workbook quantity pending documented conversion convention and density basis. The workbook codes all rows as Method=1 (Sessile Drop), but the publisher page only identifies a high-pressure/high-temperature drop tensiometer. This does not establish the IFT drop configuration; leave method unresolved.

The publisher abstract reports selected H2-CH4 endpoints (69.4 mN/m in distilled water and 61.3 mN/m in brine at 25 °C and 1 MPa; 57.3 and 47.8 mN/m respectively at 70 °C, with the exact pressure context of the latter endpoints not explicit in the abstract). These cannot be used as direct row matches to workbook temperatures 293 K and 343 K without the full tables. The accessible publisher page's full-text section does not expose numerical tables; all 27 IFT central values therefore remain unverified. No row-level source coordinates, uncertainty values, or measurement configuration are certified. Keep all 27 rows excluded from primary benchmark eligibility pending full article tables/PDF or author data and row-by-row reconciliation. See `research/daraii_2026_source_verification_audit.md`.
### [1] Chow et al. (2018) — 79 records
DOI: 10.1016/j.fluid.2018.07.022. All 79 IFT central values match primary tables at workbook precision (43 binary H2-water rows from corrected Table 4; 36 ternary H2-CO2-water rows from Table 6). Pendant-drop method and 1.7% expanded IFT uncertainty at 95% confidence are verified. The 2020 erratum corrects Table 4 column headings and must govern source-coordinate reconstruction. Jiao's 36 ternary rows have a systematic gas-feature mapping defect: source y_CO2 is stored under CH4 while CO2 is zero. Repair only in canonical derivative and preserve source feed composition separately. See `research/chow_2018_source_verification_audit.md`.

## Cross-cutting data-quality flags

1. **Gas-feature mapping needs source-specific review.** Chow's 36 ternary rows store source y_CO2 under CH4; canonical gas identity and phase basis must be corrected.\n2. **Method coding needs source-specific review.** The workbook's legend maps 0 to Pendant Drop and 1 to Sessile Drop. Group [6] appears to assign Sessile Drop to IFT observations although its paper describes pendant-drop IFT and sessile-drop contact-angle measurement. Group [4] also needs method verification.
2. **Concentration basis must be preserved.** Janjua's published design is specified at 1 and 3 M, while the Jiao workbook contains salt-specific molality values that appear to be converted quantities. Keep M as the reported basis and molality as derived pending documented conversion. The workbook also omits seawater and Na2SO4 conditions from the article's stated design.
3. **Mixed-system features are not homogeneous.** Chow has CO2 composition but no salt; Isfehani has H2-CO2 and NaCl; Mirchi has H2-CH4 and CO2 composition fields; Daraii has cushion-gas mixtures. They need explicit gas identity and composition semantics, not generic CH4/CO2 columns alone.
4. **A cited source is not proof of independent measurement.** Some papers use validation measurements from earlier work. Check each row against its primary source and references before assigning independent-observation status.
5. **Corrected literature must supersede erroneous values.** For Esfandyari, use the corrigendum's corrected table and exclude any superseded Figure 6 values.

## Current decisions

- Hosseini [2]: primary-source extraction completed; 64 canonical source rows retained; 64 Jiao workbook copies identified as duplicates and excluded from independent row counts.
- Esfandyari [4]: all 16 IFT values match the corrigendum's corrected distilled-water Table 2 exactly; method code remains unverified pending full methods text.
- Chow [1]: all 79 IFT central values numerically matched to primary tables; gas-feature mapping defect documented; canonical extraction and global overlap review remain.
- Daraii [9]: 27-row workbook subset structurally mapped to the publisher's 54-condition design; all 27 IFT values remain unverified and excluded.
- Other source groups [3], [5], [6], [8]: remain unverified or quarantined as detailed above. Do not promote workbook rows to primary benchmark eligibility.
- No model training or benchmark metrics are authorised by this audit.

## Immediate next verification targets

1. Resolve the method-code conflict for Al-Mukainah [6] and verify its six IFT values.
2. Janjua [8]: 135-row design subset structurally audited; obtain primary numerical data and confirm molarity-to-molality conversion and IFT drop configuration.
3. Esfandyari [4]: 16 corrected IFT values verified exactly against corrigendum Table 2; resolve only the drop-method metadata from full article methods or author confirmation.
4. Obtain primary source tables/supplementary data for Chow [1], Higgs [3], Isfehani [5], Mirchi [7], and Daraii [9].
