# Higgs et al. (2022): primary-source verification audit

**Audit date:** 2026-11-21  
**Published source:** Higgs S, Wang Y D, Sun C, Ennis-King J, Jackson S J, Armstrong R T, Mostaghimi P (2022). “In-situ hydrogen wettability characterisation for underground hydrogen storage.” *International Journal of Hydrogen Energy* 47(26), 13062–13075. DOI: [10.1016/j.ijhydene.2022.02.022](https://doi.org/10.1016/j.ijhydene.2022.02.022).  
**Jiao workbook group:** Ref [3], 36 observations, workbook observation numbers 144–179.

## Sources inspected

1. Published ScienceDirect article record and abstract.
2. EarthArXiv-hosted pre-publication manuscript PDF, titled “In-situ hydrogen wettability characterisation for Underground Hydrogen Storage” (version states it had not yet been peer reviewed or formally accepted at the time of posting).
3. Jiao et al. (2026) supplementary workbook, sheet “Experiment data from literature”, Ref [3] rows.

The preprint PDF contains Appendix Tables 3–8 with numerical IFT observations, which are not exposed in the accessible publisher abstract. The published abstract independently confirms the key endpoint values and experimental scope. The preprint and final published version must still be reconciled before final certification.

## Verified study-level metadata

- System: hydrogen + distilled water / aqueous NaCl solutions.
- IFT measurement: pendant-drop method. The preprint methods section explicitly states IFT was determined using pendant drop; captive bubble was used for contact-angle work.
- Temperature: 298 K in the appendix IFT tables (25 °C).
- High-pressure IFT range: approximately 6.89–20.68 MPa.
- Brine: NaCl solutions. The manuscript materials describe 1000, 2000 and 5000 ppm solutions for captive-bubble experiments; IFT appendix tables include concentration-specific subsets.
- Hydrogen purity: 99.99% according to the preprint.
- IFT image processing: ImageJ analysis, calibrated using a 1.52 mm needle; pendant-drop geometry and density difference used in the IFT calculation.
- Reported high-pressure distilled-water endpoint: 72.45 mN/m at 6.894757 MPa and 69.43284 mN/m at 20.68427 MPa.

## Row-level numerical comparison

All 36 Jiao workbook IFT values in observations 144–179 were compared against the numerical IFT values presented in the preprint appendix (Tables 3–8). The values agree at the workbook's reported two-decimal precision. The preprint appendix provides more digits for many observations; the workbook is a rounded transcription.

The row groups cover low-pressure distilled-water observations, low-pressure saline observations, high-pressure distilled-water observations and high-pressure saline observations. The preprint tables also report pressure and density difference, while the Jiao workbook retains rounded pressure and IFT but does not preserve the source density-difference values.

**Important qualification:** this is a 36/36 numerical match to the accessible preprint appendix at the workbook's displayed precision. It is not yet a final-version certified match because the accessible publisher record does not expose the final article's full tables or supplementary numerical data. The preprint itself expressly identifies its status as not yet peer reviewed/formally accepted.

## Metadata and interpretation cautions

1. **Method code:** Jiao code 0 = Pendant Drop; the preprint explicitly confirms pendant drop for IFT. This is supported.
2. **Salinity:** preserve the original source basis in ppm and record any molality conversion as derived. The workbook values 0.0171, 0.0342 and 0.0856 mol/kg are numerically consistent with approximate NaCl molalities for 1000, 2000 and 5000 ppm if ppm is interpreted as mg NaCl per kg solution/water under a specified convention. The preprint's precise ppm preparation convention should be checked against the final published methods before promoting converted values.
3. **Temperature:** workbook 298 K is the source's 298 K, not 298.15 K; do not silently replace the reported value.
4. **Pressure:** workbook pressure is rounded to two decimal places relative to appendix values (e.g., 6.894757 MPa becomes 6.89 MPa). Preserve both original and normalized precision.
5. **Uncertainty:** the preprint describes measurement/resolution error bars in parts of the paper, but an observation-level IFT uncertainty field was not established from the accessible appendix. Do not assign an uncertainty value without the final methods/results definition.
6. **Scope:** the paper includes contact-angle measurements and other methods; only the pendant-drop IFT records belong in this IFT benchmark. Do not import contact-angle values as IFT observations.
7. **Independence:** the preprint states that the apparatus was calibrated against Chow et al. nitrogen-water measurements. Those calibration values are not the 36 H2-brine IFT observations and must not be mistaken for independent H2 observations. The publication's references and data lineage still need a complete overlap check.

## Eligibility decision

**Numerical status:** 36/36 values match the preprint appendix at two-decimal workbook precision.  
**Method status:** pendant drop verified in preprint methods.  
**Primary benchmark eligibility:** keep quarantined pending final-published-version reconciliation, exact row-coordinate capture, and concentration-basis/uncertainty review. Do not claim final primary-source certification solely from the preprint.

## Required next actions

1. Obtain the final published full text or author supplementary file and reconcile all 36 values against the preprint appendix.
2. Record exact table and row coordinates for each observation.
3. Verify the original ppm preparation basis and document molality conversions separately.
4. Resolve whether reported error bars quantify measurement uncertainty, image-resolution uncertainty, or both, and capture only what the paper explicitly defines.
5. Run cross-publication overlap checks, including the Chow calibration series, before assigning independent observation IDs.
6. If final-version values are unchanged, promote these 36 observations to table-extracted provenance with a source-specific eligibility decision.

## Sources

- Published article: https://www.sciencedirect.com/science/article/pii/S0360319922005456
- Preprint PDF: https://eartharxiv.org/repository/object/2762/download/5615/
- DOI: https://doi.org/10.1016/j.ijhydene.2022.02.022


## Final-publication reconciliation checkpoint (2026-11-21)

The publisher record confirms that the work was formally published as Scott Higgs et al., “In-situ hydrogen wettability characterisation for underground hydrogen storage,” *International Journal of Hydrogen Energy* 47(26), 13062–13075 (26 March 2022), DOI 10.1016/j.ijhydene.2022.02.022. The EarthArXiv record explicitly links this preprint to that published version. However, the accessible publisher record exposes bibliographic information and highlights, not the final article's numerical IFT tables or a downloadable supplementary dataset. I therefore **cannot certify that the 36 preprint appendix rows are unchanged in the final version**. Their existing 36/36 match is a preprint-level numerical match only; do not relabel it as final-publication verification.

The preprint appendix records six IFT blocks: 7 low-pressure distilled-water rows, 4 low-pressure 2000-ppm NaCl rows, 2 low-pressure 5000-ppm NaCl rows, 9 high-pressure distilled-water rows, 9 high-pressure 1000-ppm NaCl rows, and 5 high-pressure 5000-ppm NaCl rows. The reported IFT method is pendant drop; the captive-bubble method applies to the contact-angle measurements, not the IFT observations. Temperature is approximately 298 K throughout. Preserve original pressure values and the reported ppm basis; do not silently convert ppm to molality without confirming the preparation basis.

A separate 2024 synthesis/modeling paper by Hosseini and Leonenko states that the Higgs and Esfandyari data were inconsistent with trends in the other samples and were assigned to an “extra set” rather than ordinary train/test allocation. This is not proof that the Higgs measurements are erroneous; it is an independent warning that the data should be examined as a distinct external challenge set, with source and methodological differences investigated before pooling. The study's treatment strengthens the case for quarantining Higgs rows from the primary benchmark until final-version and data-lineage verification is complete.

**Disposition:** all 36 Higgs rows remain quarantined. Required evidence: final publisher PDF or author-supplied final tables/data; row-by-row comparison against the preprint appendix; exact salinity preparation basis and uncertainty semantics; and review of the later-reported trend discrepancy. No Higgs rows have been added to the canonical stage-1 dataset.
