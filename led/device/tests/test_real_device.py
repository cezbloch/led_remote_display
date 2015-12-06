import time
from random import randint
import sys

import numpy
from PIL import Image

sys.path.append('/home/pi/keesware/led/')
print sys.path
from device.device import Ws281xDevice
from imaging.image_factory import ImageFactory


def test_displays_image():
    display_size = (3, 1)
    device = Ws281xDevice(display_size)
    image = Image.open("rgb.png")
    image_rotated = image.rotate(180)
    rgb_image = image.convert('RGB')
    rgb_image_rotated = image_rotated.convert('RGB')

    while True:
        device.display_frame(rgb_image)
        time.sleep(1)
        device.display_frame(rgb_image_rotated)
        time.sleep(1)

def test_displays_buffer():
    display_size = (3, 1)
    device = Ws281xDevice(display_size)
    image = Image.new('RGB', display_size)
    while True:
        for r in range(255):
            image.putpixel((0, 0), (r, 255 - r, 0))
            image.putpixel((1, 0), (255 - r, r, 0))
            image.putpixel((2, 0), (0, (128 + r) % 255, r))
            device.display_frame(image)
            time.sleep(5/100.0)

def fill_image_uniformly(image):
    (width, height) = image.size
    max_luminance = 60
    red = numpy.uint8(randint(0, max_luminance))
    green = numpy.uint8(randint(0, max_luminance))
    blue = numpy.uint8(randint(0, max_luminance))

    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), (red, green, blue))

def fill_image_increasingly(image):
    (width, height) = image.size
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), (x+y, 0, 0))

def test_random_images():
    display_size = (8, 8)
    max_luminance = 10
    device = Ws281xDevice(display_size, max_luminance)
    green = (0, 255, 0)
    image = ImageFactory.generate_gradient_image(display_size, green)

    while True:
        #fill_image_uniformly(image)
        #fill_image_randomly(image)
        #fill_image_increasingly(image)
        device.display_frame(image)
        time.sleep(1/30.)

def test_snake():
    display_size = (8, 8)
    max_luminance = 10
    device = Ws281xDevice(display_size, max_luminance)
    painter = DotPainter(display_size)
    while True:
        image = DotPainter.draw_next_frame()
        device.display_frame(image)
        time.sleep(1/10.)


class DotPainter(object):
    def __init__(self, size):
        self._count = 0
        self._size = size
        self._image = ImageFactory.create_rgb_image(size)

    def draw_next_frame(self):

        self._image.putpixel((self._size[0], self._size[1]), (255, 255, 255))
        self._count+1
        return self._image


if __name__ == '__main__':
    print "starting test"
    test_random_images()
