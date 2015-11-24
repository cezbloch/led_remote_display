import unittest

from imaging.image_factory import ImageFactory
from networking.message_factory import *


class TestMessageFactory(unittest.TestCase):
    def test_create_set_size_message(self):
        size = (44, 66)

        message = MessageFactory.create_set_size_message(size)

        self.assertEqual(message, '{"command": {"set_size": {"width": 44, "height": 66}}}')

    def test_create_red_image_frame_message(self):
        size = (8, 8)
        color = (255, 0, 0)
        image = ImageFactory.generate_gradient_image(size, color)

        message = MessageFactory.create_display_frame_message(image)

        self.assertEqual(message, '{"command": {"display_frame": {"mode": "RGB", "pixels": "AAAAHwAAPwAAXwAAfwAAnwAAvwAA3wAAAAAAHwAAPwAAXwAAfwAAnwAAvwAA3wAAAAAAHwAAPwAA\\nXwAAfwAAnwAAvwAA3wAAAAAAHwAAPwAAXwAAfwAAnwAAvwAA3wAAAAAAHwAAPwAAXwAAfwAAnwAA\\nvwAA3wAAAAAAHwAAPwAAXwAAfwAAnwAAvwAA3wAAAAAAHwAAPwAAXwAAfwAAnwAAvwAA3wAAAAAA\\nHwAAPwAAXwAAfwAAnwAAvwAA3wAA\\n", "size": [8, 8]}}}')

    def test_create_green_gradient_image_frame_message(self):
        size = (10, 2)
        color = (0, 255, 0)
        image = ImageFactory.generate_gradient_image(size, color)

        message = MessageFactory.create_display_frame_message(image)

        self.assertEqual(message, '{"command": {"display_frame": {"mode": "RGB", "pixels": "AAAAABkAADMAAEwAAGYAAH8AAJkAALIAAMwAAOUAAAAAABkAADMAAEwAAGYAAH8AAJkAALIAAMwA\\nAOUA\\n", "size": [10, 2]}}}')
