"""
Benchmark for EMNIST dataset using a simple neural network.
"""

import time
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


def load_and_preprocess_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load and preprocess EMNIST training and test data.

    Returns:
        Tuple of (train_df, test_df)
    """
    print("Loading EMNIST data...")
    train_df = pd.read_csv("scripts/emnist/train.csv")
    test_df = pd.read_csv("scripts/emnist/test.csv")

    print(f"Training data shape: {train_df.shape}")
    print(f"Test data shape: {test_df.shape}")

    return train_df, test_df


def prepare_features_and_labels(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Prepare features and labels for training.

    Args:
        train_df: Training dataframe with labels
        test_df: Test dataframe without labels

    Returns:
        Tuple of (X_train, y_train, X_test)
    """
    # Separate features and labels from training data
    X_train = train_df.drop("label", axis=1).values
    y_train = train_df["label"].values
    X_test = test_df.values

    # Normalize pixel values to [0, 1] range
    print("Normalizing pixel values...")
    X_train = X_train.astype(np.float32) / 255.0
    X_test = X_test.astype(np.float32) / 255.0

    # Apply standard scaling for better neural network performance
    print("Applying standard scaling...")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print(f"Training features shape: {X_train.shape}")
    print(f"Training labels shape: {y_train.shape}")
    print(f"Test features shape: {X_test.shape}")

    return X_train, y_train, X_test


def create_and_train_model(
    X_train: np.ndarray, y_train: np.ndarray
) -> MLPClassifier:
    """
    Create and train a neural network with 2 hidden layers of 16 neurons each.

    Args:
        X_train: Training features
        y_train: Training labels

    Returns:
        Trained MLPClassifier model
    """
    print("Creating neural network with 2 hidden layers (16 neurons each)...")

    # Create MLPClassifier with specified architecture
    mlp = MLPClassifier(
        hidden_layer_sizes=(16, 16),  # 2 hidden layers with 16 neurons each
        activation="relu",
        solver="adam",
        alpha=0.01,  # L2 penalty parameter
        batch_size="auto",
        learning_rate="constant",
        learning_rate_init=0.001,
        max_iter=500,
        shuffle=True,
        random_state=42,
        tol=0.0001,
        verbose=True,
        warm_start=False,
        momentum=0.9,
        nesterovs_momentum=True,
        early_stopping=False,
        validation_fraction=0.1,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-08,
    )

    print("Training the neural network...")
    start_time = time.time()

    mlp.fit(X_train, y_train)

    end_time = time.time()
    print(f"Training completed in {end_time - start_time:.2f} seconds")
    print(f"Number of iterations: {mlp.n_iter_}")

    return mlp


def evaluate_model(
    mlp: MLPClassifier, X_train: np.ndarray, y_train: np.ndarray
) -> None:
    """
    Evaluate the trained model on training data.

    Args:
        mlp: Trained MLPClassifier model
        X_train: Training features
        y_train: Training labels
    """
    print("\nEvaluating model on training data...")

    # Make predictions on training data
    y_train_pred = mlp.predict(X_train)

    # Calculate accuracy
    train_accuracy = accuracy_score(y_train, y_train_pred)
    print(f"Training accuracy: {train_accuracy:.4f}")

    # Print detailed classification report
    print("\nClassification Report:")
    print(classification_report(y_train, y_train_pred))


def make_predictions_and_save(
    mlp: MLPClassifier,
    X_test: np.ndarray,
    output_filename: str = "predictions.csv",
) -> None:
    """
    Make predictions on test data and save in the required format.

    Args:
        mlp: Trained MLPClassifier model
        X_test: Test features
        output_filename: Name of the output file
    """
    print(f"\nMaking predictions on {X_test.shape[0]} test samples...")

    # Make predictions
    y_pred = mlp.predict(X_test)

    # Create submission dataframe in the same format as sample_submission.csv
    submission_df = pd.DataFrame(
        {"id": range(len(y_pred)), "label": y_pred.astype(int)}
    )

    # Save to CSV
    submission_df.to_csv(output_filename, index=False)
    print(f"Predictions saved to {output_filename}")

    # Print some statistics
    unique_labels, counts = np.unique(y_pred, return_counts=True)
    print("\nPrediction distribution:")
    for label, count in zip(unique_labels, counts):
        percentage = count / len(y_pred) * 100
        print(f"Class {label}: {count} predictions ({percentage:.1f}%)")


def main() -> None:
    """Main function to run the EMNIST benchmark."""
    print("EMNIST Neural Network Benchmark")
    print("=" * 50)

    # Load and preprocess data
    train_df, test_df = load_and_preprocess_data()

    # Prepare features and labels
    X_train, y_train, X_test = prepare_features_and_labels(train_df, test_df)

    # Create and train the model
    mlp = create_and_train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(mlp, X_train, y_train)

    # Make predictions and save results
    make_predictions_and_save(mlp, X_test, "emnist_predictions.csv")

    print("\nBenchmark completed successfully!")


if __name__ == "__main__":
    main()
