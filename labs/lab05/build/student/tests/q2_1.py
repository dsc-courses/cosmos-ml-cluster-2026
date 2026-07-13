OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> small_songs = pd.DataFrame([[0.0, 0.0], [0.4, 0.4], [0.8, 0.8]], columns=['a', 'b'], index=['a', 'b', 'c'])\n"
                                               ">>> new_song = pd.Series([0.3, 0.3], index=['a', 'b'])\n"
                                               '>>> answer = k_nearest_songs(new_song, small_songs, 2)\n'
                                               ">>> bool(isinstance(answer, pd.DataFrame) and answer.shape[0] == 2 and ('distance' in answer.columns) and (answer.index.tolist() == ['b', 'a']) and "
                                               "answer['distance'].is_monotonic_increasing)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
