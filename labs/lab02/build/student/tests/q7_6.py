OK_FORMAT = True

test = {   'name': 'q7_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(decid_and_conif, float) and 0 <= decid_and_conif <= 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(decid_and_conif * 10 ** 3 % 10 ** 2 * 10) == 271)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.isclose(decid_and_conif, 0.22714681440443213) or np.isclose(decid_and_conif, 0.22222222222222))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
