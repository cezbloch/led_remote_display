from kivy.uix.screenmanager import Screen
from PIL import ImageFont
from imaging.text_effect import TextEffect
from context import ApplicationContext
from kivy.lang import Builder
from os.path import join
import PIL

Context = ApplicationContext.get_instance()
Builder.load_file(join('screens', 'text_effect_screen.kv'))


class TextEffectScreen(Screen):
    def __init__(self, **kwargs):
        super(TextEffectScreen, self).__init__(**kwargs)
        self._effect_provider = Context.get_effect_provider()

    def draw_text(self):
        text_input = self.ids.text_input
        text = text_input.text
        font = ImageFont.truetype("arial.ttf", 14)
        display_size = Context.get_display().get_size()
        effect = TextEffect(display_size).with_font(font)
        image = effect.draw_text(text)
        image = image.crop((0, 0, display_size[0], display_size[1])).transpose(PIL.Image.FLIP_TOP_BOTTOM)
        self._effect_provider.set_image(image)
        self._effect_provider.apply_image()
