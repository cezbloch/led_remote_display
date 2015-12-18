import unittest
from imaging.scroll_animation import ScrollAnimation
from imaging.image_factory import ImageFactory
from maths.containers import Array
from imaging.font import Font
from imaging.text_effect import TextEffect


class TestTextScrollAnimation(unittest.TestCase):
    def setUp(self):
        text_height = 10
        font = Font()
        font.auto_adjust_font_size_to_height(text_height)
        effect = TextEffect()
        text = "KeesWare"
        effect.draw_text(text, font)
        effect.crop()
        self.image = effect.get_image()

    def test_scroll_animation_horizontally_from_right_to_left(self):
        animation_size = (30, 10)
        animation = ScrollAnimation(animation_size, self.image)
        start_point = Array([0, 0])
        image_size = self.image.size
        end_point = Array([-image_size[0], -image_size[1]])
        # move by one pixel per frame
        frames_amount = image_size[0] + animation_size[0]

        animation.pre_render(start_point, end_point, frames_amount)
        middle_frame = animation[len(animation)/2 - 1]

        self.assertEqual(middle_frame.size, animation_size)
        self.assertEqual(middle_frame.getpixel((6, 4)), (255, 255, 255))
        self.assertEqual(len(animation), frames_amount)
