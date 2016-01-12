from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Point, GraphicException
from math import sqrt
from kivy.graphics import (Translate, Fbo, ClearColor, ClearBuffers, Scale)
from imaging.image_factory import ImageFactory
from ui.error_window import ErrorWindow


def calculate_points(x1, y1, x2, y2, steps=5):
    dx = x2 - x1
    dy = y2 - y1
    dist = sqrt(dx * dx + dy * dy)
    if dist < steps:
        return None
    o = []
    m = dist / steps
    for i in range(1, int(m)):
        mi = i / m
        lastx = x1 + dx * mi
        lasty = y1 + dy * mi
        o.extend([lastx, lasty])
    return o


class TouchWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(TouchWidget, self).__init__(**kwargs)
        self.__point_size = 20
        self.__brush_color = [0, 0, 0, 0]

    def on_touch_down(self, touch):
        try:
            if not self.is_touch_within_widget_boarders(touch.pos):
                return False

            ud = touch.ud
            ud['group'] = g = str(touch.uid)
            pointsize = self.__point_size
            if 'pressure' in touch.profile:
                ud['pressure'] = touch.pressure
                pointsize = (touch.pressure * 100000) ** 2

            with self.canvas:
                Color(rgba=self.__brush_color)
                ud['lines'] = [Point(points=(touch.x, touch.y), pointsize=pointsize, group=g)]

            touch.grab(self)
            return True
        except Exception as ex:
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            popup.open()

    def on_touch_move(self, touch):
        try:
            if touch.grab_current is not self:
                return
            if not self.is_touch_within_widget_boarders(touch.pos):
                return

            ud = touch.ud
            index = -1

            while True:
                try:
                    points = ud['lines'][index].points
                    oldx, oldy = points[-2], points[-1]
                    break
                except:
                    index -= 1

            points = calculate_points(oldx, oldy, touch.x, touch.y)

            # if pressure changed create a new point instruction
            if 'pressure' in ud:
                if not .95 < (touch.pressure / ud['pressure']) < 1.05:
                    g = ud['group']
                    pointsize = (touch.pressure * 100000) ** 2
                    with self.canvas:
                        Color(rgba=self.__brush_color)
                        ud['lines'].append(Point(points=(),pointsize=pointsize, group=g))

            if points:
                try:
                    lp = ud['lines'][-1].add_point
                    for idx in range(0, len(points), 2):
                        lp(points[idx], points[idx + 1])
                except GraphicException:
                    pass

            import time
            t = int(time.time())
            if t not in ud:
                ud[t] = 1
            else:
                ud[t] += 1
        except Exception as ex:
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            popup.open()

    def on_touch_up(self, touch):
        try:
            if touch.grab_current is not self:
                return
            if not self.is_touch_within_widget_boarders(touch.pos):
                return

            touch.ungrab(self)
        except Exception as ex:
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            popup.open()

    def set_point_size(self, point_size):
        self.__point_size = point_size

    def set_brush_color(self, color):
        self.__brush_color = color

    def is_touch_within_widget_boarders(self, touch_position):
        x, y = touch_position
        min_x = self.__point_size
        min_y = self.__point_size
        max_x = self.width - self.__point_size
        max_y = self.height - self.__point_size
        is_within_widget_width = min_x <= x < max_x
        is_within_widget_height = min_y <= y < max_y

        if is_within_widget_height and is_within_widget_width:
            return True
        else:
            return False

    def clear_canvas(self):
        self.canvas.clear()

    def capture_image(self):
        try:
            if self.parent is not None:
                canvas_parent_index = self.parent.canvas.indexof(self.canvas)
                self.parent.canvas.remove(self.canvas)

            fbo = Fbo(size=self.size, with_stencilbuffer=True)

            with fbo:
                ClearColor(0, 0, 0, 1)
                ClearBuffers()
                Scale(1, -1, 1)
                Translate(-self.x, -self.y - self.height, 0)

            fbo.add(self.canvas)
            fbo.draw()
            # copy texture here
            texture = fbo.texture
            fbo.remove(self.canvas)

            if self.parent is not None:
                self.parent.canvas.insert(canvas_parent_index, self.canvas)

            pixels = texture.pixels
            size = (int(self.size[0]), int(self.size[1]))
            image = ImageFactory.create_image_from_string('RGBA', size, pixels)

            return image
        except Exception as ex:
            popup = ErrorWindow()
            popup.gather_traces(ex.message)
            popup.open()


