from numpy_wrapper import transpose, interpolate_1d, depth


def interpolate(known_coordinates, known_values, coordinates_to_interpolate):
    array_depth = depth(known_values)
    if array_depth == 1:
        return interpolate_1d(known_coordinates, known_values, coordinates_to_interpolate)
    else:
        known_values_transposed = transpose(known_values)
        val = [transpose(interpolate(known_coordinates,
                         values_one_dimension,
                         coordinates_to_interpolate))
               for values_one_dimension in known_values_transposed]

        return transpose(val)
