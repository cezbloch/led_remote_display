from maths.interpolation import Math
import unittest
import numpy as np
from maths.containers import Array
from maths.testing import assert_arrays_equal

class TestInterpolation(unittest.TestCase):
    def test_1D_interpolation_integer(self):
        x_boarder_coords = Array([0, 10])
        y_boarder_coords = Array([10, 30])
        x_values_to_interpolate = Array([0, 5, 10])

        y_values_interpolated = Math.Interpolate(x_boarder_coords, y_boarder_coords, x_values_to_interpolate)

        assert_arrays_equal(y_values_interpolated, Array([10, 20, 30]))

    def test_1D_interpolation_float(self):
        x_boarder_coords = Array([0, 2])
        y_boarder_coords = Array([2, 3])
        x_values_to_interpolate = Array([0.1, 0.5, 1.5])

        y_values_interpolated = Math.Interpolate(x_boarder_coords, y_boarder_coords, x_values_to_interpolate)

        assert_arrays_equal(y_values_interpolated, Array([2.05, 2.25, 2.75]))

    def test_3D_vector_interpolation(self):
        known_coordinates = Array([0, 10])
        known_values = Array([[200, 0, 50], [100, 10, 50]])
        coordinates_to_interpolate = Array([5])

        interpolated_values = Math.Interpolate(known_coordinates, known_values, coordinates_to_interpolate)

        expected_interpolated_values = Array([[150., 5., 50.]])
        assert_arrays_equal(interpolated_values, expected_interpolated_values)
