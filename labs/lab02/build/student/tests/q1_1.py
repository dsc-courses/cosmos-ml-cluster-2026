OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> import numbers\n'
                                               '>>> bool(isinstance(scarecrow_debut, numbers.Integral) & isinstance(tin_man_debut, numbers.Integral) & isinstance(lion_debut, numbers.Integral))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(scarecrow_debut in range(1, 13) and tin_man_debut in range(1, 13) and (lion_debut in range(1, 13)))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(scarecrow_debut == 3)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(tin_man_debut == 5)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(lion_debut == 6)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
