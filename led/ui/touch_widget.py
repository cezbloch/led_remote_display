from kivy.uix.floatlayout import FloatLayout
import logging


class TouchWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(TouchWidget, self).__init__(**kwargs)
        self.__logger = logging.getLogger()
        self.__points = []
        self.move_callback = None

    def clear(self):
        self.__points = []

    def on_touch_down(self, touch):
        if not self.is_touch_within_widget_boarders(touch.pos):
            return False

        touch.grab(self)

        # add two points to make first one-point line
        self.__points.append((touch.x, touch.y))
        self.__points.append((touch.x, touch.y))
        if self.move_callback is not None:
            self.move_callback(self.__points)

        return True

    def on_touch_move(self, touch):
        if touch.grab_current is not self:
            return
        if not self.is_touch_within_widget_boarders(touch.pos):
            return

        self.__points.append((touch.x, touch.y))
        self.move_callback(self.__points)

    def on_touch_up(self, touch):
        if touch.grab_current is not self:
            return
        if not self.is_touch_within_widget_boarders(touch.pos):
            return

        touch.ungrab(self)
        self.clear()

    def is_touch_within_widget_boarders(self, touch_position):
        x, y = touch_position
        is_within_widget_width = 0 <= x < self.width
        is_within_widget_height = 0 <= y < self.height

        if is_within_widget_height and is_within_widget_width:
            return True
        else:
            return False
