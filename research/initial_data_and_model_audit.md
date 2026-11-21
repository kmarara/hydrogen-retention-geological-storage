# Initial research data and model audit

**Branch:** `research-audit-and-revision`  
**Audit date:** 2026-11-21  
**Scope:** Initial inspection of `data/raw/ift_experimental.csv`, `src/train_pinn_v3.py`, `outputs/week11_integration_metadata.json`, and `paper/paper_draft.md`.

## Status and caution

This is an initial repository-level audit, not a completed source-by-source verification. The 91 CSV records must not yet be described as 91 independently verified experimental measurements. No raw observations have been silently corrected or removed.

## 1. Dataset inventory

The CSV contains 91 numeric records:
- 64 attributed to Hosseini et al. (2022)
- 27 attributed to Ai & Trusler (2026)

The CSV labels the Ai & Trusler records as "Representative points from the study (empirical correlation validation)". Until their origin is checked against the publication and supplementary information, these records must be classified as representative/unverified rather than direct experimental observations.

The Hosseini rows are divided into:
- 16 pure-water rows
- 16 rows labelled NaCl_KCl_brine at 63,660 ppm (commented as 1.05 mol/kg)
- 16 rows at 190,980 ppm (commented as 3.15 mol/kg)
- 16 rows at 300,120 ppm (commented as 4.95 mol/kg)

The Ai & Trusler rows comprise 15 zero-salinity points and 12 points labelled 292,200 ppm (commented as 5 mol/kg NaCl).

## 2. Data issues requiring source verification

### 2.1 Repeated values in the 1.05 mol/kg block

Fourteen of the sixteen IFT values in the 63,660 ppm block exactly match the pure-water values at the same pressure and temperature. The two exceptions are at 298.15 K and 27.58 MPa (72.50 vs 72.10 mN/m) and 298.15 K and 34.47 MPa (72.00 vs 71.50 mN/m).

This pattern may reflect transcription, copying, rounding, or source-table interpretation. It is not proof of error. Verify against the original paper and its supplementary tables before retaining the values as measurements.

### 2.2 Concentration basis and fluid identity

The CSV comments describe conversion from molality to "ppm NaCl-equivalent" using an approximate factor. Molality (mol/kg solvent) is not automatically interchangeable with ppm or mg/kg of final solution. The exact concentration definition and conversion must be documented from the source.

Hosseini's CSV block is described as a NaCl+KCl brine with a stated ratio, whereas Ai & Trusler is a NaCl solution. These fluid systems must not be pooled as if they were chemically identical. Preserve original molality, salt composition, and concentration basis as separate fields.

### 2.3 Measurement provenance

The CSV does not provide DOI, source page/table/figure, original reported value, measurement uncertainty, digitisation status, or a per-row provenance identifier. These fields are required before this can become a traceable benchmark.

## 3. PINN implementation audit

Inspection of `src/train_pinn_v3.py` shows:
- The network predicts IFT from normalized pressure, temperature and salinity.
- The loss includes derivative-sign penalties for pressure, temperature and salinity.
- The loss forces the network output toward zero at a constructed point with T=33.2 K.
- Learnable `log_Tc`, `log_Pc` and `omega` parameters are created and regularized toward constants, but they are not used in the forward model or in a Peng–Robinson EOS residual.

Therefore, the current implementation does **not** implement a Peng–Robinson EOS-constrained PINN, despite the comments and manuscript description. It is a neural network with monotonic-gradient penalties, an imposed critical-temperature point penalty, and unused/regularized parameters.

The critical-temperature penalty at 33.2 K requires a system-specific thermodynamic justification. The training observations are 298.15–423.15 K, so this condition is far outside the observed temperature domain.

The physics collocation points are sampled at P=10–50 MPa, T=300–500 K and salinity=0–300,000 ppm. Parts of these ranges lie outside the dataset (which includes P up to 34.47 MPa and T up to 423.15 K), so the monotonicity assumptions are imposed in extrapolation regions without current empirical verification.

## 4. Validation and reproducibility issues

- The script uses an unseeded random row-wise 80/20 split.
- The split does not group observations by publication or experimental campaign.
- Normalization statistics are calculated on the full dataset before splitting, leaking validation-set distribution information into preprocessing.
- The data loader drops source and salinity-type metadata, preventing study-level splitting and fluid-system stratification.
- The reported metrics from this script cannot be treated as study-independent generalisation performance.
- The script does not implement dropout layers, so Monte Carlo dropout claims must be checked against the actual inference implementation rather than inferred from this training script.

## 5. Manuscript and metadata inconsistencies

- The manuscript describes the PINN as using Peng–Robinson EOS constraints; the inspected training script does not implement this.
- The manuscript describes the 91 records as experimental data, while 27 CSV rows are explicitly labelled representative points.
- The manuscript reports candidate-site IFT predictions around 9.42 mN/m in one section, while the metadata reports a regional IFT range of approximately 57.48–65.40 mN/m. This must be traced to the exact run and output files.
- The manuscript reports an integrated-score range of 0.176–0.825, while Week 11 metadata reports 0.03491–0.96361. Identify the run/configuration used for each reported result.
- The manuscript states 100x100 grid is approximately 0.1 degree. It is an angular grid; its physical cell size varies with latitude and is not uniformly 1 km.
- A uniform safety score of 0.500 across all five candidate sites, as shown in the manuscript, needs explanation and traceability to the actual calculation.

## 6. Literature source verification established so far

The Edith Cowan University thesis repository confirms the Hosseini thesis and lists the related 2022 paper:
Hosseini, M., Fahimpour, J., Ali, M., Keshavarz, A., & Iglauer, S. (2022). H2–brine interfacial tension as a function of salinity, temperature, and pressure; implications for hydrogen geo-storage. Journal of Petroleum Science and Engineering, 213, 110441. DOI: https://doi.org/10.1016/j.petrol.2022.110441

The thesis repository describes H2–brine IFT measurements, pendant-drop methodology, and trends with pressure, temperature and salinity. This confirms the source family and experimental context, but does not verify every CSV row.

The Ai & Trusler 2026 article metadata and abstract confirm measurements for H2–NaCl(aq) at NaCl molalities 0, 1, 3 and 5 mol/kg, temperatures 298.15–423.15 K, and pressures 0.5–30 MPa, using pendant-drop measurements. The current CSV has 27 rows explicitly described as representative points; the abstract alone does not verify these individual values.

The 2023 Omrani et al. paper reports molecular-dynamics-generated data and ML for H2–brine IFT. It is relevant background, but must not be merged into an experimental-only dataset without clearly separating simulation-derived data.

## 7. Required next actions

1. Obtain the full Hosseini 2022 article/supplementary data and verify all 64 attributed values, including the 1.05 mol/kg block.
2. Obtain the Ai & Trusler 2026 supplementary data and establish whether the 27 representative points are measured values, values digitised from figures, or correlation-generated examples.
3. Add row-level provenance, original units, concentration basis, fluid composition, measurement method, and status.
4. Separate experimental observations, digitised observations, calculated/correlation-generated values, simulation data and unverified records.
5. Build a new clean dataset from verified records without overwriting the original raw CSV.
6. Rebuild validation using study-grouped splits and training-fold-only preprocessing.
7. Reassess the physics formulation before retaining or rewriting the PINN.
8. Reconcile manuscript results with the exact versioned output files.

## Audit conclusion

The current repository is a valuable prototype, but the present 91-row file and PINN script are not yet ready to support claims of a source-verified experimental benchmark or a Peng–Robinson-constrained PINN. The immediate scientific priority is source verification and dataset reconstruction, followed by a leakage-resistant benchmark.
