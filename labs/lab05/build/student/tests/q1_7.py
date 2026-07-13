OK_FORMAT = True

test = {   'name': 'q1_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(one_nn_predictions, pd.Series))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(one_nn_predictions.index.equals(test_features.index))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(one_nn_predictions.isin(training_labels.unique()).all())\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
