from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from widgets.display_settings import DisplaySettings
from client_facade.context import ApplicationContext

from client_facade.settings_defines import *

#must be before .kv files imports
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')
Context = ApplicationContext.get_instance()

#.kv file requirements
from screens.text_effect_screen import TextEffectScreen
from screens.rainbow_effect_screen import RainbowEffectScreen
from screens.file_chooser_screen import FileChooserScreen
from screens.project_screen import ProjectScreen
from screens.main_screen import MainScreen
from screens.paint_effect_screen import PaintEffectScreen


class EffectScreenManager(ScreenManager):
    pass


class LedScreenManager(ScreenManager):
    pass


class LedApp(App):
    def __init__(self, **kwargs):
        super(LedApp, self).__init__(**kwargs)
        self.__context = kwargs['context']
        self.__settings_provider = self.__context.get_settings_provider()

    # called when building UI after config
    def build(self):
        self.use_kivy_settings = False
        self.settings_cls = DisplaySettings
        # settings are loaded only here
        self.__context.startup()
        return LedScreenManager()

    # called before UI is build
    def build_config(self, config):
        self.__settings_provider.set_config(config)
        self.__settings_provider.set_defaults()

    # called when opening settings
    def build_settings(self, settings):

        self.__settings_provider.add_display_connection_settings_panel(settings)

if __name__ == '__main__':
    LedApp(context=Context).run()
