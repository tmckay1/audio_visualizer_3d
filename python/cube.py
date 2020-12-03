import numpy as np

def draw_points(strip, rgb, num_leds, p, prev_pixels):
    for x in range(num_leds):
      for i in range(num_leds):
        for j in range(num_leds):
          odd_row = ((i // num_leds) % 2) == 1
          if odd_row:
              # we're snaked so the index of the rbg array is not exactly the mod of the current led position
              index = num_leds - (i % num_leds) - 1
          else:
              index = i % num_leds
          # Ignore pixels if they haven't changed (saves bandwidth)
          if np.array_equal(p[:, index], prev_pixels[:, index]):
              continue
          strip._led_data[i] = int(rgb[index])