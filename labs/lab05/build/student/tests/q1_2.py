OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(songs_per_genre, pd.Series))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(songs_per_genre.index.tolist() == ['classical', 'hip-hop', 'rock'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(songs_per_genre.sum() == training_songs.shape[0])\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
