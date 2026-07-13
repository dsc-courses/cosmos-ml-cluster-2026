OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> small_songs = pd.DataFrame([[0.0, 0.0], [0.9, 0.9], [0.2, 0.2]], columns=['a', 'b'], index=['a', 'b', 'c'])\n"
                                               ">>> new_song = pd.Series([0.15, 0.15], index=['a', 'b'])\n"
                                               '>>> answer = nearest_song(new_song, small_songs)\n'
                                               ">>> bool(isinstance(answer, pd.Series) and answer.name == 'c' and np.allclose(answer.to_numpy(), np.array([0.2, 0.2])))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
