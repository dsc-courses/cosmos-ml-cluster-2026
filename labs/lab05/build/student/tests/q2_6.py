OK_FORMAT = True

test = {   'name': 'q2_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(accuracy_by_k, pd.DataFrame) and accuracy_by_k.index.tolist() == [1, 3, 5, 9])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(accuracy_by_k.columns.tolist() == ['accuracy'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(((accuracy_by_k['accuracy'] >= 0) & (accuracy_by_k['accuracy'] <= 1)).all())\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(np.isclose(accuracy_by_k.loc[5, 'accuracy'], five_nn_accuracy))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
