from message_factory import MessageFactory
from twisted.internet.protocol import Protocol, ClientFactory


class LedClientProtocol(Protocol):
    def connectionMade(self):
        self.factory.client.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.message_received(data)


class LedClientProtocolFactory(ClientFactory):
    protocol = LedClientProtocol

    def __init__(self, client):
        self.client = client

    def message_received(self, message):
        self.client.callback(message)

    def clientConnectionLost(self, conn, reason):
        self.client.on_connection_lost("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.client.on_connection_lost("connection failed")


class Client(object):
    def __init__(self, callback=None, errback=None):
        self.connection = None
        self.connector = None
        self.callback = callback
        self.errback = errback

    def is_connected(self):
        return self.connection is not None

    def connect(self, address='localhost', port=8000):
        from twisted.internet import reactor
        self.connector = reactor.connectTCP(address, port, LedClientProtocolFactory(self))

    def disconnect(self):
        self.connector.disconnect()
        self.on_connection_lost("disconnected requested by client")

    def on_connection(self, connection):
        self.connection = connection
        if self.callback is not None:
            self.callback("connected to server :)")

    def on_connection_lost(self, reason):
        self.connection = None
        if self.errback is not None:
            self.errback(reason)

    def send_message(self, message):
        if self.connection and message:
            self.connection.write(message)

    def send_set_size(self, size):
        command = MessageFactory.create_set_size_message(size)
        self.send_message(command)

    def send_image_frame(self, image):
        command = MessageFactory.create_display_frame_message(image)
        self.send_message(command)
