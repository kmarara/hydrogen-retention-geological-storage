# Canonical dataset stage 1 — Hosseini et al. (2022)

**Audit date:** 2026-11-21  
**Status:** source-specific canonical extraction prepared; global benchmark release remains blocked pending cross-study overlap review.  
**Primary source:** Hosseini et al. (2022), DOI [10.1016/j.petrol.2022.110441](https://doi.org/10.1016/j.petrol.2022.110441), original supporting-information DOCX, Tables S1–S4.

## Extracted derivative

A 64-row canonical derivative was reconstructed from the verified primary-SI extraction preserved in the project file library.

- Output: `data/processed/canonical/hosseini_2022_ift_observations.csv` (committed)
- Rows: 64
- Columns: 38
- Provenance: all 64 rows `table_extracted`
- Reviewer status: all 64 `verified`
- Source-level eligibility flag: all 64 true, as in the verified extraction; this is **not** a declaration that the multi-study benchmark is released.
- Primary SI SHA-256: `16b6ae258043a370db31e85d5deaf5062bfbd873d3ed152762def30083b8e2d2`
- Verified source extraction SHA-256 (34 columns): `0e1d4715ffd66d01ee7963652621bbfaa6dcb387920cecf69775c3d394adbc1d`
- Canonical derivative SHA-256 (38 columns): `e4509b99ba6c578c578b159f6abfb21f8f22b893b960dd62ee5c149970a38a99`

The derivative adds four explicit grouping fields:
- `publication_group_id`: DOI:10.1016/j.petrol.2022.110441
- `experiment_group_id`: HOSSEINI_2022_PRIMARY_EXPERIMENT
- `fluid_system_group_id`: H2_PURE_WATER or H2_NACL_KCL_{1.05,3.15,4.95}_MOL_KG
- `measurement_campaign_id`: not_reported_in_source

## Chemistry and observation blocks

| Primary SI table | System | Total salt molality | Rows |
|---|---|---:|---:|
| S1 | H2 + pure water | 0.00 mol/kg | 16 |
| S2 | H2 + mixed NaCl-KCl brine | 1.05 mol/kg | 16 |
| S3 | H2 + mixed NaCl-KCl brine | 3.15 mol/kg | 16 |
| S4 | H2 + mixed NaCl-KCl brine | 4.95 mol/kg | 16 |

Mixed brine composition is 0.864 NaCl + 0.136 KCl. Original pressure, temperature, IFT, uncertainty text, density difference, source coordinates, and duplicate-group lineage are retained. The uncertainty type is not specified in the SI and must not be relabelled as standard deviation or confidence interval.

## Validation performed

- 64 rows; 38 columns.
- No missing values in the extracted derivative.
- Unique observation IDs.
- Four 16-row source-table blocks.
- All rows retain exact primary-SI source locations.
- All rows retain the Jiao 2026 secondary-compilation duplicate-group identifier; the primary Hosseini SI row is canonical and the Jiao copy must not count as an independent experiment.
- Source extraction checksum matches the previously recorded verified extraction checksum.

## Important release limitation

This is the first source-specific canonical data tranche, **not** the frozen multi-publication benchmark. Do not start model training from this tranche alone or report it as an independent train/test benchmark. The next gates are:
1. canonicalise Chow and Mirchi from their primary tables with source uncertainties and exact coordinates;
2. reconcile possible cross-paper reuse/overlap, including apparatus-validation data;
3. validate all grouping fields and conversions across the combined table;
4. freeze the complete dataset snapshot and publication-held-out split manifests.

The canonical Hosseini CSV is committed to the working branch. The combined 158-row stage-1 snapshot now includes this source plus Chow and Mirchi; see `data/processed/canonical/ift_source_verified_stage1_158_observations.csv`. Combined snapshot SHA-256: `94fde4ebfcc76ab7a12437079467dcc0e24f2cc98a5966f6802238155a25d89a`.

The original Jiao supplementary workbook remains immutable audit evidence and is not substituted for primary sources.
