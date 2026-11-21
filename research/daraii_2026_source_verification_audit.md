# Daraii et al. (2026) source-verification audit

**Audit date:** 2026-11-21  
**Primary source DOI:** [10.1016/j.ptlrs.2025.11.004](https://doi.org/10.1016/j.ptlrs.2025.11.004)  
**Article:** Daraii F, Moradi P, Bahreini S A, Anvari S. *Experimental investigation of pressure, temperature, and salinity effects on the interfacial tension of H2/brine/cushion gases: Implications for H2 geo-storage*. Petroleum Research 11(2), 545-555 (2026).  
**Secondary compilation:** Jiao et al. (2026), SI workbook `ef6c01887_si_002.xlsx`, reference [9], observations 424-450.  
**Scope:** publisher metadata, experimental design, workbook subset, feature mapping, condition-basis audit. This is not a row-level numerical certification.

## 1. Publisher-verified experimental design

The publisher's journal article page states that the study measures IFT and density for H2-N2, H2-CO2 and H2-CH4 mixtures at 70:30 mol%, in distilled water and 30,000 ppm NaCl brine, at 25, 50 and 70 °C and 1, 5 and 10 MPa. The IFT instrument is described as a high-pressure/high-temperature drop tensiometer; density is measured using an Anton Paar DMA 4500.

The stated design corresponds to 3 gas mixtures × 2 aqueous phases × 3 temperatures × 3 pressures = 54 nominal IFT conditions if the full matrix was completed.

Publisher article page: https://castjournals.cast.org.cn/joweb/pr/EN/1289282122712195729  
DOI: https://doi.org/10.1016/j.ptlrs.2025.11.004

## 2. Workbook rows and subset coverage

The Jiao workbook contains 27 Daraii observations, not 54. Direct inspection of rows 424-450 gives:

| Jiao observations | Gas system | Aqueous phase | Rows |
|---|---|---|---:|
| 424-432 | H2-CH4 (70:30) | Distilled water | 9 |
| 433-441 | H2-CH4 (70:30) | NaCl brine | 9 |
| 442-450 | H2-CO2 (70:30) | NaCl brine | 9 |

Absent from the workbook subset: H2-N2 in both aqueous phases, and H2-CO2 in distilled water. Thus the Jiao workbook is a partial subset of the publisher-described experimental programme. It must not be described as the complete Daraii dataset.

## 3. Feature and condition audit

### Gas composition
The workbook uses CH4=0.3 and CO2=0 for H2-CH4 rows, and CH4=0 and CO2=0.3 for H2-CO2 rows. This is consistent with the article's 70:30 mol% gas-mixture description. Store cushion-gas identity explicitly and preserve H2 as the balance.

### Temperature
The workbook temperatures are 293, 323 and 343 K. These are approximately 20, 50 and 70 °C. The publisher abstract specifies 25, 50 and 70 °C. The 293 K versus 25 °C discrepancy is unresolved. Do not replace 293 K with 298.15 K or silently assert equivalence. Exact source table coordinates are needed to determine whether the workbook temperature or publisher abstract/design statement is in error.

### Salinity
The publisher reports 30,000 ppm NaCl. The Jiao workbook records 0.514 mol/kg NaCl for brine records. This is not the original source basis and no conversion convention/density basis is documented in the accessible article text. Preserve 30,000 ppm as reported; mark 0.514 mol/kg as a derived secondary value pending author/source confirmation.

### Measurement method
The publisher identifies a high-pressure/high-temperature drop tensiometer. This does not independently establish pendant versus sessile drop configuration. Jiao codes all 27 records as Method=1 (Sessile Drop), but that label remains unverified. Do not promote it to canonical method metadata without the full methods text or author confirmation.

## 4. Numerical values and uncertainty: unresolved

The publisher abstract reports selected H2-CH4 IFT values:
- 69.4 mN/m in distilled water at 25 °C and 1 MPa;
- 61.3 mN/m in 30,000 ppm brine at 25 °C and 1 MPa;
- 57.3 and 47.8 mN/m at 70 °C for distilled water and brine, respectively (the abstract does not make the pressure context of these latter endpoints explicit).

The accessible publisher page's full-text section does not expose the numerical tables. Therefore these abstract values are not sufficient for a complete row-by-row match. In particular, the workbook's 293 K rows cannot be directly equated with 25 °C source conditions. No claim is made that any of the 27 workbook IFT values have been numerically verified against primary tables. Source table/figure coordinates and uncertainty values are not yet available.

**Decision:** all 27 Jiao Daraii records remain excluded from primary benchmark eligibility until the full article tables/PDF or author-supplied data are obtained and each row is reconciled.

## 5. Publication chronology metadata

The publisher article page identifies the issue as *Petroleum Research* 2026, volume 11, issue 2, pages 545-555, with a page-level published date of 2026-06-10. The same page's article information separately displays an online date of 2026-07-29. The DOI contains a 2025 registration string and the Jiao bibliography labels the reference 2025. Preserve these distinct metadata fields; do not infer that the work appeared in a 2025 journal issue.

## 6. Reproducibility and next actions

1. Obtain the full publisher PDF and any supplementary tables, or request numerical data from the corresponding author.
2. Map each workbook observation to exact primary table/figure/page and source row.
3. Resolve 293 K versus 25 °C and the source pressure context for reported 70 °C endpoints.
4. Verify the IFT drop configuration and the meaning of the Jiao method code.
5. Recover original salinity preparation basis and document any conversion to molality.
6. Capture source uncertainty and its statistical definition.
7. Check whether any source validation points are reused from other publications.
8. Keep original Jiao workbook unchanged; apply any corrections only in a traceable canonical derivative.
9. Complete cross-study duplicate/overlap review before benchmark release.

**Current classification:** structural subset verified; gas-system mapping consistent with publisher description; numerical provenance incomplete; method unresolved; primary benchmark eligibility false.
