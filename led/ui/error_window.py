from kivy.lang import Builder
from kivy.uix.popup import Popup
import traceback

Builder.load_string("""
<ErrorWindow>:
    color: 1, 1, 1, 1
    title: 'Failure'
    content:content
    BoxLayout:
        id: content
        orientation: 'vertical'
        Label:
            id: label
            text_size: self.size
        BoxLayout:
            size_hint_y: None
            height: '27sp'
            Button:
                text: 'ok'
                on_release: root.dismiss()
""")


class ErrorWindow(Popup):
    def gather_traces(self, message):
        tb = traceback.format_exc()
        self.ids.label.text = tb + message

