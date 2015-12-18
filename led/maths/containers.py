import numpy


class Array(object):
    def __init__(self, array):
        self.array = numpy.array(array)

    def __getitem__(self, index):
        return self.array[index]

    def __add__(self, other):
        return Array(self.array + other.array)

    def __sub__(self, other):
        return Array(self.array - other.array)

    def get(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            AttributeError()
