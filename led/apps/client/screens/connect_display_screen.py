from kivy.uix.screenmanager import Screen
from context import ApplicationContext
from kivy.lang import Builder
from os.path import join

Context = ApplicationContext.get_instance()

Builder.load_file(join('screens', 'connect_display_screen.kv'))

class ConnectDisplayScreen(Screen):
    def __init__(self, **kwargs):
        super(ConnectDisplayScreen, self).__init__(**kwargs)
        self._connection_provider = Context.get_connection_provider()
        self._display = Context.get_display()

    def connect(self):
        ip_address_text_input = self.ids['ip_address_text_input']
        port_text_input = self.ids['port_text_input']
        ip_address = ip_address_text_input.text
        port = int(port_text_input.text)
        self._connection_provider.connect(ip_address, port)
        self._set_display_size()
        self._update_ui()

    def disconnect(self):
        self._connection_provider.disconnect()
        self._update_ui()

    def _update_ui(self):
        connect_button = self.ids['connect_button']
        disconnect_button = self.ids['disconnect_button']
        connect_button.disabled = self._connection_provider.is_connected()
        disconnect_button.disabled = not self._connection_provider.is_connected()

    def _set_display_size(self):
        if self._connection_provider.is_connected():
            width_text_input = self.ids['width_text_input']
            height_text_input = self.ids['height_text_input']
            self._display.set_size((int(width_text_input.text), int(height_text_input.text)))
            self._connection_provider.get_client().send_set_size(self._display.get_size())