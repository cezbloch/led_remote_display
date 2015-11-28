import unittest

from imaging.color import Color


class TestColor(unittest.TestCase):

    def test_convert_from_normalized_float(self):
        normalized_color = (1, 0, 0, 1)

        color = Color.from_normalized_float(normalized_color)

        self.assertEqual(color.get_as_tuple(), (255, 0, 0))
