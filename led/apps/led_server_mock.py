from networking.factories import ServerFactory
from simulator.display import DisplayWidget

def start_mock_led_server():
    led_device = DisplayWidget()
    server = ServerFactory.create_server(led_device, address="127.0.0.1", port=6666)
    server.join()
    print "server finished"

if __name__ == '__main__':
    start_mock_led_server()
