from kivy.app import App
from led.networking.factories import ServerFactory
from led.ui.display_widget import DisplayWidget


class SimulatorWidget(DisplayWidget):
    def __init__(self, **kwargs):
        super(SimulatorWidget, self).__init__(**kwargs)
        self.server = ServerFactory.create_server(self, address="127.0.0.1", port=6666)

    def close(self):
        self.server.stop()
        self.server.join()


class LedDisplaySimulatorApp(App):
    def build(self):
        self.server = SimulatorWidget()
        return self.server

    def on_stop(self):
        self.server.close()

if __name__ == "__main__":
    LedDisplaySimulatorApp().run()

