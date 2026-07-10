"""Generate baseline Kaggle submissions for the steel plate faults competition."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
OUTPUT_DIR = Path(__file__).resolve().parent / "sandbox-submissions"
# Selected using an 80/20 stratified validation split of train.csv.
TUNED_RANDOM_FOREST_PARAMETERS = {
    "n_estimators": 400,
    "max_features": None,
    "min_samples_leaf": 2,
    "random_state": 42,
}
MODELS = {
    "1nn": KNeighborsClassifier(n_neighbors=1),
    "random_forest": RandomForestClassifier(),
    "tuned_random_forest": RandomForestClassifier(**TUNED_RANDOM_FOREST_PARAMETERS),
    "logistic_regression": LogisticRegression(),
}


def generate_submissions() -> None:
    """Train baseline models and write one Kaggle-format CSV for each."""
    train = pd.read_csv(DATA_DIR / "train.csv")
    test = pd.read_csv(DATA_DIR / "test.csv")

    feature_columns = [column for column in test.columns if column != "id"]
    X_train = train[feature_columns]
    y_train = train["fault_type"]
    X_test = test[feature_columns]

    OUTPUT_DIR.mkdir(exist_ok=True)
    for name, model in MODELS.items():
        predictions = model.fit(X_train, y_train).predict(X_test)
        submission = pd.DataFrame({"id": test["id"], "fault_type": predictions})
        output_path = OUTPUT_DIR / f"{name}_submission.csv"
        submission.to_csv(output_path, index=False)
        print(f"Wrote {len(submission):,} rows to {output_path}")


if __name__ == "__main__":
    generate_submissions()
