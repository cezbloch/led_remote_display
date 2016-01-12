import numpy


def interpolate_1d(known_coordinates, known_values, coordinates_to_interpolate):
    return numpy.interp(numpy.array(coordinates_to_interpolate),
                        numpy.array(known_coordinates),
                        numpy.array(known_values))


def transpose(matrix):
    return numpy.matrix.transpose(numpy.array(matrix))


def generate_range_points(start_point, end_point, number_of_points):
    return numpy.linspace(numpy.array(start_point), numpy.array(end_point), number_of_points)


def depth(array):
    return len(numpy.array(array).shape)
