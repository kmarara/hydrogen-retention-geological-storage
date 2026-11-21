# External data acquisition and ingestion

## Target source

Jiao et al. (2026), "Tabular Deep Learning for Hydrogen–Brine Interfacial Tension Prediction with Uncertainty Quantification", *Energy & Fuels* 40(30), 16671–16691.

- DOI: https://doi.org/10.1021/acs.energyfuels.6c01887
- Article / supporting-information landing page: https://pubs.acs.org/doi/10.1021/acs.energyfuels.6c01887
- Supporting information includes the complete curated 450-measurement XLSX, a PDF, model implementation details, and empirical correlations (per publisher record).

## Download

Download the XLSX from the article's **Supporting Information** section and place the original file at:

`data/external/jiao_2026/supplementary_dataset.xlsx`

Do not rename worksheet columns or edit the original workbook. Keep the publisher file unchanged and record its SHA-256 checksum.

## Ingest and inspect

Install dependencies:

```bash
python -m pip install pandas openpyxl
```

Run:

```bash
python scripts/ingest_jiao_2026_supplement.py data/external/jiao_2026/supplementary_dataset.xlsx
```

The script writes one CSV per worksheet plus an ingestion manifest under `data/processed/jiao_2026_audit/`. It preserves original columns and adds source sheet and Excel row identifiers. It does not claim that the rows are independent or independently measured.

## Scientific controls before merging

1. Inspect every worksheet, header, unit and footnote.
2. Identify the original publication and experimental campaign for every row.
3. Separate pure H2–water, H2–NaCl, mixed-electrolyte and cushion-gas systems.
4. Check duplicate records and overlap with Hosseini (2022), Hosseini & Leonenko (2024), Ai & Trusler (2026), and our existing 91-row CSV.
5. Record whether each value is directly measured, table-extracted, digitised, calculated or otherwise derived.
6. Preserve the source's original units and values; put conversions in separate fields.
7. Only then create a versioned harmonised benchmark table.

## API strategy

Crossref and OpenAlex can automate bibliographic discovery and DOI metadata. They do not provide a universal API for experimental IFT tables. Publisher supplementary files and repositories (including ACS Figshare) are the primary route for structured measurements. When a supplementary file is not openly retrievable, request it from the authors or extract published tables/figures with explicit provenance and uncertainty.

## Current status

The publisher record confirms that the 450-measurement XLSX exists. The workbook itself has **not yet been downloaded or inspected in this repository**. Do not describe its columns or contents beyond what the article record states until the original file is obtained.

## Automated DOI metadata discovery

Use the metadata script to retrieve bibliographic records from Crossref and OpenAlex:

```bash
python scripts/discover_publication_metadata.py \
  10.1016/j.petrol.2022.110441 \
  10.1016/j.ijhydene.2026.154442 \
  10.1021/acs.energyfuels.6c01887 \
  --out data/metadata/publication_metadata.json
```

Optionally provide `--mailto you@example.org` for Crossref's polite pool. The script stores article metadata and OA-location metadata only. It does not retrieve IFT observations, guarantee supplementary-file access, or establish permission to reuse a dataset. Crossref and OpenAlex are discovery services, not experimental-data APIs.

API documentation:
- Crossref REST API: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- OpenAlex API: https://help.openalex.org/api/
- Figshare API v2 (for repository-hosted files where applicable): https://docs.figshare.com/v2/



## Supporting-information PDF obtained (2026-11-21)

The nine-page ACS Supporting Information PDF was uploaded and inspected. It contains:
- TabM hyperparameter search spaces and three scenario-specific configurations (pure water, brine, combined system; PDF p. 1).
- Illustrative TabM/PyTorch/PLE workflow and ensemble-aware loss snippets (pp. 2–3).
- Illustrative TabPFN regression workflow with 2.5%, 50%, and 97.5% quantiles, internal shuffled five-fold validation, external prediction, permutation-SHAP and PDP snippets (pp. 3–5).
- Chow et al. (2018) H2O-H2 correlation and erratum-corrected coefficients, plus Hosseini et al. (2022) H2-brine correlation and coefficients (pp. 6–8).

The PDF is **methods and correlation supplementary information, not the 450-row measurement workbook**. It does not expose the full data table, full executable scripts, complete preprocessing or training loops. The XLSX is still required.

The Hosseini correlation printed in the PDF is:
`gamma = A*m + B`, `A = a0 + a1*p + a2*T`, `B = b11 + b21*p + b12*T + b22*p*T`.
Parameters: a0=-0.47876, a1=-0.01004, a2=0.00593, b11=135.41479, b21=-0.38368, b12=-0.20520, b22=0.00084. Units in the PDF: gamma mN/m, m mol/kg, T K, p MPa. Treat correlation outputs as calculated baselines, never as experimental measurements.

The Chow equation's typesetting/exponent placement must be checked against the original paper and 2020 erratum before implementation; do not transcribe from OCR alone.

## Model implementation decision

A dedicated protocol is maintained in `research/pretrained_tabular_model_benchmark.md`. TabPFN is the pretrained foundation-model candidate. TabM is a parameter-efficient ensemble architecture trained on each training fold, not a pretrained foundation model. Include conventional boosted-tree and empirical-correlation baselines. Pin exact package/checkpoint versions and inspect model-weight licences separately from code licences before selecting TabPFN weights.

Current status: SI PDF inspected; XLSX not obtained; no model trained; no performance claims made.
