import unittest
from imaging.text_effect import TextEffect
from PIL import ImageFont


class TestImageFactory(unittest.TestCase):
    def test_create_empty_image_from_string(self):
        size = (30, 10)
        text = "KeesWare"
        font = ImageFont.truetype("arial.ttf", 14)
        effect = TextEffect(size).with_font(font)
        image = effect.draw_text(text)
        image.show()

        self.assertEqual(image.size, size)
