# Project charter and objective control

**Project:** Source-aware independent benchmark of hydrogen–brine interfacial-tension prediction  
**Branch:** `research-audit-and-revision`  
**Last reviewed:** 2026-11-21

## North-star objective

Build an independently reproducible, source-aware benchmark to determine whether published hydrogen–brine interfacial-tension (IFT) predictive models generalise to genuinely unseen experimental publications and chemically distinct fluid systems, and whether their uncertainty estimates remain reliable under those conditions.

The project is not primarily an exercise in maximising random-split R2, proposing another neural architecture, or producing a geological site ranking. The core scientific output is a trustworthy evaluation framework and evidence about model reliability, transferability, source dependence and applicability domain.

## Primary research question

Under publication-held-out and fluid-system-aware evaluation, how reliably do pretrained and conventionally trained tabular models predict hydrogen–brine IFT from independently sourced experimental data, compared with published empirical correlations?

## Supporting questions

1. How do performance estimates change when correlation-generated, representative, digitised, simulation-derived and unverified records are separated or excluded?
2. Does a pretrained tabular foundation model (TabPFN) improve independent-publication performance over fold-trained TabM and conventional boosted-tree baselines?
3. Are nominal prediction intervals calibrated on held-out publications and fluid systems?
4. How do electrolyte identity, gas composition, measurement method and experimental study affect error and applicability domain?
5. Can published empirical correlations reproduce source-independent measurements within their stated conditions?

## Scope boundaries

### In scope
- Pure H2–water and H2–aqueous-electrolyte systems, with each fluid family separately identified.
- Mixed electrolytes and cushion-gas systems only where source records are sufficiently documented; never silently pool with pure H2–NaCl data.
- Experimental observations and clearly labelled derived/digitised records.
- TabPFN as the pretrained foundation-model candidate.
- TabM as a fold-trained, parameter-efficient ensemble (not a pretrained foundation model).
- XGBoost or CatBoost as conventional baselines.
- Published empirical correlations as transparent physics-literature baselines.
- Publication-held-out validation, fluid-system transfer, uncertainty calibration and applicability-domain diagnostics.

### Out of scope unless separately justified
- Claiming a new foundation model or novel PINN architecture.
- Treating simulation outputs or empirical-correlation predictions as experimental measurements.
- Merging all electrolyte/gas systems into one undifferentiated table.
- Using random row-wise validation as the headline generalisation result.
- Recommending storage sites from IFT alone.
- Expanding into GIS/site ranking before the IFT benchmark is scientifically defensible.

## Evidence and data eligibility rules

Every modelled observation must carry a source-study identifier, DOI, source coordinate (page/table/figure/supplement), original value and unit, pressure, temperature, original concentration basis, fluid composition, method, provenance status and documented conversions.

Allowed provenance statuses:
- direct_measurement
- table_extracted
- figure_digitised
- correlation_generated
- simulation
- derived_conversion
- representative_unverified
- unknown

Only eligible experimental observations enter the primary experimental benchmark. Digitised measurements may be included in a separately reported sensitivity analysis with digitisation uncertainty. Correlation-generated, simulation, representative-unverified and unknown records must not be labelled experimental measurements.

## Model-comparison rules

- Evaluate all models on identical eligible training/test partitions.
- Fit preprocessing only on each training fold.
- Keep held-out publications entirely outside tuning, preprocessing, model selection and training.
- Report per-publication metrics and sample counts, not only pooled metrics.
- Report MAE and RMSE in mN/m; use R2 only alongside errors and group counts.
- For predictive intervals, report empirical coverage, width and an appropriate interval score; do not equate nominal 95% with calibrated 95%.
- Record exact software versions, checkpoint identifiers, licences, seeds, hardware and configuration.
- Check TabPFN checkpoint-weight licence separately from package/source-code licence before selecting weights.

## Decision gates

**Gate 1 — Source acquisition:** obtain and checksum ACS Jiao et al. (2026) XLSX and pursue primary supplementary sources for Hosseini (2022) and Ai & Trusler (2026).

**Gate 2 — Provenance and overlap:** inspect workbook sheets, row counts, fields, source lineages and overlap with the repository's 91 legacy rows. Freeze a traceable benchmark snapshot.

**Gate 3 — Baseline reproduction:** implement and test the empirical correlations only after verifying their equations and applicability ranges against the original papers and errata.

**Gate 4 — Model benchmark:** run boosted-tree baseline, TabPFN and TabM under the same leakage-resistant split protocol.

**Gate 5 — Reliability analysis:** evaluate uncertainty calibration, physical trends and applicability domain on held-out sources.

**Gate 6 — Scientific interpretation:** decide what claims are supported, what is not, and whether any follow-on PINN or storage-containment application is justified.

No gate is considered passed without a repository artefact and verifiable evidence.

## Current status (2026-11-21)

- Nine-page ACS Supporting Information PDF directly inspected.
- ACS XLSX workbook obtained; 450 observations structurally extracted across nine cited studies. All rows remain provenance-unverified and primary-benchmark-ineligible.
- Existing 91-row legacy CSV not source-certified.
- Source overlap audit in progress; a Hosseini 2022 value/label discrepancy between the workbook and legacy CSV has been documented for primary-source resolution.
- TabPFN checkpoint and licence not selected.
- TabPFN, TabM and boosted-tree benchmark not run.
- Existing PINN requires reformulation/audit before reuse.
- No new experimental measurements have been created; the ACS workbook is a secondary compilation and its rows have not been independently source-certified.
- No model performance result is claimed.

## Decision log

- **2026-11-21:** Research direction retained as an independent source-aware benchmark.
- **2026-11-21:** Pretrained TabPFN selected as the primary foundation-model candidate; TabM retained as a fold-trained ensemble comparator; XGBoost/CatBoost and empirical correlations retained as baselines.
- **2026-11-21:** Publication-held-out validation designated as the primary generalisation test. The ACS SI's shuffled KFold examples are treated as reproducibility references, not as sufficient evidence of publication-independent generalisation.
- **2026-11-21:** GIS/site ranking and claims of a new PINN are deferred until the benchmark and physics audit justify them.


- **2026-11-21:** Added `data/metadata/observation_schema.md` as the canonical row-level schema specification. It defines provenance states, original-versus-normalised units, source coordinates, experiment/publication/fluid-system split groups and benchmark eligibility rules. This is a schema specification only; no legacy rows have been certified or transformed.


- **2026-11-21:** Acquired and checksummed the ACS Jiao et al. (2026) XLSX. Extracted 450 rows across nine cited studies; 266 Pendant Drop and 184 Sessile Drop method codes. All records remain provenance-unknown and excluded from the primary benchmark until verified against original sources.
- **2026-11-21:** Documented a material Hosseini et al. (2022) discrepancy: at 2.76 MPa and 298.15 K the workbook distinguishes pure water (73.57 mN/m) from mixed brine (74.97 mN/m), whereas the legacy CSV labels 74.97 mN/m as pure water and repeats it in a brine block. No merge or correction is authorised pending primary-source verification.


- **2026-11-22:** Directly inspected the nine-page ACS Jiao et al. (2026) Supporting Information PDF. Its TabPFN example shows shuffled five-fold KFold for internal validation and a separate external-prediction stage; source-study independence of the external sets and any publication grouping in the main article remain unverified. The SI omits standard data I/O, scaling pipelines and repetitive training loops, so it is not sufficient to reproduce the full workflow or audit the 450 rows.
- **2026-11-22:** Do not claim that publication-held-out validation is absent from Jiao et al. based on SI snippets alone. Inspect the main article and identify the external datasets before finalising the research gap. Retain publication-held-out evaluation as our planned stringent test, not yet as a proven literature novelty.
