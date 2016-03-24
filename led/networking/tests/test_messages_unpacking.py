import unittest

from networking.message_factory import *
from networking.message_unpacker import *
from networking.tests.mock_led_device import *


class TestMessageUnpacking(unittest.TestCase):
    def setUp(self):
        self.device = MockLedDevice()
        self.unpacker = MessageUnpacker(self.device)

    def test_unpack_set_size_message(self):
        size = (1920, 1080)
        set_size_message = MessageFactory.create_set_size_message(size)

        self.unpacker.process_command(set_size_message)

        self.assertEqual(self.device.size, size)

    def test_unpack_image_message(self):
        size = (8, 8)
        color_green = (0, 255, 0)
        image = ImageFactory.generate_gradient_image(size, color_green)
        image_frame_message = MessageFactory.create_display_frame_message(image)

        self.unpacker.process_command(image_frame_message)

        self.assertEqual(self.device.image, image)

