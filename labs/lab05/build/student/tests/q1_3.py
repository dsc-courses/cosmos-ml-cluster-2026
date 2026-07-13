OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> song_a = pd.Series([0.0, 0.0, 0.0])\n>>> song_b = pd.Series([3.0, 4.0, 12.0])\n>>> bool(np.isclose(distance(song_a, song_b), 13.0))\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> song_a = pd.Series([1.0, 2.0])\n>>> song_b = pd.Series([4.0, 6.0])\n>>> bool(np.isclose(distance(song_a, song_b), 5.0))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
