import json


class SettingsProvider(object):
    def __init__(self):
        self.__config = None

    def set_config(self, config):
        self.__config = config

    def get_config(self):
        return self.__config

    def set_defaults(self):
        self.__config.setdefaults('connection', {
            'reconnect_on_startup': True,
            'ip_address': '127.0.0.1',
            'port_number': 6666})
        self.__config.setdefaults('panel', {
            'width': 30,
            'height': 10})
        self.__config.setdefaults('rainbow', {
            'reconnect_on_startup': False,
            'ip_address': 'local_machine'})

    def add_display_connection_settings_panel(self, settings):
        settings_json = json.dumps([
            {'type': 'bool',
             'title': 'Reconnect on startup',
             'section': 'connection',
             'key': 'reconnect_on_startup'},

            {'type': 'string',
             'title': 'IP address',
             'desc': 'address of LED device',
             'section': 'connection',
             'key': 'ip_address'},

            {'type': 'numeric',
             'title': 'Port number',
             'desc': 'port number of the LED device',
             'section': 'connection',
             'key': 'port_number'},

            {'type': 'numeric',
             'title': 'Panel Width',
             'section': 'panel',
             'key': 'width'},

            {'type': 'numeric',
             'title': 'Panel Height',
             'section': 'panel',
             'key': 'height'}])

        settings.add_json_panel('Display Connection', self.__config, data=settings_json)
