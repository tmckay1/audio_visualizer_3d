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

        rgb_max = 2 ** 22
        max_level = int((rgb[x] / rgb_max) * num_leds)
        should_draw = max_level == z
        strip._led_data[i] = int(rgb[x]) if should_draw else 0