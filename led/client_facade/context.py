from connection_provider import ConnectionProvider
from display import Display
from imaging.effect_provider import EffectProvider
from settings_provider import SettingsProvider
from settings_defines import *


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

    def startup(self):
        config = self._settings_provider.get_config()
        reconnect_on_startup = config.getboolean(CONNECTION, RECONNECT_ON_STARTUP)
        if reconnect_on_startup:
            ip_address = config.get('connection', 'ip_address')
            port = config.getint('connection', 'port_number')
            self._connection_provider.connect(ip_address, port)
            self._set_display_size()

    def _set_display_size(self):
        config = self._settings_provider.get_config()
        if self._connection_provider.is_connected():
            width = config.getint('panel', 'width')
            height = config.getint('panel', 'height')
            self._display.set_size((width, height))
            self._connection_provider.get_client().send_set_size(self._display.get_size())