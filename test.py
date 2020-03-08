# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
#
#
# class LoginScreen(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)
#
#
# class MyApp(App):
#
#     def build(self):
#         return LoginScreen()
#
#
# if __name__ == '__main__':
#     MyApp().run()

# from kivy.app import App
# from kivy.lang import Builder
#
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.settings import SettingsWithSidebar
#
# from settingsjson import settings_json
#
# Builder.load_string('''
# <Interface>:
#     orientation: 'vertical'
#     Button:
#         text: 'open the settings!'
#         font_size: 150
#         on_release: app.open_settings()
# ''')
#
#
# class Interface(BoxLayout):
#     pass
#
#
# class SettingsApp(App):
#     def build(self):
#         self.settings_cls = SettingsWithSidebar
#         self.use_kivy_settings = False
#         setting = self.config.get('example', 'boolexample')
#         return Interface()
#
#     def build_config(self, config):
#         config.setdefaults('example', {
#             'boolexample': True,
#             'numericexample': 10,
#             'optionsexample': 'option2',
#             'stringexample': 'some_string',
#             'pathexample': '/some/path'})
#
#     def build_settings(self, settings):
#         settings.add_json_panel('Panel Name',
#                                 self.config,
#                                 data=settings_json)
#
#     def on_config_change(self, config, section,
#                          key, value):
#         print(config, section, key, value)
#
#
# SettingsApp().run()

# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.widget import Widget
# from kivy.animation import Animation
# from kivy.core.window import Window
#
# from random import random
#
# Builder.load_string('''
# <Root>:
#     AnimRect:
#         pos: 500, 300
# <AnimRect>:
#     canvas:
#         Color:
#             rgba: 0, 1, 0, 1
#         Ellipse:
#             pos: self.pos
#             size: self.size
# ''')
#
#
# class Root(Widget):
#     pass
#
#
# class AnimRect(Widget):
#     def anim_to_random_pos(self):
#         Animation.cancel_all(self)
#         random_x = random() * (Window.width - self.width)
#         random_y = random() * (Window.height - self.height)
#         print('random point:', random_x, random_y)
#
#         anim = Animation(x=random_x,
#                          y=random_y,
#                          duration=0)
#                          # t='out_elastic')
#         anim.start(self)
#
#     def on_touch_down(self, touch):
#         if self.collide_point(*touch.pos):
#             self.anim_to_random_pos()
#             print('touched')
#
#
# class MainApp(App):
#     def build(self):
#         return Root()
#
#
# def test():
#     MainApp().run()
#
#
# if __name__ == '__main__':
#     test()

# '''
# Widget animation
# ================
#
# This example demonstrates creating and applying a multi-part animation to
# a button widget. You should see a button labelled 'plop' that will move with
# an animation when clicked.
# '''
#
# import kivy
# kivy.require('1.0.7')
#
# from kivy.animation import Animation
# from kivy.app import App
# from kivy.uix.button import Button
#
#
# class TestApp(App):
#
#     def animate(self, instance):
#         # create an animation object. This object could be stored
#         # and reused each call or reused across different widgets.
#         # += is a sequential step, while &= is in parallel
#         animation = Animation(pos=(100, 100), t='out_bounce')
#         animation += Animation(pos=(200, 100), t='out_bounce')
#         animation &= Animation(size=(500, 500))
#         animation += Animation(size=(100, 50))
#
#         # apply the animation on the button, passed in the "instance" argument
#         # Notice that default 'click' animation (changing the button
#         # color while the mouse is down) is unchanged.
#         animation.start(instance)
#
#     def build(self):
#         # create a button, and  attach animate() method as a on_press handler
#         button = Button(size_hint=(None, None), text='plop',
#                         on_press=self.animate)
#         return button
#
#
# if __name__ == '__main__':
#     TestApp().run()
