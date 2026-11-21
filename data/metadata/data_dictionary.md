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

See `data/metadata/source_register.csv`. Bibliographic metadata and broad experimental ranges have been confirmed from publisher/institutional records. Individual repository values have not yet been verified against source tables or supplementary data.
