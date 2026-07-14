OK_FORMAT = True

test = {   'name': 'q5_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> bool(list(frozen_test_results.columns) == ['model', 'recipe', 'cv_accuracy', 'closed_accuracy', 'open_accuracy'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(len(frozen_test_results) == 3 and set(frozen_test_results['model']) == set(model_specs))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(frozen_test_results[['closed_accuracy', 'open_accuracy']].apply(lambda column: column.between(0.8, 1).all()).all())\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
