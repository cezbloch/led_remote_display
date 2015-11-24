from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.config import Config

from os import getcwd
from os.path import join
from PIL import ImageFont
import PIL
from context import ApplicationContext
from imaging.text_effect import TextEffect

#.kv file requirements
from ui.display_widget import DisplayWidget
from kivy.uix.image import Image


Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')
Context = ApplicationContext()


class AutoTextSizeButton(Button):
    pass


class EffectsWidget(Widget):
    pass


class EffectScreenManager(ScreenManager):
    pass


class TextEffectScreen(Screen):
    pass


class RainbowEffectScreen(Screen):
    pass


class FileChooserScreen(Screen):
    chosen_image_path = StringProperty("")

    def get_empty_photo_path(self):
        current_directory = getcwd()
        return join(current_directory, 'empty_photo.png')

    def update_image_path(self):
        selected_files = self.ids['file_chooser_icon_view'].selection
        image = self.ids['preview_image']
        image.source = self.get_empty_photo_path()
        if selected_files and selected_files[0]:
            self.chosen_image_path = selected_files[0]
        else:
            self.chosen_image_path = self.ids['file_chooser_icon_view'].path


class ProjectScreen(Screen):
    def __init__(self, **kwargs):
        super(ProjectScreen, self).__init__(**kwargs)
        self._connection_provider = Context.get_connection_provider()
        self._display = Context.get_display()
        self._image = None
        self.screens = sorted(['Text Effect', 'Rainbow Effect', 'Other'])

    def draw_text(self):
        text_input = self.ids.text_input
        text = text_input.text
        font = ImageFont.truetype("arial.ttf", 14)
        display_size = self._display.get_size()
        effect = TextEffect(display_size).with_font(font)
        image = effect.draw_text(text)
        self._image = image.crop((0, 0, display_size[0], display_size[1])).transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self.update_ui()
        self.send_image(self._image)

    def send_image(self, image):
        if self._connection_provider.is_connected():
            client = self._connection_provider.get_client()
            client.send_image_frame(image)

    def update_ui(self):
        display_widget = self.ids.display_widget
        display_widget.set_size(self._display.get_size())
        display_widget.display_frame(self._image)

    def effect_changed(self):
        #self.ids.effect_screen_manager.current =  self.ids.select_effect_spinner.
        pass



class MainScreen(Screen):
    pass


class ConnectDisplayScreen(Screen):
    def __init__(self, **kwargs):
        super(ConnectDisplayScreen, self).__init__(**kwargs)
        self._connection_provider = Context.get_connection_provider()
        self._display = Context.get_display()

    def connect(self):
        ip_address_text_input = self.ids['ip_address_text_input']
        port_text_input = self.ids['port_text_input']
        ip_address = ip_address_text_input.text
        port = int(port_text_input.text)
        self._connection_provider.connect(ip_address, port)
        self._set_display_size()
        self._update_ui()

    def disconnect(self):
        self._connection_provider.disconnect()
        self._update_ui()

    def _update_ui(self):
        connect_button = self.ids['connect_button']
        disconnect_button = self.ids['disconnect_button']
        connect_button.disabled = self._connection_provider.is_connected()
        disconnect_button.disabled = not self._connection_provider.is_connected()

    def _set_display_size(self):
        if self._connection_provider.is_connected():
            width_text_input = self.ids['width_text_input']
            height_text_input = self.ids['height_text_input']
            self._display.set_size((int(width_text_input.text), int(height_text_input.text)))
            self._connection_provider.get_client().send_set_size(self._display.get_size())



class LedScreenManager(ScreenManager):
    pass


class LedApp(App):
    def build(self):
        return LedScreenManager()

if __name__ == '__main__':
    LedApp().run()
