# Data preparation

`prepare_data.py` downloads the original UCI Steel Plates Faults data and creates the files used by the competition:

- `../data/train.csv`: features, `id`, and the `fault_type` target
- `../data/test.csv`: features and `id`, with the target removed
- `../data/sample_submission.csv`: the required submission-file shape
- `../data/solution.csv`: Kaggle answer key with `id`, `fault_type`, and a
  stratified 50/50 `Usage` split between public and private leaderboard rows

Run it from the repository root with:

```sh
uv run projects/proj02/data-prep/prepare_data.py
```

To create sandbox submissions, run:

```sh
uv run projects/proj02/data-prep/generate_sandbox_submissions.py
```

This writes Kaggle-format CSVs to `sandbox-submissions/` for a 1-nearest-
neighbor classifier, default random forest, tuned random forest, and logistic
regression. The 1-nearest-neighbor classifier uses `n_neighbors=1`; the default
random forest and logistic regression use scikit-learn's default parameters.
The tuned random forest uses 400 trees, all features at each split, and a
minimum leaf size of two; it was selected with an 80/20 stratified validation
split of `train.csv`.

The script uses a stratified 75/25 split and a fixed random seed, so rerunning it produces the same files. The source data encodes the seven target categories as seven indicator columns. The script converts them to one `fault_type` column and removes every indicator column before writing the features, preventing target leakage. It also verifies and removes the three redundant, base-10 log features; students can derive them during feature engineering if they choose.

Source: [UCI Steel Plates Faults dataset](https://archive.ics.uci.edu/dataset/198/steel+plates+faults).
