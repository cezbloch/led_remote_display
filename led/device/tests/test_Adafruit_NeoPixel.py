import time

from rpi_ws281x.python.neopixel import Adafruit_NeoPixel, Color
from PIL import Image

# LED strip configuration:
LED_COUNT      = 3      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def viewImage(strip, image):
    for i in range(strip.numPixels()):
        r, g, b = image.getpixel((i, 0))
        color = Color(r, g, b)
        strip.setPixelColor(i, color)
    strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    image = Image.open("rgb.png")
    print image.size
    rgb_im = image.convert('RGB')
    viewImage(strip, rgb_im)
    time.sleep(2)

    blue_color = Color(0, 0, 255)
    colorWipe(strip, blue_color)
