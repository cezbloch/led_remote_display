import time
import unittest

from imaging.image_factory import ImageFactory

from networking.twisted_server import LedServer
from networking.twisted_client import Client
from networking.tests.mock_led_device import MockLedDevice
from twisted.internet import reactor

class MockApplication(object):
    def __init__(self):
        self.errors = []
        self.messages = []

    def on_error(self, error):
        self.errors.append(error)

    def on_message_received(self, message):
        self.messages.append(message)

class TestClientServerLocalCommunication(unittest.TestCase):
    def setUp(self):
        self.device = MockLedDevice()
        self.server = LedServer(self.device)
        self.port = 4567
        self.server.start(self.port)
        self.app = MockApplication()
        self.client = Client(self.app.on_message_received, self.app.on_error)
        self.client.connect('localhost', self.port)
        reactor.callLater(5, self.clean_up)

    def clean_up(self):
        self.client.disconnect()
        self.server.close()

        reactor.stop()

    def test_send_set_size_from_client_to_server(self):
        display_size = (8, 8)

        reactor.callLater(1, self.client.send_set_size, display_size)
        reactor.run()

        self.assertEqual(self.device.size, display_size)

    def test_send_image_frame_from_client_to_server(self):
        size = (6, 9)
        color = (0, 255, 0)
        image = ImageFactory.generate_gradient_image(size, color)

        reactor.callLater(1, self.client.send_image_frame, image)
        reactor.run()

        self.assertEqual(self.device.image, image)
