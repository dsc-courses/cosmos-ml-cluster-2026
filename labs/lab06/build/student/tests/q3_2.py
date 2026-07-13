OK_FORMAT = True

test = {   'name': 'q3_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(list(scaled_steel_5nn.named_steps) == ['standardscaler', 'kneighborsclassifier'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(scaled_steel_5nn.named_steps['kneighborsclassifier'].n_neighbors == 5)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.allclose(scaled_steel_5nn_errors.to_numpy(), [0.20618556701030932, 0.28865979381443296]))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(scaled_steel_5nn_errors['valid_error'] < steel_errors_by_k.loc[5, 'valid_error'])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
