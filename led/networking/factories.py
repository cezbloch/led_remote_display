from time import sleep
from led_client import LedClient
from message_unpacker import MessageUnpacker

from jsocket.jsocket_base import JsonClient
from led_server import LedServerThreaded
from mocked_jsocket import JsonClientMock


class ServerFactory(object):
    @staticmethod
    def create_server(device, **kwargs):
        message_unpacker = MessageUnpacker(device)
        server = LedServerThreaded(message_unpacker, **kwargs)
        server._set_timeout(10.0)
        server.start()
        return server

    @staticmethod
    def clean_up_server(server):
        server.stop()
        server.join()


class ClientFactory(object):
    @staticmethod
    def create_and_connect_client(**kwargs):
        use_fake_sockets = kwargs['fake']
        if use_fake_sockets:
            socket_client = JsonClientMock(**kwargs)
        else:
            address = kwargs['address']
            port = kwargs['port']
            sleep(1)
            socket_client = JsonClient(address, port)

        led_client = None

        if socket_client.connect():
            led_client = LedClient(socket_client)
        return led_client

