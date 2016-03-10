import unittest
from device.gpio_pwm_device import Ws281xDevice
from mocks import MockStripeFactory
from imaging.image_factory import ImageFactory
from imaging.color import Color



class TestDevice(unittest.TestCase):
    def setUp(self):
        self.red = Color(255, 0, 0)
        self.green = Color(0, 255, 0)
        self.blue = Color(0, 0, 255)
        self.stripe_factory = MockStripeFactory()

    def create_stripe_and_device(self, size):
        device = Ws281xDevice(self.stripe_factory, size)
        stripe = self.stripe_factory.get_stripe()
        return stripe, device

    def test_3x1_panel(self):
        size = (3, 1)
        stripe, device = self.create_stripe_and_device(size)
        image = ImageFactory.create_rgb_image(size)
        image.putpixel((0, 0), self.red.get_as_tuple())
        image.putpixel((1, 0), self.green.get_as_tuple())
        image.putpixel((2, 0), self.blue.get_as_tuple())

        device.display_frame(image)

        self.assertEqual(stripe.getPixelColor(0), self.red.get_as_int())
        self.assertEqual(stripe.getPixelColor(1), self.green.get_as_int())
        self.assertEqual(stripe.getPixelColor(2), self.blue.get_as_int())

    def test_3x2_panel(self):
        size = (3, 2)
        stripe, device = self.create_stripe_and_device(size)
        image = ImageFactory.create_rgb_image(size)
        image.putpixel((0, 0), self.red.get_as_tuple())
        image.putpixel((1, 0), self.green.get_as_tuple())
        image.putpixel((2, 0), self.blue.get_as_tuple())

        image.putpixel((0, 1), self.red.get_as_tuple())
        image.putpixel((1, 1), self.green.get_as_tuple())
        image.putpixel((2, 1), self.blue.get_as_tuple())

        device.display_frame(image)

        self.assertEqual(stripe.getPixelColor(5), self.red.get_as_int())
        self.assertEqual(stripe.getPixelColor(4), self.green.get_as_int())
        self.assertEqual(stripe.getPixelColor(3), self.blue.get_as_int())
