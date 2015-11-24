from message_factory import MessageFactory

class LedClient(object):
    def __init__(self, socket_client):
        self.socket_client = socket_client

    def send_image_frame(self, image):
        display_frame_command = MessageFactory.create_display_frame_message(image)
        self.socket_client.send_obj(display_frame_command)

    def send_set_size(self, size):
        display_frame_command = MessageFactory.create_set_size_message(size)
        self.socket_client.send_obj(display_frame_command)

    def close(self):
        self.socket_client.close()
