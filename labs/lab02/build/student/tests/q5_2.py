OK_FORMAT = True

test = {   'name': 'q5_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(likes, np.ndarray))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(likes[0] == 'I like surfing')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(np.all(likes == np.array(['I like surfing', 'otters', 'and popcorn.'])))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
