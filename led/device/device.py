from imaging.color import Color
from imaging.image_factory import ImageFactory

DEFAULT_LED_BRIGHTNESS = 40   # Set to 0 for darkest and 255 for brightest


class Ws281xDevice(object):
    def __init__(self, stripe_factory, size, brightness=DEFAULT_LED_BRIGHTNESS):
        self._stripe_factory = stripe_factory
        self._brightness = brightness
        self._size = size
        self._stripe = None
        self._setup_strip(self._size, self._brightness)

    def _setup_strip(self, size, brightness):
        self._stripe = self._stripe_factory.create_stripe(size, brightness)
        self._stripe.begin()

    def set_size(self, size):
        self._setup_strip(size, self._brightness)

    def set_brightness(self, brightness):
        self._stripe.setBrightness(brightness)

    def display_frame(self, image):
        (width, height) = image.size
        image_length = width * height
        strip_length = self._stripe.numPixels()

        if image_length != strip_length:
            raise AttributeError("trying to display image with different size than the stripe")

        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                color = Color(r, g, b)
                diode_index_in_stripe = y * width
                if y % 2 == 0:
                    diode_index_in_stripe += x
                else:
                    diode_index_in_stripe += (width - 1) - x
                self._stripe.setPixelColor(diode_index_in_stripe, color.get_as_int())

        self._stripe.show()

    def clear(self):
        black_image = ImageFactory.create_rgb_image(self._size)
        self.display_frame(black_image)
