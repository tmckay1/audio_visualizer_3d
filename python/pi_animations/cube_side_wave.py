import numpy as np

"""
This function represents the 3d version from the simple 1d strip example and 
extends the value of the index from the 1d version across the y and z axis of that index.
In this case, however, we only extend the wave to as high as the max value for that index
in the z plane
"""
def draw_points(strip, rgb, num_leds, p, prev_pixels, rgb_max):
    leds_per_plane = num_leds ** 2

    # loop through all indexes in the 1d strip and map it to the 3d cube based on
    # our setup (snaked leds on each plane and snaked planes)
    for i in range(num_leds ** 3):
        (x, y, z) = get_cube_xyz_from_1d_index(i, num_leds)

        # Ignore pixels if they haven't changed (saves bandwidth)
        # if np.array_equal(p[:, x], prev_pixels[:, x]):
        #     continue

        max_level = int((rgb[x] / rgb_max) * num_leds)
        should_draw = z <= max_level
        strip._led_data[i] = int(rgb[x]) if should_draw else 0

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