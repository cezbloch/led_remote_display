from imaging.text_effect import TextEffect
from imaging.scroll_animation import ScrollAnimation
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from imaging.font import Font
from client_facade.context import ApplicationContext
from kivy.lang import Builder
from os.path import join
import PIL
from kivy.clock import Clock
from maths.containers import Array

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
        text_input = self.ids.text_input
        text = text_input.text
        font = Font()
        width, height = Context.get_display().get_size()
        font.auto_adjust_font_size_to_height(height)
        effect = TextEffect()
        effect.draw_text(text, font)
        effect.crop()
        text_image = effect.get_image()
        self.__animation = ScrollAnimation((width, height), text_image)
        start_point = Array([width, 0])
        end_point = Array([-text_image.size[0], 0])
        steps = text_image.size[0] + width
        self.__animation.pre_render(start_point, end_point, steps)

    def apply_effect(self, time_delta):
        if not self.focused:
            Clock.unschedule(self.apply_effect)
        if self.__animation is None:
            self.draw_text()
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
