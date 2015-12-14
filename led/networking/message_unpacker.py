import logging
import json

from defines import *
from imaging.image_factory import ImageFactory
from binary_encoder import *


class MessageUnpacker(object):
    def __init__(self, server_handler, logger=logging.getLogger("jsocket.example_servers")):
        self._server = server_handler
        self._logger = logger

    def process_command(self, object):
        json_object = json.loads(object)
        if json_object != '':
            command = json_object[COMMAND]
            if self.isCommand(command, COMMAND_SET_SIZE):
                size = self.unpack_set_size_command(command)
                self._logger.info("Setting size on device: " + str(size))
                self._server.set_size(size)
            elif self.isCommand(command, COMMAND_DISPLAY_FRAME):
                image = self.unpack_display_frame_command(command)
                #self._logger.info("Displaying image with size: " + str(image.size))
                self._server.display_frame(image)
            else:
                self._logger.error("Unknown command - dumping json: " + object)
        else:
            self._logger.error("Empty json object!")

    @staticmethod
    def isCommand(command, command_name):
        return command_name in command

    @staticmethod
    def unpack_set_size_command(command):
        concrete_command = command[COMMAND_SET_SIZE]
        width = concrete_command[WIDTH]
        height = concrete_command[HEIGHT]
        return width, height

    @staticmethod
    def unpack_display_frame_command(command):
        concrete_command = command[COMMAND_DISPLAY_FRAME]
        size = concrete_command[SIZE]
        mode = concrete_command[MODE]
        data = BinaryEncoder.decode_bytes(concrete_command[PIXELS])
        image = ImageFactory.create_image_from_string(mode, size, data)
        return image
