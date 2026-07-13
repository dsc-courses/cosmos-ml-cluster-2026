OK_FORMAT = True

test = {   'name': 'q1_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(best_spotify_k == 5)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(isinstance(final_spotify_model, KNeighborsClassifier) and final_spotify_model.n_neighbors == best_spotify_k)\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(np.isclose(spotify_test_error, 0.1625))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
