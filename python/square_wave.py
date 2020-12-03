import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for i in range(num_leds ** 2):
        odd_row = ((i // num_leds) % 2) == 1
        remainder = (i % num_leds)
        index = remainder
        if odd_row:
            # we're snaked so the index of the rbg array is not exactly the mod of the current led position
            index = num_leds - remainder - 1
        # Ignore pixels if they haven't changed (saves bandwidth)
        if np.array_equal(p[:, index], prev_pixels[:, index]):
            continue
        strip._led_data[i] = int(rgb[index])