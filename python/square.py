import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for i in range(num_leds ** 2):
        y = (i // num_leds)
        x = i % num_leds
        odd_row = (y % 2) == 1
        if odd_row:
            # we're snaked so the index of the rbg array is not exactly the mod of the current led position
            x = num_leds - (i % num_leds) - 1
            
        # Ignore pixels if they haven't changed (saves bandwidth)
        if np.array_equal(p[:, x], prev_pixels[:, x]):
            continue
        strip._led_data[i] = int(rgb[x])