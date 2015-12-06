import numpy

class MockStripeFactory(object):
    def __init__(self):
        self._stripe = None

    def create_stripe(self, size, brightness):
        self._stripe = MockStipe(size, brightness)
        return self._stripe

    def get_stripe(self):
        return self._stripe


class MockStipe(object):
    def __init__(self, (width, height), brightness):
        self._length = width * height
        self._brightness = brightness
        self._is_initialized = False
        self._led_data = [0] * self._length

    def begin(self):
        self._is_initialized = True

    def setBrightness(self, brightness):
        self._validate_is_initialized()
        self._brightness = brightness

    def setPixelColor(self, n, color):
        self._validate_is_initialized()
        if 0 <= n < self._length:
            self._led_data[n] = color
        else:
            raise AttributeError

    def numPixels(self):
        self._validate_is_initialized()
        return self._length

    def getPixelColor(self, n):
        self._validate_is_initialized()
        if 0 <= n < self._length:
            return self._led_data[n]
        else:
            raise AttributeError

    def getPixels(self):
        self._validate_is_initialized()
        return self._led_data

    def show(self):
        self._validate_is_initialized()

    def _validate_is_initialized(self):
        if not self._is_initialized:
            raise AttributeError
