import sys
sys.path.append('/home/pi/keesware/led')

from device.device import Ws281xDevice
from networking.twisted_server import LedServer
from device.strip_factory import StripeFactory


def start_real_led_server():
    led_device = Ws281xDevice(StripeFactory(), (30, 10))
    server = LedServer(led_device)
    server.start(6666)
    led_device.clear()

    from twisted.internet import reactor
    reactor.run()

if __name__ == '__main__':
    start_real_led_server()
