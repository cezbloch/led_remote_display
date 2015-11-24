import sys
sys.path.append('/home/pi/keesware/led')

from rpi_ws281x.device import Ws281xDevice
from networking.factories import ServerFactory


def start_real_led_server():
    led_device = Ws281xDevice((8, 8))
    server = ServerFactory.create_server(led_device, address="192.168.1.3", port=6666)
    raw_input("Press Enter to continue...")
    ServerFactory.clean_up_server(server)

if __name__ == '__main__':
    start_real_led_server()
