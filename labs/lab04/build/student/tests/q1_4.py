OK_FORMAT = True

test = {   'name': 'q1_4',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(isinstance(month_of_year('18-Feb-25'), str))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(month_of_year('18-Feb-25').isalpha())\nTrue",
                                       'failure_message': 'Make sure to exclude the year and day from your answer!',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(len(month_of_year('18-Feb-25')) == 3)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(month_of_year('25-Apr-25') == 'Apr')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(month_of_year('5-Mar-25') == 'Mar')\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
