#import logging
from message_unpacker import MessageUnpacker
from twisted.internet.protocol import Factory, Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import ReconnectingClientFactory


class LedServerProtocol(LineReceiver):
    #def __init__(self, device):
    #    self.__logger = logging.getLogger()

    def connectionMade(self):
        pass

    def dataReceived(self, data):
        #self.__logger.debug(__name__ + "data with size {0} received from {1}".format(len(data), self.transport.getPeer()))
        self.factory.message_unpacker.process_command(data)


class LedServerProtocolFactory(ReconnectingClientFactory):
    protocol = LedServerProtocol

    def __init__(self, message_unpacker):
        #self.__logger = logging.getLogger()
        self.message_unpacker = message_unpacker


class LedServer(object):
    def __init__(self, device):
        #self.__logger = logging.getLogger()
        self.__device = device
        self.__port = None

    def start(self, port=6666):
        #self.__logger.debug(__name__ + "starting server at port {0}".format(port))
        message_unpacker = MessageUnpacker(self.__device)
        from twisted.internet import reactor
        self.__port = reactor.listenTCP(port, LedServerProtocolFactory(message_unpacker))

    def close(self):
        #self.__logger.debug(__name__ + "stopping to listen")
        self.__port.stopListening()
