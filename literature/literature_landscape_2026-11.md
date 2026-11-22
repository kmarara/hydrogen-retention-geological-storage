# Literature landscape and benchmark positioning (living review)

Review date: 21 November 2026. This is a targeted search, not a completed systematic review. Bibliographic details and abstracts below were checked against publisher/institutional records where available.

## 1. Directly relevant studies

### Hosseini et al. (2022)
Hosseini, M., Fahimpour, J., Ali, M., Keshavarz, A., & Iglauer, S. (2022). H2–brine interfacial tension as a function of salinity, temperature, and pressure; implications for hydrogen geo-storage. Journal of Petroleum Science and Engineering, 213, 110441. https://doi.org/10.1016/j.petrol.2022.110441

Publisher abstract reports pendant-drop experimental measurements and linear trends: IFT decreases with pressure and temperature and increases with salinity. The paper reports an empirical equation. The existence of a supplementary DOCX is indicated by the ResearchGate record, but the file has not yet been obtained and individual CSV values have not been verified against it.

### Ai & Trusler (2026)
Ai, L., & Trusler, J. P. M. (2026). Experimental study of hydrogen-brine interfacial tension: Implications for natural hydrogen production. International Journal of Hydrogen Energy, 224, 154442. https://doi.org/10.1016/j.ijhydene.2026.154442

Publisher abstract reports pendant-drop H2–NaCl(aq) measurements at NaCl molalities 0, 1, 3 and 5 mol/kg, T=298.15–423.15 K, P=0.5–30 MPa. It reports an empirical correlation with average absolute deviation 0.24 mN/m. Our repository CSV labels its 27 entries "representative points" for empirical-correlation validation. These entries must be traced to the article's actual tables/figures/supplementary data; do not label them independent experimental observations without evidence.

### Hosseini & Leonenko (2024)
Hosseini, M., & Leonenko, Y. (2024). Predicting interfacial tension in brine-hydrogen/cushion gas systems under subsurface conditions: Implications for hydrogen geo-storage. International Journal of Hydrogen Energy, 91, 1394–1406.

A publisher-hosted PDF search result reports a data summary from 16 sources, including 1,050 and 600 records for some source groups and a broad range of gas compositions. This indicates that larger multi-source IFT compilation and prediction work predates the current project. We must inspect the full paper and its cited sources before defining the novelty or building a comparison dataset. Its mixed H2/cushion-gas systems must not be conflated with pure H2–NaCl(aq).

### Omrani et al. (2023)
Omrani et al. (2023). Interfacial Tension-Temperature-Pressure-Salinity Relationship for the Hydrogen-Brine System under Reservoir Conditions: Integration of Molecular Dynamics and Machine Learning.

The PubMed abstract identifies molecular-dynamics simulation as the data-generation method. Any such records must be labelled simulation-derived, not experimental.

### New 2026 cushion-gas/brine study
A 2026 Petroleum Research paper reports experimental investigation of H2/brine/cushion-gas IFT. This broadens the evidence base but represents multicomponent gas systems and should be stratified separately from pure hydrogen–brine measurements.

### New November 2026 hybrid ML study
Jiao et al. (2026), Geoenergy Science and Engineering, article 214681, DOI 10.1016/j.geoen.2026.214681, is indexed as a hybrid machine-learning study of brine–hydrogen/cushion-gas IFT. Its abstract claims CatBoost-based prediction, generalisation to unseen monovalent electrolytes, SHAP/trend diagnostics, and conformalised quantile regression uncertainty intervals. This is very recent and directly overlaps several initially proposed benchmark components. Obtain and inspect the full paper before claiming novelty. The current project must not claim that ML, generalisation testing, or calibrated uncertainty are absent from the literature.

## 2. Implications for our research design

The proposed contribution "another ML/PINN model plus uncertainty" is not sufficiently differentiated on current evidence. A benchmark may still be valuable, but its novelty must be demonstrated, not assumed.

Potentially defensible directions to investigate:
1. An independent reproduction audit: reproduce published correlations/models and evaluate claims using strictly source-traceable data and clearly separated fluid systems.
2. Cross-study transferability: test whether a model trained on one experimental campaign transfers to a genuinely independent campaign, with publication-level grouping and harmonised conditions.
3. Data lineage and target integrity: distinguish raw observations, table extractions, digitised points, correlation-generated representative values and simulation outputs; quantify how mixing these categories affects apparent model performance.
4. Benchmark protocol: define leakage-resistant evaluation, domain-of-applicability diagnostics and reproducible uncertainty assessment. Compare against the latest 2024–2026 studies rather than claiming these ideas are new.
5. Scope restriction: begin with pure H2–water/NaCl(aq) data. Treat mixed electrolytes, cushion gases, molecular-dynamics data and other fluid systems as separate benchmark tracks unless enough metadata exists for defensible pooling.

## 3. Immediate literature tasks

- Obtain and read the full Hosseini & Leonenko (2024) paper and its data sources.
- Obtain full text and supplementary information for Ai & Trusler (2026).
- Obtain the Hosseini (2022) supporting-information DOCX and compare every relevant source value.
- Obtain the full Jiao et al. (2026) article and examine dataset, validation split, uncertainty method, code/data availability, and claimed generalisation.
- Compare the 2026 cushion-gas paper and 2023 MD paper to define separate system tracks.
- Update the research gap only after these comparisons.

## 4. Sources checked in this targeted search

- ScienceDirect record for Hosseini et al. (2022): https://www.sciencedirect.com/science/article/pii/S0920410522003278
- ScienceDirect record for Ai & Trusler (2026): https://www.sciencedirect.com/science/article/pii/S0360319926010797
- Imperial College publication record for Ai & Trusler (2026): https://www.imperial.ac.uk/a-z-research/towards-net-zero/publications/?id=1653353
- Hosseini & Leonenko (2024) publisher-hosted PDF: https://uwaterloo.ca/waterloo-institute-sustainable-energy/sites/default/files/uploads/documents/predicting-interfacial-tension-in-brine-hydrogencushion-gas-systems-under-subsurface-conditions-implications-for-hydrogen-geo-storage.pdf
- ScienceDirect record for 2026 H2/brine/cushion gas experimental study: https://www.sciencedirect.com/science/article/pii/S2096249525001097
- ScienceDirect record for Jiao et al. (2026): https://www.sciencedirect.com/science/article/pii/S2949891026003258
- PubMed record for 2023 molecular-dynamics/ML study: https://pubmed.ncbi.nlm.nih.gov/37650690/

## 5. Research integrity rule

Do not claim a literature gap, dataset size, model superiority, experimental validation, or novelty until the full relevant sources and source data have been inspected. Keep a dated literature matrix and document negative findings as well as positive ones.


## 6. Full-text verification update (21 November 2026)

### Hosseini & Leonenko (2024): inspected full publisher-hosted PDF

The full 2024 paper was inspected. It reports a compilation of 2,569 samples from 16 sources (the paper's abstract/search metadata elsewhere can show slightly different totals; the database section states 2,569). It identifies 23 gas compositions and uses composition-group splitting: five compositions were assigned to testing and 18 to training. The authors also moved 68 samples from Higgs et al. and Esfandyari et al. to an "extra" set because they considered those records inconsistent with common trends. The paper reports 603 test samples and 68 extra samples. This is important prior work: group-based validation by gas composition, external/extra-set evaluation, SHAP and multiple ML models are already in the literature. (Full text, pp. 1396–1399; Table 1 and Sections 3.1–3.4.)

The 2024 dataset is heterogeneous: it combines pure H2, H2/CO2, H2/CH4 and multicomponent H2/CO2/CH4/N2 mixtures, with different brine systems and experimental sources. For example, its Table 1 identifies Hosseini et al. (2022) as 64 observations for pure H2 and 0.864 NaCl + 0.136 KCl brine at 1.05, 3.15 and 4.95 mol/kg, while other source groups include NaCl-only brines and mixed formation brines. This reinforces the need to preserve source, gas composition and electrolyte identity rather than pool records as if they were one homogeneous H2–NaCl dataset.

The paper explicitly says standard scaling should be fitted on training data and then applied to test data to avoid leakage. It also explains why gas composition is more informative than specific gravity alone. The paper's group split is by gas composition, not a leave-one-publication-out evaluation. Therefore, a genuinely independent publication-level replication/transfer test remains a distinct question to investigate; it must not be presented as an established gap until the source-level dataset and later work have been checked.

### Jiao et al. (2026): abstract and publisher-indexed section snippets inspected

The publisher-indexed record reports a 2,689-measurement database (the indexed conclusion snippet elsewhere says 2,673; this discrepancy needs full-text resolution). The abstract claims IVYA-CatBoost, R2=0.9991, RMSE=0.29 mN/m, unseen-electrolyte generalisation, SHAP/trend diagnostics, Williams-plot applicability diagnostics, and conformalised quantile regression with calibrated 95% intervals. The publisher-indexed methods snippets say the source data were compiled from published experimental studies. The full article could not be opened through the publisher in this review, so these are abstract/snippet-level claims, not an independent verification of the methods or results.

This study directly overlaps the initial proposal's broad claims around machine learning, electrolyte generalisation, physical trend diagnostics and calibrated uncertainty. Those elements cannot be claimed as novel in isolation. The more defensible potential distinction is an independently reproducible, row-level source-lineage audit and publication-held-out reproduction protocol, if full-text comparison confirms that these are not already addressed.

### Ai & Trusler (2026) and Hosseini et al. (2022)

Publisher records confirm Ai & Trusler's experimental H2–NaCl(aq) pendant-drop scope: 0, 1, 3 and 5 mol/kg NaCl; 298.15–423.15 K; 0.5–30 MPa. The repository's 27 entries are labelled representative points for empirical-correlation validation. Until matched to the article's tables, figures or supplementary data, they remain representative/unverified rather than independent experimental rows.

The Hosseini (2022) publisher abstract confirms pendant-drop H2–brine measurements and an empirical correlation. Its brine is not simply NaCl: the 2024 source table identifies the salt mixture as 0.864 NaCl + 0.136 KCl, at total salt molalities 1.05, 3.15 and 4.95 mol/kg. The supplementary DOCX is listed in a ResearchGate record but has not yet been obtained or inspected.

### Revised provisional research positioning

Do not position the work as the first IFT ML benchmark, first grouped validation, first electrolyte generalisation study, first SHAP/physical-trend assessment, or first calibrated uncertainty study. A narrower candidate is:

"An independently reproducible, source-aware audit of published H2–brine IFT correlations and predictive models, quantifying how source provenance, data-generation status, electrolyte identity and publication-level holdout affect reported predictive performance."

This remains a hypothesis for the literature gap, not a novelty claim. It must be tested against the full Jiao et al. (2026) article and the original source datasets before the proposal is finalised.


## 7. Newly indexed study requiring immediate review (22 November 2026)

### Davoodi & Wood (2026): physics-guided, chemistry-aware empirical IFT equations

Davoodi, S., & Wood, D. A. (2026). “Physics-informed and chemistry-aware framework to predict hydrogen-brine interfacial tension for underground hydrogen storage reservoir conditions.” *Geoenergy Science and Engineering*, 266, Article 214609. DOI: [10.1016/j.geoen.2026.214609](https://doi.org/10.1016/j.geoen.2026.214609).

**Evidence inspected:** publisher-indexed abstract and bibliographic metadata, plus an independent library catalogue record. The full article and its underlying data were not inspected in this update. Treat all methodological details below as abstract-level claims pending full-text review.

The abstract reports a 2,649-record compilation of published gas–brine IFT measurements, divided into:
- Class I: H2 only;
- Class II: binary H2+CO2, H2+CH4 or H2+N2 mixtures;
- Class III: quaternary H2+CO2+CH4+N2 mixtures.

It develops 13 class-specific equations using physics-guided chemistry-aware feature influence (CAFI) and customized formulaic optimization (CFO), plus three general equations for the combined dataset. The abstract reports the best Class III equation at R2=0.9602 and RMSE=2.27 mN/m for 2,240 records, and the best general equation at R2=0.7878 and RMSE=5.25 mN/m for 2,649 records. It states that class-focused equations outperform general equations and CFO equations outperform CAFI equations.

**Implications for our project positioning:**
1. Physics-guided and chemistry-aware empirical modelling of hydrogen/cushion-gas–brine IFT is now explicitly represented in the late-2026 literature. We must not claim that such modelling, class-specific equations or large multi-source compilations are absent.
2. The abstract does not establish whether the 2,649 records are independently source-audited, how duplicate lineage is handled, whether source-level holdouts are used, or how uncertainty is quantified. These are questions for the full paper, not assumptions.
3. The paper's 2,240-record Class III result appears to be dominated by quaternary gas-mixture records. Its headline scores are not directly comparable to our proposed pure-H2/limited-binary source-verified tranche without matching fluid-system definitions and evaluation partitions.
4. The possible distinction for our work remains an independently reproducible observation-level provenance audit and publication-held-out evaluation of pretrained and conventional tabular models, but this is only a candidate distinction until the Davoodi & Wood paper, its data lineage and the Jiao et al. (2026) hybrid-ML paper are fully compared.

**Required follow-up:** obtain the full paper; inspect its data-source table, per-source record counts, treatment of duplicate/derived/simulated data, train/test protocol, chemistry encoding, equations, applicability ranges and uncertainty treatment. Map every cited experimental source against our source register before asserting any benchmark gap.

Source checked: publisher record, https://www.sciencedirect.com/science/article/abs/pii/S2949891026002538 ; independent catalogue, https://vufind.lib.tpu.ru/vufind/Record/687177.
