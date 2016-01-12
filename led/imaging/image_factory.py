import PIL
from random import randint


def multiply_color(color, number, div):
    (r, g, b) = color
    if div == 0:
        return 0, 0, 0
    else:
        return r*number/div, g*number/div, b*number/div


class ImageFactory(object):
    @staticmethod
    def create_rgb_image(size, color=None):
        if color is None:
            return PIL.Image.new('RGB', size)
        else:
            return PIL.Image.new('RGB', size, color.get_as_tuple())

    @staticmethod
    def create_rgba_image(size, color=None):
        if color is None:
            return PIL.Image.new('RGBA', size)
        else:
            return PIL.Image.new('RGBA', size, color)

    @staticmethod
    def create_image(mode, size):
        image = PIL.Image.new(mode, size)
        return image

    @staticmethod
    def create_image_from_string(mode, size, data):
        image = PIL.Image.fromstring(mode, size, data)
        return image

    @staticmethod
    def generate_gradient_image(size, color):
        image = ImageFactory.create_rgb_image(size)
        (width, height) = size

        for y in range(height):
            for x in range(width):
                interpolated_color = multiply_color(color, x, width)
                image.putpixel((x, y), interpolated_color)
        return image

    @staticmethod
    def fill_image_randomly(image):
        (width, height) = image.size
        max_luminance = 60
        for y in range(height):
            for x in range(width):
                red = randint(0, max_luminance)
                green = randint(0, max_luminance)
                blue = randint(0, max_luminance)

                image.putpixel((x, y), (red, green, blue))
