import math


def sum_gp(a, n, r):
	return ((1 - math.pow(r, n)) * a) / (1 - r)
