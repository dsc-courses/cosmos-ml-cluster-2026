OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(same_name_events, pd.DataFrame))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(same_name_events.shape == (2, 10))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool((same_name_events.iloc[0] == same_name_events.iloc[1]).sum() == 7)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
