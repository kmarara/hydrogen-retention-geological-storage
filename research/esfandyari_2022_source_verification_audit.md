# Esfandyari et al. (2022): corrected IFT data verification audit

**Audit date:** 2026-11-21  
**Original article:** Esfandyari H, Sarmadivaleh M, Esmaeilzadeh F, Ali M, Iglauer S, Keshavarz (2022). “Experimental evaluation of rock mineralogy on hydrogen-wettability: Implications for hydrogen geo-storage.” *Journal of Energy Storage* 52, 104866. DOI: https://doi.org/10.1016/j.est.2022.104866.  
**Corrigendum:** *Journal of Energy Storage* 57 (2023), 106162. DOI: https://doi.org/10.1016/j.est.2022.106162.  
**Jiao source group:** Reference [4], workbook observations 180–195 (16 records).

## Why the corrigendum is authoritative

The corrigendum explicitly states that the data originally presented in Figure 6 had a systematic error caused by surfactant in the experimental system. The authors repeated all H2/distilled-water and H2/formation-brine IFT experiments and replaced Figure 6 with a corrected Table 2. Therefore the corrected Table 2, not the superseded original Figure 6, is the valid source for these observations.

## Exact comparison: 16/16 values match

The Jiao workbook observations 180–195 correspond to the H2/distilled-water portion of corrected Table 2.

| Pressure (MPa, workbook) | Pressure (bar, corrigendum) | T (K, workbook) | T (°C, corrigendum) | IFT (mN/m) |
|---:|---:|---:|---:|---:|
| 1 | 10 | 293 | 20 | 60.6 |
| 4 | 40 | 293 | 20 | 60.2 |
| 7 | 70 | 293 | 20 | 59.2 |
| 10 | 100 | 293 | 20 | 58.8 |
| 1 | 10 | 313 | 40 | 62.8 |
| 4 | 40 | 313 | 40 | 61.4 |
| 7 | 70 | 313 | 40 | 61.2 |
| 10 | 100 | 313 | 40 | 60.8 |
| 1 | 10 | 333 | 60 | 70.4 |
| 4 | 40 | 333 | 60 | 68.5 |
| 7 | 70 | 333 | 60 | 68.2 |
| 10 | 100 | 333 | 60 | 67.5 |
| 1 | 10 | 353 | 80 | 71.0 |
| 4 | 40 | 353 | 80 | 70.2 |
| 7 | 70 | 353 | 80 | 69.3 |
| 10 | 100 | 353 | 80 | 68.4 |

**Result:** all 16 IFT values match the corrected Table 2 exactly, with zero numerical discrepancies.

The workbook pressures are exact conversions from bar to MPa. Workbook temperatures are rounded integer-kelvin representations of the corrigendum's Celsius setpoints: 20 °C = 293.15 K, 40 °C = 313.15 K, 60 °C = 333.15 K, and 80 °C = 353.15 K. Preserve original source temperatures in °C and retain workbook rounded K values as compiled values rather than silently adding precision.

## Coverage limitation

The corrigendum Table 2 also reports 16 H2/formation-brine values, but the 16-row Jiao group represents only the H2/distilled-water block. It must not be described as the complete corrected IFT dataset from this paper. The omitted formation-brine block should be considered for separate extraction if its electrolyte composition and conditions can be captured from the original article/supplementary information.

## Method metadata remains unresolved

The Jiao workbook assigns method code 1 (Sessile Drop) to all 16 IFT observations. The accessible publisher abstract and institutional repository record establish that the paper measured H2/aqueous-phase IFT and rock/H2/brine contact angles, but they do not expose the exact IFT-specific drop configuration in the original methods section. A drop-shape analyser can support different configurations, and the contact-angle method cannot be automatically assigned to the IFT measurement. Thus:
- Numerical values: verified against corrected Table 2.
- P/T mapping: verified, with workbook rounding noted.
- IFT-specific measurement method: unresolved.
- Do not silently change code 1 to Pendant Drop or treat it as verified Sessile Drop.
- Keep method as unknown/unverified in the canonical record until full methods text or author confirmation resolves it.

## Benchmark decision

The 16 numerical observations are source-verified corrected measurements and are suitable for a source-verified dataset layer, provided method metadata is explicitly marked unresolved and the data provenance points to the corrigendum Table 2. For the primary model comparison, either retain these rows with an explicit unknown method category and run a sensitivity analysis excluding them, or conservatively exclude them from method-conditioned analyses until the method is resolved.

Do not exclude the values merely because the original paper required a corrigendum; the corrected table is the authoritative published record. Do not use the superseded Figure 6 values.

## Sources and coordinates

- Corrigendum DOI 10.1016/j.est.2022.106162, corrected Table 2: H2/distilled-water IFT values, 4 pressure rows × 4 temperature columns.
- Original article DOI 10.1016/j.est.2022.104866: article scope and experimental context.
- Jiao et al. (2026) supplementary workbook, “Experiment data from literature”, observations 180–195: secondary compilation of the corrected distilled-water block.

## Next evidence needed

Obtain the complete original article methods section or written author clarification to resolve whether the IFT measurement was pendant-drop or another drop-shape configuration. Also inspect the original supplementary file for density data, uncertainty and exact source coordinates. The numerical values themselves are already verified against the corrigendum and should not be re-extracted from the superseded figure.

## Additional corrected formation-brine block extracted (2026-11-21)

The official corrigendum's corrected Table 2 contains a second 4-pressure × 4-temperature block for H2/formation brine, separate from the 16 H2/distilled-water observations already represented in the Jiao workbook. I have now transcribed these **16 additional central IFT values** into `data/processed/canonical/esfandyari_2022_corrected_formation_brine_16_observations.csv` (42 columns; one row per Table 2 condition).

| Pressure (bar) | 20 °C | 40 °C | 60 °C | 80 °C |
|---:|---:|---:|---:|---:|
| 10 | 63.6 | 62.6 | 60.3 | 58.5 |
| 40 | 63.1 | 62.2 | 59.8 | 58.3 |
| 70 | 62.9 | 62.0 | 59.5 | 57.6 |
| 100 | 62.8 | 61.3 | 59.1 | 57.2 |

All values are directly transcribed from the corrected Table 2. Original pressure (bar), temperature (°C), and IFT (mN/m) are preserved; normalized pressure (MPa) and temperature (K) are stored separately. The corrigendum states that both distilled-water and formation-brine experiments were repeated after surfactant contamination affected the original Figure 6, so the corrected table supersedes the original figure.

**Important limitations:** the corrigendum does not provide uncertainty alongside these 16 values, nor does its corrected table specify the IFT-specific drop configuration. A later literature synthesis describes the formation brine as containing NaCl, KCl, CaCl2 and MgCl2, but the exact recipe and component concentrations have not been verified from the original article/SI in this pass. Accordingly, the new rows are marked `table_extracted`, `reviewer_status=needs_clarification`, and `benchmark_eligible_primary=false`. They are source-traceable corrected measurements, but must not enter the primary benchmark until brine composition and method metadata are resolved or explicitly accepted under a documented unknown-category policy.

The 16 new formation-brine observations are **not** present in Jiao's 16-row Esfandyari group, which contains the distilled-water block only. They therefore expand source coverage rather than duplicate those Jiao rows. Source: official corrigendum DOI 10.1016/j.est.2022.106162, corrected Table 2; contextual brine-ion description: later literature synthesis (see project source register before final citation freeze).
