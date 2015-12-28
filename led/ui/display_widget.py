from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import PIL


class DisplayWidget(Image):
    def __init__(self, **kwargs):
        super(DisplayWidget, self).__init__(**kwargs)
        self.buf_size = None
        self.my_image = None
        Clock.schedule_interval(self.update, 1/60.)

    def create_texture(self):
        if self.my_image.size == self.buf_size:
            width, height = self.size
            scaled_image = self.my_image.resize((int(width), int(height)))
            texture = Texture.create(size=self.size)
            data_bytes = scaled_image.tobytes()
            texture.blit_buffer(data_bytes, colorfmt='rgb', bufferfmt='ubyte')
            self.texture = texture
        else:
            #TODO: log something
            pass

    def display_frame(self, image):
        # just update image in this thread - comes from server thread
        self.my_image = image.transpose(PIL.Image.FLIP_TOP_BOTTOM)

    def set_size(self, buf_size):
        self.buf_size = buf_size

    def update(self, *args):
        #update the image in the UI thread - it doesn't work to update from server thread
        if self.my_image is not None and self.buf_size is not None:
            self.create_texture()
