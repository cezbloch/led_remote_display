from connection_provider import ConnectionProvider
from display import Display

class ApplicationContext(object):
    def __init__(self):
        self._connection_provider = ConnectionProvider()
        self._display = Display()

    def get_connection_provider(self):
        return self._connection_provider

    def get_display(self):
        return self._display
