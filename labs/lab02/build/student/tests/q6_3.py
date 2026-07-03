OK_FORMAT = True

test = {   'name': 'q6_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> bool(np.all(percent_majors_23 < 1) == False)\nTrue',
                                       'failure_message': 'Make sure to use percentages and not proportions!',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bool(round(percent_majors_23[0], 2) == percent_majors_23[0])\nTrue',
                                       'failure_message': 'Read the instructions carefully!',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(int(percent_majors_23[7] * 11 ** 3 % 10 ** 2) == 65)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(np.allclose(percent_majors_23, np.round(majors_23 / students_23 * 100, 2)))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
