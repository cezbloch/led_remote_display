import unittest
from imaging.image_effect import RainbowEffect
from imaging.color import Color


class TestRainbowEffect(unittest.TestCase):
    def test_create_3x2_rainbow_image(self):
        size = (3, 2)
        effect = RainbowEffect(size)
        start_color = Color(255, 0, 0)
        end_color = Color(0, 0, 255)

        effect.draw_vertical_rainbow(start_color, end_color)
        image = effect.get_image()

        self.assertEqual(image.getpixel((0, 0)), start_color.get_as_tuple())
        self.assertEqual(image.getpixel((2, 1)), end_color.get_as_tuple())
        self.assertEqual(image.getpixel((1, 1)), (127, 0, 127))

    def test_create_30x10_rainbow_image(self):
        size = (29, 10)
        effect = RainbowEffect(size)
        start_color = Color(127, 255, 63)
        end_color = Color(255, 0, 180)

        effect.draw_vertical_rainbow(start_color, end_color)
        image = effect.get_image()

        self.assertEqual(image.getpixel((0, 5)), start_color.get_as_tuple())
        self.assertEqual(image.getpixel((28, 9)), end_color.get_as_tuple())
        self.assertEqual(image.getpixel((14, 0)), (191, 127, 121))
