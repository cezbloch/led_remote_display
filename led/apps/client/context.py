from connection_provider import ConnectionProvider
from display import Display
from imaging.effect_provider import EffectProvider

class ApplicationContext(object):
    def __init__(self):
        self._connection_provider = ConnectionProvider()
        self._display = Display()
        self._effect_provider = EffectProvider()

    def get_connection_provider(self):
        return self._connection_provider

    def get_display(self):
        return self._display

    def get_effect_provider(self):
        return self._effect_provider
