OK_FORMAT = True

test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> bool(isinstance(steel_errors_by_size, pd.DataFrame) and steel_errors_by_size.index.tolist() == steel_training_sizes)\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(steel_errors_by_size.columns.tolist() == ['train_error', 'valid_error'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(np.allclose(steel_errors_by_size.iloc[[0, -1]].to_numpy(), [[0.52, 0.6838487972508591], [0.37915234822451316, 0.570446735395189]]))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
