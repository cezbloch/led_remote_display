from networking.factories import ClientFactory


class ConnectionProvider(object):
    def __init__(self):
        self._isConnected = False
        self._client = None

    def is_connected(self):
        return self._isConnected

    def connect(self, **kwargs):
        if self.is_connected():
            self.disconnect()

        self._client = ClientFactory.create_and_connect_client(**kwargs)
        if self._client is not None:
            self._isConnected = True

    def get_client(self):
        return self._client

    def disconnect(self):
        self._isConnected = False
        if self._client is not None:
            self._client.close()
