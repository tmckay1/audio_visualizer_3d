import numpy as np
from .helpers import coordinate_mapper

"""
Instead of drawing the entire 2d plane, only draw out the wave which is the 
"""
def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    for i in range(num_leds ** 2):
        (x, y) = coordinate_mapper.get_square_xy_from_1d_index(i, num_leds)

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue

        max_level = int((rgb[x] / rgb_max) * num_leds) # the maximum level this wave form should reach for the given x
        should_draw = y <= max_level # only draw the pixel if it is at or below the maximum level, so we see a wave
        strip._led_data[i] = int(rgb[x]) if should_draw else 0