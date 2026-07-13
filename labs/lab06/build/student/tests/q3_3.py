OK_FORMAT = True

test = {   'name': 'q3_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> bool(isinstance(scaled_steel_errors_by_k, pd.DataFrame) and scaled_steel_errors_by_k.index.tolist() == k_values)\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> bool(scaled_steel_errors_by_k.columns.tolist() == ['train_error', 'valid_error'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(np.allclose(scaled_steel_errors_by_k['valid_error'].to_numpy(), [0.3298969072164948, 0.28865979381443296, 0.2852233676975945, "
                                               '0.3161512027491409, 0.4054982817869416, 0.49828178694158076, 0.6529209621993127]))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(best_scaled_steel_k == 15)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> bool(steel_scaling_comparison.columns.tolist() == ['raw features', 'standardized features'])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
