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