# Hydrogen Retention and Fluid–Rock Interactions in Underground Hydrogen Storage

**Research focus:** Hydrogen dissolution, retention and loss in water-bearing geological formations.

**Researcher:** Kudakwashe Marara  
**Background:** BSc (Hons) Petroleum Chemistry and Technology, University of Zimbabwe (Upper Second Class, 2.1)  
**Contact:** kudakwashe.d.marara@gmail.com  
**GitHub:** https://github.com/kmarara

## Research question

How do brine chemistry, pore confinement and mineral–fluid interactions influence hydrogen dissolution, retention and loss in geological formations considered for underground hydrogen storage?

This repository is an evolving, independently developed research programme. It is not a validated hydrogen-storage safety model and does not claim to predict field-scale hydrogen loss.

## Why this problem matters

Underground hydrogen storage depends on more than the nominal storage capacity of a geological formation. Hydrogen can interact with formation water, mineral surfaces and pore structures. Understanding dissolution, adsorption and transport in water-bearing formations is therefore important when assessing hydrogen retention and potential losses.

A central motivation is the work of Zhang and co-authors on hydrogen dissolution in water-saturated kaolinite nanopores under nanoconfinement:

- Zhang et al. (2023), *Molecular Simulation of H₂ Loss by Dissolution in Caprock Water-Saturated Nanopores under the Nanoconfinement Effect for Underground Hydrogen Storage*, **Energy & Fuels**. https://doi.org/10.1021/acs.energyfuels.3c03384
- Zhang et al. (2023), *Molecular Simulation of H₂/CH₄ Mixture Storage and Adsorption in Kaolinite Nanopores for Underground Hydrogen Storage*, **ACS Omega**. https://doi.org/10.1021/acsomega.3c06475
- Luo, Jia & Zhang (2023), *Technical challenges and outlook of underground hydrogen storage in depleted oil and gas reservoirs*, **Oil & Gas Storage and Transportation**. [Bibliographic details and full text should be checked before relying on specific claims.]

These studies motivate questions about pore size, water saturation, salinity, mineral surface chemistry and hydrogen retention. The repository's proposed work is intended to build evidence around these questions, not to reproduce molecular simulations without the necessary methods or supervision.

## Research programme

The programme has one scientific centre—**hydrogen retention and loss in water-bearing geological formations**—with supporting work packages.

### 1. Experimental evidence for H₂–brine behaviour

An ongoing source-verification effort examines published hydrogen–brine interfacial-tension (IFT) observations. The work checks original sources, fluid composition, experimental method, units, uncertainty and data lineage before any observation is used in modelling.

The current stage-one candidate dataset contains 158 observations attributed to Chow et al. (2018), Hosseini et al. (2022) and Mirchi et al. (2022). This is a **candidate tranche, not a released benchmark**: global overlap review, full schema/conversion validation and final eligibility gates remain open. Other study groups remain quarantined where source, method or chemistry questions are unresolved.

IFT and solubility are different physical properties. The IFT dataset is not a substitute for H₂-solubility measurements. A separately sourced and verified H₂–brine solubility dataset is a possible future work package, subject to availability of suitable primary experimental evidence.

### 2. Pore-scale fluid–rock interactions

The proposed next scientific extension is to examine how water saturation, pore confinement, mineralogy and brine chemistry influence hydrogen dissolution and adsorption. Molecular simulation is a method to be learned under appropriate supervision; no molecular-dynamics study is claimed as completed in this repository.

Initial work will be literature-based and evidence-led: define the relevant mechanisms, identify suitable primary experimental and simulation sources, compare reported conditions, and establish what can and cannot be compared.

### 3. Geological screening context

The repository also contains an exploratory Python-based geospatial site-screening framework for a Southern Africa study area. It uses preliminary data layers and weighted-overlay/sensitivity workflows.

This framework is supporting context, not the primary scientific claim. Its geological inputs are coarse, it does not currently model hydrogen loss or hydrogen-sensitive mineral/ionic/microbial conditions, and its map outputs are not validated storage-safety or site-selection recommendations. Any future use must incorporate appropriate geological, geochemical and uncertainty evidence and must not infer safety from IFT alone.

## What has been done

- Built an exploratory Python geospatial workflow and performed preliminary weighted-overlay sensitivity analysis.
- Audited the legacy IFT dataset and identified source-provenance, concentration-basis, validation and implementation limitations.
- Obtained and structurally inspected the Jiao et al. (2026) supplementary workbook containing 450 observations attributed to nine literature sources.
- Independently reconciled multiple workbook groups against original papers or supplementary information and documented unresolved discrepancies and metadata issues.
- Created a 158-observation stage-one canonical candidate tranche from three source studies; it has not passed all benchmark-release gates.
- Audited the legacy PINN implementation and found that it does not currently implement the Peng–Robinson EOS-constrained PINN described in the earlier project narrative. It is not presented here as a validated PINN.

## What has not been done

- No new H₂-solubility dataset has yet been source-verified and released.
- No molecular-dynamics simulations have been performed by the repository author.
- No validated field-scale hydrogen-loss or caprock-integrity model has been produced.
- No publication-held-out benchmark model training has been completed under the current source-audit programme.
- No new PINN architecture or validated physics-informed model is claimed.
- The exploratory GIS outputs are not evidence that a particular site is safe or suitable for hydrogen storage.

## Research principles

1. **Primary-source traceability:** every observation used in a scientific analysis must have a traceable source and extraction location.
2. **Chemistry-aware comparison:** preserve electrolyte identity, concentration basis, gas composition, experimental method and measurement conditions.
3. **Separate evidence types:** do not mix experimental measurements, digitised values, correlations, simulations and unverified records without explicit labels.
4. **Uncertainty and limitations:** preserve reported uncertainty and distinguish unknown uncertainty from zero uncertainty.
5. **Reproducibility:** record data versions, checksums, transformations, code and analysis decisions.
6. **No unsupported safety claims:** IFT alone cannot establish caprock sealing, containment or site suitability.

## Repository guide

- `research/` — project decisions, source audits, benchmark protocols and research planning.
- `data/metadata/` — observation schema, data dictionary and source registers.
- `data/processed/canonical/` — traceable derivative datasets; check each accompanying audit before use.
- `scripts/` — data-ingestion and audit utilities.
- `src/`, `notebooks/`, `outputs/` — exploratory computational workflows and outputs.

Start with:
- [Research vision](research/research_vision.md)
- [Project charter and decision log](research/project_charter_and_decision_log.md)
- [Consolidated provenance matrix](research/consolidated_provenance_matrix_2026-11-21.md)
- [Jiao 2026 workbook reconciliation](research/jiao_2026_workbook_reconciliation_status_2026-11-22.md)
- [Initial data and model audit](research/initial_data_and_model_audit.md)

## Collaboration interests

I am interested in postgraduate research and research collaboration on hydrogen dissolution and retention in water-bearing geological formations, particularly the role of brine chemistry, pore confinement and mineral–fluid interactions. I can contribute to literature and experimental-data verification, Python-based data analysis, reproducible research documentation and preliminary geospatial analysis, while developing further expertise in molecular simulation and subsurface modelling under supervision.

**Current status:** exploratory and evidence-building research. Claims and datasets are subject to the limitations documented in their individual audit reports.
