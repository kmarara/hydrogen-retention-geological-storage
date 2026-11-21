# Consolidated provenance matrix — Jiao 2026 supplementary workbook

**Status:** audit synthesis; not a released benchmark dataset.  
**Audit date:** 2026-11-21  
**Secondary workbook:** `ef6c01887_si_002.xlsx`, 450 rows, nine cited study groups.  
**Purpose:** distinguish numerical source matching, metadata verification, duplicate lineage, and benchmark eligibility. A numerical match alone does not make a row benchmark-ready.

## 1. Study-level matrix

| Source study | Jiao rows | Count | Numerical comparison | Method / chemistry status | Current disposition |
|---|---:|---:|---|---|---|
| Chow et al. (2018) | 1-79 | 79 | 79/79 match corrected primary tables at workbook precision | Pendant drop verified. Ternary workbook feature mapping is wrong: source y_CO2 appears under CH4; nominal feed composition and equilibrium-phase composition must be separated. | Source-verified candidate; canonical extraction and overlap review still required. |
| Hosseini et al. (2022) | 80-143 | 64 | 64/64 match original SI exactly after correction of legacy CSV errors | Pendant drop; mixed NaCl-KCl composition; original SI includes density difference and reported uncertainty. | Jiao copies are duplicates of canonical 64-row primary-SI extraction; exclude Jiao copies from independent sample count. |
| Higgs et al. (2022) | 144-179 | 36 | 36/36 match EarthArXiv preprint appendix at displayed precision | Pendant drop verified in preprint; final published-version reconciliation and salinity-basis/uncertainty review remain. | Quarantine pending final-version reconciliation. |
| Esfandyari et al. (2022) + 2023 corrigendum | 180-195 | 16 | 16/16 match corrected Table 2; superseded contaminated Figure 6 must not be used | IFT-specific drop configuration remains unresolved; workbook says Sessile Drop but that label is not confirmed. | Corrected numerical values verified; retain method as unknown and resolve before method-conditioned analysis/release. |
| Isfehani et al. (2023) | 196-267 | 72 | No row-level numerical match yet | Pendant-drop method confirmed by abstract; row-level conditions, exact chemistry, source coordinates and overlap unresolved. | Exclude pending primary tables/data. |
| Al-Mukainah et al. (2022) | 268-273 | 6 | No exact row-level match; workbook endpoints conflict with source-text endpoints | Primary paper distinguishes pendant-drop IFT from sessile-drop contact-angle work; 10 wt% NaCl is source basis. | Exclude pending exact numerical source/author data; correct method metadata in derivative only. |
| Mirchi et al. (2022) | 274-288 | 15 | 15/15 match primary Table 6 central values at two-decimal precision | Pendant drop verified; five H2-CH4 mixtures; source uncertainty available but omitted from Jiao. | Source-verified candidate; canonical extraction of uncertainty and global overlap review required. |
| Janjua et al. (2024) | 289-423 | 135 | No row-level numerical match yet | DSA-100 verified; pendant/sessile configuration unresolved. Article reports M, workbook contains derived molality with undocumented conversion basis. | Exclude pending numerical data and metadata reconciliation. |
| Daraii et al. (2026 issue) | 424-450 | 27 | No row-level numerical match yet | Three of six gas/aqueous combinations appear in workbook; 293 K vs publisher 25 °C discrepancy; drop configuration unresolved. | Exclude pending full tables/author data. |

## 2. Counts and interpretation

- Total records in Jiao workbook: **450**.
- Numerically matched workbook rows at currently inspected source precision: **146** (Chow 79 + Higgs preprint 36 + Esfandyari corrected table 16 + Mirchi 15).
- Hosseini: **64 additional primary-source observations** verified from original SI, but the 64 Jiao rows are duplicate representations and must not increase the independent observation count.
- Rows with unresolved or conflicting numerical provenance: **240** (Isfehani 72 + Al-Mukainah 6 + Janjua 135 + Daraii 27).
- The 36 Higgs matches are against a preprint, not yet the final published version.
- The 16 Esfandyari matches are against the official corrigendum replacement table; method remains unresolved.
- Chow and Mirchi have been canonicalized: 79 Chow rows (43 binary Table 4 + 36 ternary Table 6) and 15 Mirchi Table 6 rows, including source uncertainty and corrected gas-composition semantics. Global overlap/duplicate review remains open.
- These figures describe audit status, not a count of globally eligible independent measurements.

## 3. Current conservative benchmark eligibility

The source-verified stage-1 canonical tranche now contains **158 rows across three independent publications**:
- Hosseini et al. (2022): 64 original SI rows.
- Chow et al. (2018): 43 binary H2-water Table 4 rows + 36 ternary H2-CO2-water Table 6 rows.
- Mirchi et al. (2022): 15 H2-CH4/brine Table 6 rows.

All 158 have unique observation IDs, source locations, IFT values, uncertainty records, provenance labels and grouping identifiers. The combined 42-column file is `data/processed/canonical/ift_source_verified_stage1_158_observations.csv`, SHA-256 `94fde4ebfcc76ab7a12437079467dcc0e24f2cc98a5966f6802238155a25d89a`.

This is a source-verified candidate tranche, not a globally released benchmark. The global duplicate/overlap audit and split-manifest gate remain open. Esfandyari's 16 corrected values are numerically verified but the IFT drop configuration is unresolved. Higgs's 36 values remain quarantined until final-version reconciliation.

**No 450-row Jiao workbook export is approved as the benchmark dataset.** The original workbook remains immutable audit evidence.

## 4. Dataset release gates

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

## 5. Immediate next actions

1. Obtain Daraii's complete primary tables or author-supplied numerical data; resolve 293 K versus 25 °C, source coordinates, uncertainty, concentration basis and drop configuration.
2. Complete final-version source reconciliation for Higgs.
3. Obtain full numerical sources for Isfehani and Janjua.
4. Request exact Al-Mukainah point values or original data file because the workbook endpoints conflict with article text.
5. Continue canonicalizing Esfandyari only if the IFT method can be resolved; otherwise retain a method-unknown sensitivity candidate.
6. Run cross-source duplicate/overlap review, particularly for apparatus-validation points and reused literature data.

**Decision:** stage-1 canonical extraction is complete for 158 source-level candidate observations. Proceed to cross-publication overlap/duplicate review, schema/conversion tests and a documented release decision. Do not start model training yet.
