OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> bool(train_valid_errors(spotify_5nn_split, X_spotify_train, y_spotify_train, X_spotify_valid, y_spotify_valid).index.tolist() == ['train_error', "
                                               "'valid_error'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(np.allclose(train_valid_errors(spotify_5nn_split, X_spotify_train, y_spotify_train, X_spotify_valid, y_spotify_valid).to_numpy(), '
                                               '[0.1054198927933293, 0.1339285714285714]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
