# arXiv Submission Metadata — Hydrogen Storage Site Selection Paper

## 1. Basic Information

| Field | Value |
|-|-|
| **Title** | A Decision-Support Framework for Subsurface Green Hydrogen Storage Site Selection: A Physics-Informed Multi-Objective Optimization Approach |
| **Authors** | Kudakwashe Douglas Marara |
| **Affiliation** | University of Zimbabwe (BSc Hons Petroleum Chemistry, 2025) |
| **Email** | kudakwashe.d.marara@gmail.com |
| **DOI** | (leave blank — arXiv assigns after submission) |
| **arXiv ID** | (assigned after submission) |

## 2. Abstract (copy-paste ready)

The global energy transition requires large-scale, long-term hydrogen storage. Subsurface geological formations - depleted oil and gas fields and saline aquifers - offer the safest and most economical option. However, identifying optimal storage locations requires balancing competing factors: renewable energy potential, water availability, geological suitability, socio-economic constraints, and physics-based storage safety. No open-source decision-support framework currently integrates multi-objective geospatial optimization with physics-informed neural networks (PINNs) for hydrogen-brine interfacial tension (IFT) prediction. This paper presents a two-layer decision-support framework for subsurface green hydrogen storage site selection. The strategic screening layer performs regional suitability analysis using geospatial multi-objective optimization with weight sensitivity analysis and robustness mapping. The tactical planning layer integrates a PINN predicting H$_2$-brine IFT under reservoir conditions (pressure, temperature, salinity) with Peng-Robinson equation-of-state (PR-EOS) physics constraints, producing a spatially-varying safety penalty layer. Applied to a Southern Africa case study ($12^\circ$E--$22^\circ$E, $10^\circ$S--$20^\circ$S; Namibia, Botswana, western South Africa), the framework identifies 4.4\% of pixels as GO zones and 15.5\% as conditional GO, with candidate regions in the Etosha and Kalahari basins passing integrated go/no-go thresholds. The framework is open-source and transferable to other regions and energy-storage applications.

**Keywords:** hydrogen storage, site selection, multi-objective optimization, physics-informed neural networks, interfacial tension, geospatial decision support, Peng-Robinson equation of state

## 3. Subjects (arXiv Classification)

**Primary:** `physics.geo-ph` (Physics > Geophysics)

**Alternatives to consider:**
- `cs.GE` (Computer Science > Geoscience) — if emphasizing the computational/PINN aspect
- `stat.ML` (Statistics > Machine Learning) — if emphasizing the PINN methodology
- `eess.SP` (Electrical Engineering > Signal Processing) — less ideal

**Recommendation:** Primary `physics.geo-ph`. You can add a secondary subject during submission if needed.

## 4. Files to Upload

| File | Path | Required |
|--|--|--|
| Main LaTeX source | `paper/paper.tex` | Yes |
| Bibliography | `paper/references.bib` | Yes |
| Figure 1 (decision map) | `paper/figures/week11_full_integration.png` | Yes |
| Figure 2 (training history) | `paper/figures/pinn_training_v3.png` | Yes |

**Note:** arXiv compiles LaTeX server-side. Upload `.tex` + `.bib` + figures. Do NOT upload a pre-compiled PDF unless you want to bypass their compilation.

## 5. Submission Steps

1. Go to https://arxiv.org/submit
2. Log in (create account if needed)
3. Click "New Submission"
4. **Step 1 — Subjects:** Select `physics.geo-ph`
5. **Step 2 — Abstract:** Paste the abstract above
6. **Step 3 — Authors:** Add Kudakwashe Douglas Marara, affiliation University of Zimbabwe
7. **Step 4 — Files:** Upload all 4 files listed above
8. **Step 5 — Review:** Check metadata, click submit
9. **Step 6 — Confirmation:** You'll receive a submission ID and arXiv link after processing (typically 24-48 hours)

## 6. Post-Submission

- arXiv will email you when the paper is live (usually within 1-2 business days)
- Note your arXiv ID (e.g., arXiv:26XX.XXXXX)
- Use this ID in your journal cover letter as a preprint reference
- You can submit a revised version later if reviewers request changes

## 7. ORCID (Optional but Recommended)

Get an ORCID iD at https://orcid.org — many journals require it, and it links your preprint to your publications automatically.
