import numpy as np
from .helpers import coordinate_mapper

def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    leds_per_plane = num_leds ** 2
    cube_mapping = coordinate_mapper.gen_center_sphere_vector(num_leds, num_leds, num_leds)

    # loop through all indexes in the 1d strip and map it to the 3d cube based on
    # our setup (snaked leds on each plane and snaked planes)
    for i in range(num_leds ** 3):
        (x, y, z) = coordinate_mapper.get_cube_xyz_from_1d_index(i, num_leds)

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue

        rgb_index = cube_mapping[x][y][z] # this is the radius away from the center of the sphere
        max_level = int((rgb[rgb_index] / rgb_max) * num_leds) # the maximum level this wave form should reach for the given index
        should_draw = rgb_index <= max_level # only draw the pixel if it is at or below the maximum level, so we see a wave
        strip._led_data[i] = int(rgb[rgb_index]) if should_draw else 0

