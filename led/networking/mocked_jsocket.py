class LedServerThreaded(object):
    def __init__(self, unpacker, **kwargs):
        pass

    def _process_message(self, json_object):
        pass

    def close(self):
        pass

    def _set_timeout(self, time):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def join(self):
        pass


class JsonClient(object):
    def __init__(self, **kwargs):
        pass

    def connect(self):
        return True

    def send_obj(self, json_object):
        pass

    def close(self):
        pass
