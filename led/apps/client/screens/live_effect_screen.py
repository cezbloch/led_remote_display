from facades.context import ApplicationContext
from facades.paint_effect_facade import PaintEffectFacade
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import FocusBehavior
from os.path import join
from ui.color_selector import ColorSelector
import logging

Context = ApplicationContext.get_instance()
Builder.load_file(join('apps', 'client', 'screens', 'live_effect_screen.kv'))


class LiveEffectScreen(FocusBehavior, Screen):
    def __init__(self, **kwargs):
        super(LiveEffectScreen, self).__init__(**kwargs)
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

    def send_current_frame(self, points):
        pass

    def update_ui(self):
        image = self.__effect.get_image()
        self.__effect_provider.set_image(image)
        self.__effect_provider.apply_image()


