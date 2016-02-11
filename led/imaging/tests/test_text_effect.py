import unittest
from imaging.color import Color
from imaging.font import Font
from imaging.text_effect import TextEffect
from os.path import join


class TestTextEffect(unittest.TestCase):
    def test_draw_text(self):
        size = (30, 10)
        font = Font(10, join('..', '..', 'apps', 'client', 'resources', 'fonts', 'Arcon.otf'))
        font.auto_adjust_font_size_to_height(size[1])
        effect = TextEffect()
        text = "KeeSWare"

        effect.draw_text(text, font)
        effect.crop()
        image = effect.get_image()

        self.assertEqual(image.size[1], 10)

    def test_draw_text_red_green(self):
        size = (30, 10)
        font = Font(10, join('..', '..', 'apps', 'client', 'resources', 'fonts', 'Arcon.otf'))
        font.auto_adjust_font_size_to_height(size[1])
        effect = TextEffect(Color.Red(), Color.Green())
        text = "KeesWare"

        effect.draw_text(text, font)
        effect.crop()
        image = effect.get_image()

        self.assertEqual(image.size[1], 10)
