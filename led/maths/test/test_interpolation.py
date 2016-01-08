from maths.interpolation import interpolate
import unittest
from maths.testing import assert_arrays_equal


class TestInterpolation(unittest.TestCase):
    def test_1D_interpolation_integer(self):
        x_boarder_coords = [0, 10]
        y_boarder_coords = [10, 30]
        x_values_to_interpolate = [0, 5, 10]

        y_values_interpolated = interpolate(x_boarder_coords, y_boarder_coords, x_values_to_interpolate)

        assert_arrays_equal(y_values_interpolated, [10, 20, 30])

    def test_1D_interpolation_float(self):
        x_boarder_coords = [0, 2]
        y_boarder_coords = [2, 3]
        x_values_to_interpolate = [0.1, 0.5, 1.5]

        y_values_interpolated = interpolate(x_boarder_coords, y_boarder_coords, x_values_to_interpolate)

        assert_arrays_equal(y_values_interpolated, [2.05, 2.25, 2.75])

    def test_3D_vector_interpolation(self):
        known_coordinates = [0, 10]
        known_values = [[200, 0, 50], [100, 10, 50]]
        coordinates_to_interpolate = [5]

        interpolated_values = interpolate(known_coordinates, known_values, coordinates_to_interpolate)

        expected_interpolated_values = [[150., 5., 50.]]
        assert_arrays_equal(interpolated_values, expected_interpolated_values)

    def test_multiple_vector_interpolation(self):
        known_coordinates = [0, 2000]
        color_1_start = [1, 2, 3]
        color_2_start = [10, 20, 30]
        color_1_end = [3, 8, 9]
        color_2_end = [30, 80, 90]
        color_1_known_values = [color_1_start, color_1_end]
        color_2_known_values = [color_2_start, color_2_end]

        known_values = [color_1_known_values, color_2_known_values]
        coordinates_to_interpolate = [1000]

        interpolated_values = interpolate(known_coordinates, known_values, coordinates_to_interpolate)

        expected_color_1_values = [2., 5., 6.]
        expected_color_2_values = [20., 50., 60.]
        expected_interpolated_values = [[expected_color_1_values, expected_color_2_values]]
        assert_arrays_equal(interpolated_values, expected_interpolated_values)
