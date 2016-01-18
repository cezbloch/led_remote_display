from imaging.color import Color
from imaging.paint_effect import PaintEffect
from PIL.Image import FLIP_TOP_BOTTOM


class PaintEffectParameters(object):
    def __init__(self):
        self.color = None
        self.point_size = None
        self.points = None


class PaintEffectFacade(object):
    def __init__(self, display_size, widget_size):
        self.__effect = PaintEffect(display_size, widget_size)

    def apply(self, parameters):
        self.__effect.set_point_size(int(parameters.point_size))
        self.__effect.set_line_color(Color.from_normalized_float(parameters.color))
        self.__effect.draw_lines(parameters.points)

    def get_image(self):
        return self.__effect.get_image().transpose(FLIP_TOP_BOTTOM)

    def clear(self):
        self.__effect.clear()

