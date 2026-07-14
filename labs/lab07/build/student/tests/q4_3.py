OK_FORMAT = True

test = {   'name': 'q4_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(forest_importances, pd.Series))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.isclose(forest_importances.sum(), 1))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(forest_importances.is_monotonic_decreasing)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(set(forest_importances.index) == set(forest_feature_names))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
