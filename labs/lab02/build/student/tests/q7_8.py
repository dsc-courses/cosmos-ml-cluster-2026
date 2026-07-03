OK_FORMAT = True

test = {   'name': 'q7_8',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(ranked_seasons, np.ndarray))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> import numbers\n>>> bool(all((isinstance(season, numbers.Integral) for season in ranked_seasons)))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(len(ranked_seasons) == 31)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> bool(ranked_seasons[0] == 12 and ranked_seasons[1] == 10 or (ranked_seasons[0] == 10 and ranked_seasons[1] == 12))\nTrue',
                                       'failure_message': 'Try again!',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(np.allclose(ranked_seasons[8:12], np.array([27, 20, 23, 24])))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(ranked_seasons[-1] == 25)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
