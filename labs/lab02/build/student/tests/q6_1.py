OK_FORMAT = True

test = {   'name': 'q6_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import numbers\n'
                                               '>>> bool(isinstance(enrolled_23, numbers.Integral) and isinstance(enrolled_24, numbers.Integral) and (enrolled_23 > enrolled_24))\n'
                                               'True',
                                       'failure_message': 'Make sure the order is correct!',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(int(enrolled_23 / enrolled_24 * 10 ** 3 % 10 ** 2) == 11)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(enrolled_23 == 482 and enrolled_24 == 218)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
