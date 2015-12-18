import unittest
import numpy as np
from scipy import interpolate


class TestNumpyExamples(unittest.TestCase):

    def test_color_interpolation(self):
        pixel_x_coordinates = np.array([0, 10])
        colors = np.array([[200, 100], [0, 10], [50, 50]])
        fun = interpolate.interp1d(pixel_x_coordinates, colors)
        val = fun(5)

        self.assertEqual(val[0], 150)
        self.assertEqual(val[1], 5)
        self.assertEqual(val[2], 50)

    def test_value_interpolation_in_2D(self):
        pixel_x_coordinates = np.array([0, 0, 30, 30])
        pixel_y_coordinates = np.array([0, 10, 0, 10])
        values = np.array([[0, 100, 0, 100]])
        fun = interpolate.interp2d(pixel_x_coordinates, pixel_y_coordinates, values)
        val = fun(15, 5)

        self.assertEqual(val[0], 50)

    def test_vector_interpolation_in_2D_fails(self):
        pixel_x_coordinates = np.array([0, 0, 30, 30])
        pixel_y_coordinates = np.array([0, 10, 0, 10])
        #values = np.array([[255, 0, 0, 255], [0, 255, 0, 255], [0, 0, 255, 255]])
        values = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]])
        fun = interpolate.interp2d(pixel_x_coordinates, pixel_y_coordinates, values)
        val = fun(15, 5)

        self.assertEqual(val[0], 50)

    def scipy_2d_interpolation_example(self):
        # http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.interpolate.interp2d.html
        from scipy import interpolate
        import matplotlib.pyplot as plt
        x = np.arange(-5.01, 5.01, 0.25)
        y = np.arange(-5.01, 5.01, 0.25)
        xx, yy = np.meshgrid(x, y)
        z = np.sin(xx**2+yy**2)
        f = interpolate.interp2d(x, y, z, kind='cubic')

        xnew = np.arange(-5.01, 5.01, 1e-2)
        ynew = np.arange(-5.01, 5.01, 1e-2)
        znew = f(xnew, ynew)
        plt.plot(x, z[0, :], 'ro-', xnew, znew[0, :], 'b-')
        plt.show()

    def func(self, x, y):
        return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

    def test_griddata(self):
        grid_x, grid_y = np.mgrid[0:29:30j, 0:9:10j]
        #points = np.random.rand(3, 2)
        points = np.array([[0, 0], [29, 9]])
        values = self.func(points[:,0], points[:,1])
        values = np.array([1, 2])
        from scipy.interpolate import griddata
        grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
        grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
        grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')