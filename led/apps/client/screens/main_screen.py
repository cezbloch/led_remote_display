from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os.path import join

Builder.load_file(join('apps', 'client', 'screens', 'main_screen.kv'))


class MainScreen(Screen):
    def get_banner_path(self):
        return join('apps', 'client', 'resources', 'keesware_led_banner.gif')
