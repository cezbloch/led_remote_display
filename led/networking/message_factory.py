import json

from defines import *
from binary_encoder import *

def create_command_dictionary():
    data = dict()
    data[COMMAND] = dict()
    return data

def create_concrete_command(data, concrete_command):
    command = data[COMMAND]
    command[concrete_command] = dict()
    return command[concrete_command]


class MessageFactory(object):
    @staticmethod
    def dump_json(data):
        return json.dumps(data)

    @staticmethod
    def create_set_size_message(size):
        (width, height) = size
        data = create_command_dictionary()
        concrete_command = create_concrete_command(data, COMMAND_SET_SIZE)
        concrete_command[WIDTH] = width
        concrete_command[HEIGHT] = height
        return MessageFactory.dump_json(data)

    @staticmethod
    def create_display_frame_message(image):
        data = create_command_dictionary()
        concrete_command = create_concrete_command(data, COMMAND_DISPLAY_FRAME)
        concrete_command[PIXELS] = BinaryEncoder.encode_bytes(image.tostring())
        concrete_command[SIZE] = image.size
        concrete_command[MODE] = image.mode
        return MessageFactory.dump_json(data)
