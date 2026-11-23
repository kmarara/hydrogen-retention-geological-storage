# Project Charter and Decision Log

**Project:** Hydrogen retention and loss in water-bearing geological formations  
**Researcher:** Kudakwashe Marara  
**Last reviewed:** 2026-11-23

## Origin and motivation

The research interest developed during the Pio Petro Online Internship (August–November 2026), through exposure to subsurface geology and underground hydrogen storage. That exposure prompted further independent study and the development of this research programme. The internship is the origin of the research interest, not evidence that all subsequent repository work was conducted as part of the internship.

## North-star objective

Develop a rigorous, evidence-led understanding of how brine chemistry, pore confinement and mineral–fluid interactions influence hydrogen dissolution, retention and loss in geological formations considered for underground hydrogen storage.

Experimental fluid-property verification and preliminary geological screening are supporting work packages, not independent competing research directions.

## Primary research question

How do brine chemistry, pore confinement and mineral–fluid interactions influence hydrogen dissolution, retention and loss in water-bearing geological formations?

## Supporting questions

1. What primary experimental evidence exists for H₂–brine interfacial properties and H₂ solubility, and what are its source, chemistry, method and uncertainty limitations?
2. How do water saturation, pore size, mineral surface chemistry and brine composition affect hydrogen dissolution and adsorption in published experimental and simulation studies?
3. Under what conditions can bulk-fluid measurements inform, and where do they fail to represent, confined pore-scale behaviour?
4. What evidence can responsibly inform geological screening, and what additional data and upscaling are required before making storage-suitability claims?

## Work packages

### WP1 — Experimental evidence

Continue source verification of H₂–brine interfacial-tension (IFT) data. Treat IFT and solubility as distinct properties. A separate H₂-solubility dataset is a proposed future task only if suitable primary experimental sources and metadata can be obtained.

### WP2 — Pore-scale fluid–rock interactions

Build a critical evidence base on hydrogen dissolution and adsorption in water-bearing mineral nanopores. Molecular simulation is a training/research method to be selected with a supervisor; no completed molecular-dynamics work is claimed.

### WP3 — Geological implications

Retain the existing Southern Africa geospatial framework as exploratory supporting infrastructure. Its geological inputs are coarse; hydrogen loss and hydrogen-sensitive minerals, ions and microorganisms are not comprehensively represented. Its outputs are not validated site-safety recommendations.

## Scope boundaries

### In scope
- Hydrogen dissolution and retention in water-bearing geological media.
- Brine chemistry, water saturation, pore confinement and mineral surface interactions.
- Primary-source verification and separate treatment of IFT, solubility, adsorption and simulation evidence.
- Learning and, where justified, reproducing published pore-scale methods under supervision.
- Carefully bounded geological implications.

### Out of scope unless separately justified
- Claiming IFT alone predicts hydrogen loss, caprock sealing or site safety.
- Claiming a completed H₂-solubility benchmark before primary data verification.
- Claiming molecular-dynamics expertise or completed simulations.
- Claiming the legacy PINN is a validated Peng–Robinson EOS-constrained PINN.
- Treating coarse GIS weighted-overlay outputs as validated site rankings.
- Promising a new foundation model or broad multi-physics framework before evidence and scope justify it.

## Existing research assets and status

- **H₂–brine IFT:** 158-observation stage-one candidate tranche from Chow (2018), Hosseini (2022) and Mirchi (2022). Not yet a released benchmark; global overlap and release validation remain open.
- **Jiao et al. (2026) workbook:** 450 secondary-compilation observations structurally inspected and source groups audited. It is not approved as a primary benchmark dataset; group-specific unresolved issues remain documented.
- **Geospatial site-screening framework:** exploratory Python workflow; coarse geological inputs and no validated hydrogen-loss or hydrogen-sensitive-strata term.
- **Legacy PINN:** audit found that the current implementation does not implement the Peng–Robinson EOS-constrained PINN described in earlier project text. Do not present it as validated.
- **Molecular simulation:** no simulations completed by the researcher.

## Evidence rules

- Preserve source DOI and exact page, table, figure or supplement location.
- Preserve original values, units, concentration basis, fluid composition, method and reported uncertainty.
- Separate measured, table-extracted, digitised, derived, correlation-generated, simulation and unverified evidence.
- Never silently correct an original source or workbook; make traceable derivative records.
- Distinguish unknown uncertainty from zero uncertainty.
- Record checksums, code versions, transformations and decisions.

## Decision log

- **2026-11-21:** The earlier project emphasis was a source-aware H₂–brine IFT predictive-model benchmark. Source audits and data products are retained as supporting research assets.
- **2026-11-22:** Jiao workbook reconciliation documented; no 450-row workbook release or model training authorised.
- **2026-11-23:** Research identity narrowed around hydrogen retention and loss in water-bearing geological formations, with brine chemistry, pore confinement and mineral–fluid interactions as the central scientific factors.
- **2026-11-23:** IFT benchmark retained as WP1 evidence-quality work; H₂ solubility is a separate proposed evidence stream, not inferred from IFT.
- **2026-11-23:** Existing site-screening framework retained only as exploratory downstream context; no safety or suitability claims.
- **2026-11-23:** Molecular simulation is a proposed training/research method, not an existing researcher capability or completed result.
- **2026-11-23:** Repository README and public-facing project identity are being repositioned to explain that the research interest originated during the Pio Petro Online Internship and developed through independent follow-up work.

## Immediate gates

1. Review legacy top-level documents and clearly mark or archive those that describe the superseded site-selection-first direction.
2. Complete source audits and release checks before calling the IFT candidate tranche a benchmark.
3. Assess availability and quality of primary H₂-solubility experimental data before committing to a solubility dataset.
4. Select one tractable pore-scale mechanism and identify appropriate training, software, data and validation with a prospective supervisor.
5. Do not directly convert nanoscale results into field-scale safety scores.
