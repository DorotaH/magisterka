from math import pi, tan


def area_polygon(s,l):
  return s * (l ** 2) / (4 * tan(pi / s))