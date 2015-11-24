import jsocket


class LedServerThreaded(jsocket.ThreadedServer):
    def __init__(self, message_unpacker, **kwargs):
        jsocket.ThreadedServer.__init__(self, **kwargs)
        self.timeout = 2.0
        self.message_unpacker = message_unpacker

    def _process_message(self, json_object):
        self.message_unpacker.process_command(json_object)

    def close(self):
        self.stop()
        self.join()


class LedServerFactoryThreaded(jsocket.ServerFactoryThread):
    def __init__(self):
        super(LedServerFactoryThreaded, self).__init__()
        self.timeout = 2.0
        self.message_unpacker = None

    def _process_message(self, json_object):
        self.message_unpacker.process_command(json_object)
