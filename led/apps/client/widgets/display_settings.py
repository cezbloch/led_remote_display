from kivy.uix.settings import Settings
from kivy.config import Config
from context import ApplicationContext

Context = ApplicationContext.get_instance()

from kivy.lang import Builder

Builder.load_string("""
<DisplaySettings>
    orientation: 'vertical'
    BoxLayout:
        size_hint: 1, 0.1
        orientation: 'horizontal'
        AutoTextSizeButton:
            id: connect_button
            text: "Connect"
            on_release: root.connect()
            disabled: False
        AutoTextSizeButton:
            id: disconnect_button
            text: "Disconnect"
            on_release: root.disconnect()
            disabled: True
""")


class DisplaySettings(Settings):
    def __init__(self, **kwargs):
        super(DisplaySettings, self).__init__(**kwargs)
        self._connection_provider = Context.get_connection_provider()
        self._display = Context.get_display()
        self.__config = Context.get_settings_provider().get_config()

    def connect(self):
        ip_address = self.__config.get('connection', 'ip_address')
        port = self.__config.getint('connection', 'port_number')
        self._connection_provider.connect(ip_address, port)
        self._set_display_size()
        self._update_ui()

    def disconnect(self):
        self._connection_provider.disconnect()
        self._update_ui()

    def is_connected(self):
        if self._connection_provider is None:
            return False
        is_connected = self._connection_provider.is_connected()
        if is_connected is not None:
            return is_connected
        return False

    def _update_ui(self):
        connect_button = self.ids.connect_button
        disconnect_button = self.ids.disconnect_button
        connect_button.disabled = self._connection_provider.is_connected()
        disconnect_button.disabled = not self._connection_provider.is_connected()

    def _set_display_size(self):
        if self._connection_provider.is_connected():
            width = self.__config.getint('panel', 'width')
            height = self.__config.getint('panel', 'height')
            self._display.set_size((width, height))
            self._connection_provider.get_client().send_set_size(self._display.get_size())
