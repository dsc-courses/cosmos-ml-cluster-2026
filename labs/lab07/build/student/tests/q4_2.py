OK_FORMAT = True

test = {   'name': 'q4_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> bool(len(frozen_choices) == 3 and set(frozen_choices['model']) == set(model_specs))\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> bool(set(frozen_searches) == set(model_specs))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(all((search is searches[frozen_choices.set_index('model').loc[name, 'recipe'], name] for name, search in frozen_searches.items())))\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool(np.allclose(frozen_choices.set_index('model')['cv_accuracy'].sort_index(), cv_results.groupby('model')['cv_accuracy'].max().sort_index()))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
