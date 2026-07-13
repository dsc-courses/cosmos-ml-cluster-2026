OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(spotify_errors_by_k, pd.DataFrame) and spotify_errors_by_k.index.tolist() == k_values)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(spotify_errors_by_k.columns.tolist() == ['train_error', 'valid_error'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(np.allclose(spotify_errors_by_k['valid_error'].to_numpy(), [0.15, 0.1339285714285714, 0.14464285714285718, 0.15892857142857142, "
                                               '0.16607142857142854, 0.19999999999999996, 0.2767857142857143]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(spotify_errors_by_k.loc[1, 'train_error'] == 0)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
