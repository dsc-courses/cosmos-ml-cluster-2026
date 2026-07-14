OK_FORMAT = True

test = {   'name': 'q5_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(len(external_results) == 36 and (not external_results.duplicated(['recipe', 'model']).any()))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(list(external_results.columns) == ['recipe', 'model', 'cv_accuracy', 'closed_accuracy', 'open_accuracy', 'mean_external_accuracy'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(external_results['mean_external_accuracy'].is_monotonic_decreasing)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(np.allclose(external_results['mean_external_accuracy'], external_results[['closed_accuracy', 'open_accuracy']].mean(axis=1)))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
