OK_FORMAT = True

test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(two_feature_scaler, StandardScaler))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(isinstance(steel_two_standardized, pd.DataFrame) and steel_two_standardized.index.equals(X_steel_train.index) and '
                                               '(steel_two_standardized.columns.tolist() == two_features))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(np.allclose(steel_two_standardized.mean().to_numpy(), [0, 0], atol=1e-12))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.allclose(steel_two_standardized.to_numpy().std(axis=0), [1, 1]))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
