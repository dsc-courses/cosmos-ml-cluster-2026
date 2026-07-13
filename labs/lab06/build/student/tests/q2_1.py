OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(steel_features == [column for column in steel.columns if column not in ['id', 'fault_type']])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool((len(X_steel_train), len(X_steel_valid), len(X_steel_test)) == (873, 291, 291))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(set(X_steel_train.index).isdisjoint(X_steel_valid.index) and set(X_steel_train.index).isdisjoint(X_steel_test.index) and '
                                               'set(X_steel_valid.index).isdisjoint(X_steel_test.index))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(X_steel_train.index.equals(y_steel_train.index) and X_steel_valid.index.equals(y_steel_valid.index) and '
                                               'X_steel_test.index.equals(y_steel_test.index))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
