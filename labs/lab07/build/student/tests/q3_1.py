OK_FORMAT = True

test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> bool(isinstance(folds, StratifiedKFold) and folds.n_splits == 5 and folds.shuffle and (folds.random_state == 0))\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(set(model_specs) == {'logistic_regression', 'knn', 'random_forest'})\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(isinstance(model_specs['logistic_regression']['estimator'], LogisticRegression) and "
                                               "isinstance(model_specs['logistic_regression']['parameter_grid'], dict))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(model_specs['logistic_regression']['parameter_grid']['logisticregression__C'] == [0.01, 0.1, 1, 10])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(model_specs['random_forest']['estimator'].n_estimators == 200 and model_specs['random_forest']['estimator'].random_state == 0)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
