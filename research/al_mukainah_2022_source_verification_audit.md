# Al-Mukainah et al. (2022): primary-source verification audit

**Audit date:** 2026-11-21  
**Primary source:** Al-Mukainah H, Al-Yaseri A, Yekeen N, Al Hamad J, Mahmoud M (2022), *Energy Reports* 8, 8830–8843. DOI: [10.1016/j.egyr.2022.07.004](https://doi.org/10.1016/j.egyr.2022.07.004).  
**Jiao source group:** Reference [6], workbook observations 268–273 (six records).  
**Scope:** Method, concentration basis, pressure/temperature mapping, and value-level verification. This audit does not certify the six IFT values.

## Primary-source evidence

The full article PDF was inspected from the author-uploaded full-text record. Relevant source coordinates:

- **Abstract, article PDF p. 1 / journal p. 8830:** explicitly says modified sessile-drop was used for contact-angle measurement, while H2–brine IFT was measured by pendant drop.
- **Section 2.2, article PDF p. 5 / journal p. 8834:** describes the modified sessile-drop contact-angle procedure and separately states that H2/brine IFT was measured by the pendant-drop technique with Young–Laplace fitting.
- **Section 3.2, article PDF p. 6 / journal p. 8835:** reports H2/brine IFT at 50 °C, pressures 14.7–1000 psi, and gives endpoint values of 63.68 mN/m at 14.7 psi and 51.29 mN/m at 1000 psi.
- **Figure 4, article PDF p. 6 / journal p. 8835:** plots six IFT observations against pressure; its caption reports ±1 mN/m uncertainty. The four intermediate values are plotted, not tabulated in the inspected article text.

## Workbook-to-source comparison

| Workbook observation | P (MPa) | T (K) | Workbook NaCl (mol/kg) | Workbook IFT (mN/m) | Primary-source comparison |
|---:|---:|---:|---:|---:|---|
| 268 | 0.101 | 323 | 1.91 | 64.46 | Pressure maps to 14.7 psi; source text gives 63.68 |
| 269 | 1.38 | 323 | 1.91 | 61.04 | Pressure maps to approximately 200 psi; source Fig. 4 is graphical |
| 270 | 2.76 | 323 | 1.91 | 60.73 | Pressure maps to approximately 400 psi; source Fig. 4 is graphical |
| 271 | 4.14 | 323 | 1.91 | 57.93 | Pressure maps to approximately 600 psi; source Fig. 4 is graphical |
| 272 | 5.52 | 323 | 1.91 | 53.81 | Pressure maps to approximately 800 psi; source Fig. 4 is graphical |
| 273 | 6.89 | 323 | 1.91 | 52.02 | Pressure maps to approximately 1000 psi; source text gives 51.29 |

The pressure sequence maps to the six experimental pressure positions in Figure 4 after unit conversion. The workbook's 323 K is a rounded representation of 50 °C (323.15 K).

**Critical discrepancy:** the workbook's first and last IFT values do not match the article's explicitly stated endpoint values. The article gives 63.68 and 51.29 mN/m; the workbook gives 64.46 and 52.02 mN/m. The workbook values are higher by 0.78 and 0.73 mN/m respectively. Since the intermediate source values are only available graphically in the inspected article, no claim of exact point-level matching is made. The graph's stated ±1 mN/m uncertainty does not justify silently replacing or accepting discrepant values; provenance and numerical identity must still be established.

## Confirmed metadata correction

The Jiao workbook legend maps method code 0 to Pendant Drop and code 1 to Sessile Drop. All six records in observations 268–273 are coded 1. This is inconsistent with the primary paper's explicit method description. For these IFT observations, the correct method is **Pendant Drop**. The sessile-drop procedure belongs to contact-angle measurements, not the IFT measurements.

The primary paper reports **10 wt% NaCl**, not molality. The workbook's 1.91 mol/kg is approximately consistent with converting a 10 wt% solution:
- 10 g NaCl / 58.44 g mol−1 = 0.1711 mol
- 90 g water = 0.090 kg solvent
- molality = 0.1711 / 0.090 = approximately 1.90 mol/kg

This conversion assumes 10 wt% means 10 g NaCl per 100 g final solution. Retain 10 wt% as the original reported basis; store 1.90–1.91 mol/kg only as a derived value with the convention and rounding recorded. Do not relabel the source's original concentration as molality.

## Benchmark decision

- **Method:** verified; correct IFT method metadata to Pendant Drop in a corrected derivative, retaining raw workbook unchanged.
- **Original concentration:** verified as 10 wt% NaCl.
- **Molality:** plausible derived conversion, not source-reported.
- **Pressure/temperature mapping:** consistent with the six pressure positions and 50 °C after rounding.
- **IFT values:** not verified; endpoint discrepancy is material.
- **Eligibility:** all six workbook records remain excluded from primary benchmark eligibility pending author-provided numerical data or a defensible exact point-level source match.
- **Provenance:** treat the workbook as a secondary compilation. Do not mark these six as source-verified experimental rows merely because the study citation and broad trend match.

## Reproducibility and next action

Keep the original Jiao workbook and its checksum unchanged. Any eventual correction must be represented in a separate canonical observation layer with:
1. original source value and units;
2. workbook value and units;
3. explicit source coordinates (Fig. 4 and, if obtained, author data file);
4. correction/conversion note;
5. reviewer decision and duplicate lineage.

The next decisive step is to obtain the authors' underlying numerical data or supplementary table for Figure 4. Until then, do not train on these six rows.
