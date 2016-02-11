from kivy.uix.settings import Settings
from client_facade.context import ApplicationContext

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
        self.__client = Context.get_connection_provider().get_client()
        self.__display = Context.get_display()
        self.__config = Context.get_settings_provider().get_config()

    def connect(self):
        ip_address = self.__config.get('connection', 'ip_address')
        port = self.__config.getint('connection', 'port_number')
        self.__client.callback = self.on_connected
        self.__client.errback = self.on_connect_failed
        self.__client.connect(ip_address, port)

    def on_connected(self, text):
        self._set_display_size()
        self._update_ui()

    def on_connect_failed(self, reason):
        self._update_ui()

    def disconnect(self):
        self.__client.disconnect()
        self._update_ui()

    def is_connected(self):
        return self.__client.is_connected()

    def _update_ui(self):
        connect_button = self.ids.connect_button
        disconnect_button = self.ids.disconnect_button
        connect_button.disabled = self.__client.is_connected()
        disconnect_button.disabled = not self.__client.is_connected()

    def _set_display_size(self):
        width = self.__config.getint('panel', 'width')
        height = self.__config.getint('panel', 'height')
        self.__display.set_size((width, height))
        self.__client.send_set_size(self.__display.get_size())
