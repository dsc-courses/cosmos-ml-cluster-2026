OK_FORMAT = True

test = {   'name': 'q4_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(0 < dissimilarity < 100)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(dissimilarity ** 0.5 * 10 ** 6 % 10 ** 5) == 45751)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> import numpy as np\n>>> bool(np.isclose(dissimilarity, 7))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
