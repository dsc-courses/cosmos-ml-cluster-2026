OK_FORMAT = True

test = {   'name': 'q1_4',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> small_songs = pd.DataFrame([[0.0, 0.0, 0.0], [3.0, 4.0, 12.0]], columns=['a', 'b', 'c'], index=['first', 'second'])\n"
                                               ">>> new_song = pd.Series([0.0, 4.0, 12.0], index=['a', 'b', 'c'])\n"
                                               '>>> answer = distances_to_song(new_song, small_songs)\n'
                                               ">>> bool(isinstance(answer, pd.Series) and answer.index.tolist() == ['first', 'second'] and np.allclose(answer.to_numpy(), np.array([np.sqrt(160), "
                                               '3.0])))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
