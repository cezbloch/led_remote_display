from color import Color
from image_factory import ImageFactory
from maths.interpolation import interpolate
from maths.numpy_wrapper import generate_range_points


class RainbowEffect(object):
    def __init__(self, size):
        self._size = size
        self._width, self._height = self._size
        self._image = ImageFactory.create_rgb_image(self._size)

    def draw_vertical_rainbow(self, left_color, right_color):
        known_coordinates = [0, self._width - 1]
        known_colors = [left_color.rgb, right_color.rgb]

        self._draw_vertical_rainbow(known_coordinates, known_colors)

    def _draw_vertical_rainbow(self, known_coordinates, known_colors):
        coordinates_to_interpolate = generate_range_points(0, self._width - 1, self._width)

        interpolated_colors = interpolate(known_coordinates, known_colors, coordinates_to_interpolate)

        for x in range(self._width):
            for y in range(self._height):
                color = Color.from_float_array(interpolated_colors[x])
                self._image.putpixel((x, y), color.get_as_tuple())

    def get_image(self):
        return self._image


class RainbowEffectAnimation(RainbowEffect):
    def __init__(self, size):
        super(RainbowEffectAnimation, self).__init__(size)
        self._start_colors = [Color(), Color()]
        self._end_colors = [Color(), Color()]
        self._duration_in_miliseconds = 0

    def set_left_colors(self, start_colors):
        self._start_colors = start_colors

    def set_right_colors(self, end_colors):
        self._end_colors = end_colors

    def set_duration(self, duration_in_miliseconds):
        self._duration_in_miliseconds = duration_in_miliseconds

    def draw_vertical_rainbow_frame_at(self, time):
        time %= self._duration_in_miliseconds
        known_time_points = [0, self._duration_in_miliseconds]
        known_colors = [self._start_colors, self._end_colors]

        time_to_interpolate = [time]

        interpolated_colors = interpolate(known_time_points, known_colors, time_to_interpolate)
        colors = interpolated_colors[0]
        left_color = colors[0]
        right_color = colors[1]

        self.draw_vertical_rainbow(Color.from_float_array(left_color), Color.from_float_array(right_color))
