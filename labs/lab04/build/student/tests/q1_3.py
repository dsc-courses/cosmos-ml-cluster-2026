OK_FORMAT = True

test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(chamber_music, pd.DataFrame))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(chamber_music.shape[0] == 4)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(np.all((chamber_music.get('Category') == 'Chamber Music') | (chamber_music.get('Category') == 'Chamber Music*')))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
