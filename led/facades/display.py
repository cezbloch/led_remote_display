class Display(object):
    def __init__(self):
        self._width = 0
        self._height = 0

    def set_size(self, size):
        self._width, self._height = size

    def get_size(self):
        return self._width, self._height
