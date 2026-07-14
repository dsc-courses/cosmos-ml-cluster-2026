OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(list(occupancy_rates.index) == [0, 1])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.isclose(occupancy_rates.sum(), 1))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.isclose(occupancy_rates.loc[1], 0.2123296082524868))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.isclose(majority_baseline, occupancy_rates.loc[0]))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
