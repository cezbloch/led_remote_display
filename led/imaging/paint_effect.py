from imaging.color import Color
from imaging.image_factory import ImageFactory
from PIL import ImageDraw


class PaintEffect(object):
    def __init__(self, size, widget_size):
        self.__size = size
        self.__widget_size = widget_size
        self.__point_size = 10
        self.__line_color = Color.White()
        self.__image = ImageFactory.create_rgb_image(self.__size)

    def set_point_size(self, point_size):
        self.__point_size = point_size

    def set_line_color(self, color):
        self.__line_color = color

    def draw_lines(self, points):
        converted = self.__convert_widget_points_to_image(points)
        image = self.__image
        draw = ImageDraw.Draw(image)
        color = self.__line_color.get_as_rgba_tuple()
        draw.line(converted, fill=color, width=self.__point_size)
        del draw

    def __convert_widget_points_to_image(self, points):
        size = [float(i) for i in self.__size]
        widget_size = [float(i) for i in self.__widget_size]
        ratio = [size[i] / widget_size[i] for i in range(len(self.__size))]
        converted = [(point[0] * ratio[0], point[1] * ratio[1]) for point in points]
        return converted

    def get_image(self):
        return self.__image

    def clear(self):
        self.__image = ImageFactory.create_rgb_image(self.__size)
