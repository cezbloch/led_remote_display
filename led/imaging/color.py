class Color(object):
    def __init__(self, r=0, g=0, b=0):
        self.rgb = [r, g, b]

    @staticmethod
    def from_float_array(rgb_float):
        return Color(int(rgb_float[0]), int(rgb_float[1]), int(rgb_float[2]))

    @staticmethod
    def from_int(rgb_int):
        r = chr((rgb_int >> 16))
        g = chr((rgb_int >> 8))
        b = chr(rgb_int & 0xFF)
        return Color(r, g, b)

    def get_as_int(self):
        return (self.rgb[0] << 16) | (self.rgb[1] << 8) | self.rgb[2]

    def build(self):
        return self.rgb

    def get_as_tuple(self):
        return self.rgb[0], self.rgb[1], self.rgb[2]

    @staticmethod
    def from_normalized_float(normalized_float):
        return Color(int(255*normalized_float[0]), int(255*normalized_float[1]), int(255*normalized_float[2]))
