from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton

Builder.load_string("""
<ColorButton>
    font_size: root.height / 3
    background_normal: ''
    background_down: ''
""")


class ColorButton(ToggleButton):
    pass
