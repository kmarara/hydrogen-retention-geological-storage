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
