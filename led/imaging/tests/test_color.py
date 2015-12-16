import unittest

from imaging.color import Color


class TestColor(unittest.TestCase):

    def test_convert_from_normalized_float(self):
        normalized_color = (1, 0, 0, 1)

        color = Color.from_normalized_float(normalized_color)

        self.assertEqual(color.get_as_tuple(), (255, 0, 0))

    def test_to_int(self):
        color = Color(255, 255, 255)

        self.assertEqual(color.get_as_int(), 16777215)

    def test_to_int(self):
        color = Color(240, 15, 204)

        self.assertEqual(color.get_as_int(), 15732684)

    def test_get_rgba(self):
        color = Color(240, 15, 204)

        self.assertEqual(color.get_as_rgba_tuple(), (240, 15, 204, 255))
