class Color(object):
    def __init__(self, r=0, g=0, b=0):
        self.rgb = [r, g, b]

    @staticmethod
    def from_float(rgb_float):
        return Color(int(rgb_float[0]), int(rgb_float[1]), int(rgb_float[2]))

    def build(self):
        return self.rgb

    def get_as_tuple(self):
        return self.rgb[0], self.rgb[1], self.rgb[2]

    @staticmethod
    def from_normalized_float(normalized_float):
        return Color(int(255*normalized_float[0]), int(255*normalized_float[1]), int(255*normalized_float[2]))
