"""Create the cleaned, balanced three-genre CSV for the k-NN lecture.

Run from the repository root after reviewing the candidate analysis:

    uv run python lectures/lec07/data-prep/build_teaching_subset.py
"""

from pathlib import Path

import pandas as pd


SOURCE = Path("/Users/sam/Downloads/spotify.csv")
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "spotify-three-genres.csv"
GENRES = ("classical", "hip-hop", "rock")
RANDOM_STATE = 42


def main() -> None:
    data = pd.read_csv(SOURCE)
    subset = data.loc[data["track_genre"].isin(GENRES)].copy()

    # Do not let duplicated songs—or songs with contradictory selected labels—
    # cross from training into the held-out test set.
    label_counts = subset.groupby("track_id")["track_genre"].nunique()
    conflicting_ids = label_counts[label_counts > 1].index
    subset = subset.loc[~subset["track_id"].isin(conflicting_ids)].drop_duplicates("track_id")

    n_per_genre = subset["track_genre"].value_counts().min()
    subset = (
        subset.groupby("track_genre", group_keys=False)
        .sample(n=n_per_genre, random_state=RANDOM_STATE)
        # Keep this ordering aligned with analyze_candidates.clean_subset so
        # the fixed train/test split in the notebook reproduces its results.
        .sort_values("track_genre")
    )

    keep = [
        "track_id",
        "artists",
        "track_name",
        "danceability",
        "energy",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "track_genre",
    ]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subset[keep].to_csv(OUTPUT, index=False)
    print(f"Wrote {len(subset):,} songs ({n_per_genre:,} per genre) to {OUTPUT}")


if __name__ == "__main__":
    main()
