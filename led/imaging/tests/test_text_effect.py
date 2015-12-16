import unittest
from imaging.text_effect import TextEffect
from imaging.font import Font


class TestTextEffect(unittest.TestCase):
    def test_draw_text(self):
        size = (30, 10)
        font = Font()
        font.auto_adjust_font_size_to_height(size[1])
        effect = TextEffect()
        text = "KeeSWare"

        effect.draw_text(text, font)
        effect.crop()
        image = effect.get_image()

        self.assertEqual(image.size[1], 10)
