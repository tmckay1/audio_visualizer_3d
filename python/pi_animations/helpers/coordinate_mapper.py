import math

def get_cube_xyz_from_1d_index(i, num_leds):
    leds_per_plane = num_leds ** 2

    current_led_in_plane = i % leds_per_plane
    z = i // leds_per_plane
    y = (current_led_in_plane // num_leds) # for even z
    odd_z = z % 2 == 1

    # if we are an odd z, the y is reversed since we are snaked
    if odd_z:
        y = (leds_per_plane - (current_led_in_plane + 1)) // num_leds
    
    x = i % num_leds # for even y, even z
    odd_y = (y % 2) == 1

    # if we are an odd y and even z, the x is reversed. If y and z were
    # both odd, then the reflection would cancel it out and x will
    # be as if it is even y, even z
    if (odd_y and not odd_z) or (odd_z and not odd_y):
        x = num_leds - (current_led_in_plane % num_leds) - 1

    return (x, y, z)

def get_square_xy_from_1d_index(i, num_leds):
    x = i % num_leds # for even y since we are in a snaking pattern
    y = i // num_leds
    
    # check if y is odd, in which case the x needs to change
    if y % 2 == 1:
        # we're snaked so the index of the rbg array is not exactly the mod of the current led position
        # instead it's the reflection of this point across the center of the number of leds
        x = num_leds - x - 1

    return (x, y)


def gen_half_sphere_vector(x, y, z, x_mult=1, y_mult=1, z_mult=1):
    """Generates a map of vector lengths from the center point to each coordinate
    x - width of matrix to generate
    y - height of matrix to generate
    z - depth of matrix to generate
    x_mult - value to scale x-axis by
    y_mult - value to scale y-axis by
    z_mult - value to scale z-axis by
    """
    cX = (x - 1) / 2.0
    cY = (y - 1) / 2.0
    cZ = 0

    num_leds = z

    def vect(_x, _y, _z):
        return min(int(math.sqrt(math.pow(_x - cX, 2 * x_mult) +
                             math.pow(_y - cY, 2 * y_mult) +
                             math.pow(_z - cZ, 2 * z_mult))), num_leds - 1)

    return [[[vect(_x, _y, _z) for _z in range(z)] for _y in range(y)] for _x in range(x)]

def gen_center_sphere_vector(x, y, z, x_mult=1, y_mult=1, z_mult=1):
    """Generates a map of vector lengths from the center point to each coordinate
    x - width of matrix to generate
    y - height of matrix to generate
    z - depth of matrix to generate
    x_mult - value to scale x-axis by
    y_mult - value to scale y-axis by
    z_mult - value to scale z-axis by
    """
    cX = (x - 1) / 2.0
    cY = (y - 1) / 2.0
    cZ = (z - 1) / 2.0

    def vect(_x, _y, _z):
        return int(math.sqrt(math.pow(_x - cX, 2 * x_mult) +
                             math.pow(_y - cY, 2 * y_mult) +
                             math.pow(_z - cZ, 2 * z_mult)))

    return [[[vect(_x, _y, _z) for _z in range(z)] for _y in range(y)] for _x in range(x)]