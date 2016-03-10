import sys
sys.path.append('/home/pi/keesware/led')

from device.gpio_pwm_device import Ws281xDevice
from device.strip_factory import StripeFactory
from facades.logger_provider import LoggerProvider
from networking.twisted_server import LedServer


def start_real_led_server():
    LoggerProvider().setup_logging()
    led_device = Ws281xDevice(StripeFactory(), (30, 10))
    server = LedServer(led_device)
    server.start()

    from twisted.internet import reactor
    reactor.run()

if __name__ == '__main__':
    start_real_led_server()
