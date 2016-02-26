import logging
from message_factory import MessageFactory
from twisted.internet.protocol import Protocol, ClientFactory


class LedClientProtocol(Protocol):
    def __init__(self):
        self.__logger = logging.getLogger()
        self.__logger.debug(__name__ + "Creating led protocol")

    def connectionMade(self):
        self.__logger.debug(__name__ + "Connection made with {0}".format(self.transport.getPeer()))
        self.factory.client.on_connection(self.transport)

    def dataReceived(self, data):
        self.__logger.debug(__name__ + "data with size {0} received from {1}".format(len(data), self.transport.getPeer()))
        self.factory.message_received(data)


class LedClientProtocolFactory(ClientFactory):
    protocol = LedClientProtocol

    def __init__(self, client):
        self.__logger = logging.getLogger()
        self.client = client

    def message_received(self, message):
        self.client.callback(message)

    def clientConnectionLost(self, conn, reason):
        self.__logger.error(__name__ + "connection lost")
        self.client.on_connection_lost("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.__logger.error(__name__ + "connection failed")
        self.client.on_connection_lost("connection failed")


class Client(object):
    def __init__(self, callback=None, errback=None):
        self.__logger = logging.getLogger()
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
        self.__logger.debug(__name__ + "disconnecting".format())
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
            self.connection.write('%d:%s,' % (len(message), message))

    def send_set_size(self, size):
        self.__logger.debug(__name__ + " sending size message {0}".format(size))
        command = MessageFactory.create_set_size_message(size)
        self.send_message(command)

    def send_image_frame(self, image):
        self.__logger.debug(__name__ + "sending image frame with size {0}".format(image.size))
        command = MessageFactory.create_display_frame_message(image)
        self.send_message(command)
