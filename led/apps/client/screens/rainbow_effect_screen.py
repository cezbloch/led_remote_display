from client_facade.context import ApplicationContext
from imaging.rainbow_effect import RainbowEffectAnimation
from imaging.color import Color
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from os.path import join
from ui.error_window import ErrorWindow
from ui.color_selector import ColorSelector
import logging

Context = ApplicationContext.get_instance()
Builder.load_file(join('apps', 'client', 'screens', 'rainbow_effect_screen.kv'))


class RainbowEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(RainbowEffectScreen, self).__init__(**kwargs)
        self.__logger = logging.getLogger()
        self._effect_provider = Context.get_effect_provider()
        self.__color_selector = ColorSelector()
        self._time_elapsed = 0
        self._direction = "Up"
        self.__frame_count = 0

    def button_pressed(self, button):
        self.__logger.info(__name__ + " changing color for button={0}".format(button.text))
        self.__color_selector = ColorSelector()
        self.__color_selector.color = button.background_color
        self.__color_selector.unbind()
        self.__color_selector.bind(color=button.setter('background_color'))
        self.__color_selector.open()
        self._time_elapsed = 0

    def on_enter(self, *args):
        pass
        # TODO: this gets triggered when loading application - trigger only when entering project screen
        #self.animation_speed_changed()

    def on_leave(self, *args):
        Clock.unschedule(self.apply_effect)

    def apply_effect(self, time_delta):
        try:
            self.__logger.info(__name__ + " drawing frame {0}".format(self.__frame_count))
            self.__frame_count += 1

            display_size = Context.get_display().get_size()
            effect = RainbowEffectAnimation(display_size)
            left_color = self.ids.left_color_button.background_color
            left_color_end = self.ids.left_color_button_end.background_color
            right_color = self.ids.right_color_button.background_color
            right_color_end = self.ids.right_color_button_end.background_color
            left_colors = [Color.from_normalized_float(left_color).rgb, Color.from_normalized_float(left_color_end).rgb]
            right_colors = [Color.from_normalized_float(right_color).rgb, Color.from_normalized_float(right_color_end).rgb]
            effect.set_left_colors(left_colors)
            effect.set_right_colors(right_colors)
            effect.set_duration(2000)
            effect.draw_vertical_rainbow_frame_at(self._time_elapsed)
            image = effect.get_image()
            self._effect_provider.set_image(image)
            self._effect_provider.apply_image()

            if self._direction is "Up":
                self._time_elapsed += int(time_delta*1000)
            else:
                self._time_elapsed -= int(time_delta*1000)

            if self._time_elapsed > 2000:
                self._direction = "Down"
                self._time_elapsed = 1999

            if self._time_elapsed < 0:
                self._direction = "Up"
                self._time_elapsed = 0
        except Exception as ex:
            self.__logger.error(__name__ + " drawing frame failed")
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            Clock.unschedule(self.apply_effect)
            popup.open()

    def animation_speed_changed(self):
        try:
            Clock.unschedule(self.apply_effect)
            fps = self.ids.speed_slider.value
            if fps != 0:
                period = 1/fps
                Clock.schedule_interval(self.apply_effect, period)
            self.__logger.info(__name__ + " changing framerate - new fps={:.2f}".format(fps))
            self.ids.fps_label.text = "FPS: {:.2f}".format(fps)
        except Exception as ex:
            self.__logger.error(__name__ + " failed applying new speed")
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            Clock.unschedule(self.apply_effect)
            popup.open()
