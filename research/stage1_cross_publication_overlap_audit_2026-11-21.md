# Stage-1 cross-publication overlap screen

**Date:** 2026-11-21  
**Input:** `data/processed/canonical/ift_source_verified_stage1_158_observations.csv`  
**Input SHA-256:** `94fde4ebfcc76ab7a12437079467dcc0e24f2cc98a5966f6802238155a25d89a`

## Dataset inventory

| Study | Observations |
|---|---:|
| Chow et al. (2018) | 79 |
| Hosseini et al. (2022) | 64 |
| Mirchi et al. (2022) | 15 |
| **Total** | **158** |

All 158 observation IDs are unique. All rows have a non-null IFT value, source coordinate, and source uncertainty record.

## Automated candidate screen

The script `scripts/audit_cross_study_overlap.py` compares cross-publication rows only when the declared electrolyte identity, electrolyte composition and gas mole fractions match.

- Exact match definition: same fluid key, pressure, temperature and IFT (floating tolerance (10^{-10})).
- Near-match thresholds: pressure ≤ 0.02 MPa, temperature ≤ 0.5 K, and IFT ≤ 0.10 mN/m.
- Exact cross-publication matches: **0**.
- Near cross-publication candidates: **0**.

This means no obvious row-level duplicated measurements were detected among the 158 canonical observations under these explicit rules.

## Manual lineage controls

1. The 64 Hosseini Jiao workbook copies are excluded from the canonical row count; the original Hosseini supporting-information rows are retained.
2. Chow's 2020 erratum corrects Table 4 headings; it is not an additional experiment or an additional observation set.
3. Mirchi Table 4 contains apparatus-validation comparisons with literature. Those validation values are not added to the 15 new H2–CH4 mixture rows in Table 6.
4. Mirchi's primary article discusses prior Chow and Hosseini measurements as literature context; those cited comparisons are not the 15 new Table 6 measurements.
5. The Jiao supplementary workbook remains a secondary compilation and is not treated as an independent source of experiments.

## Limitations and release decision

A zero automated match count **does not prove full experimental independence**. The screen cannot detect copied data with altered rounding, hidden common experimental campaigns, unreported reuse, or a value reused under different fluid metadata. Manual source review and author clarification remain necessary where lineage is ambiguous.

**Decision:** no exact or near duplicates detected in the current 158-row tranche. Keep global overlap status open until remaining study groups and external source lineages are reviewed. Do not start model training yet.
