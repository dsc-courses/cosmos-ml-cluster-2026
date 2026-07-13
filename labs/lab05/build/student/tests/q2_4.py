OK_FORMAT = True

test = {   'name': 'q2_4',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(five_nn_predictions, pd.Series) and five_nn_predictions.index.equals(test_songs.index))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(isinstance(five_nn_results, pd.DataFrame) and set(five_nn_results.columns) == {'genre', 'predicted_genre', 'correct'})\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(np.isclose(five_nn_accuracy, five_nn_results['correct'].mean()))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
