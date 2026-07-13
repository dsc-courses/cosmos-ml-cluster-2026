OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> bool(features == ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(target == 'genre')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(isinstance(feature_songs, pd.DataFrame) and feature_songs.columns.tolist() == features and (feature_songs.shape[0] == songs.shape[0]))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
