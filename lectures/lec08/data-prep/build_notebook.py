"""Build the Lecture 8 notebook.

Run from the repository root with:

    uv run python lectures/lec08/data-prep/build_notebook.py
"""

from pathlib import Path
from textwrap import dedent

import nbformat as nbf


OUTPUT = Path(__file__).parents[1] / "lec08.ipynb"


def clean(source: str) -> str:
    return dedent(source).strip("\n") + "\n"


def markdown(source: str, slide_type: str | None = None):
    cell = nbf.v4.new_markdown_cell(clean(source))
    if slide_type is not None:
        cell.metadata["slideshow"] = {"slide_type": slide_type}
    return cell


def code(source: str, slide_type: str | None = None):
    cell = nbf.v4.new_code_cell(clean(source))
    if slide_type is not None:
        cell.metadata["slideshow"] = {"slide_type": slide_type}
    return cell


def main() -> None:
    cells = [
        code(
            r'''
            # Run this cell to set up packages for lecture.
            import pandas as pd
            import numpy as np
            from pathlib import Path

            import matplotlib.pyplot as plt
            from IPython.display import display

            path = 'lectures/lec08'
            if not Path('data').exists():
                !wget -q -O /content/course.zip https://github.com/dsc-courses/cosmos-ml-cluster-2026/archive/refs/heads/main.zip
                !unzip -q -o /content/course.zip "cosmos-ml-cluster-2026-main/{path}/data/*" -d /content/course-assets
                !cp -R /content/course-assets/cosmos-ml-cluster-2026-main/{path}/data .

            plt.style.use('seaborn-v0_8-colorblind')
            plt.rcParams.update({
                'figure.figsize': (10, 5),
                'axes.titlesize': 14,
                'axes.titleweight': 'bold',
                'axes.labelsize': 12,
                'axes.labelweight': 'bold',
                'axes.linewidth': 1.5,
                'grid.color': '#999999',
                'grid.alpha': 0.35,
                'font.weight': 'bold',
                'legend.fontsize': 11,
            })

            pd.set_option('display.max_rows', 10)
            pd.set_option('display.max_columns', 10)
            pd.set_option('display.precision', 3)
            ''',
            "skip",
        ),
        markdown(
            r'''
            # Lecture 8 - Building and Choosing a k-NN Classifier

            ## COSMOS ML Cluster 2026
            ''',
            "slide",
        ),
        markdown(
            r'''
            ### Agenda

            - Generalization and model complexity.
            - Bias and model variance.
            - Hyperparameters and cross-validation.
            - Feature engineering and standardization.
            - Pipelines.
            - Selecting and evaluating a final classifier.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ### Learning goals

            By the end of today, you should be able to:

            - Explain why the model with the lowest training error may not make the best future predictions.
            - Describe bias and model variance using decision boundaries.
            - Use cross-validation to choose a number of neighbors.
            - Explain why feature scale affects k-NN.
            - Combine `StandardScaler` and k-NN in a `Pipeline`.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Opening challenge

            Last time, we used 5-NN—but we did not establish that five was the best number of neighbors.

            > How should we choose a classifier that will work well on points it has never seen?
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## A toy classification problem

            Each point belongs to one of two classes. Its two features describe its horizontal and vertical position.

            The curved shape is artificial on purpose: it lets us see exactly what different classifiers learn.
            ''',
            "slide",
        ),
        code(
            r'''
            from sklearn.model_selection import KFold, cross_val_score, train_test_split
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.pipeline import make_pipeline
            from sklearn.preprocessing import StandardScaler

            data = pd.read_csv('data/toy-moons.csv')
            data.head()
            '''
        ),
        code(
            r'''
            features = ['horizontal_position', 'vertical_position']
            class_order = ['purple', 'gold']
            class_colors = {'purple': '#6f4aa8', 'gold': '#e69f00'}

            X = data[features]
            y = data['class']

            # Use an ordinary random split. The test data stays untouched until the end.
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.25, random_state=42
            )

            print(f'Training points: {len(X_train)}')
            print(f'Test points kept hidden: {len(X_test)}')
            '''
        ),
        code(
            r'''
            def scatter_classes(X_data, y_data, ax, title=None, alpha=0.8):
                for label in class_order:
                    points = X_data[y_data == label]
                    ax.scatter(
                        points.iloc[:, 0], points.iloc[:, 1],
                        s=36, alpha=alpha, color=class_colors[label], label=label
                    )
                ax.set(
                    xlabel=X_data.columns[0].replace('_', ' '),
                    ylabel=X_data.columns[1].replace('_', ' '),
                    title=title,
                )
                ax.legend()


            fig, ax = plt.subplots(figsize=(8, 5))
            scatter_classes(X_train, y_train, ax, 'The training data')
            ax.set_aspect('equal', adjustable='box')
            plt.show()
            '''
        ),
        markdown(
            r'''
            ### Quick recall from Lecture 7

            - k-NN finds nearby labeled training points.
            - The $k$ closest points vote on the prediction.
            - A decision boundary shows where predictions change.
            - Training error measures mistakes on familiar points.
            - We care most about predictions on new, unseen points.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## The number of neighbors controls model complexity

            Before running the next cell, predict which boundary belongs to:

            - 1 neighbor,
            - 9 neighbors, and
            - 75 neighbors.
            ''',
            "slide",
        ),
        code(
            r'''
            def plot_boundary(model, X_data, y_data, ax, title, grid_size=220):
                x_name, y_name = X_data.columns
                x_pad = 0.08 * (X_data[x_name].max() - X_data[x_name].min())
                y_pad = 0.08 * (X_data[y_name].max() - X_data[y_name].min())
                x_values = np.linspace(X_data[x_name].min() - x_pad,
                                       X_data[x_name].max() + x_pad, grid_size)
                y_values = np.linspace(X_data[y_name].min() - y_pad,
                                       X_data[y_name].max() + y_pad, grid_size)
                xx, yy = np.meshgrid(x_values, y_values)
                grid = pd.DataFrame({x_name: xx.ravel(), y_name: yy.ravel()})
                predicted = model.predict(grid)
                prediction_codes = pd.Categorical(
                    predicted, categories=class_order
                ).codes.reshape(xx.shape)

                ax.contourf(
                    xx, yy, prediction_codes,
                    levels=[-0.5, 0.5, 1.5],
                    colors=['#e8def3', '#fff0c7'], alpha=0.9
                )
                scatter_classes(X_data, y_data, ax, title=title, alpha=0.75)


            neighbor_counts_for_picture = [1, 9, 75]
            fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), sharex=True, sharey=True)

            for neighbors, ax in zip(neighbor_counts_for_picture, axes):
                model = KNeighborsClassifier(n_neighbors=neighbors).fit(X_train, y_train)
                plot_boundary(model, X_train, y_train, ax, f'{neighbors}-NN')

            plt.tight_layout()
            plt.show()
            '''
        ),
        code(
            r'''
            training_errors = []
            for neighbors in neighbor_counts_for_picture:
                model = KNeighborsClassifier(n_neighbors=neighbors).fit(X_train, y_train)
                training_errors.append({
                    'neighbors': neighbors,
                    'training error': 1 - model.score(X_train, y_train),
                })

            pd.DataFrame(training_errors).set_index('neighbors')
            '''
        ),
        markdown(
            r'''
            ### Flexibility runs in the opposite direction from the number of neighbors

            | Number of neighbors | Boundary | Typical risk |
            | --- | --- | --- |
            | Small | Jagged and flexible | Overfitting |
            | Medium | Smoother, but still local | A useful balance |
            | Very large | Very smooth and simple | Underfitting |

            **Overfitting** means learning quirks or noise in the training sample.

            **Underfitting** means using a rule too simple to capture the pattern.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Generalization

            A model **generalizes** when it works well on new examples drawn from the same process as its training data.

            A classifier that memorizes every training point may still generalize poorly.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## What if we collected a different training sample?

            Our training data is only one possible sample. The next figure fits classifiers to three new samples generated by the same process.

            Look for:

            - predictions that change from sample to sample;
            - structure that a classifier consistently misses.
            ''',
            "slide",
        ),
        code(
            r'''
            from sklearn.datasets import make_moons


            def sample_moons(seed, n=120):
                sample_X, sample_y = make_moons(
                    n_samples=n, noise=0.22, random_state=seed
                )
                sample_X = pd.DataFrame(sample_X, columns=features)
                sample_y = pd.Series(sample_y).map({0: 'purple', 1: 'gold'})
                return sample_X, sample_y


            sample_seeds = [3, 11, 25]
            fig, axes = plt.subplots(2, 3, figsize=(15, 8), sharex=True, sharey=True)

            for column, seed in enumerate(sample_seeds):
                sample_X, sample_y = sample_moons(seed)
                for row, neighbors in enumerate([1, 75]):
                    model = KNeighborsClassifier(n_neighbors=neighbors).fit(sample_X, sample_y)
                    plot_boundary(
                        model, sample_X, sample_y, axes[row, column],
                        f'Sample {column + 1}: {neighbors}-NN', grid_size=160
                    )

            plt.tight_layout()
            plt.show()
            '''
        ),
        markdown(
            r'''
            ## Bias and model variance

            **Model variance** describes how much a model's predictions change when its training sample changes.

            - High variance is associated with overfitting.
            - 1-NN has high variance because individual points strongly control its boundary.

            **Bias** describes systematic error caused by a model being unable to capture the real pattern.

            - High bias is associated with underfitting.
            - A very large number of neighbors smooths away useful curved structure.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ### Concept Check

            Suppose replacing five training points causes large sections of a classifier's decision boundary to move.

            1. Does this illustrate bias or model variance?
            2. Would you expect this more often with a small or large number of neighbors?
            ''',
            "slide",
        ),
        markdown(
            r'''
            ### Concept Check answer

            1. **Model variance**: the fitted classifier is sensitive to the training sample.
            2. A **small** number of neighbors is usually more sensitive to individual points.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Hyperparameters

            A **hyperparameter** is a setting we choose before fitting a model.

            For k-NN, the number of neighbors is a hyperparameter:

            ```python
            KNeighborsClassifier(n_neighbors=9)
            ```

            The training data does not automatically tell `KNeighborsClassifier` which value to use.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Why not choose using the test set?

            Suppose we try 40 neighbor counts and choose the one with the highest test accuracy.

            Then our choice is tailored to that particular test set. The test set is no longer an honest simulation of future data.

            > Use training data to design and select the model. Use test data once, at the end.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Cross-validation

            Cross-validation lets different parts of the training data take turns acting like unseen data.

            In **5-fold cross-validation**:

            1. Divide the training rows into five folds of nearly equal size.
            2. Train on four folds and validate on the remaining fold.
            3. Repeat until every fold has been used for validation.
            4. Average the five validation scores.
            ''',
            "slide",
        ),
        code(
            r'''
            fold_diagram = pd.DataFrame(
                [
                    ['validation' if row == column else 'training'
                     for column in range(1, 6)]
                    for row in range(1, 6)
                ],
                index=[f'Fit {i}' for i in range(1, 6)],
                columns=[f'Fold {i}' for i in range(1, 6)],
            )
            fold_diagram
            '''
        ),
        markdown(
            r'''
            ### Ordinary, uniform `KFold`

            We will use regular `KFold`, which makes fold sizes as equal as possible.

            ```python
            folds = KFold(n_splits=5, shuffle=True, random_state=42)
            ```

            Shuffling makes the assignment random. Regular `KFold` does **not** force every fold to have identical class proportions.
            ''',
            "slide",
        ),
        code(
            r'''
            folds = KFold(n_splits=5, shuffle=True, random_state=42)

            fold_summaries = []
            for fold_number, (_, validation_positions) in enumerate(
                folds.split(X_train), start=1
            ):
                validation_labels = y_train.iloc[validation_positions]
                counts = validation_labels.value_counts()
                fold_summaries.append({
                    'fold': fold_number,
                    'validation rows': len(validation_positions),
                    'purple': counts.get('purple', 0),
                    'gold': counts.get('gold', 0),
                })

            pd.DataFrame(fold_summaries).set_index('fold')
            '''
        ),
        markdown(
            r'''
            ### Two unrelated uses of the letter $k$

            - In **k-NN**, $k$ is the number of neighbors.
            - In **k-fold cross-validation**, $k$ is the number of folds.

            Five-fold cross-validation does **not** require a 5-NN classifier.

            We will say **neighbor count** and **number of folds** to keep them separate.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## A surprise: changing units changes k-NN

            Imagine that horizontal and vertical position are both measured in meters.

            Now report horizontal position in centimeters by multiplying it by 100. We have not changed any physical locations or labels.

            > Should changing units change a classifier's predictions?
            ''',
            "slide",
        ),
        code(
            r'''
            def use_mixed_units(X_data):
                converted = X_data.copy()
                converted['horizontal_position'] *= 100
                return converted


            X_train_mixed = use_mixed_units(X_train)
            X_test_mixed = use_mixed_units(X_test)  # Prepared, but not examined yet.

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            scatter_classes(X_train, y_train, axes[0], 'Both positions measured in meters')
            axes[0].set(xlabel='horizontal position (meters)', ylabel='vertical position (meters)')
            axes[0].set_aspect('equal', adjustable='box')

            scatter_classes(X_train_mixed, y_train, axes[1],
                            'Horizontal in centimeters; vertical in meters')
            axes[1].set(xlabel='horizontal position (centimeters)',
                        ylabel='vertical position (meters)')

            plt.tight_layout()
            plt.show()
            '''
        ),
        code(
            r'''
            # Create unlabeled demo locations. These are not test data.
            x_values = np.linspace(X_train['horizontal_position'].min(),
                                   X_train['horizontal_position'].max(), 120)
            y_values = np.linspace(X_train['vertical_position'].min(),
                                   X_train['vertical_position'].max(), 120)
            xx, yy = np.meshgrid(x_values, y_values)
            demo_locations = pd.DataFrame({
                'horizontal_position': xx.ravel(),
                'vertical_position': yy.ravel(),
            })
            demo_locations_mixed = use_mixed_units(demo_locations)

            same_units_model = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
            mixed_units_model = KNeighborsClassifier(n_neighbors=5).fit(X_train_mixed, y_train)

            predictions_same_units = same_units_model.predict(demo_locations)
            predictions_mixed_units = mixed_units_model.predict(demo_locations_mixed)
            agreement = np.mean(predictions_same_units == predictions_mixed_units)

            print(f'Predictions that agree after only changing units: {agreement:.1%}')
            '''
        ),
        code(
            r'''
            changed_positions = np.flatnonzero(
                predictions_same_units != predictions_mixed_units
            )
            changed_locations = demo_locations.iloc[changed_positions]
            standardized_distance_from_center = (
                (changed_locations - X_train.mean()) / X_train.std(ddof=0)
            ) ** 2
            most_central_disagreement = standardized_distance_from_center.sum(axis=1).argmin()
            changed_position = changed_positions[most_central_disagreement]
            query_meters = demo_locations.iloc[[changed_position]]
            query_mixed = demo_locations_mixed.iloc[[changed_position]]

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))
            for ax, train_space, query, model, title in [
                (axes[0], X_train, query_meters, same_units_model, 'Both features in meters'),
                (axes[1], X_train_mixed, query_mixed, mixed_units_model, 'Mixed units'),
            ]:
                scatter_classes(train_space, y_train, ax, title, alpha=0.45)
                distances, positions = model.kneighbors(query)
                neighbors = train_space.iloc[positions[0]]
                ax.scatter(query.iloc[:, 0], query.iloc[:, 1],
                           marker='*', s=260, color='black', label='query')
                for _, neighbor in neighbors.iterrows():
                    ax.plot(
                        [query.iloc[0, 0], neighbor.iloc[0]],
                        [query.iloc[0, 1], neighbor.iloc[1]],
                        color='black', alpha=0.55, linewidth=1.2
                    )
                ax.legend()

            print('Prediction with both features in meters:',
                  same_units_model.predict(query_meters)[0])
            print('Prediction with mixed units:',
                  mixed_units_model.predict(query_mixed)[0])
            plt.tight_layout()
            plt.show()
            '''
        ),
        markdown(
            r'''
            ## Why scale matters for k-NN

            Distance adds together differences from every feature.

            When horizontal position is multiplied by 100, its contribution to distance becomes much larger. Horizontal position is effectively over-weighted, while vertical position is under-weighted.

            This is a feature-engineering decision—even though no information was added or removed.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Feature engineering

            **Feature engineering** means turning raw data into useful numerical features for a model.

            Good feature engineering depends on:

            - what each column means;
            - the units and numerical spread of each column;
            - how the model uses the features.

            Scaling is especially important for models like k-NN that use distance.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## `StandardScaler`

            `StandardScaler` transforms each feature into **standard units**:

            $$
            z = \frac{x - \text{training mean}}{\text{training standard deviation}}.
            $$

            After transformation, each training feature has:

            - mean approximately 0;
            - standard deviation approximately 1.
            ''',
            "slide",
        ),
        code(
            r'''
            scaler = StandardScaler()
            scaler.fit(X_train_mixed)

            X_train_scaled = pd.DataFrame(
                scaler.transform(X_train_mixed),
                columns=features,
                index=X_train_mixed.index,
            )

            scale_summary = pd.DataFrame({
                'mean before': X_train_mixed.mean(),
                'SD before': X_train_mixed.std(ddof=0),
                'mean after': X_train_scaled.mean(),
                'SD after': X_train_scaled.std(ddof=0),
            })
            scale_summary
            '''
        ),
        markdown(
            r'''
            ### A transformer learns from data

            ```python
            scaler.fit(X_train)
            scaler.transform(X_train)
            scaler.transform(X_new)
            ```

            - `fit` learns the training means and standard deviations.
            - `transform` uses those already-learned values.
            - Do **not** fit the scaler on validation or test data.

            Otherwise, information from supposedly unseen data leaks into the modeling process.
            ''',
            "slide",
        ),
        code(
            r'''
            # With scaling, changing meters to centimeters no longer changes predictions.
            scaled_same_units_model = make_pipeline(
                StandardScaler(), KNeighborsClassifier(n_neighbors=5)
            ).fit(X_train, y_train)

            scaled_mixed_units_model = make_pipeline(
                StandardScaler(), KNeighborsClassifier(n_neighbors=5)
            ).fit(X_train_mixed, y_train)

            scaled_predictions_1 = scaled_same_units_model.predict(demo_locations)
            scaled_predictions_2 = scaled_mixed_units_model.predict(demo_locations_mixed)

            print('Agreement without scaling:',
                  f'{np.mean(predictions_same_units == predictions_mixed_units):.1%}')
            print('Agreement with scaling:',
                  f'{np.mean(scaled_predictions_1 == scaled_predictions_2):.1%}')
            '''
        ),
        markdown(
            r'''
            ## Pipelines

            A `Pipeline` combines feature transformations and a classifier into one object.

            ```python
            model = make_pipeline(
                StandardScaler(),
                KNeighborsClassifier(n_neighbors=9)
            )
            ```

            ```text
            raw features → StandardScaler → scaled features → k-NN → prediction
            ```
            ''',
            "slide",
        ),
        code(
            r'''
            model = make_pipeline(
                StandardScaler(),
                KNeighborsClassifier(n_neighbors=9),
            )

            model.fit(X_train_mixed, y_train)
            model.predict(demo_locations_mixed.iloc[:5])
            '''
        ),
        markdown(
            r'''
            ### What a pipeline does

            When we call `model.fit(X_train, y_train)`, the pipeline:

            1. fits the scaler on `X_train`;
            2. transforms `X_train`;
            3. fits k-NN on the transformed values.

            When we call `model.predict(X_new)`, it:

            1. transforms `X_new` using the **training** means and SDs;
            2. passes the transformed values to k-NN.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ### Pipelines and cross-validation

            Passing a pipeline to cross-validation is important:

            ```python
            cross_val_score(model, X_train, y_train, cv=folds)
            ```

            For each fit, the scaler learns only from that fit's four training folds. It does not peek at the validation fold.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Cross-validation scores

            Let's begin with three candidate neighbor counts. Each column below contains five validation accuracies—one from each fold.
            ''',
            "slide",
        ),
        code(
            r'''
            candidate_scores = {}
            for neighbors in [1, 9, 75]:
                candidate_model = make_pipeline(
                    StandardScaler(),
                    KNeighborsClassifier(n_neighbors=neighbors),
                )
                candidate_scores[f'{neighbors} neighbors'] = cross_val_score(
                    candidate_model, X_train_mixed, y_train, cv=folds
                )

            fold_scores = pd.DataFrame(
                candidate_scores,
                index=[f'Fold {i}' for i in range(1, 6)],
            )
            fold_scores.loc['Mean'] = fold_scores.mean()
            fold_scores
            '''
        ),
        markdown(
            r'''
            ### Concept Check

            Suppose we compare 12 neighbor counts using 5-fold cross-validation.

            1. How many classifiers are fitted?
            2. How many times does each training row appear in a validation fold for each neighbor count?
            ''',
            "slide",
        ),
        markdown(
            r'''
            ### Concept Check answer

            1. $12 \times 5 = 60$ classifiers are fitted.
            2. Each training row appears in a validation fold **once per neighbor count**.

            Across the entire search, each row is used for validation 12 times.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Selecting the full modeling recipe

            We will compare:

            - neighbor counts from 1 through 75;
            - raw k-NN on the mixed-unit features;
            - standardized k-NN pipelines.

            Scaling is part of the model choice, not a separate afterthought.
            ''',
            "slide",
        ),
        code(
            r'''
            search_results = []

            for neighbors in range(1, 76, 2):
                raw_model = KNeighborsClassifier(n_neighbors=neighbors)
                scaled_model = make_pipeline(
                    StandardScaler(),
                    KNeighborsClassifier(n_neighbors=neighbors),
                )

                raw_validation_scores = cross_val_score(
                    raw_model, X_train_mixed, y_train, cv=folds
                )
                scaled_validation_scores = cross_val_score(
                    scaled_model, X_train_mixed, y_train, cv=folds
                )

                scaled_model.fit(X_train_mixed, y_train)
                search_results.append({
                    'neighbors': neighbors,
                    'raw validation error': 1 - raw_validation_scores.mean(),
                    'scaled validation error': 1 - scaled_validation_scores.mean(),
                    'validation error SD': scaled_validation_scores.std(),
                    'scaled training error': 1 - scaled_model.score(X_train_mixed, y_train),
                })

            search_results = pd.DataFrame(search_results)
            search_results.head()
            '''
        ),
        code(
            r'''
            fig, axes = plt.subplots(1, 2, figsize=(15, 5))

            axes[0].plot(
                search_results['neighbors'], search_results['scaled training error'],
                marker='o', markersize=3, label='Training error'
            )
            axes[0].plot(
                search_results['neighbors'], search_results['scaled validation error'],
                marker='o', markersize=3, label='5-fold validation error'
            )
            axes[0].set(
                xlabel='Number of neighbors', ylabel='Classification error',
                title='Training vs. validation error (scaled)'
            )
            axes[0].legend()
            axes[0].grid(True)

            axes[1].plot(
                search_results['neighbors'], search_results['raw validation error'],
                marker='o', markersize=3, label='Raw mixed-unit features'
            )
            axes[1].plot(
                search_results['neighbors'], search_results['scaled validation error'],
                marker='o', markersize=3, label='Standardized pipeline'
            )
            axes[1].set(
                xlabel='Number of neighbors', ylabel='5-fold validation error',
                title='Feature scale is part of model selection'
            )
            axes[1].legend()
            axes[1].grid(True)

            plt.tight_layout()
            plt.show()
            '''
        ),
        code(
            r'''
            best_row = search_results.loc[
                search_results['scaled validation error'].idxmin()
            ]
            chosen_neighbors = int(best_row['neighbors'])

            print(f'Chosen neighbor count: {chosen_neighbors}')
            print(f'Mean validation error: {best_row["scaled validation error"]:.1%}')
            print(f'Mean validation accuracy: {1 - best_row["scaled validation error"]:.1%}')
            '''
        ),
        markdown(
            r'''
            ### Do not overinterpret tiny differences

            Cross-validation scores depend on the particular folds and sample.

            If several neighbor counts have nearly identical validation scores, there may not be a meaningful winner. A slightly smoother model can be a reasonable choice when performance is effectively tied.

            The important result is the useful **range**, not just one magic integer.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Final evaluation

            We have now chosen:

            - the feature transformation: standardization;
            - the classifier: k-NN;
            - the neighbor count: selected by cross-validation.

            We can finally fit on all training rows and evaluate once on the untouched test set.
            ''',
            "slide",
        ),
        code(
            r'''
            final_model = make_pipeline(
                StandardScaler(),
                KNeighborsClassifier(n_neighbors=chosen_neighbors),
            )

            final_model.fit(X_train_mixed, y_train)
            final_test_predictions = final_model.predict(X_test_mixed)
            final_test_accuracy = final_model.score(X_test_mixed, y_test)

            print(f'Final test accuracy: {final_test_accuracy:.1%}')
            print(f'Final test error: {1 - final_test_accuracy:.1%}')
            '''
        ),
        code(
            r'''
            fig, ax = plt.subplots(figsize=(10, 5.5))
            plot_boundary(
                final_model, X_train_mixed, y_train, ax,
                f'Final standardized {chosen_neighbors}-NN classifier'
            )

            for label in class_order:
                points = X_test_mixed[y_test == label]
                ax.scatter(
                    points.iloc[:, 0], points.iloc[:, 1],
                    marker='x', s=75, linewidth=2.2,
                    color=class_colors[label],
                    label=f'test: {label}',
                )

            ax.set(
                xlabel='horizontal position (centimeters)',
                ylabel='vertical position (meters)',
            )
            ax.legend(ncol=2)
            plt.tight_layout()
            plt.show()
            '''
        ),
        markdown(
            r'''
            ## The modeling workflow

            1. Split the data into training and test sets.
            2. Keep the test set untouched.
            3. Define candidate pipelines and hyperparameters.
            4. Use cross-validation on the training data to compare candidates.
            5. Choose the full modeling recipe.
            6. Fit that recipe on all training data.
            7. Evaluate once on the test set.
            ''',
            "slide",
        ),
        markdown(
            r'''
            ## Takeaways

            - The best fit to training data is not necessarily the best predictor of new data.
            - Small-neighbor k-NN is flexible and can have high model variance.
            - Large-neighbor k-NN is smooth and can have high bias.
            - Cross-validation helps select hyperparameters without using the test set.
            - Regular `KFold` creates equally sized folds but does not balance their class proportions.
            - Feature scale changes distance and therefore changes k-NN predictions.
            - A pipeline keeps feature engineering and classification together.
            ''',
            "slide",
        ),
        code("", None),
    ]

    notebook = nbf.v4.new_notebook(cells=cells)
    notebook.metadata = {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.14.0",
        },
        "livereveal": {"scroll": True, "transition": "none"},
        "rise": {"enable_chalkboard": True},
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(notebook, OUTPUT)
    print(f"Wrote {len(cells)} cells to {OUTPUT}")


if __name__ == "__main__":
    main()
