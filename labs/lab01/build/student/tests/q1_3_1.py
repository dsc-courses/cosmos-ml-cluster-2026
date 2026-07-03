OK_FORMAT = True

test = {   'name': 'q1_3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(population_magnitudes) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(population_magnitudes) == 74\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(sum(abs(population_magnitudes - np.log10(population))) < 1e-06)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
