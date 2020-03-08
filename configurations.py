
import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'Training Wheels'},
    {'type': 'string',
     'title': 'Monkey Name',
     'desc': 'The name of the monkey being tested',
     'section': 'trainingwheels',
     'key': 'monkey_name'},
    {'type': 'path',
     'title': 'Icon',
     'desc': 'The icon to use',
     'section': 'trainingwheels',
     'key': 'icon'},
    {'type': 'numeric',
     'title': 'Clicks',
     'desc': 'The number of clicks to shrink the icon',
     'section': 'trainingwheels',
     'key': 'num_clicks'},
    {'type': 'numeric',
     'title': 'Delay',
     'desc': 'The number of seconds between trials',
     'section': 'trainingwheels',
     'key': 'delay'},
    {'type': 'numeric',
     'title': 'Initial Size',
     'desc': 'The initial size of the icon as a percentage of the screen size',
     'section': 'trainingwheels',
     'key': 'max_size'},
    {'type': 'numeric',
     'title': 'Smallest Size',
     'desc': 'The smallest size the icon can get before it moves around as a percentage of the screen size',
     'section': 'trainingwheels',
     'key': 'min_size'},
    {'type': 'bool',
     'title': 'Use Fail Audio',
     'desc': 'Use fail audio or don\'t',
     'section': 'trainingwheels',
     'key': 'use_fail_audio'},
    {'type': 'numeric',
     'title': 'Start Delay',
     'desc': 'Choose to delay the start by 30 seconds to allow for setup',
     'section': 'trainingwheels',
     'key': 'start_delay'},
    {'type': 'path',
     'title': 'Success Audio',
     'desc': 'The audio to use for success events',
     'section': 'trainingwheels',
     'key': 'success_audio_path'},
    {'type': 'path',
     'title': 'Failure Audio',
     'desc': 'The audio to use for failure events',
     'section': 'trainingwheels',
     'key': 'failure_audio_path'},
    {'type': 'path',
     'title': 'Results Folder',
     'desc': 'Folder to store results in',
     'section': 'trainingwheels',
     'key': 'results_path'}
])
