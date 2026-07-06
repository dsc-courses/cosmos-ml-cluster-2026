OK_FORMAT = True

test = {   'name': 'q2_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(most_weeks_show, str))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(most_weeks_show in broadway.get('Show').unique())\nTrue",
                                       'failure_message': 'most_weeks_show should be the name of a show',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(most_weeks_show == 'The Phantom of the Opera')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
