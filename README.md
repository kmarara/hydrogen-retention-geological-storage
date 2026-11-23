# Hydrogen Retention and Fluid–Rock Interactions in Underground Hydrogen Storage

**Current research focus:** Hydrogen dissolution, retention and loss in water-bearing geological formations.

**Researcher:** Kudakwashe Marara  
**Background:** BSc (Hons) Petroleum Chemistry and Technology, University of Zimbabwe (Upper Second Class, 2.1)  
**Contact:** kudakwashe.d.marara@gmail.com  
**GitHub:** https://github.com/kmarara

## Research direction

This repository documents an evolving, independently developed research programme focused on the question:

> **How do brine chemistry, pore confinement and mineral–fluid interactions influence hydrogen dissolution, retention and loss in geological formations considered for underground hydrogen storage?**

My interest in underground hydrogen storage developed during the Pio Petro Online Internship (August–November 2026), where exposure to subsurface geology and underground hydrogen storage prompted me to investigate the subject further. I continued this learning independently through literature review, source verification and exploratory computational work. The internship was the starting point for this research interest; the work documented here represents subsequent self-directed development.

A key motivation is the research of Zhang and co-authors on hydrogen dissolution and gas storage in water-saturated kaolinite nanopores:

- Zhang et al. (2023), *Molecular Simulation of H₂ Loss by Dissolution in Caprock Water-Saturated Nanopores under the Nanoconfinement Effect for Underground Hydrogen Storage*, **Energy & Fuels**. https://doi.org/10.1021/acs.energyfuels.3c03384
- Zhang et al. (2023), *Molecular Simulation of H₂/CH₄ Mixture Storage and Adsorption in Kaolinite Nanopores for Underground Hydrogen Storage*, **ACS Omega**. https://doi.org/10.1021/acsomega.3c06475

These studies motivate further examination of water saturation, pore size, mineral surface chemistry and brine composition. They do not imply that I have already performed molecular-dynamics simulations; learning and applying suitable pore-scale methods is a proposed direction for supervised postgraduate research.

## Research work programme

The programme has one scientific centre—**hydrogen retention and loss in water-bearing geological formations**—with supporting work packages.

### 1. Experimental evidence for H₂–brine behaviour

An ongoing source-verification effort examines published hydrogen–brine interfacial-tension (IFT) observations. It checks original sources, fluid composition, experimental method, units, uncertainty and data lineage before observations are used in modelling.

The current stage-one candidate tranche contains 158 observations attributed to Chow et al. (2018), Hosseini et al. (2022) and Mirchi et al. (2022). It is **not a released benchmark**: cross-study overlap review, full schema/conversion validation and final eligibility gates remain open.

IFT and solubility are distinct physical properties. The IFT dataset is not a substitute for H₂-solubility measurements. A separately sourced H₂-solubility evidence set is a possible future task, subject to the availability and quality of primary experimental data.

### 2. Pore-scale fluid–rock interactions

The proposed scientific extension is to examine how water saturation, pore confinement, mineralogy and brine chemistry influence hydrogen dissolution and adsorption. Molecular simulation is a method to be learned under appropriate supervision; no molecular-dynamics study is claimed as completed.

### 3. Geological screening context

The repository retains an exploratory Python geospatial site-screening workflow developed earlier in the learning process. It is supporting context, not the primary research direction. Its geological inputs are coarse, it does not currently represent hydrogen loss or all hydrogen-sensitive mineral, ionic and microbial conditions, and its outputs are not validated storage-safety or site-selection recommendations.

## Work completed and current limitations

- Built an exploratory Python geospatial workflow and performed preliminary weighted-overlay sensitivity analysis.
- Audited published H₂–brine IFT data for source provenance, fluid chemistry, experimental method and uncertainty.
- Structurally inspected the Jiao et al. (2026) supplementary workbook and documented unresolved source-reconciliation issues.
- Created a 158-observation stage-one IFT candidate tranche; it has not passed all benchmark-release gates.
- Audited the legacy PINN implementation and found that it does not implement the Peng–Robinson EOS-constrained PINN described in earlier project text. It is not presented as a validated PINN.

The repository does **not** claim a completed H₂-solubility benchmark, completed molecular-dynamics simulations, a validated field-scale hydrogen-loss model, a validated PINN, or a field-scale storage-safety score.

## Research principles

1. **Primary-source traceability:** every observation used in analysis must have a traceable source and extraction location.
2. **Chemistry-aware comparison:** preserve electrolyte identity, concentration basis, gas composition, method and measurement conditions.
3. **Separate evidence types:** distinguish measurements, digitised values, derived data, correlations, simulations and unverified records.
4. **Uncertainty:** preserve reported uncertainty and distinguish unknown uncertainty from zero uncertainty.
5. **Reproducibility:** record data versions, checksums, transformations, code and decisions.
6. **Bounded interpretation:** IFT alone cannot establish caprock sealing, containment or site suitability; nanoscale findings cannot be directly converted into field-scale safety claims.

## Repository map

- `research/` — research vision, project decisions, source audits and evidence limitations.
- `literature/` — literature landscape and comparison material.
- `data/` — metadata and traceable candidate datasets; consult the accompanying audits before use.
- `scripts/`, `src/`, `notebooks/` — computational and audit workflows.
- `outputs/` — exploratory outputs, not validated site recommendations.

Start with the [research vision](research/research_vision.md) and [project charter](research/project_charter_and_decision_log.md).

## Collaboration interests

I am interested in postgraduate research on hydrogen dissolution and retention in water-bearing geological formations, especially the roles of brine chemistry, pore confinement and mineral–fluid interactions. I can contribute petroleum-chemistry training, laboratory experience, literature and experimental-data verification, Python-based analysis and reproducible documentation, while developing further expertise in molecular simulation and subsurface modelling under supervision.

**Current status:** exploratory, self-directed and evidence-building research. The scope and claims are intentionally bounded by the limitations documented in the repository.
