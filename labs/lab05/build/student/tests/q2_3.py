OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> small_songs = pd.DataFrame([[0.0, 0.0], [0.1, 0.1], [0.2, 0.2], [0.9, 0.9], [0.8, 0.8]], columns=['a', 'b'])\n"
                                               ">>> labels = pd.Series(['rock', 'rock', 'classical', 'hip-hop', 'hip-hop'])\n"
                                               ">>> new_song = pd.Series([0.05, 0.05], index=['a', 'b'])\n"
                                               ">>> bool(predict_knn(new_song, small_songs, labels, 3) == 'rock')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> tie_songs = pd.DataFrame([[0.0, 0.0], [0.1, 0.1], [0.2, 0.2], [0.3, 0.3]], columns=['a', 'b'])\n"
                                               ">>> labels = pd.Series(['rock', 'hip-hop', 'rock', 'hip-hop'])\n"
                                               ">>> new_song = pd.Series([0.05, 0.05], index=['a', 'b'])\n"
                                               ">>> bool(predict_knn(new_song, tie_songs, labels, 4) == 'hip-hop')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
