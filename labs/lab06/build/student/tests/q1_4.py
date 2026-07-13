OK_FORMAT = True

test = {   'name': 'q1_4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> bool(isinstance(spotify_errors_by_size, pd.DataFrame) and spotify_errors_by_size.index.tolist() == spotify_training_sizes)\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(spotify_errors_by_size.columns.tolist() == ['train_error', 'valid_error'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(np.allclose(spotify_errors_by_size.iloc[[0, -1]].to_numpy(), [[0.22, 0.2410714285714286], [0.1054198927933293, 0.1339285714285714]]))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
