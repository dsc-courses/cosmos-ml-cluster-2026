OK_FORMAT = True

test = {   'name': 'q3_4',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(list(final_steel_model.named_steps) == ['standardscaler', 'kneighborsclassifier'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(final_steel_model.named_steps['kneighborsclassifier'].n_neighbors == best_scaled_steel_k)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(len(final_steel_model.named_steps['standardscaler'].mean_) == len(steel_features))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.isclose(steel_test_error, 0.281786941580756))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
