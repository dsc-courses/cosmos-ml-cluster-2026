OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool((len(X_spotify_train), len(X_spotify_valid), len(X_spotify_test)) == (1679, 560, 560))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(set(X_spotify_train.index).isdisjoint(X_spotify_valid.index) and set(X_spotify_train.index).isdisjoint(X_spotify_test.index) and '
                                               'set(X_spotify_valid.index).isdisjoint(X_spotify_test.index))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(X_spotify_train.index.equals(y_spotify_train.index) and X_spotify_valid.index.equals(y_spotify_valid.index) and '
                                               'X_spotify_test.index.equals(y_spotify_test.index))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(y_spotify_train.value_counts().max() - y_spotify_train.value_counts().min() <= 1)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
