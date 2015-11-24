import unittest

import defines
from imaging.image_factory import *


class TestImageFactory(unittest.TestCase):
    @staticmethod
    def get_image_data(image):
        image_data = {
            defines.PIXELS: image.tostring(),
            defines.SIZE: image.size,
            defines.MODE: image.mode,
        }
        data = image_data[defines.PIXELS]
        size = image_data[defines.SIZE]
        mode = image_data[defines.MODE]

        return data, size, mode

    def test_create_empty_image_from_string(self):
        image = ImageFactory.generate_gradient_image((8, 8), (255, 0, 0))
        (data, size, mode) = TestImageFactory.get_image_data(image)

        image_from_string = ImageFactory.create_image_from_string(mode, size, data)

        self.assertEqual(image, image_from_string)

    def test_create_green_image_from_string(self):
        image = ImageFactory.generate_gradient_image((8, 8), (0, 255, 0))
        (data, size, mode) = TestImageFactory.get_image_data(image)

        image_from_string = ImageFactory.create_image_from_string(mode, size, data)

        self.assertEqual(image, image_from_string)
