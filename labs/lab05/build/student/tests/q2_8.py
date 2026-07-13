OK_FORMAT = True

test = {   'name': 'q2_8',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(isinstance(five_nn_by_genre, pd.DataFrame) and five_nn_by_genre.columns.tolist() == ['accuracy'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(five_nn_by_genre.index.tolist() == ['classical', 'hip-hop', 'rock'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(hardest_genre in five_nn_by_genre.index and np.isclose(five_nn_by_genre.loc[hardest_genre, 'accuracy'], five_nn_by_genre['accuracy'].min()))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
