from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.clock import Clock

#import PIL
#from context import ApplicationContext

#Context = ApplicationContext.get_instance()


#must be before .kv files imports
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '800')

#.kv file requirements
from screens.text_effect_screen import TextEffectScreen
from screens.rainbow_effect_screen import RainbowEffectScreen
from screens.connect_display_screen import ConnectDisplayScreen
from screens.file_chooser_screen import FileChooserScreen
from screens.project_screen import ProjectScreen
#from ui.display_widget import DisplayWidget
#from kivy.uix.image import Image
#from kivy.uix.slider import Slider


class AutoTextSizeButton(Button):
    pass


class ColorButton(ToggleButton):
    pass


class EffectScreenManager(ScreenManager):
    pass


class MainScreen(Screen):
    pass


class LedScreenManager(ScreenManager):
    pass


class LedApp(App):
    def build(self):
        return LedScreenManager()

if __name__ == '__main__':
    LedApp().run()
