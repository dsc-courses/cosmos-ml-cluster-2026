OK_FORMAT = True

test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> bool(isinstance(make_search(model_specs['knn']['estimator'], model_specs['knn']['parameter_grid'], feature_recipes['all_plus_time']), "
                                               'GridSearchCV))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(list(make_search(model_specs['knn']['estimator'], model_specs['knn']['parameter_grid'], "
                                               "feature_recipes['all_plus_time']).estimator.named_steps) == ['functiontransformer', 'standardscaler', 'kneighborsclassifier'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(make_search(model_specs['knn']['estimator'], model_specs['knn']['parameter_grid'], feature_recipes['all_plus_time']).scoring == 'accuracy')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(make_search(model_specs['knn']['estimator'], model_specs['knn']['parameter_grid'], feature_recipes['all_plus_time']).return_train_score)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
