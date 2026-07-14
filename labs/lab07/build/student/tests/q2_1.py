OK_FORMAT = True

test = {   'name': 'q2_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(list(make_occupancy_features(X_train.head(), ['Light'], False).columns) == ['Light'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(list(make_occupancy_features(X_train.head(), ['Light'], True).columns) == ['Light', 'seconds_since_midnight', 'is_weekend'])\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(make_occupancy_features(pd.DataFrame({'date': ['2015-02-07 00:00:00', '2015-02-09 12:00:00'], 'Light': [0, 1]}), ['Light'], "
                                               "True)['seconds_since_midnight'].tolist() == [0, 43200])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(make_occupancy_features(pd.DataFrame({'date': ['2015-02-07 00:00:00', '2015-02-09 12:00:00'], 'Light': [0, 1]}), ['Light'], "
                                               "True)['is_weekend'].tolist() == [1, 0])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
