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