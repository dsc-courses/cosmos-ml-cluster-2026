OK_FORMAT = True

test = {   'name': 'q2_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(better_model in {'1-NN', '5-NN', 'tie'})\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(better_model == '1-NN' and one_nn_accuracy > five_nn_accuracy or (better_model == '5-NN' and five_nn_accuracy > one_nn_accuracy) or "
                                               "(better_model == 'tie' and np.isclose(one_nn_accuracy, five_nn_accuracy)))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
