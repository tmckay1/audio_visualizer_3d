import numpy as np
from .helpers import coordinate_mapper

"""
This function represents the 2d version from the simple 1d strip example and 
extends the value of the index from the 1d version across the y axis of that index.
"""
def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    for i in range(num_leds ** 2):
        (x, y) = coordinate_mapper.get_square_xy_from_1d_index(i, num_leds)

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue

        strip._led_data[i] = int(rgb[x])