#from rpi_ws281x.legacy.python.neopixel import Adafruit_NeoPixel
import rpi_ws281x

LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5           # DMA channel to use for generating signal (try 5)
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)


class StripeFactory(object):
    def create_stripe(self, (width, height), brightness):
        stripe = rpi_ws281x.Adafruit_NeoPixel(width * height, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, brightness)
        return stripe
