OK_FORMAT = True

test = {   'name': 'q4_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(len(searches) == len(feature_recipes) * len(model_specs) == 36)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(list(cv_results.columns) == ['recipe', 'model', 'num_features', 'cv_accuracy', 'cv_std', 'train_accuracy', 'best_parameters'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(len(cv_results) == 36 and (not cv_results.duplicated(['recipe', 'model']).any()))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(cv_results['cv_accuracy'].between(majority_baseline, 1).all())\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
