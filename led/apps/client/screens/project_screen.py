from kivy.uix.screenmanager import Screen
from client_facade.context import ApplicationContext
from kivy.lang import Builder
from os.path import join

Context = ApplicationContext.get_instance()
Builder.load_file(join('apps', 'client', 'screens', 'project_screen.kv'))


class ProjectScreen(Screen):
    def __init__(self, **kwargs):
        super(ProjectScreen, self).__init__(**kwargs)
        self._connection_provider = Context.get_connection_provider()
        self._effect_provider = Context.get_effect_provider()
        self._effect_provider.set_apply_effect_callback(self.apply_effect)
        self._display = Context.get_display()
        self._image = None
        self._screen_text_to_ids = {'Text Effect': 'text_effect_screen',
                                    'Rainbow Effect': 'rainbow_effect_screen',
                                    'Paint Effect': 'paint_effect_screen'}

    def apply_effect(self):
        self._image = self._effect_provider.get_image()
        self.update_ui()
        self.send_image(self._image)

    def send_image(self, image):
        if self._connection_provider.is_connected():
            client = self._connection_provider.get_client()
            client.send_image_frame(image)

    def update_ui(self):
        display_widget = self.ids.display_widget
        display_widget.set_size(self._display.get_size())
        display_widget.display_frame(self._image)

    def effect_changed(self):
        self.ids.effect_screen_manager.current = self._screen_text_to_ids[self.ids.select_effect_spinner.text]
