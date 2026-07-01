#!/usr/bin/env python3
"""
EMNIST Dataset Processor

This script loads EMNIST digit dataset from compressed IDX files and creates
balanced training and test datasets in CSV format for machine learning.

Usage:
    python emnist_processor.py --input-dir /path/to/emnist/files --output-dir ./emnist
"""

import argparse
import gzip
from pathlib import Path
from typing import Optional, Tuple

try:
    import matplotlib.pyplot as plt

    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

import numpy as np
import pandas as pd


def load_emnist_images(file_path: Path) -> np.ndarray:
    """
    Load EMNIST images from IDX format (same as MNIST format).

    Args:
        file_path: Path to the gzipped IDX file

    Returns:
        Array of images with shape (n_samples, height, width)
    """
    with gzip.open(file_path, "rb") as f:
        # Read the magic number (4 bytes)
        magic = int.from_bytes(f.read(4), byteorder="big")

        # Read number of images (4 bytes)
        n_images = int.from_bytes(f.read(4), byteorder="big")

        # Read number of rows (4 bytes)
        n_rows = int.from_bytes(f.read(4), byteorder="big")

        # Read number of columns (4 bytes)
        n_cols = int.from_bytes(f.read(4), byteorder="big")

        print(f"Magic number: {magic}")
        print(f"Number of images: {n_images}")
        print(f"Image dimensions: {n_rows} x {n_cols}")

        # Read the image data
        images = np.frombuffer(f.read(), dtype=np.uint8)

        # Reshape to (n_images, n_rows, n_cols)
        images = images.reshape(n_images, n_rows, n_cols)

        return images


def load_emnist_labels(file_path: Path) -> np.ndarray:
    """
    Load EMNIST labels from IDX1 format.

    Args:
        file_path: Path to the gzipped IDX1 file

    Returns:
        Array of labels with shape (n_samples,)
    """
    with gzip.open(file_path, "rb") as f:
        # Read the magic number (4 bytes)
        magic = int.from_bytes(f.read(4), byteorder="big")

        # Read number of labels (4 bytes)
        n_labels = int.from_bytes(f.read(4), byteorder="big")

        print(f"Magic number: {magic}")
        print(f"Number of labels: {n_labels}")

        # Read the label data
        labels = np.frombuffer(f.read(), dtype=np.uint8)

        return labels


def visualize_images(
    images: np.ndarray,
    labels: Optional[np.ndarray] = None,
    n_samples: int = 10,
    figsize: Tuple[int, int] = (15, 6),
) -> None:
    """
    Visualize a sample of images from the dataset.

    Args:
        images: Array of images
        labels: Array of corresponding labels
        n_samples: Number of images to display
        figsize: Figure size for the plot
    """
    if not HAS_MATPLOTLIB:
        print(
            "Error: matplotlib is required for visualization but not installed."
        )
        print("Install with: pip install matplotlib")
        return

    fig, axes = plt.subplots(2, 5, figsize=figsize)
    axes = axes.flatten()

    for i in range(min(n_samples, len(images))):
        axes[i].imshow(images[i].T, cmap="gray")
        if labels is not None:
            axes[i].set_title(f"Label: {labels[i]}")
        else:
            axes[i].set_title(f"Image {i}")
        axes[i].axis("off")

    plt.tight_layout()
    plt.show()


def create_balanced_sample(
    images: np.ndarray,
    labels: np.ndarray,
    samples_per_class: int = 6000,
    random_seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create a balanced random sample from the dataset.

    Args:
        images: Array of images
        labels: Array of labels
        samples_per_class: Number of samples per class
        random_seed: Random seed for reproducibility

    Returns:
        Tuple of (sampled_images, sampled_labels)
    """
    np.random.seed(random_seed)

    # Lists to store the sampled data
    sampled_images = []
    sampled_labels = []

    print(
        f"Creating balanced random sample with {samples_per_class} samples per class..."
    )

    for digit in range(10):
        # Find all indices where the label equals the current digit
        digit_indices = np.where(labels == digit)[0]

        print(f"Class {digit}: {len(digit_indices)} available samples")

        # Randomly sample indices from this class
        if len(digit_indices) >= samples_per_class:
            selected_indices = np.random.choice(
                digit_indices, samples_per_class, replace=False
            )
        else:
            # If we don't have enough samples, use all available and sample with replacement
            selected_indices = np.random.choice(
                digit_indices, samples_per_class, replace=True
            )
            print(
                f"Warning: Class {digit} has only {len(digit_indices)} samples, sampling with replacement"
            )

        # Extract the selected images and labels
        class_images = images[selected_indices]
        class_labels = labels[selected_indices]

        sampled_images.append(class_images)
        sampled_labels.append(class_labels)

    # Combine all classes
    final_images = np.concatenate(sampled_images, axis=0)
    final_labels = np.concatenate(sampled_labels, axis=0)

    print(f"Final dataset shape: {final_images.shape}")
    print(f"Final labels shape: {final_labels.shape}")

    # Verify class balance
    unique_labels, counts = np.unique(final_labels, return_counts=True)
    print("Class distribution:")
    for label, count in zip(unique_labels, counts):
        print(f"Class {label}: {count} samples")

    return final_images, final_labels


def process_and_save_dataset(
    images: np.ndarray,
    labels: np.ndarray,
    output_dir: Path,
    filename: str,
    include_labels: bool = True,
) -> Tuple[pd.DataFrame, np.ndarray]:
    """
    Process images and save as CSV dataset.

    Args:
        images: Array of images
        labels: Array of labels
        output_dir: Output directory path
        filename: Output filename
        include_labels: Whether to include labels in the dataset

    Returns:
        Tuple of (DataFrame containing the processed dataset, shuffled labels)
    """
    # Shuffle the data to mix the classes
    print("Shuffling the data...")
    shuffle_indices = np.random.permutation(len(images))
    images = images[shuffle_indices]
    labels = labels[shuffle_indices]

    # Flatten the images from 28x28 to 784 features
    print("Flattening images...")
    flattened_images = images.reshape(images.shape[0], -1)
    print(f"Flattened images shape: {flattened_images.shape}")

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created/verified directory: {output_dir}/")

    # Create a DataFrame
    print("Creating DataFrame...")
    # Create column names for the pixel features
    pixel_columns = [str(i) for i in range(784)]

    # Create the DataFrame with pixel data
    df = pd.DataFrame(flattened_images, columns=pixel_columns)

    if include_labels:
        df["label"] = labels
        print(f"DataFrame shape: {df.shape}")
        print(
            f"DataFrame columns: {len(df.columns)} total (784 pixel features + 1 label)"
        )
    else:
        print(f"DataFrame shape: {df.shape}")
        print(
            f"DataFrame columns: {len(df.columns)} (784 pixel features, NO labels)"
        )

    # Save to CSV
    csv_path = output_dir / filename
    print(f"Saving to {csv_path}...")
    df.to_csv(csv_path, index=False)

    print(f"Successfully saved {len(df)} samples to {csv_path}")

    if include_labels:
        # Display class distribution
        print("Final class distribution in saved file:")
        print(df["label"].value_counts().sort_index())

    return df, labels


def create_submission_files(
    test_labels: np.ndarray, output_dir: Path
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Create test_labels.csv and sample_submission.csv files.

    Args:
        test_labels: Array of true test labels
        output_dir: Output directory path

    Returns:
        Tuple of (test_labels_df, sample_submission_df)
    """
    print("Creating test_labels.csv...")

    # Calculate midpoint for Usage column
    n_samples = len(test_labels)
    midpoint = n_samples // 2

    # Create Usage column: first half "Public", second half "Private"
    usage_values = ["Public"] * midpoint + ["Private"] * (n_samples - midpoint)

    # Create the test labels DataFrame with true labels and Usage column
    test_labels_df = pd.DataFrame(
        {
            "id": range(len(test_labels)),
            "label": test_labels.astype(int),
            "Usage": usage_values,
        }
    )

    # Save the test labels file
    test_labels_path = output_dir / "test_labels.csv"
    test_labels_df.to_csv(test_labels_path, index=False)
    print(
        f"Successfully saved {len(test_labels_df)} entries to {test_labels_path}"
    )

    # Create sample_submission.csv with all labels as 0
    print("Creating sample_submission.csv with all labels as 0...")
    sample_submission_df = pd.DataFrame(
        {"id": range(len(test_labels)), "label": [0] * len(test_labels)}
    )

    # Save the sample submission file
    sample_submission_path = output_dir / "sample_submission.csv"
    sample_submission_df.to_csv(sample_submission_path, index=False)
    print(
        f"Successfully saved {len(sample_submission_df)} entries to {sample_submission_path}"
    )

    return test_labels_df, sample_submission_df


def print_summary(
    train_df: pd.DataFrame,
    test_df: pd.DataFrame,
    test_labels_df: pd.DataFrame,
    sample_submission_df: pd.DataFrame,
) -> None:
    """Print a summary of all created files."""
    print("=" * 60)
    print("DATASET CREATION SUMMARY")
    print("=" * 60)
    print()

    print("📁 FILES CREATED IN OUTPUT DIRECTORY:")
    print(f"   • train.csv: {len(train_df):,} samples with labels")
    print(f"   • test.csv:  {len(test_df):,} samples without labels")
    print(
        f"   • test_labels.csv: {len(test_labels_df):,} entries with true labels"
    )
    print(
        f"   • sample_submission.csv: {len(sample_submission_df):,} entries with label 0"
    )
    print()

    print("📊 TRAIN.CSV STRUCTURE:")
    print(f"   • Shape: {train_df.shape}")
    print(f"   • Features: {len(train_df.columns) - 1} pixel columns (0-783)")
    print("   • Labels: 1 label column (values 0-9)")
    if "label" in train_df.columns:
        print(
            f"   • Class balance: {train_df['label'].value_counts().min()}-{train_df['label'].value_counts().max()} samples per class"
        )
    print()

    print("📊 TEST.CSV STRUCTURE:")
    print(f"   • Shape: {test_df.shape}")
    print(f"   • Features: {len(test_df.columns)} pixel columns (0-783)")
    print("   • Labels: None (for prediction)")
    print("   • Balanced sampling: 1,000 samples per class (hidden)")
    print()

    print("✅ All datasets are ready for machine learning!")


def main() -> None:
    """Main function to process EMNIST dataset."""
    parser = argparse.ArgumentParser(
        description="Process EMNIST dataset and create balanced train/test CSV files"
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("/Users/sam/Downloads/gzip"),
        help="Directory containing EMNIST .gz files (default: /Users/sam/Downloads/gzip)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("emnist"),
        help="Output directory for processed CSV files (default: ./emnist)",
    )
    parser.add_argument(
        "--train-samples-per-class",
        type=int,
        default=6000,
        help="Number of training samples per class (default: 6000)",
    )
    parser.add_argument(
        "--test-samples-per-class",
        type=int,
        default=1000,
        help="Number of test samples per class (default: 1000)",
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Show sample images (requires display)",
    )
    parser.add_argument(
        "--random-seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)",
    )

    args = parser.parse_args()

    # Define expected file paths
    input_dir = args.input_dir
    test_images_path = input_dir / "emnist-digits-test-images-idx3-ubyte.gz"
    test_labels_path = input_dir / "emnist-digits-test-labels-idx1-ubyte.gz"
    train_images_path = input_dir / "emnist-digits-train-images-idx3-ubyte.gz"
    train_labels_path = input_dir / "emnist-digits-train-labels-idx1-ubyte.gz"

    # Verify input files exist
    for file_path in [
        test_images_path,
        test_labels_path,
        train_images_path,
        train_labels_path,
    ]:
        if not file_path.exists():
            print(f"Error: Required file not found: {file_path}")
            print(f"Please download EMNIST dataset files to {input_dir}")
            return

    print("Loading training data...")
    print("=" * 50)

    # Load training data
    train_images_data = load_emnist_images(train_images_path)
    train_labels_data = load_emnist_labels(train_labels_path)

    print(f"Loaded training images shape: {train_images_data.shape}")
    print(f"Loaded training labels shape: {train_labels_data.shape}")

    # Visualize if requested
    if args.visualize:
        print("Displaying sample training images...")
        visualize_images(train_images_data, train_labels_data)

    # Create balanced training sample
    final_train_images, final_train_labels = create_balanced_sample(
        train_images_data,
        train_labels_data,
        samples_per_class=args.train_samples_per_class,
        random_seed=args.random_seed,
    )

    # Process and save training data
    train_df, shuffled_train_labels = process_and_save_dataset(
        final_train_images,
        final_train_labels,
        args.output_dir,
        "train.csv",
        include_labels=True,
    )

    print("\nLoading test data...")
    print("=" * 50)

    # Load test data
    test_images_data = load_emnist_images(test_images_path)
    test_labels_data = load_emnist_labels(test_labels_path)

    print(f"Test images shape: {test_images_data.shape}")
    print(f"Test labels shape: {test_labels_data.shape}")

    # Create balanced test sample
    final_test_images, final_test_labels = create_balanced_sample(
        test_images_data,
        test_labels_data,
        samples_per_class=args.test_samples_per_class,
        random_seed=123,  # Different seed for test set
    )

    # Process and save test data (without labels)
    test_df, shuffled_test_labels = process_and_save_dataset(
        final_test_images,
        final_test_labels,
        args.output_dir,
        "test.csv",
        include_labels=False,
    )

    # Create submission files
    test_labels_df, sample_submission_df = create_submission_files(
        shuffled_test_labels, args.output_dir
    )

    # Print summary
    print_summary(train_df, test_df, test_labels_df, sample_submission_df)


if __name__ == "__main__":
    main()
