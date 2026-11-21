# Consolidated provenance matrix — Jiao 2026 supplementary workbook

**Status:** audit synthesis; stage-1 canonical tranche assembled, not a released benchmark dataset.  
**Audit date:** 2026-11-21  
**Secondary workbook:** `ef6c01887_si_002.xlsx`, 450 rows, nine cited study groups.  
**Purpose:** distinguish numerical source matching, metadata verification, duplicate lineage, and benchmark eligibility. A numerical match alone does not make a row benchmark-ready.

## 1. Study-level matrix

| Source study | Jiao rows | Count | Numerical comparison | Method / chemistry status | Current disposition |
|---|---:|---:|---|---|---|
| Chow et al. (2018) | 1-79 | 79 | 79/79 match corrected primary tables at workbook precision | Pendant drop verified. Ternary workbook feature mapping is wrong: source y_CO2 appears under CH4; nominal feed composition and equilibrium-phase composition must be separated. | Source-verified candidate; canonical extraction and overlap review still required. |
| Hosseini et al. (2022) | 80-143 | 64 | 64/64 match original SI exactly after correction of legacy CSV errors | Pendant drop; mixed NaCl-KCl composition; original SI includes density difference and reported uncertainty. | Jiao copies are duplicates of canonical 64-row primary-SI extraction; exclude Jiao copies from independent sample count. |
| Higgs et al. (2022) | 144-179 | 36 | 36/36 match EarthArXiv preprint appendix at displayed precision; final published numerical tables not accessible for row-by-row reconciliation | Pendant-drop IFT verified in preprint; final-version, salinity-basis and uncertainty checks remain. A 2024 synthesis flags trend inconsistency and treats Higgs data as an extra set. | Quarantined; retain as a potential external challenge set, not primary training data, pending final-source verification and discrepancy review. |
| Esfandyari et al. (2022) + 2023 corrigendum | 180-195 | 16 | 16/16 Jiao rows match corrected distilled-water Table 2; 16 additional formation-brine values now extracted directly from the same corrected Table 2 | IFT-specific drop configuration remains unresolved; formation-brine recipe/concentrations not yet fully verified. | 32 corrected central values now captured across separate distilled-water and formation-brine blocks; new 16-row formation-brine file quarantined pending chemistry/method clarification. |
| Isfehani et al. (2023) | 196-267 | 72 | **72/72 exact IFT matches** to primary SI Tables S1-S3; P/T/molality grid reconciled after rounded unit conversions. | Pendant drop confirmed by publisher abstract and Jiao method code 0. Critical Jiao mapping error: CO2 percentage stored in CH4 column for all 72 rows; corrected extraction preserves source composition wording. Salt identity/brine recipe, gas-percentage basis and uncertainty remain unreported in supplied SI. | 72 primary-SI rows extracted and source-numerically verified; retained outside eligible tranche pending metadata clarification. No data-value request email needed. |
| Al-Mukainah et al. (2022) | 268-273 | 6 | No exact row-level match; workbook endpoints conflict with source-text endpoints | Primary paper distinguishes pendant-drop IFT from sessile-drop contact-angle work; 10 wt% NaCl is source basis. | Exclude pending exact numerical source/author data; correct method metadata in derivative only. |
| Mirchi et al. (2022) | 274-288 | 15 | 15/15 match primary Table 6 central values at two-decimal precision | Pendant drop verified; five H2-CH4 mixtures; source uncertainty available but omitted from Jiao. | Source-verified candidate; canonical extraction of uncertainty and global overlap review required. |
| Janjua et al. (2024) | 289-423 | 135 | No row-level numerical match yet | DSA-100 verified; pendant/sessile configuration unresolved. Article reports M, workbook contains derived molality with undocumented conversion basis. | Exclude pending numerical data and metadata reconciliation. |
| Daraii et al. (2026 issue) | 424-450 | 27 | No row-level numerical match yet | Three of six gas/aqueous combinations appear in workbook; 293 K vs publisher 25 °C discrepancy; drop configuration unresolved. | Exclude pending full tables/author data. |

## 2. Counts and interpretation

- Total records in Jiao workbook: **450**.
- Numerically matched workbook rows at currently inspected source precision: **218** (Chow 79 + Higgs preprint 36 + Esfandyari corrected table 16 + Isfehani primary SI 72 + Mirchi 15).
- Hosseini: **64 additional primary-source observations** verified from original SI, but the 64 Jiao rows are duplicate representations and must not increase the independent observation count.
- Rows with unresolved or conflicting numerical provenance: **168** (Al-Mukainah 6 + Janjua 135 + Daraii 27). Isfehani's 72 values are now source-matched, although metadata gaps still block primary benchmark eligibility.
- The 36 Higgs matches are against a preprint, not the final published tables; a later 2024 synthesis flags trend inconsistency and treats them as an extra set, so they remain quarantined.
- The 16 Jiao Esfandyari rows match the official corrigendum's distilled-water block; a separate 16-row formation-brine block has now been extracted directly from corrected Table 2. All 32 corrected central values are captured, but IFT-specific method remains unresolved and the new brine rows are quarantined pending composition/method clarification.
- Chow, Isfehani and Mirchi have primary-source numerical reconciliations: 79 Chow rows (43 binary Table 4 + 36 ternary Table 6), 72 Isfehani SI rows, and 15 Mirchi Table 6 rows. Chow and Mirchi canonical derivatives include source uncertainty; Isfehani's supplied SI has no uncertainty field and its gas-percentage basis/salt identity remain unresolved. Global overlap/duplicate review remains open.
- These figures describe audit status, not a count of globally eligible independent measurements.

## 3. Current conservative benchmark eligibility

The source-verified stage-1 canonical tranche now contains **158 rows across three independent publications**:
- Hosseini et al. (2022): 64 original SI rows.
- Chow et al. (2018): 43 binary H2-water Table 4 rows + 36 ternary H2-CO2-water Table 6 rows.
- Mirchi et al. (2022): 15 H2-CH4/brine Table 6 rows.

All 158 have unique observation IDs, source locations, IFT values, uncertainty records, provenance labels and grouping identifiers. The combined 42-column file is `data/processed/canonical/ift_source_verified_stage1_158_observations.csv`, SHA-256 `94fde4ebfcc76ab7a12437079467dcc0e24f2cc98a5966f6802238155a25d89a`.

This is a source-verified candidate tranche, not a globally released benchmark. The global duplicate/overlap audit and split-manifest gate remain open. Esfandyari's 16 corrected values are numerically verified but the IFT drop configuration is unresolved. Higgs's 36 values remain quarantined until final-version reconciliation. Isfehani's 72 primary-SI values are now extracted and numerically reconciled, but remain outside this eligible tranche because the supplied SI does not identify the salt species/complete brine recipe, gas-percentage basis or uncertainty.

**No 450-row Jiao workbook export is approved as the benchmark dataset.** The original workbook remains immutable audit evidence.

## 4. Stage-1 cross-publication overlap screen

The 158-row source-verified tranche was screened using `scripts/audit_cross_study_overlap.py`. With matching declared electrolyte/gas composition required, the strict screen found:
- exact cross-publication matches: **0**;
- near-match candidates: **0** at thresholds ΔP ≤ 0.02 MPa, ΔT ≤ 0.5 K, and ΔIFT ≤ 0.10 mN/m.

See `research/stage1_cross_publication_overlap_audit_2026-11-21.md`. This does not prove experimental independence: manual source-lineage review remains open for unreported data reuse, altered rounding, and shared campaigns. The 64 Hosseini Jiao copies are excluded; Mirchi's apparatus-validation comparisons are not counted as new Table 6 observations; Chow's erratum is not a new experiment.

## 5. Dataset release gates

Before model training:
1. Build canonical long-form observations from original primary sources, not by blindly copying the Jiao workbook.
2. Populate every required field in `data/metadata/observation_schema.md`, including exact source coordinates, original concentration basis, gas composition, method and uncertainty.
3. Keep reported source values distinct from derived conversions and phase-specific equilibrium compositions.
4. Assign source-study, original-experiment, publication, fluid-system and measurement-campaign group IDs.
5. Identify reused validation measurements and cross-publication duplicate lineages.
6. Resolve source-level exclusions and reviewer decisions in an auditable change log.
7. Run schema, unit, uniqueness, conversion and duplicate tests.
8. Freeze and checksum the first eligible dataset snapshot and split manifests.
9. Only then train TabPFN, TabM, boosted-tree baselines and empirical correlations on matched folds.

## 6. Immediate next actions

1. Obtain Daraii's complete primary tables or author-supplied numerical data; resolve 293 K versus 25 °C, source coordinates, uncertainty, concentration basis and drop configuration.
2. Complete final-version source reconciliation for Higgs.
3. Obtain full numerical sources for Isfehani and Janjua.
4. Request exact Al-Mukainah point values or original data file because the workbook endpoints conflict with article text.
5. Continue canonicalizing Esfandyari only if the IFT method can be resolved; otherwise retain a method-unknown sensitivity candidate.
6. Run cross-source duplicate/overlap review, particularly for apparatus-validation points and reused literature data.

**Decision:** stage-1 canonical extraction is complete for 158 source-level candidate observations. The first automated overlap screen found no exact or near matches, but manual lineage review and schema/conversion tests remain. Do not start model training yet.


## 7. Isfehani primary-SI reconciliation update (2026-11-21)

The supplied Isfehani supporting information contains 72 primary numerical observations in Tables S1-S3 (pages 2-4). All 72 were matched one-to-one to Jiao Ref [5], observations 196-267, with **72/72 exact IFT central-value matches**. Pressure, temperature and molality combinations reconcile after accounting for rounded MPa/K values in Jiao.

A secondary-workbook species mapping error was identified: the Isfehani CO2 percentages are stored in the Jiao `CH4` column, while the Jiao `CO2` column is zero, for all 72 rows. The corrected extraction does not preserve this erroneous CH4 assignment.

The local 72-row extraction is `/mnt/data/recovered/isfehani_2023_ift_observations.csv`; a 230-row local extracted inventory combines the 158 prior candidate rows with the 72 Isfehani rows. These files are locally prepared; the 158-row eligible candidate tranche remains unchanged.

The 72 Isfehani rows are source-numerically verified, with pendant-drop method supported by the publisher abstract and workbook method code 0. They remain `benchmark_eligible_primary=false` because the supplied SI does not specify salt identity/complete brine recipe, gas percentage basis, or measurement uncertainty/repeatability. No missing chemistry is inferred from other publications.


## 8. Janjua secondary-compilation cross-check (2026-11-21)

The Jiao 2026 workbook was re-uploaded and observations 289–423 (135 Janjua-labelled rows) were compared with the 180 Janjua-labelled rows extracted from Ibrahim 2025 supplementary Table S1.

- 135/135 Jiao observations have a corresponding P-T condition in the Ibrahim block after converting psi to MPa and °F to K; maximum absolute coordinate differences are approximately 0.00521 MPa and 0.15 K.
- 134/135 IFT pairs agree within 0.05 mN/m; 13/135 are numerically identical at the displayed precision; mean absolute difference is approximately 0.02644 mN/m.
- One unresolved mismatch: Jiao observation 396 = 74.46 mN/m versus Ibrahim secondary row 183 = 74.80 mN/m (CaCl2, 10 MPa, approximately 298 K).
- The 45 Ibrahim rows not represented in Jiao are 15 seawater and 30 Na2SO4 rows.
- Ibrahim prints both repeated CaCl2 blocks and both repeated MgCl2 blocks as 1M. Jiao distinguishes lower/higher molality-like values for these blocks, but this does not authorise relabelling the second Ibrahim blocks as 3M. Original Janjua source confirmation remains necessary.
- Jiao method code 1 maps to Sessile Drop in the Jiao legend, but Janjua's primary-source DSA-100 description does not verify the drop configuration.

This is a cross-check between two secondary compilations, not primary-source verification or independent experimental replication. All 135 Jiao and 180 Ibrahim Janjua-derived rows remain excluded from primary benchmark training. See the detailed Janjua audit for the comparison protocol and unresolved evidence needs.
