# Benchmark data dictionary and provenance policy

## Current raw file

Source: `data/raw/ift_experimental.csv`

The raw file currently has six columns:
- `P_MPa`: pressure, MPa.
- `T_K`: temperature, K.
- `Salinity_ppm`: a value described in comments as ppm / NaCl-equivalent; this is not a sufficiently precise concentration definition for scientific use.
- `IFT_mN_m`: interfacial tension, mN/m.
- `Source`: source key.
- `Salinity_type`: broad fluid label.

The file contains 91 numeric rows: 64 attributed to Hosseini et al. (2022) and 27 attributed to Ai & Trusler (2026). This inventory is not equivalent to row-level verification.

## Required new fields for a verified benchmark

Every observation in a future processed dataset should have:
- `observation_id`: stable unique identifier.
- `source_id`: foreign key to `source_register.csv`.
- `source_location`: exact table, figure, page, supplementary file and/or row.
- `source_value`: value as reported, before conversion.
- `source_unit`: original unit.
- `P_MPa`, `T_K`, `IFT_mN_m`: harmonised numerical values.
- `salinity_molality_mol_kg`: molality when reported.
- `salinity_mass_fraction` or `salinity_mg_kg_solution`: only when source supports this basis.
- `salt_composition`: explicit species and composition (e.g. NaCl, KCl, mixed electrolyte).
- `measurement_method`: pendant drop or other reported method.
- `measurement_uncertainty`: numeric value and basis, if reported.
- `data_status`: one of `direct_measurement`, `table_extracted`, `digitised`, `calculated`, `simulation`, `representative`, `unverified`.
- `transformation_notes`: all unit conversions and transformations.
- `verification_status`: `verified`, `partially_verified`, or `unverified`.

## Provenance rules

1. Never infer a measured value from a correlation and label it experimental.
2. Never replace original concentration basis with an approximate ppm conversion without preserving the original value and formula.
3. Keep pure water, NaCl brine, KCl brine, mixed NaCl-KCl brine and multicomponent formation brines distinguishable.
4. Do not merge experimental, digitised, calculated and simulation records without explicit status labels and separate evaluation.
5. Keep the raw source file unchanged. Generate processed data through a documented script.
6. Record exact source location for every accepted row.
7. If a source value cannot be traced, retain it only in a quarantined/unverified dataset, not the primary experimental benchmark.

## Current source-level status

See `data/metadata/source_register.csv` and `research/consolidated_provenance_matrix_2026-11-21.md`. A source-verified stage-1 tranche now contains 158 canonical candidate observations: 64 Hosseini primary-SI rows, 79 Chow primary-table rows, and 15 Mirchi primary-table rows. The combined CSV has 42 columns and SHA-256 `94fde4ebfcc76ab7a12437079467dcc0e24f2cc98a5966f6802238155a25d89a`.

This tranche is not yet the frozen benchmark. Global overlap/duplicate review and final release gates remain open. The 450-row Jiao workbook and legacy 91-row CSV are not approved as benchmark datasets.

## Non-destructive legacy CSV audit

Run:

```bash
python scripts/audit_ift_csv.py data/raw/ift_experimental.csv
```

The default report is written to `outputs/data_audit/legacy_ift_profile.json`. Override it with `--out path/to/report.json`. The script skips comment lines, checks required columns and numeric fields, profiles source/system counts and ranges, and flags exact duplicates and repeated IFT values at matching pressure/temperature across different salinities.

These are diagnostic flags only. The script does not establish whether a value is experimentally measured, correct, independent, or suitable for model training. In particular, repeated IFT values must be checked against the original supporting information rather than automatically deleted.

Run its unit tests with:

```bash
python -m unittest discover -s tests -v
```

