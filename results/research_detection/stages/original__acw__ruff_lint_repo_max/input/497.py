import math


def surfacearea_cone(r,h):
  l = math.sqrt(r * r + h * h)
  return math.pi * r * (r + l)