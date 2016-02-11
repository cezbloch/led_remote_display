from networking.twisted_client import Client


class ConnectionProvider(object):
    def __init__(self):
        self.__client = Client()

    def is_connected(self):
        return self.__client.is_connected()

    def connect(self, **kwargs):
        if self.is_connected():
            self.disconnect()

        address = kwargs['address']
        port = kwargs['port']

        self.__client.connect(address, port)

    def get_client(self):
        return self.__client

    def disconnect(self):
        self.__client.disconnect()
