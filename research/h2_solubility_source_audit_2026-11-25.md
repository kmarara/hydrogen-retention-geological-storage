# H₂ solubility source audit

**Audit date:** 2026-11-25  
**Work package:** WP1 experimental evidence  
**Status:** source inventory and extraction protocol; no new numerical observations released  
**Branch:** `research-audit-and-revision`

## 1. Purpose and scope

This work package evaluates primary experimental measurements of molecular hydrogen dissolved in water and aqueous brines under conditions relevant to underground hydrogen storage.

It is separate from the H₂–brine interfacial-tension (IFT) work. Solubility is an aqueous-phase concentration or phase-equilibrium quantity. IFT is an interfacial property. Adsorption is surface accumulation, and diffusion is molecular transport. None is a substitute for another.

The immediate objective is to determine whether a reproducible, source-traceable experimental solubility dataset can be assembled. No model training or cross-study numerical pooling is authorised until extraction, unit harmonisation, uncertainty review and source-lineage checks are complete.

## 2. Primary-source inventory

| Source ID | Publication | Experimental system and reported envelope | Method / uncertainty | Current disposition |
|---|---|---|---|---|
| CHABAB_2024 | Chabab et al. (2024), *Solubility of H₂ in water and NaCl brine under subsurface storage conditions: Measurements and thermodynamic modeling*, International Journal of Hydrogen Energy, 50, 648–658. DOI: [10.1016/j.ijhydene.2023.10.290](https://doi.org/10.1016/j.ijhydene.2023.10.290) | H₂ + H₂O + NaCl; 298–373 K; 0–4 mol NaCl/kg water; pressure up to 200 bar. | Publisher record identifies volumetric measurement. Exact apparatus, uncertainty, reported solubility basis and row-level table coordinates require full-paper verification. | **Priority extraction source.** Original article and any supplementary material must be obtained before numerical transcription. |
| CHABAB_2020 | Chabab, Théveneau, Coquelet, Corvisier & Paricaud (2020), *Measurements and predictive models of high-pressure H₂ solubility in brine (H₂O+NaCl) for underground hydrogen storage application*, International Journal of Hydrogen Energy, 45(56), 32206–32220. DOI: [10.1016/j.ijhydene.2020.08.192](https://doi.org/10.1016/j.ijhydene.2020.08.192) | H₂ + water/NaCl; 323–373 K; 0–5 mol/kg NaCl; pressure up to 230 bar. | Static-analytic method with gas chromatography, as described in the publisher abstract. Exact uncertainty and row-level source locations require article/SI verification. | Comparison source. Do not assume the 2024 paper simply repeats the 2020 observations; verify apparatus, protocol and overlap. |
| TORIN_2021 | Torín-Ollarves & Trusler (2021), *Solubility of hydrogen in sodium chloride brine at high pressures*, Fluid Phase Equilibria, 539, 113025. DOI: [10.1016/j.fluid.2021.113025](https://doi.org/10.1016/j.fluid.2021.113025) | H₂ in pure water and NaCl brine at 2.5 mol/kg; 323.15–423.15 K; pressures up to about 40 MPa. | Synthetic apparatus. Authors report 3% expanded relative uncertainty in solubility at given T and P, coverage factor k=2. | Comparison source. Preserve the 3% expanded relative uncertainty (k=2); do not reinterpret it as standard uncertainty. Exact observation table and pressure grid still require extraction. |
| WOLFF_2026 | Wolff et al. (2026), *Experimental investigation of hydrogen solubility in water, NaCl solutions, and deep saline reservoir fluids from the Ketzin site under subsurface conditions*, Frontiers in Energy Research. DOI: [10.3389/fenrg.2026.1919332](https://doi.org/10.3389/fenrg.2026.1919332) | Pure water, 3 mol/kg NaCl, Ketzin synthetic brine and natural well brine; 295.15–373.15 K; 50–200 bar. | Experimental study. Reported table values are described as mol H₂/kg water in the available article view; complete uncertainty and brine chemistry fields must be transcribed from the article. | Separate later comparison source. A preliminary 56-row transcription exists outside the canonical dataset; it remains provisional pending source-coordinate, chemistry and uncertainty review. Natural well brine has a narrower temperature coverage and must not be treated as a complete factorial grid. |

### Important source distinction

Chabab et al. (2024) state that their measurements fall between two earlier high-pressure datasets that showed substantial disagreement. This is a reason to investigate the experimental methods and definitions carefully, not a reason to select one dataset as correct in advance. The 2024 paper reports average absolute deviations below 3% for its fitted thermodynamic models; that model-fit statistic is not an experimental measurement uncertainty and must not be copied into an observation-level uncertainty field.

## 3. First-pass comparison questions

For each primary source, extract and compare:

1. **Measured quantity:** dissolved H₂ concentration, liquid-phase mole fraction, molality, or another explicitly defined quantity.
2. **Phase definition:** whether the reported quantity is H₂ in the aqueous liquid phase and whether the basis excludes dissolved salt from the denominator.
3. **Pressure definition:** total cell pressure, H₂ partial pressure/fugacity, or another pressure variable; preserve the exact source definition.
4. **Temperature:** original value and unit, with a separate normalised kelvin field.
5. **Brine chemistry:** salt identity, molality basis, preparation method, water basis, and any impurities or additional ions.
6. **Experimental method:** equilibrium approach, sampling/analysis method, apparatus volume, equilibration criterion and calibration.
7. **Uncertainty:** absolute or relative; standard or expanded; coverage factor; repeatability; and whether it applies to each point or the method generally.
8. **Data lineage:** whether later publications reuse, reprocess, digitise or compare earlier observations.
9. **Model-generated values:** keep calculated correlations, fitted model outputs and simulated values outside the experimental-observation table.

## 4. Extraction protocol

- Obtain the publisher article PDF and all supplementary files for each source.
- Record exact page, table, figure, sheet and cell/row coordinates.
- Transcribe source values without rounding or silent correction.
- Preserve original pressure, temperature, solubility value, unit, composition and uncertainty fields.
- Record a separate normalised value only after the original quantity and basis are unambiguous.
- Keep molality (mol H₂/kg water), aqueous mole fraction and salt-free mole fraction as separate fields. Do not convert between them without an explicit formula and denominator definition.
- If data are available only as a plotted curve, place them in a separate digitised table with software, calibration points and digitisation uncertainty.
- Compare common T-P-salinity conditions only after matching the physical definition and concentration basis.
- Treat model-generated correlations as predictions, not experimental observations.
- Preserve unresolved values in a quarantine register rather than deleting or repairing them silently.

## 5. Current evidence status

No new Chabab 2024 observation has been extracted into a canonical file in this audit. The paper's abstract and publisher metadata establish the study's broad experimental envelope and method family, but do not provide enough detail for row-level data entry.

The Torín-Ollarves and Trusler abstract provides a method-level expanded relative uncertainty of 3% (k=2). This is not a substitute for checking the paper's full uncertainty budget or the uncertainty definition attached to individual tables.

The Wolff 2026 provisional 56-row transcription and the Torín 2021 provisional nine-row report inventory must remain provisional until their exact source coordinates, definitions, units, chemistry and uncertainty metadata are reconciled.

## 6. Immediate next actions

1. Obtain the full Chabab et al. (2024) paper and supplementary information.
2. Extract its complete experimental tables into a source-faithful raw file.
3. Read the method and uncertainty sections and record the actual measurement definition.
4. Reconcile the 2024 paper's comparisons with Chabab et al. (2020) and Torín-Ollarves & Trusler (2021) against the original papers, not only the 2024 discussion.
5. Compare matched conditions only after confirming the same solubility basis, pressure definition and brine composition.
6. Revisit the provisional Wolff 2026 and Torín 2021 transcriptions under the same schema.
7. Run schema and conversion tests before producing any canonical release.

## 7. Selected sources

- Chabab, S. et al. (2024). DOI: [10.1016/j.ijhydene.2023.10.290](https://doi.org/10.1016/j.ijhydene.2023.10.290).
- Chabab, S., Théveneau, P., Coquelet, C., Corvisier, J. & Paricaud, P. (2020). DOI: [10.1016/j.ijhydene.2020.08.192](https://doi.org/10.1016/j.ijhydene.2020.08.192).
- Torín-Ollarves, G.A. & Trusler, J.P.M. (2021). DOI: [10.1016/j.fluid.2021.113025](https://doi.org/10.1016/j.fluid.2021.113025).
- Wolff, N. et al. (2026). DOI: [10.3389/fenrg.2026.1919332](https://doi.org/10.3389/fenrg.2026.1919332).
