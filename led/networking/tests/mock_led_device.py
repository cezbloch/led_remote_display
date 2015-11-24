class MockLedDevice(object):
    def __init__(self):
        self.image = None
        self.size = None

    def display_frame(self, image):
        self.image = image

    def set_size(self, size):
        self.size = size
