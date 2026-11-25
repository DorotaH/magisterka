import math
import sys

a, b, c, d = map(int, input().split())


def distance(x, y):
	return abs(x - y)


def min_time(a, b, c, d):
	if a >= b and a >= c:
		return math.ceil(max(0, max(b - a - d, c - a - d)))
	elif a <= b and b >= c:
		return math.ceil(max(0, max(a - b - d, c - b - d)))
	else:
		return math.ceil(max(0, max(a - c - d, b - c - d)))


print(min_time(a, b, c, d))
