OK_FORMAT = True

test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(set(baseline_searches) == set(model_specs))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(all((isinstance(search, GridSearchCV) for search in baseline_searches.values())))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(list(baseline_results.columns) == ['model', 'cv_accuracy', 'cv_std', 'train_accuracy', 'best_parameters'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(len(baseline_results) == 3 and baseline_results['cv_accuracy'].between(0.95, 1).all())\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
