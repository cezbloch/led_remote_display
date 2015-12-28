from client_facade.context import ApplicationContext
from client_facade.paint_effect_facade import PaintEffectFacade, PaintEffectParameters
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from os.path import join
from ui.color_selector import ColorSelector


Context = ApplicationContext.get_instance()
Builder.load_file(join('screens', 'paint_effect_screen.kv'))


class PaintEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(PaintEffectScreen, self).__init__(**kwargs)
        self.__effect_provider = Context.get_effect_provider()
        self.__display = Context.get_display()
        self.__color_selector = ColorSelector()
        self.__effect = PaintEffectFacade()
        self.__touch_widget = None

    def on_enter(self, *args):
        self.schedule_frame_updates()
        self.__touch_widget = self.parent.parent.parent.ids.touch_widget

    def on_leave(self, *args):
        Clock.unschedule(self.send_current_frame)

    def send_current_frame(self, time_delta):
        parameters = PaintEffectParameters()
        parameters.display_size = self.__display.get_size()
        brush_color = self.ids.brush_color_button.background_color
        self.__touch_widget.set_brush_color(brush_color)
        parameters.image = self.__touch_widget.capture_image()
        self.__effect.apply(parameters)
        image = self.__effect.get_image()

        self.__effect_provider.set_image(image)
        self.__effect_provider.apply_image()

    def schedule_frame_updates(self):
        Clock.unschedule(self.send_current_frame)
        fps = self.ids.scroll_speed_slider.value

        if fps != 0:
            period = 1/fps
            Clock.schedule_interval(self.send_current_frame, period)

        self.ids.speed_label.text = "FPS: {:.2f}".format(fps)

    def button_pressed(self, button):
        self.__color_selector.color = button.background_color
        self.__color_selector.unbind()
        self.__color_selector.bind(color=button.setter('background_color'))
        self.__color_selector.open()

    def clear_canvas(self):
        self.__touch_widget.clear_canvas()

    def point_size_changed(self):
        point_size = self.ids.point_size_slider.value
        self.__touch_widget.set_point_size(point_size)
