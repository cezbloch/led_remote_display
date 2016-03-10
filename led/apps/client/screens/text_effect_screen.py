from facades.context import ApplicationContext
from facades.text_effect_facade import TextEffectFacade, TextEffectParameters
from imaging.font import Font
from imaging.color import Color
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from os.path import join
from ui.color_selector import ColorSelector
from ui.error_window import ErrorWindow
import logging

Context = ApplicationContext.get_instance()
Builder.load_file(join('apps', 'client', 'screens', 'text_effect_screen.kv'))


class TextEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(TextEffectScreen, self).__init__(**kwargs)
        self.__logger = logging.getLogger()
        self.__effect_provider = Context.get_effect_provider()
        self.__display = Context.get_display()
        self.__color_selector = ColorSelector()
        self.__text_effect = TextEffectFacade()

    def recreate_text_effect(self):
        try:
            self.__logger.info(__name__ + " recreating text effect")
            width, height = self.__display.get_size()
            font = Font()
            font.auto_adjust_font_size_to_height(height)

            parameters = TextEffectParameters()

            parameters.text_color = Color.from_normalized_float(self.ids.text_color_button.background_color)
            parameters.background_color = Color.from_normalized_float(self.ids.background_color_button.background_color)
            parameters.text = self.ids.text_input.text
            parameters.display_size = self.__display.get_size()
            parameters.font = font

            self.__text_effect.apply(parameters)
        except Exception as ex:
            self.__logger.info(__name__ + " recreate text effect failed with ex={0}".format(ex.message))
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            Clock.unschedule(self.send_current_frame)
            popup.open()

    def on_enter(self, *args):
        self.recreate_text_effect()
        self.schedule_frame_updates()

    def on_leave(self, *args):
        Clock.unschedule(self.send_current_frame)

    def send_current_frame(self, time_delta):
        try:
            image = self.__text_effect.get_next_frame()
            self.__effect_provider.set_image(image)
            self.__effect_provider.apply_image()
        except Exception as ex:
            self.__logger.info(__name__ + " sending frame failed with ex={0}".format(ex.message))
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            Clock.unschedule(self.send_current_frame)
            popup.open()

    def schedule_frame_updates(self):
        Clock.unschedule(self.send_current_frame)
        self.__text_effect.restart_animation()
        fps = self.ids.scroll_speed_slider.value

        if fps != 0:
            period = 1/fps
            Clock.schedule_interval(self.send_current_frame, period)

        self.ids.speed_label.text = "Scroll Speed: {:.2f}".format(fps)
        self.__logger.info(__name__ + " scheduling with framerate={0}".format(fps))

    def button_pressed(self, button):
        self.__color_selector = ColorSelector()
        self.__color_selector.color = button.background_color
        self.__color_selector.unbind()
        self.__color_selector.bind(color=button.setter('background_color'))
        self.__color_selector.bind(color=self.color_changed)
        self.__color_selector.open()

    def color_changed(self, *args):
        self.recreate_text_effect()
        self.schedule_frame_updates()

    def font_size_changed(self):
        pass
