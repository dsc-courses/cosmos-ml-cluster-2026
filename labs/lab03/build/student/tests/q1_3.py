OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> type(walmart_revenue) != str\nTrue', 'failure_message': 'It looks like your answer is still a string.', 'hidden': False, 'locked': False},
                                   {   'code': '>>> walmart_revenue != 611.29\nTrue',
                                       'failure_message': "Don't forget the data is given in billions of dollars, and you want dollars.",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> walmart_revenue == 611290000000\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
