OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(isinstance(steel_errors_by_k, pd.DataFrame) and steel_errors_by_k.index.tolist() == k_values)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(steel_errors_by_k.columns.tolist() == ['train_error', 'valid_error'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(np.allclose(steel_errors_by_k['valid_error'].to_numpy(), [0.6116838487972509, 0.570446735395189, 0.5498281786941581, 0.5395189003436427, "
                                               '0.5670103092783505, 0.6254295532646048, 0.6529209621993127]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
