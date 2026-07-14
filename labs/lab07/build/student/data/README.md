---
nav_exclude: true
---

# Occupancy Detection data

These files are cleaned copies of the data accompanying:

> Luis M. Candanedo and Véronique Feldheim, “Accurate occupancy detection of
> an office room from light, temperature, humidity and CO2 measurements using
> statistical learning models,” *Energy and Buildings* 112 (2016), 28–39.
> <https://doi.org/10.1016/j.enbuild.2015.11.071>

Original data and analysis code:
<https://github.com/LuisM78/Occupancy-detection-data>

UCI dataset record and DOI:
<https://doi.org/10.24432/C5X01N>

The UCI record licenses the dataset under CC BY 4.0. The only schema change in
these copies is that the unlabeled first field in each original file is named
`id`. No measurements, timestamps, targets, rows, or dataset partitions were
changed.

| File | Original file | Rows | Purpose |
| --- | --- | ---: | --- |
| `occupancy_train.csv` | `datatraining.txt` | 8,143 | Training and cross-validation |
| `occupancy_test_closed.csv` | `datatest.txt` | 2,665 | External test period; door mostly closed during occupancy |
| `occupancy_test_open.csv` | `datatest2.txt` | 9,752 | External test period; door mostly open during occupancy |

`feature_recipes.csv` is course-authored experiment configuration, not part of
the original dataset. Its `sensor_columns` values use JSON list syntax so they
can be parsed unambiguously after loading the CSV.
