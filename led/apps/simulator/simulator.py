from kivy.support import install_twisted_reactor
install_twisted_reactor()

from kivy.app import App
from led.ui.display_widget import DisplayWidget
from networking.twisted_server import LedServer
from twisted.internet import reactor


class SimulatorWidget(DisplayWidget):
    def __init__(self, **kwargs):
        super(SimulatorWidget, self).__init__(**kwargs)
        self.server = LedServer(self)
        self.server.start(6666)

    def close(self):
        self.server.close()


class LedDisplaySimulatorApp(App):
    server = None

    def build(self):
        self.server = SimulatorWidget()
        return self.server

    def on_stop(self):
        self.server.close()

if __name__ == "__main__":
    LedDisplaySimulatorApp().run()

