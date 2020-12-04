import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for i in range(num_leds ** 3):
        leds_per_plane = num_leds ** 2
        current_led_in_plane = i % leds_per_plane
        z = i // leds_per_plane
        y = (current_led_in_plane // num_leds) # for even z
        odd_z = z % 2 == 1

        # if we are an odd z, the y is reversed
        if odd_z:
            y = (leds_per_plane - (current_led_in_plane + 1)) // num_leds
        
        x = i % num_leds # for even y, even z
        odd_y = (y % 2) == 1

        # if we are an odd y, the x is reversed
        if odd_y and not odd_z:
            x = num_leds - (current_led_in_plane % num_leds) - 1

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue
        
        rgb_max = 2 ** 22
        max_level = int((rgb[get_index_for_point(x, y, z)] / rgb_max) * num_leds)
        should_draw = get_index_for_point(x, y, z) <= max_level
        strip._led_data[i] = int(rgb[get_index_for_point(x, y, z)]) if should_draw else 0

def genCubeVector(x, y, z, x_mult=1, y_mult=1, z_mult=1):
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
        return int(max(abs(_x - cX), abs(_y - cY), abs(_z - cZ)))

    return [[[vect(_x, _y, _z) for _z in range(z)] for _y in range(y)] for _x in range(x)]

cube_mapping = genCubeVector(8, 8, 8)

def get_index_for_point(x, y, z):
    global cube_mapping
    return cube_mapping[x][y][z]