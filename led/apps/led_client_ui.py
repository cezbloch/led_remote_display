from kivy.app import App
from networking.factories import ClientFactory
from imaging.image_factory import ImageFactory
from kivy.clock import Clock
from ui.display_widget import DisplayWidget


class ClientWidget(DisplayWidget):
    def __init__(self, **kwargs):
        super(ClientWidget, self).__init__(**kwargs)
        self.client = ClientFactory.create_and_connect_client(address="127.0.0.1", port=6666)
        Clock.schedule_interval(self.generate_frame, 1/60.)
        size = (30, 10)
        self.set_size(size)
        self.client.send_set_size(self.buf_size)
        self.image = ImageFactory.create_rgb_image(self.buf_size)
        self.counter = 0

    def generate_frame(self, *args):
        ImageFactory.fill_image_randomly(self.image)
        self.counter += 10
        #self.image = ImageFactory.generate_gradient_image(self.buf_size, (self.counter % 255, (255 - self.counter) % 255, 128))
        self.display_frame(self.image)
        self.client.send_image_frame(self.image)

    def close(self):
        self.client.close()


class LedClientApp(App):
    def build(self):
        self.client = ClientWidget()
        return self.client

    def on_stop(self):
        self.client.close()

if __name__ == "__main__":
    LedClientApp().run()

