"""Compare Spotify genre subsets and feature pairs for the k-NN lecture.

Run from the repository root:

    uv run python lectures/lec07/data-prep/analyze_candidates.py

The script reads /Users/sam/Downloads/spotify.csv and writes CSV summaries and
PNG figures next to this file.  It evaluates k=5 using one fixed, stratified
80/20 train/test split for every candidate subset.  All evaluated features are
already bounded between 0 and 1, so their distances can be compared directly
without introducing feature scaling in the first ML lecture.
"""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


SOURCE = Path("/Users/sam/Downloads/spotify.csv")
HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"

# These features are intelligible to students and lie in [0, 1].  In
# particular, omitting tempo and loudness means the first distance calculation
# does not require a detour into feature scaling.
FEATURES = [
    "danceability",
    "energy",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
]

# The groups include familiar genre names and a range from easy-to-separate to
# substantially overlapping.  The comparisons are deliberately curated rather
# than treating every Spotify metadata label as equally meaningful for class.
CANDIDATE_GENRES = [
    ("classical", "hip-hop", "metal"),
    ("classical", "hip-hop", "rock"),
    ("classical", "hip-hop", "pop"),
    ("classical", "disco", "metal"),
    ("classical", "country", "hip-hop"),
    ("classical", "country", "rock"),
    ("acoustic", "hip-hop", "metal"),
    ("acoustic", "hip-hop", "rock"),
    ("acoustic", "pop", "rock"),
    ("acoustic", "disco", "metal"),
    ("country", "hip-hop", "metal"),
    ("country", "pop", "rock"),
    ("jazz", "hip-hop", "metal"),
    ("jazz", "pop", "rock"),
]

# The recommendation favors familiar labels, intuitive features, visible
# overlap, and enough error cases to motivate k-NN over 1-NN.
RECOMMENDED_GENRES = ("classical", "hip-hop", "rock")
RECOMMENDED_FEATURES = ("speechiness", "acousticness")
RANDOM_STATE = 42


def clean_subset(data: pd.DataFrame, genres: tuple[str, str, str]) -> pd.DataFrame:
    """Return a balanced subset with no duplicate or conflicting track IDs.

    The source has some repeated track IDs.  A repeated ID could otherwise
    appear in both train and test data, or even have different genre labels.
    Removing it keeps the demo's held-out evaluation honest.
    """
    subset = data.loc[data["track_genre"].isin(genres)].copy()
    genre_counts = subset.groupby("track_id")["track_genre"].nunique()
    conflicting_ids = genre_counts[genre_counts > 1].index
    subset = subset.loc[~subset["track_id"].isin(conflicting_ids)]
    subset = subset.drop_duplicates("track_id")

    n_per_genre = subset["track_genre"].value_counts().min()
    return (
        subset.groupby("track_genre", group_keys=False)
        .sample(n=n_per_genre, random_state=RANDOM_STATE)
        .sort_values("track_genre")
        .reset_index(drop=True)
    )


def split_data(subset: pd.DataFrame):
    """Make the fixed, stratified split used throughout the comparison."""
    return train_test_split(
        subset[FEATURES],
        subset["track_genre"],
        test_size=0.2,
        stratify=subset["track_genre"],
        random_state=RANDOM_STATE,
    )


def score_feature_pairs(data: pd.DataFrame, genres: tuple[str, str, str]) -> pd.DataFrame:
    """Evaluate every two-feature k=5 classifier for one genre triple."""
    subset = clean_subset(data, genres)
    X_train, X_test, y_train, y_test = split_data(subset)
    rows = []
    for first, second in combinations(FEATURES, 2):
        pair = [first, second]
        model = KNeighborsClassifier(n_neighbors=5).fit(X_train[pair], y_train)
        rows.append(
            {
                "genres": " / ".join(genres),
                "feature_1": first,
                "feature_2": second,
                "feature_pair": " + ".join(pair),
                "test_accuracy_k5": accuracy_score(y_test, model.predict(X_test[pair])),
                "songs_per_genre": len(subset) // len(genres),
            }
        )
    return pd.DataFrame(rows).sort_values("test_accuracy_k5", ascending=False)


def plot_score_heatmap(scores: pd.DataFrame) -> None:
    """Plot every candidate triple against every evaluated feature pair."""
    ordered_pairs = [" + ".join(pair) for pair in combinations(FEATURES, 2)]
    table = scores.pivot(index="genres", columns="feature_pair", values="test_accuracy_k5")
    table = table.reindex(columns=ordered_pairs)
    table = table.loc[table.max(axis=1).sort_values(ascending=False).index]

    fig, ax = plt.subplots(figsize=(18, 8))
    sns.heatmap(table, cmap="viridis", vmin=0.33, vmax=1, annot=True, fmt=".2f", ax=ax)
    ax.set_title("Held-out accuracy of k=5 for candidate genre triples and feature pairs")
    ax.set_xlabel("Two audio features")
    ax.set_ylabel("Three genre labels")
    fig.tight_layout()
    fig.savefig(FIGURES / "candidate-feature-pair-accuracy.png", dpi=200)
    plt.close(fig)


def plot_best_candidate_scatters(data: pd.DataFrame, summary: pd.DataFrame) -> None:
    """Show the top six candidates using each candidate's best feature pair."""
    top = summary.head(6).reset_index(drop=True)
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), sharex=False, sharey=False)
    palette = {"classical": "#4C78A8", "hip-hop": "#F58518", "rock": "#54A24B", "metal": "#E45756",
               "pop": "#B279A2", "disco": "#FF9DA6", "country": "#9D755D", "acoustic": "#72B7B2",
               "jazz": "#ECA82C"}

    for ax, row in zip(axes.flat, top.to_dict("records"), strict=True):
        genres = tuple(row["genres"].split(" / "))
        subset = clean_subset(data, genres)
        for genre in genres:
            points = subset.loc[subset["track_genre"].eq(genre)]
            ax.scatter(
                points[row["feature_1"]],
                points[row["feature_2"]],
                s=13,
                alpha=0.45,
                label=genre,
                color=palette[genre],
                edgecolors="none",
            )
        ax.set_title(f"{row['genres']}\n{row['test_accuracy_k5']:.1%} test accuracy")
        ax.set_xlabel(row["feature_1"])
        ax.set_ylabel(row["feature_2"])
        ax.legend(fontsize=8, frameon=False)

    fig.suptitle("Best feature pair for the six strongest candidate genre triples", y=1.02)
    fig.tight_layout()
    fig.savefig(FIGURES / "top-candidate-scatters.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


def prediction_grid(model: KNeighborsClassifier, X: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return a grid of predictions for a two-feature decision-boundary plot."""
    x_name, y_name = X.columns
    x_pad = (X[x_name].max() - X[x_name].min()) * 0.06
    y_pad = (X[y_name].max() - X[y_name].min()) * 0.06
    x_values = np.linspace(X[x_name].min() - x_pad, X[x_name].max() + x_pad, 250)
    y_values = np.linspace(X[y_name].min() - y_pad, X[y_name].max() + y_pad, 250)
    xx, yy = np.meshgrid(x_values, y_values)
    grid = pd.DataFrame({x_name: xx.ravel(), y_name: yy.ravel()})
    labels = model.predict(grid).reshape(xx.shape)
    return xx, yy, labels


def plot_recommendation(data: pd.DataFrame) -> None:
    """Plot the recommended subset and its 1-NN versus 5-NN boundaries."""
    subset = clean_subset(data, RECOMMENDED_GENRES)
    X_train, X_test, y_train, y_test = split_data(subset)
    pair = list(RECOMMENDED_FEATURES)
    X_train_pair = X_train[pair]
    X_test_pair = X_test[pair]
    colors = {"classical": "#4C78A8", "hip-hop": "#F58518", "rock": "#54A24B"}
    label_codes = {genre: index for index, genre in enumerate(RECOMMENDED_GENRES)}
    background = plt.matplotlib.colors.ListedColormap(["#D7E4F3", "#FDE2C7", "#DDF0DD"])

    rows = []
    for k in (1, 5):
        model = KNeighborsClassifier(n_neighbors=k).fit(X_train_pair, y_train)
        predictions = model.predict(X_test_pair)
        rows.append({"k": k, "test_accuracy": accuracy_score(y_test, predictions)})

    pd.DataFrame(rows).to_csv(HERE / "recommended-knn-comparison.csv", index=False)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharex=True, sharey=True)
    for ax, k in zip(axes, (1, 5), strict=True):
        model = KNeighborsClassifier(n_neighbors=k).fit(X_train_pair, y_train)
        xx, yy, predicted_labels = prediction_grid(model, X_train_pair)
        predicted_codes = np.vectorize(label_codes.get)(predicted_labels)
        ax.contourf(xx, yy, predicted_codes, levels=[-0.5, 0.5, 1.5, 2.5], cmap=background, alpha=0.8)

        for genre in RECOMMENDED_GENRES:
            mask = y_train.eq(genre)
            ax.scatter(
                X_train_pair.loc[mask, pair[0]],
                X_train_pair.loc[mask, pair[1]],
                s=15,
                alpha=0.65,
                color=colors[genre],
                label=genre,
                edgecolors="none",
            )
        accuracy = next(row["test_accuracy"] for row in rows if row["k"] == k)
        ax.set_title(f"{k}-NN decision boundary\nHeld-out accuracy: {accuracy:.1%}")
        ax.set_xlabel(pair[0])
        ax.set_ylabel(pair[1])
        ax.legend(frameon=False)

    fig.suptitle("Recommended classroom subset: classical, hip-hop, and rock", y=1.02)
    fig.tight_layout()
    fig.savefig(FIGURES / "recommended-1nn-vs-5nn-boundaries.png", dpi=200, bbox_inches="tight")
    plt.close(fig)

    model = KNeighborsClassifier(n_neighbors=5).fit(X_train_pair, y_train)
    fig, ax = plt.subplots(figsize=(6, 5))
    ConfusionMatrixDisplay.from_predictions(y_test, model.predict(X_test_pair), ax=ax, cmap="Blues", colorbar=False)
    ax.set_title("5-NN test-set predictions for the recommended subset")
    fig.tight_layout()
    fig.savefig(FIGURES / "recommended-5nn-confusion-matrix.png", dpi=200)
    plt.close(fig)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(SOURCE)

    all_scores = pd.concat(
        [score_feature_pairs(data, genres) for genres in CANDIDATE_GENRES], ignore_index=True
    )
    all_scores.to_csv(HERE / "candidate-feature-pair-scores.csv", index=False)

    summary = (
        all_scores.sort_values("test_accuracy_k5", ascending=False)
        .groupby("genres", as_index=False)
        .first()
        .sort_values("test_accuracy_k5", ascending=False)
    )
    summary.to_csv(HERE / "candidate-summary.csv", index=False)

    plot_score_heatmap(all_scores)
    plot_best_candidate_scatters(data, summary)
    plot_recommendation(data)

    recommended = summary.loc[summary["genres"].eq(" / ".join(RECOMMENDED_GENRES))].iloc[0]
    print("Recommended genres:", recommended["genres"])
    recommended_pair = " + ".join(RECOMMENDED_FEATURES)
    recommended_score = all_scores.loc[
        all_scores["genres"].eq(" / ".join(RECOMMENDED_GENRES))
        & all_scores["feature_pair"].eq(recommended_pair)
    ].iloc[0]
    print("Recommended features:", recommended_pair)
    print(f"5-NN held-out accuracy: {recommended_score['test_accuracy_k5']:.1%}")
    print(f"Wrote analysis outputs to {HERE}")


if __name__ == "__main__":
    main()
