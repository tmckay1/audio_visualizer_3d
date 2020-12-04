"""
Given the 24 bit color, return the classic color that the visualizer should
show (think green/yellow/red)
"""
def get_classic_color(percent_of_max):
  normalized_value = percent_of_max * 100
  if normalized_value < 50:
    return 2 ** 6
  elif normalized_value < 80:
    return 2 ** 6
  else:
    return 2 ** 6