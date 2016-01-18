from imaging.color import Color
from imaging.paint_effect import PaintEffect
from unittest import TestCase


class TestImageFactory(TestCase):
    def test_paint_straight_line(self):
        widget_size = (500, 1000)
        display_size = (50, 100)
        start_point = [100, 400]
        end_point = [400, 800]
        brush_color = Color.Blue()
        point_size = 1
        effect = PaintEffect(display_size, widget_size)

        effect.set_point_size(point_size)
        effect.set_line_color(brush_color)
        effect.draw_lines([start_point, end_point])

        image = effect.get_image()
        self.assertEqual(image.size, display_size)
        self.assertEqual(image.getpixel((10, 40)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((40, 80)), brush_color.get_as_tuple())

    def test_paint_square(self):
        widget_size = (500, 1000)
        display_size = (50, 100)
        points = [[100, 100], [100, 900], [400, 900], [400, 100], [100, 100]]
        brush_color = Color.Red()
        point_size = 3
        effect = PaintEffect(display_size, widget_size)

        effect.set_point_size(point_size)
        effect.set_line_color(brush_color)
        effect.draw_lines(points)

        image = effect.get_image()
        self.assertEqual(image.size, display_size)
        self.assertEqual(image.getpixel((10, 10)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((10, 90)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((40, 90)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((40, 10)), brush_color.get_as_tuple())

    def test_paint_cross(self):
        widget_size = (500, 1000)
        display_size = (50, 100)
        vertical_line = [[250, 0], [250, 1000]]
        horizontal_line = [[0, 800], [500, 800]]
        brush_color = Color.White()
        point_size = 5
        effect = PaintEffect(display_size, widget_size)

        effect.set_point_size(point_size)
        effect.set_line_color(brush_color)
        effect.draw_lines(vertical_line)
        effect.draw_lines(horizontal_line)

        image = effect.get_image()
        self.assertEqual(image.size, display_size)
        self.assertEqual(image.getpixel((25, 0)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((25, 99)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((0, 80)), brush_color.get_as_tuple())
        self.assertEqual(image.getpixel((49, 80)), brush_color.get_as_tuple())
