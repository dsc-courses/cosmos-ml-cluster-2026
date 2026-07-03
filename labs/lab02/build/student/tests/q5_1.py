OK_FORMAT = True

test = {   'name': 'q5_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(quirky_numbers, np.ndarray) and len(quirky_numbers) == 5)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(quirky_numbers[0] * 10 ** 4 % 10 ** 3) == 853)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(quirky_numbers[1] * 10 ** 3 % 10 ** 3) == 575)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(quirky_numbers[2] * 10 % 10 ** 3) == 66)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(quirky_numbers[3] * 10 ** 3 % 10 ** 3) == 388)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(int(quirky_numbers[4] * 10 ** 3 % 10 ** 3) == 944)\nTrue', 'failure_message': 'Try again!', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(np.allclose(quirky_numbers, np.array([np.sqrt(67), np.radians(33), (3 ** 4 + 9 ** 4) / 1000, np.e / 7, np.log10(88)])))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
