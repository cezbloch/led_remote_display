import numpy


def assert_arrays_equal(value, expected):
    numpy.testing.assert_array_equal(value.array, expected.array)
