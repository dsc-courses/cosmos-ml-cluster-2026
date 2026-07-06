OK_FORMAT = True

test = {   'name': 'q2_7',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(isinstance(theatre_proportions, pd.DataFrame) and set(theatre_proportions.columns) == {'Proportion'})\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(np.isclose(theatre_proportions.get('Proportion').sum(), 1))\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(theatre_proportions.index[1] == 'Minskoff Theatre')\nTrue",
                                       'failure_message': 'Tests that the DataFrame is sorted.',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(np.isclose(theatre_proportions.get('Proportion').loc['Gershwin Theatre'], 0.03276820328517201))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
