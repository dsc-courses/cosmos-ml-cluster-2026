OK_FORMAT = True

test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(time_transformer, FunctionTransformer))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(transformed_example.shape == (3, 7))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(list(transformed_example.columns[-2:]) == ['seconds_since_midnight', 'is_weekend'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(np.isclose(transformed_example.iloc[0]['seconds_since_midnight'], 64260))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
