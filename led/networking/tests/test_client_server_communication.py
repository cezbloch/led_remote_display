import time
import unittest

from imaging.image_factory import ImageFactory

from networking.factories import ServerFactory, ClientFactory
from networking.tests.mock_led_device import MockLedDevice


class TestClientServerLocalCommunication(unittest.TestCase):
    def setUp(self):
        self.device = MockLedDevice()
        self.server = ServerFactory.create_server(self.device, address='localhost', port=4567)
        self.client = ClientFactory.create_and_connect_client(address='localhost', port=4567, fake=False)

    def tearDown(self):
        self.client.close()
        self.server.close()

    def test_send_set_size_from_client_to_server(self):
        display_size = (8, 8)

        self.client.send_set_size(display_size)
        time.sleep(2)

        self.assertEqual(self.device.size, display_size)

    def test_send_image_frame_from_client_to_server(self):
        size = (6, 9)
        color = (0, 255, 0)
        image = ImageFactory.generate_gradient_image(size, color)

        self.client.send_image_frame(image)
        time.sleep(2)

        self.assertEqual(self.device.image, image)

