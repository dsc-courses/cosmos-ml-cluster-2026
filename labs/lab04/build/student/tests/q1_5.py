OK_FORMAT = True

test = {   'name': 'q1_5',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(most_month, str) and isinstance(least_month, str))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> import numbers\n>>> bool(isinstance(difference_month, numbers.Integral))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(difference_month >= 0)\nTrue', 'failure_message': 'Subtract in the other order.', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(most_month == 'Feb')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(least_month == 'Jan')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(difference_month == 7)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
