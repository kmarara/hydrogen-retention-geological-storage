# Pretrained and tabular-model benchmark protocol

**Status:** proposed protocol; no model has been trained and no pretrained checkpoint has yet been selected.  
**Branch:** `research-audit-and-revision`  
**Basis:** Jiao et al. (2026), *Energy & Fuels* Supporting Information PDF uploaded as `ef6c01887_si_001.pdf`, plus the official TabPFN and TabM project documentation reviewed 2026-11-21.

## 1. Research purpose

Evaluate whether pretrained tabular priors improve prediction of hydrogen–brine interfacial tension (IFT) under strict source-independent evaluation. The scientific contribution is the source-aware, leakage-resistant evaluation and audit of model transfer—not the mere application of a fashionable architecture.

Primary question:

> Under publication-held-out and fluid-system-aware evaluation, does a pretrained tabular foundation model provide more reliable hydrogen–brine IFT predictions than models trained only on the available experimental training data?

Secondary questions:
1. Does TabM's parameter-efficient ensemble improve performance and stability over conventional baselines?
2. Are predictive intervals calibrated on independent studies and chemically distinct fluid systems?
3. Does apparent performance depend on including correlation-generated, representative, digitised, or otherwise non-independent records?
4. Where do models extrapolate beyond their training support in pressure, temperature, molality, electrolyte identity, gas composition, or method?

## 2. Model roles (do not conflate these)

| Model | Pretrained? | Role |
|---|---|---|
| TabPFN regression | Yes; checkpoint/version-specific | Primary foundation-model candidate |
| TabM | No; architecture trained on benchmark training folds | Efficient ensemble deep-learning comparator |
| XGBoost or CatBoost | No | Strong conventional tabular baseline |
| Regularised linear / empirical correlations | No | Transparent low-complexity and physics-literature baselines |
| Existing repository PINN | No | Defer until the physical formulation and code/manuscript mismatch are resolved |

TabM is a parameter-efficient ensemble architecture, not a pretrained foundation model. TabPFN is the actual pretrained candidate. The Jiao SI PDF (pp. 1–5) provides TabM configuration and TabPFN workflow examples, but its code omits data I/O, scaling, full training loops and other implementation details.

## 3. Source evidence extracted from the uploaded SI PDF

### TabM (PDF pp. 1–3)
The SI reports separate optimal configurations for H2–pure-water, H2–brine and combined-system scenarios:
- Learning rates: 4.80e-3, 4.61e-3, 4.30e-3.
- Weight decay: 3.83e-3, 3.89e-3, 4.57e-4.
- Batch size: 16 in all three scenarios.
- PLE bins: 32, 40, 40.
- Embedding dimensions: 16, 8, 16.

These are reported settings from the paper, not guaranteed optimal settings for our reconstructed dataset. Use as reproduction starting points, not as fixed truths.

### TabPFN (PDF pp. 3–5)
The SI shows `TabPFNRegressor`, fitting on each training fold, and quantile prediction at 0.025, 0.5 and 0.975. It describes internal shuffled 5-fold validation and a separate external dataset, and mentions permutation-SHAP and partial-dependence analysis. The snippet is illustrative and omits the data-loading and metric aggregation code. Its exact API/checkpoint must be reconciled with the currently installed TabPFN version before execution.

### Empirical correlations (PDF pp. 6–8)
The SI gives the Hosseini et al. (2022) H2–brine form:
`gamma = A*m + B`,
`A = a0 + a1*p + a2*T`,
`B = b11 + b21*p + b12*T + b22*p*T`,
where gamma is mN/m, m is total brine molality in mol/kg, T is K and p is MPa. Parameters:
- a0 = -0.47876
- a1 = -0.01004
- a2 = 0.00593
- b11 = 135.41479
- b21 = -0.38368
- b12 = -0.20520
- b22 = 0.00084

The SI also prints a Chow et al. (2018) H2O–H2 polynomial and erratum-corrected coefficients (p. 7). The equation typography/exponent placement must be checked against the original article/erratum before coding; do not implement from OCR alone.

These formulae are literature baselines, not independent experimental observations. Predictions generated from correlations must never be labelled measured IFT.

## 4. Dataset eligibility and leakage controls

No modelling begins until each record has:
- source DOI and source-study ID;
- source page/table/figure/supplement coordinate;
- original value, unit, pressure, temperature and concentration basis;
- electrolyte identity and composition, gas composition, method;
- status: direct measurement, table-extracted, figure-digitised, correlation-generated, simulation, derived conversion, representative/unverified, or unknown;
- documented conversion and uncertainty where applicable.

Keep pure water, NaCl, mixed NaCl–KCl, multicomponent brines, cushion-gas mixtures and simulation data distinguishable. A dataset described as 450 curated measurements in the ACS article is not automatically 450 independent observations or 450 rows from unique experiments.

The uploaded SI PDF is nine pages of methods/code/correlations; it is **not** the 450-row workbook. The XLSX remains required to reconstruct the article dataset and audit source overlap.

## 5. Evaluation design

### Primary: leave-one-publication-out (LOPO)
For each eligible publication with enough observations:
1. Hold out all observations from that publication.
2. Train/tune only on the remaining eligible publications.
3. Fit all learned preprocessing only within each training fold.
4. Keep hyperparameter selection nested within training data.
5. Report per-publication metrics and pooled metrics, with uncertainty across source groups.

### Secondary: fluid-system transfer
Where sample size permits, hold out a fluid family (e.g. H2–NaCl or a mixed-electrolyte family) as an external test. Do not claim generalisation if train/test fluid systems overlap chemically in a way that invalidates the intended test; document the exact split.

### Sensitivity analyses
- Exclude representative/unverified and correlation-generated records.
- Compare direct/table-extracted observations with digitised observations.
- Remove overlapping source lineages and duplicated observations.
- Compare row-random split only as a deliberately optimistic diagnostic, never as the headline result.

### Metrics
Report MAE and RMSE in mN/m; R2 only alongside error metrics and per-group counts. For intervals report empirical coverage, mean interval width and a proper interval score where supported. Evaluate calibration separately on held-out publications; nominal 95% does not mean calibrated 95%.

### Applicability domain and physical diagnostics
Report train/test ranges and support by P, T, molality, salt identity, gas composition and measurement method. Test physically motivated trends only where the relevant controlled comparison and chemistry justify them. Do not impose a universal monotonicity rule without checking phase/system-specific evidence.

## 6. TabPFN checkpoint and reproducibility gate

Before selecting TabPFN:
1. Pin package version and exact model checkpoint.
2. Inspect the checkpoint's model-weight licence and intended-use terms.
3. Record hardware, inference mode, random seeds where applicable, package versions and model configuration.
4. Confirm regression API and quantile output against the installed version.
5. Check input-feature and sample-size recommendations for that checkpoint.
6. Keep all test publications entirely outside fitting, tuning, preprocessing and model selection.

Current upstream repository information indicates that model-weight licences vary by release; some recent checkpoints are non-commercial, while v2 has separate terms. Do not assume the code licence also licenses the weights. For an academic/non-commercial project, verify the exact checkpoint terms and cite the model appropriately.

Official references:
- TabPFN: https://github.com/PriorLabs/TabPFN
- TabM: https://github.com/yandex-research/tabm
- TabM ICLR 2025 paper: https://openreview.net/forum?id=du6oz4Gg9D
- Jiao et al. SI PDF: uploaded source `ef6c01887_si_001.pdf`

## 7. Staged implementation roadmap

1. Obtain the ACS supplementary XLSX; checksum and preserve original workbook.
2. Ingest worksheets without modifying original columns; inspect headers, units, footnotes and row counts.
3. Build source-lineage and overlap map against Hosseini 2022, Ai–Trusler 2026 and existing repository rows.
4. Complete source-aware eligibility labels and produce a frozen benchmark snapshot.
5. Implement and test empirical-correlation baselines.
6. Implement conventional baseline (XGBoost or CatBoost).
7. Implement TabPFN regression using a licence-cleared pinned checkpoint.
8. Implement TabM from scratch using fold-specific training.
9. Run LOPO and fluid-system transfer; quantify calibration and applicability domain.
10. Only then decide whether to retain, reformulate or remove the existing PINN from the research paper.

## 8. Current status

- Uploaded ACS SI PDF inspected: nine pages.
- Model workflow and empirical correlation details extracted into this protocol.
- ACS XLSX workbook: not yet obtained.
- Source overlap audit: pending.
- TabPFN checkpoint/licence: not selected.
- Models trained: none.
- Tests/benchmark results: none.

Do not report performance claims until the dataset is source-verified and the split protocol has been executed.


## 9. Source-specific reproduction notes from direct PDF reinspection

The uploaded source file `ef6c01887_si_001.pdf` was re-opened and inspected page by page on 2026-11-21.

- TabM SI workflow (pp. 2–3) imports `KFold` and uses `KFold(n_splits=5, shuffle=True, random_state=42)`. The code comment says fold-specific scaling is omitted from the displayed snippet. This is a shuffled row-level five-fold scheme, not a publication-held-out split.
- TabPFN SI workflow (pp. 4–5) also uses shuffled five-fold `KFold` for internal validation, then fits on all internal data and predicts a separate external dataset. The SI does not identify the external dataset's full source lineage in these code snippets.
- The TabPFN snippet requests quantiles `[0.025, 0.5, 0.975]` using `output_type="quantiles"`. Treat this as the authors' illustrative API example; confirm compatibility with the pinned installed package/checkpoint before use.
- The Chow et al. (2018) equation as typeset on PDF p. 6 reads `gamma = a1*T^2 - a2^p + a3*p + a4*T*p + a5`; coefficients on p. 7 are a1=-2.6040e-4, a2=8.950e-2, a3=-0.2553, a4=5.153e-4, a5=96.24. Because this expression incorporates an erratum and has a superscripted pressure term, independently compare the original paper and 2020 erratum before coding or reporting a reproduction.
- The Hosseini et al. (2022) correlation and coefficients are transcribed on PDF pp. 7–8; see Section 3 above. Verify equation domain and source conditions before use.

**Implication:** The ACS SI provides reproducible starting points, but its displayed internal validation examples do not establish publication-independent generalisation. Our primary LOPO design is an intentionally stricter evaluation. Any numerical comparison with the article must distinguish exact reproduction of its shuffled-fold setup from our stricter source-held-out audit.
