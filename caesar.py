# kivy.require('1.0.6')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import subprocess
import time

from configurations import settings_json


class MainApp(App):

    def build(self):
        global start_delay_time
        start_delay_time = self.config.get('trainingwheels', 'start_delay')
        return Interface()

    def build_config(self, config):
        config.setdefaults('trainingwheels', {
            'monkey_name': 'Daisy',
            'icon': '/',
            'num_clicks': 1,
            'delay': 0,
            'max_size': 100,
            'min_size': 30,
            'use_fail_audio': True,
            'start_delay': 0,
            'success_audio_path': '/',
            'failure_audio_path': '/',
            'results_path': '/'
        })

    def build_settings(self, settings):
        settings.add_json_panel('Training Wheels',
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section, key, value):
        global start_delay_time
        start_delay_time = self.config.get('trainingwheels', 'start_delay')


class Interface(BoxLayout):

    def call_paint_app(self):
        retval = subprocess.run(['python3', 'paint.py'])
        print(retval)
        if retval.returncode != 0:
            print('App did not run successfully')
        if retval.returncode == 0:
            print('App closed')

    def call_training_wheels_app(self):

        # Start Delay handling is a bit wonky
        time.sleep(int(start_delay_time))

        retval = subprocess.run(['python3', './apps/trainingwheels.py'])
        print(retval)
        if retval.returncode != 0:
            print('App did not run successfully')
        if retval.returncode == 0:
            print('App closed')


class TrainingWheelsApp(App):

    def build(self):
        return Label()


interface = Builder.load_file('caesar.kv')


def main():

    caesar = MainApp()

    caesar.run()


if __name__ == '__main__':
    main()
