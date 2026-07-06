OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(broadway.shape[1] == 7)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool('AvgTicket' in broadway.columns)\nTrue",
                                       'failure_message': 'Check capitalization and spelling of your column name.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(np.all(broadway.get('AvgTicket') == broadway.get('Weekly Gross') / broadway.get('Seats Sold')))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
