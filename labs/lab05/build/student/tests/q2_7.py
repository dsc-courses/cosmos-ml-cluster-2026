OK_FORMAT = True

test = {   'name': 'q2_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(best_k in {1, 3, 5, 9})\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(np.isclose(accuracy_by_k.loc[best_k, 'accuracy'], accuracy_by_k['accuracy'].max()))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
