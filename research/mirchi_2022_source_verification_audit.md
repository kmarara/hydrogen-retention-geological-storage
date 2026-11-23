# Mirchi et al. (2022): primary-source verification audit

**Audit date:** 2026-11-21  
**Source:** Mirchi V, Dejam M, Alvarado V (2022). “Interfacial tension and contact angle measurements for hydrogen-methane mixtures/brine/oil-wet rocks at reservoir conditions.” *International Journal of Hydrogen Energy* 47(82), 34963–34975. DOI: [10.1016/j.ijhydene.2022.08.056](https://doi.org/10.1016/j.ijhydene.2022.08.056).  
**Jiao workbook group:** Ref [7], observations 274–288 (15 rows).

## Primary-source material inspected

The publisher's full-text HTML version was accessible through its article/am endpoint. The paper's Table 6 gives the H2-CH4/brine IFT data for five gas mixtures at 1000 psi and three temperatures. The paper's validation section distinguishes the pendant-drop IFT method from the sessile-drop/captive-bubble contact-angle method. The same full text describes 2 wt% NaCl brine and the 22, 40 and 60 °C experimental temperatures.

## Row-by-row numerical verification

All 15 workbook IFT values match Table 6 exactly at the workbook's displayed precision (two decimal places). Table 6 additionally reports an uncertainty alongside each IFT value; these uncertainties are not retained in the Jiao workbook.

| Workbook observations | Gas composition | Source IFT at 22 / 40 / 60 °C (mN/m) |
|---|---|---|
| 274–276 | 100% H2 / 0% CH4 | 70.36 / 68.04 / 65.94 |
| 277–279 | 80% H2 / 20% CH4 | 69.24 / 67.85 / 65.24 |
| 280–282 | 50% H2 / 50% CH4 | 66.26 / 64.88 / 62.46 |
| 283–285 | 40% H2 / 60% CH4 | 65.76 / 62.32 / 59.89 |
| 286–288 | 20% H2 / 80% CH4 | 63.62 / 60.56 / 56.41 |

No numerical discrepancies were found among the 15 central IFT values.

## Metadata verification and corrections/annotations

1. **Method:** Table 6 reports IFT. The paper's validation section explicitly identifies the pendant-drop system as the IFT technique. Sessile-drop/captive-bubble is used for contact-angle measurements. Workbook code 0 (Pendant Drop) is correct for all 15 IFT observations.
2. **Gas composition:** Table 6 defines the five gas mixtures as 100% H2; 80% H2–20% CH4; 50% H2–50% CH4; 40% H2–60% CH4; and 20% H2–80% CH4. The workbook's CH4 fractions 0, 0.2, 0.5, 0.6 and 0.8 are correct; H2 is the balance. CO2 fraction is zero.
3. **Brine:** the paper reports 2 wt% NaCl (20,000 ppm). The workbook stores 0.349 mol/kg. This is a derived conversion: 2 g NaCl per 100 g solution gives 0.3489 mol/kg (2/58.44 mol divided by 0.098 kg water). Retain 2 wt% as the source-reported basis and annotate 0.349 mol/kg as a derived molality under this convention; do not represent molality as the paper's reported unit.
4. **Pressure:** source is 1000 psi = 6.89476 MPa; workbook value 6.89 MPa is a rounded conversion.
5. **Temperature:** source values 22, 40 and 60 °C correspond to 295.15, 313.15 and 333.15 K. Workbook values 295, 313 and 333 K are rounded representations.
6. **Uncertainty:** Table 6 reports uncertainty for every IFT value (e.g., 70.36 ± 0.36 mN/m). The workbook contains only central values. Preserve the source uncertainty in a separate field and verify the paper's stated uncertainty definition before interpreting it as a standard deviation, standard error or confidence interval.
7. **Source coordinates:** exact numerical source location is Table 6, five gas-mixture row blocks × three temperature entries. The row ordering maps directly to workbook observations 274–288.
8. **Validation data and duplicate lineage:** Table 4 contains apparatus-validation comparisons against literature for pure gas/brine systems. Those validation rows are not the 15 H2-CH4 mixture observations in Table 6. Do not import them as additional observations or confuse them with the study's new mixture dataset. A wider cross-publication overlap review remains necessary.

## Canonical extraction completed (stage 1)

The 15 H2-containing Table 6 observations have been transcribed into the source-level canonical tranche `data/processed/canonical/chow_mirchi_2022_ift_observations_stage1.csv` and included in `data/processed/canonical/ift_source_verified_stage1_158_observations.csv`.

- The five H2/CH4 compositions are represented explicitly; H2 is calculated as the balance of the source-reported CH4 fraction.
- Original pressure is retained as 1000 psi and normalized pressure is calculated as 6.894757 MPa (not rounded to 6.89).
- Original temperatures are retained as 22, 40 and 60 °C and normalized to 295.15, 313.15 and 333.15 K.
- Source-reported 2 wt% NaCl is retained; 0.349 mol/kg is stored as a derived molality using 2 g NaCl per 100 g solution (0.098 kg water).
- All 15 source uncertainties are carried as reported ± values; their statistical meaning is not assumed.
- The Jiao workbook's methane fraction is stored under its CO2 column; the canonical derivative maps it to CH4, with CO2=0.
- Source table coordinates, publication/experiment/fluid-system group IDs and duplicate lineage are populated.

## Eligibility decision

- **Numerical values:** 15/15 verified against primary published Table 6.
- **Method:** pendant drop verified.
- **Gas composition:** verified, H2 is balance of stated CH4 fraction.
- **Original brine basis:** 2 wt% NaCl verified; workbook molality is derived.
- **Pressure/temperature:** source conditions verified; workbook units are rounded conversions.
- **Uncertainty:** source-reported for all 15; semantics need exact definition before use.
- **Provenance classification:** table_extracted.
- **Benchmark admission:** canonicalized as a source-level candidate in the 158-row stage-1 snapshot. Global overlap/duplicate review and frozen split-manifest checks remain open; no model training yet.

## Sources

- Publisher full text: https://www.sciencedirect.com/science/article/am/pii/S0360319922035133
- Published article record: https://www.sciencedirect.com/science/article/pii/S0360319922035133
- DOI: https://doi.org/10.1016/j.ijhydene.2022.08.056
