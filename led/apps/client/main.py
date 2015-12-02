from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config

#must be before .kv files imports
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')

#.kv file requirements
from screens.text_effect_screen import TextEffectScreen
from screens.rainbow_effect_screen import RainbowEffectScreen
from screens.connect_display_screen import ConnectDisplayScreen
from screens.file_chooser_screen import FileChooserScreen
from screens.project_screen import ProjectScreen
from screens.main_screen import MainScreen


class EffectScreenManager(ScreenManager):
    pass


class LedScreenManager(ScreenManager):
    pass


class LedApp(App):
    def build(self):
        return LedScreenManager()

if __name__ == '__main__':
    LedApp().run()
