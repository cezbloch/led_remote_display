import numpy

class Array(object):
    def __init__(self, array):
        self.array = numpy.array(array)

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            AttributeError()