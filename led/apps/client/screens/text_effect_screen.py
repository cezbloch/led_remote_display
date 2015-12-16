from imaging.text_effect import TextEffect
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from imaging.font import Font
from context import ApplicationContext
from kivy.lang import Builder
from os.path import join
import PIL
from kivy.clock import Clock

Context = ApplicationContext.get_instance()
Builder.load_file(join('screens', 'text_effect_screen.kv'))


class TextEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(TextEffectScreen, self).__init__(**kwargs)
        self._effect_provider = Context.get_effect_provider()
        self._display = Context.get_display()
        self._text_position = 0
        self._image = None
        self._speed = 0

    def draw_text(self):
        self._text_position = 0
        text_input = self.ids.text_input
        text = text_input.text
        _, font_size = self._display.get_size()
        font = Font()
        _, height = Context.get_display().get_size()
        font.auto_adjust_font_size_to_height(height)
        effect = TextEffect()
        effect.draw_text(text, font)
        effect.crop()
        self._image = effect.get_image()
        self._crop_image()

    def _crop_image(self):
        if self._image is not None:
            display_size = Context.get_display().get_size()
            image = self._image.crop((self._text_position, 0, display_size[0] + self._text_position, display_size[1])).transpose(PIL.Image.FLIP_TOP_BOTTOM)
            self._effect_provider.set_image(image)
            self._effect_provider.apply_image()
            self._text_position += self._speed
            if self._text_position > self._image.size[0]:
                self._text_position = -display_size[0]

    def apply_effect(self, time_delta):
        if not self.focused:
            Clock.unschedule(self.apply_effect)
        self._crop_image()

    def animation_speed_changed(self):
        self._text_position = 0
        Clock.unschedule(self.apply_effect)
        fps = self.ids.scroll_speed_slider.value
        self._speed = int(fps)
        if fps != 0:
            period = 1/fps
            Clock.schedule_interval(self.apply_effect, period)
        self.ids.speed_label.text = "Scroll Speed: {:.2f}".format(fps)
