from kivy.app import App
from ui.touch_widget import TouchWidget


class TouchtracerApp(App):
    title = 'Touchtracer'

    def build(self):
        return TouchWidget()

    def on_pause(self):
        return True

if __name__ == '__main__':
    TouchtracerApp().run()
