from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.clock import Clock

from os import getcwd
from os.path import join
from PIL import ImageFont
import PIL
from context import ApplicationContext
from imaging.text_effect import TextEffect
from imaging.image_effect import RainbowEffect
from imaging.color import Color

#must be before .kv files imports
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')

#.kv file requirements
from ui.display_widget import DisplayWidget
from kivy.uix.image import Image
from kivy.uix.slider import Slider

Context = ApplicationContext()


class AutoTextSizeButton(Button):
    pass


class ColorButton(ToggleButton):
    pass


class EffectsWidget(Widget):
    pass


class EffectScreenManager(ScreenManager):
    pass


class TextEffectScreen(Screen):
    def __init__(self, **kwargs):
        super(TextEffectScreen, self).__init__(**kwargs)
        self._effect_provider = Context.get_effect_provider()

    def draw_text(self):
        text_input = self.ids.text_input
        text = text_input.text
        font = ImageFont.truetype("arial.ttf", 14)
        display_size = Context.get_display().get_size()
        effect = TextEffect(display_size).with_font(font)
        image = effect.draw_text(text)
        image = image.crop((0, 0, display_size[0], display_size[1])).transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self._effect_provider.set_image(image)
        self._effect_provider.apply_image()


class RainbowEffectScreen(Screen):
    def __init__(self, **kwargs):
        super(RainbowEffectScreen, self).__init__(**kwargs)
        self._selected_button = None
        self._effect_provider = Context.get_effect_provider()

    def on_color(self):
        if self._selected_button is None:
            self._selected_button = self.ids.right_color_button
        self._selected_button.background_color = self.ids.color_picker.color
        self.apply_effect()

    def apply_effect(self, time_delta):
        display_size = Context.get_display().get_size()
        effect = RainbowEffect(display_size)
        left_color = self.ids.left_color_button.background_color
        right_color = self.ids.right_color_button.background_color
        effect.draw_vertical_rainbow(Color.from_normalized_float(left_color), Color.from_normalized_float(right_color))
        image = effect.get_image()
        self._effect_provider.set_image(image)
        self._effect_provider.apply_image()

    def animation_speed_changed(self):
        Clock.unschedule(self.apply_effect)
        fps = self.ids.speed_slider.value
        if fps != 0:
            period = 1/fps
            Clock.schedule_interval(self.apply_effect, period)
        self.ids.fps_label.text = "FPS: {:.2f}".format(fps)


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
        self._effect_provider = Context.get_effect_provider()
        self._effect_provider.set_apply_effect_callback(self.apply_effect)
        self._display = Context.get_display()
        self._image = None
        self._screen_text_to_ids = {'Text Effect': 'text_effect_screen', 'Rainbow Effect': 'rainbow_effect_screen'}

    def apply_effect(self):
        self._image = self._effect_provider.get_image()
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
        self.ids.effect_screen_manager.current = self._screen_text_to_ids[self.ids.select_effect_spinner.text]


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
