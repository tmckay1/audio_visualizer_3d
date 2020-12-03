import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for i in range(num_leds):
        # Ignore pixels if they haven't changed (saves bandwidth)
        if np.array_equal(p[:, i], prev_pixels[:, i]):
            continue
        plot_point(strip, rbg, i)

def plot_point(strip, rgb, i):
    strip._led_data[i] = int(rgb[i])