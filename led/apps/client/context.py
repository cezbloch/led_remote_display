from connection_provider import ConnectionProvider
from display import Display
from settings_provider import SettingsProvider
from imaging.effect_provider import EffectProvider


class ApplicationContext(object):
    instance = None

    def __init__(self):
        self._connection_provider = ConnectionProvider()
        self._display = Display()
        self._effect_provider = EffectProvider()
        self._settings_provider = SettingsProvider()

    @staticmethod
    def get_instance():
        if ApplicationContext.instance is None:
            ApplicationContext.instance = ApplicationContext()
        return ApplicationContext.instance

    def get_connection_provider(self):
        return self._connection_provider

    def get_display(self):
        return self._display

    def get_effect_provider(self):
        return self._effect_provider

    def get_settings_provider(self):
        return self._settings_provider
