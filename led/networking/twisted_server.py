import logging
from message_unpacker import MessageUnpacker
from twisted.internet.protocol import Factory
from twisted.protocols.basic import NetstringReceiver


class LedServerProtocol(NetstringReceiver):
    def __init__(self):
        self.__logger = logging.getLogger()
        self.__peer = None

    def connectionMade(self):
        self.__peer = self.transport.getPeer()
        self.__logger.info(__name__ + " connected to client {0}".format(self.__peer))

    def connectionLost(self, info):
        self.__logger.info(__name__ + " connection with client {0} lost".format(self.__peer))
        self.__peer = None

    def stringReceived(self, data):
        self.__logger.debug(__name__ + "data with size {0} received from {1}".format(len(data), self.transport.getPeer()))
        self.factory.message_unpacker.process_command(data)


class LedServerProtocolFactory(Factory):
    protocol = LedServerProtocol

    def __init__(self, message_unpacker):
        self.__logger = logging.getLogger()
        self.message_unpacker = message_unpacker

    def clientConnectionLost(self, conn, reason):
        self.__logger.error(__name__ + " connection with client lost".format())

    def clientConnectionFailed(self, conn, reason):
        self.__logger.error(__name__ + " connection with client failed".format())


class LedServer(object):
    def __init__(self, device):
        self.__logger = logging.getLogger()
        self.__logger.info(__name__ + " Creating server instance".format())
        self.__device = device
        self.__port = None

    def start(self, port=6666):
        self.__logger.info(__name__ + " server is starting to listen at port {0}".format(port))
        message_unpacker = MessageUnpacker(self.__device)
        from twisted.internet import reactor
        self.__port = reactor.listenTCP(port, LedServerProtocolFactory(message_unpacker))
        self.__logger.info(__name__ + " server is listening at {0}".format(self.__port.getHost()))

    def close(self):
        self.__logger.info(__name__ + " server is stopping to listen from {0}".format(self.__port.getHost()))
        self.__port.stopListening()
