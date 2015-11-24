import numpy
from scipy.interpolate import interp1d
from containers import Array

class Math(object):
    @staticmethod
    def Interpolate(known_coordinates, known_values, coordinates_to_interpolate):
        known_values_transposed = numpy.matrix.transpose(known_values.array)
        f = interp1d(known_coordinates.array, known_values_transposed)
        interpolated_values = numpy.matrix.transpose(f(coordinates_to_interpolate.array[:]))
        return Array(interpolated_values)

    @staticmethod
    def generate_range_points(start_point, end_point, number_of_points):
        return Array(numpy.linspace(start_point, end_point, number_of_points))
