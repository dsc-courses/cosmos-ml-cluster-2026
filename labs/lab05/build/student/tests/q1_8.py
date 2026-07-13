OK_FORMAT = True

test = {   'name': 'q1_8',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> bool(isinstance(one_nn_results, pd.DataFrame) and set(one_nn_results.columns) == {'genre', 'predicted_genre', 'correct'})\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(one_nn_results.shape[0] == test_songs.shape[0] and one_nn_results['correct'].dtype == bool)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(np.isclose(one_nn_accuracy, one_nn_results['correct'].mean()))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
