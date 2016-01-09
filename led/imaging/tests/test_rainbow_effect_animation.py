import unittest
from imaging.rainbow_effect import RainbowEffectAnimation
from imaging.color import Color


class TestRainbowEffectAnimation(unittest.TestCase):
    def test_generate_initial_frame(self):
        size = (17, 10)
        effect = RainbowEffectAnimation(size)
        left_start_color = Color(255, 0, 0)
        left_end_color = Color(0, 0, 0)
        right_start_color = Color(0, 0, 255)
        right_end_color = Color(0, 255, 0)
        duration_in_miliseconds = 2000

        effect.set_left_colors([left_start_color.rgb, left_end_color.rgb])
        effect.set_right_colors([right_start_color.rgb, right_end_color.rgb])
        effect.set_duration(duration_in_miliseconds)

        effect.draw_vertical_rainbow_frame_at(0)
        image = effect.get_image()

        self.assertEqual(image.getpixel((0, 0)), (255, 0, 0))
        self.assertEqual(image.getpixel((16, 9)), (0, 0, 255))
        self.assertEqual(image.getpixel((8, 4)), (127, 0, 127))

    def test_generate_intermediate_frame(self):
        size = (17, 10)
        effect = RainbowEffectAnimation(size)
        left_start_color = Color(255, 0, 0)
        left_end_color = Color(0, 0, 0)
        right_start_color = Color(0, 0, 255)
        right_end_color = Color(0, 255, 0)
        duration_in_miliseconds = 2000

        effect.set_left_colors([left_start_color.rgb, left_end_color.rgb])
        effect.set_right_colors([right_start_color.rgb, right_end_color.rgb])
        effect.set_duration(duration_in_miliseconds)

        effect.draw_vertical_rainbow_frame_at(1000)
        image = effect.get_image()

        self.assertEqual(image.getpixel((0, 0)), (127, 0, 0))
        self.assertEqual(image.getpixel((16, 9)), (0, 127, 127))
        self.assertEqual(image.getpixel((8, 4)), (63, 63, 63))
