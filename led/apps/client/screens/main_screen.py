from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import join

Builder.load_file(join('screens', 'main_screen.kv'))


class MainScreen(Screen):
    pass
