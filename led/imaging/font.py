from PIL import ImageFont
from os.path import join


class Font(object):
    def __init__(self, size=10, font_path=join('apps', 'client', 'resources', 'fonts', 'Arcon.otf')):
        self.__size = size
        self.__font_path = font_path
        self.__font = ImageFont.truetype(self.__font_path, self.__size)

    def get_true_type(self):
        return self.__font

    def auto_adjust_font_size_to_height(self, height):
        letter_size = 0
        font_size = 0
        while letter_size < height:
            font_size += 1
            self.__font = ImageFont.truetype(self.__font_path, font_size)
            letter_size = self.get_ascent() - self.get_descent()

    def get_text_size(self, text):
        return self.__font.getsize(text)

    def get_ascent(self):
        return self.__font.font.ascent

    def get_descent(self):
        return self.__font.font.descent
