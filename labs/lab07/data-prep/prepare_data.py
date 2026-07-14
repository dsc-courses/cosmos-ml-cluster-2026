"""Download and clean the data used in the occupancy-detection paper."""

from pathlib import Path

import pandas as pd


SOURCE_ROOT = (
    "https://raw.githubusercontent.com/LuisM78/"
    "Occupancy-detection-data/master"
)
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "src" / "data"

FILES = {
    "datatraining.txt": "occupancy_train.csv",
    "datatest.txt": "occupancy_test_closed.csv",
    "datatest2.txt": "occupancy_test_open.csv",
}


def main() -> None:
    """Create CSVs with an explicit ID column and otherwise unchanged data."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for source_name, output_name in FILES.items():
        data = pd.read_csv(f"{SOURCE_ROOT}/{source_name}")

        # The original files contain an unlabeled first field. pandas reads it
        # as the index; make it explicit so students see a conventional schema.
        data = data.reset_index(names="id")
        output_path = OUTPUT_DIR / output_name
        data.to_csv(output_path, index=False)
        print(f"Wrote {len(data):,} rows to {output_path}")


if __name__ == "__main__":
    main()
