from kivy.support import install_twisted_reactor
install_twisted_reactor()

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')

from client_facade.context import ApplicationContext
from apps.client.widgets.display_settings import DisplaySettings

from kivy.app import App

from kivy.uix.screenmanager import ScreenManager

Context = ApplicationContext.get_instance()


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
        #settings are loaded only here
        self.__context.startup()
        return LedScreenManager()

    #called before UI is build
    def build_config(self, config):
        self.__settings_provider.set_config(config)
        self.__settings_provider.set_defaults()

    # called when opening settings
    def build_settings(self, settings):

        self.__settings_provider.add_display_connection_settings_panel(settings)

if __name__ == '__main__':
    LedApp(context=Context).run()
