OK_FORMAT = True

test = {   'name': 'q2_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> bool(feature_recipes_df.shape == (12, 3))\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(feature_recipes_df['sensor_columns'].map(lambda value: isinstance(value, list) and all((isinstance(column, str) for column in "
                                               'value))).all())\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> bool(len(feature_recipes) == 12)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> bool(set(feature_recipes['all_sensors']['sensor_columns']) == set(sensor_columns) and (not feature_recipes['all_sensors']['include_time']))\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bool('Light' not in feature_recipes['no_light_time']['sensor_columns'] and feature_recipes['no_light_time']['include_time'])\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
