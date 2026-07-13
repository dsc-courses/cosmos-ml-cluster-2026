OK_FORMAT = True

test = {   'name': 'q1_9',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(isinstance(one_nn_mistakes, pd.DataFrame) and (~one_nn_mistakes['correct']).all())\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(one_nn_num_mistakes == one_nn_mistakes.shape[0])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(one_nn_num_mistakes + one_nn_results['correct'].sum() == test_songs.shape[0])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
