import numpy as np
from .helpers import coordinate_mapper

"""
This function represents the 3d version from the simple 1d strip example and 
extends the value of the index from the 1d version across the y and z axis of that index.
"""
def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    leds_per_plane = num_leds ** 2

    # loop through all indexes in the 1d strip and map it to the 3d cube based on
    # our setup (snaked leds on each plane and snaked planes)
    for i in range(num_leds ** 3):
        (x, y, z) = coordinate_mapper.get_cube_xyz_from_1d_index(i, num_leds)

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue

        strip._led_data[i] = int(rgb[x])