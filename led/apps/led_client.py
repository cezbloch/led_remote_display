import time
from imaging.image_factory import ImageFactory
from networking.factories import ClientFactory


def start_led_client_and_send_blue_gradient():
    client = ClientFactory.create_and_connect_client(address="127.0.0.1", port=6666)
    #client = ClientFactory.create_and_connect_client(address="192.168.1.2", port=6666)

    size = (8, 8)
    client.send_set_size(size)

    color = (255, 255, 0)
    image = ImageFactory.generate_gradient_image(size, color)
    client.send_image_frame(image)

    client.close()

def animate():
    #client = ClientFactory.create_and_connect_client(address="192.168.1.2", port=6666)
    client = ClientFactory.create_and_connect_client(address="127.0.0.1", port=6666)

    size = (8, 8)
    client.send_set_size(size)

    for x in range(255):
        #ImageFactory.fill_image_randomly(image)
        image = ImageFactory.generate_gradient_image(size, (0, 0, x))
        client.send_image_frame(image)
        time.sleep(50.0/1000.0)

    client.close()


if __name__ == '__main__':
    #start_led_client_and_send_blue_gradient()
    animate()

