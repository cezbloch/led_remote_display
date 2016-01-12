from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string("""
<ColorSelector>:
    color: 1, 1, 1, 1
    title: 'Color Selector'
    content:content
    BoxLayout:
        id: content
        orientation: 'vertical'
        ColorPicker:
            id: clr_picker
            color: root.color
        BoxLayout:
            size_hint_y: None
            height: '27sp'
            Button:
                text: 'ok'
                on_release:
                    root.color = clr_picker.color
                    root.dismiss()
            Button:
                text: 'cancel'
                on_release: root.dismiss()
""")


class ColorSelector(Popup):
    pass

