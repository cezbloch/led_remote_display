import sys
sys.path.append('/home/pi/keesware/led')

from device.device import Ws281xDevice
from networking.factories import ServerFactory
from device.strip_factory import StripeFactory


def start_real_led_server():
    led_device = Ws281xDevice(StripeFactory(), (30, 10))
    server = ServerFactory.create_server(led_device, address="192.168.1.4", port=6666)
    raw_input("Press Enter to continue...")
    led_device.clear()
    ServerFactory.clean_up_server(server)

if __name__ == '__main__':
    start_real_led_server()
