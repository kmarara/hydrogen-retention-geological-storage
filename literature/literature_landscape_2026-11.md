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
