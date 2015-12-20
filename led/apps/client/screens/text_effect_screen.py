from client_facade.context import ApplicationContext
from imaging.font import Font
from imaging.text_effect import TextEffect
from imaging.scroll_animation import ScrollAnimation
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from os.path import join
import PIL
from maths.containers import Array
from ui.color_selector import ColorSelector
from imaging.color import Color

Context = ApplicationContext.get_instance()
Builder.load_file(join('screens', 'text_effect_screen.kv'))


class TextEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(TextEffectScreen, self).__init__(**kwargs)
        self._effect_provider = Context.get_effect_provider()
        self._display = Context.get_display()
        self.__animation = None
        self._speed = 0
        self.__current_frame = 0

    def draw_text(self):
        self.__current_frame = 0
        text_color = Color.from_normalized_float(self.ids.text_color_button.background_color)
        background_color = Color.from_normalized_float(self.ids.background_color_button.background_color)
        text = self.ids.text_input.text
        font = Font()
        width, height = Context.get_display().get_size()
        font.auto_adjust_font_size_to_height(height)
        effect = TextEffect(text_color, background_color)
        effect.draw_text(text, font)
        effect.crop()
        text_image = effect.get_image()
        self.__animation = ScrollAnimation((width, height), text_image, background_color)
        start_point = Array([width, 0])
        end_point = Array([-text_image.size[0], 0])
        steps = text_image.size[0] + width
        self.__animation.pre_render(start_point, end_point, steps)

    def on_enter(self, *args):
        self.draw_text()
        self.animation_speed_changed()

    def on_leave(self, *args):
        Clock.unschedule(self.apply_effect)

    def apply_effect(self, time_delta):
        # if not self.focused:
        #     Clock.unschedule(self.apply_effect)
        # if self.__animation is None:
        #     self.draw_text()
        image = self.__animation[self.__current_frame % len(self.__animation)].transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self._effect_provider.set_image(image)
        self._effect_provider.apply_image()
        self.__current_frame += 1

    def animation_speed_changed(self):
        self.__current_frame = 0
        Clock.unschedule(self.apply_effect)
        fps = self.ids.scroll_speed_slider.value
        self._speed = int(fps)
        if fps != 0:
            period = 1/fps
            Clock.schedule_interval(self.apply_effect, period)
        self.ids.speed_label.text = "Scroll Speed: {:.2f}".format(fps)

    def button_pressed(self, button):
        color_selector = ColorSelector()
        color_selector.color = button.background_color
        color_selector.bind(color=button.setter('background_color'))
        color_selector.bind(color=self.color_changed)
        color_selector.open()

    def color_changed(self, *args):
        self.draw_text()
        self.animation_speed_changed()
