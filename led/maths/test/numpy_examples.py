import unittest
import numpy as np

from scipy.interpolate import interp1d


class TestNumpyExamples(unittest.TestCase):

    def test_color_interpolation(self):
        pixel_x_coordinates = np.array([0, 10])
        colors = np.array([[200, 100], [0, 10], [50, 50]])
        fun = interp1d(pixel_x_coordinates, colors)
        val = fun(5)

        self.assertEqual(val[0], 150)
        self.assertEqual(val[1], 5)
        self.assertEqual(val[2], 50)
