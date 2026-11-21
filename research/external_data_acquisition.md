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
