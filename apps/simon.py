import kivy

from random import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Line

Builder.load_string('''
<BackgroundColor@Widget>
    background_color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos

<BackgroundLabel@Label+BackgroundColor>
    background_color: 0, 0, 0, 0

Interface:
    GridLayout:
        BackgroundLabel
            id: green_label
            text: 'green'
            background_color: [0, 1, 0, 1]
        BackgroundLabel
            id: red_label
            text: 'red'
            background_color: [1, 0, 0, 1]
        BackgroundLabel
            id: yellow_label
            text: 'yellow'
            background_color: [0, 1, 1, 1]
        BackgroundLabel
            id: blue_label
            text: 'blue'
            background_color: [0, 0, 1, 1]
''')


class Interface(GridLayout):
    pass


class SimonApp(App):

    def build(self):
        return Interface()


def simon():
    SimonApp().run()


if __name__ == '__main__':
    simon()
