from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from widgets.display_settings import DisplaySettings
from context import ApplicationContext
from kivy.config import Config

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


class EffectScreenManager(ScreenManager):
    pass


class LedScreenManager(ScreenManager):
    pass


class LedApp(App):
    def __init__(self, **kwargs):
        super(LedApp, self).__init__(**kwargs)
        self.__settings_provider = Context.get_settings_provider()

    def build(self):
        self.use_kivy_settings = False
        self.settings_cls = DisplaySettings
        return LedScreenManager()

    def build_config(self, config):
        self.__settings_provider.set_config(config)
        self.__settings_provider.set_defaults()

    def build_settings(self, settings):
        self.__settings_provider.add_display_connection_settings_panel(settings)

if __name__ == '__main__':
    LedApp().run()
