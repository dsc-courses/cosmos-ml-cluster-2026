"""Prepare train/test CSVs for the steel-plate fault Kaggle competition."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


DATA_URL = "https://archive.ics.uci.edu/static/public/198/steel+plates+faults.zip"
RANDOM_STATE = 42
TEST_SIZE = 0.25
PUBLIC_TEST_SIZE = 0.50
TARGET_COLUMNS = [
    "Pastry",
    "Z_Scratch",
    "K_Scatch",
    "Stains",
    "Dirtiness",
    "Bumps",
    "Other_Faults",
]
LOG_FEATURES = ["LogOfAreas", "Log_X_Index", "Log_Y_Index"]


def download_source_data() -> tuple[list[str], BytesIO]:
    """Download the UCI archive and return its variable names and data bytes."""
    with urlopen(DATA_URL) as response:
        archive = ZipFile(BytesIO(response.read()))
        columns = archive.read("Faults27x7_var").decode().splitlines()
        data = BytesIO(archive.read("Faults.NNA"))
    return columns, data


def verify_log_features(faults: pd.DataFrame) -> None:
    """Confirm that the source log columns are redundant derived features."""
    expected_features = {
        "LogOfAreas": np.log10(faults["Pixels_Areas"]),
        "Log_X_Index": np.log10(faults["X_Maximum"] - faults["X_Minimum"]),
        "Log_Y_Index": np.log10(faults["Y_Maximum"] - faults["Y_Minimum"]),
    }
    for column, expected in expected_features.items():
        if not np.allclose(faults[column], expected, rtol=0, atol=6e-5):
            raise ValueError(f"{column} is not the expected base-10 logarithm.")


def prepare_data() -> None:
    """Create reproducible train, test, and sample-submission CSV files."""
    columns, data = download_source_data()
    faults = pd.read_csv(data, sep=r"\s+", header=None, names=columns)

    if columns[-len(TARGET_COLUMNS) :] != TARGET_COLUMNS:
        raise ValueError("The target columns in the downloaded source have changed.")

    verify_log_features(faults)

    target_indicators = faults[TARGET_COLUMNS]
    if not (target_indicators.sum(axis="columns") == 1).all():
        raise ValueError("Each row must have exactly one fault type.")

    target = target_indicators.idxmax(axis="columns").rename("fault_type")
    features = faults.drop(columns=TARGET_COLUMNS + LOG_FEATURES)
    features.insert(0, "id", range(len(features)))

    train_features, test_features, train_target, test_target = train_test_split(
        features,
        target,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=target,
    )

    train = train_features.copy()
    train["fault_type"] = train_target
    test = test_features.copy()

    public_ids, _ = train_test_split(
        test["id"],
        test_size=1 - PUBLIC_TEST_SIZE,
        random_state=RANDOM_STATE + 1,
        stratify=test_target,
    )
    solution = pd.DataFrame(
        {
            "id": test["id"],
            "fault_type": test_target,
            "Usage": "Private",
        }
    )
    solution.loc[solution["id"].isin(public_ids), "Usage"] = "Public"

    data_dir = Path(__file__).resolve().parents[1] / "data"
    data_dir.mkdir(exist_ok=True)
    train.to_csv(data_dir / "train.csv", index=False)
    test.to_csv(data_dir / "test.csv", index=False)
    solution.to_csv(data_dir / "solution.csv", index=False)
    pd.DataFrame({"id": test["id"], "fault_type": "Other_Faults"}).to_csv(
        data_dir / "sample_submission.csv", index=False
    )

    print(f"Wrote {len(train):,} training rows to {data_dir / 'train.csv'}")
    print(f"Wrote {len(test):,} testing rows to {data_dir / 'test.csv'}")
    print(f"Wrote Kaggle solution rows to {data_dir / 'solution.csv'}")


if __name__ == "__main__":
    prepare_data()
