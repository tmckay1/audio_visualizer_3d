import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for i in range(num_leds ** 2):
        # Ignore pixels if they haven't changed (saves bandwidth)
        if np.array_equal(p[:, i], prev_pixels[:, i]):
            continue
        #strip._led_data[i] = rgb[i]
        strip._led_data[i] = int(rgb[i])