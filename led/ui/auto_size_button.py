from kivy.uix.button import Button

from kivy.lang import Builder

Builder.load_string("""
<AutoTextSizeButton>
    font_size: root.height / 3
""")

class AutoTextSizeButton(Button):
    pass
