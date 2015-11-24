from image_factory import ImageFactory
from maths.interpolation import Math
from maths.containers import Array
from color import Color

class RainbowEffect(object):
    def __init__(self, size):
        self._size = size
        self._width, self._height = self._size
        self._image = ImageFactory.create_rgb_image(self._size)

    def draw_vertical_rainbow(self, left_color, right_color):
        known_coordinates = Array([0, self._width - 1])
        known_colors = Array([left_color.rgb, right_color.rgb])
        coordinates_to_interpolate = Math.generate_range_points(0, self._width - 1, self._width)

        interpolated_colors = Math.Interpolate(known_coordinates, known_colors, coordinates_to_interpolate)

        for x in range(self._width):
            for y in range(self._height):
                color = Color()
                color.from_float(interpolated_colors.get(x))
                self._image.putpixel((x, y), color.get_as_tuple())

    def get_image(self):
        return self._image


