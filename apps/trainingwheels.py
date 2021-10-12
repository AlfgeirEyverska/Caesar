from kivy.app import App
from kivy.lang import Builder
from kivy.config import ConfigParser
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

from datetime import datetime
from random import random
from os import path

import requests

# import dispenser
# import multiprocessing as mp

# dispenser setup

# tw_dispenser_q = mp.Queue()

# tw_dispenser_process = mp.Process(target=dispenser.thread_dispenser, args=(tw_dispenser_q,))
# tw_dispenser_process.start()

# Load in the configuration options set from the main app
# TODO: Figure out how to load settings upon use, not load
#   Consider moving it and its dependents into the run function
tw_config = ConfigParser()
tw_config.read('main.ini')

caesar_config = dict(tw_config.items('trainingwheels'))
print(caesar_config)

# Success audio setup
if path.exists(caesar_config['success_audio_path']):
    print(caesar_config['success_audio_path'])
    success_sound = SoundLoader.load(caesar_config['success_audio_path'])
    if success_sound:
        print('woohoo, success sound')
    else:
        print('doh, no sound')

# Failure audio setup
if path.exists(caesar_config['failure_audio_path']):
    print(caesar_config['failure_audio_path'])
    failure_sound = SoundLoader.load(caesar_config['failure_audio_path'])
    if failure_sound:
        print('woohoo, failure sound')
    else:
        print('doh, no sound')

# max size setup
max_size = Window.width if Window.height > Window.width else Window.height
max_size = max_size * float(caesar_config['max_size']) / 100.0
print(f'Maximum size: {float(caesar_config["max_size"])}% - {max_size}')

# min size setup
min_size = Window.width if Window.height > Window.width else Window.height
min_size = min_size * float(caesar_config['min_size']) / 100.0
print(f'Minimum size: {float(caesar_config["min_size"])}% - {min_size}')

print(f'Window width - {Window.width}\nWindow height - {Window.height}')

# markup
Builder.load_string(f'''
<Root>:
    Target:
        pos: (root.center_x - self.width/2.), (root.center_y - self.height/2.)
        size_hint_x: None
        size_hint_y: None
        width: {max_size}
        height: {max_size}
<Target>:
    canvas:
        Color:
            rgba: 0.7, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')

# Initiate timing
start_time = datetime.now()

# Create log file name based off of the current date and time
log_file_name = f'{caesar_config["results_path"]}/{caesar_config["monkey_name"]}_{start_time.date()}_{start_time.hour}-{start_time.minute}-{start_time.second}.log'


# log: monkey, stimulus,
def log_event(event_data):
    try:
        log_file = open(log_file_name, 'a')
    except FileNotFoundError:
        log_file = open(log_file_name, 'x')

    print(event_data)
    log_file.write(str(event_data) + '\n')
    log_file.close()


# TODO: update to use actual api address
def post_event(event_data):
    response = requests.post('http://127.0.0.1:3000/api/sessions/5', data=event_data)
    print(response.content)


class Root(Widget):
    pass


class Target(Widget):

    def shrink(self):
        print('shrinking')
        self.width -= 30
        self.height -= 30

    def random_movement(self):
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)
        random_y = random() * (Window.height - self.height)
        print('random point:', random_x, random_y)

        anim = Animation(x=random_x,
                         y=random_y,
                         duration=1,
                         t='out_elastic')
        anim.start(self)

    def on_touch_down(self, touch):

        rn = datetime.now()
        hit = 0

        if self.collide_point(*touch.pos):
            # TODO: investigate laggy audio
            success_sound.play()

            # dispense
            # tw_dispenser_q.put(1)

            if self.width > min_size:
                self.shrink()
            else:
                self.random_movement()
            print('touched')
            # NOTE: I am using center x and center y, not the bottom left corner like in the calculation
            hit = 1
        else:
            failure_sound.play()
            hit = 0

        event_data = {'hit': hit,
                      'radius': self.width / 2.0,
                      'position': f'{self.center_x}, {self.center_y}',
                      'time': str(rn.time()),
                      'hitMarker': f'{touch.pos[0]}, {touch.pos[1]}',
                      'session': 5}
        log_event(event_data)
        post_event(event_data)


class MainApp(App):
    def build(self):
        return Root()

    def __del__(self):
        # tw_dispenser_q.put('poison pill')
        # print('Poisoned')
        # tw_dispenser_process.join(timeout=1.)
        print('Closing thread')


def tw():
    MainApp().run()


if __name__ == '__main__':
    tw()
