from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import join

#for kv file
from ui.auto_size_button import AutoTextSizeButton

Builder.load_file(join('screens', 'main_screen.kv'))


class MainScreen(Screen):
    pass
