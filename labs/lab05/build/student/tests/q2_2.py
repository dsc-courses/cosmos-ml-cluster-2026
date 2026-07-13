OK_FORMAT = True

test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> small_songs = pd.DataFrame([[0.0, 0.0], [0.1, 0.1], [0.2, 0.2], [0.9, 0.9]], columns=['a', 'b'])\n"
                                               ">>> labels = pd.Series(['rock', 'rock', 'classical', 'hip-hop'])\n"
                                               ">>> new_song = pd.Series([0.05, 0.05], index=['a', 'b'])\n"
                                               '>>> votes = neighbor_votes(new_song, small_songs, labels, 3)\n'
                                               ">>> bool(isinstance(votes, pd.Series) and votes.sum() == 3 and (votes.to_dict() == {'rock': 2, 'classical': 1}))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
