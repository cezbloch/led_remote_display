from connection_provider import ConnectionProvider
from display import Display
from imaging.effect_provider import EffectProvider
from logger_provider import LoggerProvider
from settings_provider import SettingsProvider
from settings_defines import *


class ApplicationContext(object):
    instance = None

    def __init__(self):
        self.__logger_provider = LoggerProvider()
        self.__connection_provider = ConnectionProvider()
        self.__display = Display()
        self.__effect_provider = EffectProvider()
        self.__settings_provider = SettingsProvider()

    @staticmethod
    def get_instance():
        if ApplicationContext.instance is None:
            ApplicationContext.instance = ApplicationContext()
        return ApplicationContext.instance

    def get_logger_provider(self):
        return self.__logger_provider

    def get_connection_provider(self):
        return self.__connection_provider

    def get_display(self):
        return self.__display

    def get_effect_provider(self):
        return self.__effect_provider

    def get_settings_provider(self):
        return self.__settings_provider

    def startup(self):
        self.__logger_provider.setup_logging()

        config = self.__settings_provider.get_config()
        reconnect_on_startup = config.getboolean(CONNECTION, RECONNECT_ON_STARTUP)
        if reconnect_on_startup:
            ip_address = config.get('connection', 'ip_address')
            port = config.getint('connection', 'port_number')
            use_fake_sockets = config.getboolean('connection', 'use_fake_sockets')
            self.__connection_provider.connect(address=ip_address, port=port, fake=use_fake_sockets)
            self._set_display_size()

    def _set_display_size(self):
        config = self.__settings_provider.get_config()
        if self.__connection_provider.is_connected():
            width = config.getint('panel', 'width')
            height = config.getint('panel', 'height')
            self.__display.set_size((width, height))
            self.__connection_provider.get_client().send_set_size(self.__display.get_size())