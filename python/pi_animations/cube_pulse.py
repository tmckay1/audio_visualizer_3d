import numpy as np
from .helpers import coordinate_mapper
from .helpers import color_mapper

"""
This function represents a pulsing cube in the center of the led cube that has half the width map to a
frequency of the data, so the cube simulates pulsing in and out.
"""
def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    leds_per_plane = num_leds ** 2
    cube_mapping = coordinate_mapper.gen_cube_vector(num_leds, num_leds, num_leds)

    # loop through all indexes in the 1d strip and map it to the 3d cube based on
    # our setup (snaked leds on each plane and snaked planes)
    for i in range(num_leds ** 3):
        (x, y, z) = coordinate_mapper.get_cube_xyz_from_1d_index(i, num_leds)

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue
        
        rgb_index = cube_mapping[x][y][z] # this is how far the top of the cube is from the center
        percent_of_max = rgb[rgb_index] / rgb_max
        max_level = int(percent_of_max * num_leds) # the maximum level this wave form should reach for the given index
        should_draw = rgb_index <= max_level # only draw the pixel if it is at or below the maximum level, so we see a wave
        strip._led_data[i] = int(color_mapper.get_classic_color(percent_of_max)) if should_draw else 0