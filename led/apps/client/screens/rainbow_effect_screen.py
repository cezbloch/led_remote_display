from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from imaging.rainbow_effect import RainbowEffectAnimation
from imaging.color import Color
from context import ApplicationContext
from kivy.clock import Clock
from kivy.lang import Builder
from os.path import join

#for kv file
from ui.color_button import ColorButton

Context = ApplicationContext.get_instance()
Builder.load_file(join('screens', 'rainbow_effect_screen.kv'))

class RainbowEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(RainbowEffectScreen, self).__init__(**kwargs)
        self._selected_button = None
        self._effect_provider = Context.get_effect_provider()
        self._time_elapsed = 0
        self._direction = "Up"

    def on_color(self):
        if self._selected_button is None:
            self._selected_button = self.ids.right_color_button
        self._selected_button.background_color = self.ids.color_picker.color
        self._time_elapsed = 0

    def apply_effect(self, time_delta):
        if not self.focused:
            Clock.unschedule(self.apply_effect)

        display_size = Context.get_display().get_size()
        effect = RainbowEffectAnimation(display_size)
        left_color = self.ids.left_color_button.background_color
        left_color_end = self.ids.left_color_button_end.background_color
        right_color = self.ids.right_color_button.background_color
        right_color_end = self.ids.right_color_button_end.background_color
        start_colors = [Color.from_normalized_float(left_color).rgb, Color.from_normalized_float(right_color).rgb]
        end_colors = [Color.from_normalized_float(left_color_end).rgb, Color.from_normalized_float(right_color_end).rgb]
        effect.set_start_colors(start_colors)
        effect.set_end_colors(end_colors)
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

    def animation_speed_changed(self):
        Clock.unschedule(self.apply_effect)
        fps = self.ids.speed_slider.value
        if fps != 0:
            period = 1/fps
            Clock.schedule_interval(self.apply_effect, period)
        self.ids.fps_label.text = "FPS: {:.2f}".format(fps)
