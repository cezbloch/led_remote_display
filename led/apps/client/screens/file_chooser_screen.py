from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from client_facade.context import ApplicationContext
from kivy.lang import Builder
from os.path import join
from os import getcwd

Builder.load_file(join('screens', 'file_chooser_screen.kv'))


class FileChooserScreen(Screen):
    chosen_image_path = StringProperty("")

    def get_empty_photo_path(self):
        current_directory = getcwd()
        return join(current_directory, 'resources', 'empty_photo.png')

    def update_image_path(self):
        selected_files = self.ids['file_chooser_icon_view'].selection
        image = self.ids['preview_image']
        image.source = self.get_empty_photo_path()
        if selected_files and selected_files[0]:
            self.chosen_image_path = selected_files[0]
        else:
            self.chosen_image_path = self.ids['file_chooser_icon_view'].path
