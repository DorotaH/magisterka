from math import pi, tan


def area_polygon(s, l):
	return (l**2) * s / (tan(pi / s) * 4)
