# Isfehani et al. (2023): primary-source verification audit

**Audit date:** 2026-11-21  
**Source:** Isfehani ZD, Sheidaie A, Hosseini M, Fahimpour J, Iglauer S, Keshavarz A (2023). “Interfacial tensions of (brine + H2 + CO2) systems at gas geo-storage conditions.” *Journal of Molecular Liquids* 374, 121279. DOI: [10.1016/j.molliq.2023.121279](https://doi.org/10.1016/j.molliq.2023.121279).  
**Jiao workbook group:** Ref [5], observations 196–267 (72 rows).

## Scope and evidence inspected

The publisher's ScienceDirect article record and the Edith Cowan University research repository record were inspected. Both identify the same paper and publication details. The ECU repository record gives the publication date as 15 March 2023 and identifies a CC BY 4.0 licence. Its download link was attempted but returned HTTP 403 in this audit session. The publisher page exposes the abstract and article metadata but not the full methods, numerical tables, figures or supplementary numerical data in the accessible result.

## Findings supported by accessible primary-source metadata

1. **System identity:** the paper concerns interfacial tensions for brine + H2 + CO2 systems, with CO2 as cushion gas.
2. **Measurement method:** the article abstract explicitly states that IFT was measured using the pendant-drop method. This supports the study-level method assignment Pendant Drop (Jiao workbook code 0), subject to confirming the workbook's row-level records all belong to this study and this measurement series.
3. **Study variables and reported trends:** the abstract states that the study varied CO2 fraction, reservoir pressure, temperature and water salinity. It reports lower IFT with increasing CO2 fraction, pressure and temperature, and a linear increase with brine salinity.
4. **Publication identity:** *Journal of Molecular Liquids*, volume 374, article 121279, published 15 March 2023.

## Not yet verified

- None of the 72 Jiao workbook IFT values has been matched to a numerical table, figure coordinate, supplementary data row or author-provided raw-data file in this audit.
- Exact source locations for each observation are unavailable.
- The workbook's three CO2 fractions (0.3, 0.5, 0.7), three NaCl molalities (0, 1.05, 3.15 mol/kg), and associated P/T grid have not been independently checked against the full paper.
- Gas composition semantics (whether CO2 fraction is mole fraction and whether H2 is the balance), concentration basis and any conversions have not been confirmed from the full methods.
- Measurement uncertainty, replicate treatment, density inputs and instrument/configuration details beyond pendant-drop method have not been verified.
- Reuse of any measurements from prior publications or validation datasets has not been ruled out.

## Data-access limitation

The ECU repository record identifies a CC BY 4.0 licence and exposes a Download link, but following that link returned HTTP 403 in this session. The accessible ScienceDirect record provides the abstract and article metadata, not the numerical tables. The publisher's data-availability text reads “No data was used for the research described in the article”; this statement does not provide a downloadable measurement dataset and should not be interpreted as evidence that the experimental measurements do not exist.

## Eligibility decision

**Do not promote the 72 Jiao records to primary benchmark eligibility yet.** Keep all 72 quarantined as unverified secondary-compilation records until the original numerical observations and row-level source coordinates are obtained and reconciled.

The study-level pendant-drop method is supported by the abstract. It is reasonable to correct/retain the study-level method label as Pendant Drop in an audit annotation, but this does not certify the numerical observations or all row-level metadata.

## Required next actions

1. Obtain the complete article PDF and any supplementary files through an accessible repository route or directly from the authors.
2. Transcribe the original numerical tables or digitise figures with documented calibration and uncertainty.
3. Match all 72 workbook observations against primary-source coordinates, including P, T, CO2 fraction, salinity and IFT.
4. Verify original concentration basis and gas-composition basis; preserve source-reported units and record conversions separately.
5. Check the paper's references and methods for reused/validation measurements and assign duplicate-group identifiers where applicable.
6. Only after the above, classify rows as table_extracted or figure_digitised and reconsider benchmark eligibility.

## Sources

- Publisher article record: https://www.sciencedirect.com/science/article/pii/S016773222300082X
- ECU institutional repository record: https://ro.ecu.edu.au/ecuworks2022-2026/1859/
- DOI: https://doi.org/10.1016/j.molliq.2023.121279


## Additional access and provenance checks (2026-11-21)

The ECU repository record was reopened and its explicit Download link followed. The repository resolves the file to a `cgi/viewcontent.cgi` endpoint, which returned HTTP 403 in this session. The record itself explicitly identifies the article as CC BY 4.0 and confirms pendant-drop IFT measurements; the publisher's accessible article record likewise confirms pendant-drop measurements and states “No data was used for the research described in the article.” That data-availability statement does not provide raw experimental values and does not establish that the 72 Jiao points are source-verified. A ResearchGate record was also checked and explicitly indicates that no full text is available there, offering only an author full-text request. No alternative public numerical table or raw-data repository was located in this search pass.

**Decision unchanged:** 72 rows remain quarantined. Do not reconstruct the numerical table from the Jiao compilation or use trend statements as substitute measurements. The most efficient next route is a direct request to the corresponding author(s) for the accepted manuscript and row-level data/table, including exact gas fractions, salt basis, pressure/temperature coordinates, uncertainty and any reused validation points.


## Primary supplementary-information reconciliation (2026-11-21)

A four-page DOCX supplied for this audit was inspected directly. It is the Isfehani et al. supporting information titled **“Interfacial tensions of (brine + H2 + CO2) systems at gas geo-storage conditions”** and contains three numerical tables:

- Table S1, page 2: 70% CO2 + 30% H2.
- Table S2, page 3: 50% CO2 + 50% H2.
- Table S3, page 4: 30% CO2 + 70% H2.

Each table contains 24 observations: two temperatures (50 and 80 °C), three reported molality values (0, 1.05 and 3.15 mol/kg), and four pressures (500, 1200, 2000 and 3000 psi). Total primary-SI observations: **72**.

### Row-by-row reconciliation against Jiao et al. (2026)

All 72 primary-SI observations were matched one-to-one to Jiao workbook Ref [5], observations 196–267:

- Primary SI rows extracted: **72/72**.
- Jiao Ref [5] rows reconciled: **72/72**.
- Exact IFT central-value matches: **72/72** at the two-decimal precision reported in the SI.
- Pressure, temperature and reported molality combinations: all matched after accounting for rounded conversions in Jiao (psi to MPa; °C to K).
- Jiao method code: **0 for all 72**, corresponding to Pendant Drop in the workbook legend. The publisher abstract independently states that pendant-drop measurements were used.
- Primary-source coordinates: recorded as table, page, data row and left/right temperature block in the extraction.

### Critical secondary-workbook gas-species mapping error

For all 72 Isfehani rows, the Jiao workbook places the source CO2 percentage (0.3, 0.5 or 0.7) in the **CH4** column and leaves the **CO2** column at zero. This is inconsistent with the primary SI table titles, which explicitly identify CO2 + H2 mixtures. The canonical derivative corrects this mapping by preserving the source gas-composition wording and not carrying the erroneous Jiao CH4 assignment into the corrected CH4/CO2 feature fields. The original Jiao workbook is not modified.

This is a metadata/species-mapping defect in the secondary compilation; it is not a discrepancy in the 72 IFT values.

### Extraction and checksums

- Primary SI supplied for this audit: SHA-256 `61066a67d6e70991a3e0f60c476df23c143f802b2764b1c7fe194f3a07e0c033`.
- Jiao workbook: SHA-256 `9ef4197720c9f37237bda9de8bc666d5deca63d209ccb24c4f957f010efb6d84`.
- Local 72-row extraction: `/mnt/data/recovered/isfehani_2023_ift_observations.csv`, SHA-256 `02165e8fabe442b976716d5220e104253676f5c42f3fb39af64e3f4dc68c25cd`.
- Local 230-row extracted inventory (158 prior candidate rows + 72 Isfehani rows): SHA-256 `853a8c37882e94d53f8c304f4ac07c08ee49db3379e82afb03fe02867a59ac31`.

### Remaining metadata gaps and eligibility

The supplied SI reports molality values but does not identify the salt species/complete brine recipe, explicitly state the basis of the gas percentages, or report measurement uncertainty/repeatability. The article abstract verifies the pendant-drop method, but does not close those missing row-level metadata fields. These omissions are not filled by transferring composition details from other Isfehani publications.

Accordingly, all 72 observations are classified as `table_extracted` and source-numerically verified, but `benchmark_eligible_primary=false` and `reviewer_status=verified_with_metadata_gaps` pending chemistry and uncertainty review. They are retained as primary-source extracted data, not promoted into the currently eligible training tranche.

### Revised email decision

A request to Dr Mirhasan Hosseini for the 72 numerical values is no longer necessary: the supplied primary SI provides them and all 72 reconcile exactly. A narrowly targeted clarification request may still be useful for the exact brine recipe/salt identity, gas-percentage basis, uncertainty/repeatability and any reused validation measurements.

### Sources

- Primary supporting information supplied in this conversation (Tables S1–S3, pages 2–4).
- Publisher article record: https://www.sciencedirect.com/science/article/pii/S016773222300082X
- ECU institutional record: https://ro.ecu.edu.au/ecuworks2022-2026/1859/
- DOI: https://doi.org/10.1016/j.molliq.2023.121279
