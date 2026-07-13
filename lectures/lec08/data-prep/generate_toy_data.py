"""Generate the fixed two-moons classification dataset used in Lecture 8.

Run from the repository root with:

    uv run python lectures/lec08/data-prep/generate_toy_data.py
"""

from pathlib import Path

import pandas as pd
from sklearn.datasets import make_moons


OUTPUT = Path(__file__).parents[1] / "data" / "toy-moons.csv"


def main() -> None:
    features, labels = make_moons(
        n_samples=240,
        noise=0.22,
        random_state=8,
    )
    data = pd.DataFrame(
        {
            "horizontal_position": features[:, 0],
            "vertical_position": features[:, 1],
            "class": pd.Series(labels).map({0: "purple", 1: "gold"}),
        }
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False)
    print(f"Wrote {len(data)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
