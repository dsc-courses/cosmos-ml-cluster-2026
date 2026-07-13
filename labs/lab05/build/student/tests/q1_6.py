OK_FORMAT = True

test = {   'name': 'q1_6',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> small_songs = pd.DataFrame([[0.02, 0.9], [0.7, 0.02], [0.3, 0.1]], columns=['a', 'b'])\n"
                                               ">>> labels = pd.Series(['classical', 'hip-hop', 'rock'])\n"
                                               ">>> new_song = pd.Series([0.65, 0.05], index=['a', 'b'])\n"
                                               '>>> first_prediction = predict_1nn(new_song, small_songs, labels)\n'
                                               ">>> new_song = pd.Series([0.04, 0.8], index=['a', 'b'])\n"
                                               '>>> second_prediction = predict_1nn(new_song, small_songs, labels)\n'
                                               ">>> bool(first_prediction == 'hip-hop' and second_prediction == 'classical')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
