OK_FORMAT = True

test = {   'name': 'q5_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(by_comma, str) and isinstance(by_space, str))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(len(by_comma) == 36)\nTrue',
                                       'failure_message': 'You have the wrong length for by_comma. Make sure by_comma appears EXACTLY as described.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(by_comma == 'I like surfing, otters, and popcorn.' or by_comma == ', '.join(likes))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(by_space == 'I like surfing otters and popcorn.' or by_space == ' '.join(likes))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
