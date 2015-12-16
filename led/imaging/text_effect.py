from color import Color
from PIL import ImageDraw
from image_factory import ImageFactory


class TextEffect(object):
    def __init__(self, text_color=Color.White(), background_color=Color.Black()):
        self.__background_color = background_color
        self.__text_color = text_color
        self.__image = None

    def draw_text(self, text, font):
        image_size = font.get_text_size(text)
        self.__image = ImageFactory.create_rgb_image(image_size, self.__background_color)
        draw = ImageDraw.Draw(self.__image)
        draw.text((0, 0), text, self.__text_color.get_as_rgba_tuple(), font=font.get_true_type())
        del draw

    def get_image(self):
        return self.__image

    def crop(self):
        bounding_box = self.__image.getbbox()
        self.__image = self.__image.crop(bounding_box)

