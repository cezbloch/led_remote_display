from client_facade.context import ApplicationContext
from client_facade.paint_effect_facade import PaintEffectFacade, PaintEffectParameters
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from os.path import join
from ui.color_selector import ColorSelector
from ui.error_window import ErrorWindow
import logging

Context = ApplicationContext.get_instance()
Builder.load_file(join('apps', 'client', 'screens', 'paint_effect_screen.kv'))


class PaintEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(PaintEffectScreen, self).__init__(**kwargs)
        self.__logger = logging.getLogger()
        self.__effect_provider = Context.get_effect_provider()
        self.__display = Context.get_display()
        self.__color_selector = ColorSelector()
        self.__effect = None
        self.__touch_widget = None
        self.__frame_count = 0

    def on_enter(self, *args):
        self.__touch_widget = self.parent.parent.parent.ids.touch_widget
        self.__touch_widget.move_callback = self.send_current_frame
        self.__effect = PaintEffectFacade(self.__display.get_size(), self.__touch_widget.size)
        self.update_ui()
        self.point_size_changed()

    def send_current_frame(self, points):
        try:
            if self.__frame_count % 10 == 0:
                self.__logger.debug(__name__ + " drawing frame {0}".format(self.__frame_count))
            self.__frame_count += 1

            parameters = PaintEffectParameters()
            parameters.color = self.ids.brush_color_button.background_color
            parameters.point_size = self.ids.point_size_slider.value
            parameters.points = points
            self.__effect.apply(parameters)
            self.update_ui()
        except Exception as ex:
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            popup.open()

    def update_ui(self):
        image = self.__effect.get_image()
        self.__effect_provider.set_image(image)
        self.__effect_provider.apply_image()

    def button_pressed(self, button):
        self.__color_selector.color = button.background_color
        self.__color_selector.unbind()
        self.__color_selector.bind(color=button.setter('background_color'))
        self.__color_selector.open()

    def clear_canvas(self):
        self.__effect.clear()
        self.update_ui()

    def point_size_changed(self):
        self.ids.point_size_label.text = "point size ({0})".format(int(self.ids.point_size_slider.value))
