# Janjua et al. (2024): primary-source and workbook-scope audit

**Audit date:** 2026-11-21  
**Primary article:** Janjua A N, Ali M, Murtaza M, Patil S, Kamal M S (2024). “Effects of salinity, temperature, and pressure on H2–brine interfacial tension: Implications for underground hydrogen storage.” *Journal of Energy Storage* 95, 112510. DOI: [10.1016/j.est.2024.112510](https://doi.org/10.1016/j.est.2024.112510).  
**Jiao source group:** Reference [8], workbook observations 289–423 (135 records).  
**Scope:** Published experimental design versus workbook coverage; concentration basis; method and row-value provenance. Exact IFT values are not certified by this audit.

## Primary-source information verified

The publisher abstract and the KFUPM institutional research record report:
- Density measured using an Anton Paar DMA-HP densitometer.
- IFT measured using a Krüss drop shape analyzer DSA-100.
- Pressures: 0.1, 5, 10, 15 and 20 MPa.
- Temperatures: 25, 50 and 70 °C.
- Fluid conditions: deionized water; seawater/mixed brine; and individual NaCl, KCl, MgCl2, CaCl2 and Na2SO4 brines at 1 and 3 M.

The stated matrix therefore comprises 12 fluid conditions (DI water + seawater + five salts × two concentrations) and 15 P-T combinations per condition: 180 conditions if the full stated matrix was measured.

**Method limitation:** the accessible publisher abstract and institutional record identify the DSA-100 instrument but do not identify the specific drop configuration used for IFT. A DSA-100 can be used in different drop-shape configurations; the instrument name alone is not sufficient to certify pendant versus sessile drop. The Jiao workbook method code 1 (Sessile Drop) is therefore unverified, not confirmed.

## Direct inspection of the 135 Jiao workbook rows

Workbook observations 289–423 contain exactly 135 rows. Each of the nine fluid conditions has the full 5-pressure × 3-temperature grid.

| Workbook fluid condition | Workbook concentration (mol/kg) | Rows |
|---|---:|---:|
| Deionized water | 0 | 15 |
| NaCl | 1.00 | 15 |
| NaCl | 3.21 | 15 |
| KCl | 1.00 | 15 |
| KCl | 3.47 | 15 |
| CaCl2 | 1.05 | 15 |
| CaCl2 | 3.28 | 15 |
| MgCl2 | 1.00 | 15 |
| MgCl2 | 3.23 | 15 |
| **Total** | | **135** |

The workbook temperatures are 298, 323 and 343 K, which are rounded representations of 25, 50 and 70 °C. Pressure values match the five published setpoints.

**Coverage gap:** the Jiao workbook contains DI water and four salts at two concentrations each. It contains no seawater/mixed-brine condition and no Na2SO4 condition. Relative to the article's stated design, the workbook is a nine-condition subset; it must not be described as the full 2024 Janjua dataset.

## Molarity versus molality

The published abstract describes the prepared salt solutions as 1 and 3 M (mol/L). The Jiao workbook's grouped columns are labelled “molalities of individual salts” (mol/kg), with salt-specific values:
- NaCl: 1.00 and 3.21 mol/kg
- KCl: 1.00 and 3.47 mol/kg
- CaCl2: 1.05 and 3.28 mol/kg
- MgCl2: 1.00 and 3.23 mol/kg

The non-integer values are plausible converted molalities for nominal 1 M and 3 M solutions, but the workbook does not document the calculation, density basis, reference temperature, or exact source location for these converted values. Molarity and molality are not interchangeable. The canonical record must preserve:
1. original reported concentration: 1 or 3 mol/L;
2. any converted molality as a derived value;
3. conversion equation, solution density and temperature used;
4. source coordinate and reviewer status.

Do not use the workbook molality values as if they were directly reported or independently verified by the primary paper until the conversion is traced.

## Row-level value and provenance decision

- Matrix structure: verified against the published design for the nine represented conditions.
- P-T coordinates: structurally match the published five-pressure, three-temperature grid, with workbook temperatures rounded to integer kelvin.
- Fluid coverage: partial; seawater and Na2SO4 conditions are absent from the Jiao subset.
- Concentration basis: source says M; workbook says molality. Conversion plausible but undocumented.
- IFT measurement instrument: DSA-100 confirmed.
- Drop configuration: unverified; do not certify workbook's Sessile Drop code.
- Exact IFT values: not compared row-by-row with primary numerical tables, figures, or an author data file.
- Independent-observation status: not yet globally checked for reuse/overlap with other cited sources.
- Benchmark eligibility: all 135 Jiao records remain excluded from primary benchmark eligibility pending numerical source verification and metadata resolution.

## Required next evidence

Obtain the full primary article PDF and any supplementary/raw data files, then:
1. identify the exact preparation procedure and reported 1/3 M basis;
2. determine whether authors converted molarity to molality and reproduce that conversion;
3. verify the DSA-100 drop configuration used for IFT;
4. compare all 135 IFT values against source tables/data with exact coordinates;
5. determine whether the omitted seawater and Na2SO4 cases were measured but not included in the Jiao compilation;
6. check for overlap/reuse in later benchmark datasets.

Until those steps are complete, retain the raw Jiao workbook unchanged and quarantine the 135 observations from model training.


## Additional full-text and independent-summary checks (2026-11-21)

A publisher-indexed full-text search result exposes additional article text, including the stated rationale and experimental scope, but opening the publisher full-text page returns HTTP 403. The KFUPM institutional record independently confirms the five pressure levels, three temperatures, solution families, 1/3 M preparation basis, and DSA-100 instrument. It does not identify the IFT drop configuration or expose the numerical result tables.

A later 2025 review reports broad IFT ranges by salt type for Janjua et al. (NaCl 66–76, KCl 63–77, MgCl2 66–87, CaCl2 67–87, Na2SO4 70–85 mN/m). These are secondary aggregate ranges, not point-level values with pressure, temperature and concentration coordinates; they cannot validate any of the 135 Jiao rows or be ingested as experimental observations. The 135-row Jiao subset still represents only DI water and four salts at two concentrations each, not the full 180-condition article design.

**Decision unchanged:** all 135 Jiao rows remain quarantined. The DSA-100 instrument is confirmed, but pendant versus sessile configuration remains unknown. Original 1/3 M must be retained as molarity; workbook molality values remain derived and undocumented. The next useful route is author-supplied point data or the publisher's complete tables/supplement, followed by exact row matching and independent reconstruction of any molarity-to-molality conversion from solution density and temperature.


## Additional cross-publication data-source investigation (2026-11-21)

A targeted search located Ibrahim (2025), “Advanced generalized machine learning models for predicting hydrogen–brine interfacial tension in underground hydrogen storage systems,” Scientific Reports 15, 18972, DOI: 10.1038/s41598-025-02304-4. Its methods state that a literature-compiled dataset of around 500 observations was assembled from sources including Janjua et al. (2024), with unit checks, outlier removal and duplicate filtering. The article's data-availability statement says data are provided in the manuscript or supplementary information. The PMC record exposes a 104 KB DOCX supplementary-information attachment, but the attachment retrieval endpoint returned a browser verification page during this audit.

This is a potentially useful additional secondary compilation to inspect, not primary-source evidence. It may provide a route to cross-check Janjua-derived records or reveal how the later author interpreted the source. It must not be treated as an independent experimental campaign or as a substitute for Janjua's original tables. The later paper's reported dataset statistics are not sufficient to validate any individual Janjua observation.

The 2025 article's stated dataset size is approximate. No row-level Janjua mapping or exact 135-value match has yet been established. The article's model validation design is not adopted for this project; our publication-held-out benchmark protocol remains unchanged.

**New retrieval lead:** obtain and inspect the 2025 supplementary DOCX (PMC attachment 41598_2025_2304_MOESM1_ESM.docx) and determine whether it contains row-level experimental data, source attribution, or only model/configuration information. If row-level values are present, compare them with the 135 Jiao Janjua rows as a secondary cross-check while preserving Janjua's original paper as the authority.

**Decision unchanged:** no Janjua IFT value is newly verified by this discovery. All 135 Jiao rows remain quarantined pending exact primary-source numerical verification and resolution of method configuration and concentration-conversion provenance.


## Inspection of user-provided Ibrahim (2025) supplementary DOCX (2026-11-21)

The user supplied the supplementary DOCX for Ahmed Farid Ibrahim's 2025 *Scientific Reports* article. The file was inspected as a Word document, including its embedded 102-page table layout. Its first table is headed “Data Set used in the study” and contains 498 data records across literature sources. Janjua et al. (2024), DOI 10.1016/j.est.2024.112510, is explicitly attributed in 180 records (table rows 81–260, counting the header as row 1). The Janjua block therefore contains the complete 180-row nominal design represented in this secondary compilation, rather than only the 135-row subset in the Jiao 2026 workbook.

The 180 rows report:
- Pure H2 (CO2=0, CH4=0, H2=100%);
- temperatures 77, 122 and 158 °F (nominally 25, 50 and 70 °C);
- pressures 14.5, 725, 1450, 2175 and 2900 psi (nominally 0.1, 5, 10, 15 and 20 MPa);
- nine explicitly distinguishable table labels: deionized water, seawater, 1M/3M NaCl, 1M/3M KCl, and nominally 1M MgCl2, 1M CaCl2 and 1M Na2SO4.

**Critical label ambiguity:** MgCl2, CaCl2 and Na2SO4 each appear as two distinct 15-row condition blocks at each temperature series, but both blocks are labelled “1M-[salt]” in the DOCX. These appear structurally consistent with two concentration levels in the original 1 M/3 M design, but the second block must NOT be relabelled 3 M without confirmation from Janjua's original source. Retain the printed label and add a separate ambiguity flag. This is a concrete data-quality issue in the secondary compilation.

The DOCX table's header labels temperature as °F and pressure as psi. The reported 77/122/158 °F values correspond to 25/50/70 °C after conversion; the reported 14.5/725/1450/2175/2900 psi correspond approximately to 0.1/5/10/15/20 MPa. These are secondary-compilation values and rounded unit representations, not proof of exact original values or measurement precision.

A 180-row extraction was generated at `data`-working-copy level for review as `/mnt/data/janjua_2024_secondary_compilation_180_rows.csv`. SHA-256: `4caa78d873ba364324c84fffb193a227062d9c9d887c5c13b8251733209010a0`. The supplied DOCX SHA-256 is `fe596ef7db579fa51a2095c5e53b862c158f5a4cb3b16323725d628b6df5aa03`. The extraction preserves the table row index and every printed field; all 180 extracted rows are distinct.

**Evidence status remains secondary_only.** This supplementary dataset is a later ML author's compilation, not Janjua's original primary data. It can guide source reconciliation and reveal missing design blocks, but cannot independently certify the experimental values, exact concentration labels for the ambiguous blocks, measurement configuration, uncertainty, or molarity-to-molality conversions. The 135 Jiao rows must still be compared row-by-row with the 180 Ibrahim supplementary rows, and both must ultimately be checked against Janjua's original tables or author-provided data. No row is promoted to primary benchmark eligibility on the basis of this DOCX alone.

The uploaded DOCX is 102 pages in rendered layout; the key Janjua entries span its Table S1 rows 81–260 (approximately pages 17–53; page layout is dense and repeated table continuation). Visual/table parsing should be checked against the Word table structure before any row-level transcription is published.


## 2026-11-21 follow-up: Ibrahim (2025) secondary-compilation methodology review

The full text of Ibrahim (2025), DOI 10.1038/s41598-025-02304-4, was reviewed through the PubMed Central version (PMCID PMC12125213).

### What the paper explicitly reports
- The author compiled approximately 500 IFT data points from multiple literature sources, including Janjua et al. (2024).
- The QA/QC procedure is described as unit-consistency checks, outlier removal, duplicate filtering, visual inspection and statistical diagnostics.
- The manuscript does not provide, in the inspected methodological text, a row-level change log identifying which Janjua records were removed, retained, altered or relabelled.
- The model-development description uses random subsampling cross-validation with random train/test ratios, a 100-point validation set described as unseen, and tenfold cross-validation. The inspected text does not state that the 100-point validation set is held out by publication/source study.
- The supplementary information is linked by the article, and the data availability statement says data are provided in the manuscript or supplementary information.

### Consequence for Janjua reconciliation
The Ibrahim 180-row block is a valuable secondary transcription/comparison source, but it cannot independently establish the original Janjua measurements or the identity of ambiguous concentration blocks. In particular:
- Do not infer that two blocks both printed as 1M are actually 1M and 3M.
- Do not infer that Ibrahim's outlier/duplicate filtering preserved every original Janjua observation.
- Do not use Ibrahim's model validation results as evidence of publication-independent generalisation.
- Retain the 180 rows as secondary-only and benchmark-ineligible until each row is traced to Janjua's original article/SI or confirmed by the authors.

### Retrieval status
A targeted search located Janjua's publisher article record and KFUPM institutional record, both confirming the 5-pressure × 3-temperature design and the listed fluid systems. No publicly indexed original pointwise supplementary file was located in this search. The publisher article page was inaccessible to direct inspection during this pass; absence of a located SI link is not proof that no SI exists.

### Next evidence required
1. Original Janjua pointwise data (publisher SI, author-provided workbook, or explicit author confirmation).
2. Jiao 2026 supplementary workbook to compare its 135 Janjua rows against the 180 Ibrahim rows.
3. Clarification of the duplicated 1M labels in Ibrahim's MgCl2, CaCl2 and Na2SO4 blocks.
4. A row-level reconciliation log documenting exact matches, conversion-only matches, mismatches, omitted conditions and unresolved cases.

**Status remains unchanged:** all Janjua records in both secondary compilations remain excluded from the primary benchmark pending primary-source verification.


## 2026-11-21: row-level comparison with Jiao 2026 and Ibrahim 2025 secondary compilations

The user re-uploaded the Jiao 2026 supplementary workbook (sheet `Experiment data from literature`) and the previously extracted Ibrahim 2025 supplementary Janjua block was available for direct comparison. The 135 Jiao rows are observations 289–423; the Ibrahim DOCX-derived Janjua block contains 180 rows.

### Comparison procedure
- Matched rows by fluid-condition group and the five pressure × three temperature coordinates, not by source row order.
- Converted Ibrahim's printed pressure from psi to MPa using 0.006894757293 MPa/psi and temperature from °F to K using `(°F − 32) × 5/9 + 273.15`.
- Compared the two IFT values in mN/m.
- For the duplicated Ibrahim CaCl2 and MgCl2 labels, separated the two repeated 15-condition blocks using their repeated five-pressure sequences at each temperature. The block pairing to Jiao's lower/higher molality group is an observed cross-compilation pattern, not confirmation of the original Janjua concentration label.

### Results
- **135/135 Jiao observations** have a corresponding pressure-temperature condition in the Ibrahim Janjua block.
- All 135 P-T pairs reconcile within the precision of the printed units (maximum absolute pressure difference approximately 0.00521 MPa; maximum temperature difference 0.15 K).
- **13/135 IFT values are numerically identical** at the displayed precision.
- **134/135 differ by no more than 0.05 mN/m**; mean absolute difference is approximately 0.02644 mN/m.
- One material discrepancy requires review: Jiao observation 396 reports 74.46 mN/m; Ibrahim secondary-table row 183 reports 74.80 mN/m. The paired condition is CaCl2, 10 MPa, 77 °F in Ibrahim (approximately 298 K); Jiao-minus-Ibrahim difference is −0.34 mN/m. Neither secondary value is promoted as correct.
- The Jiao 135-row subset corresponds to nine represented condition groups: DI water; NaCl and KCl at two concentrations each; CaCl2 and MgCl2 in two molality-like groups each.
- The Ibrahim 180-row block additionally contains 15 seawater rows and 30 Na2SO4 rows, accounting for the 45 records not represented in Jiao's Janjua subset.

### Concentration-label issue retained
Ibrahim's supplementary table prints both CaCl2 blocks as `1M-CaCl2` and both MgCl2 blocks as `1M-MgCl2`. Jiao's corresponding salt columns distinguish lower and higher values (CaCl2 1.05/3.28 mol/kg; MgCl2 1.00/3.23 mol/kg). The higher blocks pair numerically with the second Ibrahim block, but the printed Ibrahim labels remain ambiguous. **Do not relabel the second blocks as 3 M** until Janjua's primary article/SI or the authors confirm this. Similarly, do not treat Jiao's workbook molality-like values as primary-reported concentrations; the primary design is described as 1/3 M and any conversion remains undocumented.

### Method and eligibility
All 135 Jiao rows carry method code 1, which the Jiao workbook legend maps to Sessile Drop. This is a secondary workbook assignment only. Janjua's accessible primary-source records identify the Krüss DSA-100 but do not establish the IFT drop configuration. Therefore this comparison does not resolve the method conflict/uncertainty.

The Ibrahim DOCX is a secondary ML compilation and Jiao is also a secondary compilation. Their close numerical agreement is a cross-source consistency check, not independent experimental replication and not primary-source verification. The 180 Ibrahim records and 135 Jiao records remain benchmark-ineligible. The original Janjua numerical tables/SI or author-supplied data are still required, especially to resolve observation 396, the duplicate CaCl2/MgCl2 labels, concentration conversions, method configuration, and uncertainties/repeatability.

A row-level comparison CSV was generated for the user in this conversation. It preserves both printed source values, converted P-T values, the source-row mapping, the secondary printed salinity label, and the single mismatch flag. The GitHub audit records the aggregate findings and the exact discrepant row.
