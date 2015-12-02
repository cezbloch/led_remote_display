from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.lang import Builder

Builder.load_string("""
<ColorButton>
    font_size: root.height / 3
    background_normal: ''
    background_down: ''
""")

class ColorButton(ToggleButton):
    pass
