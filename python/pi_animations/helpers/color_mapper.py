"""
Given the 24 bit color, return the classic color that the visualizer should
show (think green/yellow/red)
"""
def get_classic_color(percent_of_max):
  normalized_value = percent_of_max * 100
  if normalized_value < 50:
    return 2 ** 14
  elif normalized_value < 75:
    return 16776960
  else:
    return 2 ** 21