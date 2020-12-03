import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for i in range(num_leds ** 2):
        remainder = (i % num_leds)
        x = remainder
        y = i // num_leds
        odd_y = (y % 2) == 1
        if odd_y:
            # we're snaked so the index of the rbg array is not exactly the mod of the current led position
            x = num_leds - remainder - 1

        # Ignore pixels if they haven't changed (saves bandwidth)
        if np.array_equal(p[:, x], prev_pixels[:, x]):
            continue
        rgb_max = 2 ** 22
        max_level = int((rgb[x] / rgb_max) * num_leds)
        should_draw = max_level == y
        strip._led_data[i] = int(rgb[x]) if should_draw else 0